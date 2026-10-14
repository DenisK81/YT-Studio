# Channel Analytics Tool

**Added:** 2026-10-14. **Implementation:** `Workflows/channel_analytics_report.py`. **Read-only.**

## What it does

One command that answers "where do our views come from, and which Short patterns work", from the
real YouTube Data API + YouTube Analytics API numbers for the channel's own uploads:

```
python Workflows/channel_analytics_report.py --start 2026-07-01 --end 2026-10-14 [--json out.json]
```

Output (stdout, Markdown-like): channel totals, traffic-source split, Shorts vs long-form medians
(views, average view duration/percentage, minutes watched, subscribers gained), the correlation
between retention and reach for Shorts, title-pattern medians (verdict/sentence, number in title,
"911/call", camera/video, quotation marks, victim-first vs perpetrator-first), Shorts by publish
month, and the top 10 Shorts.

## Limits (real, not bugs)

The API does NOT expose thumbnail impressions, click-through rate, or the per-Short "stayed to watch
vs swiped away" split (see `youtube_agent.video_analytics`). Those exist only in YouTube Studio:
Analytics -> Advanced mode -> Content report -> filter "Shorts" (the owner exported this on
2026-10-14: 15 Shorts, 6,041 thumbnail impressions, 0.9% CTR). The channel-level "stayed to watch /
swiped away" split is on Studio's Content tab -> "How viewers engaged" (30.1% / 69.9% for the
28 days to 2026-10-12). Read both by hand next to this report.

## When to run

At the start of each batch (before choosing the Short hook style) and 7 days after any A/B test
batch. Compare each variant's median against the median of the previous 20 Shorts, not against the
all-time median (the channel is growing: the October median was 139 vs ~30 earlier).
