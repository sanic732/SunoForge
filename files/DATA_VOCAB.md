---
file_id: DATA_VOCAB
version: "3.0"
layer: data
scope: timbre · dynamics · groove · space · instrument_descriptors · production_character · key_tempo · modes · theory_to_prompt
key_concepts: [timbre, spectral_centroid, adsr, compression, groove, pocket, swing, stereo, depth, reverb, instrument_descriptors, mix_character, key_mood, bpm_genre, modal_language, theory_translation]
depends_on: [CORE_01_STYLE]
used_by: [CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE, DATA_RECIPES, DATA_POSTPROD]
rag_priority: high
redundancy: high
updated: "2026-07-27"
changelog: "v3.0 — undated: this file describes sound, not platforms · all parametric tag forms converted to prose · instrument descriptor catalogue moved here from the style engine · theory→tag table rewritten as theory→prompt-language · pipe-stacked examples unstacked"
---

# 🔊 SUNOFORGE v3.0 — SOUND VOCABULARY
# File 9 of 12 · DATA layer · undated

> **Why this file has no expiry date.** It describes how sound works and what
> to call it. Spectral centroid, ADSR, pocket and reverb decay do not change
> when a platform ships an update. Nothing here needs replacing quarterly.

> 📌 **This is a catalogue.** Completeness beats compactness. It exists to be
> drawn from — by a person looking for the right word, and by a model
> assembling a prompt. Long lists are the point, not a failure of editing.

> ⚠️ **Everything here goes into a prompt as prose.** No brackets, no colons,
> no values. "Warm, close-mic, heavily compressed" — not `[eq: warm]`. Bracket
> syntax belongs to structural labels in the Lyrics field only (CORE_02 §1).

═══════════════════════════════════════════════════════════════════
§1. HOW TO USE THIS
═══════════════════════════════════════════════════════════════════

<rag_zone id="how_to_use">

Four axes describe almost any recorded sound. Between them they cover what a
listener notices and what a producer adjusts:

  TIMBRE     what colour it is        §2
  DYNAMICS   how it moves in time     §3
  GROOVE     how it sits against the beat  §4
  SPACE      where it is              §5

A useful prompt names one or two of these deliberately rather than all four
vaguely. "Warm and close" says more than "good production".

─── THE SUBSTITUTION HABIT ───

Whenever you are about to write a generic word, come here and take a specific
one instead:

  "good production"     → warm, close-mic, lightly compressed
  "nice guitar"         → jangly clean tone with spring reverb
  "cool drums"          → tight, punchy, slightly behind the beat
  "big sound"           → wide stereo with long hall decay
  "professional"        → balanced, controlled, commercially polished

─── HOW MANY ───

Two or three of these per prompt. This is a catalogue to select from, not a
list to exhaust. Ten descriptors pulling in different directions produce an
average, and the average of everything is nothing (CORE_01 §13).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. TIMBRE — the colour of a sound
═══════════════════════════════════════════════════════════════════

<rag_zone id="timbre_core">

─── THE CORE WORDS ───

  BRIGHT      energy high in the spectrum · piercing, clear, cutting
  DARK        energy low in the spectrum · soft, deep, rounded
  WARM        strong lower midrange · full, saturated, comfortable
  AIRY        open extreme top · breath, space, lightness
  METALLIC    hard harmonics · cold, glassy, ringing
  MELLOW      gentle harmonic envelope, no sharp edges
  HARSH       rough and uneven, often distorted
  REEDY       thin and nasal, narrow band of energy
  BRASSY      bold metallic harmonics, forward and assertive
  WOODY       resonant and hollow, organic body
  GLASSY      clean and brittle, high and fragile
  SMOKY       soft-edged and slightly veiled
  GRITTY      textured with dirt, deliberately imperfect
  SILKY       smooth top end, no abrasion
  MUDDY       congested low midrange, unclear
  BOXY        a narrow resonant honk, like a small enclosure
  NASAL       concentrated upper midrange
  HOLLOW      missing midrange, scooped out
  FAT         wide and heavy, generous low end
  THIN        lacking body, weight missing
  LUSH        dense, layered, harmonically rich
  STERILE     technically clean and emotionally flat

</rag_zone>

<rag_zone id="timbre_spectral">

─── SPECTRAL CHARACTER, PRECISELY ───

