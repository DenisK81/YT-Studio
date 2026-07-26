```json
{
  "release_plan": [
    { "date": "2026-07-25 (actual)", "asset": "main video", "video_id": "37SdUL9S-AY", "status": "published (channel owner uploaded directly via YouTube Studio, title picked from SEO.md's options)", "pinned_comment": "She sent nude photos to her husband's killer during his funeral. If you'd been sitting next to her in that church, grieving beside her — would you have felt anything was wrong? Tell us below. We read every comment." },
    { "date": "2026-07-26 08:00 PDT / 2026-07-26T15:00:00Z", "asset": "short 1 (She Watched The Murder On Camera)", "video_id": "MWImIifQNzg", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-07-26 20:00 PDT / 2026-07-27T03:00:00Z", "asset": "short 2 (She Sexted Her Husband's Killer...)", "video_id": "NbizOpw65pg", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-07-27 07:00 PDT / 2026-07-27T14:00:00Z", "asset": "short 3 (The Killer Took The Stand To Save Her)", "video_id": "arqfpT5AanM", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-07-27 19:00 PDT / 2026-07-28T02:00:00Z", "asset": "short 4 (8 Years Later, The Verdict Finally Came)", "video_id": "NvIekvoLu1k", "status": "scheduled via youtube_agent.py confirm_publish()" }
  ],
  "playlists": ["Love Triangle Murders (PLex0mHScQ9nU)", "Wife Killed Husband (PLe6_jN9U_ijM)", "Murder For Insurance Money (PLVCbFw1Wp6mk)"],
  "awaiting_human_confirmation": false
}
```

**Update 2026-07-26:** the original plan below (one short per day, main + short 1 same day) was
superseded by the channel owner's own real schedule — 2 shorts per day across 07-26/07-27, all
4 scheduled for real via `youtube_agent.py` after the channel owner gave explicit go-ahead with
exact LA-local times for each slot. `awaiting_human_confirmation` is now `false` because that
confirmation already happened for these 4 specific videos, at these specific times — this does
NOT waive the hard rule for any future video; each new publish still needs its own explicit
go-ahead per `Agents/publishing_agent.md`.

**Hard rule, unchanged:** nothing is published automatically going forward. Per
`Agents/publishing_agent.md`, every future upload still requires explicit human confirmation at
the time, with no exceptions regardless of pipeline automation elsewhere.

**Original pacing rationale (superseded, kept for reference):** one strong short (the
surveillance-video hook, matching the thumbnail) same-day as the main video to drive immediate
cross-traffic, remaining three staged one per day — never all dumped on day one, per the
channel's existing pacing note. The channel owner chose a tighter 2-per-day cadence instead for
this batch.
