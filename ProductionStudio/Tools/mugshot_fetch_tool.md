# Tool: mugshot_fetch_tool

## Purpose
Fetch real photos for a case to mix with Image Generation Agent's AI-generated reenactment
stills, not to replace them. Covers **two tracks with different rules**, because they carry
different legal risks:

1. **Person photos** (mugshots, booking photos, court exhibits showing an identifiable
   individual) — official public-record sources only, always redacted before use.
2. **Non-person photos** (house exteriors, courthouse buildings, evidence items, streets,
   general scenery) — any source is fine, including the news articles already collected in a
   case's `Sources.md`, per the channel owner's explicit decision below.

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

## Escalate to human when
- A jurisdiction's mugshot-publication rules are unclear or contested (e.g. recently changed
  law, pending litigation about booking-photo publication in that state).
- No public-record person-photo exists for a subject who is nonetheless central to the story
  (the video relies on AI-generated reenactment only for that person — a content decision, not
  a tool decision).
- A "non-person" image turns out to contain an identifiable person on closer inspection.

## Implementation notes
- Not yet built — this is a draft spec (Stage 1, per `Tests/TEST_PLAN.md`). Before wiring a real
  scraper: confirm current mugshot-availability rules for the specific state(s) involved in the
  chosen case, and check each target site's robots.txt/terms of service for automated-access
  restrictions (a separate concern from copyright, still needs respecting).
- Output feeds Image Generation Agent's asset pool as a secondary source alongside
  `Assets/images/{scene_id}.png`, not as a replacement.

## Status: unblocked (2026-07-19), Track 1 live-tested end-to-end (2026-07-20)
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
