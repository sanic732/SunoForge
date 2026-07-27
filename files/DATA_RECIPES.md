---
file_id: DATA_RECIPES
version: "3.0"
layer: data
scope: genre_recipes · hybrid_recipes · duet · style_presets · task_scenarios · cross_platform_versions · style_library
key_concepts: [recipe_format, genre_recipes, hybrid_recipes, duet_recipe, style_presets, task_scenarios, cross_platform, style_library]
depends_on: [CORE_01_STYLE, CORE_02_LYRICS, DATA_VOCAB]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS]
rag_priority: high
redundancy: high
updated: "2026-07-27"
changelog: "v3.0 — undated · MAX MODE tags and the slash-asterisk separator removed from every recipe · per-section anti-drift reminders removed · parametric and colon-prefixed sound tags converted · slider values and exclude vocabularies now referenced rather than restated · Udio templates dropped, Stable Audio added"
---

# 📋 SUNOFORGE v3.0 — RECIPES & PRESETS
# File 10 of 12 · DATA layer · undated

> Menu entry **[9] RECIPE LIBRARY** per CORE_00 §4.

> **Why this file has no expiry date.** A recipe is a creative configuration —
> which era to name, which instruments carry the sound, who is singing. None
> of that expires. The numbers that do expire (slider ranges, exclude
> vocabularies, field limits) live in DATA_SUNO and are referenced from here,
> never copied.

> 📌 **This is a catalogue.** More working starting points is the whole value.
> Recipes are meant to be edited — a template followed exactly is a large part
> of why so much generated music sounds alike.

═══════════════════════════════════════════════════════════════════
§1. HOW TO READ A RECIPE
═══════════════════════════════════════════════════════════════════

<rag_zone id="recipe_format">

Each recipe carries five things:

  STYLE       a complete, ready-to-paste Style description, six layers
              assembled (CORE_01 §1). This is the part that matters.
  LYRICS      a section skeleton to fill with your own words (CORE_02)
  SETTINGS    tempo and key as specific starting values, plus which slider
              posture to use — by name, not by number
  EXCLUDE     which ready list to start from, plus anything specific to this
              recipe
  NOTES       what to change first, and what breaks it

─── WHY SLIDERS AND EXCLUDE LISTS ARE REFERENCES ───

Slider ranges by goal and by genre are in **DATA_SUNO §7**. Ready exclude
vocabularies by target genre are in **DATA_SUNO §3**. Both are platform facts
that move, and thirty copies scattered through this file would drift out of
sync with the source without anyone noticing. Three copies of a version matrix
is how the previous edition silently contradicted itself.

So a recipe says *"genre-faithful posture"* and you read the current numbers
from one place. If the platform changes them, one file changes.

─── SLIDER POSTURES, BY NAME ───

  GENRE-FAITHFUL      low experimentation, high literalness — recreate a
                      recognised sound accurately
  BALANCED            middle of both — the default for most work
  EXPERIMENTAL        high experimentation, lower literalness — for hybrids
                      and deliberate strangeness
  EXTENDING           lower experimentation than the base track

  Numbers for each: DATA_SUNO §7.

─── WHAT IS NOT IN THESE RECIPES ───

No quality-mode tags, no separator lines, no bracketed parameters, no
per-section style reminders repeated down the page. Those were in the previous
edition, none of them did anything, and the reasons are in CORE_00 §2 and
CORE_03 §3.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. CORE GENRE RECIPES
═══════════════════════════════════════════════════════════════════

<rag_zone id="recipe_edm">

─── EDM · FESTIVAL MAIN STAGE ───

STYLE
```
peak-time festival EDM, euphoric and relentless, massive supersaw lead stack
over a sidechained synth bass with layered white-noise risers, airy female
vocal chops rather than a sung lead, wide stereo festival PA polish,
128 BPM, F minor
```

LYRICS
```
[Intro]
[Instrumental]

[Build]

[Drop]
[Instrumental]

[Breakdown]
(vocal chop hook, wordless)

[Build]

[Drop]
[Instrumental]

[Outro]
[Fade Out]
```

SETTINGS   128 BPM · F minor · balanced posture
EXCLUDE    start from the pop/radio list, DATA_SUNO §3; add acoustic guitar,
           folk fingerpicking, live drum kit
NOTES      The drop is instrumental. Putting a sung lead over it is the most
           common way this recipe fails — the vocal and the lead fight for the
           same space. Keep words in the breakdown, chops in the drop.

</rag_zone>

<rag_zone id="recipe_pop">

─── POP · MODERN RADIO ───

STYLE
```
modern radio pop, bright and confident, plucked synth hooks over punchy
electronic drums and a warm round bass, female lead with a clear belted
chorus and a close conversational verse, glossy contemporary mix,
118 BPM, C major
```

LYRICS
```
[Intro]
[Hook first]

[Verse 1]

[Pre-Chorus]

[Chorus]

[Verse 2]

[Pre-Chorus]

[Chorus]

[Bridge — stripped to voice and one instrument]

[Final Chorus]

[Outro]
```

SETTINGS   118 BPM · C major · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3
NOTES      The verse-to-chorus contrast is the whole recipe. If the verse is
           already full, the chorus has nowhere to go. Keep the verse sparse
           even when it feels too empty while you are writing it.

</rag_zone>

<rag_zone id="recipe_trap">

─── TRAP ───

STYLE
```
2015 Atlanta trap, dark and unhurried, deep 808 sub with rolling triplet
hi-hats and an eerie minor synth motif, male baritone with a tuned
conversational flow, heavy modern low-end polish, 140 BPM at a half-time
feel, D minor
```

LYRICS
```
[Intro]

[Verse 1]
(hey)
(uh)

[Hook]

[Verse 2]
(yeah)

[Hook]

[Bridge]
[Beat switch]

[Hook]

[Outro]
```

SETTINGS   140 BPM, half-time feel · D minor · balanced posture
EXCLUDE    hip-hop/trap list, DATA_SUNO §3
NOTES      140 with a half-time feel sounds slower than 90 straight — say the
           feel as well as the number (DATA_VOCAB §8). Ad-libs go in the gaps
           between lines, not on top of them (CORE_02 §7).

</rag_zone>

<rag_zone id="recipe_grunge">

─── GRUNGE · ALT-ROCK ───

