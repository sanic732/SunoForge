# SunoForge v3.0 — AI Music Prompt Orchestrator

`[EN]` this file · `[RU]` [README.ru.md](README.ru.md)

A set of instructions that turns any chat assistant into a prompt engineer for
music generation. Twelve files, five platforms, one principle: **never present a
guess as a fact**.

Runs in Claude, Gemini, ChatGPT, Grok — anything you can paste a long text into
or attach files to.

**Try it without installing anything** — a ready-made Gem with everything already
loaded: [SunoForge v3.0](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing)

---

## It works at both ends

**If you know nothing about music.** Write what you want the way you would say it
to a friend — "something sad but not depressing, with a piano, for the end of a
video". You get finished prompts, ready to paste. No terminology, no menu numbers,
no settings to configure first. The system asks for the era and the mood, not for
your BPM.

**If you know exactly what you want.** The same system takes you down to the
level of tempo and key, spectral brightness of a timbre, where the groove sits
against the beat, stereo depth and reverb decay, slider values per genre, the
gender and character of a voice, section-by-section performance notation, chord
progressions written inline, mastering chain thresholds and ratios. The vocabulary
file alone is 42 KB of descriptors, and the recipe library carries 45 presets
with BPM, key and slider settings already dialled in.

Nobody has to grow into the professional layer to use the beginner one. Ask in
plain words and it stays out of your way; ask for a scooped-mid guitar tone at
92 BPM in D minor with a laid-back pocket and it is already there.

---

## What changed in v3.0

Three independent fact-checking passes on 27 July 2026 established that both
previous editions had been presenting community folklore in the voice of
documentation. Four load-bearing "mechanics" did not survive the check:

| Taught as fact | What checking found |
|---|---|
| **MAX MODE** — a hidden quality mode | No such mode. Controlled comparison found no difference |
| **Two-Minute Drift** — tracks degrade after ~2 min | Anecdotes only. No testing, no vendor acknowledgment |
| **Tags like `[Reverb: 30%]`, `[BPM: 120]`** | Never parsed by any covered platform |
| **A ~200 character Style limit** | Wrong. It cut prompts to a fifth of the working range |

Two principles follow from that.

**Confidence marking.** Every claim about platform behaviour carries
`[OFFICIAL]` (vendor documentation), `[COMMUNITY]` (independent testing and
guides) or `[UNVERIFIED]` (widely repeated, no primary source). An unmarked
claim is a defect.

**A CORE / DATA split.** Rules and facts live in separate files because they
decay at different rates. Between March and July 2026 every platform fact broke
— the default model version, Lyria's track length, the name of Flow Music, the
Studio version, stem mechanics, the lyrics editor — and two products shut down
entirely. **Not one prompting rule broke in the same period.** So updating means
replacing one `DATA_*` file, not rebuilding the system.

---

## Platforms

- **Suno** — the strongest vocals, your own voice, a model trained on your catalogue, full editing
- **Google Lyria 3** Pro / Clip / RealTime — the only platform with a vendor-published prompting guide
- **Google Flow Music** — change one part without regenerating the rest
- **ElevenMusic** — licensed training data, mid-track genre switching, per-section regeneration
- **Stable Audio 3.0** — open weights, the longest single generation, you own the output

Udio is not a target platform: downloads were disabled following its settlement.
It remains in the system as a cautionary case.

---

## Quick start

1. Open an assistant with a long context window.
2. Load the contents of `files/` — all twelve files, or the five `CORE_*` files plus an archive of the `DATA_*` files (see [docs/GEMINI.md](docs/GEMINI.md)).
3. Type `start` or `/menu`.
4. Then pick a menu entry, or just describe the task in plain words.

In detail: [docs/QUICKSTART.md](docs/QUICKSTART.md) ·
for experienced users: [docs/ADVANCED.md](docs/ADVANCED.md)

---

## How to use it

You never have to name a menu number. Describe the task and the system routes it:

| You write | Where it goes |
|---|---|
| "a dark cinematic track with cello" | Quick start, 2–3 variants |
| "like this track, but slower" | Clone mode `[3]` |
| "blend phonk and jazz" | Hybrid lab `[4]` — finds a bridge genre |
| "I need a raspy female vocalist" | Persona workshop `[5]` — a biography, not a tag |
| "I need a five-minute track" | Platform compare `[10]` |
| "here's my prompt, why does it sound bad" | Audit `[12]` — diagnosis and repair |
| "can I monetise this?" | `/legal` |

Every request returns **two or three interpretations** rather than one "correct"
answer. Usually the genre changes while mood and vocal hold steady — the same
intent as several different records.

---

## Configuring the core

All settings live at the top of `files/CORE_00_ENTRY.md`, in the `<preloader>`
block. Edit the values in the file before loading, or change them mid-session
with `/set`.

```
HOST_MODEL       = "auto"     // auto | claude | gemini | gpt | grok
TARGET_PLATFORM  = "auto"     // auto | suno | lyria | flow | eleven | stable | dual | all
SUNO_VERSION     = "v5.5"     // v5.5 | v5 | v4.5-all (free tier)
LYRIA_MODEL      = "pro"      // pro | clip | realtime
DURATION         = "auto"     // auto | a target track length
OUTPUT_LANG      = "en"       // en | ru — language of explanations
VARIANT_COUNT    = 2          // 1 | 2 | 3 — interpretations per idea
USER_LEVEL       = "auto"     // auto | beginner | pro — depth of explanation
SESSION_MODE     = "creative" // creative | technical | clone
VOICES_ENABLED   = false      // true if Suno Pro/Premier and a voice is uploaded
CUSTOM_MODEL     = ""         // name of your trained Suno model
SHOW_CONFIDENCE  = true       // show reliability marks
FOLKLORE_MODE    = "off"      // off | on — unproven techniques
```

