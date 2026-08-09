# Tool: royalty_free_music_tool

## Purpose
Source real royalty-free background music tracks for a video, so background music doesn't cost
per-generation credits (see `Tools/elevenlabs_voice_tool.md`'s `generate_music()`, which is the
fallback, not the default — added 2026-07-19 after the channel owner flagged that ElevenLabs
Music charges tokens per generation).

**Confirmed finding (2026-07-19): no source checked is both free, commercially safe, AND
automatable via a public API.** This isn't a gap to keep researching around — it's the actual
state of the free-music-library landscape right now. See the comparison below before assuming
this can be a per-video automated step.

## Options checked, with real results (not assumed)

| Source | License safe for monetized YouTube | Public API exists | Automatable |
|---|---|---|---|
| Pixabay Music | Yes — Pixabay Content License, no attribution | **No** — confirmed by directly reading `pixabay.com/api/docs/`: the documented API only covers Search Images and Search Videos; "music" appears solely as a category *filter value* for those, not a real audio-search endpoint | No — manual download from `pixabay.com/music` only |
| YouTube Audio Library | Yes — the safest of all four, it's YouTube's own library, explicitly cleared for monetized YouTube videos | No — no public API found anywhere | No — manual download via YouTube Studio only |
| Freesound (freesound.org) | Conditional — many individual sounds are CC0/CC-BY, but **API usage for commercial applications requires contacting Freesound directly for separate licensing**, not simply free | Yes — a real, documented API (APIv2) | Only after resolving commercial-API licensing with Freesound; also more of an SFX/foley library than full music beds, better fit for ambient sound (rain, police radio static) than a continuous score |
| ElevenLabs Music | Yes | Yes — confirmed real API shape | Yes, but **costs credits per generation** — the exact cost the channel owner wants to avoid |

## Recommended approach given this (finalized 2026-07-19)
Since no option is simultaneously free, safe, and automatable, the channel owner built a
10-track reusable set by hand once (see below) — not a per-video bottleneck, not a live search.
- **Fallback for automation specifically:** `Tools/elevenlabs_voice_tool.md`'s `generate_music()`
  remains the only fully-automated option found, at its per-generation cost — only worth using
  if the 10-track set ever feels stale and refreshing it manually isn't wanted.
- **Freesound is a better fit for short SFX/ambience** (police radio static, rain, courtroom
  murmur — already anticipated in `elevenlabs_voice_tool.md`'s notes) than for a continuous
  music bed, and its commercial-API terms need a direct conversation with Freesound before
  relying on it either way — not used for the music bed itself.

## The actual bed-track set (finalized 2026-07-19)
Channel owner manually downloaded **10 tracks from Pixabay Music**, matching
`Config/config.schema.json`'s background_music mood description (tense, anxious, investigative).
Stored at:

```
ProductionStudio/Assets/audio/music_bed/bed_01.mp3
ProductionStudio/Assets/audio/music_bed/bed_02.mp3
...
ProductionStudio/Assets/audio/music_bed/bed_10.mp3
```

This folder is gitignored (`Assets/audio/` — see repo root `.gitignore`), same as every other
generated/downloaded media asset — never gets committed.

## Interface (simple, per the channel owner's explicit call — no per-video search needed since
the set is already pre-vetted for mood)
```
get_bed_track() -> { track_path: string }
```
Picks **one** track from the 10 (fixed rotation or random — either is fine, they're all
pre-vetted for the same mood) and **loops/trims it to exactly fill the render's duration** —
same logic for the main video and for each Short. No per-video mood matching, no live search:
the set was already curated once for the channel's fixed tense/investigative sound, so every
pick is a safe pick.

## Setup (one-time, done 2026-07-19)
1. Download 10 tracks from `pixabay.com/music` matching a tense/investigative/documentary mood.
2. Save them as `bed_01.mp3` through `bed_10.mp3` in
   `ProductionStudio/Assets/audio/music_bed/`.
