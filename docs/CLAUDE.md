# Running in Claude

> **Note on packages.** Version 5.0 ships the Claude plugin only
> (`sunoforge.plugin`). The Skill packages, `Prompt.zip` and the ChatGPT, Antigravity and Grok
> plugins for 5.0 are built separately and are still to come. Where this page names a `v4.0` file,
> that is the working package you can download today, from the
> [4.0 release](https://github.com/sanic732/SunoForge/releases/tag/v4.0).

---

## Claude Edition

**Claude Edition** is the same system in Claude's native XML: each file wrapped in
`<sunoforge_file>`, metadata in `<file_meta>`, sections in `<section>`, semantic
blocks in `<rag_zone>`. Claude reads this markup more precisely than flat Markdown.

Three ways to install it in Claude:

| Way | Where it works | Plan | What loads |
|---|---|---|---|
| **Plugin** from the marketplace | chat on the web, Claude Desktop, Cowork, Claude Code | paid | only the files a task needs |
| **Skill** as a ZIP | chat on the web, Claude Desktop | any, with Code execution on | only the files a task needs |
| **Project** | chat on the web, Claude Desktop | any | all thirteen files |

The Skill and the plugin open files per task. A Suno prompt needs `CORE_00`,
`CORE_01` and `DATA_SUNO` — about 37 thousand tokens instead of 124 thousand in a
Project.

The mobile app: install on the web or in Claude Desktop. Whether the phone app picks
up the account's skills, plugins and connectors is not confirmed yet.

### Plugin (paid plans)

**Chat, Claude Desktop, Cowork.** **Customize** menu → **Plugins** tab → **Add** →
**Add marketplace** → enter `sanic732/SunoForge` → install **SunoForge**. In Cowork,
open the Cowork tab first, then Customize. Plugins on your account also reach Claude
Code when you sign in with the same account.

**Without GitHub — as a file.** **Customize** → **Plugins** → **Add** → **Upload
plugin** → `sunoforge.plugin` from the release. A plugin added this way does not update
itself: upload the new version again.

**Claude Code:**
```
/plugin marketplace add sanic732/SunoForge
/plugin install sunoforge@sunoforge
```
Call it with `/sunoforge` or the word `SunoForge`, or just describe the task.
Update: `claude plugin update sunoforge@sunoforge`. Auto-update is off by default for
third-party marketplaces; in chat, the **Sync automatically** switch turns it on.

Language is automatic: SunoForge answers in the language you write in.

### Skill as a ZIP

1. **Settings → Capabilities** — turn on Code execution.
2. **Customize → Skills** → **+** → **Create skill** → **Upload a skill** → choose
   `SunoForge_v4.0_Skills_for_Claude.zip`.
3. The Skill switches on by itself when you ask for a music prompt, lyrics or a
   repair. You can also ask directly: "use SunoForge".

Anthropic's help article lists Skills on every plan, Free included; one
documentation page names paid plans only. No Skills section in your settings — use a
Project.

### Project

1. Create a Project.
2. Upload all thirteen files from the `claude/` folder to **Project knowledge**.
3. One line of project instructions is enough:
   `Read CORE_00_ENTRY.md first and follow it.`
4. In a project chat, type `start`.

Claude's help: project files up to 30 MB each, no cap on the number, but everything
together must fit the context window. The Claude Edition is about 124 thousand
tokens; a 200K window holds it with room for the conversation.

Without a project: attach the thirteen files to the first message (up to 20 files per
chat) and type `start`. The downside: every new chat starts over.

### Suno from Claude (optional, beta)

Suno's official MCP server is `https://api.suno.com/mcp`: sign in with your Suno
account, no API key, and it spends your Suno credits. With it SunoForge can send a
prompt to Suno from the chat — menu `[15] LIVE`, `send` — and always asks first;
`mcp-info` shows which generation servers the session sees and how to enable them,
connecting nothing itself. The same protocol works with any music-generation MCP server
the session shows. Details: [SUNO_MCP.md](SUNO_MCP.md).

The plugin does not bundle Suno's server — you add it like any MCP.

**Chat, Claude Desktop, Cowork:** **Customize** → **Connectors** → **Add custom
connector** → the URL `https://api.suno.com/mcp` → sign in to Suno.

**Claude Code:**
```
claude mcp add --transport http suno https://api.suno.com/mcp
/mcp
```
In `/mcp`, pick `suno` and sign in to Suno; until you do, `/mcp` shows "needs
authentication".

"Connecting AI apps to Suno is not yet available for your account" at sign-in means
Suno has not admitted the account to the beta yet: the early-access form is on
suno.com/mcp. It is not a SunoForge or settings problem.

**Your own server.** A music MCP server of your own is added the same way as Suno's: in
Claude Code with `claude mcp add`, in claude.ai chat and Cowork as a connector. The plugin starts no server.

### Settings and library

Two files of your own data — `settings.md` (`PLATFORMS`, persisted `set` values) and
`library.md` (`save` entries). The first hit of this order wins: the folder set in the
plugin's Settings (Claude Code and the desktop app — it survives an uninstall, and an empty
one gets the old files copied in once), the plugin's data folder in Claude Code (survives
updates, removed with the plugin unless `claude plugin uninstall --keep-data`), `.sunoforge/`
of the working folder in Cowork and with a standalone Skill, and in the chat and the mobile
app a Project file `sunoforge-settings.md` / `sunoforge-library.md`: no disk there, so
SunoForge prints the file as a block and you keep it in the Project. The first run asks one
question after the menu (which generators); `config` on demand also sets the view and
prices on the card. The same Settings tab sets the language (auto, en, ru, uk, de, es, fr, it, pt-BR, id); `set lang`
in the chat wins over it. Entries `[2]` Studio, `[5b]` custom persona, `[9]` recipes and
`[14]` Speech open a form when you ask for one — one choice per field, **Build** → a
blueprint; any result can be kept with `save`, and `library export` prints the whole
library as a block or a file.

### Commands and views

SunoForge commands are words typed without a slash — `set lang ru`, `menu`, `send`,
`mcp-info`, `config`, `why front-load`; the plugin itself is `/sunoforge`. The small line at
the foot of every answer switches the view: **M** menu (widgets with buttons — web, desktop
and phone apps, Cowork), **T** text, **B** buttons (one multiple-choice question). The
Claude Code terminal draws no widgets, so there M falls back to B by itself.
