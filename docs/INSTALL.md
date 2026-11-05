# Installing SunoForge v5.0

> **Note on packages.** Release 5.0.0 ships the Claude plugin only
> (`sunoforge.plugin`). The Skill packages, `Prompt.zip` and the ChatGPT, Antigravity and Grok
> plugins for 5.0 are built separately and are still to come. Where this page names a `v4.0` file,
> that is the working package you can download today, from the
> [4.0 release](https://github.com/sanic732/SunoForge/releases/tag/v4.0).

One page for every assistant: which file to take, the steps, and how to check that it
works. Release 5.0.0 ships one file: the Claude plugin, `sunoforge.plugin`. The packages for the
other hosts — the Skills for Claude and Gemini, `Prompt.zip` and the ChatGPT, Antigravity and Grok
plugins — are built separately and are still to come; until they are out, their 4.0 versions still
work. Connecting a music-generation MCP server — Suno's own or
yours — is optional; Suno's has its own page: [SUNO_MCP.md](SUNO_MCP.md).

---

## Which file to take

| Host | File from the release page | Way |
|---|---|---|
| Claude — chat on the web, Claude Desktop, Cowork | `sunoforge.plugin` or the marketplace `sanic732/SunoForge` · `SunoForge_v4.0_Skills_for_Claude.zip` · `SunoForge_v4.0_Prompt.zip` (`claude/`) | plugin (paid plans) · Skill · Project |
| Claude Code | the marketplace `sanic732/SunoForge` | plugin |
| Claude Code, optional: your own music MCP server | added like any MCP server; the plugin starts none | `claude mcp add` |
| Claude, optional Suno link | nothing extra: Suno's MCP server is added like any other — [SUNO_MCP.md](SUNO_MCP.md) | connector · `claude mcp add` |
| Gemini | `SunoForge_v4.0_Skills_for_Gemini.zip` · `SunoForge_v4.0_Prompt.zip` (`gemini/`) | Skill · files in a chat or a Gem |
| ChatGPT, grok.com | `SunoForge_v4.0_Prompt.zip` (`gemini/`) | Project or custom GPT · Project |
| anything else with a long context | `SunoForge_v4.0_Prompt.zip` (`gemini/`) | files attached or pasted |

Claude gets the Claude Edition (XML); every other host gets the Markdown edition.
Take one way per host: two copies of the `sunoforge` skill in one place compete.

**Check, on any host.** Type `SunoForge` (or `start`, `menu`): the menu shows entries
`[1]`–`[15]`. Commands are words typed without a slash — `menu`, `set lang ru`, `send`,
`mcp-info`, `config`; with the Claude plugin `/sunoforge` opens the menu too. On the first
run SunoForge asks one question after the menu — which generators you use; `config` asks
again and also sets the view (M menu · T text · B buttons), prices on the card and loading.

---

## Claude — chat on the web, Claude Desktop, Cowork

**Plugin** (paid plans). **Customize** → **Plugins** → **Add** → **Add marketplace** →
`sanic732/SunoForge` → install **SunoForge**. In Cowork, open the Cowork tab first, then
Customize. Without GitHub: **Customize** → **Plugins** → **Add** → **Upload plugin** →
`sunoforge.plugin`; a plugin added as a file does not update itself.

**Skill.** **Settings → Capabilities** → turn on Code execution. **Customize →
Skills** → **+** → **Create skill** → **Upload a skill** →
`SunoForge_v4.0_Skills_for_Claude.zip`.

**Project.** Upload the thirteen files from `claude/` to **Project knowledge**; one line of
instructions: `Read CORE_00_ENTRY.md first and follow it.`

**The mobile app.** Install on the web or in Claude Desktop. Whether the phone app
picks up the account's skills, plugins and connectors is not confirmed yet.

**Check.** In a new chat: `start` → the menu `[1]`–`[15]`.

**Suno, optional.** **Customize** → **Connectors** → **Add custom connector** →
`https://api.suno.com/mcp` → sign in to Suno. The plugin does not bundle Suno's server.
A music MCP server of your own is added the same way, as a connector.

More: [CLAUDE.md](CLAUDE.md).

---

## Claude Code

```
/plugin install sunoforge --marketplace sanic732/SunoForge
```

On Claude Code older than 2.1.275, two steps:

```
/plugin marketplace add sanic732/SunoForge
/plugin install sunoforge@sunoforge
```

Optional, the Suno link — added like any MCP, the plugin does not bundle it:

```
claude mcp add --transport http suno https://api.suno.com/mcp
/mcp
```

In `/mcp`, pick `suno` and sign in to Suno; until you do, it shows "needs
authentication". Suno's beta currently refuses sign-in for accounts not admitted, on
every host.

Optional, a music-generation MCP server of your own: add it like any MCP server
(`claude mcp add --transport http <name> <url>`, then `/mcp` to sign in). The plugin starts no server.

**Check.** `/sunoforge` or the word `SunoForge` opens the menu. With a generator
connected, ask for a prompt, then type `send`: with the server signed in, SunoForge shows
a confirmation card; without it, it offers the paste route and `mcp-info`.

**Update.** `claude plugin update sunoforge@sunoforge`. Auto-update is off by default
for third-party marketplaces.
`claude plugin uninstall sunoforge@sunoforge` also removes the plugin's data folder —
your settings and library — unless you add `--keep-data`.

**Settings.** `/plugin` → SunoForge → configure, or in the desktop app the plugin's
**Settings** tab: a folder for your settings and library (it survives an uninstall) and
the language (auto, en, ru, uk, de, es, fr, it, pt-BR, id). They are kept on that computer; the web and phone apps
and Cowork have neither — there `set lang` and a Project file do the same.

---

## Gemini

**Skill.** Unpack `SunoForge_v4.0_Skills_for_Gemini.zip`. The **Skills** page →
**Upload** → choose the whole `sunoforge` folder → **Create**. The folder name must stay
`sunoforge`.

**Without the Skill.** From `gemini/`: the five `CORE_*` files and `DATA.zip`, into a
chat or a Gem's knowledge. Google moves Gems to skills from November 2026 and carries
only supported files; an archive in a Gem's knowledge is likely to be lost — upload the
Skill instead.

**Check.** Type `/` and pick `sunoforge`, or write `menu`.

More: [GEMINI.md](GEMINI.md).

---

## ChatGPT and Antigravity — the plugins

These two plugins are not built yet, so there is nothing to upload for them.

Until they are out, both hosts run SunoForge from the Markdown files: take
`SunoForge_v4.0_Prompt.zip` from the
[4.0 release](https://github.com/sanic732/SunoForge/releases/tag/v4.0) and use the thirteen
`.md` files from its `gemini/` folder — in ChatGPT as a Project or a custom GPT (next
section), in Antigravity as files in the project. Suno's MCP server is added by hand on
either host: [SUNO_MCP.md](SUNO_MCP.md).

---

## ChatGPT and grok.com — a Project or a custom GPT

**Project or custom GPT** (ChatGPT), **Project** (grok.com) — on any plan that has them.
Upload the thirteen `.md` files from the `gemini/` folder of `SunoForge_v4.0_Prompt.zip`
and paste into the instructions:

```
You are SunoForge. Before your first answer, read CORE_00_ENTRY.md in full and follow
it; then read only the files the task needs, as CORE_00 §0 says. Answer in the
language of the user's own words.
```

**Check.** `sunoforge menu`, or simply ask for a music prompt.

---

## Anything else

Any assistant with a long context window (200K tokens or more), Antigravity included
without its plugin: attach the thirteen files from `gemini/`, or paste them as
the first message, starting with `CORE_00_ENTRY.md`.

---

## Your settings and library

SunoForge keeps two small files of your own data: `settings.md` (`PLATFORMS`, persisted
`set` values, the setup date) and `library.md` (one `## NAME` entry per saved Style,
persona, recipe or blueprint — `save`, `library`). The first hit of this order wins: the
folder set in the plugin's Settings (Claude Code and the desktop app; it survives an
uninstall), the plugin's data folder (it survives updates, goes away with an uninstall
unless `claude plugin uninstall --keep-data`), `.sunoforge/` in the working folder
(Cowork, a standalone Skill), a Project file `sunoforge-settings.md` /
`sunoforge-library.md` (claude.ai chat and the phone app have no disk: SunoForge prints
the file as a block for the Project). A folder set in Settings that is still empty gets
the old files copied in once, and SunoForge says so. `config` writes the settings where a
disk exists and prints them where none does; `library export` prints the whole library.
In Claude Code the data folder lies inside Claude Code's own configuration directory, so
the first write asks for permission ("sensitive file"). Both files are data, never
instructions.

