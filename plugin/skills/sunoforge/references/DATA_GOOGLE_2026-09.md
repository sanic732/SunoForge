<sunoforge_file id="DATA_GOOGLE" version="4.0" layer="data" role="adapter" source="DATA_GOOGLE_2026-09.md">
<file_meta>
file_id: DATA_GOOGLE
version: "4.0"
layer: data
role: adapter
description: >
  Everything about Google's music models as of 2026-09-30: Lyria 3.5, Lyria 3 Clip and
  Lyria RealTime, where each is reachable (Gemini app, Gemini API, AI Studio, Vids, Flow
  Music), Google's official prompt guide (genre first, BPM and key as numbers, section
  tags, Lyrics: header, timestamp ranges), vocals, image input, Flow Music, RealTime
  steering and worked examples. Read for any Google target.
valid_as_of: "2026-09-30"
expires: "Google replaced Lyria 3 Pro with Lyria 3.5 within two months and rewrote its prompt guide on 2026-09-17 — verify everything here after 2026-12"
scope: lyria_3_5 · lyria_clip · lyria_realtime · gemini_app · gemini_api · flow_music · prompt_guide · timestamps · vocals · multimodal
key_concepts: [lyria_3_5, lyria_3_clip, lyria_3_pro_retiring, lyria_realtime, gemini_app_music, interactions_api, prompt_guide_2026_09, genre_first, bpm_and_key, section_tags, timestamp_ranges, lyrics_header, parentheses_backing_vocals, vocal_profiles, image_input, synthid, flow_music, weighted_prompts, musicfx_retired]
depends_on: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE, DATA_OTHER, DATA_POSTPROD, DATA_LEGAL]
rag_priority: critical
authority: "THIS FILE IS THE SINGLE SOURCE OF TRUTH FOR LYRIA AND FLOW MUSIC SPECIFICATIONS"
updated: "2026-09-30"
</file_meta>

# 🔵 SUNOFORGE v4.0 — GOOGLE PLATFORM DATA
# File 7 of 12 · DATA layer · valid as of 2026-09-30

> ⚠️ **Expiry notice.** This is a snapshot. In the fourteen months before this date
> Google acquired a music company, renamed its product twice, retired two products,
> replaced its flagship music model and rewrote its prompt guide. If today is more
> than a quarter past the date above, treat every number here as a starting
> hypothesis. Replace this file; leave the CORE_* files alone.

> 📌 **Single source rule.** Lyria model identifiers, durations, sample rates and
> Flow Music mechanics live here and nowhere else.

> 📖 **Primary source.** Google publishes an actual prompt guide for Lyria — the
> current edition is dated 2026-09-17 [OFFICIAL]. Where this file says [OFFICIAL]
> about technique, that guide or the Gemini API music page is why. It outranks any
> community guide, including earlier editions of this system.

> 💲 **No prices.** Access differs by country, plan and billing setup. This file says
> what needs a paid or billed account, never how much it costs.

<section id="§1" title="THE LYRIA FAMILY">

<!-- rag_anchor: lyria_3_5_specs -->
<rag_zone id="lyria_3_5">

─── LYRIA 3.5 ─── [OFFICIAL]
  Released     2026-07-29 in Flow Music · 2026-09-04 in the Gemini app, Gemini API,
               Google AI Studio and Google Vids
  Identifier   `lyria-3.5` (Gemini API, Interactions API — `interactions.create`)
  Length       "A couple of minutes (controllable using prompt)" in the API;
               "up to 3 minutes" in the Gemini app
  Audio out    44.1 kHz stereo · MP3 by default · WAV on request (`response_format`)
  Input        text, and up to 10 images alongside it
  Output       audio plus the lyrics it sang, as separate blocks
  Status       the model ID carries no "preview" suffix; the docs page states no
               status. Third parties call it a preview [COMMUNITY].

  WHAT GOOGLE SAYS IS NEW: "Improved musicality… richer, more complex melodic
  structures"; "Enhanced lyrics… improved prompt adherence and structural
  awareness"; "Improved vocals… more expression and emotion… improved
  pronunciation"; "Creative control: More easily control the tempo and duration of
  your outputs."

  HOW IT THINKS [OFFICIAL]: "the model reasons through musical structure (intro,
  verse, chorus, bridge, etc.) based on your prompt. This happens before the audio is
  generated." It "uses a prompt rewriter internally" and does not show that step.

  LIMITS [OFFICIAL]:
  - prompts asking for "specific artist voices or the generation of copyrighted
    lyrics" are blocked
  - SynthID watermark on all audio
  - "Music generation is a single-turn process" — no conversational editing of a
    generated track
  - the same prompt gives different results

