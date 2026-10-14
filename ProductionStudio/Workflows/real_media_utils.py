"""Shared helpers for real archival media (Track 3, see Tools/mugshot_fetch_tool.md and
Tools/remotion_assembly_tool.md's SceneClip / real-media-insert sections). Used by
prep_remotion_render.py and prep_short_render.py; first real use: the Stephen McCullagh case
(2026-09-18).
"""
import os
import shutil
import subprocess

_WINGET_FFMPEG = (
    "C:/Users/kurba/AppData/Local/Microsoft/WinGet/Packages/"
    "Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1.2-full_build/bin/"
)
FFMPEG = shutil.which("ffmpeg") or _WINGET_FFMPEG + "ffmpeg.exe"
FFPROBE = shutil.which("ffprobe") or _WINGET_FFMPEG + "ffprobe.exe"


def probe_duration(path):
    out = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return float(out)


def cut_clip(src, dst, duration_seconds, fps=30, start_seconds=0.0):
    """Writes a silent 1920x1080 mp4 exactly duration_seconds long. If the source clip is
    shorter than the scene it is held on its last frame (never looped - looping surveillance
    footage would read as a fake extra event); if longer, it is trimmed from the start."""
    src_dur = probe_duration(src) - start_seconds
    pad = max(0.0, duration_seconds - src_dur) + 0.25
    vf = f"fps={fps},scale=1920:1080:flags=lanczos,tpad=stop_mode=clone:stop_duration={pad:.3f}"
    subprocess.run(
        [FFMPEG, "-y", "-ss", f"{start_seconds:.3f}", "-i", src, "-an", "-vf", vf, "-t", f"{duration_seconds:.3f}",
         "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-pix_fmt", "yuv420p",
         "-bf", "0", "-g", "15", "-movflags", "+faststart", dst],
        check=True, capture_output=True,
    )


def copy_media(src, dst_dir, dst_name):
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, dst_name)
    shutil.copyfile(src, dst)
    return dst
