```json
{
  "text_options": ["STAGED HER SUICIDE", "HE FAKED THE CPR", "33 YEARS FOR THE LIE"],
  "chosen_primary": "STAGED HER SUICIDE",
  "base_image_source": "REAL PHOTO — official Northamptonshire Police photo",
  "base_image_path": "ProductionStudio/Assets/images/real_photos/thompson_mugshot_REDACTED.jpg",
  "base_image_credit": "Northamptonshire Police, via Northampton Chronicle (see Cases/michael-thompson-staged-suicide-murder/PersonPhotos.md)",
  "style_tags": ["real-photo-base", "16:9", "eyes-redacted", "no watermark"]
}
```

**Real photo, continuing the studio's established practice** of building the thumbnail from a
real, redacted photo whenever a clean Track 1 photo is available. This source photo is a very
tight, close-cropped official mugshot (687x459) — even tighter framing than prior cases' source
photos, so the final thumbnail reads as an extreme close-up (nose/mouth fill most of the lower
frame). This is consistent with the source material rather than a cropping error.

**Build process:**
1. Base is the redacted official Northamptonshire Police photo of Michael Thompson (see
   `PersonPhotos.md`) — redaction applied via the manual debug-grid method since automated eye
   detection failed on this photo (face detected, eyes did not).
2. Source is 687x459 (not native 16:9) — cropped from the top (`top=0`, keeping the full head
   and redaction box, losing only ~73px of chin/neck from the bottom) rather than an even
   top/bottom split, since an even split would have clipped the top of the redaction box itself
   — caught and corrected after the first attempt visibly cut the box's top edge.
3. Graded (desaturated 30%, contrast +20%, brightness -20%, subtle #A30E15 red-accent blend at
   7%), bottom-weighted dark vignette for text legibility.
4. Headline in Impact, white fill + black stroke (8px), auto-sized to fit width, centered lower
   third.
5. Output: `ProductionStudio/Assets/images/michael-thompson-staged-suicide-murder/thumbnail_with_text.png`
   (final) and `.../thumbnail.png` (graded base, no text).

**Rationale for "STAGED HER SUICIDE":** leads with the single most attention-grabbing, verified
fact — not the murder itself (which every true-crime thumbnail implies) but the specific,
unusual detail that makes this case stand out: he didn't just kill her, he spent time
afterward building a false story before ever calling for help. "HE FAKED THE CPR" and "33 YEARS
FOR THE LIE" were considered but held back as Shorts hooks, since both work as secondary reveals
rather than the cold-open line.

**Redaction note:** the black box is the mandatory eyes-blacked redaction from `PersonPhotos.md`,
verified to survive the 16:9 crop with the corrected top-anchored crop — still needs verification
against this video's actual Ken-Burns zoom range once the Remotion component is built, per the
standing QC rule from the Rimoni Muliaga case.
