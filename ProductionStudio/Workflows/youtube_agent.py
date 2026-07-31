"""Official YouTube Data API v3 wrapper - the single module every future publish goes
through, per the channel owner's instruction (2026-07-25): write it once, reuse it for
every case going forward. Implements the prepare/confirm split from
Tools/youtube_publish_tool.md exactly:

    prepare_upload()  -> uploads the video as PRIVATE with full metadata, returns video_id
    confirm_publish() -> the ONLY call that makes a video public/scheduled. Requires
                          human_confirmed=True - never set that programmatically. This
                          mirrors Agents/publishing_agent.md's hard rule: publishing is
                          human-gated, no exceptions, regardless of how automated the rest
                          of the pipeline becomes.

Credentials (never committed - see .gitignore):
    Config/client_secret_*.json   OAuth client (Desktop app type), from Google Cloud Console
    Config/youtube_token.json     Cached OAuth token after the one-time consent flow below

First-time setup (run once per machine):
    python youtube_agent.py auth
This opens a local browser window - YOU log into your own Google account and click Allow.
Claude never sees or enters your credentials; it only reads the resulting token file.

Scopes requested: youtube.upload (video uploads) + youtube (channel/playlist/thumbnail
management) - the two together cover everything "manage the channel" needs.

Usage:
    python youtube_agent.py auth
    python youtube_agent.py channel-info
    python youtube_agent.py upload <video_file> <title> <description> <tags_csv> [--category ID] [--thumbnail PATH]
    python youtube_agent.py set-thumbnail <video_id> <thumbnail_file>
    python youtube_agent.py list-uploads [--max N]
    python youtube_agent.py update-metadata <video_id> [--title T] [--description D] [--tags CSV] [--category ID]
    python youtube_agent.py list-playlists
    python youtube_agent.py get-or-create-playlist "<title>" [--description D]
    python youtube_agent.py add-to-playlist <playlist_id> <video_id>
    python youtube_agent.py publish <video_id> --confirm [--at ISO_TIMESTAMP]
    python youtube_agent.py comment <video_id> <text>
    python youtube_agent.py analytics <video_id> --start YYYY-MM-DD --end YYYY-MM-DD
"""
import argparse
import glob
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",  # required for commentThreads.insert
    "https://www.googleapis.com/auth/yt-analytics.readonly",  # required for the Analytics API (views, retention, CTR)
]

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_DIR = os.path.join(REPO, "ProductionStudio", "Config")
TOKEN_PATH = os.path.join(CONFIG_DIR, "youtube_token.json")

DEFAULT_CATEGORY_ID = "24"  # Entertainment - see https://developers.google.com/youtube/v3/docs/videoCategories/list

# Every video and Short description must end with this line (added 2026-07-26, after a real
# viewer commented on a Short asking which channel it was from). SEO Agent / Shorts Agent must
# append it when writing Description text - not enforced automatically by prepare_upload(),
# since the exact placement (end of description, after hashtags, etc.) is a content decision.
CHANNEL_FOOTER = "Fatal Affairs — subscribe for more true crime cases: https://www.youtube.com/@fatalaffairs-f1i"


def _find_client_secret_file():
    matches = glob.glob(os.path.join(CONFIG_DIR, "client_secret_*.json"))
    if not matches:
        raise SystemExit(
            f"No client_secret_*.json found in {CONFIG_DIR}. "
            "Download the OAuth client (Desktop app type) from Google Cloud Console first."
        )
    return matches[0]


def get_authenticated_service():
    """Loads cached credentials, refreshing if expired. Raises with clear instructions
    if no token exists yet - run `python youtube_agent.py auth` first."""
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, "w", encoding="utf-8") as f:
            f.write(creds.to_json())

    if not creds or not creds.valid:
        raise SystemExit(
            "No valid YouTube credentials found. Run `python youtube_agent.py auth` first "
            "- this opens a browser for you to log into your own Google account."
        )

    return build("youtube", "v3", credentials=creds)


def get_analytics_service():
    """Same cached credentials as get_authenticated_service(), but builds the
    separate YouTube Analytics API v2 service (different API surface: reports.query,
    not videos/playlists). Requires the yt-analytics.readonly scope - see SCOPES."""
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, "w", encoding="utf-8") as f:
            f.write(creds.to_json())
    if not creds or not creds.valid:
        raise SystemExit(
            "No valid YouTube credentials found. Run `python youtube_agent.py auth` first."
        )
    return build("youtubeAnalytics", "v2", credentials=creds)