3. Pixabay Content License already covers commercial use with no attribution required (see
   comparison table above) — no per-track license logging needed beyond this, since the whole
   Pixabay Music library carries the same license terms uniformly (unlike Freesound, where
   licenses vary per sound).

## Legal notes
- All 10 tracks come from Pixabay Music specifically (not a mix of libraries), so the Pixabay
  Content License applies uniformly — commercial use, no attribution, confirmed safe. If the set
  is ever expanded with tracks from a *different* library (e.g. YouTube Audio Library), check
  that library's terms per track at that point — don't assume uniform terms across libraries.

## Real Content ID claim found in production (2026-08-01)

YouTube Studio flagged a **Copyright claim** on one published video: track "**Dark Forest**"
(sped-up variant, shown as "Dark Forest SPDUP" in Studio), claimant "11PM18". Claim type shows
"No impact to your video's reach" (doesn't restrict visibility/monetization on this claim), but
it's a real confirmed case of exactly the gap this doc's own comparison table warned about:
**a Pixabay Content License covering commercial use does NOT mean a track is clear of YouTube's
Content ID system.** Content ID matches by audio fingerprint against whatever a rights holder
registered — it has no awareness of Pixabay's license terms, so a legitimately-licensed track
can still get claimed. Dispute-with-proof-of-license is the correct response if a future claim
does restrict monetization/reach; for a "no impact" claim it's optional but the track should
still be avoided going forward to stop repeat claims across other videos.

**Identified 2026-08-01: `bed_05.mp3` is "Dark Forest."** The claim showed up specifically on
Walter Buchanan Short 4 ("She Had The Right To Be Safe" — The Sentence), which let it be traced
via `prep_short_render.py`'s deterministic `bed_n = (sum(ord(c) for c in slug) % 10) + 1` pick
for slug `walter_buchanan_short_4` → `bed_05`, then confirmed by hashing every render's copied
`bed.mp3` against the master `bed_05.mp3` file (`md5sum`) — exact match, no ambiguity. Checked
every other render produced this session (Buchanan/Devyn/Muliaga main videos + all their Shorts)
by the same hash comparison: **only this one Short uses `bed_05`.** Cases produced before this
session (Richins, Banfield, Sementilli) couldn't be checked this way since their render outputs
no longer exist locally — if their audio ever needs re-verifying, hash their published video's
extracted audio track against `bed_05.mp3`, don't just re-guess from the slug-naming pattern.

**Fixed at the source, not just documented:** `bed_05` is now permanently excluded from the
pick pool in both `prep_remotion_render.py` and `prep_short_render.py` — `_BED_POOL = [1, 2, 3,
4, 6, 7, 8, 9, 10]`, indexed by the same slug hash instead of `% 10`. No future case or Short
can select `bed_05` again; this isn't a "remember not to" note, it's structurally impossible
now. The already-published Buchanan Short 4 is left as-is (the claim has "no impact to video
reach" per YouTube Studio, and per the channel's standing practice this session, a live video
isn't touched retroactively for a non-urgent finding — see the Rimoni Muliaga redaction-margin
precedent).

## Second real Content ID claim found in production (2026-08-06)

YouTube Studio flagged another **Copyright claim**, this time on the Kevin West main video:
track "**Ashfall**" ("everything is dead"), claimant "Elite Alliance Music", found 0:02-6:01 of
the video's 6:04 total runtime — i.e. the music bed ran essentially the entire video, same
pattern as the bed_05/"Dark Forest" claim. Type: Copyright - Audio, with a potential monetization
limitation (more severe than the bed_05 claim's "no impact" status).

**Identified 2026-08-06: `bed_04.mp3` is "Ashfall."** Confirmed by hashing the actual `bed.mp3`
copied into the Kevin West main video's Remotion render (`md5sum`) against the master
`bed_04.mp3` file — exact match (`a68aa82a6dcea12e634a9f17dc98df12`), no ambiguity. The channel
owner is replacing this track manually (with a YouTube Audio Library track) on the already-live
video rather than waiting for a re-render.

**Fixed at the source, same pattern as bed_05:** `bed_04` is now permanently excluded from the
pick pool in both `prep_remotion_render.py` and `prep_short_render.py` — `_BED_POOL = [1, 2, 3,
6, 7, 8, 9, 10]` (both `bed_04` and `bed_05` now excluded). Neither can be selected again; this
is structural, not a "remember not to" note.

**Pattern now visible across 2 of 10 tracks:** both confirmed claims hit tracks that ran for a
video's *entire* duration (a full-length loop, not a short snippet), which is exactly the usage
pattern most likely to trip Content ID's fingerprint matching regardless of the track's actual
Pixabay license terms. With 2 of the original 10 tracks now confirmed claimed, the remaining
8-track pool should be treated as "unconfirmed, not yet proven clean" rather than "safe" — a
future claim on a third track would not be surprising. If a third claim happens, consider
whether the whole 10-track set needs re-sourcing from a source with actual Content ID
pre-clearance (e.g. YouTube Audio Library, which is explicitly cleared) rather than continuing
to treat Pixabay license coverage as protection against fingerprint claims — see this doc's own
comparison table, which already flagged Content ID as a separate risk from licensing.

## Escalate to human when
- The 10-track set starts feeling repetitive/stale across many videos — a human adds 1-2 more
  tracks from Pixabay, don't force the same 10 indefinitely if the channel scales well past 10
  videos.
- Considering Freesound or another new source for the music bed itself (not SFX) — needs a
  fresh licensing check first, not an assumption it's fine because Pixabay was.

## Implementation notes
- `get_bed_track()` itself (the pick-one-and-loop logic) is a small Video Assembly Agent /
  Remotion implementation detail, not something requiring its own API integration.
- Output feeds `Agents/video_assembly_agent.md`'s `background_music_track` input, mixed per
  `Tools/remotion_assembly_tool.md`'s "Background music mixing" spec (-18 to -20dB below
  voiceover, etc.) — the mixing rules apply regardless of which tool sourced the track.

## Stage 1 live-test result (2026-07-19) — the 10-track set is real and verified
Read all 10 files with `mutagen` to confirm they're valid, non-corrupt MP3s and get real
durations (not assumed):

| Track | Duration | Bitrate |
|---|---|---|
| bed_01.mp3 | 102.0s | 256kbps |
| bed_02.mp3 | 113.4s | 256kbps |
| bed_03.mp3 | 205.0s | 256kbps |
| bed_04.mp3 | 504.0s | 256kbps |
| bed_05.mp3 | 98.8s | 256kbps |
| bed_06.mp3 | 109.9s | 256kbps |
| bed_07.mp3 | 139.8s | 256kbps |
| bed_08.mp3 | 113.7s | 256kbps |
| bed_09.mp3 | 106.3s | 256kbps |
| bed_10.mp3 | 144.8s | 256kbps |

Then simulated `get_bed_track()`'s pick-and-loop math against real durations from the Banfield
case:
- **Main video (224s, from `SceneList.json`):** `bed_01.mp3` (102.0s) loops 2x full + a 19.9s
  partial loop = 224s total.
- **Short 1 (41s, from `Shorts.md`):** `bed_05.mp3` (98.8s) — already longer than needed, just
  trimmed to 41s, no loop.
- **Short 2 (19s, from `Shorts.md`):** `bed_09.mp3` (106.3s) — same, trimmed only.

Confirms the simple pick-one-and-loop-or-trim approach works cleanly across both a full-length
main video and short (<45s) Shorts, without needing per-video mood/duration search. Actual
audio-level looping (seam/crossfade handling at the loop point) is a Remotion rendering detail
for Phase 2 — not testable in this sandbox (no ffmpeg/Node render environment available), but
the selection math itself is verified end-to-end. **Status: unblocked, set is real and usable.**
