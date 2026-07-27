---
file_id: CORE_01_STYLE
version: "3.0"
layer: core
scope: six_layer_style · time_and_place · mood · instrumentation · vocal_direction · personas · hybrids · atmosphere · clone_mode
key_concepts: [six_layer, google_formula, time_and_place, hero_instrument, vocal_arc, persona_biography, duet_protocol, bridge_genre, anti_pairs, scene_painting, acoustic_deconstruction]
depends_on: [CORE_00_ENTRY]
used_by: [CORE_02_LYRICS, CORE_03_DIAGNOSE, CORE_04_WHY, DATA_RECIPES, DATA_VOCAB, DATA_GOOGLE, DATA_SUNO]
rag_priority: critical
updated: "2026-07-27"
changelog: "v3.0 — GMIV+P and the v2.0 6-Layer merged into one framework · Google's official Lyria formula added alongside ours · parametric tags removed from every layer · drift counter-measures moved to CORE_03 · persona bios expanded from Polymath, real-artist names replaced with trait translation · descriptor catalogues moved to DATA_VOCAB"
---

# 🎨 SUNOFORGE v3.0 — STYLE ENGINE
# File 2 of 12 · CORE · How a Style prompt is built

> This file covers menu entries **[2] STUDIO MODE**, **[3] CLONE MODE**,
> **[4] HYBRID LAB** and **[5] PERSONA WORKSHOP**. Numbers per CORE_00 §4.
>
> Nothing here is dated. Version numbers, field limits, slider ranges and plan
> tiers are **not** in this file by design — they live in DATA_SUNO / DATA_GOOGLE
> / DATA_OTHER and are referenced, never copied. See CORE_00 §8.

═══════════════════════════════════════════════════════════════════
§1. THE SIX-LAYER FRAMEWORK
═══════════════════════════════════════════════════════════════════

<rag_zone id="six_layer_definition">

A Style prompt is not a pile of adjectives. It is six decisions, each answering a
different question. Make them one at a time, in order, then join them into one
line. Skipping a layer does not save space — it hands that decision to the model.

  LAYER 1  GENRE          What tradition is this?
  LAYER 2  MOOD           What does it feel like?
  LAYER 3  INSTRUMENTATION What carries the sound?
  LAYER 4  VOCAL          Who is singing, and how?
  LAYER 5  STRUCTURE      How does it unfold?
  LAYER 6  PRODUCTION     What room was it recorded in?

─── LAYER 1 · GENRE — load-bearing, goes first ───

  Format:  [subgenre]  or  [subgenre] meets [subgenre] for a hybrid
  Ceiling: two genres. A third is not a third flavour, it is noise.
  Rule:    a subgenre always beats its parent genre.

  The opening words carry the most weight [COMMUNITY, consistent across
  independent guides and reproduced in controlled comparisons]. Whatever you put
  first is what the model commits to before it has read the rest.

  Method: §3 TIME & PLACE.

─── LAYER 2 · MOOD & ENERGY — one or two compatible words ───

  Two moods maximum, and they must be able to coexist. Contradictory pairs do
  not produce tension, they average out into something flat [COMMUNITY].

    works:        brooding + introspective
    averages out: dark + euphoric

  Method: §4.

─── LAYER 3 · INSTRUMENTATION — two or three hero instruments plus texture ───

  The genre already implies a rhythm section. Naming it spends words on
  something you were getting anyway. Name only what makes this track sound like
  itself, and say how it is played rather than what it is called.

  Method: §5. Full descriptor catalogue: DATA_VOCAB.

─── LAYER 4 · VOCAL — gender, character, delivery, and how it changes ───

  Always state gender explicitly. Without it the result varies between takes
  [COMMUNITY]. On Suno the Advanced Options gender selector is more reliable
  than any wording — see DATA_SUNO §7.

  Method: §6. Biographies: §7.

─── LAYER 5 · STRUCTURE — usually not in the Style field ───

  On Suno, structure is expressed in the Lyrics field, not in Style. The
  exception is when the form *is* the genre: a twelve-bar blues, an AABA jazz
  standard, a call-and-response gospel arrangement. Then name the form.

  On Lyria, structure is expressed as timestamps in the prompt itself. That is
  the single largest difference between the two platforms — §2.

  Method: CORE_02_LYRICS. Timestamps: DATA_GOOGLE.

─── LAYER 6 · PRODUCTION — the closing phrase ───

  Era, mix character, and the space the recording lives in. This is where
  numbers go, as prose: tempo, key, stereo width, compression character.

  Method: §9.

</rag_zone>

─── WHERE PARAMETERS GO ───

Parameters are written as ordinary words inside the Style text:

    ✅  92 BPM, D minor, heavily compressed, wide stereo field
    ❌  [BPM: 92] [Key: D minor] [compression: heavy] [wide stereo field]

Bracketed parameter syntax was never parsed by any covered platform
[UNVERIFIED — no vendor documentation, no controlled test showing an effect].
It circulated for years, it is in the previous editions of this system, and it
does nothing. Square brackets have exactly one documented job: structural
section labels in the Lyrics field (CORE_02), and timestamps on Lyria
(DATA_GOOGLE). Repair table for prompts that still contain them: CORE_03 §7.

