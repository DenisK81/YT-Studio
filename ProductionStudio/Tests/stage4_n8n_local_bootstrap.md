# n8n — local bootstrap + real workflow execution (2026-07-20/21)

Second half of the local Phase 2 bootstrap (after the Remotion render test): prove n8n actually
runs on this machine and can execute a real HTTP call using the exact contract this session
already validated directly (`Tools/image_gen_tool.md`'s Stage 2 fal.ai test).

## Setup
- No Docker on this machine, so n8n was run via `npx n8n` (no global install) rather than the
  official Docker image (n8n itself flags running outside a container as deprecated, but that's
  a long-term guidance note, not a blocker for a local proof-of-concept).
- First run required creating a **local owner account** (email/name/password) — this is n8n's
  own local SQLite-backed admin user, not an external/cloud account. Per this session's rule
  about never entering passwords on the user's behalf, the user completed that step themselves
  in the shared Browser pane.
- Generated a local n8n API key (label `claude-code-local-test`, all 72 scopes) via
  Settings → n8n API — **the full key value is deliberately never rendered in the page DOM**
  (only the first/last few characters, with a literal `"..."` in between — confirmed by
  querying `document.body.innerText` directly, not just visually). n8n only ever exposes the
  full key through the OS clipboard via its "Copy" button, which isn't something this session's
  tools can read. **Result: the API key was created but never actually used** — building the
  workflow instead went through the CLI (see below), which needed no key at all.

## Real friction hit while trying to use the browser UI directly
- The Browser pane's `computer{action:"screenshot"}` **consistently timed out** on n8n's
  workflow editor specifically (worked fine on plain content pages like WJLA earlier this
  session) — likely the canvas-heavy Vue Flow editor keeps something continuously
  repainting/animating in a way that never reaches whatever "idle" state the screenshot tool
  waits for.
- `get_page_text` kept returning a static, generic shell ("Personal / workflow name / Publish /
  Editor / Executions...") regardless of what was actually open on screen — it wasn't reading
  the live canvas/node-detail content at all.
- Clicking "Execute workflow" via `computer{action:"left_click", ref:...}` **appeared to
  succeed** (correct coordinates logged, no error) but **produced zero rows in
  `execution_entity`** when checked directly against `C:\Users\kurba\.n8n\database.sqlite` via
  `sqlite3` — the clicks were not actually reaching whatever click handler triggers a real
  execution, despite `read_page`'s accessibility tree correctly identifying and describing the
  button.
- **Conclusion: `read_page` (accessibility tree) was reliable for finding elements and reading
  structure; `computer` (screenshot/click) and `get_page_text` were not reliable for this
  specific canvas-based SPA.** Worth remembering for any future n8n UI automation — don't trust
  a click "worked" just because it didn't error; verify against a ground-truth source (the DB,
  an API, a log) before concluding an action actually fired.

## What actually worked: CLI-driven, not UI-driven
1. **Build the workflow as JSON, not by clicking nodes together.** Wrote a Python script
   (`build_n8n_workflow.py`) that reads `FAL_KEY` from the environment and generates a workflow
   JSON with a Manual Trigger → HTTP Request node calling `https://fal.run/fal-ai/flux/schnell`,
   using the exact header/body shape already proven in `Tools/image_gen_tool.md`'s Stage 2 test.
   Kept entirely in the session scratchpad — the real key never touched a file inside the actual
   repo.
2. `npx n8n import:workflow --input=<file> --projectId=<id>` — **first attempt failed**:
   `SQLITE_CONSTRAINT: NOT NULL constraint failed: workflow_entity.id`. The CLI import expects an
   explicit top-level `"id"` field in the workflow JSON (unlike the API, which auto-generates
   one) — added a random hex id, re-ran, succeeded.
3. `npx n8n execute --id=<workflow_id> --rawOutput` — **first attempt failed**:
   `n8n Task Broker's port 5679 is already in use` (the background `npx n8n` server was still
   holding the port even after this session's `TaskStop`, confirmed via `netstat` showing PID
   10344 still listening — `TaskStop` didn't actually kill the underlying Node child process).
   Force-killed it directly (`taskkill /F /PID 10344`), then `execute` ran cleanly.

## Real result (success, not simulated)
```json
{
  "status": "success",
  "finished": true,
  "resultData": {
    "runData": {
      "Image Generation Agent (fal.ai Flux schnell)": [{
        "executionStatus": "success",
        "executionTime": 996,
        "data": { "main": [[{ "json": {
          "images": [{ "url": "https://v3b.fal.media/files/b/0aa31a55/h32B1NgxsFM6RhjL2Rvsl.png", "width": 1024, "height": 576, "content_type": "image/png" }],
          "timings": { "inference": 0.1008 }, "seed": 901780664, "has_nsfw_concepts": [false]
        }}]] }
      }]
    }
  }
}
```
Downloaded and viewed the actual returned image — a photorealistic 1024x576 (correct 16:9) night
scene matching the test prompt exactly, same visual quality as the earlier direct-Python fal.ai
test. **This confirms n8n, running locally with no Docker, can execute a real external API call
using the exact same credential/contract already proven outside n8n** — the first real link of
`Workflows/n8n_master_workflow.skeleton.json` (the `image_generation_loop` node) is no longer a
placeholder shape, it's a demonstrated-working HTTP Request node.

## What's still not done (explicitly, per the approved plan's scope)
- The other 13 agents (Research, Story, etc.) are not wired — needs a standalone
  `ANTHROPIC_API_KEY`, which doesn't exist yet. n8n also has a native Anthropic/Claude node
  (separate from a raw HTTP Request node) worth checking once that key exists, rather than
  assuming the skeleton's generic `httpRequest` type is the only option.
- ElevenLabs real API wiring — same story, needs a standalone `ELEVENLABS_API_KEY`.
- Nothing here touches the Hetzner VPS — this was entirely local, as scoped.
- The generated n8n API key (`claude-code-local-test`) was never actually used for anything; it
  remains in the local instance's credential list, harmless (scoped to `localhost:5678`, not
  committed anywhere) but could be revoked if this local instance is kept around.
