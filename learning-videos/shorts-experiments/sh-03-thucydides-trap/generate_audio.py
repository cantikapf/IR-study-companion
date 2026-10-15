"""Audio generation for SH-03 Thucydides Trap Shorts.
Uses Kokoro-82M ONNX local ('am_adam', 1.06x speed) with precise timing and sfx mixing.
"""
import os
import json
import math
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

SR = 24000
VOICE = "am_adam"
SPEED = 1.06
LEAD_IN = 0.50
LINE_GAP = 0.40
TAIL = 1.20

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
AUDIO_DIR = os.path.join(HERE, "audio")
MODEL = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
VOICES = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")

LINES = [
    {
        "id": "beat1_hook",
        "text": "If you think peace lasts, why did 12 out of 16 great powers fail to stop world war before it broke out?",
        "subtitle": "If you think peace lasts, why did 12 out of 16 great powers fail to stop world war before it broke out?"
    },
    {
        "id": "beat2_origin",
        "text": "2,400 years ago, Greek historian Thucydides identified the pattern: 'It was the rise of Athens and the fear this instilled in Sparta that made war inevitable.'",
        "subtitle": "2,400 years ago, Greek historian Thucydides identified the pattern: 'It was the rise of Athens and the fear this instilled in Sparta that made war inevitable.'"
    },
    {
        "id": "beat3_pivot",
        "text": "Today, that chessboard shifted to the Pacific. Washington is the established superpower. Beijing is the challenger rising at historic speed.",
        "subtitle": "Today, that chessboard shifted to the Pacific. Washington is the established superpower. Beijing is the challenger rising at historic speed."
    },
    {
        "id": "beat4_chokepoint",
        "text": "China now commands the largest naval fleet on Earth. And America's defense perimeter runs straight through this 100-mile strait.",
        "subtitle": "China now commands the largest naval fleet on Earth. And America's defense perimeter runs straight through this 100-mile strait."
    },
    {
        "id": "beat5_climax",
        "text": "When the hegemon feels surrounded and the challenger feels contained, miscalculation is fatal. Are we doomed to repeat it?",
        "subtitle": "When the hegemon feels surrounded and the challenger feels contained, miscalculation is fatal. Are we doomed to repeat it?"
    }
]

def main():
    print("Loading Kokoro ONNX model...")
    kokoro = Kokoro(MODEL, VOICES)
    
    os.makedirs(AUDIO_DIR, exist_ok=True)
    manifest = []
    
    current_time = LEAD_IN
    all_audio = [np.zeros(int(LEAD_IN * SR), dtype=np.float32)]
    
    print("Synthesizing voice lines...")
    for idx, item in enumerate(LINES):
        samples, sr = kokoro.create(item["text"], voice=VOICE, speed=SPEED, lang="en-us")
        duration = len(samples) / SR
        
        start_time = round(current_time, 3)
        end_time = round(current_time + duration, 3)
        
        manifest.append({
            "id": item["id"],
            "index": idx + 1,
            "text": item["text"],
            "subtitle": item["subtitle"],
            "start": start_time,
            "end": end_time,
            "duration": round(duration, 3)
        })
        
        all_audio.append(samples.astype(np.float32))
        
        # Add gap between lines or tail at end
        gap = TAIL if idx == len(LINES) - 1 else LINE_GAP
        all_audio.append(np.zeros(int(gap * SR), dtype=np.float32))
        current_time += duration + gap
        print(f"  Line {idx+1}: {start_time}s -> {end_time}s ({duration:.2f}s)")
    
    full_audio = np.concatenate(all_audio)
    
    # Peak normalization
    peak = np.max(np.abs(full_audio))
    if peak > 0:
        target_peak = 10 ** (-1.5 / 20)
        full_audio = full_audio * (target_peak / peak)
    
    out_wav = os.path.join(AUDIO_DIR, "voiceover.wav")
    out_mp3 = os.path.join(AUDIO_DIR, "voiceover.mp3")
    manifest_path = os.path.join(AUDIO_DIR, "manifest.json")
    
    sf.write(out_wav, full_audio, SR)
    
    # Convert to MP4-ready MP3 with ffmpeg
    cmd = f'ffmpeg -y -i "{out_wav}" -codec:a libmp3lame -b:a 192k "{out_mp3}"'
    os.system(cmd)
    
    total_sec = len(full_audio) / SR
    meta = {
        "title": "The 2,400-Year War Trap",
        "duration_seconds": round(total_sec, 2),
        "total_frames_30fps": int(math.ceil(total_sec * 30)),
        "voice": VOICE,
        "sample_rate": SR,
        "lines": manifest
    }
    
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
        
    print(f"\nDone! Total duration: {total_sec:.2f}s ({meta['total_frames_30fps']} frames at 30fps)")
    print(f"Manifest written to: {manifest_path}")

if __name__ == "__main__":
    main()
