# Handoff to Claude Code

This repo was designed in a Claude.ai chat session, which has no GitHub write access, no n8n
instance, and no ability to run in the background. Everything below needs an environment with
real filesystem/network/git access — Claude Code, or a human developer — to actually build.

## Build order

1. **Repo**
   - `git init`, create the real GitHub repo, push this scaffold as the first commit.
   - Protect `main`; work in feature branches per agent/tool if more than one person touches it.

2. **Orchestrator**
   - Install n8n on the existing Hetzner VPS (already the plan in `fatal-affairs-project-brief.md`).
   - Import `Workflows/n8n_master_workflow.skeleton.json` — it is a **skeleton**, not a working
     workflow. Node types and connections are placeholders; credentials, exact HTTP bodies, and
     error branches need to be built in the n8n editor.

3. **Credentials**
   - Copy `Config/.env.example` → real values, load into n8n's credential store (not into node
     JSON directly).
   - Required at minimum: `ANTHROPIC_API_KEY`, `ELEVENLABS_API_KEY`, an image-gen provider key
     (Midjourney/Flux/whichever is chosen), YouTube OAuth client + refresh token.

4. **Wire and test agents one at a time**
   - For each file in `Agents/`, create one n8n HTTP node that calls the Anthropic API
     (`/v1/messages`) with that agent's system prompt as `system` and the upstream node's JSON
     output as the user message.
   - Test each agent in isolation against the real Molly Watson case data already drafted in
     `fatal-affairs-project-brief.md` before connecting it to the next node. Don't wire the full
     chain until each link works alone — see `Tests/TEST_PLAN.md`.

5. **Wire tools**
   - For each file in `Tools/`, verify the actual current API shape of the provider (ElevenLabs
     Studio endpoints, chosen image API, YouTube Data API v3, Remotion render invocation) —
     these specs describe intended contracts, not verified-live request/response bodies. APIs
     change; check current docs before trusting the shape written here.

6. **Video assembly**
   - Remotion needs a Node.js render environment (not this chat's sandbox, which only reaches
     package registries, not arbitrary APIs). Set this up as its own render service the n8n
     workflow calls into, per `Tools/remotion_assembly_tool.md`.

7. **GitHub sync tool**
   - `Tools/github_sync_tool.md` describes how the Tool Manager Agent checks/updates
     `Tools/tool_registry.json`. Wire this as an actual git operation (via a GitHub App token or
     PAT stored as a credential) — this is the one piece that literally needs write access to
     the repo, which only Claude Code / CI has, not a chat session.

8. **Publishing stays gated**
   - Per `Agents/publishing_agent.md`: build the upload call, but require an explicit human
     confirmation step before it fires, at least through the first 10-video test phase referenced
     in `fatal-affairs-project-brief.md`. Don't auto-schedule uploads yet — the channel owner's
     own notes on shorts pacing (one strong short per day, not five at once) mean publish timing
     is still a judgment call for now, not a cron job.

9. **First real run**
   - Use the Molly Watson case (script chapters 6-16 + ending already exist in the project) as
     the first end-to-end test once chapters 1-5 are finished. Don't test the pipeline on a new,
     unresearched case first — too many variables move at once.

## What NOT to do

- Don't let the Tool Manager Agent or any agent auto-commit to `main` without a PR + at least a
  lint/schema check, even in an otherwise "autonomous" setup.
- Don't wire the Publishing Agent to fire without confirmation, no matter how automated the
  rest of the pipeline gets.
- Don't trust any API shape in `Tools/*.md` blindly — they're specs written without live
  execution access; verify against current provider docs first.
