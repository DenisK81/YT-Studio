# Voice Production Agent

## Responsibility
Reformat the scene list into ElevenLabs-ready voiceover text: natural American English, short
sentences, no robotic phrasing, no emotion tags (per this channel's current brief — tags like
[whispers] are an option for a future variant of Eleven v3, not the default). Chunk into
Studio-chapter-sized blocks so long-form narration stays coherent.

## Input
```json
{ "scenes": [ {"scene_id":"", "text":"", "beat":""} ] }
```

## Output
`Templates/Voiceover.txt`, chunked by chapter, each chunk labeled with its scene_id range —
**and** the actual rendered audio, one file per chapter chunk (not per scene_id):
`Assets/audio/chapter_01.mp3`, `chapter_02.mp3`, etc., matching `Voiceover.txt`'s own chapter
boundaries.

**Stage 3 link note (added 2026-07-20):** this agent's Output section previously only named
`Voiceover.txt` (text), leaving the actual audio-file convention undeclared even though Video
Assembly Agent's input (`audio_chunks: ["Assets/audio/*.mp3"]`) needs real files to exist.
Per-chapter (not per-scene) is the right granularity — it matches ElevenLabs Studio's own
chapter-splitting mode (see `Tools/elevenlabs_voice_tool.md`'s "Default provider notes") and
avoids an awkward re-stitch of many tiny per-scene clips into natural-sounding continuous
narration. Video Assembly Agent (via `Tools/remotion_assembly_tool.md`, whose `assemble()`
interface takes one `audio_track: string`, singular) is responsible for concatenating these
per-chapter chunks into one continuous track before rendering — not this agent's job.

## Tools
`Tools/elevenlabs_voice_tool.md` (provider-swappable — see Voice Policy in
`Documentation/ARCHITECTURE.md`; the contract is `generate(text, voice_id) -> audio`, so
another TTS provider can replace ElevenLabs without touching this agent). Call it once per
chapter chunk, using the `chapter_label` param for naming.

## Escalate to human when
A single scene's text is long enough that it risks exceeding the TTS provider's recommended
chunk length — flag rather than silently truncating.

## System prompt (draft)
"""
You are the Voice Production Agent. Convert the given scenes into clean voiceover text for
text-to-speech: natural spoken American English, short sentences, no stage directions, no
emotion tags, no markdown. Preserve scene order and group scenes into chapter-sized chunks
(roughly 300-500 words) for long-form narration. Label each chunk with its scene_id range.
Output only the formatted voiceover text.
"""
