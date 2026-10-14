"""Prepare a Remotion render from a case's REAL timing.json (produced by
process_pipeline_audio.py) + its scene images: copies assets into the
Remotion project's public/ dir and writes a TS data file with real per-scene
durations and real per-word caption timing - no estimation anywhere.

Usage:
    CASE_DIR=".../Cases/<slug>/<run>" AUDIO_DIR=".../Assets/audio/<run>" \\
    IMAGES_DIR=".../Assets/images/<run>" REMOTION_DIR=".../remotion-test" \\
    python prep_remotion_render.py
"""
import hashlib
import json
import os
import shutil
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from real_media_utils import cut_clip, probe_duration, copy_media

FPS = 30
WORDS_PER_CAPTION_CHUNK = 3

REPO = "D:/SHOPS/AI Projects/YT_Crime/YT-Studio"
CASE_DIR = os.environ.get(
    "CASE_DIR",
    REPO + "/ProductionStudio/Cases/brendan-banfield-double-murder/auto-run-2026-07-21",
)
AUDIO_DIR = os.environ.get("AUDIO_DIR", REPO + "/ProductionStudio/Assets/audio/banfield_auto")
IMAGES_DIR = os.environ.get("IMAGES_DIR", REPO + "/ProductionStudio/Assets/images/banfield_auto")
REMOTION_DIR = os.environ["REMOTION_DIR"]
PUB_SUBDIR = os.environ.get("PUB_SUBDIR", "banfield")
DATA_MODULE = os.environ.get("DATA_MODULE", "banfield_data")  # src/<DATA_MODULE>.ts, export name = BANFIELD
DATA_EXPORT = os.environ.get("DATA_EXPORT", "BANFIELD")

PUB = os.path.join(REMOTION_DIR, "public", PUB_SUBDIR)
os.makedirs(PUB, exist_ok=True)

with open(os.path.join(AUDIO_DIR, "timing.json"), encoding="utf-8") as f:
    timing = json.load(f)

for ch in timing["chapters"]:
    shutil.copyfile(os.path.join(AUDIO_DIR, ch["audio"]), os.path.join(PUB, ch["audio"]))

# Pull-quote scenes (PullQuoteCard, see Tools/remotion_assembly_tool.md) are a drop-in
# SceneImage replacement with no image file at all - sourced from the case's own
# ImagePrompts.md rather than timing.json, since they carry text, not a generated asset.
quote_scenes = {}
# Real-photo scenes (RealBadge overlay, see Tools/remotion_assembly_tool.md's "REAL badge
# overlay + source citation" section, added 2026-09-15) need an isReal/realSource flag on their
# scene entry so ShortComposition/the case's SceneImage can render the badge - without this the
# generated TS data is indistinguishable from an AI-generated scene.
real_photo_scenes = {}
# Real archival VIDEO (Track 3, added 2026-09-18 for the McCullagh case - first real use):
#  - real_clip_scenes: a muted real clip replaces one scene's image (cut to the scene's length)
#  - real_media_inserts: real audio/video with its OWN audio inserted between chapters (never in
#    the middle of a narration chapter, since a chapter is one TTS file)
real_clip_scenes = {}
real_media_inserts = []
# CASE_DIR is usually a per-run subdir (.../Cases/<slug>/auto-run-...); ImagePrompts.md lives
# one level up, at the case root. Fall back to CASE_DIR itself in case it's already the root.
_candidates = [
    os.path.join(os.path.dirname(CASE_DIR.rstrip("/\\")), "ImagePrompts.md"),
    os.path.join(CASE_DIR, "ImagePrompts.md"),
]
image_prompts_path = next((p for p in _candidates if os.path.exists(p)), _candidates[0])
if os.path.exists(image_prompts_path):
    with open(image_prompts_path, encoding="utf-8") as f:
        raw = f.read().strip()
    import re as _re
    fence = _re.search(r"```(?:json)?\s*([\s\S]*?)```", raw)
    if fence:
        raw = fence.group(1)
    try:
        ip_data = json.loads(raw[raw.index("{"): raw.rindex("}") + 1])
        for qs in ip_data.get("pull_quote_scenes", []):
            quote_scenes[qs["scene_id"]] = qs
        for rp in ip_data.get("real_photo_scenes", []):
            real_photo_scenes[rp["scene_id"]] = rp
        for rc in ip_data.get("real_clip_scenes", []):
            real_clip_scenes[rc["scene_id"]] = rc
        real_media_inserts = ip_data.get("real_media_inserts", [])
    except (ValueError, json.JSONDecodeError):
        pass

