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
  documentary format), burned-in captions per the fixed style below, multiple export presets
  (16:9 for main video, 9:16 for Shorts).

## Caption style (fixed, research-grounded 2026-07-19 — see `Documentation/ARCHITECTURE.md`'s
"Shorts & captions requirement" section)
- **Font**: Montserrat Bold — reuses the channel's existing body font
  (`Config/config.schema.json`), not a new arbitrary font, for brand consistency.
- **Color/stroke**: white text, thin black stroke/outline for contrast on any background.
- **Chunking**: 1 word or short 2-5 word phrases, not full sentences at once.
- **Word-by-word karaoke highlight**: the actively-spoken word is enlarged/highlighted in the
  channel's accent color (`#A30E15`), surrounding words stay dimmer/smaller — this is the
  dominant 2026 short-form caption style, not a stylistic guess.
- **Position**: centered, lower third of frame.
- **Minimum on-screen duration**: 2 seconds per phrase, even if the spoken pace is faster —
  readability matters more than perfect audio sync, especially since 60%+ of Shorts viewers
  watch muted.
- Applies to both the main video (16:9) and Shorts (9:16) — one caption style across the
  channel, not a per-video decision.

## Implementation notes
- **Shorts are no longer a blind re-export of the same scene data.** `Agents/shorts_agent.md`
  now selects specific moments and writes each Short's own hook/title/description
  (`Templates/Shorts.md`) immediately after this tool produces the main render — this tool then
  renders each selected Short as its own 9:16 composition (hard cap 45 seconds, per
  `Config/config.schema.json` `shorts.max_seconds`), not a generic same-content repackage.
- This spec has not been tested against a real Remotion project — Claude Code should scaffold
  a minimal composition first and confirm render output before wiring it into the full agent
  chain.
