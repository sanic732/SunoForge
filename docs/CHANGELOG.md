# История версий · Changelog

---

## v4.0 — 2026-09-30

**Why.** Between July and September 2026 Suno retired every model it had and
shipped v6, Google replaced Lyria 3 Pro with Lyria 3.5 and rewrote its prompt
guide, ElevenMusic, MiniMax and Stable Audio all moved. Facts were rechecked
against vendors' own pages (help centres, terms, API docs, a court press release);
every page is kept as text.

**Platforms**
- Suno v6 family (`v6`, `v6-wild`, `v6-mini`); every earlier model retired —
  removed from the menu and settings, recognised by the repair table only
- Suno Max Mode (official switch, not the old tags), Variety slider (0 keeps the
  style text), Duration on v6, plain-language edits, single-line lyric edits,
  multi-source mashup, sampling, image/video/audio references, Studio 2.0
- Suno rights follow the download (terms in force 2026-09-03); download caps per plan
- Lyria 3.5 (`lyria-3.5`), Clip at 44.1 kHz, Lyria 3 Pro retiring; Google's
  2026-09-17 guide: numeric BPM and key, section tags, `Lyrics:` header,
  timestamp ranges, vocal profiles, genre and instrument keyword lists
- ElevenMusic v2.5 — ownership on every plan, commercial use on Free with a credit,
  3 s to 5 min; ElevenLabs' prompting guidance
- Stable Audio 3.0 corrected (6:20 is Medium) and its DAW plugin; MiniMax Music 3.0
  with open weights; ACE-Step 1.5 and YuE2 for local generation
- Legal: GEMA v Suno (Munich, 2026-07-31), the second UMG/Sony suit, Believe/TuneCore,
  UMG v DistroKid, Spotify AI Persona badges, Deezer AI tagging, EU AI Act Art. 50

**System**
- Two editions from one source: Claude Edition (XML) and Gemini Edition (Markdown,
  no XML); one build for every language
- Claude also gets a Skill and a plugin: a short `SKILL.md` router with the twelve
  files as references, opened per task. The repository is the plugin marketplace
  (`/plugin marketplace add sanic732/SunoForge`), and the release carries a Skill ZIP
  for a manual upload to claude.ai; Gemini gets the same Skill built from its Markdown
  files. The release page carries three archives and the plugin:
  `SunoForge_v4.0_Prompt.zip`, `SunoForge_v4.0_Skills_for_Claude.zip`,
  `SunoForge_v4.0_Skills_for_Gemini.zip`, `sunoforge.plugin`
- Menu: `[13] STEMS, STUDIO & MASTERING` added at the tail; new sub-entries
  `2i`–`2k`, `3d`–`3f`, `4d`, `5g`, `6g`–`6h`, `7k`–`7l`; numbers `[1]`–`[12]` unchanged
- Preloader: `SUNO_VERSION` v6 family, `SUNO_PLAN`, `SUNO_MAX_MODE`, `LYRIA_MODEL 3.5`;
  `OUTPUT_LANG` "auto" — answers and the menu follow the language the user writes in,
  and before that the language the host shows;
  `HOST_MODEL` removed, since nothing read it
- No prices anywhere; plans named where features or rights depend on them
- Repair engine: symptom index first, 15 checks, rows 20–25 (retired models,
  Lyria 3 Pro numbers, single-point markers, prices, Variety, Lyria lyrics header);
  row 11 revised — numeric BPM is no longer a defect on Lyria
- CORE_04: why no prices, why rights follow the download, a rule that was wrong
  (Lyria tempo in words), Variety 0
- RAG to the P2P standard: frontmatter with role and description, a system map in
  CORE_00, anchors before every zone, `## TAGS`, zones split, every file under
  50,000 characters; twelve build invariants checked mechanically
- Fixed v3 cross-references (repair table is CORE_03 §3; delivery CORE_02 §6)

## v3.0 — 27 июля 2026

Файлов: 12 (было 10) · 411,9 КБ · 90 767 токенов

### Главное

Три независимые проверки фактов показали, что предыдущие сборки подавали
комьюнити-догадки тоном документации. Четыре центральные «механики» не выдержали
проверки и удалены.

**Убрано, потому что не работает:**

- **MAX MODE** — теги `[Is_MAX_MODE: MAX]`, `(MAX)(MAX)(MAX)(MAX)`. Скрытого
  режима качества нет: контролируемое сравнение не нашло разницы. Если такие теги
  есть в вашем старом промпте — система их распознает, уберёт и объяснит.
- **DRIFT_GUARD** и «деградация после двух минут». Механизм правил каждый ваш
  промпт на основании утверждения, которое никто не проверял. Сами приёмы
  (сильный жанровый якорь, reset на бридже) остались — но как необязательные.
- **Параметрические теги** `[Reverb: 30%]`, `[BPM: 120]`, `[eq: scooped]`,
  `[Mood: Uplifting]`, `[Sound: Rain]`, `[Chord progression: ...]`. Ни одна
  платформа их не читала. Параметры теперь пишутся прозой внутри Style.
