# Assets

Generated media lives here at build/run time: `images/`, `audio/`, `renders/`. These are
gitignored (see repo root `.gitignore`) — this folder should stay empty in git except for this
README, so the repo stays a code/prompt/template repo, not a media dump.

Expected subfolders once running:
```
Assets/
    images/          one file per scene_id, from Image Generation Agent
    audio/           voiceover chunks, from Voice Production Agent / ElevenLabs
    audio/music_bed/ 10 channel-wide background music tracks (bed_01.mp3..bed_10.mp3),
                     hand-picked once from Pixabay Music — reused across every video/Short,
                     not per-case. See Tools/royalty_free_music_tool.md.
    renders/         draft.mp4 and final.mp4, from Video Assembly Agent
```
