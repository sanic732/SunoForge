---
file_id: DATA_GOOGLE
version: "3.0"
layer: data
valid_as_of: "2026-07-27"
expires: "Google renamed this product line twice and retired two products in the twelve months before this date — verify everything here before trusting it after 2026-10"
scope: lyria_3_family · flow_music · timestamp_prompting · multimodal · vocal_control · retired_products
key_concepts: [lyria_3_pro, lyria_3_clip, lyria_realtime, flow_music, timestamp_prompting, google_formula, descriptive_tempo, multimodal_input, synthid, c2pa, musicfx_retired]
depends_on: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE, DATA_OTHER, DATA_POSTPROD, DATA_LEGAL]
rag_priority: critical
authority: "THIS FILE IS THE SINGLE SOURCE OF TRUTH FOR LYRIA AND FLOW MUSIC SPECIFICATIONS"
updated: "2026-07-27"
---

# 🔵 SUNOFORGE v3.0 — GOOGLE PLATFORM DATA
# File 7 of 12 · DATA layer · valid as of 2026-07-27

> ⚠️ **Expiry notice.** This is a snapshot. In the year before this date Google
> acquired a music company, renamed its product twice, retired two products,
> and shipped a family of models still labelled preview. If today is more than
> a quarter past the date above, treat every number here as a starting
> hypothesis. Replace this file; leave the CORE_* files alone.

> 📌 **Single source rule.** Lyria model identifiers, durations, sample rates,
> language lists and Flow Music mechanics live here and nowhere else. If you
> find them repeated in another file, that is a defect — delete the copy and
> link here.

> 📖 **Primary source.** Unlike every other platform this system covers, Google
> has published an actual prompting guide (April 2026) [OFFICIAL]. Where this
> file says [OFFICIAL] about prompting technique, that guide is why. It
> outranks any community guide, including the earlier editions of this system.

═══════════════════════════════════════════════════════════════════
§1. THE LYRIA 3 FAMILY
═══════════════════════════════════════════════════════════════════

<rag_zone id="lyria_family">

Three models with different jobs. All three carry a preview or experimental
label, which means specifications can move without notice.

─── LYRIA 3 PRO ─── [OFFICIAL] released 2026-03-25

  Identifier      lyria-3-pro-preview
  Maximum length  184 seconds
                  (the prompting guide rounds this to "up to three minutes")
  Audio out       MP3 · 44.1 kHz · 192 kbps
  Input           text · PDF · up to 10 reference images
  Languages       English, German, Spanish, French, Hindi, Japanese,
                  Korean, Portuguese — eight, with more stated as coming
  Status          Preview, available globally
  Provenance      SynthID watermark on every output, plus C2PA signed
                  metadata. The watermark cannot be removed.

  CAN DO: text to music · image to music · vocals and instrumental · write
  its own lyrics or perform yours · timed structural control · multi-vocal
  conditioning · prompt rewriting.

─── LYRIA 3 CLIP ─── [OFFICIAL]

  Identifier      lyria-3-clip-preview
  Length          30 seconds, fixed
  Audio out       MP3 · 48 kHz stereo
  Input limit     131,072 tokens
  Status          Preview

  ⚠️ NAMING. Google's own prompting guide calls this model simply "Lyria 3",
  without the word Clip. The API identifier says clip. Both names refer to the
  same 30-second model. When a user says "Lyria 3" they may mean the short
  model or the family — ask.

  ⚠️ SAMPLE RATE, COUNTER-INTUITIVELY. Clip outputs at the higher sample rate,
  Pro at the lower. This looks backwards and it is easy to state from memory
  the wrong way round. Earlier working notes for this system got it wrong in
  exactly that direction.

─── LYRIA REALTIME ─── [OFFICIAL] experimental

  Identifier      lyria-realtime-exp
  Type            continuous interactive stream over a WebSocket connection
                  through the Gemini API
  Audio           48 kHz raw PCM, 16-bit, stereo at the model
                  a client may request 44.1 kHz when opening the stream
  Latency         around two seconds for a change to take effect [COMMUNITY]

  ⚠️ Both sample-rate figures are correct and describe different things: the
  model's own rate, and what the client asks for. Earlier editions treated
  this as a contradiction to be resolved. It was not one.

  WHAT IT IS: an instrument, not a track generator. An endless instrumental
  stream you steer while it plays.
  WHAT IT IS NOT: a way to produce a finished song. There is no file at the
  end unless you record the stream.
  VOCALS: none. Vocal-like output is abstract timbre, not sung words.

  ALSO: Magenta RealTime is Google's open counterpart in this space.

