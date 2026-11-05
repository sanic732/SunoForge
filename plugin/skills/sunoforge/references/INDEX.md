<sunoforge_file id="INDEX" version="5.0" layer="index" role="router" source="INDEX.md">
<file_meta>
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
updated: "2026-11-05"
</file_meta>

# 🧭 SUNOFORGE v5.0 — INDEX
# The route map · generated at build · line ranges match the files of this edition

> SunoForge is a metaprompt: a reference that is also the prompt which writes the music
> prompt. This file is its route map. For a request, take the TASK row (§3) and the
> PLATFORM row (§2), join their sections, walk the CONVEYOR (§1), and open each section
> with the Read tool at the line range given — `offset` = the first line, `limit` = the
> range's length. A section already read in this conversation is not read again. All the
> files named here sit in the same folder as this one. If a range lands mid-text (a file was
> edited after the build), search the file for its `§N` heading instead.
> Files marked "on request" (DATA_OTHER, DATA_LEGAL, CORE_04_WHY) are read when the task
> needs them; DATA_OTHER is announced in one line and read on a yes (CORE_00 §9 LOADING).

<section id="§1" title="THE CONVEYOR — every prompt, every platform">

```
1 INTAKE    a menu pick shows the entry's blank — DATA_BLANKS §1 L31–58 and its § in §3 below; a
            concrete task fills the slots silently; the settings are the preloader of CORE_00
            and the user's settings file (already read)
2 DECIDE    how many readings (VARIANT_COUNT) and how far apart — CORE_00 §3 L167–202; no platform
            named → TARGET_PLATFORM, else the auto-detect of CORE_00 §5 L305–364; the CHOOSE row of
            §2 only for [10] or "which generator"
3 METHOD    the task's sections — §3 below (CORE_01 for sound, CORE_02 for words)
4 DIALECT   the platform's sections — §2 below: its fields, limits, what it rewrites, its traps
5 WORDS     the exact descriptor — DATA_VOCAB §1 L34–65 then the matching §; a genre, preset or
            task that matches a recipe — DATA_RECIPES §1 L34–83 then §2–§6
6 WRITE     the RESULT FRAME and the platform's block — CORE_00 §6 L365–585
7 CHECK     before delivery — CORE_01 §14 L1052–1077 (style) · CORE_02 §15 L977–997 (lyrics) · the checks of
            CORE_03 §2 L108–222 that apply to the platform · CORE_00 §7 L586–664 critical rules
8 SEND      only with a generator server in the session and the user's yes —
            DATA_SUNO_LIVE §6 L277–340 pre-flight → DATA_SUNO_LIVE §7 · PRICE CARD L509–522 card → CORE_00 §6 · LIVE L470–520
9 AFTER     the take — DATA_SUNO_LIVE §5 L249–276 read back → CORE_03 §0 L34–69 symptom index → the
            next blueprint
```
Steps 2, 6 and 7 happen on every prompt, step 1 on a menu pick; 3–5 by the rows below; 8–9 only
with a server.

</section>

<section id="§2" title="PLATFORM PROFILES — the dialect of each generator">

