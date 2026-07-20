# Tool Manager Agent — Stage 1 isolated test (2026-07-19)

Two real lookup requests against the current `Tools/tool_registry.json`, per
`Agents/tool_manager_agent.md`'s input/output contract.

## Test A — clear existing match
**Input:** `{ "capability_needed": "download real booking/court photos for a case", "tags": ["images", "public-records"] }`

**Output:**
```json
{ "existing_tool": {
    "name": "mugshot_fetch_tool",
    "path": "Tools/mugshot_fetch_tool.md",
    "description": "Fetches real booking photos / court exhibits / agency press-release images from public-record sources only (sheriff/DOC/court)... BLOCKED pending legal review." } }
```
Correct — a tool with this exact capability already exists (registered earlier this session).
Tool Manager's job is lookup/registration, not legal-status filtering, so it correctly returns
the match even though that tool's own status is `blocked pending legal review` — the caller is
expected to read the tool file and see that, not have Tool Manager silently hide a blocked tool.

## Test B — near-match that should be extended, not duplicated
**Input:** `{ "capability_needed": "generate ambient sound effects (police radio static, rain, courtroom murmur) for a video", "tags": ["audio", "sfx"] }`

**Reasoning:** No tool is tagged `sfx`. `elevenlabs_voice_tool` (tags: `voice, tts, audio`) is the
closest match, and its own "Default provider notes" already anticipate this: *"Sound Effects
(SFX) and generated Music are also available from the same provider... useful for ambient
sound... called from the same tool with a different `mode` parameter if extended later."*

**Correct output should recommend extension, not a new tool** — but here's a real schema gap:
`Agents/tool_manager_agent.md`'s output schema only has two shapes, `{existing_tool}` or
`{new_tool_registered}`. Neither cleanly represents "a near-match tool exists but its
*interface* doesn't cover this yet — extend it" as a distinct case. Forcing this into
`{existing_tool}` risks the caller assuming `elevenlabs_voice_tool.generate()` already accepts
an SFX mode (it doesn't — its Interface section only defines `generate(text, voice_id,
chapter_label)`); forcing it into `{new_tool_registered}` risks a duplicate tool for a
capability that should live in the existing one.

**Corrected output (2026-07-19, after adding the `extend_existing` shape to
`Agents/tool_manager_agent.md`):**
```json
{ "extend_existing": {
    "name": "elevenlabs_voice_tool",
    "path": "Tools/elevenlabs_voice_tool.md",
    "missing_capability": "SFX/ambient sound + music generation",
    "suggested_change": "Add a `mode: 'tts' | 'sfx' | 'music'` parameter to the Interface's generate() signature; ElevenLabs already supports this via the same provider account, per this tool's own 'Default provider notes' section." } }
```

## Resolution
Added a third output shape, `extend_existing`, to `Agents/tool_manager_agent.md` — this test's
original finding is now fixed rather than just flagged. No new `sfx_tool` was registered; the
recommendation stays "extend `elevenlabs_voice_tool`'s Interface," which is a follow-up
implementation task (adding the actual `mode` parameter), not something to do speculatively
ahead of an actual SFX need.
