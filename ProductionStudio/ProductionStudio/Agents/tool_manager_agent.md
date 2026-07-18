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
Either:
```json
{ "existing_tool": {"name":"", "path":"", "description":""} }
```
or, after a new tool is created elsewhere:
```json
{ "new_tool_registered": true,
  "entry": {"name":"","path":"","description":"","input_schema_ref":"","output_schema_ref":"","tags":[""],"provider":"","status":"draft|active|deprecated","last_updated":""} }
```

## Notes
This is a lookup/registration step, not a creative agent — in practice it can be a simple
function (search `tool_registry.json` by tag) with an LLM call only needed to judge whether a
near-match tool can be *extended* to cover the new need instead of creating a duplicate. It is
the enforcement mechanism for `TOOL MANAGEMENT POLICY` in the top-level brief.

## Escalate to human when
Two existing tools appear to overlap significantly (signals the registry itself needs
cleanup/merging) — flag rather than silently picking one.
