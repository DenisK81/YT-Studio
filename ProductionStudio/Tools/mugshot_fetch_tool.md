# Tool: mugshot_fetch_tool

## Purpose
Fetch real material for a case — photos and, where publicly available, video clips — to mix
with Image Generation Agent's AI-generated reenactment stills, not to replace them. **Sourcing
priority, escalated 2026-08-30 per explicit channel-owner instruction:** real archival video
clips first, real photos second, AI generation last — generation exists to fill genuine gaps
(a scene with no real footage or photo available), not as the default. This is a tightening of
the existing "real photos mandatory" rule (`Documentation/ARCHITECTURE.md`), not a new policy —
the channel owner's concrete framing: "больше реальных фото, а не тупой генерации картинок... генерация
нужна, но только точечно чтоб закрыть какие-то дыры." Covers **three tracks with different
rules**, because they carry different legal/production risks:

1. **Person photos** (mugshots, booking photos, court exhibits showing an identifiable
   individual) — official public-record sources only, always redacted before use.
2. **Non-person photos** (house exteriors, courthouse buildings, evidence items, streets,
   general scenery) — any source is fine, including the news articles already collected in a
   case's `Sources.md`, per the channel owner's explicit decision below.
3. **Archival video clips** (bodycam footage, press-conference clips, court-hearing video,
   911-call audio-only excerpts) — see Track 3 below. New track, added 2026-08-30.

## Interface
```
fetch(case_name: string,
      subjects: [{ name: string, jurisdiction: string }],
      scene_targets: [{ description: string }]) -> {
  person_images: [{
    subject_name: string,
    source_url: string,
    source_type: "mugshot" | "court_exhibit" | "agency_press_release",
    issuing_authority: string,      // e.g. "Fairfax County Sheriff's Office"
    retrieved_date: string,
    license_note: string,           // why this is usable — cite the public-record basis
    redaction: "eyes_blacked",      // mandatory, never "none" for this track
    local_path: string
  }],
  scene_images: [{
    description: string,            // e.g. "exterior of the Banfield home"
    source_url: string,
    outlet: string,
    retrieved_date: string,
    local_path: string
  }],
  not_found: [{ target: string, reason: string }]
}
```

## Track 1 — Person photos (mugshot/booking/court exhibit)

**Source priority (fixed — narrower than `fact_check_tool`'s list, on purpose):**
1. County sheriff / jail booking-photo pages (the original mugshot release).
2. State Department of Corrections inmate-lookup photo pages (post-sentencing).
3. Court exhibit images released directly by the court or prosecutor's office.

Never from news-outlet article pages, stock photo sites, social media scrapes, or third-party
"mugshot lookup" aggregator sites (jailexchange.com-style sites) — those carry their own
copyright/legitimacy problems distinct from the person themselves being a public figure in a
public-record case.

**Exception, decided 2026-07-20 after a real Stage 2 test found this exact case:** a mugshot
*hosted* on a news-outlet page still counts as Track 1 (official source) **if the outlet's own
caption explicitly attributes it to an official issuing authority** — e.g. "(Fairfax County
Police Department)" — rather than crediting the outlet's own photography. The outlet is just
republishing a public record in that case, not claiming it as their work, so the "never from
outlet pages" rule (aimed at avoiding outlet/photographer copyright) doesn't actually apply.
Ambiguous or uncredited outlet photos still don't count — this exception is narrow, only for a
clear, explicit official-source caption.

**Mandatory redaction:** every person photo gets a black rectangle over the eyes before it's
used anywhere in the video. This is the channel owner's own risk-mitigation decision
(2026-07-19) — using the real photo for documentary authenticity while reducing full
identifiability. Never publish the unredacted original.

**Redaction is automated, not manual — confirmed working 2026-07-20 (Stage 2 live test, see
`Cases/brendan-banfield-double-murder/PersonPhotos.md`).** The original "not worth automating
at current volume, do manually until Phase 2" plan was too pessimistic: OpenCV's bundled Haar
cascades (`opencv-python-headless<5` — note v5.0 dropped `cv2.CascadeClassifier` from the main
namespace, install the 4.x line) do this in under a second with no external model download, no
GPU, and no Node/Remotion environment needed — runs fine in this same Phase 1 sandbox.
**Method:**
1. `haarcascade_frontalface_default.xml` to find the face box.
2. Run `haarcascade_eye.xml` **restricted to the upper 60% of the face box only** — running it
   on the whole image produces false positives (nostrils/mouth misdetected as eyes).
