---
file_id: CORE_03_DIAGNOSE
version: "3.0"
layer: core
scope: audit_protocol · repair_engine · failure_modes · trigger_words · session_health · platform_troubleshoot
key_concepts: [audit_12, diagnostic_checks, repair_table, dead_constructs, migration_repair, failure_modes, hallucinations, trigger_words, long_track_consistency, session_health]
depends_on: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS]
used_by: [CORE_00_ENTRY, CORE_04_WHY, DATA_SUNO, DATA_GOOGLE, DATA_OTHER]
rag_priority: critical
authority: "THIS FILE IS THE SINGLE SOURCE FOR THE TRIGGER-WORD LIST"
updated: "2026-07-27"
changelog: "v3.0 — repair engine for menu [12] rebuilt around dead constructs from CORE_00 §10 · trigger-word list consolidated here as the only copy · two-minute drift demoted from a diagnosis to an unverified belief · pipe-artifact section withdrawn · MAX MODE troubleshooting replaced with MAX MODE removal · Udio section replaced by retired-platform repairs"
---

# 🩺 SUNOFORGE v3.0 — DIAGNOSE & REPAIR
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

═══════════════════════════════════════════════════════════════════
§1. WHAT AUDIT IS FOR
═══════════════════════════════════════════════════════════════════

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

─── THE TONE RULE ───

An audit repairs a prompt. It does not lecture the person who wrote it.

Most defects in circulating prompts came from guides that were confident and
wrong, including previous editions of this system. Say what changed and what to
write instead. Do not imply the user should have known.

  ✅  "MAX MODE tags don't do anything — controlled testing found no hidden
      mode. I've dropped them and put the quality intent into the description."
  ❌  "You're using outdated MAX MODE syntax, which has been debunked."

─── WHAT NOT TO CHANGE ───

  - Creative choices. A strange genre pairing is not a defect (§6).
  - Anything working that is merely undocumented. Unproven is not broken.
  - The user's voice in the lyrics.
  - `///*****///` and other harmless remnants — say they do nothing, leave them
    if the user likes them.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. THE DIAGNOSTIC PROTOCOL — fourteen checks, in order
═══════════════════════════════════════════════════════════════════

<rag_zone id="diagnostic_checks">

Run in order. Earlier checks change what later checks are looking at.

─── CHECK 1 · FRONT-LOADING ───
  Do the opening words name a specific subgenre?
  FAIL:  "a rock song with some grunge influence"
  FIX:   lead with the most specific thing — "mid-90s Seattle grunge"
  WHY:   the opening words carry the most weight (CORE_01 §1)

─── CHECK 2 · GENRE COUNT ───
  More than two genres named?
  FIX:   keep one primary and one modifier. If the user wants a real blend,
         that is a hybrid and needs a bridge — CORE_01 §10

─── CHECK 3 · INSTRUMENT COUNT ───
  More than three or four instruments listed?
  FIX:   cut to two or three hero instruments plus one texture word
  WHY:   an undifferentiated list produces an undifferentiated arrangement

─── CHECK 4 · MOOD CONFLICT ───
  Contradictory moods, or more than two?
  FAIL:  "happy dark aggressive peaceful"
  FIX:   one or two that can coexist (CORE_01 §4)

─── CHECK 5 · BRACKET VIOLATION ───
  Instructions inside round brackets?
  FAIL:  "(play the guitar softly here)"
  FIX:   move to square brackets, or delete if it was never performable
  WHY:   round brackets are sung — the model will sing the instruction

─── CHECK 6 · PARAMETRIC CONSTRUCTS ───
  Any `[parameter: value]` forms?
  FIX:   rewrite as prose in Style; see the repair table §3
  NOTE:  this is the highest-volume defect in circulating prompts

─── CHECK 7 · GENRE CONFLICT ───
  Is the pairing on the incompatible list?
  FIX:   name the conflict, offer the bridge genre
  WHERE: the compatibility table is menu [4c] — CORE_01 §10
  NOTE:  this is advice, not a blocker. Users may want the collision.

─── CHECK 8 · FIELD MIX-UP ───
  Tempo, key, genre or production language sitting in the Lyrics field?
  Section structure sitting in the Style field?
  FIX:   swap them. Style describes the record; Lyrics places the events
         (CORE_01 §8, CORE_02 §13)

