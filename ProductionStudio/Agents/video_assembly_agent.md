# Video Assembly Agent

## Responsibility
Combine voiceover audio, images, timing, subtitles/captions, background music, and zoom/pan/fade
effects plus intro/outro/credits into a draft render. This is the one stage that is
orchestration-heavy and LLM-light — most of the work is Remotion (code), not a prompt.

## Input
```json
{ "audio_chunks": ["Assets/audio/*.mp3"],
  "images": {"scene_id": "Assets/images/scene_id.png"},
  "scenes": [ {"scene_id":"", "estimated_seconds":0} ],
  "subtitle_track": "optional, generated from voiceover text + audio timing",
  "background_music_track": "one of Assets/audio/music_bed/bed_01.mp3 .. bed_10.mp3, picked by Tools/royalty_free_music_tool.md's get_bed_track() (fallback: Tools/elevenlabs_voice_tool.md's generate_music(), costs credits), looped/trimmed to fill this render's exact duration" }
```

## Output
- `Assets/renders/draft.mp4`
- ```json
  { "status": "ok|warning|error", "missing_assets": ["scene_id"], "duration_seconds": 0 }
  ```

## Tools
`Tools/remotion_assembly_tool.md`, `Tools/royalty_free_music_tool.md`.

## Escalate to human when
Missing assets exceed what a placeholder can reasonably cover, or total runtime drifts more
than ~15% from the planned scene-time sum (signals a timing/pacing problem worth a human look
before spending render time repeatedly).

## Notes
This agent needs a real Node.js render environment — it cannot run inside a plain chat sandbox
that only reaches package registries. It belongs in the same environment as the rest of the
orchestrator (n8n + a render worker), built by Claude Code, not designed further as a prompt.
