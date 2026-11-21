SunoForge command `self-check` — a word typed in the chat once SunoForge is active (no slash command of its own). The
same word in other languages: «самодиагностика» (ru) · «самодіагностика» (uk) · "Selbstdiagnose" (de) ·
"autodiagnóstico" (es, pt-BR) · "autodiagnostic" (fr) · "autodiagnosi" (it) · "diagnosis mandiri" (id).

Checks the installed copy of SunoForge in this session. It calls NO tool of a generation server — not even a free
one — spends nothing and writes no file.

1. VERSION — the same number in three places: `version` in the plugin's `.claude-plugin/plugin.json`; the title of
   `SKILL.md`; the INTRO line `**SUNOFORGE v…**` of `CORE_00_ENTRY.md` §4. A file that cannot be read is "not checked",
   not a mismatch.
2. ROUTE MAP — take 3–5 references from `INDEX.md` (`FILE §N`), each in another file; open each file and confirm the
   heading `## §N · …` is there. Name the references you picked.
3. FILES — every file `CORE_00_ENTRY.md` §0 names is in this skill folder. The folder cannot be listed → "not checked".
4. SUNO TOOLS — the tools this session shows whose descriptions name suno.com, by name only (the prefix depends on the
   host), against the 41 names of `DATA_SUNO_LIVE_2026-10.md` §1 (the tool families §1 covers; a tool with another name
   is outside this check: neither listed nor counted): which are missing, which are new. No Suno server in the
   session → "not checked".
5. SETTINGS — whether `${user_config.library_dir}`, `${user_config.language}` and `${CLAUDE_PLUGIN_DATA}` in SKILL.md
   arrived substituted or as literal `${`; which place the order of "Where state lives" picks for `settings.md` and
   `library.md` here; whether that place outlives the chat. Write nothing to find out.

ANSWER — in OUTPUT_LANG, one Markdown table: Check · Result (✓ / ✗ / —) · Details. Under it one fix line per ✗ (update
or reinstall the plugin; a missing Suno tool is the server's change — tell the author). Last line: "Nothing was sent
or spent."
