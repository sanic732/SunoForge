# Запуск в Claude · Running in Claude

`[RU]` ниже · `[EN]` further down

---

## [RU] Claude Edition

**Claude Edition** — та же система в нативном для Claude XML: каждый файл обёрнут в
`<sunoforge_file>`, метаданные — в `<file_meta>`, разделы — в `<section>`, смысловые
блоки — в `<rag_zone>`. Claude читает такую разметку точнее, чем сплошной Markdown.

Три способа поставить её в Claude:

| Способ | Где работает | Тариф | Сколько грузится |
|---|---|---|---|
| **Плагин** из маркетплейса | чат на сайте, Claude Desktop, Cowork, Claude Code | платные | только нужные файлы |
| **Skill** архивом | чат на сайте, Claude Desktop | любой, нужен Code execution | только нужные файлы |
| **Project** | чат на сайте, Claude Desktop | любой | все двенадцать файлов |

Skill и плагин открывают файлы по задаче. Для промпта под Suno это `CORE_00`,
`CORE_01` и `DATA_SUNO` — около 32 тысяч токенов вместо 114 тысяч в Project.

### Плагин (платные тарифы)

**Чат, Claude Desktop, Cowork.** Меню **Customize** → вкладка **Plugins** → **Add** →
**Add marketplace** → введите `sanic732/SunoForge` → установите **SunoForge**. В Cowork
сначала откройте вкладку Cowork, потом Customize. Плагины из аккаунта сами приходят
в Claude Code, если войти тем же аккаунтом.

**Без GitHub — файлом.** **Customize** → **Plugins** → **Add** → **Upload plugin** →
`sunoforge.plugin` из релиза. Так плагин не обновляется сам: новую версию загружают
заново.

**Claude Code:**
```
/plugin marketplace add sanic732/SunoForge
/plugin install sunoforge@sunoforge
```
Вызов — `/sunoforge` (или `/sunoforge:sunoforge`), либо просто опишите задачу.
Обновление: `claude plugin update sunoforge@sunoforge`. Автообновление для сторонних
маркетплейсов выключено по умолчанию; в чате его включает переключатель
**Sync automatically**.

Язык — автоматический: SunoForge отвечает на том языке, на котором вы пишете.

### Skill архивом

1. **Settings → Capabilities** — включите выполнение кода (Code execution).
2. **Customize → Skills** → **+** → **Create skill** → **Upload a skill** → выберите
   `SunoForge_v4.0_Skills_for_Claude.zip`.
3. Skill включается сам, когда вы просите промпт, текст или разбор для музыки. Можно
   и прямо: «используй SunoForge».

По справке Anthropic Skills доступны на всех тарифах, включая Free, но одна
страница документации называет только платные. Нет раздела Skills — ставьте Project.

### Project

1. Создайте Project.
2. В **Project knowledge** загрузите все двенадцать файлов из папки `claude/`.
3. В инструкции проекта одной строки достаточно:
   `Read CORE_00_ENTRY.md first and follow it.`
4. В чате проекта напишите `старт`.

Справка Claude: файлы проекта — до 30 МБ каждый, количество не ограничено, но всё
вместе должно помещаться в контекст. Claude Edition — около 114 тысяч токенов; в
окно 200K она помещается с запасом на разговор.

Без проекта: приложите двенадцать файлов к первому сообщению (до 20 файлов на чат)
и напишите `старт`. Минус: в каждом новом чате всё заново.

### Команды в терминале Claude Code

Терминал Claude Code сам разбирает строки, начинающиеся со слеша, и на `/set` ответит
«Unknown command». Там пишите команды SunoForge без слеша — `set lang ru`, `menu`,
`why front-load` — или после имени навыка: `/sunoforge set lang ru`. Вкладка Code в
Claude Desktop передаёт такую строку модели. Форма без слеша работает везде.

Генерацию музыки прямо из Claude Code (Lyria через Gemini API, ElevenLabs, локальные
модели) описывает отдельное предложение по интеграции — в состав релиза оно не входит.

---

## [EN] Claude Edition

**Claude Edition** is the same system in Claude's native XML: each file wrapped in
`<sunoforge_file>`, metadata in `<file_meta>`, sections in `<section>`, semantic
blocks in `<rag_zone>`. Claude reads this markup more precisely than flat Markdown.

Three ways to install it in Claude:

| Way | Where it works | Plan | What loads |
|---|---|---|---|
| **Plugin** from the marketplace | chat on the web, Claude Desktop, Cowork, Claude Code | paid | only the files a task needs |
| **Skill** as a ZIP | chat on the web, Claude Desktop | any, with Code execution on | only the files a task needs |
| **Project** | chat on the web, Claude Desktop | any | all twelve files |

The Skill and the plugin open files per task. A Suno prompt needs `CORE_00`,
`CORE_01` and `DATA_SUNO` — about 32 thousand tokens instead of 114 thousand in a
Project.

### Plugin (paid plans)

**Chat, Claude Desktop, Cowork.** **Customize** menu → **Plugins** tab → **Add** →
**Add marketplace** → enter `sanic732/SunoForge` → install **SunoForge**. In Cowork,
open the Cowork tab first, then Customize. Plugins on your account also reach Claude
Code when you sign in with the same account.

**Without GitHub — as a file.** **Customize** → **Plugins** → **Add** → **Upload
plugin** → `sunoforge.plugin` from the release. A plugin added this way does not update
itself: upload the new version again.

**Claude Code:**
```
/plugin marketplace add sanic732/SunoForge
/plugin install sunoforge@sunoforge
```
Call it with `/sunoforge` (or `/sunoforge:sunoforge`), or just describe the task.
Update: `claude plugin update sunoforge@sunoforge`. Auto-update is off by default for
third-party marketplaces; in chat, the **Sync automatically** switch turns it on.

Language is automatic: SunoForge answers in the language you write in.

### Skill as a ZIP

1. **Settings → Capabilities** — turn on Code execution.
2. **Customize → Skills** → **+** → **Create skill** → **Upload a skill** → choose
   `SunoForge_v4.0_Skills_for_Claude.zip`.
3. The Skill switches on by itself when you ask for a music prompt, lyrics or a
   repair. You can also ask directly: "use SunoForge".

Anthropic's help article lists Skills on every plan, Free included; one
documentation page names paid plans only. No Skills section in your settings — use a
Project.

### Project

1. Create a Project.
2. Upload all twelve files from the `claude/` folder to **Project knowledge**.
3. One line of project instructions is enough:
   `Read CORE_00_ENTRY.md first and follow it.`
4. In a project chat, type `start`.

Claude's help: project files up to 30 MB each, no cap on the number, but everything
together must fit the context window. The Claude Edition is about 114 thousand
tokens; a 200K window holds it with room for the conversation.

Without a project: attach the twelve files to the first message (up to 20 files per
chat) and type `start`. The downside: every new chat starts over.

### Commands in the Claude Code terminal

The Claude Code terminal parses lines that start with a slash itself and answers
`/set` with "Unknown command". There, type SunoForge commands without the slash —
`set lang ru`, `menu`, `why front-load` — or after the skill name:
`/sunoforge set lang ru`. The Code tab in Claude Desktop passes such a line on to the
model. The form without the slash works everywhere.