| Platform (TARGET_PLATFORM) | Facts, fields, limits | Lyrics and structure | Output block | Traps and repairs | Rights |
|---|---|---|---|---|---|
| Suno v6 — `suno` (default) | DATA_SUNO §1 L44–113 models · DATA_SUNO §2 · PRACTICAL SHAPE L148–165 Style field · DATA_SUNO §3 · HOW TO WRITE IT L202–239 Exclude and ready lists · DATA_SUNO §4 L240–338 Max Mode, Variety, duration (the evidence above each rule: DATA_SUNO §2–§3 L114–239, on "why") · DATA_SUNO §8 L598–655 sliders | CORE_02 §1–§2 L30–163 · CORE_02 §13 L866–927 | CORE_00 §6 · SUNO v6 L367–434 | CORE_03 §7 L847–920 · DATA_SUNO §14 L882–933 myths | DATA_SUNO §12 L768–835 |
| Suno v6 edit of a finished song | DATA_SUNO §7 L430–597 · DATA_SUNO §11 L747–767 lyrics editor | CORE_02 §2 L92–163 | CORE_00 §6 · SUNO v6 EDIT L435–449 | CORE_03 §7 L847–920 | DATA_SUNO §12 L768–835 |
| Suno Voices, Custom Models | DATA_SUNO §5–§6 L339–429 | — | CORE_00 §6 · SUNO v6 L367–434 | — | DATA_LEGAL §3–§4 L162–224 (on request) |
| Suno Speech — `speech` | DATA_SUNO §15 L934–976 | CORE_02 §16 L998–1045 | CORE_00 §6 · SUNO SPEECH L450–469 | DATA_SUNO_LIVE §3 L130–222 (Tone rewritten) | DATA_SUNO §12 L768–835 |
| Suno through the MCP (LIVE) | DATA_SUNO_LIVE §1–§4 L38–248 tools, field map, traps, plan gating · DATA_SUNO_LIVE §9 L563–639 capabilities | as for Suno v6 | CORE_00 §6 · LIVE L470–520 · DATA_SUNO_LIVE §7 · PRICE CARD L509–522 card | DATA_SUNO_LIVE §6 L277–340 pre-flight and recovery | DATA_SUNO §16 L977–1041 |
| Suno Studio, stems | DATA_SUNO §9–§10 L656–746 | — | — | — | DATA_SUNO §12 L768–835 |
| Lyria 3.5 / Clip — `lyria` | DATA_GOOGLE §1 L51–126 · DATA_GOOGLE §3 L147–251 Google's guide | DATA_GOOGLE §4–§5 L252–388 · CORE_02 §14 L928–976 | CORE_00 §6 · LYRIA 3.5 / 3 CLIP L537–561 | CORE_03 §7 L847–920 | DATA_LEGAL §2 L80–161 (on request) |
| Lyria from a photo or a video | DATA_GOOGLE §6 L389–414 | DATA_GOOGLE §4 L252–316 timing | CORE_00 §6 · LYRIA 3.5 / 3 CLIP L537–561 | — | — |
| Lyria RealTime | DATA_GOOGLE §8 L483–506 | — | CORE_00 §6 · LYRIA 3.5 / 3 CLIP L537–561 | — | — |
| Gemini app | DATA_GOOGLE §2 L127–146 · DATA_GOOGLE §10 L523–555 | DATA_GOOGLE §5 L317–388 | CORE_00 §6 · LYRIA 3.5 / 3 CLIP L537–561 | — | — |
| Google Flow Music — `flow` | DATA_GOOGLE §7 L415–482 | DATA_GOOGLE §5 L317–388 | CORE_00 §6 · GOOGLE FLOW MUSIC L562–570 | — | — |
| ElevenMusic — `eleven` | DATA_OTHER §1 L38–145 (on request) | CORE_02 §14 L928–976 | CORE_00 §6 · ELEVENMUSIC L571–573 | CORE_03 §7 L847–920 | DATA_OTHER §1 L38–145 |
| Stable Audio — `stable` | DATA_OTHER §2 L146–202 (on request) | — | CORE_00 §6 · STABLE AUDIO 3.0 L574–576 | — | DATA_OTHER §2 L146–202 |
| MiniMax, local models — `minimax`, `local` | DATA_OTHER §3 L203–251 · DATA_OTHER §5 L282–324 (on request) | CORE_02 §14 L928–976 | CORE_00 §6 · MINIMAX MUSIC 3.0 / LOCAL MODELS L577–579 | — | DATA_OTHER §5 L282–324 |
| Several at once — `dual`, `all` | DATA_OTHER §10–§11 L531–659 · DATA_RECIPES §7 L1655–1664 | each platform's own | CORE_00 §6 · DUAL / ALL L580–585 | — | — |
| CHOOSE — no platform named | CORE_00 §3 L167–202 platform rule · DATA_OTHER §7 L371–436 decision tree · DATA_OTHER §6 L325–370 free plans | — | — | — | — |

Every platform also takes the sound method of CORE_01 §2 L118–183, which lines the six layers up
with each vendor's own guide.

</section>

<section id="§3" title="TASKS AND MENU CODES — the method">

