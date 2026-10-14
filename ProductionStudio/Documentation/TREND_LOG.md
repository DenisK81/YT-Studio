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

### 2026-09-15 — Real channel-performance audit #2 (16 days after the 2026-08-30 audit, 5 cases later)

- **Finding:** 8 subscribers, 6,191 total views, 100 public videos. Compared to the 2026-08-30
  audit (8 subscribers, 4,836 views, 78 videos): **+22 videos, +1,355 views, +0 net subscribers**
  in 16 days. `subscribersGained`/`subscribersLost` for the 2026-08-30→2026-09-15 window queried
  directly: exactly 0 and 0. This is a hard stall, not a slowdown — every fix shipped since the
  last audit (real-photo mandate, `ChannelBumper`, `PullQuoteCard` visual variety, the UK/Scotland
  international-case angle tried on Thompson/Buchanan/Isaacs/Greer) produced zero measurable
  subscriber conversion in this window.
  — Why it matters: the prior audit's framing ("cold-start variance, not an algorithm problem")
    needs re-checking — 5 cases and 3 concrete fixes with a flat subscriber line is a longer
    trend now, not a single noisy data point.
- **Finding:** `insightTrafficSourceType` breakdown (whole-channel, 2026-06-01 to 2026-09-15):
  SHORTS 5,431 views (87.3%), YT_SEARCH 380, RELATED_VIDEO 116, NOTIFICATION 83, YT_CHANNEL 57,
  YT_OTHER_PAGE 52, SUBSCRIBER 40, all others <10 each.
  — Why it matters: main long-form videos get almost no traffic from any source — not just low
    totals, only 116 views channel-wide ever came from Shorts→related-video click-through, which
    is the mechanism the 4-Shorts-per-case cadence is implicitly betting on to drive main-video
    views. That bet is not paying off: per-video main sample this pass (Greer, Ferguson,
    Hildabrand-era, Goodine, Orsini) ranged 1-14 views each, only one main video channel-wide
    (`tbTY_Wz3Tp4`, "He Posed As His Own Wife...", 10:37) has ever broken 50 views (90, with 272
    minutes watched — the single best absolute watch-time performer on the channel).
  — Also found: engagement signal is near-zero channel-wide in this window — 128 likes but only
    4 comments and 0 shares across 6,220 views (2026-06-01 to 2026-09-15) despite every script
    ending on a comment-bait CTA. Even the channel's viral-est Shorts (500-700 views) converted
    0-2 subscribers each.
  — Action: **not yet decided — flagged to channel owner 2026-09-15 for a strategy discussion
    before continuing to produce cases at the same cadence/format.** Candidate levers not yet
    tried: thumbnail CTR is still not API-queryable (same tier limitation as 2026-08-30) and
    still needs a manual YouTube Studio check; title/hook pattern-matching against the small set
    of videos that *did* break out (all are short, punchy, first-person-quote or verdict-reveal
    titles under 8 words — worth testing as a title-writing rule going forward, not yet applied).

### 2026-09-15 — Real competitor-channel research pass (PoliceActivity, Law&Crime BodyCam,
Grizzly True Crime, That Chapter, plus Coffeehouse Crime and a cautionary AI-fabrication case)

- **Finding:** Real footage is table stakes at the top of this niche, not a nice-to-have. The two
  biggest channels researched (PoliceActivity ~6.9M subs, Law&Crime BodyCam) are 100% real bodycam
  footage by definition. Meanwhile "True Crime Case Files" (104 videos, millions of views,
  entirely AI-fabricated script/narration/images with zero disclosure) was publicly exposed by
  Denver Post reporting after a viral 1.8M-view video described a 2014 Colorado murder that never
  happened — no court records, no news coverage, nothing.
  — Why it matters: directly validates this channel's existing real-photo mandate and no-100%-AI
    rule as responding to a real, current, documented failure mode in this exact niche — not
    overcaution.
- **Finding — no evidence of a per-shot "REAL" badge/watermark convention anywhere researched.**
  The pattern that actually recurs across PoliceActivity and Grizzly True Crime is **citing the
  source in the description or on-screen text** (case numbers, court documents, department names,
  "per [outlet]") — channels self-segregate by format (100%-real vs. narrated-with-real-assets)
  rather than labeling individual shots.
  — Why it matters: the `RealBadge` component built the same day (see
    `Tools/remotion_assembly_tool.md`) is worth testing but should NOT be treated as a proven
    competitor tactic — pair it with an actual on-screen source-citation text convention, which
    IS the validated pattern, not just the badge alone.
  — Action: added a source-citation overlay requirement alongside the badge (see
    `Tools/remotion_assembly_tool.md`'s updated "REAL badge overlay" section).
- **Finding:** every channel with confirmed upload-cadence data published weekly or more often at
  their current scale (Coffeehouse Crime weekly, Law&Crime BodyCam weekly+, Grizzly True Crime
  multiple/week in bursts). This channel already publishes far more often than that (100 videos
  in ~2.5 months) — cadence is not the growth bottleneck here, discovery/credibility is.
  — Action: none needed on cadence; ruled out as a lever to pull.
- **Finding:** mid/large narration-driven channels (Coffeehouse Crime ~36 min avg, Grizzly
  frequently 60+ min) run longer than this channel's 11-15 min format.
  — Why it matters: not proof this channel's runtime is wrong for a cold-start channel (shorter
    = faster/cheaper iteration), but worth revisiting once the channel is past pure cold-start.
  — Action: none yet, flagged for a later pass.
