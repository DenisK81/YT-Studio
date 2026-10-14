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

## Scheduling collision — real incident, 2026-08-06 (`list-uploads` is blind to scheduled-private videos)

Scheduled the 5 Kevin West assets after checking `list-uploads` for "anything already booked in
the future" and seeing nothing past 2026-08-05 — concluded the near-future slots were free.
**They weren't.** 4 of the 5 chosen slots exactly collided with Michael Thompson's 4 remaining
Shorts, which were sitting `privacyStatus: private` with a future `publishAt` at the time.

**Root cause:** `list-uploads` calls `playlistItems().list()` on the channel's uploads playlist.
That endpoint only returns videos that are already public (or otherwise visible in the playlist
listing) — it does **not** surface videos in `privacyStatus: private` with a future `publishAt`,
even though they are real, already-scheduled videos that will go live and would collide.
Checking "is this future slot free?" via `list-uploads` alone is structurally unable to see the
exact case it needs to catch.

**Fix — standing rule, not a one-off:** before calling `confirm_publish(..., publish_at=...)`
for any new batch, check the real `status.publishAt` of every video ID from **every other
case's own `PublishPlan.md`** whose release window could plausibly overlap (not just the most
recent case — check any case with a still-in-the-future schedule), via:
```
videos().list(part="status", id="<comma-separated video_ids>")
```
and read each one's `status.privacyStatus` + `status.publishAt` directly. This is the only
reliable way to see a scheduled-but-still-private video. `list-uploads`/`playlistItems().list()`
is fine for "what has already gone live," never for "is this future slot free."

No videos were lost or overwritten in this incident — `confirm_publish()` only ever sets a
`publishAt` on the video ID it's called with, so both sets of videos were untouched and intact
throughout; the problem was purely that two unrelated videos would have gone live in the same
instant. Fixed by re-checking via `videos().list()` and rescheduling the colliding batch to start
after the other case's last remaining slot.

**Lesson learned:** don't identify an already-uploaded video by title-matching alone — a
channel-owner-uploaded video titled "She Sexted Her Husband's Killer — At His Funeral" was
initially assumed to be Short #2, but checking its real `contentDetails.duration` via the API
(`PT11M35S`) showed it was actually the **main video** uploaded under one of its `SEO.md` title
options, not a Short at all. Always verify by real duration/file size, not title text, before
concluding a specific render was or wasn't already published.

## Pinned comment automation — added 2026-07-31 (real gap found: SEO Agent/Shorts Agent always
drafted a `pinned_comment` field, but nothing ever actually posted it)

`post_comment(video_id, text)` in `youtube_agent.py` posts the pre-drafted `pinned_comment` from
`SEO.md`/`Shorts.md` as a top-level comment via `commentThreads().insert()`. Called once per
video/Short, right alongside that asset's `confirm_publish()` call, using the same
already-given human go-ahead for the batch (this is a much smaller, easily-reversible action
than the publish decision itself — a comment can be deleted — so it does not need its own
separate confirmation beyond the batch-level "yes, publish these" already required for
`confirm_publish`).

**Real limitation, not a bug to route around:** the YouTube Data API v3 has no endpoint to pin
a comment — `commentThreads.insert` can only post it. Making it the *pinned* top comment (the
one shown first, marked "Pinned by [channel]") is a channel-owner-only action in YouTube
Studio's own UI (comment's `...` menu → Pin). This tool posts the comment; it does not and
cannot pin it. If the channel owner wants it visibly pinned, that's a ~5-second manual step in
Studio after each publish — no API workaround exists, and scraping Studio's web UI to fake it
would be fragile and against the API's terms, so this tool deliberately doesn't attempt that.

**New scope required:** `youtube.force-ssl` was added to `SCOPES` for `commentThreads.insert`.
Since scopes changed, the cached token at `Config/youtube_token.json` needs one more
`python youtube_agent.py auth` re-consent (opens a browser, channel owner clicks Allow again)
before `comment`/`post_comment()` will work — the old token issued under the narrower scope set
will otherwise fail on this specific call.

**Resolved 2026-07-31:** the new scope initially failed with a silent `403 insufficient
permissions` even after re-auth — the scope appeared in the consent URL but Google wasn't
actually granting it. Root cause: **this app's OAuth consent screen (Google Cloud Console →
APIs & Services → OAuth consent screen → Scopes) has its own explicit allow-list of scopes** —
requesting a scope in the auth URL that isn't also added there gets silently dropped from the
issued token, no error at auth time. Fixed by adding `youtube.force-ssl` there, then re-running
`python youtube_agent.py auth` once more. `post_comment()` now works.

**Real platform restriction (not a bug):** `commentThreads.insert` returns the same
`403 insufficient permissions` error on a video that is still `privacyStatus: private`
(i.e. scheduled but not yet live) — YouTube does not allow comment threads on private videos
regardless of scope/ownership. Comments for a scheduled video can only be posted once
`publishAt` has actually passed and the video flips public. There's no way to pre-stage a
comment for a not-yet-public video; `post_comment()` must be called again after the video goes
live.

## Analytics — added 2026-07-31 (channel owner asked for real per-video performance data,
not just the aggregate stats `videos().list` gives)

`get_analytics_service()` builds a separate `youtubeAnalytics` v2 API client (distinct from the
`youtube` v3 client used everywhere else in this module — different discovery doc, same cached
OAuth credentials). `video_analytics(video_id, start_date, end_date)` queries `reports().query()`
for `views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage` on `dimensions=
video`, filtered to one video.