| Task, code | The blank | Method sections | Also |
|---|---|---|---|
| a song from an idea · [1] | DATA_BLANKS §2 L59–89 | CORE_01 §1 L29–117 six layers · CORE_01 §3 L184–264 time and place · CORE_01 §13 L967–1051 assembly | DATA_RECIPES §2 L84–1097 when the genre matches |
| studio by hand · [2] | DATA_BLANKS §3 L90–145 | 2a CORE_01 §3–§4 L184–328 · 2b CORE_01 §5 L329–378 · 2c CORE_01 §6 L379–449 · 2d DATA_VOCAB §8 L539–601 · 2e CORE_01 §9 L670–736 · 2f CORE_01 §8 L635–669, CORE_02 §12 L800–865 | 2g DATA_SUNO §8 L598–655 · 2h DATA_SUNO §3 L166–239 · 2i DATA_SUNO §7 L430–597 · 2j, 2k DATA_SUNO §4 L240–338 |
| clone a style · [3] | DATA_BLANKS §4 L146–204 | CORE_01 §12 L901–966 · DATA_VOCAB §2–§5 L66–312 | 3d–3g DATA_SUNO §7 L430–597 |
| hybrid · [4] | DATA_BLANKS §5 L205–230 | CORE_01 §10 L737–843 | DATA_RECIPES §3 L1098–1304 |
| voices, personas · [5] | DATA_BLANKS §6 L231–280 | CORE_01 §6–§7 L379–634 · 5c CORE_02 §9 L581–677 · 5d CORE_02 §6 L386–469 | 5e DATA_SUNO §5 L339–397 · 5f DATA_SUNO §6 L398–429 · 5g DATA_GOOGLE §5 L317–388 |
| lyrics and markup · [6] | DATA_BLANKS §7 L281–326 | CORE_02 §1–§4 L30–323 · CORE_02 §12–§13 L800–927 · 6c CORE_02 §5–§6 L324–469 · 6d CORE_02 §10 L678–741 · 6e CORE_02 §7–§8 L470–580 | 6f DATA_SUNO §11 L747–767 · 6g DATA_SUNO §7 L430–597 · 6h CORE_02 §14 L928–976 |
| another generator · [7] | DATA_BLANKS §8 L327–368 | the platform's row of §2 | — |
| one idea, several generators · [8] | DATA_BLANKS §9 L369–381 | DATA_OTHER §10–§11 L531–659 | DATA_RECIPES §7 L1655–1664 |
| recipes · [9] | DATA_BLANKS §10 L382–397 | DATA_RECIPES §1–§6 L34–1654 | — |
| which generator · [10] | DATA_BLANKS §11 L398–415 | DATA_OTHER §7 L371–436 | DATA_OTHER §6 L325–370 |
| rights before release · [11] | DATA_BLANKS §12 L416–436 | DATA_LEGAL §1–§2 L44–161 · DATA_LEGAL §10–§11 L437–496 | DATA_SUNO §12 L768–835 |
| fix a prompt · [12] | DATA_BLANKS §13 L437–460 | CORE_03 §0 L34–69 · CORE_03 §2–§3 L108–515 · CORE_03 §5 L575–810 · CORE_03 §8 L921–928 | 12b DATA_SUNO_LIVE §5 L249–276 |
| after the take · [13] | DATA_BLANKS §14 L461–482 | DATA_POSTPROD §2 L65–157 · DATA_POSTPROD §4 L214–265 · DATA_POSTPROD §7 L427–470 · DATA_POSTPROD §9 L505–550 | DATA_SUNO §9–§10 L656–746 |
| speech · [14] | DATA_BLANKS §15 L483–512 | CORE_02 §16 L998–1045 | DATA_SUNO §15 L934–976 |
| Suno + MCP, your songs · [15] · `mcp-menu` | DATA_BLANKS §16 L513–603 | DATA_SUNO_LIVE §7 · MCP MENU L382–408 the hub · DATA_SUNO_LIVE §7 · MY SONGS L409–435 and DATA_SUNO_LIVE §7 · SONG ACTIONS L436–480 when songs are asked for · DATA_SUNO_LIVE §9 L563–639 | CORE_00 §6 · LIVE L470–520 · CORE_00 §6 · CONNECTIONS L521–536 |
| an edit in plain words ("slower", "younger voice") | — | CORE_03 §0 L34–69 → CORE_03 §3 L223–515 or CORE_03 §5 L575–810 · the layer in CORE_01 | DATA_VOCAB §12 L795–835 |
| "surprise me" | — | CORE_01 §10–§11 L737–900 · CORE_02 §5–§6 L324–469 · CORE_02 §10–§11 L678–799 | DATA_VOCAB §6 L313–480 |
| the user's own lyrics | — | CORE_02 §1 L30–91 · CORE_02 §13 L866–927 — format, never rewrite (CORE_00 §7 L586–664 rule 9a) | — |
| "why this rule?" | — | CORE_04 §1–§3 L34–617 (on request) | — |
| "what is free?" | — | DATA_OTHER §6 L325–370 (on request) | — |

