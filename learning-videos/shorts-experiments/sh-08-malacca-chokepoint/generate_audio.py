"""Generate voiceover and word alignment for SH-08 Malacca Chokepoint.
Uses Kokoro-82M ONNX model locally.
"""

import json
import os
import re
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

SR = 24000
VOICE = "am_adam"
SPEED = 1.06

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
AUDIO_DIR = os.path.join(HERE, "audio")
MODEL = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
VOICES = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")

LINES = [
    {
        "id": "line_01",
        "text": "Why you could lose your next phone if this 1.5-mile Malacca strait closes for 24 hours?",
        "spoken": "Why you could lose your next phone if this one point five mile Malacca strait closes for twenty-four hours?",
        "display": "COULD YOU LOSE YOUR PHONE IF THIS STRAIT CLOSES?",
        "highlight": "LOSE YOUR PHONE"
    },
    {
        "id": "line_02",
        "text": "This is Phillips Channel in the Strait of Malacca, the world's most congested maritime chokepoint.",
        "spoken": "This is Phillips Channel in the Strait of Malacca, the world's most congested maritime chokepoint.",
        "display": "PHILLIPS CHANNEL: WORLD'S DENSEST MARITIME CHOKEPOINT",
        "highlight": "PHILLIPS CHANNEL"
    },
    {
        "id": "line_03",
        "text": "Over 94,000 vessels squeeze through this narrow strip every year, hauling 60% of global maritime oil.",
        "spoken": "Over ninety-four thousand vessels squeeze through this narrow strip every year, hauling sixty percent of global maritime oil.",
        "display": "94,000+ VESSELS / YEAR · 60% OF GLOBAL OIL",
        "highlight": "94,000+ VESSELS"
    },
    {
        "id": "line_04",
        "text": "Even worse: nearly half of all advanced microchips from Taiwan and Korea must pass right here to reach Western factories.",
        "spoken": "Even worse: nearly half of all advanced microchips from Taiwan and Korea must pass right here to reach Western factories.",
        "display": "CRITICAL SEMICONDUCTORS TRANSIT THROUGH THIS EXACT BOTTLENECK",
        "highlight": "MICROCHIPS TRANSIT"
    },
    {
        "id": "line_05",
        "text": "If a tanker grounds or conflict erupts, rerouting around Indonesia adds 3 full days and nearly $5 billion in freight shocks.",
        "spoken": "If a tanker grounds or conflict erupts, rerouting around Indonesia adds three full days and nearly five billion dollars in freight shocks.",
        "display": "DETOUR ADDS 3 DAYS & $5 BILLION IN FREIGHT SURCHARGES",
        "highlight": "+3 DAYS & $5 BILLION"
    },
    {
        "id": "line_06",
        "text": "In modern geopolitics, the entire global economy is anchored to one and a half miles of water.",
        "spoken": "In modern geopolitics, the entire global economy is anchored to one and a half miles of water.",
        "display": "THE GLOBAL ECONOMY ANCHORED TO 1.5 MILES OF WATER",
        "highlight": "1.5 MILES OF WATER"
    }
]

def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    print("Initializing Kokoro ONNX...")
    kokoro = Kokoro(MODEL, VOICES)
    
    combined_audio = []
    manifest = []
    current_time = 0.4  # head silence
    
    # 0.4s silence samples
    head_silence = np.zeros(int(current_time * SR), dtype=np.float32)
    combined_audio.append(head_silence)
    
    for item in LINES:
        spoken_text = item["spoken"]
        print(f"Synthesizing [{item['id']}]: {spoken_text}")
        samples, sample_rate = kokoro.create(
            spoken_text,
            voice=VOICE,
            speed=SPEED,
            lang="en-us"
        )
        duration = len(samples) / sample_rate
        
        start_time = current_time
        end_time = current_time + duration
        
        manifest.append({
            "id": item["id"],
            "text": item["text"],
            "spoken": item["spoken"],
            "display": item["display"],
            "highlight": item["highlight"],
            "start": round(start_time, 2),
            "end": round(end_time, 2),
            "duration": round(duration, 2)
        })
        
        combined_audio.append(samples)
        current_time = end_time
        
        # Add pause between sentences
        pause_samples = np.zeros(int(0.25 * SR), dtype=np.float32)
        combined_audio.append(pause_samples)
        current_time += 0.25
        
    full_audio = np.concatenate(combined_audio)
    
    # Normalize peak to -1.5 dBFS
    peak = np.max(np.abs(full_audio))
    target_peak = 10 ** (-1.5 / 20.0)
    if peak > 0:
        full_audio = full_audio * (target_peak / peak)
        
    wav_path = os.path.join(AUDIO_DIR, "vo_full.wav")
    sf.write(wav_path, full_audio, SR)
    print(f"Saved full audio WAV to: {wav_path} (Duration: {current_time:.2f}s)")
    
    # Convert to MP3 via ffmpeg
    mp3_path = os.path.join(AUDIO_DIR, "vo_full.mp3")
    os.system(f'ffmpeg -y -i "{wav_path}" -b:a 192k "{mp3_path}" -loglevel error')
    print(f"Converted to MP3: {mp3_path}")
    
    manifest_path = os.path.join(AUDIO_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_duration": round(current_time, 2),
            "lines": manifest
        }, f, indent=2)
    print(f"Manifest written to: {manifest_path}")

if __name__ == "__main__":
    main()