3. Draw one black bar spanning both detected eyes, with ~15% horizontal / ~25% vertical margin
   beyond the tightest bounding box, so the bar reads as a deliberate redaction rather than a
   tight, precise crop.
4. If eye detection fails within the face ROI, fall back to a fixed proportional estimate (eyes
   sit ~30-50% down a frontal mugshot face box) rather than leaving the photo unredacted.

**Manual fallback margin bug, found 2026-07-28 in production (Rimoni Muliaga case) — real
consequence, not theoretical:** when BOTH the face cascade and the eye cascade fail (an off-angle
custody/escort photo, not a frontal mugshot — see `Cases/rimoni-muliaga-jealousy-murder/
PersonPhotos.md`), the fallback in that session was a **bare eyeballed box from a debug grid
overlay, with no margin added** — skipping the 15%/25% margin rule above, which only got applied
to the automated-detection path in the code, not written into the manual/human-drawn fallback
path. The box looked correct at full-frame view, but the channel's Remotion Ken-Burns pan/zoom
crops and enlarges the frame — at higher zoom, ~15-20% of the box's own width (the subject's ear
and jaw line) fell outside the box and was visible on the published video. **Root cause: the
redaction box was checked for correctness only at full-frame, static view — never re-checked
after the same image goes through the video's actual zoom/pan treatment, which is a strictly
tighter effective crop than the source frame.** Fix for every future case, no exceptions: (a) the
manual/eyeballed fallback box must add the same 15%/25% margin the automated path already uses,
generously, since a hand-drawn box is a worse estimate than a cascade-detected one, not a better
one; (b) after redacting any real photo whose scene will be Ken-Burns panned/zoomed in Remotion,
re-render or at minimum re-check the redaction at the scene's *maximum* zoom level (the tightest
crop in its `interpolate()` range, both `zoomIn` and `zoomOut` directions in
`Tools/remotion_assembly_tool.md`'s `SceneImage` component), not just the static source file —
a redaction that looks complete in the raw JPG can still leak once the video crops into it.

