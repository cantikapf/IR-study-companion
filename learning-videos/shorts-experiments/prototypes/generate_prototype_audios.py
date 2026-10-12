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

public_proto_dir = os.path.join(repo_root, 'simulation', 'ir-motion-library', 'public', 'prototypes')
os.makedirs(public_proto_dir, exist_ok=True)

print(f"Loading Kokoro-82M ONNX from: {model_path}")
kokoro = Kokoro(model_path, voices_path)

SAMPLE_RATE = 24000
FPS = 30
pause_between = np.zeros(int(SAMPLE_RATE * 0.22), dtype=np.float32)

prototypes = [
    {
        "id": "proto1",
        "title": "The 38-Minute War",
        "voice": "bm_george", # British narrator for Anglo-Zanzibar war
        "speed": 1.05,
        "sentences": [
            "In 1896, a war began at 9:02 AM.",
            "By 9:40 AM... it was completely over.",
            "The British Royal Navy bombarded the Sultan's palace, firing 500 shells in 38 minutes.",
            "It remains the shortest war in human history."
        ]
    },
    {
        "id": "proto2",
        "title": "The Malacca Dilemma",
        "voice": "am_adam", # Authoritative American voice for geopolitics
        "speed": 1.05,
        "sentences": [
            "This narrow strip of water is just 1.5 nautical miles wide.",
            "Yet over 100,000 ships pass through every year, carrying 80% of East Asia's oil.",
            "If this chokepoint closes tomorrow... global trade collapses."
        ]
    },
    {
        "id": "proto3",
        "title": "Machiavelli's Rule",
        "voice": "bm_george", # Classical intellectual cadence
        "speed": 1.02,
        "sentences": [
            "500 years ago, Niccolò Machiavelli gave rulers one ruthless rule:",
            "It is much safer to be feared than loved.",
            "Because love is held by a fragile thread of gratitude...",
            "While fear is maintained by the dread of punishment."
        ]
    }
]

for p in prototypes:
    pid = p["id"]
    p_dir = os.path.join(public_proto_dir, pid)
    os.makedirs(p_dir, exist_ok=True)
    
    print(f"\n--- Generating {pid}: {p['title']} ({p['voice']}) ---")
    chunks = []
    current_sample = 0
    subs = []
    
    lang = 'en-gb' if p["voice"].startswith('b') else 'en-us'
    
    for s_idx, sent in enumerate(p["sentences"]):
        sent_start_sec = current_sample / SAMPLE_RATE
        sent_start_frame = int(round(sent_start_sec * FPS))
        
        # Phonetic tweaks
        spoken = sent
        spoken = re.sub(r'9:02 AM', 'nine o two A M', spoken)
        spoken = re.sub(r'9:40 AM', 'nine forty A M', spoken)
        spoken = re.sub(r'500', 'five hundred', spoken)
        spoken = re.sub(r'38', 'thirty-eight', spoken)
        spoken = re.sub(r'1\.5', 'one point five', spoken)
        spoken = re.sub(r'100,000', 'one hundred thousand', spoken)
        spoken = re.sub(r'80%', 'eighty percent', spoken)
        spoken = re.sub(r'Niccolò Machiavelli', 'Niccolo Machiavelli', spoken)
        
        samples, sr = kokoro.create(spoken, voice=p["voice"], speed=p["speed"], lang=lang)
        chunks.append(samples)
        current_sample += len(samples)
        
        sent_end_sec = current_sample / SAMPLE_RATE
        sent_end_frame = int(round(sent_end_sec * FPS))
        
        subs.append({
            "id": s_idx + 1,
            "text": sent,
            "startSec": round(sent_start_sec, 3),
            "endSec": round(sent_end_sec, 3),
            "startFrame": sent_start_frame,
            "endFrame": sent_end_frame
        })
        
        if s_idx < len(p["sentences"]) - 1:
            chunks.append(pause_between)
            current_sample += len(pause_between)
            
    # Add brief 0.5s tail
    tail = np.zeros(int(SAMPLE_RATE * 0.5), dtype=np.float32)
    chunks.append(tail)
    current_sample += len(tail)
    
    full_audio = np.concatenate(chunks)
    total_sec = len(full_audio) / SAMPLE_RATE
    total_frames = int(round(total_sec * FPS))
    
    wav_path = os.path.join(p_dir, 'voiceover.wav')
    mp3_path = os.path.join(p_dir, 'voiceover.mp3')
    sf.write(wav_path, full_audio, SAMPLE_RATE)
    
    cmd = ['ffmpeg', '-y', '-i', wav_path, '-codec:a', 'libmp3lame', '-b:a', '192k', mp3_path]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    manifest = {
        "id": pid,
        "title": p["title"],
        "fps": FPS,
        "totalSec": round(total_sec, 3),
        "totalFrames": total_frames,
        "subtitles": subs
    }
    
    with open(os.path.join(p_dir, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
        
    print(f"Generated {pid}: {total_sec:.2f}s ({total_frames} frames @ 30fps) -> {mp3_path}")

print("\nAll 3 prototype audio tracks generated successfully!")
