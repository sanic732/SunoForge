# Запуск в Gemini · Running in Gemini

`[RU]` ниже · `[EN]` further down

Готовый Gem, всё уже загружено · A ready-made Gem, everything loaded:
[SunoForge v4.0](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing)

---

## [RU] Gemini Edition — папка `gemini/`

Для Gemini отдельная редакция: чистый Markdown, без единого XML-тега. XML в системном
контексте Gemini работает хуже, поэтому структура держится на заголовках. Содержание
то же, что в папке `claude/`.

**Навык — самый короткий путь.** В Gemini появились навыки (Skills), и Google переводит
в них Gem-боты — по объявлению в приложении, с 17 ноября 2026. Навык SunoForge — это
`SKILL.md` и двенадцать файлов, которые Gemini открывает по мере надобности, а не
держит все сразу.

1. Распакуйте `SunoForge_v4.0_Skills_for_Gemini.zip`. Внутри — папка `sunoforge`: в ней
   `SKILL.md` и двенадцать файлов.
2. Страница **Навыки** → **Загрузить** → выберите папку `sunoforge` целиком. Имя папки
   должно совпадать с именем навыка — `sunoforge`; другое Gemini не примет.
3. Проверьте и нажмите **Создать**.

Окно загрузки принимает файлы и папки в форматах CSV, PY, TXT и MD — архив целиком там
может не пройти, поэтому сначала распаковка.

Включённый навык Gemini применяет сам, когда просите промпт для музыки; вызвать явно —
`/` и выбрать `sunoforge`. Поэтому команды SunoForge в Gemini надёжнее писать без
слеша: `set lang ru`, `menu`. По справке Google навыки есть в веб-версии, мобильном
приложении и на Mac, для личного аккаунта Google и с 18 лет.

Google предупреждает: большинство инструментов Gem с навыками не работает, в том числе
«Создать музыку» (Create music). Если в чате с навыком генерации нет, вставьте готовый
промпт для Lyria в обычный чат Gemini. Автоматический перенос Gem берёт только
поддерживаемые файлы; архива среди них нет, поэтому навык лучше загрузить из релиза, а
не ждать переноса.

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

**A Skill — the shortest way.** Gemini now has skills, and Google is turning Gems into
them — from 17 November 2026, by the notice in the app. The SunoForge Skill is
`SKILL.md` plus the twelve files, which Gemini opens as it needs them instead of
holding them all at once.

1. Unpack `SunoForge_v4.0_Skills_for_Gemini.zip`. Inside is a folder `sunoforge` holding
   `SKILL.md` and the twelve files.
2. The **Skills** page → **Upload** → choose the whole `sunoforge` folder. The folder
   name must match the skill name, `sunoforge`; Gemini refuses any other.
3. Review it and click **Create**.

The upload window takes files and folders in CSV, PY, TXT and MD — a whole archive may
not pass there, hence unpacking first.

Gemini applies a skill that is turned on by itself when you ask for a music prompt; to
call it directly, type `/` and pick `sunoforge`. That is why SunoForge commands are
safer without the slash in Gemini: `set lang ru`, `menu`. Google's help lists skills in
the web app, the mobile app and on Mac, for personal Google Accounts, 18 and over.

Google warns that most tools available in Gems do not work with skills, Create music
among them. If a chat with the skill cannot generate, paste the finished Lyria prompt
into a regular Gemini chat. The automatic move from Gems carries only supported files,
and an archive is not one of them — so upload the skill from the release rather than
waiting for the move.

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
