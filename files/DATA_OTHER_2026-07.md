---
file_id: DATA_OTHER
version: "3.0"
layer: data
valid_as_of: "2026-07-27"
expires: "free-tier allowances and prices are the fastest-moving numbers in this whole system — verify before trusting anything here after 2026-10"
scope: elevenmusic · stable_audio · minimax · aggregators · free_tier_comparison · platform_selector
key_concepts: [elevenmusic_v2, section_regeneration, mid_track_genre_switch, stable_audio_3, open_weights, community_license, minimax_2_6, aggregators, free_tiers, platform_compare]
depends_on: [CORE_00_ENTRY, DATA_SUNO, DATA_GOOGLE]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE, DATA_LEGAL, DATA_POSTPROD]
rag_priority: high
authority: "SINGLE SOURCE OF TRUTH FOR ELEVENMUSIC, STABLE AUDIO AND MINIMAX SPECIFICATIONS"
updated: "2026-07-27"
---

# 🟣 SUNOFORGE v3.0 — OTHER PLATFORMS
# File 8 of 12 · DATA layer · valid as of 2026-07-27

> ⚠️ **Expiry notice.** Free allowances and subscription prices change more
> often than anything else in this system, and they change without
> announcement. If today is more than a quarter past the date above, treat
> every figure here as a starting hypothesis and check your own account.

> 📌 **Single source rule.** ElevenMusic, Stable Audio and MiniMax figures live
> here and nowhere else. Suno figures live in DATA_SUNO. Google figures live in
> DATA_GOOGLE. The comparison tables in §5 and §6 deliberately point at those
> files rather than copying their numbers — three copies of a specification is
> how the previous edition silently contradicted itself.

═══════════════════════════════════════════════════════════════════
§1. ELEVENMUSIC — menu [7i]
═══════════════════════════════════════════════════════════════════

<rag_zone id="elevenmusic">

The commercially cleanest option this system covers, and the only one whose
selling point is what it was *not* trained on.

─── WHAT MATTERS MOST ───

[COMMUNITY] Trained only on licensed material, and marketed on that basis for
commercial use. For advertising, film, and any client who will ask where the
music came from, this is the answer that survives the question.

─── MUSIC V2 ─── [COMMUNITY] released 2026-05-27

Three capabilities that are hard to find elsewhere:

  MID-TRACK GENRE SWITCHING
    A track can change genre partway through and change back — the
    demonstrations go as far as opera into metal and out again. Not a
    crossfade between two generations: one piece that moves.

  PER-SECTION REGENERATION
    Any section can be regenerated on its own while the rest stays untouched.
    Suno has no direct equivalent, and this alone justifies giving ElevenMusic
    its own line in any platform comparison rather than a footnote.

  IMPROVED FAST DELIVERY
    Rapid rap phrasing specifically called out as improved in this release.

─── SPECIFICATIONS ───

  Length      ⚠️ sources disagree. One line of reporting says up to five
              minutes; another describes a range from about fifteen seconds to
              eight minutes. Neither is vendor-confirmed in a citable form.
              [UNVERIFIED] Do not quote a maximum. Tell the user to check.
  Editing     section editor in the interface
  Stems       available
  Style       transfer from a reference of roughly ten to thirty seconds
  Platforms   web and iOS; Android was projected for Q3 2026 [COMMUNITY]
  Extras      integrates with the same vendor's speech and voice tooling

─── PRICING ─── [COMMUNITY]

  FREE   7 tracks per day
  PRO    around $9.99 per month, roughly 500 tracks
         commercial rights on the paid tier

─── PROMPTING ───

Descriptive prose, the same shape as Lyria (CORE_01 §2). No documented tag
syntax — bracket markup from Suno has no meaning here and will be ignored or
read as text. Structure is handled in the interface, not in the prompt.

```
A warm, mid-tempo indie folk-pop piece for a travel advertisement. Acoustic
guitar fingerpicking, brushed drums, a soft string pad arriving late. A warm
female lead, hopeful and close. Builds from almost nothing to full
arrangement, then falls away to a single guitar.
```

─── THE HONEST TRADE-OFF ───

[COMMUNITY] Expressive lead vocals are reported as its relative weakness — the
same conservatism in the training data that makes it legally clean makes it
less wild. If the vocal performance is the point of the track, generate it
elsewhere. If clearance is the point, generate it here.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. STABLE AUDIO 3.0 — menu [7j]
═══════════════════════════════════════════════════════════════════

