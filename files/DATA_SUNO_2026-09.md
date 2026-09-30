---
file_id: DATA_SUNO
version: "4.0"
layer: data
role: adapter
description: >
  Every Suno fact the system uses, as of 2026-09-30: the v6 model family and the
  retirement of all earlier models, field limits, Exclude Styles, Max Mode, Variety,
  Duration, sliders, Voices, Custom Models, plain-language editing, Studio 2.0, stems,
  the lyrics editor, what each plan unlocks, download-bound rights, and the myths.
  Read for any Suno target. The single source of truth for Suno versions and limits.
valid_as_of: "2026-09-30"
expires: "Suno replaced its whole model line on 2026-09-09 and ships user-facing changes every few weeks — verify anything here after 2026-12"
scope: suno_v6 · fields · max_mode · variety · duration · sliders · voices · custom_models · editing · studio_2 · stems · plans · downloads
key_concepts: [version_matrix, v6, v6_wild, v6_mini, retired_models, style_field, exclude_styles, max_mode, variety_slider, duration, sliders, voices, custom_models, plain_language_edit, mashup, sample, references, studio_2, stems, lyrics_editor, plans, download_limits, myths]
depends_on: [CORE_00_ENTRY]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE, DATA_RECIPES, DATA_POSTPROD, DATA_LEGAL, DATA_OTHER]
rag_priority: critical
authority: "THIS FILE IS THE SINGLE SOURCE OF TRUTH FOR SUNO VERSIONS, LIMITS AND PLAN GATING"
updated: "2026-09-30"
---

# 🟠 SUNOFORGE v4.0 — SUNO PLATFORM DATA
# File 6 of 12 · DATA layer · valid as of 2026-09-30

> ⚠️ **Expiry notice.** Everything in this file is a snapshot. On 2026-09-09 Suno
> retired every model it had and replaced them with the v6 family; in the eight weeks
> before that it rebuilt Studio, rewrote its terms and capped downloads. If today is
> more than a quarter past the date above, treat every number here as a starting
> hypothesis, not a fact. Replace this file; leave the CORE_* files alone.

> 📌 **Single source rule.** Model names, field limits and plan gating live here and
> nowhere else. If you find them repeated in another file, that is a defect — delete
> the copy and link here instead.

> 💲 **No prices.** This file names plans because features and rights depend on them.
> It never states what a plan costs: that differs by country and changes without
> notice. Credits are mentioned only where they change a decision.

## §1. VERSION MATRIX

[OFFICIAL] Released 2026-09-09 as "a new generation of music models developed with
our industry partners, including Warner Music Group, BMG and Believe".

─── v6 — DEFAULT ─── Pro and Premier
  "our flagship model… reliable, precise and consistently delivers polished music
  across every genre and style. When you know what you want, v6 helps you get there."
  Help center: "Suno's latest model. Recommended for most songs."

─── v6-wild ─── Pro and Premier
  "built for exploration… less predictable and more varied, producing unexpected,
  textured and ambitious results. It gives you new ideas to riff on, build from or
  bring back into v6 for further refinement."
  The CEO, to the press: if you are looking for a specific thing, v6-wild "may not be
  the right thing for you" [COMMUNITY: press interview].

─── v6-mini ─── every plan, including Free
  "our fastest and free version of our premium v6 models"; "A faster, lighter version
  of v6. Good for quick iterations."

─── CUSTOM MODELS ─── Pro and Premier
  Listed in the same picker: "Models trained on your own music." Powered by v6 (§6).

  WHERE: the model picker, top-right corner of the Create form. The choice stays set
  until you change it. [OFFICIAL]
  The picker shows a "Pro" badge on v6 and v6-wild [COMMUNITY + first-hand].

─── EVERYTHING BEFORE v6 IS RETIRED ─── [OFFICIAL]
  "All models prior to v6 have been retired, but your songs will still be in your
  library and remain unchanged. You will still be able to listen to, share, remaster
  and cover songs made with old models."
  "You can continue working on songs made with older models, but any new iterations
  will be made with our latest models."

  That covers v5.5, v5, v4.5-all, v4.5+ and everything older. The free tier moved
  from v4.5-all to v6-mini.

  ⚠️ A guide, preset or saved prompt that names v5.5, v5 or v4.5 is describing a
  model you can no longer select. The prompt text may still work; the version label
  does not. Repair: CORE_03 §3.

