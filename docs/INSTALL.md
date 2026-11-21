# Installing SunoForge v5.0

> **Note on packages.** Version 5.0.5 ships four: the Claude plugin (`sunoforge.plugin`), the Gemini skill
> (`SunoForge_v5.0.5_Skill_for_Gemini.zip`), the ChatGPT plugin (`SunoForge_v5.0.5_Plugin_for_ChatGPT.zip`) and the prompt
> with RAG markup, the file edition (`SunoForge_v5.0.5_Prompt_RAG.zip`: plain Markdown files for a Gemini notebook, NotebookLM,
> a Project or a chat that takes attachments). The Skill package for Claude and the Antigravity and Grok plugins are built separately and are
> still to come. Where this page names a `v4.0` file,
> that is the working package you can download today, from the
> [4.0 release](https://github.com/sanic732/SunoForge/releases/tag/v4.0).

One page for every assistant: which file to take, the steps, and how to check that it
works. Version 5.0.5 ships four: the Claude plugin, the Gemini skill, the ChatGPT plugin and the prompt with RAG markup (file edition). The
packages for the other hosts — the Skill for Claude and the Antigravity and Grok
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
| Gemini | `SunoForge_v5.0.5_Skill_for_Gemini.zip` · `SunoForge_v5.0.5_Prompt_RAG.zip` | skill · files in a chat or a notebook |
| ChatGPT | `SunoForge_v5.0.5_Plugin_for_ChatGPT.zip` · `SunoForge_v5.0.5_Prompt_RAG.zip` | plugin from an archive · Project or custom GPT |
| grok.com | `SunoForge_v5.0.5_Prompt_RAG.zip` | Project |
| A Gemini notebook, NotebookLM | `SunoForge_v5.0.5_Prompt_RAG.zip` — Prompt with RAG markup (file edition) | the files as the notebook's sources; tried in a Gemini notebook, not yet in NotebookLM |
| anything else with a long context | `SunoForge_v5.0.5_Prompt_RAG.zip` | files attached or pasted |

Claude gets the Claude Edition (XML); every other host gets the Markdown edition.
Take one way per host: two copies of the `sunoforge` skill in one place compete.

**Check, on any host.** Type `SunoForge` (or `start`, `menu`): the menu shows entries
`[1]`–`[16]`. Commands are words typed without a slash — `menu`, `set lang ru`, `send`,
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

**Check.** In a new chat: `start` → the menu `[1]`–`[16]`.

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

**Skill.** Unpack `SunoForge_v5.0.5_Skill_for_Gemini.zip`. The **Skills** page →
**Upload** → choose the whole `sunoforge` folder → **Create**. The folder name must stay
`sunoforge`. An older SunoForge skill is deleted first: they share the name.

**Suno.** Once: `gemini.google.com/customize/connectors` (**Customize → Connectors**) → **+** → `https://api.suno.com/mcp` →
**Create**, then **Connect** and sign in to Suno. On 20 November 2026 the **+** button was there only with the
browser's language set to English and a connection from the US. In a chat call both:
`@Suno @sunoforge`.

**Without the Skill.** From `gemini/`: the five `CORE_*` files and `DATA.zip`, into a
chat or a Gem's knowledge. Google moves Gems to skills from November 2026 and carries
only supported files; an archive in a Gem's knowledge is likely to be lost — upload the
Skill instead.

**Check.** Type `/` and pick `sunoforge`, or write `menu`.

More: [GEMINI.md](GEMINI.md).

---

## ChatGPT — the plugin

`SunoForge_v5.0.5_Plugin_for_ChatGPT.zip` from the release page. Done this way in the ChatGPT app on 20 November 2026:

1. ChatGPT → **Plugins** in the left sidebar → **Add** → **Upload plugin archive** → choose the zip. The
   SunoForge page opens: install the plugin.
2. Suno, optional — the same **Add** menu → **Add custom MCP server**: name `Suno`, server URL `https://api.suno.com/mcp`,
   leave the rest as it is, tick **I understand and want to continue**, then **Create as a plugin**. Connect
   Suno and sign in with your Suno account. Created as a plugin, Suno sits next to SunoForge — two plugins —
   and they work together; added as a bare MCP server it did not work with SunoForge.
3. A new chat: `@SunoForge` and your words — `@Suno @SunoForge` with Suno.

**Check.** `@SunoForge` opens the menu as text, with one question to pick from; `self-check` checks the
installed copy. If the first answer says SunoForge has no tools, send `@SunoForge` once more.

The plugin carries no MCP server of its own. An archive does not update itself: upload the next version again.
The phone app takes the plugin from the same account: the menu, [15] and the song editor worked in the Android app
on 20 November 2026; the skill shows there as `$sunoforge`.

---

## Antigravity — the plugin

This plugin is not built yet, so there is nothing to upload for it. Until it is out, Antigravity runs
SunoForge from the Markdown files: take `SunoForge_v5.0.5_Prompt_RAG.zip` from the release page and use its
`.md` files as files in the project, `_preloader.md` first. Suno's MCP server is added by hand:
[SUNO_MCP.md](SUNO_MCP.md).

---

## ChatGPT and grok.com — a Project or a custom GPT

**Project or custom GPT** (ChatGPT), **Project** (grok.com) — on any plan that has them.
Upload the `.md` files of `SunoForge_v5.0.5_Prompt_RAG.zip` (the prompt with RAG markup: eighteen files;
`_preloader.md` is its entry and already says what the lines below say)
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
- **Other hosts.** Suno's setup page also covers ChatGPT (a custom MCP server created as a
  plugin) and Gemini (a custom connector, then mention @Suno). SunoForge ran against Suno on
  both on 20 November 2026; the steps are in their sections above.

`mcp-info` lists which generation servers the session sees, which are off and how this
host enables them — it connects nothing itself. Everything else: [SUNO_MCP.md](SUNO_MCP.md).

## What comes next

- The Grok plugin, on the same pattern as the ChatGPT and Antigravity ones.
