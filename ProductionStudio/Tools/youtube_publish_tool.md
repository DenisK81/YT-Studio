# Tool: youtube_publish_tool

## Purpose
Wraps YouTube Data API v3 for upload + metadata. The actual publish call is always gated by an
explicit human confirmation step (see `Agents/publishing_agent.md`) — this tool prepares and
can stage the upload, but firing it is never silent/automatic.

## Interface
```
prepare_upload(video_file: string, metadata: {
  title, description, tags, category, thumbnail_file, publish_at
}) -> { draft_id }

confirm_publish(draft_id: string) -> { video_id, status }   // only called after human go-ahead
```

## Implementation notes
- Requires YouTube OAuth client + refresh token stored in the orchestrator's credential store —
  not something available from a plain chat sandbox.
- Respect the channel owner's own pacing plan (documented in `fatal-affairs-project-brief.md`):
  main video + one strong short same day, remaining shorts staged one per day after — this
  tool should support scheduled `publish_at` timestamps per asset, not just immediate publish.
- Quota-aware: YouTube Data API has daily quota limits; batch metadata reads/writes sensibly
  once this scales past a handful of videos a week.
