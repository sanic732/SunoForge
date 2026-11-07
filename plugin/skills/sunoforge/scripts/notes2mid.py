#!/usr/bin/env python3
"""notes2mid.py - SunoForge `15q notes`: a notes string (or a JSON note list) -> a type-1 .mid, and a check of any .mid.

Standard library only, Python 3.8+. LAB (experimental). Spends nothing: no network, no Suno call.

NOTES FORMAT (space-separated tokens):
    [15q notes] [bpm=96] [key=Am] [ts=4/4] [prog=0[,33]] [vel=90]  NOTE:BEATS[:VEL] ...  [| bass voice ...]
  NOTE  = C4, F#3, Bb4 (C4 = MIDI 60, octaves -1..9) or a MIDI number 0-127, or R for a rest
  BEATS = quarter-note beats as a decimal (1, 0.5, 1.5) or a fraction (1/2); VEL 1-127 (default 90 or vel=)
  " | "  starts a second voice (the bass line: its own track, channel 2); prog= inside a voice sets that voice's
         GM program (0-127); prog=a,b in the header sets both. No prog= -> no program change is written.
  Example: bpm=96 key=Am E4:1 A4:1 C5:1.5 B4:0.5 A4:1 G4:1 E4:2 | A2:4 E2:4

JSON input: [{"note":"E4","beats":1,"vel":90}, ...] or [["E4",1], ...] or
            {"bpm":96,"key":"Am","ts":"4/4","prog":[0,33],"notes":[...],"bass":[...]}  ("note": null or "R" = rest)

USAGE
    notes2mid.py "bpm=96 key=Am E4:1 A4:1 C5:1.5" -o melody.mid    write the .mid, print one JSON summary line
    notes2mid.py "bpm=96 E4:1 A4:1"                                 no -o: summary only (key check), nothing written
    notes2mid.py --json notes.json -o melody.mid                     JSON note list ('-' = stdin)
    notes2mid.py --check song.mid                                    read any .mid back, print the same summary
  The summary: bytes, bars, notes, range, duration_s, key_detected (Krumhansl-Schmuckler, Krumhansl-Kessler profiles,
  duration-weighted, best of 24 keys) with key_r, key_given, key_match ("same" | "close" = relative major/minor |
  "no" | null when no key was given), bpm. Suno's MIDI upload takes a .mid of at most 256 KB with notes in it.
EXIT: 0 ok; 2 refused (no notes, over 256 KB, pitch outside 0-127, a malformed token, not a MIDI file) - the JSON
  line then has "ok": false and "error", and the same message goes to stderr.
"""
import json
import math
import os
import re
import struct
import sys

MAX_BYTES = 256 * 1024
PPQ = 480
NAMES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
MAJ_NAMES = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
MIN_NAMES = ['Cm', 'C#m', 'Dm', 'Ebm', 'Em', 'Fm', 'F#m', 'Gm', 'G#m', 'Am', 'Bbm', 'Bm']
# Krumhansl & Kessler (1982) probe-tone profiles
KK_MAJOR = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
KK_MINOR = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]
PC = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
SF_MAJOR = {0: 0, 7: 1, 2: 2, 9: 3, 4: 4, 11: 5, 6: 6, 1: -5, 8: -4, 3: -3, 10: -2, 5: -1}


class Refuse(Exception):
    pass


