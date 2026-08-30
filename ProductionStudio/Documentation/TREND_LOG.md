# Trend Log

Persistent, cross-case memory of real trend research — distinct from `Templates/SuccessRules.md`
(which tracks THIS channel's own retro data per video). This file tracks the outside world:
what's working across the true-crime genre right now, on YouTube itself and on Reddit/X/other
platforms where true-crime audiences congregate. Started 2026-07-26 after the channel owner
asked for ongoing trend-tracking to inform growth, not just a one-off per-case search.

## Why a separate file from Research Agent's per-case `genre_trend_notes`
`genre_trend_notes` (see `Agents/research_agent.md`) is real, but it's re-derived fresh on every
run and thrown away afterward — nothing compounds across cases. This file is where real findings
get appended over time, so patterns become visible (e.g. "thumbnail CTR gap has come up in 3
separate research passes now") instead of being rediscovered/re-searched from scratch each time.

## Sources to check (broadened 2026-07-26 per explicit request — not just generic web search)
- YouTube itself: what's actually ranking/trending in true crime search and recommendations
  right now (real search, not assumption).
- Reddit: r/TrueCrime, r/UnresolvedMysteries, r/TrueCrimeDiscussion — audience sentiment and
  what cases/formats people are actively discussing (leads/signal, never fact-citation — see
  `Agents/research_agent.md`'s existing rule, unchanged).
- X/Twitter: true-crime commentary accounts, breaking-case discussion threads.
- Direct competitor-channel observation: what similar-sized/larger true-crime channels are
  actually publishing, titling, and thumbnailing right now.

## Format per entry
```
### {date} — {what was checked}
- Finding: {the actual trend/data point, with source}
- Why it matters for this channel: {concrete implication}
- Action taken / to take: {what changed as a result, if anything}
```

---

### 2026-07-26 — Initial real-search pass (competitor/format/platform-risk research)

- **Finding:** True crime is one of YouTube's three highest-RPM niches in 2026 ($4-$12 per 1,000
  views), with one case told chronologically in 15-25 minutes as the backbone format of most
  successful channels. Long-form documentary-style content is dominating the 2026 algorithm;
  faceless channels perform exceptionally well in this niche specifically.
  — Why it matters: this channel's existing format (single-case, ~11-15 min, faceless/AI-visual
    documentary) already matches the format that's winning, not something to change.
  — Action: none needed, current format validated by real data, not just internal preference.

- **Finding:** English-speaking true-crime audiences are saturated on US cases; international
  and lesser-known cases (Brazil, Japan, Eastern Europe, etc.) are the fastest-growing corner of
  the niche as of 2026.
  — Why it matters: all 4 cases produced so far (Molly Watson, Banfield, Kouri Richins, Monica
    Sementilli) are US cases. This is a real, concrete growth lever not yet tried.
  — Action: **Research Agent should actively surface at least one non-US candidate in its next
    "find next case" discovery run**, not just default to US DOJ/AG press releases.

- **Finding:** The revenue/subscriber-growth gap between high-CTR and low-CTR true-crime channels
  is measurable and driven specifically by thumbnail design quality.
  — Why it matters: reinforces treating `Agents/thumbnail_agent.md`'s output as a real growth
    lever, not a formality — worth periodically A/B-checking thumbnail concepts against what's
    getting clicks on comparable channels.
  — Action: none yet — flagging as an area to watch, not a process change today.

- **Finding:** YouTube's January 2026 enforcement wave specifically targets "AI slop" (mass-
  produced, template-based AI content judged to add no original insight) under a three-strike
  system (warning → 90-day Partner Program suspension → permanent removal). Separately, YouTube
  now requires creators to disclose "altered or synthetic" realistic AI content at upload time.
  — Why it matters: direct platform-survival risk for a studio that generates most of its
    imagery with AI. This is the concrete reason real photos became mandatory (see
    `Documentation/ARCHITECTURE.md`) rather than just a stylistic preference.
  — Action: real-photo sourcing made mandatory per case; synthetic-content disclosure check
    added to `Agents/quality_control_agent.md`'s pre-publish checklist. Both done 2026-07-26.

### 2026-07-28 — Archival-material usage, cold opens, and interactivity (prompted by real QC feedback on the Rimoni Muliaga video)

