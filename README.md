# 🎧 SunoForge v1.1 — AI Music Prompt Orchestrator

> **Multi-platform AI producer and prompt engineer for music generation.**
> Suno AI (v4.5-all / v4.5+ / v5 / v5.5) + Google Gemini Lyria 3.

---

## What is SunoForge?

SunoForge is a structured **meta-prompt system** — a set of 10 interconnected instruction files that turn any compatible AI assistant (Gemini, Claude, GPT, Grok) into a professional music prompt engineer.

Instead of typing "make a sad song," you get:

- A **ready-to-paste Style block** for Suno AI
- A **Lyrics block** with proper meta-tags and structure
- An **EXCLUDE list** to prevent unwanted elements
- **Slider recommendations** (Weirdness / Style Influence)
- A **Gemini Lyria 3 narrative prompt** in parallel (Dual Mode)

SunoForge generates **2–3 creative variants** per request — different genres, eras, and approaches — so you choose, not guess.

---

## Key Features

| Feature | Description |
|---|---|
| **GMIV+P Formula** | Genre + Mood + Instruments + Vocals + Production — the core style construction method |
| **Time & Place Rule** | "Rock" → "mid-90s Seattle grunge". Era + location = precise sound |
| **Dual Mode** | One idea → Suno prompt + Gemini Lyria 3 prompt simultaneously |
| **Clone Mode** | Extract "sonic DNA" from an artist or audio file (Copyright Safe) |
| **Hybrid Lab** | Blend two genres via bridge genre theory; anti-pair conflict detection |
| **Persona Workshop** | Vocal micro-biographies instead of "sad female vocal" |
| **MAX MODE** | Semantic conditioning for maximum audio quality on free v4.5-all |
| **Pipe Stacking** | `[Section | era | tone | mix | quirk]` — multi-modifier tag syntax |
| **Audit Mode** | 10-point diagnostic + automatic prompt correction |
| **v5.5 Support** | Voices, Custom Models, My Taste — full coverage of the newest Suno version |
| **Lyria 3 Pro** | Time-based structure, 3-min tracks, ProducerAI integration |

---

## File Structure

```
SunoForge_v1.1/
├── 00_CORE.md           Entry point · Preloader · Menu · Identity · Routing
├── 01_ROUTER.md         5-phase pipeline: Intent → Platform → Depth → Modules → Variants
├── 02_STYLE_ENGINE.md   GMIV+P · Time&Place · Personas · Hybrids · Atmosphere
├── 03_LYRICS_ENGINE.md  Tags · Performance Notation · Pipe Stacking · Chords
├── 04_AUDIO_VOCAB.md    Timbre · Dynamics · Groove · Spatial · Theory→Tag mapping
├── 05_SUNO.md           Suno adapter · MAX MODE · Sliders · EXCLUDE · Clean Block
├── 06_GEMINI.md         Gemini adapter · Lyria 3 Clip/Pro · Photo/Video · Transfer
├── 07_TROUBLESHOOT.md   Fixes · Hallucination types · Anti-Pairs · Session health
├── 08_POSTPROD.md       Mastering chain · Stems · DAW tools · Transfer workflows
└── 09_TEMPLATES.md      Genre recipes · Quick recipes · Presets · Style Library
```

Each file is an **autonomous module** with a clear responsibility. The Router (01) determines which modules to load for each request.

---

## How to Use

### Step 1 — Choose your host AI
SunoForge works as a system prompt (or uploaded file set) in:
- **Google Gemini** (recommended — native multimodal, photo/video → music)
- **Claude** (Anthropic)
- **ChatGPT / GPT-4**
- **Grok**

### Step 2 — Load the files
**Option A — Full system prompt:**
Paste the contents of all 10 files into your AI's system prompt / custom instructions.

**Option B — File upload (Gemini / Claude):**
Upload all `.md` files and instruct the AI to treat them as operating instructions.

**Option C — Single session:**
Paste `00_CORE.md` first, then load other files as needed per request.

### Step 3 — Set your version in the Preloader
At the top of `00_CORE.md`, edit the `<preloader>` block:

```
SUNO_VERSION     = "v4.5-all"   // or v5 / v5.5
TARGET_PLATFORM  = "auto"        // auto | suno | gemini | dual
OUTPUT_LANG      = "en"
VARIANT_COUNT    = 2
```

Or use runtime commands at any time:
```
/set suno v5.5
/set platform dual
/set variants 3
/set lang en
```

### Step 4 — Start
```
start
```
→ Shows the full menu with all 10 modules.

Or just describe your idea in plain language — the system finds the route automatically.

---

## Quick Examples

**Free-form request:**
> "I need a dark lo-fi track about insomnia, no vocals"

→ System detects: lo-fi hip-hop, dark mood, instrumental, Suno v4.5-all
→ Outputs 2 variants: Style + Lyrics + EXCLUDE + Sliders, copy-paste ready

---

**Clone mode:**
> "Make something that sounds like early Radiohead"

→ Extracts sonic DNA: late-90s Oxford art-rock, atmospheric guitars, falsetto male vocal, spacious production
→ 2 variants: faithful clone + creative reinterpretation (Copyright Safe)

