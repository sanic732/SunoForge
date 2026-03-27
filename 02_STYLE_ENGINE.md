# 🎨 SUNOFORGE v1.1 — STYLE ENGINE
# File 02 of 10 · Genres · Personas · Hybrids · Atmosphere

═══════════════════════════════════════════════════════════════════
§1. THE STYLE FORMULA: GMIV+P
═══════════════════════════════════════════════════════════════════

<gmivp_formula>
// Core formula for constructing a Style prompt.
// Works for Suno (Style box) and Gemini (narrative prompt).

FORMULA:
  [G] Genre    → Genre + sub-genre (via Time & Place)
  [M] Mood     → Mood + energy
  [I] Instrum. → Key instruments with descriptors
  [V] Vocals   → Vocal persona or characteristic
  [+P] Prod.   → Production: mix, space, texture, effects

─── LIMITS (critical) ───
  Genres:      MAX 2 (main genre first)
  Instruments: MAX 3–4 (with descriptors of playing style)
  Mood words:  MAX 1–2
  Total length: up to 1000 characters (priority drops after ~200)

─── WORD ORDER (critical) ───
  FIRST 20–30 WORDS = maximum weight for the model.
  Place at the start: genre → mood → key instrument → vocals.
  Production and details — at the end.

─── PROMPT LENGTH (version-aware · NEW v1.1) ───
  v4.5-all: First 20–30 words are critical. Rest is supplementary. Limit 1000 chars.
  v5/v5.5:  100–200 FOCUSED words work BETTER than short ones!
            Old short prompts (2–3 words) → clipped/strange results.
            Style box = technical brief for a sound engineer.
            Describe sound characteristics: density, panning, dynamics.
  Gemini:   2–4 sentences for Clip. Extended block for Pro.

  GOOD (v5.5): "Dark atmospheric folk-rock with cinematic blues influence,
  85 BPM, A minor. Weathered baritone male vocals with gravelly exhausted
  delivery, close-mic recording with analog tape saturation. Acoustic guitar
  resonance paired with haunting violin melody and distorted electric bass.
  Cold rainy atmosphere, heavy compression maintaining dynamics, wide stereo
  field with mid-clear EQ profile. Production reminiscent of late-2000s
  post-rock with Slavic folk undertones, intimate yet powerful."

  BAD (v5.5):  "dark rock, sad, guitar" → generic, clipped result

─── CONSTRUCTION PIPELINE ───

STEP 1 — GENRE (Time & Place):
  Input: "rock" or "sad music"
  Output: "mid-90s Seattle grunge" or "late-night Tokyo lo-fi hip-hop"
  Method: → §2 TIME & PLACE RULE

STEP 2 — MOOD (1–2 words):
  Choose from the mood palette (see below).
  One primary + one nuance at most.
  GOOD: "melancholic, intimate"
  BAD:  "sad, melancholic, depressing, lonely, dark, hopeless" (6 = overload)

STEP 3 — INSTRUMENTS (3–4 with descriptors):
  NOT just "guitar" → "jangly clean Fender tone"
  NOT just "drums" → "brushed jazz drums, laid-back shuffle"
  NOT just "synth" → "warm analog Moog bass"
  Method: → §3 INSTRUMENT DESCRIPTORS

STEP 4 — VOCALS (Persona or characteristic):
  Minimum: "female vocal, soft delivery"
  Optimal: micro-biography (2–3 lines)
  Method: → §5 PERSONA WORKSHOP

STEP 5 — PRODUCTION (+P):
  Closing block of the Style prompt.
  Includes: mix character, space, texture, effects.
  Method: → §4 PRODUCTION ENVIRONMENTS
</gmivp_formula>

═══════════════════════════════════════════════════════════════════
§2. TIME & PLACE RULE
═══════════════════════════════════════════════════════════════════

<time_and_place>
// Instead of generic genres, use a specific era + location + subculture.
// This gives the model context: "room tone", production aesthetic, cultural code.

─── PRINCIPLE ───