─── WHAT DOES NOT EXIST ───

There is no published successor to Lyria 3 as of this file's date, and no
announced date for one.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. SURFACES — where these models are reachable
═══════════════════════════════════════════════════════════════════

<rag_zone id="surfaces">

[OFFICIAL] The Lyria 3 family appears across a wide set of Google products
rather than in a single app:

  Gemini                          conversational access
  Google Flow Music               the dedicated music workspace (§5)
  Google Vids                     soundtracks inside the video editor
  Dream Track                     music creation inside YouTube Shorts
  AI Studio                       developer playground
  Vertex AI                       API access, plus the Media Studio playground
  Gemini Enterprise Agent Platform  agent-based access

WHAT THIS MEANS IN PRACTICE: the same model behaves differently depending on
the surface, because each wraps it with its own controls. A prompt tuned in
the API may need adjusting in a consumer surface, and vice versa.

─── PRICING ───

⚠️ Google has not published consumer pricing or plan limits for music
generation in a form this system can cite. Do not state a price, a credit
cost, or a free-tier allowance for any Google music surface. If a user asks,
tell them it is not published and point them at their own account.

Access generally requires a paid Gemini tier or a billed cloud project, but
the specifics are not documented well enough to state. [UNVERIFIED]

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. PROMPTING LYRIA — the official framework
═══════════════════════════════════════════════════════════════════

<rag_zone id="google_framework">

[OFFICIAL] Google's recommended prompt skeleton:

```
[Genre and style] + [Mood] + [Instrumentation] + [Tempo and rhythm]
+ [Vocal style and language] + [Lyrics]
```

  GENRE AND STYLE   the primary category, stated plainly
  MOOD              the emotional intent
  INSTRUMENTATION   the instruments that drive the track. If you name none,
                    the model picks defaults from the genre.
  TEMPO AND RHYTHM  speed, pace and groove — in descriptive words
  VOCAL             gender, tone, delivery, language
  LYRICS            a theme to write from, or your own words to perform

How this compares to the six-layer framework used elsewhere in this system,
and when to use which, is in **CORE_01 §2**.

─── THE FOUR STATED BEST PRACTICES ───

[OFFICIAL] Google's own guidance, in its own priority order:

  1. BE DESCRIPTIVE AND SPECIFIC. More detail produces a closer match. This
     is the opposite of the "keep it short" instinct many users bring from
     other platforms.
  2. NAME THE GENRE AND THE ERA. Both. A stylistic timeframe is explicitly
     called for — which is independent confirmation of the Time & Place
     approach this system has used since v1.1 (CORE_01 §3).
  3. NAME THE KEY INSTRUMENTS.
  4. ITERATE. Adjust keywords rather than rewriting from scratch.

─── TEMPO IS DESCRIBED, NOT NUMBERED ───

[OFFICIAL] This is the single most important difference from Suno, and the
most common cross-platform mistake.

    ✅  a fast, energetic pace with a driving beat
    ✅  a slow, swaying tempo
    ✅  unhurried, with a heavy backbeat

    ❌  140 BPM

  BPM exists as an API parameter. Inside the text of the prompt, Google's
  guidance is natural-language description. On Suno the number is what works
  (DATA_SUNO §2). Carry the habit across and results get worse in both
  directions — this has its own row in the repair engine, CORE_03 §3.

  ⚠️ Earlier editions of this system instructed users to give Lyria an exact
  numeric BPM. That was wrong.

─── INSTRUMENTAL ───

[OFFICIAL] Write the word "instrumental" in the prompt. That is the entire
mechanism. There is no switch, and no tag.

─── WHAT DOES NOT WORK HERE ───

  ❌ NEGATIVE PROMPTING IS NOT SUPPORTED [OFFICIAL]
     Do not emit an exclude list, a "no X" construction, or a negative
     prompt field for Lyria. This is not a weak control — it is absent.
     State what you want instead.

  ❌ REAL ARTIST NAMES are filtered. Describe the era and scene instead
     (CORE_01 §12).

  ❌ SUNO BRACKET MARKUP has no meaning here. Section labels, performance
     notation, pipe stacks and parametric tags are all Suno conventions.
     The one bracketed construction Lyria does document is the timestamp (§4).