─── LENGTH ─── [OFFICIAL]
  "up to 8 minutes of music in a single generation across v6, v6-wild, and v6-mini."
  Longer still: Extend continues a song from its end.

─── ONE GENERATION = TWO SONGS ─── [OFFICIAL]
  v6 generations cost the same as the previous models did. Many images or videos in
  one prompt raise the cost.

─── HOW v6 WANTS TO BE ADDRESSED ─── [OFFICIAL]
  "v6 understands more of the language and building blocks musicians use, from
  vocals, instrumentation and structure to mood, references and the overall feel of
  a song… Describe what you want and v6 figures out how to get there."
  In Simple mode "you don't need to know which tool to reach for (like Cover, Remix,
  Extend)… The model figures out the workflow if you want it to."
  Suno also says v6 was designed "to support all the ways you have liked creating
  with past models" and links a tutorial on reproducing old-model results.

## §2. THE STYLE FIELD — limits, weighting, and the myth

WHAT IS ACTUALLY KNOWN:

  [OFFICIAL]   Suno publishes no numeric character limit for Style or Lyrics.

  [COMMUNITY]  Field limits observed on v6: Style 1,000 characters · Lyrics 5,000 ·
               Exclude Styles 1,000 · the Simple-mode prompt 3,000 — reported as
               unchanged from v5.5. Observed, not vendor-stated.

  [COMMUNITY]  Measurable influence fades well before the hard limit. Pre-v6 testing
               put the practical ceiling near 300–400 characters; nobody has re-run
               that on v6.

  [UNVERIFIED] "Attention collapses after 200 characters." No controlled test ever
               supported a cliff at that number, and none exists for v6. An earlier
               edition of this system taught it and was wrong.

LONG OR SHORT ON v6?
  [OFFICIAL]  Suno's direction is natural language: describe the song the way a
              musician would; complex, multi-part instructions are welcome.
  [COMMUNITY] One tester (sponsored by Suno, ~150 songs) found a four-word style no
              clearly worse than a detailed one on the same lyrics.
  [COMMUNITY] Another guide recommends per-instrument, per-section sentences and
              "say everything twice" — once in Style, once in the matching section
              label.
  [COMMUNITY] Users quoted on launch: v6 "wants to be directed exactly what to do,
              with little deviation"; others: "Your old prompts won't work."
  None of this is a controlled test. WHAT HOLDS EVERYWHERE: decisions beat
  adjectives, and the first words carry the most weight.

PRACTICAL SHAPE:
  genre + era · mood in 1–2 words · 3–4 instruments · vocal gender and character ·
  production signature · parameters as prose (BPM, key, space)

  ⚠️ Those are slot names, not syntax. The whole thing is one plain sentence, as in
  the example. Bracketed `parameter: value` forms are not read (CORE_02 §1).

  Example:
    mid-90s Seattle grunge, weary and defiant, detuned electric guitar, heavy bass,
    live drums, male baritone with a gravelly worn delivery, analog tape saturation,
    wide stereo field, 92 BPM, D minor

  ⚠️ If the Style text was engineered with care, set Variety to 0 — otherwise v6 may
  rewrite it before generating (§4).

## §3. EXCLUDE STYLES — the negative field

[OFFICIAL, 2024] A dedicated field for styles, instruments or vocal traits to keep
out. Excluded items show with a leading minus: `-piano`. Launched for Pro and Premier
as an early-access beta; Suno asked for likes and dislikes to improve it.
[COMMUNITY, v6] Present in the v6 More Options panel. Current plan gating on v6 is
not stated anywhere official.

[COMMUNITY, v6] Early v6 users call it "far more necessary than previous versions":
asking v6 in the prompt text to remove humming produced more humming; the Exclude
field is the place for it.

WHAT IT IS GOOD AT:
  - removing an instrument the genre would otherwise drag in
  - suppressing a production aesthetic ("polished pop production", "auto-tune")
  - keeping an era out of a period piece

VOCAL GENDER: use the Vocal Gender selector [COMMUNITY — the most reliable control
anyone has found]. Suno's own 2024 tip pairs a positive tag with an exclusion:
"[female vocals]" in Lyrics plus "male vocals" in Exclude Styles [OFFICIAL, 2024].

