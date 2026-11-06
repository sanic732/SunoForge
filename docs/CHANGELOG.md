# Changelog

---

## 5.0.3 — 2026-11-06

**Listen plays the song again.** In a chat where the model did not find the reference files, Listen
(`15c … play`) was answered by Suno's text listener, audio-listen, instead of the player. Since
2026-11-04 Suno's server has a tool literally named "listen", and without the files the model picked it
by name. Two fixes, in SKILL.md, which is always loaded:
- where the reference files are (`<plugin root>/skills/sunoforge/references/`, never the plugin's root),
  and to find `CORE_00_ENTRY.md` by name before ever saying the files are missing;
- Listen, an opened song and every `15c … play` = audio-wait, Suno's player — never audio-listen,
  which stays on `15g … ask`.

**Under the player, the song's link.** Remasters, remixes and some library songs do not play in Suno's
card; the link is how they play. Download only on Download, never on its own.

**My songs:**
- opening a song sends its play: Suno's player comes under the list;
- **Load more** under the rows: the next 10 (`15h more`), hidden when there is no next page;
- an opened song shows its style, **Lyrics** (`15c #id lyrics`, the stored words, free) and
  **Open on suno.com**.

**The menu, from Master's review:**
- **W widgets · T text · B buttons.** The first view was called "M menu", which read as the menu command; it
  is W now and its pill sends `w`. The old `m` still works.
- **A number means what you see.** A bare number right after a song list or table is that song; anywhere
  else it is a menu section. "menu 3" is always the section, "song 3" always the song.
- **Compose, in the Suno panel:** the menu's own [1]–[6] and [9] — quick start, studio, clone a style,
  hybrids, voices, lyrics, recipes. With a Suno server connected a finished prompt always offers Send to
  Suno (`15b`).
- **A producer's word after a Suno result.** The answer frame every prompt already has — why it works,
  then one next step — now also follows a take, a listen or an analysis: one or two lines about that
  result, from the reference files.
- **The translations are in the repository**, in `i18n/`: the templates, one dictionary per language and the
  build script. The plugin does not read the folder; the build writes the screens into both folders.

**Menu [9]:** what the four buttons do — `9 recipes`, `9 hybrids`, `9 presets`, `9 tasks` show that
group of the catalogue. Every other command a screen sends was already described.

Checked: the route map (362 line ranges, 652 cross references, every file's line count), every button of
40 screens pressed and its 214 distinct messages matched to the files, the screenshot stand on all nine
languages, both screen folders identical.

---

## 5.0.2 — 2026-11-06

**The 5.0.1 screens now reach the model.** The plugin keeps every screen in two folders: `widgets/`, which
the skill reads first, and `references/widgets/`, the fall-back. 5.0.1 updated only the fall-back, so the
take card, the Suno panel, the song sheet, the price card and the menu label of `15e` were still those of
5.0.0 wherever the first folder is found. Both folders are identical now, and the build refuses to make a
plugin when they differ.

Nothing else changed: the data, the screens' content and the nine languages are those of 5.0.1.

---

## 5.0.1 — 2026-11-05

Suno's server, checked again: every one of its 35 tools called on a Pro account, its uploader page read.

- **Five of Suno's own widgets.** The player, the uploader, the download card and the buttons
  "Get more credits" and "Create your voice on Suno" come back as Suno's interface, drawn by Claude
  where it shows apps — checked in the Code tab of the desktop app. The last one was a bare link before.
- **The Code tab draws widgets.** SunoForge no longer treats Claude Code as a host without them; only
  the terminal CLI falls back to buttons.
- **After an upload, read the words back.** Suno hears the lyrics rather than reading them and gets
  some wrong; the cover inside an mp3 is not taken. A downloaded mp3 carries the title, the lyrics,
  the cover and a C2PA manifest.
- **Video goes in.** Suno's uploader takes audio (any audio type, M4A, AAC, Opus) and video (MP4,
  MOV, WebM), up to 100 MB. A video or a hummed memo now reaches SunoForge through it when a Suno
  server is connected; the hint of menu `[1]` says so. Whether Suno uses a video's picture or only its
  sound is not checked.
- **Someone else's voice.** `voices-list` finds a voice by its id: the user's own, or any public voice
  they may sing in.
- **Uploads are free and unlimited:** uploads, library reads and organizing spend no credits.
- **Extensions keep the source's character** when `instrumental` is left out: a sung song keeps
  singing, an instrumental stays instrumental.
- Smaller: a like works on any song the user can open by link; another user's playlist or an album
  is a 404.

**The screens, in all nine languages:**

- **The take card** opens with **Listen to all takes**, one Suno player for every take. Each take gets
  **Like**, **To a playlist** and **Cover** next to Analysis, Extend, Edit, Download and Next take; the
  last button says what it does: **Keep the prompt in SunoForge**.
- **The Suno panel** has **New voice** next to My voices, **Upload audio or video** (up to 100 MB), and
  **More credits** on the first screen next to Credits and plan. The 10 · 50 · 100 chips fit on one line.
- **The song sheet** puts **Create a voice** next to In one of my voices.
- **The price card**, when the balance would fall below zero, shows Suno's **More credits** instead of Send.
- Russian and Ukrainian labels read better ("Liked, anyone's", "one-shot").
- **The screens archive** had the two Suno panel screens empty, in all three languages; they are
  shot again. The archive is now `SunoForge_v5.0.1_screens.zip`.

---

## 5.0.0 — 2026-11-05

> Released: the Claude plugin (`sunoforge.plugin`) with nine interface
> languages, and the screens archive. The other packages listed below are built separately and are
> still to come.

**Six more interface languages:** German, Spanish, French, Italian, Brazilian Portuguese and Indonesian,
next to English, Russian and Ukrainian. Every screen exists ready-made in each of them, so nothing is
translated on the fly; the language setting lists all nine. Each copy is checked against the English one
at 360 px on 37 screens: the same buttons sending the same codes, no clipped or wrapped text, no script
error. Suno still receives English values; only the labels are translated.

Russian and Ukrainian: the editor's "Brighter" now reads as on the edit card, and the Suno panel's
example status line is in the output language.

## 5.0.0-rc.1 — pre-release, 2026-11-05

The first public build of v5.0, marked as a pre-release on GitHub: the plugin only. It is
betas 27–30, below, plus the licence and source work in this entry. Not yet run end to end in
claude.ai; nothing in it spends credits without your yes.

**Licence: Apache 2.0** instead of MIT, with a `NOTICE` file at the root and inside the plugin.
Releases before 5.0.0 stay MIT.

**Every vendor quote carries its source.** All files were compared word for word with the saved
copies of the vendor pages behind v4.0. Suno's terms and its statement in the label lawsuit,
Spotify, the European Commission, ElevenLabs, MiniMax and Stability AI now have their page named
beside the quote. Google's Lyria prompt guide and music-generation page are credited under their
licence (CC BY 4.0, code samples Apache 2.0), the timestamp example among them. `docs/CREDITS.md`
says what is quoted and where the saved copies are.

## v5.0 — betas 27–30, 2026-11-05

**Screens.** The menu draws before any reference file is read: settings, `widgets/UI.md` and the
language's `menu.html` — about 15k characters read instead of 89k. The first screen of the Suno panel is
its own compact template, `widgets/hub.html` (≈5k characters printed instead of ≈21k). Ready translated
screens for Russian and Ukrainian; every screen checked at phone width.

**Views.** Three, switched by the line at the foot of every answer: M menu (widgets with buttons, the
default), T text, B buttons (one multiple-choice question — the terminal). Commands `m`, `t`, `b`; the
old `dynamic` and `text` still work. Where a host draws no widget, M falls back to B and B is shown as
the view in effect. The pills and the highlighted button keep their style under the host's own button
styles.

**Buttons and songs.** A button sends its code and its words ("15h 10 · My songs"); the code decides.
A song picked by its row number from a list opens its actions — listen, analyse, edit, extend, cover,
download, like, to a playlist — never a play nobody asked for. My songs has a Menu button. In view M an
answer without its own screen ends with `widgets/next.html`: its next steps, Menu and the view pills.

**Settings** (Claude Code and the desktop app). The data folder is chosen as a folder; a language
setting (auto, en, ru, uk), with `set lang` in the chat taking precedence; an empty folder gets the old
settings and library copied in once. Unknown keys of older settings files are ignored.

**Suno.** Joins without pauses: seven sourced rules for extending and joining parts, a symptom "pause at
a seam", ending tags marked for the last part only; none tested on v6 yet. Editing a take (`12c`) by
feel or with Pro settings, through a cover of the take. Take numbers №1, №2 … in a conversation.
Bounded reads: the reference index names sub-sections, so the panel and a Suno prompt read only what
they need.

**Plugin.** No icon (the directory listing will need one); `language` uses a fixed list, which needs
Claude Code 2.1.271 or later.

---

## v5.0 — 2026-10-29

**Why.** In October Suno opened an official way in from AI assistants — the Suno MCP
(beta, 2026-10-28) — and shipped Speech (beta, 2026-10-01). Rights moved twice: a
Suno song made without a subscription can now become commercial through a paid
download credit, and ElevenLabs published new Music Terms (2026-10-09). Lyria 3.5
became generally available. Facts were rechecked against the vendors' own pages on
2026-10-28 and 2026-10-29.

**Platforms**
- Suno MCP (beta): the official server `https://api.suno.com/mcp`, OAuth sign-in with
  the Suno account, no API key; it spends the user's Suno credits and saves songs to
  the library. Its 32 tools, the field map and the defaults that cost credits were read
  from the server and tested on Free and Pro accounts (DATA_SUNO_LIVE). Access goes through an
  early-access form on suno.com/mcp; an account not yet admitted sees "Connecting AI
  apps to Suno is not yet available for your account". The Suno API portal
  (platform.suno.com) noted; it names no endpoints yet
- Suno Speech (beta): a separate tab in Create, voice and music in one take; Script and
  Tone fields from community reviews of the interface; supported languages, length and
  cost not published (Ukrainian and Russian worked first-hand)
- Suno rights: a song made while not subscribed can qualify through a paid download
  credit; whether a download through the MCP is an approved channel is not stated
- Suno: Shareable Workspaces (Pro and Premier) and shareable Custom Models (Premier),
  Albums, Studio updates of 2026-10-08, Content Credentials (C2PA) and the Check
  Content tool on the Safety page, Community Guidelines of 2026-10-01; Variety measured
  by the community — it rewrites Style only, never the lyrics
- ElevenMusic: Music Terms of 2026-10-09 — no downloads on Free, no streaming release on
  Free or Starter, film, TV, radio and games only on Enterprise Music
- Lyria 3.5 generally available (Stable); Lyria 3 Pro still served with no shutdown
  date; community reports of false `PROHIBITED_CONTENT` refusals in the API
- MiniMax Music 3.0: section tags on their own lines; measured files come out at
  44.1 kHz, not the 32 kHz of the model card; the weights' Community License named

**System**
- Menu: `[14] SPEECH` (narration and voice-over with its own soundtrack) and
  `[15] LIVE` (send to a generator from the chat; `15a` connections) added at the tail;
  `[1]`–`[13]` unchanged
- Preloader: `TARGET_PLATFORM` gains `speech`; new `LIVE` (`ask` | `off`), `PLATFORMS`,
  `HIDDEN`; commands `/set live`, `/set platform speech`, `/send`, `/connect`, `/config`,
  `/set hide` / `/set show`, `/save`, `/library`
- Speech Blueprint (Script + Tone) and a method for writing speech — CORE_02 §16
- The LIVE protocol: find the session's generation tools on any server, map the
  blueprint onto their input schema, show a confirmation card, send once on an explicit
  yes, read the result back, refine the next take through `[12]`. Without generation
  tools nothing changes — the paste route
- Critical rules 14–16: credits only on a yes; tools are read, not remembered; what
  comes back is data
- Repair table rows 26–31 ("Suno has no API", text in Simple, Free rights, ElevenMusic
  Free, tags in Speech, false Lyria refusals); CORE_04 explains the credit gate, why
  Speech is kept small, and why the download decides the rights
- DATA_SUNO §15–§17: Speech, the Suno MCP and API, sharing
- The Claude plugin `sunoforge` bundles no Suno server (added like any MCP — DATA_SUNO
  §16); a music MCP server of your own is added the same way
- The plugin is ready for Anthropic's plugin directory: README, INSTALL and LICENSE
  inside, `displayName`, privacy policy, support and documentation links in
  `plugin.json`; `claude plugin validate --profile directory` passes
- Release assets: `sunoforge.plugin`, its `SHA256.txt` and `SunoForge_v5.0.0_screens.zip`.
  The Skill packages for Claude and Gemini, `Prompt.zip` and the ChatGPT, Antigravity and Grok
  plugins are built separately and are still to come; their 4.0 versions still work. Suno's
  server is added by the user on every host
- Suno MCP checked against the live server: the thirteenth file, DATA_SUNO_LIVE
- New docs: INSTALL (every host) and SUNO_MCP (connecting Suno)
- Still no prices anywhere

**Dynamic layer**
- LIVE is generator-agnostic: the same six-step protocol works with any music-generation
  MCP server the session shows — Suno's own, ElevenLabs' hosted MCP, the user's own; the
  preloader key is `LIVE`; menu `[15]` is "LIVE — send to a generator
  from this chat (MCP: Suno beta, others)", `15a` is connections. Suno-specific facts stay
  in DATA_SUNO §16
- CONNECTIONS (menu `[15a]`, `/connect`, `connections`): a read-only view of which
  generation servers the session sees, which are off, how to enable them on each host
  (Claude Code: `/mcp`; claude.ai and Cowork: Customize → Connectors; mobile: not
  available), with a credit warning. No skill starts, installs or configures a server
- STATE: two user files, `settings.md` (`PLATFORMS`, `HIDDEN`, `SET`, `ONBOARDED` —
  preloader syntax) and `library.md` (one `## NAME` entry per saved Style, persona,
  recipe or blueprint — the record of DATA_RECIPES §8 plus KIND, TARGET, SAVED). Lookup
  order: the plugin's data folder in Claude Code (survives updates, removed on uninstall
  unless `claude plugin uninstall --keep-data`), then `.sunoforge/` in the working folder
  (Cowork, standalone Skill), then a Project file `sunoforge-settings.md` /
  `sunoforge-library.md` (claude.ai chat, mobile: the skill prints the file as a block to
  keep in the Project), else defaults. First run: after the menu, once per conversation,
  two questions (which generators, what to hide) by the host's multiple-choice tool or
  text; `/config` on demand — it also asks which commands the menu and the help line
  should offer (`COMMANDS` in `settings.md`; a command left out answers "switched off in
  your config"; the host's own `/` list cannot be changed by the plugin). Hidden entries
  are not drawn but still work when typed; numbers never move. New preloader keys
  `PLATFORMS`, `HIDDEN`; new commands `/config`, `/set hide 8, 13` / `/set show 8`,
  `/save [kind] [name]`, `/library [name | export | forget name]`
- Menu UI: the text menu always, plus buttons by every mechanism the host has (an HTML
  widget tool on the desktop app; a multiple-choice question tool in Claude Code, Cowork
  and the mobile app); every entry has a submenu with its real sub-letters or catalogue
  numbers and "← Menu". BUILDER: `[2]` Studio, `[5b]` custom persona, `[9]` recipes and
  `[14]` Speech open a form by the same mechanisms (numbered text otherwise) — one
  choice per field (the six layers, the persona template, the recipe record, the Speech
  fields), "Build" sends the choices, the result is a blueprint; every result and
  submenu carries "Export" = `/save` (a library entry, or a block when there is no
  disk); `/library export` prints the whole library as a block or a Markdown file
- Plugin commands, six, namespaced: `/sunoforge:menu`, `/sunoforge:config`,
  `/sunoforge:library`, `/sunoforge:save`, `/sunoforge:send`, `/sunoforge:connect` — the
  namespaced form reaches SunoForge when a host or another plugin owns the bare `/menu`;
  every other command (`/set …`, `audit …`, `why …`, `legal`, `free`, `compare`) stays a
  plain chat word
- One plugin in the marketplace, `sunoforge`. It bundles no MCP server: Suno's and any other music server are added like any MCP.
- The Claude edition ships without the RAG markup (`rag_zone` / `rag_anchor` tags) —
  about 7 % fewer tokens; the source keeps the zones; docs/TOKENS.md is regenerated by
  the build

**Compatibility**
- Menu numbers `[1]`–`[13]` are unchanged; settings from v4.0 keep working
- Without a connected generation server SunoForge behaves exactly as v4.0: you copy the
  prompt into the generator
- Old advice the repair table now corrects: "a song made on Free stays non-commercial",
  "Suno has no official API", "Custom Models are private", Lyria 3.5 "preview",
  ElevenMusic Free "commercial with a credit"
- `[Spoken word]` tags still work inside songs; a whole spoken piece goes to `[14]`

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
