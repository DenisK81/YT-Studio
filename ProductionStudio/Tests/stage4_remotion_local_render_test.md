# Remotion — local render test (2026-07-20)

First real Phase 2 infrastructure test: prove the render engine `Tools/remotion_assembly_tool.md`
depends on actually works on this machine, using real assets from the Banfield case rather than
a throwaway "hello world" composition. Per the tool file's own long-standing note: *"Claude Code
should scaffold a minimal composition first and confirm render output before wiring it into the
full agent chain."*

## Environment setup
- Node.js, npm, and Docker were all absent from this machine (confirmed via `node --version` /
  `npm --version` / `docker --version` all failing before this).
- Installed Node.js LTS via `winget install OpenJS.NodeJS.LTS --accept-package-agreements
  --accept-source-agreements` — resolved to v24.18.0, npm 11.16.0.
- PATH doesn't persist across separate Bash tool calls in this environment, so every subsequent
  command needed `export PATH="/c/Program Files/nodejs:$PATH"` prepended.

## Project scaffold
- `npx create-video@latest --yes --blank --no-tailwind remotion-test` — this actually created the
  project inside the repo root the first time (a relative-path `cd` to the intended scratch
  location silently failed first, and the scaffold command still ran from the fallback cwd).
  Caught via `git status` showing nothing added — the project was moved out to the session
  scratchpad directory (`.../scratchpad/remotion-test`) before installing dependencies, so the
  actual studio repo never had Node.js artifacts committed or even present in its working tree.
- `npm install` — 365 packages, no errors.

## Real assets used (not synthetic test data)
- `ProductionStudio/Assets/images/0001.png` — the real fal.ai/Flux-generated Hook-scene image
  from this session's Stage 2 image_gen_tool test.
- `D:\SHOPS\AI Projects\YT_Crime\Voices\tts_2026-07-19T04-29-43-923Z.mp3` — the corrected
  Jimmy-voice Hook TTS clip from this session's Stage 1/2 elevenlabs_voice_tool test (17.87s,
  read via `mutagen`).
- `ProductionStudio/Assets/audio/music_bed/bed_05.mp3` — one of the 10 real hand-picked Pixabay
  tracks.
- The real Hook-beat text from `Cases/brendan-banfield-double-murder/Voiceover.txt`.

## What was built
A custom `HookTestComponent` (replacing the blank template's placeholder) implementing:
- **Ken Burns pan/zoom**: `interpolate(frame, [0, DURATION_FRAMES], [1, 1.12], ...)` on CSS
  `scale()`, plus a slight `translateX` — subtle, visible across the clip, matches the
  documentary style `remotion_assembly_tool.md` calls for.
- **Karaoke captions**: text chunked into 3-word groups, each chunk's on-screen window computed
  by **proportional word-count timing** (not the written "2s minimum" rule — see finding below),
  with the currently-spoken word inside each chunk highlighted in `#A30E15` against white,
  `WebkitTextStroke` for the black outline, Montserrat Bold, centered lower-third.
- **Audio mix**: voiceover `<Audio>` at default volume, music `<Audio volume={0.126}>` — `0.126
  = 10^(-18/20)`, i.e. Remotion's linear `volume` prop computed from the fixed -18dB spec.
- Composition: `1920x1080`, `30fps`, `536` frames (`17.87s`), id `BanfieldHookTest`.

## Real findings (not hypothetical — hit these building it)
1. **The "minimum 2 seconds per caption phrase" rule breaks continuous main-video narration.**
   62 words over 17.87s (~3.5 words/sec) — a 2s floor on 3-word chunks would require ~40s of
   captions to cover 17.87s of audio. Fixed in `Tools/remotion_assembly_tool.md`: natural
   proportional timing for the main video, the 2s floor stays correct for Shorts (sparse, punchy,
   by design).
2. **Blind fixed-word-count chunking (every 3 words) cuts across natural clause boundaries** —
   e.g. "...needs him to be —" and "and the husband..." ended up as separate, awkwardly-timed
   chunks split right at a dash. Documented as the right target (break on punctuation/clause
   boundaries) but not implemented in this test — would need real NLP/clause-boundary logic, out
   of scope for a render-mechanics proof.
3. **Remotion's `<Audio>` component has no built-in EQ.** The fixed mixing spec's "1-3kHz dip /
   high-pass / low-pass" would need an actual audio-processing step (e.g. a Web Audio API graph
   or an external library), not just the `volume` prop. Only the volume/level part of the mixing
   spec was actually implemented and tested here.
4. **No `ffmpeg` on this machine either.** Not needed for this basic render (Remotion bundles
   its own encoding), but frame extraction for visual verification needed `cv2.VideoCapture`
   instead of the more usual `ffmpeg -ss ... -frames:v 1`. Worth installing `ffmpeg` before real
   production renders in case Remotion needs it for other operations at scale.

## Result
Render succeeded: 536/536 frames, encoded to a 12.8MB MP4, no errors. Verified by actually
extracting and looking at frames at multiple points (10, 150, 300, 480) via OpenCV — captions
render with correct styling and karaoke highlighting, the Ken Burns pan is visible, audio muxed
into the output file. **This closes the open "not tested against a real Remotion project" item**
that existed in `Tools/remotion_assembly_tool.md` since it was first drafted.

Not committed to the repo — this was a local scratch proof-of-concept (per the approved plan),
not the real Phase 2 render worker. The real worker build (proper clause-aware caption chunking,
actual EQ processing, wired to receive real agent output rather than hand-copied test assets)
is future work, tracked via the findings above.
