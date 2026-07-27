---
file_id: CORE_02_LYRICS
version: "3.0"
layer: core
scope: bracket_rule · two_paths · section_labels · performance_notation · delivery · adlibs · spoken_word · duet · chords · structure_templates
key_concepts: [round_vs_square, editor_path, manual_path, section_labels, label_density, performance_notation, emotion_line, adlibs, spoken_word, duet_three_anchors, inline_chords, structure_templates]
depends_on: [CORE_00_ENTRY, CORE_01_STYLE]
used_by: [CORE_03_DIAGNOSE, CORE_04_WHY, DATA_RECIPES, DATA_SUNO, DATA_GOOGLE]
rag_priority: critical
updated: "2026-07-27"
changelog: "v3.0 — two paths documented (Suno's rebuilt editor labels sections itself) · verbose section labels demoted from mandatory to optional · pipe stacking presented as genuinely disputed · DRIFT_GUARD per-section reminders removed as a mechanism · parametric tags stripped from top-load template and chord section · duet protocol consolidated here from CORE_01"
---

# 📝 SUNOFORGE v3.0 — LYRICS ENGINE
# File 3 of 12 · CORE · Structure, notation, and how words are sung

> This file covers menu entry **[6] LYRICS WORKSHOP** and the duet protocol at
> **[5c]**. Numbers per CORE_00 §4.
>
> The Style field decides what the record sounds like (CORE_01). The Lyrics
> field decides what happens, when, and how it is delivered. They are different
> instruments and the most common mistake is playing one on the other.

═══════════════════════════════════════════════════════════════════
§1. THE BRACKET RULE
═══════════════════════════════════════════════════════════════════

<rag_zone id="bracket_rule">

This is the rule that breaks the most tracks. It is also the easiest to get
right, because it has no exceptions.

─── ( ) ROUND BRACKETS ARE SUNG ───

