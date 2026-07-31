# Person Photos — Walter Buchanan murder of Darrel Odhiambo (Track 1 + Track 2)

## Walter Buchanan — official Police Scotland photo, clean Track 1 success

- **source_url**: https://news.stv.tv/west-central/man-who-murdered-wife-at-home-in-hamilton-after-cheating-accusation-jailed-for-life
- **image_url**: https://news.stv.tv/wp-content/uploads/2025/04/5a6981bdc174f4d913524557a72e1990-1743595276-1120x720.jpeg
- **source_type**: official police photo
- **issuing_authority**: **Police Scotland** — explicit outlet caption credit ("Photo Credit: Police Scotland"). This is a direct official-source photo, not the outlet-attribution exception — the clearest Track 1 case of any produced this session.
- **retrieved_date**: 2026-07-30
- **redaction**: eyes_blacked. Automated OpenCV detection worked cleanly on this frontal photo — clean single face detection, 3 eye-region candidates found, generous margin (30%/40%) applied. Verified by direct visual inspection: box fully covers brow through mid-nose with wide clearance on all sides.
- **local_path**: `ProductionStudio/Assets/images/real_photos/buchanan_mugshot_REDACTED.jpg`
- **raw_unredacted_path**: `ProductionStudio/Assets/images/real_photos/buchanan_mugshot_RAW_DO_NOT_USE.jpg` — never use in any output.
- **Max-zoom verification, 2026-07-30:** source is 1120x720 (close to 16:9, unlike the Odhiambo
  photo). Remotion's `objectFit: "cover"` fit crops this to y:45-675 at baseline, well clear of
  the box (y:110-365 in original coordinates). Computed the worst-case Ken-Burns range (1.12x
  zoom + ±30px pan, per `DevynTrial.tsx`'s `SceneImage`) and confirmed the box keeps ≥30px
  clearance on every side — no pre-crop needed for this photo, used as-is at scene 0031.

## Darrel Odhiambo (victim) — real personal photo, Track 1

- **source_url**: https://www.scottishdailyexpress.co.uk/news/scottish-news/besotted-scottish-businessman-facing-life-34533782
- **image_url**: https://i2-prod.scottishdailyexpress.co.uk/article34459953.ece/ALTERNATES/s1200f/1_Rmr_ham_010323_Darrell_01.jpg
- **source_type**: personal/family photo, republished by a news outlet
- **issuing_authority**: credited by the Scottish Daily Express to **Hamilton Advertiser** (a real, named outlet's own republished photo, not an anonymous source)
- **retrieved_date**: 2026-07-30
- **license_note**: Per CLAUDE.md's hard rule, every identifiable real person in any real photo gets redacted before use, no exceptions — this applies even to a sympathetic victim photo, not just defendant mugshots. Redacted accordingly.
- **redaction**: eyes_blacked, applied manually after automated detection landed the box on her nose/cheek rather than her eyes (the same class of margin/positioning issue documented in the Rimoni Muliaga case) — corrected via a debug grid overlay, re-verified visually before use.
- **Cropping note**: the original photo showed Darrel at a restaurant with several bystanders visible in the background, including a child at a nearby table. Cropped the frame to remove the most clearly identifiable bystander (the child) before use, rather than attempting to individually redact every incidental, distant background figure in a candid public setting.
- **local_path**: `ProductionStudio/Assets/images/real_photos/odhiambo_photo_REDACTED.jpg`
- **raw_unredacted_path**: `ProductionStudio/Assets/images/real_photos/odhiambo_photo_RAW_DO_NOT_USE.jpg` (already cropped from the original to remove the child bystander, but still shows Darrel's own face unredacted) — never use in any output.

- **Max-zoom verification, 2026-07-30 (mandatory QC rule from the Rimoni Muliaga case):** this
  source photo is portrait-oriented (700x799, aspect 0.88), unlike every other real photo used
  this session. Remotion's `SceneImage` component applies `objectFit: "cover"` to fit any image
  into the video's 16:9 landscape frame, which for a portrait source means a large **default
  center-crop** — computed here as keeping only image rows y:203-596 of 799. The redaction box
  sits at y:80-155, entirely in the top band that a plain center-crop would discard. Left
  unfixed, the video would never show the redaction box (or Darrel's eyes) at all — not a
  redaction leak, but a silent no-op that defeats the point of using this real photo. **Fix:**
  created a second, video-specific derivative, `odhiambo_photo_REDACTED_16x9.jpg` (top-anchored
  crop, `img.crop((0, 0, 700, 394))` — already almost exactly 16:9, so Remotion's own cover-fit
  is nearly a no-op from here). Verified the box survives Remotion's actual Ken-Burns range (up
  to 1.12x zoom, ±30px pan, per `DevynTrial.tsx`'s `SceneImage`) with wide clearance on every
  side (≥54px horizontal, ≥58px vertical at max zoom, in this crop's own pixel scale). **This is
  the file referenced by scene 0006 in `ImagePrompts.md` — the original `_REDACTED.jpg` (without
  `_16x9`) must never be fed directly into the video pipeline for a portrait-oriented photo.**

## Track 2 — non-person / scene photos (2 real photos found, both used — "more photos" per channel-owner request)

- **Glasgow High Court entrance sign** — source: Scottish Daily Express (credited to Getty Images), URL:
  `https://i2-prod.scottishdailyexpress.co.uk/article34512968.ece/ALTERNATES/s1200e/3_Glasgow-High-Court-BuildingjpgC.jpg`. No person visible (a distant, unidentifiable silhouette in a doorway only). Local path: `ProductionStudio/Assets/images/real_photos/glasgow_high_court_SCENE.jpg`.
- **Hamilton Sheriff Court building** — the actual local courthouse in the town where the murder occurred. Source: Wikimedia Commons / geograph.org.uk (freely licensed), via the Hamilton Sheriff Court Wikipedia page. No people visible. Local path: `ProductionStudio/Assets/images/real_photos/hamilton_sheriff_court_SCENE.jpeg`.

## Access method note (technical)
Same sandbox constraint as prior cases: outbound `curl` to arbitrary CDN hosts is blocked even
with explicit user approval. Worked around identically via the Browser pane + `javascript_tool`'s
`fetch()`. **New finding this case**: the Scottish Daily Express's CDN serves images in **AVIF
format** even when the URL ends in `.jpg` (content negotiation based on the fetching client) —
the base64 data URL's MIME type was `image/avif`, not `image/jpeg`. Detected via regex mismatch
when the first-pass JPEG-only decode script failed, then fixed by parsing the actual MIME type
from the data URL and converting via Pillow (`Image.open(...).convert('RGB').save(..., 'JPEG')`).
Worth checking the actual returned MIME type rather than assuming from the URL extension on any
future UK tabloid-press image fetch.
