<sunoforge_file id="CORE_03_DIAGNOSE" version="4.0" layer="core" role="troubleshoot" source="CORE_03_DIAGNOSE.md">
<file_meta>
file_id: CORE_03_DIAGNOSE
version: "4.0"
layer: core
role: troubleshoot
description: >
  The engine behind menu [12] AUDIT and every "why does it sound like this": a symptom
  index, fifteen diagnostic checks, the repair table for dead and stale constructs
  (MAX tags, parametric tags, retired Suno models, old Lyria timestamp forms, prices),
  the single trigger-word list, failure modes including early Suno v6 reports, what is
  not a defect, and platform-specific problems. Read to fix or explain a prompt.
scope: audit_protocol · repair_engine · failure_modes · trigger_words · session_health · platform_troubleshoot
key_concepts: [audit_12, diagnostic_checks, repair_table, dead_constructs, migration_repair, failure_modes, hallucinations, trigger_words, long_track_consistency, session_health]
depends_on: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS]
used_by: [CORE_00_ENTRY, CORE_04_WHY, DATA_SUNO, DATA_GOOGLE, DATA_OTHER]
rag_priority: critical
authority: "THIS FILE IS THE SINGLE SOURCE FOR THE TRIGGER-WORD LIST"
updated: "2026-09-30"
changelog: "v4.0 — symptom index moved to the top (§0) · check 15 and repair rows 20–25 for retired Suno models, Lyria 3 Pro numbers, single-point Lyria markers, prices, Variety, Lyria lyrics without a header · row 11 retired: numeric BPM is right on Lyria now · MAX tags separated from the official Max Mode toggle · early v6 failure reports · v3.0 — repair engine for menu [12] rebuilt around dead constructs from CORE_00 §10 · trigger-word list consolidated here as the only copy · two-minute drift demoted from a diagnosis to an unverified belief · pipe-artifact section withdrawn · MAX MODE troubleshooting replaced with MAX MODE removal · Udio section replaced by retired-platform repairs"
</file_meta>

# 🩺 SUNOFORGE v4.0 — DIAGNOSE & REPAIR
# File 4 of 12 · CORE · The engine behind menu [12] AUDIT

> Menu entry **[12] AUDIT** per CORE_00 §4: the user pastes a prompt, gets a
> diagnosis and a repaired version. This file is that engine.
>
> 📌 **Single source.** The trigger-word list (§4) exists here and nowhere else.
> If you find it repeated in another file, that is a defect — delete the copy
> and link here.
>
> This file diagnoses **prompts**, not audio. It cannot hear the track. Every
> judgement below is made by reading text, which is why the failure modes in §5
> are matched by symptom description rather than by analysis.

<section id="§0" title="SYMPTOM INDEX — start here">

<!-- rag_anchor: symptom_index_table -->
<rag_zone id="triage_index">

| The user says | Go to |
|---|---|
| generic, boring, characterless | §5 · then CORE_01 §3 |
| wrong vocal gender | §5 · §3 row 8 |
| muddy, too many instruments | §2 check 3 |
| structure not followed | §5 · CORE_02 §3 |
| nonsense lyrics, missing words | §5 |
| unwanted talking or narration | §5 · §2 check 5 |
| vocals in an instrumental | §5 |
| loud finish nobody asked for | §5 |
| quality falling over a session | §5 |
| metallic ring on the high end | §5 |
| character fades later in the track | §5 — read the status note; Max Mode |
| "Suno changed / ignored my style text" | §3 row 24 (Variety) |
| muffled or buried vocals, humming before the first line, last line cut off (Suno v6) | §5 — early v6 reports |
| Suno sang a different lyric than I pasted | §5 · CORE_02 §2 (Simple mode) |
| Lyria sang my instructions | §3 row 25 |
| Lyria song ends early / the plan lost its ending | §7 · DATA_GOOGLE §4 |
| old prompt behaving oddly | §3 — run the whole table |
| prompt names v5.5, v4.5, Lyria 3 Pro | §3 rows 20, 22 |
| prompt aimed at the wrong platform | §2 check 12 · §3 rows 9–11, 21, 25 |
| a guide contradicts this system | §3 rows 16–19 · DATA_SUNO §14 |

</rag_zone>

</section>

<section id="§1" title="WHAT AUDIT IS FOR">

<!-- rag_anchor: audit_purpose -->
<rag_zone id="audit_purpose">

Three kinds of request arrive at [12], and they need different answers:

  "FIX THIS PROMPT"      → run §2, apply §3, return the repaired prompt
  "WHY DID I GET THIS?"  → §5, match the symptom, explain the cause
  "IS THIS STILL VALID?" → §3, check for dead constructs and retired platforms

The third is the most common in practice and the least often asked directly.
Prompts circulate. A prompt written a year ago still looks fine — the syntax
has not changed shape, it has simply stopped meaning anything. Nothing errors.
The track just comes out worse than it should, and there is no signal telling
the user why.

### THE TONE RULE

An audit repairs a prompt. It does not lecture the person who wrote it.

Most defects in circulating prompts came from guides that were confident and
wrong, including previous editions of this system. Say what changed and what to
write instead. Do not imply the user should have known.

  ✅  "The MAX tags don't do anything — they're text, not a setting. Suno's real
      Max Mode is a switch in the Create form. I've dropped the tags, put the
      quality intent into the description, and marked Max Mode on because this
      one runs past two minutes."
  ❌  "You're using outdated MAX MODE syntax, which has been debunked."

### WHAT NOT TO CHANGE

  - Creative choices. A strange genre pairing is not a defect (§6).
  - Anything working that is merely undocumented. Unproven is not broken.
  - The user's voice in the lyrics.
  - `///*****///` and other harmless remnants — say they do nothing, leave them
    if the user likes them.

</rag_zone>

</section>