STYLE
```
mid-90s Seattle grunge, brooding and worn out, tape-saturated distorted
guitar wall with a bass carrying the melody underneath, male gravelly
baritone, close-miked and unpolished, raw independent-label production,
92 BPM, E minor
```

LYRICS
```
[Intro]

[Verse 1 — quiet, guitar barely moving]

[Chorus — full distortion]

[Verse 2]

[Chorus]

[Guitar Solo]

[Bridge — stripped to voice and one guitar]

[Final Chorus]

[Outro]
```

SETTINGS   92 BPM · E minor · balanced posture
EXCLUDE    rock/metal list, DATA_SUNO §3; add autotune, polished pop
           production
NOTES      The quiet-loud contrast is the genre. Mark the verse as quiet
           explicitly — left alone, the model plays the verse at chorus
           volume and the song has no shape.

</rag_zone>

<rag_zone id="recipe_metal">

─── METAL · MODERN HEAVY ───

STYLE
```
modern melodic death metal, furious and cold, downtuned palm-muted riffing
over double-kick drums with a tremolo-picked lead line above, male harsh
growl with clean sung choruses, dense and brutally compressed modern metal
mix, 168 BPM, D minor
```

LYRICS
```
[Intro]
[Instrumental]

[Verse 1]
[Growl]

[Pre-Chorus]

[Chorus]
[Clean vocal]

[Verse 2]
[Growl]

[Chorus]
[Clean vocal]

[Guitar Solo]

[Breakdown]

[Final Chorus]
[Clean vocal]

[Outro]
```

SETTINGS   168 BPM · D minor · genre-faithful posture
EXCLUDE    rock/metal list, DATA_SUNO §3
NOTES      Alternating harsh and clean is what makes this genre legible.
           Label the switch on every section — it is the one thing the model
           will not infer.

</rag_zone>

<rag_zone id="recipe_country">

─── COUNTRY · OUTLAW ───

STYLE
```
1970s Nashville outlaw country, warm and unhurried, twangy Telecaster with
spring reverb alongside pedal steel and a plain acoustic strum, male warm
baritone with a slight drawl and a storyteller's phrasing, vintage analog
studio warmth, 104 BPM, G major
```

LYRICS
```
[Intro]

[Verse 1]

[Chorus]

[Verse 2]

[Chorus]

[Bridge]

[Final Chorus]

[Outro]
```

SETTINGS   104 BPM · G major · genre-faithful posture
EXCLUDE    country list, DATA_SUNO §3
NOTES      Country is a lyric-first genre. The structure is deliberately
           plain because the words carry it. Write a story with a turn in the
           last verse and this recipe works with no other changes.

</rag_zone>

<rag_zone id="recipe_lofi">

─── LO-FI HIP-HOP ───

STYLE
```
late-night Tokyo lo-fi hip-hop, mellow and unhurried, dusty jazz piano
samples over a soft swung boom-bap break with a warm sub underneath and
vinyl crackle across everything, no vocals, intimate bedroom production,
74 BPM, A minor
```

LYRICS
```
[Intro]
[Instrumental]

[Theme A]

[Theme B]

[Break]

[Theme A]

[Outro]
[Fade Out]
```

SETTINGS   74 BPM · A minor · balanced posture
EXCLUDE    lo-fi/chill list, DATA_SUNO §3
NOTES      Usually instrumental. If you want a voice, make it whispered and
           low in the mix — a present lead vocal turns this into a different
           genre entirely. Nothing should ask for attention.

VARIATION — with a vocal
```
…as above, with a whispered female vocal sitting low and close, almost
spoken, barely above the piano
```

</rag_zone>

<rag_zone id="recipe_cinematic">

─── CINEMATIC · TRAILER ───

STYLE
```
modern trailer orchestral, dark and heroic, sweeping string swells with
enormous taiko percussion and brass rising underneath, a wordless choir
singing open vowels rather than lyrics, wide and deep cinematic mix,
100 BPM, E minor
```

LYRICS
```
[Intro]
[Instrumental]

[Build]

[Theme]
[Choir]

[Breakdown — solo cello and harp]

[Build]

[Final Theme]
[Choir]

[Outro]
```

SETTINGS   100 BPM · E minor · genre-faithful posture
EXCLUDE    cinematic/epic list, DATA_SUNO §3
NOTES      "Wordless choir on open vowels" is doing important work — ask for
           a choir without it and you get lyrics you did not write. Consider
           Lyria for orchestral material with timestamps (DATA_GOOGLE §4).

</rag_zone>

<rag_zone id="recipe_gospel">

─── GOSPEL ───

STYLE
```
late-60s Memphis gospel, joyful and rising, swirling drawbar organ through
a rotary speaker with hand claps and a live rhythm section, powerful female
soprano with melismatic runs answered by a full choir, warm church room
sound, 96 BPM, B♭ major
```

LYRICS
```
[Intro]

[Verse 1]

[Pre-Chorus]

[Chorus]
[Gospel choir]

[Verse 2]

[Chorus]
[Gospel choir]

[Bridge]
[Spoken word]

[Final Chorus]
[Gospel choir]

[Outro]
```

SETTINGS   96 BPM · B♭ major · genre-faithful posture
EXCLUDE    gospel list, DATA_SUNO §3
NOTES      Gospel builds. Starting at full power leaves nowhere to go — the
           first chorus should be smaller than the last. Call-and-response
           between the lead and the choir is the defining feature; write the
           lyric so the choir has something to answer.

</rag_zone>

<rag_zone id="recipe_rnb">

─── R&B · NEO-SOUL ───

STYLE
```
late-90s neo-soul, warm and intimate, electric piano with a tremolo over a
laid-back drum pocket and a melodic fretless bass, female alto singing
conversationally with layered harmonies on the hook, warm analog mix with
plenty of space, 88 BPM, E♭ major
```

LYRICS
```
[Intro]

[Verse 1]

[Chorus]
[Stacked harmonies]

[Verse 2]

[Chorus]
[Stacked harmonies]

[Bridge]

[Chorus]

[Outro]
```

SETTINGS   88 BPM · E♭ major · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add electronic drums, autotune
NOTES      The pocket is the genre. "Laid-back", "behind the beat" — say it
           explicitly (DATA_VOCAB §4). Played straight, this becomes ordinary
           pop with a Rhodes.