The technical layer. Useful when deconstructing a reference (CORE_01 §12), or
when a plain adjective is not landing.

  SPECTRAL CENTROID — where the perceived "brightness" sits
    high, above roughly 4 kHz      bright, piercing, cutting
    middle, roughly 1–3 kHz        warm, balanced, clear
    low, below roughly 1 kHz       dark, dim, soft

  SPECTRAL SPREAD — how wide the energy is distributed
    wide                           bright, shimmering, complex
    narrow                         focused, percussive, singular

  SPECTRAL SKEWNESS — which side of centre holds the energy
    positive                       weighted toward the highs, bright slope
    negative                       weighted toward the lows, warm slope

─── FREQUENCY RANGES AND WHAT THEY DO ───

Knowing which band produces which adjective lets you describe a sound
accurately instead of approximately, and it is the same map used when
correcting a mix afterward (DATA_POSTPROD).

  20–60 Hz        sub                weight you feel rather than hear
  60–120 Hz       bass               power, punch, the body of a kick
  120–250 Hz      low mid            warmth — and, in excess, mud
  250–500 Hz      lower mid          body and fullness; boxiness if crowded
  500 Hz–2 kHz    midrange           where most instruments live; presence
  2–4 kHz         upper mid          attack and intelligibility; harshness
  4–8 kHz         presence           clarity, definition, sibilance
  8–15 kHz        air                shimmer, openness, breath
  above 15 kHz    extreme top        sense of space more than audible content

  WARM         more energy in the lower midrange
  BRIGHT       more energy in the presence band and above
  SMOOTH       less energy around the harshness peak
  HARSH        a peak in the upper midrange
  MUDDY        excess in the low midrange
  AIR          lifted extreme top

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. DYNAMICS — how a sound moves
═══════════════════════════════════════════════════════════════════

<rag_zone id="dynamics_adsr">

─── THE SHAPE OF A NOTE ───

Four stages. Naming the one that matters is often more useful than naming the
instrument.

  ATTACK — how quickly it arrives
    fast        percussive, immediate, struck — a piano, a plucked string
    slow        swelling, gradual, blown in — pads, bowed strings

  DECAY — how it falls from its peak
    fast        short and bright, gone quickly
    slow        an extended tail with the brightness still in it

  SUSTAIN — what it holds while the note lasts
    high        continuous and present
    low         fading away as it is held

  RELEASE — how it ends
    fast        cut off cleanly, abrupt
    slow        lingering, trailing away

  Two shorthand words cover most cases:
    PERCUSSIVE  fast attack, fast decay — hits and plucks
    SUSTAINED   slow attack, long hold — pads, strings, drones

</rag_zone>

<rag_zone id="dynamics_compression">

─── COMPRESSION CHARACTER ───

  TIGHT / CONTROLLED   consistent levels, small dynamic swings
  PUNCHY               transients survive while peaks are held down
  TRANSPARENT          applied so gently it is not audible as an effect
  GLUED                elements locked together as one performance
  PUMPING              the compression is audible and rhythmic — house, EDM
  SQUASHED             flattened deliberately, no dynamic left
  BREATHING            audible recovery between phrases
  OPEN                 barely touched, full dynamic range intact
  BRICK-WALL           limited hard for maximum loudness

─── TRANSIENTS ───

  SNAPPY       sharply defined attacks
  SOFT         rounded, smoothed attacks
  AGGRESSIVE   attacks pushed forward, in your face
  NATURAL      untreated, as played

─── DYNAMIC RANGE AS A DESCRIPTION ───

  WIDE DYNAMICS      quiet passages stay quiet — classical, jazz, film score
  NARROW DYNAMICS    everything at a similar level — radio pop, EDM
  TERRACED           sudden jumps between levels rather than gradual change
  SWELLING           continuous rise and fall across phrases

  A loud-quiet-loud arrangement is a dynamic statement worth making
  explicitly: it is the defining feature of several genres and the model will
  not infer it from the genre name alone.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. GROOVE — how it sits against the beat
═══════════════════════════════════════════════════════════════════

<rag_zone id="groove_feel">

The most underused axis in prompt writing, and the one that most determines
whether music feels alive.

─── FEEL ───

  STRAIGHT       evenly divided, on the grid — rock, pop, techno
  SWUNG          unevenly divided, bouncing — jazz, blues, shuffle
  SHUFFLE        swing applied to the smaller subdivisions
  TRIPLET        divided in threes throughout
  HALF-TIME      the pulse feels half as fast — trap, dubstep breakdowns
  DOUBLE-TIME    the pulse feels twice as fast — drum and bass, punk
  RUBATO         tempo bends expressively, no strict grid
  MACHINE-TIGHT  quantised, deliberately inhuman
  LOOSE / HUMAN  small timing variations left in