─── CHECK 9 · VOCAL GENDER NEGATIVES ───
  "no male vocals", "not a female singer", or similar?
  FIX:   delete the negative, state the wanted voice positively in Layer 4,
         and point at the interface gender selector (DATA_SUNO §7)
  WHY:   naming a voice type to exclude it can summon it

─── CHECK 10 · TRIGGER WORDS ───
  Any of the words in §4?
  FIX:   swap for the positive equivalent given there

─── CHECK 11 · RETIRED PLATFORMS ───
  References to platforms that no longer serve this purpose?
  FIX:   repair table §3, rows 12–15

─── CHECK 12 · PLATFORM SYNTAX MISMATCH ───
  Suno bracket markup aimed at Lyria? An exclude list aimed at Lyria?
  Tempo written as a number for Lyria, or as words for Suno?
  Lyria timestamps written in the old parenthetical form?
  FIX:   repair table §3, rows 9–11

─── CHECK 13 · LENGTH AND SUBSTANCE ───
  Is there enough lyric material for the intended track length?
  FIX:   add material, or shorten the target
  WHY:   a long target with thin material produces padding, aimless
         instrumental passages, or an abrupt cut (CORE_02 §12)

─── CHECK 14 · MYTH DEPENDENCY ───
  Does the prompt rely on something that does not work?
  Does it show signs of having been cut to fit a limit that does not exist?
  FIX:   repair table §3, and say plainly what the evidence shows
  WHERE: the catalogue of debunked claims is DATA_SUNO §13

─── OUTPUT FORMAT ───

```
🩺 AUDIT

WORKING
  ✅ Check 1 — front-loaded on a specific subgenre
  ✅ Check 4 — two compatible moods

NEEDS REPAIR
  ❌ Check 6 — three parametric tags; never parsed
  ❌ Check 9 — gender negative in Style; unreliable and can backfire
  ⚠️ Check 12 — tempo given as a number, but the target is Lyria

REPAIRED VERSION
  [full output in the target platform's protocol — CORE_00 §6]

WHAT CHANGED AND WHY
  [one line per repair, in plain language]
```

Report what passed as well as what failed. A user who only sees failures cannot
tell which of their habits are good ones.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. THE REPAIR TABLE — dead constructs
═══════════════════════════════════════════════════════════════════

<rag_zone id="repair_table">

Every row: what to find, what to write instead, and what to tell the user.
This is the mechanical core of [12]. Rows 1–8 are syntax, 9–11 are
cross-platform, 12–15 are retired products, 16–19 are stale facts.

─── 1 · MAX MODE TAGS ───
  FIND     [Is_MAX_MODE: MAX] · [QUALITY: MAX] · [REALISM: MAX]
           [REAL_INSTRUMENTS: MAX] · (MAX)(MAX)(MAX)(MAX)
  REPLACE  delete. If the user wanted a quality signal, express it as
           description: "studio-grade recording, detailed and dynamic"
  SAY      There is no hidden quality mode. A controlled comparison found no
           difference beyond normal variation. The tags read as plain
           descriptive words, so removing them costs nothing.
  MARK     [UNVERIFIED] · origin: a single forum post

─── 2 · THE SLASH-ASTERISK SEPARATOR ───
  FIND     ///*****/// as the first line of the Lyrics field
  REPLACE  nothing. Leave it.
  SAY      It does nothing, and it does no harm. Keep it if you like it.

─── 3 · MIX PARAMETER TAGS ───
  FIND     [eq: scooped] · [eq: midrange-clear] · [compression: heavy]
           [focus: bass] · [wide stereo field] · [Sidechain] · [Reverb: 30%]
  REPLACE  the same intent as prose inside Style:
           "scooped mids, heavily compressed, wide stereo, pumping sidechain"
  SAY      Bracketed mix parameters were never parsed. The same words work
           as ordinary description — that part was always doing the work.
  MARK     [UNVERIFIED]

─── 4 · MUSICAL PARAMETER TAGS ───
  FIND     [BPM: 120] · [Tempo: 120 BPM] · [Key: A minor]
           [Chord progression: Am - F - C - G]
  REPLACE  in Style, as prose: "120 BPM, A minor"
           for chords, inline in the lyric: "(Am) the city sleeps"
  SAY      Same as above. The inline chord form is the one that works.
  WHERE    CORE_02 §10