</rag_zone>

<rag_zone id="recipe_folk">

─── FOLK · SINGER-SONGWRITER ───

STYLE
```
early-70s British folk revival, austere and wintry, fingerpicked steel-string
guitar with a bowed double bass underneath and a fiddle entering only in the
last verse, female voice pure and unornamented, recorded live in a cold stone
room, 74 BPM, D minor
```

LYRICS
```
[Intro]

[Verse 1]

[Chorus]

[Verse 2]

[Chorus]

[Verse 3]

[Final Chorus]

[Outro]
```

SETTINGS   78 BPM · G major · genre-faithful posture
EXCLUDE    folk/acoustic list, DATA_SUNO §3
NOTES      No bridge. Folk often uses a third verse where pop would put a
           bridge, and the difference is audible. Arrangement should stay
           almost empty until the last chorus.

</rag_zone>

<rag_zone id="recipe_jazz">

─── JAZZ · SMALL GROUP ───

STYLE
```
1959 New York cool jazz, smoky and restrained, muted trumpet and brushed
drums over a walking upright bass with sparse comping piano, no vocals,
warm mono-leaning room recording with the band in one space, 132 BPM with a
medium swing, B♭ major
```

LYRICS
```
[Intro]
[Instrumental]

[Head]

[Trumpet Solo]

[Piano Interlude]

[Head]

[Outro]
```

SETTINGS   132 BPM, medium swing · B♭ major · genre-faithful posture
EXCLUDE    jazz list, DATA_SUNO §3
NOTES      "Medium swing" matters more than the tempo number. A vocal
           version works — ask for a crooned close-miked delivery and add
           verses around the head.

</rag_zone>

<rag_zone id="recipe_punk">

─── PUNK ───

STYLE
```
1977 London punk, furious and joyful, three chords of overdriven guitar
with a bass locked to the root and a drummer slightly ahead of the beat,
male shouted vocal, barely in tune and entirely committed, raw single-take
production, 176 BPM, A major
```

LYRICS
```
[Intro]

[Verse 1]

[Chorus]

[Verse 2]

[Chorus]

[Verse 3]

[Chorus]

[Outro]
```

SETTINGS   176 BPM · A major · balanced posture
EXCLUDE    rock/metal list, DATA_SUNO §3; add polished production, layered
           harmonies
NOTES      "Slightly ahead of the beat" is the genre in four words
           (DATA_VOCAB §4). Under two minutes. Resist adding a bridge.

</rag_zone>

<rag_zone id="recipe_synthwave">

─── SYNTHWAVE ───

STYLE
```
2018 retrowave, nostalgic and driving, a wide analog bass sequence under
gated drums with a bright detuned lead and shimmering pads, male vocal with
a distant reverberant delivery, glossy neon 1980s production, 112 BPM,
D minor
```

LYRICS
```
[Intro]
[Instrumental]

[Verse 1]

[Chorus]

[Verse 2]

[Chorus]

[Solo]

[Final Chorus]

[Outro]
[Fade Out]
```

SETTINGS   112 BPM · D minor · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add acoustic instruments, modern
           trap drums
NOTES      Works well instrumental — drop the vocal sections and extend the
           solo. The era is inside the genre name, so no additional decade
           is needed (CORE_01 §3).

</rag_zone>

<rag_zone id="recipe_ambient">

─── AMBIENT · LONG-FORM ───

STYLE
```
early-90s Warp Records ambient, still and unresolved, sustained analog pads
with very slow attacks over a low drone, a distant filtered piano figure
returning every few bars, no percussion and no vocals, enormous diffuse
reverb, extremely slow, A minor
```

LYRICS
```
[Intro]
[Instrumental]

[Theme A]

[Theme B]

[Theme A]

[Outro]
[Fade Out]
```

SETTINGS   no fixed tempo · A minor · balanced posture
EXCLUDE    ambient/sleep list, DATA_SUNO §3
NOTES      "Unresolved" is the important word — without it the model writes
           toward an ending, which is wrong for something meant to loop or
           sit under a scene. For long durations, consider Stable Audio
           (DATA_OTHER §2).

</rag_zone>

<rag_zone id="recipe_house">

─── HOUSE · DEEP ───

STYLE
```
late-90s deep house, warm and patient, a four-on-the-floor kick under a
filtered chord stab and a round sub bass, soulful female vocal appearing in
short phrases rather than verses, warm analog club mix, 122 BPM, A minor
```

LYRICS
```
[Intro]
[Instrumental]

[Build]

[Verse]

[Hook]

[Break]

[Hook]

[Outro]
[Fade Out]
```

SETTINGS   122 BPM · A minor · balanced posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add acoustic guitar, live drum kit
NOTES      House vocals are fragments, not songs. Writing full verses turns
           this into dance-pop. Long intro and outro are structural — they
           exist so a DJ can mix in and out.

</rag_zone>

<rag_zone id="recipe_techno">

─── TECHNO ───

STYLE
```
peak-time Berlin techno, relentless and industrial, machine-tight drum
programming with a single evolving metallic drone and a filtered hi-hat
pattern, no vocals, dry unforgiving club mix, 134 BPM, F minor
```

LYRICS
```
[Intro]
[Instrumental]

[Build]

[Theme A]

[Breakdown]

[Build]

[Theme A]

[Outro]
```

SETTINGS   134 BPM · F minor · experimental posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add melody, chord progression,
           vocals, acoustic instruments
NOTES      Excluding "melody" is deliberate and unusual. Techno is texture
           and repetition; a tune makes it something else. Change should
           happen through filtering, not through new material.

</rag_zone>

<rag_zone id="recipe_dnb">

─── DRUM AND BASS · LIQUID ───

STYLE
```
liquid drum and bass, weightless and warm, chopped breakbeats at high tempo
over a rolling sub with lush pads and a distant piano, soft female vocal
floating high above the rhythm, wide open modern mix, 174 BPM, E minor
```

LYRICS
```
[Intro]
[Instrumental]

[Build]

[Drop]

[Verse]

[Drop]

[Breakdown]

[Drop]

[Outro]
```

SETTINGS   174 BPM · E minor · balanced posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add half-time feel, trap hi-hats
NOTES      The bass sits at half the drum tempo, which is what makes it feel
           calm at 174. Saying "rolling" rather than "fast" for the sub keeps
           the two layers apart.

