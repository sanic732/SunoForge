---
file_id: DATA_POSTPROD
version: "3.0"
layer: data
scope: mastering_chain · stems · editing_environments · daw_handoff · loudness · restoration · transfer_workflows
key_concepts: [mastering_chain, de_esser, glue_compression, harmonic_enrichment, surgical_eq, limiting, stems_builtin_vs_external, per_stem_processing, daw_handoff, loudness_targets, double_mastering]
depends_on: [DATA_SUNO, DATA_GOOGLE, DATA_VOCAB]
used_by: [CORE_00_ENTRY, CORE_03_DIAGNOSE, DATA_RECIPES]
rag_priority: medium
updated: "2026-07-27"
changelog: "v3.0 — stems reordered: built-in separation is now the default path and external tools the fallback · Studio and Flow Music feature lists replaced with references · unverified track-length claims removed · rights claims moved to DATA_LEGAL · loudness targets added"
---

# 🎛️ SUNOFORGE v3.0 — POST-PRODUCTION
# File 11 of 12 · DATA layer · mostly undated

> **Why this file is mostly undated.** A de-esser works the way a de-esser
> works. Frequencies, ratios and signal order do not change when a platform
> ships an update. What does change is which editing environment can do what,
> and those parts point at DATA_SUNO and DATA_GOOGLE rather than restating.

═══════════════════════════════════════════════════════════════════
§1. SHOULD YOU PROCESS THIS AT ALL?
═══════════════════════════════════════════════════════════════════

<rag_zone id="whether_to_process">

The first question, and the one most people skip.

Generated audio usually arrives already mastered — limited, balanced and
loud. Treating it as a raw mix and running a full chain over it makes it
worse, not better. That is the single most common post-production mistake
with this material, and it is worth stating before anything else.

─── WHEN TO LEAVE IT ALONE ───

  ✅ You like it, and it is going straight to a listener
  ✅ It is background for a video and sits under a voice anyway
  ✅ You are auditioning ideas rather than finishing one

─── WHEN PROCESSING EARNS ITS PLACE ───

  ✅ The track sits in a mix with other material and has to match it
  ✅ You are combining generated audio with recorded performances
  ✅ A specific problem is audible — sibilance, a resonance, a muddy low mid
  ✅ You are cutting between several generations and levels jump
  ✅ You are delivering to a specification with a loudness target (§9)
  ✅ You have separated stems and are rebalancing the arrangement

─── THE ORDER OF PREFERENCE ───

  1. FIX IT IN THE PROMPT. A better description costs one regeneration and
     no processing at all (CORE_01).
  2. FIX IT IN THE PLATFORM. Modern editing environments move a lot of this
     work upstream — a muddy stem or baked-in reverb no longer requires a
     perfect prompt (§6).
  3. FIX IT IN A DAW. When the first two cannot reach it.

  Reaching for the third when the first would do is how people spend an hour
  rescuing a take they could have regenerated in ninety seconds.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. THE MASTERING CHAIN
═══════════════════════════════════════════════════════════════════

<rag_zone id="mastering_chain">

Five stages, in this order. The order matters more than the tools — each
stage assumes the previous one has already happened.

  Everything below is [COMMUNITY] — standard mastering practice adapted for
  generated material, not vendor guidance. Starting values, not settings to
  apply blind. Use your ears; these are where to begin.

─── STAGE 1 · DE-ESSING ───

  PURPOSE     control harsh sibilance in the 3–7 kHz region
  THRESHOLD   around −3 dB
  REDUCTION   around 2 dB on peaks only
  WHY FIRST   everything downstream amplifies what you leave here.
              Compressing first makes sibilance louder, then you are
              de-essing a problem you just made worse.
  TOOLS       any dedicated de-esser; a dynamic EQ band works as well

  Generated vocals tend to sibilance more than recorded ones. This stage is
  rarely skippable on vocal material and rarely needed on instrumentals.

