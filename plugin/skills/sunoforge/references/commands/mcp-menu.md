<!-- SunoForge mcp-menu: read by the sunoforge skill when the user types `mcp-menu` (SKILL.md, Commands). -->
SunoForge command `mcp-menu` — a word typed in the chat once SunoForge is active (no slash command of its own). Same as `[15]` or `suno`.


1. Draw the MCP MENU of `references/DATA_SUNO_LIVE_2026-10.md` §7, its capabilities from §9: the HUB
   first — the account tool once for the status line (free), no songs; songs only when asked
   (`15h 10 | 50 | 100`, a filter, `15n`) with the library-list tool — matched by purpose
   (DATA_SUNO_LIVE §1); a song picked → its SONG ACTIONS (§7). "Listen" → audio-wait (Suno's
   player in the chat) and one line with the song's suno.com link, for a song the card does not play. With
   UI = widget, the HUB is `${CLAUDE_PLUGIN_ROOT}/widgets/hub.html` and a list, a pick or a card
   `widgets/mcp.html` (if the path shows the literal `${`,
   the folder `widgets/` beside `skills/`); a song's Remix or Edit and `15m` open
   `widgets/editor.html` (DATA_SUNO_LIVE §7 CREATE AND EDITOR); with UI = buttons, the four most
   likely items as a question; otherwise the list as text.
2. No Suno server in the session: the same panel, the items that need it marked "needs the Suno connector",
   then CONNECTIONS (CORE_00 §6) for how to add it. The panel never calls a spending tool: a pick
   opens the item's blank and, for a spend, the card of §7 and the user's yes.
