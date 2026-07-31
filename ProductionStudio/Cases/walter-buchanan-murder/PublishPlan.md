```json
{
  "release_plan": [
    { "date": "2026-08-02 20:00 PT (America/Los_Angeles) / 2026-08-03T03:00:00Z", "asset": "main video", "video_id": "Eht9nJmIerE", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-08-03 07:00 PT / 2026-08-03T14:00:00Z", "asset": "short 1 (He Never Mentioned The Fight)", "video_id": "k9L54SZ1kwA", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-08-03 19:00 PT / 2026-08-04T02:00:00Z", "asset": "short 2 (She Caught Him Cheating)", "video_id": "a2w4MjorybM", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-08-04 07:00 PT / 2026-08-04T14:00:00Z", "asset": "short 3 (What Police Found On Her Phone)", "video_id": "cKm7YEP6Lpg", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-08-04 19:00 PT / 2026-08-05T02:00:00Z", "asset": "short 4 (15 Years Minimum)", "video_id": "Zw7QoMCl4q0", "status": "scheduled via youtube_agent.py confirm_publish()" }
  ],
  "playlists": ["Husband Killed Wife (PLbNIKr64Fk0Y) — new playlist created for this case"],
  "awaiting_human_confirmation": false
}
```

**Update 2026-07-31:** the channel owner reviewed the proposed schedule (checked against every
prior case's real slots to avoid overlap — see chat) and confirmed it as-is. All 5 videos
uploaded as PRIVATE drafts via `prepare_upload()` (thumbnail set on the main video), added to
the newly-created `Husband Killed Wife` playlist, then all 5 scheduled for real via
`confirm_publish(human_confirmed=True, publish_at=...)`. `awaiting_human_confirmation` is now
`false` because that confirmation already happened for these 5 specific videos, at these
specific times — this does NOT waive the hard rule for any future publish.

**Playlist resolved:** `Husband Killed Wife` was confirmed and created — no existing playlist
fit this case (see `SEO.md`'s reasoning: no love triangle, no insurance motive, no frame-up of
an innocent third party, and unlike Muliaga the jealousy was well-founded, not unfounded).

**Pinned-comment automation — partially blocked:** per the channel owner's 2026-07-31 request,
every publish should also post its pre-drafted `pinned_comment`/short `comment` text. Built
`post_comment()` in `youtube_agent.py` (see `Tools/youtube_publish_tool.md`'s new section) and
attempted it for all 5 videos immediately after scheduling — **all 5 failed with HTTP 403
"insufficient permissions,"** even after re-running `youtube_agent.py auth` to pick up the new
`youtube.force-ssl` scope. The scope shows up in the consent URL, but Google is not actually
granting it — this almost always means the scope needs to be explicitly added under **Google
Cloud Console → APIs & Services → OAuth consent screen → Scopes** for this app before Google
will issue a token that actually carries it; requesting an unlisted scope in the auth URL alone
doesn't grant it. This is a channel-owner action in Google Cloud Console, not something fixable
from this session. Once added there, re-run `python youtube_agent.py auth` once more and the 5
comments below can be posted via `python youtube_agent.py comment <video_id> "<text>"`:
- main (`Eht9nJmIerE`): "The judge called Buchanan's incomplete 911 call itself evidence of guilt — he never once mentioned the fight, not to the operator, not to the paramedics. Investigators also found a text on Darrel's phone, sent by Buchanan, reading \"I hope you die you black b****.\" What stood out to you most? Tell us below, we read every comment."
- short 1 (`k9L54SZ1kwA`): "The judge called this omission itself \"a consciousness of guilt.\" Full case on the main channel — what do you think, was it enough on its own to prove guilt?"
- short 2 (`a2w4MjorybM`): "\"I guess you are having fun in Bothwell without your wife, cheater\" — that's the text she found. Full story on the main channel."
- short 3 (`cKm7YEP6Lpg`): "Friends and neighbours had already said the marriage had turned volatile. This text is part of why. Full story on the main channel."
- short 4 (`Zw7QoMCl4q0`): "\"Darrel Odhiambo was a loving mother, daughter, sister and friend, who had the right to be safe in her relationship and home.\" — Prosecutor Moira Orr. Full story on the main channel."

**Hard rule, unchanged:** nothing is published automatically going forward. Per
`Agents/publishing_agent.md`, every future upload still requires explicit human confirmation at
the time, with no exceptions regardless of pipeline automation elsewhere.
