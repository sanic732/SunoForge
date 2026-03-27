# 🟠 SUNOFORGE v1.1 — SUNO ADAPTER
# File 05 of 10 · v4.5-all / v5 / v5.5 · MAX MODE · Sliders · EXCLUDE · Clean Block

═══════════════════════════════════════════════════════════════════
§1. VERSION SELECTOR
═══════════════════════════════════════════════════════════════════

<version_selector>
─── v4.5-all (FREE · DEFAULT) ───
Description: "Best free model"
Architecture: Narrative prompting + meta-tags
Strengths:    Rhythm-oriented genres, compositional variety
Audio:        Clear foundation, may need post-processing
Style limit:  up to 1000 characters
Recommended:  Quick iterations, experiments, rhythm music (hip-hop, EDM)

─── v4.5+ (PRO) ───
Description: "Advanced creation techniques"
Improvements: Better meta-tag adherence, improved vocals

─── v5 (PRO) ───
Description: "Authentic vocals, superior quality and control"
Architecture: Enhanced narrative + JSON structures
Audio:        44.1kHz studio quality, balanced sound
Strengths:    Realistic vocals, prompt adherence 88%+
Exclusive:    JSON Structuring, Persona Tags, Studio 1.1, [Callback]
Recommended:  Professional vocals, commercial production

─── v5.5 (PRO · NEWEST · March 26, 2026) ───
Description: "Best and most expressive model — reflects the user's personality"
Architecture: v5 + Voices + Custom Models + My Taste
New features:
  - Voices: upload your own voice (30s–4min audio, verification, 4 credits/track beta)
  - Custom Models: train on 6+ own tracks (up to 3 models, rights required!)
  - My Taste: auto-adjustment + Magic Wand (free for everyone!)
  - Personas renamed to Voices (auto-migrated)
Prompting:    Long prompts (100–200 words) work BETTER than short ones
              New dynamic instructions: [Solo: 12s swell], modulate...
Includes:     Everything from v5

─── SELECTION LOGIC ───
IF SUNO_VERSION from preloader == "v4.5-all":
  → Do NOT use: JSON, V5 Persona Tags, [Callback]
  → DO use: all meta-tags, MAX MODE, Performance Notation, Pipe Stacking
  → Sliders: Weirdness + Style Influence

IF SUNO_VERSION == "v5":
  → All v4.5 capabilities PLUS:
  → JSON Structuring (§3)
  → V5 Persona Tags
  → Extended mood format [Mood: X], [Atmosphere: Y]

IF SUNO_VERSION == "v5.5":
  → Everything from v5 PLUS:
  → Voices (§11): voice upload, verification
  → Custom Models (§11): train on own tracks
  → My Taste: Magic Wand auto style selection
  → Long prompts (100–200 words) for best results
  → Dynamic instructions: [Solo: 12s swell], "modulate after 16 bars"
</version_selector>

═══════════════════════════════════════════════════════════════════
§2. MAX MODE TECHNIQUE
═══════════════════════════════════════════════════════════════════

<max_mode>
// Works on v4.5-all (free) and above.
// Semantic conditioning through prompt formatting.
// Pushes the model to allocate resources toward audio cleanliness.

─── LYRICS BOX (first line) ───
///*****///

─── STYLE BOX (start) ───
[Is_MAX_MODE: MAX] [QUALITY: MAX] [REALISM: MAX]

─── OPTIONAL (amplification) ───
[REAL_INSTRUMENTS: MAX]    — for acoustic genres

─── FULL EXAMPLE ───
Style:
  [Is_MAX_MODE: MAX] [QUALITY: MAX] [REALISM: MAX] Weathered baritone male
  vocals, gravelly exhausted delivery. Dark Atmospheric Stalker Folk-Rock,
  cinematic blues, acoustic guitar resonance, haunting violin, distorted
  electric bass. 85 BPM, 4/4 time. Cold rainy atmosphere, analog saturation,
  heavy compression, wide stereo field, [eq: mid-clear], [compression: heavy].

Lyrics (first line):
  ///*****///

HOW IT WORKS:
  MAX MODE tags are not "commands" by themselves.
  They function as semantic conditioning — prompt formatting
  that pushes the model to prioritize quality.
</max_mode>

═══════════════════════════════════════════════════════════════════
§3. JSON STRUCTURING (v5 Pro Only)
═══════════════════════════════════════════════════════════════════

<json_structuring>
// For maximum control in v5. Does NOT work on v4.5-all.

