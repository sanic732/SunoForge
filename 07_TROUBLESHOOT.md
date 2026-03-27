# 🔧 SUNOFORGE v1.1 — TROUBLESHOOT
# File 07 of 10 · Fixes · Diagnostics · Artifacts · Anti-Pairs

═══════════════════════════════════════════════════════════════════
§1. DIAGNOSTIC PROTOCOL
═══════════════════════════════════════════════════════════════════

<diagnostic>
// When the user pastes their prompt for audit.
// Or describes a problem with generation.

─── CHECKLIST (check in order) ───

CHECK 1 — FRONT-LOADING:
  Do the first 20–30 words of Style contain genre + mood + key instrument?
  ❌ FIX: Move important content to the beginning.

CHECK 2 — GENRE OVERLOAD:
  More than 2 genres in Style?
  ❌ FIX: Keep 1 main + 1 sub-genre maximum.

CHECK 3 — INSTRUMENT OVERLOAD:
  More than 4 instruments?
  ❌ FIX: Reduce to 3–4 with specific descriptors.

CHECK 4 — MOOD CONFLICT:
  Contradictory moods ("happy dark aggressive peaceful")?
  ❌ FIX: Keep 1–2 compatible ones.

CHECK 5 — () vs [] VIOLATION:
  Instructions inside round brackets ()?
  ❌ FIX: Move to square brackets []. () = backing vocal.

CHECK 6 — PIPE OVERLOAD:
  More than 6 modifiers in one pipe stack?
  ❌ FIX: Reduce to 4–6. Break into producer-level categories.

CHECK 7 — ANTI-PAIR:
  Genre combination from the Anti-Pairs list?
  ❌ FIX: Suggest a bridge genre or replace one of the genres.

CHECK 8 — BPM/KEY IN LYRICS:
  Technical parameters (BPM, Key) in the Lyrics field instead of Style?
  ❌ FIX: Move to Style.

CHECK 9 — NEGATIVE VOCAL:
  "No male vocals" or similar gender exclusions?
  ❌ FIX: Replace with positive "Solo female vocalist, [type]" at the start of Style.

CHECK 10 — TRIGGER WORDS:
  Artifact trigger words ("artifact", "glitches", "clipping")?
  ❌ FIX: Replace with positive ones ("clean tone", "balanced dynamics").

─── OUTPUT FORMAT ───
Diagnostics:
  ✅ Check 1: OK — genre at the start
  ❌ Check 5: () violation — "(play guitar)" on line 12
  ❌ Check 9: "no male vocals" in Style
  ...

Corrected version:
  [Full corrected prompt in Clean Block format]
</diagnostic>

═══════════════════════════════════════════════════════════════════
§2. HALLUCINATION TYPES & FIXES
═══════════════════════════════════════════════════════════════════

<hallucinations>

─── TYPE 1: LYRIC HALLUCINATIONS ───
Symptoms: Nonsense, mispronunciation, dropped words.
Cause:    Mismatch in Suno's internal lyrics file system.
          When Suno skips a line — all subsequent alignment breaks.

FIX:
  1. After generation, manually check ALL text against what was sung
  2. Check for dropped words and fallen line endings
  3. Fix the lyrics file
  4. Use Replace Section with corrected text

─── TYPE 2: CONVERSATIONAL HALLUCINATIONS ───
Symptoms: AI adds unexpected dialogue or spoken word.
Cause:    Largely fixed in v4.5.

FIX:
  - "no choir, no spoken words, no dialogue" in Style (for clean vocals)
  - Avoid incomplete instructions like [Play guitar] — model may SING it
  - Use correct tags: [Verse] instead of [Verse breakdown]

─── TYPE 3: NONSENSE IN LONG SESSIONS ───
Symptoms: Quality degradation, nonsensical text after extended work.
Cause:    Server state accumulation.

FIX:
  1. Copy prompt + edits to notepad
  2. Full page refresh in Suno
  3. Paste back
  4. Regenerate

