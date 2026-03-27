# 📝 SUNOFORGE v1.1 — LYRICS ENGINE
# File 03 of 10 · Tags · Notation · Structures · Chords

═══════════════════════════════════════════════════════════════════
§1. CRITICAL RULE: () vs []
═══════════════════════════════════════════════════════════════════

<parentheses_rule>
// THE MOST IMPORTANT RULE IN SUNO. Violation = broken track.

() ROUND BRACKETS = SUNG / PERFORMED
  Suno treats the content of () as backing vocal, echo, inner voice.
  ✅ (I'm still here)     → soft echo / backing vocal
  ✅ (Yeah!) (Ooh-whoa)   → ad-libs, sung as background
  ✅ (deep resonant)      → performance quality hint (with vocal drone)
  ❌ (say this in a spoken voice)  → Suno will SING this instruction!
  ❌ (play guitar softly here)     → Suno will SING "play guitar softly here"!

[] SQUARE BRACKETS = INSTRUCTIONS / NOT SUNG
  Suno treats [] as structural and production commands.
  ✅ [Chorus]              → start of chorus
  ✅ [Guitar Solo]         → guitar solo
  ✅ [spoken word]         → next line will be spoken
  ✅ [Whisper]             → next line whispered

SPOKEN WORD RULE:
  ✅ CORRECT: [spoken word] on a separate line, then text below
  ❌ WRONG: (say this as spoken word) — Suno will sing it as backing vocal
</parentheses_rule>

═══════════════════════════════════════════════════════════════════
§2. PERFORMANCE NOTATION (Formatting Symbols)
═══════════════════════════════════════════════════════════════════

<performance_notation>
// NOT tags. These are symbols INSIDE the lyrics text that change performance.

SYMBOL    │ EFFECT                          │ EXAMPLE
──────────┼─────────────────────────────────┼──────────────────
~         │ Hold note, vibrato, pitch       │ ho~me, free~dom~
          │ movement                        │
──────────┼─────────────────────────────────┼──────────────────
-         │ Stretch syllables, break words; │ al-most,
          │ spell out letters               │ G-A-L-A-X-Y
──────────┼─────────────────────────────────┼──────────────────
ALL CAPS  │ Louder, more forceful, power    │ WE RISE together
          │ (MAX 1–3 words per section!)    │ (not all caps)
──────────┼─────────────────────────────────┼──────────────────
" "       │ Spoken, whispered, stylized     │ "you were never
          │ delivery                        │ there"
──────────┼─────────────────────────────────┼──────────────────
...       │ Stretch/sustain note.           │ Whispers.........
          │ More dots = longer hold         │ ................
──────────┼─────────────────────────────────┼──────────────────
/         │ Structure alternative signal    │ soft / broken
          │ (NOT sung)                      │

─── ALL CAPS RULES ───
  ✅ WE RISE together          (1–2 words = emphasis accent)
  ✅ NEVER coming back         (1 word = maximum impact)
  ❌ WE RISE TOGETHER NOW FOREVER (all caps = loses effect)
  Rule: 1–3 CAPS words per section maximum. More = dilution.

─── SCREAM / GROWL NOTATION ───
  For aggressive vocals: stretch vowels + ALL CAPS + tag
  [Scream]
  AAAAAH WE WILL NEVER BOW
  [Growl]
  RAAAAH TEAR THIS SYSTEM DOWN
  Rule: More vowel letters = stronger delivery. "AAAAAH" > "AH".

─── VOCAL DRONE / SUSTAIN ───
  [Vocal drone]
  (deep resonant)
  Whispers.....................
  → Long ellipsis = long sustain. 10+ dots = maximum hold.
</performance_notation>

═══════════════════════════════════════════════════════════════════
§3. PIPE STACKING SYNTAX
═══════════════════════════════════════════════════════════════════

<pipe_stacking>
// Primary method for combining tags in v4.5+.
// | acts as AND — Suno applies all instructions simultaneously.

─── FORMAT ───
[core element | era/genre | tone/mix | quirk detail]

─── RULES ───
1. Leading element = section or main function (left of first |)
2. MAX 4–6 modifiers (more = noise, model starts ignoring)
3. Use era anchors for genre accuracy (60s, 80s, 90s)
4. Each section gets its OWN stack (not one for the whole song)
5. Emotion tags — on a SEPARATE LINE, NOT in pipe (see §4)

─── EXAMPLES ───

60s Rock Verse:
  [Verse | 60s jangly guitar rhythm | clean Fender tone | bright treble EQ | light spring reverb | tambourine hits]

80s Glam Metal Solo:
  [Guitar solo | 80s glam metal lead | heavy distortion | pinch harmonics | wide stereo | whammy bar bends]

Cinematic EDM Drop:
  [Drop | sidechained synth bass | layered white noise riser | sub drop impact | stereo delay tail]

Gospel Pop Chorus:
  [Chorus | anthemic chorus | stacked harmonies | modern pop polish | bass drop]

Trap Verse:
  [Verse | autotuned delivery | tuned male vocal | light reverb | stereo slapback]

Lo-fi Intro:
  [Intro | instrumental only | dusty vinyl texture | warm jazz piano | soft rain ambience]

─── PRODUCER-LEVEL CATEGORY TAGS ───
(For maximum precision — labeled categories)

[Instrumentation: overdriven punk guitar | palm-muted power chords | fast downstrokes]
[Vocal: raspy lead vocal | gang shouts on last line]
[Mix: mono bass, stereo guitar | slight room reverb]

─── DYNAMIC INSTRUCTIONS (v5/v5.5 · NEW v1.1) ───

v5+ understands semantically clear instructions better than abstract images:

[Solo: 12s swell]                — solo with 12-second build
[Break: distorted bass drop]     — break with distortion bass drop
"extend section"                  — extend the current section
"modulate after 16 bars"          — modulation after 16 bars
"brief silence as reset"          — brief silence for "reset"
"soft drop then rebuild"          — soft drop and rebuild
"tempo shift from 90 to 120"     — tempo change

Rule: The more specific the instruction — the better v5.5 follows it.
      "12s swell" > "make it louder". "modulate after 16 bars" > "change key".

Category Rules:
  - Everything inside ONE set of brackets
  - Short, production-ready terms (not storytelling)
  - Place BEFORE section lyrics
  - Bar counts with care: [8 bar guitar solo | fast alternate picking]
</pipe_stacking>

═══════════════════════════════════════════════════════════════════
§4. CORE SECTION TAGS
═══════════════════════════════════════════════════════════════════

<section_tags>
// Core structural tags. Every section MUST begin with a tag.
// Without tags Suno "drifts" — loses structure after ~30 seconds.

─── MAIN STRUCTURE ───
[Intro]         — Opening, palette setup. Short. Stack style cues.
[Verse] / [Verse 1] / [Verse 2]  — Narrative, story. Lower energy than chorus.
[Pre-Chorus]    — Build before hook. Short lines, rising tension.
[Chorus]        — Main hook, emotional peak. Most memorable lines.
[Post-Chorus]   — Hook extension. Chants, vocal chops, instrumental response.
[Bridge]        — Contrast: mood/harmony change. If it sounds like Verse 3 — fail.
[Outro]         — Finale. Short text, space for fade.
[Hook]          — Memorable phrase (standalone from chorus).

─── DYNAMIC / ENERGY TAGS ───
[Build] / [Build-Up]   — Rising tension, drums and energy building
[Drop]                  — High-energy release (EDM, trap, bass music)
[Breakdown]             — Stripped-back, contrast, "breathing" space
[Break]                 — Short pause for contrast
[Instrumental]          — No vocals. Pure instrumental section.
[Solo]                  — Instrumental solo (guitar solo, sax solo)
[Interlude]             — Transition between sections
[Fade Out] / [Fade In]  — Volume change

─── ADVANCED STRUCTURE (v4+) ───
[Final Chorus]          — Climactic last chorus
[Chorus x2]             — Repeat chorus twice
[Outro: Fade out]       — Explicit fade-out ending
[Outro: Big finish]     — Explicit crescendo ending
[Hook Loop]             — Short loop-friendly hook (for Shorts/Reels)
[Beat switch]           — Tempo/rhythm change
[Hook first]            — Open with hook before verse
[Band drop-out before final chorus]  — Strip arrangement before finale
[Emotional release]     — Climactic emotional moment

─── V5 ONLY ───
[Callback: Chorus melody]  — Reference to melody from a previous section

─── PLACEMENT RULES ───
1. Tag ALWAYS on a separate line BEFORE section text
2. Every section STARTS with one or more stacked tags
3. Do NOT skip tags — Suno uses them as structural anchors
4. [Chorus] directly before chorus text is more effective than once at file start
</section_tags>

═══════════════════════════════════════════════════════════════════
§5. VOCAL TAGS
═══════════════════════════════════════════════════════════════════

<vocal_tags>

─── GENDER & CHARACTER ───
[Male Vocal] / [Male Vocalist]    — Male voice
[Female Vocal] / [Female Vocalist] — Female voice
[Duet]                             — Duet (see Duet Protocol in 02 §5)
[Choir]                            — Choir
[Boy] / [Girl]                     — Young voice
[Announcer] / [Reporter]           — Announcer / Reporter
[Female narrator]                  — Female narrator

─── DELIVERY STYLE ───
[Whisper] / [Whispers]      — Whisper (ASMR, ballads, ambient)
[Spoken word]                — Speech, not singing (hip-hop, intro, poetry)
[Rap]                        — Rhythmic flow
[Chant vocals]               — Group chant (anthems, rock, metal)
[Crowd-style vocals]         — Mass energy (stadium)
[Harmonies] / [Stacked harmonies] — Layered voices (pop, R&B, gospel)
[Falsetto]                   — High male register
[Belting]                    — Powerful sustained notes
[Growl]                      — Aggressive texture (metal)
[Crooning]                   — Smooth, intimate (jazz, vintage pop)
[Operatic]                   — Classical vocal technique
[Scat]                       — Jazz improvisation with syllables
[Screaming] / [Screams]      — Extreme vocals
[Anthemic chorus]            — Stadium delivery
[Autotuned delivery]         — Modern hip-hop/pop processing
[Raspy lead vocal]           — Hoarse, textured
[Cinematic vocal pacing]     — Deliberate, dramatic tempo
[Spoken word verse]          — Entire verse spoken

─── EMOTION DELIVERY ───
⚠️ Place on a SEPARATE LINE before text. NOT in pipe stack.

[Crying voice]               — Weeping, heartbroken delivery
[Angry tone]                 — Aggression, confrontation
[Mocking laughter]           — Sarcasm, dark humor
[Spoken word crying]         — Spoken + weeping (killer combo)
[Vulnerable]                 — Raw, exposed emotion
[Defiant]                    — Rebellious, strong
[Sultry]                     — Seductive, smooth
[Joyful]                     — Happy, celebratory
[Melancholic]                — Sad, wistful
[Intimate]                   — Personal, close

"Killer Combo" — Emotional Whiplash:
  [spoken word crying] Why did you leave me [laughter]
  → Instant dramatic break in one line.

─── VOCAL EFFECTS ───
[Reverb] / [Reverb Heavy]    — Space, echo
[Delay] / [Echoing vocals]   — Repeating echo
[AutoTune]                    — Pitch correction/effect
[No AutoTune]                 — Natural pitch
[Distorted Vocals]            — Overdriven, gritty
[Filtered Vocals]             — Lo-fi, telephone effect
[Vocoder]                     — Robotic synthesis (electronic, synthwave)
[Telephone Effect]            — Narrow, filtered speaker
[Tape-Saturated]              — Warm analog degradation
[Harmonized chorus]           — Harmonized backing on chorus

─── SATB / CHORAL ───
[Multiple voice chorus s a t b] — Soprano + Alto + Tenor + Bass
[SATB]                          — Same, abbreviated
[Choir: Gospel]                 — Gospel choir

SATB RULE: Use ONLY on the chorus. Whole song = kills impact.

─── V5 PERSONA TAGS (Pro only) ───
[Whisper Soul]            — Soft, intimate R&B
[Power Praise]            — Gospel power
[Retro Diva]              — Classic 60s–80s female
[Conversational Flow]     — Natural, rap-adjacent
[Persona: Pop Star]       — Modern pop
[Vocal Style: Breathless] — Breathless, urgent
[Vocal Style: Melismatic] — Complex vocal runs (R&B/soul)
[Vocal Style: Monotone]   — Flat, deadpan (post-punk, rap)
[Vocal Style: Raspy]      — Hoarse, weathered
[Vocal Style: Shouting]   — High energy (punk, metal)
</vocal_tags>

═══════════════════════════════════════════════════════════════════
§6. AD-LIBS & ONOMATOPOEIA
═══════════════════════════════════════════════════════════════════

<adlibs>
// Ad-libs add bounce, attitude, organic energy.
// Work best in hip-hop, trap, pop, R&B.

─── FORMAT ───
[adlib TAG]
SOUND ALL CAPS

Place on a separate line between lyric lines, on the beat:

[Verse | autotuned delivery]
Running through the city lights
[adlib HEY]
Nothing ever slows me down
[adlib UH UH]
Still the same, still alive

─── COMMON AD-LIBS ───
[adlib boom]    — impact/hit
[adlib clap]    — clap
[adlib hey]     — "HEY" shout
[adlib yeah]    — "YEAH"
[adlib whoa]    — "WHOA"
[adlib uh]      — "UH" rhythmic filler
[adlib ayy]     — "AYY"
[adlib ok]      — "OK"
</adlibs>

═══════════════════════════════════════════════════════════════════
§7. ATMOSPHERE & SOUND TAGS
═══════════════════════════════════════════════════════════════════

<atmosphere_tags>

─── ENVIRONMENTAL ───
[Birds chirping]    [Rain]           [Thunder]
[Wind]              [Ocean waves]    [City ambience]
[Forest]            [Fire crackling]

─── HUMAN & CROWD ───
[Applause]          [Cheering]       [Crowd noise]
[Distant chanting]  [Stadium ambience] [Stage reverb]
[Clapping]          [Chuckles]       [Audience laughing]
[Sighs]             [Whistling]

─── MECHANICAL / ELECTRONIC ───
[Phone ringing]     [Beeping]        [Bell dings]
[Bleep]             [Static]         [Record scratch]

─── MUSICAL EFFECTS ───
[Silence]           — Complete silence, dramatic pause
[Censored]          — Bleep censorship
[Fade]              — Volume reduction
[Stop]              — Abrupt ending
[Drum fill transition into chorus]  — Drum fill as transition
[Smooth crossfade intro to verse]   — Smooth crossfade
</atmosphere_tags>

═══════════════════════════════════════════════════════════════════
§8. SONG STRUCTURE TEMPLATES
═══════════════════════════════════════════════════════════════════

<structure_templates>
// Ready-made structures. Choose or modify.

─── POP (standard) ───
[Intro] → [Verse 1] → [Pre-Chorus] → [Chorus] →
[Verse 2] → [Pre-Chorus] → [Chorus] →
[Bridge] → [Final Chorus] → [Outro]

─── ROCK ───
[Intro] → [Verse 1] → [Chorus] →
[Verse 2] → [Chorus] →
[Guitar Solo] → [Bridge] → [Final Chorus] → [Outro]

─── EDM / ELECTRONIC ───
[Intro] → [Build-Up] → [Drop] →
[Breakdown] → [Build-Up] → [Drop] → [Outro]

─── HIP-HOP ───
[Intro] → [Verse 1] → [Hook] →
[Verse 2] → [Hook] → [Verse 3] → [Hook] → [Outro]

─── BALLAD ───
[Intro] → [Verse 1] → [Verse 2] → [Chorus] →
[Verse 3] → [Chorus] → [Bridge] →
[Final Chorus | key change] → [Outro]

─── INSTRUMENTAL ───
[Intro] → [Theme A] → [Theme B] →
[Development] → [Recap] → [Coda]

─── CINEMATIC / EPIC ───
[Intro | vocal drone] → [Verse | sparse, building] →
[Build | orchestral tension] → [Chorus | full orchestra | choir] →
[Bridge | stripped] → [Final Chorus | epic wall of sound] →
[Outro | fade, rain, distant echo]

─── SHORT / REELS (30 sec) ───
[Hook first] → [Verse 1 | 4 lines] → [Chorus | Hook Loop]
</structure_templates>

═══════════════════════════════════════════════════════════════════
§9. CHORD ENGINE
═══════════════════════════════════════════════════════════════════

<chord_engine>
─── BASIC SYNTAX ───
(Am) The city sleeps at night (F) beneath the silver moon
(C) Only the wind is singing (G) its age-old song

─── ADVANCED SYNTAX ───
[Chord progression: Am - F - C - G]
[Key: A minor]
[Tempo: 120 BPM]

─── POPULAR PROGRESSIONS ───
I-V-vi-IV   (C-G-Am-F)      — Most popular (pop, rock)
vi-IV-I-V   (Am-F-C-G)      — Emotional (ballads)
I-vi-IV-V   (C-Am-F-G)      — Classic (50s–60s)
ii-V-I      (Dm-G-C)        — Jazz
I-IV-V      (C-F-G)         — Blues/rock foundation
vi-V-IV-I   (Am-G-F-C)      — Modern pop

─── GENRE-SPECIFIC ───
Trap/Hip-Hop:  i-VI-III-VII  (Am-F-C-G in minor)
EDM Drop:      i-III-VI-VII  (minor progression, energetic)
Jazz:          ii-V-I-vi     (Dm-G-C-Am, extended)
Blues:          I-I-I-I-IV-IV-I-I-V-IV-I-V (12-bar blues)
</chord_engine>

═══════════════════════════════════════════════════════════════════
§10. LYRICS TOP-LOAD STRUCTURE
═══════════════════════════════════════════════════════════════════

<lyrics_topload>
// First 3–5 lines of Lyrics = "anchor tags" for initialization.

TEMPLATE (top of the Lyrics field):

///*****///
[BPM] | [Genre] | Key: [Key]
[Mood: X]
[Energy: Y]
[Intro | stacked style tags]
(opening atmosphere or hook)

[Verse 1 | stacked vocal + style tags]
[Vocal: style | mix]
lyric line
lyric line...

EXAMPLE (S.T.A.L.K.E.R. reference):

///*****///
[Intro | Dark Ambient | Sound: Wind and Geiger Counter]
[Acoustic Guitar | Slow Picking]

[Verse 1 | Female Vocal | Soft and Melancholic]
A rusty dawn o'er Pripyat starts to rise,
The counter in my pocket hisses lies...

NOTE: ///*****/// as first line activates MAX MODE semantic conditioning.

─── VERSION-AWARE PROMPT LENGTH (NEW v1.1) ───
v4.5-all: First 20–30 words of Style = maximum weight. Rest is bonus.
v5/v5.5:  ENTIRE Style length matters (up to 1000 characters).
          100–200 focused words > 10–20 keywords.
          But first words still have higher priority.
          Old short v3/v4 prompts → clipped/strange tracks on v5+.
Gemini:   Clip: 2–4 sentences. Pro: extended + time-based structure.
</lyrics_topload>

// ═══════════════════════════════════════════════════════════════
// END OF 03_LYRICS_ENGINE.md · SunoForge v1.1
// Next file: 04_AUDIO_VOCAB.md
// ═══════════════════════════════════════════════════════════════
