<sunoforge_file id="DATA_BLANKS" version="5.0" layer="data" role="templates" source="DATA_BLANKS.md">
<file_meta>
file_id: DATA_BLANKS
version: "5.0"
layer: data
role: templates
description: >
  A ready blank for every menu entry and sub-entry: what to ask in one line, the fill-in
  skeleton the user sees, a filled example, and the one tip with its reason. Read when an
  entry or a code is picked (CORE_00 §4 ENTRY SCREEN) and for "N adapt". Not a reference: the
  blank is shown, then filled from the conversation. Platform facts stay in DATA_SUNO,
  DATA_GOOGLE, DATA_OTHER; the methods behind each blank stay in CORE_01, CORE_02, CORE_03.
scope: blanks · entry_screens · asks · fill_in_skeletons · examples · tips
depends_on: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS]
used_by: [CORE_00_ENTRY]
updated: "2026-11-05"
</file_meta>

# 🧩 SUNOFORGE v5.0 — BLANKS
# File 14 of 14 · DATA layer · one blank per menu entry

> A menu entry is not a chapter to read; it is a form to fill. When an entry or a code is
> picked, the ENTRY SCREEN of CORE_00 §4 shows the submenu AND the entry's blank from here:
> the ASK (one question with an example answer), the BLANK (slots in ⟨angle brackets⟩, shown
> in a code block the user can edit or ignore), and the TIP with its reason — then the result.
> The user may answer the ASK in plain words, fill the blank, or say "fill it" — then every
> slot is filled from the conversation and the result follows at once (CORE_00 §6 RESULT
> FRAME). A slot the user leaves empty is a decision for SunoForge, named in "why this works".
> Slots are never shown as a questionnaire of several questions: one ASK, one blank, one go.

<section id="§1" title="HOW A BLANK IS SHOWN">

```
[N] NAME — the promise                       ← as in the menu
one or two sentences: what this entry changes in the song
`codes` — the sub-entries, one line each      ← SUB-ENTRIES at the head of the section

ASK:   one question, with an example answer in brackets
BLANK: (a code block)
       ⟨slot⟩ — what goes here, a few words
       …
TIP:   one sentence · WHY: one sentence
EXAMPLE: the blank filled once, one line — shown under the blank so the user sees a finished one
→ "fill it", answer the ask, or edit the blank · the most likely next codes · menu
```

Rules: the blank is translated into OUTPUT_LANG, slot names included; the filled result
keeps generator text in English (CORE_00 §9 LANGUAGE). A sub-entry with its own blank
below shows that one instead of the entry's. A catalogue code (`5a`, `9`) shows the
catalogue, and "N adapt" uses the ADAPT blank of §16. When the user asks for a form, the
blank's slots become the BUILDER form of CORE_00 §9 (one choice per slot, free text
allowed); otherwise the blank stays text. An entry without its own ASK or TIP shows none —
nothing is invented to fill the shape. Every code has an EXAMPLE (the EXAMPLES list at the
end of its section, or a catalogue of ready items); a pick shows its example under its blank,
and "this one" or "like the example" fills the blank with it.

</section>

<section id="§2" title="[1] QUICK START — the song brief">

SUB-ENTRIES — plain words are enough; a photo works too, and with a Suno server connected a video or a hummed memo goes in through Suno's uploader.
VARIANT_COUNT variants (two by default), each a different reading of the idea. No sub-entries:
the first answer is the result.

