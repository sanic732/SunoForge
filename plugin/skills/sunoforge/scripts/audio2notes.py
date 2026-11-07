#!/usr/bin/env python3
"""audio2notes.py - SunoForge `15q hum`: a voice memo, humming or one simple melody -> the `15q notes` string.

LAB (experimental). Spends nothing: no network, no Suno call. Python 3.8+ and numpy (the only dependency).

FOR ONE VOICE OR ONE MELODY LINE, NOT A FULL MIX. It tracks a single (monophonic) pitch: humming, whistling, a
sung line, one instrument playing a tune. A finished song with drums, chords and a singer gives garbage. For a full
song the route is Suno's own stems, then MIDI (`15p #id two`, then `15q #id midi`, Premier) - or the stems, then
this script on the vocals stem.

HOW: read WAV with the stdlib `wave` (any rate, mixed to mono; other formats - mp3, m4a, ogg, webm, a WAV it
cannot read - go through `ffmpeg` to 16 kHz mono WAV when ffmpeg is installed, else it asks for a WAV) ->
resample to 16 kHz -> YIN pitch per 10 ms frame (de Cheveigne & Kawahara 2002: difference function, cumulative
mean normalised difference, absolute threshold, parabolic interpolation) -> voiced/unvoiced from the YIN
aperiodicity and the frame energy -> octave-jump repair and median smoothing -> the singer's overall tuning offset
removed -> notes cut where the pitch moves by more than ~0.6 semitone for 40 ms or the loudness jumps (a repeated
note) -> notes shorter than --min-note dropped -> semitones -> tempo from the note onsets (inter-onset intervals
against an eighth-note grid, 60-180 BPM, a mild preference for ~100) unless --bpm -> onsets and lengths snapped
to the --grid (0.5 beat by default), gaps of a grid step or more become rests -> key by Krumhansl-Schmuckler
(notes2mid.py, next to this file).

USAGE
    audio2notes.py memo.wav                    line 1: the notes string (bpm=.. key=.. E4:1 ...), line 2: JSON
    audio2notes.py memo.m4a --bpm 92           a known tempo; other formats need ffmpeg
    audio2notes.py memo.wav --grid 0.25        a sixteenth grid for fast lines
    audio2notes.py memo.wav --mid melody.mid   also write the .mid (same as notes2mid.py on line 1)
    audio2notes.py memo.wav --json             only the JSON (the notes string is in "notes_string")
  Options: --fmin 65 --fmax 1600 (Hz), --min-note 0.08 (s), --threshold 0.15 (YIN).
  JSON: notes, bpm, bpm_source, key, key_r, confidence (0-1, mean YIN periodicity on the notes), voiced_share,
        duration_s, tuning_cents, warnings.
LIMITS: one voice; at most 10 minutes are read; the tempo of a free, rubato performance is a guess - give --bpm
  when it is known; vibrato is followed, slides become the note they land on; very low (< 65 Hz) or very high
  (> 1600 Hz, above G6) notes need --fmin / --fmax.
EXIT: 0 ok; 2 refused (no file, unreadable audio, no ffmpeg for a non-WAV, no notes found); 3 numpy missing.
"""
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import wave

try:
    import numpy as np
except ImportError:
    sys.stderr.write("audio2notes: numpy is needed: pip install numpy\n")
    print(json.dumps({'ok': False, 'error': 'numpy is needed: pip install numpy'}))
    sys.exit(3)

SR = 16000
HOP = 160          # 10 ms
WIN = 640          # 40 ms integration window
MAX_S = 600


class Refuse(Exception):
    pass


def _notes2mid():
    import importlib.util
    sys.dont_write_bytecode = True        # no __pycache__ next to the plugin's scripts
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notes2mid.py')
    sp = importlib.util.spec_from_file_location('sf_notes2mid', p)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