─── POCKET — where notes sit relative to the beat ───

  IN THE POCKET     locked and natural, neither early nor late
  LAID-BACK         deliberately behind the beat — soul, lo-fi, hip-hop
  BEHIND THE BEAT   the same idea stated plainly
  PUSHED            ahead of the beat, urgent — punk, drum and bass
  RUSHING           further ahead, deliberately restless
  TIGHT POCKET      very precise placement
  LOOSE POCKET      flexible, breathing placement

  This single choice changes a track's whole character more than most
  instrument decisions. The same notes at the same tempo, played behind the
  beat instead of on it, become a different genre.

─── GROOVE CHARACTER ───

  TIGHT GROOVE      rhythm section locked together
  LOOSE GROOVE      relaxed, elastic, breathing
  FUNKY GROOVE      syncopated, weight on the offbeats
  SOULFUL GROOVE    warm and unhurried, sitting back
  PROPULSIVE        driving forward, never settling
  LOPING            long-short, ambling
  BUOYANT           lifting, bouncing, weightless
  DRIVING           insistent and forward
  HYPNOTIC          repetitive to the point of trance
  STUTTERING        deliberately interrupted, glitching
  MARCHING          even, deliberate, inevitable

─── TIME SIGNATURES ───

  4/4      the default; state it only to be explicit
  3/4      waltz feel, circular
  6/8      compound, rolling, triplet-based
  12/8     slow blues and doo-wop feel
  5/4      unsettled, restless
  7/8      progressive, tense, off-balance
  odd meter, changing meter — describe the effect as well as the number

  Suno's editing environment supports meters beyond 4/4 [OFFICIAL], and the
  details are in DATA_SUNO §8. In a prompt, saying "in a rolling 6/8" usually
  works better than the number alone, because the description carries the feel
  and the number does not.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. SPACE — where the sound is
═══════════════════════════════════════════════════════════════════

<rag_zone id="spatial">

─── STEREO PLACEMENT ───

  MONO                 single point, centred, no width
  STEREO               ordinary two-channel width
  WIDE / EXPANSIVE     full field, hard left to hard right, spacious
  NARROW / INTIMATE    centred and close, direct
  PRECISE IMAGING      clearly defined positions across the field
  MONO BASS            low end centred while the rest is wide — standard
                       practice and worth stating for dance music
  HARD-PANNED          elements pushed fully to one side — 1960s character

─── DEPTH — how far away things are ───

  CLOSE / INTIMATE     little reverb, full frequency range, present
  DISTANT / RECESSED   more reverb, softened highs, further back
  DEPTH CONTRAST       some elements close, others far — the single most
                       effective way to make a mix sound three-dimensional
  FLAT                 everything at the same distance, deliberately or not
  FORWARD              pushed toward the listener, confrontational

─── REVERB ───

  DRY                  almost none; direct and immediate
  WET / DRENCHED       heavily reverberant, swimming in reflections
  ROOM                 short decay; intimate and contained
  HALL                 long decay; grand, open
  CATHEDRAL            enormous decay; sacred, overwhelming
  PLATE                bright and metallic; classic vocal treatment
  SPRING               bouncy and characterful; surf, dub, retro amplifiers
  AMBIENT              very long and diffuse, no clear reflections
  GATED                cut off abruptly; the 1980s drum signature
  SLAPBACK             a single short echo; rockabilly, early rock and roll

─── DECAY LENGTH IN WORDS ───

  a tight room             very short
  a live room              short
  a scoring stage          medium
  a large hall             long
  a cathedral              very long, several seconds
  an endless wash          diffuse, no discernible end

─── ROOMS AS SHORTHAND ───

Naming a space carries reverb, tone and era in one phrase:

  a small dry booth · a wooden live room · a tiled bathroom
  a concrete stairwell · a school gymnasium · a jazz club
  a stone church · a scoring stage · an empty stadium
  a parked car · a bedroom with a duvet on the wall

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. INSTRUMENT DESCRIPTORS — the catalogue
═══════════════════════════════════════════════════════════════════

<rag_zone id="instruments_guitars">