<rag_zone id="stable_audio">

[OFFICIAL] Released 2026-05-19. The only platform in this system whose weights
you can hold.

─── THE FAMILY ───

  Small SFX    sound design and effects
  Small        short-form generation
  Medium       general use
  Large        the full model

  ⚠️ Open weights are published for Small SFX, Small and Medium. Large is not
  in that set.

─── LARGE — SPECIFICATIONS ───

  Maximum length   6 minutes 20 seconds
  Audio            44.1 kHz stereo
  Training data    licensed, from a commercial stock audio library
  Input            text, and audio-to-audio transformation

  That length is the longest single generation available anywhere in this
  system's coverage.

─── LICENSING ─── [OFFICIAL]

  A community licence grants ownership of the output and commercial use.
  Organisations above roughly $1M in revenue need an enterprise agreement.

  Read that as: individuals and small studios are covered by default; if you
  are large enough for it to matter, you are large enough to have a lawyer
  read the current terms. Broader context: DATA_LEGAL.

─── WHY IT REPLACED UDIO IN THIS SYSTEM ───

The previous edition kept Udio for instrumental and DAW work. Udio disabled
downloads after its settlement [OFFICIAL + COMMUNITY], which removes the
entire point of using it in a production pipeline — see DATA_LEGAL §7. Stable Audio occupies
the same niche and does it without the exposure: strong instrumental output,
clean licensing, and output you own and can run locally.

─── WHAT IT IS FOR ───

  ✅ instrumental beds, textures and sound design
  ✅ long-form ambient and background work
  ✅ anything that must run offline or on your own hardware
  ✅ anything where owning the output outright matters
  ✅ transforming existing audio rather than generating from nothing

  ❌ character-led vocal songs — not what it is built for

─── PROMPTING ───

Descriptive prose. Keep vocal language out entirely for instrumental work;
mentioning a singer in a prompt for a bed is the most common cause of
unwanted vocal artefacts here (CORE_03 §7).

```
A slow, spacious ambient bed. Sustained analog synth pads with a very slow
attack, a distant filtered piano figure repeating every few bars, and a low
sine drone underneath. No percussion. Unhurried, unresolved, and even
throughout. Instrumental.
```

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. MINIMAX MUSIC 2.6
═══════════════════════════════════════════════════════════════════

<rag_zone id="minimax">

[OFFICIAL] Released 2026-04-10. A reference entry rather than a recommended
target — worth knowing about, mainly for volume work through an API.

  COVER MODE     keep the melody, change the genre and the lyrics
  FIRST OUTPUT   under twenty seconds
  INSTRUMENTS    over one hundred

  The previous version worked with fourteen structural tags applied at the
  paragraph level.

─── WHERE IT FITS ───

  ✅ generating at volume through an API where unit cost dominates
  ✅ Cover mode specifically — melody-preserving genre change is unusual
  ✅ reachable through aggregators from regions where the majors are not (§4)

  ❌ vocal and instrumental quality below the leaders in this system
  ❌ not a first choice for an individual project

⚠️ Do not quote a per-track price. Figures circulating for this platform come
from marketing material and API resellers rather than a published price list.
[UNVERIFIED]

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. AGGREGATORS AND REGIONAL ACCESS
═══════════════════════════════════════════════════════════════════

<rag_zone id="aggregators">

A practical problem this system's audience actually has: several of these
platforms are hard to reach without a foreign payment card, and some are
region-restricted outright.

─── WHAT AN AGGREGATOR IS ───

A third-party service that holds accounts with the underlying platforms and
resells generation, usually per-generation rather than by subscription, often
with local payment methods.

─── HOW TO PRESENT THEM ───

⚠️ Always as **third-party intermediaries**, never as official access.

  - They are not affiliated with the platforms they resell.
  - Your prompt and output pass through their infrastructure.
  - Commercial rights are murky: the underlying platform's terms attach to
    the account holder, which is the aggregator, not you. If the work is for
    a client, this is a real problem and not a theoretical one.
  - Service can stop without notice when an upstream relationship ends.

  [UNVERIFIED] as a category. None of these has been independently verified
  by this system, and their terms are not published in a form worth citing.