scene_entries = []
for s in timing["scenes"]:
    if s["sceneId"] in quote_scenes:
        qs = quote_scenes[s["sceneId"]]
        scene_entries.append({
            "sceneId": s["sceneId"],
            "type": "quote",
            "quote": qs["quote"],
            "attribution": qs.get("attribution", ""),
            "startFrame": round(s["startSeconds"] * FPS),
            "durationFrames": round(s["durationSeconds"] * FPS),
        })
        continue
    if s["sceneId"] in real_clip_scenes:
        rc = real_clip_scenes[s["sceneId"]]
        lp = rc["local_path"]
        csrc = lp if os.path.isabs(lp) else os.path.join(REPO, lp)
        cname = s["sceneId"] + ".mp4"
        cut_clip(csrc, os.path.join(PUB, cname), s["durationSeconds"] + 0.15, start_seconds=rc.get("start_sec", 0.0))
        scene_entries.append({
            "sceneId": s["sceneId"],
            "type": "clip",
            "src": f"{PUB_SUBDIR}/{cname}",
            "isReal": True,
            "realSource": rc.get("source", ""),
            "startFrame": round(s["startSeconds"] * FPS),
            "durationFrames": round(s["durationSeconds"] * FPS),
        })
        continue
    img_name = s["sceneId"] + ".png"
    is_real = s["sceneId"] in real_photo_scenes
    if is_real:
        rp = real_photo_scenes[s["sceneId"]]
        local_path = rp["local_path"]
        src = local_path if os.path.isabs(local_path) else os.path.join(REPO, local_path)
    else:
        src = os.path.join(IMAGES_DIR, img_name)
    if not os.path.exists(src):
        print(f"WARNING: missing image for scene {s['sceneId']}, skipping")
        continue
    shutil.copyfile(src, os.path.join(PUB, img_name))
    entry = {
        "sceneId": s["sceneId"],
        "type": "image",
        "image": f"{PUB_SUBDIR}/{img_name}",
        "startFrame": round(s["startSeconds"] * FPS),
        "durationFrames": round(s["durationSeconds"] * FPS),
    }
    if is_real:
        entry["isReal"] = True
        entry["realSource"] = real_photo_scenes[s["sceneId"]].get("source", "")
    scene_entries.append(entry)

# --- real-media inserts (audio/video with their own audio, placed BETWEEN chapters) ---
chapters_f = [{"audio": f"{PUB_SUBDIR}/{c['audio']}", "startFrame": round(c["startSeconds"] * FPS),
               "durationFrames": round(c["durationSeconds"] * FPS)} for c in timing["chapters"]]
inserts = []
for ins in sorted(real_media_inserts, key=lambda i: i["after_scene_id"]):
    after = next(e for e in scene_entries if e["sceneId"] == ins["after_scene_id"])
    T = after["startFrame"] + after["durationFrames"]
    if not any(abs(c["startFrame"] + c["durationFrames"] - T) <= 2 for c in chapters_f):
        raise SystemExit(f"real_media_insert after scene {ins['after_scene_id']} is not on a chapter "
                         f"boundary - a chapter is one TTS file, split the chapter there first")
    lp = ins["local_path"]
    isrc = lp if os.path.isabs(lp) else os.path.join(REPO, lp)
    iname = f"insert_{ins['after_scene_id']}" + os.path.splitext(isrc)[1]
    copy_media(isrc, PUB, iname)
    dur_frames = math.ceil(probe_duration(isrc) * FPS)
    entry = {"sceneId": f"insert_{ins['after_scene_id']}", "type": "insert", "kind": ins["kind"],
             "src": f"{PUB_SUBDIR}/{iname}", "label": ins.get("label", "REAL FOOTAGE"),
             "realSource": ins.get("source", ""), "T": T, "durationFrames": dur_frames}
    if ins.get("background_image"):
        bp = ins["background_image"]
        bsrc = bp if os.path.isabs(bp) else os.path.join(REPO, bp)
        copy_media(bsrc, PUB, f"insert_{ins['after_scene_id']}_bg.jpg")
        entry["background"] = f"{PUB_SUBDIR}/insert_{ins['after_scene_id']}_bg.jpg"
    if ins.get("captions_json"):
        cp = ins["captions_json"]
        cpath = cp if os.path.isabs(cp) else os.path.join(REPO, cp)
        with open(cpath, encoding="utf-8") as cf:
            cwords = json.load(cf)["words"]
        cchunks = []
        for i in range(0, len(cwords), WORDS_PER_CAPTION_CHUNK):
            g = cwords[i:i + WORDS_PER_CAPTION_CHUNK]
            cchunks.append({"startFrame": round(g[0]["startSeconds"] * FPS),
                            "endFrame": round(g[-1]["endSeconds"] * FPS),
                            "words": [{"text": w["word"], "startFrame": round(w["startSeconds"] * FPS),
                                       "endFrame": round(w["endSeconds"] * FPS)} for w in g]})
        entry["captionChunks"] = cchunks
    inserts.append(entry)
