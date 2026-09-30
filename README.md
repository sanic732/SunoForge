# SunoForge v4.0 — AI Music Prompt Orchestrator

`[EN]` this file · `[RU]` [README.ru.md](README.ru.md)

A set of instructions that turns a chat assistant into a prompt engineer for music
generation. Twelve files, seven platforms, two editions, one principle: **never
present a guess as a fact**.

- **Claude Edition** — XML-native, for Claude: a plugin, a Skill or a Project (chat on
  the web, the apps, Cowork, Claude Code).
- **Gemini Edition** — pure Markdown with no XML, for Gemini Gems and the Gemini app;
  it also suits ChatGPT and Grok.

Same content, same menu, same rules. Only the packaging differs, because each model
reads its own format best. One archive holds both: the `claude/` and `gemini/` folders.

**Try it without installing anything** — the Gem with everything loaded:
[SunoForge v4.0](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing)

---

## It works at both ends

**If you know nothing about music.** Write what you want the way you would say it
to a friend — "something sad but not depressing, with a piano, for the end of a
video" — or hand it a photo, a video or a hummed voice memo. You get finished
prompts, ready to paste. No terminology, no menu numbers, no settings first.

**If you know exactly what you want.** The same system goes down to tempo and key,
spectral brightness of a timbre, where the groove sits against the beat, stereo
depth and reverb decay, slider postures per genre, Suno's Variety and Max Mode,
section-by-section performance notation, chord progressions inline, timestamp
ranges for scoring video, mastering thresholds and ratios. The vocabulary file
alone is 40 KB of descriptors; the recipe library carries 45 presets with BPM, key
and slider posture already dialled in.

Nobody has to grow into the professional layer to use the beginner one.

---

## What changed in v4.0

Between July and September 2026 the ground moved under every platform:

| What happened | What v4.0 does with it |
|---|---|
| **Suno v6** (9 Sep): v6, v6-wild, v6-mini — every earlier model retired | the whole Suno file rewritten; old model names are recognised and repaired, never offered |
| Suno added a real **Max Mode** switch and a **Variety** slider | when to use Max Mode; Variety 0 for any engineered style — above zero v6 rewrites your style text |
| Suno v6 edits finished songs in plain words: one section, one line, mashups, samples | new menu entries `2i`, `3d`–`3f`, `6g` |
| Suno **rights now follow the download** (terms in force 3 Sep), downloads capped per plan | release planning and the legal file rewritten |
| **Lyria 3.5** replaced Lyria 3 Pro; Google's prompt guide rewritten (17 Sep) | numeric BPM and key, section tags, `Lyrics:` header, timestamp **ranges** — three old rules reversed |
| **ElevenMusic v2.5**: ownership on every plan, commercial use on Free with a credit | new position in platform choice and `/free` |
| **Stable Audio 3.0** DAW plugin; **MiniMax Music 3.0** with open weights; **ACE-Step 1.5** and **YuE2** run locally | a section on music you can run on your own hardware |
| GEMA v Suno (Munich, 31 Jul), a second UMG/Sony suit, Spotify AI Persona badges, Deezer AI tagging, EU AI Act transparency rules | `/legal` updated from court and vendor texts |

And two decisions:

**No prices.** Nobody knows which country, account or plan the reader has, and
prices change without notice. Plans are named where a feature or a right depends on
them; nothing is priced.

**Only what exists.** The menu and the settings show only models and features you
can select today. Retired names live in one place: the repair table of `[12] AUDIT`,
which needs them to fix old prompts.

---

## What did not change

**Confidence marking.** Every claim about platform behaviour carries `[OFFICIAL]`
(vendor documentation), `[COMMUNITY]` (independent testing and guides) or
`[UNVERIFIED]` (widely repeated, no primary source). This time the facts were
checked against the vendors' own pages — help centres, terms of service, API docs,
a court's press release — and every page is kept as text for the record.

**The CORE / DATA split.** Rules and facts live in separate files. v4.0 is honest
about the one place it strained: three rules moved this quarter, and all three
named a platform. A rule about one platform is a fact about that platform, so it
now lives in that platform's DATA file.

**Myths stay catalogued.** MAX MODE tags, the "two-minute drift", `[Reverb: 30%]`,
the 200-character limit. Suno's real Max Mode shares a name with the old tags and
nothing else; the system says so.

---