**Legal grounding (informational research, not legal advice — see
`Documentation/ARCHITECTURE.md`'s "Real-photo sourcing decision" section for the full research):**
the news/commentary ("newsworthy") exception to right-of-publicity claims broadly covers
documentary/true-crime use of a real, adjudicated case's photo, even when the channel is
monetized — courts have found fictionalized content erodes this defense (*Porco v. Lifetime
Entertainment*), which is exactly why this studio's verified-claims-only, no-invented-dialogue
practice matters here beyond just accuracy. Still genuinely state-specific and not a substitute
for an actual media/entertainment lawyer's opinion if higher certainty is wanted before scaling
up.

**Access is a separate, still-unresolved constraint from the legal question:** Fairfax County
(the Banfield case's jurisdiction) has no public mugshot API/database — only a Virginia FOIA
request to the Sheriff's Office. That's a manual, per-case human task, not something this tool
can automate yet for that jurisdiction. Other jurisdictions may differ — check per case.

## Track 2 — Non-person photos (scenes, buildings, evidence, locations)

May be sourced from **any outlet**, including the same news articles already used in
`Sources.md` (CNN, ABC, NBC, WJLA, etc.) — per the channel owner's explicit decision
(2026-07-19) to accept photographer/publication copyright risk for this category, since no
person's right-of-publicity is implicated when no person appears in the photo.

Prefer official/public-domain sources when convenient (Google Street View, court exhibits,
government releases) since they carry zero copyright risk — but this is a preference, not a
hard requirement, for this track specifically.

No redaction needed — there's nothing to redact.

**Escalate to the person-photo track instead of using as-is** if a "non-person" image turns out
on closer look to actually include an identifiable individual in frame (e.g. a house-exterior
photo with a family member visible) — don't publish that unredacted just because it was sourced
as a "scene" photo.

## Track 3 — Archival video clips (bodycam, press conference, court hearing)

**Escalated 2026-08-30, prompted by a real channel audit finding this format gap.** Sourced the
same way Track 2 scene photos are — public official releases and news-outlet coverage of a
genuinely adjudicated case — but the target is a short video clip, not a still, to embed
directly in the Remotion timeline via a `SceneClip` component (see
`Tools/remotion_assembly_tool.md`) instead of a Ken-Burns-panned still image.

**What counts:**
- Police department body-worn-camera footage released publicly (a public-records release, not a
  leak) — often posted directly to the department's own YouTube channel or included in a press
  release.
- Press-conference video (DA/police chief announcing charges or a verdict) — usually on the
  agency's own channel or embedded in outlet coverage.
- Court-hearing video where the jurisdiction livestreams or publishes recordings (varies hugely
  by state/country — many US states allow cameras in court, many don't; check per case).
- A 911 call audio recording released by the agency (audio-only; pairs with a static visual in
  Remotion, but the real audio itself is the point, not a narrated paraphrase).

**Source priority (same officialness bar as Track 1, since a video clip is a stronger
identifiability signal than a still photo):**
1. The issuing agency's own channel/website (police department YouTube channel, DA's office
   press release page, court's own recording archive).
2. An outlet's coverage that clearly re-embeds the agency's own released video (not the outlet's
   own original camera footage of, say, a courtroom sketch artist — that is the outlet's IP).

**Never** use an outlet's own original video journalism (their reporter's stand-up, their own
courtroom camera crew's footage) — that is squarely the outlet's copyrighted work, a different
risk profile from a still photo republishing a public record. If no agency-sourced clip exists
for a moment, that moment stays a real-photo-or-generated scene — don't reach for outlet video.

**Redaction:** any identifiable bystander or minor visible in a bodycam clip needs the same
eyes-blacked treatment as a Track 1 still — for video this means blacking out the region across
the clip's duration, not a single frame. If that's not practical for a given clip, don't use it;
find a shorter excerpt that avoids the bystander, or fall back to a still photo instead.

**Usage in Remotion:** a clip scene replaces a `SceneImage` scene 1:1 in the scene list — same
`[[SCENE:NNNN]]` timing convention, same duration budget, just video content instead of a panned
still. See `Tools/remotion_assembly_tool.md`'s `SceneClip` component. Keep the clip's own audio
muted unless the specific moment calls for it (e.g. a 911 call excerpt) — the channel's narration
track is the primary audio everywhere else.

**Not yet live-tested end-to-end on a real case** — the `SceneClip` Remotion component was built
2026-08-30 in response to this finding, but no case has sourced and embedded a real clip yet.
Treat the first real attempt as a test, same as Track 1 was on the Banfield case.

## Escalate to human when
- A jurisdiction's mugshot-publication rules are unclear or contested (e.g. recently changed
  law, pending litigation about booking-photo publication in that state).
- No public-record person-photo exists for a subject who is nonetheless central to the story
  (the video relies on AI-generated reenactment only for that person — a content decision, not
  a tool decision).
- A "non-person" image turns out to contain an identifiable person on closer inspection.
- A video clip's rights/officialness are ambiguous (agency-sourced vs. outlet's own footage
  unclear) — default to not using it rather than guessing.

## Implementation notes
- Not yet built — this is a draft spec (Stage 1, per `Tests/TEST_PLAN.md`). Before wiring a real
  scraper: confirm current mugshot-availability rules for the specific state(s) involved in the
  chosen case, and check each target site's robots.txt/terms of service for automated-access
  restrictions (a separate concern from copyright, still needs respecting).
- Output feeds Image Generation Agent's asset pool as a secondary source alongside
  `Assets/images/{scene_id}.png`, not as a replacement.

## Status: unblocked (2026-07-19), Track 1 live-tested end-to-end (2026-07-20), MANDATORY per case (2026-07-26)
Previously blocked pending legal review (see git history for the original Stage 2 live-check
note). Unblocked after real research into the newsworthy/documentary exception (favorable, see
above) and an explicit, informed risk decision by the channel owner: use real person photos with
mandatory eye redaction, and accept photographer-copyright risk for non-person photos sourced
from news articles. The Fairfax County FOIA-only access constraint for person photos still
stands separately as the general rule for that jurisdiction — but the outlet-attribution
exception above found a real, usable photo for the Banfield case specifically without needing
that FOIA request. Full pipeline (find → verify official attribution → download → detect →
redact → save) run for real on the Banfield mugshot; Track 2 (non-person) tried on the same
article and found no valid candidate that run — see `Tests/stage2_mugshot_tool_test.md`.

**Escalated 2026-07-26 from "recommended mixing" to "mandatory attempt, every case, no
exceptions."** See `Documentation/ARCHITECTURE.md`'s "Real photos are now MANDATORY per case"
section for the full rationale (YouTube's 2026 AI-slop enforcement policy). Concretely: run
both tracks' fetch step for every new case before Image Generation Agent starts filling gaps
with AI generation. A case may still end up generation-only for a given person/scene if access
is genuinely blocked (a jurisdiction with no API and no outlet-attribution exception, exactly
like the Sementilli LAPD/CDCR case) — but that has to be a documented, checked outcome in the
case's own `PersonPhotos.md` (see the Sementilli case for the template), never a silently
skipped step the way the Kouri Richins production skipped it entirely.