def video_analytics(video_id, start_date, end_date):
    """Real per-video performance: views, watch time, average view duration/percentage -
    none of this is available from videos().list(part='statistics'), which only has
    views/likes/comments. Dates are 'YYYY-MM-DD' strings. Returns a dict of
    metric -> value, or None values if YouTube has no data yet for this video/range.

    Note: impressions/impressionsClickThroughRate (thumbnail CTR) were tried and
    rejected by this account's API access with 'Unknown identifier (impressions)' -
    that metric pair isn't queryable via this reports().query() shape on this
    channel/product tier, so it's deliberately left out rather than silently
    retried/masked. If thumbnail CTR data is needed later, check YouTube Studio's
    own Analytics tab directly (it has real CTR per video) rather than assuming
    the API gap can be worked around here."""
    analytics = get_analytics_service()
    metrics = "views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage"
    resp = analytics.reports().query(
        ids="channel==MINE",
        startDate=start_date,
        endDate=end_date,
        metrics=metrics,
        dimensions="video",
        filters=f"video=={video_id}",
    ).execute()
    headers = [h["name"] for h in resp.get("columnHeaders", [])]
    rows = resp.get("rows", [])
    if not rows:
        return {m: None for m in metrics.split(",")}
    row = rows[0]
    return dict(zip(headers, row))


def cmd_auth():
    """One-time interactive OAuth consent flow. Opens a local browser window - the
    channel owner logs in and clicks Allow themselves. Writes the resulting token
    (including refresh token) to Config/youtube_token.json."""
    client_secret_file = _find_client_secret_file()
    flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(TOKEN_PATH, "w", encoding="utf-8") as f:
        f.write(creds.to_json())
    print(f"Authorized. Token saved to {TOKEN_PATH}")


def cmd_channel_info():
    """Read-only sanity check that the OAuth token actually works."""
    yt = get_authenticated_service()
    resp = yt.channels().list(part="snippet,statistics", mine=True).execute()
    for ch in resp.get("items", []):
        snippet = ch["snippet"]
        stats = ch["statistics"]
        print(f"Channel: {snippet['title']} ({ch['id']})")
        print(f"  Subscribers: {stats.get('subscriberCount', '?')}")
        print(f"  Videos: {stats.get('videoCount', '?')}")
        print(f"  Views: {stats.get('viewCount', '?')}")


