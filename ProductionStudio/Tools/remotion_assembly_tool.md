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

## Chapter-to-chapter voice loudness inconsistency (found 2026-07-28 in production, confirmed with
real measurements — Rimoni Muliaga case)
The channel owner reported the narrator sounding "sometimes louder, then normal again" on a
published video. Measured via `ffmpeg -af loudnorm=print_format=summary` on the 5 real
ElevenLabs chapter files for that case: Input Integrated loudness ranged from **-30.0 LUFS to
-22.9 LUFS** across the 5 chapters — a ~7 LU swing, clearly audible as a volume jump at every
chapter boundary. **Root cause:** each chapter is a separate ElevenLabs `/with-timestamps` API
call (`generate_case_assets.py`'s `cmd_audio()`), and ElevenLabs does not guarantee consistent
output loudness across separate calls — nothing in the pipeline normalizes them relative to each
other afterward. The Remotion composition (`SementilliTrial.tsx`/`MuliagaTrial.tsx`-style
components) just plays each chapter's raw mp3 back to back via a plain `<Audio src={...} />` with
no volume adjustment per chapter. **Fix for every future case:** after `cmd_audio()` produces the
per-chapter mp3s, run each through `ffmpeg -af loudnorm` (two-pass, targeting a fixed integrated
loudness, e.g. -24 LUFS) before they reach Remotion's `public/` dir, so every chapter starts from
the same measured loudness rather than trusting ElevenLabs' per-call consistency. This is a
render-pipeline gap, not a one-off — every prior case (Banfield, Richins, Sementilli) has the same
un-normalized multi-chapter structure and is presumably carrying the same defect, just not yet
reported.

## Channel intro bumper — built 2026-07-28 (open since 2026-07-21, escalated by real channel-owner
feedback the same day: published videos "start immediately" and "look raw")
Real 2026 true-crime-channel research (see `Documentation/TREND_LOG.md`'s 2026-07-28 entry for
citations) found two points that initially look contradictory but aren't: long animated intros
measurably hurt retention (~22% average boost in 30-second retention after channels removed
them), but true-crime viewers specifically reward a short, consistent, dramatic structure —
either a brief branded stinger or a distinct cold-open teaser ahead of the Hook. Presented both
options to the channel owner; **short branded stinger was the explicit choice**, over a
cold-open teaser-with-backstory alternative.
- **Component:** `src/ChannelBumper.tsx` — `ChannelBumperComponent` (2.5s @ 30fps = 75 frames,
  exported as `BUMPER_DURATION_FRAMES`) plus a standalone `ChannelBumper` composition for
  isolated preview/render. Visual: "FATAL AFFAIRS" in Impact/Oswald 900-weight 130px, brand
  white on brand black, thin red accent underline — reuses `ChannelTrailer.tsx`'s existing
  title-card styling exactly for visual consistency with the channel trailer. Audio: a real
  generated 2.5s sting (`Assets/audio/channel_bumper/bumper_sting.mp3`, ElevenLabs
  sound-generation API — dark cinematic drone/reverb hit, no melody/percussion), generated
  once and reused unchanged, same principle as the visual.
- **Fixed and reused unchanged across every future video** — this is the one render element
  that should NOT vary case-to-case. Not yet wired into `prep_remotion_render.py`'s per-case
  data generation — the next case's Trial/Short composition should prepend
  `<Sequence from={0} durationInFrames={BUMPER_DURATION_FRAMES}><ChannelBumperComponent />
  </Sequence>` and shift every other Sequence's `from` by `BUMPER_DURATION_FRAMES`, rather than
  copy-pasting the bumper's JSX into each new Trial component.
- **Deliberately NOT applied to the already-published Rimoni Muliaga video** — channel owner's
  explicit instruction was to fix the pipeline for future cases, not retroactively touch a live
  video.