BAD (generic):           GOOD (Time & Place):
"Heavy Metal"         →  "1980s LA Sunset Strip metal"
"Electronic music"    →  "late-90s Bristol trip-hop"
"Hip hop"            →  "2012 London grime"
"Rock"               →  "mid-90s Seattle grunge"
"Jazz"               →  "1959 New York cool jazz"
"Pop"                →  "early-2000s Scandinavian pop"
"Lo-fi"              →  "2020s bedroom lo-fi from Bandcamp"
"Folk"               →  "late-60s Laurel Canyon folk"
"Punk"               →  "1977 London punk"
"R&B"                →  "mid-90s Atlanta R&B"
"Ambient"            →  "early-90s Warp Records ambient"
"Country"            →  "1970s Nashville outlaw country"
"Reggae"             →  "1970s Kingston roots reggae"
"Soul"               →  "late-60s Memphis soul"
"Disco"              →  "late-70s Studio 54 disco"
"Trap"               →  "2015 Atlanta trap"
"Synthwave"          →  "2018 retrowave, 80s-inspired neon city"

─── HOW TO CONSTRUCT ───

FORMULA: [Decade/Era] + [City/Region] + [Subculture/Scene] + [Core Genre]

EXAMPLES:
  "sad song"
    → "early-2000s Reykjavik post-rock" (if atmospheric)
    → "late-night Tokyo lo-fi hip-hop" (if background)
    → "mid-90s Manchester Britpop ballad" (if rock ballad)

  "energetic dance"
    → "peak-time 2015 Berlin techno"
    → "early-2000s Parisian French house"
    → "late-80s Chicago acid house"

  "epic cinematic"
    → "2010s Hollywood trailer epic orchestral"
    → "late-70s Italian giallo score"
    → "2020s dark fantasy cinematic"

─── WHEN TIME & PLACE IS NOT NEEDED ───

For some sub-genres, Time & Place is already built into the name:
  "Synthwave" = 80s-inspired (era is embedded)
  "Vaporwave" = 80s-90s nostalgia (embedded)
  "City Pop" = 80s Japan (embedded)
  "Boom Bap" = 90s NYC hip-hop (embedded)

In these cases, the name + clarifying descriptors is sufficient.
</time_and_place>

═══════════════════════════════════════════════════════════════════
§3. INSTRUMENT DESCRIPTORS
═══════════════════════════════════════════════════════════════════

<instrument_descriptors>
// NOT just the instrument name — but HOW it sounds.
// "Hidden GPT" technique: extract 3 adjectives for the target sound.

─── GUITARS ───
Generic: "guitar"
Specific:
  "jangly clean Fender tone"          (indie, 60s rock)
  "overdriven Marshall crunch"         (hard rock)
  "warm nylon-string fingerpicking"    (folk, bossa nova)
  "heavy downtuned palm-muted riffs"   (metal)
  "shimmering clean arpeggios"         (post-rock, shoegaze)
  "gritty slide guitar, open tuning"   (blues, delta blues)
  "twangy Telecaster with spring reverb" (country)
  "fuzzy psychedelic wah-wah"          (psych rock)

─── KEYBOARDS & SYNTHS ───
Generic: "piano", "synth"
Specific:
  "intimate close-mic grand piano"      (ballad, classical)
  "warm Rhodes with tremolo"            (neo-soul, jazz)
  "bright Wurlitzer"                    (60s-70s pop)
  "lush analog Moog bass"              (synthwave, electronic)
  "crystalline FM synth bells"          (80s pop, city pop)
  "supersaw trance leads"              (EDM, trance)
  "dusty lo-fi electric piano"         (lo-fi hip-hop)
  "haunting Mellotron strings"         (prog rock, cinematic)
  "spooky Hammond organ with Leslie"   (rock, gospel)

─── DRUMS & RHYTHM ───
Generic: "drums"
Specific:
  "tight punchy acoustic kit"           (pop, rock)
  "brushed jazz drums, relaxed shuffle" (jazz, lounge)
  "deep 808 kicks, crisp hi-hats"      (trap, hip-hop)
  "TR-909 four-on-the-floor"           (house, techno)
  "breakbeat chopped drum loops"        (DnB, jungle)
  "cinematic taiko percussion"          (epic, trailer)
  "lo-fi boom-bap, dusty samples"      (lo-fi hip-hop)
  "blast beats, double bass pedals"     (metal, extreme)
  "minimal electronic clicks"           (minimal, IDM)