# ---------------------------------------------------------------- names, keys
def note_name(m):
    return NAMES[m % 12] + str(m // 12 - 1)


def parse_pitch(s):
    """'C4' -> 60, 'F#3', 'Bb4', 'E-1', or a bare MIDI number. Returns None for a rest."""
    if s in ('R', 'r', 'rest', '-'):
        return None
    if re.fullmatch(r'\d{1,3}', s):
        m = int(s)
    else:
        mt = re.fullmatch(r'([A-Ga-g])([#b♯♭]{0,2})(-?\d{1,2})', s)
        if not mt:
            raise Refuse("malformed note %r (expected C4, F#3, Bb4, a MIDI number or R)" % s)
        acc = mt.group(2)
        m = (int(mt.group(3)) + 1) * 12 + PC[mt.group(1).upper()] + acc.count('#') + acc.count('♯') \
            - acc.count('b') - acc.count('♭')
    if not 0 <= m <= 127:
        raise Refuse("pitch %r is MIDI %d, outside 0-127" % (s, m))
    return m


def parse_key(s):
    """'Am' / 'A minor' / 'C#m' / 'Bb' / 'F major' -> (pc, 'major'|'minor')."""
    if s is None:
        return None
    t = str(s).strip().replace('♯', '#').replace('♭', 'b').replace('_', ' ').replace('-', ' ')
    mt = re.fullmatch(r'([A-Ga-g])([#b]?)\s*(m|min|minor|moll|maj|major|dur|M)?', t, re.I)
    if not mt:
        raise Refuse("malformed key %r (expected Am, C, F#m, Bb major)" % s)
    pc = (PC[mt.group(1).upper()] + (1 if mt.group(2) == '#' else -1 if mt.group(2) == 'b' else 0)) % 12
    q = mt.group(3) or ''
    minor = q == 'm' or q.lower() in ('min', 'minor', 'moll')
    return pc, 'minor' if minor else 'major'


def key_label(k):
    if k is None:
        return None
    return (MIN_NAMES if k[1] == 'minor' else MAJ_NAMES)[k[0]]


def _corr(a, b):
    ma, mb = sum(a) / 12.0, sum(b) / 12.0
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    da = math.sqrt(sum((x - ma) ** 2 for x in a))
    db = math.sqrt(sum((y - mb) ** 2 for y in b))
    return num / (da * db) if da and db else 0.0


def detect_key(weighted):
    """weighted: iterable of (midi_pitch, duration). Krumhansl-Schmuckler, best of 24 keys.
    Returns (best_key, r, runner_up_key, r2) or None when there is nothing to weigh."""
    hist = [0.0] * 12
    for m, d in weighted:
        hist[m % 12] += max(d, 0.0)
    if sum(hist) <= 0:
        return None
    scores = []
    for tonic in range(12):
        for mode, prof in (('major', KK_MAJOR), ('minor', KK_MINOR)):
            rot = [prof[(i - tonic) % 12] for i in range(12)]
            scores.append((_corr(hist, rot), (tonic, mode)))
    scores.sort(key=lambda x: -x[0])
    return scores[0][1], scores[0][0], scores[1][1], scores[1][0]


def relation(given, found):
    if given is None or found is None:
        return None
    if given == found:
        return 'same'
    (gp, gm), (fp, fm) = given, found
    if gm != fm:
        maj, mnr = (given, found) if gm == 'major' else (found, given)
        if (maj[0] - 3) % 12 == mnr[0]:
            return 'close'
    return 'no'


# ---------------------------------------------------------------- notes string / JSON -> voices
def parse_beats(s, tok):
    try:
        if '/' in s:
            a, b = s.split('/', 1)
            v = float(a) / float(b)
        else:
            v = float(s)
    except (ValueError, ZeroDivisionError):
        raise Refuse("malformed beats in token %r" % tok)
    if not (v > 0 and v <= 64 and math.isfinite(v)):
        raise Refuse("beats out of range (0 < beats <= 64) in token %r" % tok)
    return v


def parse_vel(s, tok):
    if not re.fullmatch(r'\d{1,3}', s) or not 1 <= int(s) <= 127:
        raise Refuse("velocity must be 1-127 in token %r" % tok)
    return int(s)


def parse_prog(s):
    out = []
    for p in s.split(','):
        if not re.fullmatch(r'\d{1,3}', p) or int(p) > 127:
            raise Refuse("prog must be 0-127 (GM program, 0 = piano), got %r" % s)
        out.append(int(p))
    return out


def parse_ts(s):
    mt = re.fullmatch(r'(\d{1,2})/(\d{1,2})', s)
    if not mt or int(mt.group(1)) < 1 or int(mt.group(2)) not in (1, 2, 4, 8, 16, 32):
        raise Refuse("malformed ts %r (expected 4/4, 3/4, 6/8)" % s)
    return int(mt.group(1)), int(mt.group(2))


def parse_text(text):
    """Returns a dict: bpm, key, ts, progs, voices=[[(pitch|None, beats, vel), ...], ...]."""
    head = {'bpm': 120.0, 'bpm_given': False, 'key': None, 'ts': (4, 4), 'progs': {}, 'vel': 90}
    text = text.replace(' ', ' ').strip()
    text = re.sub(r'^\s*(15q\s+)?notes\b', '', text, flags=re.I).strip()
    text = re.sub(r'^\s*15q\b', '', text, flags=re.I).strip()
    parts = [p.split() for p in re.split(r'\s*\|\s*', text)] if text else [[]]
    voices = []
    for vi, toks in enumerate(parts):
        cur = []
        for tok in toks:
            if '=' in tok:
                k, _, v = tok.partition('=')
                k = k.lower()
                if k in ('bpm', 'tempo'):
                    try:
                        b = float(v)
                    except ValueError:
                        raise Refuse("malformed bpm %r" % tok)
                    if not 20 <= b <= 400:
                        raise Refuse("bpm must be 20-400, got %r" % v)
                    head['bpm'], head['bpm_given'] = b, True
                elif k == 'key':
                    head['key'] = parse_key(v)
                elif k in ('ts', 'time'):
                    head['ts'] = parse_ts(v)
                elif k in ('prog', 'program'):
                    ps = parse_prog(v)
                    if len(ps) == 1:
                        head['progs'][vi] = ps[0]
                    else:
                        for i, p in enumerate(ps):
                            head['progs'][i] = p
                elif k == 'vel':
                    head['vel'] = parse_vel(v, tok)
                else:
                    raise Refuse("unknown header %r (known: bpm= key= ts= prog= vel=)" % tok)
                continue
            f = tok.split(':')
            if len(f) not in (2, 3) or not f[0] or not f[1]:
                raise Refuse("malformed token %r (expected NOTE:BEATS[:VEL], e.g. E4:1 or R:0.5)" % tok)
            p = parse_pitch(f[0])
            b = parse_beats(f[1], tok)
            vel = parse_vel(f[2], tok) if len(f) == 3 else None
            cur.append((p, b, vel))
        voices.append(cur)
    for v in voices:
        for i, (p, b, vel) in enumerate(v):
            v[i] = (p, b, vel if vel is not None else head['vel'])
    head['voices'] = [v for v in voices if v] or [[]]
    return head


def parse_json(data):
    head = {'bpm': 120.0, 'bpm_given': False, 'key': None, 'ts': (4, 4), 'progs': {}, 'vel': 90}

    def one(lst):
        out = []
        if not isinstance(lst, list):
            raise Refuse("a JSON voice must be a list of notes")
        for it in lst:
            if isinstance(it, dict):
                n = it.get('note', it.get('pitch'))
                b = it.get('beats', it.get('dur', it.get('len')))
                v = it.get('vel', it.get('velocity'))
            elif isinstance(it, (list, tuple)) and len(it) in (2, 3):
                n, b = it[0], it[1]
                v = it[2] if len(it) == 3 else None
            else:
                raise Refuse("malformed JSON note %r" % (it,))
            tok = json.dumps(it)
            p = None if n is None else parse_pitch(str(n))
            if isinstance(b, (int, float)) and not isinstance(b, bool):
                b = parse_beats(repr(float(b)), tok)
            elif isinstance(b, str):
                b = parse_beats(b, tok)
            else:
                raise Refuse("malformed beats in JSON note %s" % tok)
            v = head['vel'] if v is None else parse_vel(str(v), tok)
            out.append((p, b, v))
        return out

    if isinstance(data, list):
        head['voices'] = [one(data)]
        return head
    if not isinstance(data, dict):
        raise Refuse("JSON must be a note list or an object with \"notes\"")
    if 'bpm' in data:
        try:
            head['bpm'], head['bpm_given'] = float(data['bpm']), True
        except (TypeError, ValueError):
            raise Refuse("malformed bpm in JSON")
        if not 20 <= head['bpm'] <= 400:
            raise Refuse("bpm must be 20-400")
    if data.get('key'):
        head['key'] = parse_key(data['key'])
    if data.get('ts'):
        head['ts'] = parse_ts(str(data['ts']))
    if data.get('vel') is not None:
        head['vel'] = parse_vel(str(data['vel']), 'vel')
    pr = data.get('prog')
    if pr is not None:
        for i, p in enumerate(pr if isinstance(pr, list) else [pr]):
            head['progs'][i] = parse_prog(str(p))[0]
    voices = [one(data.get('notes', []))]
    if data.get('bass'):
        voices.append(one(data['bass']))
    for extra in data.get('voices', []) or []:
        voices.append(one(extra))
    head['voices'] = voices
    return head


# ---------------------------------------------------------------- MIDI writing
def vlq(n):
    out = [n & 0x7F]
    n >>= 7
    while n:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(out))


