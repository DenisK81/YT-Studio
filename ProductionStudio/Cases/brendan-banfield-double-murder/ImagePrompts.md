# Image Prompts — Brendan Banfield double murder (Christine Banfield & Joseph Ryan)

Style (fixed for all scenes unless noted): photorealistic, cinematic, 35mm, ultra realistic,
16:9, no text, no watermark, Netflix true-crime documentary look.

| scene_id | beat | prompt | notes |
|---|---|---|---|
| 0001 | hook | Wide nighttime establishing shot of a suburban house in Virginia, red and blue police lights reflecting off the front of the home, a police cruiser parked in the driveway, dark and tense atmosphere. | Police-light motif used here as the crime-scene establishing shot — the one deliberate exception before it's reserved for evidence/investigation beats below. |
| 0002 | hook | A man in his 40s wearing a dark jacket standing in a driveway at night, silhouetted against flashing police lights in the background, arms crossed, looking away from the house. | Generic figure, no named likeness — reenactment silhouette only. |
| 0003 | conflict | Interior of a suburban home hallway at night, evidence markers on the floor, a detective's flashlight beam cutting through the dark, no visible faces. | |
| 0004 | conflict | Close-up of a broken window frame with forced-entry damage, splintered wood, glass fragments on a windowsill, dim interior lighting. | Staged break-in detail. |
| 0005 | conflict | A man in his 40s in business-casual attire sitting alone at a kitchen table, hands clasped, dim lighting, pensive expression. | Generic reenactment figure. |
| 0006 | mystery | A generic federal law-enforcement identification badge and lanyard resting on a desk beside a stack of case files, dim office lighting, close-up. | Avoids depicting an actual IRS badge/seal — kept generic. |
| 0007 | mystery | A detective's desk covered with case photos and a corkboard with string connecting notes, dim lamp light, moody investigation-room atmosphere. | |
| 0008 | escalation | Close-up of a smartphone screen showing an anonymous messaging app conversation, blurred/illegible text, dim ambient lighting. | No readable text, per "no text" style rule. |
| 0009 | escalation | A man in his late 30s driving a car at night, city lights blurred through the windshield, focused expression. | Generic figure representing Ryan — no named likeness. |
| 0010 | evidence | A laptop screen on a desk showing a generic login page, gloved hands nearby, red and blue police lights faintly visible through a window. | Police-light motif reintroduced here — evidence beat. |
| 0011 | evidence | A young woman in her mid-20s standing alone in a dimly lit bedroom, looking out a window, pensive expression, no identifiable features. | Generic figure representing the au pair — no named likeness. |
| 0012 | evidence | Split composition: a smartphone screen with a generic silhouette profile photo on one side, a shadowy figure typing on a keyboard on the other, dim lighting. | |
| 0013 | twist | Yellow crime-scene tape stretched across a suburban doorway at night, red and blue police lights reflecting on the tape, dramatic close-up. | Police-light/tape motif — twist beat, appropriate use. |
| 0014 | twist | Two silhouetted figures standing close together in a dark room, backlit by a single window, tense body language, no visible faces. | |
| 0015 | investigation | Interior of an empty courtroom, jury box, wood paneling, soft overhead lighting, no visible individuals. | |
| 0016 | investigation | A prosecutor's table with case binders and photographs stacked neatly, courtroom in soft focus behind. | |
| 0017 | reveal | A courtroom gallery filled with blurred, out-of-focus spectators, a judge's bench in soft focus in the background, tense atmosphere. | |
| 0018 | reveal | Close-up of a gavel resting on a wooden courtroom bench, dim overhead lighting, dramatic shallow depth of field. | |
| 0019 | aftermath | Exterior of a state prison at dusk, high fences with barbed wire, overcast sky, wide shot. | |
| 0020 | aftermath | An empty suburban house at dusk with a "For Sale" sign in the front yard, quiet street, somber atmosphere. | |
| 0021 | question | Wide symmetrical shot of a quiet suburban street at night, a single porch light glowing in the distance, contemplative closing atmosphere. | |

(21 rows — matches the scene_id list from `SceneList.json` exactly.)

## Image Planning Agent notes (Stage 1 isolated test, 2026-07-19)
- All 21 prompts written; none name or physically describe a real, identifiable living person —
  every human figure is generic ("a man in his 40s", "a young woman in her mid-20s", silhouettes)
  per the agent's rule. No escalation triggered.
- Police-light / crime-tape motif deliberately limited to 4 of 21 scenes (0001 as the crime-scene
  establishing shot, 0010/0013 as evidence/twist beats, plus the badge close-up at 0006 stays
  generic rather than using the motif) — respects "reserved for evidence/investigation beats,
  not every scene."
- All prompts carry the fixed base style tags: `photorealistic, cinematic, 35mm, 16:9, no text,
  no watermark`.
