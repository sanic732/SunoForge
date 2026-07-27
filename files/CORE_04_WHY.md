---
file_id: CORE_04_WHY
version: "3.0"
layer: core
lazy: "/why"
scope: pedagogy · rule_rationale · consequences · architecture_rationale
key_concepts: [why_front_load, why_specific, why_time_and_place, why_gender, why_prose_parameters, why_brackets, why_positive, why_emotion_line, why_iterate_one, why_hints, why_platform_first, why_rights, why_confidence, why_core_data_split]
depends_on: [CORE_00_ENTRY, CORE_01_STYLE, CORE_02_LYRICS, CORE_03_DIAGNOSE]
used_by: [CORE_00_ENTRY]
rag_priority: medium
updated: "2026-07-27"
changelog: "v3.0 — pedagogical layer restored from Polymath in the advice/why/consequence format · covers all twelve critical rules plus the architectural decisions · explanations for withdrawn techniques replaced with explanations of why they were withdrawn"
---

# 🎓 SUNOFORGE v3.0 — WHY
# File 5 of 12 · CORE · Loaded only on request

> Reached with `/why <topic>` per CORE_00 §5. Not loaded by default.
>
> **This is the one file allowed to explain at length.** Every other file
> keeps its rules short and points here. That split is deliberate: a rule you
> are trying to apply wants to be one line, and a rule you are trying to
> understand wants a paragraph. Mixing the two makes both worse.
>
> Format throughout: **the advice** → **why it is better** → **what happens
> if you ignore it**. Nothing here is a new instruction. If this file and a
> rule file disagree, the rule file is right and this one has drifted.

═══════════════════════════════════════════════════════════════════
§1. THE TWELVE CRITICAL RULES
═══════════════════════════════════════════════════════════════════

Numbered as in CORE_00 §7.

<rag_zone id="why_front_load">

─── 1 · FRONT-LOAD ───

**ADVICE.** Put the genre, mood and key instruments in the opening words of
the Style description. Production detail goes at the end.

**WHY IT IS BETTER.** These models read a prompt as a sequence and commit to
an interpretation early. Whatever arrives first shapes how everything after
it is read — the same words in a different order produce a different track.
Naming a specific subgenre first is like handing a session musician a
reference record before the chart: everything they play afterward is
informed by it. Naming it last is handing them the reference after the take.

This is the most consistently reproduced finding across independent guides,
and the one thing every source agrees on even when they disagree about
everything else [COMMUNITY].

**IF YOU IGNORE IT.** A prompt that opens "a song with a sort of melancholy
feeling that uses guitars and maybe some strings, in a rock style" gets read
as a generic sad song, and "rock" arrives too late to change that. You get a
result that contains everything you asked for and sounds like nothing in
particular — the most common complaint about generated music, and usually a
word-order problem rather than a model problem.

</rag_zone>

<rag_zone id="why_specific">

─── 2 · BE SPECIFIC, NOT LONG ───

**ADVICE.** Five to eight strong descriptors beat a wall of adjectives. Add a
word only if it changes the sound you are imagining.

**WHY IT IS BETTER.** Descriptors compete. Each one pulls the result toward
some region, and past a certain count they start pulling in incompatible
directions. The model resolves the conflict by averaging, and the average of
many specific things is a generic thing. Five words that agree produce a
sharper result than fifteen that argue.

**IF YOU IGNORE IT.** Two failure modes, in opposite directions. Too few
descriptors — "sad rock" — and the model fills the gaps with the most
statistically ordinary version of that. Too many, and it averages your
conflicting requests into the same ordinary version. Both roads lead to
generic; specificity is the only exit.

**A NOTE ON LENGTH LIMITS.** Earlier versions of this system taught a hard
character ceiling as fact. It was one person's estimate, repeated until it
looked authoritative, and it made people cut prompts to a fraction of the
range that actually works. What is genuinely known about field length is in
DATA_SUNO §2, marked by confidence, including the parts where sources
disagree. This is the single clearest example of why the confidence marking
in §3 exists.

