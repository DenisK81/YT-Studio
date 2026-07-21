```json
{
  "shorts": [
    {
      "short_id": "short_1",
      "title": "The Grief Book Twist",
      "narration_script": "It's called \"Are You With Me?\" A children's book about a child learning to cope with grief after losing a parent. She wrote it. She promoted it on local media. She said she just wanted something to read to her own kids at night. Here's the problem. Prosecutors say she was the reason for that loss, and she wrote this while she was already a suspect. All of it, published and sold to other families, months before she was ever charged.",
      "source_scene_ids": ["0044", "0045", "0046", "0047"],
      "hook_overlay_text": "SHE WROTE THIS?",
      "cold_open_image_prompt": "reuse: Assets/images/kouri-richins-fentanyl-murder/thumbnail.png (dramatic close-up face, no burned-in text) — same grief-book-twist theme as the thumbnail, no new generation needed",
      "cta_text": "FULL STORY ON THE CHANNEL",
      "hashtags": ["#TrueCrime", "#KouriRichins", "#PlotTwist", "#TrueCrimeShorts"],
      "narration_seconds": 28.8,
      "total_seconds": 33.8,
      "audio_file": "Assets/audio/kouri-richins-fentanyl-murder-shorts/short_1.mp3",
      "render_file": "Assets/renders/kouri-richins-fentanyl-murder-short_1-she-wrote-this.mp4"
    },
    {
      "short_id": "short_3",
      "title": "The Text That Convicted Her",
      "narration_script": "Kouri had been seeing another man, Robert Josh Grossman, for two years, hidden underneath the marriage. Investigators recovered a text she sent him. Read it for yourself. \"If he could just go away and you could just be here! Life would be so perfect!!\" That's not a woman imagining an escape. That's a woman imagining an ending.",
      "source_scene_ids": ["0030", "0031", "0032"],
      "hook_overlay_text": "ONE TEXT. GUILTY.",
      "cold_open_image_prompt": "Extreme close-up of a woman's eyes lit by a phone screen glow in the dark, tense expression, cinematic true-crime documentary style, shallow depth of field",
      "cta_text": "FULL STORY ON THE CHANNEL",
      "hashtags": ["#TrueCrime", "#KouriRichins", "#Evidence", "#TrueCrimeShorts"],
      "narration_seconds": 21.6,
      "total_seconds": 26.6,
      "audio_file": "Assets/audio/kouri-richins-fentanyl-murder-shorts/short_3.mp3",
      "render_file": "Assets/renders/kouri-richins-fentanyl-murder-short_3-one-text-guilty.mp4"
    },
    {
      "short_id": "short_4",
      "title": "Guilty In 3 Hours",
      "narration_script": "The verdict: guilty on all five counts. First-degree aggravated murder. Attempted aggravated murder. Insurance fraud. Forgery. Four years of investigation. Delays. Disputes. All of it building to this moment. The jury needed three hours to agree on every count.",
      "source_scene_ids": ["0062", "0063", "0064"],
      "hook_overlay_text": "GUILTY IN 3 HOURS",
      "cold_open_image_prompt": "Extreme close-up of a woman's face in near-darkness, only eyes and mouth partially lit, cold and unreadable expression, cinematic true-crime documentary style",
      "cta_text": "FULL STORY ON THE CHANNEL",
      "hashtags": ["#TrueCrime", "#KouriRichins", "#Verdict", "#TrueCrimeShorts"],
      "narration_seconds": 20.2,
      "total_seconds": 25.2,
      "audio_file": "Assets/audio/kouri-richins-fentanyl-murder-shorts/short_4.mp3",
      "render_file": "Assets/renders/kouri-richins-fentanyl-murder-short_4-guilty-in-3-hours.mp4"
    },
    {
      "short_id": "short_5",
      "title": "Too Dangerous To Be Free",
      "narration_script": "The judge didn't hold back. He said she'd spent seventeen days \"doubling down, preparing to try again.\" Then he told her directly: she is \"simply too dangerous to ever be free.\" Life without parole. Plus decades more, stacked on top.",
      "source_scene_ids": ["0066", "0067", "0068"],
      "hook_overlay_text": "NEVER FREE AGAIN",
      "cold_open_image_prompt": "Extreme close-up of a woman's face in teal-toned low light, eyes half closed, faint unsettling smile, cinematic true-crime documentary style",
      "cta_text": "FULL STORY ON THE CHANNEL",
      "hashtags": ["#TrueCrime", "#KouriRichins", "#Sentencing", "#TrueCrimeShorts"],
      "narration_seconds": 16.6,
      "total_seconds": 21.6,
      "audio_file": "Assets/audio/kouri-richins-fentanyl-murder-shorts/short_5.mp3",
      "render_file": "Assets/renders/kouri-richins-fentanyl-murder-short_5-never-free-again.mp4"
    }
  ]
}
```

