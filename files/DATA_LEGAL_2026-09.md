---
file_id: DATA_LEGAL
version: "4.0"
layer: data
role: adapter
lazy: "/legal"
description: >
  Rights, terms and policies as of 2026-09-30: the difference between a platform's
  commercial licence and copyright, where each platform stands (Suno rights bound to
  the download, ElevenMusic ownership on every plan, open-model licences), uploading a
  voice, training on a catalogue, streaming and distributor policies, litigation
  (GEMA v Suno, the second UMG/Sony suit), the Udio case, watermarking, the EU AI Act
  transparency rules, when to warn, and a release checklist. Loaded on /legal or [11].
valid_as_of: "2026-09-30"
expires: "the fastest-moving and highest-consequence file in the system — terms, lawsuits and platform policies changed repeatedly in the two months before this date; verify everything before relying on it after 2026-12"
scope: commercial_rights · ownership_vs_licence · download_bound_rights · custom_models · voice_consent · litigation · platform_policies · distributors · udio_case · watermarking · eu_ai_act
key_concepts: [commercial_rights, copyright_ownership, download_bound_rights, remix_non_commercial, custom_models_terms, voice_rights_affirmation, training_licence, gema_v_suno, second_label_suit, spotify_ai_persona, deezer_ai_tagging, believe_tunecore, distrokid_suit, udio_starstruck, synthid, c2pa, eu_ai_act_article_50, release_checklist]
depends_on: [DATA_SUNO, DATA_GOOGLE, DATA_OTHER]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_03_DIAGNOSE, DATA_POSTPROD]
rag_priority: high
updated: "2026-09-30"
---

# ⚖️ SUNOFORGE v4.0 — RIGHTS AND POLICIES
# File 12 of 12 · DATA layer · valid as of 2026-09-30

> Reached with `/legal` or menu **[11] LEGAL CHECK** per CORE_00 §4.
> Not loaded by default.

> ⚠️ **This is not legal advice, and this system is not a lawyer.** What follows is a
> factual summary of publicly reported positions, assembled so you know which
> questions to ask and where the risk sits. For anything with money or a client
> attached, read the current terms yourself and take professional advice.

> ⚠️ **Expiry notice.** Of every file in this system, this one goes stale fastest and
> costs the most when it does. In the two months before this date: Suno rewrote its
> terms and tied commercial rights to downloads, a German court ruled against Suno,
> two major labels sued Suno again, a major label sued the largest distributor, and
> two streaming services introduced AI labels. Treat every statement here as a
> starting point for checking, not as a finding.

## §1. THE DISTINCTION EVERYTHING ELSE DEPENDS ON

The single most consequential misunderstanding in this field.

### "COMMERCIAL RIGHTS"
A permission from the platform: *we will not pursue you for using this commercially.*
A term of your contract with them.
  - It exists because they granted it, and it can change when terms change.
  - It is conditional — on your plan, and on Suno now also on the download (§2).
  - It says nothing about anyone else's claims.
  - It is not a warranty that the output infringes nothing.

### "COPYRIGHT"
A property right in the work itself: *this is mine, and I can stop others using it.*
  - Arises from authorship, not from a contract.
  - For purely machine-generated output, many jurisdictions hold that no one holds
    it — including United States registration practice [COMMUNITY, consistently
    reported].
  - Human contribution — your lyrics, your voice, your arrangement decisions, your
    editing — may carry its own protection independently of the generated audio.

WHY THE GAP MATTERS — you can hold full commercial rights to a track and still be
unable to stop someone distributing an identical copy, register it with a collecting
society, give a client the warranties a contract normally requires, or prove
authorship in a dispute.

Suno's own terms say it plainly: Pro and Premier users receive Suno's rights in the
output, but "Due to the nature of machine learning, Suno makes no representation or
warranty to you that any copyright will vest in any Output." [OFFICIAL]
The same terms forbid obtaining output "by any means other than a download channel
made available by Suno… (for example, recording or stream ripping are prohibited)".

