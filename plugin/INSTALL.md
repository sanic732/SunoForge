# Installing the SunoForge plugin

The plugin works in Claude Code and, on paid plans, in Claude chat on the web, Claude
Desktop and Cowork. Other ways to run SunoForge (a Skill, a Project, Gemini, any
long-context assistant) are on the release page and in `docs/INSTALL.md` of the
repository.

## Claude Code

```
/plugin install sunoforge --marketplace sanic732/SunoForge
```

On Claude Code older than 2.1.275, two steps:

```
/plugin marketplace add sanic732/SunoForge
/plugin install sunoforge@sunoforge
```

At install Claude Code may ask for one optional field, a **folder for your SunoForge data** (settings and library): it
survives uninstalling the plugin; empty means the plugin's data folder, deleted on uninstall.
Change it later with `/plugin configure sunoforge`.

**Check.** `/sunoforge` opens the menu `[1]`–`[15]` (the word `SunoForge` works too);
`SunoForge mcp-menu` opens the Suno panel.

**Update.** `claude plugin update sunoforge@sunoforge`. Auto-update is off by default for
third-party marketplaces. `claude plugin uninstall sunoforge@sunoforge` also removes the
plugin's data folder — your settings and library — unless you add `--keep-data`.

## Claude chat, Claude Desktop, Cowork (paid plans)

**Customize** → **Plugins** → **Add** → **Add marketplace** → `sanic732/SunoForge` →
install **SunoForge**. In Cowork, open the Cowork tab first, then Customize.

Without GitHub: **Customize** → **Plugins** → **Add** → **Upload plugin** →
`sunoforge.plugin` from the release page. A plugin added as a file does not update itself.

**Check.** In a new chat: `SunoForge` → the menu `[1]`–`[15]`; `SunoForge` and your words → straight to the task.

A music MCP server of your own is added as a connector in Claude chat and Cowork, and
with `claude mcp add` in Claude Code.

## Suno, optional (beta)

Suno's server is not bundled with the plugin; add it like any MCP server.

- Claude Code: `claude mcp add --transport http suno https://api.suno.com/mcp`, then
  `/mcp` → `suno` → sign in to Suno.
- Claude chat, Desktop, Cowork: **Customize** → **Connectors** → **Add custom
  connector** → `https://api.suno.com/mcp` → sign in to Suno.

Suno admits accounts through an early-access form on suno.com/mcp. Until your account is
admitted, sign-in ends with "Connecting AI apps to Suno is not yet available for your
account" on every client — that is Suno's beta gate, not a plugin fault. The server
spends your Suno credits: every creation makes two takes for 10 credits, Max Mode doubles
it. SunoForge shows a card and waits for your yes before every spend; `mcp-menu` shows the
balance and everything the connector can do. What the server takes and gives, as this
edition saw it on 4–5 November 2026: `DATA_SUNO_LIVE_2026-10.md` in the skill's references.