<section id="§2" title="THE DIAGNOSTIC PROTOCOL — fifteen checks, in order">

<!-- rag_anchor: diagnostic_checks -->
<rag_zone id="diagnostic_checks">
Run in order. Earlier checks change what later checks are looking at.

### CHECK 1 · FRONT-LOADING
  Do the opening words name a specific subgenre?
  FAIL:  "a rock song with some grunge influence"
  FIX:   lead with the most specific thing — "mid-90s Seattle grunge"
  WHY:   the opening words carry the most weight (CORE_01 §1)

### CHECK 2 · GENRE COUNT
  More than two genres named?
  FIX:   keep one primary and one modifier. If the user wants a real blend,
         that is a hybrid and needs a bridge — CORE_01 §10

### CHECK 3 · INSTRUMENT COUNT
  More than three or four instruments listed?
  FIX:   cut to two or three hero instruments plus one texture word
  WHY:   an undifferentiated list produces an undifferentiated arrangement

</rag_zone>

<!-- rag_anchor: diagnostic_checks_check_4_mood_conflict -->
<rag_zone id="diagnostic_checks_check_4_mood_conflict">

### CHECK 4 · MOOD CONFLICT
  Contradictory moods, or more than two?
  FAIL:  "happy dark aggressive peaceful"
  FIX:   one or two that can coexist (CORE_01 §4)

### CHECK 5 · BRACKET VIOLATION
  Instructions inside round brackets?
  FAIL:  "(play the guitar softly here)"
  FIX:   move to square brackets, or delete if it was never performable
  WHY:   round brackets are sung — the model will sing the instruction

### CHECK 6 · PARAMETRIC CONSTRUCTS
  Any `[parameter: value]` forms?
  FIX:   rewrite as prose in Style; see the repair table §3
  NOTE:  this is the highest-volume defect in circulating prompts

</rag_zone>

<!-- rag_anchor: diagnostic_checks_check_7_genre_conflict -->
<rag_zone id="diagnostic_checks_check_7_genre_conflict">

### CHECK 7 · GENRE CONFLICT
  Is the pairing on the incompatible list?
  FIX:   name the conflict, offer the bridge genre
  WHERE: the compatibility table is menu [4c] — CORE_01 §10
  NOTE:  this is advice, not a blocker. Users may want the collision.

### CHECK 8 · FIELD MIX-UP
  Tempo, key, genre or production language sitting in the Lyrics field?
  Section structure sitting in the Style field?
  FIX:   swap them. Style describes the record; Lyrics places the events
         (CORE_01 §8, CORE_02 §13)

### CHECK 9 · VOCAL GENDER NEGATIVES
  "no male vocals", "not a female singer", or similar?
  FIX:   delete the negative, state the wanted voice positively in Layer 4,
         and point at the Vocal Gender control (DATA_SUNO §8)
  WHY:   naming a voice type to exclude it can summon it

</rag_zone>

<!-- rag_anchor: diagnostic_checks_check_10_trigger_words -->
<rag_zone id="diagnostic_checks_check_10_trigger_words">

### CHECK 10 · TRIGGER WORDS
  Any of the words in §4?
  FIX:   swap for the positive equivalent given there

### CHECK 11 · RETIRED PLATFORMS
  References to platforms that no longer serve this purpose?
  FIX:   repair table §3, rows 12–15 and 22

### CHECK 12 · PLATFORM SYNTAX MISMATCH
  Suno-only items aimed at Lyria — an exclude list, slider values, Variety, Max
  Mode, ~ or CAPS notation?
  Lyria timestamps in the old parenthetical or single-point form?
  Lyria lyrics mixed into the directions without a `Lyrics:` header?
  Tempo given only in words, with no BPM? (a suggestion, not a defect)
  FIX:   repair table §3, rows 9–11, 21 and 25

</rag_zone>

<!-- rag_anchor: diagnostic_checks_check_13_length_and_substance -->
<rag_zone id="diagnostic_checks_check_13_length_and_substance">

### CHECK 13 · LENGTH AND SUBSTANCE
  Is there enough lyric material for the intended track length?
  FIX:   add material, or shorten the target
  WHY:   a long target with thin material produces padding, aimless
         instrumental passages, or an abrupt cut (CORE_02 §12)

### CHECK 14 · MYTH DEPENDENCY
  Does the prompt rely on something that does not work?
  Does it show signs of having been cut to fit a limit that does not exist?
  FIX:   repair table §3, and say plainly what the evidence shows
  WHERE: the catalogue of debunked claims is DATA_SUNO §14

### CHECK 15 · STALE VERSIONS, NUMBERS AND PRICES
  Does the prompt or the guide it came from name a retired model (Suno v5.5,
  v5, v4.5-all; Lyria 3 Pro), quote its old limits (184 s, 48 kHz Clip, PDF
  input), or quote prices?
  FIX:   repair table §3, rows 20, 22 and 23
  WHY:   the text may still work; the label points at something that is gone

</rag_zone>

<!-- rag_anchor: diagnostic_checks_output_format -->
<rag_zone id="diagnostic_checks_output_format">

### OUTPUT FORMAT

```
🩺 AUDIT

WORKING
  ✅ Check 1 — front-loaded on a specific subgenre
  ✅ Check 4 — two compatible moods

NEEDS REPAIR
  ❌ Check 6 — three parametric tags; never parsed
  ❌ Check 9 — gender negative in Style; unreliable and can backfire
  ⚠️ Check 15 — names Suno v5.5, which is retired; target set to v6

REPAIRED VERSION
  [full output in the target platform's protocol — CORE_00 §6]

WHAT CHANGED AND WHY
  [one line per repair, in plain language]
```

Report what passed as well as what failed. A user who only sees failures cannot
tell which of their habits are good ones.

</rag_zone>

</section>

