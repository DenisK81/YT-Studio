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
- **Endpoint shape**: verified live 2026-07-19 (Stage 2 test, see below) — matches current docs.

## Stage 2 live-test result (2026-07-19)
Real call against the Banfield case, scene 0001 from `ImagePrompts.md`:
- **Endpoint**: `POST https://fal.run/fal-ai/flux/schnell`, header `Authorization: Key $FAL_KEY`.
- **Request body confirmed**: `{ prompt, image_size, num_images, output_format }` — used
  `image_size: "landscape_16_9"` for the fixed 16:9 style rule; produced a 1024x576 image
  (correct 16:9 ratio).
- **Response shape confirmed**: `{ images: [{url, width, height, content_type}], prompt, seed,
  has_nsfw_concepts, timings }` — matches current fal.ai docs exactly.
- **Cost/latency**: inference time ~0.11s per the response `timings` field; well within the
  ~$0.003–0.01/image estimate above.
- **⚠ "no text" style rule is not reliably honored by the model**: the generated image (two
  police cruisers outside a house) rendered a legible "POLICE" decal on one vehicle despite
  `no text` being in the prompt. This is a known limitation of diffusion models with text in
  the scene concept (police cars, signage, badges) — the prompt constraint reduces but doesn't
  eliminate it. **Quality Control Agent needs to actually visually check for stray
  text/logos/watermark-like artifacts per image, not just trust that "no text" in the prompt
  was sufficient.** Worth a note in `Agents/quality_control_agent.md` if this keeps recurring
  across scenes.

## Fallback / secondary providers (keep the interface provider-agnostic)
- Leonardo.ai API — separate pay-as-you-go balance (starts with its own free credit), useful
  as a second source if fal.ai has an outage or a specific model isn't available there.
- Replicate — same Flux models, per-second/per-image billing, good drop-in alternative.
- Midjourney — deliberately NOT used for automation: no official API, Discord-only, would
  require unofficial workarounds. Fine for one-off manual generation in Phase 1 if someone
  wants to hand-pick a specific image, but never wire it into this tool's automated path.
- **fal.ai's `fal-ai/nano-banana` (Gemini 2.5 Flash Image)** — same-prompt comparison run
  2026-07-19 on scene 0001: honored "no text" better than Flux schnell and produced a more
  detailed/textured result, but (a) its response omits `width`/`height` (`null` in the JSON,
  unlike Flux's clean shape — would need a follow-up call or local image inspection to get
  dimensions if wired in), (b) adds an extra `description` text field not present in Flux's
  response, and (c) costs ~$0.039/image vs Flux's ~$0.003–0.01 — roughly 4–13x more, which at
  80-100 images/video would blow past the "near-free at test volume" budget this default was
  chosen for. **Decision (2026-07-19): keep Flux schnell as the default for all scenes** — not
  worth the cost multiplier for the whole batch. Revisit as a possible hero-shot/thumbnail-only
  override later if quality on those specific shots matters enough to justify the per-image
  cost (mirrors the existing flux-pro-for-hero-shots idea above).

## Stage 4 live-test result (2026-07-20/21) — confirmed working through n8n, not just direct Python
Ran the exact same request contract through a real local n8n instance (`npx n8n`, no Docker) as
an HTTP Request node — see `Tests/stage4_n8n_local_bootstrap.md` for the full setup/friction
notes. Result: `executionStatus: "success"`, real image returned (1024x576, correct 16:9),
identical shape to the direct-Python Stage 2 test above. **This is the first node of
`Workflows/n8n_master_workflow.skeleton.json` (`image_generation_loop`) confirmed as a working
HTTP Request configuration, not just a placeholder node type.**

## Implementation notes
- 80-100 images per video (per the channel's current plan) means this tool will be called in
  batch — build with basic rate-limit/backoff handling from day one, not as an afterthought.
- Never block the pipeline on one failed generation (see Image Generation Agent) — this tool
  should return a clear failure reason (`content_policy`, `timeout`, `rate_limit`, `other`) so
  the calling agent can decide whether to retry.
- Track spend against the free credit (fal.ai dashboard) during the test phase so there's no
  surprise bill — Tool Manager Agent can log cumulative spend per video in a future iteration.
