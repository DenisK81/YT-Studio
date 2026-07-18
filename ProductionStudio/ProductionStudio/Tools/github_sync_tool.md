# Tool: github_sync_tool

## Purpose
The one tool that needs real write access to this repository. Used by the Tool Manager Agent
to check `Tools/tool_registry.json` for existing tools before new ones are built, and to commit
registry/SuccessRules updates after a project finishes.

## Interface
```
check_registry(tags: string[]) -> { matches: [...] }
commit_update(files: [{path, content}], message: string) -> { commit_sha }
```

## Implementation notes
- Needs a GitHub token (fine-grained PAT or GitHub App installation token) with write access
  scoped to this one repo — stored as a credential in the orchestrator, never hardcoded.
- Auto-commits should go through a PR + a basic schema/lint check (validate `tool_registry.json`
  is valid JSON, validate new agent/tool files have the required sections) rather than pushing
  straight to `main`, even in an otherwise automated pipeline — see
  `Documentation/HANDOFF_TO_CLAUDE_CODE.md`, "What NOT to do."
- This tool cannot be built or tested from a plain Claude.ai chat session — it requires the
  kind of real git/network access Claude Code has.