</rag_zone>

<rag_zone id="why_time_and_place">

─── 3 · TIME AND PLACE ───

**ADVICE.** Instead of a genre name, give an era, a place and a scene.
"1980s Sunset Strip glam metal" rather than "metal".

**WHY IT IS BETTER.** A genre name is a category containing decades of
recordings that share almost nothing sonically. "Metal" spans Black Sabbath
and modern djent — the model has to pick, and it picks the average.

An era plus a place is not a category, it is a *recording*: specific studios,
specific equipment, a specific production aesthetic, a specific cultural
posture. All of that is attached to the phrase and comes along with it, for
the same number of words. You are not adding constraints, you are replacing
a vague word with a precise one at no cost.

**IF YOU IGNORE IT.** You get the genre's centre of gravity — the most
average possible example. That is occasionally what you want, and almost
never what you meant.

**THE EXCEPTION.** Some subgenre names already carry their era: synthwave,
vaporwave, city pop, boom bap. Adding a decade to those restates what the
name already said. Recognising when a name is already specific is part of
the skill (CORE_01 §3).

</rag_zone>

<rag_zone id="why_gender">

─── 4 · VOCALS NEED A GENDER ───

**ADVICE.** State the singer's gender explicitly, in positive terms. On
platforms with a dedicated selector, use the selector.

**WHY IT IS BETTER.** Unspecified, this is decided by whatever the rest of
the prompt happens to suggest, and that varies between takes. You lose
reproducibility for no reason — and reproducibility is what lets you change
one thing and learn something from the result (rule 9).

The interface selector is more reliable than any wording because it is not a
suggestion in a text field competing with everything else there. It is a
setting.

**IF YOU IGNORE IT.** Two takes from the same prompt come back with
different singers, and you cannot tell whether the change you made mattered
or whether you just got a different voice. Everything downstream becomes
guesswork.

**WHY NEGATIVES MAKE IT WORSE.** See rule 7 — this is where that mechanism
bites hardest.

</rag_zone>

<rag_zone id="why_prose_parameters">

─── 5 · PARAMETERS AS PROSE ───

**ADVICE.** Write "120 BPM, C minor, heavily compressed" rather than
`[BPM: 120] [Key: C minor] [compression: heavy]`.

**WHY IT IS BETTER.** The bracketed form was never parsed as a control by
any covered platform [UNVERIFIED]. There is no parameter system reading
those keys and applying values. What actually happens is that the words
inside are read as text — which means the brackets and the colon are, at
best, doing nothing, and at worst introducing punctuation noise into a
description that was working.

The prose version says exactly the same thing in a form the model actually
processes.

**IF YOU IGNORE IT.** Usually nothing dramatic — which is precisely the
problem. Nothing errors. No warning appears. The prompt looks more technical
and controlled than a plain sentence, so it *feels* more effective, and the
result is very slightly worse in a way you would never attribute to the
syntax. This is a silent failure, and silent failures survive for years.

**WHY IT SPREAD.** It looks like an API. Anyone who has used software
expects `parameter: value` to mean something, and a guide showing that
syntax looks more expert than one showing a sentence. It propagated through
every previous edition of this system for exactly that reason.

**THE ONE PLACE BRACKETS DO WORK.** Structural section labels in the Lyrics
field, and timestamps on Lyria. Both are documented; both mark *where*
something happens rather than *setting* a value. That distinction is the
whole rule (CORE_02 §1).

</rag_zone>

<rag_zone id="why_brackets">

─── 6 · ROUND BRACKETS ARE SUNG, SQUARE ONES ARE NOT ───

**ADVICE.** Anything in round brackets is performed. Anything in square
brackets is direction.

