---
file_id: DATA_LEGAL
version: "3.0"
layer: data
lazy: "/legal"
valid_as_of: "2026-07-27"
expires: "this is the fastest-moving and highest-consequence file in the system — litigation and terms of service changed repeatedly in the twelve months before this date; verify everything before relying on it after 2026-10"
scope: commercial_rights · ownership_vs_licence · custom_models · voice_consent · litigation · platform_policies · udio_case
key_concepts: [commercial_rights, copyright_ownership, custom_models_terms, voice_consent, training_consent, label_settlements, spotify_policy, youtube_labelling, ddex_disclosure, synthid, c2pa, udio_case]
depends_on: [DATA_SUNO, DATA_GOOGLE, DATA_OTHER]
used_by: [CORE_00_ENTRY, CORE_01_STYLE, CORE_03_DIAGNOSE, DATA_POSTPROD]
rag_priority: high
updated: "2026-07-27"
---

# ⚖️ SUNOFORGE v3.0 — RIGHTS AND POLICIES
# File 12 of 12 · DATA layer · valid as of 2026-07-27

> Reached with `/legal` or menu **[11] LEGAL CHECK** per CORE_00 §4.
> Not loaded by default.

> ⚠️ **This is not legal advice, and this system is not a lawyer.** What
> follows is a factual summary of publicly reported positions, assembled so
> you know which questions to ask and where the risk sits. For anything with
> money or a client attached, read the current terms yourself and take
> professional advice.

> ⚠️ **Expiry notice.** Of every file in this system, this one goes stale
> fastest and costs the most when it does. In the year before this date:
> multiple label settlements, one platform's export function disabled, one
> vendor's terms rewritten, and new platform disclosure policies at two major
> services. Treat every statement here as a starting point for checking, not
> as a finding.

═══════════════════════════════════════════════════════════════════
§1. THE DISTINCTION EVERYTHING ELSE DEPENDS ON
═══════════════════════════════════════════════════════════════════

<rag_zone id="rights_vs_ownership">

The single most consequential misunderstanding in this field.

─── "COMMERCIAL RIGHTS" ───

A permission from the platform. It says: *we will not pursue you for using
this commercially.* It is a term of your contract with them.

  - It exists because they granted it, and it can change when terms change.
  - It is usually conditional on your plan, and on your plan at the time of
    generation rather than now.
  - It says nothing about anyone else's claims.
  - It is not a warranty that the output infringes nothing.

─── "COPYRIGHT" ───

A property right in the work itself. It says: *this is mine, and I can stop
others using it.*

  - Arises from authorship, not from a contract.
  - For purely machine-generated output, many jurisdictions hold that no one
    holds it — including, notably, the United States registration practice
    [COMMUNITY, consistently reported].
  - Human contribution — your lyrics, your voice, your arrangement decisions,
    your editing — may carry its own protection independently of the
    generated audio.

─── WHY THE GAP MATTERS ───

You can hold full commercial rights to a track and still be unable to:

  - stop someone else distributing an identical copy
  - register it with a collecting society
  - give a client the warranties a commercial contract normally requires
  - prove authorship in a dispute

  None of that is a defect in the platform. It is the difference between a
  licence and a property right, and it surprises people precisely because
  "commercial rights" sounds like ownership.

─── THE SHIFT IN LANGUAGE ───

[COMMUNITY] Following a major label partnership in late 2025, terms language
at one leading platform moved from wording that read as *you own this* toward
wording that reads as *you have commercial rights*.

That is a meaningful change and it went largely unremarked. If you are
working from a guide, a course or a forum post written before it, the rights
description in that material may no longer match the terms you actually
agreed to.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§2. WHERE EACH PLATFORM STANDS
═══════════════════════════════════════════════════════════════════

<rag_zone id="platform_positions">

⚠️ Plan tiers, prices and allowances are not restated here — they live in
DATA_SUNO §11 and DATA_OTHER §5 and they move. This section describes the
*character* of each position, which moves more slowly.

─── SUNO ───

  FREE TIER          non-commercial [COMMUNITY]
  PAID TIERS         commercial rights granted [COMMUNITY]
  THE TRAP           ⚠️ upgrading does **not** retroactively license tracks
                     made while on the free tier. Anything you might ever
                     want to use commercially must be generated on a paid
                     plan from the start.
  LITIGATION         settled with one major label group in late 2025; as of
                     this date, not settled with another [COMMUNITY]
  UPLOADS            you must hold rights to everything you upload — voice
                     material and training material alike (§3, §4)

  The free-tier trap is the most expensive routine mistake in this system.
  It costs nothing to avoid and cannot be fixed afterward.

