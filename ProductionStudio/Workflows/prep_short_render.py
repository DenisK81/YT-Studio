"""Prepare a single Short's Remotion render data: copies its narration audio,
cold-open image, scene images, and a music bed into the Remotion project's
public/ dir, and writes a TS data file matching ShortComposition.tsx's
ShortData shape - real per-word timing throughout, no estimates, same
principle as prep_remotion_render.py for the main video.

Usage:
    python prep_short_render.py <short_id> <hook_overlay_text> <cta_text> \\
        <images_dir> <audio_dir> <coldopen_image_path> <remotion_dir> [--slug SLUG]
"""
import argparse
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from real_media_utils import cut_clip

FPS = 30
COLD_OPEN_SECONDS = 1.5
CTA_SECONDS = 3.5
WORDS_PER_CAPTION_CHUNK = 3

parser = argparse.ArgumentParser()
parser.add_argument("short_id")
parser.add_argument("hook_overlay_text")
parser.add_argument("cta_text")
parser.add_argument("images_dir")
parser.add_argument("audio_dir")
parser.add_argument("coldopen_image_path")
parser.add_argument("remotion_dir")
parser.add_argument("--slug", default=None)
parser.add_argument("--coldopen-is-real", action="store_true",
                     help="Flags the cold-open image as a real photo for RealBadge overlay, see "
                          "Tools/remotion_assembly_tool.md's 'REAL badge overlay' section.")
parser.add_argument("--coldopen-source", default="",
                     help="Attribution string shown under the REAL PHOTO badge, e.g. 'D.C. Witness'.")
parser.add_argument("--cold-open-seconds", type=float, default=COLD_OPEN_SECONDS,
                     help="Length of the photo + hook-text cold open before the narration starts "
                          "(default 1.5). 0 = narration and first scene from frame 0 (A/B test variant, "
                          "added 2026-10-14 after 70%% of viewers swiped away).")
parser.add_argument("--cta-seconds", type=float, default=CTA_SECONDS,
                     help="Length of the closing CTA card (default 3.5).")
parser.add_argument("--first-scene-real", action="store_true",
                     help="Show the real cold-open photo as the first image scene under the narration "
                          "(use with --cold-open-seconds 0 so the Short still opens on a real photo). Skipped if "
                          "one of the first two scenes is already a real photo.")
args = parser.parse_args()

slug = args.slug or args.short_id
pub_subdir = f"shorts/{slug}"
PUB = os.path.join(args.remotion_dir, "public", pub_subdir)
os.makedirs(PUB, exist_ok=True)

timing_path = os.path.join(args.audio_dir, f"{args.short_id}_timing.json")
with open(timing_path, encoding="utf-8") as f:
    timing = json.load(f)

# narration audio
narration_src = os.path.join(args.audio_dir, f"{args.short_id}.mp3")
shutil.copyfile(narration_src, os.path.join(PUB, "narration.mp3"))

# cold-open image
shutil.copyfile(args.coldopen_image_path, os.path.join(PUB, "coldopen.png"))

# Quote scenes (PullQuoteCard) and real-photo scenes (RealBadge) a Short's source_scene_ids
# range might cross into - same case-root ImagePrompts.md as prep_remotion_render.py, so a
# Short reusing a main-video quote/real beat renders identically instead of crashing on a
# missing PNG. CASE_DIR isn't passed to this script; case root = two levels up from
# images_dir (.../Assets/images/<slug>) -> repo root -> Cases/<slug>.
_repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_case_slug = os.path.basename(os.path.normpath(args.images_dir))
_image_prompts_path = os.path.join(_repo_root, "ProductionStudio", "Cases", _case_slug, "ImagePrompts.md")
quote_scenes = {}
real_photo_scenes = {}
real_clip_scenes = {}
if os.path.exists(_image_prompts_path):
    with open(_image_prompts_path, encoding="utf-8") as f:
        _raw = f.read().strip()
    import re as _re
    _fence = _re.search(r"```(?:json)?\s*([\s\S]*?)```", _raw)
    if _fence:
        _raw = _fence.group(1)
    try:
        _ip_data = json.loads(_raw[_raw.index("{"): _raw.rindex("}") + 1])
        for qs in _ip_data.get("pull_quote_scenes", []):
            quote_scenes[qs["scene_id"]] = qs
        for rp in _ip_data.get("real_photo_scenes", []):
            real_photo_scenes[rp["scene_id"]] = rp
        for rc in _ip_data.get("real_clip_scenes", []):
            real_clip_scenes[rc["scene_id"]] = rc
    except (ValueError, json.JSONDecodeError):
        pass

# --first-scene-real: the real cold-open photo becomes the first scene under the narration,
# unless one of the first two scenes is already a real photo/clip or a quote card.
_lead_ids = [t_["sceneId"] for t_ in timing["scenes"][:2]]
_use_real_first = args.first_scene_real and not any(
    x in real_photo_scenes or x in real_clip_scenes for x in _lead_ids)