─── CATEGORIES WORTH KNOWING ───

  REGIONAL RESELLERS
    Pay per generation, local payment methods, no foreign card or VPN needed.
    Typically front several platforms at once. Genuinely useful where the
    alternative is no access at all. Present the caveats above every time.

  UNIFIED DEVELOPER APIS
    A single API across several music models, pay-as-you-go, generally no
    free tier. For building something rather than making a track. Same
    caveat about whose account the terms attach to.

─── WHAT NOT TO RECOMMEND ───

  ❌ Repackaged utility apps that added music generation to an unrelated
     product — file converters, ringtone makers, chat apps with a music tab.
     Licensing terms are usually undisclosed and quality is reported as poor.

  ❌ Any site trading under the Riffusion name. Riffusion as an independent
     service ceased to exist in February 2026 (DATA_GOOGLE §7). Sites still
     using the name are selling subscriptions with no verifiable connection
     to the original project. Never emit a web address for one.

  ❌ Any service whose training data provenance is unstated, if the user has
     told you the work is commercial.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. FREE TIER COMPARISON — the `/free` command
═══════════════════════════════════════════════════════════════════

<rag_zone id="free_tiers">

The most-asked question this system receives, and the one previous editions
answered worst. Reached by `/free` per CORE_00 §5.

⚠️ **Read the caveat before the table.** For Suno and Google, this table gives
the shape of the offer and points at the authoritative file for the numbers.
That is deliberate. Allowances change monthly, and a copy here would go stale
against DATA_SUNO and DATA_GOOGLE without anyone noticing.

─── THE TABLE ───

  PLATFORM        FREE OFFER                    COMMERCIAL USE?
  ─────────────── ───────────────────────────── ────────────────────────────
  Suno            daily credit allowance,       ❌ NO — and upgrading later
                  older model only              does not retroactively
                  → figures: DATA_SUNO §11      license what you already made

  Google Lyria    access varies by surface;     ⚠️ not documented clearly
  / Flow Music    no published free allowance   enough to state
                  → DATA_GOOGLE §2

  ElevenMusic     7 tracks per day              ❌ paid tiers only

  Stable Audio    open weights for the smaller  ✅ community licence covers
                  models — run them yourself,   ownership and commercial use
                  no allowance at all           below the revenue threshold

  MiniMax         via aggregators; no direct    ⚠️ depends entirely on the
                  free tier worth citing        aggregator's terms (§4)

─── THE ANSWER MOST PEOPLE ACTUALLY NEED ───

**"Free" and "free to use commercially" are two different questions, and the
platforms differ far more on the second than the first.**

  IF YOU JUST WANT TO MAKE MUSIC AND LISTEN TO IT
    Any free tier is fine. Start with whichever interface you like.

  IF IT WILL EVER BE PUBLISHED, MONETISED, OR HANDED TO A CLIENT
    The free tiers of the major hosted platforms do not grant commercial
    rights, and — this is the part that surprises people — upgrading later
    does not retroactively license tracks you already made on a free plan.
    Anything you might want to use commercially should be made on a paid plan
    from the start.

    The exception is running an open-weights model yourself, where the licence
    covers you from the beginning (§2).

  IF YOU CANNOT PAY THE MAJORS FROM YOUR REGION
    Aggregators solve access and complicate rights (§4). Fine for personal
    work. Read §4 carefully before anything commercial.

─── WHAT NOT TO SAY ───

  ❌ Do not state a credit-to-track conversion from memory. The arithmetic
     has been reported wrong by a factor of two in widely circulated guides.
     Read DATA_SUNO §11.
  ❌ Do not tell anyone a free tier grants commercial rights without checking
     the current terms.
  ❌ Do not present "free forever" marketing language as covering the rights
     to the output. It refers to generation, not to what you may do with the
     result.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. PLATFORM COMPARE — menu [10]
═══════════════════════════════════════════════════════════════════

<rag_zone id="platform_selector">

The decision tree behind menu entry [10] and the `/compare` command.

─── BY WHAT THE TASK NEEDS ───