─── STAGE 2 · GLUE COMPRESSION ───

  PURPOSE     hold the whole track together and even out level
  TYPE        transparent bus compressor
  RATIO       2:1 to 4:1 — gentle
  RELEASE     around 0.1 s for rhythmic material; longer for slow material
  GAIN REDUCTION  1–3 dB at the loudest points. If the meter is moving more
              than that, the source has a balance problem that compression
              will not fix
  TOOLS       a bus compressor of the classic console type, or a well-known
              FET compressor for a more aggressive character

  "Glue" is the goal, not loudness. If you can hear it working, it is doing
  too much.

─── STAGE 3 · HARMONIC ENRICHMENT ───

  PURPOSE     vintage warmth and definition; makes digital material feel
              recorded rather than rendered
  TYPE        tape saturation or transformer colour
  DRIVE       low — this is seasoning
  FOCUS       a lift around 2–4 kHz is what reads as "definition"
  TOOLS       a tape machine emulation, or a transformer or console
              saturation plugin

  This stage is optional and the most stylistic. Skip it on material that is
  already warm — it is a corrective for clinical digital output, and lo-fi
  material does not need help sounding analog.

─── STAGE 4 · SURGICAL EQ ───

  PURPOSE     targeted correction, not tone shaping
  STARTING MOVES
    50–70 Hz        +2 to +3 dB for weight and warmth
    80–120 Hz       −1 to −2 dB where the low end is congested
    high-pass       30–40 Hz, to remove rumble that costs headroom
                    and contributes nothing audible
    around 8 kHz    +1 to +2 dB for clarity and air
  TOOLS       a transparent parametric EQ

  ⚠️ Cut narrow, boost wide. A narrow boost sounds like a resonance; a narrow
  cut sounds like nothing at all, which is what you want when removing a
  problem frequency. The frequency map for deciding what to reach for is in
  DATA_VOCAB §2.

  ⚠️ Order note: EQ after saturation, because saturation generates new
  harmonic content that you may then need to correct.

─── STAGE 5 · LIMITING ───

  PURPOSE     safety and final level
  TYPE        lookahead limiter, true-peak aware
  CEILING     −1 dBTP. Not −0.1: lossy encoding for streaming creates peaks
              above the ceiling you set, and −1 leaves room for them
  REDUCTION   as little as gets you to your target (§9)
  TOOLS       any modern true-peak limiter

  If you need more than 3–4 dB of limiting to hit your target, the problem is
  earlier in the chain. Go back to stage 2.

─── THE WHOLE CHAIN, SHORT ───

```
de-ess  →  glue compress  →  saturate  →  EQ  →  limit
```

  On generated material that arrives already mastered, stages 2 and 5 are
  often unnecessary and actively harmful (§3).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. WHAT NOT TO DO
═══════════════════════════════════════════════════════════════════

<rag_zone id="what_not_to_do">

─── ❌ DOUBLE MASTERING ───

The most damaging and most common error with this material.

If the platform delivered a finished master — limited and loud — running a
mastering chain over it compounds the limiting. The result is flat, fatiguing
and often distorted in the low mids, and no amount of subsequent EQ recovers
the dynamics that were destroyed.

  HOW TO TELL: look at the waveform. If it is a solid block with no visible
  peaks, it has already been limited. Do not limit it again.

  WHAT TO DO INSTEAD: work from stems (§4), which are delivered before the
  master bus, or accept the master as it is and only correct specific
  problems with narrow EQ.

─── ❌ OVER-COMPRESSION ───

Heavy dynamic compression kills the natural phrasing that makes a vocal
performance convincing. Generated vocals are already fairly consistent in
level, so they need less than a recorded performance, not more.

  If the vocal sounds robotic after processing and did not before, this is
  why.

─── ❌ PHASE-INCOMPATIBLE STEREO WIDENING ───

Widening by delaying one channel against the other produces impressive width
on headphones and partial cancellation in mono — which is what a phone
speaker, a club system's subwoofer and many broadcast paths actually play.

  ✅ USE     mid/side processing, or multiband widening applied only above
             roughly 300 Hz
  ❌ AVOID   delay-based widening across the whole spectrum
  ALWAYS     check in mono before delivering. If the low end disappears,
             something in the chain is out of phase.

  Around 50–60% of the available widening is a natural-sounding ceiling
  [COMMUNITY]. Beyond that it starts sounding hollow in the centre.

