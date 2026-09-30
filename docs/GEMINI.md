# Запуск в Gemini · Running in Gemini

`[RU]` ниже · `[EN]` further down

Готовый Gem, всё уже загружено · A ready-made Gem, everything loaded:
[SunoForge v4.0](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing)

---

## [RU] Gemini Edition — папка `gemini/`

Для Gemini отдельная редакция: чистый Markdown, без единого XML-тега. XML в системном
контексте Gemini работает хуже, поэтому структура держится на заголовках. Содержание
то же, что в папке `claude/`.

**Как загружать.** Gemini принимает в одно сообщение до 10 вложений, а в архиве может
быть до 10 файлов. Поэтому ядро идёт файлами, а данные — одним архивом:

```
из папки gemini/ — в чат или в знания Gem:
  CORE_00_ENTRY.md      ← точка входа, обязателен
  CORE_01_STYLE.md
  CORE_02_LYRICS.md
  CORE_03_DIAGNOSE.md
  CORE_04_WHY.md
  DATA.zip              ← семь файлов DATA_* внутри
```

Затем в чат: `старт`.

**Почему так.** Ядро читается постоянно: `CORE_00_ENTRY` — это настройки, меню и
маршрутизация. Данные читаются выборочно, под платформу и задачу, им хватает архива.
Обновление данных — замена одного `DATA.zip`.

**Свой Gem.** Те же шесть вложений — в знания Gem. В инструкции Gem одной строки
достаточно: «Read CORE_00_ENTRY.md first and follow it».

**ChatGPT и Grok.** Берите папку `gemini/`: Markdown им подходит лучше XML. В ChatGPT —
проект с файлами (кастомные GPT OpenAI выводит из работы к 11.12.2026). В Grok —
вложением.

---

## [EN] Gemini Edition — the `gemini/` folder

Gemini gets its own edition: plain Markdown with no XML tags at all. XML in the system
context works worse on Gemini, so the structure rides on headings. The content is the
same as in the `claude/` folder.

**How to load it.** Gemini takes up to 10 attachments per message, and an archive can
hold up to 10 files. So the core goes as files and the data as one archive:

```
from the gemini/ folder — into the chat or the Gem's knowledge:
  CORE_00_ENTRY.md      ← entry point, required
  CORE_01_STYLE.md
  CORE_02_LYRICS.md
  CORE_03_DIAGNOSE.md
  CORE_04_WHY.md
  DATA.zip              ← the seven DATA_* files inside
```

Then type `start`.

**Why this way.** The core is read constantly: `CORE_00_ENTRY` holds the settings, the
menu and the routing. The data layer is read selectively, per platform and task, so an
archive is enough. Updating the data means replacing one `DATA.zip`.

**Your own Gem.** The same six attachments go into the Gem's knowledge. One line of Gem
instructions is enough: "Read CORE_00_ENTRY.md first and follow it".

**ChatGPT and Grok.** Use the `gemini/` folder — Markdown suits them better than XML.
In ChatGPT, a project with the files (OpenAI is retiring custom GPTs by 11 December
2026). In Grok, attach the files.