─── A WORKED PROMPT ───

Following the framework, all six slots present, tempo described:

```
A late-1970s Laurel Canyon folk song, bittersweet and unhurried. Fingerpicked
nylon-string guitar, brushed drums and a distant pedal steel. A relaxed,
walking pace that never pushes. A female alto voice, unpolished and
conversational, recorded very close, singing in English.
Lyrics: a song about leaving a house you were happy in.
```

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. TIMESTAMP PROMPTING — the structural control
═══════════════════════════════════════════════════════════════════

<rag_zone id="timestamp_prompting">

[OFFICIAL] The documented way to control what happens when. Google presents it
as the workflow for genre shifts inside a track and for scoring video.

─── THE FORMAT ───

```
[MM:SS] a description of what happens at this point
```

A bracketed timestamp, then ordinary prose describing the event. Markers run
from the start of the track to its end, and the final marker sets the ending.

⚠️ NEVER WRITE A MARKER PAST THE MODEL'S CEILING.
  Lyria 3 Pro stops at 184 seconds — the last marker belongs at or before
  `[03:00]`. Lyria 3 Clip stops at 30 seconds, so its whole map lives inside
  `[00:00]`–`[00:30]`.
  A structure running to `[04:00]` describes music the model cannot produce.
  The generation does not fail; it simply ends early and the plan quietly loses
  its last third — the ending you designed never arrives.
  When someone asks for a longer track, say the ceiling out loud and offer the
  choice: compress the structure to fit, or move to a platform that can hold the
  length (§9, and DATA_OTHER for Stable Audio).

─── WHAT A MARKER DESCRIBES ───

An event, not a section name. This is the part that trips up anyone arriving
from Suno: you are not labelling "this is the chorus", you are saying what the
listener hears arrive, leave, or change.

```
[00:00] Opens with a solo pipe organ, slow and unaccompanied.
[00:18] A low string section enters underneath, holding long notes.
[00:44] Drums arrive and the tempo settles into a steady march.
[01:30] Everything drops away except a single voice.
[02:05] The full arrangement returns, brighter than before.
[02:50] Ends on a sustained chord left to decay.
```

─── HOW TO WRITE THEM WELL ───

  - ONE EVENT PER MARKER. Two instructions in one marker compete.
  - COVER THE WHOLE TRACK. Gaps get filled by the model's own judgement.
  - END EXPLICITLY. A final marker describing the ending is how you avoid an
    abrupt cut or an unrequested big finish.
  - SPACE THEM SENSIBLY. Markers a few seconds apart ask for more change than
    a piece of music can absorb.
  - STAY INSIDE THE LENGTH. Markers past the model's maximum have nowhere
    to go (§1).

─── WHAT THIS REPLACES ───

  ❌  Intro (0–15s) · [Verse - 0:15] · [End - 2:15]

Those forms were invented by earlier editions of this system and were never
Google's syntax. Any prompt containing them should be converted — CORE_03 §3
row 9.

─── SCORING VIDEO ───

The reason this workflow exists. Generate or edit the video first, note the
timings of the cuts, then place markers on those timings so the music changes
where the picture does. Google names Veo as the intended companion for this.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. VOCALS AND LYRICS ON LYRIA
═══════════════════════════════════════════════════════════════════

<rag_zone id="lyria_vocals">

─── SUPPLYING LYRICS ───

[OFFICIAL] Introduce your words with a `Lyrics:` prefix. The lines after it are
what the model sings.

```
Lyrics: I counted every window on the way back down the hill
```

  Or describe a theme and let the model write: "a song about meeting someone
  in a city neither of them is from". Both are documented.

─── BACKING VOCALS ───

[OFFICIAL] Requested by describing where you want them. There is no tag.

```
with backing singers echoing the last line of each chorus
```

─── CONTROLLING THE VOICE ───

[OFFICIAL] Four dimensions, all in plain description:

  DEMOGRAPHICS AND RANGE   "commanding baritone", "a clear, high soprano"
  TIMBRE                   "gravelly", "soulful", "breathy"
  PATTERN AND DELIVERY     "fast-paced", "laid-back", "rapping"
  LANGUAGE                 any of the eight supported (§1)

─── THE VOCAL ARC — a voice that changes across the track ───

[OFFICIAL] The capability with no equivalent elsewhere in this system's
coverage: direct the voice to change over the length of the song.

