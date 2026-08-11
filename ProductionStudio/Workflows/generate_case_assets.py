"""Local, no-n8n, no-Anthropic-key asset generator for a case.

Phase 1 default (see Documentation/ARCHITECTURE.md's "Orchestration decision"
section, 2026-07-21): Claude Code plays each of the 11 agent roles directly in
conversation and writes the case's text files itself (Script.md, SceneList.json,
Voiceover.txt with inline [[SCENE:NNNN]] markers, ImagePrompts.md, etc.). This
script handles only the two things that need a real external API call: turning
Voiceover.txt into real narrated audio (ElevenLabs, with real per-character
timestamps so captions can never drift from or mismatch the narration - see
Tools/remotion_assembly_tool.md) and turning ImagePrompts.md into real scene
images (fal.ai Flux schnell).

Usage:
    python generate_case_assets.py audio  <case_dir> [--audio-dir DIR]
    python generate_case_assets.py images <case_dir> [--images-dir DIR]
    python generate_case_assets.py all    <case_dir> [--audio-dir DIR] [--images-dir DIR]

Reads Voiceover.txt / ImagePrompts.md from <case_dir>. Defaults audio/images
output to Assets/audio/<case_dir basename>/ and Assets/images/<case_dir basename>/
next to the repo's ProductionStudio folder (both gitignored).

Requires ELEVENLABS_API_KEY and/or FAL_KEY in the environment - never hardcode.
"""
import argparse
import base64
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request

VOICE_ID = "wSChTcAxdiTjLPhHeyrM"  # Jimmy - Canadian Podcast Narration (fixed in config)
ELEVENLABS_MODEL = "eleven_multilingual_v2"
# Natural-delivery tuning (2026-08-10, channel owner asked for less robotic/more natural
# pacing). Verified against ElevenLabs' current docs before setting these - no voice_settings
# were being sent at all before (silent API defaults: stability 0.5, similarity_boost 0.75,
# style 0). eleven_multilingual_v2 doesn't support <break time="Xs" /> SSML tags (that's
# eleven_flash_v2 only, and Flash trades narration quality for low latency - not worth it here),
# so pacing comes from voice_settings + the speed param + punctuation in the script text itself
# (em dashes / ellipses at natural breath points), not markup.
ELEVENLABS_VOICE_SETTINGS = {
    "stability": 0.38,       # lower than the 0.5 default -> more natural pitch/pace variation,
                              # less flat "read aloud" monotone, still stable enough not to drift
    "similarity_boost": 0.75,
    "style": 0.0,             # keep at 0 - non-zero style adds latency and can overact for this
                              # documentary-narrator register
    "use_speaker_boost": True,
}
ELEVENLABS_SPEED = 0.93       # slightly slower than the 1.0 default -> more deliberate, less
                              # rushed delivery, closer to a real documentary narrator's pace
TTS_REQUEST_SPACING_SECONDS = 20  # Creator plan: max 5 concurrent - stay well under it
FAL_REQUEST_SPACING_SECONDS = 1
LOUDNORM_TARGET_I = -24  # integrated LUFS target - see Tools/remotion_assembly_tool.md's
LOUDNORM_TARGET_TP = -1.5  # "Chapter-to-chapter voice loudness inconsistency" note (2026-07-28):
LOUDNORM_TARGET_LRA = 11  # each chapter is a separate ElevenLabs call with no cross-call loudness
                           # guarantee - a real case measured up to a 9.7 LU swing between chapters
                           # (clearly audible as a volume jump) before this normalization existed.


def _find_ffmpeg():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    # Known winget install location on this machine - shutil.which alone won't find it since
    # ffmpeg isn't on PATH by default even after `winget install`.
    candidates = glob.glob(
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg_*\ffmpeg-*\bin\ffmpeg.exe")
    )
    return candidates[0] if candidates else None


