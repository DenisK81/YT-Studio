```json
{
  "text_options": ["HE STAGED THE SEIZURE", "44 MINUTES TO DIE", "THE FIRE CHIEF LIED"],
  "chosen_primary": "HE STAGED THE SEIZURE",
  "base_image_source": "REAL PHOTO — Kevin West professional/staff photo (not an actual booking mugshot despite the source filename)",
  "base_image_path": "ProductionStudio/Assets/images/real_photos/west_mugshot_REDACTED_16x9.jpg",
  "base_image_credit": "republished by The Columbian (see Cases/kevin-west-staged-seizure-murder/PersonPhotos.md)",
  "style_tags": ["real-photo-base", "16:9", "eyes-redacted", "no watermark"]
}
```

**Real photo, continuing the studio's established practice** of building the thumbnail from a
real, redacted photo whenever a clean Track 1 photo is available. Used the already-built `_16x9`
derivative (451x254) rather than the raw portrait-cropped file, since that derivative was
specifically created to keep the redaction box centered and safely clear of any crop — see
`PersonPhotos.md`'s Ken-Burns verification note for scene 0031.

**Build process:**
1. Base is `west_mugshot_REDACTED_16x9.jpg`, upscaled to the standard 1280x720 thumbnail
   resolution (native aspect 1.776 vs target 1.778 — effectively a direct resize, no further
   cropping needed).
2. Graded (desaturated 30%, contrast +20%, brightness -20%, subtle #A30E15 red-accent blend at
   7%), bottom-weighted dark vignette for text legibility — identical recipe to every prior case
   this session (Buchanan, Thompson).
3. Headline in Impact, white fill + black stroke (8px), auto-sized to fit 92% of frame width,
   centered lower third.
4. Output: `ProductionStudio/Assets/images/kevin-west-staged-seizure-murder/thumbnail_with_text.png`
   (final) and `.../thumbnail.png` (graded base, no text).

**Rationale for "HE STAGED THE SEIZURE":** matches the established convention (see Thompson
case's "STAGED HER SUICIDE") of leading with the specific staged/faked mechanism rather than the
murder itself — every true-crime thumbnail on this channel implies a killing, so the hook has to
be the unusual detail: a 22-year fire battalion chief used his own professional knowledge of what
words trigger the fastest emergency response to fake a medical crisis. "44 MINUTES TO DIE" (the
gap between the 911 call and time of death) and "THE FIRE CHIEF LIED" were considered but held
back as Shorts hooks — both work as secondary reveals rather than the cold-open line.

**Redaction note:** the black box is the mandatory eyes-blacked redaction from `PersonPhotos.md`,
already verified against this exact video's Ken-Burns zoom range (100% box visibility, 36.4px
minimum clearance) since the `_16x9` derivative was purpose-built for that check before this
thumbnail was made — no further verification needed here.
