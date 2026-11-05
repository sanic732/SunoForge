<sunoforge_file id="DATA_SUNO" version="5.0" layer="data" role="adapter" source="DATA_SUNO_2026-10.md">
<file_meta>
file_id: DATA_SUNO
version: "5.0"
layer: data
role: adapter
description: >
  Every Suno fact the system uses, as of 2026-11-04: the v6 model family and the
  retirement of all earlier models, field limits, Exclude Styles, Max Mode, Variety,
  Duration, sliders, Voices, Custom Models, plain-language editing, Studio 2.0, stems,
  the lyrics editor, what each plan unlocks, download-bound rights, Speech (beta), the
  Suno MCP and API, shared workspaces and albums, and the myths.
  Read for any Suno target. The single source of truth for Suno versions and limits.
valid_as_of: "2026-11-04"
expires: "Suno ships user-facing changes every week or two (Speech 10-01, Collaboration 10-15, MCP 10-28) — verify anything here after 2026-12"
scope: suno_v6 · fields · max_mode · variety · duration · sliders · voices · custom_models · editing · studio_2 · stems · plans · downloads · speech · mcp · api · collaboration · albums
depends_on: [CORE_00_ENTRY]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE, DATA_RECIPES, DATA_POSTPROD, DATA_LEGAL, DATA_OTHER]
authority: "THIS FILE IS THE SINGLE SOURCE OF TRUTH FOR SUNO VERSIONS, LIMITS AND PLAN GATING"
updated: "2026-11-05"
</file_meta>

# 🟠 SUNOFORGE v5.0 — SUNO PLATFORM DATA
# File 6 of 14 · DATA layer · valid as of 2026-11-04

> ⚠️ **Expiry notice.** Everything in this file is a snapshot. On 2026-09-09 Suno
> retired every model it had and replaced them with the v6 family; in the eight weeks
> before that it rebuilt Studio, rewrote its terms and capped downloads; in October it
> added Speech, sharing and an official MCP server. Help-center articles show an
> "Edited" date — quote it with the claim. A text-only fetch shows a bare "Edited"
> (the date is rendered by script): read it from the category list or the raw HTML.
> Several rules here rest on pages last edited before v6 (2026-09-09). If today is
> more than a quarter past the date above, treat every number here as a starting
> hypothesis, not a fact. Replace this file; leave the CORE_* files alone.

> 📌 **Single source rule.** Model names, field limits and plan gating live here and
> nowhere else. If you find them repeated in another file, that is a defect — delete
> the copy and link here instead.

> 💲 **No prices.** This file names plans because features and rights depend on them.
> It never states what a plan costs: that differs by country and changes without
> notice. Credits are mentioned only where they change a decision.

<section id="§1" title="VERSION MATRIX">

Quotes in this section are Suno's, from the v6 announcement
https://suno.com/blog/introducing-v6 and the v6 FAQ https://help.suno.com/en/articles/13924481

[OFFICIAL] Released 2026-09-09 as "a new generation of music models developed with
our industry partners, including Warner Music Group, BMG and Believe".

─── v6 — THIS SYSTEM'S DEFAULT ─── Pro and Premier
  "our flagship model… reliable, precise and consistently delivers polished music
  across every genre and style. When you know what you want, v6 helps you get there."
  Help center: "Suno's latest model. Recommended for most songs."

─── v6-wild ─── Pro and Premier
  "built for exploration… less predictable and more varied, producing unexpected,
  textured and ambitious results. It gives you new ideas to riff on, build from or
  bring back into v6 for further refinement."
  The CEO, to the press: if you are looking for a specific thing, v6-wild "may not be
  the right thing for you" [COMMUNITY: press interview].

─── v6-mini ─── every plan, including Free
  "our fastest and free version of our premium v6 models"; "A faster, lighter version
  of v6. Good for quick iterations."

─── CUSTOM MODELS ─── Pro and Premier
  Listed in the same picker: "Models trained on your own music." Powered by v6 (§6).

  WHERE: the model picker, top-right corner of the Create form. The choice stays set
  until you change it. [OFFICIAL]
  The picker shows a "Pro" badge on v6 and v6-wild [COMMUNITY + first-hand].
  The help article on current models was reworded after these quotes were taken
  (re-checked 2026-10-28); the facts above still hold, the wording may differ.

─── SPEECH (beta) ─── every plan, since 2026-10-01
  Not a picker entry: a separate Speech tab in Create, next to Songs. Voice and music
  in one generation — §15.

─── EVERYTHING BEFORE v6 IS RETIRED ─── [OFFICIAL]
  "All models prior to v6 have been retired, but your songs will still be in your
  library and remain unchanged. You will still be able to listen to, share, remaster
  and cover songs made with old models."
  "You can continue working on songs made with older models, but any new iterations
  will be made with our latest models."

  That covers v5.5, v5, v4.5-all, v4.5+ and everything older. The free tier moved
  from v4.5-all to v6-mini.

  ⚠️ A guide, preset or saved prompt that names v5.5, v5 or v4.5 is describing a
  model you can no longer select. The prompt text may still work; the version label
  does not. Repair: CORE_03 §3.

─── LENGTH ─── [OFFICIAL]
  "up to 8 minutes of music in a single generation across v6, v6-wild, and v6-mini."
  Longer still: Extend continues a song from its end.

─── ONE GENERATION = TWO SONGS ─── [OFFICIAL]
  v6 generations cost the same as the previous models did. Many images or videos in
  one prompt raise the cost.

─── HOW v6 WANTS TO BE ADDRESSED ─── [OFFICIAL]
  "v6 understands more of the language and building blocks musicians use, from
  vocals, instrumentation and structure to mood, references and the overall feel of
  a song… Describe what you want and v6 figures out how to get there."
  In Simple mode "you don't need to know which tool to reach for (like Cover, Remix,
  Extend)… The model figures out the workflow if you want it to."
  Suno also says v6 was designed "to support all the ways you have liked creating
  with past models" and links a tutorial on reproducing old-model results.

</section>

<section id="§2" title="THE STYLE FIELD — limits, weighting, and the myth">

WHAT IS ACTUALLY KNOWN:

  [OFFICIAL]   Suno publishes no numeric character limit for Style or Lyrics.

  [OFFICIAL, MCP schema 2026-11-04]  Style ≤1,000 characters · Lyrics ≤5,000 · Exclude
               Styles ≤1,000 · the Simple-mode description ≤3,000 · a Speech script
               ≤5,000 (DATA_SUNO_LIVE §1). The web form matched these on v5.5 and v6
               [COMMUNITY].

  [COMMUNITY]  Measurable influence fades well before the hard limit. Pre-v6 testing
               put the practical ceiling near 300–400 characters; nobody has re-run
               that on v6.

  [UNVERIFIED] "Attention collapses after 200 characters." No controlled test ever
               supported a cliff at that number, and none exists for v6. An earlier
               edition of this system taught it and was wrong.

LONG OR SHORT ON v6?
  [OFFICIAL]  Suno's direction is natural language: describe the song the way a
              musician would; complex, multi-part instructions are welcome.
  [COMMUNITY] One tester (~150 v6 songs; Suno sponsored his v6 video and gave early
              access; affiliate links; promotes his own Suno guide and bundle) found a
              detailed style "wasn't clearly better than a four-word one" on the same
              lyrics. Moe Lueker, 2026-09-19 · `https://moelueker.com/blog/suno-v6-guide`
  [COMMUNITY] Another guide recommends per-instrument, per-section sentences and
              "say everything twice" — once in Style, once in the matching section
              label.
  [COMMUNITY] Users quoted on launch: v6 "wants to be directed exactly what to do,
              with little deviation"; others: "Your old prompts won't work."
  None of this is a controlled test. WHAT HOLDS EVERYWHERE: decisions beat
  adjectives, and the first words carry the most weight.

