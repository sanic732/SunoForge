---
file_id: DATA_SUNO
version: "3.0"
layer: data
valid_as_of: "2026-07-27"
expires: "this file describes a platform that ships changes monthly — verify before trusting anything here after 2026-10"
scope: suno_versions · fields · sliders · voices · custom_models · studio · stems · plans
key_concepts: [version_matrix, style_field, exclude_styles, duration_slider, voices, custom_models, studio_12, stems, credits, plans]
depends_on: [CORE_00_ENTRY]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE, DATA_RECIPES, DATA_POSTPROD, DATA_LEGAL]
rag_priority: critical
authority: "THIS FILE IS THE SINGLE SOURCE OF TRUTH FOR SUNO VERSIONS AND LIMITS"
updated: "2026-07-27"
---

# 🟠 SUNOFORGE v3.0 — SUNO PLATFORM DATA
# File 6 of 12 · DATA layer · valid as of 2026-07-27

> ⚠️ **Expiry notice.** Everything in this file is a snapshot. Suno shipped seven
> user-facing changes between March and July 2026. If today is more than a quarter
> past the date above, treat every number here as a starting hypothesis, not a fact.
> Replace this file; leave the CORE_* files alone.

> 📌 **Single source rule.** Version numbers, field limits, credit costs and plan
> tiers live here and nowhere else. If you find them repeated in another file,
> that is a defect — delete the copy and link here instead.

═══════════════════════════════════════════════════════════════════
§1. VERSION MATRIX
═══════════════════════════════════════════════════════════════════

<rag_zone id="suno_version_matrix">

─── v5.5 — CURRENT, DEFAULT ─── [OFFICIAL] released 2026-03-26
Positioning: Suno's most expressive and most personal model.
Exclusive:
  - Voices — sing in your own voice (§5)
  - Custom Models — train on your own catalog (§6)
  - My Taste + Magic Wand — free for every account, including free tier
  - Duration Slider — explicit track length, web only (§4)
Plans: Pro and Premier. Not available on free.

─── v5 ─── [OFFICIAL]
Studio-grade audio, realistic vocals, JSON-style structuring accepted.
Superseded by v5.5 for most work; still selectable.

─── v4.5-all — FREE TIER ─── [OFFICIAL]
The model free accounts get. Described by Suno as a free model for everyone.
Still active, no deprecation announced.
Limitations that matter in practice:
  - no Voices, no Custom Models, no Studio
  - no Duration Slider (it is v5.5-only)
  - non-commercial use only — and upgrading later does NOT retroactively grant
    commercial rights to tracks made on free

─── v6 — DOES NOT EXIST ─── [OFFICIAL as of 2026-07-27]
No release-notes entry, no help-center article, no model in the picker.
Suno has said a first model developed together with the music industry is coming;
no name, no date. Anything calling itself "Suno v6" today is speculation.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. THE STYLE FIELD — limits, weighting, and the myth
═══════════════════════════════════════════════════════════════════

<rag_zone id="style_field">

WHAT IS ACTUALLY KNOWN:

  [OFFICIAL]   Suno publishes no numeric character limit for the Style field.
               The help center and release notes are silent on this.

  [COMMUNITY]  Third-party API wrappers document a hard server-side limit:
               1000 characters on v4.5-all / v4.5+ / v5 / v5.5,
               200 characters on v4 and older.
               Verified indirectly — exceeding it returns an HTTP 400 before any
               credits are spent. This is community-verified, not vendor-stated.

  [COMMUNITY]  Measurable influence fades well before the hard limit. Independent
               testing puts the practical ceiling near 300–400 characters.

  [COMMUNITY]  Independent guides converge on 5–8 strong descriptors — roughly
               80–180 characters — as the range where the prompt reliably steers
               the result. Past ~10 descriptors, signals start contradicting.

  [UNVERIFIED] "Attention collapses after 200 characters." No controlled test
               supports a cliff at that number. This claim shipped in an earlier
               edition of SunoForge and was wrong — it made users cut prompts to a
               fifth of the working range. Corrected here.