**WHY IT IS BETTER.** It is not a convention you could reason your way to —
it is how the field is interpreted, and it is unusually consistent
[COMMUNITY]. Round brackets are how you get backing vocals and answering
phrases, which is genuinely useful. Square brackets are how you get
structure without it being sung.

**IF YOU IGNORE IT.** You hear your own stage directions. A prompt
containing "(play the guitar softly here)" produces a backing vocalist
singing the words "play the guitar softly here". It is the most immediately
audible mistake in this whole system, and the easiest to avoid: if you would
not want to hear it, do not put it in round brackets.

</rag_zone>

<rag_zone id="why_positive">

─── 7 · NEGATIVES ARE WEAK ───

**ADVICE.** State what you want. Where a platform has a dedicated exclude
field, use that rather than writing negatives into the description.

**WHY IT IS BETTER.** To exclude a concept, a model has to represent it
first. "No male vocals" contains the phrase "male vocals" in a description
that is being read as a whole, and the exclusion is a weak modifier attached
to a strong noun. Sometimes the modifier survives. Sometimes only the noun
does.

A positive statement has no such failure mode: "solo female vocalist,
breathy soprano" contains nothing you do not want.

A dedicated exclude field is different in kind — it is a separate input
processed as exclusions, not a phrase competing inside a description. That is
why the advice differs by field rather than being one blanket rule.

**IF YOU IGNORE IT.** At best the negative is ignored. At worst you summon
the thing you were excluding, and it feels like the tool is mocking you. The
gender case is the most reported instance, and the most frustrating, because
the harder you push the more you reinforce it.

**THE SAME MECHANISM, ELSEWHERE.** This is also why words describing audio
defects appear to cause them (CORE_03 §4). "No clipping" and "no male
vocals" fail for the same reason. Once you see the pattern, both rules
collapse into one: describe the destination, not the ditch.

**AND ON LYRIA.** Negative prompting is not supported at all [OFFICIAL]. Not
weak — absent. An exclude list there is not a poor tool, it is no tool.

</rag_zone>

<rag_zone id="why_emotion_line">

─── 8 · EMOTION ON ITS OWN LINE ───

**ADVICE.** Put delivery direction on a line of its own, immediately above
the lines it governs.

**WHY IT IS BETTER.** Scope. A direction folded into a section label among
five other modifiers is one of six things competing for that section's
interpretation. On its own line directly above a lyric, its scope is
unambiguous: these words, sung this way.

It also survives editing. Move the lines and the direction moves with them;
bury it in a label and it stays behind.

**IF YOU IGNORE IT.** The emotional direction gets averaged into the general
character of the section, which is exactly the granularity you were trying
to escape. You asked for one broken line and got a mildly sad verse.

**WHY IT MATTERS MORE THAN IT SOUNDS.** Persona sets who is singing across
the whole track. Delivery sets how they sing this passage. Without the
second, every section is performed at the same emotional level, and a song
performed at one level is the definition of flat — the single most common
reason generated vocals sound synthetic even when the timbre is convincing.

</rag_zone>

<rag_zone id="why_iterate_one">

─── 9 · ITERATE ONE THING ───

**ADVICE.** Change a single element between generations.

**WHY IT IS BETTER.** These models are stochastic: two generations from an
identical prompt differ. That variance is the reason this rule exists. If you
change five things and the result improves, you cannot tell which change
helped, whether any did, or whether you simply got a better roll. You have
spent a generation and learned nothing.

Change one thing and the difference is attributable — with the caveat that
one comparison is still one sample. Two or three takes per side is where you
start believing a result.

**IF YOU IGNORE IT.** You develop a personal folklore. Techniques that
happened to coincide with good takes become rules you follow forever. This
is not hypothetical — it is exactly how the folklore this version had to
remove came into existence. Someone changed several things, got a good
result, and attributed it to the most memorable one.

