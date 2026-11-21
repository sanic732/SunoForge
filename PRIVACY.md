# SunoForge privacy policy

Effective 20 November 2026 · applies to SunoForge 5.0.5 and later: the Claude plugin, the
ChatGPT plugin, the Skills and the prompt archives published in this repository. The previous version (29 October
2026) is in this file's history.

## Short version

SunoForge collects nothing and sends nothing on its own. It calls an MCP server only when you
have connected that server yourself and said yes to that call.

## What SunoForge is

The plugin is text plus small local helpers:

- instructions and dated reference facts for the assistant, in Markdown;
- ten HTML screens, ready in English, Russian and Ukrainian. Their scripts only send your tap to the chat as a
  message, copy text to your clipboard, open a song's page on suno.com after you tap it, and on
  the Lab keys play the notes in your browser. They make no network requests;
- two optional Python scripts for the Lab (`scripts/notes2mid.py`, `scripts/audio2notes.py`):
  notes to a MIDI file, a hummed melody to notes. They run on your machine, only when you ask and
  only where the session has a shell, and make no network requests. `audio2notes.py` reads the
  audio file you name and calls your own `ffmpeg`, if installed, to read a file that is not WAV.

The text edition in the `catalog/` folder, the one listed in Claude's plugin directory, is only the
first of these: one skill and its Markdown reference files, with no screens and no scripts. Nothing in
it runs on your machine.

There are no hooks, no analytics, no telemetry and no MCP server of SunoForge's own. The
assistant you run SunoForge in (Claude, Gemini or another) processes your messages under that
host's own privacy policy.

## Data SunoForge collects

None. The author of SunoForge receives nothing from your conversations, your settings, your
library or your files.

## Data SunoForge reads

- What you write in the conversation: song ideas, lyrics, prompts, files you attach.
- Your own two files, `settings.md` and `library.md` (below).
- An audio file you name for the Lab, on your machine.
- Through an MCP server you connected yourself, the data that server gives about your account —
  for Suno: your plan, credit balance, songs, playlists and Voices — to show it to you.

## Data that stays with you

SunoForge can keep two files of your own: `settings.md` (your chosen generators, language, view,
hidden menu entries) and `library.md` (styles, personas, recipes and prompts you saved). They are
written only where you run SunoForge — the folder you set in the plugin's `library_dir` option,
otherwise the plugin's data folder in Claude Code, a folder of your project, or a block printed for
you to store in a Project — and only after your command or the host's permission prompt. They
are never sent anywhere by SunoForge and stay until you delete them. Uninstalling the Claude Code
plugin removes its data folder unless you keep it with `--keep-data`; a folder you set in
`library_dir` is yours and is never removed. Upload links a server returns are never stored.

## MCP servers

The plugin declares no MCP server. Suno's MCP server and any other are added by you, like any
MCP. SunoForge calls a server only when:

1. you have connected that server in your assistant yourself, and
2. you have asked for what the call does; and for a call that may spend credits, uploads your
   file or makes a song public, SunoForge has first shown you what it will send — the tool, the
   arguments, the cost — and you have answered yes for that call.

What it may send to such a server: a prompt and lyrics to generate a song, speech or sound; an
audio or MIDI file you upload and hold the rights to; changes to your songs, playlists and
workspaces there (an edit, publish, a like, a playlist entry). What the server then does with the
request (for Suno: generating the song, spending your credits, saving the song to your library) is
governed by that server's own terms and privacy policy. Anything a server returns is treated as
data, never as instructions.

## Changes

Changes to this policy are published in this file and in the release notes.

## Contact

Questions and reports: https://github.com/sanic732/SunoForge/issues