</rag_zone>

<rag_zone id="recipe_dubstep">

─── BASS MUSIC · DUBSTEP ───

STYLE
```
modern dubstep, heavy and mechanical, a modulated wobble bass under
half-time drums with metallic percussion and a sparse minor motif, no lead
vocal, enormous low end with a hard aggressive mix, 140 BPM at a half-time
feel, G minor
```

LYRICS
```
[Intro]
[Instrumental]

[Build]

[Drop]

[Breakdown]

[Build]

[Drop]

[Outro]
```

SETTINGS   140 BPM, half-time feel · G minor · balanced posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add acoustic instruments, gentle,
           orchestral strings
NOTES      Everything serves the drop. The build should be longer than feels
           comfortable — dubstep tension is mostly anticipation.

</rag_zone>

<rag_zone id="recipe_reggae">

─── REGGAE · ROOTS ───

STYLE
```
1970s Kingston roots reggae, spacious and unhurried, offbeat guitar skank
over a deep melodic bass with a dry drum kit and dub delays on the snare,
male voice with close harmony answers, warm vintage analog mix, 76 BPM,
A minor
```

LYRICS
```
[Intro]

[Verse 1]

[Chorus]
[Harmonies]

[Verse 2]

[Chorus]
[Harmonies]

[Bridge]

[Chorus]

[Outro]
[Fade Out]
```

SETTINGS   76 BPM · A minor · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add electronic drums, distorted
           guitar, autotune
NOTES      The bass carries the melody and the guitar carries the rhythm —
           the reverse of most genres. Say so explicitly or you get rock
           played slowly.

</rag_zone>

<rag_zone id="recipe_afrobeat">

─── AFROBEAT ───

STYLE
```
1970s Lagos afrobeat, insistent and communal, interlocking clean guitar
figures with a full horn section and dense layered percussion over a
melodic bass, male lead with a group answering in chant, live room
recording with the whole band together, 112 BPM, E minor
```

LYRICS
```
[Intro]
[Instrumental]

[Verse 1]

[Chorus]
[Chant vocals]

[Instrumental]
[Saxophone Solo]

[Verse 2]

[Chorus]
[Chant vocals]

[Outro]
```

SETTINGS   112 BPM · E minor · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add electronic drums, synthesiser
NOTES      Long instrumental sections are structural, not filler. The groove
           is the song. Resist shortening the solo.

</rag_zone>

<rag_zone id="recipe_latin">

─── LATIN · SALSA ───

STYLE
```
1970s New York salsa, jubilant and hot, montuno piano over clave percussion
with a punchy brass section and a driving bass tumbao, male lead with a
call-and-response chorus, bright live band recording, 180 BPM, D minor
```

LYRICS
```
[Intro]
[Instrumental]

[Verse 1]

[Chorus]
[Chant vocals]

[Verse 2]

[Chorus]
[Chant vocals]

[Instrumental]
[Brass Section]

[Chorus]
[Chant vocals]

[Outro]
```

SETTINGS   180 BPM · D minor · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add electronic drums, distorted
           guitar
NOTES      Naming the clave is what makes this genuinely salsa rather than
           generic Latin pop. The final section traditionally opens up into
           call-and-response — leave room for it.

</rag_zone>

<rag_zone id="recipe_disco">

─── DISCO · FUNK ───

STYLE
```
late-70s Studio 54 disco, euphoric and glossy, four-on-the-floor drums with
a slap bass line and muted rhythm guitar chops under sweeping strings,
female lead with full stacked backing vocals, wide warm vintage mix,
120 BPM, F♯ minor
```

LYRICS
```
[Intro]
[Instrumental]

[Verse 1]

[Pre-Chorus]

[Chorus]
[Stacked harmonies]

[Verse 2]

[Chorus]
[Stacked harmonies]

[Break — bass and drums only]

[Final Chorus]
[Stacked harmonies]

[Outro]
[Fade Out]
```

SETTINGS   120 BPM · F♯ minor · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add electronic drums, autotune,
           trap hi-hats
NOTES      The stripped break before the final chorus is the genre's
           signature move. Fade the outro — disco records almost never end
           cleanly.

</rag_zone>

<rag_zone id="recipe_dreampop">

─── DREAM POP · SHOEGAZE ───

STYLE
```
early-90s shoegaze, blissful and submerged, a wall of reverb-drenched
tremolo guitars over a simple driving drum pattern with a melodic bass
beneath, female vocal buried in the mix as another texture rather than a
lead, enormous washed-out production, 128 BPM, D major
```

LYRICS
```
[Intro]
[Instrumental]

[Verse 1]

[Chorus]

[Verse 2]

[Chorus]

[Instrumental]

[Final Chorus]

[Outro]
[Fade Out]
```

SETTINGS   128 BPM · D major · experimental posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add clear vocals, dry mix, close-mic
NOTES      "Buried in the mix" contradicts every other recipe here and is
           correct for this one. If the words are intelligible, it is not
           shoegaze.

</rag_zone>

<rag_zone id="recipe_kpop">

─── K-POP ───

STYLE
```
contemporary K-pop, bright and maximal, plucked synth hooks over a hard
electronic beat with a section that switches to a half-time rap passage,
female group vocal alternating a belted lead with tight stacked harmonies,
extremely polished wide modern mix, 124 BPM, B minor
```

LYRICS
```
[Intro]
[Hook first]

[Verse 1]

[Pre-Chorus]

[Chorus]
[Stacked harmonies]

[Verse 2]
[Rap]

[Pre-Chorus]

[Chorus]
[Stacked harmonies]

[Bridge]

[Beat switch]

[Final Chorus]
[Stacked harmonies]

[Outro]
```

SETTINGS   124 BPM · B minor · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3; add lo-fi, raw production
NOTES      The genre's signature is sudden section changes — a rap passage
           and a beat switch inside a pop song. Mark both explicitly. More
           sections than a Western pop track by design.

</rag_zone>

<rag_zone id="recipe_blues">

─── BLUES ───

STYLE
```
1950s Chicago electric blues, hot and close, overdriven guitar with wailing
harmonica over a shuffling rhythm section and walking bass, male voice
cracked and shouting, a single microphone in a small hard room, 96 BPM with
a heavy shuffle, E major
```