def meta(t, data):
    return b'\xff' + bytes([t]) + vlq(len(data)) + data


def track(events):
    """events: list of (abs_tick, order, bytes). Returns an MTrk chunk."""
    events.sort(key=lambda e: (e[0], e[1]))
    body, last = bytearray(), 0
    for t, _, ev in events:
        body += vlq(t - last) + ev
        last = t
    body += b'\x00\xff\x2f\x00'
    return b'MTrk' + struct.pack('>I', len(body)) + bytes(body)


def build_midi(h):
    bpm, (num, den), key = h['bpm'], h['ts'], h['key']
    conductor = [(0, 0, meta(0x03, b'SunoForge notes')),
                 (0, 1, meta(0x51, struct.pack('>I', int(round(60000000 / bpm)))[1:])),
                 (0, 2, meta(0x58, bytes([num, int(math.log2(den)), 24, 8])))]
    if key is not None:
        pc, mode = key
        sf = SF_MAJOR[pc if mode == 'major' else (pc + 3) % 12]
        conductor.append((0, 3, meta(0x59, struct.pack('>bB', sf, 1 if mode == 'minor' else 0))))
    chunks = [track(conductor)]
    names = ['Melody', 'Bass']
    for vi, voice in enumerate(h['voices']):
        ch = vi if vi < 9 else vi + 1
        if ch > 15:
            raise Refuse("too many voices (at most 15)")
        ev = [(0, 0, meta(0x03, (names[vi] if vi < 2 else 'Voice %d' % (vi + 1)).encode()))]
        if vi in h['progs']:
            ev.append((0, 1, bytes([0xC0 | ch, h['progs'][vi]])))
        t = 0.0
        for p, b, vel in voice:
            t0, t1 = int(round(t * PPQ)), int(round((t + b) * PPQ))
            if p is not None and t1 > t0:
                ev.append((t1, 2, bytes([0x80 | ch, p, 0])))   # offs sort before ons at the same tick
                ev.append((t0, 3, bytes([0x90 | ch, p, vel])))
            t += b
        chunks.append(track(ev))
    return b'MThd' + struct.pack('>IHHH', 6, 1, len(chunks), PPQ) + b''.join(chunks)