- **Visual-variety point — escalated from "flagged, not built" to a mandatory requirement,
  2026-08-30, after a real channel audit found real supporting evidence:** the same feedback
  pass ("not enough interactivity") is most likely about visual-format variety, not the intro
  specifically — creators report crime-scene/location map graphics boost retention (~35% in one
  cited case) and recommend 5-7 distinct visual element *types* per video, not just narrated
  Ken-Burns pans over still photos for the full runtime. The audit found this is not just theory
  for this channel: main-video average-view-percentage on a real sample (28-36%) is genuinely
  low for a 4-7 minute documentary, consistent with the single-visual-format hypothesis (not
  proof on its own — sample was 3 videos with low absolute view counts — but consistent enough,
  combined with the prior research, to act on rather than keep flagging). **Every case from here
  forward must use at least one non-`SceneImage` visual format** — a `PullQuoteCard` (built,
  ready to use) at minimum, a `SceneClip` (built, needs a real case to test end-to-end) wherever
  `Tools/mugshot_fetch_tool.md` Track 3 finds usable footage. A map/timeline graphic remains
  not yet built — it needs real per-case geographic/chronological content to design against, not a
  generic component; build it when a case's story actually calls for one (e.g. a case with a
  meaningful multi-location chase or a complex timeline worth visualizing), not speculatively.

### PullQuoteCard component (built 2026-08-30)
A second visual format for on-screen text: a full-bleed dark card with a large centered quote
(one striking line from the case — a real quote, not invented), matching the channel's brand
typography (Impact/Oswald headline weight) and color palette (`#111111` background, `#FFFFFF`
text, `#A30E15` accent rule above/below the quote). Distinct from `CaptionOverlay` (which
tracks narration word-by-word) — this is a held, static beat for a scene the narration script
already marks as a quote (`[[SCENE:NNNN]]` text wrapped in quotation marks is the natural
trigger). `src/PullQuoteCard.tsx` — `PullQuoteCardComponent({ quote, attribution })`, used as a
drop-in `SceneImage` replacement in the scene sequence (same duration-frame budget as any other
scene). No new asset sourcing needed — reuses text already in the script.

**Wiring convention (built out 2026-08-30, first real case: Zarrius Hildabrand):** a case's
`ImagePrompts.md` gets a `pull_quote_scenes` array (same pattern as `real_photo_scenes`):
`[{ "scene_id": "0032", "quote": "I did what I did.", "attribution": "Zarrius Hildabrand, to a
friend after his arrest" }]`. That scene_id must NOT also appear in `prompts` — there's no image
to generate or copy for it. `Workflows/prep_remotion_render.py` reads `ImagePrompts.md` directly
(in addition to `timing.json`) and emits a `type: "quote"` scene entry (with `quote`/
`attribution`, no `image`) instead of the usual `type: "image"` entry, skipping the image-file
existence check for that scene entirely. Every case's Trial component (e.g. `HildabrandTrial.tsx`)
must branch per scene on `s.type === "quote"` → `<PullQuoteCardComponent>`, else → `<SceneImage>`
— copy this branch into each new case's Trial component, it isn't automatic.

### SceneClip component (built 2026-08-30)
Plays a real archival video clip (`Tools/mugshot_fetch_tool.md` Track 3) in place of a panned
still, using Remotion's `OffthreadVideo`. `src/SceneClip.tsx` —
`SceneClipComponent({ src, durationFrames, muted })`, same drop-in replacement pattern as
`PullQuoteCard`: swaps in for one scene's `SceneImage` in the sequence list, same
`[[SCENE:NNNN]]` timing. Muted by default (narration carries the audio) — pass `muted={false}`
only for a scene built specifically around real clip audio (e.g. a 911 call). Clip file goes in
the case's `public/{slug}/` dir alongside the scene images, same as any other asset
`prep_remotion_render.py` copies in. Not yet exercised on a real case — the first real use is a
genuine end-to-end test, same as every other Track 1/2 real-asset pipeline was on its first case.
- **Found and fixed while building this:** the local Remotion project's `node_modules`
  (`@remotion/studio`, `@remotion/bundler`, likely others) had missing `dist` files — a latent
  pre-existing install defect masked by webpack's build cache until a new file
  (`ChannelBumper.tsx`) invalidated that cache and forced a fresh bundle-config resolution,
  which then failed on `require.resolve()` calls into the broken packages. Fixed with a full
  `rm -rf node_modules package-lock.json && npm install`. Worth doing this clean reinstall
  proactively at the start of any future session that resumes this render project, rather than
  waiting for a cache-invalidating change to surface it again.