### PRACTICAL SHAPE
PRACTICAL SHAPE:
  genre + era · mood in 1–2 words · 3–4 instruments · vocal gender and character ·
  production signature · parameters as prose (BPM, key, space)

  ⚠️ Those are slot names, not syntax. The whole thing is one plain sentence, as in
  the example. Bracketed `parameter: value` forms are not read (CORE_02 §1).

  Example:
    mid-90s Seattle grunge, weary and defiant, detuned electric guitar, heavy bass,
    live drums, male baritone with a gravelly worn delivery, analog tape saturation,
    wide stereo field, 92 BPM, D minor

  ⚠️ If the Style text was engineered with care, set Variety to 0 — otherwise v6 may
  rewrite it before generating (§4).

</section>

<section id="§3" title="EXCLUDE STYLES — the negative field">

[OFFICIAL, 2024] A dedicated field for styles, instruments or vocal traits to keep
out. Excluded items show with a leading minus: `-piano`. Launched for Pro and Premier
as an early-access beta; Suno asked for likes and dislikes to improve it.
[COMMUNITY, HookGenius v6 guide, updated 2026-10-22, one account] After generation
Suno renders the Exclude Styles list back into the style view, after the Style text,
each item with a leading minus, in the order entered; the Style text itself is stored
untouched (an exact byte-for-byte prefix). The minus is display, not syntax: negatives
go in Exclude Styles. Whether a "-term" typed into Style does anything has not been
tested. Relayed by Roo, 2026-09-27. `https://hookgenius.app/learn/suno-v6-guide/`
[COMMUNITY, v6] Present in the v6 More Options panel. Current plan gating on v6 is
not stated anywhere official.

[COMMUNITY, v6] Early v6 users call it "far more necessary than previous versions":
asking v6 in the prompt text to remove humming produced more humming; the Exclude
field is the place for it.

WHAT IT IS GOOD AT:
  - removing an instrument the genre would otherwise drag in
  - suppressing a production aesthetic ("polished pop production", "auto-tune")
  - keeping an era out of a period piece

VOCAL GENDER [OFFICIAL, help "Can I choose the gender of the singer in my song?",
ed. 2026-09-09]: Custom mode → Advanced Options → Vocal Gender, Male or Female;
optionally a voice word in Style ("gritty", "soft"; e.g. "blues rock with gritty male
vocal" plus Male). Simple mode: "male" or "female" in the description ("A 90's
alternative song with female vocals"). On v6 the panel is called More Options
[COMMUNITY, v6]. The selector is "the most reliable control anyone has found"
[COMMUNITY]; the help page does not compare it with anything.
HISTORY ONLY [UNVERIFIED, checked 2026-11-05]: the 2024 tip "[female vocals]" in Lyrics
plus "male vocals" in Exclude Styles is not in Suno's current gender article (help
10153473, ed. 2026-09-09) or Exclude article (help 3161921, ed. 2025-12-19). Earlier
wording of either page could not be retrieved; this file cites no source for the 2024
tip. Absence from the current pages does not show the pairing stopped working.

### HOW TO WRITE IT
HOW TO WRITE IT:
  8–12 items, musical vocabulary, not engineering jargon.
  Specific beats generic: "polished pop production" outperforms "pop".

  GOOD: EDM, auto-tune, overproduced, electronic drums, heavy bass, crowd noise
  WEAK: brick-wall compression, dithering, sidechain   ← engineering terms
  WEAK: bad sound, weird, cheap                        ← not musical categories

READY LISTS BY TARGET GENRE:
  Lo-fi / chill      EDM, aggressive, auto-tune, heavy drums, screaming, bright,
                     overproduced, trap bass
  Rock / metal       synth pop, smooth jazz, gentle, lo-fi, whisper vocals,
                     acoustic, mellow, electronic
  Pop / radio        death metal, noise, lo-fi, experimental, drone, harsh,
                     distorted vocals, dissonant
  Jazz               EDM, distorted guitars, auto-tune, screaming, trap, 808,
                     blast beats, overproduced
  Hip-hop / trap     orchestral, acoustic guitar, country, folk, operatic,
                     jazz scat, classical
  Cinematic / epic   lo-fi, bedroom recording, punk, garage, raw, minimal,
                     muffled, thin
  Country            EDM, synthwave, death metal, auto-tune, robotic,
                     electronic drums, dubstep
  Ambient / sleep    drums, vocals, loud, aggressive, fast, energetic, distorted,
                     bass-heavy
  Folk / acoustic    EDM, synthesizers, distortion, electronic drums, auto-tune,
                     stadium reverb, trap hi-hats
  Gospel             lo-fi, whisper, minimal, cold, robotic, distorted, sparse
  Intro humming fix  humming, vocalise, wordless vocals   (v6 launch complaint)

NEGATIVES IN THE STYLE FIELD (as opposed to the Exclude field):
  [COMMUNITY] Weak and sometimes counterproductive on every Suno generation to date.
  Naming a concept can summon it. Keep at most one or two, each right after a strong
  positive statement.

</section>

<section id="§4" title="MAX MODE, VARIETY AND DURATION — the v6 controls">

─── MAX MODE ─── [OFFICIAL] since 2026-09-09 · quote: Suno's v6 FAQ, https://help.suno.com/en/articles/13924481
  "Max Mode is an option you can turn on for any generation when you want v6 to
  spend more on getting it right. It costs more credits and it's best for: songs
  longer than two minutes, covers where you want the result to stay close to the
  original, transferring the style of one song onto another, and keeping vocals and
  style consistent through the whole track. For quick ideas and shorter songs,
  standard mode is all you need."

  COST: "more credits" [OFFICIAL]. The tooltip, captured from the interface, reads
  "Uses more compute to maximize consistency throughout the song. Costs 2x credits per
  song." [COMMUNITY: UI capture]. Through the MCP the same 2x: 20 credits for a generation
  of two takes instead of 10 [first-hand, Pro, 2026-11-04; DATA_SUNO_LIVE §3]. Whether it
  is offered on v6-mini or on Free is not documented [UNVERIFIED].

  LATE-SONG DEGRADATION, MEASURED [COMMUNITY, one user, 2026-09-20]: on standard mode a
  dense 3:32 track lost dynamic range minute by minute — peak-to-RMS about 3.0–4.6 dB
  in the first minute, 2.5–2.9 in the second, 1.9–2.3 after 2:00, while loudness rose;
  1:10 versions of the same song showed none of it. Others report "muffled after ~2:30"
  and say Max Mode reduces the effect without removing it [COMMUNITY].

  WHEN THE SYSTEM RECOMMENDS IT (SUNO_MAX_MODE = "suggest"):
    ✅ target length over two minutes
    ✅ a cover that must stay close to the original
    ✅ moving one song's style onto another
    ✅ a track for release, where the vocal must hold from first line to last
    ❌ sketches, drafts, anything you will regenerate anyway

  ⚠️ NOT THE SAME THING AS THE "MAX MODE" TAGS. `[Is_MAX_MODE: MAX]`,
  `(MAX)(MAX)(MAX)(MAX)` and friends are community folklore from the v4 era — text in
  the prompt that no controlled test ever connected to quality (§14). Suno's toggle
  is a control in the interface. The tags do not switch it on, and Suno has never
  linked the two. Strip the tags; use the toggle.

  Untested: whether Max Mode fixes late-song degradation reported on standard mode.
  Suno's own wording ("keeping vocals and style consistent through the whole track")
  says that is what it is for.