# ---------------------------------------------------------------- MIDI reading (--check)
def read_midi(data):
    """Parse an SMF. Returns a dict with notes [(start_tick, end_tick, pitch, ch)], tempos, ts, key, names."""
    if data[:4] == b'RIFF' and data[8:12] == b'RMID':
        i = data.find(b'MThd')
        if i < 0:
            raise Refuse("RIFF file without MIDI data")
        data = data[i:]
    if len(data) < 14 or data[:4] != b'MThd':
        raise Refuse("not a MIDI file (no MThd header)")
    hlen, fmt, ntrk, div = struct.unpack('>IHHH', data[4:14])
    if hlen < 6:
        raise Refuse("broken MIDI header")
    pos = 8 + hlen
    out = {'format': fmt, 'ntracks': ntrk, 'division': div, 'notes': [], 'tempos': [], 'ts': None,
           'key': None, 'names': [], 'programs': set(), 'end_tick': 0}
    tr = 0
    while pos + 8 <= len(data) and tr < ntrk:
        cid, clen = data[pos:pos + 4], struct.unpack('>I', data[pos + 4:pos + 8])[0]
        pos += 8
        chunk = data[pos:pos + clen]
        pos += clen
        if cid != b'MTrk':
            continue
        tr += 1
        i, tick, status, held = 0, 0, None, {}

        def rd_vlq():
            nonlocal i
            v = 0
            for _ in range(4):
                if i >= len(chunk):
                    raise Refuse("truncated MIDI track %d" % tr)
                c = chunk[i]
                i += 1
                v = (v << 7) | (c & 0x7F)
                if not c & 0x80:
                    return v
            raise Refuse("bad variable-length number in track %d" % tr)

        while i < len(chunk):
            tick += rd_vlq()
            if i >= len(chunk):
                break
            b = chunk[i]
            if b == 0xFF:
                if i + 1 >= len(chunk):
                    break
                mt = chunk[i + 1]
                i += 2
                ln = rd_vlq()
                d = chunk[i:i + ln]
                i += ln
                if mt == 0x51 and ln == 3:
                    out['tempos'].append((tick, (d[0] << 16) | (d[1] << 8) | d[2]))
                elif mt == 0x58 and ln >= 2 and out['ts'] is None:
                    out['ts'] = (d[0], 2 ** d[1])
                elif mt == 0x59 and ln == 2 and out['key'] is None:
                    sf = struct.unpack('b', d[:1])[0]
                    maj = [k for k, v in SF_MAJOR.items() if v == sf]
                    if maj:
                        out['key'] = ((maj[0] - 3) % 12, 'minor') if d[1] else (maj[0], 'major')
                elif mt == 0x03 and d:
                    out['names'].append(d.decode('latin-1', 'replace'))
                elif mt == 0x2F:
                    break
                status = None
                continue
            if b in (0xF0, 0xF7):
                i += 1
                i += rd_vlq()
                status = None
                continue
            if b & 0x80:
                status = b
                i += 1
            elif status is None:
                raise Refuse("running status without a status byte in track %d" % tr)
            hi, ch = status & 0xF0, status & 0x0F
            n = 1 if hi in (0xC0, 0xD0) else 2
            if hi == 0xF0:
                raise Refuse("unexpected system message 0x%02X in track %d" % (status, tr))
            d = chunk[i:i + n]
            i += n
            if len(d) < n:
                break
            if hi == 0x90 and d[1] > 0:
                held.setdefault((ch, d[0]), []).append(tick)
            elif hi == 0x80 or (hi == 0x90 and d[1] == 0):
                st = held.get((ch, d[0]))
                if st:
                    out['notes'].append((st.pop(0), tick, d[0], ch))
            elif hi == 0xC0:
                out['programs'].add((ch, d[0]))
        for (ch, p), starts in held.items():
            for s in starts:
                out['notes'].append((s, tick, p, ch))
        out['end_tick'] = max(out['end_tick'], tick)
    return out


