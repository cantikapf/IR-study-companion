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

project_dir = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(project_dir, 'script', 'script.json')
audio_dir = os.path.join(project_dir, 'audio')
os.makedirs(audio_dir, exist_ok=True)

print(f"Loading Kokoro-82M ONNX from: {model_path}")
kokoro = Kokoro(model_path, voices_path)

SAMPLE_RATE = 24000
VOICE = 'am_adam'
SPEED = 1.10

with open(script_path, 'r', encoding='utf-8') as f:
    beats = json.load(f)

chunks = []
current_sample = 0
subtitles = []

# Pause between sentences (0.35 sec)
pause_between = np.zeros(int(SAMPLE_RATE * 0.35), dtype=np.float32)

for b_idx, b in enumerate(beats):
    text = b["text"]
    
    # Phonetic pronunciation fixes for neural TTS
    spoken = text
    spoken = re.sub(r'1962', 'nineteen sixty-two', spoken)
    spoken = re.sub(r'U-2', 'you-two', spoken)
    spoken = re.sub(r'B-59', 'B-fifty-nine', spoken)
    spoken = re.sub(r'Vasili Arkhipov', 'Vah-see-lee Ar-khee-pov', spoken)
    
    sent_start_sec = current_sample / SAMPLE_RATE
    
    samples, sr = kokoro.create(spoken, voice=VOICE, speed=SPEED, lang='en-us')
    chunks.append(samples)
    current_sample += len(samples)
    
    sent_end_sec = current_sample / SAMPLE_RATE
    
    subtitles.append({
        "id": b["id"],
        "beat": b["beat"],
        "asset": b["asset"],
        "kicker": b["kicker"],
        "headline": b["headline"],
        "text": text,
        "focus": b["focus"],
        "docket": b["docket"],
        "chips": b["chips"],
        "startSec": round(sent_start_sec, 3),
        "endSec": round(sent_end_sec, 3),
        "duration": round(sent_end_sec - sent_start_sec, 3)
    })
    
    if b_idx < len(beats) - 1:
        chunks.append(pause_between)
        current_sample += len(pause_between)

# Add 0.6s tail
tail = np.zeros(int(SAMPLE_RATE * 0.6), dtype=np.float32)
chunks.append(tail)
current_sample += len(tail)

full_audio = np.concatenate(chunks)
total_sec = len(full_audio) / SAMPLE_RATE

wav_path = os.path.join(audio_dir, 'voiceover.wav')
mp3_path = os.path.join(audio_dir, 'voiceover.mp3')

sf.write(wav_path, full_audio, SAMPLE_RATE)
cmd = ['ffmpeg', '-y', '-i', wav_path, '-codec:a', 'libmp3lame', '-b:a', '192k', mp3_path]
subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

manifest_path = os.path.join(audio_dir, 'manifest.json')
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump({
        "totalSec": round(total_sec, 3),
        "voice": VOICE,
        "speed": SPEED,
        "beats": subtitles
    }, f, indent=2)

print(f"Audio generated successfully: {mp3_path} (Total duration: {total_sec:.2f}s)")
for s in subtitles:
    print(f"  {s['id']}: {s['startSec']}s -> {s['endSec']}s ({s['duration']}s)")
