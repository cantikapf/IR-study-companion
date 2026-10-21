import os
import json
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

REPO = "D:/PERSONAL PROJECT/IR-study-companion"
MODEL_PATH = os.path.join(REPO, "simulation/ir-motion-library/models/kokoro/kokoro-v1.0.onnx")
VOICES_PATH = os.path.join(REPO, "simulation/ir-motion-library/models/kokoro/voices-v1.0.bin")
OUT_DIR = os.path.join(REPO, "learning-videos/shorts-experiments/paul-bunyan-1976/audio")

kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

VOICE = "am_adam"
SPEED = 1.06
SR = 24000

# Script lines per brief
lines = [
    {
        "id": "line_1",
        "scene": 1,
        "text": "In 1976, the United States deployed an entire war armada... just to cut down a single tree."
    },
    {
        "id": "line_2",
        "scene": 1,
        "text": "It started when North Korean soldiers killed two American officers attempting to trim a poplar tree blocking the DMZ view."
    },
    {
        "id": "line_3",
        "scene": 2,
        "text": "Washington refused to back down. They launched Operation Paul Bunyan."
    },
    {
        "id": "line_4",
        "scene": 2,
        "text": "813 combat engineers and troops marched in. 27 helicopters circled above."
    },
    {
        "id": "line_5",
        "scene": 3,
        "text": "Behind them? Nuclear-capable B-52 bombers, fighter jets, and an aircraft carrier battle group stood ready."
    },
    {
        "id": "line_6",
        "scene": 4,
        "text": "North Korea watched in dead silence. In 42 minutes, the tree was gone. Zero bullets fired."
    },
    {
        "id": "line_7",
        "scene": 4,
        "text": "Discover more untold geopolitics on IR in a Nutshell."
    }
]

timeline = []
full_audio_chunks = []
current_time = 0.6  # 0.6s intro buffer for Hook Ladder sound design & first visual impact

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
    
    # Save individual chunk
    sf.write(os.path.join(OUT_DIR, f"{item['id']}.wav"), samples, sample_rate)
    full_audio_chunks.append(samples)
    
    # Gap between lines (0.35s)
    gap_samples = int(0.35 * sample_rate)
    full_audio_chunks.append(np.zeros(gap_samples, dtype=np.float32))
    current_time += duration + 0.35

# Concat full audio
full_audio = np.concatenate(full_audio_chunks)
total_duration = len(full_audio) / SR
print(f"Total narration duration: {total_duration:.2f} seconds")

# Save master track
sf.write(os.path.join(OUT_DIR, "voiceover_master.wav"), full_audio, SR)

# Save manifest
with open(os.path.join(OUT_DIR, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump({
        "total_duration": round(total_duration, 2),
        "lines": timeline
    }, f, indent=2)

print("Audio generation complete!")