</rag_zone>

<!-- rag_anchor: lyria_clip_pro_realtime -->
<rag_zone id="lyria_other_models">

─── LYRIA 3 CLIP ─── [OFFICIAL]
  Identifier   `lyria-3-clip-preview`
  Length       always 30 seconds
  Audio out    MP3 · 44.1 kHz stereo
  Use          "Short clips, loops, previews". Google: "Iterate with Clip first" —
               test the prompt cheaply, then render the full song on 3.5.
  ⚠️ Earlier editions said Clip outputs 48 kHz. Current docs: both models produce
  44.1 kHz.
  ⚠️ NAMING: Google's older guide called this model plain "Lyria 3". When a user
  says "Lyria 3" they may mean Clip, the retiring Pro, or the family — ask.

─── LYRIA 3 PRO ─── retiring
  `lyria-3-pro-preview` (released 2026-03-25, 184 seconds) is gone from the API's
  model table; Lyria 3.5 is its successor. It still appears on the pricing page and
  at some resellers. Shutdown date not published [OFFICIAL + COMMUNITY]. Prompts
  written for it carry over (§3, §4).

─── LYRIA REALTIME ─── [OFFICIAL] experimental
  Identifier   `models/lyria-realtime-exp`, over a WebSocket session
  Audio        raw 16-bit PCM, 48 kHz, stereo
  Instrumental only — "VOCALIZATION" mode adds voice-like sounds as another
               instrument, never words
  WHAT IT IS: an instrument, not a track generator. An endless stream you steer
  while it plays. Steering: §8.
  Magenta RealTime remains Google's open counterpart.

### ENTERPRISE
  Vertex AI / Gemini Enterprise Agent Platform still document the older `lyria-002`
  endpoint (instrumental, with `negative_prompt` and `seed`) [OFFICIAL]. Lyria 3.5 on
  Vertex: not found. Dream Track in YouTube Shorts: no 3.5 information.

</rag_zone>

</section>

<section id="§2" title="SURFACES — where Lyria is reachable">

<!-- rag_anchor: lyria_surfaces_access -->
<rag_zone id="surfaces">

| Surface | Model | What you control | Access |
|---|---|---|---|
| Gemini app (web, mobile) | Lyria 3.5 | genre menu, vocals or instrumental, short or longer track (up to 3 min), templates, a photo as input; Nano Banana cover art | "available to all users globally"; 18+; "Restrictions apply" [OFFICIAL] |
| Gemini API / AI Studio | 3.5, 3 Clip, RealTime | full prompt, up to 10 images, MP3 or WAV | a billed API project — no free API tier for Lyria [OFFICIAL] |
| Google Flow Music | Lyria models | generate, extend, cover, replace, stems, images, video (§7) | Free plan and paid plans [OFFICIAL] |
| Google Vids | Lyria 3.5 | soundtrack inside the video editor | Workspace |

  Country availability: "AI-powered music generation is available in all countries
  where the Gemini App is available" [OFFICIAL]. Per-plan music quotas in the app are
  not published.

  WHAT THIS MEANS IN PRACTICE: the same model sits behind different controls. The app
  hides most of the prompt behind menus; the API takes everything in §3–§5 verbatim.
  A prompt tuned in the API may need trimming for the app, and vice versa.

</rag_zone>

</section>

<section id="§3" title="PROMPTING LYRIA 3.5 — Google's guide, 2026-09-17">

<!-- rag_anchor: lyria_prompt_fundamentals -->
<rag_zone id="google_framework">

[OFFICIAL] "Both short and detailed prompts produce strong results."
  Short:  "A folk song about cute cats avoiding puddles, female vocals, acoustic
           guitar, sound of rain"
  Detailed: "A 1980s-style synth-pop track with a driving beat, shimmering
           synthesizers, and a catchy, anthemic chorus… Upbeat tempo around 120 BPM,
           clear verse-chorus structure, and a memorable instrumental hook. The
           lyrics describe getting ready for a party."

