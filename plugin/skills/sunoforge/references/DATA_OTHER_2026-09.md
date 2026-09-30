<sunoforge_file id="DATA_OTHER" version="4.0" layer="data" role="adapter" source="DATA_OTHER_2026-09.md">
<file_meta>
file_id: DATA_OTHER
version: "4.0"
layer: data
role: adapter
description: >
  Platforms other than Suno and Google, as of 2026-09-30: ElevenMusic (Music v2.5),
  Stable Audio 3.0, MiniMax Music 3.0, local open models (ACE-Step 1.5, YuE2),
  aggregators, the /free comparison and the platform decision tree behind menu [10].
  Read for any non-Suno, non-Google target, for "what can I do for free" and for
  "which platform should I use".
valid_as_of: "2026-09-30"
expires: "three of the five platforms here released a new model between July and September 2026 — verify anything here after 2026-12"
scope: elevenmusic · stable_audio · minimax · local_open_models · aggregators · free_plans · platform_selector · portability · all_mode_example
key_concepts: [elevenmusic_v2_5, composer, audio_reference, finetunes, ownership_on_free, stable_audio_3, open_weights, community_license, daw_plugin, minimax_music_3, section_tags_minimax, ace_step_1_5, yue2, local_generation, aggregators, free_tiers, platform_compare, portability]
depends_on: [CORE_00_ENTRY, DATA_SUNO, DATA_GOOGLE]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE, DATA_LEGAL, DATA_POSTPROD]
rag_priority: high
authority: "SINGLE SOURCE OF TRUTH FOR ELEVENMUSIC, STABLE AUDIO, MINIMAX AND LOCAL MODEL SPECIFICATIONS"
updated: "2026-09-30"
</file_meta>

# 🟣 SUNOFORGE v4.0 — OTHER PLATFORMS
# File 8 of 12 · DATA layer · valid as of 2026-09-30

> ⚠️ **Expiry notice.** Between July and September 2026 ElevenMusic moved to v2.5,
> MiniMax released Music 3.0 with open weights, Stable Audio shipped a DAW plugin and
> two open music models appeared. If today is more than a quarter past the date above,
> treat every figure here as a starting hypothesis.

> 📌 **Single source rule.** ElevenMusic, Stable Audio, MiniMax and local-model figures
> live here and nowhere else. Suno figures live in DATA_SUNO, Google figures in
> DATA_GOOGLE. The comparison tables in §6 and §7 point at those files instead of
> copying their numbers.

> 💲 **No prices.** Plans are named because rights and features depend on them.
> What they cost is left to the user's own account and country.

<section id="§1" title="ELEVENMUSIC — menu [7i]">

<!-- rag_anchor: elevenmusic_v2_5 -->
<rag_zone id="elevenmusic">

The hosted platform whose selling point is what it was trained with, and the one
that states ownership on every plan.

─── MUSIC v2.5 ─── [OFFICIAL] released 2026-09-11
  The default for prompted and reference generation in ElevenMusic; Music v2 stays
  available. In the API: `model_id="music_v2_5"`.
  In a blind test of 47,885 same-prompt pairs, v2.5 was preferred most of the time;
  the gap is widest on vocal-led and acoustic-heavy genres — R&B, soul, hip hop,
  rock, metal, orchestral, cinematic.
  "Created in collaboration with labels, publishers, and artists", "cleared for nearly
  all commercial uses, from film and television to podcasts and social media videos,
  and from advertisements to gaming." [OFFICIAL]
  ElevenLabs signed a multi-year agreement with Universal Music Group in September
  2026; "This deal is separate from Music 2.5" [OFFICIAL].

─── WHAT IT DOES ─── [OFFICIAL]
  Length          3 seconds to 5 minutes
  Audio           MP3 44.1 kHz (128–192 kbps) or WAV; lossless downloads
  Vocals          any genre, several languages (English, Spanish, German, Japanese
                  named), fast rap and dense phrasing; or instrumental
  Editing         add, remove and resize sections; edit the lyrics or prompt of one
                  section; regenerate just that section (inpainting); composition
                  plans; mid-track genre transitions
  Audio Reference up to about 30 seconds of your own audio guides sound, style,
                  instrumentation, tempo and mood — never copied; screened for
                  copyright; paid plans; not for genre transformation
  Finetunes       train on your own non-copyrighted tracks (about 5–10 minutes),
                  or pick a curated genre Finetune
  New in the app  Sounds — free library of sounds and loops (2026-08-13) · Composer —
                  section-by-section song editing (2026-08-25) · Muse — a
                  conversational co-writer (2026-08-27)
  API             paid plans only