def normalize_chapter_loudness(mp3_path):
    """Two-pass ffmpeg loudnorm in place, sample-accurate (no duration change - verified via
    mutagen on a real case), so it's always safe to run right after ElevenLabs writes a chapter
    and before its real per-word timing (derived independently from the API's own alignment,
    not from the audio file) is used downstream."""
    ffmpeg = _find_ffmpeg()
    if not ffmpeg:
        print(f"  WARNING: ffmpeg not found - skipping loudness normalization for {mp3_path}")
        return
    measure_cmd = [ffmpeg, "-i", mp3_path, "-af",
                   f"loudnorm=I={LOUDNORM_TARGET_I}:TP={LOUDNORM_TARGET_TP}:LRA={LOUDNORM_TARGET_LRA}:print_format=json",
                   "-f", "null", "-"]
    result = subprocess.run(measure_cmd, capture_output=True, text=True)
    match = re.search(r"\{[^{}]*\}", result.stderr, re.DOTALL)
    if not match:
        print(f"  WARNING: loudnorm measurement failed for {mp3_path} - leaving un-normalized")
        return
    m = json.loads(match.group(0))
    out_path = mp3_path + ".norm.mp3"
    apply_cmd = [
        ffmpeg, "-y", "-i", mp3_path, "-af",
        f"loudnorm=I={LOUDNORM_TARGET_I}:TP={LOUDNORM_TARGET_TP}:LRA={LOUDNORM_TARGET_LRA}:"
        f"measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
        f"measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true",
        "-ar", "44100", "-c:a", "libmp3lame", "-b:a", "192k", out_path,
    ]
    subprocess.run(apply_cmd, capture_output=True, text=True)
    os.replace(out_path, mp3_path)
    print(f"  normalized loudness: {m['input_i']} LUFS -> {LOUDNORM_TARGET_I} LUFS")


def repo_root():
    # this file lives at ProductionStudio/Workflows/generate_case_assets.py
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def post_json(url, headers, body, timeout=300):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP {e.code} calling {url}: {e.read().decode(errors='replace')[:500]}")


def get_bytes(url, timeout=120):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.read()


# --- shared: parse Voiceover.txt into chapters + [[SCENE:NNNN]] marker offsets ---
def parse_voiceover(voiceover_text):
    # Guard against exactly the bug found 2026-07-21: a Voice Production Agent turn
    # (real or Claude Code acting the role) can append trailing prose after the real
    # narration - "Rendered audio: chapter_01.mp3 - scenes ...", an escalation note,
    # etc. - and that text got literally read aloud by TTS because nothing separated
    # it from the real content. If the file wraps its narration in a ``` fence (as
    # this agent has done when adding such notes), only text INSIDE the first fence
    # counts; anything outside is meta-commentary for a human, never narration.
    fence = re.search(r"```(?:\w+)?\n([\s\S]*?)```", voiceover_text)
    if fence:
        before, after = voiceover_text[:fence.start()], voiceover_text[fence.end():]
        stray = (before + after).strip()
        if stray:
            print(f"NOTE: {len(stray)} chars outside the ``` fence were excluded from narration "
                  f"(meta-commentary, not spoken text) - review Voiceover.txt if this looks wrong:")
            print("  " + stray[:300].replace("\n", "\n  "))
        voiceover_text = fence.group(1)

    parts = re.split(r"^===\s*CHAPTER\s+", voiceover_text, flags=re.M)[1:]
    if not parts:
        raise SystemExit("No '=== CHAPTER NN (scenes ...) ===' headers found in Voiceover.txt")
    chapters = []
    for p in parts:
        num = (re.match(r"(\d+)", p) or [None, "00"])[1].zfill(2) if re.match(r"(\d+)", p) else "00"
        body = p[p.index("===") + 3:].strip()
        marker_re = re.compile(r"\[\[SCENE:(\d{4})\]\]\s*")
        clean_parts = []
        markers = []
        last_end = 0
        clean_len = 0
        for m in marker_re.finditer(body):
            clean_parts.append(body[last_end:m.start()])
            clean_len += len(body[last_end:m.start()])
            markers.append({"scene_id": m.group(1), "char_offset": clean_len})
            last_end = m.end()
        clean_parts.append(body[last_end:])
        clean_text = "".join(clean_parts)
        if not markers:
            raise SystemExit(f"Chapter {num} has no [[SCENE:NNNN]] markers - re-check Voiceover.txt")
        if len(clean_text) > 9500:
            raise SystemExit(f"Chapter {num} is {len(clean_text)} chars, over the TTS limit")
        chapters.append({"label": f"chapter_{num}", "text": clean_text, "markers": markers})
    return chapters


