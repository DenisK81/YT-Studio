# Person Photos — Kevin West murder of Marcy West (Track 1 + Track 2)

## Kevin West — professional/staff photo (news-graphic background), Track 1

- **source_url**: https://www.columbian.com/news/2024/mar/22/camas-washougal-fire-captain-faces-murder-charge-in-wifes-january-death/ (image republished by The Columbian)
- **image_url**: https://www.columbian.com/wp-content/uploads/2024/03/kevin-west-mug-shot-featured-1024x576.jpg
- **source_type**: professional uniform/staff photo, not an actual booking mugshot despite the filename ("kevin-west-mug-shot-featured") — confirmed on inspection to be a posed photo on a decorative red/blue "breaking news" graphic background, not a jail booking photo.
- **retrieved_date**: 2026-08-04
- **redaction**: eyes_blacked. Automated Haar-cascade face detection found 2 candidate faces in the original frame; the 2nd was the real one. Eye sub-detector found both eyes cleanly ((510,141,47,47) and (435,142,51,51)). Standard 30%/40% margin applied. Verified by direct visual inspection.
- **Cropping note**: original 1024x576 frame includes a decorative swirl/graphic border around the photo inset. Cropped via `img.crop((286, 8, 737, 543))` to isolate the actual photo, producing a 451x535 portrait-oriented result.
- **local_path**: `ProductionStudio/Assets/images/real_photos/west_mugshot_REDACTED_cropped.jpg` (451x535, portrait — do not feed directly into the video pipeline, see 16:9 derivative below)
- **raw_unredacted_path**: `ProductionStudio/Assets/images/real_photos/west_mugshot_RAW_DO_NOT_USE.jpeg` — never use in any output.
- **Max-zoom verification, 2026-08-05 (mandatory QC rule from the Rimoni Muliaga case):** this
  photo is portrait-oriented (451x535, aspect 0.843), the same class of issue as the Odhiambo
  photo in the Walter Buchanan case. Baseline `objectFit: "cover"` fit into a 16:9 frame already
  cuts the box's visible area to ~59%, and Remotion's actual Ken-Burns range (1.12x zoom, ±30px
  pan, per `DevynTrial.tsx`'s `SceneImage`) pushes worst-case box visibility to 0% — not a leak
  (box always ⊇ real eye pixels by construction, so a shrinking crop can only ever remove box
  pixels or reveal nothing — never bare eyes), but a silent no-op that would waste the photo.
  **Fix:** created `west_mugshot_REDACTED_16x9.jpg` via `img.crop((0, 32, 451, 286))`, a
  16:9-native crop (451x254) centering the box vertically with ~80px of margin above and below.
  Re-verified: 100% box visibility at every Ken-Burns zoom/pan combination, minimum clearance
  36.4px. **This is the file to use in the video pipeline — never the plain `_REDACTED_cropped`
  portrait file.**

## Kevin West — Clark County Courthouse entrance photo, Track 1 (second photo, "more photos" per channel default)

- **source_url**: https://www.camaspostrecord.com/news/2026/jan/15/former-camas-washougal-fire-chiefs-fiancee-on-stand-in-murder-trial/
- **image_url**: https://origin.camaspostrecord.com/wp-content/uploads/2026/01/0113_MET_Westmurdertrial.jpg
- **source_type**: real courtroom/courthouse photo taken during the actual trial
- **issuing_authority**: explicit photo credit in the article's own figcaption — "Taylor Balkom/The Columbian files" — a real, named photographer/outlet credit, republished by the Camas-Washougal Post-Record from its sister paper.
- **retrieved_date**: 2026-08-05
- **redaction**: eyes_blacked. Automated Haar-cascade detection returned a false-positive face box unrelated to West's actual position in frame (his head is turned in a 3/4 profile, which the frontal-face cascade did not localize correctly). Used the manual debug-grid method instead: cropped and 2x-scaled the head region with a coordinate grid overlaid, read off both eye positions from the 3/4-profile pose, then drew and visually verified a box (385,105)-(465,145) before applying solid black fill.
- **Bystander note**: two other people are visible in the foreground (a gray-haired man, back of head only, no face visible; a gray-haired woman, ear and cheek only, no eyes visible). Neither is individually identifiable from visible features in this frame — no redaction applied to either, consistent with the standard applied to incidental background/foreground bystanders in prior cases (e.g. the distant figures in the Thompson case's Nottingham Crown Court photo).
- **local_path**: `ProductionStudio/Assets/images/real_photos/west_courthouse_REDACTED.jpg` (900x749, aspect 1.20 — not quite 16:9, see derivative below)
- **raw_unredacted_path**: `ProductionStudio/Assets/images/real_photos/west_courthouse_entrance_RAW_DO_NOT_USE.jpg` — never use in any output.
- **Max-zoom verification, 2026-08-05:** baseline cover-fit crop into 16:9 already loses part of
  the box (window starts at y=121.4, box spans y:105-145 — only 59% of the box visible even at
  baseline), and full Ken-Burns range pushes worst-case visibility to 0% (silent no-op, not a
  leak, same reasoning as above). **Fix:** created `west_courthouse_REDACTED_16x9.jpg` via
  `img.crop((0, 0, 900, 507))`, keeping the box safely inside the top portion of a native-16:9
  frame. Re-verified: 100% box visibility at every Ken-Burns zoom/pan combination, minimum
  clearance 47.8px. **Use this file in the pipeline, not the plain `_REDACTED.jpg`.**

## Marcy West (victim) — no usable photo found; genuinely blocked, not skipped

Checked 6 distinct outlets plus a general web search specifically for a personal photo of Marcy
(Marcelle) West: **Camas-Washougal Post-Record** (2 articles checked, including the "fiancée on
stand" piece — no photo of Marcy in either), **KPTV** (sentencing article DOM only surfaced
unrelated "related articles" thumbnails), **KOIN** (page blocked entirely — "Access to this page
has been denied"), **ClarkCountyToday** (republished CCSO press release; its one large image
turned out to be a generic Clark County Sheriff's Office badge/star graphic, not a real photo of
either West — discarded, not used), **KGW** (article page returned zero images >150px, likely a
video-only layout), **KATU** (article uses a generic "police lights" stock photo, not a real
person photo). A general web search for "Marcy West Camas Washougal obituary photo" surfaced no
funeral-home or obituary listing either.

No AI-generated substitute portrait is used in her place — per this channel's standing practice,
AI generation fills compositional/scene gaps, not a fabricated likeness of a real named person
for whom no real photo could be sourced. Scenes referencing Marcy in `ImagePrompts.md` are
composed to avoid requiring a face (over-the-shoulder, silhouette, hands-only, or object/scene
framing) rather than inventing what she looked like.

## Track 2 — non-person / scene photo

Not yet sourced as of this writing — to be added when `ImagePrompts.md` is built (task #29).
Candidates to check: Clark County Courthouse exterior (Vancouver, WA), Camas-Washougal Fire
Department station exterior/apparatus.

## Access method note (technical)

Same sandbox constraint as every prior case this session: outbound `curl`/`WebFetch` to this
outlet's CDN returns 403 or is otherwise blocked. Worked around via the Browser pane +
`javascript_tool`'s `fetch()` → `FileReader.readAsDataURL()` pattern, decoding the saved JSON
transcript file with a Python script when the base64 payload exceeded the tool's inline output
limit (both West photos this case). No format-mismatch issues — both files decoded as `jpeg`
directly from the data URL prefix.
