# Tokens and size

Measured 5 November 2026 on the fourteen files of the Claude plugin, release 5.0.0. Encoding
`o200k_base`, with `cl100k_base` alongside. `INDEX.md`, the map the plugin reads first, is not in the
table: 6 426 tokens (`o200k`).

**Claude counts more.** Claude's own tokenizer gives about 1.45 times the `o200k` figure for these
files: `CORE_00_ENTRY.md` is 15 010 in `o200k` and about 21 700 for Claude. The whole set, by the plugin's own
estimate from that file, comes to about 235 000 Claude tokens — more than a 200K window holds together with a conversation. That is why
the plugin, by default, reads only the sections a task needs (`LOAD = sections`); `set load full` reads
everything and is meant for larger windows.

---

## Claude plugin (XML)

| File | KB | Lines | `o200k` | `cl100k` |
|---|---:|---:|---:|---:|
| `CORE_00_ENTRY.md` | 56.9 | 902 | 15 010 | 15 241 |
| `CORE_01_STYLE.md` | 45.1 | 1 082 | 11 170 | 11 352 |
| `CORE_02_LYRICS.md` | 38.2 | 1 050 | 9 850 | 10 018 |
| `CORE_03_DIAGNOSE.md` | 45.4 | 933 | 11 290 | 11 400 |
| `CORE_04_WHY.md` ⏸ | 36.0 | 755 | 8 405 | 8 508 |
| `DATA_BLANKS.md` | 37.8 | 608 | 11 822 | 11 230 |
| `DATA_GOOGLE_2026-10.md` | 33.3 | 666 | 8 722 | 8 917 |
| `DATA_LEGAL_2026-10.md` ⏸ | 29.3 | 501 | 6 999 | 7 139 |
| `DATA_OTHER_2026-10.md` ⏸ | 33.8 | 665 | 8 559 | 8 713 |
| `DATA_POSTPROD.md` | 28.6 | 678 | 6 766 | 6 865 |
| `DATA_RECIPES.md` | 44.2 | 1 730 | 11 607 | 11 756 |
| `DATA_SUNO_2026-10.md` | 61.6 | 1 065 | 16 046 | 16 163 |
| `DATA_SUNO_LIVE_2026-10.md` | 53.5 | 644 | 14 757 | 14 901 |
| `DATA_VOCAB.md` | 37.8 | 840 | 8 640 | 8 806 |
| **Total** | **581.5** | **12 119** | **149 643** | **151 009** |

Without the on-request files: **125 680** (`o200k`).

| Window | Full | Without on-request files |
|---|---:|---:|
| 1000K | 15.0% | 12.6% |
| 200K | 74.8% | 62.8% |
| 128K | 116.9% | 98.2% |

⏸ — read on request (`INDEX.md`: DATA_OTHER, DATA_LEGAL, CORE_04_WHY), not for every task.

---

## Markdown edition

The 5.0 Markdown edition for Gemini and other assistants is not out yet; its numbers come with it.
The 4.0 edition is measured in the [4.0 release](https://github.com/sanic732/SunoForge/releases/tag/v4.0).
