# Quality Control Agent

## Responsibility
Final gate before publishing. Aggregates every prior stage's status and produces
`Templates/Checklist.md`. Only a `pass` allows the Publishing Agent to proceed.

## Input
All prior outputs: Script.md, scene list, Voiceover.txt, ImagePrompts.md + generation report,
assembly report, Thumbnail.md, SEO.md.

## Checks
- Story consistency (does the twist/reveal follow from setup?)
- Timeline consistency (dates/order match verified facts)
- Fact consistency (any flagged/unknown claims still present in the final script?)
- Scene consistency (every scene has audio + image or an explicit missing-asset flag)
- Voice timing / subtitle timing (assembly report duration vs. planned)
- Missing assets
- Grammar / readability
- Export integrity (file exists, plays, correct format)
- **Real-photo attempt (added 2026-07-26, mandatory — see `Documentation/ARCHITECTURE.md`):**
  does this case have a `PersonPhotos.md` documenting a real attempt at both
  `Tools/mugshot_fetch_tool.md` tracks? A case with zero real photos and no documented access-
  wall reason is a `fail`, not a `warning` — this is the concrete evidence the video isn't
  YouTube's targeted "AI slop." Also confirm every real photo with an identifiable person has
  eyes-blacked/blurred redaction applied.
- **Synthetic-content disclosure reminder:** flag for Publishing Agent that YouTube Studio's
  "Altered or synthetic content" toggle needs a human decision at upload time for videos with
  realistic AI-generated scenes — this agent can't set it, just needs to make sure it isn't
  forgotten.
- The five brief questions: Would I stop scrolling? Would I click this? Would an American
  viewer care? Can the hook be stronger? Can retention be improved?
- **Redaction-under-zoom check (added 2026-07-28, mandatory — real published bug, see
  `Tools/mugshot_fetch_tool.md`'s "Manual fallback margin bug" note):** for every real photo
  scene, extract and visually check a frame at that scene's *maximum* Ken-Burns zoom level
  (both ends of the `interpolate()` range), not just the static source JPG. A redaction that
  looks complete at full-frame can still leak ear/jaw/eye at the video's actual crop. `fail` if
  any part of an eye is visible at any point in the rendered scene, not just at rest.
- **AI-generated-image artifact scan (added 2026-07-28, mandatory):** visually check every
  AI-generated scene image for anatomical/object hallucinations (extra limbs, duplicated
  tool handles, warped hands/faces) before render — a real published case had a courtroom gavel
  rendered with two crossed handles through one head, caught only after publish. Regenerate any
  flagged image with a more constrained prompt rather than accepting it.
- **Chapter-to-chapter loudness check (added 2026-07-28, mandatory):** run
  `ffmpeg -af loudnorm=print_format=summary` on every chapter mp3 before assembly; flag if
  Input Integrated loudness varies by more than ~2-3 LU across chapters (a real case measured a
  7 LU swing, audible as a volume jump at chapter boundaries) — normalize with `loudnorm`
  per-chapter before handing off to Remotion rather than trusting ElevenLabs' per-call
  consistency.
- **Real-photo bookending (added 2026-09-15, mandatory — see `Tools/remotion_assembly_tool.md`'s
  "Real-photo bookending" section):** does `real_photo_scenes` include the cold-open/earliest
  scene AND at least one scene in the back third, not just middle-of-video placements? `fail`
  if both bookends aren't present and no documented reason (e.g. genuinely no real material
  fits the closing beat) is given.
- **Track 3 real-attempt log (added 2026-09-15, mandatory):** does `Sources.md`/`PersonPhotos.md`
  show an actual documented search for a Track 3 archival clip, not just a bare "gap" line? A
  gap with no search log is a `fail`; a gap WITH a real documented attempt is an acceptable
  `pass`, per `Tools/remotion_assembly_tool.md`'s "Track 3 escalated to mandatory-attempt" note.
- **REAL badge wiring (added 2026-09-15, mandatory):** for every scene in `real_photo_scenes`,
  does the rendered output actually show the `RealBadgeComponent` overlay (spot-check at least
  one real-photo frame), and does no AI-generated scene incorrectly show it? `fail` on either a
  missing badge on a real scene or a false badge on a generated one.

