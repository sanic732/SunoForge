# Токены и объём · Tokens and size

Замер 30.09.2026 по файлам обеих редакций. Кодировка `o200k_base`, для сравнения `cl100k_base`.
Measured 30 September 2026 against both editions. Encoding `o200k_base`, with `cl100k_base` alongside.

---

## Claude Edition (XML)

| Файл · File | КБ · KB | Строк · Lines | `o200k` | `cl100k` |
|---|---:|---:|---:|---:|
| `CORE_00_ENTRY.md` | 37.9 | 783 | 10 093 | 10 270 |
| `CORE_01_STYLE.md` | 48.3 | 1 229 | 11 878 | 12 044 |
| `CORE_02_LYRICS.md` | 37.8 | 1 107 | 9 680 | 9 846 |
| `CORE_03_DIAGNOSE.md` | 45.0 | 1 017 | 11 160 | 11 243 |
| `CORE_04_WHY.md` ⏸ | 38.8 | 882 | 9 152 | 9 242 |
| `DATA_GOOGLE_2026-09.md` | 33.2 | 736 | 8 668 | 8 844 |
| `DATA_LEGAL_2026-09.md` ⏸ | 27.1 | 531 | 6 520 | 6 641 |
| `DATA_OTHER_2026-09.md` | 32.6 | 725 | 8 300 | 8 448 |
| `DATA_POSTPROD.md` | 29.9 | 754 | 7 077 | 7 179 |
| `DATA_RECIPES.md` | 49.2 | 1 985 | 13 012 | 13 138 |
| `DATA_SUNO_2026-09.md` | 36.5 | 787 | 9 330 | 9 404 |
| `DATA_VOCAB.md` | 40.3 | 943 | 9 239 | 9 394 |
| **Итого · Total** | **456.6** | **11 479** | **114 109** | **115 693** |

Без ленивых файлов · without lazy files: **98 437** (`o200k`).

| Окно · Window | Полный комплект · Full | Без ленивых · Without lazy |
|---|---:|---:|
| 1000K | 11.4% | 9.8% |
| 200K | 57.1% | 49.2% |
| 128K | 89.1% | 76.9% |

---

## Gemini Edition (Markdown)

| Файл · File | КБ · KB | Строк · Lines | `o200k` | `cl100k` |
|---|---:|---:|---:|---:|
| `CORE_00_ENTRY.md` | 35.5 | 676 | 9 483 | 9 662 |
| `CORE_01_STYLE.md` | 43.9 | 1 032 | 10 746 | 10 922 |
| `CORE_02_LYRICS.md` | 35.0 | 960 | 8 958 | 9 123 |
| `CORE_03_DIAGNOSE.md` | 40.2 | 823 | 9 901 | 9 994 |
| `CORE_04_WHY.md` ⏸ | 35.3 | 719 | 8 180 | 8 280 |
| `DATA_GOOGLE_2026-09.md` | 30.8 | 603 | 8 027 | 8 207 |
| `DATA_LEGAL_2026-09.md` ⏸ | 25.4 | 433 | 6 055 | 6 175 |
| `DATA_OTHER_2026-09.md` | 30.1 | 593 | 7 659 | 7 811 |
| `DATA_POSTPROD.md` | 27.4 | 634 | 6 423 | 6 525 |
| `DATA_RECIPES.md` | 44.2 | 1 711 | 11 615 | 11 765 |
| `DATA_SUNO_2026-09.md` | 34.2 | 648 | 8 711 | 8 788 |
| `DATA_VOCAB.md` | 37.8 | 809 | 8 587 | 8 749 |
| **Итого · Total** | **419.7** | **9 641** | **104 345** | **106 001** |

Без ленивых файлов · without lazy files: **90 110** (`o200k`).

| Окно · Window | Полный комплект · Full | Без ленивых · Without lazy |
|---|---:|---:|
| 1000K | 10.4% | 9.0% |
| 200K | 52.2% | 45.1% |
| 128K | 81.5% | 70.4% |

---

⏸ — ленивые файлы, по умолчанию не грузятся · lazy files, not loaded by default.

XML-разметка Claude Edition добавляет около 10 % токенов к той же информации; за это Claude получает
явные границы разделов и зон. The Claude Edition's XML adds about 10 % tokens for the same content;
in exchange Claude gets explicit section and zone boundaries.