HOW TO WRITE IT:
  8–12 items, musical vocabulary, not engineering jargon.
  Specific beats generic: "polished pop production" outperforms "pop".

  GOOD: EDM, auto-tune, overproduced, electronic drums, heavy bass, crowd noise
  WEAK: brick-wall compression, dithering, sidechain   ← engineering terms
  WEAK: bad sound, weird, cheap                        ← not musical categories

READY LISTS BY TARGET GENRE:
  Lo-fi / chill      EDM, aggressive, auto-tune, heavy drums, screaming, bright,
                     overproduced, trap bass
  Rock / metal       synth pop, smooth jazz, gentle, lo-fi, whisper vocals,
                     acoustic, mellow, electronic
  Pop / radio        death metal, noise, lo-fi, experimental, drone, harsh,
                     distorted vocals, dissonant
  Jazz               EDM, distorted guitars, auto-tune, screaming, trap, 808,
                     blast beats, overproduced
  Hip-hop / trap     orchestral, acoustic guitar, country, folk, operatic,
                     jazz scat, classical
  Cinematic / epic   lo-fi, bedroom recording, punk, garage, raw, minimal,
                     muffled, thin
  Country            EDM, synthwave, death metal, auto-tune, robotic,
                     electronic drums, dubstep
  Ambient / sleep    drums, vocals, loud, aggressive, fast, energetic, distorted,
                     bass-heavy
  Folk / acoustic    EDM, synthesizers, distortion, electronic drums, auto-tune,
                     stadium reverb, trap hi-hats
  Gospel             lo-fi, whisper, minimal, cold, robotic, distorted, sparse
  Intro humming fix  humming, vocalise, wordless vocals   (v6 launch complaint)

NEGATIVES IN THE STYLE FIELD (as opposed to the Exclude field):
  [COMMUNITY] Weak and sometimes counterproductive on every Suno generation to date.
  Naming a concept can summon it. Keep at most one or two, each right after a strong
  positive statement.

## §4. MAX MODE, VARIETY AND DURATION — the v6 controls

─── MAX MODE ─── [OFFICIAL] since 2026-09-09
  "Max Mode is an option you can turn on for any generation when you want v6 to
  spend more on getting it right. It costs more credits and it's best for: songs
  longer than two minutes, covers where you want the result to stay close to the
  original, transferring the style of one song onto another, and keeping vocals and
  style consistent through the whole track. For quick ideas and shorter songs,
  standard mode is all you need."

  COST: "more credits" [OFFICIAL]. Reported as double a standard generation, with a
  tooltip reading "Uses more compute to maximize consistency throughout the song"
  [COMMUNITY]. Whether it is offered on v6-mini or on Free is not documented.

  WHEN THE SYSTEM RECOMMENDS IT (SUNO_MAX_MODE = "suggest"):
    ✅ target length over two minutes
    ✅ a cover that must stay close to the original
    ✅ moving one song's style onto another
    ✅ a track for release, where the vocal must hold from first line to last
    ❌ sketches, drafts, anything you will regenerate anyway

  ⚠️ NOT THE SAME THING AS THE "MAX MODE" TAGS. `[Is_MAX_MODE: MAX]`,
  `(MAX)(MAX)(MAX)(MAX)` and friends are community folklore from the v4 era — text in
  the prompt that no controlled test ever connected to quality (§14). Suno's toggle
  is a control in the interface. The tags do not switch it on, and Suno has never
  linked the two. Strip the tags; use the toggle.

  Untested: whether Max Mode fixes late-song degradation reported on standard mode.
  Suno's own wording ("keeping vocals and style consistent through the whole track")
  says that is what it is for.

─── VARIETY ─── [OFFICIAL] since 2026-09-09
  "The Variety slider is designed to introduce variety in your outputs by adjusting
  and updating your style prompts. If you'd like to retain full control of your style
  tags, reduce the Variety slider to 0."

  In plain words: above zero, v6 may rewrite your Style text before it generates —
  differently for each take. [COMMUNITY] Observed on camera: Style rewritten at the
  higher settings.

  REPORTED STEPS [COMMUNITY]: Off "Exact style" → Normal "Balanced variety" → High
  "Distinct styles" → Extra "Bold exploration" → Max "Unreasonably varied". Default
  reported as Normal on v6 and v6-mini, Off on v6-wild.

  RULE FOR THIS SYSTEM:
    Engineered Style (recipes, clones, client briefs)  → Variety 0
    Loose idea, happy to be surprised                  → default
    Exploring directions                               → High, or switch to v6-wild

  This is the best-supported v6-specific prompting rule there is: the vendor states
  it. When a user says "Suno ignored my style", check Variety first.

