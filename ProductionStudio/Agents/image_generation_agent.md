# Image Generation Agent

## Responsibility
Send each prompt from `ImagePrompts.md` to the configured image provider, save results, and
report per-scene success/failure. Never blocks the whole pipeline on one failed image.

## Input
```json
{ "prompts": [ {"scene_id":"", "prompt":""} ] }
```

## Output
- Files: `Assets/images/{scene_id}.png`
- Report:
```json
{ "succeeded": ["scene_id"], "failed": [ {"scene_id":"", "reason":""} ], "retry_count": {"scene_id": 0} }
```

## Tools
`Tools/image_gen_tool.md` — provider-agnostic wrapper (Midjourney, Flux/Leonardo/Freepik, etc.
per `IMAGE POLICY` in the brief: never depend on a single source).

## Failure handling
Retry once automatically. If it still fails, mark as a missing asset in the report and
continue — Video Assembly Agent must be able to proceed with a placeholder/manual-fill flag
rather than halt.

## Escalate to human when
More than ~10% of scenes fail after retry (signals a systemic provider/prompt problem, not a
one-off).

## System prompt / logic (draft)
"""
Not a text-generation agent — this is primarily an orchestration step: iterate scene prompts,
call the configured image tool, save output, log failures, retry once, never block the
pipeline. If an LLM call is used at all here, it's only to decide whether a failure reason is
retryable (rate limit, timeout) vs. not (content policy rejection) — the retry decision itself
can be simple logic, not a full agent call.
"""