**Change these first**

- `OUTPUT_LANG` sets the language of explanations. Prompts themselves are always
  English — the platforms understand it best.

  ⚙️ The release ships as two archives, `_ru` and `_en`, but **you do not have to
  choose by language**: they hold the same twelve files and differ by exactly
  this line. Whichever you downloaded is fine — switch any time with
  `/set lang en` or `/set lang ru`.
- `TARGET_PLATFORM` — set it if you only use one platform, and you stop getting
  variants you cannot use. `all` renders one idea for every platform at once.
- `VARIANT_COUNT` — set `1` when you know exactly what you want, `3` when you
  are still looking for the idea.
- `SUNO_VERSION` — on the free tier set `v4.5-all`, or the system will offer
  features your account does not have.

**Finer adjustments**

- `SHOW_CONFIDENCE = false` hides the `[OFFICIAL]`/`[COMMUNITY]` marks if they
  make output harder to read. The system keeps applying the distinction — it
  just stops printing it.
- `FOLKLORE_MODE = "on"` restores unproven techniques such as MAX MODE. They
  stay labelled as unproven. Turn it on if you want to compare for yourself.
- `USER_LEVEL = "pro"` drops the explanations and returns prompts only.

The same settings mid-session, without editing the file:

```
/set lang en          /set platform suno       /set variants 3
/set suno v4.5-all    /set duration 3:30       /confidence off
/set lyria clip       /folklore on             /menu
```

---

## What is inside

**The CORE layer — rules. Undated, they last for years.**

| File | Covers |
|---|---|
| `CORE_00_ENTRY.md` | Preloader, the 12-entry menu, routing, output protocols, confidence marking |
| `CORE_01_STYLE.md` | Six-layer Style construction, Time & Place, personas, hybrids, style cloning |
| `CORE_02_LYRICS.md` | Section labels, performance notation, ad-libs, duets, chords, two markup paths |
| `CORE_03_DIAGNOSE.md` | The repair engine: 14 checks and 19 replacement rows for dead constructs |
| `CORE_04_WHY.md` | Why each rule is shaped the way it is. Loaded on `/why` |

**The DATA layer — facts. Dated, replaced quarterly.**

| File | Covers |
|---|---|
| `DATA_SUNO_2026-07.md` | Versions, fields, sliders, voice training, custom models, stems, plans |
| `DATA_GOOGLE_2026-07.md` | The Lyria 3 family, Flow Music, `[MM:SS]` prompting, multimodal input |
| `DATA_OTHER_2026-07.md` | ElevenMusic, Stable Audio, MiniMax, aggregators, free-tier comparison |
| `DATA_VOCAB.md` | Sound vocabulary: timbre, dynamics, groove, space, instrument descriptors |
| `DATA_RECIPES.md` | Genre recipes, 45 presets, task-driven scenarios |
| `DATA_POSTPROD.md` | Mastering chain, stems, DAW handoff, loudness targets |
| `DATA_LEGAL_2026-07.md` | Rights, consent, litigation, platform policies. Loaded on `/legal` |

---

## Size and tokens

414.7 KB · **~91,300 tokens** (o200k_base).

Two files are lazy and are not loaded by default, so the starting load is
**78,716 tokens**. Full table: [docs/TOKENS.md](docs/TOKENS.md).

| Context window | Full set | Without lazy files |
|---|---|---|
| 1M | 9.1 % | 7.9 % |
| 200K | 45.4 % | 39.4 % |
| 128K | 70.9 % | 61.5 % |

---

## Built with P2P

This system was designed and assembled using **[P2P](https://github.com/sanic732/P2P-4PDA-edition)**
— an open cross-model meta-prompt framework by the same author.

That is not a badge. P2P shaped how v3.0 is built, and the two share the same
convictions:

- **A prompt is proven, not admired.** The rule that a technique earns its place
  by surviving a test — not by looking authoritative — comes straight from P2P's
  core. It is why MAX MODE and three other "mechanics" were removed here.
- **Core is not a database.** Invariants and routing belong in one layer,
  catalogues and reference data in another. Migrating one into the other is an
  architectural defect, not a shortcut. That principle produced the CORE / DATA
  split.
- **Fix a declaration, then check everyone who cites it.** Link connectivity is
  the defect class both projects fight hardest. Seven build invariants here are
  mechanical checks for exactly that.

If you write prompt systems rather than prompts, P2P is the tool that makes this
kind of build repeatable.

---

## Licence and sources

MIT. Free to use, modify and redistribute, commercially included.

Suno, Google, Lyria, ElevenLabs, Stability AI and other names belong to their
respective owners. This project is unaffiliated with and unendorsed by any of
them. Full source list and legal notes: [docs/CREDITS.md](docs/CREDITS.md).

Version history: [docs/CHANGELOG.md](docs/CHANGELOG.md)

**Where is v2.0?** It exists, but it never came here. The May 2026 edition was
Russian-only and was published on the 4PDA forum:
[SunoForge v2.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142556185).
It introduced the six-layer Style construction and multi-platform support, both
carried into v3.0 — along with several ideas that later failed fact-checking and
were removed.