ASK: What is the song about, and what should the listener feel at the end? ("my
brother's wedding — happy and a bit teary")

BLANK:
```
⟨about⟩        — the subject in one line, a real moment beats a theme
⟨feeling⟩      — ONE feeling at the end; "and also" → pick one
⟨image⟩        — one picture or physical detail that anchors it
⟨hook⟩         — a phrase worth repeating, draft words welcome
⟨energy⟩       — low · mid · high, plus a texture word ("calm authority")
⟨voice⟩        — who sings: gender, age, character — or "surprise me"
⟨generator⟩    — Suno (default) · Lyria · Flow · Eleven · Stable · MiniMax · local
```
Filled example: wedding toast for a brother · joy with a lump in the throat · the two of
them dancing in a kitchen at 2 a.m. · "we were never good at goodbyes" · mid, warm ·
male, thirty-something, slightly hoarse · Suno v6.

TIP: start from a moment, not a genre — the genre comes out of the moment. WHY: a genre
alone gives the model nothing to decide; a kitchen at 2 a.m. decides tempo, instruments
and the voice for it (CORE_01 §3 Time & Place).

Output: two or three readings of the brief (CORE_00 §3 variants), each a full blueprint.

</section>

<section id="§3" title="[2] STUDIO — the studio sheet">

SUB-ENTRIES — `2a` genre and era · `2b` instruments · `2c` the voice: gender, height, delivery
· `2d` tempo and key · `2e` production and space · `2f` song form · `2g` sliders: Weirdness,
Style Influence, Variety (the Suno app, and the connector since 2026-11-05) · `2h` what to exclude · `2i` edit a
finished song in plain words — one section, one line (Suno app: Replace with a hint, two
versions to choose from) · `2j` Max Mode — only when you ask for it by name; through the MCP
too, on a plan that has it · `2k` a long song — up to 6 min a call, longer by extend and join
(`15f`); up to 8 min in the Suno app

ASK: Which parameters do you want to set yourself — all of them, or just a few?
("tempo, key and the voice; choose the rest")

BLANK (the whole sheet; the sub-entries `2a`–`2h` are its rows):
```
2a ⟨genre⟩ + ⟨era⟩ + ⟨place⟩      — "1980s Sunset Strip metal", not "metal"
2b ⟨hero instrument⟩, ⟨bed⟩        — one instrument that leads, two or three behind it
2c ⟨voice⟩                         — gender · height (high, middle, low) · delivery
2d ⟨tempo⟩ BPM, ⟨key⟩              — numbers as prose: "96 BPM, A minor"
2e ⟨production⟩                    — room, era of the gear, polish or grit, stereo width
2f ⟨form⟩                          — verse–chorus · AABA · build-and-drop · through-composed
2g Weirdness ⟨N⟩% · Style Influence ⟨N⟩% · Variety ⟨0 | default⟩
2h ⟨exclude⟩                       — 8–12 terms that are the opposite of the target
```
A row left empty is chosen by SunoForge from the rest of the sheet and named in "why".
Slider postures by genre: DATA_SUNO §8; descriptor words: DATA_VOCAB.

TIP: fill 2a and 2c first — they carry the most weight at the front of the Style field.
WHY: Suno front-loads (CORE_00 §7 rule 1); the voice's gender and character are the
least random control the text has (rule 4).

`2i` EDIT A FINISHED SONG — ASK: which section, what changes, what stays? BLANK:
```
⟨section⟩ — chorus · verse 2 · bridge · the last 20 seconds
⟨change⟩  — one change, in plain words: "sung by a gospel choir", "half the tempo"
⟨keep⟩    — what must not move: the melody · the words · the key
⟨hint⟩    — optional, for Suno's Replace: "make it dreamier" (DATA_SUNO §7)
```
Output: the edit instruction for the Suno app (Replace Section, Song Editor) — no MCP
tool does this; and the same change as a blueprint diff for a new take.

`2j` MAX MODE — no blank: a yes/no and the reason. TIP: ask for it by name for songs over
two minutes, close covers and whole-track consistency. WHY: it costs a multiple of the
credits and through the MCP it is sent only when you name it (DATA_SUNO_LIVE §3).

`2k` A LONG SONG — BLANK: `⟨total length⟩ · ⟨parts⟩: part 1 ⟨what⟩, part 2 ⟨what⟩ …` —
up to 6 min a call; longer by extend and a free join (`15f`); 8 min in the Suno app.

EXAMPLES — one filled line each:
- `2a`–`2h` (the sheet): 1990s Bristol trip-hop · a Rhodes leads, a dusty breakbeat and sub bass behind · female, low and smoky, half-spoken · 84 BPM, D minor · a small room, tape, narrow stereo · verse–chorus with a bridge · Weirdness 40% · Style Influence 60% · exclude: EDM, autotune, bright pop
- `2i`: the chorus · sung by a gospel choir · keep the words and the key · hint: bigger, warmer
- `2j`: a 4-minute ballad that must stay one voice to the end → yes, Max Mode, by name
- `2k`: 9:00 · part 1 intro and two verses, 5:30 · part 2 bridge, last chorus, a long outro, 3:30

</section>

<section id="§4" title="[3] CLONE A STYLE — the DNA sheet">

SUB-ENTRIES — `3a` from an audio file (your own audio: a Suno MCP upload returns its sung
lyrics and style, free) · `3b` from an artist, copyright-safe · `3c` "like that track, but…" · `3d` cover in
another style · `3e` mashup of exactly two songs · `3f` sample a riff and build a new beat ·
`3g` Inspire — a playlist of 3–5 of your own songs steers the new one (Suno app)

`3a` FROM AN AUDIO FILE — ASK: attach the file (or paste what you hear) — what in it do
you want to keep? ("the drum sound and the room, not the melody") BLANK:
```
⟨timbre⟩   — bright · dark · warm · airy; the one instrument that defines it
⟨dynamics⟩ — percussive or sustained; compressed flat or breathing
⟨groove⟩   — behind the beat · pushed · swung · straight; the BPM if you know it
⟨space⟩    — close and dry · wide · a hall · a bedroom; stereo width
⟨keep⟩ / ⟨drop⟩ — what to carry over, what to leave behind
```
With a Suno server: an upload returns the sung lyrics, a style line and a description
for free (DATA_SUNO_LIVE §3) — the sheet starts filled. Only audio the user holds the rights
to: the upload lands in their Suno library under Suno's upload licence (DATA_LEGAL §10), so
say that in one line and wait for a yes; someone else's record → describe it, or paste what
you hear. TIP: 15–30 seconds of the most
characteristic part beat the whole track. WHY: a short fragment has one timbre and one
groove to read; a whole song averages them (CORE_01 §12).

`3b` FROM AN ARTIST — BLANK: `⟨artist⟩ → ⟨era of theirs⟩ · ⟨three traits of the sound⟩ ·
⟨what of it you want⟩`. The name never reaches the generator: the traits do (CORE_01 §12
translation table). TIP: name the record, not the artist. WHY: one artist has five
sounds; a record has one.

`3c` "LIKE THAT TRACK, BUT…" — BLANK: `like ⟨track or sound⟩, but ⟨one change⟩, keep
⟨what⟩`. One "but" per take.

`3d` COVER — BLANK: `⟨source song: a library song, an upload, or a description⟩ → in the
style of ⟨genre + era⟩ · ⟨voice⟩ · ⟨keep the lyrics: yes/no⟩`. With a Suno server the
cover takes a library song by id (`15d`); the source's lyrics must be passed in or the
cover comes back instrumental (DATA_SUNO_LIVE §3).

`3e` MASHUP — BLANK: `⟨song A⟩ + ⟨song B⟩ → ⟨what from A⟩, ⟨what from B⟩, ⟨new lyrics or
none⟩`. Exactly two songs; through the MCP a mashup sings only with lyrics given.

`3f` SAMPLE A RIFF — BLANK: `⟨the riff: where in the track, mm:ss⟩ → ⟨what to build on it⟩
· ⟨tempo⟩ · ⟨genre of the new beat⟩`.

`3g` INSPIRE — BLANK: `⟨3–5 of your own songs⟩ (a playlist on suno.com) → ⟨the new song's
subject and lyrics⟩ · ⟨what the playlist should lend: mood · tempo · instruments⟩`. In the
Suno app: Custom mode, +Inspo above the lyrics (DATA_SUNO §7). No MCP tool. TIP: three to
five songs. WHY: Suno's own advice — a long playlist averages into nothing.

EXAMPLES — one filled line each:
- `3a`: warm, a felt piano defines it · breathing, little compression · behind the beat, about 70 BPM · a small wooden room, narrow · keep the piano and the room, drop the melody
- `3b`: a 1990s trip-hop record → its early sound · vinyl crackle, spy-film strings, a broken slow beat · the mood, not the voice
- `3c`: like an 1980s synth-pop ballad, but on acoustic guitar, keep the gated drums
- `3d`: my song "Neon Rain" → in the style of 1960s bossa nova · a soft male voice · keep the lyrics: yes
- `3e`: "Neon Rain" + "Kitchen at 2 a.m." → the beat of A, the chorus mood of B, new lyrics: none
- `3f`: the guitar riff at 0:42 → a boom-bap beat on it · 88 BPM · lo-fi hip-hop
- `3g`: three of my night-drive songs → a new song about leaving the city · lend the mood and the tempo

</section>

<section id="§5" title="[4] HYBRID LAB — the bridge sheet">

SUB-ENTRIES — `4a` ready pairs that work · `4b` your own mix through a bridge genre · `4c` what
refuses to blend · `4d` hand it to v6-wild, Suno's model built for exploration

ASK: Which two worlds, and which of them leads? ("phonk and jazz, phonk leads")

BLANK:
```
⟨genre A⟩ (leads)   — its rhythm or its sound carries the song
⟨genre B⟩           — what B lends: ⟨one instrument⟩, ⟨one habit⟩ (a chord, a groove)
⟨bridge⟩            — the third thing both can live in: lo-fi · cinematic · dub · folk
⟨where they meet⟩   — intro A, verse B, chorus both — or all at once
```
`4a` shows the ready pairs of CORE_01 §10 as a catalogue; `4b` is the sheet above with your
own two worlds; `4c` the anti-pairs; `4d` sends the sheet to v6-wild instead of a bridge. TIP: name the bridge, not the sum. WHY: "orchestra
+ dubstep" is a collision; "cinematic bass music" is a genre the model has heard.

EXAMPLES — one filled line each:
- `4b`: phonk (leads) · jazz lends a muted trumpet and ii–V turnarounds · bridge: lo-fi · verses phonk, the chorus both
- `4a`: the ready pairs are the examples — pick one by number
- `4c`: "orchestra + dubstep" → why it collides, and the bridge that saves it: cinematic bass music
- `4d`: the sheet of `4b` → v6-wild, no bridge named, Weirdness 70%

</section>

<section id="§6" title="[5] VOICES — the persona sheet">

SUB-ENTRIES — `5a` ten ready voices — pick one and adapt it · `5b` your own singer from a
description · `5c` duet — two voices that stay apart · `5d` emotion delivery · `5e` your own
recorded voice (Suno Voices; used through the MCP, recorded in the Suno app) · `5f` Custom
Models — a model trained on your catalogue (Suno Pro/Premier, Suno app) · `5g` Google vocal
profiles for Lyria

On the [5] screen, under the codes, four ready voices as quick picks — 01 soul alto
(female), 04 pop soprano (female), 03 weathered baritone (male), 08 rap storyteller — and
"all ten" (`5a`); the user's own personas, when the library has any, beside them.

`5a` TEN READY VOICES — the catalogue of CORE_01 §7 (01–10) as cards: number, name, the voice
in a few words; a pick shows its long and short form, then "N adapt" (§16). After the ten,
YOURS: the personas saved in the library (KIND persona), picked by name; then "+ your own"
(`5b`). A persona built or adapted here is kept with `save persona NAME` and shows under
YOURS from then on. `5b` YOUR OWN SINGER — ASK: tell me about the singer the way
you'd describe a friend's voice ("a woman around forty, smoky, sings like she's tired of
the song but means it") BLANK:
```
⟨name⟩        — for your library
⟨gender⟩      — female · male · a duet (→ 5c)
⟨height⟩      — high and light · middle · low and deep
⟨age⟩ and ⟨character⟩ — "late twenties, restless", "a grandfather telling it again"
⟨how sung⟩    — behind the beat · precise · belting · half-spoken
⟨how recorded⟩ — close and dry · a warm room · a stage · a phone in a kitchen
```
Output: the long form (for the library) and the short form (goes into Style), and how to
keep her the same across songs (CORE_01 §7); then `save persona ⟨name⟩` — it shows under
YOURS in `5a` from then on. TIP: three to seven traits. WHY: more than
ten and the model averages them into a generic voice [COMMUNITY].

`5c` DUET — BLANK: `⟨voice 1⟩ vs ⟨voice 2⟩ — polar registers · who sings ⟨which
sections⟩ · ⟨the chorus: both, who above⟩`. Three anchors: Style, the first lyrics line,
every section (CORE_02 §9). `5d` EMOTION — BLANK: `⟨section⟩ → ⟨delivery word⟩` per
section (CORE_02 §6). `5e` YOUR OWN VOICE — no blank: voices-list → a voice id; none → the
suno.com link (DATA_SUNO_LIVE §7). `5f` CUSTOM MODELS — the Suno app (DATA_SUNO §6).
`5g` LYRIA PROFILES — the vocal profiles of DATA_GOOGLE §5.

EXAMPLES — one filled line each:
- `5a`: "04" → the pop soprano in both forms · "04 adapt" for a birthday song in Russian
- `5b`: Mara · female · low and deep · around forty, tired but tender · behind the beat, half-spoken · close and dry → `save persona Mara`
- `5c`: a cracked male baritone vs a clear female soprano · he sings the verses, she the pre-chorus · the chorus both, she above
- `5d`: verse 1 → whispered · chorus → belted · bridge → spoken
- `5e`: voices-list → "My voice 1" → the next song sung in it
- `5f`: 24 of your own songs in one style (six is the floor) → a model trained and picked in the Suno app, Pro or Premier
- `5g`: Lyria, Female Alto: "rich, warm, and husky lower range" — Google's own profile words

</section>

<section id="§7" title="[6] LYRICS AND MARKUP — the lyric sheet">

SUB-ENTRIES — `6a` lyrics on a theme, marked up · `6b` structure for an instrumental · `6c`
delivery: whisper, belt, stretch · `6d` chords for the genre · `6e` backing vocals, ad-libs,
spoken lines · `6f` Lyricist, Suno's own lyrics helper (Suno app) · `6g` replace one sung line
in a finished song (Suno app) · `6h` the same lyrics laid out for Lyria, MiniMax, local models

`6a` LYRICS ON A THEME — ASK: what is the song about, from whose point of view, and what
is the one line that must be in it? BLANK:
```
⟨theme⟩      — the subject, one line
⟨voice⟩      — I · you · we · a narrator; present or past
⟨truth⟩      — the one sentence the song proves
⟨hook⟩       — the line to repeat, or "write one"
⟨form⟩       — verse–chorus · with a bridge · AABA · a story in verses
⟨language⟩   — the song's language; the markup stays English
⟨length⟩     — about ⟨N⟩ words or ⟨M:SS⟩
```
TIP: short lines, one idea per section. WHY: a lyric written as an essay is unsingable;
the model stretches or swallows it.

`6b` STRUCTURE FOR AN INSTRUMENTAL — BLANK: `[Intro ⟨what⟩] → [⟨section⟩ ⟨what enters⟩] →
… → [Outro ⟨how it ends⟩]` with a word on each section, labels only, nothing sung.
`6c` DELIVERY — BLANK: `⟨section⟩: ⟨whisper · belt · stretch · spoken · falsetto⟩`, one per
section, on its own line (CORE_02 §5–§6). `6d` CHORDS — BLANK: `⟨genre⟩ · ⟨key⟩ → a
progression in parentheses before the beats` (CORE_02 §10). `6e` BACKING, AD-LIBS, SPOKEN
— BLANK: `⟨line⟩ (⟨backing words⟩)` — round brackets are sung, square are not.
`6f` Lyricist and `6g` one-line replace — the Suno app (DATA_SUNO §7, §11). `6h` THE SAME
LYRICS FOR LYRIA, MINIMAX, LOCAL — no blank: paste the lyrics, get them laid out per
platform (CORE_00 §6).

The user's own lyrics are never rewritten (CORE_00 §7 rule 9a): the blank adds labels and
delivery around them.

EXAMPLES — one filled line each:
- `6a`: leaving a hometown · I, past tense · you can go back to a place, never to a time · "the porch light still burns for no one" · verse–chorus with a bridge · Russian · about 180 words
- `6b`: [Intro: rain and a lone piano] → [Build: strings enter] → [Drop: full drums] → [Outro: the piano alone]
- `6c`: verse 1: whisper · chorus: belt · bridge: spoken
- `6d`: lo-fi hip-hop · A minor → (Am7 – Dm9 – G7 – Cmaj7)
- `6e`: I keep the light on (keep it on) — the round brackets are sung, [Spoken] is not
- `6f`: the writing voice of your last three songs → Lyricist keeps it for the next one, in the Suno app's lyrics editor
- `6g`: the second line of the chorus, "the night was long" → "the road was long", in the Suno app
- `6h`: your verse–chorus lyrics → the same text under Lyria's `Lyrics:` header, and laid out for a local model

</section>

<section id="§8" title="[7] OTHER GENERATORS — one blank per dialect">

SUB-ENTRIES — `7a` Lyria Clip, 30 s sketches · `7b` Lyria 3.5, full songs · `7c` music for a
photo · `7d` music for a video · `7e` image references · `7f` music timed to the cuts `[0:00 -
0:10]` · `7g` Google Flow Music · `7h` Lyria RealTime · `7i` ElevenMusic · `7j` Stable Audio ·
`7k` MiniMax and local models on your own GPU · `7l` the Gemini app

`7b` LYRIA 3.5 — BLANK (genre first, prose, then ranges):
```
⟨genre⟩, ⟨era⟩, ⟨mood⟩, ⟨instruments⟩, ⟨vocal profile⟩, ⟨BPM⟩, ⟨key⟩
[0:00 - 0:⟨N⟩] Intro: ⟨what is heard first⟩
[0:⟨N⟩ - ⟨M⟩] Verse 1: ⟨what enters, how the vocal sounds⟩
[… - …] Chorus: ⟨the lift⟩ · [… - …] Outro: ⟨how it ends⟩
Lyrics: [Verse 1] … [Chorus] … (backing in parentheses)
```
`7a` LYRIA CLIP — the same, 30 s, no sections. `7c` PHOTO · `7d` VIDEO → BLANK: `⟨attach⟩ ·
⟨what in it to score: the light · the motion · the cuts⟩ · ⟨length⟩`. `7e` IMAGE REFERENCES →
BLANK: `⟨images⟩ · ⟨what each lends: colour → mood, place → era, texture → production⟩`
(DATA_GOOGLE §6). `7h` LYRIA REALTIME → BLANK: `⟨the starting prompt⟩ · ⟨what changes over
time and when⟩ · ⟨the weights⟩` (DATA_GOOGLE §8). `7f` TIMED TO THE
CUTS — BLANK: the ranges above, one per cut. `7g` FLOW MUSIC · `7i` ELEVENMUSIC · `7j`
STABLE AUDIO · `7k` MINIMAX AND LOCAL — BLANK: `⟨idea⟩ · ⟨length⟩ · ⟨vocal or
instrumental⟩ · ⟨the platform's own fields⟩` — the fields and the shape: DATA_GOOGLE §3
(Google), DATA_OTHER §1–§3, §5 (read on request, CORE_00 §9 LOADING). `7l` the Gemini app
— DATA_GOOGLE §2 (surfaces), §10 (choosing within Google).

EXAMPLES — one filled line each:
- `7a`: 30 s · a lo-fi loop: rain, Rhodes, vinyl crackle, 75 BPM
- `7b`: dream pop, 1990s, wistful, shimmering guitars and a soft drum machine, a breathy female vocal, 92 BPM, E major · [0:00 - 0:12] Intro: reverb guitar alone · [0:12 - 0:40] Verse 1: the voice close and quiet · Chorus: the drums open up
- `7c`: a photo of a foggy pier at dawn · the cold light and the stillness · 30 s
- `7d`: a 45-second skate clip · the cuts and the falls · 45 s
- `7e`: three images · a neon street → night mood · an old radio → the 1960s · chrome → a glossy mix
- `7f`: [0:00 - 0:10] calm · [0:10 - 0:18] the hit on the cut · [0:18 - 0:30] it resolves
- `7g`: a 2-minute ambient piece for a meditation app · instrumental · Flow's own fields
- `7h`: deep house, 122 BPM · at 1:00 strings come in, at 2:00 drums only · weights: deep house 1.0, strings 0.6
- `7i`: a 60-second jingle for a coffee shop · vocal · ElevenMusic's own fields
- `7j`: a 90-second drone bed for a podcast · instrumental · Stable Audio's own fields
- `7k`: a 3-minute rock song with your lyrics · vocal · on your own GPU
- `7l`: a 30-second birthday clip from a photo, made in the Gemini app

</section>

<section id="§9" title="[8] ONE IDEA, SEVERAL GENERATORS">

SUB-ENTRIES — `8a` two generators side by side · `8b` every generator at once

BLANK: `⟨idea in one line⟩ → ⟨platform 1⟩ · ⟨platform 2⟩ (8a) or all (8b)`. Output: the
same song in each platform's own format, side by side, and one line on where they differ.

EXAMPLES — one filled line each:
- `8a`: a sea shanty about debugging at 3 a.m. → Suno v6 · Lyria 3.5
- `8b`: the same idea → every generator on your list, side by side

</section>

<section id="§10" title="[9] RECIPES">

SUB-ENTRIES — genres · hybrids · duet · 45 presets by group · task scenarios (an ad, a lullaby,
a game loop); the buttons send `9 recipes` · `9 hybrids` · `9 presets` · `9 tasks` — that group of DATA_RECIPES (§2 · §3 · §5 · §6) as a numbered list; a catalogue item sends "recipe <name>" / "preset <N>" / "task <name>"

The catalogue (DATA_RECIPES §2–§6) with its own numbers; a pick is `preset ⟨N⟩`, `recipe
⟨name⟩`, `task ⟨name⟩`. BLANK after a pick: `⟨preset⟩ for ⟨my song: subject · voice ·
length⟩` → the preset adapted (§16). TIP: a preset is a starting posture, not a verdict.
WHY: its sliders and key fit the genre; your song decides the rest.

EXAMPLES — one filled line each:
- after a pick: preset 12 for my song: a birthday song for my mother · a female voice · 2:30
- yours: a recipe you saved with `save recipe NAME` shows after the ready ones and is picked by name

</section>

<section id="§11" title="[10] WHICH GENERATOR — three questions">

SUB-ENTRIES — the decision tree, one question at a time (DATA_OTHER §7)

BLANK (answered one at a time, or all at once):
```
⟨length⟩      — a 30-second sketch · a 3–4 minute song · over 6 minutes
⟨rights⟩      — for myself · for a client or a release · for film, TV, a game
⟨after⟩       — done is done · I will edit parts · I need stems · I need my own voice
⟨where⟩       — in a browser · offline, own GPU · inside a DAW · live, reacting
```
→ the decision tree of DATA_OTHER §7 (read on request) gives one or two platforms and why.

EXAMPLES — one filled line each:
- a 3–4 minute song · for a release · I need stems · in a browser

</section>

<section id="§12" title="[11] RIGHTS BEFORE RELEASE — the release check">

SUB-ENTRIES — the topics of DATA_LEGAL: plans · a paid download · remixes · voices and
catalogues · artist names · streaming policies · AI labelling

BLANK:
```
⟨platform⟩ and ⟨plan⟩        — Suno free / pro / premier · Lyria · Eleven · Stable · local
⟨how it was made⟩            — from scratch · a cover of ⟨whose⟩ · with ⟨whose⟩ voice · a remix
⟨where it goes⟩              — streaming · a client · film / TV / game · just friends
⟨downloaded how⟩             — in the app with a paid credit · through the MCP · not yet
```
→ DATA_LEGAL §10–§11 (read on request): what the plan allows, what to check, what to
label. TIP: on Suno the rights follow a paid download, not the generation. WHY: CORE_00 §7
rule 12; DATA_SUNO §12.

EXAMPLES — one filled line each:
- Suno Pro · made from scratch · streaming · downloaded in the app with a paid credit

</section>

<section id="§13" title="[12] FIX A PROMPT">

SUB-ENTRIES — `12a` fix a prompt · `12b` check a finished take: tempo, key, the words actually
sung — MCP clips and, since 04.11.2026, songs from your suno.com library (= `15g`) · `12c` edit a
take: by feel or pro, then a cover of it (CORE_00 §9 EDIT A TAKE)

`12a` — ASK: paste the prompt (Style, Lyrics, Exclude — whatever you have) and say what
went wrong, if you know. BLANK: `⟨the prompt⟩ · ⟨the symptom: "ignores my tags", "talks
in the intro", "cuts off"⟩ · ⟨platform and model⟩`. Output: the diagnosis and the
repaired prompt (CORE_03 §2–§3). `12b` CHECK A TAKE — BLANK: `⟨the take: a link, an id, or
"the last one"⟩ · ⟨what to check: tempo · key · the words sung · the tags⟩`. With a Suno
server: analysis and alignment, free (DATA_SUNO_LIVE §5); without one, by ear against the
failure modes of CORE_03 §5. `12c` EDIT A TAKE — BLANK: `⟨the take: №, an id, or "the last
one"⟩ · ⟨by feel: brighter, warmer, more energy … · pro: remove or add an instrument, BPM, key,
vocal, sliders⟩`. With a Suno server: the editor widget, then a cover of the take with the
edited Style and its own lyrics — a card first; without one, the edited Style as text.

EXAMPLES — one filled line each:
- `12a`: the Style and Lyrics I pasted · "the vocals start in the intro" · Suno v6
- `12b`: the last one · the words sung and the tempo
- `12c`: №7 · brighter, a little warmer, no guitar

</section>

<section id="§14" title="[13] AFTER THE TAKE">

SUB-ENTRIES — `13a` which stem split: Auto, Split from Mix, Advanced (Suno app) · `13b` Suno
Studio 2.0 — MIDI, chat bar, effects (Suno app) · `13c` mastering and loudness for release ·
`13d` hand-off to a DAW

`13a` STEMS — BLANK: `⟨the take⟩ → ⟨a quick vocal/instrumental split · full stems · one
instrument⟩` → which Suno split (DATA_SUNO §10, DATA_POSTPROD §4), in the app. `13b` STUDIO 2.0 — BLANK:
`⟨the take⟩ → ⟨what to do: MIDI · effects · a second take on one track⟩`, in the app.
`13c` MASTERING — BLANK: `⟨target: streaming · a video bed · a podcast · a club⟩` → the
chain (DATA_POSTPROD §2) and the loudness target (DATA_POSTPROD §9). `13d` TO A DAW — BLANK: `⟨DAW⟩ · ⟨what you
need: stems · tempo and key · the beat grid⟩`; with a Suno server the analysis gives BPM,
key and every beat (DATA_SUNO_LIVE §5).

EXAMPLES — one filled line each:
- `13a`: my last take → a quick vocal/instrumental split
- `13b`: the last take → MIDI of the bass line
- `13c`: streaming
- `13d`: Ableton · stems, tempo and key, the beat grid

</section>

<section id="§15" title="[14] SPEECH — the script sheet">

SUB-ENTRIES — `14a` your text over music · `14b` voice only, no music · `14c` a toast, an ad, a
story, an intro — written for you · `14d` a long text, in parts. Suno rewrites the Tone:
compare the delivery by ear

ASK: what should be said, by whom, and with music under it or not? ("a bedtime story,
a warm woman's voice, quiet piano under it")

BLANK:
```
⟨text⟩        — the exact words (14a, 14b, 14d) or the brief for one to be written (14c)
⟨who⟩         — gender · age · character: "a tired but kind radio host"
⟨pace⟩        — slow · measured · brisk; where to pause
⟨music⟩       — none (14b) · a bed: ⟨genre, mood, how quiet⟩ (14a)
⟨length⟩      — about ⟨N⟩ words (70–75 fill 45 s; keep under 60 when the ending matters)
```
Output: the Speech Blueprint (Script + Tone) of CORE_00 §6, written as CORE_02 §16 says;
`14d` splits a long text into parts with one card for the batch. TIP: compare the delivery
by ear and keep the take, not the Tone. WHY: Suno rewrites the Tone in every take
(DATA_SUNO_LIVE §3) — the script it keeps word for word.

EXAMPLES — one filled line each:
- `14a`: a 60-second bedtime story about a lighthouse cat · a warm woman's voice, around fifty · slow, a pause after each sentence · a quiet piano bed · about 130 words
- `14b`: "Welcome to the museum. The tour starts on your left." · a calm male guide · measured · no music
- `14c`: a toast for my brother's wedding, written for me · a warm male voice · 40 seconds
- `14d`: a 900-word story → three parts of about 300 words, one card for the batch

</section>

<section id="§16" title="[15] SUNO + MCP — your songs and the send sheet">

SUB-ENTRIES — `15a` Suno in this chat: status, balance, how to connect it · `15b` send the last prompt
— the card first: two takes a call, never fewer, the credits, then your yes · `15c` listen and
check the take · `15d` cover, extend or mash up a library song · `15e` start from your own
audio or your Voice · `15f` a song longer than 6 minutes — extend, then a free join · `15g`
check a take (= `12b`); `15g … ask` a question to Suno's own listener, free · `15h` your songs: a list, a tap shows all one song can do; find, liked
· `15i` playlists · `15j` workspaces · `15k` fix a title or the stored lyrics · `15l` download
(a download credit) · `15m` one screen like Suno's Create page: a new song (simple, song,
speech, loop) or one of yours in the editor — extend from a point to the millisecond, cover,
mashup, exact times for Replace Section, the lyrics and the styles each in its own tab; a sound (one-shot or loop, Suno Sounds) · `15n` mix two of your songs: a mashup, the style of one with the lyrics of
the other, or a cover of one with the other's lyrics · `15o` a new song from up to ten of your songs:
sample the hook, restyle, remaster, drop or keep a part — one sentence says what to do. With a
Suno server this screen is the MCP MENU with your songs (DATA_SUNO_LIVE §7)

`15a` CONNECT AND BALANCE — no blank: the status line (plan · credits · this month ·
download credits · models · tools vs DATA_SUNO_LIVE §1), free; no server → how to add it.

`15b` SEND — the card is the blank, filled from the last blueprint (DATA_SUNO_LIVE §7):
```
tool · model        — audio-create · v6 (or the model the plan allows)
title · length      — ⟨title⟩ · ⟨M:SS⟩ (a target unless strict)
takes · credits     — 2 (the server's own, never fewer) · 10 · balance after ≈ ⟨N⟩
Max Mode            — off, unless you asked for it by name (more credits)
variety             — ⟨0 Off … 4 Max | default⟩, as the blueprint says (0 keeps the Style as written)
not in the MCP      — what no field takes (a Custom Model: set it on suno.com)
```
→ Send · Edit · Cancel. `15c` LISTEN — BLANK: `⟨what to listen for first⟩` from the
blueprint's "why"; then `12b`. `15g` CHECK A TAKE — the blank of `12b` (§13). `15d` COVER · EXTEND · MASHUP — the blanks of §4 (`3d`,
`3e`) and `⟨take⟩ → extend from ⟨mm:ss⟩ with ⟨what happens next⟩`. `15e` OWN AUDIO OR
VOICE — `15e upload` opens Suno's uploader at once (only audio the user holds the rights to),
then the sheet of `3a`; `15e voices`: voices-list, a voice to sing in; `15e voice`: a new voice
on suno.com (voices-start). `15a upgrade`: Suno's own button to buy credits. `15f` LONGER THAN 6 MINUTES — BLANK:
`part 1 ⟨what⟩ · part 2 ⟨what⟩ … → one batch card → extend, extend, join (free)`. `15h`
YOUR SONGS — the list is the blank: `15h 10 | 50 | 100` the last ones (nothing is listed before you
ask); a tap, or `15h ⟨row⟩`, shows all that song can do; "Listen" draws Suno's player in the chat, with
the song's link beside it (DATA_SUNO_LIVE §7 SONG ACTIONS); BLANK: `find ⟨title or style words⟩ · only ⟨liked · downloaded · uploads · covers ·
extensions · remasters · public · private⟩ · like | dislike | unlike ⟨song⟩` · ask ⟨song⟩ ⟨a question about how it
sounds⟩ (`15g … ask`, free). `15n` MIX TWO SONGS — pick A and B in the list
(or name them): `mashup` (A + B blended) · `style` (a new song: the style of A, the lyrics of B) · `cover`
(A's music sung with the lyrics of B) — each opens the editor first, then the card. `15i` PLAYLISTS — BLANK: `⟨new playlist name⟩
(private by default; public only when you say so) · add ⟨songs⟩ · remove ⟨songs⟩ · show ⟨playlist⟩`. `15j` WORKSPACES — BLANK:
`⟨workspace: one per album or project⟩ · move ⟨songs⟩ in · take ⟨songs⟩ out` — a song lives in
one workspace at a time. `15k` FIX A TITLE OR THE STORED LYRICS — BLANK: `⟨song⟩ → title
⟨new title⟩ · lyrics ⟨the corrected text⟩` — the library entry only, the song is not re-sung;
read the stored text first and show "was → will be" before the write, which cannot be undone.
To change what is sung: a cover with the new lyrics, an extension from a second, or `2i` /
`6g` in the app (DATA_SUNO_LIVE §7 SONG ACTIONS). `15l` DOWNLOAD — BLANK: `⟨song⟩ · ⟨mp3 |
wav⟩` → a card: one download credit. Whether a download through the MCP carries the rights of
a download on suno.com is not stated — for a release, download on suno.com (DATA_SUNO §12).
`15m` CREATE AND EDIT — the screen is the blank (DATA_SUNO_LIVE §7 CREATE AND EDITOR); in text:
`⟨song or new⟩ · ⟨extend from mm:ss.mmm for N s | cover | mashup with ⟨song⟩ | replace mm:ss.mmm–
mm:ss.mmm | lyrics only⟩ · lyrics ⟨…⟩ · style ⟨…⟩ · options ⟨model, exclude, sliders, Variety 0–4, voice⟩`. `15o` FROM YOUR SONGS — BLANK: `⟨up to ten of your
songs, by title or row⟩ → ⟨what to do: sample the hook · a new style · remaster · drop the vocals · keep only the
drums · take it as inspiration⟩` → one sentence for Suno that names the songs by title, never an id or a link;
Simple mode, so no Style or Lyrics of your own; then the card (two takes, 10 credits). Tried once on
2026-11-05 (Pro): a restyle kept the source's tempo, key and piano; dropping or keeping a part is not tried yet.

EXAMPLES — one filled line each:
- `15a`: "15a" → Pro · ≈2 345 credits · 155 of 2 500 this month · 20 downloads
- `15b`: the last blueprint → audio-create · v6 · two takes · 10 credits → Send
- `15c`: listen for: does the voice stay behind the beat in verse 2
- `15d`: "Neon Rain" → extend from 2:31 with a slow bridge
- `15e`: `15e voices` → "My voice 1" → this song sung in it
- `15f`: part 1 intro and the story, 5:30 · part 2 the long instrumental outro, 3:00 → extend, then join
- `15g`: the last take · the words sung, the key · `15g ask`: "is the chorus louder than the verse?"
- `15h`: `15h 50` · find "night drive" · only liked
- `15i`: your playlists as rows → tap "Road trip" to add the song; or a new one: "Summer 2026"
- `15j`: your workspaces as rows → tap "Album 2026" to move the three demos in; or a new one by name
- `15k`: "Untitled 3" → title "Kitchen at 2 a.m." · the stored lyrics with the typo fixed
- `15l`: the last take · mp3
- `15m`: "Neon Rain" · extend from 2:31.250 for 60 s · lyrics [Bridge] … · the same style
- `15n`: A "Neon Rain" + B "Kitchen at 2 a.m." · style: the sound of A with the lyrics of B
- `15o`: "Neon Rain" and "Kitchen at 2 a.m." → chop the vocal hook of Neon Rain into a lo-fi beat, the piano of Kitchen at 2 a.m. under it

MCP MENU (`[15]`, `mcp-menu`) — no blank: the panel of DATA_SUNO_LIVE §7 — the status line
(plan · credits · downloads · models), your latest songs, then every capability by its code;
a pick opens its blank above. Without a Suno server: the same panel marked "needs the Suno connector".

ADAPT ("N adapt", "preset 12 for my song", "recipe lo-fi for this") — BLANK:
```
⟨the catalogue item⟩ → ⟨the song in hand: subject · voice · language · length⟩
keep: ⟨its signature trait⟩ · change: ⟨one thing the song needs⟩
```
Output: one sentence on what the adaptation changes, the adapted piece (both forms for a
persona), then the full blueprint — the model is the 5a → "04 adapt" exchange SunoForge
v4 users kept.

</section>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_BLANKS.md · SunoForge v5.0
// Blanks are shapes, not facts: fields, limits and plans live in the DATA files
// ═══════════════════════════════════════════════════════════════
</sunoforge_file>
