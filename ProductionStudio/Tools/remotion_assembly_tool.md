# Tool: remotion_assembly_tool

## Purpose
Programmatic video assembly — audio + images + timing + subtitles + effects + intro/outro,
rendered to a final .mp4. Replaces manual CapCut editing once Phase 2 automation is built (see
`fatal-affairs-project-brief.md` — CapCut stays the Phase 1 manual tool; Remotion is the
Phase 2 automated replacement).

## Interface
```
assemble({
  scenes: [{ scene_id, image_path, start_seconds, end_seconds }],
  audio_track: string,
  subtitle_track: string,   // e.g. SRT/VTT generated from voiceover + audio timing
  intro: string, outro: string, credits: string
}) -> {
  render_path,
  duration_seconds
}
```

## Requirements
- Needs a Node.js render environment (Remotion runs on React + Node). This cannot run in a
  plain chat sandbox restricted to package registries — it needs its own render worker,
  reachable from n8n as an HTTP call or a queued render job.
- Should support: zoom/pan/fade transitions between images (Ken-Burns-style, standard for this
  documentary format), burned-in or soft subtitles, multiple export presets (16:9 for main
  video, 9:16 for shorts).

## Implementation notes
- Build the shorts export (9:16, ~30-60s cuts) as a second composition sharing the same scene
  data, not a separate pipeline — reuse the same assets.
- This spec has not been tested against a real Remotion project — Claude Code should scaffold
  a minimal composition first and confirm render output before wiring it into the full agent
  chain.
