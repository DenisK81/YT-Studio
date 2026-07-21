# Stage 4 — Full 14-agent pipeline trial through n8n (local, 2026-07-21)

> **Superseded as the Phase 1 default the same day** — see
> `Documentation/ARCHITECTURE.md`'s "Orchestration decision: no n8n / no API key for Phase 1"
> section. This run proved the chain works and surfaced real bugs (fixed below), but its
> ~$4.50 cost + n8n-specific footguns led the channel owner to run the agent chain via Claude
> Code directly instead, for Phase 1 test videos. n8n stays as a working, tested reference for
> a later scale/autonomy decision — this document is not obsolete, just not the current path.

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

## Full trial render (same day, follow-up)

The complete 70-scene video was then rendered locally with Remotion from the generated
assets: `Assets/renders/banfield_auto_draft.mp4` (gitignored) — 1920x1080 @ 30fps,
25,574 frames / 14.21 min, 360 MB, rendered in ~13 min. Composition
(`BanfieldTrial.tsx` in the local remotion project): 7 chapter MP3s sequenced back-to-back,
per-scene timing scaled proportionally to each chapter's *real* audio duration (not the
estimates), alternating-direction Ken Burns per scene with an 8-frame fade-in, karaoke
captions (natural word-count timing, `#A30E15` active word), `bed_07.mp3` looped at -18dB.
Spot-checked frames at the start/middle/end: images on-style, captions correct throughout.
QC-relevant observation: "anonymized face" prompts occasionally render as a literal
mask-like face (seen in a courtroom scene) — human frame review should watch for this.

## Research Agent memory (same day, follow-up)

The re-picked-Banfield problem is now solved structurally, not by a hardcoded list:
`Cases/covered_cases.json` is the channel's covered-case memory, injected into the Research
node's prompt by `Workflows/build_master_workflow.py` on every build (see
`Agents/research_agent.md`'s "Covered-case memory" section). Append a case there the moment
it enters production.

## User feedback on the render, and two real fixes (2026-07-21, second follow-up)

Watching the full render surfaced two things:

**1. Caption drift/mismatch after ~9 minutes, nonsensical near the end.** Root-caused by
diffing `SceneList.json` scene text against `Voiceover.txt` per chapter: chapters 1-6 matched
1:1, but Voice Production Agent's chapter 7 (the longest, and — at ~10 min cumulative — right
where the drift started) came out **74% longer** than its source scenes. Captions were being
built from the scene-list text while the narrator was reading Voice Production's own (longer,
reworded) text — two different texts for the same audio. Fixed at the root, not patched:
- Voice Production Agent's pipeline prompt now requires an inline `[[SCENE:NNNN]]` marker at
  the real start of each scene's narration (`Agents/voice_production_agent.md`, "Caption/scene
  alignment marker" section) — it can still reword/expand freely, the marker just records
  where each scene actually begins in the real narration.
- TTS now calls ElevenLabs' `with-timestamps` endpoint instead of the plain audio endpoint,
  returning real per-character alignment (`Tools/elevenlabs_voice_tool.md`).
- `Workflows/process_pipeline_audio.py` (new) decodes the audio and derives **real per-word
  caption timing and real scene/image boundaries directly from that alignment** — never from
  an estimate. `Tools/remotion_assembly_tool.md`'s caption-timing section documents this fix.
- Validated cheaply: `Workflows/build_voice_regen_workflow.py` (new) re-runs *only* Voice
  Production Agent (now on Sonnet 5) against the already-generated `SceneList.json` — no
  Research/Story/etc. re-run, no re-paying the rest of the chain. Re-render
  (`Assets/renders/banfield_auto_draft.mp4`, overwritten) confirmed captions track the real
  narration throughout, including in what was chapter 7.

**2. Cost.** The first trial run's ANTHROPIC_API_KEY_N8N spend was ~$4.50 (11 Opus 4.8 calls,
inflated further by the ElevenLabs-concurrency re-run above). `Workflows/build_master_workflow.py`
now mixes models: Opus 4.8 stays only on Research, Story, and Quality Control (the
reasoning/accuracy-critical steps); Fact Verification, Scene Planner, Voice Production, Image
Planning, SEO, Thumbnail, Shorts, and Publishing all run on Sonnet 5 ($2/$10 per MTok intro
pricing vs Opus's $5/$25) — expected to roughly halve the per-run Anthropic cost on the next
full run. Not yet re-validated with a fresh full 11-agent run (that costs real money again;
deferred pending the channel owner's go-ahead).

## Verdict

The full LLM chain, both asset branches, the Stage 3 contracts, the escalation/QC/publish
gating, and the Remotion render all work end-to-end on this machine — the complete
case-query → draft-video path has now run for real, locally, with real (not estimated)
audio-caption sync. Remaining:
- Human resolution of the QC escalation (victim identities via official sources) before any
  publish of this content; clause-boundary caption chunking (vs. blind 3-word grouping) is
  still a known cosmetic polish item.
- A fresh full pipeline run to confirm the new Opus/Sonnet mix holds text quality while
  cutting cost — not run yet, since it costs new money.
- On Hetzner: set `N8N_RESTRICT_FILE_ACCESS_TO`, keep the 20s TTS spacing, and use n8n
  credentials store instead of embedded keys (local build script embeds them because the
  local editor-credential flow was already proven unreliable to automate here).