─── BASS ───
Generic: "bass"
Specific:
  "round warm sub-bass"                 (lo-fi, chill)
  "aggressive 808 sub with distortion"  (trap, phonk)
  "funky slap bass, tight pocket"       (funk, disco)
  "deep upright bass, jazz walking line" (jazz, swing)
  "sidechained synth bass, pumping"     (house, EDM)
  "gritty distorted bass guitar"        (metal, grunge)

─── STRINGS & ORCHESTRAL ───
Generic: "strings", "orchestra"
Specific:
  "sweeping cinematic string swells"    (trailer, epic)
  "intimate string quartet, close-mic"  (indie, chamber)
  "haunting solo violin, vibrato"       (folk, cinematic)
  "dark cello drone"                    (ambient, horror)
  "full orchestral tutti with brass"    (symphonic)

─── BRASS & WIND ───
Generic: "saxophone", "trumpet"
Specific:
  "smoky tenor sax, jazz club tone"     (jazz, noir)
  "bright mariachi trumpet"             (Latin, Mexican)
  "muted jazz trumpet, Miles Davis vibe" (cool jazz)
  "aggressive brass stabs"              (funk, soul, EDM)
  "mournful harmonica, blues phrasing"  (blues, folk)
  "Celtic tin whistle"                  (Celtic, folk)
</instrument_descriptors>

═══════════════════════════════════════════════════════════════════
§4. PRODUCTION ENVIRONMENTS
═══════════════════════════════════════════════════════════════════

<production_environments>
// Closing block of the Style prompt. Defines the "room" and "mix".

─── PRODUCTION PRESETS ───

"Polished studio master"
  → clean, balanced, wide stereo field, professional mix, modern pop polish

"Lo-fi demo tape"
  → tape saturation, vinyl hiss, warm analog degradation, narrow stereo,
    slight wow and flutter, bedroom recording quality

"Intimate bedroom recording"
  → close-mic, dry room, minimal reverb, raw, honest, small space

"Live concert recording"
  → stage reverb, crowd ambience, natural room sound, live energy,
    slight bleed between instruments

"Festival PA system"
  → massive low end, wide stereo, crowd energy, outdoor reverb,
    punchy transients

"Vintage analog studio"
  → analog saturation, tape warmth, valve compression, 70s recording
    aesthetic, warm and round

"Cathedral / large hall"
  → massive reverb, distant choir, soaring acoustics, ethereal space

"Dark underground club"
  → heavy bass in small room, close and sweaty, minimal reverb,
    loud monitors, gritty

─── MIX CHARACTER TAGS ───
(to append at the end of the Style prompt)

Lo-fi / Warm:      analog saturation, tape warmth, vinyl crackle, lo-fi texture
Clean / Polished:  modern pop polish, clean mix, balanced dynamics, bright
Raw / Gritty:      raw recording, distorted, gritty, unprocessed
Atmospheric:       spacious, ambient, wide stereo pads, ethereal, reverb-heavy
Punchy:            tight low end, punchy transients, in-your-face, compressed
Cinematic:         wide stereo field, cinematic depth, orchestral dynamics
Minimal:           sparse, space between notes, negative space, less is more

─── SPATIAL DESCRIPTORS ───
(from 04_AUDIO_VOCAB, brief version here for quick access)

Wide stereo field    — full stereo space
Mono center          — everything centered, intimate
Close-mic            — close to microphone, detailed
Distant / Recessed   — far away, in reverb
Dry mix              — minimal reverb
Wet / Drenched       — heavy reverb
</production_environments>

═══════════════════════════════════════════════════════════════════
§5. PERSONA WORKSHOP (Voice Architecture)
═══════════════════════════════════════════════════════════════════

<persona_workshop>
// Instead of "sad female vocal" — create a micro-biography.
// Bio-Hack: contextual description creates "character DNA" for the model.
// Optimal: 3–7 adjectives + context + scene.
// Overload: >10 adjectives = model ignores some.

─── PERSONA TEMPLATE ───

[CHARACTER/VOICE]:
  Detailed description: age, timbre, technique, emotion, influences.
[MUSICAL CONTEXT]:
  Genre, scene, time, place.
[SOUND DETAILS]:
  Effects, microphone, space, recording approach.

─── READY-MADE PERSONA LIBRARY ───