### DURATION
  [OFFICIAL] Added 2026-07-20 for v5.5 on the web, under More Options.
  [COMMUNITY, v6] Present on v6: Auto, or Custom from 10 seconds to 6 minutes, with
  3:00 as the reported default. Step size and mobile availability not documented.
  [OFFICIAL] A single generation can reach 8 minutes; beyond the slider's range,
  length comes from the amount of lyrics, and past 8 minutes from Extend.

  BEHAVIOR [COMMUNITY]:
  - The value is a TARGET, not a guarantee. Long settings often undershoot; give
    enough lyrics to fill it
  - If the audio has not resolved by the target, it can cut abruptly
  - On Auto, v6 tends to come back longer than v5.5 did
  - A widely repeated tip for v6: under about three and a half minutes holds up
    better; for longer pieces, generate the back half separately with Extend — or
    use Max Mode, which Suno aims at exactly this

  PRACTICAL PAIRING:
    Set duration AND give the lyrics to fill it. A 5-minute target with two verses
    produces padding, instrumental drift, or an early cut.
    Rough guide: ~1 minute of song ≈ one verse + one chorus at moderate tempo.

  RELATIONSHIP TO EXTEND: complementary. Duration shapes the first generation;
  Extend adds material to a finished track.

  HISTORY: a 2026-07 first-hand measurement reached 7:59 on the old free model in one
  generation. The claim that the free tier caps near two minutes had no source then
  and has none now.

## §5. VOICES — your own voice

[OFFICIAL] Introduced 2026-03-26. Personas became Voices; "Style Personas are still
available within the Voices menu".

WHO: the plan page lists "Record, upload, and create with your own voice" under Pro
and Premier. Since 2026-08-07 Voices is on iOS and Android and "Now available to try
on free plans. Do more on paid plans." [OFFICIAL]. 18+ only; not offered in every
country [OFFICIAL].

THREE WAYS IN [OFFICIAL]: a voice from a song in your library · record in real time
· upload a file.

INPUT LENGTH [OFFICIAL]: "15 seconds up to 4 minutes"; you pick the best 2 minutes.
  [COMMUNITY] 90–120 seconds of varied singing gives the best result.

AUDIO [OFFICIAL]: acapella with a decent microphone in a neutral room works best.
Backing music is accepted — Suno runs stem extraction to isolate the vocal.

VERIFICATION [OFFICIAL]: "Suno will display a short phrase for you to read aloud.
This spoken recording is compared against your uploaded singing recording to confirm
they are from the same person."
CHECKBOX [OFFICIAL]: you "affirm that you have the rights to use this voice".
TERMS [OFFICIAL]: "you can only create a Voice Model resembling your own voice".
Training: every upload falls under the general content licence in the terms, which
covers improving Suno's models — see DATA_LEGAL §3.

ON v6:
  [OFFICIAL] "If you use Voices, Custom Models, or My Taste, make sure you're on a
  compatible model." The Voices help page still names v5.5 as required — it predates
  v6 and is out of date.
  [COMMUNITY] Existing voices get an "Upgrade Voice to v6" action; the menu shows
  "Voice (new)" and "Style Voice (legacy)"; Voices do not apply to instrumentals.

PRIVACY: only the creator can generate with their voice [OFFICIAL].

COST: no separate price published. Assume normal generation credits.

WORKING WITH VOICES:
  - Draft with stock vocals, switch to your Voice for the final take
  - Audio Influence decides how much of your voice survives; if the result does not
    sound like you, raise it [OFFICIAL troubleshooting tip]
  - It is directional, not exact cloning — expect your character, not your double
  - Give the model range: sing high and low, loud and soft, in the source clip

## §6. CUSTOM MODELS — train on your catalog