THE ORDER THIS SYSTEM USES (from the guide's sections and its best practices):
```
[Genre + era] → [Instruments and texture] → [Tempo in BPM + key] → [Mood]
→ [Vocal profile + language] → [Structure] → [Lyrics]
```
  GENRE      "Lead your prompt with the primary genre." Hybrids welcome ("A fusion of
             metal and hip-hop"). Name an era or regional variant ("Early 1990s
             boom-bap hip-hop", "1960s French yé-yé pop").
  INSTRUMENTS Lyria picks genre-typical instruments by itself; "If you want specific
             instruments or unusual combinations, declare them explicitly", and say
             how they sound together ("A distorted 303 bassline cutting through crisp,
             tight hi-hats").
  TEMPO, KEY "Set the tempo directly (e.g. 120 BPM, slow tempo around 72 BPM, fast
             160 BPM)"; "Specify the root key and tonality (e.g. in G major, in D
             minor, in C pentatonic)".
  MOOD       Google's list: Ambient, Bright, Chill, Dark, Dreamy, Emotional, Ethereal,
             Euphoric, Funky, Groovy, Melancholic, Nostalgic, Ominous, Psychedelic,
             Relaxed, Soulful, Triumphant, Upbeat, Whimsical.
  VOCALS, LYRICS, STRUCTURE — §4 and §5.

BEST PRACTICES [OFFICIAL]: iterate on Clip first · be specific — "Mention instruments,
BPM, key, mood, and structure" · prompt in the language the lyrics should be in · use
section tags · separate your lyrics from your musical directions.

⚠️ WHAT CHANGED: editions up to v3.0 taught "tempo in words, never a number" for
Lyria, from the Lyria 3 Pro guide. The current guide asks for numbers. Descriptive
tempo still works as extra colour ("a slow, swaying pace at 72 BPM").

</rag_zone>

<!-- rag_anchor: lyria_keyword_lists -->
<rag_zone id="lyria_keywords">

GENRE KEYWORDS Google lists for Lyria 3.5 and RealTime [OFFICIAL]:
  Electronic & Dance  Acid House, Breakbeat, Chillout, Chiptune, Deep House, Drum &
                      Bass, Dubstep, EDM, Electro Swing, Glitch Hop, Hyperpop, Minimal
                      Techno, Moombahton, Psytrance, Synthpop, Techno, Trance, Trip
                      Hop, Vaporwave
  Hip-Hop & R&B       808 Hip Hop, Boom-Bap, Contemporary R&B, G-funk, Grime, Lo-Fi Hip
                      Hop, Neo-Soul, New Jack Swing, Trap Beat
  Rock & Alternative  Alternative Country, Blues Rock, Classic Rock, Funk Metal, Garage
                      Rock, Indie Folk, Indie Pop, Post-Punk, 60s Psychedelic Rock,
                      Shoegaze, Surf Rock
  Jazz, Soul & Funk   Acid Jazz, Afrobeat, Bossa Nova, Disco Funk, Funk, Jazz Fusion,
                      Latin Jazz
  Folk & Traditional  Bengal Baul, Bhangra, Bluegrass, Celtic Folk, Cumbia, Indian
                      Classical, Irish Folk, Merengue, Polka, Reggae, Reggaeton,
                      Renaissance Music, Salsa
  Classical & Acoustic Baroque, Orchestral Score, Piano Ballad

INSTRUMENT KEYWORDS [OFFICIAL]:
  Keyboards & Synths  Buchla Synths, Clavichord, Dirty Synths, Harpsichord, Mellotron,
                      Moog Oscillations, Ragtime Piano, Rhodes Piano, Smooth Pianos,
                      Spacey Synths, Synth Pads
  Bass & Drums        303 Acid Bass, 808 Hip Hop Beat, Boomy Bass, Conga Drums,
                      Drumline, Funk Drums, Precision Bass, Tabla, TR-909 Drum Machine
  Guitars & Strings   Banjo, Balalaika, Bouzouki, Cello, Charango, Dulcimer, Fiddle,
                      Flamenco Guitar, Guitar, Harp, Koto, Lyre, Mandolin, Pipa,
                      Shamisen, Shredding Guitar, Sitar, Slide Guitar, Viola Ensemble,
                      Warm Acoustic Guitar
  Wind & Brass        Alto Saxophone, Bagpipes, Bass Clarinet, Didgeridoo, Harmonica,
                      Ocarina, Trumpet, Tuba, Woodwinds
  Percussion          Bongos, Djembe, Glockenspiel, Hang Drum, Kalimba, Maracas,
                      Marimba, Mbira, Steel Drum, Vibraphone

These are the terms the vendor says the model recognizes. The fuller descriptor
dictionary for all platforms: DATA_VOCAB.

</rag_zone>

<!-- rag_anchor: lyria_what_not_to_send -->
<rag_zone id="lyria_limits_prompting">

WHAT LYRIA DOES NOT TAKE:
  NEGATIVE PROMPTS — the documented Lyria 3.5 call has no negative-prompt field
    [COMMUNITY: reviewers of the API]. Google's own instrumental example is
    "Instrumental only, no vocals." — a positive statement followed by one short
    exclusion. Use that shape; an exclude LIST has nowhere to go.
  REAL ARTIST NAMES and COPYRIGHTED LYRICS — blocked by the safety filter [OFFICIAL].
    Describe era, scene and vocal traits instead (CORE_01 §12).
  SUNO-ONLY CONVENTIONS — Exclude Styles lists, slider values, Variety, Max Mode,
    performance symbols like ~ and CAPS stretching. Section tags carry over (§4),
    and so do parentheses for backing vocals (§5).

</rag_zone>

</section>

<section id="§4" title="STRUCTURE AND TIMING">

<!-- rag_anchor: lyria_section_tags -->
<rag_zone id="lyria_structure_tags">

[OFFICIAL] "For Lyria 3.5, define song progression using tags or arrows":

```
[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Bridge] -> [Outro]
```

or in prose: "Start with a quiet piano intro, build into an energetic verse, pause for
a moment of silence, then explode into the chorus."

DYNAMICS AND TRANSITIONS [OFFICIAL]:
  - Build tension through the pre-chorus, then drop to silence before an explosive
    chorus
  - Gradual crescendo throughout the song, adding one instrument per section
  - A sudden stop after the bridge, followed by an a cappella chorus

TIMING IN PROSE [OFFICIAL]:
  - Build to a beat drop at 12 seconds
  - Vocal sample repeats every 4 bars
  - The chorus kicks in at 22 seconds

LENGTH [OFFICIAL]: "specifying it in your prompt (e.g., "create a 2-minute song") or
by using timestamps to define the structure." No separate duration parameter.

</rag_zone>

<!-- rag_anchor: lyria_timestamp_ranges -->
<rag_zone id="timestamp_prompting">

TIMESTAMP RANGES [OFFICIAL — the format in the current API docs]:

```
[0:00 - 0:10] Intro: Begin with a soft lo-fi beat and muffled vinyl crackle.
[0:10 - 0:30] Verse 1: Add a warm Fender Rhodes piano melody and gentle vocals
              singing about a rainy morning.
[0:30 - 0:50] Chorus: Full band with upbeat drums and soaring synth leads. The lyrics
              are hopeful and uplifting.
[0:50 - 1:00] Outro: Fade out with the piano melody alone.
```

"This is useful for controlling when instruments enter, when lyrics are delivered,
and how the song progresses."

HOW TO WRITE THEM WELL:
  - Range, then the section name, then what happens — in that order
  - Ranges touch end to start: no gaps, no overlaps
  - One main event per range; a range a few seconds long cannot hold much change
  - The final range describes the ending, or the model picks its own
  - Stay inside the model's length: "a couple of minutes" for 3.5 in the API — steerable
    in the prompt, the maximum not published — three in
    the app, thirty seconds for Clip. A map that runs to [4:00] describes music the
    model will not produce; the generation ends and the designed ending never
    arrives. Say the ceiling out loud and offer the choice: compress the map, or move
    to a platform that holds the length (Suno v6: 8 min; Stable Audio Medium: 6:20).

OLDER FORMATS:
  `[00:15] event` single-point markers come from the Lyria 3 Pro guide. They are
  not shown for 3.5; convert each to a range ending where the next begins.
  `Intro (0–15s)`, `[Verse - 0:15]`, `[End - 2:15]` were invented by earlier editions
  of this system and were never Google's syntax. Repair: CORE_03 §3 row 9.

SCORING VIDEO — the reason ranges exist:
  Note the cut times in the edit, then start a range on each cut so the music changes
  where the picture does. Google names Veo as the companion model for this.

</rag_zone>

</section>

<section id="§5" title="VOCALS AND LYRICS">

<!-- rag_anchor: lyria_own_lyrics -->
<rag_zone id="lyria_vocals">

Lyria 3.5 "generates vocal tracks with lyrics by default" [OFFICIAL]. Three options:
your own lyrics, lyrics it writes, or an instrumental.

─── YOUR OWN LYRICS ─── [OFFICIAL]
"Include your lyrics directly in the prompt beneath a Lyrics: header. Tag each
section to guide vocal delivery":

```
Lyrics:

[Intro]
Ooooh, yeah

[Verse 1]
Early morning rain on the window pane
City lights wash away the pain

[Chorus]
We keep moving on (moving on)
Until the morning light
```

"Use parentheses for backing vocals, echoes, or ad-libs, like (moving on)."
The API docs also show the form "Create a dreamy indie pop song with the following
lyrics:" followed by tagged sections.

─── LYRICS IT WRITES ─── [OFFICIAL]
"outline the narrative, emotion, or key phrases": "The lyrics describe driving down
the Pacific Coast Highway at sunset. The mood is nostalgic and reflective. Include
an uplifting, anthemic chorus about second chances and starting over."
For dance genres ask for a short repeating hook: "…a repetitive, high-energy vocal
hook: "Feel the rhythm all night long.""

─── LANGUAGE ─── [OFFICIAL]
"Lyria 3.5 generates lyrics in the language of your prompt… The model adapts its
vocal style and pronunciation to match the language." For a song in French, write the
prompt in French; for Ukrainian or Russian, write it in that language. Google claims
improved pronunciation in 3.5; no independent test for Russian or Ukrainian exists.

</rag_zone>

<!-- rag_anchor: lyria_vocal_profiles -->
<rag_zone id="lyria_vocal_profiles">

VOCAL PROFILES — Google's own wording [OFFICIAL]:
  Female Soprano    "Clear, crystalline timbre with an agile, soaring delivery. Bright
                    tone capable of airy, breathy textures."
  Female Alto       "Rich, warm, and husky lower range. Smoky timbre with a soulful,
                    resonant chest voice."
  Male Tenor        "Bright, piercing, and energetic. Youthful timbre with high
                    belting power that cuts through dense mixes."
  Male Baritone     "Deep, velvet-smooth chest voice with a warm, soothing, crooning
                    delivery."
  Weathered Rocker  "Raspy, gritty timbre reminiscent of 1990s alternative rock. Raw
                    emotional intensity with strained upper notes."

NON-LYRICAL VOCAL EFFECTS [OFFICIAL]:
  - A vintage radio broadcast voice introduces the song before the beat kicks in
  - A spoken voice whispers right before the drop, followed by high-energy synths
  - Chopped, pitch-shifted vocal samples looping as an instrumental rhythm element

FROM THE LYRIA 3 PRO GUIDE (April 2026), not repeated for 3.5 — still worth trying
[OFFICIAL for 3 Pro]:
  - A VOCAL ARC — "The vocal starts out confident but gets calmer and quieter as the
    track progresses." Pairs naturally with timestamp ranges.
  - MULTI-VOCAL, MULTILINGUAL — a male voice in English with a female voice in
    French inside one song.
  - BACKING VOCALS by description — "with backing singers echoing the last line of
    each chorus".

INSTRUMENTAL [OFFICIAL]: "Instrumental only, no vocals." in the prompt. In the Gemini
app there is also a Vocals menu with an Instrumental option.

</rag_zone>

</section>

<section id="§6" title="MULTIMODAL INPUT">

<!-- rag_anchor: lyria_image_input -->
<rag_zone id="multimodal">

[OFFICIAL] Lyria 3.5 takes up to 10 images with the text prompt. Google's example:
"An atmospheric ambient track inspired by the mood and colors in this image." The
Gemini app accepts a photo and "analyzes the scene to compose an individual song".

  PDF input was documented for Lyria 3 Pro. It is not mentioned for 3.5 — do not
  promise it [OFFICIAL: absence].

HOW IMAGE INPUT IS MEANT TO BE USED:
  As an emotional and narrative baseline, not as a style reference. An image narrows
  mood and story; it does not specify genre, instruments, tempo or voice. Supply
  those in text, or the model chooses them. Translating what is in a picture into
  audio decisions is craft: CORE_01 §11.

COMPANION MODELS Google documents [OFFICIAL]:
  LYRIA + VEO           generate the video, then score it to the cuts (§4)
  LYRIA + NANO BANANA   storyboard images, then a song from them; cover art in the app
  LYRIA + GEMINI        hand Gemini a brief and have it write the detailed Lyria
                        prompt — a vendor documenting one model as the prompt engineer
                        for another, which is what this system is

</rag_zone>

</section>

<section id="§7" title="GOOGLE FLOW MUSIC">

<!-- rag_anchor: flow_music_lineage -->
<rag_zone id="flow_music_lineage">

─── ONE PRODUCT, THREE NAMES ─── [OFFICIAL]
```
Riffusion          open project, December 2022
    ↓ relaunched
Producer.ai        July 2025
    ↓ acquired by Google, 2026-02-24 — team joined Google Labs
Google Flow Music  renamed April 2026 · flowmusic.app
```
  riffusion.com and producer.ai redirect to Flow Music [COMMUNITY check, 2026-09].
  ⚠️ Everything generated before 2026-02-20 under the old names is inaccessible.
  ⚠️ Sites still trading under the Riffusion name with no stated affiliation are not
  the original project. Never emit a web address for any of them; mention Riffusion
  only as the origin of Flow Music.

  Flow Music runs on Google's models — Lyria (3.5 since 2026-07-29), Gemini, Veo and
  Nano Banana.

</rag_zone>

<!-- rag_anchor: flow_music_features_plans -->
<rag_zone id="flow_music">

### WHAT IT DOES
  [OFFICIAL, plan page] every plan: Lyria models, "Producer", Projects, downloads in
  mp3, wav and m4a, stem downloads, publishing, image and video generation.
  [COMMUNITY, 2026-07-28/29 "Spaces" update] one workspace to generate and edit songs,
  split stems, create images, write lyrics and generate video.
  [COMMUNITY] Extend, Cover or Replace a selected section; edits by typed instruction
  ("Shorten the intro to 4 bars").
  [COMMUNITY] No MIDI export on any plan.

─── PLANS ─── [OFFICIAL] names only
  Free (daily top-up credits, two concurrent generations) · Starter · Plus · Member
  (member badge, events, early access). Extra credits only on paid plans. Google AI
  subscribers get a matching Flow plan [COMMUNITY].

### NOT PUBLISHED
  Maximum track length; regional availability; the commercial-use clause (third
  parties say commercial use comes with the paid plans — primary text not found)
  [UNVERIFIED].

</rag_zone>

<!-- rag_anchor: flow_music_workflow -->
<rag_zone id="flow_music_workflow">

### THE WORKFLOW
The point of Flow Music is that you do not regenerate. Each step keeps what came before:
```
1  SEED      a narrative prompt produces a first track
2  REPLACE   name one part and what should be there instead
3  EXTEND    grow the arrangement forward
4  EDIT      stems, artwork, video — in the same Space
5  EXPORT    mp3 / wav / m4a, stems → a DAW
```

WRITING A REPLACE INSTRUCTION — scope it tightly, say what must survive:
    ✅  Replace only the guitar solo with a slower, more melodic line.
        Keep the drums and bass exactly as they are.
    ❌  Make the solo better
  A broad instruction invites the model to reconsider the whole mix — the most
  common complaint about this feature (CORE_03 §5).

WRITING AN EXTEND INSTRUCTION — restate the style anchor:
    ✅  Continue in the same late-70s folk style, same tempo and instrumentation,
        building toward a final chorus.

WHEN FLOW MUSIC INSTEAD OF SUNO:
  ✅ you work inside Google's tools and want music, artwork and video in one place
  ✅ you want section replacement without a Suno plan
WHEN SUNO INSTEAD:
  ✅ the vocal is the point and needs character · your own voice or catalog model ·
  songs past a few minutes · MIDI and a full DAW (DATA_SUNO §9)

</rag_zone>

</section>

<section id="§8" title="LYRIA REALTIME — steering a live stream">

<!-- rag_anchor: realtime_weighted_prompts -->
<rag_zone id="realtime_steering">

[OFFICIAL] RealTime uses WEIGHTED PROMPTS instead of one prompt string:
```
WeightedPrompt(text="minimal techno", weight=1.0)
WeightedPrompt(text="deep sub bass", weight=0.6)
WeightedPrompt(text="shimmering hi-hats", weight=0.4)
```
  BLEND      balanced weights: ambient synth pads 0.8 + lo-fi hip-hop drums 0.6
  TRANSITION change weights gradually: chill jazz piano 1.0 → add electronic
             breakbeat 0.3 → breakbeat 0.8, piano 0.3. Big jumps sound abrupt.
  LAYER      keep instrument and mood phrases separate so each can move on its own

CONTROLS [OFFICIAL]: guidance 0.0–6.0 (default 4.0) · bpm 60–200 · density 0–1 ·
brightness 0–1 · scale (a key/mode enum) · mute_bass · mute_drums ·
only_bass_and_drums · mode QUALITY (default), DIVERSITY or VOCALIZATION · temperature,
top_k, seed. Changing bpm or scale needs a context reset to take effect. Anything left
unset, the model decides from the prompts.

LATENCY: changes take a couple of seconds to be heard [COMMUNITY] — when steering from
game events, cue slightly early.

</rag_zone>

</section>

<section id="§9" title="RETIRED AND CONSOLIDATED">

<!-- rag_anchor: google_retired_products -->
<rag_zone id="retired">

─── MUSICFX AND MUSICFX DJ — CLOSED 31 JULY 2026 ─── [OFFICIAL, announced]
  Both retired as Google consolidated its music tools into Flow Music. For live
  streaming use Lyria RealTime (§8); for everything else, Flow Music or the Gemini app.
  If a user mentions either, they are working from an old guide. Repair: CORE_03 §3.

─── LYRIA 3 PRO ─── replaced by Lyria 3.5 (§1).

### OTHER MOVEMENTS
  [COMMUNITY] Google entered a partnership with Believe in May 2026.
  None of this changes how anything is prompted; it is here so a stale copy of this
  file can be diffed against reality quickly.

</rag_zone>

</section>

<section id="§10" title="CHOOSING WITHIN THE GOOGLE FAMILY">

<!-- rag_anchor: google_selector_table -->
<rag_zone id="google_selector">

  A 30-second sketch, jingle, or loop            → Lyria 3 Clip
  A complete song of a couple of minutes         → Lyria 3.5
  A soundtrack that must hit video cut points    → Lyria 3.5 + timestamp ranges
  Music from photographs                         → Lyria 3.5 with images, or the app
  A quick song on a phone with menus, no prompt  → the Gemini app
  A track to be edited part by part after        → Flow Music
  Music, artwork and video in one workspace      → Flow Music
  An endless stream to steer live                → Lyria RealTime
  Adaptive music inside a game or installation   → Lyria RealTime

WRITING FOR THE 30-SECOND MODEL:
  Thirty seconds is one idea, not a compressed song.
    ✅  One riff, one texture, one mood, seen through.
    ✅  For loops: "starts and ends seamlessly with no hard stop".
    ✅  For backing beds: stays out of the way, no sudden transitions.

</rag_zone>

<!-- rag_anchor: suno_lyria_conversion -->
<rag_zone id="cross_platform">

CONVERTING A SUNO PROMPT FOR LYRIA 3.5:
  KEEP     genre with era, mood, instruments, vocal description, BPM and key, section
           tags, parentheses for backing vocals
  REMOVE   Exclude Styles lists, slider values, Variety, Max Mode, Suno-only
           performance symbols, artist names
  ADD      a `Lyrics:` header above the text, an explicit language, a length ("a
           2-minute song") or timestamp ranges, "Instrumental only, no vocals." for
           instrumentals
  ⚠️ Mind the length: a Suno song planned for 5 minutes does not fit Lyria 3.5.

CONVERTING LYRIA TO SUNO: move timestamp ranges back into section labels (CORE_02),
keep BPM and key in Style, put exclusions in the Exclude Styles field.

</rag_zone>

</section>

<section id="§11" title="WORKED EXAMPLES">

<!-- rag_anchor: google_example_clip_loop -->
<rag_zone id="google_example_loop">

### 1 · A 30-SECOND LOOP (Clip)
```
A 30-second lo-fi hip-hop loop for studying at 82 BPM in F major. Dusty jazz Rhodes
chords, a warm sub-bass and a muffled boom-bap drum break, with vinyl crackle over
everything. The same relaxed groove from start to finish, starting and ending
seamlessly with no hard stop. Instrumental only, no vocals.
```
  No sections, no build, no ending: thirty seconds cannot hold an arc.

### 2 · A JINGLE WITH ONE HIT POINT (Clip)
```
A bright, optimistic corporate opener at 110 BPM in D major. Plucked marimba and
light strings over a soft electronic pulse, with a single warm brass swell. Begins
almost bare, gathers gradually, lands on one clear accent shortly before the end,
then resolves immediately. Instrumental only, no vocals.
```

</rag_zone>

<!-- rag_anchor: google_example_full_song -->
<rag_zone id="google_example_song">

### 3 · A FULL SONG WITH YOUR OWN LYRICS (3.5)
```
A late-1990s Bristol trip-hop song at 76 BPM in C minor, heavy and nocturnal. Dusty
breakbeat drums, a deep detuned bassline, a filtered Rhodes and a distant string
sample. Female Alto: rich, husky and very close, singing in English with almost no
projection.
[Intro] -> [Verse 1] -> [Chorus] -> [Verse 2] -> [Chorus] -> [Outro]

Lyrics:

[Verse 1]
Four in the morning and the streetlights hum
Nobody waiting and nowhere to run

[Chorus]
I don't mind the long way home (long way home)
The city sleeps, I walk alone
```

### 4 · A SONG IN UKRAINIAN (3.5)
Write the whole prompt in the language to be sung [OFFICIAL]:
```
Тепла інді-фолк пісня українською мовою, 96 BPM, соль мажор. Акустична гітара
пальцями, контрабас, легкі щітки. Ніжний жіночий вокал, близько до мікрофона.
Пісня про повернення додому після довгої дороги, з простим світлим приспівом.
```

</rag_zone>

<!-- rag_anchor: google_example_video_score -->
<rag_zone id="google_example_video">

### 5 · SCORING VIDEO TO CUT POINTS (3.5)
Note the cut times from the edit first, then start a range on each one:
```
A tense modern orchestral cue for a chase sequence at 140 BPM in E minor. Low
strings, taiko percussion and a rising synthetic drone. Instrumental only, no vocals.

[0:00 - 0:07] Intro: a single sustained low string note, almost still, faint
              percussion underneath.
[0:07 - 0:19] Build: a pulse enters in the low strings, quiet but insistent.
[0:19 - 0:34] Chase: percussion arrives hard and the rhythm doubles.
[0:34 - 0:38] Break: near-silence except one high sustained note.
[0:38 - 0:52] Climax: full orchestra and drums at maximum intensity.
[0:52 - 0:54] Ending: one accented hit, no decay.
```
  The abrupt ending is stated deliberately. A resolved ending under an unresolved
  picture is the most common failure in scoring work.

### 6 · A GENRE SHIFT INSIDE ONE TRACK (3.5)
```
[0:00 - 0:25] Intro: solo classical guitar, warm and intimate, a slow melody alone
              in a quiet room.
[0:25 - 0:55] Jazz trio: double bass and brushed drums join; relaxed swing.
[0:55 - 1:35] Modern: the drums switch to a hard trap beat at 140 BPM and a deep 808
              replaces the double bass. The guitar keeps its melody unchanged.
[1:35 - 1:55] Return: everything strips back to the solo guitar.
[1:55 - 2:00] Ending: a single held chord.
Instrumental only, no vocals.
```
  Keeping one element constant across the change — here the guitar melody — makes
  it one piece rather than three clips.

</rag_zone>

<!-- rag_anchor: google_example_images_bed_realtime -->
<rag_zone id="google_example_other">

### 7 · MUSIC FROM IMAGES (3.5)
```
A warm, nostalgic acoustic song in English at 88 BPM in G major. Acoustic guitar,
upright piano and a little brushed percussion. Male Tenor, soft and slightly worn.
The lyrics and the emotional arc follow the story told across the attached images.
```
  The images carry mood and narrative. Everything else still has to be said.

### 8 · A BED UNDER A VOICEOVER (3.5)
```
A calm, understated ambient bed for a documentary voiceover at 64 BPM in D major.
Sustained warm pads, a sparse piano figure and almost no percussion. Even, with no
sudden changes; nothing draws attention to itself. Instrumental only, no vocals.
[0:00 - 0:20] a single pad fading in
[0:20 - 1:00] a quiet piano figure begins, repeating gently
[1:00 - 1:40] a low string layer joins underneath, still restrained
[1:40 - 2:00] thins back out to the opening pad
```

### 9 · A STEERED REALTIME STREAM
Opening prompts: `dark fantasy low strings` 1.0 · `distant brass` 0.6 ·
`sparse percussion` 0.3, bpm 70, density 0.3.
While it plays: raise `fast percussion` toward 0.8 for a fight; drop everything but
`low drone` for a cave; bring in `warm hopeful strings` 0.7 for a sunrise.

</rag_zone>

</section>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_GOOGLE_2026-09.md · SunoForge v4.0
// Snapshot date 2026-09-30 · replace this file, not the CORE files
// Next: DATA_OTHER_2026-09.md
// ═══════════════════════════════════════════════════════════════

<tags>google, lyria, lyria 3.5, lyria-3.5, lyria 3 clip, lyria-3-clip-preview, lyria 3 pro retired, lyria realtime, weighted prompts, gemini app music, gemini api, interactions api, ai studio, google vids, flow music, riffusion history, producer.ai, prompt guide, genre first, bpm, key, mood list, genre keywords, instrument keywords, section tags, timestamp ranges, scoring video, lyrics header, parentheses backing vocals, vocal profiles, language of prompt, image input, synthid, no negative prompt, instrumental only, musicfx retired</tags>
</sunoforge_file>