- **Лимит Style «200 символов»**. Резал промпт вдвое ниже реально работающего
  диапазона. Что известно о длине на самом деле — в `DATA_SUNO`.

**Добавлено:**

- **Разметка достоверности.** Каждое утверждение о платформе помечено
  `[OFFICIAL]`, `[COMMUNITY]` или `[UNVERIFIED]`. Видно прямо в ответах.
  Переключается флагом `SHOW_CONFIDENCE`.
- **Разделение CORE / DATA.** Правила отдельно, факты отдельно. Обновление —
  это замена одного датированного файла, а не пересборка всего.
- **Два ленивых файла.** `CORE_04_WHY` и `DATA_LEGAL` не грузятся по умолчанию,
  вызываются командами `/why` и `/legal`. Экономия ~12 000 токенов на старте.

### Меню

Номера `[1]`–`[12]` не изменились и больше меняться не будут — на них ссылаются
посты и сторонние гайды.

- `[7j]` — вместо Udio теперь **Stable Audio 3.0**. Ниша та же (инструментал,
  DAW), но выход можно скачать.
- `[12] AUDIT` переработан: 14 проверок промпта и таблица замены мёртвых
  конструкций. Распознаёт MAX MODE, параметрические теги, неверный формат
  таймкодов Lyria, негативы по полу вокала, ссылки на закрытые платформы.

### Preloader

Появились:

```
DURATION         = "auto"     // длина трека (Suno v5.5, веб)
SHOW_CONFIDENCE  = true       // показывать метки достоверности
FOLKLORE_MODE    = "off"      // включить неподтверждённые приёмы
```

Убраны: `DRIFT_GUARD`, `STYLE_MODE`, `FLOW_MUSIC`, `LYRIA_VERSION`
(заменён на `LYRIA_MODEL`).

### Новые команды

```
/why <тема>        почему правило устроено именно так
/legal             права и лицензирование
/free              что можно без оплаты
/compare           выбор платформы под задачу
/audit <промпт>    диагностика и починка
/confidence on|off метки достоверности
/folklore on|off   неподтверждённые приёмы
```

### Платформы

- **Suno** — поле `Exclude Styles` стало настоящим элементом интерфейса (раньше
  подавалось как самодельный приём). Добавлен слайдер длительности. Стемы в трёх
  режимах. Studio 1.2 — **только Premier** (в v1.1 было ошибочно написано «Pro»).
- **Lyria** — таймкоды в официальном формате `[MM:SS]`. Темп задаётся **словами**,
  а не числом — это противоположно Suno, и перенос привычки ухудшает результат.
  Мультимодальный ввод: текст, PDF и до 10 изображений. Негативные промпты не
  поддерживаются вовсе.
- **Flow Music** — прежние ProducerAI и Riffusion. Это один продукт с тремя
  именами, а не три конкурента.
- **ElevenMusic** — смена жанра внутри трека и регенерация отдельных секций.
- **Stable Audio 3.0** — открытые веса, до 6:20, выход принадлежит вам.
- **Udio** — убран из целевых платформ: скачивание отключено. Остался в
  `DATA_LEGAL` как поучительный кейс.
- **MusicFX и MusicFX DJ** — закрываются 31.07.2026, из рекомендаций убраны.

### Работа с лирикой

Веб-редактор Suno теперь сам расставляет структурные метки. Описаны **два пути**:
чистый текст для веба и ручная разметка для API, мобильного приложения и вставки.
Разметка руками поверх редактора даёт две накладывающиеся структуры.

### Совместимость

Старые промпты продолжают работать. Часть их содержимого — нет. Вставьте
промпт в `/audit`, и система покажет, что в нём мертво, и выдаст исправленную
версию.

---

## v2.0 — 13 мая 2026

Файлов: 10 · русская · **на GitHub не выкладывалась**.

📎 Промежуточная версия, доступна только на форуме:
[4PDA — SunoForge v2.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142556185)

- Шестислойное построение Style вместо формулы GMIV+P.
- Мультиплатформенность: добавлены Flow Music, ElevenMusic, Udio, Lyria Realtime.
- Новый файл `06_PLATFORMS` вместо `06_GEMINI`, дерево выбора платформы.
- YAML-frontmatter и семантические зоны во всех файлах.
- Гибриды 2026: Amapiano, Drift Phonk, Hyperpop, Lo-fi Trap.

⚠️ Часть введённого в v2.0 не подтвердилась при проверке и удалена в v3.0 —
см. раздел выше.

---

## v1.1 — март 2026

Файлов: 10 · опубликована на GitHub, английская.

- Формула Style GMIV+P, Time & Place, мастерская персон, гибридная лаборатория.
- Clean Block Protocol, дуэтный протокол, словарь звука, рецепты жанров.
- Поддержка Suno и Gemini.

---
---

# Version history

---

## v3.0 — 27 July 2026

12 files (was 10) · 411.9 KB · 90,767 tokens

### Headline

Three independent fact-checking passes established that previous editions had
been presenting community folklore in the voice of documentation. Four central
"mechanics" did not survive and have been removed.

