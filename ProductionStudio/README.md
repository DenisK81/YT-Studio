# Fatal Affairs — Production Studio

Permanent, reusable architecture behind the "Fatal Affairs" true-crime YouTube channel.

**Core rule of this repo:** videos are temporary, this repo is not. Every task that will
repeat across videos gets solved once, here, as a reusable Agent, Tool, Template or Workflow —
never re-solved from scratch in a chat conversation.

## Philosophy

- An **Agent** is a system prompt + a strict input/output contract. It is invoked as an API
  call from the orchestrator (n8n) — it is not a separate standing AI that runs on its own.
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
