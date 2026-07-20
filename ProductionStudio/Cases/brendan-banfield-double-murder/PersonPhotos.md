# Person Photos — Brendan Banfield double murder (Track 1, mugshot_fetch_tool)

## Brendan Banfield — mugshot
- **source_url**: https://wjla.com/news/local/brendan-banfield-murder-trial-fairfax-county-virginia-timeline-affairs-fetish-site-fatal-plot-juliana-peres-magalhaes-au-pair-wife-christine-court-prosection-joseph-ryan-investigations-arrests-shootings-stabbings
- **image_url**: https://wjla.com/resources/media2/16x9/1200/800/0x23/80/f65bfb84-a69f-452d-8c1d-c8fd7334fe09-Untitleddesign52.jpg
- **source_type**: mugshot
- **issuing_authority**: Fairfax County Police Department (explicit caption attribution on the WJLA page: "Mugshot of Brendan Banfield (Fairfax County Police Department)")
- **retrieved_date**: 2026-07-20
- **license_note**: Qualifies under the 2026-07-20 exception to `Tools/mugshot_fetch_tool.md`'s Track 1 rule — WJLA explicitly attributes the photo to the issuing police department rather than claiming their own photographic credit, so this is treated as an official-source Track 1 photo republished by an outlet, not outlet-owned photography.
- **redaction**: eyes_blacked — applied via OpenCV Haar-cascade face detection (`haarcascade_frontalface_default.xml`) restricted to the detected face box, then eye detection (`haarcascade_eye.xml`) run only within the upper 60% of that face box to avoid false positives (nose/mouth regions were being misdetected as eyes when scanning the full image). Two eyes detected cleanly within the face ROI; black bar drawn spanning both with a 15% horizontal / 25% vertical margin.
- **local_path**: `ProductionStudio/Assets/images/real_photos/banfield_mugshot_REDACTED.jpg`
- **raw_unredacted_path**: `ProductionStudio/Assets/images/real_photos/banfield_mugshot_RAW_DO_NOT_USE.jpg` — kept only to verify redaction accuracy against the original; **never use this file in any output**.

## Stage 2 live-test result (2026-07-20)
First real end-to-end Track 1 pipeline run: source discovery → official-attribution verification
→ download → automated face/eye detection → redaction → save. Confirms the "not worth
automating at current volume, do it manually until Phase 2" note in `mugshot_fetch_tool.md` was
too pessimistic — OpenCV's bundled Haar cascades (no external model download, no GPU, ~1 second
runtime) make this cheap enough to automate now, in Phase 1, not just in a future Phase 2 build.
Updated the tool spec accordingly.
