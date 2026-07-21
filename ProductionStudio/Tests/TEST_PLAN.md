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

**Partially started 2026-07-20/21 (local Phase 2 bootstrap, not the full chain yet):**
Node.js/Remotion/n8n were all missing from this machine — installed/scaffolded them and ran two
real infrastructure tests: (1) a real Remotion render using actual Banfield assets, confirmed
correct visually (`Tests/stage4_remotion_local_render_test.md`); (2) a real n8n workflow
(imported/executed via CLI, since browser-UI canvas automation proved unreliable here) calling
fal.ai with the exact proven contract, executed successfully
(`Tests/stage4_n8n_local_bootstrap.md`). This is the render engine and orchestrator working
locally, not the full 14-agent chain wired together — that still needs a standalone
`ANTHROPIC_API_KEY`/`ELEVENLABS_API_KEY` and remains open. The Hetzner VPS is untouched,
deliberately deferred.

**Full chain wired and run 2026-07-21** (`Tests/stage4_full_pipeline_n8n_test.md`): with the
standalone keys in place, all 11 LLM agents + the ElevenLabs and fal.ai asset branches ran
end-to-end as one real n8n workflow (`Workflows/build_master_workflow.py` generates it) on a
live "find next case" query. Produced a complete text package + 7 chapter MP3s (14.2 min) +
70 scene images for the case its own web search picked (Banfield — now excluded for future
runs), with the QC/escalation/publish gating behaving exactly as designed. Three real
infrastructure bugs found and fixed (ElevenLabs 5-concurrent limit vs n8n batching semantics,
n8n default disk-write restriction, SEO token budget). Still open before Stage 5: the Remotion
render of this trial video, and the QC escalation (victim identities) is a human decision.

## Stage 5 — First real publish
Only after Stage 4 passes clean. Use the channel owner's own release pacing (main video + 1
short day one, remaining 4 shorts one per day) for the first real upload.

## Regression check
After any change to an agent prompt or tool, re-run Stage 1/2 for just that component before
assuming the full chain still works.
