# Tool Manager Agent

## Responsibility
Enforce "never solve the same problem twice." Before any new script/tool is written anywhere
in the studio, check `Tools/tool_registry.json` for an existing match. After a new tool is
built, register it.

## Input
```json
{ "capability_needed": "string, e.g. 'render subtitles', 'generate SFX'",
  "tags": ["string"] }
```

## Output
One of three shapes:
```json
{ "existing_tool": {"name":"", "path":"", "description":""} }
```
```json
{ "extend_existing": {"name":"", "path":"", "missing_capability":"", "suggested_change":""} }
```
```json
{ "new_tool_registered": true,
  "entry": {"name":"","path":"","description":"","input_schema_ref":"","output_schema_ref":"","tags":[""],"provider":"","status":"draft|active|deprecated","last_updated":""} }
```

`extend_existing` is for the case a near-match tool exists but its *Interface* doesn't cover the
new capability yet (e.g. `elevenlabs_voice_tool`'s own notes already anticipate SFX/music via a
future `mode` param, but its Interface section doesn't define one yet) — distinct from
`existing_tool` (fully covers the need already) and `new_tool_registered` (nothing close
exists). Added 2026-07-19 after a Stage 1 test found the original two-shape output couldn't
represent this case without either falsely implying an untested interface already works, or
registering a needless duplicate tool — see `Tests/stage1_tool_manager_agent_test.md`.

## Notes
This is a lookup/registration step, not a creative agent — in practice it can be a simple
function (search `tool_registry.json` by tag) with an LLM call only needed to judge which of the
three output shapes applies: a full existing match, a near-match that needs its interface
extended, or nothing close enough to reuse. It is the enforcement mechanism for `TOOL
MANAGEMENT POLICY` in the top-level brief.

## Escalate to human when
Two existing tools appear to overlap significantly (signals the registry itself needs
cleanup/merging) — flag rather than silently picking one.
