# SunoForge scripts (LAB): melody → Suno

Two small helpers for the `15q` MIDI screen. Both are experimental (LAB), spend nothing and reach no network.

| Script | What it does | Needs |
|---|---|---|
| `notes2mid.py` | A notes string or a JSON note list → a type-1 `.mid` (tempo, time signature, key signature, track names, optional programs). Prints one JSON line: bytes, bars, notes, range, duration_s, key_detected + key_r (Krumhansl–Schmuckler), key_given, key_match, bpm. `--check` reads any `.mid` back and prints the same summary. | Python 3.8+, standard library only |
| `audio2notes.py` | A voice memo, humming or one simple melody → the notes string (YIN pitch tracking, notes, tempo, quantize, key). | Python 3.8+, numpy; ffmpeg for anything that isn't WAV |

## Usage

```
python3 notes2mid.py "bpm=96 key=Am E4:1 A4:1 C5:1.5 B4:0.5 A4:1 G4:1 E4:2" -o melody.mid
python3 notes2mid.py "bpm=96 key=Am E4:1 A4:1 C5:1.5 | A2:4 E2:4" -o melody.mid   # second voice = bass track
python3 notes2mid.py "bpm=90 ts=3/4 prog=0,33 D4:1 F#4:1 A4:1" -o waltz.mid       # GM programs, 3/4
python3 notes2mid.py --json notes.json -o melody.mid
python3 notes2mid.py --check users-file.mid      # before an upload: notes present, at most 256 KB

python3 audio2notes.py memo.wav                  # line 1: notes string, line 2: JSON summary
python3 audio2notes.py memo.m4a --bpm 92 --mid melody.mid
```

Notes format (the same one `15q notes` and the keys widget use): `NOTE:BEATS[:VEL]` tokens, NOTE = `C4` (= MIDI 60),
`F#3`, `Bb4` or `R` for a rest; BEATS in quarter-note beats (`1`, `0.5`, `1.5`); VEL 1–127, default 90. An optional
header leads: `bpm=96 key=Am ts=4/4 prog=0 vel=90`. ` | ` starts a second voice (a bass line).

## Limits

- `notes2mid.py` refuses (exit 2, a clear message, `"ok": false` in the JSON) on no notes, a `.mid` over 256 KB
  (Suno's MIDI upload limit), a pitch outside 0–127, a malformed token or header, a file that is not MIDI.
- The key is a statistical guess from the notes' pitch classes, weighted by length; a short melody often fits its
  relative major/minor almost as well — `key_runner_up` shows the next best. `key_match` is `same`, `close`
  (relative major/minor) or `no`.
- `audio2notes.py` is for one voice or one melody line, not a full mix. For a full song: Suno's own stems, then
  MIDI (`15p #id two`, then `15q #id midi`, Premier) — or the stems, then this script on the vocals stem. The tempo
  of a free performance is a guess (give `--bpm` when known); slides become the note they land on; notes below
  65 Hz or above 1600 Hz need `--fmin` / `--fmax`; at most 10 minutes are read.

## Where they run

Only where the session has a shell: Claude Code, or a cloud session with a container. In a plain chat there is no
shell: the model writes the notes string itself, and the user attaches their own `.mid` or uses Suno's uploader.