</section>

<section id="§4" title="QUESTIONS → SECTIONS">

| The user asks | Go to |
|---|---|
| "which Suno model?" / "what is v6-wild?" | DATA_SUNO §1 L44–113 |
| "what is Max Mode?" / "does MAX MODE work?" | DATA_SUNO §4 L240–338 · CORE_03 §3 L223–515 |
| "why was my style rewritten?" | DATA_SUNO §4 L240–338 (Variety) |
| "change the chorus / one line of a finished song" | DATA_SUNO §7 L430–597 · CORE_02 §2 L92–163 |
| "how long can a song be?" | DATA_SUNO §4 L240–338 · DATA_GOOGLE §4 L252–316 · DATA_OTHER §1–§3 L38–251 |
| "how many credits does a call cost?" / "why two songs?" | DATA_SUNO_LIVE §3–§4 L130–248 |
| "what can the Suno connector do?" | DATA_SUNO_LIVE §9 L563–639 |
| "stems?" | DATA_SUNO §10 L708–746 · DATA_POSTPROD §4 L214–265 |
| "my own voice?" | DATA_SUNO §5 L339–397 · DATA_LEGAL §3 L162–191 |
| "can I use it commercially?" / "can my Free song become commercial?" | DATA_SUNO §12 L768–835 · DATA_LEGAL §2 L80–161 |
| "what can I do for free?" | DATA_OTHER §6 L325–370 |
| "it sounds muffled / cuts off / ignores my tags / talks in the intro" | CORE_03 §0 L34–69 · CORE_03 §5 L575–810 |
| "a pause where the parts join" / "how do I join two parts or genres" | DATA_SUNO §7 L430–597 · CORE_03 §5 L575–810 · DATA_POSTPROD §6 L331–426 |
| "how loud for Spotify?" | DATA_POSTPROD §9 L505–550 |
| "a Lyria / Gemini song" | DATA_GOOGLE §3–§5 L147–388 |

</section>

<section id="§5" title="SECTION MAP — every section of every file, with its lines">

