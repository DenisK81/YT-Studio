# Tool: image_gen_tool

## Purpose
Provider-agnostic image generation wrapper, per Image Policy: the pipeline must never depend
on a single image source. Default provider is set below for the test phase (Phase 1, first 10
videos) — chosen for cost, not locked in permanently.

**Role clarified 2026-08-30 (channel-owner instruction, after a real channel audit):** AI
generation is the **gap-filler**, not the default. Sourcing priority for every scene is real
archival video clip (`Tools/mugshot_fetch_tool.md` Track 3) → real photo (Track 1/2) → AI
generation only when nothing real exists for that specific scene. Before writing a scene's
prompt for this tool, check whether a real clip or photo could cover it instead — don't default
to generation just because it's fast. This doesn't relax the mandatory-redaction or
trigger-surface-avoidance rules below; it just changes how many scenes should reach this tool
at all.

## Interface
```
generate(prompt: string, style_tags: string[]) -> {
  image_url_or_file
}
```

## Default provider: fal.ai + Flux

Chosen for the test phase because it has a real API (unlike Midjourney, which is Discord-only
with no official API) and is effectively free at this volume:

- **Model**: `flux/schnell` for most scenes (fast, cheap, commercially licensed open weights).
  Reserve a pricier model (`flux-pro` or similar) only for the thumbnail / hero shots if
  `flux/schnell` quality isn't good enough there — see `Agents/thumbnail_agent.md`.
- **Cost**: ~$0.003-0.01 per image on `schnell`. At 80-100 images/video, that's roughly
  $0.25-1.00 per video — a new fal.ai account starts with $20 free credit, which covers the
  entire 10-video test phase with room to spare.
- **Auth**: `FAL_KEY` (or equivalent per current fal.ai docs) in `Config/.env.example` /
  n8n credential store. Never commit the real key.
- **Endpoint shape**: verified live 2026-07-19 (Stage 2 test, see below) — matches current docs.

## Stage 2 live-test result (2026-07-19)
Real call against the Banfield case, scene 0001 from `ImagePrompts.md`:
- **Endpoint**: `POST https://fal.run/fal-ai/flux/schnell`, header `Authorization: Key $FAL_KEY`.
- **Request body confirmed**: `{ prompt, image_size, num_images, output_format }` — used
  `image_size: "landscape_16_9"` for the fixed 16:9 style rule; produced a 1024x576 image
  (correct 16:9 ratio).
- **Response shape confirmed**: `{ images: [{url, width, height, content_type}], prompt, seed,
  has_nsfw_concepts, timings }` — matches current fal.ai docs exactly.
- **Cost/latency**: inference time ~0.11s per the response `timings` field; well within the
  ~$0.003–0.01/image estimate above.
- **⚠ "no text" style rule is not reliably honored by the model**: the generated image (two
  police cruisers outside a house) rendered a legible "POLICE" decal on one vehicle despite
  `no text` being in the prompt. This is a known limitation of diffusion models with text in
  the scene concept (police cars, signage, badges) — the prompt constraint reduces but doesn't
  eliminate it. **Quality Control Agent needs to actually visually check for stray
  text/logos/watermark-like artifacts per image, not just trust that "no text" in the prompt
  was sufficient.** Worth a note in `Agents/quality_control_agent.md` if this keeps recurring
  across scenes.