─── 5 · MOOD AND ENERGY TAGS ───
  FIND     [Mood: Uplifting] · [Energy: High] · [Energy: Low→High]
           [Atmosphere: Cyberpunk] · [Vibe: Midnight drive]
  REPLACE  in Style: "uplifting", "builds from near-silence to full force",
           "cyberpunk night city"
  SAY      Parametric form again. The words were carrying the meaning; the
           brackets and colon were not.

─── 6 · ATMOSPHERE TAGS WITH A COLON ───
  FIND     [Sound: Rain] · [sound:thunder] · [Sound: City ambience]
  REPLACE  section-level: [Rain] · [Thunder] · [City ambience]
           track-level: describe it in Style — "with rain under the intro"
  SAY      Drop the "Sound:" prefix. The plain bracket is a section event,
           which is what you wanted.
  WHERE    CORE_02 §11

─── 7 · VOCAL PARAMETER TAGS ───
  FIND     [Vocal Style: Raspy] · [Vocal: female] · [Choir: Gospel]
           [Persona: Pop Star]
  REPLACE  [Raspy lead vocal] · [Gospel choir] — or, better, a persona
           description in Style (CORE_01 §7)
  SAY      Delivery direction belongs in plain brackets; who is singing
           belongs in the Style field.

─── 8 · GENDER NEGATIVES ───
  FIND     "no male vocals" · "without male voice" · "not a female singer"
           stacked gender exclusions of any kind
  REPLACE  a positive statement in Layer 4: "solo female vocalist, breathy
           soprano, intimate delivery" — plus the interface gender selector
  SAY      Gender negatives are unreliable and sometimes produce the opposite,
           because naming a voice type puts it in front of the model. The
           selector in Advanced Options is the reliable control.
  WHERE    DATA_SUNO §7 for the selector; §3 there for the Exclude Styles field
  MARK     [COMMUNITY, widely reproduced]

─── 9 · LYRIA STRUCTURE IN THE OLD FORMAT ───
  FIND     "Intro (0–15s)" · "[End - 2:15]" · "verse (15-45s)"
  REPLACE  timestamp markers: `[00:00]` then a description of what happens,
           `[00:15]` then what enters, and so on to the end
  SAY      Google documents timestamp prompting, and the format is a bracketed
           `[MM:SS]` followed by plain description. The parenthetical form was
           our invention and it was wrong.
  MARK     [OFFICIAL] · full syntax in DATA_GOOGLE

─── 10 · EXCLUDE LISTS AIMED AT LYRIA ───
  FIND     any negative prompt, exclude list or "no X" aimed at Lyria
  REPLACE  delete, and state the wanted result positively instead
  SAY      Negative prompting is not supported there. An exclude list is not
           weak on this platform — it is not read at all.
  MARK     [OFFICIAL]

─── 11 · TEMPO IN THE WRONG FORM ───
  FIND     a numeric BPM in a prompt targeting Lyria
           a purely descriptive tempo in a prompt targeting Suno
  REPLACE  Lyria: "a fast, driving pace with an insistent backbeat"
           Suno:  "140 BPM"
  SAY      The two platforms want opposite things here. Vendor guidance for
           Lyria is descriptive tempo; on Suno the number works.
  MARK     [OFFICIAL] for Lyria · [COMMUNITY] for Suno
  WHERE    CORE_01 §2

─── 12 · UDIO REFERENCES ───
  FIND     Udio named as a generation target, or its inpainting workflow
  REPLACE  Stable Audio for instrumental and DAW work; ElevenMusic for
           released material with clean licensing
  SAY      Udio still generates, but downloads are disabled following its
           settlement, so anything made there cannot be exported. It is
           covered in this system only as a cautionary case.
  MARK     [OFFICIAL + COMMUNITY] — see DATA_LEGAL §7 for the sourcing
  WHERE    DATA_LEGAL