─── ❌ FIXING A BAD ARRANGEMENT WITH PROCESSING ───

If two instruments occupy the same range and mask each other, EQ can only
trade one for the other. The fix is a different arrangement — a different
instrument, a different register, or one of them removed. Regenerate with a
clearer instrumentation instruction (CORE_01 §5).

─── ❌ MASTERING BEFORE THE ARRANGEMENT IS FINISHED ───

Process last. Every change upstream invalidates the decisions you made
downstream.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. STEMS
═══════════════════════════════════════════════════════════════════

<rag_zone id="stems">

─── THE DEFAULT PATH HAS CHANGED ───

⚠️ Earlier editions of this system treated external separation tools as the
main route to stems, with the platform's own separation as a secondary
option. That is now backwards.

Suno's separation was overhauled and its highest tier **regenerates** stems
using the model rather than filtering them out of a finished mix [OFFICIAL]. That is a
fundamentally different operation, and it is why the artefacts that made
external separation a compromise are largely absent. Modes, what each does,
which plans have them and what they cost: **DATA_SUNO §9**.

  ORDER OF PREFERENCE NOW:
  1. The platform's own separation, where available
  2. External separation tools, as a fallback

─── WHEN EXTERNAL TOOLS STILL WIN ───

  ✅ The audio did not come from a platform with built-in separation
  ✅ You are separating a track you did not generate
  ✅ You need to work offline or in bulk
  ✅ The platform's separation is behind a tier you do not have
  ✅ You want a specific separation model's particular character

  Otherwise, separating inside the platform is both better and cheaper in
  effort.

─── WHICH SEPARATION FOR WHICH JOB ───

  Just need the vocal off, or just the vocal
    → the simplest isolation mode. Fast and cheap.

  Need the whole band laid out for a DAW
    → full multi-category separation.

  Need one clean instrument for sampling or replacement, and artefacts are
  unacceptable
    → the regenerating mode, where available. This is the one that changed
      the calculus.

  Specifics and costs: DATA_SUNO §9. Stem work is the expensive operation on
  most platforms — considerably more than generating the track was.

─── WHAT SEPARATION CANNOT DO ───

Separation cannot recover information that was never distinct. Two guitars
playing the same part in the same register will not come apart, no matter
which tool you use. If you need them separate, generate them separately.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. PROCESSING INDIVIDUAL STEMS
═══════════════════════════════════════════════════════════════════

<rag_zone id="stem_processing">

Once separated, each stem wants a different treatment. Starting points, all
[COMMUNITY]:

─── VOCALS ───

```
de-ess  →  compress  →  EQ  →  reverb and delay
```

  DE-ESS      first, always — see §2
  COMPRESS    3:1 to 4:1, more than you would use on the bus, aiming for a
              consistent front-of-mix level
  EQ          high-pass around 80–100 Hz; cut whatever muddiness sits in
              the 200–400 Hz region; lift presence around 3–5 kHz for
              intelligibility
  SPACE       add reverb last. Separated vocals often arrive with the
              original reverb still attached — if the platform offers a
              dry-stem or effect-removal option, use it before adding your
              own, or the two spaces will fight

─── DRUMS ───

```
transient shaping  →  parallel compression  →  EQ
```

  TRANSIENTS  restore attack that separation softened
  PARALLEL    compress a duplicate hard and blend it under the original —
              adds weight without flattening the dynamics
  EQ          lift 60–80 Hz for kick weight, 200 Hz down if boxy, 5–8 kHz
              up for snare crack and cymbal definition

─── BASS ───

```
high-pass  →  compress  →  saturate
```

  HIGH-PASS   30–40 Hz to remove inaudible rumble that eats headroom
  COMPRESS    firmly — bass benefits from consistency more than any other
              element
  SATURATE    adds harmonics an octave up, which is how bass stays audible
              on speakers that cannot reproduce the fundamental at all
  MONO        keep the bass centred below roughly 120 Hz

