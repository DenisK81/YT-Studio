# Tool: remotion_assembly_tool

## Purpose
Programmatic video assembly — audio + images + timing + subtitles + background music + effects
+ intro/outro, rendered to a final .mp4. Replaces manual CapCut editing once Phase 2 automation
is built (see `fatal-affairs-project-brief.md` — CapCut stays the Phase 1 manual tool; Remotion
is the Phase 2 automated replacement).

## Interface
```
assemble({
  scenes: [{ scene_id, image_path, start_seconds, end_seconds }],
  audio_track: string,
  background_music_track: string,   // from Tools/royalty_free_music_tool.md (default), fallback Tools/elevenlabs_voice_tool.md's generate_music() (costs credits)
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

## Background music mixing (fixed, research-grounded 2026-07-19 — see
`Tools/royalty_free_music_tool.md` for sourcing, `Tools/elevenlabs_voice_tool.md`'s "Background
music" section for the fallback path)
- **Level**: -18 to -20dB below the voiceover track, never less than -15dB below (masking risk,
  especially on phone speakers). This is a mix requirement on every render, not per-video taste.
- **EQ**: subtle 1.5-2.5dB dip on the music track between 1-3kHz (where the voice sits) instead
  of pushing narration louder to compensate; 40Hz high-pass / 10kHz low-pass on the music track
  to keep it clean under the mix.
- **One track per render, looped/trimmed to exactly fill its duration** — not per-scene tracks.
  `Tools/royalty_free_music_tool.md`'s `get_bed_track()` picks one of the 10 curated Pixabay
  tracks; the same simple pick-one-and-loop logic applies to the main video (16:9) and
  independently to each Short (9:16) — a Short does not need to inherit a specific segment from
  the main video's bed, just its own looped pick from the same pre-vetted set. Subtle,
  investigative, emotionally controlled; never overwhelms or becomes melodic/dramatic enough to
  distract from narration.

## Implementation notes
- **Shorts are no longer a blind re-export of the same scene data.** `Agents/shorts_agent.md`
  now selects specific moments and writes each Short's own hook/title/description
  (`Templates/Shorts.md`) immediately after this tool produces the main render — this tool then
  renders each selected Short as its own 9:16 composition (hard cap 45 seconds, per
  `Config/config.schema.json` `shorts.max_seconds`), not a generic same-content repackage.
- This spec has not been tested against a real Remotion project — Claude Code should scaffold
  a minimal composition first and confirm render output before wiring it into the full agent
  chain.