─── BASIC JSON ───
{
  "genre": "jazz-trap fusion",
  "mood": "introspective, tension-building",
  "bpm": 95,
  "elements": ["upright bass", "lo-fi boom bap", "melancholic piano"],
  "structure": "intro (ambient) → verse (trap drums) → chorus (full)",
  "vocals": "male, smoky, conversational"
}

─── EXTENDED JSON ───
{
  "primary_genre": "synthwave",
  "subgenre": "darkwave",
  "tempo": 110,
  "key": "D minor",
  "mood": {
    "primary": "melancholic",
    "secondary": "nostalgic",
    "energy": "medium-high"
  },
  "instruments": {
    "lead": "analog synth lead",
    "rhythm": "drum machine with gated reverb",
    "bass": "deep analog synth bass",
    "pads": "atmospheric pads with slow attack"
  },
  "vocals": {
    "type": "male",
    "style": "breathy, intimate",
    "effects": ["light reverb", "subtle delay"]
  },
  "production": {
    "mix_style": "wide stereo field",
    "compression": "light",
    "reverb": "medium hall",
    "eq": "warm, bass-heavy"
  }
}

IF user on v4.5-all requests JSON:
  → "JSON structuring is available in Suno v5 Pro.
     For v4.5-all I'll generate an equivalent narrative Style prompt.
     /set suno v5 to switch."
</json_structuring>

═══════════════════════════════════════════════════════════════════
§4. SLIDER SETTINGS
═══════════════════════════════════════════════════════════════════

<slider_settings>

─── SLIDERS ───

Weirdness (0–100%):
  How experimental/unpredictable the result will sound.
  Low → safe, genre standard
  High → unexpected, experimental

Style Influence (0–100%):
  How strictly Suno follows the Style prompt.
  High → precise adherence
  Low → more creative freedom for the model

Audio Influence (0–100%) — for Remix:
  How strongly the remix preserves the original.

Strength (v5):
  High (>70%) → strongly pulls toward the described sound prompt
  Low (<30%) → gentle influence
  Negative → repulsion from the described sound

Lyrics Strength (v5):
  High (>70%) → clear pronunciation, strict adherence
  Low (<30%) → free phrasing, atmospheric

─── RECOMMENDED COMBOS BY GOAL ───

GOAL                    │ WEIRDNESS │ STYLE INFLUENCE
────────────────────────┼───────────┼────────────────
Authentic genre         │ 20–35%    │ 90–100%
recreation              │           │
────────────────────────┼───────────┼────────────────
Balanced creative       │ 40–50%    │ 70–85%
fusion                  │           │
────────────────────────┼───────────┼────────────────
Wild experimental       │ 70%+      │ 40–60%
────────────────────────┼───────────┼────────────────
Faithful remix          │ 20–30%    │ 90%+
────────────────────────┼───────────┼────────────────
Transformative remix    │ 50%+      │ 60–75%

─── RECOMMENDED COMBOS BY GENRE ───

GENRE              │ WEIRDNESS │ STYLE INF │ NOTES
───────────────────┼───────────┼───────────┼──────────────
Rock/Metal         │ 40–60%    │ 70–85%    │ Low = clear guitar
Electronic/EDM     │ 50–80%    │ 50–70%    │ High weird OK for creative
Jazz/Classical     │ 30–50%    │ 75–95%    │ Low chaos for accuracy
Lo-fi/Hip-hop      │ 45–65%    │ 65–80%    │ Moderate for groove variety
Vocal-focused      │ 40–50%    │ 80–95%    │ Max vocal quality
Instrumental       │ 35–55%    │ 80–90%    │ Low weird for clarity
Pop/Radio          │ 20–35%    │ 85–95%    │ Safe, predictable
Trap/Rap           │ 35–55%    │ 70–85%    │ Balanced
Country            │ 25–40%    │ 85–95%    │ Genre accuracy critical
Cinematic/Epic     │ 30–50%    │ 80–90%    │ Controlled drama
</slider_settings>

═══════════════════════════════════════════════════════════════════
§5. EXCLUDE FIELD
═══════════════════════════════════════════════════════════════════

<exclude_field>
// Mandatory field. Always generate what should NOT be in the track.

─── FORMAT ───
Comma-separated, 1 line, 8–12 items.

─── RULES ───
1. Use MUSICAL terms, NOT engineering jargon
   GOOD: "EDM", "trap", "overproduced", "robotic drums", "auto-tune"
   BAD:  "brick-wall compression", "sidechain", "dithering"

2. Sources: genre names, instrument sounds, vibe/feel, era mismatches

