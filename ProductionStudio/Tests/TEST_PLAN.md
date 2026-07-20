# Test Plan

Test bottom-up: one agent/tool alone, then one link, then the full chain. Never wire the whole
pipeline first and debug it as one black box.

## Stage 1 — Agents in isolation
For each `Agents/*.md`, send a single real request (use the Molly Watson case already drafted
in `fatal-affairs-project-brief.md` as the fixture) and check the output matches the schema in
that agent's file exactly. Do this for all 14 agents before connecting any two together.

## Stage 2 — Tools in isolation
For each `Tools/*.md`, make one real call against the actual provider (small/cheap request —
e.g. generate 1 test image, 1 short voice clip) and confirm the response shape matches what the
tool spec assumes. Update the spec file if the real API differs — these were written without
live verification.

## Stage 3 — Two-node links
Research → Fact Verification. Fact Verification → Story. Story → Scene Planner. Scene Planner
→ Voice Production. Scene Planner → Image Planning. Image Planning → Image Generation. Voice +
Images → Assembly. Assembly → Shorts (runs immediately after the render, not a later pass).
Shorts + Thumbnail + SEO → QC. QC → Publishing (prepare only, no real publish call yet).

**Audited 2026-07-20** (`Tests/stage3_link_audit.md`) — checked every link's actual declared
output against the next agent's actual declared input, not just re-running agents with
hand-fed data. Found and fixed 4 real schema mismatches (Research→FactVerification claim
derivation, ImagePlanning→ImageGeneration style_tags merging, VoiceProduction→Assembly missing
audio-file convention, QC→Publishing field name mismatch) — see the linked audit and
`Documentation/ARCHITECTURE.md`'s "Stage 3 link contracts" section. This was a schema audit, not
a live n8n rewiring (that's Stage 4/Phase 2 territory) — but every link listed above was
exercised at least once with real chained data during this session's Banfield case work.

## Stage 4 — Full chain, one real case, dry-run publish
Run the Molly Watson case end to end once chapters 1-5 exist. Stop at the human-confirmation
gate before Publishing Agent's actual YouTube call — verify everything up to that point without
actually publishing.

## Stage 5 — First real publish
Only after Stage 4 passes clean. Use the channel owner's own release pacing (main video + 1
short day one, remaining 4 shorts one per day) for the first real upload.

## Regression check
After any change to an agent prompt or tool, re-run Stage 1/2 for just that component before
assuming the full chain still works.
