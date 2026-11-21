SunoForge command `config` — a word typed in the chat once SunoForge is active (no slash command of its own).

1. No argument → the question of CORE_00 §9 FIRST RUN (the generators) plus three more: the mode (`USER_LEVEL`:
   Simple = beginner, Extended = pro, or auto — a new user starts in Simple), the view (T = text only, the default;
   B = one multiple-choice question under the text) and whether a confirmation card shows the price (PRICE; the yes
   stays). Ask by the mechanisms the host offers (a multiple-choice tool where there is one, text otherwise). With an
   argument (`platforms …`, `level …`, `ui …`, `price …`, or any `set` key) → apply it. A question left unanswered
   writes nothing for its key; never write a value the user did not pick.
2. Write `settings.md` by the WRITE rule of CORE_00 §9 STATE: where the read found the file, else the first writable
   place of the WHERE order (the folder set in the plugin's configuration, then the plugin's data folder named in
   SKILL.md, then `.sunoforge/` in the working folder); a sandbox that does not outlive the chat counts as no disk.
   No disk, or the host refuses the write → print the file as a block and say "keep this block". Then show the main
   menu (every entry — settings never hide one).
3. `config folder` (or "where are my files") → say where settings and library live now, in the WHERE order, and how
   to choose the folder: it is the plugin's own setting "Folder for your SunoForge data" (`library_dir`) — any folder
   of yours; the same place sets the language (`language`: auto, or a language name or code such as en, ru, uk). A
   folder there survives an uninstall and an update. Never write outside the folders of the WHERE order.