def word_spans(characters, starts, ends):
    """Group per-character alignment into (start, end, word) spans on whitespace."""
    words = []
    cur_chars, cur_start, prev_end = [], None, None
    for ch, s, e in zip(characters, starts, ends):
        if ch.strip() == "":
            if cur_chars:
                words.append((cur_start, prev_end, "".join(cur_chars)))
                cur_chars, cur_start = [], None
            continue
        if cur_start is None:
            cur_start = s
        cur_chars.append(ch)
        prev_end = e
    if cur_chars:
        words.append((cur_start, prev_end, "".join(cur_chars)))
    return words


def cmd_audio(case_dir, audio_dir):
    el_key = os.environ["ELEVENLABS_API_KEY"]
    voiceover_path = os.path.join(case_dir, "Voiceover.txt")
    with open(voiceover_path, encoding="utf-8") as f:
        chapters = parse_voiceover(f.read())

    os.makedirs(audio_dir, exist_ok=True)
    chapters_out, scenes_out, caption_words_out = [], [], []
    global_offset = 0.0

    for i, ch in enumerate(chapters):
        if i > 0:
            print(f"  waiting {TTS_REQUEST_SPACING_SECONDS}s before next chapter (rate limit)...")
            time.sleep(TTS_REQUEST_SPACING_SECONDS)

        print(f"generating {ch['label']} ({len(ch['text'])} chars)...")
        resp = post_json(
            f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps"
            f"?output_format=mp3_44100_128",
            {"xi-api-key": el_key, "Content-Type": "application/json"},
            {"text": ch["text"], "model_id": ELEVENLABS_MODEL,
             "voice_settings": ELEVENLABS_VOICE_SETTINGS, "speed": ELEVENLABS_SPEED},
        )

        audio_bytes = base64.b64decode(resp["audio_base64"])
        mp3_path = os.path.join(audio_dir, ch["label"] + ".mp3")
        with open(mp3_path, "wb") as f:
            f.write(audio_bytes)
        normalize_chapter_loudness(mp3_path)

        align = resp.get("alignment") or resp.get("normalized_alignment")
        if not align:
            raise SystemExit(f"{ch['label']}: no alignment in response - with-timestamps endpoint required")
        chars, starts, ends = align["characters"], align["character_start_times_seconds"], align["character_end_times_seconds"]
        chapter_duration = ends[-1] if ends else 0.0

        for j, mk in enumerate(ch["markers"]):
            offset = mk["char_offset"]
            start_s = starts[offset] if offset < len(starts) else chapter_duration
            if j + 1 < len(ch["markers"]):
                next_offset = ch["markers"][j + 1]["char_offset"]
                end_s = starts[next_offset] if next_offset < len(starts) else chapter_duration
            else:
                end_s = chapter_duration
            scenes_out.append({
                "sceneId": mk["scene_id"],
                "startSeconds": round(global_offset + start_s, 3),
                "durationSeconds": round(max(0.0, end_s - start_s), 3),
            })

        for w_start, w_end, word in word_spans(chars, starts, ends):
            caption_words_out.append({
                "word": word,
                "startSeconds": round(global_offset + w_start, 3),
                "endSeconds": round(global_offset + w_end, 3),
            })

        chapters_out.append({
            "label": ch["label"], "audio": ch["label"] + ".mp3",
            "startSeconds": round(global_offset, 3), "durationSeconds": round(chapter_duration, 3),
        })
        global_offset += chapter_duration
        print(f"  -> {chapter_duration:.1f}s, {len(ch['markers'])} scenes -> {mp3_path}")

    timing = {
        "totalSeconds": round(global_offset, 3),
        "chapters": chapters_out, "scenes": scenes_out, "captionWords": caption_words_out,
    }
    timing_path = os.path.join(audio_dir, "timing.json")
    with open(timing_path, "w", encoding="utf-8") as f:
        json.dump(timing, f, indent=2, ensure_ascii=False)
    print(f"\nwrote {timing_path}: {len(chapters_out)} chapters, {len(scenes_out)} scenes, "
          f"{len(caption_words_out)} words, {global_offset/60:.2f} min total")