## §2. WHERE EACH PLATFORM STANDS

⚠️ Plan names and what they unlock live in DATA_SUNO §12, DATA_OTHER §6. No prices
anywhere. This section describes the character of each position.

─── SUNO ─── terms dated 2026-08-10, in force since 2026-09-03 [OFFICIAL]
  FREE          "you will only use such Outputs for your lawful, personal and
                non-commercial purposes". (Older guides add an attribution
                requirement; the current clause has none.)
  PRO / PREMIER "Suno hereby assigns to you all of its right, title and interest in
                and to any Output owned by Suno…" — subject to the commercial-use
                conditions.
  THE NEW RULE  "You may not commercially exploit Output that has not been
                downloaded by you through an approved channel." Downloads are capped
                per plan (DATA_SUNO §12). Suno: "Songs downloaded from Suno on paid
                plans remain yours to use commercially or personally."
  REMIXES       of another user's song are "a joint work owned jointly and equally by
                you and the Remixer" and may be used only for "lawful, personal and
                non-commercial purposes" — on every plan.
  MARKS         "You agree not to remove, alter, obscure or circumvent any
                fingerprint, watermark or metadata Suno appends to an Output."
  UPLOADS       every submission — lyrics, audio, voice, training tracks — is licensed
                to Suno "worldwide… perpetual, irrevocable" including for improving
                "the artificial intelligence and machine learning models" (§3).

  THE TWO TRAPS:
  1. Free stays non-commercial. Upgrading later does not reach back to songs made on
     Free. Anything you might release must be made on a paid plan.
  2. Made-but-not-downloaded is not enough any more. Download what you intend to
     release while subscribed; the monthly cap is part of release planning.
  Neither can be fixed afterwards; both cost nothing to avoid.

### GOOGLE — LYRIA, GEMINI APP, FLOW MUSIC
  PROVENANCE      SynthID on every output [OFFICIAL]; the Gemini app can check a file
                  for it. C2PA was documented for Lyria 3 Pro; not re-confirmed for 3.5.
  COMMERCIAL USE  ⚠️ not stated clearly enough for this system to rely on. The app,
                  the API and Flow Music are governed by different documents. Third
                  parties say Flow Music's paid plans include commercial use; the
                  primary clause was not found [UNVERIFIED].
  WHAT TO DO      read the terms of the surface you generated on, not "Google's
                  terms" in general.
  BLOCKED INPUTS  specific artist voices and copyrighted lyrics [OFFICIAL].

─── ELEVENMUSIC ─── [OFFICIAL] since 2026-09-11
  "You own what you make in ElevenMusic, on every plan, including Free." On Free,
  commercial use is allowed "as long as you credit ElevenMusic". Rights attach when
  the track is made; cancelling or downgrading does not change them; future term
  changes apply only to new tracks. Downloads are blocked for tracks built on another
  artist's song. "cleared for nearly all commercial uses". For client work this is
  the clearest position among hosted platforms. ElevenMusic's own post is softer —
  "Rights and commercial use vary by subscription tier. See Terms for details."

─── STABLE AUDIO ─── [OFFICIAL]
  Licensed training data; "You own your outputs" under the Community Licence;
  organisations above the revenue threshold need the Enterprise Licence, which adds
  indemnification. The smaller models run on your own hardware.

─── OPEN MODELS YOU RUN YOURSELF ─── [OFFICIAL: project licences]
  ACE-Step 1.5 — MIT. YuE2 — weights CC BY-NC 4.0 plus a creator permission: free to
  use and monetize for individuals and musicians; companies need a licence.
  MiniMax Music 3.0 — read the model card. With these, the licence of the weights is
  the whole rights question; no platform stands between you and the output.

### AGGREGATORS
  The upstream terms attach to the account holder — the aggregator. With Suno's rights
  now bound to the user's own download on the user's own paid plan, output bought
  through a reseller is hard to call yours. DATA_OTHER §4.

## §3. UPLOADING YOUR VOICE

