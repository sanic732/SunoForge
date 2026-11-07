"""Recompute every line range in INDEX.md from the reference files as they are now.

  python3 -I -X utf8 tools/index_ranges.py plugin/skills/sunoforge/references        rewrites INDEX.md in place, prints a summary

A reference is `FILE §N[–§M][ · SUBHEADING] L<a>[–<b>]`: the numbers are recomputed from the file's
<section id="§N"> tags (a section runs to the line before the next one; the last to its </section>) and its
`### SUBHEADING` lines (a subheading runs to the line before the next ### or the section's end). The SECTION MAP
lines `- FILE.md (N lines): …` get the new line count too. A reference that cannot be resolved is an error.
"""
import os, re, sys

D = sys.argv[1]
FILES = {'CORE_00': 'CORE_00_ENTRY.md', 'CORE_01': 'CORE_01_STYLE.md', 'CORE_02': 'CORE_02_LYRICS.md',
         'CORE_03': 'CORE_03_DIAGNOSE.md', 'CORE_04': 'CORE_04_WHY.md', 'DATA_BLANKS': 'DATA_BLANKS.md',
         'DATA_GOOGLE': 'DATA_GOOGLE_2026-10.md', 'DATA_LEGAL': 'DATA_LEGAL_2026-10.md',
         'DATA_OTHER': 'DATA_OTHER_2026-10.md', 'DATA_POSTPROD': 'DATA_POSTPROD.md', 'DATA_RECIPES': 'DATA_RECIPES.md',
         'DATA_SUNO_LIVE': 'DATA_SUNO_LIVE_2026-10.md', 'DATA_SUNO': 'DATA_SUNO_2026-10.md', 'DATA_VOCAB': 'DATA_VOCAB.md'}
BYNAME = {v: k for k, v in FILES.items()}

def structure(fn):
    lines = open(os.path.join(D, fn), encoding='utf-8').read().split('\n')
    if lines and lines[-1] == '': lines = lines[:-1]
    secs, subs = [], []
    for i, l in enumerate(lines, 1):
        m = re.match(r'<section id="(§\d+)" title="([^"]*)"', l)
        if m: secs.append([m.group(1), i, None, m.group(2)])
        m = re.match(r'### (.+)', l)
        if m: subs.append((i, m.group(1)))
    last_close = max(i for i, l in enumerate(lines, 1) if l.startswith('</section>'))
    foot = [i for i, l in enumerate(lines, 1) if i > last_close and l.startswith('// ═')]
    if foot: last_close = foot[0]   # as the 5.0.3 build counted: the last section runs to the footer's first line
    for k, s in enumerate(secs):
        s[2] = secs[k + 1][1] - 1 if k + 1 < len(secs) else last_close
    return len(lines), {s[0]: (s[1], s[2], s[3]) for s in secs}, subs

ST = {k: structure(v) for k, v in FILES.items()}

def sub_range(key, sec, name):
    n, secs, subs = ST[key]
    a, b, _ = secs[sec]
    inside = [(i, t) for i, t in subs if a <= i <= b]
    for j, (i, t) in enumerate(inside):
        if t == name or t.startswith(name + ' ') or t.startswith(name + ' —'):
            end = inside[j + 1][0] - 1 if j + 1 < len(inside) else b
            return i, end
    raise KeyError(f'{key} {sec} · {name}')

names = '|'.join(sorted(FILES, key=len, reverse=True))
REF = re.compile(r'\b(' + names + r')(?:_2026-10)?(?:\.md)? (§\d+)(?:–(§\d+))?(?: · ([A-Z][A-Za-z0-9 .,\'’&/()+-]*?))? L(\d+)(?:–(\d+))?')

def fix_ref(m):
    key, s1, s2, sub, a, b = m.groups()
    secs = ST[key][1]
    if sub:
        x, y = sub_range(key, s1, sub.strip())
    else:
        x = secs[s1][0]; y = secs[s2 or s1][1]
    head = m.group(0)[:m.group(0).rindex(' L')]
    return f'{head} L{x}–{y}' if b is not None else f'{head} L{x}'

MAPLINE = re.compile(r'^- `([^`]+)` \((\d+) lines\): (.*)$')
ITEM = re.compile(r'(§\d+)( · [^L]+?| [^·]+?) L(\d+)(?:–(\d+))?')

def fix_map(line):
    m = MAPLINE.match(line)
    key = BYNAME[m.group(1)]
    n, secs, subs = ST[key]
    out = []
    for part in m.group(3).split(' · §'):
        part = part if part.startswith('§') else '§' + part
        mm = re.match(r'(§\d+) (.*?) L(\d+)(?:–(\d+))?$', part)
        sid, label = mm.group(1), mm.group(2)
        if label.startswith('· '):   # a subheading item: "§6 · LIVE L470"
            x, y = sub_range(key, sid, label[2:])
            out.append(f'{sid} {label} L{x}' + (f'–{y}' if mm.group(4) else ''))
        else:
            a, b, title = secs[sid]
            out.append(f'{sid} {label} L{a}–{b}')
    seen = {p.split(' ', 1)[0] for p in out if ' · ' not in p.split(' ', 1)[1][:3]}
    missing = [s for s in secs if s not in seen]
    for s in missing:   # a section new to the file gets its own item
        a, b, title = secs[s]
        out.append(f'{s} {title.split(" — ")[0].upper()} L{a}–{b}')
    return f'- `{m.group(1)}` ({n} lines): ' + ' · '.join(out)

idx = os.path.join(D, 'INDEX.md')
txt = open(idx, encoding='utf-8').read().split('\n')
new, refs = [], 0
for line in txt:
    if MAPLINE.match(line):
        new.append(fix_map(line)); continue
    c = len(REF.findall(line)); refs += c
    new.append(REF.sub(fix_ref, line))
out = '\n'.join(new)
open(idx, 'w', encoding='utf-8').write(out)
left = re.findall(r'L0–0', out)
print(f'INDEX: {refs} references recomputed, section map for {len(FILES)} files, L0–0 left: {len(left)}')
