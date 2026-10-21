import os
import subprocess

AUDIO_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/audio"
BGM_SRC = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/paul-bunyan-1976/audio/battlefield_heroes.mp3"
VO_PATH = os.path.join(AUDIO_DIR, "voiceover_short_master.wav")
MIXED_OUT = os.path.join(AUDIO_DIR, "final_soundtrack_master.wav")

print("Mixing TH-01 short 26s voiceover with epic ancient tension BGM ducked at -18 dBFS...")
cmd = [
    "ffmpeg", "-y",
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
