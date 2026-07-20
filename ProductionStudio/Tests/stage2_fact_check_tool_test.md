# fact_check_tool — Stage 2 live test (2026-07-20)

Real call: `check(claims)` against the Boston murder-for-hire case (Mohammed Chowdhury), found
via the DOJ press-release discovery source added earlier this session — a fresh case not yet in
the `Cases/` backlog, used here specifically to test this tool's contract in isolation.

## Input
```json
{ "claims": [
    "Mohammed Chowdhury was sentenced to 92 months in prison for a murder-for-hire plot targeting his ex-wife and her boyfriend.",
    "Chowdhury pleaded guilty in January 2024 to two counts of use of interstate commerce facilities in the commission of murder-for-hire.",
    "An undercover agent posed as a contract killer to communicate with Chowdhury about the plot.",
    "Chowdhury had been diagnosed with a mental illness that contributed to his actions.",
    "Online commenters called this one of the most disturbing murder-for-hire cases of the year."
  ] }
```
Claims 4 and 5 were deliberately included as bait — nothing in real coverage supports either, to
confirm the tool actually flags rather than rubber-stamps every claim.

## Output
```json
{ "verified": [
    { "claim": "Mohammed Chowdhury was sentenced to 92 months in prison for a murder-for-hire plot targeting his ex-wife and her boyfriend.",
      "source_url": "https://www.justice.gov/usao-ma/pr/boston-man-sentenced-over-six-years-prison-murder-hire-plot-targeting-his-former-wife",
      "outlet": "DOJ / US Attorney, District of Massachusetts" },
    { "claim": "Chowdhury pleaded guilty in January 2024 to two counts of use of interstate commerce facilities in the commission of murder-for-hire.",
      "source_url": "https://www.justice.gov/usao-ma/pr/boston-man-sentenced-over-six-years-prison-murder-hire-plot-targeting-his-former-wife",
      "outlet": "DOJ / US Attorney, District of Massachusetts" },
    { "claim": "An undercover agent posed as a contract killer to communicate with Chowdhury about the plot.",
      "source_url": "https://www.justice.gov/usao-ma/pr/boston-man-sentenced-over-six-years-prison-murder-hire-plot-targeting-his-former-wife",
      "outlet": "DOJ / US Attorney, District of Massachusetts" }
  ],
  "flagged": [
    { "claim": "Chowdhury had been diagnosed with a mental illness that contributed to his actions.",
      "reason": "no supporting source" },
    { "claim": "Online commenters called this one of the most disturbing murder-for-hire cases of the year.",
      "reason": "would need a Reddit/sentiment source, which per the fixed ranking is never usable as verified regardless of whether the sentiment is real" }
  ] }
```

## Result
- Ranking applied correctly: the DOJ press release (tier 1, since the `research_agent.md`
  update this session) was preferred over NBC Boston/Boston Globe/Fox News coverage of the same
  facts, even though those are also credible — tier 1 wins when it directly supports a claim.
- Bait claims 4 and 5 were correctly flagged, not fabricated a citation for — confirms "never
  let this tool fabricate a source URL" holds in practice, not just on paper.
- Secondary outlets found in this search (Boston Globe, Fox News, WWLP, NBC Boston) are credible
  journalism but **not on the fixed priority list** (only AP/ABC/CBS/NBC are, and NBC Boston
  counts as NBC) — this case actually has strong sourcing: DOJ (tier 1) + NBC affiliate (tier 2)
  clearly independent, so it would likely clear the 5-source bar with a couple more pulls,
  unlike some earlier candidates that stalled at 2/5.