def cmd_images(case_dir, images_dir):
    from PIL import Image

    fal_key = os.environ["FAL_KEY"]
    prompts_path = os.path.join(case_dir, "ImagePrompts.md")
    with open(prompts_path, encoding="utf-8") as f:
        raw = f.read().strip()
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw)
    if fence:
        raw = fence.group(1)
    data = json.loads(raw[raw.index("{"): raw.rindex("}") + 1])
    prompts = data.get("prompts") or []
    if not prompts:
        raise SystemExit("No prompts parsed from ImagePrompts.md")

    # Real-photo scenes (mandatory mixing, see Tools/mugshot_fetch_tool.md) are copied
    # in as-is instead of generated - never send their placeholder prompt to fal.ai.
    real_photo_scenes = {rp["scene_id"]: rp["local_path"] for rp in data.get("real_photo_scenes", [])}

    os.makedirs(images_dir, exist_ok=True)
    generated = 0
    for p in prompts:
        scene_id = p["scene_id"]
        out_path = os.path.join(images_dir, scene_id + ".png")

        if scene_id in real_photo_scenes:
            src_path = os.path.join(repo_root(), real_photo_scenes[scene_id])
            img = Image.open(src_path).convert("RGB")
            img.save(out_path)
            print(f"real photo scene {scene_id}: copied {src_path} -> {out_path}")
            continue

        if generated > 0:
            time.sleep(FAL_REQUEST_SPACING_SECONDS)
        generated += 1
        full_prompt = p["prompt"] + ", " + ", ".join(p.get("style_tags", []))
        print(f"generating scene {scene_id}...")
        resp = post_json(
            "https://fal.run/fal-ai/flux/schnell",
            {"Authorization": f"Key {fal_key}", "Content-Type": "application/json"},
            {"prompt": full_prompt, "image_size": "landscape_16_9", "num_images": 1, "output_format": "png"},
        )
        img_bytes = get_bytes(resp["images"][0]["url"])
        with open(out_path, "wb") as f:
            f.write(img_bytes)
        print(f"  -> {out_path} ({len(img_bytes)} bytes)")
    print(f"\ndone: {generated} generated + {len(real_photo_scenes)} real photos -> {images_dir}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["audio", "images", "all"])
    parser.add_argument("case_dir")
    parser.add_argument("--audio-dir")
    parser.add_argument("--images-dir")
    args = parser.parse_args()

    case_dir = os.path.abspath(args.case_dir)
    slug = os.path.basename(case_dir.rstrip("/\\"))
    repo = repo_root()
    audio_dir = args.audio_dir or os.path.join(repo, "ProductionStudio", "Assets", "audio", slug)
    images_dir = args.images_dir or os.path.join(repo, "ProductionStudio", "Assets", "images", slug)

    if args.command in ("audio", "all"):
        cmd_audio(case_dir, audio_dir)
    if args.command in ("images", "all"):
        cmd_images(case_dir, images_dir)


if __name__ == "__main__":
    main()