─── TYPE 4: AUDIO HALLUCINATIONS ───
Symptoms: Sudden loud vocals, screaming, dramatic genre shift at the end.
Cause:    Model predicts a "climactic ending" from training data.
          Long extensions (3rd+) reduce coherence.
          High Weirdness (>70%) with Extend.

FIX:
  - Avoid 3rd+ Extend — regenerate fully instead
  - Weirdness for Extend: 45–55% (lower than for base)
  - Specify mood: "continue quietly, no drums, minimal energy"
  - [Outro: Fade out] or [Outro: Big finish] — explicitly set ending

─── TYPE 5: VOCAL HALLUCINATIONS IN INSTRUMENTALS ───
Symptoms: Vocals appear in an instrumental track.
Cause:    Single protection is insufficient.

FIX: Triple protection:
  1. Instrumental toggle in UI
  2. [Instrumental] tag in Lyrics
  3. "instrumental only, no vocals" in Style
</hallucinations>

═══════════════════════════════════════════════════════════════════
§3. TRIGGER WORDS (Avoid in Style)
═══════════════════════════════════════════════════════════════════

<trigger_words>

TRIGGER WORD           │ EFFECT                    │ REPLACEMENT
───────────────────────┼───────────────────────────┼──────────────────
"artifact"             │ Increases artifacts        │ "clean tone"
"glitches"             │ Audio stuttering           │ "smooth playback"
"clipping audio"       │ Loud distortion            │ "balanced dynamics"
"background noise"     │ Increases hissing          │ "clean background"
"shimmer" (in context  │ Can cause metallic         │ "bright presence"
 of exclusion)         │ effect                     │
"hiss"                 │ Amplifies hissing          │ "warm tone"

PRINCIPLE: Naming the problem makes the model "imagine" it and amplify it.
ALWAYS: Use positive framing instead of describing problems.

❌ "no clipping, no distortion, no noise"
✅ "balanced dynamics, clean tone, consistent volume, warm sound, smooth frequency response"
</trigger_words>

═══════════════════════════════════════════════════════════════════
§4. ANTI-PAIRS (Genre Conflicts)
═══════════════════════════════════════════════════════════════════

<anti_pairs>
// Genre combinations with low co-existence weight.
// Blending gives unpredictable or incoherent results.

❌ AVOID:
  Cinematic + Dark        (weight: 10 — near zero)
  Opera + Melodic         (weight: 16 — interpretation conflict)
  Drum and Bass + Funk    (weight: 7 — extremely low)
  Country + Death Metal   (subculture conflict)
  Gospel + Industrial     (emotional core conflict)
  Classical + Trap        (aesthetic conflict)
  Ambient + Hardcore      (energy conflict)

IF user requests Anti-Pair:
  → "⚠️ These genres conflict (low co-existence weight).
     The result may be unpredictable."
  → Suggest a bridge genre (from 02_STYLE_ENGINE §6)
  → If user insists → generate with Weirdness 65%+, Style Influence 50–60%
</anti_pairs>

═══════════════════════════════════════════════════════════════════
§5. COMMON PROBLEMS & QUICK FIXES
═══════════════════════════════════════════════════════════════════

<quick_fixes>

PROBLEM: "Track sounds generic / boring"
FIX:
  - Apply Time & Place rule: add era + location
  - Replace generic instruments with specific descriptors
  - Add Production Environment ("lo-fi demo tape" instead of default)
  - Increase Weirdness by 10–15%

PROBLEM: "Wrong vocal gender"
FIX:
  - Remove ALL negative gender mentions
  - First words of Style: "Solo [gender] vocalist, [voice type]"
  - Use Persona (biography) instead of a simple descriptor

PROBLEM: "Too many instruments / muddy mix"
FIX:
  - Reduce to 3–4 instruments in Style
  - Remove instruments from Lyrics (keep only in Style)
  - Add "[sparse]" or "[minimal]" to Style