The instrument name is a category. The adjective is the record. Method for
choosing between these: CORE_01 §5.

─── GUITARS, ELECTRIC ───

  jangly clean tone                       1960s pop, indie
  overdriven amp crunch                   hard rock
  heavy downtuned palm-muted riffing      metal
  shimmering clean arpeggios              post-rock, shoegaze
  tape-saturated wall of distortion       grunge, shoegaze
  gritty slide in open tuning             delta blues
  twangy single-coil with spring reverb   country, surf
  fuzzy psychedelic wah                   psych rock
  chiming twelve-string                   jangle pop
  tremolo-picked tremolo wall             black metal, shoegaze
  muted funk chops on the offbeat         funk, disco
  ringing harmonics over an open chord    ambient, math rock
  swampy tremolo                          southern gothic, noir
  scratchy post-punk angularity           post-punk

─── GUITARS, ACOUSTIC ───

  warm nylon-string fingerpicking         folk, bossa nova
  bright steel-string strumming           singer-songwriter
  percussive body-hit playing             modern acoustic
  close-miked and intimate                bedroom folk
  resonator slide                         blues, americana
  twelve-string shimmer                   1970s folk rock
  travis-picked alternating bass          country, folk

</rag_zone>

<rag_zone id="instruments_keys">

─── PIANO AND KEYBOARDS ───

  intimate close-miked grand              ballad, chamber
  bright hammered upright                 honky-tonk, ragtime
  dusty detuned upright                   lo-fi, saloon
  felted piano, soft and muted            modern neoclassical
  warm electric piano with tremolo        neo-soul, jazz
  bright reedy electric piano             1960s and 70s pop
  dusty sampled electric piano            lo-fi hip-hop
  prepared piano, damped and percussive   experimental
  cascading concert grand                 romantic, cinematic

─── ORGANS ───

  swirling drawbar organ through a rotary speaker   rock, gospel
  church pipe organ, enormous and sustained          sacred, gothic
  cheap combo organ, thin and buzzing                garage rock
  warm pumping gospel organ                          soul, gospel

─── SYNTHESISERS ───

  lush analog bass, round and warm        synthwave, funk
  crystalline digital bells               1980s pop, city pop
  supersaw lead stack                      trance, EDM
  squelching resonant acid line            acid house
  detuned pad with a slow attack           ambient, dream pop
  gritty bitcrushed lead                   chiptune, hyperpop
  wide unison brass stab                   synthwave, disco
  breathy vocal-like formant pad           ambient, cinematic
  arpeggiated sequence, tight and driving  synthwave, Berlin school
  tape-warped mellotron strings            prog rock, cinematic
  glassy FM electric piano                 1980s ballad

</rag_zone>

<rag_zone id="instruments_drums">

─── DRUMS, ACOUSTIC ───

  tight punchy kit, close-miked           pop, rock
  roomy kit with natural ambience         classic rock, indie
  brushed drums, relaxed shuffle          jazz, lounge
  gated snare, enormous and abrupt        1980s rock and pop
  dry deadened kit, no ring               1970s funk and soul
  crashing loose jazz kit                 bebop, free jazz
  double-kick blast beats                 extreme metal
  marching field drums                    cinematic, martial
  hand percussion, congas and shakers     latin, afrobeat
  taiko drums, enormous and slow          trailer, cinematic
  timpani rolls under the orchestra       symphonic
  tambourine on the backbeat              1960s pop, gospel

─── DRUMS, PROGRAMMED ───

  deep 808 kick with crisp hi-hat rolls   trap
  four-on-the-floor drum machine          house, techno
  chopped breakbeat loop                  drum and bass, jungle
  dusty boom-bap, lightly swung           lo-fi hip-hop
  minimal electronic clicks and pops      IDM, minimal
  slowed Memphis cowbell pattern          drift phonk
  log drum bassline                        amapiano
  reverse-reversed snare fills             modern pop
  handclaps and finger snaps in place of a snare   soul, indie pop

─── BASS ───

  round warm sub                          lo-fi, chill
  distorted 808 sub                       trap, phonk
  funky slap, tight in the pocket         funk, disco
  walking upright                         jazz, swing
  sidechained synth bass, pumping         house, EDM
  gritty overdriven bass guitar           grunge, stoner rock
  rumbling modulated reese                drum and bass, dubstep
  melodic picked bass high in the mix     post-punk, new wave
  fretless bass, sliding between notes    jazz fusion, 1980s ballad
  tuba or sousaphone as the bass          new orleans brass

