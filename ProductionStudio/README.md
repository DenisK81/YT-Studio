# Fatal Affairs — Production Studio

Permanent, reusable architecture behind the "Fatal Affairs" true-crime YouTube channel.

**Core rule of this repo:** videos are temporary, this repo is not. Every task that will
repeat across videos gets solved once, here, as a reusable Agent, Tool, Template or Workflow —
never re-solved from scratch in a chat conversation.

## Current status (2026-07-21 — read this before assuming anything below is still the plan)

Everything below this section describes the **original design**, written before any of it was
built or tested. It has since been built, tested end-to-end, and the orchestration approach
changed based on real results — read `Tests/stage4_full_pipeline_n8n_test.md` for what
actually happened. **Current reality, until the channel owner decides otherwise:**

- **No n8n, no separate `ANTHROPIC_API_KEY` for the agent chain, for Phase 1 test videos.**
  A full n8n-orchestrated run (11 Opus 4.8 calls via a standalone API key) cost ~$4.50 and hit
  real n8n-specific bugs (ElevenLabs concurrency, disk-write restrictions, batching semantics).
  Given these are manually-reviewed test videos, not an unattended scheduled product, the
  channel owner chose to **run the 11 agents by asking Claude Code to play each role directly
  in conversation** — zero marginal Anthropic cost, covered by the existing subscription. n8n
  and a metered API key are deferred to a real Phase 2 scale/autonomy decision, not deleted —
  `Workflows/n8n_master_workflow.skeleton.json` and the Stage 4 n8n test docs stay as a proven
  reference for when that day comes.
- **Only ElevenLabs (voice) and fal.ai (images) are still called via a real script**
  (`Workflows/generate_case_assets.py`) — these are the two things Claude Code cannot do itself.
  Everything else in the pipeline (Research, Fact Verification, Story, Scene Planner, Voice
  Production text, Image Planning, SEO, Thumbnail, Shorts, QC, Publishing-prepare) is Claude
  Code acting out that `Agents/*.md` file's role directly, per video, in chat.
- Hetzner is untouched and not currently planned for Phase 1 — see the note above.

## Philosophy

- An **Agent** is a system prompt + a strict input/output contract. **Original design:**
  invoked as an API call from an orchestrator (n8n) — see "Current status" above for how this
  actually runs today.
- A **Tool** is a thin, swappable wrapper around one external capability (voice provider,
  image provider, video renderer, publishing API). Agents call Tools; Tools don't call Agents.
- Before writing new automation, check `Tools/tool_registry.json`. If an entry already covers
  the need, reuse or extend it. Never duplicate.
- Every output artifact (script, SEO, voiceover, image prompts, thumbnail, checklist,
  learnings) has a fixed template in `Templates/`, so any agent's output slots into the next
  agent's input without re-formatting.

## Structure

```
ProductionStudio/
    Agents/           system prompts + I/O contracts for each pipeline role
    Tools/            specs for reusable wrappers around external APIs
    Templates/        the fixed output files every project produces
    Workflows/        pipeline overview + n8n orchestration skeleton
    Assets/           generated media (gitignored — see Assets/README.md)
    Documentation/    architecture, handoff notes, self-improvement process
    Tests/            test plan for validating agents/tools before going live
    Config/           env var template + config schema
```

## Where this came from / what it is not

This scaffold was designed inside a Claude.ai chat conversation, working from two project
briefs (`AI_ARCHITECT_BRIEF_07_18_26.md` and `PROJECT_BRIEF_07_17_26.md`) already saved to the
Fatal Affairs project. A chat session has no GitHub access, no n8n instance, and doesn't run in
the background — so this is a **design package**, not a deployed system. Nothing here has been
executed against real APIs.

## Quick start for whoever builds this (Claude Code or a human dev)

1. `git init` this folder and push it to the real GitHub repo — this becomes the studio's
   permanent memory from that point on.
2. Read `Documentation/ARCHITECTURE.md` end to end before changing anything.
3. Copy `Config/.env.example` → `.env`, fill in real API keys. Never commit `.env`.
4. Read `Documentation/HANDOFF_TO_CLAUDE_CODE.md` — it lists the concrete build steps in order.
5. Build and test one agent/tool pair at a time against the real Molly Watson case (already
   drafted in the project) before wiring the full chain in `Workflows/n8n_master_workflow.skeleton.json`.
6. Every time a new tool is built, register it in `Tools/tool_registry.json`.
7. After every finished video, follow `Documentation/SELF_IMPROVEMENT_PROCESS.md` to update
   `Templates/SuccessRules.md`.