─── MELODIC AND HARMONIC PARTS ───

```
EQ to make room  →  stereo placement
```

  EQ          carve out the vocal's range rather than boosting the vocal —
              subtractive space is more natural than additive presence
  PLACEMENT   widen or pan to create separation from the centre

─── THE PRINCIPLE ───

Make room rather than making things louder. Every boost costs headroom and
crowds something else. Most mixes improve more from three well-placed cuts
than from any boost.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. EDITING ENVIRONMENTS
═══════════════════════════════════════════════════════════════════

<rag_zone id="editing_environments">

Three places to do this work, with different strengths.

─── THE PLATFORM'S OWN EDITOR ───

Suno's editing environment offers per-track EQ with presets, effect removal
for dry stems, time-stretching with markers, alternate takes in lanes,
meters beyond 4/4, and export as full mix, multitrack or MIDI [OFFICIAL]. Feature list,
version and which plan it requires: **DATA_SUNO §8**.

  WHAT IT CHANGES ABOUT PROMPTING: less than people expect, and that is the
  point. It moves fixes downstream. A muddy stem or baked-in reverb no longer
  demands a perfect prompt or a full regeneration. Prompt for the
  performance; repair the mix afterward.

  STRONGEST AT: working with material generated in the same place,
  multitrack takes, precise time alignment to picture, and anything
  involving a trained voice or a custom model.

─── GENERATIVE EDITING ───

Google Flow Music works differently: instead of editing audio, you ask for
part of it to be regenerated. Replace one instrument, extend a section,
change a passage — without touching the rest. Mechanics and how to write the
instructions: **DATA_GOOGLE §7**.

  STRONGEST AT: changing musical content rather than sonic character. It can
  give you a different guitar solo. It cannot give you a −1 dBTP master.

  ⚠️ Earlier editions claimed a specific maximum track length here and built
  a recommendation on it. That figure is not published (DATA_GOOGLE §7).

─── A DAW ───

Strongest at everything the other two cannot do: combining generated audio
with recorded performances, precise automation, third-party processing, and
final delivery to a specification.

  Also the only environment where you own the session and it will still open
  in five years.

─── CHOOSING ───

  Change what is played              → generative editing
  Change how it sounds               → the platform editor, then a DAW
  Combine with recorded material     → a DAW
  Deliver to a loudness spec         → a DAW
  Match several tracks to each other → a DAW

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. HANDING OFF TO A DAW
═══════════════════════════════════════════════════════════════════

<rag_zone id="daw_handoff">

─── EXPORT BEFORE YOU LEAVE ───

  ✅ Highest quality format available — never a lossy file if a lossless one
     is offered. Every subsequent process compounds encoding artefacts.
  ✅ Stems as well as the full mix, even if you think you only need the mix.
     Going back for them later means regenerating, and the regeneration will
     not match.
  ✅ MIDI where offered — it survives every future decision and lets you
     replace a part entirely.
  ✅ A dry version, if effect removal is available, alongside the processed
     one.

─── ORGANISE ON ARRIVAL ───

```
1  import stems, aligned to the same start point
2  check phase — sum to mono and confirm nothing disappears
3  gain-stage: pull everything down so the bus is not already clipping
4  group by section — drums, bass, harmony, lead, vocal
5  only then start processing
```

  Step 3 matters more than it looks. Stems that summed correctly in the
  platform frequently clip a DAW bus, and everything you do afterward is
  built on a distorted foundation.

─── KEEP THE ORIGINAL ───

Archive the untouched export before you touch anything. Generated audio is
not reproducible: the same prompt does not return the same track, so an
unprocessed original is genuinely irreplaceable in a way that a recording of
a live performance never is.

─── WHAT NOT TO EXPECT ───

Generated stems are not multitrack recordings. Reverb and room may be baked
into individual parts, edits may not fall on bar lines, and tempo may drift
slightly. Warp and time-alignment tools exist for exactly this. Treat the
material as a live recording rather than a programmed session.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. RESTORATION
═══════════════════════════════════════════════════════════════════

<rag_zone id="restoration">

