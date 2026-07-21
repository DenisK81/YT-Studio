"""Generate standalone audio + real per-word timing for a single Short from
its own condensed script (a separate, tighter re-narration of the same
verified facts - Shorts have different pacing needs than the continuous
main-video narration, per Agents/shorts_agent.md's "different job, different
constraints" principle). The script file uses the same [[SCENE:NNNN]] marker
convention as the main Voiceover.txt, so scene images are reused unchanged.

Usage:
    python generate_shorts_audio.py --script <script_txt_path> <short_id> <out_dir>
    python generate_shorts_audio.py <case_dir> <short_id> <scene_id_lo> <scene_id_hi> <out_dir>
"""
import base64
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_case_assets import post_json, word_spans, VOICE_ID, ELEVENLABS_MODEL


def extract_marked_text_from_script(script_path):
    """A standalone script file already in [[SCENE:NNNN]] text ... format,
    one paragraph per scene. Just strip markers and record offsets."""
    raw = open(script_path, encoding="utf-8").read()
    marker_re = re.compile(r"\[\[SCENE:(\d{4})\]\]\s*")
    clean = []
    markers = []
    last_end = 0
    clean_len = 0
    for m in marker_re.finditer(raw):
        clean.append(raw[last_end:m.start()])
        clean_len += len(raw[last_end:m.start()])
        markers.append({"scene_id": m.group(1), "char_offset": clean_len})
        last_end = m.end()
    clean.append(raw[last_end:])
    clean_text = "".join(clean).strip()
    return clean_text, markers


def extract_marked_text(voiceover_path, scene_lo, scene_hi):
    vo = open(voiceover_path, encoding="utf-8").read()
    fence = re.search(r"```\n([\s\S]*?)```", vo)
    body = fence.group(1) if fence else vo
    markers = list(re.finditer(r"\[\[SCENE:(\d{4})\]\]\s*", body))
    scene_text = {}
    for i, m in enumerate(markers):
        sid = m.group(1)
        start = m.end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(body)
        scene_text[sid] = body[start:end].strip()

    lo, hi = int(scene_lo), int(scene_hi)
    ordered_ids = [f"{i:04d}" for i in range(lo, hi + 1)]
    parts = []
    scene_markers = []
    offset = 0
    for sid in ordered_ids:
        text = scene_text[sid]
        scene_markers.append({"scene_id": sid, "char_offset": offset})
        parts.append(text)
        offset += len(text) + 1  # +1 for the joining space
    clean_text = " ".join(parts)
    return clean_text, scene_markers


def main(short_id, out_dir, script_path=None, case_dir=None, scene_lo=None, scene_hi=None):
    el_key = os.environ["ELEVENLABS_API_KEY"]
    if script_path:
        text, markers = extract_marked_text_from_script(script_path)
    else:
        voiceover_path = os.path.join(case_dir, "Voiceover.txt")
        text, markers = extract_marked_text(voiceover_path, scene_lo, scene_hi)
    print(f"{short_id}: {len(text)} chars, {len(markers)} scenes")

    resp = post_json(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps"
        f"?output_format=mp3_44100_128",
        {"xi-api-key": el_key, "Content-Type": "application/json"},
        {"text": text, "model_id": ELEVENLABS_MODEL},
    )

    os.makedirs(out_dir, exist_ok=True)
    audio_bytes = base64.b64decode(resp["audio_base64"])
    mp3_path = os.path.join(out_dir, f"{short_id}.mp3")
    with open(mp3_path, "wb") as f:
        f.write(audio_bytes)

    align = resp.get("alignment") or resp.get("normalized_alignment")
    chars, starts, ends = align["characters"], align["character_start_times_seconds"], align["character_end_times_seconds"]
    duration = ends[-1] if ends else 0.0

    scenes_out = []
    for i, mk in enumerate(markers):
        offset = mk["char_offset"]
        start_s = starts[offset] if offset < len(starts) else duration
        if i + 1 < len(markers):
            next_offset = markers[i + 1]["char_offset"]
            end_s = starts[next_offset] if next_offset < len(starts) else duration
        else:
            end_s = duration
        scenes_out.append({"sceneId": mk["scene_id"], "startSeconds": round(start_s, 3),
                            "durationSeconds": round(max(0.0, end_s - start_s), 3)})

    words_out = [{"word": w, "startSeconds": round(s, 3), "endSeconds": round(e, 3)}
                 for s, e, w in word_spans(chars, starts, ends)]

    timing = {"totalSeconds": round(duration, 3), "audio": f"{short_id}.mp3",
              "scenes": scenes_out, "captionWords": words_out}
    timing_path = os.path.join(out_dir, f"{short_id}_timing.json")
    with open(timing_path, "w", encoding="utf-8") as f:
        json.dump(timing, f, indent=2, ensure_ascii=False)
    print(f"  -> {duration:.1f}s -> {mp3_path}")
    print(f"  -> {timing_path}")


if __name__ == "__main__":
    if sys.argv[1] == "--script":
        # generate_shorts_audio.py --script <script_txt_path> <short_id> <out_dir>
        main(short_id=sys.argv[3], out_dir=sys.argv[4], script_path=sys.argv[2])
    elif len(sys.argv) == 6:
        main(short_id=sys.argv[2], out_dir=sys.argv[5], case_dir=sys.argv[1],
             scene_lo=sys.argv[3], scene_hi=sys.argv[4])
    else:
        raise SystemExit(
            "usage: generate_shorts_audio.py --script <script_txt_path> <short_id> <out_dir>\n"
            "   or: generate_shorts_audio.py <case_dir> <short_id> <scene_lo> <scene_hi> <out_dir>"
        )
