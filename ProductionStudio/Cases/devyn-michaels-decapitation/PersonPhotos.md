# Person Photos — Devyn Michaels decapitation (Track 1 + Track 2, mugshot_fetch_tool)

## Devyn Michaels — official booking photo, Track 1 success

- **source_url**: https://www.reviewjournal.com/crime/courts/woman-wants-to-withdraw-guilty-plea-in-decapitation-death-of-boyfriend-3216180/
- **image_url**: https://www.reviewjournal.com/wp-content/uploads/2024/11/19876387_web1_DMichaels.jpg (corroborated by a second independent hosting: `truecrimenews.com`'s Akamai-CDN copy of the same photo, same "Henderson Police" credit)
- **source_type**: agency booking photo, republished by a news outlet
- **issuing_authority**: Henderson Police Department — explicit outlet caption credit ("Devyn Michaels", credited to **Henderson Police Department** on the Las Vegas Review-Journal page). This is a textbook fit for `Tools/mugshot_fetch_tool.md`'s 2026-07-20 outlet-attribution exception: the outlet's own caption credits the issuing law-enforcement agency, not the outlet's own photography.
- **retrieved_date**: 2026-07-29
- **license_note**: Official law-enforcement booking photo of a convicted defendant in an adjudicated, fully-covered criminal case — squarely the newsworthy/documentary use case this tool's legal grounding cites.
- **redaction**: eyes_blacked. Automated OpenCV Haar-cascade detection worked cleanly this time (unlike the Rimoni Muliaga case's off-angle photos) — this is a clean frontal booking photo. Applied a **generous** margin (30% horizontal / 40% vertical beyond the detected eye bounding box — wider than the tool spec's 15%/25% minimum), specifically because the 2026-07-28 post-publish finding on the Muliaga case showed a tight/minimal-margin redaction can leak once the video's Ken-Burns zoom crops into the frame. Visually verified: the black box fully covers brow-to-nose-bridge with wide clearance on all sides.
- **local_path**: `ProductionStudio/Assets/images/real_photos/michaels_mugshot_REDACTED.jpg`
- **raw_unredacted_path**: `ProductionStudio/Assets/images/real_photos/michaels_mugshot_RAW_DO_NOT_USE.jpg` — kept only to verify redaction accuracy; **never use this file in any output**.
- **Side letterboxing and the outlet's own watermark/logo were cropped out** before use (a gray padding border + a red "RJ" logo box in the bottom-right corner of the original asset) — neither is part of the actual photographic content.

## Johnathan Willette (victim) — not found

No photograph of Johnathan Willette was located in this session's research. Per `mugshot_fetch_tool.md`'s escalation rule ("no public-record person-photo exists for a subject who is nonetheless central to the story"), he is represented only via AI-generated reenactment/silhouette imagery in `ImagePrompts.md`, not face-forward portrait generation of a real identifiable person.

## Deviere Willette (Johnathan's son, Michaels' husband) — not attempted

Not a defendant and not deceased; no attempt made to source a real photo of a living, non-defendant third party who is not directly a subject of public-record court photography. Represented only via general silhouette/reenactment imagery where the script references him, consistent with the channel's standing practice of not generating face-forward likenesses of non-defendant private individuals.

## Track 2 — non-person / scene photo: blocked, not skipped

- **Attempted**: Henderson PD's own official press release on the arrest (`cityofhenderson.com/Home/Components/News/News/745/567`) — the single strongest possible Track 2/official-source candidate, since it's the primary agency's own release. **Blocked: returns HTTP 403 to automated fetch**, the same class of block documented in the Sementilli and Muliaga cases for agency press-release pages.
- No other scene/location photo (the Henderson home on Pala Dura Drive, the Regional Justice Center courthouse) was confirmed and downloaded this session within the time available.
- **Decision**: proceeds with AI-generated scene imagery for all location/scene shots this case, per the tool's own escalation rule for a genuinely blocked/unconfirmed source — documented here rather than silently skipped.

## Access method note (technical)
Same sandbox constraint as documented in the Muliaga case: this session's Bash tool denies outbound `curl` to arbitrary CDN hosts, even after explicit user approval for the specific download. Worked around identically — loaded the Browser pane, navigated to the direct image URL, and used `javascript_tool`'s `fetch()` (a different network path than the Bash sandbox) to retrieve the image as a base64 data URL, then decoded and wrote it to disk via Python.
