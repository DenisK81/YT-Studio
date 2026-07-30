```json
{
  "text_options": ["SHE BEHEADED HIM", "NEVER TESTED", "MARRIED THE SON"],
  "chosen_primary": "SHE BEHEADED HIM",
  "base_image_source": "REAL PHOTO — official Henderson Police Department booking photo",
  "base_image_path": "ProductionStudio/Assets/images/real_photos/michaels_mugshot_REDACTED.jpg",
  "base_image_credit": "Henderson Police Department, via Las Vegas Review-Journal (see Cases/devyn-michaels-decapitation/PersonPhotos.md)",
  "style_tags": ["real-photo-base", "16:9", "eyes-redacted", "no watermark"]
}
```

**Real photo, continuing the studio's established practice** (per the Rimoni Muliaga case) of
building the thumbnail from a real, redacted photo rather than an AI generation whenever a real
Track 1 photo is available. This case had a clean, front-facing official mugshot — a stronger
source than Muliaga's off-angle press photos — so the redaction margin was made deliberately
generous (30%/40% beyond the detected eye box, per the 2026-07-28 lesson from that case) and
verified to survive both the thumbnail crop and the video's Ken-Burns zoom.

**Build process:**
1. Base is the redacted official Henderson PD booking photo of Devyn Michaels (see
   `PersonPhotos.md`).
2. Cropped to 1280x720 (manually positioned — the automatic "quarter down" crop rule from the
   Muliaga case cut off too much of the face for this taller source photo; positioned to keep
   the redaction box plus jaw/mouth in frame, not mostly hair), graded (desaturated ~30%,
   contrast +20%, brightness -20%, subtle #A30E15 red-accent blend at 7%), bottom-weighted dark
   vignette for text legibility.
3. Headline in Impact, white fill + black stroke, auto-sized, centered lower third.
4. Output: `ProductionStudio/Assets/images/devyn-michaels-decapitation/thumbnail_with_text.png`
   (final) and `.../thumbnail.png` (graded base, no text).

**Rationale for "SHE BEHEADED HIM":** leads with the single most shocking, simplest verified
fact — direct, no euphemism — matching the channel's brand rule of large dramatic imagery +
max-3-word high-impact text. "NEVER TESTED" (the untested-swords evidentiary gap) and "MARRIED
THE SON" (the tangled family relationship) were considered but held back as Shorts hooks instead,
since they work better as a secondary reveal than a cold-open thumbnail line.

**Redaction note:** the black box is the mandatory eyes-blacked redaction from `PersonPhotos.md`,
applied with a wide margin specifically verified against this video's actual Ken-Burns zoom
range, not just the static source photo (per the 2026-07-28 QC rule) — not a rendering error.
