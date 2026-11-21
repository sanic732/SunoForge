<!-- SunoForge self-check: read by the sunoforge skill when the user types `self-check` or its word in their language (SKILL.md, Commands). -->
SunoForge command `self-check` — a word typed in the chat once SunoForge is active (no slash command of its own). The same
word in the menu's languages: «самодиагностика» (ru) · «самодіагностика» (uk) · "Selbstdiagnose" (de) · "autodiagnóstico"
(es, pt-BR) · "autodiagnostic" (fr) · "autodiagnosi" (it) · "diagnosis mandiri" (id).

Checks the installed copy of SunoForge in this session. It calls NO tool of a generation server — not even a free one —
spends nothing and writes no file. Reads: `plugin.json`, a few INDEX ranges, DATA_SUNO_LIVE §1 and §10, SKILL.md's
"Where state lives" (about 35–45 thousand tokens). `<plugin root>` is the folder that holds `.claude-plugin/` and
`skills/` (SKILL.md, "where the reference files are").

1. VERSION — the same number in three places: `version` in `<plugin root>/.claude-plugin/plugin.json`; the status line
   `SUNOFORGE v…` in `references/widgets/menu.html`; the INTRO line `**SUNOFORGE v…**` of CORE_00 §4. A file that
   cannot be read is "not checked", not a mismatch.
2. ROUTE MAP — take 3–5 references from `references/INDEX.md`, each in a different file (a `FILE §N L<a>–<b>` or
   `FILE §N · SUBHEADING L<a>–<b>`), read each by its range (offset = a, limit = b − a + 1) and confirm that its first
   line is that section's `<section id="§N"` tag or that `### SUBHEADING`. Name the references you picked.
3. SUNO TOOLS — the tools this session shows whose descriptions name suno.com (the name prefix depends on the host:
   DATA_SUNO_LIVE §1), by name only, against the 41 names of DATA_SUNO_LIVE §1 (the
   tool families §1 covers; a tool with another name is outside this check: neither listed nor counted): which are missing, which are new. No Suno server in the session → "not checked". Fields are the
   pre-flight's job (§6), not this check's.
4. SETTINGS — whether `${user_config.library_dir}`, `${user_config.language}` and `${CLAUDE_PLUGIN_DATA}` in SKILL.md
   arrived substituted or as literal `${`; which place the order of "Where state lives" picks for `settings.md` and
   `library.md` here; whether that place outlives the chat (a cloud sandbox does not: then `set`, `config` and `save`
   print a block). Write nothing to find out.
5. SCREENS — `references/widgets/` holds `UI.md`, the nine templates, `lab/keys.html` and the Russian and Ukrainian
   copies (`ru/`, `uk/`, nine files each): name what is missing. The folder cannot be listed → "not checked".

ANSWER — in OUTPUT_LANG, one table, one row per check: what was checked · result (checked ✓ / differs ✗ / not checked —) ·
what was seen (the numbers, the names, the paths). Under it, one line per ✗ with the likely cause and the fix
(update or reinstall the plugin; a missing Suno tool is the server's change — tell the author). Last line: "Nothing was
sent or spent." In view W: `widgets/next.html` with the fixes as steps.