def prepare_upload(video_file, title, description, tags, category_id=DEFAULT_CATEGORY_ID,
                    thumbnail_file=None):
    """Uploads the video as PRIVATE with full metadata. Returns the video_id (the
    "draft_id" from youtube_publish_tool.md's contract) - nothing is public yet.
    Safe to call without a human-confirmation gate: a private, unlisted-to-everyone-
    but-the-owner upload is reversible and not a publish action."""
    yt = get_authenticated_service()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id,
        },
        "status": {
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(video_file, chunksize=-1, resumable=True, mimetype="video/mp4")
    request = yt.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  uploaded {int(status.progress() * 100)}%")

    video_id = response["id"]
    print(f"Uploaded as PRIVATE draft: video_id={video_id}")

    if thumbnail_file:
        set_thumbnail(video_id, thumbnail_file)

    return video_id


def set_thumbnail(video_id, thumbnail_file):
    yt = get_authenticated_service()
    yt.thumbnails().set(videoId=video_id, media_body=MediaFileUpload(thumbnail_file)).execute()
    print(f"Thumbnail set for {video_id}")


def update_metadata(video_id, title=None, description=None, tags=None, category_id=None):
    """Edits title/description/tags/category on an existing video, public or not.
    Only the fields passed are changed - existing snippet fields are preserved.
    Not gated behind human_confirmed: editing the title of an ALREADY-public video is a
    much smaller, easily-reversible action than the initial publish decision, but it does
    modify public-facing content, so Claude must still only call this after the channel
    owner has said what the new text should be in the current session - never invent or
    apply wording on its own initiative."""
    yt = get_authenticated_service()
    current = yt.videos().list(part="snippet", id=video_id).execute()
    if not current["items"]:
        raise SystemExit(f"No video found with id {video_id}")
    snippet = current["items"][0]["snippet"]

    if title is not None:
        snippet["title"] = title
    if description is not None:
        snippet["description"] = description
    if tags is not None:
        snippet["tags"] = tags
    if category_id is not None:
        snippet["categoryId"] = category_id

    yt.videos().update(part="snippet", body={"id": video_id, "snippet": snippet}).execute()
    line = f"Updated metadata for {video_id}: title={snippet['title']!r}"
    print(line.encode("ascii", "replace").decode("ascii"))


def list_uploads(max_results=10):
    """Read-only: lists the channel's most recent uploads (any privacy status)."""
    yt = get_authenticated_service()
    ch = yt.channels().list(part="contentDetails", mine=True).execute()
    uploads_playlist = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    resp = yt.playlistItems().list(
        part="snippet,status", playlistId=uploads_playlist, maxResults=max_results
    ).execute()
    for item in resp.get("items", []):
        s = item["snippet"]
        line = f"{s['resourceId']['videoId']}  {s['title']}  (published {s['publishedAt']})"
        print(line.encode("ascii", "replace").decode("ascii"))


def confirm_publish(video_id, human_confirmed=False, privacy_status="public", publish_at=None):
    """THE ONLY function in this module that makes a video visible to anyone besides the
    channel owner. Per Agents/publishing_agent.md's hard rule, this requires an explicit
    human go-ahead EVERY time - human_confirmed must be True, and that must come from a
    real "yes, publish this" in the current chat session, never set programmatically or
    inferred. If publish_at is given (ISO 8601, e.g. "2026-08-01T15:00:00Z"), the video is
    scheduled instead of published immediately (YouTube requires privacyStatus="private"
    plus a future publishAt for scheduling)."""
    if not human_confirmed:
        raise SystemExit(
            "Refusing to publish: human_confirmed=True was not passed. This call must "
            "only happen after the channel owner explicitly said to publish this specific "
            "video in the current session - see Agents/publishing_agent.md."
        )

    yt = get_authenticated_service()
    status = {"privacyStatus": "private" if publish_at else privacy_status}
    if publish_at:
        status["publishAt"] = publish_at

    yt.videos().update(part="status", body={"id": video_id, "status": status}).execute()
    if publish_at:
        print(f"Scheduled {video_id} to publish at {publish_at}")
    else:
        print(f"Published {video_id} as {privacy_status}")


def post_comment(video_id, text):
    """Posts a single top-level comment on a video/Short as the channel owner (the
    authenticated account). Per the channel owner's 2026-07-31 instruction, every
    publish should leave the pre-drafted `pinned_comment` from SEO.md/Shorts.md under
    the video - closing a real gap where that field was always written but never
    actually posted.

    IMPORTANT LIMITATION: the YouTube Data API v3 has no endpoint to pin a comment.
    commentThreads.insert can only post it; making it the pinned top comment is a
    channel-owner-only action in YouTube Studio's own UI (click the comment's ... menu
    -> Pin). This function posts the comment - it does not and cannot pin it. If you
    want it pinned, do that manually in Studio after publish; there is no API
    workaround (scraping the Studio web UI would be fragile and outside the API's
    terms, so this tool deliberately does not attempt it)."""
    yt = get_authenticated_service()
    body = {
        "snippet": {
            "videoId": video_id,
            "topLevelComment": {"snippet": {"textOriginal": text}},
        }
    }
    resp = yt.commentThreads().insert(part="snippet", body=body).execute()
    comment_id = resp["id"]
    print(f"Posted comment {comment_id} on {video_id} (not pinned - pin manually in Studio if wanted)")
    return comment_id


def delete_comment(comment_id):
    """Deletes a comment (only works on comments this channel's own account posted or
    otherwise has moderation rights over)."""
    yt = get_authenticated_service()
    yt.comments().delete(id=comment_id).execute()
    print(f"Deleted comment {comment_id}")


def list_playlists():
    """Read-only: lists the channel's existing playlists."""
    yt = get_authenticated_service()
    resp = yt.playlists().list(part="snippet", mine=True, maxResults=50).execute()
    for pl in resp.get("items", []):
        title = pl["snippet"]["title"].encode("ascii", "replace").decode("ascii")
        print(pl["id"], " ", title)


def find_playlist_by_title(title):
    yt = get_authenticated_service()
    resp = yt.playlists().list(part="snippet", mine=True, maxResults=50).execute()
    for pl in resp.get("items", []):
        if pl["snippet"]["title"] == title:
            return pl["id"]
    return None


def get_or_create_playlist(title, description=""):
    """Idempotent: returns the existing playlist's id if one with this exact title
    already exists, otherwise creates a new public playlist. Safe to call every time a
    new video in a given case/theme is published - never creates a duplicate playlist."""
    existing = find_playlist_by_title(title)
    if existing:
        return existing

    yt = get_authenticated_service()
    body = {
        "snippet": {"title": title, "description": description},
        "status": {"privacyStatus": "public"},
    }
    resp = yt.playlists().insert(part="snippet,status", body=body).execute()
    print(f"Created playlist {resp['id']}: {title}")
    return resp["id"]


def add_video_to_playlist(playlist_id, video_id):
    """Idempotent-ish: YouTube allows the same video in a playlist only once in practice
    for this use case, but we don't de-dupe here - check with list_playlist_items first
    if calling this in a loop across repeated runs."""
    yt = get_authenticated_service()
    body = {
        "snippet": {
            "playlistId": playlist_id,
            "resourceId": {"kind": "youtube#video", "videoId": video_id},
        }
    }
    yt.playlistItems().insert(part="snippet", body=body).execute()
    print(f"Added {video_id} to playlist {playlist_id}")


def delete_playlist(playlist_id):
    """Removes a playlist. Does NOT delete the videos in it - only the grouping."""
    yt = get_authenticated_service()
    yt.playlists().delete(id=playlist_id).execute()
    print(f"Deleted playlist {playlist_id}")


def list_playlist_items(playlist_id):
    yt = get_authenticated_service()
    resp = yt.playlistItems().list(part="snippet", playlistId=playlist_id, maxResults=50).execute()
    return [item["snippet"]["resourceId"]["videoId"] for item in resp.get("items", [])]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("auth")
    sub.add_parser("channel-info")

    p_upload = sub.add_parser("upload")
    p_upload.add_argument("video_file")
    p_upload.add_argument("title")
    p_upload.add_argument("description")
    p_upload.add_argument("tags_csv")
    p_upload.add_argument("--category", default=DEFAULT_CATEGORY_ID)
    p_upload.add_argument("--thumbnail", default=None)

    p_thumb = sub.add_parser("set-thumbnail")
    p_thumb.add_argument("video_id")
    p_thumb.add_argument("thumbnail_file")

    p_list = sub.add_parser("list-uploads")
    p_list.add_argument("--max", type=int, default=10)

    p_meta = sub.add_parser("update-metadata")
    p_meta.add_argument("video_id")
    p_meta.add_argument("--title", default=None)
    p_meta.add_argument("--description", default=None)
    p_meta.add_argument("--tags", default=None, help="comma-separated")
    p_meta.add_argument("--category", default=None)

    sub.add_parser("list-playlists")

    p_getplaylist = sub.add_parser("get-or-create-playlist")
    p_getplaylist.add_argument("title")
    p_getplaylist.add_argument("--description", default="")

    p_addplaylist = sub.add_parser("add-to-playlist")
    p_addplaylist.add_argument("playlist_id")
    p_addplaylist.add_argument("video_id")

    p_delplaylist = sub.add_parser("delete-playlist")
    p_delplaylist.add_argument("playlist_id")

    p_publish = sub.add_parser("publish")
    p_publish.add_argument("video_id")
    p_publish.add_argument("--confirm", action="store_true",
                            help="Required. Only pass this after the channel owner explicitly said to publish.")
    p_publish.add_argument("--privacy", default="public")
    p_publish.add_argument("--at", default=None, help="ISO 8601 timestamp to schedule instead of publishing now")

    p_comment = sub.add_parser("comment")
    p_comment.add_argument("video_id")
    p_comment.add_argument("text")

    p_analytics = sub.add_parser("analytics")
    p_analytics.add_argument("video_id")
    p_analytics.add_argument("--start", required=True, help="YYYY-MM-DD")
    p_analytics.add_argument("--end", required=True, help="YYYY-MM-DD")

    args = parser.parse_args()

    if args.cmd == "auth":
        cmd_auth()
    elif args.cmd == "channel-info":
        cmd_channel_info()
    elif args.cmd == "upload":
        tags = [t.strip() for t in args.tags_csv.split(",") if t.strip()]
        prepare_upload(args.video_file, args.title, args.description, tags,
                        category_id=args.category, thumbnail_file=args.thumbnail)
    elif args.cmd == "set-thumbnail":
        set_thumbnail(args.video_id, args.thumbnail_file)
    elif args.cmd == "list-uploads":
        list_uploads(max_results=args.max)
    elif args.cmd == "update-metadata":
        tags = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else None
        update_metadata(args.video_id, title=args.title, description=args.description,
                         tags=tags, category_id=args.category)
    elif args.cmd == "list-playlists":
        list_playlists()
    elif args.cmd == "get-or-create-playlist":
        get_or_create_playlist(args.title, description=args.description)
    elif args.cmd == "add-to-playlist":
        add_video_to_playlist(args.playlist_id, args.video_id)
    elif args.cmd == "delete-playlist":
        delete_playlist(args.playlist_id)
    elif args.cmd == "publish":
        confirm_publish(args.video_id, human_confirmed=args.confirm,
                         privacy_status=args.privacy, publish_at=args.at)
    elif args.cmd == "comment":
        post_comment(args.video_id, args.text)
    elif args.cmd == "analytics":
        result = video_analytics(args.video_id, args.start, args.end)
        for k, v in result.items():
            print(f"  {k}: {v}")