</rag_zone>

<rag_zone id="instruments_orchestral">

─── STRINGS ───

  sweeping cinematic swells               trailer, epic
  intimate string quartet, close-miked    chamber, indie
  haunting solo violin with heavy vibrato folk, cinematic
  dark cello drone                        ambient, horror
  pizzicato strings, plucked and playful  comedy, light cinematic
  tremolo strings, trembling and tense    suspense
  full tutti with brass                   symphonic
  fiddle, driving and rhythmic            celtic, bluegrass
  sul ponticello, glassy and scraping     avant-garde, horror

─── BRASS AND WIND ───

  smoky tenor saxophone, club tone        jazz, noir
  bright mariachi trumpet                 latin
  muted trumpet, cool and restrained      cool jazz
  aggressive brass stabs                  funk, soul, EDM
  mournful harmonica                      blues, folk
  celtic tin whistle                      folk
  low brass swells, ominous               cinematic
  clarinet, liquid and agile              klezmer, swing, classical
  flute, breathy and close                folk, ambient, jazz
  bagpipes, droning and martial           celtic, cinematic
  french horn, noble and distant          orchestral, pastoral

─── VOICE AS AN INSTRUMENT ───

  wordless choir on open vowels           cinematic
  gospel choir answering the lead         gospel, soul
  four-part close harmony                 doo-wop, barbershop
  layered breathy vocal pad               dream pop, ambient
  chopped and pitched vocal samples       house, future bass
  throat singing, low and overtone-rich   world, cinematic
  spoken crowd chant                      anthem, stadium

</rag_zone>

<rag_zone id="instruments_world">

─── INSTRUMENTS THAT CARRY A PLACE WITH THEM ───

Naming one of these does more genre work than an adjective can, because each
arrives with a tradition attached.

  sitar, tabla                    indian classical, psychedelic
  koto, shakuhachi                japanese traditional
  guzheng, erhu                   chinese traditional
  oud, qanun, ney                 middle eastern
  balalaika, bayan accordion      slavic folk
  bouzouki                        greek
  kora, ngoni                     west african
  mbira, marimba, balafon         african
  steel pan                       caribbean
  charango, pan flute             andean
  didgeridoo                      australian
  bandoneón                       tango
  banjo, dobro, washboard         appalachian, old-time
  hurdy-gurdy, nyckelharpa        medieval, nordic folk
  gamelan                         indonesian
  duduk                           armenian, cinematic grief

  ⚠️ These carry cultural weight, not just a timbre. Use them because the
  music belongs there, not as decoration.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. PRODUCTION AND MIX CHARACTER
═══════════════════════════════════════════════════════════════════

<rag_zone id="production_character">

─── OVERALL CHARACTER, IN ONE PHRASE ───

  WARM        analog saturation, tape warmth, vinyl crackle
  POLISHED    clean, balanced, commercially finished
  RAW         unprocessed, gritty, left as recorded
  SPACIOUS    ambient, wide pads, reverb-forward
  PUNCHY      tight low end, fast transients, immediate
  CINEMATIC   wide, deep, orchestral dynamics
  MINIMAL     sparse, space between everything
  DENSE       layered, full, nothing unoccupied
  MURKY       deliberately unclear, submerged
  CRISP       defined, articulate, well-separated
  VINTAGE     period-accurate limitations, embraced
  MODERN      loud, wide, controlled

─── TEXTURE AND DEGRADATION ───

  tape saturation · tape hiss · wow and flutter · vinyl crackle
  bit reduction · sample-rate degradation · radio bandpass
  telephone filtering · cassette warble · tube warmth
  transformer colour · console noise floor · room bleed

  These are how a recording says when and where it was made. One is usually
  enough — stacking three produces something that sounds broken rather than
  characterful.

─── EFFECTS, DESCRIBED ───

  ping-pong delay bouncing across the field
  a single slapback echo
  long modulated delay washing into reverb
  chorus, thickened and slightly detuned
  flanging sweep
  phaser, slow and swirling
  ring modulation, metallic and atonal
  pitch-shifted harmony above the lead
  vocoded, robotic and pitched
  heavy sidechain pumping against the kick
  filter sweep opening across a build
  reverse reverb swelling into a hit

─── ERA SHORTHAND ───

