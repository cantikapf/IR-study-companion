import os
import subprocess

AUDIO_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/audio"
BGM_SRC = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/paul-bunyan-1976/audio/battlefield_heroes.mp3"
VO_PATH = os.path.join(AUDIO_DIR, "voiceover_master.wav")
MIXED_OUT = os.path.join(AUDIO_DIR, "final_soundtrack_master.wav")

FFMPEG_BIN = "C:/ProgramData/chocolatey/bin/ffmpeg.exe"

print("Mixing SH-11 voiceover with dramatic military BGM ducked at -18 dBFS...")
cmd = [
    FFMPEG_BIN, "-y",
    "-i", VO_PATH,
    "-stream_loop", "-1", "-i", BGM_SRC,
    "-filter_complex",
    "[1:a]volume=0.12[bgm];[0:a][bgm]amix=inputs=2:duration=first:dropout_transition=2[out]",
    "-map", "[out]",
    "-c:a", "pcm_s16le",
    MIXED_OUT
]

subprocess.run(cmd, check=True)
print(f"Mixed soundtrack saved to {MIXED_OUT} ({os.path.getsize(MIXED_OUT)} bytes)")
