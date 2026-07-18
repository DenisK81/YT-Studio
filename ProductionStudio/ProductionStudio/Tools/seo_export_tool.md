# Tool: seo_export_tool

## Purpose
Pure formatting step: takes SEO Agent's structured JSON output and writes it into the fixed
`Templates/SEO.md` layout, so every project's SEO file looks identical regardless of which
model/run produced it.

## Interface
```
export(seo_json: {
  titles, description, chapters, pinned_comment, tags, hashtags
}) -> "Templates/SEO.md content"
```

## Implementation notes
- No LLM call needed — this is a template-fill function, not an agent. Keep it that way; don't
  let "everything is an agent" creep turn simple formatting into an unnecessary API call.