- Shorts strategy could not be verified for any researched competitor (channel pages are
  JS-rendered and blocked to this session's web tools) — a real gap in this research pass, not a
  "competitors don't use Shorts" finding. Needs a follow-up pass with direct browser/mobile
  access if Shorts strategy specifically becomes a priority question.

### Suggested cadence
Re-run this research pass at the start of each new case's discovery step at minimum (feeds
Research Agent's `genre_trend_notes` for that case), and do a dedicated "just trends, no specific
case" pass every 5-10 videos to catch platform-policy or format shifts between cases. No
automated/scheduled version of this exists yet — it's a manual step until the channel owner
decides Phase 1 is ready to schedule it (see CLAUDE.md's Phase 1/2 boundary).

## 2026-10-14 - Own-channel analytics pass + adjacent-niche scan

**Source:** YouTube Analytics API (Jul 1 - Oct 14), Studio screenshots from the owner (Overview, Content, Audience, Advanced mode 'Shorts' content report for Sep 15 - Oct 12), and a web scan whose only credible source was Tubular Labs via The Drop (3 Sep 2026).

- **Finding:** 89.7% of views come from the Shorts feed (11,426 of 12,763); search 6.4%; everything else under 1.5%. 118 Shorts have a median of 37.5 views (mean ~105, max 961); 28 long-form videos have a median of 5 and 672 minutes watched in total.
  - Why it matters: long-form is not being distributed at all (viewers who do find it watch ~2 min / 34%), so the cost of a main video (~15 min render + 4 Shorts) buys almost no reach.
  - Action: test, do not conclude. Run the adjacent-niche Shorts test below before reallocating production.
- **Finding:** retention does not drive reach on Shorts (corr(avg view %, log views) = -0.10). 69.9% of viewers swipe away (30.1% stay), channel-wide, 28 days to Oct 12. In the 15-Short Advanced-mode export, thumbnail CTR is 0.9% on 6,041 impressions: the feed does not use the thumbnail, so impressions there are search/browse only.
  - Action: the first second decides; test removing the 1.5 s cold open (variant A).
- **Finding:** audience is 99.5% new viewers, <0.1% regular; +14/-4 subscribers in 105 days (9 of the 14 from Shorts, ~0.07% of views). October Short median 139 vs ~30 earlier (growth is real, retention of people is not).
  - Action: test a subscribe CTA (variant C) instead of 'FULL STORY ON THE CHANNEL', which points at the long video.
- **Finding (title patterns, small n, correlation only):** verdict/sentence/years in title median 80 vs 31; number in title 92 vs 36; '911 / call / text' 20 vs 44 (worse than the rest); victim-first (her/she) 51 vs 36.
- **Finding (market, Tubular Labs):** true-crime YouTube viewership about 10x since early 2023; active channels at scale <100 -> ~3,000; 20-40 min videos capture most views; voiceover-over-bodycam is the most scalable format (100M+ views from a handful of videos in 90 days) but has the lowest engagement. No reliable per-view data was found for scams, cults, heists, wrongful convictions.
- **Open test (started 2026-10-14):** 3 Shorts per variant - control, A (no cold open), C (subscribe CTA), A+C - on the unpublished Corcoran/Rudolph batch; then 3 Shorts each for four adjacent topics (scams/fraud, DNA cold cases, wrongful convictions, heists/escapes) against the previous-20-Shorts median at day 7. Run `Workflows/channel_analytics_report.py`.

## 2026-10-13 - v2 rebuild of six scheduled Shorts (owner decision: 'real photos, a good hook, a subscribe ask, Shorts only')

- **What changed:** Corcoran Shorts 3-4 and Rudolph Shorts 1-4 were re-narrated and re-rendered. The first spoken sentence is now a person in motion or direct speech (e.g. 'A game scout heard a shot... and ran', '"I wanted it out of my sight."'), the 1.5 s cold open is gone where the real photo now IS the first scene (a vertical face-centred crop, not the 16:9 centre crop), and both the spoken outro ('New true crime stories every day. Subscribe.') and the on-screen card ('SUBSCRIBE: NEW TRUE CRIME EVERY DAY') ask for the subscribe.
- **Controls:** Corcoran Shorts 1-2 and the Penney Shorts keep the old cold open and 'FULL STORY ON THE CHANNEL' card. Corcoran Short 4 keeps its cold open (variant C only). Everything is confounded (hook + cold open + CTA change together): read the day-7 result as 'new package vs old package', not per-variable.
- **Measure at day 7:** `python Workflows/channel_analytics_report.py`, plus Studio Advanced mode 'stayed to watch' per Short; compare each Short's views to the median of the previous 20 Shorts.
- **Shorts-only strategy:** next cases are produced as Shorts packs without a long-form main until the day-7 data is in.
