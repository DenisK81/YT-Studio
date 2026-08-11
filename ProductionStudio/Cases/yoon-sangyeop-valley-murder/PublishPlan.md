```json
{
  "release_plan": [
    { "date": "TBD - not yet scheduled", "asset": "main video", "video_id": null, "status": "not yet uploaded — awaiting render completion and channel owner's go-ahead" },
    { "date": "TBD", "asset": "short 1 (The Text That Proved It Was Murder)", "video_id": null, "status": "not yet uploaded" },
    { "date": "TBD", "asset": "short 2 (He Said Four Words And Stayed Anyway)", "video_id": null, "status": "not yet uploaded" },
    { "date": "TBD", "asset": "short 3 (He Surfaced. Nobody Moved.)", "video_id": null, "status": "not yet uploaded" },
    { "date": "TBD", "asset": "short 4 (The Court's Real Verdict)", "video_id": null, "status": "not yet uploaded" }
  ],
  "playlists": ["Wife Killed Husband", "Murder For Insurance Money", "Love Triangle Murders"],
  "awaiting_human_confirmation": true
}
```

**Status:** no publish schedule has been given yet for this case. Per `Agents/publishing_agent.md`'s
hard rule, `confirm_publish(human_confirmed=True, ...)` will not be called for any of these 5
assets until the channel owner gives an explicit go-ahead.

**Mandatory real-schedule check before proposing slots (per the 2026-08-06 Kevin West incident):**
`list-uploads`/`playlistItems().list()` is blind to videos sitting `privacyStatus: private` with
a future `publishAt` — it must NOT be used alone to judge whether a slot is free. Before proposing
times for this case, run `videos().list(part="status", id=...)` against every video ID from every
other case's own `PublishPlan.md` whose release window could still be in the future — at the time
this file was written, Kevin West's short 2/3/4 (`Vn7wnR0g9qo`, `gvES3KmQNeE`, `w7IhyyOtVvA`) were
still scheduled for 2026-08-09/10, and must be checked again (their actual state may have changed
by the time this case is ready to publish) before picking slots for this case.

**Playlist fit:** three existing themes apply — `Wife Killed Husband`, `Murder For Insurance
Money`, `Love Triangle Murders` — no new playlist needed.

**Pinned comment text (ready in advance, see `SEO.md`/`Shorts.md` for full text):**
- main: "Detective work aside, the courts never found that Lee or Cho physically pushed Yoon into the water — every court that heard this case, up to the Supreme Court, convicted on the theory that they let him drown in front of them and chose not to help. What stood out to you most about this case? Tell us below, we read every comment."
- short 1: "He knew what she'd already tried twice. He climbed the cliff anyway. Full story on the main channel." *(placeholder — confirm against final short 1 content before posting)*
- short 2, 3, 4: see each short's narrative beat in `Shorts.md`, draft a matching one-line pinned comment at publish time following the same pattern as every prior case this session.

**Next steps once render is verified:** upload all 5 assets as PRIVATE via `prepare_upload()`
(thumbnail set on the main video), add the main video to all 3 fitting playlists, re-check the
real schedule via `videos().list()` (not `list-uploads`) immediately before proposing times, then
wait for the channel owner's explicit schedule confirmation before any `confirm_publish()` call.
