# 🎛️ SUNOFORGE v1.1 — POST-PRODUCTION
# File 08 of 10 · Mastering · Stems · DAW · Transfer Workflows

═══════════════════════════════════════════════════════════════════
§1. MASTERING CHAIN (5 stages)
═══════════════════════════════════════════════════════════════════

<mastering_chain>
// Recommended chain for Suno-generated tracks.

STAGE 1 — DE-ESSER:
  Goal:      Control harsh frequencies (3–7 kHz)
  Settings:  Threshold -3 dB, reduction 2 dB during peaks
  Tools:     Fabfilter Pro-DS, Waves De-esser

STAGE 2 — COMPRESSION:
  Goal:      Glue and dynamics control
  Type:      Transparent compressor
  Ratio:     2:1 — 4:1 (soft glue)
  Release:   0.1s (fast for tempo-driven content)
  Tools:     SSL G-Series, Universal Audio 1176

STAGE 3 — HARMONIC ENRICHMENT:
  Goal:      Vintage warmth and definition
  Type:      Tape saturation, transformer mode
  Drive:     Low, boost 2–4 kHz
  Tools:     UAD Ampex Tape Machine, Waves J37

STAGE 4 — PRECISE EQ:
  Low (50–70 Hz):    +2–3 dB for punch and warmth
  Mud (80–120 Hz):   -1–2 dB, high-pass at 30–40 Hz
  High (8 kHz):      +1–2 dB for clarity and air
  Tools:             Fabfilter Pro-Q, Waves SSL E-Channel

STAGE 5 — LIMITING:
  Type:       Lookahead limiter
  Ceiling:    -1 dB True Peak
  Color:      Enable color mode for character
  Tools:      Fabfilter Pro-L, Waves L2

─── WHAT NOT TO DO ───
❌ Double mastering: If Suno outputs a master → do NOT re-master in DAW
❌ Over-compression: Kills natural phrasing
❌ Phase-incompatible widening: Use M/S instead of Haas delay
</mastering_chain>

═══════════════════════════════════════════════════════════════════
§2. STEMS (Track Separation)
═══════════════════════════════════════════════════════════════════

<stems>
─── TOOLS ───
Ultimate Vocal Remover — stem separation (free)
Suno Studio 1.1       — built-in separation (Pro only)
LALAL.AI              — online separation service
Demucs                — Meta AI, open-source

─── WORKFLOW ───
1. Export track from Suno
2. Separate into stems: Vocals, Drums, Bass, Melody/Other
3. Import stems into DAW (Ableton, Logic Pro, FL Studio)
4. Individual processing of each track
5. Remixing / replacing elements / adding live instruments
6. Final mastering

─── STEM PROCESSING TIPS ───
Vocals:   De-esser → compression → EQ (remove muddiness) → reverb
Drums:    Transient shaping → parallel compression → EQ
Bass:     High-pass filter (remove sub-rumble) → compression → saturation
Melody:   EQ (clear space for vocals) → stereo widening
</stems>

═══════════════════════════════════════════════════════════════════
§3. DAW & TOOLS REFERENCE
═══════════════════════════════════════════════════════════════════

<tools>
─── DAW ───
Ableton Live     — Electronic music, live performance
Logic Pro        — Full production, Mac only
FL Studio        — Hip-hop, electronic, Windows/Mac
Reaper           — Budget-friendly, powerful, cross-platform
GarageBand       — Free, Mac/iOS, for beginners

─── MASTERING ───
Izotope Ozone    — Comprehensive processing (AI-assisted)
Diktatorial Suite — Professional mastering
CloudBounce      — Automatic online mastering (free tier)
LANDR            — AI online mastering

─── RESTORATION ───
Izotope RX       — Audio restoration (noise removal, clipping repair)
Unchirp          — Artifact removal
Accusonus ERA    — Quick correction

─── STEREO WIDTH ───
Recommendation: 50–60% width for natural sound.
Use multi-band widening or M/S processing.
Do NOT use Haas delay (phase issues with mono compatibility).
</tools>

═══════════════════════════════════════════════════════════════════
§4. GEMINI → SUNO TRANSFER WORKFLOW
═══════════════════════════════════════════════════════════════════

<transfer_workflow>
// When the user created a 30-sec sketch in Gemini and wants a full track.

─── PIPELINE ───
1. LISTEN:  Listen to the Gemini sketch, identify what you like
2. ANALYZE: Extract: genre, mood, instruments, vocals, tempo
3. EXPAND:  30-sec hook → full song structure (3–4 min)
4. ADAPT:   Gemini narrative → Suno GMIV+P + meta-tags + EXCLUDE
5. ENHANCE: Add MAX MODE, Slider recommendations, Production details
6. OUTPUT:  Clean Block Protocol

─── EXPANSION EXAMPLE ───

Gemini 30-sec sketch:
  "Mellow lofi hip-hop, soft drums, warm piano, vinyl crackle, chill vibe"

→ Suno 4-min track:

Style:
  [Is_MAX_MODE: MAX] [QUALITY: MAX] Late-night lo-fi hip-hop, 78 BPM,
  A minor, dusty jazz piano chords, warm sub-bass, soft boom-bap drums,
  vinyl crackle texture, intimate breathy female vocal, mellow chill vibe,
  close-mic bedroom recording, gentle sidechain, analog warmth

Lyrics:
  ///*****///
  [Intro | instrumental | soft piano | vinyl crackle | 4 bars]

  [Verse 1 | Female Vocal | whispered, intimate]
  text...

  [Chorus | soft harmonies | layered]
  text...

  [Verse 2 | Female Vocal | slightly more energy]
  text...

  [Chorus]
  text...

  [Bridge | stripped, just vocal and piano]
  text...

  [Outro | instrumental fade | vinyl noise]
</transfer_workflow>

═══════════════════════════════════════════════════════════════════
§5. SUNO STUDIO 1.1 EQ PRESETS (Pro Reference)
═══════════════════════════════════════════════════════════════════

<eq_presets>
// For Suno Pro users. Built-in 6-band EQ.

Flat       — No changes (default)
High-pass  — Removes low frequencies (clarity)
Vocal      — Emphasis on vocal range (2–5 kHz)
Warm       — Boost low mids (200–400 Hz)
Presence   — Boost presence (3–6 kHz)
Bass Boost — Boost lows (60–120 Hz)
Air        — Boost highs (10+ kHz)
Clarity    — Cut muddiness + boost clarity
Fullness   — Overall body boost
Lo-fi      — Cut highs + boost mids (lo-fi aesthetic)
Modern     — Modern bright mix
</eq_presets>

// ═══════════════════════════════════════════════════════════════
// END OF 08_POSTPROD.md · SunoForge v1.1
// Next file: 09_TEMPLATES.md
// ═══════════════════════════════════════════════════════════════