## Final set: 4 shorts (2026-07-21)

`short_2` (The Forged Policy) was dropped per the channel owner's request to cap this batch at
four. The remaining four cover distinct beats (twist reveal, evidence, verdict, sentencing) so
they don't cannibalize each other's hook.

Each short's `narration_script` is a **freshly condensed re-narration** of the same verified
facts from `FactCheck.md`/`Script.md` — not a verbatim scene-text reuse. Verbatim reuse was
tried first for `short_1` and came out to 49.6s of narration alone (over the 45s hard cap before
even adding cold-open/CTA overhead); tighter, Shorts-specific phrasing brought every short in
well under budget. `source_scene_ids` still record which main-video scenes/images anchor each
short (for image reuse and continuity), but the spoken words are not identical to the main
video's Voiceover.txt for these ranges.

All 4 durations below are **real, from ElevenLabs with-timestamps audio**, not estimates
(`narration_seconds` = spoken audio; `total_seconds` = narration + 1.5s cold open + 3.5s CTA
card). All are comfortably under the 45s cap.

## Visual structure (see `Agents/shorts_agent.md` → "Shorts visual style")

- **Cold open (1.5s)**: a dramatic face close-up (reused thumbnail for short_1; new fal.ai
  generations for short_3/4/5) with `hook_overlay_text` in big, high-contrast center-screen text
  (Impact/Oswald, white fill + black stroke) — the "big faces like the thumbnail" hook the
  channel owner asked for.
- **Body**: scene images (Ken Burns), captions in **center-screen karaoke** style (distinct
  placement from the main video's lower-third), active word highlighted in `#A30E15`.
  Real per-word timing throughout, from the same ElevenLabs with-timestamps mechanism as the
  main video — no estimated captions.
  - **No intro bumper** on any Short — the channel owner explicitly excluded Shorts from the
    upcoming bumper template (`Documentation/ARCHITECTURE.md` → "Channel intro bumper
    requirement"); the bumper is a main-video-only piece, not yet built.
- **CTA (3.5s)**: last scene frame held and darkened under `cta_text` ("FULL STORY ON THE
  CHANNEL"), same big center-screen text style, timed to the final ~3-5 seconds per the
  research findings below.

## Why this structure (real 2026 web research, not assumption)

True-crime-specific Shorts conventions differ from generic viral-video advice:
bold/high-contrast on-screen text (3-7 words, ideally 3-4) drives retention past the first few
seconds; CTAs work best as on-screen text in the final 3-5 seconds since most Shorts viewers
watch muted; true-crime audiences specifically disengage from manufactured/fake cliffhangers, so
each hook here is a genuine claim from the case (a real text message, a real verdict, a real
sentencing quote) rather than invented mystery. All 4 hook texts above are 2-4 words.

## Rendered files

All 4 rendered 2026-07-21, 1080x1920, real audio + real per-word captions, spot-checked frame by
frame (cold open, mid-body captions, CTA card) — see `render_file` paths above
(`Assets/renders/`, gitignored).
