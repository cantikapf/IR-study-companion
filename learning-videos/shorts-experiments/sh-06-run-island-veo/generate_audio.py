"""Generate voiceover and word alignment for Run Island Vox explainer.
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
SPEED = 1.05

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
AUDIO_DIR = os.path.join(HERE, "audio")
MODEL = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
VOICES = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")

LINES = [
    {
        "id": "line_01",
        "text": "You think Manhattan was bought with cash.",
        "display": "YOU THINK MANHATTAN WAS BOUGHT WITH CASH",
        "highlight": "CASH"
    },
    {
        "id": "line_02",
        "text": "In sixteen sixty-seven, Britain traded New York for a three-kilometer island in Indonesia.",
        "display": "BRITAIN TRADED NEW YORK FOR A 3KM ISLAND",
        "highlight": "TRADED NEW YORK"
    },
    {
        "id": "line_03",
        "text": "Pulau Run, hidden in Indonesia's Banda Sea, the world's only source of nutmeg.",
        "display": "INDONESIA'S BANDA ISLANDS: THE WORLD'S ONLY NUTMEG",
        "highlight": "BANDA ISLANDS"
    },
    {
        "id": "line_04",
        "text": "Back then, one sack of nutmeg bought an entire estate in London.",
        "display": "NUTMEG WAS WORTH MORE THAN GOLD",
        "highlight": "MORE THAN GOLD"
    },
    {
        "id": "line_05",
        "text": "Thirty-nine British sailors held the island under Dutch naval siege for fifteen hundred days.",
        "display": "39 DEFENDERS UNDER NAVAL SIEGE",
        "highlight": "NAVAL SIEGE"
    },
    {
        "id": "line_06",
        "text": "To end the war, Britain kept Manhattan, while the Dutch seized full control of the spice trade.",
        "display": "1667 TREATY OF BREDA SEALED THE DEAL",
        "highlight": "TREATY OF BREDA"
    },
    {
        "id": "line_07",
        "text": "Today, Manhattan is worth trillions. And Run is a quiet village of fifteen hundred people.",
        "display": "MANHATTAN BECAME WALL STREET",
        "highlight": "WALL STREET"
    },
    {
        "id": "line_08",
        "text": "The worst real estate trade in human history.",
        "display": "THE WORST TRADE IN HUMAN HISTORY",
        "highlight": "WORST TRADE"
    }
]

def main():
    os.makedirs(AUDIO_DIR, exist_ok=True)
    print("Initializing Kokoro ONNX...")
    kokoro = Kokoro(MODEL, VOICES)
    
    combined_audio = []
    manifest = []
    current_time = 0.5  # head silence
    
    # Prepend silence
    combined_audio.append(np.zeros(int(current_time * SR), dtype=np.float32))
    
    for item in LINES:
        text = item["text"]
        print(f"Synthesizing [{item['id']}]: {text}")
        samples, _ = kokoro.create(text, voice=VOICE, speed=SPEED, lang="en-us")
        duration = len(samples) / SR
        
        start_time = current_time
        end_time = start_time + duration
        
        manifest.append({
            "id": item["id"],
            "text": item["text"],
            "display": item["display"],
            "highlight": item["highlight"],
            "start": round(start_time, 2),
            "end": round(end_time, 2),
            "duration": round(duration, 2)
        })
        
        combined_audio.append(samples)
        
        # Add pause between lines (0.35s)
        gap = 0.35
        combined_audio.append(np.zeros(int(gap * SR), dtype=np.float32))
        current_time = end_time + gap
        
    full_audio = np.concatenate(combined_audio)
    out_wav = os.path.join(AUDIO_DIR, "voiceover.wav")
    out_mp3 = os.path.join(AUDIO_DIR, "voiceover.mp3")
    
    sf.write(out_wav, full_audio, SR)
    print(f"Wrote {out_wav} (total duration: {len(full_audio)/SR:.2f}s)")
    
    # Convert to mp3 via ffmpeg
    import subprocess
    cmd = ["ffmpeg", "-y", "-i", out_wav, "-b:a", "192k", out_mp3]
    subprocess.run(cmd, check=True)
    print(f"Converted to {out_mp3}")
    
    out_manifest = os.path.join(AUDIO_DIR, "manifest.json")
    with open(out_manifest, "w", encoding="utf-8") as f:
        json.dump({"total_duration": round(len(full_audio)/SR, 2), "lines": manifest}, f, indent=2)
    print(f"Saved manifest to {out_manifest}")

if __name__ == "__main__":
    main()
