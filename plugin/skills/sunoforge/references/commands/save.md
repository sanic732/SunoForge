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
   Confirm in one line with the name and where it went.