<section id="§3" title="THE REPAIR TABLE — dead constructs">

<!-- rag_anchor: repair_table -->
<rag_zone id="repair_table">
Every row: what to find, what to write instead, and what to tell the user.
This is the mechanical core of [12]. Rows 1–8 are syntax, 9–11 are
cross-platform, 12–15 are retired products, 16–19 are stale facts, 20–25 are the
v4.0 migrations (September 2026). Rows are numbered for reference; new rows go at
the end.

### 1 · MAX MODE TAGS
  FIND     [Is_MAX_MODE: MAX] · [QUALITY: MAX] · [REALISM: MAX]
           [REAL_INSTRUMENTS: MAX] · (MAX)(MAX)(MAX)(MAX)
  REPLACE  delete. If the user wanted a quality signal, express it as
           description: "studio-grade recording, detailed and dynamic"
  SAY      There is no hidden quality mode behind these tags. A controlled
           comparison found no difference beyond normal variation. The tags
           read as plain descriptive words, so removing them costs nothing.
           Since 2026-09-09 Suno has a REAL Max Mode — a switch in the Create
           form, for songs over two minutes, close covers, style transfer and
           whole-track consistency. The tags do not turn it on.
  THEN     for a long track or a release, set "Max Mode: on" in the blueprint
           and say that it costs more credits (DATA_SUNO §4)
  MARK     tags [UNVERIFIED] · origin: a single forum post · toggle [OFFICIAL]

</rag_zone>

<!-- rag_anchor: repair_table_2_the_slash_asterisk_separator -->
<rag_zone id="repair_table_2_the_slash_asterisk_separator">

### 2 · THE SLASH-ASTERISK SEPARATOR
  FIND     ///*****/// as the first line of the Lyrics field
  REPLACE  nothing. Leave it.
  SAY      It does nothing, and it does no harm. Keep it if you like it.

### 3 · MIX PARAMETER TAGS
  FIND     [eq: scooped] · [eq: midrange-clear] · [compression: heavy]
           [focus: bass] · [wide stereo field] · [Sidechain] · [Reverb: 30%]
  REPLACE  the same intent as prose inside Style:
           "scooped mids, heavily compressed, wide stereo, pumping sidechain"
  SAY      Bracketed mix parameters were never parsed. The same words work
           as ordinary description — that part was always doing the work.
  MARK     [UNVERIFIED]

</rag_zone>

<!-- rag_anchor: repair_table_4_musical_parameter_tags -->
<rag_zone id="repair_table_4_musical_parameter_tags">

### 4 · MUSICAL PARAMETER TAGS
  FIND     [BPM: 120] · [Tempo: 120 BPM] · [Key: A minor]
           [Chord progression: Am - F - C - G]
  REPLACE  in Style, as prose: "120 BPM, A minor"
           for chords, inline in the lyric: "(Am) the city sleeps"
  SAY      Same as above. The inline chord form is the one that works.
  WHERE    CORE_02 §10

### 5 · MOOD AND ENERGY TAGS
  FIND     [Mood: Uplifting] · [Energy: High] · [Energy: Low→High]
           [Atmosphere: Cyberpunk] · [Vibe: Midnight drive]
  REPLACE  in Style: "uplifting", "builds from near-silence to full force",
           "cyberpunk night city"
  SAY      Parametric form again. The words were carrying the meaning; the
           brackets and colon were not.

</rag_zone>

<!-- rag_anchor: repair_table_6_atmosphere_tags_with_a_colon -->
<rag_zone id="repair_table_6_atmosphere_tags_with_a_colon">

### 6 · ATMOSPHERE TAGS WITH A COLON
  FIND     [Sound: Rain] · [sound:thunder] · [Sound: City ambience]
  REPLACE  section-level: [Rain] · [Thunder] · [City ambience]
           track-level: describe it in Style — "with rain under the intro"
  SAY      Drop the "Sound:" prefix. The plain bracket is a section event,
           which is what you wanted.
  WHERE    CORE_02 §11

### 7 · VOCAL PARAMETER TAGS
  FIND     [Vocal Style: Raspy] · [Vocal: female] · [Choir: Gospel]
           [Persona: Pop Star]
  REPLACE  [Raspy lead vocal] · [Gospel choir] — or, better, a persona
           description in Style (CORE_01 §7)
  SAY      Delivery direction belongs in plain brackets; who is singing
           belongs in the Style field.

</rag_zone>

<!-- rag_anchor: repair_table_8_gender_negatives -->
<rag_zone id="repair_table_8_gender_negatives">

### 8 · GENDER NEGATIVES
  FIND     "no male vocals" · "without male voice" · "not a female singer"
           stacked gender exclusions of any kind
  REPLACE  a positive statement in Layer 4: "solo female vocalist, breathy
           soprano, intimate delivery" — plus the interface gender selector
  SAY      Gender negatives are unreliable and sometimes produce the opposite,
           because naming a voice type puts it in front of the model. The
           selector in Advanced Options is the reliable control.
  WHERE    DATA_SUNO §8 for the Vocal Gender control; §3 for Exclude Styles
  MARK     [COMMUNITY, widely reproduced]

</rag_zone>

<!-- rag_anchor: repair_table_9_lyria_structure_in_the_old_format -->
<rag_zone id="repair_table_9_lyria_structure_in_the_old_format">

### 9 · LYRIA STRUCTURE IN THE OLD FORMAT
  FIND     "Intro (0–15s)" · "[End - 2:15]" · "verse (15-45s)"
  REPLACE  timestamp ranges: `[0:00 - 0:15] Intro: what happens` and so on to
           the end — or section tags with arrows: `[Intro] -> [Verse 1] -> …`
  SAY      Google documents timestamps and section tags. The parenthetical form
           was our invention and it was wrong.
  MARK     [OFFICIAL] · full syntax in DATA_GOOGLE §4

