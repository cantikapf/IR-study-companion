import os
import sys
import re
import json
import numpy as np
import soundfile as sf
import subprocess
from kokoro_onnx import Kokoro

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
model_path = os.path.join(repo_root, 'simulation', 'ir-motion-library', 'models', 'kokoro', 'kokoro-v1.0.onnx')
voices_path = os.path.join(repo_root, 'simulation', 'ir-motion-library', 'models', 'kokoro', 'voices-v1.0.bin')

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script', 'script.json')
audio_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio')
public_dir = os.path.join(repo_root, 'simulation', 'ir-motion-library', 'public', 'archival_proto')
os.makedirs(public_dir, exist_ok=True)
os.makedirs(audio_dir, exist_ok=True)

print(f"Loading Kokoro-82M ONNX from: {model_path}")
kokoro = Kokoro(model_path, voices_path)

SAMPLE_RATE = 24000
FPS = 30
VOICE = 'am_adam' # Deep authoritative narrator voice
SPEED = 1.08

with open(script_path, 'r', encoding='utf-8') as f:
    beats = json.load(f)

chunks = []
current_sample = 0
subtitles = []

# Natural pause between sentences (0.28 sec)
pause_between = np.zeros(int(SAMPLE_RATE * 0.28), dtype=np.float32)

for b_idx, b in enumerate(beats):
    text = b["text"]
    
    # Phonetic pronunciation fixes for neural TTS
    spoken = text
    spoken = re.sub(r'1667', 'sixteen sixty-seven', spoken)
    spoken = re.sub(r'1664', 'sixteen sixty-four', spoken)
    spoken = re.sub(r'uti possidetis', 'oo-tee poss-ee-day-tees', spoken)
    spoken = re.sub(r'Breda', 'Bray-dah', spoken)
    spoken = re.sub(r'Banda', 'Bahn-dah', spoken)
    spoken = re.sub(r'Maluku', 'Mah-loo-koo', spoken)
    spoken = re.sub(r'Pulau Run', 'Poo-lau Roon', spoken)
    spoken = re.sub(r'Courthope', 'Court-hope', spoken)
    
    sent_start_sec = current_sample / SAMPLE_RATE
    sent_start_frame = int(round(sent_start_sec * FPS))
    
    samples, sr = kokoro.create(spoken, voice=VOICE, speed=SPEED, lang='en-us')
    chunks.append(samples)
    current_sample += len(samples)
    
    sent_end_sec = current_sample / SAMPLE_RATE
    sent_end_frame = int(round(sent_end_sec * FPS))
    
    subtitles.append({
        "id": b["id"],
        "beat": b["beat"],
        "asset": b["asset"],
        "kicker": b["kicker"],
        "headline": b["headline"],
        "text": text,
        "focus": b["focus"],
        "startSec": round(sent_start_sec, 3),
        "endSec": round(sent_end_sec, 3),
        "startFrame": sent_start_frame,
        "endFrame": sent_end_frame
    })
    
    if b_idx < len(beats) - 1:
        chunks.append(pause_between)
        current_sample += len(pause_between)

# Add 0.5s tail
tail = np.zeros(int(SAMPLE_RATE * 0.5), dtype=np.float32)
chunks.append(tail)
current_sample += len(tail)

full_audio = np.concatenate(chunks)
total_sec = len(full_audio) / SAMPLE_RATE
total_frames = int(round(total_sec * FPS))

wav_path = os.path.join(audio_dir, 'voiceover.wav')
mp3_path = os.path.join(audio_dir, 'voiceover.mp3')
public_mp3 = os.path.join(public_dir, 'voiceover.mp3')

sf.write(wav_path, full_audio, SAMPLE_RATE)
cmd = ['ffmpeg', '-y', '-i', wav_path, '-codec:a', 'libmp3lame', '-b:a', '192k', mp3_path]
subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

import shutil
shutil.copy2(mp3_path, public_mp3)

manifest = {
    "title": "The Island Traded for Manhattan: Pulau Run & The 1667 Treaty of Breda",
    "fps": FPS,
    "totalSec": round(total_sec, 3),
    "totalFrames": total_frames,
    "beats": subtitles
}

with open(os.path.join(audio_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)
with open(os.path.join(public_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)

print(f"Generated Archival Audio: {total_sec:.2f}s ({total_frames} frames @ {FPS}fps)")
print(f"Saved to: {mp3_path} and {public_mp3}")
