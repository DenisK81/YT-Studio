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
```

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
