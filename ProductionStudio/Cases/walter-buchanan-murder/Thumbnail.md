```json
{
  "text_options": ["STRANGLED HIS WIFE", "LIED TO 911", "CAUGHT HIM CHEATING"],
  "chosen_primary": "STRANGLED HIS WIFE",
  "base_image_source": "REAL PHOTO — official Police Scotland booking photo",
  "base_image_path": "ProductionStudio/Assets/images/real_photos/buchanan_mugshot_REDACTED.jpg",
  "base_image_credit": "Police Scotland, via STV News (see Cases/walter-buchanan-murder/PersonPhotos.md)",
  "style_tags": ["real-photo-base", "16:9", "eyes-redacted", "no watermark"]
}
```

**Real photo, continuing the studio's established practice** of building the thumbnail from a
real, redacted photo rather than an AI generation whenever a clean Track 1 photo is available.
This case's official Police Scotland photo was a clean, front-facing frontal shot — automated
redaction worked cleanly on the first pass, generous 30%/40% margin — so it needed no manual
correction, unlike the Devyn Michaels or Odhiambo photos this session.

**Build process:**
1. Base is the redacted official Police Scotland photo of Walter Buchanan (see `PersonPhotos.md`).
2. Source photo is 1120x720 (not native 16:9) — cropped evenly top/bottom to 1120x630, then
   resized to 1280x720. The redaction box sits well within the vertical middle of the frame, so
   an even top/bottom crop (unlike the Devyn case's manual off-center crop) kept the box fully in
   frame with wide clearance on all sides — verified by direct visual inspection after crop.
3. Graded (desaturated 30%, contrast +20%, brightness -20%, subtle #A30E15 red-accent blend at
   7%), bottom-weighted dark vignette for text legibility.
4. Headline in Impact, white fill + black stroke (8px), auto-sized to fit width, centered lower
   third.
5. Output: `ProductionStudio/Assets/images/walter-buchanan-murder/thumbnail_with_text.png`
   (final) and `.../thumbnail.png` (graded base, no text).

**Rationale for "STRANGLED HIS WIFE":** leads with the single most shocking, simplest verified
fact — the actual cause of death — direct, no euphemism, matching the channel's brand rule of
large dramatic imagery + max-3-word high-impact text. "LIED TO 911" (the consciousness-of-guilt
angle the judge cited) and "CAUGHT HIM CHEATING" (the twist on who accused whom) were considered
but held back as Shorts hooks instead, since both work better as secondary reveals than a
cold-open thumbnail line.

**Redaction note:** the black box is the mandatory eyes-blacked redaction from `PersonPhotos.md`,
verified to survive the 16:9 crop with wide clearance — still needs verification against this
video's actual Ken-Burns zoom range once the Remotion component is built, per the standing QC
rule from the Rimoni Muliaga case.