### 10 · EXCLUDE LISTS AIMED AT LYRIA
  FIND     an exclude list or a negative-prompt block aimed at Lyria
  REPLACE  delete the list; state the wanted result positively. If one thing
           must be kept out, use Google's own shape — a positive statement and
           one short clause: "Instrumental only, no vocals."
  SAY      Lyria 3.5 has no negative-prompt field. A list has nowhere to go.
  MARK     no field [COMMUNITY: API reviewers] · the one-clause example [OFFICIAL]

</rag_zone>

<!-- rag_anchor: repair_table_11_tempo_without_a_number_rule_revised_in_v4_0 -->
<rag_zone id="repair_table_11_tempo_without_a_number_rule_revised_in_v4_0">

### 11 · TEMPO WITHOUT A NUMBER — rule revised in v4.0
  FIND     a tempo given only in words, on any platform
  REPLACE  keep the words, add the number: "a fast, driving pace at 140 BPM"
  SAY      Google's current Lyria guide asks for BPM as a number, and so does
           ElevenLabs. Earlier editions of this system told you the opposite
           for Lyria — that came from the older Lyria 3 Pro guide. A numeric
           BPM is no longer a defect anywhere; a missing one is a missed chance.
  MARK     [OFFICIAL] for Lyria and ElevenMusic · [COMMUNITY] for Suno
  WHERE    CORE_01 §2

### 12 · UDIO REFERENCES
  FIND     Udio named as a generation target, or its inpainting workflow
  REPLACE  Stable Audio for instrumental and DAW work; ElevenMusic for
           released material with clean licensing
  SAY      Udio disabled downloads after its late-2025 settlement [OFFICIAL +
           COMMUNITY]; they are reported still closed [UNVERIFIED], and its
           licensed successor is a walled fan app. Anything made there cannot be
           relied on for export. Covered here only as a cautionary case.
  MARK     [OFFICIAL + COMMUNITY] — see DATA_LEGAL §7 for the sourcing
  WHERE    DATA_LEGAL

</rag_zone>

<!-- rag_anchor: repair_table_13_musicfx_and_musicfx_dj -->
<rag_zone id="repair_table_13_musicfx_and_musicfx_dj">

### 13 · MUSICFX AND MUSICFX DJ
  FIND     MusicFX · MusicFX DJ · "MusicFX DJ in AI Studio" as a live tool
  REPLACE  Google Flow Music or the Gemini app; for interactive streams, Lyria
           RealTime
  SAY      Both products were retired as Google consolidated its music tools
           into Flow Music.
  WHERE    DATA_GOOGLE §9

### 14 · PRODUCER.AI AND RIFFUSION
  FIND     Riffusion or Producer.ai named as current services
  REPLACE  Google Flow Music
  SAY      One product, three names: Riffusion became Producer.ai, Google
           acquired it, and it is now Flow Music. Not three competitors.
  ⚠️ NEVER  Never emit a web address for anything trading under the Riffusion
           name. Several such sites are live and selling subscriptions with no
           verifiable connection to the original project — no named company,
           no stated affiliation. Direct users to Flow Music by name only.
  WHERE    DATA_GOOGLE

</rag_zone>

<!-- rag_anchor: repair_table_15_old_menu_numbers -->
<rag_zone id="repair_table_15_old_menu_numbers">

### 15 · OLD MENU NUMBERS
  FIND     a guide instructing "press 10" and meaning audit
  REPLACE  audit is [12]
  SAY      The guide predates the current menu. Numbers are frozen now and
           will not move again.
  WHERE    CORE_00 §4 and §10

### 16 · PROMPTS CUT TO A LIMIT THAT DOES NOT EXIST
  FIND     a Style prompt visibly truncated to a round number of characters,
           or a user stating a character ceiling as a rule
  REPLACE  rebuild the prompt at the length the content needs
  SAY      The strict short ceiling taught by earlier guides — including
           earlier versions of this system — was never measured. It made
           people cut prompts well below the range that actually steers the
           result. Front-loading matters; that arbitrary ceiling did not.
  WHERE    DATA_SUNO §2 for what is actually known about length

</rag_zone>

<!-- rag_anchor: repair_table_17_adherence_percentages -->
<rag_zone id="repair_table_17_adherence_percentages">

### 17 · ADHERENCE PERCENTAGES
  FIND     "88% prompt adherence" or any similar cited accuracy figure
  REPLACE  delete the number
  SAY      No such metric is published. The figure has no traceable source.

### 18 · WRONG PLAN FOR A FEATURE
  FIND     a claim that a given feature comes with a particular subscription
  REPLACE  the current tier for that feature
  SAY      Plan mapping has changed more than once and getting it wrong costs
           the user real money in the wrong direction.
  WHERE    DATA_SUNO §12 — do not state tiers from memory, read them there

### 19 · CREDIT COSTS QUOTED FROM GUIDES
  FIND     a specific per-generation credit cost for a feature
  REPLACE  point the user at their own account; keep only the relative fact
           where it matters ("Max Mode costs more", "stems cost the most")
  SAY      Several widely repeated figures are contradicted by other guides
           and were never published by the vendor.
  WHERE    DATA_SUNO

</rag_zone>

<!-- rag_anchor: repair_table_20_retired_suno_model_names -->
<rag_zone id="repair_table_20_retired_suno_model_names">

### 20 · RETIRED SUNO MODEL NAMES
  FIND     v5.5 · v5 · v4.5-all · v4.5+ · v4 and older, as a target or setting
  REPLACE  v6; v6-wild for experiments; v6-mini for free drafts
  SAY      Suno retired every model before v6 on 2026-09-09. Old songs stay
           playable; any new iteration runs on v6. The prompt text usually
           carries over — only the label is dead.
  MARK     [OFFICIAL] · WHERE DATA_SUNO §1

