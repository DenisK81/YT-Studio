# Stage 4 — Full 14-agent pipeline trial through n8n (local, 2026-07-21)

First end-to-end run of the whole agent chain as a real n8n workflow on the local machine,
using standalone API keys (`ANTHROPIC_API_KEY_N8N`, `ELEVENLABS_API_KEY`, `FAL_KEY` in
`.claude/settings.local.json`, gitignored). This is the test the user asked for before
installing anything on the Hetzner VPS.

## What was built

`Fatal Affairs - Master Pipeline (local)` (n8n workflow id `fa11a57e9f01ab2e`, 21 nodes),
generated programmatically by `Workflows/build_master_workflow.py` (keys read from env at
build time, never committed) and imported via `n8n import:workflow` CLI:

- **11 Anthropic LLM nodes** (`claude-opus-4-8`, adaptive thinking, per-node `max_tokens`):
  Research (with server-side `web_search_20260209`), Fact Verification, Story, Scene Planner,
  Voice Production, Image Planning, SEO, Thumbnail, Shorts, Quality Control, Publishing
  (prepare only). System prompt of each node = the full corresponding `Agents/*.md` file,
  passed via a raw-string Set node ("Agent Prompts") so braces in the spec JSON schemas
  don't hit n8n's `{{ }}` templater. Links follow the Stage 3 audited contracts (claim
  flattening for Fact Verification, style_tags merge before fal, `checklist_status` gate).
- **ElevenLabs branch**: Code node splits the voiceover into `=== CHAPTER NN ===` chunks →
  HTTP TTS node (voice `wSChTcAxdiTjLPhHeyrM`, `eleven_multilingual_v2`) → write
  `Assets/audio/.../chapter_NN.mp3`.
- **fal.ai branch**: Code node parses ImagePrompts JSON, merges `style_tags` into the prompt
  string (Image Generation Agent's Stage 3 contract) → Flux schnell → download → write
  `Assets/images/.../NNNN.png`.
- Out of band by design: Video Assembly (local Remotion render, next step), Tool Manager
  (design-time agent, not a runtime node), YouTube publish (always human-gated, no such node
  exists in the workflow at all).

## Run result (case query: "find next true crime candidate case")

Research Agent, via real web search, independently picked **the Brendan Banfield case** —
the exact case this studio already uses as its fixture. Funny, but also a real gap: the
agent had no knowledge of what the channel already covered. **Fixed**: the Research node's
user prompt now carries an ALREADY COVERED exclusion list (Molly Watson/Addie, Banfield).

Produced (all under `Cases/brendan-banfield-double-murder/auto-run-2026-07-21/`):
- ResearchOutput.md (14.5k chars, real sources), FactCheck.md, Script.md (~2,200 words),
  SceneList.json (70 scenes, ~13 min), Voiceover.txt (7 chapters, 12.9k chars),
  ImagePrompts.md (70 prompts), SEO.md, Thumbnail.md, Shorts.md (5 shorts), Checklist.md,
  PublishPlan.md.
- 7 real chapter MP3s (14.2 min total, 128 kbps) in `Assets/audio/banfield_auto/`
  (gitignored) — within the assembly spec's 15% drift tolerance vs the 13-min plan.
- 70 real scene PNGs (1024x576, 34 MB) in `Assets/images/banfield_auto/` (gitignored) —
  spot-checked visually, on-style (dark, cinematic, 16:9, no text).

**The escalation chain worked unprompted**: the auto-run's own web search could source the
victims' names only to Wikipedia (restricted to timeline verification by
`Agents/research_agent.md`), so Story/SEO/Shorts wrote the entire package without asserting
the names, and QC returned `checklist_status: "warning"` demanding a human confirm the
identities from official sources before publish — exactly the designed behavior. (The
earlier manual `Sources.md` for this case already has officially-sourced names; resolving
the escalation is a human step at publish time.) Publishing Agent correctly produced
`awaiting_human_confirmation` instead of a release plan.

## Real failures found and fixed (why this test was worth running)

1. **ElevenLabs concurrency limit (Creator plan: max 5 parallel).** n8n's HTTP Request node
   fires multiple input items near-simultaneously by default → 429 on the 6th chapter.
2. **n8n `batchInterval` spaces request *starts*, it does not wait for responses.** A 2s
   interval still accumulated >5 in-flight TTS requests (each takes 10–20s to generate).
   Fix that actually holds: `batchSize: 1, batchInterval: 20000` — to exceed 5 concurrent,
   a single generation would need >100s. Confirmed working (all 7 chapters, zero 429s).
3. **n8n blocks disk writes outside its own folder by default** ("The file ... is not
   writable" from the Read/Write File node). Fix: run n8n with
   `N8N_RESTRICT_FILE_ACCESS_TO="D:/SHOPS/AI Projects/YT_Crime/YT-Studio"` (must also be set
   on the Hetzner deployment). Bonus find: when a save node fails, the already-generated
   binaries are still recoverable from `~/.n8n/storage/workflows/<wf>/executions/<n>/binary_data/`
   — the 7 TTS chapters were recovered this way with zero re-spend.
4. **SEO node truncated at `max_tokens: 4000`** (adaptive thinking shares the output
   budget). Raised to 8000; clean on re-run.
5. **`n8n execute` exits 1 but still writes full `--rawOutput`** on partial failure — the
   run data (including every successful node's output) is fully salvageable, which is how
   the interrupted first run cost nothing to resume: the completed Research→ImagePlanning
   chain was reused as-is by a continuation workflow instead of re-paying it.

## Cost of the whole trial (approximate)

- Anthropic: 11 Opus calls + 5 re-run calls ≈ $3–4 total.
- ElevenLabs: ~13k characters (one full voiceover), single-spend — the failed first TTS
  attempt was recovered from n8n's binary store, not regenerated.
- fal.ai: 70 Flux schnell images ≈ $0.2–0.7.

## Verdict

The full LLM chain, both asset branches, the Stage 3 contracts, and the escalation/QC/publish
gating all work end-to-end through n8n on this machine. Remaining before Hetzner:
- Remotion render of this trial video from the generated assets (next step, local).
- Human resolution of the QC escalation (victim identities via official sources) before any
  publish of this content.
- On Hetzner: set `N8N_RESTRICT_FILE_ACCESS_TO`, keep the 20s TTS spacing, and use n8n
  credentials store instead of embedded keys (local build script embeds them because the
  local editor-credential flow was already proven unreliable to automate here).
