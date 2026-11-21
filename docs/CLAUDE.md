# Running in Claude

> **Note on packages.** Version 5.0.5 ships four: the Claude plugin (`sunoforge.plugin`), the Gemini skill
> (`SunoForge_v5.0.5_Skill_for_Gemini.zip`), the ChatGPT plugin (`SunoForge_v5.0.5_Plugin_for_ChatGPT.zip`) and the prompt
> with RAG markup, the file edition (`SunoForge_v5.0.5_Prompt_RAG.zip`: plain Markdown files for a Gemini notebook, NotebookLM,
> a Project or a chat that takes attachments). The Skill package for Claude and the Antigravity and Grok plugins are built separately and are
> still to come. Where this page names a `v4.0` file,
> that is the working package you can download today, from the
> [4.0 release](https://github.com/sanic732/SunoForge/releases/tag/v4.0).

---

## Claude Edition

**Claude Edition** is the plugin: the same system in Claude's native XML — each reference file wrapped in
`<sunoforge_file>`, its metadata in `<file_meta>`, its sections in `<section>` — with screens that have buttons.

Three ways to run SunoForge in Claude:

| Way | Where it works | Plan | What loads |
|---|---|---|---|
| **Plugin** from the marketplace or as a file | chat on the web, Claude Desktop, Cowork, Claude Code | paid | only the sections a task needs |
| **Project** with the file edition | chat on the web, Claude Desktop | any | what the Project retrieves for the question |
| **Skill** as a ZIP | chat on the web, Claude Desktop | any, with Code execution on | the 4.0 package; the 5.0 Skill is not out yet |

The plugin opens files by section, per task. The fourteen reference files together are about 165 thousand tokens in
`o200k_base` and about 240 thousand for Claude's own tokenizer — more than a 200K window holds with a conversation,
which is why nothing is read whole by default ([TOKENS.md](TOKENS.md)).

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
third-party marketplaces; in chat, the **Sync automatically** switch turns it on. After an update start a new
chat: an open one keeps working on the copy it loaded.

Language is automatic: SunoForge answers in the language you write in.

### Project (any plan)

The file edition, `SunoForge_v5.0.5_Prompt_RAG.zip` — eighteen Markdown files with retrieval markup.

1. Create a Project.
2. Upload the `.md` files of the archive to **Project knowledge**.
3. One line of project instructions is enough:
   `Read _preloader.md first and follow it.`
4. In a project chat, type `start`.

Claude's help says that when project knowledge comes near the context window, Claude turns on retrieval for the
Project and searches the files instead of loading them all; the file edition's markup — a header on every file, an
anchor on every heading — is made for that. This edition has no screens: the menu and the cards come as text, and
settings are printed as a block to keep. It was tried in a Gemini notebook (21 November 2026); in a Claude Project
it has not been run yet.

### Skill as a ZIP (the 4.0 package)

The 5.0 Skill package is not out yet. Until it is, the 4.0 one works — older content:

1. **Settings → Capabilities** — turn on Code execution.
2. **Customize → Skills** → **+** → **Create skill** → **Upload a skill** → choose
   `SunoForge_v4.0_Skills_for_Claude.zip`.
3. The Skill switches on by itself when you ask for a music prompt, lyrics or a
   repair. You can also ask directly: "use SunoForge".

Anthropic's help article lists Skills on every plan, Free included; one
documentation page names paid plans only. No Skills section in your settings — use a
Project.

### Suno from Claude (optional, beta)

Suno's official MCP server is `https://api.suno.com/mcp`: sign in with your Suno
account, no API key, and it spends your Suno credits. With it SunoForge can send a
prompt to Suno from the chat and work with your songs there — menu `[15] MY SUNO`, `send` — and always asks first;
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
SunoForge prints the file as a block and you keep it in the Project. The folder field is empty by default: leave
it empty, or name any folder of yours. The first run asks one
question after the menu (which generators); `config` on demand also sets the view and
prices on the card. The same Settings tab sets the language of the answers (auto, en, ru, uk, de, es, fr, it,
pt-BR, id); `set lang` in the chat wins over it. Entries `[2]` By hand, `[5b]` custom persona, `[9]` recipes and
`[14]` Speech open a form when you ask for one — one choice per field, **Build** → a
blueprint; any result can be kept with `save`, and `library export` prints the whole
library as a block or a file.

### The menu, commands and views

The menu has sixteen entries, `[1]`–`[16]`, and `[0]` for settings. In Simple mode the screen shows six of them and
"All sections"; in Extended mode, all. `[16]` is the Lab (beta): play a melody on the on-screen keys or hum it, get
its notes and a MIDI file for Suno. You never have to press anything — describing the song in your own words works
the same.

SunoForge commands are words typed without a slash — `set lang ru`, `menu`, `compact`, `send`,
`mcp-info`, `config`, `self-check`, `why front-load`; the plugin itself is `/sunoforge`. `self-check` checks the
installed copy — the version, the route map, the Suno tools, the settings — and calls nothing.

The small line at the foot of every answer switches the view: **W** screens with buttons (the web and
desktop apps), **T** text, **B** questions with options. The Claude Code terminal draws no screens, so there W falls back
to B by itself. The screens come ready in English, Russian and Ukrainian; in any other language a screen is drawn
from the English template with its labels translated as it is printed.
