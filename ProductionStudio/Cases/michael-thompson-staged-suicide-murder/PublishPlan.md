```json
{
  "release_plan": [
    { "date": "TBD", "asset": "main video", "video_id": null, "status": "not yet uploaded — awaiting render completion and channel owner's publish schedule" },
    { "date": "TBD", "asset": "short 1 (He Faked The CPR)", "video_id": null, "status": "not yet uploaded" },
    { "date": "TBD", "asset": "short 2 (The Earlier Death He Used As A Threat)", "video_id": null, "status": "not yet uploaded" },
    { "date": "TBD", "asset": "short 3 (The Post-Mortem Exposed The Lie)", "video_id": null, "status": "not yet uploaded" },
    { "date": "TBD", "asset": "short 4 (He Didn't Show Up For His Own Sentencing)", "video_id": null, "status": "not yet uploaded" }
  ],
  "playlists": ["Husband Killed Wife (PLbNIKr64Fk0Y) — second video for this playlist, no new playlist needed"],
  "awaiting_human_confirmation": true
}
```

**Status:** no publish schedule has been given yet for this case. Per `Agents/publishing_agent.md`'s
hard rule, `confirm_publish(human_confirmed=True, ...)` will not be called for any of these 5
assets until the channel owner gives an explicit go-ahead with specific times, checked against
the real schedule of every prior case's slots to avoid overlap (same process used for Walter
Buchanan's schedule).

**Next steps once render is verified:** upload all 5 assets as PRIVATE via `prepare_upload()`
(with thumbnail set — ready in `Thumbnail.md`), add the main video to the existing `Husband
Killed Wife` playlist, then wait for the channel owner's explicit schedule before any
`confirm_publish()` call. Post each asset's pinned comment via `post_comment()` right alongside
its `confirm_publish()` call, per the standing process established for the Walter Buchanan case
— skip any asset that's still private when its comment attempt is made and retry once it's
actually public.