For fixing specific defects rather than shaping tone.

  PROBLEM                         APPROACH
  ─────────────────────────────── ────────────────────────────────────────
  metallic high-frequency ring    gentle low-pass or a narrow cut where the
                                  ringing sits; regenerating usually beats
                                  repairing (CORE_03 §5)
  digital chirping artefacts      dedicated artefact repair; often easier to
                                  regenerate the affected section
  a resonant frequency            narrow cut, found by sweeping a boost
                                  until it is unbearable, then inverting
  clipping already in the source  declipping, then rebuild headroom
  hiss or noise floor             broadband noise reduction, gently —
                                  aggressive settings sound underwater
  sibilance missed upstream       dynamic EQ on the offending band
  a hard cut at the end           fade it, or extend and cross-fade

─── TOOL CATEGORIES ───

  RESTORATION SUITES     spectral repair, declipping, noise reduction
  QUICK-FIX PROCESSORS   one-knob versions of the above, adequate for most
  MASTERING SUITES       analysis-assisted chains, useful as a reference
                         even if you do not take their recommendations
  ONLINE MASTERING       automated; genuinely useful when you have no
                         monitoring environment you trust

  ⚠️ Automated mastering on already-mastered generated audio produces the
  double-mastering problem (§3) with no warning. It cannot tell the
  difference between a raw mix and a finished master.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§9. LOUDNESS AND DELIVERY
═══════════════════════════════════════════════════════════════════

<rag_zone id="loudness">

─── TARGETS ───

[COMMUNITY] Streaming platforms normalise playback, so mastering louder than
their target gains nothing and costs dynamics — the platform simply turns it
down, and you are left with a flatter track played at the same volume as
everyone else's.

  Streaming, general              around −14 LUFS integrated
  Podcast and spoken-word beds    around −16 LUFS integrated
  Broadcast                       per the broadcaster's specification,
                                  usually stricter and non-negotiable
  Club and DJ use                 louder is conventional here; normalisation
                                  does not apply
  Archive and further production  do not limit at all; leave headroom

  TRUE PEAK: −1 dBTP for anything that will be encoded to a lossy format.

  ⚠️ These figures move. Check the current specification for your
  destination rather than trusting a number in a file dated last quarter.

─── THE LOUDNESS TRAP ───

Generated audio often arrives already close to a streaming target. Pushing
it louder to match a commercial reference is almost always a mistake — the
reference you are comparing against will be normalised down to the same level
on playback, and yours will have lost its dynamics for nothing.

  Compare at matched loudness, always. Louder sounds better for about ten
  seconds, and that is long enough to make a bad decision.

─── DELIVERY CHECKLIST ───

  ☐ Checked in mono — nothing disappears
  ☐ True peak at or below −1 dBTP
  ☐ Integrated loudness at the destination's target
  ☐ No clipping anywhere in the chain, not just at the output
  ☐ Fades at both ends, unless an abrupt start or end is intentional
  ☐ Listened all the way through, once, without touching anything
  ☐ Listened on a phone speaker
  ☐ Original unprocessed export archived
  ☐ Rights position understood before it goes anywhere — DATA_LEGAL

</rag_zone>

═══════════════════════════════════════════════════════════════════
§10. MOVING MATERIAL BETWEEN PLATFORMS
═══════════════════════════════════════════════════════════════════

<rag_zone id="transfer_workflows">

─── A SKETCH INTO A FULL TRACK ───

A short generation is a good way to test an idea cheaply before committing.
Turning one into a finished piece:

```
1  LISTEN    decide precisely what you liked. Usually one element, not all
2  ANALYSE   name it in the four axes — timbre, dynamics, groove, space
             (DATA_VOCAB)
3  REBUILD   write a full six-layer description containing that element
             (CORE_01), rather than trying to extend the sketch
4  GENERATE  on the platform that suits the finished piece, which may not
             be the one you sketched on (DATA_OTHER §6)
```

  Rebuilding beats extending here. A thirty-second sketch does not contain
  enough information to grow into three minutes, and extending it inherits
  its limitations.

