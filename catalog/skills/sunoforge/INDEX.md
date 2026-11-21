---
file_id: INDEX
version: "5.0"
layer: index
role: router
description: >
  The route map of SunoForge as a metaprompt: for every task and every platform, which
  sections to read, in which order, to write the prompt a music generator will read — with
  the line range of every section in this edition. Generated at build from INDEX.src.md and
  the built files; read once per conversation at the first task (SKILL.md, step 2).
scope: conveyor · platform_profiles · tasks_and_codes · questions · section_map
depends_on: [CORE_00_ENTRY]
used_by: [SKILL]
updated: "2026-11-20"
---

# 🧭 SUNOFORGE v5.0 — INDEX
# The route map · generated at build

> SunoForge is a metaprompt: a reference that is also the prompt which writes the music
> prompt. This file is its route map. For a request, take the TASK row (§3) and the
> PLATFORM row (§2), join their sections, walk the CONVEYOR (§1), and open each section
> in its file, under its heading `## §N · …`. A section already read in this conversation is not read again. All the
> files named here sit in the same folder as this one.
> Files marked "on request" (DATA_OTHER, DATA_LEGAL, CORE_04_WHY) are read when the task
> needs them; DATA_OTHER is announced in one line and read on a yes (CORE_00 §9 LOADING).

## §1 · THE CONVEYOR — every prompt, every platform

```
1 INTAKE    a menu pick shows the entry's blank — DATA_BLANKS §1 and its § in §3 below; a
            concrete task fills the slots silently; the settings are the preloader of CORE_00
            and the user's settings file (already read)
2 DECIDE    how many readings (VARIANT_COUNT) and how far apart — CORE_00 §3; no platform
            named → TARGET_PLATFORM, else the auto-detect of CORE_00 §5; the CHOOSE row of
            §2 only for [10] or "which generator"
3 METHOD    the task's sections — §3 below (CORE_01 for sound, CORE_02 for words)
4 DIALECT   the platform's sections — §2 below: its fields, limits, what it rewrites, its traps
5 WORDS     the exact descriptor — DATA_VOCAB §1 then the matching §; a genre, preset or
            task that matches a recipe — DATA_RECIPES §1 then §2–§6
6 WRITE     the RESULT FRAME and the platform's block — CORE_00 §6
7 CHECK     before delivery — CORE_01 §14 (style) · CORE_02 §15 (lyrics) · the checks of
            CORE_03 §2 that apply to the platform · CORE_00 §7 critical rules
8 SEND      only with a generator server in the session and the user's yes —
            DATA_SUNO_LIVE §6 pre-flight → DATA_SUNO_LIVE §7 · PRICE CARD card → CORE_00 §6 · LIVE
9 AFTER     the take — DATA_SUNO_LIVE §5 read back → CORE_03 §0 symptom index → the
            next blueprint
```
Steps 2, 6 and 7 happen on every prompt, step 1 on a menu pick; 3–5 by the rows below; 8–9 only
with a server.

## §2 · PLATFORM PROFILES — the dialect of each generator