─── VARIETY ─── [OFFICIAL] since 2026-09-09 · quote: Suno's v6 FAQ, https://help.suno.com/en/articles/13924481
  "The Variety slider is designed to introduce variety in your outputs by adjusting
  and updating your style prompts. If you'd like to retain full control of your style
  tags, reduce the Variety slider to 0."

  In plain words: above zero, v6 may rewrite your Style text before it generates —
  differently for each take. [COMMUNITY] Observed on camera: Style rewritten at the
  higher settings.

  REPORTED STEPS [COMMUNITY]: Off "Exact style" → Normal "Balanced variety" → High
  "Distinct styles" → Extra "Bold exploration" → Max "Unreasonably varied". Default
  reported as Normal on v6 and v6-mini, Off on v6-wild.

  RULE FOR THIS SYSTEM:
    Engineered Style (recipes, clones, client briefs)  → Variety 0
    Loose idea, happy to be surprised                  → default
    Exploring directions                               → High, or switch to v6-wild

  This is the best-supported v6-specific prompting rule there is: the vendor states
  it. When a user says "Suno ignored my style", check Variety first.

  MEASURED [COMMUNITY, HookGenius, updated 2026-10-22, 27 renders × 2 takes]: with
  Variety Off the stored Style matched the pasted text in 52 of 54 takes; with Normal
  it was rewritten in every one of 30 takes. Lyrics, title and the Exclude list were
  kept as written at every setting — Variety touches Style only.
  Source: `https://hookgenius.app/learn/suno-v6-guide/` (published 2026-09-09, updated
  2026-10-22); HookGenius sells an app and a $29 guide.

### DURATION
  [OFFICIAL] Added 2026-07-20 for v5.5 on the web, in the Create form.
  [COMMUNITY, v6] Present on v6: Auto, or Custom from 10 seconds to 6 minutes in
  5-second steps, with 3:00 as the reported default. Custom at the 6:00 end often stops
  early or trails silence. Mobile availability not documented.
  [OFFICIAL] A single generation can reach 8 minutes. [COMMUNITY] Beyond the
  slider's range, length comes from the amount of lyrics, and past 8 minutes from
  Extend.

  BEHAVIOR [COMMUNITY]:
  - The value is a TARGET, not a guarantee. Long settings often undershoot; give
    enough lyrics to fill it
  - If the audio has not resolved by the target, it can cut abruptly
  - On Auto, v6 tends to come back longer than v5.5 did
  - A widely repeated tip for v6: under about three and a half minutes holds up
    better; for longer pieces, generate the back half separately with Extend — or
    use Max Mode, which Suno aims at exactly this

  PRACTICAL PAIRING:
    Set duration AND give the lyrics to fill it. A 5-minute target with two verses
    produces padding, instrumental drift, or an early cut.
    Rough guide: ~1 minute of song ≈ one verse + one chorus at moderate tempo.

  RELATIONSHIP TO EXTEND: complementary. Duration shapes the first generation;
  Extend adds material to a finished track.

  HISTORY: a 2026-07 first-hand measurement reached 7:59 on the old free model in one
  generation. The claim that the free tier caps near two minutes had no source then
  and has none now.

</section>

<section id="§5" title="VOICES — your own voice">

[OFFICIAL] Introduced 2026-03-26. Personas became Voices; "Style Personas are still
available within the Voices menu".

WHO: the plan page lists "Record, upload, and create with your own voice" under Pro
and Premier. Since 2026-08-07 Voices is on iOS and Android and "Now available to try
on free plans. Do more on paid plans." [OFFICIAL, https://suno.com/release-notes]. The plan comparison table seen on
2026-10-28 shows Voices locked on Free — Suno's own pages disagree; check in the app.
18+ only; not offered in every country, and the list is not published [OFFICIAL].
The Voices page now markets it as cloning your voice and suggests recording in the
style you want to sing; others can cover or remix shared songs that use your Voice
[OFFICIAL]. Through the Suno MCP: "Use your own Suno Voice on any track you create
from your AI" (§16). Not offered inside Speech [COMMUNITY].

THREE WAYS IN [OFFICIAL]: a voice from a song in your library · record in real time
· upload a file.

INPUT LENGTH [OFFICIAL, help "Voices", ed. 2026-05-01, pre-v6]: "15 seconds up to
4 minutes"; you pick the best 2 minutes.
  [OFFICIAL, Suno blog, 2026-06-05, pre-v6] record as long as you can: "Aim for at
  least a minute if you can" (the upload stops at 4 min and Suno uses the best 2).
  Use a quiet room, not an echoing bathroom or hallway. No flawless studio take
  needed. Try several genres and tempos to find where the voice works.
  [UNVERIFIED] 90–120 seconds of varied singing gives the best result (no source found).

AUDIO [OFFICIAL]: acapella with a decent microphone in a neutral room works best.
Backing music is accepted — Suno runs stem extraction to isolate the vocal.

VERIFICATION [OFFICIAL]: "Suno will display a short phrase for you to read aloud.
This spoken recording is compared against your uploaded singing recording to confirm
they are from the same person."
CHECKBOX [OFFICIAL]: you "affirm that you have the rights to use this voice".
TERMS: own voice only — the clause and the training licence: DATA_LEGAL §3.
Training: every upload falls under the general content licence in the terms, which
covers improving Suno's models — see DATA_LEGAL §3.

ON v6:
  [OFFICIAL] "If you use Voices, Custom Models, or My Taste, make sure you're on a
  compatible model." The Voices help page still names v5.5 as required — it predates
  v6 and is out of date.
  [COMMUNITY] Existing voices get an "Upgrade Voice to v6" action; the menu shows
  "Voice (new)" and "Style Voice (legacy)"; Voices do not apply to instrumentals.

PRIVACY: only the creator can generate with their voice [OFFICIAL, Voices FAQ,
ed. 2026-03-26, pre-v6].

COST: no separate price published. Assume normal generation credits.

WORKING WITH VOICES:
  - Draft with stock vocals, switch to your Voice for the final take
  - Audio Influence decides how much of your voice survives; if the result does not
    sound like you, raise it [OFFICIAL, Voices FAQ troubleshooting, ed. 2026-03-26;
    how-to, ed. 2026-05-01: "up fairly high"; pre-v6]
  - Suno says "clone"; in practice expect your character, not your double
  - Give the model range: sing high and low, loud and soft, in the source clip

</section>

<section id="§6" title="CUSTOM MODELS — train on your catalog">

[OFFICIAL] Pro and Premier. Upload "as few as six songs" (bulk upload available);
"up to three models"; "about 2-5 minutes" to train; the model appears in the picker.
Sharing: since 2026-10-15 Premier can share a model with collaborators, "now with
double the inputs" (§17) — while the help page still says models are private. The
release note is newer; the exact new input count is not stated.
[OFFICIAL] "You must own the rights to all of the songs you upload." Enforced by
terms, not by a technical check — the responsibility is yours.
[OFFICIAL] Since v6: "Any custom models you've created will automatically get
upgraded so that v6 powers your model moving forward." (v6 FAQ,
https://help.suno.com/en/articles/13924481) Songs made with the old model
stay as they were.
[COMMUNITY] The upload screen suggests "24+ songs for best results". Creating a model
costs credits.
[UNVERIFIED] What happens to a model after a copyright complaint is not documented.

[COMMUNITY] 6 is the floor, not the target. Stylistic consistency matters more than
count — a catalog spanning six genres teaches the model to average them.

STRATEGIES:
  "Band" model        6+ tracks by one project → its arrangement habits
  "Beat" model        6+ lo-fi or trap instrumentals → consistent groove and mix
  "Score" model       6+ cinematic pieces → a reusable soundtrack generator
  "Client" model      a client's catalog, with written permission → on-brand music
  Switch models per task rather than building one model for everything.

