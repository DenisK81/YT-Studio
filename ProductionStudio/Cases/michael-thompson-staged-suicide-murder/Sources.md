# Sources — Michael Thompson murder of Kimberley Thompson (Bounds)

Second UK case for this channel — continues the standing `Documentation/TREND_LOG.md` finding
that international/lesser-known cases are the fastest-growing corner of the true-crime niche.

| # | Claim | URL | Outlet | Date | Status |
|---|---|---|---|---|---|
| 1 | Official charge announcement: names, ages, charges, court appearance | https://www.northants.police.uk/news/northants/news/in-court/2025/september/man-charged-with-northampton-womans-murder/ | Northamptonshire Police (official) | 2025-09 | search-summary, primary source (direct fetch blocked 403) |
| 2 | Official post-verdict statement: DCI Torie Harrison quote, family tribute | https://www.northants.police.uk/news/northants/news/in-court/2026/july/family-pay-tribute-to-the-kindest-mother-daughter-sister-auntie-and-friend/ | Northamptonshire Police (official) | 2026-07 | search-summary, primary source (direct fetch blocked 403) |
| 3 | CPS prosecutor Emma Cornell's official statement | (CPS East Midlands news, exact URL not resolved — quote corroborated across 3 independent outlets) | Crown Prosecution Service (official) | 2026-07 | search-summary, primary source, quote corroborated |
| 4 | Trial evidence: prosecutor Miranda Moore KC on the Rhonda Anderson threat, defense position | https://www.itv.com/news/anglia/2026-07-08/husband-used-previous-partners-death-to-threaten-estranged-wife | ITV News Anglia | 2026-07-08 | search-summary |
| 5 | Verdict details, staged suicide scene, 999 call, post-mortem findings | https://www.itv.com/news/anglia/2026-07-08/man-guilty-of-raping-and-killing-estranged-wife-then-staging-suicide-scene | ITV News Anglia | 2026-07-08 | search-summary |
| 6 | Sentencing details, judge's quote, Thompson's refusal to attend | https://www.itv.com/news/anglia/2026-07-14/killer-husband-who-tried-to-stage-wifes-suicide-jailed-for-33-years | ITV News Anglia | 2026-07-14 | search-summary |
| 7 | Full case narrative: relationship timeline, staged scene detail, sentence breakdown | https://www.perspectivemedia.com/man-who-raped-and-murdered-wife-and-tried-to-pass-death-off-as-suicide-is-jailed/ | Perspective Media | 2026-07 | direct-fetched |
| 8 | Verdict, trial length, charge count, defendant age at verdict | https://www.northamptonchron.co.uk/news/courts/michael-thompson-56-year-old-found-guilty-of-murdering-and-raping-kimberley-thompson-after-six-week-trial-8784593 | Northampton Chronicle | 2026-07-08 | search-summary (direct fetch blocked 403) |
| 9 | Sentence, minimum term breakdown, sex offenders register | https://www.northamptonchron.co.uk/news/crime/michael-thompson-kimberley-bounds-murderer-and-rapist-to-serve-life-in-prison-with-minimum-term-of-33-years-8798217 | Northampton Chronicle | 2026-07 | search-summary (direct fetch blocked 403) |
| 10 | Family victim-impact statement (sister Dionne Bounds, full quote) | https://www.northamptonchron.co.uk/news/crime/kimberley-bounds-family-pay-emotional-tributes-to-kindest-mother-daughter-sister-auntie-and-friend-as-killer-jailed-for-33-years-8798612 | Northampton Chronicle | 2026-07 | search-summary (direct fetch blocked 403) |
| 11 | Charging detail corroboration | https://www.itv.com/news/anglia/2025-09-18/man-charged-with-murder-and-rape-of-woman-found-dead-in-home | ITV News Anglia | 2025-09-18 | search-summary, corroborating |
| 12 | Defense position at trial (disputes murder to criminal standard) | https://www.nnjournal.co.uk/p/thompsons-lawyer-says-prosecutors | NN Journal | 2026 | search-summary, corroborating |

**Independent-source count: 2 official sources (Northamptonshire Police, Crown Prosecution
Service) + ITV News Anglia + Northampton Chronicle + Perspective Media + NN Journal + BBC
(referenced) = 8+ distinct outlets.** Clears the 5-independent-source minimum decisively.

## Access method note (technical)
`WebFetch` returned HTTP 403 on both Northamptonshire Police official pages and Northampton
Chronicle articles (bot-blocking), consistent with prior UK-outlet access patterns this
session. Worked around via `WebSearch`'s own content summarization, which surfaced direct
quotes (DCI Harrison, prosecutor Miranda Moore KC, judge Nirmal Shant KC, sister Dionne Bounds)
that were then cross-checked for consistency across 3+ independent outlets before being treated
as verified rather than single-source. No image-fetch workaround was needed this case (see
`PersonPhotos.md` for the photo-sourcing attempt and its outcome).

## Flagged for caution
- **Name variation**: the victim is referred to as both "Kimberley Thompson" (married name,
  used by police/BBC in the charge/investigation phase) and "Kimberley Bounds" (used
  consistently by Northampton Chronicle in verdict/sentencing coverage, apparently her family
  name / the name used by her own family in tributes). Script.md should introduce her once by
  both names, then use "Kimberley" or "Kim" throughout, matching how her own sister referred to
  her in the victim-impact statement.
- **Rhonda Anderson's 2000 death**: reported as ruled accidental (electrocution, radio fell into
  bathwater) by the original inquest, with a "murder inquiry opened in 2025" per ITV — but no
  source found confirms Thompson was ever charged in connection with Anderson's death, only that
  prosecutors say he used the "unusual circumstances" of her death to threaten Kimberley. Script
  must not imply Thompson was convicted of or charged with killing Anderson — only that he
  invoked her death as a threat, and that a review/inquiry into it was reported as opened.
- **Cause of death terminology**: most sources say "suffocated"; one ITV headline says
  "raped and strangled" — treated as the same underlying act described two ways by different
  headline writers, not a factual conflict; script uses "suffocated" as the majority/CPS-aligned
  term.
- **Defense's actual trial position**: per NN Journal, the defense argued prosecutors could not
  prove to the criminal standard that Kimberley was killed at all (implying an accident/suicide
  defense) — noted for balance in FactCheck.md; the jury's unanimous guilty verdict after a
  6-week trial is the resolved legal fact the script follows.
