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

**Mandatory redaction:** every person photo gets a black rectangle over the eyes before it's
used anywhere in the video. This is the channel owner's own risk-mitigation decision
(2026-07-19) — using the real photo for documentary authenticity while reducing full
identifiability. Never publish the unredacted original.
- **Phase 1 (current, low volume — ~1-2 subject photos per video):** redact manually in
  standard image-editing software before the file is used.
- **Phase 2 (once this tool is actually automated):** use a face-landmark detection step to
  locate the eye region and draw the bar programmatically. Not worth building this automation
  at current volume — do it manually until Phase 2 wiring.

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

## Status: unblocked (2026-07-19)
Previously blocked pending legal review (see git history for the original Stage 2 live-check
note). Unblocked after real research into the newsworthy/documentary exception (favorable, see
above) and an explicit, informed risk decision by the channel owner: use real person photos with
mandatory eye redaction, and accept photographer-copyright risk for non-person photos sourced
from news articles. The Fairfax County FOIA-only access constraint for person photos still
stands separately and isn't resolved by this decision — that's a manual task per case.