## Confirmed pattern (2026-07-30, Walter Buchanan case): monumental architecture resists text
suppression entirely via prompting
Flux schnell's text-hallucination tendency (noted above) turned out to have a specific,
reliably-reproducing trigger: any grand civic/monumental stone facade with a pediment or
inscription-bearing surface (courthouse fronts, column bases). On this case's Edinburgh
courthouse establishing shot, three consecutive prompt rewrites — each adding stronger negative
constraints ("no carvings, no engravings, no inscriptions, no signage, no building name, no
decorative crest") — all still produced legible gibberish lettering baked into the stonework
(`COUTT`, `GOVERRIANT`, `Ganelrrell`). **Negative prompting alone does not reliably fix this
class of image on this model.** The only fix that worked was changing the composition to avoid
the trigger surface entirely (switched to a wood-paneled courtroom interior with no exterior
stonework). If a future scene needs an exterior monumental-building shot, budget for this and
plan a non-facade alternative composition up front rather than iterating on the same shot.

## Confirmed pattern (2026-08-01, Michael Thompson case): the text-hallucination limitation
extends to small branded electronics, not just monumental architecture

The 2026-07-30 finding above (courthouse facades resist text suppression) generalizes further:
Flux schnell also reliably invents fake brand names/model numbers/display text on small
consumer electronics — voice recorders, radios, rotary phones — even when the prompt explicitly
says the surface is blank. On this case, a voice-recorder prompt with "no legible text or labels
on the device" still rendered a small embossed brand-and-model mark on the casing; the negative
constraint was strengthened twice and failed twice more. The reliable fix was the same one that
worked for architecture: **change the composition to remove the text-prone surface from frame
entirely**, not add more negative words to the same shot. Concretely: an extreme close-up
cropping to *only* the recorder's glowing display (with the branded casing edge out of frame)
came back clean on the first try; a radio scene was abandoned entirely in favor of an abstract
underwater-ripple composition after three straight failures. **General rule going forward:**
if a prompt describes a manufactured object with a face/panel/nameplate (electronics, signage,
vehicles, packaging) and a first-pass generation shows any hint of invented text, don't iterate
on that composition — reframe to exclude the branded surface, or replace the object with a
different symbol entirely.

## Confirmed pattern (2026-08-13, James Rummell case): police tape close-ups reliably hallucinate text

Same underlying limitation, a third confirmed trigger surface: close-up shots of yellow
police/crime-scene tape. Two independent scenes in this case — a wide establishing shot with
tape across a yard, and a dedicated extreme-close-up of a taped doorway — both produced legible
garbled lettering baked into the tape print (`POLICE DO NOOT COO`, `POLIICE CRIESE CRASS`) despite
"no text" in the prompt each time. The first scene was fixed by removing the tape from frame
entirely (kept the red/blue light bars, dropped the tape). The second scene needed two attempts:
softening to "completely out of focus, abstracted into a blur" still rendered readable garbled
text on the re-generation, and only a full composition pivot (dropped the tape object entirely,
replaced with a cracked window pane) came back clean. **Add police/crime-scene tape to the
known trigger-surface list** (alongside monumental architecture and small branded electronics) —
don't budget on negative-prompting or blur language fixing it; plan a tape-free alternative
composition (light bars, chalk outline, doorway ajar, etc.) for any "crime scene" beat up front.

## Confirmed pattern (2026-08-15, Yolanda Marodi case): roadside/motel signage and calendar
date grids both reliably hallucinate text

Two more confirmed trigger surfaces, same underlying limitation. **Roadside motel/hotel
signage**: three consecutive attempts on a border-town motel exterior scene all produced
legible-looking but wrong text — a spelled-correctly-but-unwanted "HOTEL" on the first try, then
garbled "MOTEL Realistins" / "MOTT COTE" / "TL" on two follow-ups that only tightened the
camera framing (removing sky/roofline) rather than changing the underlying subject — the model
kept re-inventing a sign even when the prompt explicitly said "no sign, no pole, no lettering
anywhere." **Tightening framing on the same subject did not work; only dropping the subject
itself did** — the fix that finally landed was pivoting away from the building exterior
entirely, to a close-up of a hotel room key tag on a nightstand (same scene-beat, unrelated
composition, zero signage-bearing surfaces in frame). **Calendar/date-grid close-ups**: a
"desk calendar with a date circled" prompt produced a fully rendered grid with a misspelled day
abbreviation ("SET" instead of "SAT") and numbers scattered out of real calendar order. Fix:
same pivot pattern — extreme close-up on just the red circle marker with everything else
thrown hard out of focus, avoiding a legible grid surface at all (a residual duplicated digit,
"1010" instead of a clean date, is the acceptable trade-off — it reads as an odd number, not as
broken/garbled AI slop). **Add both to the known trigger-surface list** (alongside monumental
architecture, small branded electronics, and police/crime-scene tape) — for any scene concept
that inherently implies a sign or a numbered grid (motels, storefronts, calendars, scoreboards,
clocks with numerals), assume the first draft will hallucinate on it and budget for a full
composition pivot away from the signage-bearing object, not just a tighter crop of the same one.

## Confirmed pattern (2026-08-16, Jamie/Nicholas Orsini case): retail storefront signage joins
the motel-sign pattern; printed photos/flyers of unnamed people reliably fabricate sharp,
specific-looking faces

**Retail storefront signage**: a "big-box home-improvement store parking lot" scene went through
three regeneration rounds before passing. First attempt: "The HOSTSUSH Imponment Burret" garbled
on a Walmart/Home-Depot-style facade. Second attempt (same subject, just removing the storefront
from the described foreground and pushing it to a blurred background per the motel-case playbook):
still produced legible "Bitet Ners" — the model re-added a sign even to a facade the prompt never
asked it to render. **Only the third attempt, which removed every trace of a building from the
frame entirely** (a low-angle close-up on the car's own taillights, sky and pavement only) came
back clean. A companion scene — a car's open trunk with a store facade blurred in the
background — followed the identical arc: legible "HOME IMPROVEMENT" on attempt one, a legible
"NETTIA" pole sign on attempt two (blurring the *foreground* subject wasn't enough, since the
background building was still the same rendered subject), clean only once the shot was
tightened to an extreme close-up on the trunk interior with just a sliver of sky at the frame
edge. **Confirms the motel-case lesson generalizes to any commercial-storefront subject, not
just motels** — and sharpens it further: even "same building, less sky in frame" is not a
composition pivot, it's still the same generative subject. The pivot has to remove the
sign-bearing structure from the described scene entirely.

**Printed photos/flyers of an unnamed person's face**: a "missing person flyer on a community
board" scene, prompted explicitly for "the photo and text deliberately blurred and illegible,"
came back with a fully sharp, prominent, specific-looking fabricated face plus garbled
pseudo-text body copy — twice, on two different compositions (a single flyer, then a stack of
overlapping flyers). This is a distinct risk from the text-hallucination pattern above: the
model was not asked to depict any specific real person, but a "photo of a person on a printed
document" concept reliably renders a sharp, detailed, memorable-looking face regardless of blur
instructions — which risks being misread as a depiction of an actual named subject in the case
(here, risk of being mistaken for Jamie Orsini, whose likeness this channel deliberately never
fabricates, see `Cases/orsini-beacon-murder/PersonPhotos.md`). Same root issue showed up in a
"smartphone displaying a photo" scene the same case — a "blurred, illegible photo held in a
hand" prompt rendered a sharp, clearly composed face on the screen. **Fix is a full concept
swap, not a blur/composition tweak** — for the flyer scene, dropped the person-photo concept
entirely in favor of a stack of dusty case files (same "cold case" narrative beat, zero human
faces in the composition); for the phone-screen scene, reframed so the screen's own glare/angle
hides the display from camera rather than asking the model to render-then-blur a face. **Add
"any prompt describing a photo/portrait of a person on a printed or displayed surface" to the
known trigger-surface list** — treat it as a face-fabrication risk on top of the existing
text-hallucination risk, and default straight to a no-photo, no-face alternative composition
rather than trying a blur instruction first.

## Confirmed pattern (2026-08-22, Lawrence Goodine case): "blank/blurred" instruction alone is
not reliable — the text-bearing surface itself has to leave the frame

A "close-up of a folded legal document, blank and blurred so no text is legible" scene came back
with a sharp, prominent, garbled fake headline ("EATWEUATE") across the top of the page — despite
the prompt explicitly asking for blank/blurred/illegible. This is a step further than the
Orsini-case lesson above: it's not that blur wasn't attempted, it's that the model still treated
"legal document" as a subject worth rendering a headline for, and the blur instruction lost to
that pull. **Confirms the instruction-based mitigation ("blurred", "illegible", "no text") is not
reliable on its own for any prompt whose subject is fundamentally "a page/document/sign with
text on it"** — same underlying failure as the storefront-signage lesson, just on paper instead
of a building facade. Fix: reframed the shot to an extreme close-up on the document's folded
edge and paper stack, with the flat top surface (the only place text could render) cropped
**entirely out of frame** by the composition itself, not just blurred within frame. Regenerated
clean on the first attempt with the new composition. **Rule of thumb going forward: for any
prompt involving paper, signage, screens, or printed text, prefer describing a composition where
the text-bearing surface is structurally out of frame (edge-on, cropped, angled away, or replaced
by a non-text object) over relying on "blurred so no text is legible" language** — the latter has
now failed at least once even when explicitly requested.

## Fallback / secondary providers (keep the interface provider-agnostic)
- Leonardo.ai API — separate pay-as-you-go balance (starts with its own free credit), useful
  as a second source if fal.ai has an outage or a specific model isn't available there.
- Replicate — same Flux models, per-second/per-image billing, good drop-in alternative.
- Midjourney — deliberately NOT used for automation: no official API, Discord-only, would
  require unofficial workarounds. Fine for one-off manual generation in Phase 1 if someone
  wants to hand-pick a specific image, but never wire it into this tool's automated path.
- **fal.ai's `fal-ai/nano-banana` (Gemini 2.5 Flash Image)** — same-prompt comparison run
  2026-07-19 on scene 0001: honored "no text" better than Flux schnell and produced a more
  detailed/textured result, but (a) its response omits `width`/`height` (`null` in the JSON,
  unlike Flux's clean shape — would need a follow-up call or local image inspection to get
  dimensions if wired in), (b) adds an extra `description` text field not present in Flux's
  response, and (c) costs ~$0.039/image vs Flux's ~$0.003–0.01 — roughly 4–13x more, which at
  80-100 images/video would blow past the "near-free at test volume" budget this default was
  chosen for. **Decision (2026-07-19): keep Flux schnell as the default for all scenes** — not
  worth the cost multiplier for the whole batch. Revisit as a possible hero-shot/thumbnail-only
  override later if quality on those specific shots matters enough to justify the per-image
  cost (mirrors the existing flux-pro-for-hero-shots idea above).

## Stage 4 live-test result (2026-07-20/21) — confirmed working through n8n, not just direct Python
Ran the exact same request contract through a real local n8n instance (`npx n8n`, no Docker) as
an HTTP Request node — see `Tests/stage4_n8n_local_bootstrap.md` for the full setup/friction
notes. Result: `executionStatus: "success"`, real image returned (1024x576, correct 16:9),
identical shape to the direct-Python Stage 2 test above. **This is the first node of
`Workflows/n8n_master_workflow.skeleton.json` (`image_generation_loop`) confirmed as a working
HTTP Request configuration, not just a placeholder node type.**

## Implementation notes
- 80-100 images per video (per the channel's current plan) means this tool will be called in
  batch — build with basic rate-limit/backoff handling from day one, not as an afterthought.
- Never block the pipeline on one failed generation (see Image Generation Agent) — this tool
  should return a clear failure reason (`content_policy`, `timeout`, `rate_limit`, `other`) so
  the calling agent can decide whether to retry.
- Track spend against the free credit (fal.ai dashboard) during the test phase so there's no
  surprise bill — Tool Manager Agent can log cumulative spend per video in a future iteration.