Each of these carries a full production aesthetic:

  1950s     mono, close, plate reverb, minimal overdubbing
  1960s     hard-panned stereo, spring reverb, live takes
  1970s     warm analog, dry drums, wide but natural
  1980s     gated reverb, bright, digital sheen, big drums
  1990s     loud guitars or clean digital, depending on the scene
  2000s     compressed, bright, early digital hardness
  2010s     very loud, very wide, heavily tuned vocals
  2020s     deliberately imperfect again, lo-fi textures on clean recordings

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. KEY AND TEMPO
═══════════════════════════════════════════════════════════════════

<rag_zone id="key_tempo">

⚠️ Written as prose inside the Style description, and only for platforms where
a numeric tempo works. Lyria wants tempo described in words instead
(DATA_GOOGLE §3).

─── KEY AND ITS ASSOCIATIONS ───

These associations are conventional rather than acoustic — they come from
repertoire, not physics. They are still useful, because the model learned the
same conventions.

  dark, heavy, aggressive          D minor, B minor, F minor
  bright, open, happy              C major, G major, D major
  epic, heroic, cinematic          E minor, A minor, C minor
  warm, soulful, jazzy             B♭ major, E♭ major, F major
  mysterious, unsettled            C♯ minor, F♯ minor
  blues and roots                  A, E, G
  wistful, bittersweet             E major, A major with minor turns
  sacred, still                    D major, G minor

  Guitar-led music tends toward E, A, D and G. Horn-led music tends toward
  flat keys. Stating a key that fits the instrumentation makes the
  arrangement more idiomatic.

─── TEMPO BY GENRE ───

  60–70      ballads, ambient, drone, drift phonk
  70–80      lo-fi hip-hop, slow soul
  80–95      boom-bap, trap at half-time, downtempo
  85–100     pop ballad, indie, folk
  95–110     country, R&B, mid-tempo pop
  100–115    amapiano, afrobeats, reggaeton
  110–130    pop, rock, disco, house
  120–130    house, techno, mainstream dance
  130–150    trance, hard techno, punk, modern trap at double-time
  140–160    drum and bass at half-time feel, dubstep
  160–180    drum and bass, hardcore, fast punk
  180–220    thrash, speed metal, breakcore

  ⚠️ Tempo and feel interact. Trap written at 140 with a half-time feel sounds
  slower than folk at 90. Say the feel as well as the number.

─── LENGTH AND MATERIAL ───

Roughly one minute of song is a verse plus a chorus at a moderate tempo. This
is the arithmetic that decides whether a long target produces a full song or
padding (CORE_02 §12).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§9. MODES AND SCALES
═══════════════════════════════════════════════════════════════════

<rag_zone id="modal_language">

Mode names are not reliably understood [COMMUNITY]. Describe the effect
instead — and if you want to name the mode, do both.

  LYDIAN         dreamy, floating, shimmering, unresolved brightness
  PHRYGIAN       spanish, flamenco, dark and eastern
  DORIAN         jazzy minor, soulful, hopeful within sadness
  MIXOLYDIAN     bluesy major, relaxed, rock and folk
  AEOLIAN        plain natural minor, melancholic
  LOCRIAN        unstable, unresolved — rarely useful as a whole-track idea
  HARMONIC MINOR exotic, dramatic, with a sharpened leading tone
  WHOLE TONE     dissolving, dreamlike, no gravity
  PENTATONIC     open and folk-like, works almost everywhere
  BLUES SCALE    the flattened notes of blues and rock

  Names that do tend to land as written: pentatonic, blues scale, harmonic
  minor, chromatic.

─── HARMONIC CHARACTER WITHOUT THEORY ───

Often more effective than naming a mode at all:

  simple and diatonic, nothing unexpected
  one chord throughout, hypnotic
  a descending bassline under static harmony
  a borrowed minor chord that stings
  unresolved — never returns home
  a key change up for the final chorus
  jazz harmony, extended chords throughout
  modal, drifting between two chords
  drone underneath a moving melody

  Chord progressions themselves, and how to write them into a lyric, are in
  CORE_02 §10.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§10. THEORY → PROMPT LANGUAGE, BY GENRE
═══════════════════════════════════════════════════════════════════

<rag_zone id="theory_to_prompt">