PERSONA 01 — Soulful R&B Alto:
```
Seasoned soul singer with rich warm alto voice.
Years of church and jazz lounge experience, full of grace notes
and intentional silence. Sultry without being theatrical.
Intimate performance, not for stadium — for you alone.
Close-mic, warm room reverb, slight vocal saturation.
```

PERSONA 02 — Indie Bedroom Girl:
```
Young indie artist recording from bedroom studio with warm
nostalgic microphone. Voice is small, intimate, almost fragile
with slight quaver. Not trained — sings from feeling.
Lo-fi aesthetic, tape saturation, vocal sits close to listener.
Reverb warm but not cavernous. Bedroom confession, not performance.
```

PERSONA 03 — Gravelly Blues Baritone:
```
Weathered baritone male vocals, gravelly exhausted delivery.
Decades of smoky bars and late nights in the voice.
Raw, honest, slightly hoarse. Every crack adds character.
Close-mic, dry room, analog warmth, minimal processing.
```

PERSONA 04 — K-pop High Energy:
```
Bright female vocal, crystalline high register, precise diction.
Trained pop vocalist with K-pop phrasing and breath control.
Energetic, confident, youthful. Sharp rhythmic delivery.
Modern pop production, slight auto-tune polish, wide stereo.
```

PERSONA 05 — Latin Jazz Tenor:
```
Smooth male tenor with Latin phrasing, romantic delivery.
Bossa nova influenced, gentle vibrato, sensual tone.
Sings like a warm evening in Havana.
Natural room reverb, upright bass and nylon guitar behind.
```

PERSONA 06 — Opera Soprano:
```
Classically trained soprano, powerful projection, operatic vibrato.
Dramatic phrasing, crystal clear diction, emotional range.
Concert hall reverb, full orchestral support.
```

PERSONA 07 — Death Metal Growler:
```
Guttural death growl, deep and visceral. Aggressive, relentless.
Blast beats behind, downtuned guitars. No melody, pure power.
Raw recording, heavy distortion, tight room.
```

PERSONA 08 — Rap Storyteller:
```
Male rapper with conversational flow, storytelling delivery.
Laid-back pocket, behind-the-beat timing. Street-wise but poetic.
Close-mic, dry vocal, subtle delay, boom-bap production.
```

PERSONA 09 — Lo-fi Whisper Girl:
```
Whispering female vocal, ASMR-adjacent, breathy and ethereal.
Almost spoken, gentle melody underneath. Vulnerable and intimate.
Lo-fi processing, tape hiss, vinyl warmth, very close-mic.
```

PERSONA 10 — Gospel Powerhouse:
```
Powerful gospel soprano with full chest voice and melismatic runs.
Church-trained, call-and-response instinct. Spirit and fire.
Gospel choir backing on chorus, Hammond organ, clapping.
```

─── POSITIVE FRAMING RULE ───

NEVER: "No male vocals", "without male voice"
  → v4.5 IGNORES gender exclusions due to hardcoded ranges.
  → Mentioning "male" even negatively STRENGTHENS the association.

ALWAYS: Positive statement in the first words of Style:
  GOOD: "Solo female vocalist, breathy soprano, intimate delivery"
  GOOD: "Female-led, warm alto, close-mic, no duet"
  BAD:  "No male vocals, female singer preferred"

─── VOICES (v5.5 Pro · NEW v1.1) ───
Upload your own voice: 30s–4min → verification → generate with "your" voice.
  - 4 credits/track (beta) → draft with regular voices, final with Voices
  - Voice is tied to account, not shared
  - Recording even with musical background — OK

─── CUSTOM MODELS (v5.5 Pro · NEW v1.1) ───
Train Suno on 6+ own tracks → personalized model.
  - Up to 3 models simultaneously (for different projects)
  - Prompt can be minimal — model "knows" the style
  - ⚠️ Only tracks you own the rights to! Others' material = ToS violation

─── MY TASTE (free · NEW v1.1) ───
Magic Wand in Styles field → auto-style to match your taste.
  - Analyzes your generations + listening history → adjusts
  - Starting point for Quick Start → refine manually

─── DUET PROTOCOL (Three-Anchor Stability) ───

ANCHOR 1 — Style Prompt:
  "This is a duet between John (male) and Jane (female), [genre], [tags]"