- `CORE_00_ENTRY.md` (901 lines): §0 SYSTEM MAP L64–88 · §1 IDENTITY L89–126 · §2 CONFIDENCE MARKING L127–166 · §3 CREATIVE PHILOSOPHY L167–202 · §4 MAIN MENU L203–304 · §5 ROUTING DISPATCH L305–364 · §6 OUTPUT PROTOCOL L365–585 · §6 · SUNO v6 L367 · §6 · SUNO v6 EDIT L435 · §6 · SUNO SPEECH L450 · §6 · LIVE L470 · §6 · CONNECTIONS L521 · §6 · LYRIA 3.5 / 3 CLIP L537 · §6 · GOOGLE FLOW MUSIC L562 · §6 · ELEVENMUSIC L571 · §6 · STABLE AUDIO 3.0 L574 · §6 · MINIMAX MUSIC 3.0 / LOCAL MODELS L577 · §6 · DUAL / ALL L580 · §7 CRITICAL RULES L586–664 · §8 LAYERS AND UPDATE POLICY L665–678 · §9 STARTUP BEHAVIOR L679–866 · §10 MIGRATION FROM v4.0, v3.0, v2.0 AND v1.1 L867–897
- `CORE_01_STYLE.md` (1081 lines): §1 THE SIX-LAYER FRAMEWORK L29–117 · §2 ONE FRAMEWORK, FOUR VENDOR GUIDES L118–183 · §3 TIME & PLACE L184–264 · §4 MOOD & ENERGY L265–328 · §5 INSTRUMENTATION L329–378 · §6 VOCAL DIRECTION L379–449 · §7 VOICES AND PERSONAS L450–634 · §8 STRUCTURE L635–669 · §9 PRODUCTION SIGNATURE L670–736 · §10 HYBRID LAB L737–843 · §11 ATMOSPHERE AND SCENE L844–900 · §12 CLONE A STYLE L901–966 · §13 ASSEMBLY L967–1051 · §14 CHECKLIST L1052–1077
- `CORE_02_LYRICS.md` (1049 lines): §1 THE BRACKET RULE L30–91 · §2 TWO PATHS L92–163 · §3 SECTION LABELS L164–224 · §4 HOW MUCH TO PUT IN A LABEL L225–323 · §5 PERFORMANCE NOTATION L324–385 · §6 DELIVERY AND EMOTION L386–469 · §7 AD-LIBS AND BACKING VOCALS L470–529 · §8 SPOKEN WORD L530–580 · §9 DUET AND MULTI-VOICE L581–677 · §10 CHORDS L678–741 · §11 ATMOSPHERE AT SECTION LEVEL L742–799 · §12 STRUCTURE TEMPLATES L800–865 · §13 THE TOP OF THE LYRICS FIELD L866–927 · §14 OTHER PLATFORMS L928–976 · §15 CHECKLIST L977–997 · §16 SCRIPTS FOR SUNO SPEECH L998–1045
- `CORE_03_DIAGNOSE.md` (932 lines): §0 SYMPTOM INDEX L34–69 · §1 WHAT AUDIT IS FOR L70–107 · §2 THE DIAGNOSTIC PROTOCOL L108–222 · §3 THE REPAIR TABLE L223–515 · §4 TRIGGER WORDS L516–574 · §5 FAILURE MODES L575–810 · §6 WHAT IS NOT A DEFECT L811–846 · §7 PLATFORM-SPECIFIC PROBLEMS L847–920 · §8 FAST TRIAGE L921–928
- `CORE_04_WHY.md` (754 lines): §1 THE CRITICAL RULES L34–374 · §2 TECHNIQUES L375–482 · §3 THE ARCHITECTURE L483–617 · §4 WHY THINGS WERE REMOVED L618–724 · §5 IF YOU ONLY REMEMBER FIVE THINGS L725–750
- `DATA_BLANKS.md` (607 lines): §1 HOW A BLANK IS SHOWN L31–58 · §2 [1] QUICK START L59–89 · §3 [2] STUDIO L90–145 · §4 [3] CLONE A STYLE L146–204 · §5 [4] HYBRID LAB L205–230 · §6 [5] VOICES L231–280 · §7 [6] LYRICS AND MARKUP L281–326 · §8 [7] OTHER GENERATORS L327–368 · §9 [8] ONE IDEA, SEVERAL GENERATORS L369–381 · §10 [9] RECIPES L382–397 · §11 [10] WHICH GENERATOR L398–415 · §12 [11] RIGHTS BEFORE RELEASE L416–436 · §13 [12] FIX A PROMPT L437–460 · §14 [13] AFTER THE TAKE L461–482 · §15 [14] SPEECH L483–512 · §16 [15] SUNO + MCP L513–603
- `DATA_GOOGLE_2026-10.md` (665 lines): §1 THE LYRIA FAMILY L51–126 · §2 SURFACES L127–146 · §3 PROMPTING LYRIA 3.5 L147–251 · §4 STRUCTURE AND TIMING L252–316 · §5 VOCALS AND LYRICS L317–388 · §6 MULTIMODAL INPUT L389–414 · §7 GOOGLE FLOW MUSIC L415–482 · §8 LYRIA REALTIME L483–506 · §9 RETIRED AND CONSOLIDATED L507–522 · §10 CHOOSING WITHIN THE GOOGLE FAMILY L523–555 · §11 WORKED EXAMPLES L556–660
- `DATA_LEGAL_2026-10.md` (500 lines): §1 THE DISTINCTION EVERYTHING ELSE DEPENDS ON L44–79 · §2 WHERE EACH PLATFORM STANDS L80–161 · §3 UPLOADING YOUR VOICE L162–191 · §4 TRAINING A MODEL ON YOUR CATALOGUE L192–224 · §5 STREAMING, DISTRIBUTION AND PLATFORM POLICIES L225–295 · §6 LITIGATION L296–352 · §7 THE UDIO CASE L353–382 · §8 WATERMARKING AND PROVENANCE L383–410 · §9 REGULATION L411–436 · §10 WHEN TO RAISE A WARNING L437–471 · §11 A CHECKLIST BEFORE RELEASE L472–496
- `DATA_OTHER_2026-10.md` (664 lines): §1 ELEVENMUSIC L38–145 · §2 STABLE AUDIO 3.0 L146–202 · §3 MINIMAX MUSIC 3.0 L203–251 · §4 AGGREGATORS AND REGIONAL ACCESS L252–281 · §5 LOCAL OPEN MODELS L282–324 · §6 WHAT YOU CAN DO WITHOUT A PAID PLAN L325–370 · §7 WHICH GENERATOR L371–436 · §8 PLATFORMS DELIBERATELY NOT COVERED L437–465 · §9 WORKED EXAMPLES L466–530 · §10 WHAT TRANSFERS BETWEEN PLATFORMS L531–559 · §11 ONE IDEA, EVERY PLATFORM L560–659
- `DATA_POSTPROD.md` (677 lines): §1 SHOULD YOU PROCESS THIS AT ALL? L27–64 · §2 THE MASTERING CHAIN L65–157 · §3 WHAT NOT TO DO L158–213 · §4 STEMS L214–265 · §5 PROCESSING INDIVIDUAL STEMS L266–330 · §6 EDITING ENVIRONMENTS L331–426 · §7 HANDING OFF TO A DAW L427–470 · §8 RESTORATION L471–504 · §9 LOUDNESS AND DELIVERY L505–550 · §10 MOVING MATERIAL BETWEEN PLATFORMS L551–600 · §11 THREE WALKTHROUGHS L601–673
- `DATA_RECIPES.md` (1729 lines): §1 HOW TO READ A RECIPE L34–83 · §2 CORE GENRE RECIPES L84–1097 · §3 HYBRID RECIPES L1098–1304 · §4 DUET L1305–1357 · §5 STYLE PRESETS L1358–1475 · §6 TASK SCENARIOS L1476–1654 · §7 ONE IDEA, EVERY PLATFORM L1655–1664 · §8 BUILDING YOUR OWN LIBRARY L1665–1725
- `DATA_SUNO_2026-10.md` (1064 lines): §1 VERSION MATRIX L44–113 · §2 THE STYLE FIELD L114–165 · §3 EXCLUDE STYLES L166–239 · §4 MAX MODE, VARIETY AND DURATION L240–338 · §5 VOICES L339–397 · §6 CUSTOM MODELS L398–429 · §7 EDITING, REMIXING AND REFERENCES ON v6 L430–597 · §8 SLIDERS L598–655 · §9 SUNO STUDIO 2.0 L656–707 · §10 STEM SEPARATION L708–746 · §11 LYRICS EDITOR L747–767 · §12 PLANS L768–835 · §13 WHAT SHIPPED L836–881 · §14 MYTHS L882–933 · §15 SPEECH (beta) L934–976 · §16 SUNO MCP AND THE SUNO API L977–1041 · §17 SHARING L1042–1060
- `DATA_SUNO_LIVE_2026-10.md` (643 lines): §1 TOOLS L38–82 · §2 FIELD MAP L83–129 · §3 DEFAULTS AND TRAPS L130–222 · §4 PLAN GATING L223–248 · §5 READ BACK L249–276 · §6 PRE-FLIGHT AND AUTO-RECOVERY L277–340 · §7 CHAINS, PANEL AND CARDS L341–542 · §8 NOT KNOWN L543–562 · §9 CAPABILITIES L563–639
- `DATA_VOCAB.md` (839 lines): §1 HOW TO USE THIS L34–65 · §2 TIMBRE L66–135 · §3 DYNAMICS L136–194 · §4 GROOVE L195–257 · §5 SPACE L258–312 · §6 INSTRUMENT DESCRIPTORS L313–480 · §7 PRODUCTION AND MIX CHARACTER L481–538 · §8 KEY AND TEMPO L539–601 · §9 MODES AND SCALES L602–639 · §10 THEORY → PROMPT LANGUAGE, BY GENRE L640–747 · §11 INSTRUMENT NAMES L748–794 · §12 PUTTING WORDS TOGETHER L795–835

</section>

// ═══════════════════════════════════════════════════════════════
// END OF INDEX.md · SunoForge v5.0
// Generated at build from build/index/INDEX.src.md — edit the source, not this file
// ═══════════════════════════════════════════════════════════════
</sunoforge_file>