**THE UNCOMFORTABLE COROLLARY.** Most of what circulates as prompting wisdom
for music models, including everything this system carried for two versions,
was produced by people not following this rule. That is why confidence
marking exists (§3).

</rag_zone>

<rag_zone id="why_hints">

─── 10 · TAGS ARE HINTS ───

**ADVICE.** Treat every label and descriptor as a probabilistic nudge.
Generate several takes and choose.

**WHY IT IS BETTER.** It is accurate, and accuracy here changes behaviour.
A user who believes labels are commands responds to a missed structure by
adding more labels, stacking more modifiers, and writing increasingly
elaborate prompts — none of which addresses variance. A user who knows they
are hints simply generates again.

**IF YOU IGNORE IT.** Escalation. Prompts get longer and more baroque in
pursuit of determinism that is not available. The elaborate syntaxes this
version removed were largely built by people trying to force compliance from
a system that does not offer it.

**WHAT TO DO INSTEAD.** Accept the hit rate and take more shots. Three takes
and a choice beats one take and an argument. This is also why the system
offers two or three interpretations rather than one answer (CORE_00 §3) —
the variance is not a defect to be engineered away, it is the medium.

</rag_zone>

<rag_zone id="why_platform_first">

─── 11 · PLATFORM BEFORE PROMPT ───

**ADVICE.** Decide where the track will be made before writing anything.

**WHY IT IS BETTER.** The platforms differ in ways no prompt can compensate
for: maximum length, whether you can edit afterward, what rights attach to
the output, whether tempo is written as a number or described, whether
negatives work at all. Writing first and choosing second means rewriting.

Some of these are not preferences but hard walls. A prompt for a six-minute
piece aimed at a platform that cannot produce one does not produce a
shortened version of your idea — it produces a different, worse idea.

**IF YOU IGNORE IT.** The expensive version of this mistake is discovering
after the work is done that the output cannot be used commercially, or
cannot be exported at all. That is not hypothetical either — one platform in
this field disabled downloads entirely, stranding everything its users had
made (DATA_LEGAL).

**THE HABIT TO BUILD.** Ask what the track is *for* before asking what it
sounds like. "For me" and "for a client" lead to different platforms before
they lead to different music.

</rag_zone>

<rag_zone id="why_rights">

─── 12 · RIGHTS ARE NOT OWNERSHIP ───

**ADVICE.** "Commercial rights granted by a platform" and "copyright in your
name" are different things. Do not treat one as the other.

**WHY IT IS BETTER.** A platform granting commercial rights is telling you
what it will not sue you for. That is a contract between you and them, it
can change with the terms, and it says nothing about whether you hold
copyright, whether a third party might claim something, or what happens if
the platform loses a case.

Copyright is a separate question with a different answer in different
jurisdictions, and for purely generated output the answer is frequently that
nobody holds it.

**IF YOU IGNORE IT.** You may find you cannot stop someone else using your
track, cannot register it, or cannot deliver the warranties a commercial
client asks for — despite having done nothing wrong and having paid for a
plan that said "commercial use". Full picture: DATA_LEGAL.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. TECHNIQUES
═══════════════════════════════════════════════════════════════════

<rag_zone id="why_techniques">

─── WHY A BIOGRAPHY BEATS A DESCRIPTION ───

**ADVICE.** Describe the singer as a person with a history, not as a setting.

**WHY.** "Sad female vocal" is three coordinates in a space. "A singer who
learned in church and has spent fifteen years in half-empty rooms" is a
person, and a person implies a hundred correlated details — where they
breathe, what they do with the end of a line, how hard they push, what they
leave out. Those details are correlated in the training data because they
are correlated in real singers. One coherent description activates all of
them together; three adjectives activate none of them.

**IF YOU IGNORE IT.** Technically correct, characterless vocals. The right
gender, the right mood, and no one home.

**HONESTLY.** This is [COMMUNITY]. It is reported everywhere and measured
nowhere, and results still vary between takes. It reliably produces a better
*prompt*, which is a smaller claim than the one usually made for it.

