# Thumbnail — Brendan Banfield double murder (Christine Banfield & Joseph Ryan)

## Text options (max 3 words each)
1. HE BECAME HER
2. MURDER BY CATFISH
3. THE FAKE WIFE

## Image prompt
Close-up of a man's face partially in shadow, dark background, red and blue police lights
reflecting off his skin, yellow crime-scene tape blurred in the foreground, intense expression,
photorealistic, cinematic, 16:9, no watermark.

## Brand constants (do not change per-video)
Colors: bg #111111 · text #FFFFFF · accent #A30E15 · gray #4D4D4D · light gray #BDBDBD
Fonts: headline Bebas Neue / Oswald Bold · body Montserrat

## Thumbnail Agent notes (Stage 1 isolated test, 2026-07-19)
- Input used: `case_summary` = "A husband catfishes a stranger using his wife's identity on a
  fetish site, then kills them both to fake a home invasion." / `twist` = "He and his mistress
  built a fake version of his wife online to lure an innocent man to his death."
- Image prompt deliberately kept to a **generic** man's face (per `Agents/image_planning_agent.md`'s
  no-real-likeness rule) rather than Brendan Banfield's actual likeness — no escalation fires
  under the strict rule ("requires depicting a real identifiable person's face") because we
  didn't attempt to depict him specifically.
- **Real limitation worth flagging (not a formal escalation, but a CTR concern):** the brand's
  "large face" thumbnail composition is designed around true-crime convention, where channels
  typically use the actual perpetrator's mugshot for recognition/CTR. That's currently
  unavailable here — `Tools/mugshot_fetch_tool.md` is blocked pending legal review (see its
  Stage 2 note). So this thumbnail is generic-face-only for now, which may underperform a
  real-photo thumbnail. Worth revisiting once the mugshot legal question is resolved.