─── 13 · MUSICFX AND MUSICFX DJ ───
  FIND     MusicFX · MusicFX DJ · "MusicFX DJ in AI Studio" as a live tool
  REPLACE  Google Flow Music; for interactive streams, Lyria RealTime
  SAY      Both products were retired as Google consolidated its music tools
           into Flow Music.
  WHERE    DATA_GOOGLE

─── 14 · PRODUCER.AI AND RIFFUSION ───
  FIND     Riffusion or Producer.ai named as current services
  REPLACE  Google Flow Music
  SAY      One product, three names: Riffusion became Producer.ai, Google
           acquired it, and it is now Flow Music. Not three competitors.
  ⚠️ NEVER  Never emit a web address for anything trading under the Riffusion
           name. Several such sites are live and selling subscriptions with no
           verifiable connection to the original project — no named company,
           no stated affiliation. Direct users to Flow Music by name only.
  WHERE    DATA_GOOGLE

─── 15 · OLD MENU NUMBERS ───
  FIND     a guide instructing "press 10" and meaning audit
  REPLACE  audit is [12]
  SAY      The guide predates the current menu. Numbers are frozen now and
           will not move again.
  WHERE    CORE_00 §4 and §10

─── 16 · PROMPTS CUT TO A LIMIT THAT DOES NOT EXIST ───
  FIND     a Style prompt visibly truncated to a round number of characters,
           or a user stating a character ceiling as a rule
  REPLACE  rebuild the prompt at the length the content needs
  SAY      The strict short ceiling taught by earlier guides — including
           earlier versions of this system — was never measured. It made
           people cut prompts well below the range that actually steers the
           result. Front-loading matters; that arbitrary ceiling did not.
  WHERE    DATA_SUNO §2 for what is actually known about length

─── 17 · ADHERENCE PERCENTAGES ───
  FIND     "88% prompt adherence" or any similar cited accuracy figure
  REPLACE  delete the number
  SAY      No such metric is published. The figure has no traceable source.

─── 18 · WRONG PLAN FOR A FEATURE ───
  FIND     a claim that a given feature comes with a particular subscription
  REPLACE  the current tier for that feature
  SAY      Plan mapping has changed more than once and getting it wrong costs
           the user real money in the wrong direction.
  WHERE    DATA_SUNO — do not state tiers from memory, read them there

─── 19 · CREDIT COSTS QUOTED FROM GUIDES ───
  FIND     a specific per-generation credit cost for a feature
  REPLACE  point the user at their own account
  SAY      Several widely repeated figures are contradicted by other guides
           and were never published by the vendor.
  WHERE    DATA_SUNO

─── HOW TO APPLY THE TABLE ───

  1. Repair silently in bulk. Do not narrate nineteen rows.
  2. Group the explanation: "I removed the bracketed parameters — none of
     those were ever read — and rewrote them as description."
  3. Never return only a diagnosis. Always return the repaired prompt.
  4. If a repair changes what the user asked for musically, ask first. If it
     only changes syntax, just do it.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. TRIGGER WORDS — the single copy
═══════════════════════════════════════════════════════════════════

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

─── THE PRINCIPLE ───

State what you want, not what you are afraid of.

  ❌  no clipping, no distortion, no background noise
  ✅  balanced dynamics, clean tone, consistent volume, warm and full

─── CONFIDENCE ───

[COMMUNITY] — reported consistently across independent guides and matching a
well-known behaviour of generative models generally. No controlled test of the
specific word list has been published. Treat it as a sound writing habit rather
than a mechanism: positive phrasing is better prompt-writing regardless of
whether the effect is as strong as claimed.

─── WHERE THIS DOES NOT APPLY ───

The Exclude Styles field is a real negative field with its own behaviour, and
it takes musical categories rather than defect words. Both the field and what
to put in it are documented in DATA_SUNO §3. The list above is about the Style
text, not that field.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. FAILURE MODES
═══════════════════════════════════════════════════════════════════

<rag_zone id="failure_modes">

Matched by what the user describes hearing.

─── LYRICS COME OUT AS NONSENSE, OR WORDS GO MISSING ───

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

