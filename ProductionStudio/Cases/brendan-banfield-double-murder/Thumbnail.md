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
- **Update (2026-07-20): a real, redacted photo now exists for this case.** Found an
  officially-attributed mugshot ("Fairfax County Police Department") republished by WJLA,
  downloaded and automatically redacted (eyes blacked via OpenCV face/eye detection) — see
  `Cases/brendan-banfield-double-murder/PersonPhotos.md`. Bypassed the Fairfax FOIA-only
  constraint entirely for this case via the outlet-attribution exception added to
  `Tools/mugshot_fetch_tool.md` the same day. **The thumbnail image prompt above is now stale**
  — it should be replaced with the real redacted photo
  (`Assets/images/real_photos/banfield_mugshot_REDACTED.jpg`) composited into the brand's
  dark-background / police-light thumbnail style, rather than an AI-generated generic face, for
  the CTR benefit real-face thumbnails have in this genre. Not yet re-composited — flagging as
  the next actual production step, not a blocked one.
