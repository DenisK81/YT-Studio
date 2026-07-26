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

## Playlists (added 2026-07-26, revised same day)

First attempt used one playlist per case (`Case Files: {Case Name}`). The channel owner rejected
this after checking how competitor true-crime channels actually organize their playlists — real
channels group by **theme/motive**, not by case name, since that's what a viewer browses by
("show me more love-triangle murders", not "show me more Case Files"). Deleted the 4 case
playlists (`delete_playlist()`) and replaced them with themed ones:

- `Love Triangle Murders`
- `Wife Killed Husband`
- `Murder For Insurance Money`
- `Framed The Wrong Person`

A video normally belongs in 2-3 of these — e.g. the Monica Sementilli and Kouri Richins videos
are all in `Wife Killed Husband` AND `Murder For Insurance Money`, and Sementilli/Banfield/Molly
Watson are all in `Love Triangle Murders` too. That overlap is intentional, not a dedup bug.
Created via `get_or_create_playlist(title, description)` (idempotent by title) and populated via
`add_video_to_playlist(playlist_id, video_id)`; for a new case, pick its 2-4 fitting existing
themes first, only make a new themed playlist if nothing fits. Two pre-existing videos
("Renovation", an untitled cold-open clip) had empty descriptions and no identifiable
case/theme — left out of every playlist rather than guessed.

## Scheduling in practice (2026-07-26 real run)

First real batch of `confirm_publish(..., publish_at=...)` calls: the 4 Monica Sementilli
Shorts, scheduled across 2 days per the channel owner's explicit slots, computed in
America/Los_Angeles and converted to UTC (see CLAUDE.md's timezone project fact):

| Short | LA local time | UTC `publishAt` |
|---|---|---|
| short_1 "She Watched The Murder On Camera" | 2026-07-26 08:00 PDT | `2026-07-26T15:00:00Z` |
| short_2 "She Sexted Her Husband's Killer..." | 2026-07-26 20:00 PDT | `2026-07-27T03:00:00Z` |
| short_3 "The Killer Took The Stand To Save Her" | 2026-07-27 07:00 PDT | `2026-07-27T14:00:00Z` |
| short_4 "8 Years Later, The Verdict Finally Came" | 2026-07-27 19:00 PDT | `2026-07-28T02:00:00Z` |

**Lesson learned:** don't identify an already-uploaded video by title-matching alone — a
channel-owner-uploaded video titled "She Sexted Her Husband's Killer — At His Funeral" was
initially assumed to be Short #2, but checking its real `contentDetails.duration` via the API
(`PT11M35S`) showed it was actually the **main video** uploaded under one of its `SEO.md` title
options, not a Short at all. Always verify by real duration/file size, not title text, before
concluding a specific render was or wasn't already published.