```
Is the vocal performance the point of the track?
  → Suno. Nothing else in this coverage matches it for character.

Does it need to be commercially clean, with an answer for a client?
  → ElevenMusic — licensed training data, commercial rights on paid tiers
  → or Stable Audio — you own the output outright

Do you need to own it, run it offline, or keep it off someone's servers?
  → Stable Audio. The only open-weights option here.

Does it need to hit specific timings in a video?
  → Lyria 3 Pro with timestamp markers. Built for exactly this.

Will you need to change one part later without losing the rest?
  → Flow Music (Replace) or ElevenMusic (per-section regeneration)

Do you need the longest possible single generation?
  → Stable Audio Large. See §2 for the figure.

Do you need an endless stream you steer while it plays?
  → Lyria RealTime. It is an instrument, not a track generator.

Do you need it to sing in your own voice, or in your catalogue's style?
  → Suno. Features and requirements: DATA_SUNO §5 and §6.

Do you need a 30-second sketch, jingle or loop?
  → Lyria 3 Clip

Do you need volume generation through an API at low unit cost?
  → MiniMax, usually via an aggregator

Do you need a genre change partway through a single track?
  → ElevenMusic (Music v2) or Lyria 3 Pro with timestamps

Can you not reach any of them from where you are?
  → Aggregators, with §4 read first
```

─── THE SHAPE OF THE FIELD ───

Qualitative, deliberately without numbers — the numbers are in the
authoritative files and would go stale here:

  PLATFORM       VOCAL     EDITING AFTER     LICENSING POSTURE
  ────────────── ───────── ───────────────── ──────────────────────────
  Suno           strongest full editing      commercial rights on paid
                           environment       plans; free is non-commercial
  Lyria 3 Pro    good      regenerate        Google terms; not clearly
                                             documented for music
  Flow Music     good      part-by-part      as above
  ElevenMusic    moderate  per section       strongest position of the
                                             hosted platforms
  Stable Audio   minimal   audio-to-audio    you own the output
  MiniMax        weakest   limited           depends on route

─── HOW TO ANSWER A COMPARISON QUESTION ───

  1. Ask what the track is *for* before naming a platform. The right answer
     changes completely between "for me" and "for a client".
  2. Name one platform, not five. Give the runner-up in one line.
  3. Say the trade-off out loud. Every option here loses something.
  4. If rights are involved at all, route to `/legal` — DATA_LEGAL.

─── ONE IDEA ACROSS SEVERAL PLATFORMS ───

Menu [8] DUAL / ALL renders the same idea for multiple targets. The output
formats must never be mixed — each target gets its own labelled block in its
own dialect, per CORE_00 §6.

  The six-layer content survives the trip between platforms. Only the
  packaging changes: bracket markup and numeric tempo for Suno, descriptive
  tempo and timestamps for Lyria, plain narrative for ElevenMusic and Stable
  Audio. Conversion checklists: DATA_GOOGLE §9 and CORE_02 §14.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. PLATFORMS DELIBERATELY NOT COVERED
═══════════════════════════════════════════════════════════════════

<rag_zone id="not_covered">

Recorded so the omissions read as decisions rather than gaps.

─── UDIO ───
  Not a target platform. Generation still works; downloads were disabled
  following its settlement, so output cannot be exported. Covered in this
  system only as a cautionary case — DATA_LEGAL.

─── MUSICFX AND MUSICFX DJ ───
  Retired 31 July 2026. See DATA_GOOGLE §8.

─── RIFFUSION AND PRODUCER.AI ───
  Not separate products. Both are earlier names of Google Flow Music —
  DATA_GOOGLE §7.

─── CONSUMER APPS WITHOUT PUBLISHED SPECIFICATIONS ───
  A number of chat-style and mobile music apps circulate, several of them
  front-ends that switch between the models above. Some are pleasant. None
  publishes specifications, training-data provenance, or licensing terms in a
  form worth citing, and several attach mandatory attribution to free output.
  [UNVERIFIED] Mention as a category if a user asks; do not recommend one by
  name, and never for commercial work.

─── VOICE-CLONING-ONLY TOOLS ───
  Not music generators. Where voice cloning is the requirement, the relevant
  covered feature is Suno's own — DATA_SUNO §5 — which includes a consent
  step. Tools that clone a voice in seconds without one are a legal problem
  wearing a convenience feature (DATA_LEGAL).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. WORKED EXAMPLES
═══════════════════════════════════════════════════════════════════

<rag_zone id="other_examples">

─── ELEVENMUSIC · A COMMERCIAL BED WITH A SECTION PLAN ───

Prose prompt, structure planned for the interface rather than written in
brackets:

