```json
{
  "titles": [
    "He Called 911 and Left Out the Fight That Killed Her",
    "She Caught Him Cheating. Days Later, She Was Dead.",
    "The Text Message That Got Darrel Odhiambo Killed"
  ],
  "description": "Walter Buchanan, a 66-year-old chartered surveyor, met Darrel Odhiambo on holiday in Thailand in 2015. They married in 2017. By February 2023, six years into the marriage, friends and neighbours already knew it had turned volatile.\n\nOn February 18th, 2023, Darrel found a text message on her husband's phone proving he was cheating on her. Hours later, she was dead. Buchanan called emergency services at 7:12 the next morning, claiming he'd simply found her unresponsive — and left out the fight entirely, to the 911 operator and to the paramedics who tried to save her.\n\nThis is the real timeline of the Hamilton, Scotland murder case: the cheating text that started the confrontation, Buchanan's own account of the struggle given at trial, the post-mortem findings that contradicted it, the judge's finding that his incomplete 911 call was itself \"a consciousness of guilt,\" the eight-day trial at the High Court in Glasgow, and the January 2025 verdict that followed.\n\nAll facts in this video are sourced directly from the official Judiciary of Scotland sentencing opinion (HMA v Walter Buchanan) and the Crown Office and Procurator Fiscal Service's official press release, cross-checked against Police Scotland, STV News, and the Scottish Daily Express's trial coverage.\n\n0:00 The Hook\n0:29 Who They Were\n1:08 A Volatile Marriage\n1:35 The Text That Changed Everything\n2:14 What He Admitted\n3:12 The Trial\n4:02 Eight Days of Testimony\n4:37 The Verdict and Sentence\n5:09 What Was Left Behind\n5:59 A Question For You\n\nWhat stood out to you most — the racist text found on her phone, or the fact he never once mentioned the fight? Tell us in the comments, we read every one.\n\n#TrueCrime #WalterBuchanan #Scotland #TrueCrimeDocumentary #Glasgow\n\nFatal Affairs — subscribe for more true crime cases: https://www.youtube.com/@fatalaffairs-f1i",
  "chapters": [
    { "timestamp": "0:00", "label": "The Hook" },
    { "timestamp": "0:29", "label": "Who They Were" },
    { "timestamp": "1:08", "label": "A Volatile Marriage" },
    { "timestamp": "1:35", "label": "The Text That Changed Everything" },
    { "timestamp": "2:14", "label": "What He Admitted" },
    { "timestamp": "3:12", "label": "The Trial" },
    { "timestamp": "4:02", "label": "Eight Days of Testimony" },
    { "timestamp": "4:37", "label": "The Verdict and Sentence" },
    { "timestamp": "5:09", "label": "What Was Left Behind" },
    { "timestamp": "5:59", "label": "A Question For You" }
  ],
  "pinned_comment": "The judge called Buchanan's incomplete 911 call itself evidence of guilt — he never once mentioned the fight, not to the operator, not to the paramedics. Investigators also found a text on Darrel's phone, sent by Buchanan, reading \"I hope you die you black b****.\" What stood out to you most? Tell us below, we read every comment.",
  "tags": ["Walter Buchanan", "Darrel Odhiambo", "Hamilton Scotland murder", "Glasgow High Court trial", "true crime", "Scotland murder case", "strangulation case", "true crime documentary", "UK murder trial", "murder trial 2025", "domestic violence case", "consciousness of guilt"],
  "hashtags": ["#TrueCrime", "#WalterBuchanan", "#Scotland", "#TrueCrimeDocumentary", "#Glasgow"],
  "suggested_playlists": ["Husband Killed Wife (NEW — proposed, not yet created)"]
}
```

**Verification:** chapter timestamps computed from the real
`Assets/audio/walter-buchanan-murder/timing.json` (6:11 narration total, 371.006s) plus the fixed
2.5s `ChannelBumper` prepended to the video — first chapter stays at 0:00 per YouTube's own
requirement, every other timestamp offset by +2.5s per scene `startSeconds`. The new outro bumper
(2.5s, appended per the channel owner's 2026-07-30 "same brand screen at the end too" instruction)
adds to total runtime but doesn't shift any mid-video chapter timestamp. Total video length:
2.5s (intro) + 371.0s (narration) + 2.5s (outro) = 376.0s (~6:16). Tag string well under the
500-char limit; hashtag count = 5. Description ends with `CHANNEL_FOOTER` per the 2026-07-26
hard rule.

**Playlist note — flagging, not silently deciding:** checked all 5 existing themed playlists
(`Love Triangle Murders`, `Wife Killed Husband`, `Murder For Insurance Money`, `Framed The Wrong
Person`, `Unfounded Jealousy Murders`) against this case's actual shape and none fit. There's no
love triangle (the cheating was with an unnamed text-message contact, never a named third party
in the narrative), no insurance motive, no frame-up of an innocent third party (Buchanan
minimized his own actions rather than accusing someone else), and — unlike Muliaga — his jealousy
premise doesn't apply since Darrel genuinely had caught him cheating, not the reverse. This case
is the direct gender-mirror of `Wife Killed Husband`: a husband killing his wife after being
caught, followed by a cover-up. Proposing a new playlist, **`Husband Killed Wife`**, as the
correct parallel theme — flagging for the channel owner's confirmation before creating it via
`youtube_agent.py`'s `get_or_create_playlist()`, consistent with how `Unfounded Jealousy Murders`
was created for the Muliaga case rather than forcing a wrong-fit existing playlist.
