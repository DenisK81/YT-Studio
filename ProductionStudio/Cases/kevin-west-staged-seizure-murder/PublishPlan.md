```json
{
  "release_plan": [
    { "date": "2026-08-05 20:00 PT (America/Los_Angeles) / 2026-08-06T03:00:00Z", "asset": "main video", "video_id": null, "status": "not yet uploaded — awaiting render completion and channel owner's go-ahead" },
    { "date": "2026-08-06 07:00 PT / 2026-08-06T14:00:00Z", "asset": "short 1 (He Knew Exactly What To Say)", "video_id": null, "status": "not yet uploaded" },
    { "date": "2026-08-06 19:00 PT / 2026-08-07T02:00:00Z", "asset": "short 2 (The Affair He Hid For 20 Years)", "video_id": null, "status": "not yet uploaded" },
    { "date": "2026-08-07 07:00 PT / 2026-08-07T14:00:00Z", "asset": "short 3 (His Fiancee May Have Been There That Morning)", "video_id": null, "status": "not yet uploaded" },
    { "date": "2026-08-07 19:00 PT / 2026-08-08T02:00:00Z", "asset": "short 4 (He Apologized For The Affair, Not The Murder)", "video_id": null, "status": "not yet uploaded" }
  ],
  "playlists": ["Husband Killed Wife — second-ever video, following Buchanan and Thompson", "Love Triangle Murders"],
  "awaiting_human_confirmation": true
}
```

**Status:** no publish schedule has been given yet for this case. Per `Agents/publishing_agent.md`'s
hard rule, `confirm_publish(human_confirmed=True, ...)` will not be called for any of these 5
assets until the channel owner gives an explicit go-ahead, with times checked against the real
schedule via the API immediately beforehand (not just against this file, since actual publish
times can drift from what was originally planned — see below).

**Real-schedule check, 2026-08-05:** ran `youtube_agent.py list-uploads` before proposing these
slots. The most recent real, live asset on the channel is `Zw7QoMCl4q0` ("She Had The Right To
Be Safe" — The Sentence #shorts), actually published 2026-08-05T02:00:23Z — already in the past
relative to the current real time (2026-08-05 ~07:40 PT). No video currently sits in a
future-scheduled state on the channel, so the slots above are genuinely free, not just assumed
free from a stale plan file (the Thompson case's own `PublishPlan.md` shows this exact drift: it
proposed Aug 5-7 slots, but ground truth shows all 5 of its assets actually went live Aug 3-5
instead — always re-check live, don't trust a case's own prior plan file for "is this slot
open").

**Next steps once render is verified:** upload all 5 assets as PRIVATE via `prepare_upload()`
(with thumbnail set — ready in `Thumbnail.md`), add the main video to the `Husband Killed Wife`
and `Love Triangle Murders` playlists (creating `Love Triangle Murders` via
`get_or_create_playlist()` if it doesn't already exist under that exact name — idempotent either
way), then wait for the channel owner's explicit schedule confirmation before any
`confirm_publish()` call. Post each asset's pinned comment via `post_comment()` right alongside
its `confirm_publish()` call — expect it to 403 on any asset still private and simply retry once
that asset is actually public, per the documented platform restriction in
`Tools/youtube_publish_tool.md`.

**Pinned comment text (ready in advance):**
- main: "Detective Dean Telecsan testified that strangulation takes only seven to ten seconds to cause unconsciousness. The jury deliberated for about two hours before finding Kevin West guilty on both counts. What stood out to you most about this case? Tell us below, we read every comment."
- short 1: "He spent 22 years training for calls exactly like this one. Full story on the main channel."
- short 2: "He was planning to leave his wife the exact same day she died. Full story on the main channel."
- short 3: "By the time she testified, they were already engaged. Full story on the main channel."
- short 4: "\"That is my only wrongdoing,\" he told the court — about the affair, not the killing. Full story on the main channel."