</rag_zone>

<!-- rag_anchor: elevenmusic_rights_downloads -->
<rag_zone id="elevenmusic_rights">

─── RIGHTS AND DOWNLOADS ─── [OFFICIAL] since 2026-09-11
  "You own what you make in ElevenMusic, on every plan, including Free." (ElevenLabs
  blog). ElevenMusic's own post is softer: "You have rights to what you make" and
  "Rights and commercial use vary by subscription tier. See Terms for details."
  "On the Free plan… you can use what you make commercially as long as you credit
  ElevenMusic."
  Free: five lossless downloads a day · Pro: 400 lossless downloads a month.
  "The permissions that apply when you create a track stay with it, so cancelling or
  downgrading doesn't change how you can use tracks you've already created." Future
  changes to the terms apply only to tracks made after them.
  "Downloads are blocked on tracks that reference other artists' songs."
  The per-tier details sit in ElevenLabs' music terms — read them for client work.

  THE HONEST TRADE-OFF [COMMUNITY]: expressive lead vocals were reported as its
  relative weakness before v2.5; the v2.5 blind test claims the biggest gains on
  exactly the vocal-led genres. Listen for yourself before promising a client a vocal.

</rag_zone>

<!-- rag_anchor: elevenmusic_prompting -->
<rag_zone id="elevenmusic_prompting">

─── PROMPTING — ElevenLabs' own guidance ─── [OFFICIAL]
  THE FIVE QUESTIONS: "A prompt answers five questions, whether you intend it to or
  not: genre, mood, instrumentation, tempo, and production era. Any question you
  leave open, the model answers with the most statistically likely choice — which is
  to say, the most average one."
  NUMBERS WORK: "The model accurately follows BPM and often captures the intended
  musical key" — write "130 BPM", "in A minor".
  STUDIO LANGUAGE MOVES THE MIX: sidechained, close-mic'd, bone-dry, tape saturation,
  plate reverb. The same "slow soul ballad, 68 BPM, female vocal" changes completely
  with "bone-dry drums, close-mic'd vocal, dead room" versus "cavernous plate reverb,
  tape echo throws, gospel room".
  ERA IS A DIAL and can turn mid-song ("1950s rock and roll with slapback echo").
  NARRATE THE ARRANGEMENT IN ORDER: "UK garage, 132 BPM — start with just a shuffled
  drum loop, add a warm sub bassline after four bars, then bring in chopped vocal
  stabs for the drop". "Without the just, the model fills the silence."
  LOOPS ARE EXCLUSION: "boom bap drum break, 90 BPM, dusty and swung, four bars, no
  melody — just drums".
  TIMING: "lyrics begin at 15 seconds", "instrumental only after 1:45"; length as
  "60 seconds" or auto.
  VOCAL DELIVERY: raw, live, breathy, whispered, belted, conversational, deadpan,
  stacked harmonies; "two singers harmonizing in C".
  INSTRUMENTAL: "instrumental only". STEMS: put "a cappella" before the vocal
  description. LANGUAGE: in the app, follow up with "make it Japanese".
  LENGTH OF PROMPT: short evocative keywords leave the model room; detailed prompts
  give more control.
  Bracket markup from Suno has no meaning here; structure lives in the editor or a
  composition plan.

</rag_zone>

</section>

<section id="§2" title="STABLE AUDIO 3.0 — menu [7j]">

<!-- rag_anchor: stable_audio_family -->
<rag_zone id="stable_audio">

[OFFICIAL] Released 2026-05-20. "trained on fully licensed data". Weights you can hold.