inserts.sort(key=lambda i: i["T"])


def shift_at(frame):
    """Frames of inserted real media that play before a timeline point of the ORIGINAL narration."""
    return sum(i["durationFrames"] for i in inserts if frame >= i["T"] - 2)


# --- group real per-word timing into caption chunks for on-screen display ---
# Chunks never straddle an insert boundary (the words on either side of it are separated by
# the inserted media, so a chunk spanning both would sit on screen through the insert).
words = timing["captionWords"]
boundaries = [i["T"] for i in inserts]
chunks = []
cur = []
for w in words:
    wf = round(w["startSeconds"] * FPS)
    if cur:
        pf = round(cur[-1]["startSeconds"] * FPS)
        crossed = any(pf < T - 2 <= wf or (pf < T <= wf) for T in boundaries)
        if crossed or len(cur) >= WORDS_PER_CAPTION_CHUNK:
            chunks.append(cur)
            cur = []
    cur.append(w)
if cur:
    chunks.append(cur)


def fr(x):
    return round(x * FPS)


chunks_out = []
for g in chunks:
    sh = shift_at(fr(g[0]["startSeconds"]))
    chunks_out.append({
        "startFrame": fr(g[0]["startSeconds"]) + sh,
        "endFrame": fr(g[-1]["endSeconds"]) + sh,
        "words": [{"text": w["word"], "startFrame": fr(w["startSeconds"]) + sh,
                   "endFrame": fr(w["endSeconds"]) + sh} for w in g],
    })
chunks = chunks_out

# apply the shift to scenes and chapters, then place the inserts themselves
for e in scene_entries:
    e["startFrame"] += shift_at(e["startFrame"])
for c in chapters_f:
    c["startFrame"] += shift_at(c["startFrame"])
cum = 0
insert_entries = []
quiet_ranges = []
for i in inserts:
    start = i["T"] + cum
    cum += i["durationFrames"]
    e = {k: v for k, v in i.items() if k != "T"}
    e["startFrame"] = start
    insert_entries.append(e)
    quiet_ranges.append([start, start + i["durationFrames"]])
scene_entries = sorted(scene_entries + insert_entries, key=lambda e: e["startFrame"])

total_frames = round(timing["totalSeconds"] * FPS) + cum

# deterministic music-bed pick (same rule as royalty_free_music_tool's get_bed_track)
slug = os.path.basename(os.path.dirname(CASE_DIR)) or os.path.basename(CASE_DIR)
# bed_05 excluded (2026-08-01: "Dark Forest" - confirmed real YouTube Content ID
# claim in production, see Tools/royalty_free_music_tool.md). bed_04 excluded
# (2026-08-06: "Ashfall", claimant Elite Alliance Music - confirmed real Content ID
# claim on the Kevin West main video). Maps into the remaining 8 tracks instead of
# skipping numbers in the middle of the range.
_BED_POOL = [1, 2, 3, 6, 7, 8, 9, 10]
bed_n = _BED_POOL[sum(ord(c) for c in slug) % len(_BED_POOL)]
bed_src = REPO + f"/ProductionStudio/Assets/audio/music_bed/bed_{bed_n:02d}.mp3"
shutil.copyfile(bed_src, os.path.join(PUB, "bed.mp3"))

data = {
    "fps": FPS,
    "totalFrames": total_frames,
    "chapters": chapters_f,
    "quietRanges": quiet_ranges,
    "scenes": scene_entries,
    "captionChunks": chunks,
    "musicBed": f"{PUB_SUBDIR}/bed.mp3",
}

out_ts = os.path.join(REMOTION_DIR, "src", DATA_MODULE + ".ts")
with open(out_ts, "w", encoding="utf-8") as f:
    f.write("// GENERATED by prep_remotion_render.py - do not edit by hand\n")
    f.write(f"export const {DATA_EXPORT} = " + json.dumps(data, ensure_ascii=False, indent=2) + " as const;\n")

print(f"scenes: {len(scene_entries)}, caption chunks: {len(chunks)}, "
      f"total: {total_frames} frames ({total_frames/FPS/60:.2f} min)")
print(f"music bed: bed_{bed_n:02d}.mp3")
print("wrote", out_ts)