[OFFICIAL] Pro and Premier. Upload "as few as six songs" (bulk upload available);
"up to three models"; "about 2-5 minutes" to train; the model appears in the picker.
Private, not shareable.
[OFFICIAL] "You must own the rights to all of the songs you upload." Enforced by
terms, not by a technical check — the responsibility is yours.
[OFFICIAL] Since v6: "Any custom models you've created will automatically get
upgraded so that v6 powers your model moving forward." Songs made with the old model
stay as they were.
[COMMUNITY] The upload screen suggests "24+ songs for best results". Creating a model
costs credits.
[UNVERIFIED] What happens to a model after a copyright complaint is not documented.

[COMMUNITY] 6 is the floor, not the target. Stylistic consistency matters more than
count — a catalog spanning six genres teaches the model to average them.

STRATEGIES:
  "Band" model        6+ tracks by one project → its arrangement habits
  "Beat" model        6+ lo-fi or trap instrumentals → consistent groove and mix
  "Score" model       6+ cinematic pieces → a reusable soundtrack generator
  "Client" model      a client's catalog, with written permission → on-brand music
  Switch models per task rather than building one model for everything.

WHAT IT TRANSFERS: arrangement habits, harmonic tendencies, production texture,
instrument choices. Not lyrics, not melody, not a specific singer.

## §7. EDITING, REMIXING AND REFERENCES ON v6

[OFFICIAL] What v6 added, in Suno's own examples:

| Capability | Suno's example |
|---|---|
| Edit one section in plain language, keep the rest | "Change the chorus so it's sung by a gospel choir" |
| Update a single lyric without rebuilding the song | "Change the lyric from 'love' to 'light'" |
| Mashup from several sources in one request | "Take the vocals from x, drums from y, and add new lyrics about losing control, make it 80s synthwave" |
| Sample, isolate and build a beat in one workflow | "Sample the riff at 0:45, isolate the guitar, build a beat around it" |
| Start from a vibe or a mix of inspirations | "Make a song that feels like midnight on a rooftop" |
| Start from text, audio, images and video | "Make a song based on this image, this audio and my journal entry" |

The help center groups the classic tools under "Remix & Edit — Extend, Cover, Replace
Section, and more, all powered by v6" [OFFICIAL]. The plan table lists Remix (extend,
cover, adjust speed), Basic editing (crop, fade), Advanced editing (replace or add
section), Add vocals, Add instrumental [OFFICIAL].