### 21 · LYRIA SINGLE-POINT MARKERS
  FIND     a list of `[00:15] event` markers aimed at Lyria 3.5
  REPLACE  ranges ending where the next begins: `[0:15 - 0:30] Verse 1: event`
  SAY      The single-point form comes from the Lyria 3 Pro guide; the current
           docs show ranges with section names.
  MARK     [OFFICIAL example] · WHERE DATA_GOOGLE §4

</rag_zone>

<!-- rag_anchor: repair_table_22_lyria_3_pro_and_its_numbers -->
<rag_zone id="repair_table_22_lyria_3_pro_and_its_numbers">

### 22 · LYRIA 3 PRO AND ITS NUMBERS
  FIND     "Lyria 3 Pro" as the current model · "184 seconds" · lyria-3-pro-preview
           · Clip "48 kHz" · PDF input promised for Lyria
  REPLACE  Lyria 3.5 · "a couple of minutes" (up to 3 in the Gemini app) ·
           lyria-3.5 · 44.1 kHz · images only
  SAY      Lyria 3.5 replaced 3 Pro in September 2026.
  MARK     [OFFICIAL] · WHERE DATA_GOOGLE §1

### 23 · PRICES
  FIND     subscription or API prices in a prompt, a preset or a guide excerpt
  REPLACE  delete; keep the plan NAME where a feature depends on it
  SAY      Prices differ by country and change without notice. This system
           names plans and never prices them.
  WHERE    CORE_00 §7 rule 13

</rag_zone>

<!-- rag_anchor: repair_table_24_an_engineered_style_with_variety_left_on -->
<rag_zone id="repair_table_24_an_engineered_style_with_variety_left_on">

### 24 · AN ENGINEERED STYLE WITH VARIETY LEFT ON
  FIND     "Suno changed my style" · "it ignored my tags" · or a carefully built
           Style for v6 with no Variety setting in the blueprint
  REPLACE  add "Variety: 0" to the blueprint
  SAY      Above zero, v6 rewrites the style prompt on purpose, differently for
           each take. Suno: reduce Variety to 0 "to retain full control of your
           style tags".
  MARK     [OFFICIAL] · WHERE DATA_SUNO §4

### 25 · LYRIA LYRICS WITHOUT A HEADER
  FIND     words meant to be sung mixed into the musical directions of a Lyria
           prompt; or directions inside the lyric lines
  REPLACE  directions first, then a `Lyrics:` header, then the text with
           section tags; backing vocals in parentheses
  SAY      Google: "Separate lyrics from instructions" — otherwise the model may
           sing your directions or ignore your words.
  MARK     [OFFICIAL] · WHERE DATA_GOOGLE §5

</rag_zone>

<!-- rag_anchor: repair_table_how_to_apply_the_table -->
<rag_zone id="repair_table_how_to_apply_the_table">

### HOW TO APPLY THE TABLE

  1. Repair silently in bulk. Do not narrate twenty-five rows.
  2. Group the explanation: "I removed the bracketed parameters — none of
     those were ever read — and rewrote them as description."
  3. Never return only a diagnosis. Always return the repaired prompt.
  4. If a repair changes what the user asked for musically, ask first. If it
     only changes syntax, just do it.

</rag_zone>

</section>

<section id="§4" title="TRIGGER WORDS — the single copy">

<!-- rag_anchor: trigger_words -->
<rag_zone id="trigger_words">
📌 This list exists in this file only. Other files reference it. Do not copy it.

Words that describe audio defects appear to make those defects more likely,
including when they are used in a negative construction. The mechanism is the
same one that makes gender negatives backfire: to exclude a concept the model
has to represent it first.

  AVOID              WHY                             WRITE INSTEAD
  ────────────────── ─────────────────────────────── ────────────────────────
  artifact           more artifacts, not fewer       clean tone
  glitch, glitches   stuttering, digital break-up    smooth, continuous
  clipping           loud distortion                 balanced dynamics
  distortion¹        unwanted overdrive              (see note)
  background noise   more hiss                       clean background
  hiss               more hiss                       warm tone
  shimmer²           metallic high-frequency ring    bright presence
  muddy              a muddier low-mid               clear and defined
  harsh              a harsher top end               smooth top end
  thin               a thinner result                full-bodied
  boomy              more low-mid buildup            tight low end
  static             literal static                  clean signal
  compressed³        flat, lifeless dynamics         (see note)
  low quality        exactly what it says            studio-grade
  amateur            exactly what it says            professionally recorded
  demo               lo-fi, unfinished character     (only if wanted)

  ¹ "distortion" is wanted in rock and metal. It is a trigger only when used
    to exclude it. Say "clean guitar tone" rather than "no distortion".
  ² "shimmer" as a positive descriptor for pads and reverb is fine. It is a
    trigger when used to exclude a metallic ringing artifact.
  ³ "heavily compressed" is a legitimate production instruction. The trigger
    is "over-compressed" and similar complaint phrasing.

</rag_zone>

<!-- rag_anchor: trigger_words_the_principle -->
<rag_zone id="trigger_words_the_principle">

### THE PRINCIPLE

State what you want, not what you are afraid of.

  ❌  no clipping, no distortion, no background noise
  ✅  balanced dynamics, clean tone, consistent volume, warm and full

### CONFIDENCE

[COMMUNITY] — reported consistently across independent guides and matching a
well-known behaviour of generative models generally. No controlled test of the
specific word list has been published. Treat it as a sound writing habit rather
than a mechanism: positive phrasing is better prompt-writing regardless of
whether the effect is as strong as claimed.

### WHERE THIS DOES NOT APPLY

The Exclude Styles field is a real negative field with its own behaviour, and
it takes musical categories rather than defect words. Both the field and what
to put in it are documented in DATA_SUNO §3. The list above is about the Style
text, not that field.