─── WHY TWO OR THREE HERO INSTRUMENTS ───

**ADVICE.** Name the two or three instruments that define the sound, with a
playing-style word each. Let the genre imply the rest.

**WHY.** Naming seven instruments makes seven equal claims, and equal claims
produce an even, undifferentiated arrangement. Naming two makes a hierarchy,
and hierarchy is what makes an arrangement sound arranged rather than
assembled. The genre already implies a rhythm section — spending words on it
buys nothing.

**IF YOU IGNORE IT.** A full, competent, characterless arrangement where
everything is present and nothing leads.

─── WHY A BRIDGE GENRE ───

**ADVICE.** To combine two distant genres, find the third that touches both,
and say how they connect.

**WHY.** "Phonk, jazz, lo-fi" is a list with no stated relationship, so
there is nothing to render but the strongest signal. A sentence saying which
genre provides the rhythm, which provides the harmony, and what aesthetic
holds them together describes a piece of music rather than naming three.

**IF YOU IGNORE IT.** One genre wins and the others become a faint colouring
— the usual outcome of stacked genre names, and the reason people conclude
that hybrids do not work.

**HONESTLY.** [UNVERIFIED] as a mechanism. Nobody has tested bridge-genre
theory quantitatively. It is offered because it forces you to think about
how the genres relate, and that thinking produces a better prompt regardless
of whether the bridge itself does anything.

─── WHY SCENE PAINTING ───

**ADVICE.** Describe a situation rather than a list of qualities.

**WHY.** A situation implies tempo, dynamics, register and space
simultaneously and consistently. "Someone playing alone on a wet rooftop at
three in the morning" constrains all of those at once, and constrains them in
ways that agree with each other, because they came from one coherent image.
A list of adjectives constrains each independently and lets them contradict.

**IF YOU IGNORE IT.** Nothing terrible — adjective lists work. Scenes just
work better, and Lyria's own documentation leans on scenario prompting,
which is the closest thing to vendor endorsement any technique in this system
has.

─── WHY THE DUET NEEDS THREE ANCHORS ───

**ADVICE.** State the cast in the Style field, at the top of the lyrics, and
on every section.

**WHY.** Each anchor covers a different failure. The Style anchor establishes
that two voices exist at all. The header anchor keeps them distinct as the
track proceeds. The per-section anchor says who sings *this*. Remove any one
and a different thing goes wrong: without the first you get one singer
double-tracked; without the third you get two voices distributed arbitrarily.

**IF YOU IGNORE IT.** The voices converge. Partway through, both parts are
being sung by the same indistinct singer, and no amount of labelling after
that point separates them again.

**WHY WHOLE SECTIONS.** Line-by-line trading asks the model to switch voice
identity every few seconds, and identity is exactly what it holds least
firmly. Whole sections give each voice long enough to establish itself.

─── WHY THE TWO PATHS FOR LYRICS ───

**ADVICE.** On Suno's web editor, supply clean lyrics and let it label
sections. Everywhere else, mark them up yourself.

**WHY.** The editor now places structural labels itself [OFFICIAL]. Marking
up by hand on top of that produces two overlapping structures. But the API,
mobile, and every other platform have no such editor, so the manual path
cannot be retired.

**IF YOU IGNORE IT.** In one direction, redundant work and occasionally
conflicting markup. In the other, unstructured lyrics on a surface that
expected them marked.

**THE GENERAL LESSON.** This is what happens when a platform absorbs a
technique. The technique does not become wrong — it becomes conditional. A
prompt system that only knows one path will be wrong for half its users.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. THE ARCHITECTURE
═══════════════════════════════════════════════════════════════════

<rag_zone id="why_architecture">

Why this system is shaped the way it is. Read this if you are extending it,
translating it, or wondering why a fact you expected is in another file.

