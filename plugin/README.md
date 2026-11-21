# SunoForge

**AI music prompt orchestrator for Claude.** Describe a song, a soundtrack or a voice-over
in your own words, in any language, and SunoForge writes a ready-to-paste prompt for the
generator you use: Suno v6 and Suno Speech, Google Lyria 3.5, Flow Music, ElevenMusic,
Stable Audio, MiniMax and local models. It also marks up lyrics, writes speech scripts,
repairs old prompts, checks rights before a release and plans stems and mastering. With
Suno's connector in the session it sends the prompt to Suno and works with your songs
there — only after your yes.

SunoForge is an independent project: it is not affiliated with, endorsed by or supported by
Suno, Inc., Anthropic or any other vendor it writes prompts for.

Version 5.0.5 · Apache 2.0 licence · [repository](https://github.com/sanic732/SunoForge) ·
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

The plugin is text plus small local helpers: one skill, ten HTML screens ready in three languages (English, Russian, Ukrainian)
(their scripts only send your tap as a message, copy text to your clipboard, open a song's
page on suno.com after you tap it, and — on the Lab keys — play the notes in your browser)
and two optional Python scripts for the Lab (`scripts/notes2mid.py`, `scripts/audio2notes.py`:
notes to MIDI, a hummed melody to notes; local, no network; they need Python 3 and numpy, and
`audio2notes.py` calls your own `ffmpeg`, if installed, to read a file that is not WAV). The
scripts run only when you ask and only where the session has a shell. No hooks, no MCP server
of its own, no network requests. The screens' scripts are plain JavaScript in the plugin's own files, written
compactly so that a screen prints faster; they only draw buttons and send your tap to the chat as a message.

One command: **SunoForge** (`/sunoforge`). Alone it opens the menu `[1]`–`[16]`; followed by your
own words it goes straight to the task. Everything else is a word in the chat:

| Word | What it does |
|---|---|
| `send` | Sends the last blueprint to a music-generation server the session shows; shows a card and waits for your yes |
| `mcp-menu` | Menu [15] MY SUNO, one screen at a time as in the Suno app: create, your songs (10 · 50 · 100), liked, mix two songs, playlists, workspaces, voices; a song opens its own menu |
| `mcp-info` | Which generation servers this session sees and how this host enables more |
| `self-check` | «самодиагностика» and the same word in eight more languages: checks the installed copy — the version in three places, a few route-map ranges, the Suno tools by name, where your settings are written, the two screen folders — as one table; calls no Suno tool, spends nothing |
| `library` | Your saved styles, personas, recipes and prompts: list, insert, export, forget |
| `save` | Keeps the last Style, persona, recipe or blueprint in your library |
| `config` | Which generators you use, the view (W screen · T text · B questions), prices on the card, loading by section or whole, where your files live |

Three views, switched by the small line at the foot of every answer: **T** — text only; **B** — buttons, one
multiple-choice question under the text (the terminal); **W** — screens, the widgets `widgets/menu.html` (the menu), `widgets/mcp.html` (the Suno panel) and
`widgets/editor.html` (Create and the song editor) among them, the default in the web, desktop and phone
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
edition saw it on 4–7 November 2026:

- 41 tools: songs, speech, covers, extensions, mashups and a free join; sounds (one-shots
  and loops); uploads, your Voices; tempo, key and sung-word analysis and questions to
  Suno's own listener, free; your library, playlists, workspaces; downloads with a
  download credit. Since 6 November also stems, MIDI in and out, a real edit of a song
  (Replace Section) and publish settings.
- Since 5 November the connector also takes Variety (0–4) and can make a new song from up
  to ten of yours — sample, restyle, drop or pull out a part (`15o`). Tried on 5 November:
  Variety 4 rewrote the Style as it should; a restyle from one song kept its tempo, key and piano;
  each call cost 10 credits.
- Every creation makes two takes for 10 credits; Max Mode, only when you ask for it by
  name, doubles that. SunoForge shows a card with the exact cost before every spend.
- Not reachable through the connector: Personas, Studio, Inspire, Custom Models and the
  app's own Remaster — SunoForge gives the steps in the Suno app instead.

SunoForge reads the tools the session actually shows, checks every argument before the
card, fixes what the server refuses without spending anything, and asks again whenever a
fix changes what you agreed to. Full map: `DATA_SUNO_LIVE_2026-10.md` in the skill's
references.

## Privacy

SunoForge collects no data, keeps no analytics and sends nothing anywhere on its own.
It reads what you write in the conversation and, only on your command, keeps your
`settings.md` and `library.md` in the folder you set (`library_dir`) or in the plugin's data
folder. The Lab script reads an audio file you name, on your machine. Data leaves the session
only through an MCP connector you added yourself (for example Suno's): a prompt, lyrics, a file
you upload, a change to your songs there — only when you ask, and for a call that may spend
credits, uploads a file or makes a song public, only after SunoForge has shown what it will send
and what it costs and you have said yes to that call. Full policy:
[PRIVACY.md](https://github.com/sanic732/SunoForge/blob/main/PRIVACY.md).