─── GOOGLE — LYRIA AND FLOW MUSIC ───

  PROVENANCE         every output carries SynthID watermarking and C2PA
                     signed metadata [OFFICIAL]. The watermark cannot be
                     removed and survives ordinary editing.
  COMMERCIAL USE     ⚠️ not documented clearly enough for this system to
                     state. Terms vary by surface — the consumer app, the
                     cloud API and the music workspace are not necessarily
                     governed by the same document. [UNVERIFIED]
  WHAT TO DO         if the work is commercial, read the terms for the
                     specific surface you generated on, not "Google's terms"
                     in general.

  ⚠️ Earlier editions of this system stated that Google makes no claim to
  rights in generated content. That claim was carried without a source and
  without a confidence mark, and it is not repeated here.

─── ELEVENMUSIC ───

  TRAINING DATA      licensed [COMMUNITY] — the platform's central claim
  COMMERCIAL USE     granted on paid tiers [COMMUNITY]
  FREE TIER          not for commercial use [COMMUNITY]
  WHY IT MATTERS     this is the position that survives a client asking
                     where the music came from. For advertising, film and
                     work delivered to someone else, it is the strongest
                     answer among the hosted platforms.

─── STABLE AUDIO ───

  TRAINING DATA      licensed from a commercial stock library [OFFICIAL]
  LICENCE            a community licence granting ownership of the output
                     and commercial use [OFFICIAL]
  THRESHOLD          organisations above roughly $1M revenue need an
                     enterprise agreement [OFFICIAL]
  OPEN WEIGHTS       the smaller models are published, so you can run them
                     yourself — which removes the platform from the rights
                     question entirely for those models

  The strongest position available here, and the only one where "you own the
  output" is stated rather than approximated.

─── AGGREGATORS AND RESELLERS ───

  ⚠️ The underlying platform's terms attach to the account holder, and the
  account holder is the aggregator, not you. Whatever rights the upstream
  platform grants, it grants to them.

  For personal work this is usually academic. For anything commercial it is
  a genuine problem and not a theoretical one. See DATA_OTHER §4.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§3. UPLOADING YOUR VOICE
═══════════════════════════════════════════════════════════════════

<rag_zone id="voice_consent">

The feature that lets a platform sing in your own voice involves two legal
steps people click through without reading.

─── THE VERIFICATION STEP ───

[OFFICIAL] You read a randomly generated phrase aloud, and it is matched
against the singing you uploaded.

This exists to stop you cloning someone else's voice. It is a safeguard, not
an inconvenience — a point worth making, because tools that clone a voice in
seconds *without* such a step are sometimes recommended on the basis of being
faster. Faster, in that context, means no consent check.

─── THE CONSENT CHECKBOX ───

[OFFICIAL] Alongside verification there is a checkbox permitting the platform
to use your voice to train and improve its models.

  ⚠️ Read it before you tick it. People upload their own singing voice while
  concentrating on the recording quality and agree to a training permission
  without registering that they have.

  This is a decision about your voice as biometric-adjacent personal data,
  and it is not obviously reversible. Whether deleting the voice withdraws
  the permission, and what happens to a model already trained, is not
  documented [UNVERIFIED].

─── SOMEONE ELSE'S VOICE ───

Do not upload it. Beyond the platform terms, unauthorised voice cloning is
specifically prohibited by the major streaming services (§5) and is among
the most actively litigated areas in this field.

  Consent from the voice's owner should be explicit and written if the work
  goes anywhere near commercial use. "They said it was fine" is not a
  position you want to be in.

─── PRIVACY ───

[OFFICIAL] Trained voices are tied to the account and cannot be shared or
made public. Feature requirements and accepted recording lengths: DATA_SUNO
§5.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§4. TRAINING A MODEL ON YOUR CATALOGUE
═══════════════════════════════════════════════════════════════════

<rag_zone id="custom_models">

─── THE REQUIREMENT ───

[OFFICIAL] You must hold the rights to every track you upload for training.

─── HOW IT IS ENFORCED ───

By the terms, not by a technical check. Nothing stops you uploading material
you do not own. The absence of a barrier is not permission — it is
liability sitting with you.

─── WHAT IS NOT DOCUMENTED ───

[UNVERIFIED] What happens to a trained model after a rights complaint. The
reasonable assumption is removal under general terms, but no published
process describes it. If you have built a workflow around a model, that is an
unquantified risk to your workflow, not only to your account.

─── SITUATIONS PEOPLE GET WRONG ───

  ❌ A band's catalogue, uploaded by one member, without the others
     Rights in a band's recordings are usually shared. One member's
     agreement is not the band's.

  ❌ Tracks you produced for someone else
     Producing is not owning. Check what your agreement actually assigned.

  ❌ A client's catalogue, on the client's verbal say-so
     Get it in writing, and get it from whoever actually holds the rights,
     which may be a label rather than the artist.

  ❌ Material you licensed for one purpose
     A sync licence or a stock licence almost certainly does not include
     training rights.

  ❌ "It's only for my own use"
     The terms do not turn on your intent.

  ✅ Music you wrote, recorded and own outright
  ✅ Material with a written licence that explicitly covers AI training

