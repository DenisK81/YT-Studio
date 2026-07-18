# Tool: image_gen_tool

## Purpose
Provider-agnostic image generation wrapper, per Image Policy: the pipeline must never depend
on a single image source.

## Interface
```
generate(prompt: string, style_tags: string[]) -> {
  image_url_or_file
}
```

## Provider options (pick one as default, keep interface stable if switching)
- Midjourney (via Discord + an unofficial API bridge, or a hosted proxy) — highest quality for
  photorealistic documentary style, but historically the least "API-native" of the options.
- Flux via Leonardo.ai, Freepik, or Replicate — more API-friendly, good photorealism.

## Implementation notes
- 80-100 images per video (per the channel's current plan) means this tool will be called in
  batch — build with basic rate-limit/backoff handling from day one, not as an afterthought.
- Never block the pipeline on one failed generation (see Image Generation Agent) — this tool
  should return a clear failure reason (`content_policy`, `timeout`, `rate_limit`, `other`) so
  the calling agent can decide whether to retry.
- Requires provider API key in `Config/.env.example`. Verify current provider API shape before
  building — not tested live from this design pass.