</rag_zone>

</section>

<section id="§5" title="FAILURE MODES">

<!-- rag_anchor: failure_modes -->
<rag_zone id="failure_modes">
Matched by what the user describes hearing.

### LYRICS COME OUT AS NONSENSE, OR WORDS GO MISSING

  SYMPTOM   Slurred or invented words; dropped line endings; the sung lyric
            drifts out of alignment with the written one.
  CAUSE     [COMMUNITY] Once alignment breaks early in a generation,
            everything after it is misaligned too. It compounds.
  FIX       1. Compare the written lyric against what was actually sung, all
               the way through — not just the section that sounds wrong.
            2. Note every dropped word and swallowed line ending.
            3. Correct the full lyric text first.
            4. Only then regenerate the affected section.
  WHY THAT ORDER  Replacing one section against an already-misaligned lyric
            re-creates the same misalignment.
  PREVENT   Fewer words per line in fast passages. Avoid dense consonant
            clusters at line ends.

</rag_zone>

<!-- rag_anchor: failure_modes_unasked_for_talking_dialogue_or_narration -->
<rag_zone id="failure_modes_unasked_for_talking_dialogue_or_narration">

### UNASKED-FOR TALKING, DIALOGUE OR NARRATION

  SYMPTOM   Spoken passages nobody requested; the model narrating.
  CAUSE     Instructions that were readable as lyrics, or structural labels
            malformed enough to be sung.
  FIX       - Round brackets: check nothing in them is an instruction (§2
              check 5). "(play guitar softly)" gets sung, verbatim.
            - Use clean section labels. `[Verse]` rather than an improvised
              label the model may read as words.
            - If the track should have no speech, say so positively in Style:
              "sung throughout, no spoken passages".

</rag_zone>

<!-- rag_anchor: failure_modes_quality_degrades_over_a_long_working_session -->
<rag_zone id="failure_modes_quality_degrades_over_a_long_working_session">

### QUALITY DEGRADES OVER A LONG WORKING SESSION

  SYMPTOM   Later generations worse than earlier ones with the same prompt;
            labels ignored more often; nonsense creeping in.
  CAUSE     [COMMUNITY] Accumulated session state.
  FIX       1. Copy the prompt and any edits somewhere outside the browser.
            2. Full page refresh.
            3. Paste back and regenerate.
  PREVENT   Refresh every ten to fifteen generations. Keep prompts in your own
            notes rather than relying on history. Short sessions beat marathons
            — for the tool and for your ears.

### A SUDDEN LOUD FINISH NOBODY ASKED FOR

  SYMPTOM   Quiet song, then shouting or a dramatic climax near the end.
  CAUSE     [COMMUNITY] Big finishes are heavily represented in training data,
            so a big finish is a likely continuation even when nothing in the
            song was building toward one.
  FIX       - State the ending explicitly: [Outro — fade out] or
              [Outro — ends on a single held note].
            - Describe the intended end in the Style field: "ends quietly,
              unresolved".
            - When extending, restate the energy: "continue calmly, no drums,
              minimal energy".
            - Lower the experimental slider on extensions rather than the base
              track (values by goal: DATA_SUNO §8).
  NOTE      Repeated extension compounds this. Past two, regenerating whole
            usually beats extending again [COMMUNITY].

</rag_zone>

<!-- rag_anchor: failure_modes_vocals_in_a_track_that_should_be_instrumental -->
<rag_zone id="failure_modes_vocals_in_a_track_that_should_be_instrumental">

### VOCALS IN A TRACK THAT SHOULD BE INSTRUMENTAL

  SYMPTOM   Singing, humming or wordless vocal in an instrumental.
  FIX       Three layers, all three at once [COMMUNITY]:
            1. the instrumental switch in the interface
            2. `[Instrumental]` in the Lyrics field
            3. "instrumental, no vocals" stated in Style
            Any one alone leaks occasionally. Together they hold.
  NOTE      On Lyria write "Instrumental only, no vocals." [OFFICIAL]; in the
            Gemini app there is also a Vocals menu with Instrumental. On
            ElevenMusic, "instrumental only" [OFFICIAL]. See DATA_GOOGLE §5.

</rag_zone>

<!-- rag_anchor: failure_modes_the_track_is_technically_fine_and_completely_bor -->
<rag_zone id="failure_modes_the_track_is_technically_fine_and_completely_bor">

### THE TRACK IS TECHNICALLY FINE AND COMPLETELY BORING

  SYMPTOM   Nothing wrong, nothing interesting. Generic.
  CAUSE     Almost always an under-specified Style field, not a model problem.
  FIX       - Apply Time & Place: era plus scene instead of a genre name
            - Replace generic instrument names with playing-style descriptors
            - Add a production signature — the room, the era, the tape
            - Give the singer a biography instead of a gender
            - Raise the experimental slider modestly
  WHERE     CORE_01 §3, §5, §7, §9

