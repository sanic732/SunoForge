# Running in Gemini

> **Note on packages.** Release 5.0.0 ships the Claude plugin only
> (`sunoforge.plugin`). The Skill packages, `Prompt.zip` and the ChatGPT, Antigravity and Grok
> plugins for 5.0 are built separately and are still to come. Where this page names a `v4.0` file,
> that is the working package you can download today, from the
> [4.0 release](https://github.com/sanic732/SunoForge/releases/tag/v4.0).

A ready-made Gem, everything loaded:
[SunoForge Gem](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing)
Refreshed separately from the release

---

## Gemini Edition — the `gemini/` folder

Gemini gets its own edition: plain Markdown with no XML tags at all. XML in the system
context works worse on Gemini, so the structure rides on headings. The content is the
same as in the `claude/` folder.

**A Skill — the shortest way.** Gemini now has skills, and Google is turning Gems into
them — from 17 November 2026, by the notice in the app. The SunoForge Skill is
`SKILL.md` plus the thirteen files, which Gemini opens as it needs them instead of
holding them all at once.

1. Unpack `SunoForge_v4.0_Skills_for_Gemini.zip`. Inside is a folder `sunoforge` holding
   `SKILL.md` and the thirteen files.
2. The **Skills** page → **Upload** → choose the whole `sunoforge` folder. The folder
   name must match the skill name, `sunoforge`; Gemini refuses any other.
3. Review it and click **Create**.

The upload window takes files and folders in CSV, PY, TXT and MD — a whole archive may
not pass there, hence unpacking first.

Gemini applies a skill that is turned on by itself when you ask for a music prompt; to
call it directly, type `/` and pick `sunoforge`. That is why SunoForge commands are
safer without the slash in Gemini: `set lang ru`, `menu`, `send`, `connect`. Google's
help lists skills in the web app, the mobile app and on Mac, for personal Google
Accounts, 18 and over.

Google warns that most tools available in Gems do not work with skills, Create music
among them. If a chat with the skill cannot generate, paste the finished Lyria prompt
into a regular Gemini chat. The automatic move from Gems carries only supported files,
and an archive is not one of them — a Gem that keeps `DATA.zip` in its knowledge is
likely to lose it, so upload the skill from the release rather than waiting for the
move.

**Loading it without the Skill.** Gemini takes up to 10 attachments per message, and an
archive can hold up to 10 files. So the core goes as files and the data as one archive:

```
from the gemini/ folder — into the chat or the Gem's knowledge:
  CORE_00_ENTRY.md      ← entry point, required
  CORE_01_STYLE.md
  CORE_02_LYRICS.md
  CORE_03_DIAGNOSE.md
  CORE_04_WHY.md
  DATA.zip              ← the seven DATA_* files inside
```

Then type `start`.

**Why this way.** The core is read constantly: `CORE_00_ENTRY` holds the settings, the
menu and the routing. The data layer is read selectively, per platform and task, so an
archive is enough. Updating the data means replacing one `DATA.zip`.

**Your own Gem.** The same six attachments go into the Gem's knowledge. One line of Gem
instructions is enough: "Read CORE_00_ENTRY.md first and follow it".

### Suno from Gemini (optional, beta)

Suno's official MCP server connects to Gemini as a connector: **Gemini** →
**Customize** → **Connectors** → **+** → the URL `https://api.suno.com/mcp` →
**Create**, then sign in to Suno. In the chat, mention **@Suno**. Sign-in is your Suno
account, no API key; every generation spends your Suno credits. Suno admits accounts to
the beta through the early-access form on suno.com/mcp; "Connecting AI apps to Suno is
not yet available for your account" means the account is not admitted yet.

Not confirmed yet: which Gemini plans allow custom connectors, and whether the Suno
connector and the SunoForge skill work in the same chat. With Suno connected,
SunoForge offers to send and waits for your yes; without it, you copy the prompt into
Suno as before. Details: [SUNO_MCP.md](SUNO_MCP.md).

**ChatGPT, Grok, Antigravity.** They now have their own packages with the same Markdown
edition — [INSTALL.md](INSTALL.md).
