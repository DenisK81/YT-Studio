# CLAUDE.md

## Project

Fatal Affairs — true-crime YouTube channel production studio. `ProductionStudio/` is the
studio's permanent memory: reusable agents, tools, templates, workflows. Read
`ProductionStudio/README.md` and `ProductionStudio/Documentation/ARCHITECTURE.md` before
changing anything in this repo for the first time in a session.

## Current phase

We are still in **Phase 1: manual production, testing the channel hypothesis on the first 10
videos** (see `ProductionStudio/README.md` and the channel's own project brief). Building the
full automated pipeline (n8n, agents wired end to end, auto-publishing) is **Phase 2** and only
starts once explicitly requested — don't self-initiate Phase 2 work from a Phase 1 request.

## Hard rules

- Never push to `main` without explicit approval in this session, even if the change looks
  small or obviously correct.
- Never commit `.env`, API keys, or tokens. Only `.env.example` with empty values belongs in
  git. If you ever need a real key, ask the user to set it as an environment variable or in
  `.claude/settings.local.json` (gitignored) — never type it into a file that gets committed.
- Never call the actual YouTube publish endpoint. `Agents/publishing_agent.md` requires human
  confirmation before every publish, with no exceptions, regardless of how automated the rest
  of the pipeline becomes.
- If a task isn't covered by `ProductionStudio/Documentation/` or `ProductionStudio/Agents/*.md`,
  stop and ask rather than inventing a new approach or a new architecture.
- Before writing a new script or tool, check `ProductionStudio/Tools/tool_registry.json` first.
  Reuse or extend an existing entry when one is close enough — see
  `ProductionStudio/Agents/tool_manager_agent.md`. Register anything new you add.
- Test one agent or tool in isolation before wiring it to the next one — see
  `ProductionStudio/Tests/TEST_PLAN.md`. Don't wire the full chain first and debug it as one
  black box.
- Two candidate approaches that are roughly equally good (choice of image provider, choice of
  hosting detail not already decided in the brief) — surface both and ask, don't silently pick.

## Project facts (don't re-derive these by searching or guessing)

- Orchestrator: n8n, intended to run on the user's existing Hetzner VPS (not yet installed as
  of this writing — confirm current status with the user before assuming it exists).
- Voice: ElevenLabs Studio API.
- Images: fal.ai + Flux `schnell` is the Phase 1 default (see
  `ProductionStudio/Tools/image_gen_tool.md`), with Leonardo.ai/Replicate as fallback providers.
  Midjourney is excluded from automation (no official API) but is fine for one-off manual
  generation in Phase 1.
- Video assembly: Remotion.
- Publishing: YouTube Data API v3, always human-gated.
- First real test case: the Molly Watson / James Addie script. Chapters 6-16 and the ending
  were drafted separately from this repo; chapters 1-5 may or may not be finished yet — ask the
  user for current status rather than assuming.

## Language

Talk to the user in Russian in this session, matching how they write to you. Code, comments,
commit messages, and all Markdown documentation in this repository stay in English — the
channel's audience and output are English-language (US market).

## Style

Prefer plain, working code over speculative abstractions beyond what
`Documentation/ARCHITECTURE.md` already specifies. Don't add new agents, tools, or folders that
aren't in the existing scaffold without flagging it first.
