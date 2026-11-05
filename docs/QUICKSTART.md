# Quick start — from nothing, in ten minutes

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

Anything with a long context window (200K tokens or more): **Claude**, **Gemini**,
**ChatGPT**, **Grok**, or **Antigravity** if you work in code.

The shortest path is the **ready-made Gem**, where everything is preloaded:
[SunoForge Gem](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing).
That lets you skip steps 2 and 3. The Gem is refreshed separately from the release.

## Step 2. Install it

Every host, step by step, is in [INSTALL.md](INSTALL.md). In short:

- **Claude** — the plugin or the Skill, `SunoForge_v5.0_Skills_for_Claude.zip`; or the
  thirteen files from the `claude/` folder of `SunoForge_v5.0_Prompt.zip` in a Project.
  Details in [CLAUDE.md](CLAUDE.md).
- **Gemini** — the Skill, `SunoForge_v5.0_Skills_for_Gemini.zip`, on the Skills page.
  Details in [GEMINI.md](GEMINI.md).
- **ChatGPT, Antigravity** — their plugins, `SunoForge_v5.0_plugin_chatgpt.zip` and
  `SunoForge_v5.0_plugin_antigravity.zip` ([INSTALL.md](INSTALL.md)).
- **Grok** — the files from the `gemini/` folder of the prompt archive in a project.
- **If you cannot attach files** — paste the contents as the first message,
  starting with `CORE_00_ENTRY.md`, which is the entry point.

## Step 3. Language

Nothing to set: SunoForge answers, menu included, in the language you write in. To
pin one language, type `/set lang en` or `/set lang ru`; `/set lang auto` goes back.

The prompts themselves stay English regardless — the generators understand it
best.

## Step 4. Type "start"

```
start
```

A fifteen-entry menu appears. You do not need to read all of it.

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

## Two new entries: [14] and [15]

**`[14] SPEECH` — a voice-over with its own music.** Suno Speech (beta) makes a
spoken piece and its soundtrack in one take: a bedtime story over soft piano, an
intro for a podcast, a toast. Ask for it in plain words — "read this text over quiet
piano" — and you get a **Speech Blueprint** with two blocks:

- **Script** — the exact words, written for the ear; paste into the Script field
  (Advanced mode)
- **Tone** — who speaks and how, and the music beneath; paste into the Tone field

Which languages Speech supports is not published — try a short take first.

**`[15] LIVE` — send to a generator from the chat.** If your assistant shows a
music-generation MCP server — Suno's own (beta), ElevenLabs' hosted MCP or your own —
SunoForge can send the prompt for you. It always asks first: a card shows what will be
sent and that it spends your credits, and nothing happens until you say yes. The song
lands where that service keeps it — on Suno, in your library.

- `send` — send the last prompt (it still asks first)
- `mcp-info` — connections: which generation servers your assistant sees, which are off
  and how to enable them; it connects nothing itself

Without a server nothing changes: you copy the prompt as before. Setting up Suno's:
[SUNO_MCP.md](SUNO_MCP.md). Suno lets accounts into this beta through an early-access
form on suno.com/mcp.

**The first run.** After the menu SunoForge asks one question, once: which generators you
use. The menu always shows every entry. `config` asks again and also sets the view and
prices on the card. `save` keeps a Style or a persona you liked; `library` lists them and
`library <name>` puts one into the next prompt.

**Building.** `[2]` Studio, `[5b]` custom persona, `[9]` recipes and `[14]` Speech open
a form — a widget on the desktop app, multiple-choice questions elsewhere, a numbered
text otherwise: one choice per field, **Build** sends them, the result is a blueprint.
Any result can be kept with `save`.

Commands are words without a slash: `send`, `mcp-info`, `config`, `menu`; with the Claude
plugin `/sunoforge` opens the menu. The line at the foot of every answer switches the view:
M menu (widgets), T text, B buttons (the terminal).

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
| An old prompt behaves oddly | Type `audit` and paste the prompt |
| "Not yet available for your account" when connecting Suno | Suno has not admitted your account to the MCP beta yet — the form is on suno.com/mcp |
| A menu entry is missing | The menu is always whole since 5.0: update the plugin or the files |

The full version is `CORE_03_DIAGNOSE.md`, which is also menu entry `[12]`.

---

## Where to go next

- `/why <topic>` — why a rule is shaped that way
- `/free` — what you can do without paying
- `/compare` — which platform fits the task
- `/legal` — whether you can publish and monetise this

One thing worth knowing **before** you publish anything: free plans generally do
**not** grant commercial rights, and each platform settles it its own way. On Suno a
song made without a subscription can become commercial later — by downloading it
with a paid download credit. On ElevenMusic the Free plan allows no downloads at all.
If a track might ever be used for work, check `/legal` first.
