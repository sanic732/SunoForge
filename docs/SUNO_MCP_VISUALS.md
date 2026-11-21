# Suno's MCP server — the image and video tools (Visuals)

An inventory, as of 20 November 2026.

Suno publishes no full list of its server's tools and changes the server without notice. This page is first-hand: the
tools as the session of a Pro account showed them on 19 and 20 November 2026, with every free read called and two paid
calls made on the author's own credits — an image on image-1 (1 credit) and a five-second clip on video-1 over a
window of a song (75 credits). What was not called is taken from the server's own tool descriptions and marked so.

The 41 song tools of the same server are in SunoForge's reference:
[`DATA_SUNO_LIVE_2026-10.md`](../plugin/skills/sunoforge/references/DATA_SUNO_LIVE_2026-10.md) §10. How SunoForge
works with a Suno server: [SUNO_MCP.md](SUNO_MCP.md).

## How to read the last column

- **call** — called on 19–20 November 2026 and its answer read (free reads only);
- **paid call** — run on 20 November 2026, the balance read before and after;
- **description** — the server's own tool description, not called: every other paid tool and every free write (a free
  write still changes the account).

Plan facts are from one account, Pro. The server is a beta: re-read the tool schemas before relying on a row.

## Access, balance, prices

Access: a suno.com token with the `visuals` grant, otherwise every tool answers 404. Cost: the Visuals balance (`visuals_credits_remaining`
in account-usage), separate from song credits and not sold by account-upgrade; Pro accounts got a starter grant at
launch (Suno's email, 2026-11-19). Prices from visuals-models, 2026-11-20 [call]: images per generation, two takes —
image-1 Fast 1, image-2 Standard 25, image-4 Max 50 (the default); video per second — video-1 Fast 480p 15,
video-2 Standard 720p 30 (the default); clips 5–15 s; aspects 1:1, 9:16, 16:9. Every paid tool takes `dry_run: true`,
which prices the exact request and starts nothing — on 2026-11-20 its quote matched the charge (image-1: quoted 1,
charged 1). New ids are `gen_…` (a generation) and `ast_…` (an asset); every tool takes them.

## The 18 tools

A Claude session showed 18; Gemini's connector, synced 2026-11-20, listed a 19th — `visuals-upload-consent`, the row
before the last.

| Tool | Does | Cost | Fields (required in bold) | Returns | Trap | Check |
|---|---|---|---|---|---|---|
| image-create | images from a prompt; a keyframe for a clip or a Sequence shot | 1 / 25 / 50 per generation | **prompt**, aspect, model, sequence_id + shot_id, dry_run, idempotency_key | `gen_…` id, `status: processing`, two take labels, `visuals_credits_remaining` (224 after one image-1 call) → visuals-wait | moderation 400 `prompt_refused`: revise once, only for a named artist or person; 429 `moderation_limited` = stop. 1:1 came back 1024×1024 | paid call: image-1, 1 credit, two takes |
| video-create | a 5–15 s clip, from a prompt or a first (and last) frame; for a window of a song (`song_id`, `song_start_s`) | 15 or 30 a second | **prompt**, duration_s, aspect, model, resolution, first_frame_asset_id, last_frame_asset_id, song_id, song_start_s, lip_sync, sequence_id + shot_id, dry_run, idempotency_key | `gen_…` id, `status: processing`, two take labels, `visuals_credits_remaining`; ready: two 5.17 s clips, 480×480 at 1:1 on video-1 | lip sync not guaranteed; `song_unavailable` 404, `song_not_ready` 409. The price is for both takes together, per second: `dry_run` quoted 75 for video-1 5 s and 150 for video-2 5 s, the same with or without `song_id`; the charge was the quote (224 → 149). A published song's clip downloaded as MP4 at once, no `clip_not_unlocked` | paid call: video-1, 5 s, a first frame and a window of a song, 75 credits |
| video-assemble | ready clips and stills cut over a song into an MP4 | free render | **song_id**, **clips** (≤40; a still needs duration_s ≤60), song_start_s, aspect, lyrics, idempotency_key | a render id → visuals-wait → visuals-download | a clip still being made is 400 | description |
| sequence-create | a music video as a timeline of shots over a song, with style, characters and sets | free | **shots** (≤200, each ≤15 s; plan ≤40), song_id, song_start_s, style (JSON, ≤32 KB with the rest), characters and sets (≤12 each, 1–3 images), aspect, title, lyrics, idempotency_key | the Sequence, `editor_url` | ask the user for the look, who is on screen and whether anyone sings before creating | description |
| sequence-generate | keyframes or clips for up to 8 shots at once | as the single tools | **id**, **step** (keyframes, clips), **shots** (shot_id, prompt, frames, continues / leads into), model, resolution, aspect, dry_run, idempotency_key | per shot: started, rate_limited, moderation_limited, refused, unknown | about 10 creates a minute; price a large batch with `dry_run` first | description |
| sequence-get | a Sequence as it stands | free | **id**, view (full, summary) | shots with status, takes, labels | edits made on suno.com show here | description |
| sequence-list | the user's Sequences | free | cursor, limit ≤20, query | titles, lengths | a filtered page can be empty and still have a cursor | call (none yet) |
| sequence-update | edit style, cast, sets, shots, timeline (move, delete, trim, split, add) | free write | **id**, style, characters, sets, shots, ops (≤49), view, idempotency_key | the Sequence or the changed shots | all or nothing; shots after an op move | description |
| sequence-export | the Sequence as an MP4 | free render | **id** | a render id | a shot being made, or failed, is 409 | description |
| characters-list | saved characters; with `presets` Suno's preset characters and backgrounds | free | presets | own characters; presets as `preset:<id>` refs | — | call: none saved; 25 preset characters, 39 preset backgrounds |
| characters-save | an image saved as a character | free write | **id** | — | a video is 400 | description |
| visuals-library | the user's images and videos, newest first | free | cursor, limit ≤50, media_type, liked, sequence_id, song_id | generations with their assets | items with `lgen_…` / `lasset_…` ids (seen on images of 2026-11-06, listed without prompt or model) are refused as "bad id" by visuals-show, -wait and -download, with or without the prefix; new `gen_…` / `ast_…` items carry prompt, model and size and work everywhere | call |
| visuals-show | images, video frames or presets as pictures in the chat | free | ids (≤10) or one video + at | display JPEGs (≤1568 px) | each image adds to the conversation: show only what was asked | call: a preset, an `ast_` image and an `ast_` video (one sheet of 4 frames at 1.29–5.17 s) worked; an `lasset_` id was refused |
| visuals-wait | wait for generations and renders | free | **ids** (≤8), view | jobs with assets, labels | `unread` = rate-limited this time, ask again | call: a `gen_` id came back `done` with both takes (asset id, size, label, suno_url); an `lgen_` id refused |
| visuals-download | a signed URL for an image or video | free | **id** | `url` (a button) | a music video of a song not unlocked: 403 `clip_not_unlocked` → audio-download first. An image comes as a C2PA-signed JPEG (`format`, `status: ok`, `title`, `url`) | call: an `ast_` image (JPEG) and an `ast_` video (MP4, a signed link valid one hour) worked; an `lasset_` id refused |
| visuals-models | models, durations, resolutions, aspects, prices | free | — | the price list above | — | call |
| visuals-upload-consent | records the user's answers to Suno's upload notice, one per section shown: "Accept Suno's upload notice … Only the uploader in /mcp can call this, when the user clicks Accept; a direct REST call gets 403" — an empty `pending` then lets visuals-upload-create through [OFFICIAL, Gemini's copy of the schema, 2026-11-20] | — | **decisions** (≥1: `consent_key`, `outcome` = the section's `accept_outcome`, `version`) | what is still owed (`pending`) | the model never calls it: on visuals-upload-create's 403 `upload_consent_required` the user accepts in Suno's uploader or on suno.com; a version no longer current is 409 (read the notice again). Claude's session does not show it (59 tools); Gemini's own reading — an app-only callback of the uploader, which Claude hides from the model and Gemini lists — is its explanation, not a fact | description (Gemini's schema); not called |
| visuals-upload-create · visuals-upload-complete | upload an image (≤10 MB) or video (≤500 MB) | free write | content_type, bytes, file / **id** | an asset | Suno's upload notice first (403 `upload_consent_required`); `upload_url` is a credential | description |