DOES v5.5 PREFER LONG OR SHORT PROMPTS?
  Sources genuinely disagree, and Suno has not taken a side.
  [COMMUNITY] One camp: v5.5 rewards description; several rich sentences beat tag
              stacks, because the model now distinguishes adjacent descriptors.
  [COMMUNITY] Other camp: tight prompts near 120 characters consistently produce
              cleaner songs; a bigger field does not mean better music.
  WHAT BOTH AGREE ON: front-loading and specificity beat raw length. Order matters
  more than word count. Start at 5–8 descriptors; add only what changes the sound.

PRACTICAL SHAPE:
  genre + era · mood in 1–2 words · 3–4 instruments · vocal gender and
  character · production signature · parameters as prose (BPM, key, space)

  ⚠️ Those are slot names, not syntax. Nothing above goes into the field in
  brackets — the whole thing is written as one plain sentence, as in the
  example below. Bracketed `parameter: value` forms are not read (CORE_02 §1).

  Example:
    mid-90s Seattle grunge, weary and defiant, detuned electric guitar, heavy bass,
    live drums, male baritone with a gravelly worn delivery, analog tape saturation,
    wide stereo field, 92 BPM, D minor

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. EXCLUDE STYLES — now a real field
═══════════════════════════════════════════════════════════════════

<rag_zone id="exclude_styles">

[OFFICIAL] Suno added a dedicated negative field. Pro and Premier specify styles,
instruments or vocal traits to keep out, using a leading minus: `-piano`.
Early access; behavior improves through thumbs up/down feedback.

WHAT IT IS GOOD AT:
  - removing an instrument the genre would otherwise drag in
  - suppressing a production aesthetic ("polished pop production", "auto-tune")
  - keeping an era out of a period piece

WHAT IT DOES NOT SOLVE:
  - vocal gender. Use the Advanced Options gender selector instead [COMMUNITY —
    the most reliable control anyone has found]

HOW TO WRITE IT:
  8–12 items, musical vocabulary, not engineering jargon.
  Specific beats generic: "polished pop production" outperforms "pop".

  GOOD: EDM, auto-tune, overproduced, electronic drums, heavy bass, crowd noise
  BAD:  brick-wall compression, dithering, sidechain   ← engineering terms
  BAD:  bad sound, weird, cheap                        ← not musical categories

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

NEGATIVES IN THE STYLE FIELD (as opposed to the Exclude field):
  [COMMUNITY] Weak and sometimes counterproductive. Naming a concept can summon it.
  Keep at most one or two, always paired with a strong positive statement.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. DURATION SLIDER
═══════════════════════════════════════════════════════════════════

<rag_zone id="duration">

[OFFICIAL] Added 2026-07-20. Web only. v5.5 only. Located under Advanced →
More Options, alongside Weirdness and Style Influence.

[COMMUNITY] Range and behavior from independent testing:
  - 10 seconds minimum, 6 minutes maximum, 5-second steps
  - Auto mode leaves length to the model and lands near 3 minutes
  - Custom mode is the only way to go longer
  - The value is a TARGET, not a guarantee. Long settings often undershoot;
    testers recommend 5:45 rather than 6:00, backed by enough lyrics to fill it
  - If the audio has not resolved by the target, it cuts abruptly

RELATIONSHIP TO EXTEND: complementary, not a replacement. Duration shapes the
initial generation; Extend still adds material to a finished track.

LENGTH WITHOUT THE SLIDER — v4.5-all and the free tier:
  The slider is v5.5-only, but that does not cap the free model at some short
  length. [COMMUNITY] Suno's own help center has long stated that v4.5 and v5
  generate up to 8 minutes in one pass.
  [COMMUNITY, first-hand] A user report from 2026-07 reached 7 minutes 59 seconds
  on free v4.5-all in a single generation, with a full multi-verse lyric sheet.
  What drives length there is the amount of lyrics, not a control.
  ⚠️ Guides claiming the free tier is limited to about 2 minutes are wrong.
  That figure circulates widely and has no source behind it.