NOT PUBLISHED: how many sources a mashup takes (the pre-v6 Mashup took "any two
songs"), how long a replaced section may be on v6 (in 2024 it was 10–30 seconds),
what each edit costs.

HOW TO WRITE AN EDIT INSTRUCTION (method; menu 2i):
  1. Name the target exactly — "the second chorus", "the line 'we rise above the storm'"
  2. Say what changes — performer, arrangement, a word, an instrument
  3. Say what must survive — "keep the verses, tempo and key"
  4. One change per request; listen to the WHOLE track after it
  [COMMUNITY] Whether a chorus-only edit or a one-word swap bleeds into the rest of the
  song has not been tested publicly. Check before you rely on it.

REFERENCES [OFFICIAL]: in Simple mode one prompt can reference "Suno songs, playlists,
audio uploads, images and video" together with detailed guidance. v6 "can understand
the feeling behind a reference and use it as the starting point for something
original". Limits on the number and length of references are not published.
  [COMMUNITY] Reported limits: up to 5 images, 1 video up to about 4 minutes, up to 5
  audio references — a single source, treat as a guess.
  [COMMUNITY] A voice-memo hook: describe everything except the hook in the text and
  say "The uploaded audio is the chorus melody. Keep that melody exactly."

⚠️ SIMPLE MODE AND YOUR LYRICS [COMMUNITY]: Simple mode has been seen expanding
supplied lyrics instead of singing them verbatim. When the words must stay exactly as
written, use the full form with the Lyrics field.

### SOUNDS AND SAMPLES
  [OFFICIAL] Sounds (2026-01-27): one-shot samples and loops from scratch, as a Create
  mode; Pro or Premier at launch. "Suno Sounds" now runs on v6.
  [OFFICIAL] Sample (2026-01-20): any sound in Suno can be used as a sample via the
  Remix/Edit menu.

## §8. SLIDERS

  Weirdness          how experimental the result is. Low = genre-safe.
                     Help center: from "Safe" to "Chaos" [OFFICIAL]
  Style Influence    how strictly the Style prompt is obeyed. High = literal.
  Audio Influence    for remixes, covers, Voices: how much of the source survives.
  Vocal Gender       [COMMUNITY] the most reliable vocal-gender control available.
  Variety            v6 only — see §4.

  Reported v6 defaults: Weirdness 50 · Style Influence 50 · Audio Influence 25
  [COMMUNITY].

⚠️ The tables below come from the v4.5–v5.5 era [COMMUNITY]. No one has tested them
on v6. Use them as a starting point and adjust by ear.

[COMMUNITY, v6, one tester] Weirdness 30–50 for detailed prompts; above 50 and under
90 for exploring ("past that you start hearing weird artifacts"); Style Influence
around 40 for generic prompts, around 65 for precise ones. One user fixed muffled
vocals on v6-wild with Weirdness ~20 and Style Influence ~80.

BY GOAL:
  Authentic genre recreation    Weirdness 20–35% · Style Influence 90–100%
  Balanced creative fusion      Weirdness 40–50% · Style Influence 70–85%
  Wild experiment               Weirdness 70%+   · Style Influence 40–60%  (or v6-wild)
  Faithful remix                Weirdness 20–30% · Style Influence 90%+
  Transformative remix          Weirdness 50%+   · Style Influence 60–75%

BY GENRE:
  Rock / metal        Weirdness 40–60% · Style 70–85%  low weirdness = clean guitars
  Electronic / EDM    Weirdness 50–80% · Style 50–70%  tolerates chaos well
  Jazz / classical    Weirdness 30–50% · Style 75–95%  accuracy is the point
  Lo-fi / hip-hop     Weirdness 45–65% · Style 65–80%  groove needs some slack
  Vocal-forward       Weirdness 40–50% · Style 80–95%  protects vocal quality
  Instrumental        Weirdness 35–55% · Style 80–90%  clarity over surprise
  Pop / radio         Weirdness 20–35% · Style 85–95%  predictability is the goal
  Trap / rap          Weirdness 35–55% · Style 70–85%
  Country             Weirdness 25–40% · Style 85–95%  genre fidelity is critical
  Cinematic / epic    Weirdness 30–50% · Style 80–90%  controlled drama
  Ambient / drone     Weirdness 30–55% · Style 75–90%
  Metalcore / extreme Weirdness 45–65% · Style 70–85%  [COMMUNITY, v6] v6 is reported
                                                       weakest on metal — try v6-wild
  Drum & bass         [COMMUNITY, v6] reported weak on v6 — try v6-wild
  Gospel / choir      Weirdness 25–45% · Style 85–95%  arrangement must stay legible
  Folk / singer-songwriter  Weirdness 25–45% · Style 80–95%

FOR EXTEND: lower weirdness than the base track, around 45–55% [COMMUNITY, pre-v6].
High weirdness during extension is a common cause of sudden genre shifts.

## §9. SUNO STUDIO 2.0

[OFFICIAL] "Studio 2.0 is here", 2026-08-13 — a total overhaul of the browser-based
DAW. **Premier only.** Web.

  MIDI               import, record and edit MIDI on the timeline; play with a MIDI
                     controller or the typing keyboard
  Chat bar           generate instruments and vocals, create new plugins and synth
                     presets, ask for help; aware of BPM and able to undo prompt
                     edits (2026-09-02); creates new audio stems from a MIDI clip and
                     renames clips on request (2026-09-17)
  Audio effects      including sidechain compression and convolution reverb, or
                     designed through the chat bar
  Wavetable synth    basses, leads, pads, chords; presets designed through the chat bar
  Musical typing     play MIDI parts from the keyboard, with arpeggiator and chord mode
  Automation         effect parameters that change over time
  Stems              right-click a clip → Split Stems (§10)
  Downloads          from Studio, without the monthly download limit [OFFICIAL]

  Carried from 1.1/1.2 (not re-listed by Suno for 2.0, assume present) [UNVERIFIED]:
  6-band Track EQ with presets, Loop Recording, Context Window, Cover on stems,
  Remove FX, Warp Markers, Alternates (take lanes), time signatures beyond 4/4.

EXPORT: full song, a selected time range, multitrack; MIDI from stems costs credits
[OFFICIAL].

WHAT IT CHANGES ABOUT PROMPTING: less. Studio moves fixes downstream. Prompt for the
performance; repair the mix in Studio. What goes to a DAW, and how: DATA_POSTPROD.

## §10. STEM SEPARATION — three modes

[OFFICIAL] Overhauled 2026-06-11. From the library: More Actions → Get Stems → pick
the split → Extract. In Studio: right-click the clip → Split Stems.

  Auto Split        "up to 12 stems" — the classic full split
                    Pro + Premier · the expensive one: one extraction costs as much
                    as several generations

  Split from Mix    "a single instrument or vocal, plus a complement track"
                    Pro + Premier · charged per stem

  Advanced Split    choose from "nearly 100 instruments" — "Choose exactly what to
                    extract". Suno says the overhaul made stems "cleaner, crisper,
                    free from artifacts" across the tool [OFFICIAL]; that the top
                    mode regenerates rather than filters is v3 wording [UNVERIFIED]
                    **Premier only** · charged per stem

  Free: no stem separation [OFFICIAL].
  Downloads: all stems of a song count as that one song's download [OFFICIAL].

WHEN TO USE WHICH:
  a quick vocal/instrumental split          → Split from Mix
  the full band laid out for a DAW          → Auto Split
  one clean instrument, artifacts unacceptable → Advanced Split

External separation tools are the fallback, not the default — DATA_POSTPROD says when
leaving Suno still wins.

## §11. LYRICS EDITOR

[OFFICIAL] Rebuilt 2026-07-09, web:
  Lyricist                 lock in a writing voice and reuse it across songs
  Natural language editing ask for changes in plain words
  Variations and References rhyme and reference suggestions
  Song structure labels    "Add labels like "Verse" and "Outro"… tell Suno how you
                           want the song to flow" — you place them
  Autosave · Full screen editor

The plan table also lists "Co-write with Suno", "Inspire" and "Magic Song
Descriptions" as creation features [OFFICIAL].

WHAT THIS CHANGES FOR PROMPTING:
  Two paths coexist and a prompt system must support both:
  - web with the editor → lyrics plus labels placed with the editor's label tool
  - mobile, pasting, automation, exact control → supply lyrics already marked up
  CORE_02 §2 covers both.

## §12. PLANS — what each one unlocks

[OFFICIAL] Plan names and what they unlock. Prices are deliberately absent.

  FREE      v6-mini only · a daily credit allowance · standard features · shared
            queue · audio uploads up to 8 minutes · no stems · no add-on credits
            · NO monthly downloads (see below) · NO COMMERCIAL RIGHTS
            · Voices "to try"

  PRO       v6 and v6-wild · a monthly credit allowance · 20 song downloads a month
            · commercial use rights · Auto Split and Split from Mix · own voice ·
            Custom Models · audio uploads up to 30 minutes · priority queue · extra
            credits and downloads purchasable

  PREMIER   everything in Pro · Suno Studio 2.0 · 60 song downloads a month ·
            Advanced Split · add new vocals or
            instrumentals to existing songs · a larger monthly credit allowance

  Credits bought on top do not expire but need an active subscription [OFFICIAL].

─── DOWNLOADS — since 2026-09-03 ─── [OFFICIAL]
  Free      "Up to 7 total (lifetime) trial downloads for personal, non-commercial
            use only" — for accounts that existed before 3 September; accounts
            created later "may occasionally receive trial downloads"
  Pro       20 per month, with commercial use rights
  Premier   60 per month, with commercial use rights; unlimited from inside Studio

  One song = one download, whatever the format. Stems count as part of the song's
  download. Re-downloading the same song is free. Unused downloads do not roll over.
  More can be bought. The caps apply to every song, including ones made before
  3 September; every song stays playable and shareable on Suno.

─── THE RULE THAT CHANGED ─── [OFFICIAL]
  Commercial rights now follow the DOWNLOAD, not the generation:
  "You may not commercially exploit Output that has not been downloaded by you
  through an approved channel." Suno: "Songs downloaded from Suno on paid plans remain
  yours to use commercially or personally."

  PRACTICAL CONSEQUENCES:
  - Download what you intend to release while you are subscribed
  - A song made on Free stays non-commercial — upgrading later does not change that
  - Remixes of other people's songs are non-commercial on every plan (DATA_LEGAL §2)
  Full rights picture: DATA_LEGAL.

## §13. WHAT SHIPPED — the moving parts

[OFFICIAL] Chronological, so a stale copy of this file can be diffed quickly:

  2026-01-20  Mashup (two songs) and Sample
  2026-01-27  Sounds — one-shots and loops from scratch
  2026-02-16  Studio 1.2
  2026-03-26  v5.5 — Voices, Custom Models, My Taste
  2026-05-13  Android Auto and CarPlay
  2026-05-14  mobile overhaul, vocal gender selector, Create memory
  2026-06-04  iOS: lyrics from Notes, audio from Voice Memos
  2026-06-11  stem separation overhaul — three modes
  2026-07-07  custom soccer anthem generator, mobile
  2026-07-09  lyrics editor rebuilt
  2026-07-15  iMessage keyboard
  2026-07-20  Duration slider (then v5.5, web)
  2026-07-31  cover art editing with text prompts
  2026-08-07  Voices on iOS and Android; Free can try Voices
  2026-08-10  new terms published, effective 2026-09-03; download limits announced
  2026-08-13  Studio 2.0
  2026-08-19  playlist improvements · 2026-08-20 offline playlists on mobile
  2026-09-02  Studio updates — BPM-aware chat bar, plugin copying
  2026-09-03  new terms and download caps in force
  2026-09-08  partnership with Believe and TuneCore
  2026-09-09  v6, v6-wild, v6-mini; every earlier model retired; Max Mode; Variety
  2026-09-17  Studio: better MIDI, stems from a MIDI clip

  No official public API. Suno said in July it was "exploring a developer API,
  starting with a curated group of partners" [COMMUNITY: press]. Third-party
  "Suno APIs" are unofficial resellers.

## §14. MYTHS — kept here so they stop circulating

These appear in guides, in previous SunoForge editions, and in forum advice.
None survived checking. Listed so the system can recognize and repair them.

  "MAX MODE tags unlock hidden quality"
  [UNVERIFIED] Controlled comparison (Jan 2026) found no hidden mode behind
  [Is_MAX_MODE: MAX] or (MAX)(MAX)(MAX)(MAX). Originates from a single Reddit post.
  ⚠️ Suno's REAL Max Mode (2026-09-09) is a toggle in the interface (§4). It shares
  the name and nothing else. Typing MAX into the prompt does not switch it on.

  "Style attention dies after 200 characters"
  [UNVERIFIED] No test shows a cliff there. Influence fades gradually.

  "Parametric tags control the mix"
  [UNVERIFIED] [Reverb: 30%], [BPM: 120], [eq: scooped] were never parsed.
  On v6, typing "weirdness 20%" into Style "does not move anything" [COMMUNITY].

  "Pipe stacking is deprecated and causes artifacts"
  [UNVERIFIED] Never documented as deprecated, never reproduced. Also never
  documented as supported. No v6 evidence either way.

  "Tracks drift to generic pop after two minutes"
  [UNVERIFIED] as a fixed threshold. Suno does recommend Max Mode for songs over two
  minutes and for whole-track consistency [OFFICIAL] — the concern is real, the
  schedule is folklore, and the cure is the toggle.

  "v5/v5.5 has 88% prompt adherence"
  [UNVERIFIED] No such metric was ever published.

  "Studio comes with Pro"
  [OFFICIAL — corrected] Premier only, in 1.2 and in 2.0.

  "The free tier caps songs at about two minutes"
  [OFFICIAL — corrected] v6-mini, like the rest of v6, generates up to 8 minutes.

  "My Suno songs are commercial because I made them while subscribed"
  [OFFICIAL — corrected since 2026-09-03] Rights follow the download on a paid plan.

// ═══════════════════════════════════════════════════════════════
// END OF DATA_SUNO_2026-09.md · SunoForge v4.0
// Snapshot date 2026-09-30 · replace this file, not the CORE files
// ═══════════════════════════════════════════════════════════════

## TAGS
suno, suno v6, v6-wild, v6-mini, retired models, v5.5 retired, custom models, max mode, variety slider, duration, 8 minutes, style field limit, exclude styles, weirdness, style influence, audio influence, vocal gender, voices, own voice, verification phrase, plain-language edit, replace section, mashup, sample, references, image to music, video to music, suno sounds, studio 2.0, midi, stems, auto split, advanced split, lyrics editor, lyricist, plans, free, pro, premier, download limits, commercial rights, myths