def check_file(path):
    try:
        size = os.path.getsize(path)
    except OSError as e:
        raise Refuse("cannot read %s: %s" % (path, e.strerror))
    with open(path, 'rb') as f:
        data = f.read(MAX_BYTES * 64 + 1)
    m = read_midi(data)
    div = m['division']
    tempos = sorted(m['tempos']) or [(0, 500000)]
    if tempos[0][0] != 0:
        tempos.insert(0, (0, 500000))
    if div & 0x8000:                        # SMPTE time: ticks per second
        fps = 256 - (div >> 8)
        tps = fps * (div & 0xFF) or 1

        def secs(t):
            return t / tps
        ppq, bpm = None, None
    else:
        ppq = div or PPQ

        def secs(t):
            s, prev_t, prev_us = 0.0, 0, tempos[0][1]
            for tt, us in tempos[1:]:
                if tt >= t:
                    break
                s += (tt - prev_t) * prev_us / 1e6 / ppq
                prev_t, prev_us = tt, us
            return s + (t - prev_t) * prev_us / 1e6 / ppq
        bpm = round(60000000 / tempos[0][1], 2)
    pitched = [n for n in m['notes'] if n[3] != 9]
    num, den = m['ts'] or (4, 4)
    last = max([n[1] for n in m['notes']] or [0])
    if ppq:
        beats = last / ppq
        bars = int(math.ceil(beats / (num * 4.0 / den) - 1e-9)) if beats else 0
    else:
        beats, bars = None, None
    s = {'ok': True, 'file': path, 'bytes': size, 'format': m['format'], 'tracks': m['ntracks'],
         'ppq': ppq, 'bars': bars, 'beats': round(beats, 3) if beats is not None else None,
         'notes': len(pitched), 'drum_notes': len(m['notes']) - len(pitched),
         'duration_s': round(secs(last), 3), 'bpm': bpm,
         'tempo_changes': len(set(us for _, us in tempos)) - 1, 'ts': '%d/%d' % (num, den),
         'track_names': m['names'][:16]}
    s.update(summary_keys([(p, e - st) for st, e, p, ch in pitched], m['key']))
    s['range'] = range_str([n[2] for n in pitched])
    errs = []
    if not m['notes']:
        errs.append("no notes in the file (Suno needs a .mid with notes)")
    if size > MAX_BYTES:
        errs.append("file is %d bytes, over Suno's 256 KB MIDI limit" % size)
    if errs:
        s['ok'] = False
        s['error'] = '; '.join(errs)
    return s