```
The vocal starts out confident but gets calmer and quieter as the track
progresses.
```

  This is documented, not inferred. It pairs naturally with timestamp markers,
  and it is the long-form relative of per-section delivery direction on Suno
  (CORE_02 §6). Method side: CORE_01 §6.

─── MULTI-VOCAL AND MULTILINGUAL ───

[OFFICIAL] Multiple voices are supported in one track, and they do not have to
share a language. Google's own example pairs a male vocalist singing in
English with a female vocalist singing in French inside a single song.

This is worth knowing: a cross-language duet is difficult to achieve anywhere
else in this system's coverage.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. MULTIMODAL INPUT
═══════════════════════════════════════════════════════════════════

<rag_zone id="multimodal">

[OFFICIAL] Lyria accepts more than text:

  TEXT      the prompt itself
  PDF       a document establishing the emotional baseline
  IMAGES    up to ten reference images

  ⚠️ PDF input was in none of the three research reports behind this build and
  is absent from every community guide checked. It is documented by Google.

─── HOW IMAGE INPUT IS MEANT TO BE USED ───

Not as a style reference in the way image models use them — as an emotional
and narrative baseline. Google's example asks for a song whose lyrics and mood
match the story told across the attached images.

```
A deeply emotional modern ballad in English. The lyrics and mood should
follow the story in the attached images.
```

─── STILL GIVE IT WORDS ───

An image narrows mood and narrative. It does not specify genre, instruments,
tempo or voice. Supply those in text alongside the images, or the model
chooses them for you.

The translation table for turning what is in a picture into audio decisions is
craft rather than platform data, and lives in **CORE_01 §11**.

─── COMPANION MODELS ───

[OFFICIAL] Google documents three pairings:

  LYRIA + VEO           generate video, then score it to the cut timings
                        using timestamp markers (§4)
  LYRIA + NANO BANANA   generate storyboard images, then a song from them
  LYRIA + GEMINI        hand a creative brief to Gemini and have it write the
                        detailed Lyria prompt, and the lyrics if wanted

  The third is notable: a vendor documenting one model as the prompt engineer
  for another. That is exactly what this system is, described in Google's own
  documentation.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. GOOGLE FLOW MUSIC
═══════════════════════════════════════════════════════════════════

<rag_zone id="flow_music">

─── ONE PRODUCT, THREE NAMES ───

[OFFICIAL] This lineage causes more confusion than anything else in this file,
because all three names are still in circulation and are frequently written
about as if they were competing products:

```
Riffusion          open project, December 2022
    ↓ relaunched
Producer.ai        July 2025
    ↓ acquired by Google, 2026-02-24 — team joined Google Labs
Google Flow Music  renamed April 2026
```

  Verified: the old address redirects permanently to the current one. It is
  one product.

  ⚠️ From 20 February 2026 all past generations, sessions, trained models and
  media from the previous incarnations became inaccessible. Anyone still
  expecting to retrieve old work should be told plainly that it is gone.

  ⚠️ Riffusion as an independent service has not existed since February 2026.
  Sites currently trading under that name and selling subscriptions have no
  verifiable connection to the original project — no named company, no stated
  affiliation. **Never emit a web address for any of them.** Mention Riffusion
  only as the origin of Flow Music. [UNVERIFIED as to what those sites are]

  It now runs on Google's own models — Gemini, Lyria 3, Veo and Nano Banana.

─── WHAT IT DOES ───

[COMMUNITY, July 2026] Following the Spaces update in late July, a single
workspace holds:

  GENERATE   a track from a prompt
  COVER      re-record an existing piece in a different style
  REPLACE    swap one part without regenerating the whole track
  EXTEND     grow the arrangement section by section
  STEMS      separate the parts
  IMAGES     artwork generation
  LYRICS     writing and editing
  VIDEO      video generation alongside the music

  Spaces began as a collaboration feature and became the studio itself.

─── ⚠️ WHAT IS NOT PUBLISHED ───

**Maximum track length and plan limits are not published by Google.**

Earlier editions of this system stated "up to five minutes". No source
supports it. Do not repeat it. If a user needs a specific maximum length,
tell them it is undocumented and they should test it in their own account.
[UNVERIFIED]

─── THE WORKFLOW ───

The point of Flow Music is that you do not regenerate. Each step preserves
what came before:

