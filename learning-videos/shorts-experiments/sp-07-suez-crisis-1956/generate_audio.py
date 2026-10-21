import os
import json
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

REPO = "D:/PERSONAL PROJECT/IR-study-companion"
MODEL_PATH = os.path.join(REPO, "simulation/ir-motion-library/models/kokoro/kokoro-v1.0.onnx")
VOICES_PATH = os.path.join(REPO, "simulation/ir-motion-library/models/kokoro/voices-v1.0.bin")
OUT_DIR = os.path.join(REPO, "learning-videos/shorts-experiments/sp-07-suez-crisis-1956/audio")

kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

VOICE = "am_adam"
SPEED = 1.06
SR = 24000

# Approved script with Option 1 hook
lines = [
    {
        "id": "line_1",
        "scene": 1,
        "text": "In 1956, America defeated the British Empire... without firing a single bullet."
    },
    {
        "id": "line_2",
        "scene": 2,
        "text": "When Egypt nationalized the Suez Canal, Britain, France, and Israel launched a secret invasion: Operation Musketeer."
    },
    {
        "id": "line_3",
        "scene": 3,
        "text": "They expected American backing. Instead, President Eisenhower was furious. He demanded an immediate unconditional ceasefire."
    },
    {
        "id": "line_4",
        "scene": 4,
        "text": "When London refused, Washington hit their financial jugular: dumping British pounds and blocking emergency IMF loans."
    },
    {
        "id": "line_5",
        "scene": 5,
        "text": "Facing total currency collapse within days, London surrendered. The empire died not by gunfire, but by financial checkmate."
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
    
    # Save individual chunk
    sf.write(os.path.join(OUT_DIR, f"{item['id']}.wav"), samples, sample_rate)
    full_audio_chunks.append(samples)
    
    # Gap between lines (0.32s)
    gap_samples = int(0.32 * sample_rate)
    full_audio_chunks.append(np.zeros(gap_samples, dtype=np.float32))
    current_time += duration + 0.32

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