─── THE VERIFICATION STEP ─── [OFFICIAL]
You read a random phrase aloud; it is compared with the singing you uploaded. It
exists to stop you cloning someone else's voice. It is a safeguard: tools that clone
a voice in seconds WITHOUT such a step are faster only because they check nothing.

─── THE CHECKBOX ─── [OFFICIAL]
You "affirm that you have the rights to use this voice". The terms go further: "you
can only create a Voice Model resembling your own voice".

─── THE TRAINING LICENCE ─── [OFFICIAL]
Editions up to v3.0 described a separate checkbox permitting training on your voice.
In the current terms, training permission is part of the general licence every
upload grants — worldwide, perpetual, irrevocable, including for improving Suno's
models. You do not tick it separately; you agree to it by uploading.
  ⚠️ This is a decision about your voice as biometric-adjacent personal data. Whether
  deleting the voice withdraws anything is not documented [UNVERIFIED].

### SOMEONE ELSE'S VOICE
Do not upload it. Beyond the terms, unauthorised voice cloning is prohibited by the
major streaming services (§5) and is among the most actively litigated areas here —
a US artist-identity class action against Suno was filed in August 2026 (§6).
Consent from the voice's owner should be explicit and written if the work goes
anywhere near commercial use.

Voices is 18+ and not offered in every country [OFFICIAL]. Feature details: DATA_SUNO §5.

## §4. TRAINING A MODEL ON YOUR CATALOGUE

### THE REQUIREMENT
  Suno Custom Models: "You must own the rights to all of the songs you upload"
  [OFFICIAL]. ElevenMusic Finetunes: "non-copyrighted tracks you own", screened
  automatically [OFFICIAL]. LoRA on a local model: no platform check at all — the
  responsibility is entirely yours.

### HOW IT IS ENFORCED
  On Suno by the terms, not by a technical check. The absence of a barrier is not
  permission — it is liability sitting with you. The uploads also fall under the
  training licence in §2.

### WHAT IS NOT DOCUMENTED
  [UNVERIFIED] What happens to a trained model after a rights complaint.

### SITUATIONS PEOPLE GET WRONG
  ❌ A band's catalogue, uploaded by one member — rights are usually shared
  ❌ Tracks you produced for someone else — producing is not owning
  ❌ A client's catalogue on the client's verbal say-so — get it in writing, from
     whoever holds the rights, which may be a label
  ❌ Material licensed for one purpose — a sync or stock licence almost never
     includes training
  ❌ "It's only for my own use" — the terms do not turn on intent
  ✅ Music you wrote, recorded and own outright
  ✅ Material with a written licence that explicitly covers AI training

IF THE PROJECT IS COMMERCIAL: a saved Style description reused across tracks gives
much of the same consistency with none of this exposure (DATA_RECIPES §8).
Requirements and limits of the feature itself: DATA_SUNO §6.

## §5. STREAMING, DISTRIBUTION AND PLATFORM POLICIES

─── SPOTIFY ─── [OFFICIAL, 2026-08-11]
  "starting mid-September, you'll begin to see an AI Persona badge on some artist
  profiles" — a profile whose identity "may be AI-generated and does not represent a
  real person". Artists can self-disclose in Spotify for Artists; Spotify also reviews
  profiles itself, starting with those above audience thresholds; artists can appeal.
  "By default, Spotify will not include AI Personas in any editorial or algorithmic
  recommendations."
  The badge "is about the artist's public identity, not about how the music was
  made". For how music was made: AI Credits (tens of thousands submitted daily) and
  SongDNA. Also in 2026: Verified by Spotify, Artist Profile Protection (artists
  approve releases delivered under their name).
  Earlier and still in force [COMMUNITY]: unauthorised voice cloning prohibited;
  mass-upload spam filtered; AI disclosure in credits via the industry metadata
  standard; a major-label deal lets subscribers make AI covers and remixes in-app.

  PRACTICAL READING: AI-made music is allowed. A fictional human artist persona on top
  of it now costs you recommendations. Present yourself as who you are.

