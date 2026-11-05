<!-- SunoForge library: read by the sunoforge skill when the user types `library` (SKILL.md, Commands). -->
SunoForge command `library` — a word typed in the chat once SunoForge is active (no slash command of its own). It reads the user's own `library.md`, not the songs in
their Suno account; for those, SunoForge uses Suno's tools (CORE_00 §6 LIVE).


1. Find `library.md` by the §9 lookup order. No argument → read only the `## ` lines
   and list the names with their KIND and TARGET; nothing found → say where a library
   would live on this host and offer `save`.
2. `library <name>` → read that entry's body and put it into the next blueprint
   unchanged. An entry with TAKES also offers its clips by id for a cover or an
   extension (CORE_00 §6 LIVE) without searching the Suno library; that is a new
   spend — a card and a yes — and a clip the account no longer sees answers 404.
   `library export` → print the whole file as a block (and, where the host
   can hand over a file, as a Markdown file) so the user can keep or move it.
   `library forget <name>` → ask once, then remove the entry; with no disk, print the
   file without it.