# ---------------------------------------------------------------- audio in
def read_wav(path):
    with wave.open(path, 'rb') as w:
        ch, sw, sr, n = w.getnchannels(), w.getsampwidth(), w.getframerate(), w.getnframes()
        n = min(n, sr * MAX_S)
        raw = w.readframes(n)
    if sw == 1:
        x = (np.frombuffer(raw, dtype=np.uint8).astype(np.float32) - 128.0) / 128.0
    elif sw == 2:
        x = np.frombuffer(raw, dtype='<i2').astype(np.float32) / 32768.0
    elif sw == 3:
        b = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 3).astype(np.int32)
        v = b[:, 0] | (b[:, 1] << 8) | (b[:, 2] << 16)
        v = np.where(v & 0x800000, v - 0x1000000, v)
        x = v.astype(np.float32) / 8388608.0
    elif sw == 4:
        x = np.frombuffer(raw, dtype='<i4').astype(np.float32) / 2147483648.0
    else:
        raise Refuse("unsupported WAV sample width %d" % sw)
    if ch > 1:
        x = x[:len(x) // ch * ch].reshape(-1, ch).mean(axis=1)
    return x, sr


def load_audio(path):
    if not os.path.isfile(path):
        raise Refuse("no such file: %s" % path)
    if path.lower().endswith(('.wav', '.wave')):
        try:
            return read_wav(path)
        except (wave.Error, EOFError, Refuse) as e:
            why = str(e)
    else:
        why = 'not a WAV file'
    ff = shutil.which('ffmpeg')
    if not ff:
        raise Refuse("%s and ffmpeg is not installed here: attach the recording as a WAV file "
                     "(16-bit PCM, any rate, mono or stereo)" % why)
    fd, tmp = tempfile.mkstemp(suffix='.wav')
    os.close(fd)
    try:
        r = subprocess.run([ff, '-nostdin', '-v', 'error', '-y', '-i', path, '-t', str(MAX_S), '-vn',
                            '-ac', '1', '-ar', str(SR), '-acodec', 'pcm_s16le', '-f', 'wav', tmp],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=300)
        if r.returncode != 0:
            raise Refuse("ffmpeg could not read %s: %s" % (os.path.basename(path),
                                                           r.stderr.decode('utf-8', 'replace').strip()[:300]))
        return read_wav(tmp)
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass


def resample(x, sr):
    if sr == SR:
        return x.astype(np.float64)
    x = x.astype(np.float64)
    if sr > SR:                       # windowed-sinc low-pass below the new Nyquist, then interpolate
        fc = 0.45 * SR / sr
        n = np.arange(-48, 49)
        h = 2 * fc * np.sinc(2 * fc * n) * np.hamming(len(n))
        x = np.convolve(x, h / h.sum(), mode='same')
    t = np.arange(0, len(x) / sr, 1.0 / SR)
    return np.interp(t, np.arange(len(x)) / sr, x)


# ---------------------------------------------------------------- YIN
def yin(x, fmin, fmax, thr):
    """Returns f0 (Hz, per frame), aperiodicity d'(tau*) per frame, rms per frame."""
    tmax = int(math.ceil(SR / fmin))
    tmin = max(2, int(SR / fmax))
    L = WIN + tmax + 1
    x = np.concatenate([x, np.zeros(L)])
    nf = max(0, (len(x) - L) // HOP + 1)
    N = 1 << int(math.ceil(math.log2(L + WIN)))
    f0 = np.zeros(nf)
    ap = np.ones(nf)
    rms = np.zeros(nf)
    taus = np.arange(tmax + 1)
    for c0 in range(0, nf, 256):
        idx = np.arange(c0, min(nf, c0 + 256))
        fr = x[(idx * HOP)[:, None] + np.arange(L)[None, :]]
        fr = fr - fr[:, :WIN].mean(axis=1, keepdims=True)
        F = np.fft.rfft(fr, N)
        A = np.fft.rfft(fr[:, :WIN], N)
        r = np.fft.irfft(np.conj(A) * F, N)[:, :tmax + 1]
        cs = np.concatenate([np.zeros((len(idx), 1)), np.cumsum(fr * fr, axis=1)], axis=1)
        e0 = cs[:, WIN]
        et = cs[:, taus + WIN] - cs[:, taus]
        d = np.maximum(e0[:, None] + et - 2 * r, 0.0)
        d[:, 0] = 0
        cm = np.cumsum(d[:, 1:], axis=1)
        dp = np.ones_like(d)
        dp[:, 1:] = d[:, 1:] * taus[1:][None, :] / np.maximum(cm, 1e-12)
        rms[idx] = np.sqrt(e0 / WIN)
        for j, row in enumerate(dp):
            seg = row[tmin:tmax]
            below = np.nonzero(seg < thr)[0]
            if len(below):
                t = below[0] + tmin
                while t + 1 < tmax and row[t + 1] < row[t]:
                    t += 1
            else:
                t = int(np.argmin(seg)) + tmin
            a = row[t]
            if 1 <= t < tmax:                      # parabolic interpolation
                y0, y1, y2 = row[t - 1], row[t], row[t + 1]
                den = y0 - 2 * y1 + y2
                sh = 0.5 * (y0 - y2) / den if abs(den) > 1e-12 else 0.0
                sh = max(-1.0, min(1.0, sh))
                tt = t + sh
            else:
                tt = float(t)
            f0[idx[j]] = SR / tt if tt > 0 else 0.0
            ap[idx[j]] = a
    return f0, ap, rms


def medfilt(v, k):
    if len(v) < 3 or k < 3:
        return v.copy()
    h = k // 2
    p = np.concatenate([np.full(h, v[0]), v, np.full(h, v[-1])])
    return np.median(np.stack([p[i:i + len(v)] for i in range(k)]), axis=0)


def runs(mask):
    """[(start, end_exclusive)] of True runs."""
    out, s = [], None
    for i, m in enumerate(mask):
        if m and s is None:
            s = i
        elif not m and s is not None:
            out.append((s, i))
            s = None
    if s is not None:
        out.append((s, len(mask)))
    return out


# ---------------------------------------------------------------- frames -> notes
def track(x, a):
    f0, ap, rms = yin(x, a.fmin, a.fmax, a.threshold)
    nf = len(f0)
    if nf == 0:
        raise Refuse("the recording is empty")
    peak = np.percentile(rms, 99) if nf else 0
    floor = np.percentile(rms, 10)
    if peak <= 1e-5:
        raise Refuse("the recording is silent")
    e_thr = max(floor * 2.5, peak * 0.05)
    voiced = (ap < 0.3) & (rms > e_thr) & (f0 >= a.fmin * 0.97) & (f0 <= a.fmax * 1.03)
    # bridge 1-2 frame dropouts, drop 1-2 frame blips
    v = voiced.copy()
    for s, e in runs(~v):
        if e - s <= 2 and s > 0 and e < nf:
            v[s:e] = True
    for s, e in runs(v):
        if e - s <= 2:
            v[s:e] = False
    midi = np.where(f0 > 0, 69 + 12 * np.log2(np.maximum(f0, 1e-6) / 440.0), 0.0)
    db = 20 * np.log10(np.maximum(rms, 1e-9))
    segs = []
    for s, e in runs(v):
        m = midi[s:e].copy()
        ref = medfilt(m, 9)
        jump = np.abs(m - ref) > 8                 # octave errors -> fold toward the local median
        m[jump] -= 12 * np.round((m[jump] - ref[jump]) / 12.0)
        m = medfilt(m, 5)
        segs.append((s, e, m))
    return segs, f0, ap, rms, db, v


def tuning_offset(segs):
    vals = np.concatenate([m for _, _, m in segs]) if segs else np.zeros(0)
    if len(vals) == 0:
        return 0.0
    ang = 2 * np.pi * (vals - np.round(vals))
    return float(np.arctan2(np.mean(np.sin(ang)), np.mean(np.cos(ang))) / (2 * np.pi))


def split_notes(segs, db, ap, off, min_frames):
    notes = []
    K = 4
    for s, e, m in segs:
        m = m - off
        cuts = [0]
        cur = np.round(np.median(m[:K]))
        dev = 0
        for i in range(len(m)):
            if abs(m[i] - cur) > 0.6:
                dev += 1
                if dev >= K:
                    st = i - K + 1
                    cuts.append(st)
                    cur = np.round(np.median(m[st:i + 1]))
                    dev = 0
            else:
                dev = 0
        # loudness re-attacks (a repeated note on the same pitch)
        seg_db = db[s:e]
        on = []
        for i in range(6, len(seg_db)):
            lo = int(np.argmin(seg_db[i - 6:i])) + i - 6
            if seg_db[i] - seg_db[lo] >= 7 and seg_db[lo] < np.max(seg_db) - 9:
                if not on or lo - on[-1] > 8:
                    on.append(lo)
        on_set = set(c for c in on if all(abs(c - k) > 4 for k in cuts))
        cuts = sorted(set(cuts) | on_set)
        bounds = cuts + [len(m)]
        parts = [(bounds[i], bounds[i + 1]) for i in range(len(bounds) - 1)]
        # merge parts shorter than the minimum into the neighbour with the closer pitch
        changed = True
        while changed and len(parts) > 1:
            changed = False
            for i, (a, b) in enumerate(parts):
                if b - a < min_frames:
                    pm = np.median(m[a:b])
                    left = abs(np.median(m[parts[i - 1][0]:parts[i - 1][1]]) - pm) if i > 0 else 1e9
                    right = abs(np.median(m[parts[i + 1][0]:parts[i + 1][1]]) - pm) if i + 1 < len(parts) else 1e9
                    if left <= right:
                        parts[i - 1] = (parts[i - 1][0], b)
                    else:
                        parts[i + 1] = (a, parts[i + 1][1])
                    del parts[i]
                    changed = True
                    break
        for a, b in parts:
            if b - a < min_frames:
                continue
            core = m[a + (b - a) // 5: b - (b - a) // 5] if b - a >= 10 else m[a:b]
            p = int(np.round(np.median(core)))
            conf = float(np.clip(1 - np.mean(ap[s + a:s + b]), 0, 1))
            notes.append([(s + a) * HOP / SR, (s + b) * HOP / SR, p, conf, a in on_set])
    # join neighbours that are the same pitch with a tiny gap and no re-attack (a dropout)
    out = []
    for n in notes:
        if out and n[2] == out[-1][2] and n[0] - out[-1][1] < 0.03 and not n[4]:
            out[-1][1] = n[1]
        else:
            out.append(n)
    return out


def estimate_bpm(onsets):
    if len(onsets) < 3:
        return None
    ioi = np.diff(onsets)
    ioi = ioi[ioi > 0.05]
    if len(ioi) < 2:
        return None
    best = None
    for bpm in np.arange(60.0, 180.01, 0.25):
        e = 30.0 / bpm
        r = ioi / e
        k = np.maximum(1, np.round(r))
        err = float(np.mean(np.abs(r - k))) + 0.06 * abs(math.log2(bpm / 100.0))
        if best is None or err < best[0]:
            best = (err, bpm, k)
    k = best[2]
    return float(30.0 * k.sum() / ioi.sum()), best[0]


def quantize(notes, bpm, grid):
    e = grid * 60.0 / bpm
    on = [n[0] for n in notes]
    q = [0]
    for i in range(1, len(notes)):
        q.append(q[-1] + max(1, int(round((on[i] - on[i - 1]) / e))))
    toks = []
    for i, n in enumerate(notes):
        snd = max(1, int(round((n[1] - n[0]) / e)))
        if i + 1 < len(notes):
            span = q[i + 1] - q[i]
            gap = on[i + 1] - n[1]
            if span - snd >= 1 and gap >= max(0.6 * e, 0.1):
                toks.append((n[2], snd))
                toks.append((None, span - snd))
            else:
                toks.append((n[2], span))
        else:
            toks.append((n[2], snd))
    return toks, q


FLAT_KEYS = {'F', 'Bb', 'Eb', 'Ab', 'Db', 'Dm', 'Gm', 'Cm', 'Fm', 'Bbm', 'Ebm'}
SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']


def fmt_beats(b):
    s = ('%.3f' % b).rstrip('0').rstrip('.')
    return s or '0'


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(description='One voice / one melody line -> the SunoForge notes string.')
    ap.add_argument('audio')
    ap.add_argument('--bpm', type=float, help='the tempo, when known (otherwise estimated)')
    ap.add_argument('--grid', type=float, default=0.5, help='quantize grid in beats (0.5 = eighths, 0.25)')
    ap.add_argument('--fmin', type=float, default=65.0)
    ap.add_argument('--fmax', type=float, default=1600.0)
    ap.add_argument('--min-note', type=float, default=0.08, help='shortest note kept, seconds')
    ap.add_argument('--threshold', type=float, default=0.15, help='YIN absolute threshold')
    ap.add_argument('--mid', help='also write a .mid here')
    ap.add_argument('--json', action='store_true', help='print only the JSON summary')
    a = ap.parse_args(argv)
    try:
        if not 30 <= a.fmin < a.fmax <= 2000:
            raise Refuse("need 30 <= --fmin < --fmax <= 2000")
        if a.grid not in (0.125, 0.25, 0.5, 1.0):
            raise Refuse("--grid is one of 0.125 0.25 0.5 1")
        if a.bpm is not None and not 20 <= a.bpm <= 400:
            raise Refuse("--bpm must be 20-400")
        raw, sr = load_audio(a.audio)
        dur = len(raw) / float(sr)
        x = resample(raw, sr)
        mx = np.max(np.abs(x)) if len(x) else 0
        if mx > 0:
            x = x / mx
        segs, f0, aper, rms, db, voiced = track(x, a)
        off = tuning_offset(segs)
        notes = split_notes(segs, db, aper, off, max(3, int(round(a.min_note * SR / HOP))))
        if not notes:
            raise Refuse("no notes found: is there a voice or a melody in it? (one voice, not a full mix)")
        warnings = []
        if a.bpm:
            bpm, src = float(a.bpm), 'given'
        else:
            est = estimate_bpm([n[0] for n in notes])
            if est is None:
                bpm, src = 100.0, 'default'
                warnings.append('too few notes to estimate the tempo: bpm=100 assumed, give --bpm')
            else:
                bpm, src = est[0], 'estimated'
                if est[1] > 0.22:
                    warnings.append('the rhythm fits no steady tempo well: give --bpm, or check the lengths')
        bpm_out = int(round(bpm)) if src != 'given' or bpm == int(bpm) else round(bpm, 2)
        toks, _ = quantize(notes, bpm_out, a.grid)
        n2m = _notes2mid()
        k = n2m.detect_key([(p, b) for p, b in toks if p is not None])
        key = n2m.key_label(k[0]) if k else None
        names = FLAT if key in FLAT_KEYS else SHARP
        body = ' '.join(('R' if p is None else names[p % 12] + str(p // 12 - 1)) + ':' + fmt_beats(b * a.grid)
                        for p, b in toks)
        line = 'bpm=%s%s %s' % (bpm_out, ' key=' + key if key else '', body)
        conf = float(np.mean([n[3] for n in notes]))
        vshare = float(np.mean(voiced)) if len(voiced) else 0.0
        if vshare < 0.2:
            warnings.append('little voiced sound: is there a clear melody in it?')
        if conf < 0.7:
            warnings.append('low pitch confidence: more than one voice or a full mix? For a song: Suno stems '
                            'first, then this script on the vocals stem')
        if len(notes) < 3:
            warnings.append('fewer than 3 notes found')
        if dur > MAX_S - 0.01:
            warnings.append('only the first %d s were read' % MAX_S)
        s = {'ok': True, 'notes': sum(1 for p, _ in toks if p is not None),
             'rests': sum(1 for p, _ in toks if p is None), 'bpm': bpm_out, 'bpm_source': src,
             'grid_beats': a.grid, 'key': key, 'key_r': round(k[1], 3) if k else None,
             'confidence': round(conf, 3), 'voiced_share': round(vshare, 3), 'duration_s': round(dur, 2),
             'tuning_cents': int(round(off * 100)),
             'onsets_s': [round(n[0], 3) for n in notes][:64], 'warnings': warnings}
        if a.mid:
            h = n2m.parse_text(line)
            mid = n2m.build_midi(h)
            if len(mid) > n2m.MAX_BYTES:
                raise Refuse("the .mid would be over 256 KB")
            with open(a.mid, 'wb') as f:
                f.write(mid)
            s['mid'] = os.path.abspath(a.mid)
        if a.json:
            s['notes_string'] = line
        else:
            print(line)
        print(json.dumps(s, ensure_ascii=False))
        return 0
    except Refuse as e:
        sys.stderr.write('audio2notes: refused: %s\n' % e)
        print(json.dumps({'ok': False, 'error': str(e)}, ensure_ascii=False))
        return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