| Platform (TARGET_PLATFORM) | Facts, fields, limits | Lyrics and structure | Output block | Traps and repairs | Rights |
|---|---|---|---|---|---|
| Suno v6 — `suno` (default) | DATA_SUNO §1 models · DATA_SUNO §2 · PRACTICAL SHAPE Style field · DATA_SUNO §3 · HOW TO WRITE IT Exclude and ready lists · DATA_SUNO §4 Max Mode, Variety, duration (the evidence above each rule: DATA_SUNO §2–§3, on "why") · DATA_SUNO §8 sliders | CORE_02 §1–§2 · CORE_02 §13 | CORE_00 §6 · SUNO v6 | CORE_03 §7 · DATA_SUNO §14 myths | DATA_SUNO §12 |
| Suno v6 edit of a finished song | DATA_SUNO §7 · DATA_SUNO §11 lyrics editor | CORE_02 §2 | CORE_00 §6 · SUNO v6 EDIT | CORE_03 §7 | DATA_SUNO §12 |
| Suno Voices, Custom Models | DATA_SUNO §5–§6 | — | CORE_00 §6 · SUNO v6 | — | DATA_LEGAL §3–§4 (on request) |
| Suno Speech — `speech` | DATA_SUNO §15 | CORE_02 §16 | CORE_00 §6 · SUNO SPEECH | DATA_SUNO_LIVE §3 (Tone rewritten) | DATA_SUNO §12 |
| Suno through the MCP (LIVE) | DATA_SUNO_LIVE §1–§4 tools, field map, traps, plan gating · DATA_SUNO_LIVE §9 capabilities | as for Suno v6 | CORE_00 §6 · LIVE · DATA_SUNO_LIVE §7 · PRICE CARD card | DATA_SUNO_LIVE §6 pre-flight and recovery | DATA_SUNO §16 |
| Suno Studio, stems | DATA_SUNO §9–§10 | — | — | — | DATA_SUNO §12 |
| Lyria 3.5 / Clip — `lyria` | DATA_GOOGLE §1 · DATA_GOOGLE §3 Google's guide | DATA_GOOGLE §4–§5 · CORE_02 §14 | CORE_00 §6 · LYRIA 3.5 / 3 CLIP | CORE_03 §7 | DATA_LEGAL §2 (on request) |
| Lyria from a photo or a video | DATA_GOOGLE §6 | DATA_GOOGLE §4 timing | CORE_00 §6 · LYRIA 3.5 / 3 CLIP | — | — |
| Lyria RealTime | DATA_GOOGLE §8 | — | CORE_00 §6 · LYRIA 3.5 / 3 CLIP | — | — |
| Gemini app | DATA_GOOGLE §2 · DATA_GOOGLE §10 | DATA_GOOGLE §5 | CORE_00 §6 · LYRIA 3.5 / 3 CLIP | — | — |
| Google Flow Music — `flow` | DATA_GOOGLE §7 | DATA_GOOGLE §5 | CORE_00 §6 · GOOGLE FLOW MUSIC | — | — |
| ElevenMusic — `eleven` | DATA_OTHER §1 (on request) | CORE_02 §14 | CORE_00 §6 · ELEVENMUSIC | CORE_03 §7 | DATA_OTHER §1 |
| Stable Audio — `stable` | DATA_OTHER §2 (on request) | — | CORE_00 §6 · STABLE AUDIO 3.0 | — | DATA_OTHER §2 |
| MiniMax, local models — `minimax`, `local` | DATA_OTHER §3 · DATA_OTHER §5 (on request) | CORE_02 §14 | CORE_00 §6 · MINIMAX MUSIC 3.0 / LOCAL MODELS | — | DATA_OTHER §5 |
| Several at once — `dual`, `all` | DATA_OTHER §10–§11 · DATA_RECIPES §7 | each platform's own | CORE_00 §6 · DUAL / ALL | — | — |
| CHOOSE — no platform named | CORE_00 §3 platform rule · DATA_OTHER §7 decision tree · DATA_OTHER §6 free plans | — | — | — | — |

Every platform also takes the sound method of CORE_01 §2, which lines the six layers up
with each vendor's own guide.

## §3 · TASKS AND MENU CODES — the method

