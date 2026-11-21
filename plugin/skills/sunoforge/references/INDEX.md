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
updated: "2026-11-20"
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
1 INTAKE    a menu pick shows the entry's blank — DATA_BLANKS §1 L31–79 and its § in §3 below; a
            concrete task fills the slots silently; the settings are the preloader of CORE_00
            and the user's settings file (already read)
2 DECIDE    how many readings (VARIANT_COUNT) and how far apart — CORE_00 §3 L169–204; no platform
            named → TARGET_PLATFORM, else the auto-detect of CORE_00 §5 L322–390; the CHOOSE row of
            §2 only for [10] or "which generator"
3 METHOD    the task's sections — §3 below (CORE_01 for sound, CORE_02 for words)
4 DIALECT   the platform's sections — §2 below: its fields, limits, what it rewrites, its traps
5 WORDS     the exact descriptor — DATA_VOCAB §1 L34–65 then the matching §; a genre, preset or
            task that matches a recipe — DATA_RECIPES §1 L34–83 then §2–§6
6 WRITE     the RESULT FRAME and the platform's block — CORE_00 §6 L391–626
7 CHECK     before delivery — CORE_01 §14 L1070–1095 (style) · CORE_02 §15 L977–997 (lyrics) · the checks of
            CORE_03 §2 L108–222 that apply to the platform · CORE_00 §7 L627–705 critical rules
8 SEND      only with a generator server in the session and the user's yes —
            DATA_SUNO_LIVE §6 L366–457 pre-flight → DATA_SUNO_LIVE §7 · PRICE CARD L687–706 card → CORE_00 §6 · LIVE L511–561
9 AFTER     the take — DATA_SUNO_LIVE §5 L335–365 read back → CORE_03 §0 L34–69 symptom index → the
            next blueprint
