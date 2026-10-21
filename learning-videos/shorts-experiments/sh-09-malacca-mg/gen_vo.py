"""Generate SH-09 voiceover with Kokoro-82M (local ONNX).

Wording is deliberately plain-language: no VLCC, no "draft", no "keel",
no "Phillips Channel". Every number is from the verified fact gate in SCRIPT.md.

Run: py -3.13 gen_vo.py
"""

import json
import os
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

SR = 24000
VOICE = "af_heart"
SPEED = 0.93         # targets the 140-155 wpm band from voice.md
GAP = 0.42           # silence between beats

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
AUDIO = os.path.join(HERE, "audio")
MODEL = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
VOICES = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")

# beat -> (text, slot seconds in the composition)
BEATS = [
    (1, "Two landmasses. One channel between them. One point five nautical miles of water. "
        "And no second option.", 8.0),
    (2, "At its narrowest it is two point eight kilometres across. Wide enough for most ships. "
        "Only just.", 9.5),
    (3, "A fully loaded supertanker sits twenty point five metres underwater. The seabed is "
        "twenty five metres down. That leaves four point five metres of water under the hull.",
        11.0),
    (4, "So why not go around? The Sunda route is shallower still. Big tankers have to run east, "
        "past Lombok, through Makassar.", 9.0),
    (5, "You cannot widen a strait. Chokepoints do not create risk. They concentrate it.", 7.5),
]


def main():
    os.makedirs(AUDIO, exist_ok=True)
    k = Kokoro(MODEL, VOICES)

    manifest = {"voice": VOICE, "sr": SR, "speed": SPEED, "lines": []}
    cursor = 0.0
    full = []

    for idx, (beat, text, slot) in enumerate(BEATS):
        samples, sr = k.create(text, voice=VOICE, speed=SPEED, lang="en-us")
        samples = np.asarray(samples, dtype=np.float32).reshape(-1)
        dur = len(samples) / sr

        name = f"beat_{beat}.wav"
        sf.write(os.path.join(AUDIO, name), samples, sr)

        fits = dur <= slot
        manifest["lines"].append({
            "beat": beat,
            "text": text,
            "file": name,
            "start": round(cursor, 3),
            "duration": round(dur, 3),
            "end": round(cursor + dur, 3),
            "slot": slot,
            "fits": fits,
            "overflow": round(max(0.0, dur - slot), 3),
        })
        print(f"beat {beat}: {dur:.2f}s / slot {slot}s  {'OK' if fits else 'OVER by ' + format(dur - slot, '.2f') + 's'}")

        full.append(samples)
        cursor += dur
        # pad to the next beat boundary so picture and voice stay locked
        pad_to = sum(b[2] for b in BEATS[:idx + 1])
        pad = int(max(0, pad_to - cursor) * sr)
        if pad:
            full.append(np.zeros(pad, dtype=np.float32))
            cursor += pad / sr
        manifest["lines"][-1]["place_at"] = round(sum(b[2] for b in BEATS[:idx]), 3)

    track = np.concatenate(full) if full else np.zeros(1, dtype=np.float32)
    sf.write(os.path.join(AUDIO, "vo_full.wav"), track, SR)

    total = len(track) / SR
    speech = sum(l["duration"] for l in manifest["lines"])
    words = sum(len(t.split()) for _, t, _ in BEATS)
    manifest["total_duration"] = round(total, 3)
    manifest["speech_duration"] = round(speech, 3)
    manifest["words"] = words
    manifest["wpm"] = round(words / (speech / 60), 1)
    with open(os.path.join(AUDIO, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"\ntrack: {total:.2f}s (padded to slots)")
    print(f"speech: {speech:.2f}s · {words} words · {manifest['wpm']} wpm")


if __name__ == "__main__":
    main()
