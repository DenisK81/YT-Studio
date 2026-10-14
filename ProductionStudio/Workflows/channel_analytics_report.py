"""Channel analytics report: one command that answers 'where do our views come from and
which Shorts patterns work', using only real YouTube Data / Analytics API numbers.

Built 2026-10-14 from the ad-hoc queries run during the adjacent-niche analytics pass
(see Documentation/TREND_LOG.md, entry 2026-10-14). Read-only: it never writes to the channel.

Usage:
    python channel_analytics_report.py [--start YYYY-MM-DD] [--end YYYY-MM-DD] [--json OUT.json]

What the API CANNOT give (documented in youtube_agent.video_analytics): thumbnail impressions,
click-through rate, and the per-Short 'stayed to watch vs swiped away' split. Those live only in
YouTube Studio -> Analytics -> Advanced mode (Content report, filter 'Shorts'); export the CSV by
hand and read it next to this report.
"""
import argparse
import datetime as dt
import json
import math
import os
import re
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from youtube_agent import get_authenticated_service, get_analytics_service  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SHORT_MAX_SECONDS = 120
PATTERNS = {
    "verdict/sentence/guilty/life/years": r"verdict|sentenc|guilty|life without|years|jury|judge|prison",
    "number in title": r"\d",
    "911/call/phone/text/message": r"911|call|text|phone|message|voicemail|sext",
    "camera/video/footage/recorded": r"camera|video|footage|recorded|stream|photo|bodycam|surveillance",
    "quotation marks": r"[\"“”']",
    "victim-first (her/she)": r"\b(her|she)\b",
    "perpetrator-first (his/he)": r"\b(his|he)\b",
}


def _secs(iso):
    m = re.match(r"PT(?:(\d+)M)?(?:(\d+)S)?", iso)
    return int(m.group(1) or 0) * 60 + int(m.group(2) or 0)


def list_public_videos(yt):
    up = yt.channels().list(part="contentDetails", mine=True).execute()["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, tok = [], None
    while True:
        p = yt.playlistItems().list(part="contentDetails", playlistId=up, maxResults=50, pageToken=tok).execute()
        ids += [i["contentDetails"]["videoId"] for i in p["items"]]
        tok = p.get("nextPageToken")
        if not tok:
            break
    out = {}
    for k in range(0, len(ids), 50):
        for v in yt.videos().list(part="snippet,statistics,contentDetails,status", id=",".join(ids[k:k + 50])).execute()["items"]:
            if v["status"]["privacyStatus"] != "public":
                continue
            out[v["id"]] = dict(id=v["id"], title=v["snippet"]["title"], pub=v["snippet"]["publishedAt"][:10],
                                dur=_secs(v["contentDetails"]["duration"]), views_total=int(v["statistics"].get("viewCount", 0)))
    return out


def report(start, end, json_out=None):
    yt = get_authenticated_service()
    an = get_analytics_service()
    vids = list_public_videos(yt)

    def q(**kw):
        r = an.reports().query(ids="channel==MINE", startDate=start, endDate=end, **kw).execute()
        return [c["name"] for c in r.get("columnHeaders", [])], r.get("rows", [])

    h, r = q(metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost,likes,comments,shares")
    totals = dict(zip(h, r[0])) if r else {}
    _, traffic = q(metrics="views,estimatedMinutesWatched", dimensions="insightTrafficSourceType", sort="-views")
    h, rows = q(metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,likes,shares",
                dimensions="video", sort="-views", maxResults=200)
    per = []
    for row in rows:
        d = dict(zip(h, row))
        v = vids.get(d["video"])
        if v:
            d.update(title=v["title"], dur=v["dur"], pub=v["pub"])
            per.append(d)
    shorts = [d for d in per if d["dur"] < SHORT_MAX_SECONDS]
    mains = [d for d in per if d["dur"] >= SHORT_MAX_SECONDS]

    def med(lst, k):
        return round(st.median([d[k] for d in lst]), 1) if lst else 0

    print(f"# Channel analytics {start} -> {end}")
    print(f"Totals: {totals}")
    tv = sum(t[1] for t in traffic) or 1
    print("\n## Traffic sources")
    for src, views, minutes in traffic:
        print(f"- {src}: {views} views ({100 * views / tv:.1f}%), {minutes} min")
    print("\n## Shorts vs long-form")
    for name, lst in (("Shorts", shorts), ("Long-form", mains)):
        print(f"- {name}: n={len(lst)}, median views={med(lst, 'views')}, avg view duration={med(lst, 'averageViewDuration')} s, "
              f"avg view %={med(lst, 'averageViewPercentage')}, minutes={sum(d['estimatedMinutesWatched'] for d in lst)}, "
              f"subscribers gained={sum(d['subscribersGained'] for d in lst)}")
    if len(shorts) > 3:
        xs = [d["averageViewPercentage"] for d in shorts]
        ys = [math.log10(d["views"] + 1) for d in shorts]
        mx, my = st.mean(xs), st.mean(ys)
        den = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)) or 1
        print(f"- corr(avg view %, log10 views) over Shorts = {sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den:.2f} "
              "(near 0 means retention is not what drives reach)")
    print("\n## Title patterns (Shorts, median views in vs out)")
    for name, pat in PATTERNS.items():
        a = [d["views"] for d in shorts if re.search(pat, d["title"], re.I)]
        b = [d["views"] for d in shorts if not re.search(pat, d["title"], re.I)]
        if a and b:
            print(f"- {name}: in n={len(a)} median={st.median(a):.0f} | out n={len(b)} median={st.median(b):.0f}")
    print("\n## Shorts by publish month (median / mean views)")
    byv = {}
    for d in shorts:
        byv.setdefault(d["pub"][:7], []).append(d["views"])
    for k in sorted(byv):
        print(f"- {k}: n={len(byv[k])} median={st.median(byv[k]):.0f} mean={st.mean(byv[k]):.0f}")
    print("\n## Top 10 Shorts")
    for d in sorted(shorts, key=lambda d: -d["views"])[:10]:
        print(f"- {d['views']:5d} views, {d['averageViewPercentage']:.0f}% viewed, {d['dur']}s  {d['title'][:70]}")
    if json_out:
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump({"start": start, "end": end, "totals": totals, "traffic": traffic, "videos": per}, f, ensure_ascii=False, indent=2)
        print(f"\nJSON written to {json_out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", default="2026-07-01")
    ap.add_argument("--end", default=dt.date.today().isoformat())
    ap.add_argument("--json", default=None)
    a = ap.parse_args()
    report(a.start, a.end, a.json)
