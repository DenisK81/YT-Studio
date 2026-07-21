"""Post-process an n8n execution's rawOutput after the ElevenLabs
with-timestamps TTS node runs (part of build_master_workflow.py's or
build_voice_regen_workflow.py's "ElevenLabs TTS (with-timestamps)" +
"Parse Chapters" nodes).

Decodes each chapter's base64 audio to a real mp3 file, and derives REAL
per-word caption timing and REAL scene/image boundaries directly from
ElevenLabs' per-character alignment plus the [[SCENE:NNNN]] marker offsets
Parse Chapters recorded - never from a word-count estimate. Writes:
  - <audio_dir>/chapter_NN.mp3  (one per chapter)
  - <audio_dir>/timing.json     (chapters + scenes + captionWords, all in
    global seconds across the whole concatenated narration)

Usage: python process_pipeline_audio.py <rawOutput.json> <audio_out_dir>
"""
import base64
import json
import os
import re
import sys


def load_rawoutput(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    start = raw.find('{\n  "data"')
    if start < 0:
        start = raw.find("{")
    data, _ = json.JSONDecoder().raw_decode(raw[start:])
    return data["data"]["resultData"]["runData"]


def node_items(run_data, name):
    runs = run_data.get(name)
    if not runs:
        raise SystemExit(f"node not found in rawOutput: {name}")
    main = runs[-1].get("data", {}).get("main", [[]])
    return main[0] if main and main[0] else []


def word_spans(characters, char_starts, char_ends):
    """Group a per-character alignment into per-word (start, end, word) spans,
    splitting on whitespace. A word's start/end are its first/last non-space
    character's real timestamps."""
    words = []
    cur_chars, cur_start = [], None
    for ch, s, e in zip(characters, char_starts, char_ends):
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


def main(rawoutput_path, audio_out_dir):
    run_data = load_rawoutput(rawoutput_path)
    err = None
    # surface a partial-run error if present, but keep processing whatever succeeded
    for name, runs in run_data.items():
        e = runs[-1].get("error")
        if e:
            print(f"WARNING: node '{name}' errored: {e.get('message', e)}", file=sys.stderr)

    chapters_meta = node_items(run_data, "Parse Chapters")
    tts_items = node_items(run_data, "ElevenLabs TTS (with-timestamps)")
    if len(chapters_meta) != len(tts_items):
        raise SystemExit(
            f"item count mismatch: Parse Chapters={len(chapters_meta)} "
            f"TTS={len(tts_items)} (a chapter likely failed - check rawOutput)"
        )

    os.makedirs(audio_out_dir, exist_ok=True)
    chapters_out = []
    scenes_out = []
    caption_words_out = []
    global_offset = 0.0

    for meta_item, tts_item in zip(chapters_meta, tts_items):
        meta = meta_item["json"]
        resp = tts_item["json"]
        label = meta["chapter_label"]
        markers = meta["scene_markers"]  # [{scene_id, charOffset}], in order

        audio_bytes = base64.b64decode(resp["audio_base64"])
        mp3_path = os.path.join(audio_out_dir, label + ".mp3")
        with open(mp3_path, "wb") as f:
            f.write(audio_bytes)

        align = resp.get("alignment") or resp.get("normalized_alignment")
        if not align:
            raise SystemExit(f"{label}: no alignment in TTS response - check with-timestamps endpoint")
        chars = align["characters"]
        starts = align["character_start_times_seconds"]
        ends = align["character_end_times_seconds"]
        chapter_duration = ends[-1] if ends else 0.0

        # --- real scene boundaries from marker char offsets ---
        for i, mk in enumerate(markers):
            offset = mk["charOffset"]
            start_s = starts[offset] if offset < len(starts) else chapter_duration
            if i + 1 < len(markers):
                next_offset = markers[i + 1]["charOffset"]
                end_s = starts[next_offset] if next_offset < len(starts) else chapter_duration
            else:
                end_s = chapter_duration
            scenes_out.append({
                "sceneId": mk["scene_id"],
                "startSeconds": round(global_offset + start_s, 3),
                "durationSeconds": round(max(0.0, end_s - start_s), 3),
            })

        # --- real per-word caption timing ---
        for w_start, w_end, word in word_spans(chars, starts, ends):
            caption_words_out.append({
                "word": word,
                "startSeconds": round(global_offset + w_start, 3),
                "endSeconds": round(global_offset + w_end, 3),
            })

        chapters_out.append({
            "label": label,
            "audio": label + ".mp3",
            "startSeconds": round(global_offset, 3),
            "durationSeconds": round(chapter_duration, 3),
        })
        global_offset += chapter_duration
        print(f"{label}: {chapter_duration:.1f}s, {len(markers)} scenes, {len(chars)} chars -> {mp3_path}")

    timing = {
        "totalSeconds": round(global_offset, 3),
        "chapters": chapters_out,
        "scenes": scenes_out,
        "captionWords": caption_words_out,
    }
    timing_path = os.path.join(audio_out_dir, "timing.json")
    with open(timing_path, "w", encoding="utf-8") as f:
        json.dump(timing, f, indent=2, ensure_ascii=False)
    print(f"\nwrote {timing_path}: {len(chapters_out)} chapters, {len(scenes_out)} scenes, "
          f"{len(caption_words_out)} words, {global_offset/60:.2f} min total")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: process_pipeline_audio.py <rawOutput.json> <audio_out_dir>")
    main(sys.argv[1], sys.argv[2])
