# Stage 3 — two-node link audit (2026-07-20)

Per `Tests/TEST_PLAN.md`'s Stage 3, checked every link in the pipeline for a real contract
match: does the upstream agent's *actual declared output* plug into the downstream agent's
*actual declared input* without an undocumented manual step in between? Most of this pipeline
was already exercised with real chained data during the Banfield case work — this pass is about
verifying the *schemas themselves* line up, not re-running the agents again.

## Links checked

| Link | Result |
|---|---|
| Research → Fact Verification | 🚩 **Gap found & fixed** — see below |
| Fact Verification → Story | ✅ Clean (`verified_claims` matches; `timeline_draft` is a documented multi-source merge from Research, not a bug) |
| Story → Scene Planner | ✅ Clean (`script_md` is literally `Script.md`'s text) |
| Scene Planner → Voice Production | ✅ Clean (Voice Production takes a subset of Scene Planner's fields) |
| Scene Planner → Image Planning | ✅ Clean (same — subset match) |
| Image Planning → Image Generation | 🚩 **Gap found & fixed** — see below |
| Voice + Images → Assembly | 🚩 **Gap found & fixed** — see below |
| Assembly → Shorts | ✅ Clean (`final_video` + `scenes` match Assembly's real output shape) |
| Shorts + Thumbnail + SEO → QC | ✅ Clean (QC's input is intentionally broad/holistic, not a strict schema) |
| QC → Publishing | 🚩 **Gap found & fixed** — see below |

## Gaps found and fixed

1. **Research Agent → Fact Verification Agent**: Research's real output (`candidates[]` with
   `summary`/`sources[].key_facts`/`timeline_draft`) never produces Fact Verification's expected
   pre-broken `script_draft_or_scene_claims` array — no agent in the pipeline owns that
   conversion. Added a note to `Agents/fact_verification_agent.md`: derive the claims list by
   flattening the chosen candidate's `key_facts`/`summary`/`timeline_draft` entries, since each
   `key_facts` string is already written as an atomic claim.

2. **Image Planning Agent → Image Generation Agent**: Image Planning's output keeps `prompt` and
   `style_tags` as separate fields, but the real image-gen APIs (confirmed live against fal.ai)
   only take one `prompt` string — no separate style parameter exists. Added a note to
   `Agents/image_generation_agent.md`: this agent merges `style_tags` into the `prompt` string
   before calling `image_gen_tool`, not Image Planning Agent.

3. **Voice Production Agent → Video Assembly Agent**: Voice Production's declared Output only
   named `Templates/Voiceover.txt` (text) — the actual audio-file convention Video Assembly
   needs (`Assets/audio/*.mp3`) was never declared. Added an explicit output declaration:
   one MP3 per chapter chunk (`chapter_01.mp3`, etc., matching `Voiceover.txt`'s own
   chaptering — not per scene_id, since ElevenLabs Studio's chapter mode is the intended
   provider path). Also documented that Video Assembly Agent (not Voice Production) is
   responsible for concatenating these per-chapter chunks into the one continuous `audio_track`
   string `remotion_assembly_tool.md`'s `assemble()` interface actually takes.

4. **Quality Control Agent → Publishing Agent**: QC's output field was named `status`, but
   Publishing Agent's input has always expected `checklist_status` — a real name mismatch, not
   just a documentation inconsistency. Renamed QC's output field to `checklist_status` to match
   exactly, since this is the literal field Publishing gates on.

## Non-bug pattern worth documenting once (not fixed as a "gap" — just clarified)

`Agents/thumbnail_agent.md`, `Agents/seo_agent.md`, and `Agents/shorts_agent.md` all take a
`twist`/`case_summary`-shaped field with no single upstream agent literally producing a field by
that exact name — in practice (confirmed across every real run this session) it's manually
extracted from `Script.md`'s Twist beat text and Research Agent's `summary`, the same
multi-source-derivation pattern as Story Agent's `timeline_draft` input. Not a contract bug,
just worth naming once rather than leaving implicit in three separate agent files — noted in
`Documentation/ARCHITECTURE.md`.
