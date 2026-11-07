<!-- SunoForge save: read by the sunoforge skill when the user types `save` (SKILL.md, Commands). -->
SunoForge command `save` — a word typed in the chat once SunoForge is active (no slash command of its own).


1. Take the last Style text, persona or blueprint of this conversation; ask the name
   once if none was given; build the entry of DATA_RECIPES §8 with KIND, TARGET and
   SAVED (CORE_00 §9 STATE). Lyrics only if the user asks for them.
   When that blueprint went through a generation tool in this conversation, add
   TAKES: one line per clip — clip id, date, model, credits as the tool or DATA
   recorded them, else "unknown". Never a link a server returned for an upload or a
   download.
2. Append it under `## NAME` to `library.md` at the first writable place of the §9
   lookup order; with no disk, or when the host refuses the write, print the entry as
   a block for the user's Project.
   Confirm in ONE line that answers what, where and how to get it back:
   "Saved: «Forge — folk-rock» · kind: style · file: `.sunoforge/library.md` (in this folder) · get it back: «my style
   Forge» or [0] → My SunoForge presets." With no disk (a chat with no files): "This chat has no files — here is the
   block; put it in the Project's files and I will find it next time."
3. `save` with no kind → the Save menu, one line each: Style (Style and Exclude only — fits any lyrics) · Voice (the
   persona, long and short form) · Recipe (the prompt without lyrics: genre, tempo, sliders) · Whole prompt (Style +
   Lyrics + Exclude + settings) · Lyrics (only this one keeps the words) · My SunoForge presets (by kind) · Where is the
   file (its path and how to open it) · Forget a preset (`library forget NAME`, "was → will delete" first) · ← Back.
   The name is asked once, a suggestion already filled in ("Forge — folk-rock"). "Save in SunoForge" is the presets
   file; "To a playlist / workspace in Suno" (S9 / S10) is Suno's library — two labels, never one word for both.
