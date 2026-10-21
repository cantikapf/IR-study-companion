import os
import json
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

REPO = "D:/PERSONAL PROJECT/IR-study-companion"
MODEL_PATH = os.path.join(REPO, "simulation/ir-motion-library/models/kokoro/kokoro-v1.0.onnx")
VOICES_PATH = os.path.join(REPO, "simulation/ir-motion-library/models/kokoro/voices-v1.0.bin")
OUT_DIR = os.path.join(REPO, "learning-videos/shorts-experiments/sh-11-dday-ghost-army/audio")

kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

VOICE = "am_adam"
SPEED = 1.06
SR = 24000

# Script lines per brief
lines = [
    {
        "id": "line_1",
        "scene": 1,
        "text": "Could you guess what stopped 15 Nazi Panzer divisions 200 miles before D-Day failed?"
    },
    {
        "id": "line_2",
        "scene": 2,
        "text": "In 1944, the Allies created a completely fake military force: the First US Army Group, commanded by General George Patton."
    },
    {
        "id": "line_3",
        "scene": 3,
        "text": "Across the coast of Dover, soldiers inflated dummy rubber tanks, parked wooden aircraft, and broadcasted ghost radio chatter."
    },
    {
        "id": "line_4",
        "scene": 4,
        "text": "German reconnaissance fell for the trap. Hitler became convinced the real invasion would land at Pas-de-Calais, holding his best tanks 200 miles away."
    },
    {
        "id": "line_5",
        "scene": 5,
        "text": "By the time Berlin realized Normandy was the real assault, it was too late. An army of rubber balloons saved the Western world."
    },
    {
        "id": "line_6",
        "scene": 5,
        "text": "Discover more untold geopolitics on IR in a Nutshell."
    }
]

timeline = []
full_audio_chunks = []
current_time = 0.5  # 0.5s initial buffer for visual hook impact

for idx, item in enumerate(lines):
    print(f"Synthesizing {item['id']}...")
    samples, sample_rate = kokoro.create(item["text"], voice=VOICE, speed=SPEED, lang="en-us")
    duration = len(samples) / sample_rate
    
    start_t = round(current_time, 2)
    end_t = round(current_time + duration, 2)
    
    timeline.append({
        "id": item["id"],
        "scene": item["scene"],
        "text": item["text"],
        "start": start_t,
        "end": end_t,
        "duration": round(duration, 2)
    })
    
    sf.write(os.path.join(OUT_DIR, f"{item['id']}.wav"), samples, sample_rate)
    full_audio_chunks.append(samples)
    
    # Gap between lines (0.32s)
    gap_samples = int(0.32 * sample_rate)
    full_audio_chunks.append(np.zeros(gap_samples, dtype=np.float32))
    current_time += duration + 0.32

full_audio = np.concatenate(full_audio_chunks)
total_duration = len(full_audio) / SR
print(f"Total narration duration: {total_duration:.2f} seconds")

sf.write(os.path.join(OUT_DIR, "voiceover_master.wav"), full_audio, SR)

with open(os.path.join(OUT_DIR, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump({
        "total_duration": round(total_duration, 2),
        "lines": timeline
    }, f, indent=2)

print("Audio generation complete!")
