# Tool: fact_check_tool

## Purpose
Reusable wrapper used by Research Agent and Fact Verification Agent. Wraps web search/fetch
with the channel's fixed source-priority ranking, so "which sources count as authoritative"
lives in one place, not copy-pasted into every prompt.

## Interface
```
check(claims: string[]) -> {
  verified: [{ claim, source_url, outlet }],
  flagged:  [{ claim, reason }]
}
```

## Source ranking (fixed)
1. FBI / court documents / police reports
2. AP, ABC, CBS, NBC News
3. People, CourtTV, Law&Crime, Oxygen
4. Wikipedia — timeline cross-check only, never sole source for a claim
5. Reddit — sentiment only, never usable as `verified`

## Implementation notes
- If built on the Anthropic API: use the built-in web_search tool, then apply the ranking
  above as a post-filter over returned domains before accepting a source as "verified."
- If built in n8n directly: a SerpAPI/Google Custom Search node + a domain-allowlist filter
  function node achieves the same thing without an LLM call for the ranking step itself.
- Never let this tool fabricate a source URL. If nothing supporting a claim is found, it goes
  to `flagged`, not `verified`.