ANCHOR 2 — Lyrics Header (first lines of Lyrics):
  [Duet: John male and Jane female]

ANCHOR 3 — Per-Section Labels:
  [Verse 1]
  [John]
  text...

  [Chorus]
  [Both]
  text...

  [Verse 2]
  [Jane]
  text...

STABILITY RULE:
  Assign entire verses to one singer. Do NOT alternate line by line.
  Switching mid-verse breaks voice consistency.
</persona_workshop>

═══════════════════════════════════════════════════════════════════
§6. HYBRID GENRE LAB
═══════════════════════════════════════════════════════════════════

<hybrid_lab>
// Genre blending — not "Genre1, Genre2", but a meaningful connection.
// Key: bridge genre + narrative description + preserving the core of each genre.

─── PRINCIPLE: NARRATIVE BLENDING ───

BAD (stacking):  "Phonk, Jazz, Lo-fi"
  → Suno picks one and ignores the rest.

GOOD (narrative): "A fusion of dark phonk 808 energy with smoky jazz piano
                   harmonics, connected through a lo-fi production aesthetic"
  → Suno understands HOW the genres are connected.

─── BRIDGE GENRE THEORY ───

If two genres are not directly compatible — find a bridge:

  Phonk + Jazz      → bridge: Lo-fi (shared aesthetic: dusty, sampled, laid-back)
  Orchestral + EDM  → bridge: Cinematic (shared aesthetic: epic, building, dramatic)
  Metal + Classical  → bridge: Symphonic Metal (the bridge genre already exists)
  Country + Hip-Hop → bridge: Southern Rap (shared aesthetic: storytelling, southern)
  Reggae + Electronic → bridge: Dub (shared aesthetic: bass-heavy, spacious, effects)

─── HIGH-VALUE FUSION PAIRS ───

STRONG PAIRS (⭐⭐⭐⭐⭐ — blend freely):
  Rap + Trap           — Natural pair, dominant co-existence
  Lo-fi + Chill        — Dominant lo-fi combination
  Metal + Rock         — Core of the metal spectrum
  Orchestral + Epic    — Cinematic sweet spot
  Emo + Emotional      — Maximum emo combination
  Soul + R&B           — Natural soul pairing
  Synthwave + Synth    — Synthwave core
  House + Deep         — Deep house standard

GOOD PAIRS (⭐⭐⭐⭐):
  Folk + Acoustic      — Folk anchor
  Jazz + Funk          — Natural jazz pairing
  Blues + Rock         — Classic blues-rock
  Pop + Indie          — Indie pop sweet spot
  Ambient + Electronic — Atmospheric electronic

─── ANTI-PAIRS (DO NOT BLEND) ───

  ❌ Cinematic + Dark     (weight: 10 — near zero compatibility)
  ❌ Opera + Melodic      (weight: 16 — interpretation conflict)
  ❌ Drum and Bass + Funk (weight: 7 — extremely low compatibility)
  ❌ Country + Death Metal (subculture code conflict)
  ❌ Gospel + Industrial   (emotional core conflict)

IF user requests Anti-Pair:
  → Warn: "These genres conflict. The result may be unpredictable."
  → Suggest a bridge genre as an alternative.
  → If user insists — generate with high Weirdness (65%+).

─── HYBRID CONSTRUCTION TEMPLATE ───

STEP 1: Identify the core of each genre (what makes it recognizable):
  Jazz: harmonies, swing, improvisation
  Trap: 808, hi-hats, dark mood, aggressive

STEP 2: Find a shared element or bridge:
  Jazz + Trap → shared: urban, nocturnal, groove-driven
  Bridge: "midnight", "urban noir", "smoky club"

STEP 3: Narrative Blend:
  "Late-night urban jazz-trap fusion. Smoky upright bass meets deep 808 sub.
   Sparse hi-hats with jazz shuffle feel. Introspective male vocal,
   conversational delivery. Dark, intimate, nocturnal city atmosphere."

STEP 4: Distribute genre elements across song structure:
  [Intro] — Jazz elements (piano, brush drums)
  [Verse] — Trap takes over (808, hi-hats) but jazz harmonies stay
  [Chorus] — Full fusion (both worlds)
  [Bridge] — Strip to one genre (contrast)