### THE FAMILY
  Small SFX   sound effects, on device (phones, ordinary laptops)        open weights
  Small       full music composition on device, up to 2 minutes          open weights
  Medium      higher musicality, "longer track length at up to 6:20"     open weights
  Large       the most advanced; via the Stability API and enterprise
              self-hosting; also "more than six minutes"                 not open
  Length is set to the second ("variable-length generation… at per-second
  granularity").

  ⚠️ Correction to earlier editions: 6:20 belongs to MEDIUM, the open model. Large is
  API/enterprise and also runs past six minutes.

─── WHAT ELSE ─── [OFFICIAL]
  LoRA training on your own library (documented for Small and Medium) · inpainting:
  one segment, several segments, or continuation past the end · audio-to-audio.
  2026-08-18 (beta): a DAW plugin — macOS AU and VST3, Logic Pro and Ableton Live,
  syncs to the session BPM, generates up to six minutes, keeps takes in a playlist —
  and a web app at StableAudio.com for iterative direction in plain words,
  audio-to-audio, multitrack mixing and export.

─── LICENSING ─── [OFFICIAL]
  "You own your outputs and can distribute and commercialize them under the Stability
  AI Community License, or the Enterprise License for organizations with more than
  $1M in revenue." Legal indemnification comes with the Enterprise licence.
  (The revenue threshold is a licence condition, not a price.)

</rag_zone>

<!-- rag_anchor: stable_audio_use_prompting -->
<rag_zone id="stable_audio_use">

WHAT IT IS FOR:
  ✅ instrumental beds, textures and sound design
  ✅ long-form ambient and background work
  ✅ anything that must run offline or on your own hardware
  ✅ anything where owning the output outright matters
  ✅ transforming existing audio, and working inside a DAW
  ⚠️ vocal songs are not its strength — use Suno, ElevenMusic or Lyria for those

PROMPTING:
Descriptive prose. For instrumental work keep vocal language out entirely; a
mentioned singer is the most common cause of unwanted vocal artefacts (CORE_03 §5).

```
A slow, spacious ambient bed. Sustained analog synth pads with a very slow attack,
a distant filtered piano figure repeating every few bars, and a low sine drone
underneath. Unhurried, unresolved and even throughout. Instrumental.
```

</rag_zone>

</section>

<section id="§3" title="MINIMAX MUSIC 3.0 — menu [7k]">

<!-- rag_anchor: minimax_music_3 -->
<rag_zone id="minimax">

[OFFICIAL] Released 2026-08-13, published with open weights.
  "Given a creative concept and optional lyrics, the model composes, arranges,
  performs, and produces a complete song in a single generation" — "a complete song
  of up to five minutes".

  STRUCTURE: "section tags in the lyrics — such as [intro], [verse], [pre-chorus],
  [chorus], [bridge], [instrumental], [solo], and [outro] — define the song's
  macrostructure" [OFFICIAL].
  DESCRIPTION: "Structured Captions" that name genre, tempo, time signature, key, use
  case and production character, and follow the emotional contour, the entry and exit
  of instruments, the groove, and section-level changes in vocal delivery [OFFICIAL].
  A Prompt Enhancement System expands a simple request into such a caption.
  VOCALS: timbre, breathiness, falsetto, harmony, delay and Auto-Tune can be
  described [OFFICIAL].

  Reported: 32 kHz 16-bit WAV output; an API with per-song billing [COMMUNITY].
  Licence of the weights: read the model card before commercial use [UNVERIFIED here].

  MiniMax's own example captions read exactly like a SunoForge Style line:
    "Progressive house / EDM, 126 BPM, B-flat major. Reflective and nostalgic verses
    rise into a cathartic, euphoric chorus, with a smooth breathy male tenor, pulsing
    side-chained synths, punchy club bass, crisp drums, and wide hall reverb."

WHERE IT FITS:
  ✅ open weights with vocals — run a full song model yourself
  ✅ volume generation through an API
  ✅ a platform whose documented syntax (section tags + detailed caption) matches
     this system's output with no translation
  ⚠️ Correction to earlier editions: v3.0 listed Music 2.6 as a reference entry
  "below the leaders". That version is superseded; judge 3.0 by ear.

</rag_zone>

</section>

<section id="§4" title="AGGREGATORS AND REGIONAL ACCESS">

<!-- rag_anchor: aggregators_caveats -->
<rag_zone id="aggregators">

A practical problem this system's audience actually has: several platforms are hard
to reach without a foreign payment card, and some are region-restricted outright.

WHAT AN AGGREGATOR IS: a third-party service that holds accounts with the underlying
platforms and resells generation, often with local payment methods.

PRESENT THEM ONLY AS THIRD-PARTY INTERMEDIARIES:
  - not affiliated with the platforms they resell
  - your prompts and outputs pass through their infrastructure
  - the upstream platform's terms attach to the account holder — the aggregator,
    not you. Since Suno ties commercial rights to a download on the user's own paid
    plan (DATA_SUNO §12), an aggregator's "Suno" output is hard to call yours
  - service can stop without notice when an upstream relationship ends
  - "Suno API" resellers are unofficial: Suno has no public API (DATA_SUNO §13)
  [UNVERIFIED] as a category; none has been independently checked by this system.

WHAT TO RECOMMEND INSTEAD WHEN ACCESS IS THE PROBLEM:
  a local open model (§5) or Stable Audio's open weights (§2) — no account, no
  region, no reseller between you and the output.

WHAT NOT TO RECOMMEND:
  ❌ repackaged utility apps that bolted music generation onto an unrelated product
  ❌ anything trading under the Riffusion name (DATA_GOOGLE §7) — never emit its address
  ❌ services with unstated training-data provenance, when the work is commercial

</rag_zone>

</section>

<section id="§5" title="LOCAL OPEN MODELS — run it on your own machine">

<!-- rag_anchor: local_models_ace_step -->
<rag_zone id="local_ace_step">

─── ACE-STEP 1.5 ─── [OFFICIAL: project README] MIT licence
  Songs from 10 seconds to 10 minutes · lyrics in 50+ languages · cover generation,
  repaint (regenerate a part), vocal-to-backing-track, LoRA from a few of your own
  songs ("8 songs, 1 hour on 3090") · runs with under 4 GB of video memory; the XL
  models (April 2026) want 12 GB with offloading, 20 GB without.
  The authors' own quality claim: "between Suno v4.5 and Suno v5".
  INPUT: a caption (style) plus lyrics with [Verse] / [Chorus] tags; BPM, key, time
  signature and duration as separate settings; a language-model "thinking" step that
  plans the song before rendering. Web UI and a local REST API.

</rag_zone>

<!-- rag_anchor: local_models_yue2 -->
<rag_zone id="local_yue2">

─── YUE2 ─── [OFFICIAL: project README] released 2026-09-14
  Writes an EDITABLE SCORE first — melody and chords in ABC notation — then renders
  it as a full song with vocals and accompaniment at 48 kHz stereo. The score can be
  edited by a person or an agent before rendering; covers work by transcribing a
  melody and re-rendering it in a new style.
  The authors report it "competitive with Suno v5/v6" on their own benchmark
  (WildSongBench) — the authors' measurement, not an independent one [COMMUNITY].
  Needs Linux, Python 3.12 and an NVIDIA GPU with BF16 and 24 GB of memory. There is
  a free hosted demo and an agent skill ("yue2-music").
  LICENCE: code Apache 2.0; weights CC BY-NC 4.0 with an added creator permission —
  "Personal users, content creators, and musicians: Free to use YuE2 and monetize
  generated outputs"; companies need a commercial licence.

</rag_zone>

<!-- rag_anchor: local_models_choice -->
<rag_zone id="local_choice">

WHICH LOCAL OPTION — requirements [OFFICIAL, project READMEs]; the fit is this
system's judgement:
  modest GPU, songs with vocals, many languages      → ACE-Step 1.5
  a powerful NVIDIA GPU, control over melody/chords  → YuE2
  instrumental, sound design, a DAW plugin (Mac)     → Stable Audio 3.0 Small/Medium
  a full song model from a major vendor              → MiniMax Music 3.0

HOW SUNOFORGE OUTPUT MAPS TO THEM:
  Style line → caption · marked-up lyrics → lyrics field (lowercase or capitalised
  section tags both appear in their docs) · BPM, key, duration → their own settings
  where they have them, otherwise in the caption. Suno-only items (Exclude Styles,
  sliders, Variety, Max Mode) have no equivalent.

WHY IT MATTERS: no account, no region lock, no download cap, no terms that can change
under an existing track. The licence of the weights is the only rights question.

</rag_zone>

</section>

<section id="§6" title="WHAT YOU CAN DO WITHOUT A PAID PLAN — the `/free` command">

<!-- rag_anchor: free_plans_table -->
<rag_zone id="free_tiers">

The most-asked question this system receives. Reached by `/free` (CORE_00 §5).
⚠️ Read the caveat first: this table gives the SHAPE of each free offer and points at
the file with the details. Allowances change monthly and differ by country.

| Platform | Free offer | Commercial use from the free offer? |
|---|---|---|
| Suno | v6-mini, a daily credit allowance, no stems; downloads only as occasional lifetime "trial" downloads → DATA_SUNO §12 | ❌ No. Upgrading later does not change songs made on Free |
| Google — Gemini app | Lyria 3.5 in the app, up to 3 minutes, 18+; quotas unpublished → DATA_GOOGLE §2 | ⚠️ not stated clearly enough to rely on |
| Google — Gemini API | no free tier for Lyria | — |
| Flow Music | Free plan with daily credits → DATA_GOOGLE §7 | ⚠️ primary clause not found |
| ElevenMusic | Free plan, five lossless downloads a day | ✅ yes, when you credit ElevenMusic (§1) |
| Stable Audio | open weights for Small SFX, Small, Medium — run them yourself | ✅ Community Licence, below the revenue threshold |
| MiniMax Music 3.0 | open weights | ⚠️ read the model card |
| ACE-Step 1.5 | open weights, MIT | ✅ |
| YuE2 | open weights | ✅ for individuals and musicians; companies need a licence |

Marks: every row restates a fact marked in its own section — [OFFICIAL] for Suno,
the Gemini app, the Gemini API, ElevenMusic, Stable Audio, ACE-Step and YuE2;
Flow Music and MiniMax rights [UNVERIFIED] as marked there.

</rag_zone>

<!-- rag_anchor: free_plans_answer -->
<rag_zone id="free_answer">

THE ANSWER MOST PEOPLE ACTUALLY NEED:
**"Free" and "free to use commercially" are two different questions, and the
platforms differ far more on the second than on the first.**

  IF YOU JUST WANT TO MAKE MUSIC AND LISTEN TO IT
    Any free option is fine. Start with whichever interface you like.

  IF IT WILL EVER BE PUBLISHED, MONETISED OR HANDED TO A CLIENT
    On Suno, make and download it on a paid plan — rights follow the download.
    ElevenMusic allows commercial use from Free with a credit line. Open models
    you run yourself are covered by their licence from the first second.

  IF YOU CANNOT PAY FROM YOUR REGION
    Local open models (§5) solve access and rights at once. Aggregators solve
    access and complicate rights (§4).

WHAT NOT TO SAY:
  ❌ a credit-to-song conversion or a price from memory — they vary and change
  ❌ that a free plan grants commercial rights, without naming which platform
  ❌ "free forever" marketing as if it covered the rights to the output

</rag_zone>

</section>

<section id="§7" title="PLATFORM COMPARE — menu [10]">

<!-- rag_anchor: platform_decision_tree -->
<rag_zone id="platform_selector">

The decision tree behind menu [10] and `/compare`.

```
Is the vocal performance the point of the track?
  → Suno v6. ElevenMusic v2.5 is the challenger on vocal-led genres.

Does it need an answer for a client who asks where the music came from?
  → ElevenMusic (made with rights holders, ownership on every plan)
  → Stable Audio (licensed data, you own the output)

Must it run offline, on your own hardware, with no account?
  → Stable Audio Small/Medium · ACE-Step 1.5 · YuE2 · MiniMax Music 3.0 (§5, §3)

Must it hit specific timings in a video?
  → Lyria 3.5 with timestamp ranges (DATA_GOOGLE §4)

Will you change one part later without losing the rest?
  → Suno v6 plain-language edits · Flow Music Replace · ElevenMusic Composer

Do you need a long single generation?
  → Suno v6 (8 min) · ACE-Step (10 min) · Stable Audio Medium (6:20)

An endless stream you steer while it plays?
  → Lyria RealTime. It is an instrument, not a track generator.

Your own voice, or your catalogue's style?
  → Suno Voices and Custom Models · ElevenMusic Finetunes · LoRA on ACE-Step or
    Stable Audio

A 30-second sketch, jingle or loop?
  → Lyria 3 Clip · a Suno v6-mini draft

Control over the actual melody and chords before rendering?
  → YuE2 (editable score)

Nothing reachable from where you are?
  → local open models first, aggregators second (§4)
```

</rag_zone>

<!-- rag_anchor: platform_field_shape -->
<rag_zone id="platform_shape">

THE SHAPE OF THE FIELD — qualitative on purpose; numbers live in the platform files:

| Platform | Vocal | Editing after | Rights posture |
|---|---|---|---|
| Suno v6 | strongest character; own voice | plain-language section and line edits, Studio 2.0 | commercial on paid plans, bound to the download |
| Lyria 3.5 | good, many languages | none after generation (single turn) | Google terms per surface; SynthID on everything |
| Flow Music | good | part by part | not clearly documented |
| ElevenMusic v2.5 | strong, fast rap | per section, inpainting, Composer | you own it on every plan; credit on Free |
| Stable Audio 3.0 | minimal | inpainting, audio-to-audio, DAW plugin | you own the output (Community Licence) |
| MiniMax Music 3.0 | full vocals | regenerate | depends on the weights' licence / API terms |
| ACE-Step 1.5 | full vocals, 50+ languages | repaint, cover | MIT |
| YuE2 | full vocals | edit the score, then render | free for creators; companies licence |

Marks: the vocal column is [COMMUNITY] judgement; editing and rights columns
restate [OFFICIAL] facts from each platform's section.

HOW TO ANSWER A COMPARISON QUESTION:
  1. Ask what the track is FOR before naming a platform. "For me" and "for a client"
     have different answers.
  2. Name one platform, not five. Give the runner-up in one line.
  3. Say the trade-off out loud. Every option here loses something.
  4. If rights are involved at all, route to `/legal` — DATA_LEGAL.

</rag_zone>

</section>

<section id="§8" title="PLATFORMS DELIBERATELY NOT COVERED">

<!-- rag_anchor: not_covered_platforms -->
<rag_zone id="not_covered">

Recorded so the omissions read as decisions rather than gaps.

### UDIO
  Not a target. Downloads were disabled after its 2025 settlement [OFFICIAL +
  COMMUNITY] and are reported still closed [UNVERIFIED]. Its licensed
  successor, "Starstruck" — a fan app where every creation starts from a chosen
  artist's song and belongs to that artist's rights holder — was announced for later
  in 2026 and had not launched by this file's date [COMMUNITY]. A walled garden you
  cannot export from is not a production tool. DATA_LEGAL §7.

─── MUSICFX, MUSICFX DJ, LYRIA 3 PRO ─── retired or retiring: DATA_GOOGLE §9.

─── RIFFUSION AND PRODUCER.AI ─── earlier names of Google Flow Music.

### CONSUMER APPS WITHOUT PUBLISHED SPECIFICATIONS
  Chat-style and mobile music apps, several of them front-ends that switch between the
  models above. None publishes specifications, training provenance or licensing terms
  in a form worth citing [UNVERIFIED]. Mention as a category if asked; recommend none
  by name, and never for commercial work.

### VOICE-CLONING-ONLY TOOLS
  Not music generators. Where cloning your own voice is the need, Suno Voices includes
  a verification step (DATA_SUNO §5). Tools that clone any voice in seconds without
  one are a legal problem wearing a convenience feature (DATA_LEGAL §3).

</rag_zone>

</section>

<section id="§9" title="WORKED EXAMPLES">

<!-- rag_anchor: elevenmusic_examples -->
<rag_zone id="elevenmusic_examples">

### ELEVENMUSIC · A COMMERCIAL BED, NARRATED IN ORDER
```
A sixty-second soundtrack for an outdoor clothing advertisement. Uplifting indie
folk-pop with a cinematic lift, 104 BPM, in D major. Start with just a fingerpicked
acoustic guitar, bring in brushed drums after eight bars, then a string pad and a
warm female lead singing wordless "ooh" lines. Hopeful and unforced; falls away to a
single guitar note at the end. Close-mic'd, warm, a little tape saturation.
```
  Why here: the client will ask where the music came from, and this platform has an
  answer; and a track made on Free may be used commercially with a credit.

### ELEVENMUSIC · A GENRE SWITCH
```
Begins as a slow operatic aria with full orchestra and a soprano singing in Italian,
breaks without warning into aggressive modern metal at 180 BPM with distorted guitars
and a screamed male vocal, then returns to the opening aria as if nothing happened.
```
  Then regenerate whichever passage comes back weakest, alone, in the section editor.

### ELEVENMUSIC · A REFERENCE THAT CARRIES THE FEEL
  Upload ~30 seconds of your own recording, then: "same energy, half-time drums,
  female vocal, brighter chorus". The reference carries groove and palette; the text
  says what should be different. Keep other people's recordings out — references are
  screened.

</rag_zone>

<!-- rag_anchor: stable_minimax_local_examples -->
<rag_zone id="open_model_examples">

### STABLE AUDIO · A SIX-MINUTE AMBIENT BED (Medium)
```
A six-minute slow ambient piece. Sustained analog pads with very slow attacks, a low
sine drone underneath, and a distant filtered piano figure that repeats every few
bars with slight variation. No percussion, no conventional melody, no resolution.
Even and unhurried throughout. Instrumental.
```
  "No resolution" matters: most models write toward an ending, which is wrong for
  something meant to sit under a scene or loop for hours.

### STABLE AUDIO · SOUND DESIGN (Small SFX)
```
A heavy metal door closing in a large concrete space: the impact, the latch, and a
long reverberant tail decaying over several seconds. No music.
```

### MINIMAX MUSIC 3.0 · CAPTION + TAGGED LYRICS
```
Caption: Nostalgic power pop / pop rock, 112 BPM, E-flat major. Bittersweet verses
burst into cathartic choruses, led by a clear female mezzo-soprano with soaring octave
hooks, punchy drums, wide layered guitars and a polished modern mix.
Lyrics:
[verse]
We were the kind who never stayed in one place
[chorus]
Forever friends — we promised it one day
```

### ACE-STEP 1.5 · THE SAME IDEA, LOCALLY
  caption "nostalgic power pop, female mezzo-soprano, layered guitars" · lyrics with
  [Verse 1] / [Chorus] · bpm 112 · key "Eb major" · duration 180 · thinking on.

</rag_zone>

</section>

<section id="§10" title="WHAT TRANSFERS BETWEEN PLATFORMS">

<!-- rag_anchor: portability_between_platforms -->
<rag_zone id="portability">

A convergence worth noticing in 2026: Google, ElevenLabs and MiniMax now all document —
each in its own way (Google: section tags and parentheses; MiniMax: section tags;
ElevenLabs: sections described in the prompt or planned in the editor) —
the same things this system has always written — genre with an era first, named
instruments, a numeric BPM and key, a vocal described by gender, range and timbre,
section tags in the lyrics, parentheses for backing vocals. The six-layer content
(CORE_01 §1) moves between platforms almost unchanged.

WHAT HAS TO BE STRIPPED WHEN LEAVING SUNO:
  Exclude Styles lists · slider values · Variety · Max Mode · Suno-only performance
  symbols

WHAT HAS TO BE ADDED WHEN ARRIVING:
  LYRIA 3.5      a `Lyrics:` header, the language, a length or timestamp ranges,
                 "Instrumental only, no vocals." for instrumentals (DATA_GOOGLE §10)
  ELEVENMUSIC    the arrangement narrated in order; sections planned in the editor
  STABLE AUDIO   an explicit "instrumental", and no vocal language at all
  MINIMAX 3.0    a detailed caption and lowercase section tags work as documented
  LOCAL MODELS   BPM, key and duration moved into their own settings

ONE THING THAT NEVER TRANSFERS:
Expectations about the vocal. The same description produces markedly different
amounts of character on each platform, and that difference is the main reason to
choose one over another (§7). Never promise the voice from one platform on another.

</rag_zone>

</section>

<section id="§11" title="ONE IDEA, EVERY PLATFORM — menu [8]">

<!-- rag_anchor: cross_platform_recipe -->
<rag_zone id="cross_platform_recipe">
The same brief rendered for each covered platform, demonstrating menu [8]
ALL mode. Formats are never mixed — each target gets its own dialect
(CORE_00 §6). Moved here from DATA_RECIPES in v4.0: platform syntax is dated.

BRIEF: a melancholy song about standing outside in the rain at three in the
morning.

### 🟠 SUNO v6

Settings: v6 · Variety 0 · Max Mode on (a release, over two minutes)
Style:
```
early-2000s Reykjavík post-rock, melancholic and vast, fingerpicked acoustic
guitar with a warm cello swell and soft brushed drums, female alto with a
slight quaver, close-miked, lo-fi analog warmth, 82 BPM, A minor
```

Lyrics:
```
[Intro]
[Rain]

[Verse 1]

[Chorus]

[Verse 2]

[Chorus]

[Bridge — voice and guitar only]

[Outro]
[Fade Out]
```

</rag_zone>

<!-- rag_anchor: cross_platform_recipe_lyria_3_5 -->
<rag_zone id="cross_platform_recipe_lyria_3_5">

### 🔵 LYRIA 3.5

Google's order, BPM and key as numbers, structure as ranges within a couple of minutes:
```
Early-2000s Icelandic post-rock, melancholy and vast, at 82 BPM in A minor.
Fingerpicked acoustic guitar, a warm cello swell and soft brushed drums. Female
Alto with a slight quaver, recorded very close, singing in English. The lyrics
are about standing outside in the rain at three in the morning.

[0:00 - 0:20] Intro: rain, then a single fingerpicked guitar alone.
[0:20 - 0:50] Verse 1: the voice enters, quiet and close.
[0:50 - 1:20] Chorus: cello swells underneath, brushed drums arrive.
[1:20 - 1:40] Bridge: everything falls away to voice and guitar.
[1:40 - 2:00] Outro: a held cello note fading into the rain.
```

</rag_zone>

<!-- rag_anchor: cross_platform_recipe_flow_music -->
<rag_zone id="cross_platform_recipe_flow_music">

### 🟢 FLOW MUSIC

```
SEED     the Lyria prompt above, without the ranges
REPLACE  "Replace only the brushed drums with a slower, softer pattern.
          Keep the guitar and cello exactly as they are."
EXTEND   "Continue in the same Icelandic post-rock style, same tempo and
          instrumentation, building to a final swell and then resolving."
```

### 🟣 ELEVENMUSIC

```
Early-2000s Icelandic post-rock, melancholy and vast, 82 BPM in A minor. Start
with just a fingerpicked acoustic guitar and rain, bring in a warm cello swell and
soft brushed drums on the first chorus, fall away completely in the middle, then
return larger. A female alto with a slight quaver, close and unpolished.
```
  Sections then adjusted and regenerated in the editor or Composer.

</rag_zone>

<!-- rag_anchor: cross_platform_recipe_stable_audio -->
<rag_zone id="cross_platform_recipe_stable_audio">

### 🟡 STABLE AUDIO

Instrumental, which is what it is for:
```
A slow, vast instrumental post-rock piece. Fingerpicked acoustic guitar, a
warm cello swell arriving late, soft brushed drums. Melancholy and
unresolved. Builds gradually and never fully releases. Instrumental.
```

### ⚪ MINIMAX 3.0 / LOCAL MODELS

Caption: the Suno Style line above, unchanged. Lyrics: the same skeleton with
[intro] [verse] [chorus] [bridge] [outro]. BPM 82, key A minor, duration where the
interface has them (DATA_OTHER §3, §5).

### WHAT CHANGED BETWEEN THEM

The six layers are identical in all six. Tempo and key are numbers everywhere
now. What changed: Suno keeps structure in its Lyrics field with Variety and Max
Mode as settings; Lyria puts structure inside the prompt as ranges; ElevenMusic
narrates the arrangement in order; the vocal disappears entirely for Stable
Audio. Conversion checklists: DATA_GOOGLE §10 and §10 of this file.

</rag_zone>

</section>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_OTHER_2026-09.md · SunoForge v4.0
// Snapshot date 2026-09-30 · replace this file, not the CORE files
// Next: DATA_VOCAB.md
// ═══════════════════════════════════════════════════════════════

<tags>elevenmusic, eleven music, music v2.5, music_v2_5, composer, muse, audio reference, finetunes, ownership on free, lossless downloads, stable audio 3.0, small sfx, medium 6:20, large, open weights, community license, daw plugin, lora, minimax music 3.0, structured captions, section tags, ace-step 1.5, yue2, abc score, local generation, offline, aggregators, regional access, free plans, /free, commercial use, platform compare, decision tree, portability, udio starstruck</tags>
</sunoforge_file>