─── UNASKED-FOR TALKING, DIALOGUE OR NARRATION ───

  SYMPTOM   Spoken passages nobody requested; the model narrating.
  CAUSE     Instructions that were readable as lyrics, or structural labels
            malformed enough to be sung.
  FIX       - Round brackets: check nothing in them is an instruction (§2
              check 5). "(play guitar softly)" gets sung, verbatim.
            - Use clean section labels. `[Verse]` rather than an improvised
              label the model may read as words.
            - If the track should have no speech, say so positively in Style:
              "sung throughout, no spoken passages".

─── QUALITY DEGRADES OVER A LONG WORKING SESSION ───

  SYMPTOM   Later generations worse than earlier ones with the same prompt;
            labels ignored more often; nonsense creeping in.
  CAUSE     [COMMUNITY] Accumulated session state.
  FIX       1. Copy the prompt and any edits somewhere outside the browser.
            2. Full page refresh.
            3. Paste back and regenerate.
  PREVENT   Refresh every ten to fifteen generations. Keep prompts in your own
            notes rather than relying on history. Short sessions beat marathons
            — for the tool and for your ears.

─── A SUDDEN LOUD FINISH NOBODY ASKED FOR ───

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
              track (values by goal: DATA_SUNO §7).
  NOTE      Repeated extension compounds this. Past two, regenerating whole
            usually beats extending again [COMMUNITY].

─── VOCALS IN A TRACK THAT SHOULD BE INSTRUMENTAL ───

  SYMPTOM   Singing, humming or wordless vocal in an instrumental.
  FIX       Three layers, all three at once [COMMUNITY]:
            1. the instrumental switch in the interface
            2. `[Instrumental]` in the Lyrics field
            3. "instrumental, no vocals" stated in Style
            Any one alone leaks occasionally. Together they hold.
  NOTE      On Lyria there is no switch — the word "instrumental" in the
            prompt is the mechanism [OFFICIAL]. See DATA_GOOGLE.

─── THE TRACK IS TECHNICALLY FINE AND COMPLETELY BORING ───

  SYMPTOM   Nothing wrong, nothing interesting. Generic.
  CAUSE     Almost always an under-specified Style field, not a model problem.
  FIX       - Apply Time & Place: era plus scene instead of a genre name
            - Replace generic instrument names with playing-style descriptors
            - Add a production signature — the room, the era, the tape
            - Give the singer a biography instead of a gender
            - Raise the experimental slider modestly
  WHERE     CORE_01 §3, §5, §7, §9

─── THE TRACK LOSES ITS CHARACTER PART WAY THROUGH ───

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
            weaker than the one before it. That is ordinary variance, it does
            not arrive on a schedule, and it is not a documented condition.

  IF IT HAPPENS TO YOU:
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
            add anti-drift machinery to every prompt by default.

─── A METALLIC RING ON THE HIGH END ───

  SYMPTOM   A glassy, ringing quality on cymbals and vocal sibilance.
  STATUS    [COMMUNITY] Widely reported on older models, reported as much
            improved since. Whether it persists is not settled.
  FIX       - Lower the experimental slider
            - Regenerate with a defined vocal persona
            - If it survives: pull stems and treat the top end outside the
              platform (DATA_POSTPROD)

─── SECTION LABELS SEEM TO BE IGNORED ───

  SYMPTOM   Structure does not match the markup.
  CAUSE     Labels are probabilistic hints, not commands (CORE_00 §7 rule 10).
            Some proportion will not land, on any platform, always.
  FIX       - Confirm each label sits on its own line above its section
            - Confirm labels are not duplicated by the editor (CORE_02 §2)
            - Confirm the lyric is long enough for the structure requested
            - Generate several takes and choose
  DO NOT    Do not stack more modifiers in response. That is not a fix, and it
            has no evidence behind it in either direction (CORE_02 §4).

─── THE VOICE IS THE WRONG GENDER ───

  FIX       1. Delete every gender negative.
            2. State the wanted voice positively, early in the description.
            3. Use the interface gender selector — the most reliable control
               available (DATA_SUNO §7).
            4. Give the singer a persona rather than a label (CORE_01 §7).

─── A TRAINED VOICE OR CUSTOM MODEL DOES NOT SOUND RIGHT ───

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

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. WHAT IS NOT A DEFECT
═══════════════════════════════════════════════════════════════════

<rag_zone id="not_a_defect">

An audit that flags everything unusual is worse than no audit, because the user
stops reading it.