### THE TRACK LOSES ITS CHARACTER PART WAY THROUGH

  SYMPTOM   Starts right; later sections sound flatter, more generic, less
            like the requested genre.
  STATUS    ⚠️ Read this carefully, because a specific version of this claim
            is widely repeated and does not hold up.

            The claim that tracks reliably degrade after a fixed point — the
            "two-minute drift" — is [UNVERIFIED]. It rests on anecdotes. No
            systematic testing supports it, no vendor has acknowledged it, and
            detailed independent reviews do not report a threshold. Earlier
            editions of this system built an automatic mechanism on top of it.
            That mechanism has been removed.

            What is true: long generations vary, and a section can come back
            weaker than the one before it. What changed in September 2026:
            Suno itself now recommends Max Mode for "songs longer than two
            minutes" and for "keeping vocals and style consistent through the
            whole track" [OFFICIAL]. So long-track consistency IS a problem the
            vendor acknowledges — it just does not arrive on a schedule, and
            the vendor's cure is a setting, not anchor tags in every section.

  IF IT HAPPENS TO YOU:
            - On Suno v6: turn Max Mode on for anything past two minutes
              (DATA_SUNO §4). This is the first thing to try now.
            - Regenerate. Variance is variance; the next take may be fine.
            - Make the genre anchor more specific in the opening words.
            - Restate genre and production in the later section labels
              (CORE_02 §4). Costs nothing, may help.
            - Make the bridge an explicit reset: strip the arrangement and
              name the original aesthetic again.
            - Build long tracks in sections and extend, rather than asking for
              one long generation — each extension is a fresh instruction.
            - Give the model enough lyric material for the length. Thin
              material over a long target is the most reproducible cause of
              aimless later sections.

  DO NOT    Do not tell a user their track will drift at two minutes. Do not
            add anti-drift machinery to every prompt by default. Recommend the
            toggle where it fits, and nothing more.

</rag_zone>

<!-- rag_anchor: failure_modes_a_metallic_ring_on_the_high_end -->
<rag_zone id="failure_modes_a_metallic_ring_on_the_high_end">

### A METALLIC RING ON THE HIGH END

  SYMPTOM   A glassy, ringing quality on cymbals and vocal sibilance.
  STATUS    [COMMUNITY] Widely reported on older models, reported as much
            improved since. Whether it persists is not settled.
  FIX       - Lower the experimental slider
            - Regenerate with a defined vocal persona
            - If it survives: pull stems and treat the top end outside the
              platform (DATA_POSTPROD)

### SECTION LABELS SEEM TO BE IGNORED

  SYMPTOM   Structure does not match the markup.
  CAUSE     Labels are probabilistic hints, not commands (CORE_00 §7 rule 10).
            Some proportion will not land, on any platform, always.
  FIX       - Confirm each label sits on its own line above its section
            - Confirm labels are not duplicated by the editor (CORE_02 §2)
            - Confirm the lyric is long enough for the structure requested
            - Generate several takes and choose
  DO NOT    Do not stack more modifiers in response. That is not a fix, and it
            has no evidence behind it in either direction (CORE_02 §4).

</rag_zone>

<!-- rag_anchor: failure_modes_the_voice_is_the_wrong_gender -->
<rag_zone id="failure_modes_the_voice_is_the_wrong_gender">

### THE VOICE IS THE WRONG GENDER

  FIX       1. Delete every gender negative.
            2. State the wanted voice positively, early in the description.
            3. Use the Vocal Gender control — the most reliable control
               available (DATA_SUNO §8).
            4. Give the singer a persona rather than a label (CORE_01 §7).

### A TRAINED VOICE OR CUSTOM MODEL DOES NOT SOUND RIGHT

  VOICE DOESN'T SOUND LIKE ME
            Usually the source recording. Give it range — high and low, loud
            and soft, varied phrasing. Requirements, accepted lengths and the
            practical sweet spot are in DATA_SUNO §5.
            Also: it is directional, not exact. Expect your character rather
            than your double.

  CUSTOM MODEL IS VAGUE
            Almost always a stylistically mixed training set. A catalogue
            spanning several genres teaches the model to average them. Build
            separate models per style rather than one general one. Counts,
            limits and requirements: DATA_SUNO §6.

  ON v6     Voices and Custom Models moved to v6: custom models were upgraded
            automatically [OFFICIAL]; existing voices show an "Upgrade Voice to
            v6" action [COMMUNITY]. Check that the voice was upgraded and that a
            compatible model is selected before judging the result.

</rag_zone>

<!-- rag_anchor: suno_v6_early_reports -->
<rag_zone id="v6_early_reports">

### EARLY SUNO v6 REPORTS (September 2026)