─── DEEZER ─── [OFFICIAL, 2026-07-21]
  About 90,000 fully AI-generated tracks a day — over half of new uploads at the June
  2026 peak. Detected AI tracks are tagged for listeners (since 2025 by most of the release;
  one passage says June 2026 — the text contradicts itself) and left out
  of algorithmic and editorial recommendations. Deezer will take down AI tracks used
  for streaming fraud and those not streamed for six months or more. Fully AI tracks
  are 1–3 % of listening; up to 85 % of their 2025 streams were fraudulent and
  demonetised. Deezer detects output of "the most prolific generative models, such as
  Suno and Udio" and licenses its detector to others.

─── APPLE MUSIC ─── [COMMUNITY: trade press, 2026-08]
  "Made With AI" labels on tracks that providers identify as materially AI-generated,
  expected later in 2026.

─── YOUTUBE ─── [COMMUNITY, May 2026, no change found since]
  Realistic AI-generated video is detected and labelled automatically, whether or not
  the creator discloses it; labelling reportedly does not affect recommendations or
  monetisation. A song over a static image is a video for this purpose.

### DISTRIBUTORS
  BELIEVE / TUNECORE [OFFICIAL, 2026-09-08] — "All tracks created by artists using
  Suno's new industry partner model will become eligible to distribute through
  Believe and TuneCore", reversing Believe's April 2026 block on Suno's earlier models.
  Believe and TuneCore artists who opt in are included in Suno's new models and paid.
  DISTROKID [COMMUNITY: trade press quoting the complaint, 2026-09] — sued by UMG for
  deceptive practices and infringement, accused of passing off mass AI uploads as
  artist releases. The complaint says it is "not about the distribution of
  AI-generated music when clearly disclosed as such".
  Others — check the distributor you use; its rules may be stricter than the
  streaming services'.

### THE GENERAL SHAPE
  AI music is allowed. Impersonation is not. Spam and fraud are removed. Disclosure is
  expected and increasingly automatic — Deezer tags, Spotify badges personas, Apple
  plans labels, YouTube labels video. Undisclosed AI music is detected more often than
  it is hidden. The real line is honesty: about the voice, the artist identity, and
  the volume.

## §6. LITIGATION — THE STATE OF PLAY

─── GEMA v SUNO — Landgericht München I, 2026-07-31, Az. 42 O 763/25 ─── [OFFICIAL]
  The copyright chamber granted GEMA's claims for an injunction, disclosure and
  damages in the main ("überwiegend stattgegeben"). Six works: "Atemlos durch die
  Nacht", "Rasputin", "Big in Japan", "Forever Young", the "Mambo No. 5" refrain and
  "Daddy Cool"; the lyrics were not at issue.
  The court found the works "reproducibly contained" in Suno's v3.5 and v4 models —
  memorisation — with the models stored on servers in Germany; infringement both
  through training in the US and through reproduction in the model and in outputs;
  the text-and-data-mining exception did not cover it. The court also recorded that
  Suno obtained the recordings from YouTube by circumventing its "rolling cipher"
  protection. The judgment is not final; Suno indicated an appeal [COMMUNITY].
  Effect on users today: none documented. Those two models are retired anyway.

─── SUNO — OTHER CASES ─── [COMMUNITY: trade press]
  2024-06   UMG, Sony and Warner sue Suno in Massachusetts; still running for UMG and
            Sony
  2025-11   Warner settles and partners with Suno
  2026-08   BMG partners with Suno · Round Hill Music sues for $1 billion ·
            Jason Isbell leads a proposed class action over artist identity
  2026-09   SOCAN sues (early September) · Believe partnership (09-08) · v6 launch
            (09-09) · UMG and Sony file a second, 45-page suit (Friday 09-18): v6 is
            "the fruit of the same poisoned tree", because training on outputs of
            earlier models "launders" the infringement; 60,202 recordings listed.
            Suno: the claims are "fundamentally flawed on both the facts and the law";
            v6 "was trained on content licensed from our partners, interactions
            including creations and preference signals from our community, and the
            accumulated learnings from our team."