- **Finding:** Successful true-crime channels (PoliceActivity, Law&Crime BodyCam, Grizzly True
  Crime, That Chapter) lean much harder into raw archival material than this channel currently
  does — full bodycam footage, press-conference clips, and court documents shown directly on
  screen, not just still photos mixed into otherwise AI-generated scenes. [PoliceActivity](https://en.wikipedia.org/wiki/PoliceActivity),
  [Law&Crime BodyCam](https://blog.jellysmack.com/real-crime-raw-footage-new-lawcrime-channel-bodycam-launches-on-youtube/)
  — Why it matters: this channel's current real-photo mandate (2-3 still photos per case) is a
    floor, not the ceiling other channels operate at — there is real room to lean further into
    archival material as a differentiator, not just a compliance minimum.
  — Action: **escalated 2026-08-30** from "flag for a future case" to a standing sourcing
    priority, per explicit channel-owner instruction after a real channel-performance audit:
    real archival video clip > real photo > AI generation, generation only for genuine gaps.
    `Tools/mugshot_fetch_tool.md` gained a Track 3 (archival video clips) and
    `Tools/remotion_assembly_tool.md` gained a `SceneClip` component to play one in the timeline.
    Not yet exercised on a real case — the next case is the real test.

- **Finding:** Long/animated channel intros measurably hurt retention (~22% average boost in
  30-second retention after channels removed them), but true-crime viewers specifically reward a
  short, consistent, dramatic **cold-open teaser** of the case's most striking moment ahead of a
  brief channel bumper — a distinct thing from a long branded intro. [YT SEO Architect](https://yt-seo-architect.vercel.app/blog/youtube-intro-hook-first-3-seconds),
  [1of10](https://1of10.com/blog/how-to-hook-viewers-in-the-first-30-seconds-of-a-youtube-video/)
  — Why it matters: directly answers the channel owner's 2026-07-28 feedback that videos "start
    immediately" and "look raw" — the fix is very likely a short (2-3s) bumper and/or a
    distinct cold-open teaser ahead of the existing Hook beat, NOT a return to a long animated
    intro (which the data says would hurt, not help).
  — Action: channel owner chose the short branded stinger over the teaser-with-backstory
    alternative. Built the same day — `src/ChannelBumper.tsx` (2.5s, brand title card + a real
    generated sting sound), reused unchanged across every future video, prepended ahead of the
    Hook beat. See `Tools/remotion_assembly_tool.md`'s "Channel intro bumper" section for the
    implementation. Not applied retroactively to the already-published Rimoni Muliaga video.

- **Finding:** Visual-format variety (crime-scene/location maps, on-screen timelines, pull-quote
  cards) measurably boosts retention (one cited figure: ~35% from map graphics specifically) and
  is recommended at 5-7 distinct visual element types per video — not just narrated photos panned
  end to end. [Subscribr niche-ideas roundup](https://subscribr.ai/p/true-crime-youtube-niche-ideas)
  — Why it matters: this channel's videos are currently one visual format (Ken-Burns-panned
    still photo per scene) for the entire runtime — likely what read as "raw" / lacking
    "interactivity" in the 2026-07-28 feedback, more than a literal request for YouTube polls.
  — Action: **escalated 2026-08-30 from "future-case test" to mandatory, after a real channel
    audit** (8 subscribers, 78 public videos, main-video average-view-percentage 28-36% on a real
    sample) found evidence consistent with this hypothesis. Built `PullQuoteCard.tsx` (ready to
    use — a real-quote card, second visual format) and `SceneClip.tsx` (plays a real archival
    clip, see the entry above). A map/timeline graphic remains unbuilt — needs real per-case
    content to design against, build when a case's story calls for one. Every case forward must
    use at least one non-`SceneImage` format.

### 2026-08-30 — Real channel-performance audit (first one done against actual YouTube Analytics data, not just outside-world trend research)

- **Finding:** 8 subscribers, 4,836 total views across 78 public videos, channel 7 weeks old.
  Views/day (age-normalized) range from 0.03 to 49 across videos — a 1000x+ spread, meaning most
  videos get near-zero organic distribution and a small handful get algorithmically picked up.
  Shorts outperform main videos ~2.8x on a views/day basis (4.84 vs 1.73).
  — Why it matters: this is genuine cold-start/discovery-stage behavior, not an "algorithm
    problem" to solve with a trick — the channel doesn't yet have enough subscriber/interaction
    signal for consistent organic reach. Growth levers matter, but expect a wide variance floor
    at this stage regardless.
  — Action: confirmed Shorts are the stronger current lever, reinforcing the existing 4-Shorts-
    per-case cadence. Two early videos found mistagged (short-duration but missing `#shorts` in
    title, likely hurting Shorts-feed placement) — fixed same day. Real per-video retention
    pulled via `video_analytics()` for a sample: main videos averaged 28-36% view-percentage,
    feeding directly into the visual-variety escalation above.
  — Also found: one stray non-case video ("Renovation," 44s, 3 views, off-brand title) uploaded
    near channel launch — flagged to the channel owner, who is reviewing it themselves.
  — Real thumbnail CTR (impressions/impressionsClickThroughRate) is **not queryable via the
    YouTube Analytics API on this account's tier** — confirmed in `video_analytics()`'s own code
    comment, re-confirmed this pass. Only available in YouTube Studio's own Analytics UI
    directly — the channel owner is checking this manually going forward, not automatable here.

### Suggested cadence
Re-run this research pass at the start of each new case's discovery step at minimum (feeds
Research Agent's `genre_trend_notes` for that case), and do a dedicated "just trends, no specific
case" pass every 5-10 videos to catch platform-policy or format shifts between cases. No
automated/scheduled version of this exists yet — it's a manual step until the channel owner
decides Phase 1 is ready to schedule it (see CLAUDE.md's Phase 1/2 boundary).
