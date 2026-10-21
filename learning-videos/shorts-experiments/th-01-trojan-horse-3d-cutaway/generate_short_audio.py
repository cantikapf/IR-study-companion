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
SPEED = 1.08  # Energetic, engaging pacing
SR = 24000

# 3 Scenes mapped directly to the 3 Veo video clips!
# Total target: ~27.5s
lines = [
    {
        "id": "scene_1_cutaway",
        "clip": "scene_1_cutaway.mp4",
        "target_sec": 10.0,
        "text": "Inside this giant wooden horse outside Troy, thirty Greek soldiers were sealed alive in thirty-five-degree heat. The hollow pine belly held two cramped tiers where warriors sat in absolute silence."
    },
    {
        "id": "scene_2_trapdoor",
        "clip": "scene_4_trapdoor.mp4",
        "target_sec": 9.5,
        "text": "At midnight, Odysseus unlocked a spring-loaded trapdoor beneath the horse, dropping hemp ropes to the cobblestones below."
    },
    {
        "id": "scene_3_outro",
        "clip": "scene_5_gates_outro.mp4",
        "target_sec": 8.0,
        "text": "They slipped into the city, opened the gates, and ended a ten-year siege in a single night. Subscribe to IR in a Nutshell."
    }
]

timeline = []
full_audio_chunks = []
current_time = 0.3  # Quick 0.3s visual punch before VO

for idx, item in enumerate(lines):
    print(f"Synthesizing {item['id']}...")
    samples, sample_rate = kokoro.create(item["text"], voice=VOICE, speed=SPEED, lang="en-us")
    duration = len(samples) / sample_rate
    
    start_t = round(current_time, 2)
    end_t = round(current_time + duration, 2)
    
    timeline.append({
        "id": item["id"],
        "clip": item["clip"],
        "text": item["text"],
        "start": start_t,
        "end": end_t,
        "duration": round(duration, 2)
    })
    
    sf.write(os.path.join(OUT_DIR, f"{item['id']}_short.wav"), samples, sample_rate)
    full_audio_chunks.append(samples)
    
    # 0.4s pause between scene cuts
    pause_samples = int(0.4 * sample_rate)
    full_audio_chunks.append(np.zeros(pause_samples, dtype=np.float32))
    current_time = end_t + 0.4

combined = np.concatenate(full_audio_chunks)
total_duration = len(combined) / sample_rate
print(f"\nTotal short VO duration: {total_duration:.2f} seconds")

# Save master short VO
vo_path = os.path.join(OUT_DIR, "voiceover_short_master.wav")
sf.write(vo_path, combined, sample_rate)

# Save timeline metadata
with open(os.path.join(OUT_DIR, "timeline_short.json"), "w") as f:
    json.dump(timeline, f, indent=2)

print("Saved voiceover_short_master.wav and timeline_short.json successfully!")