─── VARIATION BETWEEN TAKES ───
Two generations from one prompt differ. That is the tool working as designed,
and it is why this system asks for several takes rather than one.

─── AN UNUSUAL GENRE PAIRING ───
Incompatible pairs are expensive, not forbidden (CORE_01 §10). Say it will
take more takes; do not "correct" it.

─── AN UNDOCUMENTED TECHNIQUE THAT WORKS FOR THE USER ───
Pipe stacking is the standing example. Genuinely unsettled, no primary source
on either side (CORE_02 §4). If a user's prompts use it and they are happy,
leave it. Unproven is not the same as broken.

─── A LONG PROMPT ───
Length alone is not a defect. Contradiction is. Ten descriptors pulling in one
direction is fine; four pulling in different directions is not.

─── DELIBERATE ROUGHNESS ───
"Lo-fi", "demo", "unmastered", "bedroom recording" are aesthetic choices.
Do not repair them into polish.

─── NON-ENGLISH LYRICS ───
Not a defect and not a warning. If the user writes in another language, state
the language in the Style field so the delivery matches. On Lyria the supported
language list is in DATA_GOOGLE.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. PLATFORM-SPECIFIC PROBLEMS
═══════════════════════════════════════════════════════════════════

<rag_zone id="platform_troubleshoot">

─── LYRIA ───

  STRUCTURE IGNORED
    Use timestamp markers rather than described sections. One event per
    marker, plainly stated. Do not overload a single marker.
    Syntax: DATA_GOOGLE [OFFICIAL].

  RESULT IS GENERIC
    Time & Place works here too. Describe the shape over time — what is thin
    at the start and what has arrived by the middle. Consider generating the
    instrumental first and the vocal as a separate pass.

  THE PROMPT IS REFUSED OR RETURNS NOTHING
    Remove real artist names — they are filtered [OFFICIAL]. Replace with era
    and scene descriptions (CORE_01 §12).
    Remove any exclude list; negatives are unsupported and may confuse the
    parse rather than being harmlessly ignored.

  TEMPO NOT LANDING
    Describe it rather than numbering it (§3 row 11).

─── GOOGLE FLOW MUSIC ───

  A REPLACE BREAKS THE MIX
    Scope the instruction tightly — name the one part to change, and name
    what must stay untouched.

  AN EXTENSION CHANGES STYLE
    Restate the style anchor inside the extension instruction. Do not assume
    continuity is inherited.

─── ELEVENMUSIC ───

  VOCAL LACKS EXPRESSION
    A known trade-off in exchange for clean licensing and consistency. For
    expressive lead vocals, consider generating elsewhere. Section-by-section
    regeneration is its real strength — use it (DATA_OTHER).

─── STABLE AUDIO ───

  UNWANTED VOCAL ARTEFACTS
    Primarily an instrumental and sound-design tool. State "instrumental"
    explicitly and keep vocal language out of the prompt entirely.

─── SUNO ───

  Suno-specific interface behaviour, field limits, sliders and features are
  documented in DATA_SUNO. This file covers only what is diagnosable from the
  text of a prompt.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. FAST TRIAGE
═══════════════════════════════════════════════════════════════════

<rag_zone id="triage_index">

  SYMPTOM                                  GO TO
  ──────────────────────────────────────── ──────────────────────────────
  Generic, boring, characterless           §5 · then CORE_01 §3
  Wrong vocal gender                       §5 · §3 row 8
  Muddy, too many instruments              §2 check 3
  Structure not followed                   §5 · CORE_02 §3
  Nonsense lyrics, missing words           §5
  Unwanted talking                         §5 · §2 check 5
  Vocals in an instrumental                §5
  Loud unrequested finish                  §5
  Quality falling over a session           §5
  Metallic high-end ring                   §5
  Character fades later in the track       §5 — read the status note
  Old prompt behaving oddly                §3 — run the whole table
  Prompt aimed at the wrong platform       §2 check 12 · §3 rows 9–11
  A guide contradicts this system          §3 rows 16–19 · DATA_SUNO §13

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF CORE_03_DIAGNOSE.md · SunoForge v3.0
// Next: DATA_GOOGLE_2026-07.md
// ═══════════════════════════════════════════════════════════════