# ---------------------------------------------------------------- summary
def range_str(ps):
    if not ps:
        return None
    return {'low': note_name(min(ps)), 'high': note_name(max(ps)), 'midi': [min(ps), max(ps)],
            'semitones': max(ps) - min(ps)}


def summary_keys(weighted, given):
    k = detect_key(weighted)
    d = {'key_detected': key_label(k[0]) if k else None, 'key_r': round(k[1], 3) if k else None,
         'key_runner_up': key_label(k[2]) if k else None, 'key_runner_up_r': round(k[3], 3) if k else None,
         'key_given': key_label(given), 'key_match': relation(given, k[0] if k else None)}
    return d


def summarize(h, nbytes):
    num, den = h['ts']
    total = max(sum(b for _, b, _ in v) for v in h['voices'])
    notes = [(p, b) for v in h['voices'] for p, b, _ in v if p is not None]
    s = {'ok': True, 'bytes': nbytes, 'bars': int(math.ceil(total / (num * 4.0 / den) - 1e-9)) if total else 0,
         'beats': round(total, 3), 'notes': len(notes),
         'notes_per_voice': [sum(1 for p, _, _ in v if p is not None) for v in h['voices']],
         'range': range_str([p for p, _ in notes]), 'duration_s': round(total * 60.0 / h['bpm'], 3),
         'bpm': h['bpm'] if h['bpm'] != int(h['bpm']) else int(h['bpm']), 'bpm_given': h['bpm_given'],
         'ts': '%d/%d' % (num, den)}
    s.update(summary_keys(notes, h['key']))
    return s


def fail(msg, extra=None):
    d = {'ok': False, 'error': msg}
    if extra:
        d.update(extra)
    print(json.dumps(d, ensure_ascii=False))
    sys.stderr.write('notes2mid: refused: %s\n' % msg)
    sys.exit(2)


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(description='SunoForge notes string -> .mid; --check reads a .mid back.')
    ap.add_argument('notes', nargs='*', help='the notes string (quote it); omitted -> read stdin')
    ap.add_argument('-o', '--out', help='write the .mid here (no -o: summary only)')
    ap.add_argument('--json', dest='json_in', help='a JSON note list file, - for stdin')
    ap.add_argument('--check', help='read a .mid back and print its summary')
    a = ap.parse_args(argv)
    try:
        if a.check:
            s = check_file(a.check)
            if not s['ok']:
                fail(s.pop('error'), s)
            print(json.dumps(s, ensure_ascii=False))
            return 0
        if a.json_in:
            raw = sys.stdin.read() if a.json_in == '-' else open(a.json_in, encoding='utf-8').read()
            try:
                h = parse_json(json.loads(raw))
            except ValueError as e:
                raise Refuse("bad JSON: %s" % e)
        else:
            text = ' '.join(a.notes) if a.notes else ('' if sys.stdin.isatty() else sys.stdin.read())
            if text.lstrip()[:1] in ('[', '{'):
                try:
                    h = parse_json(json.loads(text))
                except ValueError as e:
                    raise Refuse("bad JSON: %s" % e)
            else:
                h = parse_text(text)
        if not any(p is not None for v in h['voices'] for p, _, _ in v):
            raise Refuse("no notes (only rests or nothing): give tokens like E4:1 A4:0.5")
        mid = build_midi(h)
        if len(mid) > MAX_BYTES:
            raise Refuse("the .mid would be %d bytes, over Suno's 256 KB limit: shorten the melody" % len(mid))
        s = summarize(h, len(mid))
        if a.out:
            with open(a.out, 'wb') as f:
                f.write(mid)
            s['written'] = os.path.abspath(a.out)
        else:
            s['written'] = None
        print(json.dumps(s, ensure_ascii=False))
        return 0
    except Refuse as e:
        fail(str(e))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