```
A sixty-second soundtrack for an outdoor clothing advertisement. Uplifting
indie folk-pop with a cinematic lift. Acoustic guitar fingerpicking, brushed
drums, a string pad arriving late, and a warm female lead singing wordless
"ooh" lines rather than lyrics. Hopeful and unforced. Builds from a single
guitar to a full arrangement, then falls away.
```

  Then, section by section in the interface: a bare opening, drums entering,
  the full arrangement arriving around the two-thirds mark, and a single
  guitar note to finish.

  Why here and not Suno: the client will ask where the music came from, and
  this platform has an answer.

─── ELEVENMUSIC · A GENRE SWITCH ───

```
A track that begins as a slow, serious operatic aria with full orchestra and
a soprano singing in Italian, then breaks without warning into aggressive
modern metal with distorted guitars and a screamed male vocal, then returns
to the opening aria as if nothing happened.
```

  Then use per-section regeneration to fix whichever of the three passages
  comes back weakest, without touching the other two. That is the capability
  worth coming here for (§1).

─── ELEVENMUSIC · STYLE TRANSFER FROM A REFERENCE ───

Supply a short reference of roughly ten to thirty seconds and describe what
to keep:

```
Keep the production character and groove of the reference — the same room
sound, the same laid-back drum feel — but build a new piece in a major key
with a brighter melody.
```

  Keep the melody out of it. Reproducing production is a technique;
  reproducing a tune is a copyright problem (DATA_LEGAL).

─── STABLE AUDIO · A LONG AMBIENT BED ───

Its strongest case — the longest single generation available anywhere here:

```
A six-minute slow ambient piece. Sustained analog pads with very slow
attacks, a low sine drone underneath, and a distant filtered piano figure
that repeats every few bars with slight variation. No percussion, no melody
in the conventional sense, no resolution. Even and unhurried throughout.
Instrumental.
```

  "No resolution" matters. Without it, most models write toward an ending,
  which is wrong for something meant to sit under a scene or loop for hours.

─── STABLE AUDIO · SOUND DESIGN ───

For the effects model — describe the event, not the music:

```
A heavy metal door closing in a large concrete space: the impact, the latch,
and a long reverberant tail decaying over several seconds. No music.
```

─── STABLE AUDIO · AUDIO-TO-AUDIO ───

Transforming existing material rather than generating from nothing:

```
Take the supplied piano recording and reimagine it as a string quartet,
keeping the phrasing and dynamics of the original performance intact.
```

─── MINIMAX · COVER MODE ───

The one thing worth coming here for — melody kept, everything else changed:

```
Keep the melody of the supplied track exactly as it is. Rebuild it as a slow
acoustic ballad with fingerpicked guitar and a single voice, and write new
lyrics on the theme of returning somewhere after a long time away.
```

</rag_zone>

═══════════════════════════════════════════════════════════════════
§9. WHAT TRANSFERS BETWEEN THESE PLATFORMS
═══════════════════════════════════════════════════════════════════

<rag_zone id="portability">

None of the platforms in this file has a documented tag syntax. All of them
take descriptive prose. That makes moving between them easier than moving
either of them to or from Suno.

─── WHAT SURVIVES EVERY MOVE ───

  The six-layer content itself — genre with an era, mood, hero instruments,
  vocal description, structure intent, production character (CORE_01 §1).
  It is the packaging that changes, not the thinking.

─── WHAT HAS TO BE STRIPPED WHEN LEAVING SUNO ───

  bracket markup of every kind · performance notation · slider values ·
  exclude lists · numeric tempo, if the target is Lyria

─── WHAT HAS TO BE ADDED WHEN ARRIVING ───

  ELEVENMUSIC    a section plan to execute in the interface
  STABLE AUDIO   an explicit "instrumental", and no vocal language at all
  MINIMAX        whatever the aggregator's own wrapper expects
  LYRIA          descriptive tempo, timestamps, a `Lyrics:` prefix, and an
                 explicit language — DATA_GOOGLE §9

─── ONE THING THAT NEVER TRANSFERS ───

Expectations about the vocal. The same vocal description produces markedly
different amounts of character on each platform, and that difference is the
main reason to choose one over another (§6). Do not promise a user the voice
they got on one platform on another.

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_OTHER_2026-07.md · SunoForge v3.0
// Snapshot date 2026-07-27 · replace this file, not the CORE files
// Next: DATA_VOCAB.md
// ═══════════════════════════════════════════════════════════════
