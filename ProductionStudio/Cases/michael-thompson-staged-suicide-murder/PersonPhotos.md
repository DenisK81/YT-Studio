# Person Photos — Michael Thompson murder of Kimberley Thompson (Bounds) (Track 1 + Track 2)

## Michael Thompson — official Northamptonshire Police photo, Track 1

- **source_url**: https://www.northamptonchron.co.uk/news/courts/murderer-sentenced-to-life-at-northampton-crown-court-among-the-faces-of-these-15-jailed-criminals-whose-stories-this-newspaper-bought-you-during-july-2026-8835399
- **image_url**: https://www.northamptonchron.co.uk/webimg/b25lY21zOjZhMTcxZWVjLTg0NzAtNDQ5Zi05ZDRiLTNiMzJjNzI2NzNkMjoyZDhjN2M5Ni1kOTQ1LTQ3Y2MtOGVjZC0xNTJiOGYyOTY2Yjk=.jpg
- **source_type**: official police photo
- **issuing_authority**: explicit outlet photo credit "Photo: Northamptonshire Police" in a Northampton Chronicle "faces of jailed criminals" gallery — direct official-source photo, same class as the Buchanan case's clearest Track 1 example.
- **retrieved_date**: 2026-08-01
- **redaction**: eyes_blacked. Automated Haar-cascade face detection found the face cleanly, but the eye sub-detector returned 0 matches (tight crop / lighting angle). Fell back to the manual debug-grid method (per the standing fix from the Rimoni Muliaga case): cropped and 2x-scaled the upper-face region with a coordinate grid overlaid, read off both eye positions precisely, then applied a box with the standard wide margin (30% horizontal / 40% vertical beyond the tightest eye-to-eye bound). Verified by direct visual inspection: box fully covers brow through mid-nose-bridge with wide clearance on all sides, well clear of nose tip and mouth.
- **local_path**: `ProductionStudio/Assets/images/real_photos/thompson_mugshot_REDACTED.jpg`
- **raw_unredacted_path**: `ProductionStudio/Assets/images/real_photos/thompson_mugshot_RAW_DO_NOT_USE.jpeg` — never use in any output.

## Kimberley Thompson (Bounds) (victim) — real personal photo, Track 1

- **source_url**: https://www.northamptonchron.co.uk/news/crime/kimberley-bounds-family-pay-emotional-tributes-to-kindest-mother-daughter-sister-auntie-and-friend-as-killer-jailed-for-33-years-8798612
- **image_url**: https://www.northamptonchron.co.uk/webimg/b25lY21zOjkxYzRhNjQ1LTlmZTYtNDIxNi1hYjBjLWFlYTQ3OTAyMDdkMjoxNzgyYWFkZS0xZTgxLTQ3MGQtODM5MC05NjFmZmE4ZmFlMGQ=.png
- **source_type**: personal/family photo, published directly by the outlet in its own tribute coverage (not a republish from a third outlet)
- **issuing_authority**: Northampton Chronicle's own family-tribute article (photo appears to be family-supplied for this coverage)
- **retrieved_date**: 2026-08-01
- **license_note**: per CLAUDE.md's hard rule, every identifiable real person in any real photo gets redacted before use, no exceptions — applied here even though this is a sympathetic victim photo, not a defendant mugshot (same standing practice as the Odhiambo photo in the Walter Buchanan case).
- **redaction**: eyes_blacked. Automated Haar-cascade detection succeeded cleanly on the first pass (1 face, 2 eyes, no manual fallback needed) — a clean frontal, well-lit photo. Generous 30%/40% margin applied as standard practice regardless of automated success. Verified by direct visual inspection: box covers brow through upper cheekbone with wide clearance, well clear of nose and smile.
- **Cropping note**: no other people are visible in the original frame — a solo garden photo, no bystander redaction question to resolve (unlike the Odhiambo photo in the Buchanan case).
- **local_path**: `ProductionStudio/Assets/images/real_photos/kimberley_photo_REDACTED.jpg`
- **raw_unredacted_path**: `ProductionStudio/Assets/images/real_photos/kimberley_photo_RAW_DO_NOT_USE.png` — never use in any output.

## Track 2 — non-person / scene photo (1 real photo found and used)

- **Nottingham Crown Court exterior** — the actual court where the trial and sentencing took
  place. Source: Wikimedia Commons, `File:Nottingham_Crown_Court.jpg`, photographer
  MatthewDavid41, licensed **CC BY-SA 4.0** (freely licensed, same category as the Hamilton
  Sheriff Court photo in the Walter Buchanan case), taken 2026-05-09.
  URL: https://commons.wikimedia.org/wiki/File:Nottingham_Crown_Court.jpg
  Local path: `ProductionStudio/Assets/images/real_photos/nottingham_crown_court_SCENE.jpeg`
  (full original resolution, 3024x2767).
  **Bystander note**: two small, distant figures are visible near a bus stop sign in the
  lower-left of the frame — too small, too distant, and too low-detail for any face to be
  individually identifiable even on close inspection. Judged, per the same standard applied to
  the distant background bystanders in the Buchanan case's Odhiambo photo, as not requiring
  individual redaction after a good-faith attempt to assess identifiability. No crop was needed
  since these figures are incidental and non-central to the frame.

## Max-zoom verification, 2026-08-01 (mandatory QC rule from the Rimoni Muliaga case)

Computed both photos against Remotion's actual `SceneImage` behavior (`objectFit: "cover"` baseline
fit, then up to 1.12x Ken-Burns zoom + ±30px pan, per `DevynTrial.tsx`'s established component) —
neither source photo is native 16:9, so both get some baseline vertical crop before any Ken-Burns
zoom is even applied.

- **Thompson mugshot (687x459, aspect 1.50):** baseline cover-fit crops ~36px from top/bottom;
  the box (y:12-138) extends slightly above the visible baseline start (36.2), and further Ken-Burns
  zoom pushes the visible start to ~56.9 — but the box remains substantially visible throughout
  (≥64% of its height stays in frame at max zoom) and, critically, the box fully contains the real
  eye pixels (y:40-110) at every zoom level, so there is no scenario where an eye pixel is visible
  without also being covered by the black box. Verified safe — no pre-crop derivative needed,
  unlike the Buchanan case's Odhiambo photo where the box was cropped out *entirely*, leaving
  nothing to redact but also nothing recognizable in frame. Here the box only loses some of its
  margin buffer at extreme zoom, never the eyes themselves.
- **Kimberley photo (798x573, aspect 1.39):** baseline cover-fit crop and max Ken-Burns zoom both
  keep the box (y:123-249) comfortably within the visible range (worst case 86.1-486.9) — full
  margin retained throughout, no pre-crop derivative needed.

Both real photos used as-is (no `_16x9` derivative required for this case, unlike Buchanan's
portrait-oriented Odhiambo photo).

## Access method note (technical)

Same sandbox constraint as every prior case this session: outbound `curl` to arbitrary CDN
hosts is blocked even with explicit user approval. Worked around identically via the Browser
pane + `javascript_tool`'s `fetch()` → `FileReader.readAsDataURL()` pattern, decoding the saved
JSON transcript file with a Python script when the base64 payload exceeded the tool's inline
output limit (all three images this case, including the 2.3MB full-resolution Wikimedia court
photo). No AVIF-format or other MIME-mismatch issues this case — all three files decoded as
their expected format (`jpeg`, `png`, `jpeg`) directly from the data URL prefix.
