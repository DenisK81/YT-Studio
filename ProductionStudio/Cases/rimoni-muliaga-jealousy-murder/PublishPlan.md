```json
{
  "release_plan": [
    { "date": "2026-07-29 08:00 PT (America/Los_Angeles) / 2026-07-29T15:00:00Z", "asset": "main video", "status": "PROPOSED - not yet uploaded, awaiting human go-ahead" },
    { "date": "2026-07-29 20:00 PT / 2026-07-30T03:00:00Z", "asset": "short 1", "status": "PROPOSED - not yet uploaded, awaiting human go-ahead" },
    { "date": "2026-07-30 07:00 PT / 2026-07-30T14:00:00Z", "asset": "short 2", "status": "PROPOSED - not yet uploaded, awaiting human go-ahead" },
    { "date": "2026-07-30 19:00 PT / 2026-07-31T02:00:00Z", "asset": "short 3", "status": "PROPOSED - not yet uploaded, awaiting human go-ahead" },
    { "date": "2026-07-31 07:00 PT / 2026-07-31T14:00:00Z", "asset": "short 4", "status": "PROPOSED - not yet uploaded, awaiting human go-ahead" }
  ],
  "playlists": ["NEEDS DECISION - see Checklist.md / SEO.md, no existing theme cleanly fits this case"],
  "awaiting_human_confirmation": true
}
```

**Pacing rationale:** matches the 2-per-day shorts cadence the channel owner actually chose for
the Sementilli batch (main + short 1 same day, then 2 shorts/day for the remaining days) rather
than the original 1-per-day proposal — reusing the pattern that was already explicitly approved
once. Exact dates/times are a proposal only and can be moved.

**Hard rule, unchanged:** nothing gets uploaded or scheduled until the channel owner gives
explicit go-ahead in chat for this specific batch, per `Agents/publishing_agent.md`. No video_id
exists yet for any asset in this case — `prepare_upload()`/`confirm_publish()` have not been
called.

**Blocking item before this plan can be finalized:** the playlist assignment (see `SEO.md` and
`Checklist.md`) — need either a new themed playlist created for this case's angle (unfounded
jealousy / husband kills wife) or a decision to loosely fit it into an existing one.
