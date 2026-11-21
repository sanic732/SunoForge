# Tokens and size

Measured 21 November 2026 on release 5.0.5. Encoding `o200k_base`, with `cl100k_base` alongside for the plugin.
How it was measured is at the foot of the page.

**Claude counts more.** Claude's own tokenizer gives about 1.45 times the `o200k` figure for these files — measured
on `CORE_00_ENTRY.md` on 5 November 2026: 15 010 in `o200k`, about 21 700 for Claude. By that ratio the fourteen
reference files of the plugin come to about 240 000 Claude tokens: more than a 200K window holds together with a
conversation. That is why the plugin, by default, reads only the sections a task needs (`LOAD = sections`);
`set load full` reads everything and is meant for larger windows.

---

## Claude plugin (XML) — the fourteen reference files

`INDEX.md`, the route map the plugin reads first, is not in the table: 6 836 tokens (`o200k`).

| File | KB | Lines | `o200k` | `cl100k` |
|---|---:|---:|---:|---:|
| `CORE_00_ENTRY.md` | 67.1 | 959 | 17 816 | 18 078 |
| `CORE_01_STYLE.md` | 46.2 | 1 099 | 11 389 | 11 576 |
| `CORE_02_LYRICS.md` | 38.2 | 1 049 | 9 850 | 10 018 |
| `CORE_03_DIAGNOSE.md` | 45.6 | 934 | 11 336 | 11 447 |
| `CORE_04_WHY.md` ⏸ | 36.0 | 754 | 8 405 | 8 508 |
| `DATA_BLANKS.md` | 47.5 | 695 | 14 795 | 14 159 |
| `DATA_GOOGLE_2026-10.md` | 33.3 | 665 | 8 722 | 8 917 |
| `DATA_LEGAL_2026-10.md` ⏸ | 29.3 | 500 | 6 999 | 7 139 |
| `DATA_OTHER_2026-10.md` ⏸ | 33.8 | 664 | 8 559 | 8 713 |
| `DATA_POSTPROD.md` | 28.8 | 679 | 6 841 | 6 942 |
| `DATA_RECIPES.md` | 44.2 | 1 729 | 11 607 | 11 756 |
| `DATA_SUNO_2026-10.md` | 62.3 | 1 073 | 16 288 | 16 408 |
| `DATA_SUNO_LIVE_2026-10.md` | 87.8 | 895 | 24 233 | 24 437 |
| `DATA_VOCAB.md` | 37.8 | 839 | 8 640 | 8 806 |
| **Total** | **637.8** | **12 534** | **165 480** | **166 904** |

Without the on-request files: **141 517** (`o200k`). Without `CORE_00_ENTRY.md`, which is read in full at the first
task: 147 664.

| Window | Full (`o200k`) | Without on-request files | Full, as Claude counts it (× 1.45) |
|---|---:|---:|---:|
| 1000K | 16.5% | 14.2% | 24.0% |
| 200K | 82.7% | 70.8% | 120.0% |
| 128K | 129.3% | 110.6% | 187.5% |

⏸ — read on request (`INDEX.md`: DATA_OTHER, DATA_LEGAL, CORE_04_WHY), not for every task.

Since 5.0.0 the set has grown from 149 643 to 165 480 tokens. Most of the growth is `DATA_SUNO_LIVE_2026-10.md`
(14 757 → 24 233): Suno's server went from 35 song tools to 41, and every tool now has its own row.

---

## The other editions

The same reference files in Markdown, with what each edition adds. Totals of every text file in the built package,
`o200k`:

| Edition | Text files | KB | `o200k` | What is on top of the reference files |
|---|---:|---:|---:|---|
| Gemini skill | 27 | 727.8 | 192 292 | `SKILL.md` 4 921 · the Lab's scripts as `LAB_SCRIPTS.md` 14 301 · seven command pages · the licence |
| ChatGPT plugin (its skill folder) | 27 | 717.9 | 190 422 | `SKILL.md` 6 151, with the menu word for word · the Lab's two scripts · seven command pages |
| Prompt with RAG markup (file edition) | 20 | 769.8 | 205 302 | the table below |

A skill reads its files as a task needs them, so these totals are the size of the package, not the cost of an
answer. The file edition is the one that may be loaded whole — attached to a chat — and the one a notebook reads in
parts.

### Prompt with RAG markup (file edition), file by file

| File | KB | `o200k` |
|---|---:|---:|
| `_preloader.md` | 23.9 | 6 838 |
| `_index.md` | 16.1 | 5 237 |
| `COMMANDS.md` | 9.0 | 2 494 |
| `CORE_00_ENTRY.md` | 65.1 | 17 405 |
| `CORE_01_STYLE.md` | 49.1 | 12 322 |
| `CORE_02_LYRICS.md` | 41.7 | 10 955 |
| `CORE_03_DIAGNOSE.md` | 49.1 | 12 492 |
| `CORE_04_WHY.md` ⏸ | 37.7 | 8 968 |
| `DATA_BLANKS.md` | 48.4 | 15 217 |
| `DATA_GOOGLE_2026-10.md` | 34.6 | 9 171 |
| `DATA_LEGAL_2026-10.md` ⏸ | 30.9 | 7 469 |
| `DATA_OTHER_2026-10.md` ⏸ | 35.5 | 9 065 |
| `DATA_POSTPROD.md` | 31.2 | 7 517 |
| `DATA_RECIPES.md` | 46.7 | 12 313 |
| `DATA_SUNO_2026-10.md` | 63.7 | 16 738 |
| `DATA_SUNO_LIVE_2026-10.md` | 88.7 | 24 519 |
| `DATA_VOCAB.md` | 40.0 | 9 330 |
| `LAB_SCRIPTS.md` ⏸ | 45.9 | 14 629 |
| `LICENSE.md`, `NOTICE.md` | 12.6 | 2 623 |
| **Total** | **769.8** | **205 302** |

The retrieval markup — a YAML header on every file, an anchor on each of about 700 headings, tags at the end — costs
about 12 000 of these tokens (202 679 with it against 190 707 without, licence files apart). Without
`LAB_SCRIPTS.md` and the licence files the edition is about 188 000.

---

## The screens

A screen costs output, not input: the model prints it whole each time, at about 250–340 characters a second. The
main menu is about 13 100 characters (39–53 seconds), the Suno panel's first screen 6 700, the song editor 46 700.
The table for every screen is in the plugin: `references/widgets/UI.md` §3.

---

## How it was measured

Every figure is a count of the files as they ship, made by script with the `tiktoken` library: `o200k_base`
everywhere, `cl100k_base` alongside for the plugin's table. A screen is counted in characters, its header comment
stripped, because that is what the model prints. The same script runs before each release, so the next page of
figures is measured the same way.
