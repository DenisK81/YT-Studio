# Publish Plan — Brendan Banfield double murder (Christine Banfield & Joseph Ryan)

Stage 1 isolated test of `Agents/publishing_agent.md`, two scenarios. No real YouTube API call
was made or attempted in either case — `Tools/youtube_publish_tool.md`'s `confirm_publish` is
never called without explicit human go-ahead, per this project's hard rule.

## Scenario 1 — real current state (this case, as of 2026-07-19)
**Input:** `final_video: "Assets/renders/final.mp4"` (does not exist — Video Assembly Agent was
never run, deliberately, as Phase 2 scope), `checklist_status: "fail"` (real value from
`Checklist.md`), `seo`/`thumbnail` from this case's real files, `shorts: []`.

**Output:**
```json
{ "status": "error",
  "output": null,
  "notes": "checklist_status is 'fail', not 'pass' (Checklist.md: missing images for 20/21 scenes, no per-scene audio, no render). Per this agent's input contract and its Hard Rule, no release_plan will be prepared. Returning to human review, not attempting a partial plan." }
```
Correct behavior — the agent independently re-checks its own precondition rather than trusting
that an upstream gate already caught it. In a properly wired pipeline this input would never
reach Publishing Agent (QC's `fail` routes to human review first, per `ARCHITECTURE.md`'s
pipeline diagram) — this isolated test confirms the agent also guards itself, not just relying
on that upstream routing.

## Scenario 2 — hypothetical pass-state, to test the actual release-plan logic
Since scenario 1 correctly refuses, it never exercises the "happy path" output shape. Built a
hypothetical input (**not real production data** — flagged clearly as such) assuming QC passed
and a final render existed, to verify the pacing logic in isolation:

**Input (hypothetical):** `checklist_status: "pass"`, plus 5 placeholder shorts.

**⚠ Real gap found while building this test input:** there is no agent in this pipeline that
owns "cut the script into 5 Shorts and write each one's own hook/title/description." Publishing
Agent's input schema just assumes `shorts: [{video, hook, title, description, hashtags}]`
already exists. `Tools/remotion_assembly_tool.md` only says Shorts are "a second composition
sharing the same scene data" (i.e. a render/export detail), which explains *how* a Short gets
rendered but not *which scenes* become which Short or *what its hook/title should be*. That
content-decision step has no owner. Flagging this as a real pipeline gap, not inventing a new
agent to fill it — that's a call for a human to make about the pipeline design.

**Output (hypothetical, for pacing-logic verification only):**
```json
{ "release_plan": [
    {"date":"2026-07-20","asset":"main video","pinned_comment":"The scariest part of this case isn't the murder — it's how convincing a fake version of someone you trust can be. Would you have caught it? Let me know below."},
    {"date":"2026-07-20","asset":"short 1","pinned_comment":"The fake account that fooled a real person — full story in the main video."},
    {"date":"2026-07-21","asset":"short 2","pinned_comment":"The staged scene, explained."},
    {"date":"2026-07-22","asset":"short 3","pinned_comment":"The verdict, in under a minute."},
    {"date":"2026-07-23","asset":"short 4","pinned_comment":"Why he really did it."},
    {"date":"2026-07-24","asset":"short 5","pinned_comment":"What happened to everyone involved."}
  ],
  "awaiting_human_confirmation": true }
```
Pacing rule compliance checked against `Config/config.schema.json`'s `publishing_pace`: main
video + short 1 same day ✓, remaining 4 shorts one per day after ✓, short order is
strongest-hook-first (catfishing reveal → staged scene → verdict → motive → aftermath) not
chronological-in-script order ✓.

`awaiting_human_confirmation: true` is correctly always present — this agent never sets it to
false or calls `confirm_publish` itself.