- **New scope required:** `yt-analytics.readonly`. Same Cloud Console gotcha as `force-ssl`
  above — the underlying **YouTube Analytics API also had to be explicitly enabled** in
  Google Cloud Console → APIs & Services → Library before its scope would even appear in the
  OAuth consent screen's scope picker. Enable the API first, then add the scope, then re-auth.
- **`impressions`/`impressionsClickThroughRate` (thumbnail CTR) are NOT queryable** on this
  channel via this `reports().query()` shape — the API rejects them outright with
  `Unknown identifier (impressions)`, not a permissions or data-availability error. Deliberately
  left out of `video_analytics()`'s metric list rather than silently retried or faked. If
  thumbnail CTR is ever needed, check YouTube Studio's own Analytics tab directly (it has real
  per-video CTR) — there is currently no working API path to it from this tool.
- **Processing lag:** metrics return `None` for videos published within roughly the last 1-3
  days — YouTube Analytics data isn't processed in real time. Don't read a `None` result as
  "zero performance," it means "not processed yet."
- Real first test (2026-07-31): Muliaga main (published 2026-07-28) showed 4 views, 182s average
  view duration, 41.08% average view percentage; Muliaga short_1 (published 2026-07-29) showed
  37 views, 18s average view duration, 69.49% average view percentage — the higher retention
  percentage on the Short vs. the main video is the expected short-form-vs-long-form pattern,
  not a hook-quality signal on this small a sample.

## Comment engagement — added 2026-09-15 (real gap found by a channel audit: 21 of 23 comment
threads on the whole channel were our own pinned CTA posts; only 2 were real viewers, and one —
"What channel!!! What name?" — had sat unanswered for 7 weeks, the exact scenario that already
once forced the mandatory channel-footer-link fix in CLAUDE.md)

`list_comments(video_id=None, max_results=50)` lists top-level comment threads, newest first —
omit `video_id` for a channel-wide pull via `allThreadsRelatedToChannelId` (what a "check for new
comments" pass should use), or pass one to scope to a single video. Returns each thread's
`thread_id`, top-level `comment_id`, `author`, `text`, and `reply_count`. `reply_comment
(parent_comment_id, text)` posts a threaded reply under an existing top-level comment via
`comments().insert(parentId=...)` — distinct from `post_comment()`, which starts a brand-new
top-level thread.

**Process, not full automation (Phase 1 scope):** this is a manual per-session check, not an
unattended auto-reply bot — run `list-comments` (filter out rows authored by the channel's own
handle to find real viewer comments), read/judge each one, then `reply-comment` the ones worth
answering. Do this at the start of any session that touches the channel, AND every time a batch
of videos is scheduled/published (see below) — real comments can land on any older video at any
time, so a session-start check alone isn't enough. No scheduled/cron version exists yet — same
"manual until Phase 2" boundary as the rest of this tool.

**Mandatory as part of every publish, not a separate follow-up (escalated 2026-09-27, real gap
found: McCullagh, Blaise Taylor, and Frederick Spears — 15 videos across 3 cases — all went
public with zero comment threads, because `post_comment()` was never actually called after
upload despite every case's SEO.md/Shorts.md having a pre-drafted `pinned_comment`/CTA line the
whole time).** The channel owner's instruction: comments get checked after publishing *every*
video, not as a thing to remember to circle back to. Treat this as the last step of the publish
sequence itself: once a batch of videos is scheduled, (1) call `post_comment()` with each video's
own pre-drafted line for every video that is *already public* (remember the private-video
restriction above — a scheduled-but-not-yet-live video will 403; queue the still-scheduled ones
for whenever they flip public, e.g. as part of the next session's check), and (2) run
`list-comments` across the channel (or scoped to the videos that just went live) and reply to any
genuine viewer comment. Remind the pin step is manual-in-Studio (see `post_comment()`'s own
docstring) — the API cannot pin.

- **CLI note (fixed 2026-09-27):** `list-comments`/`reply-comment`'s printed output used to hit
  `UnicodeEncodeError` on Windows' default `cp1252` console for em-dashes/emoji in comment text.
  Fixed at the source, not per-caller: `youtube_agent.py` now calls
  `sys.stdout.reconfigure(encoding='utf-8', errors='replace')` once at import time, so this no
  longer needs to be remembered per invocation.

## Interrupted upload batch (found 2026-10-09, Atrops case)

An `HTTP 410 Gone` on a resumable upload (`prepare_upload`'s `next_chunk`) in the middle of a batch
does NOT mean nothing was uploaded: the earlier file in the batch (the main video) had already
finished and processed, and the failing file (a Short) left a stuck stub (`uploadStatus: uploaded`,
`processingStatus: processing` for ~22 hours, duration `P0D`, private). Before any retry:
(1) list the channel's uploads read-only and match by title; (2) identify finished vs stub videos
by `contentDetails.duration` and `processingStatus`; (3) only a private, zero-duration, stuck
stub that you uploaded yourself may be deleted (`videos().delete`; the list can still show it for
a few seconds afterwards); (4) re-upload only the missing files, one at a time, with a title
guard against the channel's existing titles, and stop on the first error instead of auto-retrying.
Scheduling is still done only after a live read confirms five distinct titles and no slot collisions.

**Read-after-write lag (2026-10-13):** right after `confirm_publish(..., publish_at=...)` a `videos.list` read can come back WITHOUT `publishAt` for several seconds (a replacement script stopped on a false mismatch). Poll the read for up to ~60 s before treating it as a failure. When replacing a scheduled private video: upload the new one and verify it holds the old slot BEFORE deleting the old one; the new id needs the Studio 'Altered or synthetic content' toggle set again.
