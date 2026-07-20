# mugshot_fetch_tool — Stage 2 live test (2026-07-20)

Attempted a real Track 2 (non-person) download for the Banfield case, per the channel owner's
2026-07-19 decision that non-person photos may come from any outlet already cited in
`Sources.md`.

## What was tried
Fetched the WJLA timeline article (already a cited source) via both raw HTML parsing and a
real browser, looking for a downloadable non-person image (e.g. house exterior) with a clear
caption confirming what it shows.

## Result: no clean Track 2 candidate found in this article
Every photo in this specific article that has a readable caption is either:
- A generic/stock courthouse-adjacent photo credited "(7News)" — not clearly the Banfield case.
- **Mugshot of Brendan Banfield — captioned "(Fairfax County Police Department)"**
- **Photo of Juliana Peres Magalhaes — captioned "(Fairfax County police)"**
- A court-evidence photo of a framed picture on a nightstand, credited "(Court docs)" — still
  shows people (Banfield and Peres Magalhaes), not a Track 2 candidate.

Raw HTML parsing turned up 55 `<img>` tags, but most are site-template/related-story thumbnails
with no caption tying them to this case — downloading blind from an unlabeled thumbnail list
risked grabbing the wrong image entirely, so none were used. **Correct outcome: report nothing
found, don't force a guess.**

## Unexpected real finding — a Track 1 nuance worth a follow-up decision
Both mugshots in this article carry an **explicit official-source caption** ("Fairfax County
Police Department" / "Fairfax County police"), not a WJLA/7News photo credit. This is a
different situation than `mugshot_fetch_tool.md`'s Track 1 rule was written for — that rule
says "never from news-outlet article pages," aimed at avoiding outlet/photographer copyright on
the outlet's *own* photography. Here, the outlet is transparently republishing an
officially-sourced police photo, not claiming their own photographic credit.

**Not resolved here — flagging for a human call:** does a clearly-attributed police photo
hosted on a news outlet's page count as "from an official source" (the underlying content) or
"from a news-outlet page" (the hosting/file)? The letter of the current rule says no; the
substance of the rule (avoid outlet/photographer copyright) arguably doesn't apply since the
outlet isn't claiming the photography as their own. Did not download or use this image pending
that decision — mugshot access for this case is still effectively blocked in practice (the
Fairfax FOIA-only constraint stands), this is only a note about the rule's edge case for future
reference, not a resolution.