- **Shorts narration-text leak check (added 2026-10-02, mandatory):** after
  `generate_shorts_audio.py`, scan every `<short>_timing.json` `captionWords` for `CHAPTER`,
  `scenes` or `===` tokens before rendering (`ProductionStudio/Assets/audio/<case>/shorts/`). A
  real defect: in range mode the script used to append the next chapter's header line to the last
  scene of a chapter, so the narrator read "chapter 03 scenes 0015-0021" aloud and the captions
  showed it. Williams Shorts 2-4 and the already-public Flynn Short 2 were affected; the script now
  strips `=== ... ===` lines. `fail` if any such token appears; regenerate, don't ship.

- **Image-matches-narration check (added 2026-10-05, mandatory, runs BEFORE any render):** during
  the artifact scan, read each AI image next to the exact sentence of its scene and `fail` any
  image whose main object differs from the one named - not only ones with garbled text. Real
  miss: a prompt for "stun guns" rendered as a handgun-like object and was waved through as
  "fine", then caught only after the 4-minute main video had been rendered (a ~15 min re-render).
  Firearms, knives and other weapons must never be swapped for a different weapon type in a
  scene that names one; when the generator keeps drifting, replace the concept with something
  neutral that the sentence also supports (e.g. the burner phones mentioned in the same line).
- **Shorts loudness check (added 2026-10-03, mandatory):** measure every rendered Short with
  `ffmpeg -af loudnorm=print_format=summary` and `fail` if Input Integrated is more than ~3 LU
  away from the main video (about -24 LUFS). A real case had a Short at -31 LUFS because
  `generate_shorts_audio.py` never normalized its narration (it now calls
  `normalize_chapter_loudness()`); earlier cases' Shorts measured as low as -29 LUFS. Fix a failing
  Short by normalizing its mp3 and re-rendering, not by boosting the render.

## Output
`Templates/Checklist.md`:
```json
{ "checklist_status": "pass | warning | fail",
  "issues": [ {"area":"", "severity":"warning|fail", "detail":""} ],
  "qc_questions": { "stop_scrolling": true, "would_click": true, "hook_can_improve": false, "retention_can_improve": false } }
```
**Stage 3 link note (added 2026-07-20):** field renamed from `status` to `checklist_status`
(was a real name mismatch — `Agents/publishing_agent.md`'s input has always expected
`checklist_status: "must be 'pass'"`, not `status`). This is the exact field Publishing Agent
gates on, so the two must match precisely, not just "close enough for a human to map."

## Escalate to human when
`checklist_status: fail` on anything — always. This agent never overrides its own fail into a
pass.

## System prompt (draft)
"""
You are the Quality Control Agent, the last gate before publishing. Review every input for
story/timeline/fact/scene consistency, timing, missing assets, grammar, and export integrity.
Ask: would I stop scrolling? Would I click this? Would an American true-crime viewer care? Can
the hook be stronger? Can retention be improved? If any check fails, set checklist_status to
"fail" and list the specific issue — never soften a fail into a warning. Output the JSON schema
exactly.
"""

- **Redaction zoom check (added 2026-10-10, Penney case):** before any render, open every redacted real photo at 2x on the eye region (not only the contact sheet). On the graduation photo the bar for one person had landed on the chest and left both eyes open; it was caught only in the post-render frame check and cost a 16-minute re-render of the main video and one Short. Multi-person photos need a bar per person, each verified on its own zoom.
- **Jurisdiction check on AI courtroom images (added 2026-10-10):** Flux repeatedly adds US flags and seals to generic courtrooms. For non-US cases (Canada, UK, Ireland, Australia) re-roll or replace the concept (microphone close-up, railing close-up) rather than accept a flag-bearing courtroom.

- **Positive-only image prompts for jurisdiction-sensitive scenes (added 2026-10-11, Corcoran case):** Flux schnell adds US flags and seals to any courtroom prompt that contains the words 'flag', 'emblem' or 'seal', even in a negation ('no flags' made them come back on four of five re-rolls). Describe only what should be in frame (rail edge, folder on a bench, glass on a rail, microphone close-up) and never name the unwanted object; the same applies to 'poster', 'sign' and 'plaque'.

- **Verify WHO is in a fetched image before using it (added 2026-10-13, Rudolph case):** when guessing a full-size URL from an outlet's thumbnail path, the file that comes back can belong to a different story (a neighbouring image on the same CDN returned an unrelated man in a Las Vegas courtroom). Always open the downloaded/fetched file and confirm the person, caption and credit match the case before it enters real_photos; take the URL from the article's own image element, not by editing a thumbnail path.
