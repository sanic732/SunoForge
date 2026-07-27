# Лицензия, источники и оговорки · Licence, sources and notices

---

## Лицензия

**MIT.** © 2026 Sanic (`sanic732`). Полный текст — в файле `LICENSE` в корне.

Можно свободно использовать, изменять, распространять и применять коммерчески.
Единственное требование — сохранять текст лицензии и указание авторства.

Лицензия распространяется на **саму систему** — на текст инструкций. Она ничего
не говорит о правах на музыку, которую вы с её помощью создадите: те определяются
условиями платформы, на которой вы генерируете. Об этом — файл
`files/DATA_LEGAL_2026-07.md` или команда `/legal`.

---

## Стороннего кода в поставке нет

SunoForge — это набор текстовых инструкций. В поставке нет ни библиотек, ни
исполняемого кода, ни заимствованных исходников. Вопрос совместимости лицензий
не возникает.

---

## На чём построено

Система выросла из трёх собственных предшественников:

| | |
|---|---|
| **SunoForge v1.1** | март 2026, MIT, английская, опубликована на GitHub |
| **SunoForge v2.0** | май 2026, русская, публиковалась на 4PDA |
| **Suno AI Architect «Polymath»** | предшественник, русский монолит |

Из них перенесены приёмы, структуры и словари. Факты о платформах из них **не**
переносились без повторной проверки — часть оказалась устаревшей или неверной.

---

## Источники фактов

Уровни достоверности в файлах системы соответствуют типу источника.

**`[OFFICIAL]` — документация вендоров.**

- **Google Cloud Blog, «Ultimate prompting guide for Lyria 3 models»**,
  8 апреля 2026, авторы Katie Nguyen и Hussain Chinoy. Единственный вендорский
  документ по промптингу во всём покрытии системы. Использован как источник
  фактов; формулировки не воспроизводятся — за ними следует идти в оригинал.
- Карточки моделей, справка и release notes Suno, Google, ElevenLabs,
  Stability AI, MiniMax.

**`[COMMUNITY]` — независимые тесты, гайды и обзоры.** Собраны и сверены между
собой; там, где источники расходятся, расхождение показано, а не разрешено
волевым решением.

**`[UNVERIFIED]` — то, что широко повторяется без первоисточника.** Оставлено в
системе намеренно: удалить недостаточно, иначе она не сможет распознать и
починить чужой промпт, где это встретится.

---

## Оговорки

**Товарные знаки.** Suno, Google, Gemini, Lyria, Flow Music, ElevenLabs,
ElevenMusic, Stability AI, Stable Audio, MiniMax, Udio, Spotify, YouTube и
прочие названия принадлежат их владельцам. Проект с ними **не связан**, ими не
поддерживается и не одобрен.

**Не юридическая консультация.** Файл `DATA_LEGAL` — фактическая сводка публично
известных позиций, а не совет. Для всего, где есть деньги или заказчик, читайте
действующие условия сами и обращайтесь к юристу.

**Срок годности.** Файлы `DATA_*` с датой в имени описывают состояние на
27.07.2026. Область меняется ежемесячно. Через квартал считайте любое число
здесь гипотезой, а не фактом.

**Ответственность.** Система даёт рекомендации по составлению промптов.
Результат генерации, его качество и правовые последствия его использования
остаются на пользователе.

---

## Сборка

Материалы для v3.0 собраны и проверены с помощью **Perplexity Deep Research**
(три независимых прогона по одной теме — расхождения между ними прямо повлияли
на решение ввести разметку достоверности) и метапромпт-системы **P2P**.

---
---

## Licence

**MIT.** © 2026 Sanic (`sanic732`). Full text in `LICENSE` at the root.

Free to use, modify, redistribute and apply commercially. The only requirement
is preserving the licence text and the attribution.

The licence covers **the system itself** — the text of the instructions. It says
nothing about rights in the music you produce with it: those are set by the
terms of whichever platform you generate on. See
`files/DATA_LEGAL_2026-07.md`, or the `/legal` command.

---

## No third-party code ships here

SunoForge is a body of text instructions. The distribution contains no
libraries, no executable code and no borrowed source. Licence compatibility does
not arise.

---

## What it is built on

The system grew out of three of the author's own predecessors:

| | |
|---|---|
| **SunoForge v1.1** | March 2026, MIT, English, published on GitHub |
| **SunoForge v2.0** | May 2026, Russian, published on the 4PDA forum |
| **Suno AI Architect "Polymath"** | predecessor, a Russian monolith |

Techniques, structures and vocabularies were carried across. Platform facts were
**not** carried across without re-verification — a number turned out to be stale
or wrong.

---

## Sources of fact

The confidence levels used throughout the files correspond to source type.

**`[OFFICIAL]` — vendor documentation.**

- **Google Cloud Blog, "Ultimate prompting guide for Lyria 3 models"**,
  8 April 2026, by Katie Nguyen and Hussain Chinoy. The only vendor-written
  prompting document across this system's entire coverage. Used as a source of
  fact; its wording is not reproduced — go to the original for that.
- Model cards, help centres and release notes from Suno, Google, ElevenLabs,
  Stability AI and MiniMax.

**`[COMMUNITY]` — independent testing, guides and reviews.** Collected and
cross-checked; where sources disagree, the disagreement is shown rather than
resolved by preference.

**`[UNVERIFIED]` — widely repeated with no primary source.** Retained
deliberately: deleting it is not enough, or the system could not recognise and
repair someone else's prompt containing it.

---

## Notices

**Trademarks.** Suno, Google, Gemini, Lyria, Flow Music, ElevenLabs,
ElevenMusic, Stability AI, Stable Audio, MiniMax, Udio, Spotify, YouTube and
other names belong to their respective owners. This project is **unaffiliated**
with, unendorsed by and unsupported by any of them.

**Not legal advice.** `DATA_LEGAL` is a factual summary of publicly reported
positions, not counsel. For anything with money or a client attached, read the
current terms yourself and take professional advice.

**Shelf life.** The dated `DATA_*` files describe the state of things on
27 July 2026. This field changes monthly. A quarter later, treat every figure
here as a hypothesis rather than a fact.

**Liability.** The system offers guidance on composing prompts. The generated
output, its quality, and the legal consequences of using it remain the user's
responsibility.

---

## Build

Material for v3.0 was gathered and cross-checked using **Perplexity Deep
Research** — three independent passes on the same questions, whose mutual
disagreements directly motivated the decision to introduce confidence marking —
and the **P2P** meta-prompt system.
