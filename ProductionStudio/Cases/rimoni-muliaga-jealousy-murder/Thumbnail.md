```json
{
  "text_options": ["SHE NEVER CHEATED", "KILLED OVER NOTHING", "NO AFFAIR EXISTED"],
  "chosen_primary": "SHE NEVER CHEATED",
  "base_image_source": "REAL PHOTO — not AI-generated",
  "base_image_path": "ProductionStudio/Assets/images/real_photos/muliaga_court_escort_REDACTED.jpg",
  "base_image_credit": "Joel Carrett/AAP PHOTOS, via Canberra Times (see Cases/rimoni-muliaga-jealousy-murder/PersonPhotos.md)",
  "style_tags": ["real-photo-base", "16:9", "eyes-redacted", "no watermark"]
}
```

**This case's thumbnail deliberately breaks from the studio's prior AI-generated-only thumbnail
pattern** (Kouri Richins "SHE WROTE THIS", Monica Sementilli "SHE WATCHED IT HAPPEN" — both 100%
fal.ai Flux generations), per the channel owner's explicit instruction this session: the
thumbnail must come from a real photograph, in line with the mandatory real-photo-sourcing rule
escalated 2026-07-26 to counter YouTube's "AI slop" enforcement policy.

**Build process:**
1. Base is the redacted AAP wire photo of Rimoni Muliaga being escorted by custody officers
   outside the Supreme Court of Victoria (see `PersonPhotos.md` for full sourcing chain and the
   mandatory eye redaction already applied).
2. Cropped/resized to 1280x720, graded (desaturated ~25%, contrast +15%, brightness -15%, subtle
   #A30E15 red-accent blend at 6% opacity to match brand color) and given a bottom-weighted dark
   vignette for text legibility — via `PIL`/`Pillow` (no external service).
3. Headline text overlaid in Impact (bold condensed caps, matches the visual weight of the
   brand's prior Bebas Neue/Oswald-style headlines — `C:/Windows/Fonts/impact.ttf`, the same
   family of look used in the previous two cases' thumbnails), white fill with black stroke,
   auto-sized to fit width, centered in the lower third.
4. Output: `ProductionStudio/Assets/images/rimoni-muliaga-jealousy-murder/thumbnail_with_text.png`
   (final) and `.../thumbnail.png` (graded base, no text, kept in case the text needs a redo).

**Rationale for "SHE NEVER CHEATED":** leads with the single most disturbing/ironic verified
fact — a man killed his wife for an affair that never existed — rather than a generic
"husband kills wife" framing. Matches the channel's brand rule of large dramatic imagery + max-3
-word high-impact text, and mirrors the Subject-Verb-Object hook pattern already validated by
"SHE WATCHED IT HAPPEN" without repeating it.

**Redaction note:** the black box over Muliaga's face is the mandatory eye/face redaction from
`PersonPhotos.md`, not a rendering error — reads visually as an intentional documentary-style
privacy redaction (consistent with true-crime-genre convention), not a bug.
