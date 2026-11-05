# Licence, sources and notices

---

## Licence

**Apache 2.0**, from 5.0.0 on. © 2026 Sanic (`sanic732`). Full text in `LICENSE`,
notices in `NOTICE`, both at the root and inside the plugin.

Free to use, modify, redistribute and apply commercially. Keep `LICENSE` and
`NOTICE` with any copy, and mark the files you changed.

Releases before 5.0.0 (v1.1, v3.0, v4.0) were published under MIT; copies obtained
under MIT stay under MIT.

The licence covers **the system itself** — the text of the instructions. It says
nothing about rights in the music you produce with it: those are set by the
terms of whichever platform you generate on. See
`DATA_LEGAL_2026-10.md` (in `claude/` and `gemini/`), or the `/legal` command.

---

## No third-party code ships here

SunoForge is a body of text instructions. The distribution contains no
libraries and no borrowed source code. Its screens (`widgets/`) are the
author's own HTML.

## Quoted material

SunoForge does quote third-party text: short passages from vendors' terms,
documentation and announcements, so that every rule about a platform can be
checked against its source. Each quote is marked (`[OFFICIAL]`, `[COMMUNITY]`)
and its source is named next to it. Quotes stay their owners' and are not
covered by SunoForge's licence.

- **Google** — the Lyria prompt guide and "Generate music with Lyria" on
  ai.google.dev. Their text is licensed under Creative Commons Attribution 4.0
  and their code samples under Apache 2.0; `DATA_GOOGLE` uses lists, example
  prompts and sentences from them word for word or shortened, credited at the
  top of that file.
- **Suno, ElevenLabs, MiniMax, Stability AI, Spotify, Believe, the European
  Commission, Variety, Music Business Worldwide** — short quotes, each with its
  page named beside it.

Checked on 2026-11-05: every file was compared word for word with the saved
copies of the v4.0 source pages (below). Each run of twelve or more words that
matches one of them sits inside a sourced block.

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
  8 April 2026, by Katie Nguyen and Hussain Chinoy. The first vendor-written
  prompting document this system used (v3.0). Used as a source of fact; its
  wording is not reproduced — checked on 2026-11-05 against the saved copy: no
  run of eight words in common.
- **Google's Lyria prompt guide** (ai.google.dev, edition of 2026-09-17) and
  **ElevenLabs' music best practices** — the vendor prompting documents of
  v4.0 and later; quoted with their sources (see Quoted material).
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
29 October 2026. This field changes monthly. A quarter later, treat every figure
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

---

## Sources for v4.0 (checked 2026-09-30)

Primary pages read directly on 2026-09-30. The author keeps private copies of them
(the page and its extracted text, 38 pages) to re-check quotes; they are not
distributed, and no v3.0 or v4.0 package contained them. The same holds for the
saved copy of the Google Cloud Blog guide used in v3.0:
- Suno — help center: v6 FAQ, Current Models, What's new in v6, How long will my song be,
  How to change models, Stem separation, Custom Models, Voices FAQ, Creating a Voice,
  Download limits FAQ; suno.com/pricing; suno.com/release-notes; suno.com/blog/introducing-v6;
  suno.com/blog/suno-updates-tos; suno.com/terms-of-service (revised 2026-08-10, effective 2026-09-03)
- Google — ai.google.dev: Generate music with Lyria 3.5 (updated 2026-09-23), Lyria prompt guide
  (2026-09-17), Real-time music generation, Pricing; gemini.google/overview/music-generation;
  blog.google: Lyria 3.5 in Flow Music (2026-07-29), Lyria 3.5 in Gemini (2026-09-04);
  flowmusic.app/pricing; Gemini Apps help: upload files
- ElevenLabs — Music v2.5 announcement (2026-09-11), ElevenMusic blog, Music overview,
  Best practices, ElevenCreative Music, API pricing
- Stability AI — Stable Audio 3.0 (2026-05-20), new ways to work with Stable Audio (2026-08-18)
- MiniMax — Music 3.0 (2026-08-13); ACE-Step 1.5 and YuE2 READMEs
- Landgericht München I press release, Az. 42 O 763/25 (2026-07-31); Spotify newsroom
  (2026-08-11); Deezer newsroom (2026-07-21); European Commission, Code of Practice on
  marking and labelling AI-generated content; Believe press release (2026-09-08)
- Trade press used as [COMMUNITY]: Variety, Music Business Worldwide, Music Ally,
  Digital Music News, Billboard (via secondary)
- Claude Help Center (Upload files) via the local documentation mirror

Research prompts and reports: three Deep Research passes (Suno A+B; Google, other
platforms, hosts C–E; music generation from Claude Code), then checked against the
primary pages above. One report claim (an attribution requirement on Suno's Free plan)
was refuted by the current terms and not used.

---

## Sources for v5.0 (checked 2026-10-28 and 2026-10-29)

Primary pages read directly; no copies were kept, only notes:
- Suno — suno.com/mcp (the Suno MCP page, setup per host, early-access form); help
  center, category "Suno MCP (Beta)"; suno.com/release-notes (Speech 2026-10-01, Albums
  2026-10-05, Studio 2026-10-08, Collaboration 2026-10-15, iOS 2026-10-23, Suno MCP
  2026-10-28); suno.com/safety (Content Credentials, Check Content, Community
  Guidelines); platform.suno.com (the Suno API portal, checked 2026-10-29); help center,
  "Can I monetize a Remix?" (songs made while not subscribed and paid download credits,
  checked 2026-10-29)
- ElevenLabs — elevenlabs.io/music-terms (Music Terms of 2026-10-09, checked 2026-10-29)
- Google — ai.google.dev: Gemini API changelog (Lyria 3.5 generally available) and
  Deprecations (Lyria 3 Pro, checked 2026-10-29)

Used as `[COMMUNITY]`:
- HookGenius, Suno v6 guide (Variety measurements, Max Mode notes)