---

**Dual mode:**
> /dual
> "Epic orchestral track for a fantasy game boss fight"

→ Outputs:
> 🟠 **Suno v4.5-all** — Style + Lyrics + EXCLUDE + Sliders
> 🔵 **Gemini Lyria 3 Pro** — Narrative prompt with time-based structure

---

**Audit mode:**
> [paste your broken prompt here]

→ 10-point diagnostic report + corrected prompt in Clean Block format

---

## Output Format (Clean Block Protocol)

Every Suno output follows this structure:

```
🎹 SONIC BLUEPRINT: [Title]
Target: Suno v4.5-all | Weirdness: 45% | Style Influence: 80%

1. Style (→ paste into "Style of Music"):
[Is_MAX_MODE: MAX] [QUALITY: MAX] mid-90s Seattle grunge, ...

2. Lyrics (→ paste into "Lyrics"):
///*****///
[Intro | distorted guitar | slow build]
...

3. EXCLUDE:
synth pop, smooth jazz, gentle, lo-fi, whisper vocals, acoustic, mellow
```

---

## Critical Rules (Quick Reference)

| Rule | Detail |
|---|---|
| **Front-load** | First 20–30 words of Style = maximum model weight |
| **Max 2 genres** | More = conflicts. Main genre first. |
| **() = sung** | Parentheses = backing vocal. Never put instructions in `()`. |
| **[] = instruction** | Square brackets = structural/production commands. Never sung. |
| **Pipe max 4–6** | `[Section \| era \| tone \| mix]` — more = noise |
| **EXCLUDE always** | 8–12 items. Opposite of the target style. |
| **Tags = hints** | Not guarantees. Generate 3–4 versions, pick the best. |
| **Time & Place** | "Metal" → "1980s LA Sunset Strip metal" |
| **v5.5 needs long prompts** | 100–200 focused words work better than 10–20 keywords |

---

## Version Matrix

| Version | Free | Quality | Key Exclusive Features |
|---|---|---|---|
| v4.5-all | ✅ | Good | All meta-tags, MAX MODE, Pipe Stacking, Sliders |
| v4.5+ | ❌ | Better | Improved tag adherence, better vocals |
| v5 | ❌ | Studio | JSON Structuring, Persona Tags, 44.1kHz, Studio 1.1 |
| v5.5 | ❌ | Best | Voices (own voice), Custom Models, My Taste |
| Lyria 3 Clip | ✅* | Good | 30-sec tracks, photo/video input |
| Lyria 3 Pro | ❌ | Studio | 3-min tracks, time-based structure, ProducerAI |

*Free with limits in Gemini App

---

## Platform Comparison

| Need | Platform |
|---|---|
| Full creative control, long tracks (5+ min) | Suno v5 / v5.5 |
| Your own voice in the track | Suno v5.5 Voices |
| Quick 30-sec sketch or loop | Gemini Lyria 3 Clip |
| Complete 3-min song with structure | Gemini Lyria 3 Pro |
| Photo / video → music | Gemini (native multimodal) |
| Both platforms simultaneously | SunoForge Dual Mode |

---

## Genre Recipes Available

`09_TEMPLATES.md` contains ready-to-use full configurations for:

EDM / Festival Banger · Pop / Radio Hit · Trap / Hip-Hop · Pop Punk / Alt Rock · Country · Cinematic / Ambient · Hard Rock / Metal · Lo-fi Hip-Hop / Chill · Gospel · Duet (Stable Format)

Plus 25+ genre presets with BPM, Key, and Slider recommendations.

---

## Changelog

### v1.1 (March 2026)
- **Suno v5.5 support:** Voices, Custom Models, My Taste, Magic Wand
- **Lyria 3 Pro support:** 3-min tracks, time-based structure, Lyrics tags
- **ProducerAI integration:** up to ~5 min in Gemini (free)
- **v5.5 prompting guidance:** long prompts (100–200 words) work better
- **Dynamic instructions for v5.5:** `[Solo: 12s swell]`, `"modulate after 16 bars"`
- **New Router keywords:** voices, custom model, lyria pro, my taste, magic wand
- **Updated Transfer Strategy:** three-level pipeline (Clip → Pro → Suno)
- **New Quick Recipes:** Voices track, Custom Model track, RPG Boss Fight, 3-min pop

### v1.0
- Initial release: 10-file modular architecture
- Dual platform support: Suno AI + Gemini Lyria 3
- GMIV+P formula, Time & Place rule, Persona Workshop
- Clean Block Protocol, Pipe Stacking, MAX MODE
- Hybrid Lab with Fusion Pairs and Anti-Pairs
- Genre Recipe Library, Style Library System

---

## Heritage

SunoForge v1.1 is an evolution of **Suno AI Architect v2.0 (Polymath Edition)**.

Core principle:
> *You don't write text. You design sound.*
> *Every prompt is a blueprint: era, place, timbre, groove, space, emotion.*

---

## License

This meta-prompt system is released for personal and commercial use.
Attribution appreciated but not required.

---

*SunoForge v1.1 · March 2026*