### Track 3 escalated to mandatory-attempt (2026-09-15, real channel audit)
`SceneClip` shipped 2026-08-30 and, per its own note above, was still unused as of the
2026-09-15 audit — every case since (Baziad, Hildabrand, Ferguson, Greer) documented a Track 3
gap in `Sources.md`/`PersonPhotos.md` rather than actually finding and using a clip. **Every
case going forward must make a real, documented search attempt for at least one usable Track 3
clip** (press-conference footage, bodycam, agency-released CCTV — never an outlet's own
trial-camera production, per the existing Court TV exclusion) before falling back to "gap,
none found." A real attempt that finds nothing is still fine to document as a gap — the rule is
"actually try," not "must succeed" — but "gap" without a real search log is no longer
acceptable QC evidence.

### "REAL" badge overlay + source citation (added 2026-09-15, real channel audit finding;
revised same day after real competitor research — see `TREND_LOG.md`'s 2026-09-15 competitor
entry)
Audit found main videos get ~1-14 views each against near-zero `RELATED_VIDEO` traffic — the
channel's AI-generated visuals may read as generic/synthetic to a cold viewer with zero
subscriber trust built up yet. Competitor research found **no evidence of a per-shot "REAL"
badge convention anywhere** (PoliceActivity, Law&Crime BodyCam, Grizzly True Crime) — the pattern
that actually recurs is **on-screen/description source citation** (case number, department name,
"per [outlet]"). Ship both, but treat the citation text as the validated piece and the badge as
the experimental one:

- New shared component `src/RealBadge.tsx` — `RealBadgeComponent({ label, source })`. `label` is
  `"REAL PHOTO"` or `"REAL FOOTAGE"`; `source` is a short citation string (e.g. `"Police Scotland"`,
  `"STV News"`, `"Aberdeen Sheriff Court"` — pull from that scene's `PersonPhotos.md`/`Sources.md`
  attribution, never invent one). Renders as a small pill/tag, top-left corner, brand accent color
  (`#A30E15`) background, white bold text for the label, a smaller lighter line underneath for
  `source` — subtle fade-in over the first ~10 frames matching `PullQuoteCard`'s own fade pattern.
  Low-opacity enough not to obscure the image, high-contrast enough to read at a glance.
- Wire into `SceneImage` and `SceneClip`: both already receive `image`/`src` from `real_photo_
  scenes` in `ImagePrompts.md` (per-scene, matched by `scene_id`) — extend that array's entries
  with a `source` field, pass `isReal={true} source={s.source}` when the scene's `scene_id` is in
  `real_photo_scenes`, and render `<RealBadgeComponent label="REAL PHOTO" source={source} />` (or
  `"REAL FOOTAGE"` for a `SceneClip`) as a sibling overlay when `isReal` is true. Never show the
  badge on an AI-generated scene — a false "REAL" label is worse than no badge at all. If a real
  scene genuinely has no clean attribution string (rare — the mandate is to always document a
  source in `PersonPhotos.md` already), omit `source` and show just the label.