**Removed because it does not work:**

- **MAX MODE** — `[Is_MAX_MODE: MAX]`, `(MAX)(MAX)(MAX)(MAX)`. There is no
  hidden quality mode; controlled comparison found no difference. If your old
  prompt contains these, the system will recognise them, strip them and explain.
- **DRIFT_GUARD** and "degradation after two minutes". The mechanism modified
  every prompt you wrote on the basis of a claim nobody had tested. The
  underlying techniques remain available — as optional.
- **Parametric tags** `[Reverb: 30%]`, `[BPM: 120]`, `[eq: scooped]`,
  `[Mood: Uplifting]`, `[Sound: Rain]`, `[Chord progression: ...]`. No covered
  platform ever read them. Parameters are now written as prose inside Style.
- **The "200 character" Style limit.** It cut prompts to a fraction of the
  working range. What is actually known about length is in `DATA_SUNO`.

**Added:**

- **Confidence marking.** Every platform claim is tagged `[OFFICIAL]`,
  `[COMMUNITY]` or `[UNVERIFIED]`, visible in output. Toggled with
  `SHOW_CONFIDENCE`.
- **A CORE / DATA split.** Rules and facts in separate files. Updating means
  replacing one dated file rather than rebuilding the system.
- **Two lazy files.** `CORE_04_WHY` and `DATA_LEGAL` are not loaded by default;
  they are reached with `/why` and `/legal`. Saves ~12,000 tokens at startup.

### Menu

Entries `[1]`–`[12]` are unchanged and are now frozen — forum posts and
third-party guides reference them.

- `[7j]` is now **Stable Audio 3.0** instead of Udio. Same niche (instrumental,
  DAW), except you can download the result.
- `[12] AUDIT` rebuilt: 14 prompt checks plus a replacement table for dead
  constructs. Detects MAX MODE remnants, parametric tags, the wrong Lyria
  timestamp syntax, vocal-gender negatives, and references to retired platforms.

### Preloader

New:

```
DURATION         = "auto"     // track length (Suno v5.5, web)
SHOW_CONFIDENCE  = true       // show reliability marks
FOLKLORE_MODE    = "off"      // allow unproven techniques
```

Removed: `DRIFT_GUARD`, `STYLE_MODE`, `FLOW_MUSIC`, `LYRIA_VERSION`
(replaced by `LYRIA_MODEL`).

### New commands

```
/why <topic>        why a rule exists
/legal              rights and licensing
/free               what you can do without paying
/compare            pick a platform for the task
/audit <prompt>     diagnose and repair
/confidence on|off  reliability marks
/folklore on|off    unproven techniques
```

### Platforms

- **Suno** — `Exclude Styles` is a real interface field now, not a homemade
  technique. Duration slider added. Stem separation in three modes. Studio 1.2
  is **Premier only** (v1.1 said "Pro", which was wrong).
- **Lyria** — timestamps in the official `[MM:SS]` format. Tempo is given in
  **words**, not numbers — the opposite of Suno, and carrying the habit across
  makes results worse. Multimodal input: text, PDF and up to 10 images.
  Negative prompting is not supported at all.
- **Flow Music** — formerly ProducerAI and Riffusion. One product with three
  names, not three competitors.
- **ElevenMusic** — mid-track genre switching and per-section regeneration.
- **Stable Audio 3.0** — open weights, up to 6:20, you own the output.
- **Udio** — dropped as a target: downloads are disabled. Retained in
  `DATA_LEGAL` as a cautionary case.
- **MusicFX and MusicFX DJ** — retiring 31 July 2026, removed from recommendations.

### Lyrics

Suno's web editor now places section labels itself. **Two paths** are documented:
clean lyrics for the web editor, manual markup for the API, mobile and pasting.
Marking up by hand on top of the editor produces two overlapping structures.

### Compatibility

Old prompts still run. Some of what they contain no longer does. Paste one into
`/audit` and the system will show what is dead in it and return a repaired
version.

---

## v2.0 — 13 May 2026

10 files · Russian · **never released on GitHub**.

📎 An interim version, available on the forum only:
[4PDA — SunoForge v2.0](https://4pda.to/forum/index.php?showtopic=1109539&view=findpost&p=142556185)

- Six-layer Style construction replacing the GMIV+P formula.
- Multi-platform: Flow Music, ElevenMusic, Udio, Lyria Realtime added.
- New `06_PLATFORMS` file replacing `06_GEMINI`, plus a platform decision tree.
- YAML frontmatter and semantic zones across all files.
- 2026 hybrids: Amapiano, Drift Phonk, Hyperpop, Lo-fi Trap.

⚠️ Some of what v2.0 introduced did not survive fact-checking and was removed in
v3.0 — see above.

---

## v1.1 — March 2026

10 files · published on GitHub, in English.

- The GMIV+P Style formula, Time & Place, persona workshop, hybrid lab.
- Clean Block Protocol, duet protocol, sound vocabulary, genre recipes.
- Suno and Gemini support.