3. EXCLUDE = opposite of target style
   If target is "intimate acoustic" → EXCLUDE: "EDM, heavy bass, auto-tune,
   overproduced, electronic drums, synthesizers, distortion, crowd noise"

─── GENRE-SPECIFIC EXCLUDE PRESETS ───

Lo-fi / Chill:
  EDM, aggressive, auto-tune, heavy drums, screaming, bright, overproduced, trap bass

Rock / Metal:
  synth pop, smooth jazz, gentle, lo-fi, whisper vocals, acoustic, mellow, electronic

Pop / Radio:
  death metal, noise, lo-fi, experimental, drone, harsh, distorted vocals, dissonant

Jazz:
  EDM, distorted guitars, auto-tune, screaming, trap, 808, blast beats, overproduced

Hip-Hop / Trap:
  orchestral, acoustic guitar, country, folk, operatic, jazz scat, classical

Cinematic / Epic:
  lo-fi, bedroom recording, punk, garage, raw, minimal, muffled, thin

Country:
  EDM, synthwave, death metal, auto-tune, robotic, electronic drums, dubstep

Ambient / Sleep:
  drums, vocals, loud, aggressive, fast, energetic, distorted, bass-heavy
</exclude_field>

═══════════════════════════════════════════════════════════════════
§6. CLEAN BLOCK PROTOCOL (Output Format)
═══════════════════════════════════════════════════════════════════

<clean_block>
// Output format for Suno. Copy-paste ready.
// 3 blocks + metadata. Each variant — a separate block.

─── TEMPLATE ───

🎹 **SONIC BLUEPRINT: [Title]**
**Target:** Suno [version] | **Weirdness:** [X]% | **Style Influence:** [X]%

**1. Style** (→ paste into "Style of Music"):
```
[Full Style prompt, including MAX MODE if applicable]
```

**2. Lyrics** (→ paste into "Lyrics"):
```
[Full markup with tags, Performance Notation, text]
```

**3. EXCLUDE:**
```
[comma-separated list]
```

💡 **Tip:** [Specific tip]

─── COMPACT FORMAT (for beginners) ───

Without EXCLUDE, without detailed sliders:

🎹 **[Title]**

**Style** (copy):
```
[Style]
```

**Lyrics** (copy):
```
[Lyrics]
```

💡 Generate 3–4 versions in Suno and pick the best.
</clean_block>

═══════════════════════════════════════════════════════════════════
§7. EXTEND FEATURE
═══════════════════════════════════════════════════════════════════

<extend_feature>
// For changing genre/tempo mid-track.

─── WORKFLOW ───
1. Generate a base track
2. Listen and find the exact timecode to cut (at drop or fade)
3. Press Extend
4. Settings: Audio Influence 100%, Style Influence 80%+, Creativity 20–30%
5. New Style prompt describes WHERE to go

─── TRANSITION SYNTAX ───
"From this point, the tempo accelerates to 180 BPM. The orchestral arrangement
strips back to minimal elements. Heavy drums enter with a driving beat."

─── RULES ───
- V4.5 responds better to NARRATIVE descriptions ("gradually accelerates")
  than to numerical ones ("change from 100 to 140 BPM")
- Max 2 extensions. After 3rd — quality degrades.
- For long tracks (4+ min): mark structure more explicitly,
  use section tags with energy indicators.
- Weirdness for Extend: lower than for base track (45–55%)
</extend_feature>

═══════════════════════════════════════════════════════════════════
§8. STUDIO 1.1 FEATURES (v5 Pro)
═══════════════════════════════════════════════════════════════════

<studio_features>
// Available with Suno Pro subscription only.

Track EQ (6-band):
  Presets: Flat, High-pass, Vocal, Warm, Presence, Bass Boost,
           Air, Clarity, Fullness, Lo-fi, Modern
  Impact: Reduces need for perfect prompt — you can fix it in Studio.

Loop Recording:
  Repeat sections, fast generation of multiple takes.
  Workflow: Generate section → loop → try variations → pick best.

Cover Mode for Stems:
  Transform stems: piano → guitar, hummed melody → full instrument.
  Preserves original rhythm and groove.

Mashup (MAFO — Mashup And Find Out):
  Two tracks → blend lyrics, melodies, rhythms, instrumentation.
  Full control over text. Source attribution.

Context Window Control:
  Limit what the model "sees" when generating new clips.
  Allows isolated refinement of sections.

Prompt Enhancement Helper:
  Rough genre/mood → click "Enhance" → detailed prompt.
  Good starting point for iterations.

