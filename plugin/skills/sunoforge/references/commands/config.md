<!-- SunoForge config: read by the sunoforge skill when the user types `config` (SKILL.md, Commands). -->
SunoForge command `config` — a word typed in the chat once SunoForge is active (no slash command of its own).


1. No argument → the question of CORE_00 §9 FIRST RUN (the generators) plus three more:
   the view (M = menu: widgets with buttons, the default — they draw in the web, desktop and phone apps and Cowork;
   T = text only; B = buttons: one multiple-choice question under the text, for a host with no widgets, like the
   terminal), whether a confirmation card shows the price (PRICE;
   the yes stays) and how the reference is loaded (LOAD: by section as the task needs, or
   the thirteen files at the start of a conversation — DATA_OTHER still waits for a yes — ≈235k tokens (estimated from CORE_00, measured at 21.7k), more
   than a 200k window holds). Ask by the mechanisms
   the host offers (a multiple-choice tool where there is one, text otherwise). With an
   argument (`platforms …`, `ui …`, `price …`, `load …`, or any `set` key) → apply it.
   Several views picked at once → `ui widget`: it falls back to buttons and
   then text by itself. A question left unanswered writes nothing for its key; never write a
   value the user did not pick.
2. Write `settings.md` by the WRITE rule of CORE_00 §9 STATE: where the read found the
   file, else the first writable place of the WHERE order (the folder set in the plugin's
   configuration, then the plugin's data folder named in SKILL.md, then
   `.sunoforge/` in the working folder); a sandbox that does not outlive the chat counts as
   no disk. No disk, or the host refuses the write → print the file as a block and say
   "keep this in your Project". Then show
   the main menu (every entry — settings never hide one).
3. `config folder` (or "where are my files") → say where settings and library live now, in
   the WHERE order, and how to choose the folder: it is the plugin's own setting "Folder for
   your SunoForge data" (`library_dir`) — in the Claude desktop app: Settings → the SunoForge
   plugin → the Settings tab, type the path (e.g. `D:\SunoForge`) and Save — the same tab sets the language (`language`: auto, en, ru, uk); in Claude Code:
   `/plugin` → SunoForge → configure, or `/config`. A folder there survives an uninstall and
   an update. The app says so itself: the value is kept on that computer and used by new
   sessions started on it, not by SSH, WSL or cloud sessions. The claude.ai web and phone apps
   have no disk and do not use this setting: the files live in the Project
   (`sunoforge-settings.md`, `sunoforge-library.md`).
   Never write outside the folders of the WHERE order.