## Platforms

- **Suno v6** — the strongest vocals, your own voice, a model trained on your catalogue, edits in plain words, Studio 2.0
- **Google Lyria 3.5 / 3 Clip / RealTime** — full songs, 30-second sketches, a live stream; in the Gemini app, API, AI Studio, Vids
- **Google Flow Music** — change one part without regenerating the rest
- **ElevenMusic v2.5** — made with rights holders, ownership on every plan, section-by-section editing
- **Stable Audio 3.0** — licensed data, open weights, you own the output, a DAW plugin
- **MiniMax Music 3.0** — open weights, full songs with vocals
- **Local models** — ACE-Step 1.5 and YuE2 on your own GPU

Udio is not a target: downloads stayed disabled after its settlement, and its
licensed successor is a walled fan app. It remains in the system as a case study.

---

## Quick start

1. Download the release archive and unpack it. SunoForge answers in the language you
   write in; `/set lang en` or `/set lang ru` pins one.
2. Load the folder for your assistant:
   - **Claude**, any of three ways ([docs/CLAUDE.md](docs/CLAUDE.md)):
     - the plugin, paid plans: **Customize → Plugins → Add → Add marketplace** →
       `sanic732/SunoForge`; in Claude Code `/plugin marketplace add sanic732/SunoForge`,
       then `/plugin install sunoforge@sunoforge`; or upload `sunoforge.plugin` with
       **Customize → Plugins → Add → Upload plugin**
     - the Skill: upload `SunoForge_v4.0_skill.zip` in **Customize → Skills**
       (Code execution on)
     - a Project with the twelve files from `claude/` as knowledge
   - **Gemini** — the five `CORE_*` files from `gemini/` plus `gemini/DATA.zip` ([docs/GEMINI.md](docs/GEMINI.md))
   - **ChatGPT, Grok** — the files from `gemini/`, attached or pasted
3. Type `start` or `/menu`.
4. Pick a menu entry, or just describe the task.

In detail: [docs/QUICKSTART.md](docs/QUICKSTART.md) · for experienced users:
[docs/ADVANCED.md](docs/ADVANCED.md)

---

## How to use it

You never have to name a menu number:

| You write | Where it goes |
|---|---|
| "a dark cinematic track with cello" | Quick start, 2–3 variants |
| "a song from this photo" | Quick start — Suno v6 or Lyria 3.5 |
| "change the chorus to a gospel choir, keep the rest" | `2i` — an edit instruction for Suno v6 |
| "like this track, but slower" | Clone mode `[3]` |
| "blend phonk and jazz" | Hybrid lab `[4]` — a bridge genre, or v6-wild |
| "I need a raspy female vocalist" | Persona workshop `[5]` — a biography, not a tag |
| "score my video to the cuts" | Platform lab `[7]` — Lyria 3.5 with timestamp ranges |
| "can I run this offline?" | Platform compare `[10]` — open weights and local models |
| "can I monetise this?" | `/legal` |
| "split the stems and master it" | `[13]` — stems, Studio, mastering |
| "here's my old prompt" | Audit `[12]` — diagnosis and repair |

Every request returns **two or three interpretations**, not one "correct" answer.

---

## Configuring the core

Settings live at the top of `CORE_00_ENTRY.md`, in the preloader. Edit them
before loading, or change them mid-session with `/set`.

```
TARGET_PLATFORM  = "auto"      // auto | suno | lyria | flow | eleven | stable | minimax | local | dual | all
SUNO_VERSION     = "v6"        // v6 | v6-wild | v6-mini | custom
SUNO_PLAN        = "unknown"   // unknown | free | pro | premier — only gates features
SUNO_MAX_MODE    = "suggest"   // suggest | on | off
LYRIA_MODEL      = "3.5"       // 3.5 | clip | realtime
DURATION         = "auto"      // auto | a target length
OUTPUT_LANG      = "auto"      // auto | en | ru — auto: the language you write in
VARIANT_COUNT    = 2           // 1 | 2 | 3
USER_LEVEL       = "auto"      // auto | beginner | pro
SESSION_MODE     = "creative"  // creative | technical | clone
VOICES_ENABLED   = false       // true once you have a Suno Voice
CUSTOM_MODEL     = ""          // name of your trained Suno model
SHOW_CONFIDENCE  = true
FOLKLORE_MODE    = "off"
```

**Change these first**