IF user on v4.5-all asks about Studio features:
  → "Studio 1.1 is available in Suno Pro. On the free version
     you can use external tools for post-processing
     (see /help postprod). /set suno v5 to switch."
</studio_features>

═══════════════════════════════════════════════════════════════════
§9. NEGATIVE PROMPTING (Suno-specific)
═══════════════════════════════════════════════════════════════════

<negative_prompting>
// What works and what does NOT work in negative prompts.

─── WORKS ───
Removing instruments:
  "upbeat pop with drums and bass, no guitars"
  → Model has positive context + one specific exclusion

Excluding vocals:
  "instrumental only, no vocals, no choir, no spoken words"
  → Multiple confirmations prevent default vocals

Mix clarity:
  "lo-fi hip hop with piano and vinyl crackle, no synth pads"
  → Specificity prevents automatic layering

─── DOES NOT WORK ───
Gender exclusions:
  "no male vocals" → v4.5 IGNORES this (hardcoded ranges)
  SOLUTION: Positive statement "solo female vocalist, soprano" at the start

Vague phrasing:
  "without singing unless background only" → unpredictable
  "no sounds that are bad" → ignored
  "not like rock" → ignored (negates an entire concept)

─── CRITICAL LIMIT ───
Max 1–2 exclusions per prompt. More = risk of:
  - Arrangement collapse (too many removed elements)
  - Strange substitutions (model replaces with unexpected)
  - Over-interpretation

─── TRIGGER WORDS TO AVOID ───
NEVER use these in Style (paradoxically increase problems):
  "artifact"         → increases artifacts
  "glitches"         → audio stuttering
  "clipping audio"   → loud distortion
  "background noise" → increases hissing

INSTEAD use positive framing:
  "balanced dynamics, clean tone, consistent volume, warm sound"
</negative_prompting>

═══════════════════════════════════════════════════════════════════
§10. INSTRUMENTAL MODE
═══════════════════════════════════════════════════════════════════

<instrumental_mode>
// Triple protection against "vocal hallucinations":

1. Enable Instrumental toggle in Suno UI
2. Add [Instrumental] tag in first lines of Lyrics
3. Optional: "no vocals, no choir, no spoken words" in Style

Structural tags for instrumentals:
  [Dramatic Verse]           [Melodic Chorus]
  [Guitar Solo]              [Piano Interlude]
  [String Arrangement]       [Saxophone Solo]
  [Violin Melody]            [Synth Lead]
  [Orchestral Hit]           [Percussion Breakdown]
</instrumental_mode>

═══════════════════════════════════════════════════════════════════
§11. VOICES & CUSTOM MODELS (v5.5)
═══════════════════════════════════════════════════════════════════

<voices_custom>
─── VOICES (Pro/Premier) ───
Personas → renamed to Voices. All old Personas auto-migrated.

WORKFLOW:
  1. Settings → Voices → Create New Voice
  2. Record (min 30s, max 4min) or Upload audio (musical background OK)
  3. Verification: read text on screen → Suno confirms voice
  4. Voice appears in library (tied to account, not shared)
  5. When generating: select Voice in settings

COST: 4 credits per track (beta pricing)
STRATEGY:
  - Draft with regular voices → final with Voices (save credits)
  - For commercial orders: doubler not revealed
  - Recording in quiet room = better, but musical background works too

─── CUSTOM MODELS (Pro/Premier) ───
WORKFLOW:
  1. Settings → Custom Models → Create
  2. Upload 6+ own tracks (MUST have rights!)
  3. Give the model a name
  4. Wait ~a few minutes for training
  5. Select Custom Model when generating → stylistically closer to catalog

LIMITS: Up to 3 models simultaneously
STRATEGIES:
  - "Band A" model: 6+ band tracks → signature sound
  - "Lo-fi beats" model: 6+ lo-fi tracks → consistent style
  - "Film score" model: 6+ cinematic tracks → soundtrack generator
  - Switch between models by task
  ⚠️ DO NOT upload others' material — violation of Suno ToS!

─── MY TASTE (free for everyone!) ───
HOW: Analyzes what you generate and listen to → adjusts new tracks
MAGIC WAND: Button in Styles field → suggests styles matching your taste
TIP: Use Magic Wand as starting point for Quick Start
     → get auto-style → refine manually
</voices_custom>

// ═══════════════════════════════════════════════════════════════
// END OF 05_SUNO.md · SunoForge v1.1
// Next file: 06_GEMINI.md
// ═══════════════════════════════════════════════════════════════
