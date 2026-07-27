# Quick start — from nothing, in ten minutes

`[EN]` this file · `[RU]` [БЫСТРЫЙ_СТАРТ.md](БЫСТРЫЙ_СТАРТ.md)

For people who have never used a music generator. If you have,
[ADVANCED.md](ADVANCED.md) is the one you want.

---

## What this actually is

SunoForge is not an application. It is a body of text you hand to a chat
assistant, after which it works as a music producer: you describe an idea in
plain words, it returns a finished prompt to paste into Suno or another
generator.

Why the middle layer? Because music generators respond less to *what* you say
than to *how* you say it. "A sad song with a guitar" and "late-1960s Laurel
Canyon folk, bittersweet and unhurried, fingerpicked nylon-string guitar, a
female alto with no polish on it" produce different records. SunoForge writes
the second one for you.

---

## Step 1. Pick an assistant

Anything with a long context window: **Claude**, **Gemini**, **ChatGPT**,
**Grok**.

The shortest path is the **ready-made Gem**, where everything is preloaded:
[SunoForge v3.0](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing).
That lets you skip steps 2 and 3.

## Step 2. Load the files

All twelve `.md` files from the `files/` folder.

- **Claude, ChatGPT** — attach them to the chat or add them to a project.
- **Gemini** — attach the five `CORE_*` files individually, and put the seven
  `DATA_*` files into a single `.zip` and attach that. This combination is
  tested and works. Details in [GEMINI.md](GEMINI.md).
- **If you cannot attach files** — paste the contents as the first message,
  starting with `CORE_00_ENTRY.md`, which is the entry point.

## Step 3. Set your language

Open `files/CORE_00_ENTRY.md`, find the settings block at the top, and set the
language of explanations:

```
OUTPUT_LANG      = "en"       // en | ru
```

The prompts themselves stay English regardless — the generators understand it
best.

## Step 4. Type "start"

```
start
```

A twelve-entry menu appears. You do not need to read all of it.

## Step 5. Just describe what you want

Naming a menu number is optional.

```
A calm song about leaving home. Female voice, guitar.
```

You get two or three variants back, each with two blocks:

- **Style** — paste into the "Style of Music" field
- **Lyrics** — paste into the lyrics field

Copy, paste, generate.

---

## Reading the output

You will see marks in the answers:

- `[OFFICIAL]` — stated in the platform's own documentation. Trust it.
- `[COMMUNITY]` — independent testing and guides. Usually right, not guaranteed.
- `[UNVERIFIED]` — widely repeated, no primary source. May do nothing at all.

This is not decoration. In previous versions of this system several "rules"
turned out to be inventions that everyone had been copying from each other. Now
you can see which is which.

If they make output harder to read: `/confidence off`.

---

## Five things that immediately improve results

**1. Don't name a genre — name an era and a place.**
"Rock" is a category holding decades of records that sound nothing alike.
"Mid-90s Seattle grunge" is a specific record with a specific sound.

**2. Always state the singer's gender.**
Without it the voice changes between takes, and you cannot tell what your edit
actually did.

**3. Don't write "no".**
"No male vocals" works badly and sometimes produces the opposite: to exclude a
concept the model has to represent it first. Write what you want instead:
"female voice, breathy, close-miked".

**4. Change one thing at a time.**
Change five and you will not know which one worked. That is how superstitions
get made.

**5. Generate several times.**
Every label is a hint, not a command. Some will not land. That is normal — take
three shots and pick.

---

## When something goes wrong

| Symptom | What to do |
|---|---|
| Boring, characterless | Add an era and place; replace "guitar" with how it sounds |
| Wrong vocal gender | Remove every negative, state the voice you want directly |
| Muddy pile of instruments | Keep two or three; the genre implies the rest |
| It sings my instructions | You wrote them in round brackets. Round brackets are sung |
| Structure is wrong | Labels are hints. Regenerate |
| An old prompt behaves oddly | Run `/audit` and paste the prompt |

The full version is `CORE_03_DIAGNOSE.md`, which is also menu entry `[12]`.

---

## Where to go next

- `/why <topic>` — why a rule is shaped that way
- `/free` — what you can do without paying
- `/compare` — which platform fits the task
- `/legal` — whether you can publish and monetise this

One thing worth knowing **before** you publish anything: free tiers generally do
**not** grant commercial rights, and upgrading later does not retroactively
license tracks you already made. If a track might ever be used for work,
generate it on a paid plan from the start.