═══════════════════════════════════════════════════════════════════
§2. TWO FORMULAS — ours and Google's
═══════════════════════════════════════════════════════════════════

<rag_zone id="formula_comparison">

Google published a prompting guide for the Lyria 3 family in April 2026
[OFFICIAL]. It contains a recommended prompt skeleton. It is worth reading what
it does and does not say, because it is the only vendor-written prompting
document that exists for any platform this system covers.

  GOOGLE'S FORMULA [OFFICIAL]
    Genre and style + Mood + Instrumentation + Tempo and rhythm
    + Vocal style and language + Lyrics

  THIS SYSTEM'S SIX-LAYER
    Genre + Mood + Instrumentation + Vocal + Structure + Production

WHAT AGREES: the first three slots, and vocal. Two independently developed
frameworks converging on genre → mood → instrumentation → vocal is a reasonable
sign that the ordering is not arbitrary.

WHAT DIFFERS, and why:

  Google promotes TEMPO AND RHYTHM to its own slot.
  We fold tempo into Production as prose.

  Google has NO STRUCTURE SLOT — structure moves out of the sentence entirely
  and into timestamp markers.

  Google has NO PRODUCTION SLOT — production language is dissolved into the
  instrumentation and mood descriptions rather than gathered at the end.

─── WHICH ONE TO USE ───

  TARGETING SUNO → six-layer, our order.
    Structure belongs in the Lyrics field. Production works as a closing
    signature phrase. Tempo is written as a number: "92 BPM" [COMMUNITY].

  TARGETING LYRIA → six-layer thinking, Google's order and vocabulary.
    Give tempo its own descriptive phrase and write it in words, not digits —
    "a fast, driving pace with an insistent backbeat" rather than "140 BPM"
    [OFFICIAL, per Google's guide]. Move structure out to `[MM:SS]` markers.
    Let production live inside the instrument descriptions.

  TARGETING ELEVENMUSIC / STABLE AUDIO → six-layer as one flowing description.
    Both take narrative prose. Neither has a documented tag syntax.

⚠️ THE TEMPO TRAP. Suno and Lyria want opposite things here. A user who learns
"always write the BPM as a number" on Suno and carries the habit to Lyria gets
worse results, and vice versa. State the tempo the way the target platform
wants it. This is the single most common cross-platform mistake — it has its own
entry in the repair engine, CORE_03 §7.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. TIME & PLACE — Layer 1 in practice · menu [2a]
═══════════════════════════════════════════════════════════════════

<rag_zone id="time_and_place">

A genre name is a category. An era plus a place plus a scene is a recording —
with a specific room, specific gear, a specific production aesthetic and a
cultural code attached. The second gives the model far more to work with than
the first, and it costs the same number of words [COMMUNITY].

─── THE SUBSTITUTION TABLE ───

  generic            →  time & place
  ─────────────────────────────────────────────────────────
  heavy metal        →  1980s LA Sunset Strip glam metal
  electronic         →  late-90s Bristol trip-hop
  hip hop            →  1994 East Coast boom bap, MPC60 texture
  rock               →  mid-90s Seattle grunge
  jazz               →  1959 New York cool jazz
  pop                →  early-2000s Scandinavian pop
  lo-fi              →  2020s Bandcamp bedroom lo-fi
  folk               →  late-60s Laurel Canyon folk
  punk               →  1977 London punk
  R&B                →  mid-90s Atlanta R&B
  ambient            →  early-90s Warp Records ambient
  country            →  1970s Nashville outlaw country
  reggae             →  1970s Kingston roots reggae
  soul               →  late-60s Memphis soul
  disco              →  late-70s Studio 54 disco
  trap               →  2015 Atlanta trap
  synthwave          →  2018 retrowave, neon city
  phonk              →  2022 drift phonk, slowed and distorted
  house              →  late-80s Chicago acid house
  techno             →  peak-time 2015 Berlin techno
  garage             →  early-2000s UK garage
  funk               →  1970s New Orleans funk

─── CONSTRUCTION ───

  [decade or era] + [city or region] + [scene or subculture] + [core genre]

  You rarely need all four. Two well-chosen ones outperform four vague ones.
  "1977 London punk" is three. "Peak-time Berlin techno" is three without a
  decade and works because "peak-time" carries the function.

─── ONE IDEA, THREE PLACEMENTS ───

The same brief lands in different places depending on what the user actually
wants, which is why this system offers variants rather than one answer
(CORE_00 §3):

  "a sad song"
    → early-2000s Reykjavík post-rock          if it should feel vast
    → late-night Tokyo lo-fi hip-hop           if it should sit in the background
    → mid-90s Manchester Britpop ballad        if it should be sung at someone

  "something energetic to dance to"
    → peak-time 2015 Berlin techno
    → early-2000s Parisian French house
    → late-80s Chicago acid house

  "epic, cinematic"
    → 2010s Hollywood trailer orchestral
    → late-70s Italian giallo score
    → 2020s dark fantasy cinematic

─── WHEN TO SKIP IT ───

Some subgenre names already carry their era, and adding one is redundant:

  synthwave · vaporwave · city pop · boom bap · drift phonk · dungeon synth

For these, the name plus texture descriptors is enough. Adding "1980s
synthwave" spends words restating what "synthwave" already meant.

─── THE FAILURE MODE ───

Time & Place fails when the era and the instrumentation contradict each other.
"1959 New York cool jazz with heavy 808 sub bass" asks the model to hold two
incompatible recordings in mind, and it will pick one. If you want the
collision, that is a hybrid and it needs a bridge — §10.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. MOOD & ENERGY — Layer 2 · menu [2a]
═══════════════════════════════════════════════════════════════════

<rag_zone id="mood_palette">

─── THE PALETTE ───

  uplifting       positive, lifting
  melancholic     sad, contemplative
  haunting        eerie, lingering
  dark            gloomy, ominous
  joyful          happy, celebratory
  nostalgic       wistful, backward-looking
  romantic        tender
  intense         powerful, dramatic
  dreamy          ethereal, floating
  peaceful        calm, unhurried
  anxious         tense, unsettled
  euphoric        blissful, ecstatic
  mysterious      enigmatic
  aggressive      confrontational
  playful         light, teasing
  bittersweet     two feelings at once
  triumphant      victorious
  somber          grave
  intimate        close, personal
  defiant         rebellious
  vulnerable      exposed
  sultry          sensual
  brooding        heavy and inward
  introspective   self-examining
  weary           tired but still going
  reverent        awed, devotional

─── ENERGY, AS PROSE ───

Energy is a real dimension and it belongs in the prompt. It just does not
belong in brackets.

    ✅  low energy, barely moving          ❌  [Energy: Low]
    ✅  steady mid-tempo drive             ❌  [Energy: Medium]
    ✅  full-force, everything at once     ❌  [Energy: High]
    ✅  builds from near-silence to a wall ❌  [Energy: Low→High]

A rising arc is worth describing explicitly, because it is the one energy
statement the model cannot infer from genre alone.

─── WORDS THAT LOOK LIKE MOODS AND ARE NOT ───

  cool · nice · great · beautiful · amazing · wonderful · good · vibey

These carry no musical information — every genre claims all of them. They spend
prompt weight and return nothing [COMMUNITY].

"Epic" is a borderline case: it means something specific for trailer and
cinematic work and almost nothing everywhere else. Outside those genres,
"intense" or "triumphant" says what "epic" was trying to say.

─── SEPARATE FROM MOOD: WORDS THAT DEGRADE AUDIO ───

A different category of dangerous vocabulary exists — words that describe
defects and appear to summon them. That list lives in exactly one place,
CORE_03_DIAGNOSE §4, so it cannot drift out of sync across files. Do not
reproduce it here.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. INSTRUMENTATION — Layer 3 · menu [2b]
═══════════════════════════════════════════════════════════════════

<rag_zone id="instrumentation_method">

─── HERO INSTRUMENTS ───

A hero instrument is the one a listener would name if asked what the track
sounds like. Most arrangements have two, occasionally three. Everything else is
support, and support is implied by the genre.

    ❌  piano, drums, bass, guitar, synth, pads, strings
        Seven equal claims. The model cannot tell which matters, so it
        renders a generic full arrangement [COMMUNITY].

    ✅  overdriven Rhodes, brushed drums, upright bass
        Three, one of them clearly the character.

─── NAME THE PLAYING, NOT THE OBJECT ───

The instrument name is a category with a wide range of possible sounds inside
it. The adjective is what narrows it.

    guitar    → jangly clean Fender tone
    guitar    → heavy downtuned palm-muted riffs
    guitar    → gritty slide in open tuning
    piano     → intimate close-mic grand
    piano     → dusty lo-fi electric piano
    drums     → tight punchy acoustic kit
    drums     → brushed, relaxed shuffle
    bass      → deep upright, walking line

Same word on the left, four different records on the right. The full catalogue —
guitars, keys, drums, bass, strings, brass and winds, with the genre each
descriptor belongs to — is in **DATA_VOCAB**. It is a catalogue, it is long, and
it lives in one file so it can be extended without touching this one.

─── TEXTURE ───

One texture word tells the model how the recording was captured, and it does
more work than a fourth instrument:

  tape-saturated · vinyl crackle · digital and clean · gritty and unprocessed
  analog warmth · plate-verb sheen · close and dry · washed in room

─── THE ARITHMETIC ───

Two or three hero instruments, one playing-style adjective each, one texture
word. That is five to seven words carrying nearly all the sonic identity of the
track — and it leaves room for the other five layers.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. VOCAL DIRECTION — Layer 4 · menu [2c]
═══════════════════════════════════════════════════════════════════

<rag_zone id="vocal_direction">

─── THE FOUR PARTS ───

  1. GENDER      stated explicitly, always
  2. RANGE       soprano, alto, tenor, baritone, bass
  3. CHARACTER   the timbre and the wear on it
  4. DELIVERY    how it is sung, and into what microphone

    female alto, warm and slightly smoky, conversational phrasing, close-mic
    male baritone, gravelly and worn, half-spoken, dry room
    boy soprano, unforced clarity, cathedral reverb behind it

─── GENDER IS NOT OPTIONAL ───

Leave gender out and the result changes between takes [COMMUNITY]. State it in
positive terms. Negative phrasing is unreliable here and sometimes produces the
opposite of what was asked, because naming a concept — even to exclude it —
puts it in front of the model [COMMUNITY, widely reproduced]:

    ✅  solo female vocalist, breathy soprano, intimate delivery
    ❌  no male vocals, female singer preferred

On Suno the interface has a dedicated gender selector, and it is more reliable
than any phrasing in either field. Use it and keep the Style text positive. See
DATA_SUNO §7 for where it sits and §3 for the Exclude Styles field.

  ⚠️ Earlier editions of this system carried an elaborate three-tier workaround
  for vocal gender — positive framing, then stacked negatives, then bracketed
  voice tags. Two of those three tiers were working around a problem the
  interface now solves directly. The whole procedure reduces to: use the
  selector, phrase positively, never stack gender negatives.

─── VOCAL ARC — how the voice changes across the track ───

Google's guide documents something the previous editions of this system never
covered [OFFICIAL]: you can direct the voice to *change* over the length of the
track, not just describe a fixed setting.

    starts guarded and close, opens up through the second half, ends almost shouted
    confident throughout, then drops to nearly a whisper for the final lines
    grows quieter and calmer toward the end

On Lyria this is native — the guide gives it as a supported technique, and it
pairs naturally with timestamp prompting (DATA_GOOGLE).
On Suno the same idea is expressed per-section in the Lyrics field rather than
in Style (CORE_02 §5, delivery notation). Same intent, different field.

This is the long-form relative of per-line emotion delivery. Emotion delivery
shapes a line; the vocal arc shapes the song.

─── WHAT VOCAL DESCRIPTION CANNOT DO ───

It cannot reproduce a specific person. It is directional. Asking for a named
living singer is filtered on Lyria [OFFICIAL] and is a licensing problem
everywhere — see §12 for how to get the *sound* without naming the person, and
DATA_LEGAL for why it matters.

For singing in your own voice, Suno has a dedicated feature with its own
requirements and consent step — DATA_SUNO §5. It is a platform feature, not a
prompting technique, which is why it is documented there and only referenced
here (menu [5e]).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. PERSONA WORKSHOP — menu [5]
═══════════════════════════════════════════════════════════════════

<rag_zone id="persona_method">

─── A PERSON, NOT A SETTING ───

"Sad female vocal" describes a setting on a machine. "A singer who has been
doing this in half-empty rooms for fifteen years and has stopped trying to
impress anyone" describes a person, and a person implies phrasing, restraint,
where they breathe, what they do with the end of a line.

The second consistently produces more stable and more characterful vocals than
the first [COMMUNITY — reported across independent guides, never measured; it
remains probabilistic, and takes will still vary].

─── THE TEMPLATE ───

  [gender + range + timbre]
  [training and history — where this voice learned to sing]
  [performance attitude — who they are singing to, and how hard they are trying]
  [recording signature — microphone distance, room, processing]

Three to seven substantive traits. Past roughly ten, the description stops
sharpening and starts averaging [COMMUNITY].

─── SHORT FORM vs LONG FORM ───

  SHORT, for the Style field where space is shared with five other layers:
    female rich warm alto, church-trained phrasing with deliberate silences,
    close-mic with a little saturation

  LONG, for platforms that take a narrative block, or for a persona you intend
  to reuse across a project:
    the full biography below

Both describe the same singer. The short form is a compression of the long one,
and writing the long one first makes the short one better.

</rag_zone>

<rag_zone id="persona_library">

─── PERSONA LIBRARY — menu [5a] ───

Ten starting points. They are meant to be edited, not pasted unchanged.

**01 · SOUL ALTO**
```
Female vocalist, rich warm alto. Years of church singing and jazz-lounge
nights inform the phrasing — full of grace notes, deliberate silences, and
emotional restraint. The voice carries strength and vulnerability at once.
Sultry without theatrics, confident without arrogance. The performance is
intimate and conversational: not sung to a stadium, sung to one person.
Small imperfections are left in. Trusts the song instead of oversinging.
Close-mic, warm room reverb, a little vocal saturation.
```

**02 · BEDROOM INDIE**
```
Young vocalist recording at home through a warm, slightly nostalgic
microphone. The voice is small and intimate, close to fragile, with a slight
quaver that reads as honesty rather than weakness. No classical training —
sings from feeling. Cracks occasionally, shifts register unexpectedly,
carries a faintly anxious energy: the sound of someone writing their way
through something. Lo-fi treatment, tape saturation, vocal sitting very close
to the listener. Reverb warm but not cavernous. A confession, not a
performance. Every imperfection helps.
```

**03 · WEATHERED BARITONE**
```
Male baritone, gravelly and exhausted, decades of smoky rooms and late nights
audible in the tone. Raw, honest, half-hoarse. Every crack is character
rather than a flaw. Sings behind the beat, in no hurry, as if the song has
been told many times before. Close-mic, dry room, analog warmth, almost no
processing.
```

**04 · POLISHED POP SOPRANO**
```
Female vocalist, bright crystalline upper register, precise diction and
trained breath control. Energetic, confident, youthful. Sharp rhythmic
delivery with clean consonants and tight stacked harmonies on the hooks.
Modern pop production, a light polish on the tuning, wide stereo placement.
```

**05 · LATIN TENOR**
```
Male tenor, smooth and romantic, Latin phrasing with a gentle vibrato and a
sensual, unhurried delivery. Sings the way a warm evening feels. Natural room
reverb, nylon-string guitar and upright bass close behind the voice.
```

**06 · OPERATIC SOPRANO**
```
Classically trained female soprano, powerful projection, full operatic
vibrato. Dramatic phrasing, crystal-clear diction, wide emotional range from
near-whisper to full voice. Concert-hall reverb with orchestral support
underneath.
```

**07 · EXTREME METAL VOCALIST**
```
Male guttural growl, deep and visceral, relentless and aggressive. No melodic
content — pure force and rhythm. Occasional higher shrieked lines for
contrast. Raw recording, heavy distortion, tight untreated room, blast beats
and downtuned guitars behind.
```

**08 · RAP STORYTELLER**
```
Male rapper, conversational flow, delivery sitting deliberately behind the
beat. Street-wise but writerly — the phrasing of someone telling a story to
one listener rather than performing to a crowd. Close-mic, dry vocal, a
subtle slap of delay, dusty sampled production underneath.
```

**09 · WHISPER / ASMR**
```
Female vocal, whispered and breathy, close to spoken, with a gentle melody
underneath rather than on top. Vulnerable, intimate, almost too close to the
microphone. Lo-fi treatment, tape hiss, vinyl warmth, no projection at all.
```

**10 · GOSPEL POWERHOUSE**
```
Female gospel soprano, full chest voice, melismatic runs, church-trained with
an instinct for call-and-response. Spirit and fire, building across the song
rather than starting at full power. Choir answering on the chorus, Hammond
organ, hand claps, room alive with people.
```

─── BUILDING A CUSTOM PERSONA — menu [5b] ───

  1. Decide gender and range first. Everything else hangs off those.
  2. Give the voice a history. Where did it learn? What has it been doing?
  3. Decide who they are singing to. This sets the projection level, and
     projection level is what most "wrong vibe" complaints are actually about.
  4. Decide what is left imperfect. A voice with no flaws reads as synthetic.
  5. Close with the recording signature — mic distance, room, processing.

─── EMOTION DELIVERY — menu [5d] ───

Persona sets who is singing. Emotion delivery sets how a specific passage is
sung, and it is expressed per-section in the Lyrics field, not in Style. Full
notation, including the rule that delivery direction goes on its own line above
the text it governs, is in **CORE_02 §5**.

</rag_zone>

<rag_zone id="duet_pointer">

─── DUET — menu [5c] ───

A duet needs the same cast information in three places: the Style field, the
top of the Lyrics field, and every section. Only the first of those three is a
Style-field matter, so the protocol is documented as one piece where the other
two live — **CORE_02 §9**.

What belongs here is only the Style-field half: state the cast as part of
Layer 4, with gender and range for each voice.

    performed as a duet, a weathered male bass answered by a bright soprano

Two personas can be built from §7 and assigned to the two parts. Keep them
audibly different — two voices in the same range blur together regardless of
how carefully the lyrics are labelled.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. STRUCTURE — Layer 5, and where it actually goes
═══════════════════════════════════════════════════════════════════

<rag_zone id="structure_in_style">

Structure is the one layer that usually does not belong in the Style field.

  ON SUNO      section labels in the Lyrics field       → CORE_02
  ON LYRIA     `[MM:SS]` timestamps in the prompt        → DATA_GOOGLE [OFFICIAL]
  ON FLOW      built section by section in the interface → DATA_GOOGLE
  ON ELEVEN    sections regenerated in the UI            → DATA_OTHER

─── THE EXCEPTION: WHEN FORM IS GENRE ───

Some forms are so tied to a tradition that naming the form names the genre. In
those cases the form belongs in Style, in Layer 1's neighbourhood:

  twelve-bar blues form
  AABA jazz standard form
  call-and-response gospel arrangement
  strophic folk ballad, same melody every verse
  four-on-the-floor with a long build and a single drop

─── WHY THIS SPLIT MATTERS ───

Describing the full arrangement inside Style is the most common way to waste a
prompt. It spends the highest-weight real estate on information the model will
take from the Lyrics field anyway, and it pushes the genre and vocal
descriptions further from the front, where they mattered.

Long-track consistency — what happens to arrangement and character over three
or four minutes, and what to do about it — is a failure-mode question rather
than a construction question. It is handled in **CORE_03 §5**.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§9. PRODUCTION SIGNATURE — Layer 6 · menu [2e]
═══════════════════════════════════════════════════════════════════

<rag_zone id="production_environments">

The closing phrase of a Style prompt answers one question: what does this
recording sound like as an object? Not the notes — the tape, the room, the
console, the year.

─── ENVIRONMENT PRESETS ───

  POLISHED STUDIO MASTER
    clean and balanced, wide stereo, modern commercial polish

  LO-FI DEMO TAPE
    tape saturation, hiss, warm analog degradation, narrow stereo,
    a little wow and flutter

  BEDROOM RECORDING
    close-mic, dry, minimal reverb, small space, honest and unfixed

  LIVE CONCERT
    stage reverb, crowd presence, natural room, instruments bleeding
    into each other's microphones

  FESTIVAL PA
    enormous low end, wide stereo, outdoor decay, punchy transients

  VINTAGE ANALOG STUDIO
    tape warmth, valve compression, round and forgiving, 1970s aesthetic

  1980s LARGE-FORMAT CONSOLE
    bright and punchy, gated snare sheen, wide and clean

  1970s SOUTHERN SOUL ROOM
    tight groove, ribbon-microphone warmth, vintage stereo spread

  CATHEDRAL OR LARGE HALL
    long decay, distant choir, ethereal, everything swimming

  UNDERGROUND CLUB
    heavy bass in a small room, close and sweaty, loud monitors, gritty

  MODERN TRAP POLISH
    pumping sidechain, deep sub, crisp highs, wide top end

─── MIX CHARACTER, IN ONE PHRASE ───

  warm      analog saturation, tape warmth, vinyl crackle
  polished  clean mix, balanced dynamics, bright and commercial
  raw       unprocessed, distorted, gritty, left rough
  spacious  ambient, wide pads, reverb-forward, ethereal
  punchy    tight low end, fast transients, in your face
  cinematic wide field, orchestral dynamics, deep front-to-back
  minimal   sparse, space between everything, nothing added

Spatial vocabulary — stereo placement, depth, reverb types and decay lengths —
is catalogued in **DATA_VOCAB**, not repeated here.

─── TEMPO AND KEY GO HERE ───

On Suno, as numbers, in prose: `92 BPM, D minor`.
On Lyria, as description: `unhurried, with a heavy backbeat`.

Which keys and tempos suit which genres is reference material and lives in
**DATA_VOCAB**.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§10. HYBRID LAB — menu [4]
═══════════════════════════════════════════════════════════════════

<rag_zone id="hybrid_method">

─── STACKING DOES NOT BLEND ───

    ❌  phonk, jazz, lo-fi
        Three genre names with no relationship stated. The model picks the
        one with the strongest signal and drops the others [COMMUNITY].

    ✅  dark phonk 808 weight carrying smoky jazz piano harmony, held
        together by a dusty lo-fi production aesthetic
        The relationship is stated, so there is something to render.

A hybrid needs a sentence, not a list. The sentence has to say which genre
provides the rhythm, which provides the harmony, and what aesthetic makes them
belong on the same record.

─── BRIDGE GENRE THEORY — menu [4b] ───

When two genres do not meet naturally, find the third that already touches
both. The bridge supplies shared vocabulary the model can reason with.

  phonk + jazz            → lo-fi          dusty, sampled, laid-back
  orchestral + EDM        → cinematic      epic, building, dramatic
  metal + classical       → symphonic metal   the bridge already exists
  country + hip-hop       → southern rap   storytelling, regional identity
  reggae + electronic     → dub            bass-forward, spacious, effect-heavy
  afrobeats + house       → amapiano       log drum over house tempo
  hyperpop + folk         → bedroom pop    DIY intimacy plus digital damage
  jazz + drum and bass    → broken beat    swung programming, live harmony
  gospel + electronic     → house          the church origins of house music
  flamenco + metal        → progressive    rhythmic complexity as common ground

[UNVERIFIED as a mechanism — bridge-genre theory has never been tested
quantitatively. It is a craft heuristic with good demonstrations behind it.
It is offered because it reliably produces a better *prompt*, whatever the
model does with it.]

─── HYBRIDS WORTH KNOWING ───

  AMAPIANO FUSION
    log drum sub, Afrobeat percussion, airy synths, around 110–115 BPM,
    dancefloor patience — long builds, late payoffs

  LO-FI TRAP
    vinyl crackle over atmospheric trap, 808 sub, half-time feel, jazz
    sample harmony, mid-80s BPM

  DRIFT PHONK
    slowed Memphis cowbell pattern, distorted 808 hits, ambient pad
    underneath, deliberately murky
    distinct from Memphis phonk (faster) and Brazilian phonk (percussive)

  HYPERPOP FOLK
    fingerpicked acoustic guitar under glitched and stacked vocals,
    fragile writing delivered through digital damage

  CINEMATIC CHOIR ELECTRONICA
    non-lexical choir syllables, taiko and brass swells, synthetic low end,
    wide cinematic field

  SPOKEN WORD AMBIENT
    low conversational voice over sustained pads, a single repeating piano
    note, rain in the distance

─── PAIRS THAT BLEND FREELY — menu [4a] ───

  rap + trap · lo-fi + chill · metal + rock · orchestral + cinematic
  soul + R&B · synthwave + synthpop · house + deep house
  folk + acoustic · jazz + funk · blues + rock · pop + indie
  ambient + electronic · gospel + soul · bossa nova + jazz

─── PAIRS THAT FIGHT — menu [4c] ───

  ❌ country + death metal      subcultural codes with nothing in common
  ❌ gospel + industrial        opposed emotional cores
  ❌ classical + trap           opposed ideas of what production is for
  ❌ ambient + hardcore         opposed ideas of what energy is for
  ❌ opera + minimal techno     opposed ideas of what a voice is for
  ❌ drum and bass + slow funk  the tempo cannot be reconciled

These are not forbidden. They are expensive: expect more takes, and expect the
result to sound like one genre with the other as decoration rather than a true
blend.

IF A USER ASKS FOR ONE ANYWAY:
  1. Say in one line that the pair fights and why.
  2. Offer the bridge genre as an alternative.
  3. If they still want it — raise the experimental slider, lower the
     literalness slider (values by goal: DATA_SUNO §7), and split the genres
     across sections rather than layering them.

─── DISTRIBUTING A HYBRID ACROSS A SONG ───

Genres blend better in sequence than in a stack:

  intro    genre A alone, establishing the frame
  verse    genre B takes the rhythm, genre A keeps the harmony
  chorus   both at once — this is the only place they truly merge
  bridge   strip to one genre for contrast
  outro    resolve into whichever genre the song is really about

Section-level instructions are written in the Lyrics field — CORE_02.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§11. ATMOSPHERE AND SCENE
═══════════════════════════════════════════════════════════════════

<rag_zone id="atmosphere">

─── PAINT A SCENE, NOT A SPEC SHEET ───

  TECHNICAL   melancholic, acoustic guitar, female vocal, reverb
  SCENE       someone playing guitar alone on a wet rooftop at three in the
              morning, city lights smeared through the water

Both descriptions request the same track. The second gives the model a
situation, and situations imply tempo, dynamics, register and space all at once
[COMMUNITY — reported consistently; Lyria's own guide leans on scenario
prompting, which is the closest thing to vendor endorsement this technique has].

─── ERA AND VISUAL AESTHETIC ───

  neon city at night, synthwave
  sepia Laurel Canyon sunset, 1970s folk
  cyberpunk rain, reflected signage
  torchlit stone halls, medieval fantasy
  1940s detective noir, smoke and venetian blinds
  abandoned industrial decay, post-Soviet winter

─── AMBIENT SOUND ───

Environmental sound is requested in prose, inside the Style description:

    ✅  with rain and distant thunder under the intro
    ✅  a room with people in it — glasses, low conversation
    ❌  the same requests written as bracketed sound parameters

The bracketed form is a parametric tag. It was never a documented control
[UNVERIFIED] and belongs to the same family as the mix parameters in §1. If a
user brings a prompt containing them, the repair is mechanical — CORE_03 §7.

Section-level atmosphere — a crowd on the intro, applause on the outro — is a
Lyrics-field matter and is covered in CORE_02 §6.

─── IMAGE TO SOUND ───

For platforms that accept image input (Lyria takes text, PDF and multiple
reference images [OFFICIAL] — see DATA_GOOGLE), the translation is not
automatic. Give the model the audio consequence of what is in the picture:

  dark, night              → minor key, low tempo, sparse, air and reverb
  bright daylight          → major key, up-tempo, dry, present
  forest, water, stone     → acoustic instruments, natural room, organic
  neon, glass, traffic     → synthetic, sequenced, urban, modern polish
  open water, horizon      → slow, wide, unhurried, long decays
  a crowd of people        → up-tempo, rhythmic, live-sounding
  faded photograph         → vintage instruments, tape warmth, nostalgic
  rain and fog             → melancholic, reverb-forward, intimate

</rag_zone>

═══════════════════════════════════════════════════════════════════
§12. CLONE MODE — menu [3]
═══════════════════════════════════════════════════════════════════

<rag_zone id="clone_mode">

Cloning here means reproducing a *sound* — production, texture, groove, space.
Never a melody, never a specific person's voice. That boundary is not
squeamishness; it is the line between a usable track and an unusable one
(DATA_LEGAL).

─── [3a] FROM AN AUDIO FILE — acoustic deconstruction ───

Listen along four axes and write down what you hear as descriptors:

  TIMBRE     bright or dark, warm or metallic, thin or full
             → is the energy high in the spectrum or low?
  DYNAMICS   percussive or sustained, tight or breathing
             → how fast do notes start, how long do they hang?
  GROOVE     ahead of the beat, on it, or behind it; straight or swung
             → this is what makes a genre feel like itself
  SPACE      wide or narrow, close or distant, dry or drenched
             → how big is the room and where is the listener standing?

The technical vocabulary for each axis — spectral character, ADSR, pocket,
reverb types — is catalogued in **DATA_VOCAB**. Translate what you heard into
those words, then assemble them through the six layers.

Output the vibe and the production. Do not transcribe the tune.

─── [3b] FROM AN ARTIST — without naming the artist ───

Naming a living artist is filtered on Lyria [OFFICIAL], unreliable on Suno, and
a licensing exposure everywhere. It is also lazier than it looks: the name is a
compressed pointer to traits, and the traits are what the model needs.

Translate the name into its parts:

  era and scene the artist belongs to
  the two or three instruments that define their records
  the vocal range, texture and phrasing habits
  the production signature — how their records are mixed
  what they do that nobody else does

Assemble those into a normal six-layer prompt. The result is legally clean,
works on every platform, and is usually *better*, because it says what you
actually wanted rather than gesturing at a catalogue.

  ❌  in the style of [named living artist]
  ✅  late-2000s indie folk, weary male tenor sitting just behind the beat,
      fingerpicked acoustic guitar and a single brushed snare, close-mic in a
      dry wooden room, arrangements that stay almost empty until the last chorus

─── [3c] FROM A DESCRIPTION — "like that track, but…" ───

The user has a reference in their head. Extract it with the fewest questions:

  1. What is the one thing you want to keep?
  2. What is the one thing you want different?
  3. Same singer type, or a different one?

Then build normally, holding the kept element in Layer 1 or Layer 3 and putting
the changed element wherever it belongs. Change one thing per generation
(CORE_00 §7 rule 9) — otherwise the next take teaches you nothing.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§13. ASSEMBLY
═══════════════════════════════════════════════════════════════════

<rag_zone id="assembly">

─── ORDER OF OPERATIONS ───

  1  Genre via Time & Place              §3
  2  Mood, one or two words              §4
  3  Two or three hero instruments       §5
  4  Vocal: gender, range, character     §6
  5  Structure → the Lyrics field        §8 → CORE_02
  6  Production signature + tempo + key  §9

Then read it back in one breath. If it does not describe a record you could
imagine hearing, a layer is missing or a layer is fighting another one.

─── WORKED EXAMPLE · SUNO ───

  BRIEF: "something about leaving home, but not sad exactly"

  L1  late-60s Laurel Canyon folk
  L2  bittersweet, unhurried
  L3  fingerpicked nylon-string guitar, brushed drums, distant pedal steel
  L4  female alto, unpolished, close and conversational
  L5  → verses and a repeated chorus, no bridge (goes in Lyrics)
  L6  warm analog tape, dry and close, 78 BPM, G major

  ASSEMBLED:
```
late-60s Laurel Canyon folk, bittersweet and unhurried, fingerpicked
nylon-string guitar with brushed drums and distant pedal steel, female alto,
unpolished and conversational, close-mic, warm analog tape, dry room,
78 BPM, G major
```

─── THE SAME BRIEF · LYRIA ───

Google's order, tempo in words, no production block, structure lifted out:

```
Late-1960s Californian canyon folk with a bittersweet, unhurried feeling.
Fingerpicked nylon-string guitar, brushed drums and a distant pedal steel.
A relaxed, walking pace that never pushes. A female alto voice, unpolished
and conversational, recorded very close.
```

Structure for this track would then be given separately as timestamps
(DATA_GOOGLE) rather than described in the sentence.

─── LENGTH DISCIPLINE ───

Front-loading matters more than word count [COMMUNITY — the one point every
independent source agrees on]. Order first, length second.

Field limits, the practical range where description still steers the result,
and the disagreement between sources about whether the current Suno model
prefers long or short prompts are all documented in **DATA_SUNO §2**. They are
version-specific facts and they are deliberately not repeated here — this file
is meant to outlive them.

What is not version-specific: past roughly ten descriptors, they start
contradicting each other. Adding a word that does not change the sound in your
head does not change the sound coming out.

─── VARIANTS, NOT ANSWERS ───

Deliver two or three readings of the brief, not one (CORE_00 §3). The layers
make this cheap: hold Layers 2, 4 and 5 steady and change Layer 1, and you have
a genuinely different record built from the same emotional intent.

  A  late-60s Laurel Canyon folk       the straightforward reading
  B  early-90s slowcore                the same feeling, more space, more weight
  C  1970s Nashville outlaw country    the same story, told by someone harder

</rag_zone>

═══════════════════════════════════════════════════════════════════
§14. CHECKLIST
═══════════════════════════════════════════════════════════════════

<rag_zone id="style_checklist">

Before a Style prompt goes out:

  ☐ Genre is a subgenre with an era or a scene attached, and it is first
  ☐ Two genres at most
  ☐ One or two moods, and they can coexist
  ☐ Two or three hero instruments, each with a playing-style word
  ☐ One texture word
  ☐ Vocal gender stated positively; range and character present
  ☐ No gender negatives anywhere
  ☐ Structure is in the Lyrics field, not here — unless the form is the genre
  ☐ Production signature closes the prompt
  ☐ Tempo written the way the target platform wants it (§2)
  ☐ Zero bracketed parameters — every number and setting is prose
  ☐ No named living artists
  ☐ Nothing restating a fact that belongs in a DATA_* file
  ☐ Read aloud in one breath, it describes a record

If a prompt fails any of these and it came from a user rather than from this
system, that is an audit — menu [12], engine in CORE_03.

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF CORE_01_STYLE.md · SunoForge v3.0
// Next: CORE_02_LYRICS.md
// ═══════════════════════════════════════════════════════════════
