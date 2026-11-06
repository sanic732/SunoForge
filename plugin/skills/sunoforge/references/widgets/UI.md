# SunoForge UI — how a screen is drawn

One page for the model that draws SunoForge's screens. What to show is in CORE_00 §4 and §9 MENU UI; this page
says which file draws it, in which language, and what to fill. Read it once per conversation, before the first
widget.

## 1. Which file

| Screen | File | What you fill |
|---|---|---|
| Main menu and all thirteen submenus, the language picker | `menu.html` | `data-mcp`, `data-screen`, `data-p`, `data-l` |
| The voice catalogue `5a` | `voices.html` | `data-mine` |
| [15] Suno panel, the first screen: the status line and every section | `hub.html` | `data-mcp`, `data-st` |
| [15] Suno panel: a filtered list, a song's actions, mix two, playlists / workspaces (PICK), price card | `mcp.html` | as its header comment says |
| The take card — after EVERY spend | `take.html` | `data-title`, `data-sub`, `data-wait`, one `<b>` per take |
| My songs, 10 rows, no filter (`15h`); one song picked from a text table (`data-open="1"`, its actions open) | `songs.html` | one `<b>` per song, `data-open` |
| The tail of an answer with no widget of its own, view W: next steps, Menu, view pills | `next.html` | `data-b` |
| Edit a take `12c` | `edit.html` | `data-n`, `data-id`, `data-title`, `data-inst` |
| `15m` Create and the song editor | `editor.html` | `{{SONG}}` (JSON), `{{MODE}}` |

The menu navigates by itself: a tap on an entry opens its submenu inside the widget, with no message and no
wait; "Blank and tips" sends the entry number (then answer with the entry's blank of DATA_BLANKS as text, the
widget opened on that submenu with `data-screen="N"`). A sub-entry and a setting send their code; `5a` sends
"5a" and is answered with `voices.html` (read the library's `## ` lines first for `data-mine`).

Server text — song titles, styles, persona names — goes only into the attributes the header names, escaped
(& < > " ' as entities), never into the script. The compact screens (menu, voices, take, songs, edit) keep their
labels in the script's dictionaries and their data in attributes: you print the template and change only the
attributes.

## 2. Which language

The screen's language is OUTPUT_LANG (CORE_00 §9). Ready translated copies: `widgets/<lang>/<file>` for
**ru uk de es fr it pt-BR id** (Russian, Ukrainian, German, Spanish, French, Italian, Brazilian Portuguese,
Indonesian); English is
`widgets/<file>`.
- A copy exists → take it as it is and fill the attributes or slots. Translate nothing: every label, the
  script dictionaries included, is already in that language. Text you write into a slot (a status, a title,
  the credit line) is in that language too.
- No copy (any other language) → the English template; translate its visible labels and the values of its
  script dictionaries, as its header says.
- The view pills are translated (`W widgets · T text · B buttons`, the letters stay); they send `m`, `t`, `b`, commands in
  every language. They and the highlighted button carry inline styles: the desktop host restyles `<button>`.
- One source for every language: `widgets_i18n/<lang>.json` in the plugin's source; the copies are built
  from it by a script. A wrong word is fixed there, never by hand in a copy.

## 3. Speed

The chat waits while the model prints the widget — the whole fragment, every time, at about 250–340
characters a second [first-hand, claude.ai data export, 2026-11-05]. Keep it short:
- Print the template as it is: no re-indenting, the header comment stripped, no extra screens.
- A bare "SunoForge", "menu" or "start": read this page and `widgets/<lang>/menu.html`, draw at once; the
  reference files are read at the first task, not before the menu.
- One widget per answer; text under it carries only what a button cannot.
- An answer that calls tools says one line first. After every spend: one line, then `take.html`, also when
  the wait has not finished (`data-wait="1"`).
- My songs: 10 rows by default with `songs.html`; 50 and 100 only when asked, as a text table, never a widget.

| Screen (English copy, header stripped) | Characters printed |
|---|---|
| `menu.html`, every submenu inside | ≈9.9k |
| `take.html`, two takes | ≈4.7k |
| `songs.html`, ten rows | ≈5.7k |
| `edit.html` | ≈7.1k |
| `voices.html` | ≈4.1k |
| `hub.html`, the Suno panel's first screen | ≈5.1k |
| `next.html`, three steps | ≈2.3k |
| `mcp.html`, the whole template (one screen is kept: less) | ≈21.8k |
| `editor.html` | ≈46.3k |

## 4. No external files

Nothing in a SunoForge widget loads a script, a style, a font or an image from the network: the plugin
promises no network requests (README, PRIVACY). A template loaded from a CDN was prototyped on 2026-11-05
(one file draws every compact screen and `15m` from a short stub) and is not used: it needs a host test, a pinned
commit with SRI and a rewrite of that promise first.