LYRICS
```
[Intro]

[Verse 1]

[Verse 2]

[Guitar Solo]

[Verse 3]

[Harmonica Solo]

[Verse 4]

[Outro]
```

SETTINGS   96 BPM, shuffle · E major · genre-faithful posture
EXCLUDE    jazz list, DATA_SUNO §3; add polished production, synthesiser
NOTES      No chorus. Blues repeats the first line of each verse — write it
           that way and the form does the rest. Twelve-bar structure:
           CORE_02 §10.

</rag_zone>

<rag_zone id="recipe_classical">

─── ORCHESTRAL · CONCERT ───

STYLE
```
late-romantic orchestral, sweeping and tragic, full string section carrying
a long melodic line with woodwind answers and restrained brass, no
percussion beyond timpani, no vocals, recorded in a large concert hall from
the audience's perspective, slow, C minor
```

LYRICS
```
[Intro]

[Theme A]

[Development]

[Theme B]

[Development]

[Theme A]

[Coda]
```

SETTINGS   slow, no fixed tempo · C minor · genre-faithful posture
EXCLUDE    cinematic/epic list, DATA_SUNO §3; add drums, electronic
           instruments, modern production
NOTES      Naming the period does more than naming the instruments —
           baroque, classical, romantic and modernist orchestras sound
           entirely different. Consider Lyria for orchestral work
           (DATA_OTHER §6).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. HYBRID RECIPES
═══════════════════════════════════════════════════════════════════

<rag_zone id="recipe_hybrids">

Method behind these — bridge genres, narrative blending, what refuses to
combine — is CORE_01 §10.

─── AMAPIANO FUSION ───

STYLE
```
amapiano meeting modern electronic, spacious and patient, a log drum
bassline under shaker-driven percussion with airy synth chords floating
above, female vocal singing short repeated hooks rather than verses, warm
wide contemporary mix, 112 BPM, A minor
```

LYRICS
```
[Intro]
[Instrumental]

[Hook]

[Verse]

[Hook]

[Break — percussion only]

[Hook]

[Outro]
```

SETTINGS   112 BPM · A minor · balanced posture
NOTES      The tempo band is narrow and it matters — outside roughly 108–116
           this stops sounding like amapiano. Long builds, late payoffs;
           resist a Western-style drop.

─── LO-FI TRAP ───

STYLE
```
lo-fi trap, hazy and weightless, vinyl crackle and dusty jazz sample
harmony over an 808 sub with soft hi-hats at a half-time feel, female
breathy vocal sitting low and close, warm degraded bedroom production,
84 BPM, D minor
```

LYRICS
```
[Intro]
[Instrumental]

[Verse 1]

[Hook]

[Verse 2]

[Hook]

[Bridge — vocal and 808 only]

[Hook]

[Outro]
[Fade Out]
```

SETTINGS   84 BPM, half-time feel · D minor · balanced posture
NOTES      Bridge genre is the production aesthetic, not the rhythm. The
           dust holds the two halves together — remove the crackle and it
           becomes plain trap.

─── DRIFT PHONK ───

STYLE
```
drift phonk, murky and ominous, a slowed Memphis cowbell pattern with
heavily distorted 808 hits and an ambient pad underneath, male whispered
and pitched-down delivery, deliberately overloaded and lo-fi, 64 BPM,
B minor
```

LYRICS
```
[Intro]
[Instrumental]

[Verse 1]

[Drop]

[Verse 2]

[Drop]

[Outro]
```

SETTINGS   64 BPM · B minor · balanced posture
NOTES      Distinct from Memphis phonk, which is faster, and Brazilian
           phonk, which is percussive. Naming the variant matters. The
           distortion is the point — do not ask for a clean mix.

─── HYPERPOP FOLK ───

STYLE
```
bedroom folk pulled through hyperpop, fragile and chaotic at once,
fingerpicked acoustic guitar under pitch-shifted stacked vocal layers and
bursts of digital distortion, female voice small and untrained at the
centre of it, deliberately overloaded DIY production, 104 BPM, F major
```

LYRICS
```
[Intro — acoustic guitar alone]

[Verse 1]

[Pre-Chorus]

[Chorus — full glitched layers]

[Verse 2]

[Chorus]

[Bridge — acoustic and raw vocal only]

[Final Chorus]

[Outro]
```

SETTINGS   104 BPM · F major · experimental posture
NOTES      The bridge genre is bedroom production — both halves are
           intimate and homemade. The contrast only works if the quiet parts
           are genuinely quiet.

─── CINEMATIC CHOIR ELECTRONICA ───

STYLE
```
cinematic orchestral crossed with modern electronic, vast and severe,
wordless choir over taiko and brass swells with a synthetic sub and a
pulsing sequence underneath, no lead vocal, enormous wide hybrid mix,
90 BPM, C minor
```

LYRICS
```
[Intro]
[Instrumental]

[Build]

[Theme]
[Choir]

[Breakdown]

[Build]

[Final Theme]
[Choir]

[Outro]
```

SETTINGS   90 BPM · C minor · genre-faithful posture
NOTES      Bridge is the shared sense of scale. Keep the electronic elements
           low and wide so they support the orchestra rather than compete.

─── SPOKEN WORD AMBIENT ───

STYLE
```
ambient bed for spoken word, still and nocturnal, sustained pads with a
single piano note returning every few bars and distant rain underneath,
a low male speaking voice, unhurried and close, intimate bedroom recording,
very slow, no fixed pulse, D minor
```

LYRICS
```
[Intro]
[Rain]

[Spoken word]

[Interlude]

[Spoken word]

[Outro]
[Fade Out]
```

SETTINGS   no fixed tempo · D minor · balanced posture
NOTES      Write for speech, not for song — sentence rhythm, sparing rhyme,
           shorter than feels right (CORE_02 §8). Flow Music suits this well
           if you want to build it in passes (DATA_GOOGLE §7).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. DUET
═══════════════════════════════════════════════════════════════════

<rag_zone id="recipe_duet">

─── DUET · EMOTIONAL BALLAD ───

Full protocol, all three anchors, per CORE_02 §9.

STYLE — anchor one
```
an emotional pop ballad performed as a duet between a male baritone and a
female alto trading verses, intimate and building, piano with warm strings
and soft brushed drums, close and uncluttered production, 88 BPM, C major
```

