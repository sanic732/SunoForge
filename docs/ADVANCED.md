# For people who have used generators before

`[EN]` this file · `[RU]` [ADVANCED.ru.md](ADVANCED.ru.md)

If you used SunoForge v1.1 or v2.0, or write your own prompts, this is what
changed and why.

---

## First, what stopped working

A fact-checking pass on 27 July 2026 retired four constructions that previous
versions presented as working mechanics. If they are in your prompts, they are
dead there.

**MAX MODE.** `[Is_MAX_MODE: MAX]`, `(MAX)(MAX)(MAX)(MAX)`, `///*****///`.
There is no hidden mode: a controlled comparison across folk and reggae in
January 2026 found no difference beyond ordinary variation. It originates in a
single Reddit post. The tags read as plain quality adjectives — so there is an
effect, but it is the same one you get from writing "studio-grade, detailed",
and that version is honest about what it does.

**Parametric syntax.** `[Reverb: 30%]`, `[BPM: 120]`, `[eq: scooped]`,
`[compression: heavy]`, `[Mood: Uplifting]`, `[Energy: Low→High]`,
`[Sound: Rain]`, `[Chord progression: Am - F - C - G]`, `[Key: A minor]`.
No platform ever parsed any of it. Nothing breaks, nothing errors — the
construction simply is not a control. That silence is why it survived for years.
By volume of edits this was larger than MAX MODE.

**Two-Minute Drift and DRIFT_GUARD.** The claim that tracks reliably lose
character after two minutes rests on anecdotes: no systematic testing, no vendor
acknowledgment, no mention in detailed reviews. v2.0 built a mechanism on it that
modified **every** prompt by default. The mechanism is gone. The techniques —
a strong genre anchor in the opening words, a reset at the bridge, restating
style in later sections — remain available. They do no harm.

**The 200-character Style limit.** Nobody has demonstrated an attention cliff at
that number. The threshold cut prompts to well under half the range where
description reliably steers the result. What is actually known is in `DATA_SUNO`
§2, including the genuine disagreement between sources about whether the current
model rewards long prompts.

**Pipe stacking** (`[Chorus | 90s grunge | belted male]`) is a separate case.
One report calls it 2026 best practice; another says the syntax was never
documented at all. The "more than four modifiers causes hissing" claim was never
reproduced. Suno has documented it in neither direction. Verdict: genuinely
disputed. Use it if it works for you — the system neither emits it by default
nor strips it from your prompts.

---

## What changed architecturally

**CORE and DATA are separate files.** Rules apart from facts, because they decay
at different rates. Between March and July 2026 these broke: the default model
version, Lyria's track length, the name of Flow Music, the Studio version and
the plan it requires, stem mechanics, the lyrics editor — and two products shut
down. Not one prompting rule broke in the same window.

The practical consequence: updating means replacing one dated file. Working from
an old copy? Download the new `DATA_SUNO_2026-XX.md` and leave everything else.

**Single source of truth.** Versions, limits, prices and plan tiers live in
exactly one file each; everything else links. In v1.1 the version matrix existed
in three places and diverged — the README and the adapter file contradicted each
other, and nothing detected it.

**Two lazy files.** `CORE_04_WHY` and `DATA_LEGAL` are not loaded by default,
saving roughly 12,000 tokens. Reached with `/why` and `/legal`.

**Confidence marking.** `[OFFICIAL]` / `[COMMUNITY]` / `[UNVERIFIED]` on every
platform claim. The reason is concrete: three independent research passes on the
same questions within twenty-four hours produced three different pictures — on
whether a feature costs credits, on whether a syntax is recommended, on whether
a product still exists. Each was stated confidently. This field has almost no
primary sources, and a guide that hides that ages badly.

---

## What changed in v4.0 (September 2026)

**Suno v6.** Three models — `v6`, `v6-wild`, `v6-mini` — and every earlier model
retired on 9 September. Two new controls matter for prompt engineers:
**Variety**, which rewrites your style text above zero (set it to 0 for any
engineered Style), and **Max Mode**, a real switch for songs over two minutes,
close covers and whole-track consistency — unrelated to the old MAX tags. v6 edits
finished songs in plain words: one section, one lyric line, a mashup of several
songs, a sampled riff. Commercial rights now follow a **download** on a paid plan,
and downloads are capped per plan.

**Lyria 3.5.** Google replaced Lyria 3 Pro and rewrote its prompt guide on
17 September. Three rules from v3.0 reversed: tempo and key are written as
**numbers** ("at 92 BPM, in D minor"); structure goes into **section tags**
(`[Intro] -> [Verse 1] -> [Chorus]`) or **timestamp ranges**
(`[0:00 - 0:10] Intro: …`); own lyrics go under a `Lyrics:` header with tagged
sections and parentheses for backing vocals. PDF input is no longer documented.