# scene images
scene_entries = []
for s in timing["scenes"]:
    sid = s["sceneId"]
    # A quote card in first position is replaced by the real photo (the words are in the captions).
    _first_img = _use_real_first and not scene_entries
    if sid in quote_scenes and not _first_img:
        qs = quote_scenes[sid]
        scene_entries.append({
            "sceneId": sid,
            "type": "quote",
            "quote": qs["quote"],
            "attribution": qs.get("attribution", ""),
            "startFrame": round(s["startSeconds"] * FPS),
            "durationFrames": round(s["durationSeconds"] * FPS),
        })
        continue
    if sid in real_clip_scenes:
        rc = real_clip_scenes[sid]
        lp = rc["local_path"]
        csrc = lp if os.path.isabs(lp) else os.path.join(_repo_root, lp)
        cname = sid + ".mp4"
        cut_clip(csrc, os.path.join(PUB, cname), s["durationSeconds"] + 0.15, start_seconds=rc.get("start_sec", 0.0))
        scene_entries.append({
            "sceneId": sid,
            "type": "clip",
            "src": f"{pub_subdir}/{cname}",
            "isReal": True,
            "realSource": rc.get("source", ""),
            "startFrame": round(s["startSeconds"] * FPS),
            "durationFrames": round(s["durationSeconds"] * FPS),
        })
        continue
    img_name = sid + ".png"
    is_real = sid in real_photo_scenes
    if _first_img:
        src = args.coldopen_image_path
        is_real = True
    elif is_real:
        local_path = real_photo_scenes[sid]["local_path"]
        src = local_path if os.path.isabs(local_path) else os.path.join(_repo_root, local_path)
    else:
        src = os.path.join(args.images_dir, img_name)
    shutil.copyfile(src, os.path.join(PUB, img_name))
    entry = {
        "sceneId": sid,
        "type": "image",
        "image": f"{pub_subdir}/{img_name}",
        "startFrame": round(s["startSeconds"] * FPS),
        "durationFrames": round(s["durationSeconds"] * FPS),
    }
    if is_real:
        entry["isReal"] = True
        entry["realSource"] = args.coldopen_source if _first_img else real_photo_scenes[sid].get("source", "")
    scene_entries.append(entry)

# real per-word caption chunks (center-screen, grouped 3 words)
words = timing["captionWords"]
chunks = []
for i in range(0, len(words), WORDS_PER_CAPTION_CHUNK):
    group = words[i:i + WORDS_PER_CAPTION_CHUNK]
    chunks.append({
        "startFrame": round(group[0]["startSeconds"] * FPS),
        "endFrame": round(group[-1]["endSeconds"] * FPS),
        "words": [{"text": w["word"], "startFrame": round(w["startSeconds"] * FPS),
                   "endFrame": round(w["endSeconds"] * FPS)} for w in group],
    })

cold_open_frames = round(args.cold_open_seconds * FPS)
cta_frames = round(args.cta_seconds * FPS)
narration_frames = round(timing["totalSeconds"] * FPS)
total_frames = cold_open_frames + narration_frames + cta_frames

# deterministic music-bed pick (same rule as royalty_free_music_tool's get_bed_track,
# offset by short_id so each short doesn't necessarily reuse the main video's track)
# bed_05 excluded (2026-08-01: "Dark Forest" - confirmed real YouTube Content ID
# claim in production, see Tools/royalty_free_music_tool.md). bed_04 excluded
# (2026-08-06: "Ashfall", claimant Elite Alliance Music - confirmed real Content ID
# claim on the Kevin West main video). Maps into the remaining 8 tracks instead of
# skipping numbers in the middle of the range.
_BED_POOL = [1, 2, 3, 6, 7, 8, 9, 10]
bed_n = _BED_POOL[sum(ord(c) for c in slug) % len(_BED_POOL)]
repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
bed_src = repo + f"/ProductionStudio/Assets/audio/music_bed/bed_{bed_n:02d}.mp3"
shutil.copyfile(bed_src, os.path.join(PUB, "bed.mp3"))

data = {
    "fps": FPS,
    "totalFrames": total_frames,
    "coldOpenFrames": cold_open_frames,
    "ctaFrames": cta_frames,
    "coldOpenImage": f"{pub_subdir}/coldopen.png",
    "coldOpenIsReal": bool(args.coldopen_is_real),
    "coldOpenSource": args.coldopen_source,
    "hookOverlayText": args.hook_overlay_text,
    "ctaText": args.cta_text,
    "narrationAudio": f"{pub_subdir}/narration.mp3",
    "narrationStartFrame": cold_open_frames,
    "scenes": scene_entries,
    "captionChunks": chunks,
    "musicBed": f"{pub_subdir}/bed.mp3",
}

out_ts = os.path.join(args.remotion_dir, "src", f"{slug}_data.ts")
export_name = slug.upper()
with open(out_ts, "w", encoding="utf-8") as f:
    f.write("// GENERATED by prep_short_render.py - do not edit by hand\n")
    f.write(f"export const {export_name} = " + json.dumps(data, ensure_ascii=False, indent=2) + " as const;\n")

print(f"{slug}: total {total_frames} frames ({total_frames/FPS:.1f}s), "
      f"{len(scene_entries)} scenes, {len(chunks)} caption chunks, bed_{bed_n:02d}.mp3")
print("wrote", out_ts)