| Task, code | The blank | Method sections | Also |
|---|---|---|---|
| a song from an idea · [1] | DATA_BLANKS §2 | CORE_01 §1 six layers · CORE_01 §3 time and place · CORE_01 §13 assembly | DATA_RECIPES §2 when the genre matches |
| studio by hand · [2] | DATA_BLANKS §3 | 2a CORE_01 §3–§4 · 2b CORE_01 §5 · 2c CORE_01 §6 · 2d DATA_VOCAB §8 · 2e CORE_01 §9 · 2f CORE_01 §8, CORE_02 §12 | 2g DATA_SUNO §8 · 2h DATA_SUNO §3 · 2i DATA_SUNO §7 · 2j, 2k DATA_SUNO §4 |
| clone a style · [3] | DATA_BLANKS §4 | CORE_01 §12 · DATA_VOCAB §2–§5 | 3d–3g DATA_SUNO §7 |
| hybrid · [4] | DATA_BLANKS §5 | CORE_01 §10 | DATA_RECIPES §3 |
| voices, personas · [5] | DATA_BLANKS §6 | CORE_01 §6–§7 · 5c CORE_02 §9 · 5d CORE_02 §6 | 5e DATA_SUNO §5 · 5f DATA_SUNO §6 · 5g DATA_GOOGLE §5 |
| lyrics and markup · [6] | DATA_BLANKS §7 | CORE_02 §1–§4 · CORE_02 §12–§13 · 6c CORE_02 §5–§6 · 6d CORE_02 §10 · 6e CORE_02 §7–§8 | 6f DATA_SUNO §11 · 6g DATA_SUNO §7 · 6h CORE_02 §14 |
| another generator · [7] | DATA_BLANKS §8 | the platform's row of §2 | — |
| one idea, several generators · [8] | DATA_BLANKS §9 | DATA_OTHER §10–§11 | DATA_RECIPES §7 |
| recipes · [9] | DATA_BLANKS §10 | DATA_RECIPES §1–§6 | — |
| which generator · [10] | DATA_BLANKS §11 | DATA_OTHER §7 | DATA_OTHER §6 |
| rights before release · [11] | DATA_BLANKS §12 | DATA_LEGAL §1–§2 · DATA_LEGAL §10–§11 | DATA_SUNO §12 |
| fix and check · [12] | DATA_BLANKS §13 | CORE_03 §0 · CORE_03 §2–§3 · CORE_03 §5 · CORE_03 §8 | 12b DATA_SUNO_LIVE §5 |
| after the take · [13] | DATA_BLANKS §14 | DATA_POSTPROD §2 · DATA_POSTPROD §4 · DATA_POSTPROD §7 · DATA_POSTPROD §9 | DATA_SUNO §9–§10 |
| speech · [14] | DATA_BLANKS §15 | CORE_02 §16 | DATA_SUNO §15 |
| My Suno, your songs · [15] · `mcp-menu` | DATA_BLANKS §16 | DATA_SUNO_LIVE §7 · MCP MENU the hub · DATA_SUNO_LIVE §7 · MY SONGS and DATA_SUNO_LIVE §7 · SONG ACTIONS when songs are asked for · DATA_SUNO_LIVE §9 | CORE_00 §6 · LIVE · CORE_00 §6 · CONNECTIONS |
| stems, MIDI, publish · `15p` `15q` `15r` | DATA_BLANKS §16 | DATA_SUNO_LIVE §3 · DATA_SUNO_LIVE §7 · CHAINS · DATA_SUNO_LIVE §6 | DATA_SUNO §10 · DATA_POSTPROD §4 |
| a song from the user's own melody (LAB) · [16] · `15q` | DATA_BLANKS §17 · DATA_BLANKS §16 | DATA_SUNO_LIVE §2 · DATA_SUNO_LIVE §3 | DATA_SUNO §7 MIDI as a Create input |
| change a finished song (words, a part, an instrument) · `15m … replace` | DATA_BLANKS §16 | DATA_SUNO_LIVE §2 · DATA_SUNO_LIVE §7 · CREATE AND EDITOR | DATA_SUNO §7 |
| an edit in plain words ("slower", "younger voice") | — | CORE_03 §0 → CORE_03 §3 or CORE_03 §5 · the layer in CORE_01 | DATA_VOCAB §12 |
| "surprise me" | — | CORE_01 §10–§11 · CORE_02 §5–§6 · CORE_02 §10–§11 | DATA_VOCAB §6 |
| the user's own lyrics | — | CORE_02 §1 · CORE_02 §13 — format, never rewrite (CORE_00 §7 rule 9a) | — |
| "why this rule?" | — | CORE_04 §1–§3 (on request) | — |
| "what is free?" | — | DATA_OTHER §6 (on request) | — |

## §4 · QUESTIONS → SECTIONS

| The user asks | Go to |
|---|---|
| "which Suno model?" / "what is v6-wild?" | DATA_SUNO §1 |
| "what is Max Mode?" / "does MAX MODE work?" | DATA_SUNO §4 · CORE_03 §3 |
| "why was my style rewritten?" | DATA_SUNO §4 (Variety) |
| "change the chorus / one line of a finished song" | DATA_SUNO_LIVE §2 · DATA_SUNO §7 · CORE_02 §2 |
| "how long can a song be?" | DATA_SUNO §4 · DATA_GOOGLE §4 · DATA_OTHER §1–§3 |
| "how many credits does a call cost?" / "why two songs?" | DATA_SUNO_LIVE §3–§4 |
| "what can the Suno connector do?" | DATA_SUNO_LIVE §9 |
| "what does this Suno tool do, cost, return?" | DATA_SUNO_LIVE §10 |
| "self-check" / «самодиагностика» — is my copy whole? | CORE_00 §5 (the SELF-CHECK row; `command_self-check.md`) |
| "stems?" | DATA_SUNO §10 · DATA_POSTPROD §4 · DATA_SUNO_LIVE §3 |
| "MIDI?" / "can Suno play my melody?" / "publish it?" | DATA_SUNO_LIVE §3 · DATA_SUNO_LIVE §9 |
| "my own voice?" | DATA_SUNO §5 · DATA_LEGAL §3 |
| "can I use it commercially?" / "can my Free song become commercial?" | DATA_SUNO §12 · DATA_LEGAL §2 |
| "what can I do for free?" | DATA_OTHER §6 |
| "it sounds muffled / cuts off / ignores my tags / talks in the intro" | CORE_03 §0 · CORE_03 §5 |
| "a pause where the parts join" / "how do I join two parts or genres" | DATA_SUNO §7 · CORE_03 §5 · DATA_POSTPROD §6 |
| "how loud for Spotify?" | DATA_POSTPROD §9 |
| "a Lyria / Gemini song" | DATA_GOOGLE §3–§5 |

