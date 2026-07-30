```json
{
  "release_plan": [
    { "date": "2026-07-30 20:00 PT (America/Los_Angeles) / 2026-07-31T03:00:00Z", "asset": "main video", "video_id": "yIoe30D8NVc", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-07-31 07:00 PT / 2026-07-31T14:00:00Z", "asset": "short 1 (Never Tested)", "video_id": "nKPHL_E9ua8", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-07-31 19:00 PT / 2026-08-01T02:00:00Z", "asset": "short 2 (Married The Son)", "video_id": "8tSKkxq6mhY", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-08-01 07:00 PT / 2026-08-01T14:00:00Z", "asset": "short 3 (She Blamed Her Own Husband)", "video_id": "N_mPMKMgT50", "status": "scheduled via youtube_agent.py confirm_publish()" },
    { "date": "2026-08-01 19:00 PT / 2026-08-02T02:00:00Z", "asset": "short 4 (Buckle Up)", "video_id": "s2rilsnU8pM", "status": "scheduled via youtube_agent.py confirm_publish()" }
  ],
  "playlists": ["Love Triangle Murders (PLex0mHScQ9nU) - added to main video"],
  "awaiting_human_confirmation": false
}
```

**Update 2026-07-30:** the channel owner gave explicit go-ahead with exact LA-local times: main
video at 8pm on 2026-07-30, then 2 shorts per day at 7am/7pm across 2026-07-31 and 2026-08-01.
All 5 videos uploaded as PRIVATE drafts via `prepare_upload()` (with thumbnails set), then all 5
scheduled for real via `confirm_publish(human_confirmed=True, publish_at=...)`.
`awaiting_human_confirmation` is now `false` because that confirmation already happened for
these 5 specific videos, at these specific times — this does NOT waive the hard rule for any
future video.

**Playlist decision:** the channel owner was asked to choose between `Love Triangle Murders` and
`Framed The Wrong Person` (via `AskUserQuestion`) but did not answer before the upload/schedule
step. Proceeded with `Love Triangle Murders` — the better technical fit (a real triangle:
Michaels, Johnathan, Deviere) — as a reasonable default rather than blocking the whole batch.
**Flagging this explicitly: if the channel owner wants `Framed The Wrong Person` instead (or
both), the main video can be added to it after the fact via `add_video_to_playlist()` — nothing
needs to be re-uploaded.**

**Hard rule, unchanged:** nothing is published automatically going forward. Per
`Agents/publishing_agent.md`, every future upload still requires explicit human confirmation at
the time, with no exceptions regardless of pipeline automation elsewhere.
