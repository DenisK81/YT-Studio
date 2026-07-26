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

## Status: implemented (2026-07-25) — `Workflows/youtube_agent.py`

This is now the one real module every future publish goes through, per the channel owner's
explicit instruction ("write it once, reuse for all future publications") — not a draft
spec anymore.

- `prepare_upload()` = this doc's `prepare_upload()`, uploads as `privacyStatus: private`
  with full metadata and returns the real YouTube `video_id` as the `draft_id`. A private
  upload isn't a publish action (nobody but the channel owner can see it, fully reversible),
  so this runs without a separate human-confirmation gate.
- `confirm_publish()` = this doc's `confirm_publish()`, the only function that can flip a
  video to public or schedule it (`publishAt` + `privacyStatus: private` for scheduling, per
  the real API's actual mechanism). Hard-requires `human_confirmed=True` passed explicitly —
  raises and refuses otherwise. This is the code-level backstop for
  `Agents/publishing_agent.md`'s hard rule; the real gate is still that Claude must never
  pass `human_confirmed=True` without an actual "yes, publish this" from the channel owner
  in the current session, for that specific video.
- Credentials: OAuth client from Google Cloud Console at
  `Config/client_secret_*.json`, cached token at `Config/youtube_token.json` — both
  gitignored, never committed. One-time setup: `python youtube_agent.py auth` opens a local
  browser for the channel owner's own Google login; Claude never sees or enters the password.
- Scopes: `youtube.upload` + `youtube` (covers upload, metadata, thumbnails, playlists —
  the full "manage the channel" surface, not just publishing one video).
