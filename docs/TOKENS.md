# Tokens and size

Measured 29 October 2026 against both editions. Encoding `o200k_base`, with `cl100k_base` alongside.

---

## Claude Edition (XML)

| File | KB | Lines | `o200k` | `cl100k` |
|---|---:|---:|---:|---:|
| `CORE_00_ENTRY.md` | 47.8 | 844 | 12 690 | 12 885 |
| `CORE_01_STYLE.md` | 44.1 | 1 059 | 10 839 | 11 015 |
| `CORE_02_LYRICS.md` | 37.8 | 1 041 | 9 702 | 9 872 |
| `CORE_03_DIAGNOSE.md` | 44.3 | 908 | 11 003 | 11 106 |
| `CORE_04_WHY.md` ⏸ | 36.7 | 758 | 8 555 | 8 658 |
| `DATA_GOOGLE_2026-10.md` | 33.2 | 657 | 8 709 | 8 897 |
| `DATA_LEGAL_2026-10.md` ⏸ | 29.5 | 500 | 7 031 | 7 168 |
| `DATA_OTHER_2026-10.md` | 33.6 | 659 | 8 503 | 8 658 |
| `DATA_POSTPROD.md` | 27.0 | 652 | 6 370 | 6 470 |
| `DATA_RECIPES.md` | 44.4 | 1 731 | 11 680 | 11 829 |
| `DATA_SUNO_2026-10.md` | 48.1 | 888 | 12 288 | 12 387 |
| `DATA_SUNO_LIVE_2026-10.md` | 20.4 | 307 | 5 693 | 5 777 |
| `DATA_VOCAB.md` | 38.0 | 835 | 8 667 | 8 828 |
| **Total** | **484.9** | **10 839** | **121 730** | **123 550** |

Without lazy files: **106 144** (`o200k`).

| Window | Full | Without lazy |
|---|---:|---:|
| 1000K | 12.2% | 10.6% |
| 200K | 60.9% | 53.1% |
| 128K | 95.1% | 82.9% |

---

## Gemini Edition (Markdown)

| File | KB | Lines | `o200k` | `cl100k` |
|---|---:|---:|---:|---:|
| `CORE_00_ENTRY.md` | 47.3 | 821 | 12 563 | 12 760 |
| `CORE_01_STYLE.md` | 43.6 | 1 030 | 10 682 | 10 856 |
| `CORE_02_LYRICS.md` | 37.2 | 1 008 | 9 533 | 9 704 |
| `CORE_03_DIAGNOSE.md` | 43.9 | 889 | 10 884 | 10 991 |
| `CORE_04_WHY.md` ⏸ | 36.4 | 747 | 8 470 | 8 571 |
| `DATA_GOOGLE_2026-10.md` | 32.8 | 634 | 8 582 | 8 767 |
| `DATA_LEGAL_2026-10.md` ⏸ | 29.0 | 477 | 6 904 | 7 039 |
| `DATA_OTHER_2026-10.md` | 33.1 | 636 | 8 372 | 8 528 |
| `DATA_POSTPROD.md` | 26.6 | 629 | 6 243 | 6 343 |
| `DATA_RECIPES.md` | 44.0 | 1 714 | 11 577 | 11 726 |
| `DATA_SUNO_2026-10.md` | 47.4 | 853 | 12 118 | 12 214 |
| `DATA_SUNO_LIVE_2026-10.md` | 20.0 | 290 | 5 586 | 5 667 |
| `DATA_VOCAB.md` | 37.5 | 810 | 8 534 | 8 697 |
| **Total** | **478.7** | **10 538** | **120 048** | **121 863** |

Without lazy files: **104 674** (`o200k`).

| Window | Full | Without lazy |
|---|---:|---:|
| 1000K | 12.0% | 10.5% |
| 200K | 60.0% | 52.3% |
| 128K | 93.8% | 81.8% |

---

⏸ — lazy files, not loaded by default

The Claude Edition's XML adds about 10 % tokens for the same content; in exchange Claude gets explicit
section and zone boundaries.