- `SUNO_PLAN` — tell it `free` and it stops offering v6, v6-wild, stems and Studio;
  leave it `unknown` and it names the plan a feature needs and asks only when it
  matters.
- `TARGET_PLATFORM` — set it if you use one platform only.
- `VARIANT_COUNT` — `1` when you know what you want, `3` when you are searching.
- `OUTPUT_LANG` — the language of answers and the menu; `auto` follows the language
  you write in. Prompts are English, except Lyria, which sings in the language of
  the prompt.

```
/set suno v6-mini     /set plan free          /set maxmode on
/set platform lyria   /set duration 3:30      /set variants 3
/set lang ru          /confidence off         /menu
```

---

## What is inside

**CORE — rules. Undated.**

| File | Covers |
|---|---|
| `CORE_00_ENTRY.md` | Preloader, system map, the menu `[1]`–`[13]`, routing, output formats, critical rules |
| `CORE_01_STYLE.md` | Six layers and how four vendor guides line up with them, Time & Place, personas, hybrids, cloning |
| `CORE_02_LYRICS.md` | Section labels, notation, ad-libs, duets, chords; what carries over to Lyria, MiniMax, local models |
| `CORE_03_DIAGNOSE.md` | Symptom index, 15 checks, 25 repair rows, early Suno v6 failure reports |
| `CORE_04_WHY.md` | Why each rule is shaped the way it is — including the ones that turned out wrong. On `/why` |

**DATA — facts. Dated, replaced when platforms move.**

| File | Covers |
|---|---|
| `DATA_SUNO_2026-09.md` | v6 family, Max Mode, Variety, Duration, edits, Voices, Custom Models, Studio 2.0, stems, plans, downloads |
| `DATA_GOOGLE_2026-09.md` | Lyria 3.5 / Clip / RealTime, Google's prompt guide, timestamp ranges, the Gemini app, Flow Music |
| `DATA_OTHER_2026-09.md` | ElevenMusic, Stable Audio, MiniMax, local models, `/free`, platform compare, one idea for every platform |
| `DATA_VOCAB.md` | Timbre, dynamics, groove, space, instruments, key and tempo, theory as prompt language |
| `DATA_RECIPES.md` | Genre recipes, 45 presets, task scenarios |
| `DATA_POSTPROD.md` | Stems, Studio, mastering chain, loudness, DAW handoff — menu `[13]` |
| `DATA_LEGAL_2026-09.md` | Rights, terms, voices, catalogues, litigation, streaming and distributor policies, EU AI Act. On `/legal` |

Every file is prepared for retrieval: frontmatter with a description, a system map,
anchored zones, tags — assembled to the RAG standard of P2P.

For Claude the same twelve files also ship as a Skill: a short `SKILL.md` router plus
the files in `references/`, opened per task. This repository is its marketplace —
`.claude-plugin/marketplace.json` and the plugin in `plugin/`; the release carries the
Skill as a ZIP for a manual upload.

---

## Size and tokens

| Edition | Size | Tokens (o200k_base) | Without the two lazy files |
|---|---|---|---|
| Claude (XML) | 457 KB | ~114,100 | ~98,400 |
| Gemini (Markdown) | 420 KB | ~104,300 | ~90,100 |

Comfortable in a 1M or 200K window; too tight for 128K. Details: [docs/TOKENS.md](docs/TOKENS.md).

---

## Built with P2P

Designed and assembled with **[P2P](https://github.com/sanic732/P2P)** — an open
cross-model meta-prompt framework by the same author. P2P supplied the method:
a technique earns its place by surviving a test; the core is not a database; fix
a declaration, then check everyone who cites it. For v4.0 it also supplied the RAG
standard the files are built to, the rule that Gemini gets Markdown and Claude gets
XML, and a QUORUM review of the finished build.

---

## Licence and sources

MIT. Free to use, modify and redistribute, commercially included.

Suno, Google, Lyria, Gemini, ElevenLabs, Stability AI, MiniMax and other names belong
to their owners. This project is unaffiliated with and unendorsed by any of them.
Sources and legal notes: [docs/CREDITS.md](docs/CREDITS.md) · history:
[docs/CHANGELOG.md](docs/CHANGELOG.md)

**Where is v2.0?** The May 2026 edition was Russian-only and published on the 4PDA
forum: [SunoForge v2.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142556185).