─── WHY CONFIDENCE MARKING ───

**THE DECISION.** Every claim about platform behaviour carries [OFFICIAL],
[COMMUNITY] or [UNVERIFIED].

**WHY.** Music generation has almost no primary sources. Vendors publish
release notes and almost no prompting documentation — for most of this field,
the only vendor-written prompting guide that exists is Google's, and it
appeared in April 2026. Everything else in circulation is somebody's
experience retold as fact, including two previous versions of this system.

Three independent research passes on the same questions, run within
twenty-four hours of each other, produced three different pictures. They
disagreed on whether a feature costs credits, on whether a syntax is
recommended or undocumented, and on whether a product still existed. Each was
stated confidently.

The choice is between pretending to a certainty the field does not have, and
showing the reader where the ground is solid. A guide that does not
distinguish these ages badly: when a [COMMUNITY] claim turns out wrong,
everything around it becomes suspect, including the parts that were right.

**IF THE SYSTEM DID NOT DO THIS.** It would be the previous version — which
taught a character limit that was a guess, a quality mode that does not
exist, and a degradation pattern nobody has measured, all in the same
declarative voice as the parts that were true.

─── WHY CORE AND DATA ARE SEPARATE FILES ───

**THE DECISION.** Rules live in undated CORE files. Facts live in dated DATA
files.

**WHY.** They decay at different rates, and the evidence is direct. Between
March and July 2026 the following broke: the default model version, a
maximum track length, the name of a whole product, an editing environment's
version and required plan, the mechanics of stem separation, the lyrics
editor, and two products that shut down entirely.

In the same period, not one prompting rule broke. Front-loading still works.
Time and Place still works. Round brackets are still sung.

Mixing the two means the whole document ages at the speed of its fastest-
decaying part. Separating them means a user with an old copy replaces one
file and keeps everything else.

**IF THE SYSTEM DID NOT DO THIS.** Every quarterly update would touch every
file, which means every quarterly update would risk breaking rules that were
fine — and in practice would not happen, so the whole thing would rot
together.

─── WHY VERSION FACTS LIVE IN EXACTLY ONE FILE ───

**THE DECISION.** Version numbers, limits, prices and plan tiers appear in
one file each. Everywhere else links.

**WHY.** Because the previous version did the opposite and silently
contradicted itself. A version matrix duplicated across three files diverged
when one copy was updated and two were not, and nothing detected it. There is
no error state for a document disagreeing with itself — it just quietly
misinforms, and the reader has no way to know which copy is current.

**THE COST.** Some files are less self-contained than they could be. A recipe
saying "genre-faithful slider posture, values in DATA_SUNO §7" is slightly
less convenient than one with the numbers inline. That is the trade, and it
is worth it: thirty inline copies would be thirty things to update and thirty
chances to miss one.

─── WHY MYTHS ARE DOCUMENTED RATHER THAN DELETED ───

**THE DECISION.** Debunked techniques are catalogued with what the evidence
actually shows.

**WHY.** Deleting them does not remove them from the world. They remain in
other guides, forum posts, video tutorials and every prompt written in the
last two years. Users will arrive with them. A system that has never heard of
MAX MODE cannot repair a prompt containing it, and cannot answer the question
"why did you take that out?"

Recognising and repairing requires knowing. That is the entire reason
CORE_03 §3 and DATA_SUNO §13 exist.

**THE TONE THAT FOLLOWS FROM IT.** If someone arrives using folklore, they
were taught it by a confident source — quite possibly this system. Explain
what changed. Do not imply they should have known better.

─── WHY THE MENU NUMBERS ARE FROZEN ───

**THE DECISION.** Entries [1]–[12] never change number. New entries go at the
end. A retired entry keeps its number.

**WHY.** They are a public interface. Forum posts, screenshots and
third-party guides reference them, and none of those get updated when a menu
is reorganised. Renumbering silently breaks every external reference, and the
breakage is invisible from inside the project — the menu looks fine, and
someone following a year-old guide lands somewhere unexpected.