```
Steps 2, 6 and 7 happen on every prompt, step 1 on a menu pick; 3–5 by the rows below; 8–9 only
with a server.

</section>

<section id="§2" title="PLATFORM PROFILES — the dialect of each generator">

| Platform (TARGET_PLATFORM) | Facts, fields, limits | Lyrics and structure | Output block | Traps and repairs | Rights |
|---|---|---|---|---|---|
| Suno v6 — `suno` (default) | DATA_SUNO §1 L44–113 models · DATA_SUNO §2 · PRACTICAL SHAPE L148–165 Style field · DATA_SUNO §3 · HOW TO WRITE IT L202–239 Exclude and ready lists · DATA_SUNO §4 L240–338 Max Mode, Variety, duration (the evidence above each rule: DATA_SUNO §2–§3 L114–239, on "why") · DATA_SUNO §8 L600–657 sliders | CORE_02 §1–§2 L30–163 · CORE_02 §13 L866–927 | CORE_00 §6 · SUNO v6 L393–475 | CORE_03 §7 L849–922 · DATA_SUNO §14 L891–942 myths | DATA_SUNO §12 L775–842 |
| Suno v6 edit of a finished song | DATA_SUNO §7 L430–599 · DATA_SUNO §11 L754–774 lyrics editor | CORE_02 §2 L92–163 | CORE_00 §6 · SUNO v6 EDIT L476–490 | CORE_03 §7 L849–922 | DATA_SUNO §12 L775–842 |
| Suno Voices, Custom Models | DATA_SUNO §5–§6 L339–429 | — | CORE_00 §6 · SUNO v6 L393–475 | — | DATA_LEGAL §3–§4 L162–224 (on request) |
| Suno Speech — `speech` | DATA_SUNO §15 L943–985 | CORE_02 §16 L998–1045 | CORE_00 §6 · SUNO SPEECH L491–510 | DATA_SUNO_LIVE §3 L166–305 (Tone rewritten) | DATA_SUNO §12 L775–842 |
| Suno through the MCP (LIVE) | DATA_SUNO_LIVE §1–§4 L45–334 tools, field map, traps, plan gating · DATA_SUNO_LIVE §9 L753–838 capabilities | as for Suno v6 | CORE_00 §6 · LIVE L511–561 · DATA_SUNO_LIVE §7 · PRICE CARD L687–706 card | DATA_SUNO_LIVE §6 L366–457 pre-flight and recovery | DATA_SUNO §16 L986–1050 |
| Suno Studio, stems | DATA_SUNO §9–§10 L658–753 | — | — | — | DATA_SUNO §12 L775–842 |
| Lyria 3.5 / Clip — `lyria` | DATA_GOOGLE §1 L51–126 · DATA_GOOGLE §3 L147–251 Google's guide | DATA_GOOGLE §4–§5 L252–388 · CORE_02 §14 L928–976 | CORE_00 §6 · LYRIA 3.5 / 3 CLIP L578–602 | CORE_03 §7 L849–922 | DATA_LEGAL §2 L80–161 (on request) |
| Lyria from a photo or a video | DATA_GOOGLE §6 L389–414 | DATA_GOOGLE §4 L252–316 timing | CORE_00 §6 · LYRIA 3.5 / 3 CLIP L578–602 | — | — |
| Lyria RealTime | DATA_GOOGLE §8 L483–506 | — | CORE_00 §6 · LYRIA 3.5 / 3 CLIP L578–602 | — | — |
| Gemini app | DATA_GOOGLE §2 L127–146 · DATA_GOOGLE §10 L523–555 | DATA_GOOGLE §5 L317–388 | CORE_00 §6 · LYRIA 3.5 / 3 CLIP L578–602 | — | — |
| Google Flow Music — `flow` | DATA_GOOGLE §7 L415–482 | DATA_GOOGLE §5 L317–388 | CORE_00 §6 · GOOGLE FLOW MUSIC L603–611 | — | — |
| ElevenMusic — `eleven` | DATA_OTHER §1 L38–145 (on request) | CORE_02 §14 L928–976 | CORE_00 §6 · ELEVENMUSIC L612–614 | CORE_03 §7 L849–922 | DATA_OTHER §1 L38–145 |
| Stable Audio — `stable` | DATA_OTHER §2 L146–202 (on request) | — | CORE_00 §6 · STABLE AUDIO 3.0 L615–617 | — | DATA_OTHER §2 L146–202 |
| MiniMax, local models — `minimax`, `local` | DATA_OTHER §3 L203–251 · DATA_OTHER §5 L282–324 (on request) | CORE_02 §14 L928–976 | CORE_00 §6 · MINIMAX MUSIC 3.0 / LOCAL MODELS L618–620 | — | DATA_OTHER §5 L282–324 |
| Several at once — `dual`, `all` | DATA_OTHER §10–§11 L531–659 · DATA_RECIPES §7 L1655–1664 | each platform's own | CORE_00 §6 · DUAL / ALL L621–626 | — | — |
| CHOOSE — no platform named | CORE_00 §3 L169–204 platform rule · DATA_OTHER §7 L371–436 decision tree · DATA_OTHER §6 L325–370 free plans | — | — | — | — |

Every platform also takes the sound method of CORE_01 §2 L136–201, which lines the six layers up
with each vendor's own guide.

</section>

<section id="§3" title="TASKS AND MENU CODES — the method">

| Task, code | The blank | Method sections | Also |
|---|---|---|---|
| a song from an idea · [1] | DATA_BLANKS §2 L80–110 | CORE_01 §1 L29–135 six layers · CORE_01 §3 L202–282 time and place · CORE_01 §13 L985–1069 assembly | DATA_RECIPES §2 L84–1097 when the genre matches |
| studio by hand · [2] | DATA_BLANKS §3 L111–166 | 2a CORE_01 §3–§4 L202–346 · 2b CORE_01 §5 L347–396 · 2c CORE_01 §6 L397–467 · 2d DATA_VOCAB §8 L539–601 · 2e CORE_01 §9 L688–754 · 2f CORE_01 §8 L653–687, CORE_02 §12 L800–865 | 2g DATA_SUNO §8 L600–657 · 2h DATA_SUNO §3 L166–239 · 2i DATA_SUNO §7 L430–599 · 2j, 2k DATA_SUNO §4 L240–338 |
| clone a style · [3] | DATA_BLANKS §4 L167–226 | CORE_01 §12 L919–984 · DATA_VOCAB §2–§5 L66–312 | 3d–3g DATA_SUNO §7 L430–599 |
| hybrid · [4] | DATA_BLANKS §5 L227–252 | CORE_01 §10 L755–861 | DATA_RECIPES §3 L1098–1304 |
| voices, personas · [5] | DATA_BLANKS §6 L253–302 | CORE_01 §6–§7 L397–652 · 5c CORE_02 §9 L581–677 · 5d CORE_02 §6 L386–469 | 5e DATA_SUNO §5 L339–397 · 5f DATA_SUNO §6 L398–429 · 5g DATA_GOOGLE §5 L317–388 |
| lyrics and markup · [6] | DATA_BLANKS §7 L303–348 | CORE_02 §1–§4 L30–323 · CORE_02 §12–§13 L800–927 · 6c CORE_02 §5–§6 L324–469 · 6d CORE_02 §10 L678–741 · 6e CORE_02 §7–§8 L470–580 | 6f DATA_SUNO §11 L754–774 · 6g DATA_SUNO §7 L430–599 · 6h CORE_02 §14 L928–976 |
| another generator · [7] | DATA_BLANKS §8 L349–390 | the platform's row of §2 | — |
| one idea, several generators · [8] | DATA_BLANKS §9 L391–403 | DATA_OTHER §10–§11 L531–659 | DATA_RECIPES §7 L1655–1664 |
| recipes · [9] | DATA_BLANKS §10 L404–420 | DATA_RECIPES §1–§6 L34–1654 | — |
| which generator · [10] | DATA_BLANKS §11 L421–438 | DATA_OTHER §7 L371–436 | DATA_OTHER §6 L325–370 |
| rights before release · [11] | DATA_BLANKS §12 L439–459 | DATA_LEGAL §1–§2 L44–161 · DATA_LEGAL §10–§11 L437–496 | DATA_SUNO §12 L775–842 |
| fix and check · [12] | DATA_BLANKS §13 L460–486 | CORE_03 §0 L34–69 · CORE_03 §2–§3 L108–515 · CORE_03 §5 L575–812 · CORE_03 §8 L923–930 | 12b DATA_SUNO_LIVE §5 L335–365 |
| after the take · [13] | DATA_BLANKS §14 L487–511 | DATA_POSTPROD §2 L65–157 · DATA_POSTPROD §4 L214–267 · DATA_POSTPROD §7 L429–472 · DATA_POSTPROD §9 L507–552 | DATA_SUNO §9–§10 L658–753 |
| speech · [14] | DATA_BLANKS §15 L512–541 | CORE_02 §16 L998–1045 | DATA_SUNO §15 L943–985 |
| My Suno, your songs · [15] · `mcp-menu` | DATA_BLANKS §16 L542–664 | DATA_SUNO_LIVE §7 · MCP MENU L522–574 the hub · DATA_SUNO_LIVE §7 · MY SONGS L575–608 and DATA_SUNO_LIVE §7 · SONG ACTIONS L609–657 when songs are asked for · DATA_SUNO_LIVE §9 L753–838 | CORE_00 §6 · LIVE L511–561 · CORE_00 §6 · CONNECTIONS L562–577 |
| stems, MIDI, publish · `15p` `15q` `15r` | DATA_BLANKS §16 L542–664 | DATA_SUNO_LIVE §3 L166–305 · DATA_SUNO_LIVE §7 · CHAINS L459–521 · DATA_SUNO_LIVE §6 L366–457 | DATA_SUNO §10 L710–753 · DATA_POSTPROD §4 L214–267 |
| a song from the user's own melody (LAB) · [16] · `15q` | DATA_BLANKS §17 L665–691 · DATA_BLANKS §16 L542–664 | DATA_SUNO_LIVE §2 L103–165 · DATA_SUNO_LIVE §3 L166–305 · `scripts/README.md` | DATA_SUNO §7 L430–599 MIDI as a Create input |
| change a finished song (words, a part, an instrument) · `15m … replace` | DATA_BLANKS §16 L542–664 | DATA_SUNO_LIVE §2 L103–165 · DATA_SUNO_LIVE §7 · CREATE AND EDITOR L658–686 | DATA_SUNO §7 L430–599 |
| an edit in plain words ("slower", "younger voice") | — | CORE_03 §0 L34–69 → CORE_03 §3 L223–515 or CORE_03 §5 L575–812 · the layer in CORE_01 | DATA_VOCAB §12 L795–835 |
| "surprise me" | — | CORE_01 §10–§11 L755–918 · CORE_02 §5–§6 L324–469 · CORE_02 §10–§11 L678–799 | DATA_VOCAB §6 L313–480 |
| the user's own lyrics | — | CORE_02 §1 L30–91 · CORE_02 §13 L866–927 — format, never rewrite (CORE_00 §7 L627–705 rule 9a) | — |
| "why this rule?" | — | CORE_04 §1–§3 L34–617 (on request) | — |
| "what is free?" | — | DATA_OTHER §6 L325–370 (on request) | — |

</section>

<section id="§4" title="QUESTIONS → SECTIONS">

| The user asks | Go to |
|---|---|
| "which Suno model?" / "what is v6-wild?" | DATA_SUNO §1 L44–113 |
| "what is Max Mode?" / "does MAX MODE work?" | DATA_SUNO §4 L240–338 · CORE_03 §3 L223–515 |
| "why was my style rewritten?" | DATA_SUNO §4 L240–338 (Variety) |
| "change the chorus / one line of a finished song" | DATA_SUNO_LIVE §2 L103–165 · DATA_SUNO §7 L430–599 · CORE_02 §2 L92–163 |
| "how long can a song be?" | DATA_SUNO §4 L240–338 · DATA_GOOGLE §4 L252–316 · DATA_OTHER §1–§3 L38–251 |
| "how many credits does a call cost?" / "why two songs?" | DATA_SUNO_LIVE §3–§4 L166–334 |
| "what can the Suno connector do?" | DATA_SUNO_LIVE §9 L753–838 |
| "what does this Suno tool do, cost, return?" | DATA_SUNO_LIVE §10 L839–891 |
| "self-check" / «самодиагностика» — is my copy whole? | CORE_00 §5 L322–390 (the SELF-CHECK row; `commands/self-check.md`) |
| "stems?" | DATA_SUNO §10 L710–753 · DATA_POSTPROD §4 L214–267 · DATA_SUNO_LIVE §3 L166–305 |
| "MIDI?" / "can Suno play my melody?" / "publish it?" | DATA_SUNO_LIVE §3 L166–305 · DATA_SUNO_LIVE §9 L753–838 |
| "my own voice?" | DATA_SUNO §5 L339–397 · DATA_LEGAL §3 L162–191 |
| "can I use it commercially?" / "can my Free song become commercial?" | DATA_SUNO §12 L775–842 · DATA_LEGAL §2 L80–161 |
| "what can I do for free?" | DATA_OTHER §6 L325–370 |
| "it sounds muffled / cuts off / ignores my tags / talks in the intro" | CORE_03 §0 L34–69 · CORE_03 §5 L575–812 |
| "a pause where the parts join" / "how do I join two parts or genres" | DATA_SUNO §7 L430–599 · CORE_03 §5 L575–812 · DATA_POSTPROD §6 L333–428 |
| "how loud for Spotify?" | DATA_POSTPROD §9 L507–552 |
| "a Lyria / Gemini song" | DATA_GOOGLE §3–§5 L147–388 |

</section>

<section id="§5" title="SECTION MAP — every section of every file, with its lines">

- `CORE_00_ENTRY.md` (959 lines): §0 SYSTEM MAP L66–90 · §1 IDENTITY L91–128 · §2 CONFIDENCE MARKING L129–168 · §3 CREATIVE PHILOSOPHY L169–204 · §4 MAIN MENU L205–321 · §5 ROUTING DISPATCH L322–390 · §6 OUTPUT PROTOCOL L391–626 · §6 · SUNO v6 L393 · §6 · SUNO v6 EDIT L476 · §6 · SUNO SPEECH L491 · §6 · LIVE L511 · §6 · CONNECTIONS L562 · §6 · LYRIA 3.5 / 3 CLIP L578 · §6 · GOOGLE FLOW MUSIC L603 · §6 · ELEVENMUSIC L612 · §6 · STABLE AUDIO 3.0 L615 · §6 · MINIMAX MUSIC 3.0 / LOCAL MODELS L618 · §6 · DUAL / ALL L621 · §7 CRITICAL RULES L627–705 · §8 LAYERS AND UPDATE POLICY L706–719 · §9 STARTUP BEHAVIOR L720–924 · §10 MIGRATION FROM v4.0, v3.0, v2.0 AND v1.1 L925–955
- `CORE_01_STYLE.md` (1099 lines): §1 THE SIX-LAYER FRAMEWORK L29–135 · §2 ONE FRAMEWORK, FOUR VENDOR GUIDES L136–201 · §3 TIME & PLACE L202–282 · §4 MOOD & ENERGY L283–346 · §5 INSTRUMENTATION L347–396 · §6 VOCAL DIRECTION L397–467 · §7 VOICES AND PERSONAS L468–652 · §8 STRUCTURE L653–687 · §9 PRODUCTION SIGNATURE L688–754 · §10 HYBRID LAB L755–861 · §11 ATMOSPHERE AND SCENE L862–918 · §12 CLONE A STYLE L919–984 · §13 ASSEMBLY L985–1069 · §14 CHECKLIST L1070–1095
- `CORE_02_LYRICS.md` (1049 lines): §1 THE BRACKET RULE L30–91 · §2 TWO PATHS L92–163 · §3 SECTION LABELS L164–224 · §4 HOW MUCH TO PUT IN A LABEL L225–323 · §5 PERFORMANCE NOTATION L324–385 · §6 DELIVERY AND EMOTION L386–469 · §7 AD-LIBS AND BACKING VOCALS L470–529 · §8 SPOKEN WORD L530–580 · §9 DUET AND MULTI-VOICE L581–677 · §10 CHORDS L678–741 · §11 ATMOSPHERE AT SECTION LEVEL L742–799 · §12 STRUCTURE TEMPLATES L800–865 · §13 THE TOP OF THE LYRICS FIELD L866–927 · §14 OTHER PLATFORMS L928–976 · §15 CHECKLIST L977–997 · §16 SCRIPTS FOR SUNO SPEECH L998–1045
- `CORE_03_DIAGNOSE.md` (934 lines): §0 SYMPTOM INDEX L34–69 · §1 WHAT AUDIT IS FOR L70–107 · §2 THE DIAGNOSTIC PROTOCOL L108–222 · §3 THE REPAIR TABLE L223–515 · §4 TRIGGER WORDS L516–574 · §5 FAILURE MODES L575–812 · §6 WHAT IS NOT A DEFECT L813–848 · §7 PLATFORM-SPECIFIC PROBLEMS L849–922 · §8 FAST TRIAGE L923–930
- `CORE_04_WHY.md` (754 lines): §1 THE CRITICAL RULES L34–374 · §2 TECHNIQUES L375–482 · §3 THE ARCHITECTURE L483–617 · §4 WHY THINGS WERE REMOVED L618–724 · §5 IF YOU ONLY REMEMBER FIVE THINGS L725–750
- `DATA_BLANKS.md` (695 lines): §1 HOW A BLANK IS SHOWN L31–79 · §2 [1] QUICK START L80–110 · §3 [2] STUDIO L111–166 · §4 [3] CLONE A STYLE L167–226 · §5 [4] HYBRID LAB L227–252 · §6 [5] VOICES L253–302 · §7 [6] LYRICS AND MARKUP L303–348 · §8 [7] OTHER GENERATORS L349–390 · §9 [8] ONE IDEA, SEVERAL GENERATORS L391–403 · §10 [9] RECIPES L404–420 · §11 [10] WHICH GENERATOR L421–438 · §12 [11] RIGHTS BEFORE RELEASE L439–459 · §13 [12] FIX AND CHECK L460–486 · §14 [13] AFTER THE TAKE L487–511 · §15 [14] SPEECH L512–541 · §16 [15] MY SUNO L542–664 · §17 [16] LAB L665–691
- `DATA_GOOGLE_2026-10.md` (665 lines): §1 THE LYRIA FAMILY L51–126 · §2 SURFACES L127–146 · §3 PROMPTING LYRIA 3.5 L147–251 · §4 STRUCTURE AND TIMING L252–316 · §5 VOCALS AND LYRICS L317–388 · §6 MULTIMODAL INPUT L389–414 · §7 GOOGLE FLOW MUSIC L415–482 · §8 LYRIA REALTIME L483–506 · §9 RETIRED AND CONSOLIDATED L507–522 · §10 CHOOSING WITHIN THE GOOGLE FAMILY L523–555 · §11 WORKED EXAMPLES L556–660
- `DATA_LEGAL_2026-10.md` (500 lines): §1 THE DISTINCTION EVERYTHING ELSE DEPENDS ON L44–79 · §2 WHERE EACH PLATFORM STANDS L80–161 · §3 UPLOADING YOUR VOICE L162–191 · §4 TRAINING A MODEL ON YOUR CATALOGUE L192–224 · §5 STREAMING, DISTRIBUTION AND PLATFORM POLICIES L225–295 · §6 LITIGATION L296–352 · §7 THE UDIO CASE L353–382 · §8 WATERMARKING AND PROVENANCE L383–410 · §9 REGULATION L411–436 · §10 WHEN TO RAISE A WARNING L437–471 · §11 A CHECKLIST BEFORE RELEASE L472–496
- `DATA_OTHER_2026-10.md` (664 lines): §1 ELEVENMUSIC L38–145 · §2 STABLE AUDIO 3.0 L146–202 · §3 MINIMAX MUSIC 3.0 L203–251 · §4 AGGREGATORS AND REGIONAL ACCESS L252–281 · §5 LOCAL OPEN MODELS L282–324 · §6 WHAT YOU CAN DO WITHOUT A PAID PLAN L325–370 · §7 WHICH GENERATOR L371–436 · §8 PLATFORMS DELIBERATELY NOT COVERED L437–465 · §9 WORKED EXAMPLES L466–530 · §10 WHAT TRANSFERS BETWEEN PLATFORMS L531–559 · §11 ONE IDEA, EVERY PLATFORM L560–659
- `DATA_POSTPROD.md` (679 lines): §1 SHOULD YOU PROCESS THIS AT ALL? L27–64 · §2 THE MASTERING CHAIN L65–157 · §3 WHAT NOT TO DO L158–213 · §4 STEMS L214–267 · §5 PROCESSING INDIVIDUAL STEMS L268–332 · §6 EDITING ENVIRONMENTS L333–428 · §7 HANDING OFF TO A DAW L429–472 · §8 RESTORATION L473–506 · §9 LOUDNESS AND DELIVERY L507–552 · §10 MOVING MATERIAL BETWEEN PLATFORMS L553–602 · §11 THREE WALKTHROUGHS L603–675
- `DATA_RECIPES.md` (1729 lines): §1 HOW TO READ A RECIPE L34–83 · §2 CORE GENRE RECIPES L84–1097 · §3 HYBRID RECIPES L1098–1304 · §4 DUET L1305–1357 · §5 STYLE PRESETS L1358–1475 · §6 TASK SCENARIOS L1476–1654 · §7 ONE IDEA, EVERY PLATFORM L1655–1664 · §8 BUILDING YOUR OWN LIBRARY L1665–1725
- `DATA_SUNO_2026-10.md` (1073 lines): §1 VERSION MATRIX L44–113 · §2 THE STYLE FIELD L114–165 · §3 EXCLUDE STYLES L166–239 · §4 MAX MODE, VARIETY AND DURATION L240–338 · §5 VOICES L339–397 · §6 CUSTOM MODELS L398–429 · §7 EDITING, REMIXING AND REFERENCES ON v6 L430–599 · §8 SLIDERS L600–657 · §9 SUNO STUDIO 2.0 L658–709 · §10 STEM SEPARATION L710–753 · §11 LYRICS EDITOR L754–774 · §12 PLANS L775–842 · §13 WHAT SHIPPED L843–890 · §14 MYTHS L891–942 · §15 SPEECH (beta) L943–985 · §16 SUNO MCP AND THE SUNO API L986–1050 · §17 SHARING L1051–1069
- `DATA_SUNO_LIVE_2026-10.md` (895 lines): §1 TOOLS L45–102 · §2 FIELD MAP L103–165 · §3 DEFAULTS AND TRAPS L166–305 · §4 PLAN GATING L306–334 · §5 READ BACK L335–365 · §6 PRE-FLIGHT AND AUTO-RECOVERY L366–457 · §7 CHAINS, PANEL AND CARDS L458–727 · §8 NOT KNOWN L728–752 · §9 CAPABILITIES L753–838 · §10 EVERY TOOL ON ONE PAGE L839–891
- `DATA_VOCAB.md` (839 lines): §1 HOW TO USE THIS L34–65 · §2 TIMBRE L66–135 · §3 DYNAMICS L136–194 · §4 GROOVE L195–257 · §5 SPACE L258–312 · §6 INSTRUMENT DESCRIPTORS L313–480 · §7 PRODUCTION AND MIX CHARACTER L481–538 · §8 KEY AND TEMPO L539–601 · §9 MODES AND SCALES L602–639 · §10 THEORY → PROMPT LANGUAGE, BY GENRE L640–747 · §11 INSTRUMENT NAMES L748–794 · §12 PUTTING WORDS TOGETHER L795–835

</section>

// ═══════════════════════════════════════════════════════════════
// END OF INDEX.md · SunoForge v5.0
// Generated at build from build/index/INDEX.src.md — edit the source, not this file
// ═══════════════════════════════════════════════════════════════
</sunoforge_file>