All [COMMUNITY], none controlled. Collected so a user hearing one of these knows
it is not their prompt alone. Try the fix, listen, keep what works.

  MUFFLED, DULL, BURIED VOCALS · "the high end feels almost completely gone"
            (widely quoted launch complaint)
    TRY     name the vocal as the focus early in Style ("a close, present lead
            vocal, bright and upfront"); raise Style Influence; one user fixed it
            on v6-wild with Weirdness ~20 and Style Influence ~80; Max Mode for
            the final take.
  HUMMING OR VOCALISE BEFORE THE FIRST LINE
    TRY     "humming, vocalise, wordless vocals" in Exclude Styles — asking in
            the prompt to remove humming produced more humming.
  LAST LINE CUT OFF · OR AN OUTRO THAT GOES ON TOO LONG
    TRY     state the ending and its length in Style; end the lyric with an
            explicit ending label ([Outro — ends on a held chord]); for long
            songs, Max Mode, or generate the back half with Extend.
  DUET SINGERS SWAP MID-LINE
    TRY     whole sections per singer; all three duet anchors (CORE_02 §9).
  SMEARED SIBILANCE, MORE ARTIFACTS ON ROCK AND METAL
    TRY     v6-wild for metal and drum & bass, where v6 is reported weakest;
            treat the top end in post (DATA_POSTPROD).
  "SUNO CHANGED MY STYLE TEXT"
    CAUSE   Variety above zero — by design [OFFICIAL]. Fix: §3 row 24.
  "SIMPLE MODE SANG DIFFERENT WORDS"
    CAUSE   Simple mode may expand supplied lyrics. Fix: use the Lyrics field
            (CORE_02 §2).
  "MY OLD PROMPTS DON'T WORK"
    STATUS  disputed: some users say old prompts fail on v6, others that the
            grammar and field limits did not change. Run the audit, set
            Variety to 0 for engineered styles, and compare two takes.

</rag_zone>

</section>

<section id="§6" title="WHAT IS NOT A DEFECT">

<!-- rag_anchor: not_a_defect -->
<rag_zone id="not_a_defect">

An audit that flags everything unusual is worse than no audit, because the user
stops reading it.

### VARIATION BETWEEN TAKES
Two generations from one prompt differ. That is the tool working as designed,
and it is why this system asks for several takes rather than one.

### AN UNUSUAL GENRE PAIRING
Incompatible pairs are expensive, not forbidden (CORE_01 §10). Say it will
take more takes; do not "correct" it.

### AN UNDOCUMENTED TECHNIQUE THAT WORKS FOR THE USER
Pipe stacking is the standing example. Genuinely unsettled, no primary source
on either side (CORE_02 §4). If a user's prompts use it and they are happy,
leave it. Unproven is not the same as broken.

### A LONG PROMPT
Length alone is not a defect. Contradiction is. Ten descriptors pulling in one
direction is fine; four pulling in different directions is not.

### DELIBERATE ROUGHNESS
"Lo-fi", "demo", "unmastered", "bedroom recording" are aesthetic choices.
Do not repair them into polish.

### NON-ENGLISH LYRICS
Not a defect and not a warning. If the user writes in another language, state
the language in the Style field so the delivery matches ("native Ukrainian female
vocal, clear diction"). On Lyria 3.5 write the whole prompt in that language — the
model sings in the language of the prompt [OFFICIAL, DATA_GOOGLE §5]. No
independent test of Russian or Ukrainian pronunciation on Suno v6 or Lyria 3.5
exists yet; stress marks and phonetic spellings are community tricks, not syntax.

</rag_zone>

</section>

<section id="§7" title="PLATFORM-SPECIFIC PROBLEMS">

<!-- rag_anchor: platform_troubleshoot -->
<rag_zone id="platform_troubleshoot">
### LYRIA

  STRUCTURE IGNORED
    Use section tags with arrows or timestamp ranges. One main event per
    range, plainly stated.
    Syntax: DATA_GOOGLE §4 [OFFICIAL].

  THE SONG ENDS EARLY · THE PLANNED ENDING NEVER ARRIVES
    The plan is longer than the model: "a couple of minutes" for 3.5 in the API
    (steerable in the prompt, maximum not published),
    three in the app, thirty seconds for Clip. Compress the plan or move the
    song to Suno v6 (8 min) or Stable Audio Medium (6:20).

  RESULT IS GENERIC
    Time & Place works here too. Describe the shape over time — what is thin
    at the start and what has arrived by the middle. Consider generating the
    instrumental first and the vocal as a separate pass.

  THE PROMPT IS REFUSED OR RETURNS NOTHING
    Remove real artist names and copyrighted lyrics — both are blocked by the
    safety filter [OFFICIAL]. Replace names with era and scene descriptions
    (CORE_01 §12).
    Remove any exclude list; keep at most one short exclusion clause after a
    positive statement (§3 row 10).

  TEMPO NOT LANDING
    Give the BPM as a number and name the key — Google's guide asks for both
    [OFFICIAL]. §3 row 11.

  IT SANG THE INSTRUCTIONS
    Put the words under a `Lyrics:` header, directions above it (§3 row 25).

  NO WAY TO FIX ONE PART
    Lyria generation is single-turn [OFFICIAL]. Regenerate, or take the idea to
    Flow Music, which edits part by part.

</rag_zone>

<!-- rag_anchor: platform_troubleshoot_google_flow_music -->
<rag_zone id="platform_troubleshoot_google_flow_music">

### GOOGLE FLOW MUSIC

  A REPLACE BREAKS THE MIX
    Scope the instruction tightly — name the one part to change, and name
    what must stay untouched.

  AN EXTENSION CHANGES STYLE
    Restate the style anchor inside the extension instruction. Do not assume
    continuity is inherited.

### ELEVENMUSIC

  VOCAL LACKS EXPRESSION
    Reported on earlier versions; Music v2.5 claims its largest gains on
    vocal-led genres [OFFICIAL]. Regenerate the weak section alone, add delivery
    words (raw, belted, conversational), and narrate where the vocal should
    lift (DATA_OTHER §1).

  DOWNLOAD BLOCKED
    The track references another artist's song — ElevenMusic blocks downloads
    of those by design [OFFICIAL].

</rag_zone>

<!-- rag_anchor: platform_troubleshoot_stable_audio -->
<rag_zone id="platform_troubleshoot_stable_audio">

### STABLE AUDIO

  UNWANTED VOCAL ARTEFACTS
    Primarily an instrumental and sound-design tool. State "instrumental"
    explicitly and keep vocal language out of the prompt entirely.

### SUNO

  Suno-specific interface behaviour, field limits, sliders and features are
  documented in DATA_SUNO. This file covers what is diagnosable from the text of
  a prompt, plus the early v6 reports in §5.

</rag_zone>

</section>

<section id="§8" title="FAST TRIAGE">

The symptom index is at the top of this file (§0), where a symptom-first lookup
finds it first.

</section>

// ═══════════════════════════════════════════════════════════════
// END OF CORE_03_DIAGNOSE.md · SunoForge v4.0
// Next: CORE_04_WHY.md
// ═══════════════════════════════════════════════════════════════

<tags>audit, diagnose, repair, symptom index, diagnostic checks, repair table, max mode tags, max mode toggle, parametric tags, gender negatives, lyria timestamp ranges, lyria exclude list, tempo bpm, retired platforms, udio, musicfx, riffusion, retired suno models, v5.5, lyria 3 pro, prices, variety 0, lyrics header, trigger words, failure modes, hallucinated lyrics, unwanted talking, session degradation, loud finish, vocals in instrumental, long-track consistency, metallic ring, v6 early reports, muffled vocals, humming, cut-off ending, not a defect, non-english lyrics, platform problems</tags>
</sunoforge_file>