LYRICS — anchors two and three
```
[Male and female duet]

[Intro]
[Instrumental]

[Verse 1]
[Male]

[Pre-Chorus]
[Male]

[Chorus]
[Both]

[Verse 2]
[Female]

[Chorus]
[Both]

[Bridge]
[Female]

[Final Chorus]
[Both]

[Outro]
```

SETTINGS   88 BPM · C major · genre-faithful posture
EXCLUDE    pop/radio list, DATA_SUNO §3
NOTES      Whole sections per singer. Do not alternate line by line — that
           is the single most reliable way to make the two voices blur into
           one. Two voices in the same range blur regardless of labelling,
           so keep the ranges genuinely apart.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. STYLE PRESETS
═══════════════════════════════════════════════════════════════════

<rag_zone id="style_presets">

Single-line Style descriptions, ready to paste and edit. Shorter than the
full recipes above and useful when you know what you want.

  ROCK AND METAL
  1  1980s Sunset Strip glam metal, swaggering, screaming lead guitar with
     pinch harmonics, male high rasp, bright wide 1980s mix, 140 BPM, A major
  2  1991 Seattle grunge, exhausted and defiant, detuned guitar wall, male
     baritone, raw independent production, 96 BPM, D minor
  3  2000s post-hardcore, urgent, interlocking clean guitars into distortion,
     male voice alternating sung and shouted, dense mix, 154 BPM, B minor
  4  1970s British hard rock, swaggering, overdriven riffing and Hammond
     organ, male high tenor, warm analog room, 128 BPM, E major
  5  modern doom metal, immense and slow, downtuned crushing riffs with
     feedback, low growled vocal, murky heavy mix, 62 BPM, C minor

  ELECTRONIC
  6  late-80s Chicago acid house, hypnotic, squelching resonant bassline over
     a drum machine, no vocals, dry direct mix, 122 BPM, A minor
  7  peak-time Berlin techno, relentless and industrial, machine-tight
     percussion and a single evolving drone, instrumental, 134 BPM, F minor
  8  liquid drum and bass, weightless, chopped breaks under warm pads and a
     rolling sub, soft female vocal high in the mix, 174 BPM, E minor
  9  1990s Bristol trip-hop, nocturnal, dusty breakbeat with a detuned bass
     and filtered keys, female alto close and breathy, 88 BPM, G minor
  10 modern melodic house, warm and open, plucked synth over a four-on-the-
     floor pulse, wordless vocal hook, wide bright mix, 124 BPM, A minor

  HIP-HOP AND R&B
  11 1994 East Coast boom bap, dusty, chopped soul sample over a hard snare,
     male conversational rap, narrow warm mix, 92 BPM, C minor
  12 modern drill, cold and sparse, sliding 808 with skittering hi-hats and
     a minor piano motif, male deadpan delivery, 142 BPM, F minor
  13 1970s Philadelphia soul, lush, sweeping strings over a tight rhythm
     section, male tenor with falsetto, wide vintage mix, 104 BPM, E♭ major
  14 contemporary alternative R&B, hazy, sparse electric piano and a soft
     sub, female voice layered and pitched, spacious dark mix, 76 BPM, B minor

  ACOUSTIC AND ROOTS
  15 1970s Nashville outlaw country, weathered, pedal steel and Telecaster
     twang, male baritone with a drawl, vintage analog warmth, 100 BPM, G major
  16 Appalachian old-time, brisk, banjo rolls and fiddle with close harmony
     singing, single-microphone room sound, 148 BPM, D major
  17 delta blues, hot and dry, resonator slide guitar and stamping foot, male
     cracked voice, a single close microphone, 84 BPM, E major
  18 contemporary indie folk, hushed, fingerpicked steel-string and a distant
     harmonium, female alto barely projecting, close dry room, 72 BPM, C major
  19 celtic folk, rolling, fiddle and tin whistle over a bodhrán, mixed-voice
     unison singing, live room sound, 116 BPM in 6/8, D minor

  JAZZ AND LOUNGE
  20 1959 cool jazz, restrained, muted trumpet and brushed drums over walking
     bass, instrumental, warm mono-leaning room, 132 BPM medium swing, B♭ major
  21 bossa nova, gentle, nylon-string guitar with soft brushes, female voice
     close and unhurried, warm intimate mix, 128 BPM, F major
  22 1930s hot swing, exuberant, clarinet and muted brass over a rhythm
     section, group vocal, period mono recording, 180 BPM, C major

  CINEMATIC AND AMBIENT
  23 modern trailer orchestral, severe, string swells and taiko with wordless
     choir, wide and deep, 100 BPM, E minor
  24 1970s Italian giallo score, uneasy, harpsichord and fuzz bass with
     wordless female vocal, close vintage mix, 110 BPM, C♯ minor
  25 minimalist neoclassical, still, felted piano and a distant cello, no
     percussion, intimate close recording, very slow, A minor
  26 dark ambient drone, oppressive, low sustained textures with metallic
     resonance, no melody, enormous diffuse space, no fixed tempo, no key

  WORLD AND LATIN
  27 1970s Lagos afrobeat, insistent, interlocking guitars with a horn
     section and dense percussion, group vocal chant, live room, 112 BPM,
     E minor
  28 1970s Kingston roots reggae, spacious, offbeat guitar skank with deep
     bass and dub delays, male voice with harmonies, 76 BPM, A minor
  29 Buenos Aires tango, dramatic, bandoneón and violin with sharp piano
     accents, instrumental, close vintage recording, 120 BPM, D minor
  30 flamenco, urgent, fast spanish guitar with palmas and cajón, male voice
     raw and ornamented, close live recording, 140 BPM, phrygian on E

  POP AND SONGWRITING
  31 early-2000s Scandinavian pop, glossy and precise, layered synth hooks
     with a tight beat, female lead, immaculate wide mix, 116 BPM, C major
  32 1960s Brill Building pop, innocent, piano and strings with a shuffling
     beat, female group vocal, warm mono, 132 BPM, G major
  33 bedroom pop, hazy and homemade, detuned guitar and a soft drum machine,
     androgynous close vocal, lo-fi warmth, 96 BPM, E major
  34 1980s stadium pop-rock, enormous, gated drums and bright guitar with
     synth pads, male high tenor, huge reverberant mix, 126 BPM, D major
  35 chamber pop, ornate, piano and string quartet with woodwind touches,
     female alto, close intimate recording, 88 BPM, A major

  ATMOSPHERIC AND EXPERIMENTAL
  36 dungeon synth, lonely and primitive, thin sustained synth choirs and a
     simple modal melody, no vocals, deliberately degraded, slow, D minor
  37 hauntology, unsettling, decayed tape loops and a detuned childrens'
     piano, distant wordless voice, wow and flutter throughout, slow, E minor
  38 modern IDM, restless, intricate broken percussion with warm generative
     pads, no vocals, precise wide mix, 108 BPM, F♯ minor
  39 drone metal, immense, sustained downtuned guitar chords with feedback
     and no percussion, no vocals, overwhelming and slow, no fixed tempo, C
  40 musique concrète collage, disorienting, field recordings and processed
     objects with sparse piano, no vocals, close and dry, no tempo, no key

  MORE ROOTS AND WORLD
  41 New Orleans second line, celebratory, sousaphone and snare with a full
     brass section, group vocal shouts, live street recording, 96 BPM, B♭
  42 Ethiopian jazz, hypnotic and modal, vibraphone and saxophone over a
     loping rhythm section, instrumental, warm vintage mix, 104 BPM, C minor
  43 Balkan brass, frantic and joyous, massed brass with a driving snare and
     tuba bass, group shouts, live outdoor recording, 168 BPM, D minor
  44 Nordic folk, austere, nyckelharpa and frame drum with unison female
     voices, cold open-air acoustics, 92 BPM, D minor
  45 Andean folk, plaintive, charango and pan flute over a gentle percussion
     pattern, male voice high and open, natural mountain space, 108 BPM, A minor

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. TASK SCENARIOS
═══════════════════════════════════════════════════════════════════