PROBLEM: "Song structure is chaotic"
FIX:
  - Add meta-tags to EVERY section (don't skip)
  - Use structure template from 03_LYRICS_ENGINE §8
  - For long tracks: more explicit energy indicators
    [Verse | low energy] → [Build] → [Chorus | high energy]

PROBLEM: "Meta-tags are ignored"
FIX:
  - Tags = hints, not commands. Normal to ignore 30%+.
  - Simplify tags: remove overly detailed instructions
  - Combine: semantic (mood, energy) + simple structural
  - Generate 3–4 versions — tags will work better in at least one

PROBLEM: "Shimmer effect"
FIX:
  - v4.5+ significantly reduces shimmer (mostly a v4 bug)
  - If it persists: export stems + low-pass filter in DAW
  - Reduce Weirdness to 40–50%
  - Regenerate with Persona (blocking vocal identity reduces shimmer)

PROBLEM: "Gemini generates a too-generic track"
FIX:
  - More detailed prompt: add instruments, vocals, dynamics
  - Add Time & Place: "90s skate punk" instead of "rock"
  - Upload a photo for context
  - Iterate: "make it more aggressive, add distorted guitars"

PROBLEM: "v5.5 prompt doesn't work / strange result" (NEW v1.1)
FIX:
  - v5/v5.5 REQUIRES long prompts (100–200 words)
  - Old short v3/v4 prompts → clipped tracks
  - Rewrite Style as a technical brief for a sound engineer
  - Use Magic Wand (My Taste) as a starting point

PROBLEM: "Voices doesn't sound like me" (NEW v1.1)
FIX:
  - Upload a longer sample (closer to 4 min)
  - Record in a quiet room (musical background is OK, but clean voice is better)
  - Redo verification

PROBLEM: "Custom Model doesn't give the right sound" (NEW v1.1)
FIX:
  - Upload more tracks (6 = minimum, 10+ = better)
  - Make sure tracks are stylistically consistent
  - Don't mix different genres in one model
  - Create separate models for different styles

PROBLEM: "Lyria 3 Pro track is generic / boring" (NEW v1.1)
FIX:
  - Use time-based structure: "intro (0-15s), verse (15-45s)..."
  - Describe dynamics: "stripped-down → building → massive chorus"
  - Lifehack: instrumental first, then vocals as a separate request
  - Add Time & Place rule (works for Lyria too)

PROBLEM: "Lyria 3 Pro ignores structure" (NEW v1.1)
FIX:
  - Break structure down by time explicitly (seconds)
  - Each block = a separate sentence
  - Don't overload one block with details
  - Try via ProducerAI (better control)

PROBLEM: "I want a track longer than 3 min in Gemini" (NEW v1.1)
FIX:
  - ProducerAI: up to ~5 min with Lyria 3 Pro
  - Transfer to Suno: extend to 5+ min with Extend
  - Or: generate two 3-min segments and stitch in DAW
</quick_fixes>

═══════════════════════════════════════════════════════════════════
§6. SUNO SESSION HEALTH
═══════════════════════════════════════════════════════════════════

<session_health>
// Signs that a Suno session is "tired":

SYMPTOMS:
  - Lyrics start to "drift"
  - Quality drops with each generation
  - Meta-tags are ignored more frequently
  - Nonsense appears

PREVENTION:
  - Refresh the page every 10–15 generations
  - Store prompts in a separate notepad (don't rely on history)
  - Use Suno Bookmarks for successful styles
  - Short sessions (30–40 min) are more effective than marathons

RECOVERY:
  1. Copy everything to notepad
  2. Full page refresh
  3. Paste back
  4. Regenerate
</session_health>

// ═══════════════════════════════════════════════════════════════
// END OF 07_TROUBLESHOOT.md · SunoForge v1.1
// Next file: 08_POSTPROD.md
// ═══════════════════════════════════════════════════════════════