```
1  SEED      a narrative prompt produces an instrumental skeleton
2  REPLACE   name one part and what should be there instead
3  EXTEND    grow the arrangement forward
4  EDIT      stems, effects, artwork, video — in the same Space
5  EXPORT    out to a DAW
```

─── WRITING A REPLACE INSTRUCTION ───

Scope it tightly, and say what must survive:

    ✅  Replace only the guitar solo with a slower, more melodic line.
        Keep the drums and bass exactly as they are.
    ❌  Make the solo better

  A broad instruction invites the model to reconsider the whole mix, which is
  the most common complaint about this feature (CORE_03 §7).

─── WRITING AN EXTEND INSTRUCTION ───

Restate the style anchor. Continuity is not inherited as reliably as users
expect:

    ✅  Continue in the same late-70s folk style, same tempo and
        instrumentation, building toward a final chorus.

─── WHEN FLOW MUSIC INSTEAD OF SUNO ───

  ✅ You need to change one part without losing the rest
  ✅ You want music, artwork and video produced in one place
  ✅ You are working inside Google's tools already

─── WHEN SUNO INSTEAD ───

  ✅ The vocal is the point and it needs character
  ✅ You need your own voice or a model trained on your catalogue
  ✅ You need multitrack or MIDI export, or a full editing surface
     (features and tiers: DATA_SUNO §8)

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. RETIRED AND CONSOLIDATED
═══════════════════════════════════════════════════════════════════

<rag_zone id="retired">

─── MUSICFX AND MUSICFX DJ — CLOSING 31 JULY 2026 ───

[OFFICIAL] Both retired as Google consolidates its music tools into Flow
Music.

  ⚠️ Earlier editions of this system recommended MusicFX DJ in AI Studio as
  the no-code interface for the realtime model. That recommendation dies with
  the product. For interactive streaming, use the realtime model directly
  (§1); for everything else, Flow Music.

  If a user mentions either product, they are working from a guide written
  before this date. Repair: CORE_03 §3 row 13.

─── OTHER MOVEMENTS ───

  [COMMUNITY] Google entered a partnership with Believe in May 2026.
  [COMMUNITY] Mobile applications for Flow Music and Gemini Omni were shown
  at I/O 2026.

  Neither changes how anything is prompted. Both are recorded here so that a
  stale copy of this file can be diffed against reality quickly.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§9. CHOOSING WITHIN THE GOOGLE FAMILY
═══════════════════════════════════════════════════════════════════

<rag_zone id="google_selector">

  A 30-second sketch, jingle, or loop            → Lyria 3 Clip
  A complete piece up to the Pro maximum          → Lyria 3 Pro
  A soundtrack that must hit video cut points     → Lyria 3 Pro + timestamps
  Music from photographs or a document            → Lyria 3 Pro, multimodal
  A track to be edited part by part after         → Flow Music
  Music, artwork and video in one workspace       → Flow Music
  An endless stream to steer live                 → Lyria RealTime
  Adaptive music inside a game or installation    → Lyria RealTime

─── WRITING FOR THE 30-SECOND MODEL ───

Thirty seconds is one idea, not a compressed song. A verse-chorus structure
does not fit and asking for one produces a rushed sketch of both.

    ✅  One riff, one texture, one mood, seen through.
    ✅  For loops: say it should start and end seamlessly with no hard stop.
    ✅  For backing beds: say it should stay out of the way and avoid sudden
        transitions.

─── CROSS-PLATFORM ADAPTATION ───

Converting a Suno prompt for Lyria:

  REMOVE   bracket markup, performance notation, exclude lists, slider
           values, numeric BPM, any parametric tag
  KEEP     the genre, mood, instrumentation and vocal description — the
           six-layer content survives; only its packaging changes
  ADD      descriptive tempo, timestamp markers for structure, a `Lyrics:`
           prefix, an explicit language

  The reverse direction — Lyria to Suno — means moving structure out of
  timestamps and into section labels (CORE_02), and converting the tempo
  description to a number.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§10. WORKED EXAMPLES
═══════════════════════════════════════════════════════════════════

<rag_zone id="google_examples">

Complete prompts, ready to adapt. Each one follows the framework in §3 and
demonstrates one capability.

─── 1 · A 30-SECOND LOOP ───

For the short model. One idea, seamless, no structure:

