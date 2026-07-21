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

## Channel intro bumper (open task, added 2026-07-21 — see `Documentation/ARCHITECTURE.md`'s
"Channel intro bumper requirement" for full detail)
Neither trial render (Banfield, Richins) has one. Needed before the next real production
render: a **fixed, reusable 2-3 second branded template** — channel name in brand style
(`Config/config.schema.json` colors/fonts) plus a short music sting — prepended to the
`intro` field above and reused unchanged across every video, never regenerated per case. This
is the one render element that should NOT vary video-to-video; consistency is the point.

## Caption style (fixed, research-grounded 2026-07-19 — see `Documentation/ARCHITECTURE.md`'s
"Shorts & captions requirement" section)
- **Font**: Montserrat Bold — reuses the channel's existing body font
  (`Config/config.schema.json`), not a new arbitrary font, for brand consistency.
- **Color/stroke**: white text, thin black stroke/outline for contrast on any background.
- **Chunking**: 1 word or short 2-5 word phrases, not full sentences at once. Prefer breaking on
  natural punctuation/clause boundaries over a blind fixed word-count split — a live test
  (2026-07-20) found that blindly grouping every 3 words produces awkward mid-clause breaks
  (e.g. splitting "...needs him to **be —** **and** the husband..." across two unrelated
  chunks). Not fixed in code yet, just documented as the right target.
- **Word-by-word karaoke highlight**: the actively-spoken word is enlarged/highlighted in the
  channel's accent color (`#A30E15`), surrounding words stay dimmer/smaller — this is the
  dominant 2026 short-form caption style, not a stylistic guess.
- **Position**: centered, lower third of frame.
- **Minimum on-screen duration: 2 seconds per phrase — Shorts only.** A live test (2026-07-20)
  found this rule doesn't work for continuous main-video narration at natural pace: the
  Banfield Hook clip is 62 words over 17.87s (~3.5 words/sec); enforcing a 2s floor on 3-word
  chunks would need ~40s of captions to cover 17.87s of audio, desyncing captions from speech
  entirely. **For the main video (16:9), use natural proportional timing by word count instead**
  — phrases still read fine at normal speaking pace without a hard floor. The 2s floor stays
  correct for Shorts specifically, where captions are sparse and punchy by design (few phrases,
  not continuous transcription), not for continuous narration.
- **Caption timing source of truth, corrected 2026-07-21 (`Tests/stage4_full_pipeline_n8n_test.md`
  follow-up):** the first full-pipeline trial render used per-scene word-count proportional
  timing scaled against each chapter's real audio *duration*, but derived the caption *text*
  from Scene Planner's `SceneList.json` scene text — a different text than what was actually
  sent to TTS. Voice Production Agent's own job is to reformat/expand for natural narration
  (its spec never promised verbatim), and on the real run one chapter came out 74% longer than
  its scene-list source. Result: captions drifted increasingly out of sync after ~9 minutes and
  were reading completely different words than the narrator by the end of the longest chapter.
  **Fixed at the root, not patched:** captions must be derived from ElevenLabs' own per-character
  alignment of the *exact* text sent to TTS (the `with-timestamps` endpoint — see
  `Tools/elevenlabs_voice_tool.md`), never from a separate agent's estimate of that text. See
  `Workflows/process_pipeline_audio.py` for the real implementation (per-word timing + real
  scene/image boundaries, both derived from the same alignment).
- **A second, distinct bug found the same day, after switching to chat-driven agent execution
  (no n8n):** Voice Production Agent (played by Claude Code directly, per
  `Documentation/ARCHITECTURE.md`'s "Orchestration decision") appended trailing prose after
  the real narration — a "Rendered audio: chapter_01.mp3 — scenes..." note and an escalation
  reminder — with nothing separating it from the actual chapter text. Nothing in the pipeline
  stopped that trailing text from being sent to TTS and read aloud; caught by ear on the
  re-render, not automatically. **Fixed:** `Workflows/generate_case_assets.py`'s
  `parse_voiceover()` now only treats text inside the outermost `` ``` `` fence as narration —
  the convention the agent had already used to separate its actual deliverable from
  commentary — and excludes/warns about anything outside it instead of silently narrating it.
  This is a general safety net: it holds regardless of which model or which turn produced
  `Voiceover.txt`.
- Same font/color/stroke/position style applies to both the main video (16:9) and Shorts
  (9:16) — only the *timing* rule (natural pacing vs. 2s floor) differs between them.

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

## Stage 2/4 local live-test result (2026-07-20) — real Remotion render confirmed
Node.js LTS installed (`winget install OpenJS.NodeJS.LTS`), a blank project scaffolded via
`npx create-video@latest --yes --blank`, and a real ~18s composition built and rendered using
actual Banfield-case assets (kept in a local scratch project, not committed — this was a
render-mechanics proof, not the real Phase 2 render worker):
- `Assets/images/0001.png` (real Flux-generated Hook image) as the background, with a Ken
  Burns pan/zoom via `interpolate()` on a CSS `transform: scale()/translateX()`.
- The real Jimmy-voice Hook TTS clip as the voiceover `<Audio>`, one `bed_XX.mp3` track from
  `Assets/audio/music_bed/` as a second `<Audio>` with `volume={10^(-18/20)} ≈ 0.126` (the fixed
  -18dB mix spec above, expressed as Remotion's linear 0-1 volume prop — there's no separate EQ
  API in Remotion's `<Audio>` component itself; the 1-3kHz dip/high-pass/low-pass from the mixing
  spec would need an actual audio-processing library, not attempted in this proof).
- Karaoke captions per the fixed style, using natural per-word proportional timing (see the
  caption-timing finding above) — confirmed correct visually across multiple extracted frames
  (`cv2.VideoCapture` + `imwrite`, since no `ffmpeg` is installed on this machine either — worth
  installing `ffmpeg` before doing real production renders, since Remotion itself may want it
  for some codecs/operations even though this basic render didn't need it).
- **Render succeeded**: 536 frames at 1920x1080/30fps, encoded to a 12.8MB MP4 with no errors.
- **Confirmed by actually looking at the output**, not just a clean exit code: captions render
  with the correct font weight/stroke/highlight color, the Ken Burns pan is visible and subtle,
  audio muxes into the file. This satisfies the "scaffold a minimal composition, confirm render
  output before wiring into the full chain" requirement that was open since this file was first
  drafted.
- **Status: no longer untested.** The render mechanics work on this machine. Still not wired to
  the actual agent chain (that's the n8n/orchestration side, tracked separately) and still needs
  the real EQ processing and natural-language-aware caption chunking noted above before a real
  production render.
