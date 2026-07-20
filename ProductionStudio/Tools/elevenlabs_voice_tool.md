# Tool: elevenlabs_voice_tool

## Purpose
Provider-agnostic voice generation wrapper. Default provider: ElevenLabs. Per Voice Policy, any
agent calling this tool must go through this interface, never call ElevenLabs directly, so the
provider can be swapped later without touching agent prompts.

## Interface
```
generate(text: string, voice_id: string, chapter_label: string) -> {
  audio_url_or_bytes,
  duration_seconds
}

generate_music(mood_prompt: string, duration_seconds: number, instrumental: boolean = true) -> {
  audio_url_or_bytes,
  duration_seconds
}
```
`generate_music` is the real Eleven Music API (`music_length_ms` param, 10s-5min range,
natural-language mood prompt + up to 10 style tags) — added 2026-07-19 to close the gap where
background music had no spec at all. This is exactly the "extend, don't duplicate" case Tool
Manager Agent's `extend_existing` output shape (see `Agents/tool_manager_agent.md`) was built
for: this tool's own notes already anticipated SFX/music via "a different mode parameter" before
this was formalized.

**Superseded as the default the same day (2026-07-19):** Eleven Music charges per-generation
credits, and the channel owner wants background music sourced free instead —
`Tools/royalty_free_music_tool.md` is now the default for `background_music_track`.
`generate_music` here stays as the **fallback** (e.g. if the free library has no good match for
a specific mood/duration), not the primary path.

## Default provider notes (ElevenLabs, verify against current docs before building)
- Recommended for this channel's long-form narration: **Studio** project mode (chapter
  splitting, multi-voice support, timeline) rather than a single one-shot TTS call.
