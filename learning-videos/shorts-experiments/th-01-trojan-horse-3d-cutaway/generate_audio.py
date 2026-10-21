import os
import json
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

REPO = "D:/PERSONAL PROJECT/IR-study-companion"
MODEL_PATH = os.path.join(REPO, "simulation/ir-motion-library/models/kokoro/kokoro-v1.0.onnx")
VOICES_PATH = os.path.join(REPO, "simulation/ir-motion-library/models/kokoro/voices-v1.0.bin")
OUT_DIR = os.path.join(REPO, "learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/audio")

kokoro = Kokoro(MODEL_PATH, VOICES_PATH)

VOICE = "am_adam"
SPEED = 1.06
SR = 24000

# Script lines per brief
lines = [
    {
        "id": "beat_1",
        "beat": 1,
        "text": "Could you guess how thirty Greek soldiers survived inside the Trojan Horse before Troy burned?"
    },
    {
        "id": "beat_2",
        "beat": 2,
        "text": "Built from dismantled ship timber, the belly wasn't just a hollow box. It held two narrow scaffolding tiers where soldiers sat shoulder-to-shoulder in complete silence."
    },
    {
        "id": "beat_3",
        "beat": 3,
        "text": "At thirty-five degrees Celsius, body heat alone would cause suffocation in hours. The builders hid microscopic air vents disguised inside the nostrils, ears, and horse mane."
    },
    {
        "id": "beat_4",
        "beat": 4,
        "text": "When night fell and Troy slept, Odysseus unlocked a spring-loaded trapdoor beneath the horse's belly, dropping hemp ropes to the cobblestones below."
    },
    {
        "id": "beat_5",
        "beat": 5,
        "text": "Within minutes, the gates were thrown wide open. The city that resisted a ten-year siege fell in a single night... from the inside out."
    },
    {
        "id": "beat_6",
        "beat": 5,
        "text": "Discover more untold ancient geopolitics on IR in a Nutshell."
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
        "beat": item["beat"],
        "text": item["text"],
        "start": start_t,
        "end": end_t,
        "duration": round(duration, 2)
    })
    
    sf.write(os.path.join(OUT_DIR, f"{item['id']}.wav"), samples, sample_rate)
    full_audio_chunks.append(samples)
    
    # Gap between lines (0.35s)
    gap_samples = int(0.35 * sample_rate)
    full_audio_chunks.append(np.zeros(gap_samples, dtype=np.float32))
    current_time += duration + 0.35

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