WHAT IT TRANSFERS: arrangement habits, harmonic tendencies, production texture,
instrument choices. Not lyrics, not melody, not a specific singer.

</section>

<section id="§7" title="EDITING, REMIXING AND REFERENCES ON v6">

[OFFICIAL] What v6 added, in Suno's own examples (https://suno.com/blog/introducing-v6):

| Capability | Suno's example |
|---|---|
| Edit one section in plain language, keep the rest | "Change the chorus so it's sung by a gospel choir" |
| Update a single lyric without rebuilding the song | "Change the lyric from 'love' to 'light'" |
| Mashup from several sources in one request | "Take the vocals from x, drums from y, and add new lyrics about losing control, make it 80s synthwave" |
| Sample, isolate and build a beat in one workflow | "Sample the riff at 0:45, isolate the guitar, build a beat around it" |
| Start from a vibe or a mix of inspirations | "Make a song that feels like midnight on a rooftop" |
| Start from text, audio, images and video | "Make a song based on this image, this audio and my journal entry" |

The help center groups the classic tools under "Remix & Edit — Extend, Cover, Replace
Section, and more, all powered by v6" [OFFICIAL]. The plan table lists Remix (extend,
cover, adjust speed), Basic editing (crop, fade), Advanced editing (replace or add
section), Add vocals, Add instrumental [OFFICIAL].

A mashup takes exactly two songs [OFFICIAL, the MCP schema; first-hand, DATA_SUNO_LIVE §3].

SONG EDITOR [OFFICIAL, help center, 2025–2026]: Replace Section is for Pro and Premier —
highlight a region, edit its lyrics in the box, Recreate Section → two versions to choose
from, then a new full song tagged "Section" and "Full Song". A replacement may carry an
optional hint in plain words ("make this section sound dreamier"); Quick Replace and
Quick Extend skip the hint; alternatives collect in the Edits Library; the transition is
moved by dragging the boundary on the waveform. Edit Lyrics in the editor = Replace
Section with new words. Crop trims only the beginning or end; Remaster: the paragraph
below. Suno's mail of 2026-10-31 lists Replace Section, Split from Mix and
Remaster for Pro. Menu [2i], [6g].
  [first-hand, suno.com, Pro, 2026-11-05]: one Replace Section run cost 4 credits for its two
  versions. Get Whole Song on a song that was itself built from a replacement gave 4:38
  instead of 6:05 — replace on the original chain, never on a replacement, and take the
  whole song once, at the end. The editor froze once in the same session: if it hangs, say
  so and give the manual steps.

REMASTER [OFFICIAL, help center, ed. 2026-09-09]: keeps the core structure, lyrics and
arrangement; works on sound quality, the mix and balance of instruments and vocals, sonic
texture, vocal clarity and pronunciation. Controls: a model selector and Variation
strength — Subtle (very close to the original; only small acoustic and production details
change), Normal (default; same duration and style, slight variation in musical details),
High (more noticeable differences, possibly in musical elements and vocals). Suno's advice:
Subtle "if you already like the track but want a slightly cleaner mix, smoother balance, or
clearer pronunciation". Not for changing lyrics or drastically altering the style — that is
Cover, "designed for significant transformations". The page places it in the Create menu;
first-hand it sits in the song menu's Edit list (below). Credit cost not published.

THE SONG MENU [first-hand, suno.com and the phone app, Pro, 2026-11-04] — Remix: Cover · Reuse
prompt · Mashup · Sample this song · Use as inspiration (Pro) · Voice (Pro). Edit: Extend · Crop ·
Remove a section · Reverse · Adjust speed · Find a co-writer · Fade in · Fade out · Replace
section · Get stems · Remaster (the last five Pro) · Open in Studio · Open in the editor (Pro).
Manage: song details · create cover art · allow remixes · allow comments · pin to profile ·
move to a workspace. Then publish · share · download · queue · playlist · song radio · report ·
trash. Create, Simple mode: a description plus "+" for lyrics, styles (new or saved), a
playlist (Inspiration), an image, a video, MIDI, audio (browse, upload, record) and a Voice
(use one, add new). Which of these the MCP reaches: DATA_SUNO_LIVE §9.

