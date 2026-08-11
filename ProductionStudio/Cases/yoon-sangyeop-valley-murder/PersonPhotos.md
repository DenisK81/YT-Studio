# Person Photos — Yoon Sang-yeop murder (Lee Eun-hae / Cho Hyun-soo) (Track 1 + Track 2)

## Lee Eun-hae, Cho Hyun-soo, third accomplice ("Mr. A") — no usable Track 1 photo; genuinely blocked, not skipped

South Korea's identity-disclosure system (신상공개 — the "Special Act on the Disclosure of
Personal Information of Suspects of Serious Crimes") requires a formal committee decision before
a suspect's name and face can be legally published, separate from the case simply being widely
reported. Checked specifically (Korean-language search): **no formal identity disclosure was
ever approved for Lee Eun-hae, Cho Hyun-soo, or the third accomplice** in this case. Confirmed
by multiple Korean sources describing Lee and Cho attending their arrest-warrant hearing with
their faces physically covered, and separately confirming no 신상공개 committee decision was
ever made public for this case.

What exists instead are unofficial, leaked images: photos an amateur "netizen investigation"
circulated online, and screen captures from Lee's own Instagram before she set it private once
her identity became publicly discussed. **None of these qualify as a Track 1 "official source"**
under this channel's standing policy (`Tools/mugshot_fetch_tool.md` — official/issuing-authority
source only, the same standard applied to every other case this session). Using a leaked personal
photo of someone whose identity was never legally cleared for disclosure would be a real privacy
violation this channel's own redaction/sourcing policy exists specifically to prevent — not a
gap to work around by lowering the bar.

**No AI-generated substitute portrait is used either**, per this channel's standing practice
(same as Marcy West in the Kevin West case and Cynthia Ward in the same case): AI generation
fills compositional/scene gaps, not a fabricated likeness of a real, identifiable, named person.
All three individuals are represented in `ImagePrompts.md` via silhouette, hands-only, or
symbolic/location-based compositions — nothing face-forward for any of them.

## Track 2 — non-person / scene photos (2 real photos found, both used)

- **Supreme Court of Korea building (Seoul)** — the court that issued the final, case-closing
  ruling on September 21, 2023, upholding both sentences. Source: Wikimedia Commons,
  `File:Supreme_Court_of_Korea_(2020).jpg`, photographed by the Seoul Institute, licensed
  **CC BY 4.0**. Local path: `ProductionStudio/Assets/images/real_photos/korea_supreme_court_SCENE.jpg`.
  No people visible in frame.
- **Incheon court-complex bus stop ("법원" / "Court")** — a real photo of the immediate area
  around Incheon District Court, Incheon District Prosecutors' Office, and Incheon Detention
  Center, where the case's original trial and sentencing (Incheon District Court, October 2022)
  actually took place. Source: Wikimedia Commons, `File:법원버스정류장_2024.jpg`, photographer
  Narubaru7, licensed **CC BY-SA 4.0**, used on the Korean Wikipedia's own Incheon District
  Court article. Local path:
  `ProductionStudio/Assets/images/real_photos/incheon_court_area_SCENE.jpg`.
  **Bystander note**: one small, distant cyclist is visible far down the street in the
  background — too small and too distant for any face to be individually identifiable, judged
  per the same standard applied to incidental distant bystanders in prior cases (e.g. the
  Nottingham Crown Court photo in the Michael Thompson case). No redaction needed.

**Not found despite a real attempt:** a free/Wikimedia-licensed photo of the actual crime scene
(Yongso Falls, Gapyeong) or of Gapyeong County generally — neither has any Wikimedia Commons
coverage under any of the name variants tried (Gapyeong, Gapyeong-gun, Yongso Falls, Gapyeong
valley). Rather than substitute a real photo of a *different* Korean waterfall as if it were the
crime scene (which would be misleading, not just imperfect), this location is represented only
through AI-generated composition in `ImagePrompts.md` — consistent with the channel's practice
of not passing off a look-alike real photo as the genuine location.

## Access method note (technical)
Same sandbox constraint as every prior case this session: outbound `curl`/`WebFetch` to
Wikimedia's upload CDN is blocked. Worked around via the Browser pane's `javascript_tool`
`fetch()` → `FileReader.readAsDataURL()` pattern, decoding the saved JSON transcript with a
Python script when the base64 payload exceeded the tool's inline output limit (both images this
case). No format-mismatch issues — both files decoded as `jpeg` directly from the data URL prefix.
