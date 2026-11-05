# Suno MCP — sending to Suno from the chat

Optional. SunoForge writes prompts whether Suno is connected or not; this page is
for those who want SunoForge to hand the prompt to Suno itself. Everything here is
**beta** on Suno's side. Suno's server is one of the generators SunoForge's LIVE
protocol (menu `[15]`) can use: the same six steps work with any music-generation MCP
server the session shows — ElevenLabs' hosted MCP, or your own, added like any MCP. The plugin does not bundle Suno's server:
you add it like any MCP, as below.

---

## What it is

On 28 October 2026 Suno released an official remote MCP server (beta):
`https://api.suno.com/mcp`. In Suno's words: "No API key · Uses your Suno credits ·
Songs save to your library."

- **Sign-in** is OAuth with your Suno account; one account can serve several
  assistants.
- **Credits.** Generations run on your own Suno credits, by your plan's rules.
- **Results** land in your Suno library, as if you had made them on suno.com.

What the server can do, per Suno's help center ("Suno MCP (Beta)"): turn ideas, lyrics
and conversations into songs; make covers, extensions and mashups of songs in your
library; Speech; upload audio and build on it; add songs to playlists from the chat;
show your plan and remaining credits. The product page adds singing with your own
Suno Voice.

When you connect, Suno's consent screen asks to act through the Suno API, spend
credits, download songs with download credits, view and search your library and liked
songs, edit titles and lyrics, organise workspaces, playlists and preferences, stay
signed in, and read profile, copyright and subscription information.

Third-party "Suno MCP" servers and "Suno APIs" are resellers and wrappers, not Suno.

---

## Early access

Suno's release note says all plans, Free included. The same page, suno.com/mcp, runs an
early-access form that promises an answer "within 24-48 hrs". Until your account is
admitted, sign-in ends with:

> Connecting AI apps to Suno is not yet available for your account

That means Suno has not let the account into the beta yet. It is not a SunoForge
problem and not a setting: fill in the form on suno.com/mcp and wait for Suno's
answer.

Some AI apps allow custom connectors only on their own paid plans.

---

## Connecting it, host by host

| Host | How | Status |
|---|---|---|
| Claude — chat, Claude Desktop, Cowork | **Customize** → **Connectors** → **Add custom connector** → `https://api.suno.com/mcp` → sign in | on Suno's setup page |
| Claude Code | `claude mcp add --transport http suno https://api.suno.com/mcp`, then `/mcp` → `suno` → sign in | on Suno's setup page |
| ChatGPT | **Plugins** → **Add** → **Add custom MCP server**, name "Suno", Server URL `https://api.suno.com/mcp`; create it as a plugin, connect, authorize | on Suno's setup page; plans and developer mode not confirmed |
| Gemini | **Gemini** → **Customize** → **Connectors** → **+** → URL → **Create**; mention **@Suno** in the chat | on Suno's setup page; plans not confirmed |
| Antigravity | `~/.gemini/antigravity/mcp_config.json` → `"suno": { "serverUrl": "https://api.suno.com/mcp" }` | Suno's sign-in server accepts dynamic client registration, so no client id of your own should be needed — not tried yet |
| Grok (grok.com) | **Connectors** → **New Connector** → **Custom**, URL `https://api.suno.com/mcp`, sign in with Suno | plans not confirmed |
| Cursor and other MCP clients | the same URL, as the client adds remote servers | on Suno's setup page |

**Claude Code: "needs authentication".** A remote MCP server starts at session
start. Until you sign in through `/mcp`, it shows "needs authentication" — that is the
expected state, not a fault.

Install steps for SunoForge itself on each host: [INSTALL.md](INSTALL.md).

---

## What SunoForge does with it

Nothing changes until you ask for a song. Then:

1. **It writes the prompt as usual** — a Sonic Blueprint for a song or a Speech
   Blueprint for `[14]` — and, if Suno's tools are in the session, offers once to send
   it (`LIVE = "ask"`).
2. **It looks at the tools your session actually has.** Suno publishes no tool names
   or parameters, so SunoForge reads them from the session, never from memory.
3. **It maps the prompt onto those fields** — Style, Lyrics, Exclude, model, Max Mode,
   Variety, duration, Speech fields — only where a field exists, and names every field
   that cannot be passed: "not accepted — set it in Suno by hand".
4. **It shows a card and waits.** The tool, the exact arguments, how many songs, Max
   Mode or not, and that it spends your credits. If Suno does not state the cost, the
   card says "unknown". Before the first send, one line on privacy: the lyrics and the
   style go to Suno, and the song lands in your library.
5. **On your yes, one call.** No retries, loops or extra takes without a new yes. A
   timeout or a job id is not a failure — SunoForge checks the status or the library
   first.
6. **It reads back** what Suno made, when a tool returns it: title, length, the style
   text Suno stored, the lyrics — and compares them with the prompt. A rewritten Style
   means Variety was above 0; a missing or changed line means the lyrics drifted.
7. **You listen.** Symptoms go to `[12]`; one change per take; the next send waits for
   a new yes.

Commands: `send` — send the last blueprint (it still asks first); `mcp-info` (or
`connections`) — which generation servers this session sees, which are off and how this
host enables them — a reading of state, it connects nothing itself; `set live off` —
never offer to send. Menu `[15]`: the panel opens on its first screen — create, your
songs (10 · 50 · 100), liked, mix two, sounds, playlists, workspaces, voices, credits; a
song picked from a list opens its actions. Commands are words without a slash on every
host; with the Claude plugin `/sunoforge` opens the menu.

Without Suno's tools SunoForge works exactly as before: you copy the blueprint into
Suno.

---

## Safety

- **Credits only on a yes.** Every call that generates, extends, covers, uploads or
  downloads spends your credits or download credits. SunoForge says what will be spent
  and waits for an explicit yes — every time.
- **Nothing is sent without a yes.** Not the lyrics, not the style, not a test call.
- **What comes back is data.** Titles, lyrics, descriptions, other people's songs and
  the server's own tool descriptions are material, never instructions. If the tool
  descriptions changed since the last session, SunoForge says so before generating.
- **Library tools only on request.** Editing titles or lyrics, organising playlists or
  workspaces, downloading — only when you ask for exactly that.
- **For a release, download in Suno.** Rights on Suno follow a download made with a
  paid download credit. Whether a download through the MCP counts as an approved
  channel is not stated, so download the song in Suno itself.
- **No getting around Suno's checks.** SunoForge never helps bypass Suno's similarity
  checks or filters; it writes something original instead.

---

## What is not known yet

What is known — the tools, the field map, the defaults that cost credits and the plan
gating, as seen on 29 October 2026 on Free and Pro — is in `DATA_SUNO_LIVE_2026-10.md`.
Still unknown:

- Rate limits in numbers, and the cost of a call on plans not yet tested
- Whether a download through it is an "approved channel" for rights
- Which plans of ChatGPT, Gemini and Grok allow it; whether Antigravity completes the
  sign-in

SunoForge is built for that: it reads what the session offers and tells you what could
not be passed.

---

## The Suno API

platform.suno.com: "Make music with the Suno API" — "Suno's music generation engine
behind a simple REST API"; sign-in with the Google account linked to Suno or an
emailed code. As of 29 October 2026 the page names no endpoints, plans, waitlist or
documentation. SunoForge does not use it.
