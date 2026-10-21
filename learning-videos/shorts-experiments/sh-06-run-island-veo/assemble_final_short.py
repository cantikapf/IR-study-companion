"""Stitch and render final Vox-style YouTube Shorts video.
Uses:
- clip1_galleon_veo_argon.mp4 (00:00 - 00:08)
- clip2_nutmeg_vox_argon.mp4 (00:08 - 00:16)
- clip3_naval_siege_vox_argon.mp4 (00:16 - 00:26)
- clip4_treaty_breda_vox_argon.mp4 (00:26 - 00:35)
- Audio: voiceover.mp3 (34.75s)
- Subtitles: vox_captions.ass (burned directly via libass filter)
Output:
- local: learning-videos/shorts-experiments/sh-06-run-island-veo/sh06_the_island_traded_for_new_york_vox_1080p.mp4
- exports: learning-videos/exports/SH06_The_Island_Traded_for_New_York_Short_1080p.mp4
"""

import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS_DIR = os.path.join(HERE, "clips")
AUDIO = os.path.join(HERE, "audio", "voiceover.mp3")
ASS_FILE = os.path.join(HERE, "vox_captions.ass").replace("\\", "/")
LOCAL_OUT = os.path.join(HERE, "sh06_the_island_traded_for_new_york_vox_1080p.mp4")
EXPORTS_DIR = os.path.abspath(os.path.join(HERE, "../../../learning-videos/exports"))
EXPORTS_OUT = os.path.join(EXPORTS_DIR, "SH06_The_Island_Traded_for_New_York_Short_1080p.mp4")

# Trim clips to exact beat timeline
# Total audio: 34.75s
# Clip 1 (Galleon Arrival): 8.5s
# Clip 2 (Nutmeg Mace): 7.5s
# Clip 3 (Naval Siege Fort): 10.5s
# Clip 4 (Manhattan vs Run Island exchange): 8.25s
# Sum: 34.75s

def main():
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    c1 = os.path.join(CLIPS_DIR, "clip1_galleon_veo_argon.mp4")
    c2 = os.path.join(CLIPS_DIR, "clip2_nutmeg_vox_argon.mp4")
    c3 = os.path.join(CLIPS_DIR, "clip3_naval_siege_vox_argon.mp4")
    c4 = os.path.join(CLIPS_DIR, "clip4_treaty_breda_vox_argon.mp4")

    # Filter complex using relative path to ASS
    filter_complex = (
        "[0:v]trim=0:8.5,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30[v0];"
        "[1:v]trim=0:7.5,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30[v1];"
        "[2:v]trim=0:10.5,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30[v2];"
        "[3:v]trim=0:8.25,setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30[v3];"
        "[v0][v1][v2][v3]concat=n=4:v=1:a=0,ass=vox_captions.ass[v]"
    )

    cmd = [
        "ffmpeg", "-y",
        "-i", c1,
        "-i", c2,
        "-i", c3,
        "-i", c4,
        "-i", AUDIO,
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "4:a",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        LOCAL_OUT
    ]

    print("Running ffmpeg assembly...")
    subprocess.run(cmd, check=True)
    print(f"Rendered local output: {LOCAL_OUT} ({os.path.getsize(LOCAL_OUT)} bytes)")

    # Copy to exports
    import shutil
    shutil.copy2(LOCAL_OUT, EXPORTS_OUT)
    print(f"Propagated to exports: {EXPORTS_OUT} ({os.path.getsize(EXPORTS_OUT)} bytes)")

if __name__ == "__main__":
    main()
