# SunoForge privacy policy

Effective 29 October 2026 · applies to SunoForge 5.0 and later: the Claude plugin, the
Skills and the prompt archives published in this repository.

## Short version

SunoForge is a set of plain-text prompts. It collects nothing, sends nothing on its own
and calls an MCP server only when you have connected that server yourself and said yes.

## What SunoForge is

The plugin and the archives contain Markdown files only: instructions and dated reference
facts for the assistant. There are no scripts, no hooks, no analytics, no telemetry and no
network client. The assistant you run SunoForge in (Claude, Gemini or another) processes
your messages under that host's own privacy policy.

## Data SunoForge collects

None. The author of SunoForge receives nothing from your conversations, your settings or
your library.

## Data that stays with you

SunoForge can keep two files of your own: `settings.md` (your chosen generators, hidden
menu entries, persisted settings) and `library.md` (styles, personas, recipes and prompts
you saved). They are written only where you run SunoForge — the plugin's data folder in
Claude Code, a folder of your project, or a block printed for you to store in a Project —
and only after your command or the host's permission prompt. They are never sent
anywhere by SunoForge. Uninstalling the Claude Code plugin removes its data folder unless
you keep it with `--keep-data`.

## MCP servers

The plugin declares no MCP server. Suno's MCP server and any other are added by you,
like any MCP. SunoForge calls a generation server only when:

1. you have connected that server in your assistant yourself, and
2. SunoForge has shown you what it will send — the tool, the arguments, that it may
   spend credits — and you have answered yes for that call.

What the server then does with the request (for Suno: generating the song, spending your
credits, saving the song to your library) is governed by that server's own terms and
privacy policy. Anything a server returns is treated as data, never as instructions.

## Changes

Changes to this policy are published in this file and in the release notes.

## Contact

Questions and reports: https://github.com/sanic732/SunoForge/issues