- Applies to Shorts too (`ShortComposition.tsx`'s scene rendering) wherever a Short reuses a
  real-photo scene, same `isReal`/`source` prop threading.
- Since this is an experiment (not a proven competitor pattern), treat the first case that ships
  it as a real test — note in that case's `Checklist.md` whether it shipped correctly, don't
  assume success and move on silently.

### Real archival video - wiring convention (first real use: Stephen McCullagh case, 2026-09-18)
`SceneClip` finally has a real case behind it. A case's `ImagePrompts.md` gets two new arrays, read by
`Workflows/prep_remotion_render.py` and `prep_short_render.py` (helpers in `Workflows/real_media_utils.py`):
- `real_clip_scenes: [{ scene_id, local_path, source, start_sec? }]` - a **muted** real clip replaces one
  narrated scene's image. `prep_*` cuts it with ffmpeg to exactly the scene's length (`start_sec` picks the
  moment inside the master clip; a clip shorter than its scene is **held on its last frame, never looped** -
  looping surveillance footage reads as a fake second event). Rendered by the Trial component's `SceneClip`
  (no Ken-Burns zoom - burned-in CCTV timestamps must stay readable) with a `REAL FOOTAGE` badge (top-right, so
  it doesn't collide with an outlet watermark or timestamp in the top-left).
- `real_media_inserts: [{ after_scene_id, kind: "audio"|"video", local_path, label, source, background_image?,
  captions_json? }]` - real media **with its own audio**, inserted *between narration chapters*. It must sit on a
  chapter boundary (a chapter is one TTS file; `prep_remotion_render.py` refuses otherwise), so split chapters
  where an insert goes. The prep script shifts every later scene/chapter/caption by the insert's length, splits
  caption chunks so none straddles the insert, and emits `quietRanges` so the music bed is silenced under the
  insert's own audio. `kind: "audio"` renders a darkened real photo + word-by-word captions (from
  `captions_json`, produced by speech-to-text on the real audio) + `REAL AUDIO` badge; `kind: "video"` plays the
  clip full-screen with its audio + `REAL FOOTAGE` badge.
- Shorts: `real_clip_scenes` work in Shorts too (ShortComposition `type: "clip"`); a Short can also use a
  real audio file **as its narration track** by writing its own `short_N_timing.json` (scenes + `captionWords`
  from speech-to-text) - McCullagh Short 2 is the raw 999 call with captions and no TTS at all.
- **Encoding gotcha (real failure, 2026-09-18):** the first render died with `Compositor error: No frame found
  at position ...` on a clip that ffmpeg reported as perfectly valid (251 frames, 30 fps). Fix: cut clips with
  `-bf 0 -g 15 -movflags +faststart` (no B-frames, frequent keyframes) - now baked into `cut_clip()`. Re-encode
  any inserted video the same way.
- **Render concurrency rule (real failure, 2026-09-18):** the same `No frame found` error appeared when the main
  render ran at the same time as the Shorts renders (parallel OffthreadVideo compositors). A solo re-run of the
  identical composition rendered cleanly. Render a main video that contains clips **alone**; Shorts can run
  together afterwards.
- **Captions vs. PullQuoteCard in Shorts (2026-09-18):** `ShortComposition` hides the centre captions while the
  frame is inside a `quote` scene - otherwise the caption words collide with the quote card text.

### Real-photo bookending (added 2026-09-15, real channel audit finding — explicit channel-owner
instruction: real photos "и на заставке и в начале ролика и в середине и в конце", not scattered
1-2 mid-video)
Real-photo/footage placement is no longer "wherever the scene plan happens to slot them into the
middle of the scene list." Every case's `ImagePrompts.md` `real_photo_scenes` must now include,
at minimum:
- **The thumbnail** (already mandatory, unchanged — real-photo-only thumbnail rule).
- **The cold-open / first on-screen scene** (scene 0001 or the earliest scene before the Hook
  narration proper) — a real photo or Track 3 clip, not an AI-generated establishing shot, so
  the very first thing a viewer sees after the bumper is real evidence.
- **At least one real scene in the back third of the video** (the closing/aftermath/sentencing
  beats) — not just clustered in the investigation-reveal middle third where it's sat by default
  on every case so far.
- The existing middle-of-video real photos (victim/accused portraits, scene photos) stay as-is —
  this adds bookends, it doesn't replace the existing mandate.
This is a sourcing-order change for scene-to-image assignment when building `ImagePrompts.md`
for the next case, not a new tool.