MIDI AS A CREATE INPUT [OFFICIAL, help "Using MIDI files in Create", ed. 2026-11-04 ·
https://help.suno.com/en/articles/14594177 ; blog "Start Songs with MIDI", 2026-11-04 ·
https://suno.com/blog/MIDI-in-create]: a .mid or .midi file added in Create, Simple mode;
desktop web, Pro and Premier (help). At launch it runs on v6-wild (blog; the help page names
no model). The prompt says how closely to follow the file: "Use the notes and chord
progressions exactly as they appear in the MIDI file", or "take the top line motif from your
MIDI file and develop it into new ideas" (blog). Name the instruments — "The file tells Suno
what to play; the prompt tells it what to play it on" — and describe the feel, not just the
genre (help). Suno's example prompts (blog): "Arrange this MIDI for a full orchestra, with
strings, brass, woodwinds and percussion." · "Transform this MIDI into a gospel choir with
piano accompaniment." · "Transform this MIDI into a string quartet. Use the notes and chord
progressions exactly as they appear in the MIDI file." MCP: not reachable (DATA_SUNO_LIVE §9).

INSPIRE [OFFICIAL, help center "Inspire", tag 4.5+]: a playlist of the user's own songs
guides a new one — Custom mode, "+Inspo" above the lyrics box, or the Inspire button on a
playlist; Suno analyses mood, tempo and instrumentation and applies them to the new
lyrics and style. Suno's advice: short playlists of 3–5 songs. Mail of 2026-10-30: "Inspire,
now in your plan" (Pro). No MCP tool reaches it (DATA_SUNO_LIVE §8). Menu [3g].

NOT PUBLISHED: how long a replaced section may be on v6 (in 2024 it was 10–30 seconds),
what each edit costs.
  [COMMUNITY, user measurements 2026-09, repeated by third-party guides 2026-11] Replace
  Section: 4 credits for a selection under about 29.5 seconds, 10 credits from 29.5 seconds;
  Extend costs a full generation. The 2024 release note set the selection at 10–30 seconds
  [OFFICIAL, old models]; no v6 limit is published — the app shows the price before the click. Fixing one word or one short phrase in place is therefore
  cheaper than regenerating a song whose mix you like.

REMIX PERMISSIONS [OFFICIAL]: More Actions → Visibility & Permissions → "Allow
Remixes". On by default for songs made after 2025-05-21 (older songs default off). A
remix or cover links back to the original under its timestamp, and the original's
author sees every remix. Remixes of other people's songs are never commercial (§12).

HOW TO WRITE AN EDIT INSTRUCTION (method; menu 2i):
  1. Name the target exactly — "the second chorus", "the line 'we rise above the storm'"
  2. Say what changes — performer, arrangement, a word, an instrument
  3. Say what must survive — "keep the verses, tempo and key"
  4. One change per request; listen to the WHOLE track after it
  [COMMUNITY] Whether a chorus-only edit or a one-word swap bleeds into the rest of the
  song has not been tested publicly. Check before you rely on it.

JOINS AND SEAMS — a song built from parts (extend, a medley, two genres). Collected
2026-11-05; no source tested them on v6, so say "not tested on v6 — listen to the seam".
  1. No ending before a seam [COMMUNITY, pre-v6]: a part that will be extended ends on a
     verse, chorus or instrumental section — no [Outro], [End], [Fade Out], [Silence] or
     [Stop]; such tags "might trigger the end of the song". Only the last part ends.
  2. Extend from inside the music [COMMUNITY]: the point sits on a phrase end, a bar line
     or a drum fill before any tail or fade; a point after the tail gave "the same song,
     then a little bit of silence, then another song". Never extend from silence: if the
     take already fades, Crop it to just before the tail (Crop trims the start or the end
     only [OFFICIAL]) or set the point earlier, then extend.
  3. The new part starts playing, not opening [UNVERIFIED, inference]: its lyrics begin
     with the section that follows, never with [Intro].
  4. One take first [OFFICIAL length · COMMUNITY route]: a single v6 generation reaches 8
     minutes, so two genre families can be one take with a section map (genre and
     instruments in each section label) and no seam at all; chain extensions only when
     one take blends the genres too much.
  5. A genre change gets a bridge [COMMUNITY practice, untested on Suno]: one device at the
     seam (drum fill, riser, sustained pad) and one thing kept (tempo, key, motif or
     singer); the same BPM and key in every part's Style — a request, not a lock.
  6. A bad seam is repaired in place [OFFICIAL tools]: Replace Section across the boundary,
     a few seconds each side, pick the better version, drag the boundary; or the editor's
     "+" between two sections adds a bridge. A silent gap is cut, not faded around: the
     editor's Remove, or Studio's delete time (Cmd/Ctrl+Shift+Backspace) [OFFICIAL]; a
     fade-out plus a fade-in at an inner seam is itself the dip [UNVERIFIED, inference].
  7. Join once, at the end [OFFICIAL]: Get Whole Song on the last extension only; then
     listen to every seam ±10–20 s and check the total length (the first-hand note above).
  Outside Suno (a DAW, Audacity): DATA_POSTPROD §6 JOINING TWO PARTS.
  Sources: help.suno.com/en/articles/6141505 (Song Editor), 3166529 (Crop), 3271873
  (Replace Section), 2409601 (Get Whole Song), 13680385 (Studio shortcuts), 13924929
  (v6 length); r/SunoAI threads 1sak5lb and 1s9unun (pre-v6, read 2026-11-05 from a
  snapshot of 2026-04-03); howtopromptsuno.com (undated).

REFERENCES [OFFICIAL]: in Simple mode one prompt can reference "Suno songs, playlists,
audio uploads, images and video" together with detailed guidance. v6 "can understand
the feeling behind a reference and use it as the starting point for something
original" (https://suno.com/blog/introducing-v6). Limits on the number and length of references are not published.
  [COMMUNITY] Reported limits: up to 5 images, 1 video up to about 4 minutes, up to 5
  audio references — a single source, treat as a guess.
  [COMMUNITY] A voice-memo hook: describe everything except the hook in the text and
  say "The uploaded audio is the chorus melody. Keep that melody exactly."

⚠️ SIMPLE MODE AND YOUR LYRICS [COMMUNITY]: Simple mode has been seen expanding
supplied lyrics instead of singing them verbatim. When the words must stay exactly as
written, use the full form with the Lyrics field.
  Even there, v6 — v6-wild most of all — sometimes paraphrases a line, loops the last
  chorus line or drops a final verse [COMMUNITY]. The "one-line test": plant one odd,
  checkable line ("the ferry leaves at seven, forty late") and listen for it in both
  takes before trusting the rest.

SAMPLE LENGTH [COMMUNITY, one guide]: up to ~15 s tends to be looped as is; 30–60 s
gives the most room for re-arrangement; past ~60 s results fragment.

### SOUNDS AND SAMPLES
  [OFFICIAL] Sounds (2026-01-27): one-shot samples and loops from scratch, as a Create
  mode; Pro or Premier at launch. "Suno Sounds" now runs on v6.
  [OFFICIAL] Sample (2026-01-20): any sound in Suno can be used as a sample via the
  Remix/Edit menu.
  [OFFICIAL, help "Suno Sounds", ed. 2026-09-09; "a new, experimental feature", "in beta"]
  HOW TO PROMPT SOUNDS: Create → Simple / Advanced / Sounds. Type (One Shot = a single,
  short sound; Loop = a seamless repeating clip), BPM, Key; two samples a run. Specific and
  concise beats a sentence: "Wind howling strong", not "the sound of a lot of wind outside
  during a storm". Sound words Suno says are understood well: whoosh, glitch, rumble, crash,
  bark, kick drum, ambiance. One Shot for pure sound effects; Loop for musical elements or
  background beds — loops may include full musical arrangements. If "coffee shop ambiance"
  gives lofi music, name the parts: "background chatter and clinking cups ambiance". A
  sound too short or too long: state the duration ("5 second long sound of…").
  Blank for sounds-create: ⟨sound word + source + one or two qualities⟩ · loop on/off ·
  tempo · key; length only through the wording of the description — the MCP takes no
  length (DATA_SUNO_LIVE §3; an inference, not Suno's advice).

</section>

<section id="§8" title="SLIDERS">

  Weirdness          Safe → Chaos; "50% is the 'normal' expected result"
                     [OFFICIAL, help "Creative Sliders", ed. 2025-06-03, pre-v6]
  Style Influence    how close you stay to the Style input, Loose → Strong
                     [OFFICIAL, same page]
  Audio Influence    a third slider that appears only with an audio source: an
                     Audio Upload [OFFICIAL, same page] or a Voice ("have the Audio
                     Influence slider up fairly high" [OFFICIAL, help "Voices",
                     ed. 2026-05-01, pre-v6]). Suno does not say it applies to
                     covers or remixes.
  Vocal Gender       [COMMUNITY] the most reliable vocal-gender control available.
  Variety            v6 only — see §4.

  Reported v6 defaults 50 / 50 / 25 (Weirdness · Style Influence · Audio Influence):
  [UNVERIFIED], no source found 2026-11-05. "50% = normal" describes how the slider
  behaves; it is not a stated default.

⚠️ The tables below come from the v4.5–v5.5 era [COMMUNITY]. No one has tested them
on v6. Use them as a starting point and adjust by ear.

[COMMUNITY, v6, one tester, Moe Lueker, 2026-09-19 · https://moelueker.com/blog/suno-v6-guide]
Weirdness 30–50 for detailed prompts; above 50 and under 90 for exploring ("past that
you start hearing weird artifacts"); Style Influence around 40 for generic prompts,
around 65 for precise ones (the values he used: 40 and 65).
[COMMUNITY, v6, not on that page] One user fixed muffled vocals on v6-wild with
Weirdness ~20 and Style Influence ~80.

BY GOAL:
  Authentic genre recreation    Weirdness 20–35% · Style Influence 90–100%
  Balanced creative fusion      Weirdness 40–50% · Style Influence 70–85%
  Wild experiment               Weirdness 70%+   · Style Influence 40–60%  (or v6-wild)
  Faithful remix                Weirdness 20–30% · Style Influence 90%+
  Transformative remix          Weirdness 50%+   · Style Influence 60–75%

BY GENRE:
  Rock / metal        Weirdness 40–60% · Style 70–85%  low weirdness = clean guitars
  Electronic / EDM    Weirdness 50–80% · Style 50–70%  tolerates chaos well
  Jazz / classical    Weirdness 30–50% · Style 75–95%  accuracy is the point
  Lo-fi / hip-hop     Weirdness 45–65% · Style 65–80%  groove needs some slack
  Vocal-forward       Weirdness 40–50% · Style 80–95%  protects vocal quality
  Instrumental        Weirdness 35–55% · Style 80–90%  clarity over surprise
  Pop / radio         Weirdness 20–35% · Style 85–95%  predictability is the goal
  Trap / rap          Weirdness 35–55% · Style 70–85%
  Country             Weirdness 25–40% · Style 85–95%  genre fidelity is critical
  Cinematic / epic    Weirdness 30–50% · Style 80–90%  controlled drama
  Ambient / drone     Weirdness 30–55% · Style 75–90%
  Metalcore / extreme Weirdness 45–65% · Style 70–85%  [COMMUNITY, v6] v6 is reported
                                                       weakest on metal — try v6-wild
  Drum & bass         [COMMUNITY, v6] reported weak on v6 — try v6-wild
  Gospel / choir      Weirdness 25–45% · Style 85–95%  arrangement must stay legible
  Folk / singer-songwriter  Weirdness 25–45% · Style 80–95%

FOR EXTEND: lower weirdness than the base track, around 45–55% [COMMUNITY, pre-v6].
High weirdness during extension is a common cause of sudden genre shifts.

</section>

<section id="§9" title="SUNO STUDIO 2.0">

[OFFICIAL] "Studio 2.0 is here", 2026-08-13 — a total overhaul of the browser-based
DAW. **Premier only.** Web.

  MIDI               import, record and edit MIDI on the timeline; play with a MIDI
                     controller or the typing keyboard
  Chat bar           generate instruments and vocals, create new plugins and synth
                     presets, ask for help; aware of BPM and able to undo prompt
                     edits (2026-09-02); creates new audio stems from a MIDI clip and
                     renames clips on request (2026-09-17)
                     How it behaves [OFFICIAL, help 13670721, ed. 2026-08-13, pre-v6]:
                     beta; two surfaces, the floating Magic Bar and a docked left panel
                     (the 1 key toggles); requests are grounded in the focused track,
                     the selection and the tempo; an ambiguous request gets a
                     clarifying poll; every chat edit undoes with Cmd+Z; history kept
                     per project (clearable in settings); composes MIDI parts,
                     generates alternate audio takes for a selected section, builds
                     custom effect plugins offered as "Add to track". Plan and credit
                     cost are not stated on that page.
  Session chores     [OFFICIAL, blog "Meet Chat", 2026-10-29; a how-to, not stated as
                     new]: "Rename each track according to the clip name" · "Bring
                     all of the tracks down by 3dB" · "Add the Compressor and EQ
                     effect to each track" · "Put a high-pass filter up to 82 Hz on
                     every EQ in the project" · creative options and feedback on
                     request.
  Audio effects      including sidechain compression and convolution reverb, or
                     designed through the chat bar
  Wavetable synth    basses, leads, pads, chords; presets designed through the chat bar
  Musical typing     play MIDI parts from the keyboard, with arpeggiator and chord mode
  Automation         effect parameters that change over time
  Stems              right-click a clip → Split Stems (§10)
  Downloads          from Studio, without the monthly download limit [OFFICIAL]
  2026-10-08         better downbeat detection for new clips (a cappella included),
                     clip time-stretch by shift-click-drag, exponential and
                     logarithmic fade curves, pop-out windows for synth, typing
                     keyboard and plugins [OFFICIAL]
  Plan page wording  "now with MIDI, effects, automation, and design-your-own-plugins"
                     (2026-10-28) [OFFICIAL]

  Carried from 1.1/1.2 (not re-listed by Suno for 2.0, assume present) [UNVERIFIED]:
  6-band Track EQ with presets, Loop Recording, Context Window, Cover on stems,
  Remove FX, Warp Markers, Alternates (take lanes), time signatures beyond 4/4.

EXPORT: full song, a selected time range, multitrack; MIDI from stems costs credits
[OFFICIAL].

WHAT IT CHANGES ABOUT PROMPTING: less. Studio moves fixes downstream. Prompt for the
performance; repair the mix in Studio. What goes to a DAW, and how: DATA_POSTPROD.

</section>

<section id="§10" title="STEM SEPARATION — three modes">

[OFFICIAL] Overhauled 2026-06-11. From the library: More Actions → Get Stems → pick
the split → Extract. In Studio: right-click the clip → Split Stems.

  Auto Split        "up to 12 stems" — the classic full split
                    Pro + Premier · the expensive one: 50 credits an extraction
                    [OFFICIAL, help 13925185, ed. 2026-09-09] — five generations' worth
                    at 10 credits each (v6 FAQ, help 13924481)

  Split from Mix    "a single instrument or vocal, plus a complement track"
                    Pro + Premier · 10 credits a stem, and the complement is the
                    second stem: "20 credits total for both stems created" [OFFICIAL,
                    help "Advanced Stem Separation" 12702337, ed. 2026-06-12, pre-v6;
                    help 13925185, ed. 2026-09-09: "10 credits per stem"]

  Advanced Split    choose from "nearly 100 instruments" — "Choose exactly what to
                    extract". Suno says the overhaul made stems "cleaner, crisper,
                    free from artifacts" across the tool [OFFICIAL]; that the top
                    mode regenerates rather than filters is v3 wording [UNVERIFIED]
                    **Premier only** · 10 credits a stem [OFFICIAL, help 13925185,
                    ed. 2026-09-09]. Whether a complement is billed too is unclear:
                    the 2026-06-12 page's sentence for this mode is ambiguous

  Free: no stem separation [OFFICIAL].
  Downloads: all stems of a song count as that one song's download [OFFICIAL].
  Asking for an instrument the song does not contain "may still use credits", and
  may not give a usable stem [OFFICIAL, help 12702337, ed. 2026-06-12, pre-v6].

WHEN TO USE WHICH:
  a quick vocal/instrumental split          → Split from Mix
  the full band laid out for a DAW          → Auto Split
  one clean instrument, artifacts unacceptable → Advanced Split

External separation tools are the fallback, not the default — DATA_POSTPROD says when
leaving Suno still wins.

</section>

<section id="§11" title="LYRICS EDITOR">

[OFFICIAL] Rebuilt 2026-07-09, web:
  Lyricist                 lock in a writing voice and reuse it across songs
  Natural language editing ask for changes in plain words
  Variations and References rhyme and reference suggestions
  Song structure labels    "Add labels like "Verse" and "Outro"… tell Suno how you
                           want the song to flow" — you place them
  Autosave · Full screen editor

The plan table also lists "Co-write with Suno", "Inspire" and "Magic Song
Descriptions" as creation features [OFFICIAL].

WHAT THIS CHANGES FOR PROMPTING:
  Two paths coexist and a prompt system must support both:
  - web with the editor → lyrics plus labels placed with the editor's label tool
  - mobile, pasting, automation, exact control → supply lyrics already marked up
  CORE_02 §2 covers both.

</section>

<section id="§12" title="PLANS — what each one unlocks">

[OFFICIAL] Plan names and what they unlock. Prices are deliberately absent.

  FREE      v6-mini only · a daily credit allowance · standard features · shared
            queue (4 songs at once) · audio uploads up to 8 minutes · no stems ·
            no add-on credits · NO monthly downloads (see below) · NO COMMERCIAL
            RIGHTS · Remix (extend, cover, adjust speed) and Co-write with Suno ·
            Voices "to try" per the 2026-08-07 note, locked per the 2026-10-28 table
            · Speech (beta) · the Suno MCP (beta, §16)

  PRO       v6 and v6-wild · a monthly credit allowance · 20 song downloads a month
            · commercial use rights · Auto Split and Split from Mix · own voice ·
            Custom Models · audio uploads up to 30 minutes · priority queue (up to
            10 songs at once) · extra credits and downloads purchasable · early
            access to new features · Shareable Workspaces

  PREMIER   everything in Pro · Suno Studio 2.0 · 60 song downloads a month ·
            Advanced Split (Premier only — the pricing page, help 12702337 and 13925185,
            release note 2026-06-11 [OFFICIAL, checked 2026-11-04]; Suno's mail of
            2026-10-31 to a Pro account listed it anyway — a promo, not a grant) · add new vocals or
            instrumentals to existing songs · a larger monthly credit allowance ·
            shareable Custom Models

  Credits bought on top do not expire but need an active subscription [OFFICIAL].

─── DOWNLOADS — since 2026-09-03 ─── [OFFICIAL] https://help.suno.com/en/articles/13614785
  Free      "Up to 7 total (lifetime) trial downloads for personal, non-commercial
            use only" — for accounts that existed before 3 September; accounts
            created later "may occasionally receive trial downloads"
  Pro       20 per month, with commercial use rights
  Premier   60 per month, with commercial use rights; unlimited from inside Studio

  Formats in the download dialog: M4A · MP3 · WAV · video MP4 · stems and MIDI [first-hand,
  Pro, 2026-11-04]; the MCP gives MP3 and WAV only. The MP4 is a lyric video — cover, the
  lyrics in time, "made with Suno"; in one export the Cyrillic title came out as "NO GLYPH"
  placeholder boxes (on a phone they pass for a narrow font) while the lyrics showed fine —
  zoom in on the title before posting, or use a Latin title [first-hand, one export, 2026-11-04].
  One song = one download, whatever the format. Stems count as part of the song's
  download. Re-downloading the same song is free. Unused downloads do not roll over.
  More can be bought. The caps apply to every song, including ones made before
  3 September; every song stays playable and shareable on Suno.

─── THE RULE THAT CHANGED ─── [OFFICIAL] the terms: https://suno.com/terms-of-service
  Commercial rights now follow the DOWNLOAD, not the generation:
  "You may not commercially exploit Output that has not been downloaded by you
  through an approved channel." Suno: "Songs downloaded from Suno on paid plans remain
  yours to use commercially or personally."

─── SONGS MADE WITHOUT A SUBSCRIPTION ─── [OFFICIAL, help center, edit date not checked]
  "Songs made while not subscribed can now qualify by using one of your paid download
  credits." Without a paid download credit such a song is not eligible. The same
  article: original creators can make remixes of their own songs commercial the same
  way; remixes of someone else's song never qualify.

  PRACTICAL CONSEQUENCES:
  - What makes a song commercial is a download with a PAID download credit
  - A Free-plan song can become commercial later: subscribe (or buy downloads) and
    download it with a paid download credit — older advice that "upgrading later does
    not change that" is out of date
  - Free's trial downloads are personal and non-commercial
  - Remixes of other people's songs are non-commercial on every plan (DATA_LEGAL §2)
  - Whether a download made through the Suno MCP is an "approved channel" is not
    stated (§16) — for a release, download in Suno itself
  Full rights picture: DATA_LEGAL.

</section>

<section id="§13" title="WHAT SHIPPED — the moving parts">

[OFFICIAL] Chronological, so a stale copy of this file can be diffed quickly:

  2026-01-20  Mashup (two songs) and Sample
  2026-01-27  Sounds — one-shots and loops from scratch
  2026-02-16  Studio 1.2
  2026-03-26  v5.5 — Voices, Custom Models, My Taste
  2026-05-13  Android Auto and CarPlay
  2026-05-14  mobile overhaul, vocal gender selector, Create memory
  2026-06-04  iOS: lyrics from Notes, audio from Voice Memos
  2026-06-11  stem separation overhaul — three modes
  2026-07-07  custom soccer anthem generator, mobile
  2026-07-09  lyrics editor rebuilt
  2026-07-15  iMessage keyboard
  2026-07-20  Duration slider (then v5.5, web)
  2026-07-31  cover art editing with text prompts
  2026-08-07  Voices on iOS and Android; Free can try Voices
  2026-08-10  new terms published, effective 2026-09-03; download limits announced
  2026-08-13  Studio 2.0
  2026-08-14  Studio shortcuts help: delete time (Cmd/Ctrl+Shift+Backspace), duplicate time, fade
              toggle; no crossfade shortcut
  2026-08-19  playlist improvements · 2026-08-20 offline playlists on mobile
  2026-09-02  Studio updates — BPM-aware chat bar, plugin copying
  2026-09-03  new terms and download caps in force
  2026-09-08  partnership with Believe and TuneCore
  2026-09-09  v6, v6-wild, v6-mini; every earlier model retired; Max Mode; Variety
  2026-09-17  Studio: better MIDI, stems from a MIDI clip
  2026-10-01  Speech (beta) — voice and music in one take; Community Guidelines and
              Safety page updated (Content Credentials, DATA_LEGAL)
  2026-10-05  Albums
  2026-10-08  Studio: downbeat detection, clip stretch, fade curves, pop-out windows
  2026-10-15  Collaboration: Shareable Workspaces, shareable Custom Models
  2026-10-23  iOS 1.93: iPhone Duo, AirPlay
  2026-10-28  Suno MCP (beta) — generate from Claude, ChatGPT, Gemini and other
              MCP clients (§16)
  2026-10-29  Studio: Clip Settings sidebar (volume, pitch, loop, reverse, stretch), auto-stretch
              of library and uploaded clips to the project tempo, fine pitch in cents
  2026-11-04  Suno MCP schema change: clip_count gone (two takes a call), max_mode added
              (DATA_SUNO_LIVE §3)

  No patch to the v6 models themselves has been announced since 2026-09-09.
  Official programmatic access now exists: the Suno MCP and the Suno API portal (§16).

</section>

<section id="§14" title="MYTHS — kept here so they stop circulating">

These appear in guides, in previous SunoForge editions, and in forum advice.
None survived checking. Listed so the system can recognize and repair them.

  "MAX MODE tags unlock hidden quality"
  [UNVERIFIED] Controlled comparison (Jan 2026) found no hidden mode behind
  [Is_MAX_MODE: MAX] or (MAX)(MAX)(MAX)(MAX). Originates from a single Reddit post.
  ⚠️ Suno's REAL Max Mode (2026-09-09) is a toggle in the interface (§4). It shares
  the name and nothing else. Typing MAX into the prompt does not switch it on.

  "Style attention dies after 200 characters"
  [UNVERIFIED] No test shows a cliff there. Influence fades gradually.

  "Parametric tags control the mix"
  [UNVERIFIED] [Reverb: 30%], [BPM: 120], [eq: scooped] were never parsed.
  On v6, typing "weirdness 20%" into Style "does not move anything" [COMMUNITY].

  "Pipe stacking is deprecated and causes artifacts"
  [UNVERIFIED] Never documented as deprecated, never reproduced. Also never
  documented as supported. No v6 evidence either way.

  "Tracks drift to generic pop after two minutes"
  [UNVERIFIED] as a fixed threshold. Suno does recommend Max Mode for songs over two
  minutes and for whole-track consistency [OFFICIAL] — the concern is real, the
  schedule is folklore, and the cure is the toggle.

  "v5/v5.5 has 88% prompt adherence"
  [UNVERIFIED] No such metric was ever published.

  "Studio comes with Pro"
  [OFFICIAL — corrected] Premier only, in 1.2 and in 2.0.

  "The free tier caps songs at about two minutes"
  [OFFICIAL — corrected] v6-mini, like the rest of v6, generates up to 8 minutes.

  "My Suno songs are commercial because I made them while subscribed"
  [OFFICIAL — corrected since 2026-09-03] Rights follow the download on a paid plan.

  "A song made on Free can never become commercial"
  [OFFICIAL — corrected, help center, October 2026] A paid download credit can make
  it eligible (§12).

  "Suno has no official API, so it cannot be driven from an AI assistant"
  [OFFICIAL — corrected 2026-10-28] The Suno MCP (beta) and the Suno API portal (§16).
  Tool names from third-party "Suno MCP" servers are not Suno's.

  "Variety changes my lyrics"
  [COMMUNITY — measured] It rewrites Style only (§4).

</section>

<section id="§15" title="SPEECH (beta) — voice and music in one take">

[OFFICIAL] Launched 2026-10-01, opened "to everyone", web, iOS and Android: "the first
model to create a speech and its soundtrack together, in one take" — a bedtime story
over soft piano, a pep talk over stadium drums. A separate Speech tab in Create, next
to Songs; not an entry in the model picker.

WHAT YOU FILL IN [COMMUNITY: UI reviews 2026-10-02/03; matches first-hand screenshots
2026-10-28]:
  Simple     one line with the idea; Suno writes the words and picks voice and music
  Advanced   Script — the exact words to be spoken
             Tone — UI hint "Describe the delivery: tone, pacing, mood and setting";
             the music is described here too
             Vocal Gender — Male / Female
             Background music — On / Off (Off = plain narration)
             Variety — five steps, "Exact style" to "Unreasonably varied"

NOT PUBLISHED [UNVERIFIED]: supported languages (non-English scripts came back word for word
in first-hand takes through the MCP [DATA_SUNO_LIVE §3]; Japanese reported [COMMUNITY]), the
maximum duration in the docs (about 8 min by the press, below), credit cost in the docs,
separate rights terms. Until Suno says otherwise the general rule applies: rights
follow a paid download (§12).
[COMMUNITY] The web form offered no own Voice for Speech in October; the MCP's speech-create
has a `voice_id` field [OFFICIAL, schema 2026-11-04], not tried yet. There is no word-level
timing and no pause control.
[OFFICIAL, launch post] "Beta really does mean beta": dramatic pauses can run long and
accents can wander mid-read.

WHAT THE FORM GATES — facts; how to write the Script and the Tone is CORE_02 §16
(menu [14]), the only copy of the method:
  - Advanced whenever the words must be exact: numbers, names, brands, facts; Simple
    writes its own script from one line
  - Clean narration: Background music Off, Variety at "Exact style"
  - Nothing documents bracket tags or speaker labels in the Script; one voice a take
  - Length: "a maximum duration of around eight minutes" — Suno's CPO to the press on
    2026-10-02 [COMMUNITY: press, not documentation]; through the MCP 15–360 s
    (DATA_SUNO_LIVE §2). Languages and the price are not published; a speech generation
    cost 10 credits for two takes through the MCP [first-hand, 2026-11-04] and 10 in the
    web UI [COMMUNITY, one test, 2026-10]. Speech downloads count against the plan's
    monthly downloads [COMMUNITY].

</section>

<section id="§16" title="SUNO MCP AND THE SUNO API — Suno from an AI tool">

[OFFICIAL] Suno MCP (beta), release note 2026-10-28: an official remote MCP server at
`https://api.suno.com/mcp`. "No API key · Uses your Suno credits · Songs save to your
library." Sign-in is OAuth with the Suno account; one account can serve several
assistants. Suno's setup page covers Claude (custom connector), Claude Code
(`claude mcp add --transport http suno https://api.suno.com/mcp`, then `/mcp` to sign
in), ChatGPT (custom MCP server added as a plugin), Gemini (custom MCP server, then
mention @Suno), Cursor and other MCP clients.

ACCESS: the release note says all plans, Free included; the same page runs an
early-access form that promises an answer "within 24-48 hrs". An account not yet
admitted gets, at sign-in, "Connecting AI apps to Suno is not yet available for your
account" [first-hand, 2026-10-28]. Some AI apps allow custom connectors only on their
own paid plans [OFFICIAL].

WHAT IT DOES [OFFICIAL, help center "Suno MCP (Beta)"]: ideas, lyrics and conversations
into songs · covers, extends and mashups of library songs · Speech · upload audio and
build on it · add songs to playlists from the chat · plan and remaining credits. The
product page adds singing with your own Suno Voice, and edits to a finished song in
plain words ("slower", "add a bridge") [OFFICIAL, suno.com/mcp] — through the tools that
means a new take, a cover or an extension (DATA_SUNO_LIVE §3).

LIMITS NAMED BY THE PRESS [COMMUNITY: AlphaSignal 2026-10-28, Glitchwire 2026-10-29]:
every connected AI app draws on the account's one credit balance — no separate
budget per assistant; sign-in is by a person, there are no service credentials
for unattended runs; no separate licence terms for songs made through the MCP;
rate limits, model choice and the date of general availability are not published.

THE CONSENT SCREEN asks to [first-hand, 2026-10-28]: act through the Suno API, spend
credits, download songs with download credits, view and search the library and liked
songs, edit titles and lyrics, organise workspaces, playlists and preferences, stay
signed in, read profile, copyright and subscription information.

WHAT THE SERVER ITSELF SAYS [OFFICIAL, read 2026-10-29, no sign-in]: without a token it
answers 401 "sign in to Suno to use this server"; the scopes it asks for are api:v0,
credits:spend, download, library:read, library:search, library:write, offline_access,
profile:read; its sign-in server accepts both dynamic client registration and client
metadata documents, so any standard MCP client can sign in. The account gate is the
same from every client: terminal Claude Code got the same "not yet available" page as
the claude.ai connector [first-hand, 2026-10-29].

TOOLS AND FIELDS: DATA_SUNO_LIVE — the tools, the field map, the defaults that cost
credits and the plan gating, read from the server on 2026-10-29. Not published
[UNVERIFIED]: rate limits; whether a download through it counts as an "approved
channel" for rights (§12).

RULE FOR THIS SYSTEM: never name a Suno MCP tool or parameter from memory. Read the
tools the session actually has, map the blueprint onto what they accept, and say
plainly what could not be passed. Protocol: CORE_00 §6, LIVE — generic for every
generator; what is Suno-specific stays here and in DATA_SUNO_LIVE:
  - third-party "Suno MCP" servers are resellers, their tool names are not Suno's
  - a release needs a download made with a paid download credit (§12); the MCP as an
    approved channel is not stated; the beta gate and the operations list: above

[OFFICIAL] platform.suno.com: "Make music with the Suno API" — "Suno's music generation
engine behind a simple REST API"; sign-in with the Google account linked to Suno or an
emailed code. The page names no endpoints, plans, waitlist or documentation (checked
2026-10-29). In July Suno spoke of "a developer API, starting with a curated group of
partners" [COMMUNITY: press].
Third-party "Suno APIs" and "Suno MCP" servers are resellers and wrappers, not Suno;
their tool names are not the official ones.

</section>

<section id="§17" title="SHARING — workspaces, shared models, albums">

[OFFICIAL] 2026-10-15, web:
  Shareable Workspaces     a song library shared with a team; "Only the people you
                           invite can access a workspace". Pro and Premier. A remix
                           made inside a workspace stays in it.
  Shareable custom models  share a Custom Model with collaborators, "now with double the
                           inputs". Premier only. The new track count is not stated,
                           and the Custom Models help page still says "private".
  Not published: whose credits a shared workspace spends; who owns songs made there.

[OFFICIAL] Albums, 2026-10-05, web, iOS, Android: an LP or EP of your own songs only; a
playlist can become an album. Publishing an album publishes every unpublished song in
it and notifies followers — those songs turn public and open to remixes unless "Allow
Remixes" is off (§7). Albums change no rights.

</section>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_SUNO_2026-10.md · SunoForge v5.0
// Snapshot date 2026-11-04 · replace this file, not the CORE files
// ═══════════════════════════════════════════════════════════════
</sunoforge_file>