</hybrid_lab>

═══════════════════════════════════════════════════════════════════
§7. ATMOSPHERE BUILDER
═══════════════════════════════════════════════════════════════════

<atmosphere_builder>
// Creating atmosphere: not just genre + instruments, but a SCENE.
// Works for both platforms: Suno (Style + Sound tags) and Gemini (narrative).

─── SCENE PAINTING ───

Instead of technical description — paint a scene:

TECHNICAL: "melancholic, acoustic guitar, female vocal, reverb"
SCENE:     "A lonely girl playing acoustic guitar on a rainy rooftop
            at 3am, the city lights blurred through wet glass"

Suno responds better to contextual descriptions than lists of adjectives.
Gemini Lyria 3 is OPTIMIZED for scenario-based prompts.

─── ERA & AESTHETIC ───

Specify era + visual aesthetic:
  "80s synthwave, neon city atmosphere"
  "70s sepia-toned folk, Laurel Canyon sunset"
  "futuristic cyberpunk, dark rain, neon reflections"
  "medieval fantasy, torchlit stone halls"
  "noir detective story, 1940s smoky city"

─── SOUND DESIGN TAGS (Suno) ───

Atmospheric sounds via [Sound:...] tags in Lyrics:
  [Sound: Rain]              — rain
  [Sound: Wind]              — wind
  [Sound: Ocean waves]       — surf
  [Sound: Thunder]           — thunder
  [Sound: Birds chirping]    — birdsong
  [Sound: Fire crackling]    — crackling fire
  [Sound: City ambience]     — city noise
  [Sound: Vinyl crackle]     — vinyl crackle
  [Sound: Single Geiger click] — single click (very specific!)

For Gemini: describe atmosphere in words in the prompt.
  "with rain sounds in the background" instead of [Sound: Rain].

─── STADIUM / LIVE ATMOSPHERE ───

For live-feel tracks:

Stadium Intro:
  [Intro: stadium crowd ambience | big applause | cheering | distant chanting | stage reverb]

Stadium Outro:
  [Outro: crowd fade | distant chanting | stadium echo | applause]

This creates the feel of a live performance.

─── VISUAL → AUDIO TRANSLATOR ───
(For Gemini Photo→Music pipeline)

When the user uploads a photo, the system translates visual elements to audio:

  Dark photo, night     → minor key, low BPM, dark mood, ambient
  Bright colors, day     → major key, upbeat, bright instruments, energetic
  Nature, forest         → acoustic, folk, organic instruments, reverb
  City, neon             → electronic, synthwave, urban, modern production
  Ocean, beach           → chill, ambient, waves, laid-back groove
  People, party          → upbeat, party, dance, high energy
  Old photo, sepia       → vintage, lo-fi, warm analog, nostalgic
  Rain, fog              → melancholic, atmospheric, reverb-heavy, intimate
</atmosphere_builder>

═══════════════════════════════════════════════════════════════════
§8. MOOD PALETTE
═══════════════════════════════════════════════════════════════════

<mood_palette>
// Full list of mood descriptors for the Style prompt.
// Choose MAX 1–2 from this list.

─── CORE MOODS ───

Uplifting      — positive, inspiring
Melancholic    — sad, contemplative
Haunting       — eerie, lingering
Dark           — gloomy, ominous
Joyful         — happy, celebratory
Nostalgic      — wistful, longing
Romantic       — tender, loving
Intense        — powerful, dramatic
Dreamy         — ethereal, floating
Peaceful       — calm, serene
Anxious        — tense, uneasy
Euphoric       — blissful, ecstatic
Mysterious     — enigmatic, intriguing
Aggressive     — confrontational, forceful
Playful        — light, fun
Epic           — grand, heroic
Bittersweet    — mixed emotions, sweet sadness
Triumphant     — victorious, celebratory
Somber         — grave, serious
Intimate       — personal, close
Defiant        — rebellious, bold
Vulnerable     — exposed, raw
Sultry         — sensual, seductive

─── ENERGY LEVELS ───

[Energy: Low]      — minimal intensity, quiet
[Energy: Medium]   — moderate, steady
[Energy: High]     — maximum, loud
[Energy: Building] — rising, from quiet to loud
[Chill]            — relaxed, laid-back
[Driving]          — propulsive, pulsing
[Explosive]        — sudden blast
[Frantic]          — chaotic, fast

