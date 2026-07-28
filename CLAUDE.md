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
- **Real photos are mandatory per case, not optional** (escalated 2026-07-26 — see
  `Documentation/ARCHITECTURE.md`). Run both `Tools/mugshot_fetch_tool.md` tracks for every case
  before letting Image Generation fill gaps with AI. Never ship a case 100% AI-generated — real,
  downloaded crime-scene/court photos are the concrete evidence this channel isn't YouTube's
  targeted 2026 "AI slop" (mass-produced template content, three-strike enforcement policy).
  Every identifiable real person in any real photo gets eyes-blacked or blurred before use, no
  exceptions. If access is genuinely blocked, document the attempt and the wall hit in that
  case's `PersonPhotos.md` — never silently skip the step.
- Before every publish, check YouTube Studio's "Altered or synthetic content" disclosure toggle
  for videos containing realistic AI-generated scenes — a human click in Studio, not something
  the API sets.

## Project facts (don't re-derive these by searching or guessing)

- Orchestrator: n8n, intended to run on the user's existing Hetzner VPS (not yet installed as
  of this writing — confirm current status with the user before assuming it exists).
- Voice: ElevenLabs Studio API.
- Images: fal.ai + Flux `schnell` is the Phase 1 default (see
  `ProductionStudio/Tools/image_gen_tool.md`), with Leonardo.ai/Replicate as fallback providers.
  Midjourney is excluded from automation (no official API) but is fine for one-off manual
  generation in Phase 1.
- Video assembly: Remotion.
- Publishing: YouTube Data API v3, always human-gated. Real implementation:
  `ProductionStudio/Workflows/youtube_agent.py` (see `Tools/youtube_publish_tool.md`).
- **Publishing timezone: America/Los_Angeles (Pacific), confirmed 2026-07-26.** All release
  scheduling is planned in LA local time and converted to UTC for the API's `publishAt` field —
  compute the conversion with a real timezone library (e.g. Python `zoneinfo`), never hardcode
  UTC-7/UTC-8, since LA switches between PDT and PST across the year.
- **Playlists are by theme/motive, never by case name** (decided 2026-07-26, replacing an
  earlier "one playlist per case" attempt the channel owner rejected after checking how
  competitor true-crime channels organize theirs). Examples already in use: `Love Triangle
  Murders`, `Wife Killed Husband`, `Murder For Insurance Money`, `Framed The Wrong Person`. A
  single video normally belongs in 2-3 of these at once (e.g. a wife-and-lover insurance-murder
  case is both `Wife Killed Husband` and `Murder For Insurance Money` and `Love Triangle
  Murders`) — that overlap is expected and fine, not a bug. When a new case is produced, decide
  its 2-4 fitting themes from the existing playlist set first; only create a new themed
  playlist if the case genuinely doesn't fit any existing one. Created via `youtube_agent.py`'s
  `get_or_create_playlist()` (idempotent by title) and `add_video_to_playlist()`, added as soon
  as each video is uploaded, not batched up later.
- First real test case: the Molly Watson / James Addie script. Chapters 6-16 and the ending
  were drafted separately from this repo; chapters 1-5 may or may not be finished yet — ask the
  user for current status rather than assuming.
- **Every video/Short description must end with the channel name + a working link**
  (`Workflows/youtube_agent.py`'s `CHANNEL_FOOTER` constant, currently
  `https://www.youtube.com/@fatalaffairs-f1i`) — confirmed 2026-07-26 after a real viewer
  commented on a published Short asking which channel it was from. Retroactively applied to all
  20 videos already on the channel that day. Never leave a bracket placeholder like `[link to
  X]` in description text meant to be pasted directly into YouTube — resolve it to a real value
  or drop the line.

## Language

Talk to the user in Russian in this session, matching how they write to you. Code, comments,
commit messages, and all Markdown documentation in this repository stay in English — the
channel's audience and output are English-language (US market).

## Style

Prefer plain, working code over speculative abstractions beyond what
`Documentation/ARCHITECTURE.md` already specifies. Don't add new agents, tools, or folders that
aren't in the existing scaffold without flagging it first.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships. **Treat it as this project's actual memory** — for questions about architecture, agents, tools, or what happened on a past case, query the graph before grepping/reading files cold or relying on your own session recall. The point is for the graph to know the project so you don't have to hold it all in your head.

Rules:
- For any question about architecture, agents, tools, or a past case ("what does X agent do", "what happened with case Y", "why was Z decided"), first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- **This project's real content is almost entirely Markdown/JSON docs, not code** — case files
  under `ProductionStudio/Cases/*/`, agent specs under `ProductionStudio/Agents/`, tool specs
  under `ProductionStudio/Tools/`. The bare `graphify update .` CLI command is **AST-only** and
  silently skips all of these (confirmed 2026-07-25: it re-extracts `.py`/code but leaves new
  case docs completely un-indexed). **After producing or editing any case file, agent spec, or
  tool spec, run the full `/graphify --update` flow** (the skill's incremental semantic path —
  detect changed docs, dispatch extraction subagents, merge, rebuild) **before ending the
  session** — not just the bare CLI command. Skipping this is exactly how the graph went stale
  and didn't know about a fully-produced case (Monica Sementilli) until caught and fixed.
- If the merge step ever refuses to write with a "would shrink the graph" warning, don't just
  force it — check whether the nodes being removed are real content or empty `_origin: ast`
  stub nodes with no edges (a byproduct of running the bare code-only update over doc files by
  mistake). Only force through once you've confirmed it's the latter.
