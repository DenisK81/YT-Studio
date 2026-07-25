# Channel Trailer — Fatal Affairs

## Purpose
A ~60-second, movie-trailer-style channel preview (YouTube's "Channel Trailer" slot for
non-subscribers) — not a case video, not a Short. Replaces the current unbranded/no-identity
preview. Requested 2026-07-25.

## Brand facts used (from `Config/config.schema.json`, unchanged)
- Channel name: **Fatal Affairs**
- Slogan: **"Every Affair Has a Story. Some End in Murder."**
- Colors: bg `#111111`, text `#FFFFFF`, accent `#A30E15`, gray `#4D4D4D`, light_gray `#BDBDBD`
- Headline font: Bebas Neue / Oswald Bold; body: Montserrat

## Voice
Researched ElevenLabs' voice library for a movie-trailer register (dramatic/deep/cinematic
categories all point the same direction). Picked via the ElevenLabs voice-search tool:
**Brian — "Deep, Resonant and Comforting"** (`voiceId: nPczCjzI2devNBz1zQrb`, American,
middle-aged, classy/social_media use-case). Deliberately different from the standard case-
narration voice (`wSChTcAxdiTjLPhHeyrM`) — a trailer needs a distinct, more theatrical register
than the documentary narration voice used inside actual case videos.

## Script (real per-word ElevenLabs timing, not estimated)
```
[[SCENE:0001]] Every one of them looked like a normal life.
[[SCENE:0002]] A husband. A wife. A family.
[[SCENE:0003]] Behind closed doors, something else was happening.
[[SCENE:0004]] An affair.
[[SCENE:0005]] A lie.
[[SCENE:0006]] A plan.
[[SCENE:0007]] Real cases. Real evidence.
[[SCENE:0008]] Real verdicts.
[[SCENE:0009]] The people who thought they'd gotten away with it.
[[SCENE:0010]] They didn't.
[[SCENE:0011]] This is Fatal Affairs.
[[SCENE:0012]] Every affair has a story.
[[SCENE:0013]] Some end in murder.
[[SCENE:0014]] New cases, every week.
[[SCENE:0015]] Subscribe.
```
63 words total. Scenes 1-10 are the photo montage; scenes 11-15 drive the closing logo/CTA
card's internal beat timing (no photo, pure branded graphic).

## Collage images (all already-owned/produced, or freshly generated — no third-party clips)
1. `Assets/images/monica-sementilli-hairdresser-murder/0001.png` — girl at backyard pool, dusk
2. `Assets/images/kouri-richins-fentanyl-murder/0001.png` — family home pool at dusk
3. `Assets/images/channel_trailer/corkboard.png` — investigation corkboard (new, generic)
4. `Assets/images/channel_trailer/crimetape_rain.png` — rainy night street, police lights (new, generic)
5. `Assets/images/monica-sementilli-hairdresser-murder/0032.png` — phone glow in funeral pew
6. `Assets/images/kouri-richins-fentanyl-murder/0030.png` — phone glow, texts
7. `Assets/images/monica-sementilli-hairdresser-murder/0026.png` — surveillance monitor wall
8. `Assets/images/kouri-richins-fentanyl-murder/0050.png` — courthouse steps, red/blue lights
9. `Assets/images/real_photos/banfield_mugshot_REDACTED.jpg` — **real** photo (eyes redacted per
   `Tools/mugshot_fetch_tool.md`'s standing policy), from the Banfield case already produced by
   this channel
10. `Assets/images/monica-sementilli-hairdresser-murder/thumbnail.png` — clean base thumbnail
    (no burned-in text, to avoid clashing with this trailer's own text overlay)

**Rights basis:** images 1, 2, 5, 6, 7, 8, 10 are stills from videos this channel already
produced and owns (Kouri Richins, Monica Sementilli) — reusing our own cleared content, no new
rights question. Image 9 is the real redacted mugshot already cleared for the Banfield video
under the documented newsworthy-exception analysis (`Documentation/ARCHITECTURE.md` → "Real-
photo sourcing decision"). Images 3-4 are freshly AI-generated, generic (no real person/case
depicted), same fal.ai Flux schnell pipeline as every other image in this studio — chosen over
any third-party stock/footage specifically to avoid a new, ungoverned rights question for a
channel-level asset.

## Structure (target ≤ 60s / 1800 frames @ 30fps, real total confirmed after audio generation)
- Scenes 1-10: one collage image each (Ken Burns), real per-scene duration from ElevenLabs
  alignment — naturally accelerates on the short lines ("An affair." / "A lie." / "They
  didn't.") for trailer-style rapid cuts near the climax.
- Big bold on-screen text per scene = that scene's own spoken line (classic trailer
  convention), Bebas Neue, white fill + black stroke, center-screen.
- Scenes 11-15: no photo — solid `#111111` background, "FATAL AFFAIRS" title card scales/fades
  in on scene 11, slogan splits across scenes 12-13, "NEW CASES EVERY WEEK" + a pulsing
  SUBSCRIBE button-style graphic on scenes 14-15.
- Music: one `Assets/audio/music_bed/bed_XX.mp3` track, -18dB below narration (fixed studio
  mix spec, unchanged), looped/trimmed to the real total duration.

## Status
Rendered 2026-07-25: 30.1s (well under the 60s cap), 1920x1080, 903 frames @ 30fps.
`Assets/renders/fatal-affairs-channel-trailer.mp4` (gitignored, like all renders). Spot-checked
cold open, mugshot beat, and full logo/CTA sequence frame-by-frame — captions/text legible, no
garbled on-screen text, redaction intact on the real Banfield photo. Awaiting the channel
owner's review before it replaces the current channel trailer in YouTube Studio (uploading a
channel trailer is a manual step in YouTube's own UI, not something this pipeline automates).