What actually makes each genre recognisable, translated into words that go
into a Style description. Written as prose — the previous edition presented
this table in a bracketed, pipe-separated form that was never a documented
syntax (CORE_02 §4).

  GENRE            WHAT DEFINES IT      WRITE THIS
  ──────────────── ──────────────────── ──────────────────────────────────────
  Classic rock     jangly clean, back-  jangly clean guitar, driving backbeat,
                   beat                 tambourine, warm analog room
  Hard rock        power chords         palm-muted power chords, overdriven
                                        amps, driving kick and snare
  Glam metal       pinch harmonics      screaming lead with pinch harmonics
                                        and whammy bends, bright 1980s mix
  Thrash           gallop, fast 16ths   fast galloping palm-muted riffs,
                                        double-kick, snarled vocal
  Death metal      growls, blast beats  guttural growl, blast beats,
                                        downtuned guitars, no melody
  Black metal      tremolo, shrieks     tremolo-picked wall, blast beats,
                                        shrieked vocal, deliberately lo-fi
  Power metal      operatic, twin leads soaring operatic tenor, twin guitar
                                        harmonies, double-kick, epic
  Nu metal         syncopation          syncopated downtuned riff, rapped
                                        verse, screamed chorus
  Sludge           slow and crushing    very slow, downtuned, feedback-heavy,
                                        growled, dragging
  Prog rock        odd meter            shifting meters, mellotron, extended
                                        instrumental sections
  Psychedelia      fuzz and wah         fuzz guitar, wah, sitar, heavy reverb,
                                        backwards tape
  Grunge           loud-quiet dynamics  quiet verses into a distorted wall,
                                        raw untrained vocal
  Shoegaze         texture over notes   wall of reverb and distortion, vocal
                                        buried in the mix, dreamy
  Emo              clean twinkle        clean interlocking arpeggios,
                                        emotional cracked vocal
  Post-punk        angular and cold     angular scratchy guitar, melodic high
                                        bass, deadpan vocal, dry production
  Lo-fi hip-hop    dust and swing       dusty jazz piano samples, swung
                                        boom-bap, vinyl crackle, no vocal
  Boom-bap         sampled soul         chopped soul sample, hard snare,
                                        conversational rap
  Trap             808 and hi-hats      deep 808 sub, rolling triplet hi-hats,
                                        dark sparse melody, tuned vocal
  Drift phonk      slowed Memphis       slowed cowbell pattern, distorted 808,
                                        murky ambient pad
  Deep house       warm and pumping     four-on-the-floor, sidechained warm
                                        bassline, smooth chords
  Techno           relentless           machine-tight, hypnotic, minimal,
                                        industrial texture
  Drum and bass    fast breaks          chopped breakbeat at high tempo,
                                        rolling reese bass
  Dubstep          wobble, half-time    modulated wobble bass, half-time
                                        drums, heavy sub
  Synthwave        analog nostalgia     supersaw leads, analog bass, gated
                                        drums, neon 1980s atmosphere
  Hyperpop         joyful damage        pitch-shifted vocals, distorted 808,
                                        glitching, deliberately overloaded
  Amapiano         log drum             log drum bassline, shaker-driven
                                        percussion, spacious mid-tempo groove
  Afrobeats        polyrhythm           interlocking percussion, melodic bass,
                                        relaxed vocal, bright production
  Reggae           the offbeat          offbeat guitar skank, deep bass,
                                        spacious dub effects
  Gospel           call and response    full choir answering a lead, organ,
                                        hand claps, building intensity
  Soul             warmth and horns     warm horn section, tight rhythm
                                        section behind the beat, ribbon warmth
  Funk             the one              syncopated slap bass, muted guitar
                                        chops, tight horn stabs
  Jazz             swing and harmony    swung ride cymbal, walking bass,
                                        extended chords, improvised solos
  Bossa nova       gentle sway          nylon-string guitar, brushed drums,
                                        soft close vocal, swaying feel
  Blues            twelve bars          shuffled twelve-bar, slide guitar,
                                        call-and-response vocal phrasing
  Country          steel and story      pedal steel, banjo, warm baritone with
                                        a slight drawl, narrative lyric
  Bluegrass        acoustic speed       fast flatpicked guitar, banjo rolls,
                                        fiddle, high close harmony
  Folk             voice and guitar     fingerpicked acoustic, close intimate
                                        vocal, minimal arrangement
  Celtic           modal and rolling    fiddle and tin whistle over a bodhrán,
                                        rolling 6/8, modal melody
  Flamenco         phrygian and fire    fast spanish guitar, palmas, dark
                                        phrygian melody, passionate vocal
  Cinematic        scale and swell      full orchestra, taiko, string swells,
                                        wordless choir, wide and deep
  Ambient          time and space       sustained pads, no percussion, very
                                        slow, unresolved
  Classical        idiom by period      name the period — baroque counterpoint,
                                        romantic sweep, minimalist repetition