**Convergence.** Google, ElevenLabs and MiniMax now publish guidance that matches
the six-layer order almost exactly — genre with an era first, named instruments,
BPM and key, a vocal described by gender, range and timbre, section tags. The same
content now moves between platforms with little translation.

**New coverage.** ElevenMusic v2.5 (ownership on every plan), Stable Audio's DAW
plugin, MiniMax Music 3.0 with open weights, ACE-Step 1.5 and YuE2 for local
generation. Menu entry `[13]` for stems, Studio and mastering. No prices anywhere.

**Two editions.** Claude gets XML, Gemini gets Markdown with no XML at all — built
from one source by a script, so the content cannot drift apart.

---

## What v3.0 introduced (July 2026) — partly superseded


**Google's official Lyria prompting guide** (April 2026) — the first and so far
only vendor-written prompting document across this entire coverage. From it:

- *(superseded in v4.0 by ranges `[0:00 - 0:10] Intro: …`)* Timestamps in `[MM:SS]` format followed by a description. Our previous
  `Intro (0–15s)` / `[End - 2:15]` was invented.
- A marker describes an **event**, not a section name: "the beat enters", "only
  the organ remains". That is a different way of thinking about structure.
- *(reversed in v4.0: Google now asks for BPM as a number)* Tempo is given in **words**, not numbers. Suno is the opposite. Carrying the
  habit across degrades results in both directions.
- Google's framework nearly matches our six-layer one, but has `Tempo and
  rhythm` where we have Structure and Production.
- Multimodal input: text, **PDF** and up to **10 images** *(PDF not documented for Lyria 3.5)*.
- Multi-vocal generation with **different languages in one track**.
- The vocal can be directed to change across the track — "calmer and quieter
  toward the end".

**Suno.** `Exclude Styles` is a real interface field with `-item` syntax, not a
homemade technique. A duration slider. Stem separation in three modes, where the
top mode **regenerates** stems with the model instead of subtracting them from
the mix — hence dramatically fewer artefacts, and external tools demoted to a
fallback. Studio (1.2 then, 2.0 now) is **Premier only**; v1.1 said "Pro", which misled people
about which subscription to buy. The web lyrics editor now places section labels
itself, which is why there are two markup paths.

**Vocal gender control** collapsed from a three-tier procedure to one line: the
selector in Advanced Options is more reliable than any wording, and stacking
negatives works against itself.

**Platforms.** Udio dropped — downloads disabled after its settlement, and a tool
you cannot export from is useless in a pipeline. Stable Audio 3.0 took its niche:
open weights, up to 6:20, you own the output. MusicFX and MusicFX DJ retire on
31 July 2026. Riffusion, Producer.ai and Flow Music are one product with three
names, not three competitors.

---

## The repair engine `[12]`

Paste an old prompt, get a diagnosis and a repaired version.

Fourteen checks: front-loading, genre count, instrument count, mood conflict,
round versus square brackets, parametric constructs, conflicting genres, Style
and Lyrics field mix-ups, gender negatives, trigger words, retired platforms,
platform syntax mismatch, length against available material, myth dependency.

Nineteen replacement rows: what to find, what to write instead, what to tell the
user.

The tone is specified separately: the engine repairs the prompt, it does not
lecture whoever wrote it. Nearly every defect arrived from a confident guide,
including previous versions of this system.

---

## Tokens

v4.0: Claude Edition ~114,200 tokens (o200k_base), ~98,500 without the lazy files; Gemini Edition ~104,400 / ~90,200. Breakdown in
[TOKENS.md](TOKENS.md).

On a 128K window the full set takes 71 %, which is a lot: keep the lazy files
unloaded (they are by default) and consider skipping the `DATA_VOCAB` and
`DATA_RECIPES` catalogues, which are not needed in every session. At 200K and
above, load everything.

---

## If you are modifying the system

- **Menu numbers 1–12 are frozen.** Forum posts and third-party guides reference
  them. Add at the tail, never reuse a number.
- **Do not copy facts between files.** Link instead. Three copies of a version
  matrix is how v1.1 began contradicting itself.
- **Extend the catalogues freely** — `DATA_VOCAB` and `DATA_RECIPES` are
  deliberately redundant for exactly that.
- **An unmarked claim is a defect.** If you cannot mark it, do not assert it —
  write "try it and listen".