Everything inside round brackets is performed as audio — backing vocal, echo,
an answering voice [COMMUNITY, consistent everywhere and easy to verify
yourself in one generation].

    ✅  (I'm still here)          a soft echo behind the lead
    ✅  (Yeah!)  (Ooh-whoa)       ad-libs, sung as background
    ✅  (never again)             an answering phrase

    ❌  (say this in a spoken voice)   the model sings the instruction
    ❌  (play the guitar softly here)  the model sings "play the guitar softly here"

If you would not want to hear it, it does not go in round brackets.

─── [ ] SQUARE BRACKETS ARE NOT SUNG ───

Square brackets carry direction: what section this is, who is singing, how the
next lines are delivered.

    ✅  [Chorus]            a structural boundary
    ✅  [Guitar Solo]       an instrumental passage
    ✅  [Spoken word]       the lines below are spoken, not sung
    ✅  [Whisper]           the lines below are whispered

─── WHAT SQUARE BRACKETS ARE NOT FOR ───

Brackets carry **structure and performance direction**. They do not carry
**measurements or mix settings**.

    ✅  [Bridge]  [Whisper]  [Guitar Solo]  [Spoken word]  [Final Chorus]
    ❌  [BPM: 120]  [Key: A minor]  [Reverb: 30%]  [eq: scooped]
    ❌  [Mood: Uplifting]  [Energy: Low→High]  [Chord progression: Am - F - C - G]

The second group is the parametric syntax. It was never parsed by any covered
platform [UNVERIFIED — no vendor documentation, no controlled test showing an
effect] and it is in every previous edition of this system. Everything in that
group belongs in the Style field as prose, or — for chords — in the inline form
described in §10. Repair procedure for prompts that contain it: CORE_03 §7.

  The distinction is not cosmetic. "Whisper" tells the model how to perform the
  next line, which is something a singer can act on. "Reverb: 30%" is an
  instruction to a mixing desk that is not in the room.

─── THE SPOKEN WORD COROLLARY ───

    ✅  [Spoken word]
        The city never asked me to stay.

    ❌  (say this next part as spoken word)
        The city never asked me to stay.

The second version produces a backing vocal singing the words "say this next
part as spoken word".

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. TWO PATHS — the editor and the markup
═══════════════════════════════════════════════════════════════════

<rag_zone id="two_paths">

Suno rebuilt its lyrics editor in July 2026 [OFFICIAL], and one of the things
it now does is place section labels itself. That changes the advice this system
gives, because "always mark up your lyrics by hand" is no longer true
everywhere — it is true in some places and redundant in others.

Both paths are live. A prompt system has to support both.

─── PATH A · THE WEB EDITOR PLACES THE LABELS ───

  WHEN: composing on the Suno website with the current editor.

  WHAT YOU SUPPLY: clean lyrics, verses and choruses separated by blank lines,
  no brackets at all.

  WHAT THE EDITOR DOES: identifies the sections and marks them.

  WHAT YOU STILL DO BY HAND:
    - performance notation inside the text (§5) — the editor does not add it
    - delivery direction where it matters (§6)
    - speaker labels in a duet (§9)
    - anything the editor guesses wrong

  The editor also carries writing-voice profiles, plain-language editing,
  rhyme and reference suggestions, and autosave. Feature details and dates:
  DATA_SUNO §10.

─── PATH B · YOU PLACE THE LABELS ───

  WHEN: the API · the mobile app · pasting lyrics written elsewhere ·
  any platform that is not Suno web · any time you want exact control.

  WHAT YOU SUPPLY: fully marked-up lyrics as described in the rest of this file.

  This path is the one that has to be documented in full, because it is the one
  where mistakes are possible. Everything from §3 onward assumes Path B unless
  it says otherwise.

─── WHICH TO CHOOSE ───

  Writing in the browser, standard song shape        → Path A, then adjust
  Unusual structure, or the section boundaries matter → Path B
  Duet, spoken word, heavy performance notation      → Path B
  Automating anything                                 → Path B
  Targeting Lyria, Flow, ElevenMusic or Stable Audio → neither; see §14

─── WHAT NOT TO DO ───

Do not hand-mark lyrics *and* expect the editor to leave them alone, without
checking. If both you and the editor place labels, you can end up with two
overlapping structures. Look at the field after pasting.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. SECTION LABELS — the catalogue
═══════════════════════════════════════════════════════════════════

<rag_zone id="section_labels">

─── MAIN STRUCTURE ───

  [Intro]           opening; sets the palette before anything is asked of it
  [Verse]           narrative; lower energy than the chorus by design
  [Verse 1] [Verse 2] [Verse 3]
  [Pre-Chorus]      the lift; short lines, rising
  [Chorus]          the hook and the emotional peak
  [Post-Chorus]     an extension of the hook — chants, chops, a response figure
  [Bridge]          contrast. If it sounds like another verse, it has failed
  [Final Chorus]    the last one, usually bigger
  [Outro]           the exit; leave room for it
  [Hook]            a memorable phrase standing on its own
  [Refrain]         a repeated line inside verses rather than a full chorus

─── ENERGY AND DYNAMICS ───

  [Build]  [Build-Up]      rising tension
  [Drop]                   the release
  [Breakdown]              stripped back, space to breathe
  [Break]                  a short pause for contrast
  [Instrumental]           no vocal at all
  [Solo]  [Guitar Solo]  [Sax Solo]  [Piano Interlude]
  [Interlude]              a passage between sections
  [Fade In]  [Fade Out]
  [Beat switch]            the rhythm changes here
  [Emotional release]      the moment the song has been building toward
  [Band drop-out]          arrangement strips away, usually before a final chorus

─── SHAPE AND REPETITION ───

  [Hook first]             open with the hook instead of a verse
  [Hook Loop]              a hook built to loop seamlessly — short-form video
  [Chorus x2]              repeat
  [Callback]               return to an earlier melodic idea

─── QUALIFIED SECTIONS ───

A section label may carry a short qualifier describing the *kind* of section it
is. This is still structure, not parameters:

  [Outro — big finish]        [Outro — fade out]
  [Bridge — half time]        [Chorus — a cappella]
  [Verse — stripped to voice and guitar]

Write the qualifier as words. Do not write it as a measured value.

─── PLACEMENT ───

  1. A label sits on its own line, immediately above the text it governs.
  2. Every section gets one. Sections without labels are where structure
     dissolves first [COMMUNITY].
  3. Put [Chorus] above each chorus — not once at the top of the file.
  4. Blank line between sections. It costs nothing and it helps both the model
     and the human reading it [COMMUNITY].
  5. Section labels are hints, not guarantees (CORE_00 §7 rule 10). Generate
     several takes.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. HOW MUCH TO PUT IN A LABEL — three styles, honestly rated
═══════════════════════════════════════════════════════════════════

<rag_zone id="label_density">

There are three ways people write section labels. Previous editions of this
system declared a winner. The evidence does not support declaring one, so this
version describes all three and says what is actually known about each.

─── PLAIN ───

```
[Chorus]
We rise above the storm
```

  STATUS: [COMMUNITY, well supported] — plain structural labels plus
  descriptive language in the Style field is the approach independent guides
  converge on, and it is the closest thing to an official line that exists for
  Suno. It is the default in this system.

─── ENRICHED ───

```
[Chorus — female lead, belted, full arrangement, stacked harmonies]
We rise above the storm
```

  STATUS: [COMMUNITY, undocumented] — widely used, never described by the
  vendor. Reasonable people report it helps. Nobody has measured it.

  USE IT WHEN: a section needs to differ audibly from the one before it in a
  way the Style field cannot express, because the Style field applies to the
  whole track. A whispered bridge in a loud song is the clearest case.

  DO NOT: put the same enrichment on every section. If every label says "full
  arrangement, stacked harmonies", the label has stopped carrying information.

─── PIPE STACKED ───

```
[Chorus | 90s grunge | belted male]
We rise above the storm
```

  STATUS: [COMMUNITY, disputed] — and the dispute is real, not a formality.
  Some 2026 guides introduce pipe stacking as current best practice. Others
  state that plain labels work just as well and that the syntax was never
  documented by Suno in the first place. A claim that it is "deprecated in the
  current model and causes artifacts" circulated widely and could not be
  reproduced in any controlled test.

  WHAT IS ACTUALLY KNOWN: Suno has never documented this syntax in either
  direction. Neither side of the argument rests on a primary source.

  THEREFORE: use it if it works for you. This system does not emit it by
  default and does not remove it from a user's prompt on sight. If a user asks
  about it, say what the previous paragraph says rather than picking a side.

  ⚠️ Previous editions of this system stated that stacks beyond three or four
  modifiers cause hissing and vocal clipping. That claim had one source, was
  never reproduced, and is withdrawn.

─── THE ONE THING ALL THREE AGREE ON ───

Whatever style you use, a label describes *this section*, and its job is to say
how this section differs from the last one. A label that repeats the Style
field is spending space to say something already said.

─── SECTION-LEVEL STYLE RESTATEMENT ───

Restating the genre and production inside later section labels is a technique
some users rely on for long tracks:

```
[Final Chorus — belted, distorted guitar wall, raw and unpolished]
```

It is legitimate craft and costs nothing. What it is *not* is a cure for a
documented condition. Previous editions built an automatic mechanism on top of
this idea, on the assumption that tracks reliably degrade after two minutes —
an assumption that has no systematic testing and no vendor acknowledgment
behind it [UNVERIFIED]. The mechanism is gone; the technique remains available
to anyone who finds it helps. Long-track consistency is discussed as a failure
mode in **CORE_03 §5**.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. PERFORMANCE NOTATION — symbols inside the words
═══════════════════════════════════════════════════════════════════

<rag_zone id="performance_notation">

These are not labels. They are marks inside the sung text that change how a
syllable is delivered [COMMUNITY — widely used, easy to verify, never
documented].

  SYMBOL      EFFECT                                  EXAMPLE
  ─────────── ─────────────────────────────────────── ─────────────────────
  ~           hold the note, let it move in pitch     ho~me · free~dom~
  -           stretch or break a word into syllables  al-most · G-A-L-A-X-Y
  ALL CAPS    louder, harder, more force              WE RISE together
  " "         spoken, whispered, set apart            "you were never there"
  ...         sustain; more dots, longer hold         fading......................
  /           an alternative reading, not sung        soft / broken

─── CAPITALS ───

  ✅  WE RISE together           one or two words carry the accent
  ✅  NEVER coming back          a single word takes the whole weight
  ❌  WE RISE TOGETHER NOW       everything shouted is nothing emphasised

  One to three capitalised words per section. Past that, emphasis stops being
  emphasis and the delivery flattens out.

─── STRETCHING VOWELS ───

More letters means a longer, more committed delivery:

    goodbye  →  goo-o-o-odbye        a held, breaking note
    ah       →  AAAAAH               a full scream

  This is the standard way to write screams and growls, paired with a delivery
  label:

```
[Scream]
AAAAAH WE WILL NEVER BOW
```

─── SUSTAIN AND DRONE ───

```
[Vocal drone]
(deep resonant)
whispers......................
```

  The ellipsis length is the note length. The round brackets here are correct
  because "deep resonant" is meant to be *heard* as a quality of the sung drone,
  not read as an instruction — this is the one place the round-bracket rule
  looks like an exception and is not.

─── WHERE NOTATION DOES NOT REACH ───

Notation shapes syllables. It does not shape a whole passage. For "this verse
is sung differently from the last one", use a delivery label (§6). For "the
voice changes across the whole song", that is the vocal arc and it belongs in
the Style field (CORE_01 §6).

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. DELIVERY AND EMOTION
═══════════════════════════════════════════════════════════════════

<rag_zone id="delivery_labels">

─── DELIVERY STYLE ───

  [Whisper]              intimacy, ballads, ambient
  [Spoken word]          speech, not singing
  [Rap]                  rhythmic delivery
  [Chant vocals]         a group chanting together
  [Crowd-style vocals]   many voices, stadium energy
  [Harmonies]  [Stacked harmonies]
  [Falsetto]             high register
  [Belting]              full-power sustained notes
  [Growl]                aggressive texture
  [Crooning]             smooth and close, vintage
  [Operatic]             classical technique
  [Scat]                 improvised syllables
  [Screaming]            extreme delivery
  [Anthemic chorus]      built to be sung back at you
  [Raspy lead vocal]     hoarse, textured
  [Cinematic vocal pacing]  deliberate, unhurried, dramatic
  [Spoken word verse]    an entire verse spoken

─── VOCAL TREATMENT ───

  [Reverb heavy]  [Echoing vocals]  [Delay]
  [AutoTune]  [No AutoTune]
  [Distorted vocals]  [Filtered vocals]  [Telephone effect]
  [Vocoder]  [Tape-saturated vocal]
  [Harmonized chorus]

  These describe how the voice is treated, which is performance direction, not
  a mix setting with a number attached. Keep them qualitative.

─── CHORAL ───

  [Choir]  [Gospel choir]  [SATB]

  SATB means soprano, alto, tenor and bass together. Use it on the chorus, not
  on the whole song — full four-part writing everywhere removes the contrast
  that made it land [COMMUNITY].

─── EMOTION GOES ON ITS OWN LINE ───

This is the rule worth remembering from this section. Emotional direction sits
on a line of its own, immediately above the text it governs, and not folded
into a section label [COMMUNITY, consistent across guides]:

```
[Crying voice]
Why did you leave me standing there
```

  ✅  the direction is unmistakably attached to the line beneath it
  ❌  buried among five other modifiers in a section label, where it competes

─── THE EMOTION CATALOGUE ───

  [Crying voice]        [Angry tone]         [Mocking laughter]
  [Vulnerable]          [Defiant]            [Sultry]
  [Joyful]              [Melancholic]        [Intimate]
  [Exhausted]           [Tender]             [Bitter]
  [Pleading]            [Resigned]           [Triumphant]

─── EMOTIONAL WHIPLASH ───

Two contradictory directions inside one line produce a break the writing alone
cannot:

```
[Spoken word crying]
Why did you leave me
[Laughter]
```

  Used once in a song, this is devastating. Used three times, it is a tic.

─── DELIVERY VERSUS PERSONA ───

Persona is who is singing and lives in the Style field (CORE_01 §7).
Delivery is how they sing this passage and lives here.
Do not restate the persona in every section label — it is already established.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. AD-LIBS AND BACKING VOCALS
═══════════════════════════════════════════════════════════════════

<rag_zone id="adlibs">

Ad-libs are the interjections between lines — the bounce in hip-hop, trap, pop
and R&B. There are two ways to write them and they do different things.

─── AS SUNG BACKING — round brackets ───

```
Running through the city lights
(hey)
Nothing ever slows me down
(uh, uh)
```

  The content is performed as a background voice. This is the form to use when
  you want the ad-lib to be part of the vocal arrangement.

─── AS DIRECTION — square brackets ───

```
[adlib hey]
[adlib uh]
```

  This asks for an ad-lib without dictating the exact sound. Useful when you
  want the flavour and do not care about the syllable.

─── COMMON AD-LIBS ───

  hey · yeah · whoa · uh · ayy · ok · woo · come on · let's go
  boom · clap · brr · skrrt

─── PLACEMENT ───

  On its own line, between lyric lines, where the gap in the phrasing is. An
  ad-lib written at the end of a full line usually lands on top of the lead
  vocal instead of answering it.

─── BACKING VOCALS THAT ARE NOT AD-LIBS ───

A repeated answering phrase is written the same way and is worth planning
rather than sprinkling:

```
I said I'd never call again
(never again)
And here I am
(here I am)
```

  Answer phrases that echo the lead line are the single cheapest way to make a
  chorus sound arranged rather than sung once.

─── HOW MUCH ───

Two to four ad-libs per verse is a groove. Ten is a mess. They compete with the
lead vocal for the same space, and the lead vocal is carrying the song.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. SPOKEN WORD
═══════════════════════════════════════════════════════════════════

<rag_zone id="spoken_word">

─── THE BASIC FORM ───

```
[Spoken word]
There was a time this street had a different name.
```

─── WITH A CHARACTER ───

Giving the speaking voice a short biography works the same way a sung persona
does — it is a description of a person, and a person implies a delivery
[COMMUNITY]:

```
[Spoken word — weathered narrator, low and gravelly, unhurried]
There was a time this street had a different name.
```

─── WHERE SPOKEN WORD EARNS ITS PLACE ───

  INTRO       sets a scene before any music commits to a mood
  BRIDGE      the strongest contrast available in a sung song
  OUTRO       lets a song end on a thought rather than a chord
  WHOLE TRACK poetry over a bed — a real form, not a fallback

─── WRITING FOR SPEECH ───

Spoken lines are not sung lines with the melody removed. They need different
writing:

  - Sentence rhythm instead of metre. If it scans perfectly, it will sound sung.
  - Rhyme sparingly, or it turns into rap by accident.
  - Shorter than you think. Speech takes longer than melody at the same word
    count, because there is no held note to carry it.
  - Punctuation matters here in a way it does not elsewhere — a comma is a
    breath and a full stop is a beat of silence.

─── SPOKEN WORD AND RAP ARE DIFFERENT LABELS ───

  [Spoken word]  no rhythmic commitment; conversational
  [Rap]          locked to the beat; rhythmic delivery

  Asking for one and writing for the other is a common source of "the vocal
  feels wrong" with no obvious cause.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§9. DUET AND MULTI-VOICE — menu [5c]
═══════════════════════════════════════════════════════════════════

<rag_zone id="duet_protocol">

Two voices are unstable unless the same information appears in three places.
Any single anchor drifts; the three together hold [COMMUNITY].

─── ANCHOR 1 · IN THE STYLE FIELD ───

Establish that this is a duet and who is in it, as part of Layer 4
(CORE_01 §6):

```
a duet between a male baritone and a female alto, trading verses
```

─── ANCHOR 2 · AT THE TOP OF THE LYRICS FIELD ───

Before any section, restate the cast:

```
[Male and female duet]
```

  Note the form. Earlier editions wrote this as `[Duet: male baritone and female
  alto]` — which is the `[parameter: value]` shape this system tells you not to
  use (§1). Writing a rule and then breaking it in your own template teaches the
  broken version. The label above says the same thing without the colon.
  The detailed voice description belongs in Style, where Anchor 1 already put it.
  [COMMUNITY] — the three-anchor method is community practice, not documented.

─── ANCHOR 3 · ON EVERY SECTION ───

Name the singer on each section, every time:

```
[Verse 1]
[Male]
I left the door open behind me

[Chorus]
[Both]
And neither of us said a word

[Verse 2]
[Female]
I counted every hour that you didn't call
```

─── THE STABILITY RULE ───

Assign whole sections to one singer. Do not alternate line by line. Switching
inside a verse is the most common cause of two voices blurring into one
indistinct singer partway through the track [COMMUNITY].

If the lyric genuinely needs line-by-line trading — an argument, a
call-and-response — you can write it, but expect more takes and expect the
separation to be less clean. It is a real trade-off, not a solved problem.

─── HANDLING [Both] ───

`[Both]` produces two voices together, which is not the same as two voices in
harmony. If you want harmony, ask for it where instructions actually land — in
Style:

```
Style:   … duet between a male baritone and a female alto, chorus sung in
         harmony with the female voice above the male …

Lyrics:  [Chorus]
         [Both]
```

  A long descriptive phrase inside brackets — `[Both — in harmony, female above
  male]` — is unlikely to be read as a performer label. Keep bracket labels short
  and put the musical direction in Style.

─── MORE THAN TWO VOICES ───

  Three named voices is workable with the same three anchors and whole sections
  each. Beyond three, the model stops keeping them distinct and you are better
  served by treating the extra voices as a choir (§6) than as characters.

─── NAMES ───

Named characters help the model keep the parts separate and make the lyrics
readable:

```
[Ana and Mikhail duet]
```

with "Ana, a female alto; Mikhail, a male baritone" written into Style.

But the gender and range descriptors are doing the actual work. A name alone
never implies a voice type — never rely on it to.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§10. CHORDS
═══════════════════════════════════════════════════════════════════

<rag_zone id="chord_engine">

─── INLINE, IN ROUND BRACKETS, BEFORE THE WORD THEY LAND ON ───

```
(Am) The city sleeps at night (F) beneath the silver moon
(C) Only the wind is singing (G) its age-old song
```

  This is the working form [COMMUNITY]. The chord sits immediately before the
  syllable where it changes.

  Round brackets are correct here. Chord symbols are short, and in practice
  they are read as harmonic direction rather than sung — but if a take comes
  back with the letters audible, that is what has happened, and the fix is to
  move them to the Style field as prose instead.

─── NOT IN SQUARE BRACKETS WITH A COLON ───

    ❌  [Chord progression: Am - F - C - G]
    ❌  [Key: A minor]
    ❌  [Tempo: 120 BPM]

  Parametric forms (§1). Key and tempo belong in the Style field written out:
  `A minor, 120 BPM` (CORE_01 §9).

─── PROGRESSIONS WORTH KNOWING ───

  I–V–vi–IV     C  G  Am F     the one most songs use
  vi–IV–I–V     Am F  C  G     the same four chords, sadder entry point
  I–vi–IV–V     C  Am F  G     1950s and early 1960s
  vi–V–IV–I     Am G  F  C     descending, modern pop melancholy
  I–IV–V        C  F  G        the foundation of blues and early rock
  ii–V–I        Dm G  C        the jazz cadence
  I–iii–IV–iv   C  Em F  Fm    the borrowed minor fourth; the sting at the end
  i–VII–VI–VII  Am G  F  G     folk-modal, unresolved, circular

─── BY GENRE ───

  POP / ROCK        I–V–vi–IV and its rotations
  BALLAD            vi–IV–I–V; slower harmonic rhythm, one chord per bar
  TRAP / HIP-HOP    i–VI–III–VII in minor; often a two-chord loop instead
  EDM               i–III–VI–VII; the drop usually stays on one chord
  JAZZ              ii–V–I extended with sevenths and ninths throughout
  BLUES             twelve-bar: I I I I · IV IV I I · V IV I V
  GOSPEL            I–IV with passing chords and a heavy plagal cadence
  COUNTRY           I–IV–V with a IV–I turnaround
  FOLK              i–VII–VI–VII, or a drone with a moving upper voice
  CINEMATIC         i–VI, i–III; slow, few changes, weight over motion

─── HOW MUCH HARMONY TO SPECIFY ───

Specifying every chord constrains the melody, which is usually not what you
want from a generative model — the melody is the part it is good at. Two useful
levels:

  LIGHT   name the key and the feel in Style; let the model choose chords
  FIRM    write the progression inline for the chorus only, leave verses open

Writing all four minutes of harmony by hand is possible and rarely improves the
result over the firm level.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§11. ATMOSPHERE AT SECTION LEVEL
═══════════════════════════════════════════════════════════════════

<rag_zone id="section_atmosphere">

Track-wide atmosphere belongs in the Style field as prose (CORE_01 §11). What
belongs here is atmosphere that happens *at a specific point*.

─── ENVIRONMENTAL ───

  [Rain]  [Thunder]  [Wind]  [Ocean waves]
  [Birds chirping]  [Forest]  [Fire crackling]  [City ambience]

─── PEOPLE AND CROWDS ───

  [Applause]  [Cheering]  [Crowd noise]  [Distant chanting]
  [Stadium ambience]  [Clapping]  [Audience laughing]  [Whistling]

─── MECHANICAL ───

  [Phone ringing]  [Static]  [Record scratch]  [Beeping]  [Bell]

─── STRUCTURAL EFFECTS ───

  [Silence]     a full stop; the most underused effect available
  [Fade]        volume down
  [Stop]        abrupt end
  [Drum fill]   a transition into the next section
  [Crossfade]   a smooth one

─── PLAIN FORM, NOT PARAMETRIC ───

    ✅  [Rain]
    ❌  [Sound: Rain]     [sound:thunder]     [Sound: City ambience]

  The colon form is the parametric syntax again (§1). Same words, same intent,
  and the version without the colon is the one that matches how every other
  bracket in this file works.

─── A LIVE PERFORMANCE FEEL ───

```
[Intro]
[Stadium ambience]
[Distant chanting]

...

[Outro]
[Crowd noise]
[Applause]
```

  Bracketed atmosphere at the start and end does more for the illusion of a
  live recording than any amount of "live" in the Style field, because it
  places events rather than describing a quality.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§12. STRUCTURE TEMPLATES
═══════════════════════════════════════════════════════════════════

<rag_zone id="structure_templates">

Starting shapes. Modify them — a template followed exactly is why so much
generated music sounds the same.

─── POP ───
```
[Intro] → [Verse 1] → [Pre-Chorus] → [Chorus] →
[Verse 2] → [Pre-Chorus] → [Chorus] →
[Bridge] → [Final Chorus] → [Outro]
```

─── ROCK ───
```
[Intro] → [Verse 1] → [Chorus] → [Verse 2] → [Chorus] →
[Guitar Solo] → [Bridge] → [Final Chorus] → [Outro]
```

─── EDM ───
```
[Intro] → [Build] → [Drop] → [Breakdown] →
[Build] → [Drop] → [Outro]
```

─── HIP-HOP ───
```
[Intro] → [Verse 1] → [Hook] → [Verse 2] → [Hook] →
[Verse 3] → [Hook] → [Outro]
```

─── BALLAD ───
```
[Intro] → [Verse 1] → [Verse 2] → [Chorus] →
[Verse 3] → [Chorus] → [Bridge] → [Final Chorus] → [Outro]
```

─── CINEMATIC ───
```
[Intro] → [Verse] → [Build] → [Chorus] →
[Bridge] → [Final Chorus] → [Outro]
```

─── INSTRUMENTAL ───
```
[Intro] → [Theme A] → [Theme B] →
[Development] → [Theme A] → [Coda]
```

─── SHORT-FORM, UNDER A MINUTE ───
```
[Hook first] → [Verse — four lines] → [Hook Loop]
```

─── FITTING A STRUCTURE TO A LENGTH ───

Roughly one minute of song is a verse plus a chorus at a moderate tempo. Asking
for a long track with two verses of material produces padding, drift, or an
early cut — the model has nothing to fill the time with.

On Suno the target length is set in the interface, and its behaviour and range
are documented in **DATA_SUNO §4**. The relevant craft point is version-
independent: **set the length and supply enough words to fill it.**

</rag_zone>

═══════════════════════════════════════════════════════════════════
§13. THE TOP OF THE LYRICS FIELD
═══════════════════════════════════════════════════════════════════

<rag_zone id="top_of_field">

─── THE TEMPLATE ───

```
[Male and female duet]                       ← only if there is more than one voice

[Intro]
[Rain]

[Verse 1]
[Male]
first line
second line
```

That is all. The top of the Lyrics field carries the cast and the first section.

─── WHAT DOES NOT GO AT THE TOP ───

    ❌  [BPM: 120] | [Genre: 90s grunge] | [Key: A minor]
    ❌  [Mood: brooding introspective]
    ❌  [Energy: Building]

  Previous editions of this system opened the Lyrics field with a block of
  parametric anchor tags. Every item in it is either a parameter that was never
  parsed (§1) or a restatement of something the Style field already says
  better. Genre, mood, key and tempo are Style-field business (CORE_01).

─── THE `///*****///` SEPARATOR ───

Old prompts sometimes open with a line of slashes and asterisks. It was
believed to activate a hidden quality mode. There is no such mode
[UNVERIFIED — see CORE_00 §2].

  It is harmless. If a user has it in a prompt they like, leave it. Do not add
  it, and do not tell anyone it does something.

─── INSTRUMENTAL TRACKS ───

For a track with no vocals, the Lyrics field carries the arrangement rather
than words:

```
[Intro]
[Instrumental]

[Theme A]
[Piano Interlude]

[Build]

[Theme B]
[Guitar Solo]
```

  On Suno there is also an instrumental switch in the interface, and using both
  the switch and the label is the reliable combination — the switch alone
  occasionally still produces a vocal line [COMMUNITY].

</rag_zone>

═══════════════════════════════════════════════════════════════════
§14. OTHER PLATFORMS
═══════════════════════════════════════════════════════════════════

<rag_zone id="other_platforms">

Almost nothing in this file transfers. Bracket markup is a Suno convention
[COMMUNITY], and carrying it to another platform produces literal text or
nothing at all.

─── LYRIA ───

  Lyrics are supplied inside the prompt, introduced by a `Lyrics:` prefix
  [OFFICIAL]. You may also describe a topic and let the model write the words.
  Structure is expressed as timestamps, not as section labels. Backing vocals
  are requested by describing where you want them.

  Section labels in Suno's style are not the documented mechanism here. Full
  syntax, timestamps and the multimodal inputs: **DATA_GOOGLE**.

─── GOOGLE FLOW MUSIC ───

  Sections are built and replaced in the interface rather than declared in
  text. See DATA_GOOGLE.

─── ELEVENMUSIC ───

  Descriptive prose; sections are edited and regenerated in the interface.
  No documented tag syntax. See DATA_OTHER.

─── STABLE AUDIO ───

  Primarily instrumental work. Describe the arrangement in prose. See DATA_OTHER.

─── THE PORTABLE PART ───

Three things in this file are craft rather than syntax, and they survive the
trip to any platform:

  1. A section should differ audibly from the one before it.
  2. Emotional direction attached to a specific passage beats a global mood.
  3. Enough words to fill the intended length, and not more.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§15. CHECKLIST
═══════════════════════════════════════════════════════════════════

<rag_zone id="lyrics_checklist">

  ☐ Nothing in round brackets that you would not want to hear sung
  ☐ Nothing in square brackets that is a measurement or a mix setting
  ☐ Every section labelled, each label on its own line above its text
  ☐ Blank line between sections
  ☐ Labels say how this section differs — not what the Style field already said
  ☐ Emotional direction on its own line, above the line it governs
  ☐ Capitals on one to three words per section, no more
  ☐ Ad-libs placed in the gaps, not on top of the lead vocal
  ☐ Duet: all three anchors present, whole sections per singer
  ☐ Chords inline in round brackets, or not specified at all
  ☐ No parametric anchor block at the top of the field
  ☐ Enough words for the intended length
  ☐ If composing on Suno web: checked what the editor did to the markup

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF CORE_02_LYRICS.md · SunoForge v3.0
// Next: CORE_03_DIAGNOSE.md
// ═══════════════════════════════════════════════════════════════
