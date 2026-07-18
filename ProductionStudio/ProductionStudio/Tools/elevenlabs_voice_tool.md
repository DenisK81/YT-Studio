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