- Model choice: Eleven v3 supports emotion tags ([whispers], [laughs]) for a more dramatic
  read; Multilingual v2 is the stable default for long-form narration without tags (matches
  this channel's current "no emotion tags" voiceover policy).
- Voice: either an existing library voice, or Voice Cloning (instant, ~1 min sample) / 
  Professional Voice Cloning (30+ min sample, higher quality) if a signature channel voice is
  wanted later.
- Sound Effects (SFX) and generated Music are also available from the same provider and can
  replace searching for royalty-free tracks — useful for ambient sound (police radio static,
  rain, courtroom murmur) called from the same tool with a different `mode` parameter if
  extended later.

## Implementation notes
- Requires a real ElevenLabs API key stored in the orchestrator's credential store
  (`ELEVENLABS_API_KEY` in `Config/.env.example`) — not available from a plain chat sandbox.
- This spec was written without a live test against the current ElevenLabs API — confirm exact
  endpoint paths/parameters against their current docs before wiring the n8n node.

## Stage 1/2 live-test result (2026-07-19)
Ran a real call through the ElevenLabs MCP integration available in this environment
(`generate_tts`), using the Hook-beat text from the Banfield case's `Voiceover.txt` chapter 1
as a small/cheap test per `Tests/TEST_PLAN.md`.

- **Call succeeded** and returned a playable track — confirms the "no emotion tags, plain
  spoken text" input this agent produces works end-to-end with a real TTS call.
- **Output shape differs from this spec's declared contract.** The MCP tool returned
  `{ tracks: [{ id, filePath, title, artist }] }`, not the `{ audio_url_or_bytes,
  duration_seconds }` this file documents. No `duration_seconds` is returned at all — anything
  downstream (Video Assembly Agent needs per-scene duration to line up timestamps) would have
  to measure the audio file directly rather than trust a duration field from this call.
- **Output location is controlled by the MCP server, not this repo.** The file was saved to
  `D:\SHOPS\AI Projects\YT_Crime\Voices\tts_<timestamp>.mp3` — outside
  `ProductionStudio/Assets/audio/`, the location `Assets/README.md` documents. A real pipeline
  wiring would need a copy/move step into `Assets/audio/{scene_id}.mp3` rather than assuming
  the tool writes there directly.
- **Voice/model selection is opaque from the response, and the silent default is wrong for this
  channel.** `generate_tts`'s `voice_id`/`model_id` params aren't documented with an enum in the
  MCP tool schema, and the response doesn't echo back which voice/model actually ran. First
  test call omitted both params and produced a **female** voice — confirmed wrong against the
  channel's chosen narration voice (a male Canadian narration voice, per the ElevenLabs app UI).
  Found the correct voice via the separate `search_voices` MCP tool (search: `"Jimmy"`) —
  **voice_id `wSChTcAxdiTjLPhHeyrM`** ("Jimmy - Canadian Podcast Narration": male, Canadian
  accent, formal, `narrative_story` use-case — a good match for true-crime narration),
  `model_id` `eleven_multilingual_v2`. Re-ran the same Hook text with both explicit — correct
  voice confirmed. **Always pass `voice_id`/`model_id` explicitly; never rely on this MCP tool's
  default voice for real production audio.**
- **This MCP tool both generates and plays audio in one call** (per its own description) —
  different from a typical generate-only API call; calling a separate "play" step afterward is
  redundant. Note this if/when this gets reimplemented as a plain API call in n8n instead of
  through this MCP integration, since n8n won't have an equivalent "auto-play" side effect to
  account for.

## Background music — Stage 2 live-test attempt (2026-07-19)
Tried a real call through the MCP integration (`generate_music`) with a tense/ambient true-crime
mood prompt, instrumental, 30s test duration — the small/cheap test this warrants per
`Tests/TEST_PLAN.md`.

- **Call failed: `401 unauthorized — missing the permission music_generation`.** This is an
  ElevenLabs account/API-key permission gap, not a spec or code bug — Eleven Music appears to be
  gated separately from standard TTS access on this account/plan. **Needs the channel owner to
  enable the `music_generation` permission on the ElevenLabs API key (or upgrade the plan tier if
  that's what gates it) before this can be live-tested.**
- Real API shape confirmed via docs regardless (not blocked by the permission issue): mood
  described in natural language plus up to 10 style tags, `music_length_ms` for duration
  (10s-5min range), or a detailed "composition plan" JSON for finer control (chunk structure,
  arrangement) if simple prompting isn't precise enough later.
- **Fixed mixing spec (research-grounded, not a guess):** background music sits **-18 to -20dB
  below the voiceover** (never less than -15dB below, which risks masking narration,
  particularly on phone speakers). True-crime specific: apply a subtle 1.5-2.5dB EQ dip between
  1-3kHz on the music track (where the voice sits) so narration doesn't need to be pushed
  louder, plus a 40Hz high-pass / 10kHz low-pass to keep the music track clean. This is a Video
  Assembly Agent / Remotion mixing responsibility — see `Tools/remotion_assembly_tool.md`.
- **Fixed mood direction:** subtle, investigative, emotionally controlled — supports the
  narration and builds atmosphere without overwhelming or becoming melodic/dramatic. One
  continuous instrumental bed per video is the default (not a per-scene track), looped/extended
  to match the final render's duration.

## Gap closure (2026-07-19) — concrete fix for the two shape mismatches above
This MCP integration is a Phase 1 testing convenience, not the final n8n wiring — so rather than
changing this file's declared contract to match the MCP tool's shape, the fix belongs in how the
*real* ElevenLabs Data API v1 call gets wrapped in n8n:
- **`duration_seconds`**: the real ElevenLabs API doesn't return this either (it returns raw
  audio bytes/URL) — measure it locally after the call (e.g. an audio-length library reading the
  file's own header) rather than expecting any TTS provider to report it. Add this as an
  explicit post-processing step in the n8n node, not an assumption baked into this tool's output
  contract.
- **File location**: whatever calls this tool (real API or an MCP-style integration) must save
  or copy the result into `Assets/audio/{scene_id}.mp3` itself — this tool's `generate()` should
  not assume the provider writes there natively, since neither the real API nor this MCP
  integration does.
- Both of these are now explicit responsibilities of whatever *wires* this tool (Video Assembly
  Agent's input needs both a file at the right path and a duration) — not gaps in this file's
  contract, since the contract itself (`{ audio_url_or_bytes, duration_seconds }`) was always the
  *tool's* output, and the wrapping logic derives the missing piece rather than trusting the
  provider for it.
