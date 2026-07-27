# Токены и объём · Tokens and size

Замер 27.07.2026 по фактическим файлам поставки. Кодировка `o200k_base`
(GPT-4o / GPT-5, актуальная), для сравнения `cl100k_base` (GPT-4 / Claude —
приблизительная оценка).

Measured 27 July 2026 against the shipped files. Encoding `o200k_base` (current
GPT family), with `cl100k_base` alongside for comparison.

---

## По файлам · Per file

| Файл · File | КБ · KB | Строк · Lines | `o200k` | `cl100k` |
|---|---:|---:|---:|---:|
| `CORE_00_ENTRY.md` | 26,7 | 515 | 6 135 | 6 748 |
| `CORE_01_STYLE.md` | 47,3 | 1 068 | 10 441 | 11 263 |
| `CORE_02_LYRICS.md` | 38,4 | 991 | 8 672 | 9 539 |
| `CORE_03_DIAGNOSE.md` | 35,2 | 712 | 7 803 | 8 268 |
| `CORE_04_WHY.md` ⏸ | 31,9 | 693 | 7 051 | 7 373 |
| `DATA_SUNO_2026-07.md` | 25,9 | 495 | 5 459 | 6 151 |
| `DATA_GOOGLE_2026-07.md` | 30,4 | 720 | 6 619 | 7 213 |
| `DATA_OTHER_2026-07.md` | 26,7 | 596 | 5 536 | 6 059 |
| `DATA_VOCAB.md` | 42,2 | 882 | 8 889 | 9 616 |
| `DATA_RECIPES.md` | 51,1 | 1 934 | 12 784 | 13 324 |
| `DATA_POSTPROD.md` | 30,5 | 671 | 6 378 | 7 004 |
| `DATA_LEGAL_2026-07.md` ⏸ | 25,5 | 540 | 5 000 | 5 581 |
| **Итого · Total** | **411,9** | **9 817** | **90 767** | **98 139** |

⏸ — ленивые файлы, по умолчанию не грузятся.
⏸ — lazy files, not loaded by default.

---

## По слоям · By layer

| | `o200k` |
|---|---:|
| Слой CORE, 5 файлов · CORE layer, 5 files | 40 102 |
| Слой DATA, 7 файлов · DATA layer, 7 files | 50 665 |
| Из них ленивые · of which lazy | 12 051 |
| **Стартовая нагрузка · Startup load** | **78 716** |

---

## Доля окна · Share of the context window

| Окно · Window | Полный комплект · Full set | Без ленивых · Without lazy |
|---|---:|---:|
| 1M | 9,1 % | 7,9 % |
| 200K | 45,4 % | 39,4 % |
| 128K | 70,9 % | 61,5 % |

---

## Если места мало · If the window is tight

Порядок отключения — от наименее болезненного к самому:

Drop in this order, least painful first:

1. `CORE_04_WHY` и `DATA_LEGAL` — уже ленивые. Останутся недоступными `/why`
   и `/legal`. **−12 051**
2. Адаптеры платформ, которыми вы не пользуетесь. Работаете только с Suno —
   `DATA_GOOGLE` и `DATA_OTHER` не нужны. **−12 155**
3. `DATA_RECIPES` — каталог готовых рецептов. Система продолжит собирать промпты
   с нуля. **−12 784**
4. `DATA_POSTPROD` — нужен только при работе после генерации. **−6 378**
5. `DATA_VOCAB` — словарь дескрипторов. Описания станут беднее. **−8 889**

Минимальная рабочая конфигурация под одну платформу:
`CORE_00` + `CORE_01` + `CORE_02` + `CORE_03` + один адаптер `DATA_*` —
около **38 500** токенов.

Minimum working configuration for a single platform:
`CORE_00` + `CORE_01` + `CORE_02` + `CORE_03` + one `DATA_*` adapter —
roughly **38,500** tokens.

⚠️ `CORE_00_ENTRY.md` не отключается никогда: в нём preloader, меню, маршрутизация
и протоколы вывода, на которые ссылаются все остальные файлы.

⚠️ `CORE_00_ENTRY.md` is never optional: it holds the preloader, the menu, the
routing and the output protocols that every other file references.

---

## Сравнение с прошлыми версиями · Against previous versions

| | Файлов · Files | КБ · KB |
|---|---:|---:|
| v1.1 | 10 | ~200 |
| v2.0 | 10 | 327 |
| **v3.0** | **12** | **411,9** |

Слой данных вырос по требованию полноты — каталоги должны быть избыточными.
Ядро при этом похудело после удаления фольклора.

The data layer grew because catalogues are meant to be redundant. The core
shrank once the folklore was removed.
