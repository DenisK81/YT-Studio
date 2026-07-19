# Tool: image_gen_tool

## Purpose
Provider-agnostic image generation wrapper, per Image Policy: the pipeline must never depend
on a single image source. Default provider is set below for the test phase (Phase 1, first 10
videos) — chosen for cost, not locked in permanently.

## Interface
```
generate(prompt: string, style_tags: string[]) -> {
  image_url_or_file
}
```

## Default provider: fal.ai + Flux

Chosen for the test phase because it has a real API (unlike Midjourney, which is Discord-only
with no official API) and is effectively free at this volume:

- **Model**: `flux/schnell` for most scenes (fast, cheap, commercially licensed open weights).
  Reserve a pricier model (`flux-pro` or similar) only for the thumbnail / hero shots if
  `flux/schnell` quality isn't good enough there — see `Agents/thumbnail_agent.md`.
- **Cost**: ~$0.003-0.01 per image on `schnell`. At 80-100 images/video, that's roughly
  $0.25-1.00 per video — a new fal.ai account starts with $20 free credit, which covers the
  entire 10-video test phase with room to spare.
- **Auth**: `FAL_KEY` (or equivalent per current fal.ai docs) in `Config/.env.example` /
  n8n credential store. Never commit the real key.
- **Endpoint shape**: verify against fal.ai's current docs before wiring the n8n node — this
  spec was written without a live test call.

## Fallback / secondary providers (keep the interface provider-agnostic)
- Leonardo.ai API — separate pay-as-you-go balance (starts with its own free credit), useful
  as a second source if fal.ai has an outage or a specific model isn't available there.
- Replicate — same Flux models, per-second/per-image billing, good drop-in alternative.
- Midjourney — deliberately NOT used for automation: no official API, Discord-only, would
  require unofficial workarounds. Fine for one-off manual generation in Phase 1 if someone
  wants to hand-pick a specific image, but never wire it into this tool's automated path.

## Implementation notes
- 80-100 images per video (per the channel's current plan) means this tool will be called in
  batch — build with basic rate-limit/backoff handling from day one, not as an afterthought.
- Never block the pipeline on one failed generation (see Image Generation Agent) — this tool
  should return a clear failure reason (`content_policy`, `timeout`, `rate_limit`, `other`) so
  the calling agent can decide whether to retry.
- Track spend against the free credit (fal.ai dashboard) during the test phase so there's no
  surprise bill — Tool Manager Agent can log cumulative spend per video in a future iteration.