**WHAT IT COSTS.** The menu is not in the tidiest order it could be. That is
the correct trade for a public interface.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. WHY THINGS WERE REMOVED
═══════════════════════════════════════════════════════════════════

<rag_zone id="why_removed">

Users of previous versions will notice absences. Each removal has a reason,
and the reason is always evidence rather than taste.

─── THE QUALITY MODE ───

Previous versions taught a set of tags said to unlock hidden quality. A
controlled comparison across multiple genres found no difference beyond
ordinary variation, and no vendor has ever documented such a mode. The origin
is traceable to a single forum post.

The tags are not harmful. They are read as ordinary quality adjectives, which
is a real if modest effect — but it is the same effect you get from writing
"studio-grade, detailed and dynamic" in plain words, and that version is
honest about what it is doing.

**WHY IT SURVIVED SO LONG.** It was in the menu, in the output protocol, in
every recipe and in the reference example. Removing it from one place would
have left it working in eleven others. Systems propagate their own errors
through internal consistency — a thing referenced everywhere looks
load-bearing.

─── THE DEGRADATION PATTERN ───

Previous versions treated it as established that tracks reliably lose
character after a fixed duration, and built an automatic mechanism on that
assumption — one that modified every prompt by default.

The evidence is anecdotal. No systematic testing, no vendor acknowledgment,
no mention in detailed independent reviews. Long generations do vary, and a
later section can come back weaker; that is ordinary variance and it does not
arrive on a schedule.

**WHY IT MATTERED THAT THIS WAS DEFAULT.** A mandatory mechanism built on an
unverified claim modifies every prompt a user writes, forever, on the basis
of something nobody checked. The techniques remain available for anyone who
finds them useful (CORE_03 §5). What is gone is the automatic application and
the false diagnosis.

─── A PLATFORM ───

One platform was dropped as a target. It still generates music, but downloads
were disabled following a settlement, which means output cannot be exported.
A tool you cannot get your work out of is not a tool.

It remains in the system as a case study, because what happened to its users
— work stranded, with a short window to retrieve it — is the most concrete
argument available for thinking about rights and export before you start
(DATA_LEGAL).

─── AN ELABORATE WORKAROUND ───

Previous versions carried a three-tier procedure for controlling vocal
gender: positive framing, then stacked negatives, then bracketed voice tags.

Two of those three tiers worked around a problem the interface now solves
with a selector, and the second tier actively made things worse for the
reason in rule 7. The whole procedure reduces to one line.

**THE PATTERN WORTH NOTICING.** Elaborate workarounds are evidence of a
missing feature. When the feature arrives, the workaround does not become
optional — it becomes wrong, because it is now competing with the real
control. Retiring workarounds is as important as adding techniques, and far
easier to forget.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. IF YOU ONLY REMEMBER FIVE THINGS
═══════════════════════════════════════════════════════════════════

<rag_zone id="why_summary">

  1. **Put the most specific thing first.** Order matters more than length,
     and the opening words decide what everything else modifies.

  2. **Say what you want, never what you don't.** Negatives are weak at best
     and self-defeating at worst, in every field and on every platform.

  3. **Change one thing at a time.** Otherwise you are collecting
     superstitions instead of knowledge — which is how this field acquired
     most of what it believes.

  4. **Nothing is a command.** Every label is a nudge. Take more shots
     instead of writing longer instructions.

  5. **Know what you can prove.** Most prompting advice for music models,
     including two previous versions of this system, was confident and
     partly wrong. Marking what is documented, what is reported, and what is
     merely repeated is not excessive caution — it is the honest description
     of a field with almost no primary sources.

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF CORE_04_WHY.md · SunoForge v3.0
// Next: DATA_LEGAL_2026-07.md
// ═══════════════════════════════════════════════════════════════
