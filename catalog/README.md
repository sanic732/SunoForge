# SunoForge — text edition

SunoForge 5.0.5 is a metaprompt for AI music: a reference and a set of prompt-writing practices in Markdown
files. You describe a song in your own words — or pick an entry of its menu — and Claude answers with a prompt ready
to paste into a music generator: Suno v6 and Suno Speech, Google Lyria 3.5, Flow Music, ElevenMusic, Stable Audio,
MiniMax and local models. It also repairs a prompt that misbehaves, marks up lyrics, builds voices and personas, and
says what to check about rights before a release.

This folder is the text edition of the plugin: one skill and its Markdown reference files. It has no screens, no
scripts, no hooks and no MCP server.

## What it does and does not do

- It writes text. SunoForge has no tools of its own, connects to nothing and generates nothing.
- If you connected a music generator's own MCP connector to Claude yourself (Suno's, for example), Claude can send a
  prompt there and work with your songs — only after it shows you what will be sent and what it costs, and you say
  yes. Without a connector you copy the prompt by hand.
- It reads and writes two small files of yours, `settings.md` and `library.md` (your saved styles and personas), in
  the folder you set in the plugin's settings or in the plugin's data folder. Nothing else is stored and nothing is
  sent anywhere by the plugin.

## How to use it

Type `SunoForge` to open the menu — sixteen numbered entries and `[0]` for settings — or just describe the song.
Useful words: `menu`, `compact` (the short menu), `config`, `save`, `library`, `self-check`, `set lang <language>`.
Menus are text here; answers come in the language you write in.

## The full plugin

The full SunoForge plugin — the same reference with on-screen menus and buttons, ready Russian and Ukrainian
screens, and the Lab (a melody you play or hum becomes notes and a MIDI file) — is in the same repository:
https://github.com/sanic732/SunoForge (folder `plugin/`). The command below installs that full edition, with
screens, from the repository's marketplace in Claude Code — not this one, which is the text edition for Claude's
plugin directory:

```
/plugin install sunoforge --marketplace sanic732/SunoForge
```

Entry [16] LAB of the menu is not in this text edition.

## Links

Repository and documentation: https://github.com/sanic732/SunoForge · version history:
https://github.com/sanic732/SunoForge/blob/main/docs/CHANGELOG.md · privacy:
https://github.com/sanic732/SunoForge/blob/main/PRIVACY.md · questions and bug reports:
https://github.com/sanic732/SunoForge/issues

An independent open-source project by sanic732, Apache License 2.0. Not affiliated with Suno, Google, ElevenLabs,
Stability AI, MiniMax or Anthropic; their names are used only to say what the prompts are written for.