─── IF THE PROJECT IS COMMERCIAL ───

Consider whether you need a trained model at all. A saved Style description
reused across tracks achieves much of the same consistency with none of this
exposure (DATA_RECIPES §8). Requirements and limits for the feature itself:
DATA_SUNO §6.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§5. STREAMING AND PLATFORM POLICIES
═══════════════════════════════════════════════════════════════════

<rag_zone id="platform_policies">

─── SPOTIFY ───

[COMMUNITY] AI-generated music is permitted. The stated position rests on
three pillars:

  1. UNAUTHORISED VOICE CLONING IS PROHIBITED.
     The clearest red line in this whole file. Impersonating a real artist's
     voice without permission is not a grey area anywhere.

  2. SPAM FILTERING.
     Mass-uploaded, low-effort and duplicate content is removed at
     substantial scale — reported in the tens of millions of tracks over a
     year. Aimed at upload farms rather than at individual creators, but the
     filtering does not ask about your intent.

  3. AI DISCLOSURE IN CREDITS.
     Delivered through the industry metadata standard used for credits.
     Disclosure is voluntary, and disclosing does not by itself affect
     ranking or payouts.

  [COMMUNITY] Artist profile protection measures have been in testing. From
  May 2026, a deal with one major label group allows subscribers to make AI
  covers and remixes of that catalogue inside the service — a notable
  precedent for licensed AI use of commercial catalogue.

─── YOUTUBE ───

[COMMUNITY] Since May 2026, realistic AI-generated video is detected and
labelled automatically, whether or not the creator discloses it.

  - Labelling is reported not to affect recommendations or monetisation.
  - Audio is not singled out separately — the labelling applies to the
    video. A music track with a static image is a video for this purpose.

  Practical reading: disclose anyway. Being labelled by the platform after
  not disclosing is worse for an audience relationship than saying so.

─── THE GENERAL SHAPE ───

Distribution platforms have converged on: AI music is allowed, impersonation
is not, spam is removed, and disclosure is expected but not usually
penalised. Nothing in current policy at either service treats AI-generated
music as prohibited content.

⚠️ Distributors and aggregators may impose their own additional requirements
that are stricter than the streaming services'. Check the one you use.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§6. LITIGATION — THE STATE OF PLAY
═══════════════════════════════════════════════════════════════════

<rag_zone id="litigation">

[COMMUNITY] Summarised because it shapes the terms you are agreeing to, not
because you need to follow it.

  late 2025    one major label group settled with two leading generation
               platforms
  late 2025    another major group settled with one of them
  as of this   that second group had not settled with the other platform
  date
  mid 2026     a musicians' union action against a major label over the
               allocation of proceeds from AI licensing deals — a sign that
               the disputes are moving from *whether* to *how the money is
               divided*

─── WHAT THIS MEANS FOR YOU ───

  - Settlements are why terms language changed (§1). Platforms that settle
    take on obligations, and those obligations flow down into your terms.
  - A platform with unresolved litigation carries a risk that its terms may
    change, and possibly not in your favour.
  - Settlement is not the same as licensing. A settlement resolves a dispute
    over the past; it does not necessarily license the future.

─── WHAT IT DOES NOT MEAN ───

It does not mean generated music is legally unsafe to use. Millions of people
use it commercially under terms that permit it. The point is to know which
permission you actually have, and from whom.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§7. THE UDIO CASE — WHY EXPORT MATTERS
═══════════════════════════════════════════════════════════════════

<rag_zone id="udio_case">

The most useful cautionary example available, and the reason this system
treats "can you get your work out?" as a first-order question.

─── WHAT HAPPENED ───

[OFFICIAL + COMMUNITY] Following a settlement with a major label group in
November 2025, downloads were disabled. Users were given a window measured in
hours to export their work.

  Generation continued. Remixing continued. Sharing by link continued.
  Getting a file out did not.

─── THE POSITION NOW ───

[COMMUNITY] As of this date: export remains closed, commercial rights are
undefined, and no licensed successor has been announced.

─── WHY THIS SYSTEM DROPPED IT ───

Not as a judgement on the platform's quality — it was genuinely strong at
instrumental work. A tool you cannot retrieve your work from is not usable in
any pipeline, however good the output sounds. It appears in this system only
here, as a case.