WHAT THIS RETIRES: any guide claiming "Suno decides the length" or "4+ minutes
requires Extend" predates 2026-07-20.

PRACTICAL PAIRING:
  Set duration AND give the lyrics to fill it. A 5-minute target with two verses
  produces padding, instrumental drift, or an early cut.
  Rough guide: ~1 minute of song ≈ one verse + one chorus at moderate tempo.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. VOICES — your own voice
═══════════════════════════════════════════════════════════════════

<rag_zone id="voices">

[OFFICIAL] Introduced with v5.5 on 2026-03-26. Pro and Premier only.
Personas from the v5 era were renamed to Voices and migrated automatically.

INPUT LENGTH — three different numbers, all correct, for different things:
  [OFFICIAL]  15 seconds to 4 minutes — the accepted range in the help center
  [OFFICIAL]  30 seconds minimum for uploads — stated in Suno's own walkthrough
  [COMMUNITY] 10–15 seconds minimum for live recording in the browser
  [COMMUNITY] 90–120 seconds of varied singing gives the best result
  From the file, the best 2 minutes are selected for training.

  ⚠️ Earlier SunoForge editions stated "30s minimum" and "15s minimum" as if one of
  them were wrong. Both were right, about different input paths.

AUDIO REQUIREMENTS:
  Acapella preferred. Backing music is accepted — stems are separated automatically.
  A quiet room helps; a studio is not required.

VERIFICATION [OFFICIAL]:
  You read a random phrase on screen; it is matched against the singing clip.
  This exists to block cloning someone else's voice.
  A consent checkbox permits Suno to use the voice to train and improve models —
  read it before uploading. See DATA_LEGAL.

PRIVACY: Voices are tied to the account and cannot be shared or made public.

COST: [UNVERIFIED] Guides from spring 2026 cite 4 credits per generation during
beta; others report that normal song credits apply and no separate price exists.
Suno publishes no figure. The Create-a-Voice panel still carries a Beta label.
Assume normal credits, verify in your own account before planning around it.

WORKING WITH VOICES:
  - Draft with stock vocals, switch to your Voice for the final take
  - Audio influence above ~50% keeps the result recognizable [COMMUNITY]
  - It is directional, not exact cloning — expect your character, not your double
  - Give the model range: sing high and low, loud and soft, in the source clip

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. CUSTOM MODELS — train on your catalog
═══════════════════════════════════════════════════════════════════

<rag_zone id="custom_models">

[OFFICIAL] Pro and Premier. Upload at least 6 of your own tracks; up to 3 models
per account; training takes roughly 2–5 minutes; the model appears in the picker.
Models are private and cannot be shared.

[OFFICIAL] You must own the rights to every song you upload. This is enforced by
terms, not by a technical check — the responsibility is yours.
[UNVERIFIED] What happens to a model after a copyright complaint is not documented.

[COMMUNITY] 6 is the floor, not the target. Ten to sixty stylistically consistent
tracks produce a noticeably sharper model. Consistency matters more than count —
a catalog spanning six genres teaches the model to average them.

STRATEGIES THAT WORK:
  "Band" model        6+ tracks by one project → its signature arrangement habits
  "Beat" model        6+ lo-fi or trap instrumentals → consistent groove and mix
  "Score" model       6+ cinematic pieces → reusable soundtrack generator
  "Client" model      a client's catalog (with written permission) → on-brand music
  Switch models per task rather than building one model for everything.

WHAT IT TRANSFERS: arrangement habits, harmonic tendencies, production texture,
instrument choices. Not lyrics, not melody, not a specific singer.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. SLIDERS
═══════════════════════════════════════════════════════════════════

<rag_zone id="sliders">