─── V5 EXTENDED MOOD FORMAT ───
(For v5: natural language key:value tags)

[Mood: Euphoric]
[Atmosphere: Cyberpunk]
[Vibe: Midnight drive]
[Feeling: Bittersweet nostalgia]

These tags are valid in v5 and give cleaner parsing.
In v4.5-all it's better to use descriptive words in the Style prompt.
</mood_palette>

═══════════════════════════════════════════════════════════════════
§9. GENRE ANCHOR REFERENCE
═══════════════════════════════════════════════════════════════════

<genre_anchors>
// Use 1–2 genre anchors maximum. Main genre first.

Electronic & Dance:
  EDM · House · Deep House · Tech House · Techno · Trance
  Dubstep · Drum and Bass · Ambient · Synthwave · Retrowave
  Chillwave · Future Bass · Trap (EDM) · Electro · Industrial
  IDM · Downtempo · Chillstep · Hardstyle

Hip-Hop & R&B:
  Hip Hop · Rap · Boom Bap · Trap · Atlanta Rap · Hardcore Rap
  Lo-fi Hip Hop · R&B · Neo-Soul · Soul · Funk · Phonk

Rock & Alternative:
  Rock · Classic Rock · Indie Rock · Alternative Rock · Pop Rock
  Hard Rock · Punk Rock · Post-Punk · Grunge · Metal · Heavy Metal
  Alternative Metal · Progressive Rock · Psychedelic Rock · Garage Rock
  Blues Rock · Southern Rock · Post-Hardcore · Emo · Shoegaze
  Math Rock · Nu Metal · Sludge Metal · Thrash Metal · Death Metal
  Black Metal · Power Metal

Pop & Mainstream:
  Pop · Synth Pop · Electropop · Indie Pop · Dream Pop · Bedroom Pop
  Art Pop · Dance Pop · K-Pop · J-Pop · City Pop · Vocaloid

Country & Folk:
  Country · Modern Country · Outlaw Country · Bluegrass · Folk
  Indie Folk · Americana · Singer-Songwriter · Celtic

Jazz & Blues:
  Jazz · Smooth Jazz · Bebop · Cool Jazz · Jazz Fusion · Bossa Nova
  Soul Jazz · Swing · Blues · Delta Blues · Chicago Blues

World & Latin:
  Afrobeat · Reggae · Dancehall · Latin · Salsa · Bachata
  Reggaeton · Flamenco · World Music

Classical & Orchestral:
  Classical · Baroque · Orchestral · Cinematic · Neoclassical
  Opera · Minimalist

Other:
  Gospel · Lo-fi · Acoustic · Ballad
</genre_anchors>

═══════════════════════════════════════════════════════════════════
§10. KEY & TEMPO QUICK REFERENCE
═══════════════════════════════════════════════════════════════════

<key_tempo_ref>
// Quick reference. Full version — in 04_AUDIO_VOCAB.

─── KEY → MOOD MAPPING ───
Dark, aggressive, trap   → D minor, B minor
Bright, happy pop        → C major, G major
Epic, heroic             → E minor, A minor
Jazzy, soulful           → Bb major, Eb major, F major
Mysterious, cinematic    → C# minor, F# minor
Blues, roots              → A, E, G

─── BPM → GENRE MAPPING ───
60–70    Ballads, ambient, drone
73–77    Lo-fi hip hop
86–97    Pop, indie, folk
98–109   Country, R&B
109–132  Pop, rock, house
130–160  Punk, DnB, EDM
160–220  Thrash, DnB, speed metal

─── GROOVE FEEL ───
"medium swing"           → Jazz
"laid-back shuffle"      → Blues
"straight eighth notes"  → Rock, pop (driving)
"half-time feel"         → Slowed perception
"double-time feel"       → Faster perception
"triplet feel"           → Bounce, waltz-adjacent

All these parameters → INTO THE STYLE PROMPT, not into Lyrics.
</key_tempo_ref>

// ═══════════════════════════════════════════════════════════════
// END OF 02_STYLE_ENGINE.md · SunoForge v1.1
// Next file: 03_LYRICS_ENGINE.md
// ═══════════════════════════════════════════════════════════════