### ELSEWHERE
  Udio: settled with UMG (2025-10) and Warner (2025-11); licences with Merlin
  (2026-01) and Kobalt (2026-04); Sony still litigating [COMMUNITY].
  ElevenLabs: multi-year agreement with UMG (2026-09), separate from Music v2.5
  [OFFICIAL].
  Stability AI: alliances with UMG and Warner; investment from Sony, UMG and Warner
  [OFFICIAL: company news].

WHAT THIS MEANS FOR YOU:
  - Settlements and licences are why terms changed (§2). Obligations flow down.
  - A platform with open litigation may change its terms again, not necessarily in
    your favour.
  - Settlement is not licensing: it resolves the past; it does not license the future.
  - Using generated music commercially is not illegal. The point is to know which
    permission you actually have, and from whom.

## §7. THE UDIO CASE — WHY EXPORT MATTERS

─── WHAT HAPPENED ─── [OFFICIAL + COMMUNITY]
Following its settlement with a major label group in late 2025, Udio disabled
downloads, giving users a window of about 48 hours to export their work. Generation,
remixing and link sharing continued; getting a file out did not.

─── THE POSITION NOW ─── [COMMUNITY]
Downloads remain closed [UNVERIFIED: Udio's help pages not checked]. The licensed
successor, "Starstruck", was described in May 2026: a mobile app for fans with Cover,
Reimagine, Remix and Create modes, always starting from a chosen artist and song;
generic unattributed music not available; creations owned by the participating
artist's rights holder, not by the fan; no export to other services. Launch "later
this year"; not launched as of this date.

### THE LESSONS, WHICH ARE NOT ABOUT ONE PLATFORM
  1. **Export as you go.** A platform library is not storage. Download finished work
     when it is finished — on Suno that is now also when your commercial rights begin.
  2. **Terms can change retroactively in effect.** Nothing changed about the tracks
     users had made; their ability to reach them did.
  3. **A short window is the normal amount of notice.**
  4. **This is not unique.** A different service's migration made every past
     generation inaccessible (DATA_GOOGLE §7); Suno capped downloads on songs made
     before the cap existed (DATA_SUNO §12).
  5. **Keep your prompts, not only your outputs.** Generated audio is not
     reproducible, so a prompt is not a backup of the track — but it is a backup of
     the work, and the only part no platform can take.

## §8. WATERMARKING AND PROVENANCE

  GOOGLE    SynthID on every Lyria output — inaudible, not removable, designed to
            survive conversion, editing and compression. The Gemini app checks files
            for it on request [OFFICIAL].
  SUNO      the terms reserve fingerprints, watermarks and metadata on outputs and
            forbid removing them [OFFICIAL]; a C2PA manifest has been reported in a
            v6 WAV [COMMUNITY].
  DEEZER    detects Suno and Udio output with its own tool and tags it (§5) [OFFICIAL].
  UDIO      Starstruck is described with inaudible watermarking and fingerprinting
            [COMMUNITY].
  ELEVENMUSIC  no statement found.

WHAT THIS MEANS: assume generated audio is identifiable as generated, indefinitely,
even after mixing and mastering. That is mostly fine — disclosure is expected, not
penalised (§5). It is a problem only for a plan that depended on the origin staying
hidden, and that plan is the thing to change.

DO NOT ATTEMPT REMOVAL: it breaks the terms and turns a licensing question into an
argument about intent.

## §9. REGULATION — EU AI ACT TRANSPARENCY

[OFFICIAL, European Commission] The final Code of Practice on marking and labelling
AI-generated content is published. It is voluntary and helps providers and deployers
meet "the AI Act transparency obligations that will apply from 2 August 2026". From
that date: "Deepfakes and AI-generated or AI-manipulated text published on matters of
public interest must be clearly labelled."

  PROVIDERS (the platforms) must make synthetic audio machine-detectable — the
  watermarks in §8 [COMMUNITY: legal commentary].
  DEPLOYERS (people publishing the output) label deepfakes; for audio-only content the
  Code contemplates alternatives such as audio disclaimers [COMMUNITY: legal
  commentary]. Systems already on the market reportedly get until 2026-12-02 for the
  provider-side marking [COMMUNITY].

PRACTICAL READING FOR A MUSICIAN IN THE EU: an original AI-assisted song is not a
deepfake. A track that imitates a real, identifiable person's voice is — label it,
and before that, have their consent (§3). Not legal advice.

## §10. WHEN TO RAISE A WARNING

For this system, in conversation. Warn once, briefly, and continue helping — a
warning repeated on every response stops being read.

| Trigger | Say |
|---|---|
| training on material that may not be theirs | rights to every uploaded track are required, and how that usually goes wrong (§4) |
| uploading a voice | the upload is licensed to the platform for training; only your own voice is allowed (§3) |
| someone else's voice | cloning without consent is prohibited by terms and streaming services, and is a deepfake under EU rules (§3, §5, §9) |
| naming a living artist | blocked on some platforms and risky everywhere; offer the trait translation (CORE_01 §12) |
| advertising, film, client work | platform choice determines the rights position; name the strongest (§2) |
| "I'll upgrade later" | Free output stays non-commercial (§2) |
| a Suno song for release | download it on a paid plan; the download starts the rights (§2) |
| remixing someone else's Suno song | remixes are non-commercial on every plan (§2) |
| releasing to streaming | disclosure norms; a fake human persona costs recommendations on Spotify (§5) |
| building a business on one platform's library | export as you go (§7) |

### HOW TO SAY IT
  ✅ "Worth knowing before you upload: the upload lets them train on your voice, and
     only your own voice is allowed. Read that screen — people skip it."
  ❌ "WARNING: LEGAL RISK. Consult an attorney before proceeding."
  The first is useful. The second is noise, and noise gets skipped — which means the
  one time it mattered, it was also skipped.

### WHAT NOT TO DO
  - Refuse to help because a question has a legal dimension.
  - Give a confident answer about a specific jurisdiction.
  - State plan tiers from memory, or any price at all.
  - Present anything in this file as current without checking the date at the top.

## §11. A CHECKLIST BEFORE RELEASE

  ☐ Generated on a plan that grants commercial rights — and, on Suno, DOWNLOADED on
    that plan
  ☐ Not a remix of someone else's song, if the release is commercial
  ☐ Nothing uploaded that you do not hold the rights to
  ☐ No voice used without the owner's explicit permission
  ☐ No real artist named in the prompt
  ☐ You know whether you hold copyright, or merely a licence (§1)
  ☐ Exported and archived outside the platform
  ☐ Prompts saved in your own notes
  ☐ Disclosure decided — AI credits where the service offers them; no invented human
    persona
  ☐ Your distributor accepts tracks from the model you used (Believe/TuneCore: Suno v6
    yes, earlier models no)
  ☐ If a client is involved: you have read the actual terms, this quarter, for the
    actual platform
  ☐ If the stakes justify it: a lawyer has read them too

### THE ONE-LINE VERSION
**Know which permission you have, from whom, and keep your own copy of everything.**

// ═══════════════════════════════════════════════════════════════
// END OF DATA_LEGAL_2026-09.md · SunoForge v4.0
// Snapshot date 2026-09-30 · the fastest-decaying file here — check it first
// ═══════════════════════════════════════════════════════════════

## TAGS
legal, rights, commercial rights, copyright, licence vs ownership, suno terms, download-bound rights, free non-commercial, remixes non-commercial, watermark, fingerprint, training licence, voice upload, own voice only, custom models rights, elevenmusic ownership, credit elevenmusic, stable audio community licence, open model licences, aggregators, spotify ai persona, deezer ai tagging, apple music made with ai, youtube labelling, believe tunecore, distrokid lawsuit, gema v suno, munich ruling, umg sony second lawsuit, round hill, isbell, socan, udio starstruck, synthid, c2pa, eu ai act article 50, code of practice, release checklist
