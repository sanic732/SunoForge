# 🔵 SUNOFORGE v1.1 — GEMINI ADAPTER
# File 06 of 10 · Lyria 3 Clip + Lyria 3 Pro · Photo/Video · ProducerAI

═══════════════════════════════════════════════════════════════════
§1. PLATFORM TRIAD
═══════════════════════════════════════════════════════════════════

<platform_triad>
─── LYRIA 3 CLIP ───
Model ID:    lyria-3-clip-preview
Output:      30-second track (MP4 with cover or MP3)
Access:      Free (with limits) in Gemini App
Best for:    Jingles, intros, loops, moodboards, quick sketches

─── LYRIA 3 PRO ───
Model ID:    lyria-3-pro-preview
Output:      Tracks up to ~3 minutes ("studio" quality)
Structure:   Full control: intro, verse, pre-chorus, chorus, bridge, outro
Time-based:  Second-level breakdown: "intro (0–15s), verse (15–45s)..."
Lyrics:      Support for [Verse], [Chorus] and other tags
Access:      Gemini Pro/Ultra + Vertex AI + AI Studio + Google Vids
ProducerAI:  Up to ~5 minutes + editing (even free!)

─── SUNO v5.5 (→ 05_SUNO.md) ───
Output: Up to 5+ min. Exclusive: Voices, Custom Models, Studio 1.1, JSON, sliders.

KEY SHIFT v1.1: Not "Gemini=prototype, Suno=final", but THREE-LEVEL pipeline.
All Lyria tracks are marked with SynthID watermark.
</platform_triad>

═══════════════════════════════════════════════════════════════════
§2. LYRIA 3 PRO — PROMPTING (up to 3 minutes)
═══════════════════════════════════════════════════════════════════

<lyria_pro>
─── TIME-BASED STRUCTURE (key Pro technique) ───

TEMPLATE:
  Create a [X]-minute [genre] track about [theme].
  [Mood], [tempo], [instruments], [vocal].
  Structure:
  - Intro (0–Xs): [description]
  - Verse 1 (X–Xs): [description]
  - Pre-chorus (X–Xs): [description]
  - Chorus (X–Xs): [description]
  - Verse 2 (X–Xs): [description]
  - Bridge (X–Xs): [description]
  - Final chorus + outro (X–Xs): [description]

DYNAMIC INSTRUCTIONS (Pro understands):
  "big chorus with catchy vocal hook"
  "quiet breakdown with stripped-down instrumentation"
  "bridge with rising tension and modulated chords"
  "start soft under voiceover, then grow after 60 seconds"

LYRICS: WITH TAGS (Pro supports!):
  Lyrics:
  [Verse 1]
  Walking through the midnight rain...
  [Chorus]
  Light me up, I'm not afraid...
  Backing vocal in parentheses: "(go)", "(yeah!)"

"INSTRUMENTAL FIRST" WORKFLOW:
  Community lifehack — generate instrumental and vocals SEPARATELY:
  Step 1: "Create a 3-min [genre] instrumental. No vocals. Structure:..."
  Step 2: "Add [vocal type] to this track. Lyrics: [text]..."
  Result: less generic, more musical track.
</lyria_pro>

═══════════════════════════════════════════════════════════════════
§3. LYRIA 3 CLIP — 30-SECOND OPTIMIZATION
═══════════════════════════════════════════════════════════════════

<lyria_clip>
PRINCIPLE: 30 sec = ONE SCENE, not a mini-song. One riff or hook.

For scene: "fade-in pad, drop at 10s, hold groove till 30s"
For background: "no sudden transitions, consistent, no vocals, unobtrusive"
For loops: "loop-friendly, seamless start and end, no hard stop"
For jingles: "soft 5s → instruments enter → hit at 12s → groove"
</lyria_clip>

═══════════════════════════════════════════════════════════════════
§4. CORE RULES (Clip + Pro)
═══════════════════════════════════════════════════════════════════