─── COMBINING GENERATIONS FROM DIFFERENT PLATFORMS ───

Workable, with two cautions:

  ⚠️ TONAL MISMATCH. Different platforms have different characteristic
  brightness and stereo width. Match them with broad EQ and width adjustment
  before doing anything else, or the join will be audible no matter how well
  you edit it.

  ⚠️ PROVENANCE. Different platforms attach different rights to their output,
  and a track combining two sources carries both sets of terms. Some outputs
  also carry inaudible watermarking that survives editing. If the result is
  commercial, work this out before you build it, not after — DATA_LEGAL.

─── A GENERATED BED UNDER A RECORDED PERFORMANCE ───

```
1  generate the instrumental, explicitly instrumental (CORE_03 §5)
2  export stems, not just the mix
3  record over it in a DAW
4  carve space in the bed for the recorded part — subtractive EQ (§5)
5  master the combination as one piece, not the bed separately
```

  Step 4 is where this usually fails. A generated bed is mixed to be complete
  on its own, so it has no gap for a lead. Make one.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§11. THREE WALKTHROUGHS
═══════════════════════════════════════════════════════════════════

<rag_zone id="walkthroughs">

─── A · A SONG YOU INTEND TO RELEASE ───

```
1   Generate on a paid plan from the start. Free-tier output cannot be
    licensed retroactively — DATA_OTHER §5.
2   Generate several takes. Choose on the performance, not the mix; the
    mix is fixable and the performance is not.
3   Export the highest-quality full mix AND the stems AND MIDI if offered.
4   Archive the untouched export somewhere you will not overwrite it.
5   Listen once, all the way through, writing down problems without
    fixing any of them.
6   Decide from that list whether you need processing at all (§1).
7   If yes: work from stems, not the master. Balance first, process second.
8   Per-stem treatment (§5) — only where you wrote something down.
9   Bus: gentle glue only. Do not re-master an already-mastered file (§3).
10  Check in mono. Check on a phone. Check at a low volume.
11  Limit to −1 dBTP, to the target for the destination (§9).
12  Confirm the rights position before it goes anywhere — DATA_LEGAL.
```

  Steps 5 and 6 are the ones people skip, and skipping them is how a track
  gets an hour of processing it did not need.

─── B · A BED THAT SITS UNDER A VOICE ───

```
1   Generate instrumental, all three protections in place (CORE_03 §5).
2   Generate longer than the final requirement. Trimming is free;
    extending is not.
3   Import the voiceover and the bed into a DAW together.
4   Carve a wide, gentle dip in the bed across the speaking range —
    roughly 300 Hz to 3 kHz, two or three decibels, no more.
5   Ride the bed level manually under the speech rather than relying on
    automatic ducking. Ducking breathes audibly on music.
6   Mix so the bed is quieter than feels right in isolation. It will be
    right in context, and it will be too loud on a phone otherwise.
7   Master to the spoken-word target (§9), not the music target.
8   Listen once with your attention on the words. If you notice the music,
    it is still too loud.
```

─── C · REBUILDING A TRACK FROM ITS STEMS ───

For when the material is right and the balance is wrong.

```
1   Separate — inside the platform where possible (§4).
2   Import stems aligned to a common start.
3   Sum to mono and confirm nothing cancels. Fix phase before anything
    else; every later decision depends on it.
4   Pull every fader down. Rebuild the balance from silence, starting with
    the element the song is actually about — usually the vocal or the
    lead, not the drums.
5   Solo as little as possible. Balance decisions made in solo do not hold
    up in context.
6   Only once the balance works, begin processing (§5).
7   Replace anything that will not sit. A stem that resists every attempt
    to place it is usually an arrangement problem, and generating a
    replacement part costs less than another hour of EQ.
8   Master the rebuilt mix as a new piece.
```

  ⚠️ Rebuilt stems will not sound identical to the original mix, and should
  not. If the goal was the original mix with one thing changed, generative
  editing is the better route (§6).

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_POSTPROD.md · SunoForge v3.0
// Next: DATA_LEGAL_2026-07.md
// ═══════════════════════════════════════════════════════════════