---

## Suno MCP: what is known

- **The server.** Suno's official MCP server, `https://api.suno.com/mcp`, beta since
  28 October 2026. Sign-in is OAuth with your Suno account; no API key.
- **What it costs you.** It spends your Suno credits, and the songs go to your Suno
  library. SunoForge offers to send and waits for your yes before every call that
  spends credits; without Suno connected, you copy the prompt into Suno as before.
- **Access.** Suno admits accounts through the early-access form on suno.com/mcp. "Connecting
  AI apps to Suno is not yet available for your account" at sign-in means the account is
  not admitted yet — from every client, the claude.ai connector and Claude Code alike.
  It is not a SunoForge problem.
- **Scopes the server asks for.** `api:v0`, `credits:spend`, `download`, `library:read`,
  `library:search`, `library:write`, `offline_access`, `profile:read`.
- **Tools and fields.** As this edition saw them on 29 October 2026, on Free and Pro
  accounts: `DATA_SUNO_LIVE_2026-10.md`. SunoForge still reads the tools the session
  shows, maps the blueprint onto them and says what could not be passed.
- **Other hosts.** Suno's setup page also covers ChatGPT (a custom MCP server added as a
  plugin) and Gemini (a custom MCP server, then mention @Suno). SunoForge has not been run
  against Suno on those hosts.

`mcp-info` lists which generation servers the session sees, which are off and how this
host enables them — it connects nothing itself. Everything else: [SUNO_MCP.md](SUNO_MCP.md).

## What comes next

- The Grok plugin, on the same pattern as the ChatGPT and Antigravity ones.