<rag_zone id="task_scenarios">

Recipes organised by what the music is *for* rather than by genre. This is
how most requests actually arrive.

─── UNDER A VIDEO ───

```
an understated instrumental bed for video, warm and unobtrusive, sustained
pads with a sparse piano figure and light brushed percussion, no vocals,
even throughout with no sudden changes, nothing drawing attention to
itself, slow, C major
```

  Say "nothing drawing attention to itself" explicitly. Without it you get
  music that wants to be listened to, which is the opposite of a bed. If the
  music must hit specific cut points, use Lyria with timestamps
  (DATA_GOOGLE §4) rather than a generic bed.

─── PODCAST INTRO ───

```
a fifteen-second podcast opener, confident and modern, a plucked synth
motif over a light electronic pulse with one warm chord swell, no vocals,
resolves cleanly rather than fading, 110 BPM, D major
```

  Must resolve, not fade — a fade under a speaking voice sounds like a
  mistake. Keep it to one idea.

─── ADVERTISING ───

```
a sixty-second advertising bed, optimistic and building, acoustic guitar
and handclaps growing into a full arrangement with a wordless vocal hook,
lands on its biggest moment two thirds of the way through, then falls away,
95 BPM, C major
```

  Name where the hero moment lands. For anything a client will pay for,
  generate on a platform with clean licensing (DATA_OTHER §6).

─── GAME MUSIC · EXPLORATION ───

```
a calm exploration loop for a game, curious and unhurried, sparse harp and
sustained strings over a low drone, no percussion, no vocals, loops
seamlessly with no clear beginning or end, very slow, D minor
```

  For music that responds to what the player does, a steered stream is the
  better tool (DATA_GOOGLE §1).

─── GAME MUSIC · COMBAT ───

```
a combat loop for a game, urgent and driving, hammering low percussion with
tremolo strings and stabbing brass, no vocals, high tension held throughout
without resolving, loops seamlessly, 150 BPM, D minor
```

  Same key as the exploration loop above so the two can cross-fade.

─── WORKOUT ───

```
a relentless workout track, aggressive and forward-driving, hard electronic
drums with a distorted bass and a repeating synth motif, male vocal shouting
short phrases, loud modern mix, energy never drops, 150 BPM, F minor
```

  "Energy never drops" is the whole brief — a normal song structure has a
  quiet bridge, which is wrong here.

─── SLEEP AND FOCUS ───

```
an extremely slow sleep piece, still and unresolved, sustained low pads with
almost imperceptible movement, no percussion, no vocals, no melody, nothing
that could startle, enormous soft space, no fixed tempo, A minor
```

  "Nothing that could startle" prevents the sudden dynamic events that ruin
  this category. For long durations, Stable Audio (DATA_OTHER §2).

─── WEDDING OR CEREMONY ───

```
a tender ceremonial piece, warm and unhurried, solo piano with a string
quartet entering gently, no vocals, builds once and resolves fully, close
intimate recording, slow, F major
```

  Resolve fully. Ceremonial music that ends unresolved feels wrong in a way
  people notice without being able to say why.

─── SHORT-FORM VIDEO HOOK ───

```
a fifteen-second hook built to loop, bright and immediate, one memorable
synth motif over a punchy beat, female vocal singing a single repeated
phrase, starts at full energy, seamless loop, 128 BPM, A minor
```

  No introduction. Start at full energy — the listener may arrive at any
  point and will leave in seconds.

─── CORPORATE PRESENTATION ───

```
a neutral corporate underscore, positive and unobtrusive, plucked strings
and light marimba over a soft pulse, no vocals, steady with a single gentle
lift, clean modern mix, 108 BPM, C major
```

  Deliberately unremarkable. This is the one brief where "generic" is the
  correct answer rather than a failure.

─── MEDITATION AND GUIDED AUDIO ───

```
a meditation underscore, warm and completely even, a single sustained low
drone with a slow harmonic movement above it, no percussion, no melody, no
vocals, nothing that resolves or arrives, enormous soft space, no fixed
tempo, D major
```

  Major key rather than minor — meditation audio in a minor key reads as
  melancholy to most listeners. No arrival points at all: anything that
  sounds like an event pulls attention back out.

─── CHILDREN'S MUSIC ───

```
a cheerful song for young children, simple and warm, ukulele and glockenspiel
over a light shaker pulse with a plain bass, bright friendly female voice
singing clearly and slowly, clean uncluttered mix, 108 BPM, C major
```

  Diction matters more than anything else here. Ask for clear, unhurried
  delivery explicitly. Keep the arrangement thin — busy backing masks words
  that a child is still learning to parse.