─── THE LESSONS, WHICH ARE NOT ABOUT ONE PLATFORM ───

  1. **Export as you go.** Do not treat a platform's library as storage.
     Download finished work when it is finished.

  2. **Terms can change retroactively in effect.** Nothing changed about the
     tracks users had already made. What changed was their ability to reach
     them. A permission you rely on can be withdrawn without your work being
     altered at all.

  3. **A short window is the normal amount of notice.** Hours, announced
     while people were asleep, in a different time zone.

  4. **This is not unique.** The same year, a different service's migration
     made every past generation, session and trained model inaccessible
     (DATA_GOOGLE §7). Two platforms, two mechanisms, same outcome for the
     user.

  5. **Keep your prompts, not only your outputs.** A prompt in your own notes
     survives any platform. Generated audio is not reproducible — the same
     prompt does not return the same track — so a saved prompt is not a
     backup of the track. But it is a backup of the *work*, and it is the
     only part no platform can take.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§8. WATERMARKING AND PROVENANCE
═══════════════════════════════════════════════════════════════════

<rag_zone id="watermarking">

[OFFICIAL] Google's music output carries SynthID watermarking and C2PA signed
metadata. The watermark is inaudible, is not removable, and is designed to
survive ordinary processing — format conversion, editing, compression.

─── WHAT THIS MEANS PRACTICALLY ───

  - Output can be identified as machine-generated by anyone with the
    detection tooling, indefinitely.
  - Editing it, mixing it into a larger work, or mastering it does not
    remove the marking.
  - A track combining generated and recorded material carries the marking on
    the generated portion.

─── WHY THAT IS MOSTLY FINE ───

Disclosure is expected rather than penalised at the major services (§5).
Watermarking is a problem only if your plan depended on the origin not being
detectable — and if it did, that is a plan worth revisiting rather than a
technology worth defeating.

─── DO NOT ATTEMPT REMOVAL ───

Beyond being a terms violation, it is the kind of act that converts a
straightforward licensing question into an argument about intent.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§9. WHEN TO RAISE A WARNING
═══════════════════════════════════════════════════════════════════

<rag_zone id="legal_triggers">

For this system, in conversation. Warn once, briefly, and continue helping —
a warning repeated on every response stops being read.

  TRIGGER                            SAY
  ────────────────────────────────── ────────────────────────────────────
  training on material that may      that rights to every uploaded track
  not be theirs                      are required, and how that usually
                                     goes wrong (§4)
  uploading a voice                  that a training-consent checkbox is
                                     part of the flow, and to read it (§3)
  someone else's voice               that unauthorised cloning is
                                     prohibited by terms and by the
                                     streaming services (§3, §5)
  naming a living artist             that it is filtered on some platforms
                                     and risky everywhere; offer the trait
                                     translation instead (CORE_01 §12)
  advertising, film, client work     that platform choice determines the
                                     rights position, and which platforms
                                     are strongest (§2)
  "I'll upgrade later"               that upgrading does not retroactively
                                     license free-tier output (§2)
  releasing to streaming             disclosure norms, and that it is not
                                     penalised (§5)
  building a business on one         export as you go (§7)
  platform's library

─── HOW TO SAY IT ───

  ✅ "Worth knowing before you upload: there's a checkbox in that flow that
     lets them train on your voice. Read it — people miss it."
  ❌ "WARNING: LEGAL RISK. Consult an attorney before proceeding."

  The first is useful. The second is noise, and noise gets skipped — which
  means the one time it mattered, it was also skipped.

─── WHAT NOT TO DO ───

  - Do not refuse to help because a question has a legal dimension.
  - Do not give a confident answer about a specific jurisdiction.
  - Do not state plan tiers or prices from memory — read DATA_SUNO and
    DATA_OTHER, which are the only files that carry them.
  - Do not present anything in this file as current without checking the
    date at the top.

</rag_zone>

═══════════════════════════════════════════════════════════════════
§10. A CHECKLIST BEFORE RELEASE
═══════════════════════════════════════════════════════════════════

<rag_zone id="release_checklist">

  ☐ Generated on a plan that grants commercial rights — at the time it was
    generated, not now
  ☐ Nothing uploaded that you do not hold the rights to
  ☐ No voice used without the owner's explicit permission
  ☐ No real artist named in the prompt
  ☐ You know whether you hold copyright, or merely a licence (§1)
  ☐ Exported and archived outside the platform
  ☐ Prompts saved in your own notes
  ☐ Disclosure decided, and disclosed if you decided to
  ☐ If a client is involved: you have read the actual terms, this quarter,
    for the actual platform
  ☐ If the stakes justify it: a lawyer has read them too

─── THE ONE-LINE VERSION ───

**Know which permission you have, from whom, and keep your own copy of
everything.**

</rag_zone>

// ═══════════════════════════════════════════════════════════════
// END OF DATA_LEGAL_2026-07.md · SunoForge v3.0
// Snapshot date 2026-07-27 · the fastest-decaying file here — check it first
// ALL 12 FILES COMPLETE
// ═══════════════════════════════════════════════════════════════