## Channel outro bumper — built 2026-07-30 (channel owner feedback on the Devyn Michaels video:
"в прошлом видео ты забыл сделать превью в видео и концовку такую же" — the intro bumper existed
but nothing mirrored it at the end)
Presented two options — a short teaser-with-backstory preview vs. the same brand screen repeated
at both start and end — and the channel owner chose the latter: **the exact same
`ChannelBumperComponent`, unchanged, now appears at both the start AND the end of every main
video going forward**, not just the start. This is a standing requirement from the Walter
Buchanan case onward, not a one-off.
- **Implementation:** no new component needed — reuse `ChannelBumperComponent` and
  `BUMPER_DURATION_FRAMES` from `src/ChannelBumper.tsx` unchanged. In the Trial component, add a
  second `<Sequence>` starting at `totalFrames + BUMPER_DURATION_FRAMES` (i.e. right after the
  last scene/caption/audio ends, accounting for the intro bumper's own offset), with
  `durationInFrames={BUMPER_DURATION_FRAMES}`. The `Composition`'s `durationInFrames` must become
  `totalFrames + BUMPER_DURATION_FRAMES * 2` (intro + content + outro), not just `+ 1x` as before.
  See `src/WalterBuchananTrial.tsx` for the first real implementation of this pattern.
- **Not applied to Shorts** — Shorts stay bumper-free at both ends, per the existing
  intro-bumper convention (`Shorts.md`'s "Visual structure and rationale" section), to preserve
  their fast cold-open hook. The "same ending too" feedback was about the main video specifically.
- **Deliberately NOT applied retroactively to the already-published Devyn Michaels video** —
  consistent with the channel owner's standing "fix the pipeline going forward, don't touch a
  live video" precedent from the Rimoni Muliaga case's redaction-margin fix.
- **Total runtime impact:** adds one more `BUMPER_DURATION_FRAMES` (75 frames / 2.5s) to every
  future main video's total length beyond what the intro-only version added. Does not affect any
  mid-video chapter timestamp used in `SEO.md`'s YouTube chapter list — only the video's total
  duration.

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
- **Never hot-swap a public/ asset file while a render is actively in progress — confirmed real
  failure, 2026-08-30 (Hildabrand case).** A redaction fix was copied into the Remotion project's
  `public/{slug}/NNNN.png` while `remotion render` was already running (well before the render
  had reached that scene's frame position by elapsed-time math). The final MP4 still contained
  the stale, pre-fix frame. Root cause: Remotion's headless-Chrome render workers evidently
  prefetch/cache asset requests ahead of the current frame position rather than reading the file
  fresh at the moment each frame is captured, so an in-place overwrite mid-render is not reliably
  picked up even when the timing looks safe on paper. **Fix any asset file before starting the
  render, never during one.** If a defect is found mid-render, let the render finish (or kill it),
  fix every affected file, and do a full clean re-render — don't try to swap in a fix and trust
  the in-flight process to pick it up. Caught by the same frame-spot-check practice this file
  already establishes (verify actual rendered frames, not just that the render completed).
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

### Never combine harness backgrounding with a manual `&` (real failure, 2026-09-22)
Launching a render with the Bash tool's `run_in_background: true` AND a manual trailing `&` /
subshell-backgrounding inside the same shell command spawns the job through **two** independent
mechanisms at once - the result is two concurrent `npx remotion render` processes writing to the
same output file (caught via a `Win32_Process` check both times: once on the main-video launch,
once on the Shorts loop, which produced two concurrent renders of the same composition to the
same `.mp4`). Pick exactly one backgrounding mechanism per render call, never both. If duplicates
are suspected, check `Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match
'remotion render' }` before trusting any render's output.

### Scratchpad node_modules corruption - root cause and the permanent fix (real failure, 2026-09-27)
**What happened:** the Remotion scratchpad project was reused across multiple cases within one
session (McCullagh, Taylor, Spears all rendered fine from it), then broke on the 4th case
(Forcell) with three consecutive "Cannot find module" errors (`@remotion/studio/dist/
renderEntry.js`, then `@remotion/media-parser/dist/index.js` again after a full `npm install`),
each surfacing only once bundling reached that specific package. A single-package reinstall and
a full `rm -rf node_modules && npm install` both failed to fix it - same pinned version
(4.0.525) kept re-resolving broken, strongly suggesting the corruption was in that version's
resolved dependency tree/cache, not something a same-version reinstall could shake off.

**Root cause:** the project's `package.json` had `remotion`/`@remotion/cli` etc. pinned to one
exact version (`4.0.525`) and that same node_modules tree was reused, un-reinstalled, across
every case's render in the session - so any corruption (a bad cache entry, a partial write from
an earlier killed/duplicate render process, or an upstream publish issue in that exact patch)
persisted and accumulated silently until a render finally touched the broken code path.

**The permanent fix (now the DEFAULT, not a recovery step - do this for every case, not just
when something breaks):** scaffold a fresh Remotion project per case rather than reusing one
long-lived directory across a session:
```
npx create-video@latest <case-dir> --yes --blank --no-tailwind
cd <case-dir> && npm install
```
No version is pinned, so this always resolves whatever the current published patch is (the
2026-09-27 incident's fix landed on 4.0.529, one patch ahead of the broken 4.0.525 - a fresh,
unpinned install cannot inherit a stale/corrupted resolution the way a long-lived reinstall can).
Copy over only the shared components (ChannelBumper.tsx, PullQuoteCard.tsx, RealBadge.tsx,
ShortComposition.tsx) and the current case's own `*Trial.tsx`/`*Shorts.tsx`/`*_data.ts` files and
`public/<case>` + `public/shorts/*` dirs into the new project - never copy node_modules itself.
One asset does NOT live in the scratchpad and must be re-copied from its durable location every
time: the channel bumper's sting audio, at
`ProductionStudio/Assets/audio/channel_bumper/bumper_sting.mp3` (goes to `public/bumper/` in the
project). This costs about one extra minute per case versus reusing a directory - cheap
insurance against a multi-hour debugging session, and consistent with the existing
`graphify`/scratchpad philosophy already in memory (`feedback_graph_holds_the_names.md`): nothing
in the Remotion scratchpad is meant to be durable state, so don't treat it as durable by reusing
it indefinitely.

**Fresh-scaffold gotchas found 2026-10-02 (Williams case):** (1) a current `create-video --yes
--blank --no-tailwind` scaffold no longer creates `src/index.css` AND no longer installs
tailwind, but `Root.tsx` imports `./index.css` - bundling fails with "Can't resolve './index.css'".
Create `src/index.css` as a one-line plain comment (components use inline styles; do NOT copy a
previous project's `@import "tailwindcss"` file, it fails with `NotFound("tailwindcss")`).
(2) A render longer than ~4 minutes of video (253 s main) outlived the Bash background time limit:
the harness reported the task "killed" but the node/chrome-headless-shell tree kept running
orphaned and wrote the finished file ~15 min later. Don't start a second render; check
`Get-Process chrome-headless-shell` and wait for `out/<file>.mp4`, then verify with `ffprobe`
(duration) before trusting it.

**Process hygiene, unchanged:** never combine the Bash tool's backgrounding with a manual `&`
(see the entry above) - when debugging a suspected duplicate/corrupted render, check
`Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'remotion render' }` to
confirm exactly one `node.exe` process is running before trusting any output.

**Short cold-open / CTA knobs (added 2026-10-14):** `prep_short_render.py` takes `--cold-open-seconds` (default 1.5; `0` = narration and the first scene start at frame 0) and `--cta-seconds` (default 3.5); the closing CTA text is the existing positional `cta_text` argument. `ShortComposition.tsx` must guard the cold-open `<Sequence>` with `data.coldOpenFrames > 0` (Remotion rejects a zero-length Sequence). Reason: the channel's Studio data showed 69.9% of viewers swipe away and the cold open delays the first narrated second; whether removing it helps is an open A/B test (see Documentation/TREND_LOG.md, 2026-10-14). Keep the defaults for control Shorts.

**`--first-scene-real` (added 2026-10-13):** with `--cold-open-seconds 0`, the real cold-open photo becomes the first scene under the narration (it replaces a leading pull-quote card too; skipped if one of the first two scenes is already a real photo/clip). Pass a vertical face-centred crop (e.g. `*_9x16.jpg`) as the cold-open image: the 16:9 centre crop can cut the face off at the frame edge.