─── RETRO GAME ───

```
a chiptune level theme, bright and relentless, square-wave lead over a
pulse bass with noise-channel percussion, no vocals, deliberately limited
to a handful of voices, dry and direct, loops seamlessly, 150 BPM, A minor
```

  "Deliberately limited to a handful of voices" is what makes it read as
  authentic rather than as a synth pastiche. Loops matter: state it.

─── DOCUMENTARY STING ───

```
a five-second documentary transition, sombre and restrained, a single low
piano note with a rising string swell resolving into silence, no percussion,
no vocals, close and dry, very slow, A minor
```

  Very short pieces need the ending stated, because the model will otherwise
  spend the whole duration building. Say what the last moment is.

─── HOLIDAY AND SEASONAL ───

```
a warm traditional Christmas song, nostalgic and gentle, sleigh bells and
brushed drums under an upright piano with a soft string pad, male crooner
close and unhurried, vintage warm mono-leaning mix, 92 BPM, E♭ major
```

  The genre is mid-century pop with one instrument added. Sleigh bells and a
  crooned delivery do more work than any amount of seasonal vocabulary in
  the lyric.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. ONE IDEA, EVERY PLATFORM
═══════════════════════════════════════════════════════════════════

<rag_zone id="cross_platform_recipe">

The same brief rendered for each covered platform, demonstrating menu [8]
ALL mode. Formats are never mixed — each target gets its own dialect
(CORE_00 §6).

BRIEF: a melancholy song about standing outside in the rain at three in the
morning.

─── 🟠 SUNO ───

Style:
```
early-2000s Reykjavík post-rock, melancholic and vast, fingerpicked acoustic
guitar with a warm cello swell and soft brushed drums, female alto with a
slight quaver, close-miked, lo-fi analog warmth, 82 BPM, A minor
```

Lyrics:
```
[Intro]
[Rain]

[Verse 1]

[Chorus]

[Verse 2]

[Chorus]

[Bridge — voice and guitar only]

[Outro]
[Fade Out]
```

─── 🔵 LYRIA ───

Google's framework order, tempo described, structure as timestamps:
```
An early-2000s Icelandic post-rock song, melancholy and vast. Fingerpicked
acoustic guitar, a warm cello swell and soft brushed drums. A slow,
unhurried pace that never pushes. A female alto with a slight quaver in it,
recorded very close, singing in English.
Lyrics: a song about standing outside in the rain at three in the morning.

[00:00] Rain, then a single fingerpicked guitar alone.
[00:20] The voice enters, quiet and close.
[00:50] Cello swells underneath and brushed drums arrive.
[01:40] Everything falls away to voice and guitar.
[02:10] The full arrangement returns, larger than before.
[02:50] Ends on a held cello note fading into the rain.
```

─── 🟢 FLOW MUSIC ───

```
SEED     the Lyria prompt above, without the timestamps
REPLACE  "Replace only the brushed drums with a slower, softer pattern.
          Keep the guitar and cello exactly as they are."
EXTEND   "Continue in the same Icelandic post-rock style, same tempo and
          instrumentation, building to a final swell and then resolving."
```

─── 🟣 ELEVENMUSIC ───

```
An early-2000s Icelandic post-rock song, melancholy and vast. Fingerpicked
acoustic guitar, a warm cello swell, soft brushed drums. A female alto with
a slight quaver, close and unpolished. Builds slowly from almost nothing,
falls away completely in the middle, and returns larger.
```
  Sections then arranged and regenerated in the interface.

─── 🟡 STABLE AUDIO ───

Instrumental, which is what it is for:
```
A slow, vast instrumental post-rock piece. Fingerpicked acoustic guitar, a
warm cello swell arriving late, soft brushed drums. Melancholy and
unresolved. Builds gradually and never fully releases. Instrumental.
```

─── WHAT CHANGED BETWEEN THEM ───

The six layers are identical in all five. What changed: bracket markup
appears only for Suno, tempo is a number only for Suno, structure is
timestamps only for Lyria, and the vocal disappears entirely for Stable
Audio. Conversion checklists: DATA_GOOGLE §9, DATA_OTHER §9.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. BUILDING YOUR OWN LIBRARY
═══════════════════════════════════════════════════════════════════

<rag_zone id="style_library">

The most useful thing in this file is the habit, not the contents: when a
generation comes back right, save the Style description before you change
anything.

─── THE PATTERN ───

Fix the Style, vary the lyrics. A saved Style description plus new words
produces a body of work that sounds like one artist rather than a pile of
unrelated tracks. This is the cheapest route to a consistent sound, and it
requires no training and no subscription.

─── WHAT TO RECORD ───

```
NAME       something you will recognise in six months
TARGET     which platform this was written for
STYLE      the exact description, unedited
SETTINGS   tempo, key, slider posture
EXCLUDE    what you excluded, if anything
WORKS FOR  the kind of song this suits
CHANGE     the one element you vary between tracks
```

─── AN ENTRY ───

```
NAME       Cold Northern Folk-Rock
TARGET     Suno
STYLE      1991 post-Soviet dark folk-rock, brooding and ominous, resonant
           acoustic guitar with a haunting violin and a distorted bass
           underneath, male gravelly weathered baritone, close-miked, cold
           analog warmth, 85 BPM, A minor
SETTINGS   85 BPM · A minor · genre-faithful posture
EXCLUDE    bright cheerful production, electronic drums, autotune
WORKS FOR  atmospheric narrative songs, anything post-industrial
CHANGE     the vocal persona — the same arrangement carries a female alto
           without any other edit
```

─── KEEP IT OUTSIDE THE PLATFORM ───

Keep your library in your own notes, not only in the platform's history.
Interfaces get rebuilt, accounts change, and generation history is not a
backup — Flow Music's users lost every past session and trained model in a
single migration (DATA_GOOGLE §7).

─── WHEN A LIBRARY IS NOT ENOUGH ───

If you want a consistent sound across dozens of tracks and a saved Style is
not holding it, the next step is a model trained on your own catalogue —
requirements, limits and the rights you must hold are in DATA_SUNO §6.

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_RECIPES.md · SunoForge v3.0
// Next: DATA_POSTPROD.md
// ═══════════════════════════════════════════════════════════════
