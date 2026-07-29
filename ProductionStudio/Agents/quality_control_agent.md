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