</rag_zone>

═══════════════════════════════════════════════════════════════════
§11. INSTRUMENT NAMES — a flat reference
═══════════════════════════════════════════════════════════════════

<rag_zone id="instrument_names">

For recall. Combine with a descriptor from §6 before use — a bare name is a
category, not a sound.

  KEYS        piano · upright piano · grand piano · felted piano · electric
              piano · rhodes · wurlitzer · clavinet · harpsichord ·
              celesta · organ · hammond organ · pipe organ · combo organ ·
              accordion · melodica · mellotron · synthesiser · analog synth ·
              modular synth · pad · arpeggiator · lead synth · sub bass

  GUITARS     acoustic guitar · nylon-string · twelve-string · electric
              guitar · hollow-body · resonator · lap steel · pedal steel ·
              baritone guitar · bass guitar · upright bass · fretless bass ·
              synth bass · ukulele · banjo · mandolin · dobro · sitar

  DRUMS       drum kit · kick · snare · hi-hat · ride · crash · toms ·
              brushes · drum machine · 808 · 909 · breakbeat · taiko ·
              timpani · congas · bongos · djembe · cajón · tambourine ·
              shaker · cowbell · handclaps · finger snaps · woodblock ·
              triangle · gong · marimba · vibraphone · glockenspiel

  STRINGS     violin · viola · cello · double bass · string section ·
              string quartet · harp · fiddle · erhu · guzheng · koto · oud

  BRASS       trumpet · cornet · flugelhorn · trombone · tuba · french horn ·
              brass section · sousaphone

  WOODWIND    flute · piccolo · clarinet · bass clarinet · oboe · cor
              anglais · bassoon · saxophone · soprano sax · alto sax ·
              tenor sax · baritone sax · recorder · tin whistle · pan flute ·
              shakuhachi · duduk · harmonica · bagpipes · didgeridoo

  VOICE       lead vocal · backing vocals · choir · gospel choir · chamber
              choir · spoken word · rap · scat · throat singing · whistling ·
              humming · vocoder · talkbox

  ELECTRONIC  sampler · turntable scratch · field recording · white noise
              riser · sub drop · impact hit · reverse cymbal · tape stop ·
              vinyl crackle · foley

  Whether these appear as words in a Style description or as bracketed
  section labels in a Lyrics field depends on the field, not the instrument —
  CORE_01 §5 and CORE_02 §3.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§12. PUTTING WORDS TOGETHER
═══════════════════════════════════════════════════════════════════

<rag_zone id="combining">

─── A DESCRIPTOR STACK THAT WORKS ───

  [instrument] + [how it is played] + [how it is recorded]

    upright bass, walking, close-miked with plenty of finger noise
    electric guitar, tremolo-picked, drowned in plate reverb
    drum kit, brushed and behind the beat, in a small dry room

  Three decisions, one phrase, and no ambiguity left for the model to resolve.

─── DESCRIBING A WHOLE MIX ───

Pick one word from each axis rather than three from one:

    warm, punchy, close                     — intimate and immediate
    bright, wide, drenched                  — big and modern
    dark, loose, distant                    — murky and dreamlike
    clean, tight, dry                       — clinical and precise

─── CONTRADICTIONS TO AVOID ───

  ❌ warm and bright and airy and dark      picks a fight with itself
  ❌ tight, punchy, loose and breathing     opposite dynamic requests
  ❌ intimate close-mic in a cathedral      unless the contrast is the point
  ❌ minimal, dense, layered and sparse     four words, no information

  Depth contrast is the one apparent contradiction that is real and useful:
  a close vocal in a distant room is a deliberate arrangement, not a conflict.

─── WHERE THIS VOCABULARY IS USED ───

  Building a Style prompt                   CORE_01 §5, §9
  Deconstructing a reference recording      CORE_01 §12
  Ready-made genre configurations           DATA_RECIPES
  Correcting a mix after generation         DATA_POSTPROD

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_VOCAB.md · SunoForge v3.0
// Next: DATA_RECIPES.md
// ═══════════════════════════════════════════════════════════════
