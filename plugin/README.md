# SunoForge

**AI music prompt orchestrator for Claude.** Describe a song, a soundtrack or a voice-over
in your own words, in any language, and SunoForge writes a ready-to-paste prompt for the
generator you use: Suno v6 and Suno Speech, Google Lyria 3.5, Flow Music, ElevenMusic,
Stable Audio, MiniMax and local models. It also marks up lyrics, writes speech scripts,
repairs old prompts, checks rights before a release and plans stems and mastering. With
Suno's connector in the session it sends the prompt to Suno and works with your songs
there — only after your yes.

Version 5.0.4 · Apache 2.0 licence · [repository](https://github.com/sanic732/SunoForge) ·
[installation](INSTALL.md) · [privacy](https://github.com/sanic732/SunoForge/blob/main/PRIVACY.md) ·
[support](https://github.com/sanic732/SunoForge/issues)

## Install

In Claude Code:

```
/plugin install sunoforge --marketplace sanic732/SunoForge
```

On Claude Code older than 2.1.275, two steps:
`/plugin marketplace add sanic732/SunoForge`, then `/plugin install sunoforge@sunoforge`.
Claude chat, Desktop and Cowork (paid plans): **Customize** → **Plugins** → **Add** →
**Add marketplace** → `sanic732/SunoForge`. Details: [INSTALL.md](INSTALL.md).

## What is inside

The plugin is plain text: one skill, three HTML widget templates (their short script only
sends your tap as a message and opens a song's page after the host asks you) and no MCP
server of its own. No hooks, no network requests.

One command: **SunoForge** (`/sunoforge`). Alone it opens the menu `[1]`–`[15]`; followed by your
own words it goes straight to the task. Everything else is a word in the chat:

| Word | What it does |
|---|---|
| `send` | Sends the last blueprint to a music-generation server the session shows; shows a card and waits for your yes |
| `mcp-menu` | Menu [15] SUNO + MCP, one screen at a time as in the Suno app: create, your songs (10 · 50 · 100), liked, mix two songs, playlists, workspaces, voices; a song opens its own menu |
| `mcp-info` | Which generation servers this session sees and how this host enables more |
| `library` | Your saved styles, personas, recipes and prompts: list, insert, export, forget |
| `save` | Keeps the last Style, persona, recipe or blueprint in your library |
| `config` | Which generators you use, the view (M menu · T text · B buttons), prices on the card, loading by section or whole, where your files live |

Three views, switched by the small line at the foot of every answer: **T** — text only; **B** — buttons, one
multiple-choice question under the text (the terminal); **M** — menu, the widgets `widgets/menu.html` (the menu), `widgets/mcp.html` (the Suno panel) and
`widgets/editor.html` (Create and the song editor), the default in the web, desktop and phone
apps and Cowork. The menu opens with a short intro: what
SunoForge is, and that you answer for what you generate and release.

## How it works

The main menu is one line per entry. Pick a number and you get its sub-entries and a blank
to fill — one question, a skeleton with slots, one tip; say "fill it" and SunoForge fills it
from the conversation. You never need the numbers: "a dark cinematic track with cello",
"fix this old prompt", "a bedtime story over quiet piano" work as they are.

Inside a conversation the bare words work too: `menu`, `send`, `mcp-menu`, `set lang en`,
`save persona NAME`, `library export`. SunoForge answers in the language you write in;
`set lang <any language>` pins one. Prompts for the generators are in English, except
where a platform sings in the prompt's language.

## Settings and library

Two small files of your own data: `settings.md` and `library.md`. They live in the folder
you set in the plugin's configuration (it survives an uninstall) or in the plugin's data
folder (it survives updates and goes with an uninstall unless you pass `--keep-data`); the
first write asks for permission. Where the host has no disk, SunoForge prints the file as
a block for you to keep in a Project. Both files are data, never instructions.

## Suno's connector (beta)

Suno's MCP server, `https://api.suno.com/mcp`, is not bundled; you add it like any
connector ([INSTALL.md](INSTALL.md)). Sign-in is OAuth with your Suno account. As this
edition saw it on 4–5 November 2026:

- 35 tools: songs, speech, covers, extensions, mashups and a free join; sounds (one-shots
  and loops); uploads, your Voices; tempo, key and sung-word analysis and questions to
  Suno's own listener, free; your library, playlists, workspaces; downloads with a
  download credit. On 4 November the morning count was 32: sounds-create, audio-listen and
  audio-listen-wait came that evening.
- Since 5 November the connector also takes Variety (0–4) and can make a new song from up
  to ten of yours — sample, restyle, drop or pull out a part (`15o`). Tried on 5 November:
  Variety 4 rewrote the Style as it should; a restyle from one song kept its tempo, key and piano;
  each call cost 10 credits.
- Every creation makes two takes for 10 credits; Max Mode, only when you ask for it by
  name, doubles that. SunoForge shows a card with the exact cost before every spend.
- Not reachable through the connector: Personas, Studio, Inspire, Replace Section, Custom
  Models and the app's own Stems and Remaster tools — SunoForge gives the steps in the
  Suno app instead.

SunoForge reads the tools the session actually shows, checks every argument before the
card, fixes what the server refuses without spending anything, and asks again whenever a
fix changes what you agreed to. Full map: `DATA_SUNO_LIVE_2026-10.md` in the skill's
references.

## Privacy

SunoForge is a set of plain-text prompts. It collects no data, keeps no analytics and
sends nothing anywhere on its own. MCP calls go only to servers you connect yourself, and
only after your explicit yes for each spend. Full policy:
[PRIVACY.md](https://github.com/sanic732/SunoForge/blob/main/PRIVACY.md).