```
A mellow lo-fi hip-hop loop for studying. Dusty jazz piano chords, a warm
sub-bass and a muffled boom-bap drum break, with vinyl crackle over
everything. A slow, unhurried pace that stays exactly the same throughout.
Starts and ends seamlessly with no hard stop. Instrumental.
```

  Note what is absent: no sections, no build, no vocal, no ending. Thirty
  seconds cannot hold an arc, and asking for one produces a rushed sketch.

─── 2 · A JINGLE WITH ONE HIT POINT ───

```
A bright, optimistic corporate opener. Plucked marimba and light strings over
a soft electronic pulse, with a single warm brass swell. Begins almost bare,
gathers gradually, and lands on one clear accent shortly before the end, then
resolves immediately. A brisk, forward-moving pace. Instrumental.
```

─── 3 · A FULL SONG, FRAMEWORK ORDER ───

All six slots, tempo described, lyrics supplied:

```
A late-1990s Bristol trip-hop track, heavy and nocturnal. Dusty breakbeat
drums, a deep detuned bassline, a filtered Rhodes and a distant string
sample. A slow, dragging pace that sits well behind the beat. A female alto,
breathy and close, singing in English with almost no projection.
Lyrics: a song about walking home through a city at four in the morning and
not minding.
```

─── 4 · SCORING VIDEO TO CUT POINTS ───

The workflow timestamps exist for. Note the cut times from the edit first,
then place a marker on each one:

```
A tense, modern orchestral cue for a chase sequence. Low strings, taiko
percussion and a rising synthetic drone. Instrumental.

[00:00] A single sustained low string note, almost still, with faint
        percussion underneath.
[00:07] A pulse enters in the low strings, quiet but insistent.
[00:19] Percussion arrives hard and the tempo doubles.
[00:34] Everything cuts to near-silence except a single high sustained note.
[00:38] Full orchestra and drums return at maximum intensity.
[00:52] Ends abruptly on a single accented hit, no decay.
```

  The abrupt ending is stated deliberately. Without a final marker the model
  chooses its own resolution, and a resolved ending under an unresolved
  picture is the most common failure in scoring work.

─── 5 · A GENRE SHIFT INSIDE ONE TRACK ───

The other reason timestamps exist:

```
[00:00] Solo classical guitar, warm and intimate, playing a slow melody
        alone in a quiet room.
[00:25] A double bass and brushed drums join, turning it into a relaxed
        jazz trio.
[00:55] The drums switch to a hard modern beat and a deep synthetic bass
        replaces the double bass. The guitar keeps its melody unchanged.
[01:35] Everything strips back to the solo guitar from the opening.
[01:55] Ends on a single held chord.
```

  Keeping one element constant across the change — here the guitar melody —
  is what makes it read as one piece rather than three clips.

─── 6 · MUSIC FROM IMAGES ───

```
A warm, nostalgic acoustic song in English. Acoustic guitar, upright piano
and a little brushed percussion. An unhurried, gentle pace. A male tenor,
soft and slightly worn. The lyrics and the emotional arc should follow the
story told across the attached images.
```

  The images carry mood and narrative. Everything else still has to be said.

─── 7 · A BED UNDER A VOICEOVER ───

```
A calm, understated ambient bed for a documentary voiceover. Sustained warm
pads, a sparse piano figure and almost no percussion. A very slow, even pace
with no sudden changes. Nothing should draw attention to itself.
Instrumental.

[00:00] Almost silent — a single pad fading in.
[00:20] A quiet piano figure begins, repeating gently.
[01:00] A low string layer joins underneath, still very restrained.
[01:40] Gradually thins back out to the opening pad.
```

  "Nothing should draw attention to itself" is doing real work. Without an
  instruction of that kind, a generative model writes music that wants to be
  listened to, which is the opposite of what a bed is for.

─── 8 · A STEERED REALTIME STREAM ───

Opening prompt:

```
A continuous instrumental stream for a dark fantasy game: low strings, distant
brass and sparse percussion, tense but slow, leaving plenty of space.
```

Steering it while it plays:

```
raise the intensity and bring in fast percussion
drop back to almost nothing, just the low drone
shift to something warmer and more hopeful
```

  Changes take a couple of seconds to take effect (§1), which matters if you
  are triggering them from game events — cue the change slightly early.

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_GOOGLE_2026-07.md · SunoForge v3.0
// Snapshot date 2026-07-27 · replace this file, not the CORE files
// Next: DATA_OTHER_2026-07.md
// ═══════════════════════════════════════════════════════════════