Weirdness            how experimental the result is. Low = genre-safe.
Style Influence      how strictly the Style prompt is obeyed. High = literal.
Audio Influence      for remix and extend: how much of the original survives.
Vocal Gender         [COMMUNITY] the most reliable vocal-gender control available.

BY GOAL:
  Authentic genre recreation    Weirdness 20–35% · Style Influence 90–100%
  Balanced creative fusion      Weirdness 40–50% · Style Influence 70–85%
  Wild experiment               Weirdness 70%+   · Style Influence 40–60%
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
  Metalcore / extreme Weirdness 45–65% · Style 70–85%
  Gospel / choir      Weirdness 25–45% · Style 85–95%  arrangement must stay legible
  Folk / singer-songwriter  Weirdness 25–45% · Style 80–95%

FOR EXTEND: lower weirdness than the base track, around 45–55% [COMMUNITY].
High weirdness during extension is a common cause of sudden genre shifts.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. SUNO STUDIO — version 1.2
═══════════════════════════════════════════════════════════════════

<rag_zone id="studio">

[OFFICIAL] Studio 1.2 shipped 2026-02-16. **Premier only.**
⚠️ Earlier SunoForge editions said "available with Suno Pro". That was wrong and
misled users about which subscription to buy.

FROM 1.1:
  Track EQ            6-band per track. Presets: Flat, High-pass, Vocal, Warm,
                      Presence, Bass Boost, Air, Clarity, Fullness, Lo-fi, Modern
  Loop Recording      repeat a section, stack takes quickly
  Context Window      limit what the model sees when generating a new clip
  Cover Mode on stems piano → guitar, hum → full instrument, rhythm preserved
  Project Library     reworked

NEW IN 1.2:
  Remove FX           dry stems out of reverb-soaked clips
  Warp Markers        manual and transient-based time-stretching, with quantize
  Alternates          take lanes — multiple versions per track, auditioned in place
  Time Signatures     beyond 4/4 — 3/4, 6/8, 7/8, 11/4 via the transport bar

EXPORT: full mix, multitrack stems, and MIDI.

WHAT IT CHANGES ABOUT PROMPTING: less. Studio moves fixes downstream — a muddy
stem or baked-in reverb no longer requires a perfect prompt or a regeneration.
Prompt for the performance; repair the mix in Studio.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§9. STEM SEPARATION — three modes
═══════════════════════════════════════════════════════════════════

<rag_zone id="stems">

[OFFICIAL] Overhauled 2026-06-11. Reached from the Edit menu → "Get Stems".

  Auto Split        12 stem categories, the classic model
                    Pro + Premier · 50 credits per extraction

  Split from Mix    isolate any one chosen element against "everything else"
                    Pro + Premier · 10 credits (20 for a pair)

  Advanced Split    close to 100 instruments; stems are REGENERATED by the model
                    rather than filtered out of the mix, which is why artifacts
                    are dramatically lower
                    **Premier only** · 10 credits per stem (20 per pair)

The instrument list in Advanced Split reaches into unusual territory — theremin,
didgeridoo, 808 — not just the standard band layout.

WHEN TO USE WHICH:
  Need a quick vocal/instrumental split        → Split from Mix
  Need the full band laid out for a DAW        → Auto Split
  Need one clean instrument for sampling or
  replacement, and artifacts are unacceptable  → Advanced Split

⚠️ Earlier editions treated external tools as the main path for stems. They are now
the fallback, not the default — see DATA_POSTPROD for when leaving Suno still wins.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§10. LYRICS EDITOR — rebuilt
═══════════════════════════════════════════════════════════════════

<rag_zone id="lyrics_editor">

[OFFICIAL] Rebuilt 2026-07-09, web.
  Lyricist profiles      lock in a writing voice and reuse it across songs
  Natural language edits ask for changes in plain words instead of retyping
  Variations & References rhyme and reference suggestions
  Full-screen editor     distraction-free writing
  Structure labels       the editor places section markers itself
  Autosave

