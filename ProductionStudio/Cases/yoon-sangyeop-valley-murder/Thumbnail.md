```json
{
  "text_options": ["SHE LET HIM DROWN", "4 HOURS FROM $600,000", "HE KNEW SHE'D TRY AGAIN"],
  "chosen_primary": "SHE LET HIM DROWN",
  "base_image_source": "AI-generated (fal.ai Flux schnell) — scene 0028, two men's silhouettes on a cliff edge at dusk",
  "base_image_path": "ProductionStudio/Assets/images/yoon-sangyeop-valley-murder/0028.png",
  "base_image_credit": "n/a — no real Track 1 person photo exists for this case (see PersonPhotos.md), AI-generated base used instead",
  "style_tags": ["ai-generated-base", "16:9", "silhouette-only", "no watermark"]
}
```

**First thumbnail this session NOT built from a real person photo — a real, documented gap, not
an oversight.** Every prior case's thumbnail used a real, redacted defendant photo as the base,
per the studio's established practice. This case has none available: South Korea's identity-
disclosure system (신상공개) was never formally invoked for Lee Eun-hae, Cho Hyun-soo, or the
third accomplice — see `PersonPhotos.md` for the full explanation. Using one of the leaked/
unofficial photos that circulated online (netizen "investigation" images, a since-deleted
Instagram) would violate this channel's own official-source-only redaction policy, the same
policy this gap exists to protect. Not a shortcut taken — a wall documented and worked around
honestly.

**Base image chosen instead:** scene 0028 from `ImagePrompts.md` — two silhouetted men on a
cliff edge at dusk, directly depicting the moment right before the fatal dive (Cho and Yoon
climbing the rock to jump, per the script's own scene 0028-0030). This keeps the thumbnail
grounded in the case's real, verified events rather than reaching for a generic stock image —
the composition IS the actual story beat, just not a real photograph of it. The mandatory
real-photo requirement for the video as a whole is still satisfied by the two real Track 2
location photos used elsewhere (`0041`, `0042` — Incheon court area, Supreme Court of Korea).

**Build process (same recipe as every prior case this session):**
1. Base is `0028.png` (1024x576), upscaled to the standard 1280x720 thumbnail resolution.
2. Graded (desaturated 30%, contrast +20%, brightness -20%, subtle #A30E15 red-accent blend at
   7%), bottom-weighted dark vignette for text legibility.
3. Headline in Impact, white fill + black stroke (8px), auto-sized to fit 92% of frame width,
   centered lower third.
4. Output: `ProductionStudio/Assets/images/yoon-sangyeop-valley-murder/thumbnail_with_text.png`
   (final) and `.../thumbnail.png` (graded base, no text).

**Rationale for "SHE LET HIM DROWN":** leads with the specific, legally unusual mechanism of the
conviction — not a physical assault, but a deliberate choice not to save him while he drowned in
front of her — which is the single most surprising, click-worthy fact of the whole case and
matches this channel's established convention (Kevin West: "HE STAGED THE SEIZURE"; Thompson:
"STAGED HER SUICIDE") of leading with the unusual mechanism rather than a generic "murder"
framing. "4 HOURS FROM $600,000" (the insurance-timing detail) and "HE KNEW SHE'D TRY AGAIN"
(referencing the two earlier attempts) were considered and held back as Shorts hooks instead —
both work as strong secondary reveals rather than the cold-open line.

**No redaction needed:** both figures are fully AI-generated silhouettes with no identifiable
facial features — this is the one case this session where the thumbnail itself required no
eyes-blacked redaction step, since there is no real face in the base image at all.