## §5 · SECTION MAP — every section of every file, with its lines

- `CORE_00_ENTRY.md` (959 lines): §0 SYSTEM MAP · §1 IDENTITY · §2 CONFIDENCE MARKING · §3 CREATIVE PHILOSOPHY · §4 MAIN MENU · §5 ROUTING DISPATCH · §6 OUTPUT PROTOCOL · §6 · SUNO v6 · §6 · SUNO v6 EDIT · §6 · SUNO SPEECH · §6 · LIVE · §6 · CONNECTIONS · §6 · LYRIA 3.5 / 3 CLIP · §6 · GOOGLE FLOW MUSIC · §6 · ELEVENMUSIC · §6 · STABLE AUDIO 3.0 · §6 · MINIMAX MUSIC 3.0 / LOCAL MODELS · §6 · DUAL / ALL · §7 CRITICAL RULES · §8 LAYERS AND UPDATE POLICY · §9 STARTUP BEHAVIOR · §10 MIGRATION FROM v4.0, v3.0, v2.0 AND v1.1
- `CORE_01_STYLE.md` (1099 lines): §1 THE SIX-LAYER FRAMEWORK · §2 ONE FRAMEWORK, FOUR VENDOR GUIDES · §3 TIME & PLACE · §4 MOOD & ENERGY · §5 INSTRUMENTATION · §6 VOCAL DIRECTION · §7 VOICES AND PERSONAS · §8 STRUCTURE · §9 PRODUCTION SIGNATURE · §10 HYBRID LAB · §11 ATMOSPHERE AND SCENE · §12 CLONE A STYLE · §13 ASSEMBLY · §14 CHECKLIST
- `CORE_02_LYRICS.md` (1049 lines): §1 THE BRACKET RULE · §2 TWO PATHS · §3 SECTION LABELS · §4 HOW MUCH TO PUT IN A LABEL · §5 PERFORMANCE NOTATION · §6 DELIVERY AND EMOTION · §7 AD-LIBS AND BACKING VOCALS · §8 SPOKEN WORD · §9 DUET AND MULTI-VOICE · §10 CHORDS · §11 ATMOSPHERE AT SECTION LEVEL · §12 STRUCTURE TEMPLATES · §13 THE TOP OF THE LYRICS FIELD · §14 OTHER PLATFORMS · §15 CHECKLIST · §16 SCRIPTS FOR SUNO SPEECH
- `CORE_03_DIAGNOSE.md` (934 lines): §0 SYMPTOM INDEX · §1 WHAT AUDIT IS FOR · §2 THE DIAGNOSTIC PROTOCOL · §3 THE REPAIR TABLE · §4 TRIGGER WORDS · §5 FAILURE MODES · §6 WHAT IS NOT A DEFECT · §7 PLATFORM-SPECIFIC PROBLEMS · §8 FAST TRIAGE
- `CORE_04_WHY.md` (754 lines): §1 THE CRITICAL RULES · §2 TECHNIQUES · §3 THE ARCHITECTURE · §4 WHY THINGS WERE REMOVED · §5 IF YOU ONLY REMEMBER FIVE THINGS
- `DATA_BLANKS.md` (695 lines): §1 HOW A BLANK IS SHOWN · §2 [1] QUICK START · §3 [2] STUDIO · §4 [3] CLONE A STYLE · §5 [4] HYBRID LAB · §6 [5] VOICES · §7 [6] LYRICS AND MARKUP · §8 [7] OTHER GENERATORS · §9 [8] ONE IDEA, SEVERAL GENERATORS · §10 [9] RECIPES · §11 [10] WHICH GENERATOR · §12 [11] RIGHTS BEFORE RELEASE · §13 [12] FIX AND CHECK · §14 [13] AFTER THE TAKE · §15 [14] SPEECH · §16 [15] MY SUNO · §17 [16] LAB
- `DATA_GOOGLE_2026-10.md` (665 lines): §1 THE LYRIA FAMILY · §2 SURFACES · §3 PROMPTING LYRIA 3.5 · §4 STRUCTURE AND TIMING · §5 VOCALS AND LYRICS · §6 MULTIMODAL INPUT · §7 GOOGLE FLOW MUSIC · §8 LYRIA REALTIME · §9 RETIRED AND CONSOLIDATED · §10 CHOOSING WITHIN THE GOOGLE FAMILY · §11 WORKED EXAMPLES
- `DATA_LEGAL_2026-10.md` (500 lines): §1 THE DISTINCTION EVERYTHING ELSE DEPENDS ON · §2 WHERE EACH PLATFORM STANDS · §3 UPLOADING YOUR VOICE · §4 TRAINING A MODEL ON YOUR CATALOGUE · §5 STREAMING, DISTRIBUTION AND PLATFORM POLICIES · §6 LITIGATION · §7 THE UDIO CASE · §8 WATERMARKING AND PROVENANCE · §9 REGULATION · §10 WHEN TO RAISE A WARNING · §11 A CHECKLIST BEFORE RELEASE
- `DATA_OTHER_2026-10.md` (664 lines): §1 ELEVENMUSIC · §2 STABLE AUDIO 3.0 · §3 MINIMAX MUSIC 3.0 · §4 AGGREGATORS AND REGIONAL ACCESS · §5 LOCAL OPEN MODELS · §6 WHAT YOU CAN DO WITHOUT A PAID PLAN · §7 WHICH GENERATOR · §8 PLATFORMS DELIBERATELY NOT COVERED · §9 WORKED EXAMPLES · §10 WHAT TRANSFERS BETWEEN PLATFORMS · §11 ONE IDEA, EVERY PLATFORM
- `DATA_POSTPROD.md` (679 lines): §1 SHOULD YOU PROCESS THIS AT ALL? · §2 THE MASTERING CHAIN · §3 WHAT NOT TO DO · §4 STEMS · §5 PROCESSING INDIVIDUAL STEMS · §6 EDITING ENVIRONMENTS · §7 HANDING OFF TO A DAW · §8 RESTORATION · §9 LOUDNESS AND DELIVERY · §10 MOVING MATERIAL BETWEEN PLATFORMS · §11 THREE WALKTHROUGHS
- `DATA_RECIPES.md` (1729 lines): §1 HOW TO READ A RECIPE · §2 CORE GENRE RECIPES · §3 HYBRID RECIPES · §4 DUET · §5 STYLE PRESETS · §6 TASK SCENARIOS · §7 ONE IDEA, EVERY PLATFORM · §8 BUILDING YOUR OWN LIBRARY
- `DATA_SUNO_2026-10.md` (1073 lines): §1 VERSION MATRIX · §2 THE STYLE FIELD · §3 EXCLUDE STYLES · §4 MAX MODE, VARIETY AND DURATION · §5 VOICES · §6 CUSTOM MODELS · §7 EDITING, REMIXING AND REFERENCES ON v6 · §8 SLIDERS · §9 SUNO STUDIO 2.0 · §10 STEM SEPARATION · §11 LYRICS EDITOR · §12 PLANS · §13 WHAT SHIPPED · §14 MYTHS · §15 SPEECH (beta) · §16 SUNO MCP AND THE SUNO API · §17 SHARING
- `DATA_SUNO_LIVE_2026-10.md` (895 lines): §1 TOOLS · §2 FIELD MAP · §3 DEFAULTS AND TRAPS · §4 PLAN GATING · §5 READ BACK · §6 PRE-FLIGHT AND AUTO-RECOVERY · §7 CHAINS, PANEL AND CARDS · §8 NOT KNOWN · §9 CAPABILITIES · §10 EVERY TOOL ON ONE PAGE
- `DATA_VOCAB.md` (839 lines): §1 HOW TO USE THIS · §2 TIMBRE · §3 DYNAMICS · §4 GROOVE · §5 SPACE · §6 INSTRUMENT DESCRIPTORS · §7 PRODUCTION AND MIX CHARACTER · §8 KEY AND TEMPO · §9 MODES AND SCALES · §10 THEORY → PROMPT LANGUAGE, BY GENRE · §11 INSTRUMENT NAMES · §12 PUTTING WORDS TOGETHER

// ═══════════════════════════════════════════════════════════════
// END OF INDEX.md · SunoForge v5.0
// Generated at build from build/index/INDEX.src.md — edit the source, not this file
// ═══════════════════════════════════════════════════════════════
