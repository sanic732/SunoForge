# Запуск в Gemini · Running in Gemini

---

## Проверенный способ

Так система запускалась и тестировалась в Gemini. Работает.

**Пять файлов `CORE_*` — по отдельности, как файлы.
Семь файлов `DATA_*` — одним `.zip`.**

```
приложить к чату:
  CORE_00_ENTRY.md          ← точка входа, обязателен
  CORE_01_STYLE.md
  CORE_02_LYRICS.md
  CORE_03_DIAGNOSE.md
  CORE_04_WHY.md

  DATA.zip                  ← внутри семь файлов DATA_*
```

Собрать архив:

```
zip DATA.zip DATA_SUNO_2026-07.md DATA_GOOGLE_2026-07.md \
             DATA_OTHER_2026-07.md DATA_VOCAB.md \
             DATA_RECIPES.md DATA_POSTPROD.md DATA_LEGAL_2026-07.md
```

Затем в чат:

```
старт
```

### Почему именно так

Ядро должно читаться напрямую: `CORE_00_ENTRY` задаёт preloader, меню и
маршрутизацию, и модель обращается к нему постоянно. Слой данных читается
выборочно — под конкретную платформу и задачу, — поэтому архива достаточно, и он
экономит место в списке вложений.

Побочный плюс: обновление слоя данных — это замена одного архива.

### Готовый бот

Если не хотите ничего собирать — всё уже загружено:
[SunoForge v3.0](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing)

### Если делаете свой Gem

- Файлы `CORE_*` — в knowledge Gem'а.
- `DATA.zip` — туда же.
- В инструкции Gem'а достаточно одной строки: читать `CORE_00_ENTRY.md` первым
  и следовать его preloader и маршрутизации.
- Язык объяснений задавайте в самом `CORE_00_ENTRY.md` (`OUTPUT_LANG`), а не в
  инструкции Gem'а — иначе значения разойдутся.

### Замечания

- Контекст Gemini полный комплект держит свободно: 90 767 токенов — около 9 %
  окна в 1M.
- Ленивые файлы (`CORE_04_WHY`, `DATA_LEGAL`) грузить стоит: в Gemini места
  хватает, а `/why` и `/legal` без них не ответят.
- Если Gemini отвечает не на том языке — проверьте `OUTPUT_LANG` в preloader и
  при необходимости скомандуйте `/set lang ru`.

---

## Другие ассистенты

**Claude, ChatGPT** — приложите все двенадцать файлов к чату или добавьте в
проект. Архив не нужен, но и не помешает.

**Grok и любой другой** — если вложения недоступны, вставьте содержимое файлов
первым сообщением, начиная с `CORE_00_ENTRY.md`.

**Окно 128K** — полный комплект займёт 71 %. Не грузите `CORE_04_WHY` и
`DATA_LEGAL` (они и так ленивые), при необходимости оставьте за бортом
`DATA_VOCAB` и `DATA_RECIPES` — это каталоги, нужные не в каждой сессии. Ядро и
адаптер целевой платформы обязательны всегда.

---
---

## The tested arrangement

This is how the system was set up and tested in Gemini. It works.

**The five `CORE_*` files individually, as files.
The seven `DATA_*` files as a single `.zip`.**

```
attach to the chat:
  CORE_00_ENTRY.md          ← entry point, required
  CORE_01_STYLE.md
  CORE_02_LYRICS.md
  CORE_03_DIAGNOSE.md
  CORE_04_WHY.md

  DATA.zip                  ← the seven DATA_* files inside
```

Build the archive:

```
zip DATA.zip DATA_SUNO_2026-07.md DATA_GOOGLE_2026-07.md \
             DATA_OTHER_2026-07.md DATA_VOCAB.md \
             DATA_RECIPES.md DATA_POSTPROD.md DATA_LEGAL_2026-07.md
```

Then, in the chat:

```
start
```

### Why this split

The core needs to be read directly: `CORE_00_ENTRY` carries the preloader, the
menu and the routing, and the model refers back to it constantly. The data layer
is read selectively — for one platform and one task — so an archive is
sufficient, and it keeps the attachment list short.

Side benefit: updating the data layer means swapping one archive.

### Ready-made Gem

If you would rather not assemble anything, it is already loaded:
[SunoForge v3.0](https://gemini.google.com/gem/17bBfa7ucT2IjbKVLxPjz7NRuy8LSixdE?usp=sharing)

### Building your own Gem

- Put the `CORE_*` files in the Gem's knowledge.
- Put `DATA.zip` there too.
- One line of Gem instruction is enough: read `CORE_00_ENTRY.md` first and
  follow its preloader and routing.
- Set the explanation language inside `CORE_00_ENTRY.md` (`OUTPUT_LANG`), not in
  the Gem instructions, or the two will drift apart.

### Notes

- Gemini's context holds the full set comfortably: 90,767 tokens is roughly 9 %
  of a 1M window.
- Do load the lazy files (`CORE_04_WHY`, `DATA_LEGAL`) here — there is room, and
  `/why` and `/legal` cannot answer without them.
- If Gemini replies in the wrong language, check `OUTPUT_LANG` in the preloader
  and issue `/set lang en` if needed.

---

## Other assistants

**Claude, ChatGPT** — attach all twelve files to the chat or add them to a
project. The archive is unnecessary but harmless.

**Grok and anything else** — if attachments are unavailable, paste the file
contents as the first message, starting with `CORE_00_ENTRY.md`.

**128K windows** — the full set takes 71 %. Leave `CORE_04_WHY` and `DATA_LEGAL`
out (they are lazy by default), and consider skipping `DATA_VOCAB` and
`DATA_RECIPES`, which are catalogues not needed in every session. The core and
the adapter for your target platform are always required.