WHAT THIS CHANGES FOR PROMPTING:
On the web, hand-marking every section is no longer mandatory — the editor does it.
Two paths now coexist, and a prompt system must support both:
  - web with the new editor → supply clean lyrics, let the editor label sections
  - API, mobile, or pasting → supply lyrics already marked up
CORE_02_LYRICS covers the markup path in full.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§11. PLANS, CREDITS, RIGHTS
═══════════════════════════════════════════════════════════════════

<rag_zone id="plans">

[COMMUNITY] Figures consistent across multiple 2026 pricing guides:

  FREE      $0 · 50 credits/day (≈10 tracks) · v4.5-all
            NON-COMMERCIAL. Upgrading does not retroactively license old tracks.

  PRO       ≈$10/month (≈$8 annual) · 2,500 credits/month
            v5.5 · Voices · Custom Models · stems · commercial rights

  PREMIER   ≈$30/month · 10,000 credits/month
            everything in Pro · Suno Studio · Advanced Split · early access

[COMMUNITY] After the Warner partnership (Nov 2025), terms language shifted from
"you own this" to "you have commercial rights". The distinction matters — see
DATA_LEGAL.

CREDIT ARITHMETIC WORTH KNOWING:
  A generation produces 2 tracks. Auto Split alone costs 50 credits — a full day
  of free-tier allowance. Stem work is the expensive operation, not generation.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§12. WHAT SHIPPED SINCE v5.5 — the moving parts
═══════════════════════════════════════════════════════════════════

<rag_zone id="changelog_2026">

[OFFICIAL] Chronological, so a stale copy of this file can be diffed quickly:

  2026-03-26  v5.5 — Voices, Custom Models, My Taste
  2026-05-13  Android Auto and CarPlay
  2026-05-14  mobile UI overhaul, vocal gender selector, Create memory
  2026-06-04  iOS: share lyrics from Notes, audio from Voice Memos
  2026-06-11  stem separation overhaul — three modes (§9)
  2026-07-07  custom soccer anthem generator, mobile
  2026-07-09  lyrics editor rebuilt (§10)
  2026-07-15  iMessage keyboard — create and send songs inside Messages
  2026-07-20  Duration Slider (§4)

Also present in release notes without a firm date: Exclude Styles field (§3).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§13. MYTHS — kept here so they stop circulating
═══════════════════════════════════════════════════════════════════

<rag_zone id="myths">

These appear in guides, in previous SunoForge editions, and in forum advice.
None of them survived checking. Listed so the system can recognize and repair them
rather than pretend they never existed.

  "MAX MODE unlocks hidden quality"
  [UNVERIFIED] Controlled comparison (Jan 2026) across folk and reggae found no
  hidden mode. Originates from a single Reddit post. The tags act as ordinary
  quality adjectives — which is not nothing, but it is not a mode.

  "Style attention dies after 200 characters"
  [UNVERIFIED] No test shows a cliff there. Influence fades gradually past 300–400.

  "Parametric tags control the mix"
  [UNVERIFIED] [Reverb: 30%], [BPM: 120], [eq: scooped] were never parsed.
  Write them as prose instead.

  "Pipe stacking is deprecated in v5.5 and causes artifacts"
  [UNVERIFIED] Never documented as deprecated, artifacts never reproduced in a
  controlled test. Also never documented as supported. Genuinely unsettled.

  "Tracks drift to generic pop after two minutes"
  [UNVERIFIED] Anecdotal. No systematic testing, no vendor acknowledgment.

  "v5/v5.5 has 88% prompt adherence"
  [UNVERIFIED] Suno publishes no such metric. One independent review measured
  around 85% on lyric adherence specifically. The 88% figure has no source.

  "Studio comes with Pro"
  [OFFICIAL — corrected] Premier only.

  "Voices cost 4 credits per track"
  [UNVERIFIED] Cited in spring guides, contradicted by others, never published.

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_SUNO_2026-07.md · SunoForge v3.0
// Snapshot date 2026-07-27 · replace this file, not the CORE files
// ═══════════════════════════════════════════════════════════════
