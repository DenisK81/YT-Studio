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
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

VOICE_ID = "wSChTcAxdiTjLPhHeyrM"  # Jimmy - Canadian Podcast Narration (fixed in config)
ELEVENLABS_MODEL = "eleven_multilingual_v2"
TTS_REQUEST_SPACING_SECONDS = 20  # Creator plan: max 5 concurrent - stay well under it
FAL_REQUEST_SPACING_SECONDS = 1


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
            {"text": ch["text"], "model_id": ELEVENLABS_MODEL},
        )

        audio_bytes = base64.b64decode(resp["audio_base64"])
        mp3_path = os.path.join(audio_dir, ch["label"] + ".mp3")
        with open(mp3_path, "wb") as f:
            f.write(audio_bytes)

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

    os.makedirs(images_dir, exist_ok=True)
    for i, p in enumerate(prompts):
        if i > 0:
            time.sleep(FAL_REQUEST_SPACING_SECONDS)
        scene_id = p["scene_id"]
        full_prompt = p["prompt"] + ", " + ", ".join(p.get("style_tags", []))
        print(f"generating scene {scene_id}...")
        resp = post_json(
            "https://fal.run/fal-ai/flux/schnell",
            {"Authorization": f"Key {fal_key}", "Content-Type": "application/json"},
            {"prompt": full_prompt, "image_size": "landscape_16_9", "num_images": 1, "output_format": "png"},
        )
        img_bytes = get_bytes(resp["images"][0]["url"])
        out_path = os.path.join(images_dir, scene_id + ".png")
        with open(out_path, "wb") as f:
            f.write(img_bytes)
        print(f"  -> {out_path} ({len(img_bytes)} bytes)")
    print(f"\ndone: {len(prompts)} images -> {images_dir}")


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
