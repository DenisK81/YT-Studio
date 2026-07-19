# Tool: mugshot_fetch_tool

## Purpose
Fetch real photos for a case (booking photos, official court exhibits, agency press-release
images) from **public-record sources only** — never from the news-article pages already
collected in a case's `Sources.md`. Output is meant to be mixed with Image Generation Agent's
AI-generated reenactment stills, not to replace them.

**This is deliberately narrower than "any photo of this case on the internet."** News-outlet
photos (AP wire images, staff photography on CNN/NBC/ABC/WJLA articles, etc.) are excluded on
purpose — those are the same articles already cited in `Sources.md` for facts, and their
images are almost always copyrighted by the outlet or photographer. Reusing them in a
monetized video is a real copyright-strike risk. Booking photos and official court/agency
releases are a different legal category (public record in most US states) and are the only
thing this tool should touch.

## Interface
```
fetch(case_name: string, subjects: [{ name: string, jurisdiction: string }]) -> {
  images: [{
    subject_name: string,
    source_url: string,
    source_type: "mugshot" | "court_exhibit" | "agency_press_release",
    issuing_authority: string,      // e.g. "Fairfax County Sheriff's Office"
    retrieved_date: string,
    license_note: string,           // why this is usable — cite the public-record basis
    local_path: string
  }],
  not_found: [{ subject_name: string, reason: string }]
}
```

## Source priority (fixed — narrower than fact_check_tool's list, on purpose)
1. County sheriff / jail booking-photo pages (the original mugshot release).
2. State Department of Corrections inmate-lookup photo pages (post-sentencing).
3. Court exhibit images released directly by the court or prosecutor's office (press releases,
   official case filings that include images).

Never: news-outlet article pages, stock photo sites, social media scrapes, or any image whose
copyright holder is a photographer/publication rather than a government agency.

## Legal notes (do not skip)
- Mugshot public-record rules vary by state — some states restrict or require removal of
  pre-conviction booking photos, or limit republication (a handful have "mugshot extortion"
  laws aimed at removal-fee sites, which is a different issue but signals this area is legally
  active). **Check the specific state's current rule before fetching, don't assume "public
  record" applies uniformly.**
- If a subject was never booked (e.g. released on summons, or a jurisdiction that doesn't
  publish booking photos), that's an expected `not_found`, not a reason to fall back to a
  copyrighted news photo instead.
- `license_note` on every saved image exists so the channel has a defensible record of *why*
  each real photo was safe to use, in case of a future takedown dispute.

## Escalate to human when
- A jurisdiction's mugshot-publication rules are unclear or contested (e.g. recently changed
  law, pending litigation about booking-photo publication in that state).
- No public-record image exists for a subject who is nonetheless central to the story (signals
  the video may need to rely on AI-generated reenactment only for that person, which is a
  content decision, not a tool decision).

## Implementation notes
- Not yet built — this is a draft spec (Stage 1, per `Tests/TEST_PLAN.md`). Before wiring a
  real scraper: confirm current mugshot-availability rules for the specific state(s) involved
  in the chosen case, and check each target site's robots.txt / terms of service for
  automated-access restrictions (some sheriff/DOC sites explicitly prohibit scraping even
  though the photos themselves are public record — that's a separate access restriction, not a
  copyright one, but still needs respecting).
- Output feeds Image Generation Agent's asset pool as a secondary source alongside
  `Assets/images/{scene_id}.png`, not as a replacement — see `Agents/image_generation_agent.md`.

## Stage 2 live-check result (2026-07-19) — BLOCKED, needs legal review
Ran a real lookup for the Banfield case (Fairfax County, VA) before trusting this spec's shape:
- Fairfax County **does not run a public online mugshot database** — official access is via a
  Virginia FOIA request to the Sheriff's Office, not an API or scrape. Not automatable as
  originally envisioned for this jurisdiction.
- Third-party "mugshot lookup" aggregator sites (jailexchange.com,
  *.govbackgroundchecks.com, etc.) exist but are exactly the kind of source this spec already
  excludes — not an official record, and some of this site category has been the target of
  "mugshot extortion" litigation.
- **Bigger problem than access:** general guidance found is that mugshots **cannot be used for
  commercial purposes without consent of the person pictured**. A monetized YouTube channel is
  commercial use, and consent from a convicted subject is not realistically obtainable. This
  undercuts the core assumption that "official mugshot = safe to use" for this channel's use
  case, independent of the access-method problem above.
- **Status: blocked pending legal review.** Do not wire this tool for automated use until a
  human confirms (a) whether the commercial-use/consent restriction actually applies to
  documentary/news-commentary YouTube content the way it applies to straightforward commercial
  reuse, and (b) whether court-released exhibit photos (released by a prosecutor's office in a
  press briefing, rather than a jail booking photo) are a cleaner alternative category with
  different terms.