<lyria_basics>
─── 6 TIPS (Google Official) ───
1. Text: theme + mood + genre (specific, not "make a song")
2. Photo/video: Lyria analyzes the scene → matches vibe
3. Genre + era: "90s skate punk", "K-pop with Motown vibe"
4. Instruments + dynamics + vocal: "soft piano intro, big rock chorus"
5. Lyrics: prefix for your own text; or theme → Lyria writes it
6. Iterations: "make it more...", "remove vocals", "slower tempo"

─── WORKS / DOES NOT WORK ───
✅ Emotions, scenes, instruments, genres, eras, Time & Place
✅ Time-based structure (Pro), tags in Lyrics: (Pro)
✅ Narrative descriptions, multimodal input, iterations
❌ Suno meta-tags in Style, JSON, EXCLUDE, sliders
❌ Performance Notation (~, -, CAPS), Pipe Stacking
❌ Precise BPM (use "around X BPM"), chords

─── ANTIPATTERNS ───
❌ Single-line prompts → generic. Specificity is needed.
❌ Overloading one line → mess. Break into sentences.
❌ "Make it sound like [artist]" → only "broadly inspired". Describe the sound.
❌ Everything at once (arrangement + vocal + lyrics) → generic. Use "Instrumental First".
</lyria_basics>

═══════════════════════════════════════════════════════════════════
§5. PHOTO/VIDEO → MUSIC
═══════════════════════════════════════════════════════════════════

<multimodal>
PHOTO: [photo] + "Compose a [genre] track matching this photo. [Mood], [tempo]."
VIDEO: [video] + "Create a soundtrack for this video. Match energy and pacing."
Podcasts (Pro): "Start soft under voiceover, grow after 60 seconds"

Visual → Audio: Night→dark/ambient, Neon→synthwave, Nature→folk, Rain→melancholic
</multimodal>

═══════════════════════════════════════════════════════════════════
§6. OUTPUT FORMAT
═══════════════════════════════════════════════════════════════════

<o>
─── CLIP ───
🔵 GEMINI CLIP: [Title] — Prompt (→ copy) + Iterations

─── PRO ───
🔵 GEMINI PRO: [Title] — Prompt with time-based Structure + Lyrics: + Iterations
🔗 → Suno: "transfer suno" | → ProducerAI: up to 5 min

─── SUNO ADAPTATION ───
Remove: MAX MODE, EXCLUDE, sliders, eq/compression tags
Keep: genre, mood, instruments, vocals, atmosphere
Add: "Create a [X]-minute...", time-based Structure, Lyrics: with tags
</o>

═══════════════════════════════════════════════════════════════════
§7. TRANSFER STRATEGY (v1.1)
═══════════════════════════════════════════════════════════════════

<transfer>
STAY IN GEMINI: track up to 3 min, standard structure, fast result, photo/video
PRODUCERAI: up to ~5 min, editing, free access to long tracks
TRANSFER TO SUNO: >5 min, Voices, Custom Models, Studio 1.1, JSON, sliders, 44.1kHz

"transfer suno" → Gemini narrative → Suno GMIV+P + tags + MAX MODE + EXCLUDE + Sliders
</transfer>

═══════════════════════════════════════════════════════════════════
§8. EXAMPLES (7 prompts)
═══════════════════════════════════════════════════════════════════

<examples>
1. YouTube Intro (Clip): cinematic hybrid orchestral+electronic, 30s, build→hit→groove
2. Lo-fi Loop (Clip): chill lo-fi hip hop, loop-friendly, no vocals, vinyl crackle
3. Pop Song (Pro 3 min): modern pop, female vocals, time-based structure, Lyrics:
4. RPG Boss Fight (Pro 3 min): orchestral, time-based 4 phases, choir non-lexical
5. Synthwave from Photo (Clip/Pro): neon city rain photo + synthwave instrumental
6. Vocal Ballad (Pro 3 min): acoustic pop, male vocals, Lyrics: with tags
7. Remix/Iteration: "make it slower, replace drums, add strings in chorus"
</examples>

§9. LYRIA REALTIME API — WebSocket streaming for developers. 44.1kHz stereo.

// ═══════════════════════════════════════════════════════════════
// END OF 06_GEMINI.md · SunoForge v1.1
// Next file: 07_TROUBLESHOOT.md
// ═══════════════════════════════════════════════════════════════
