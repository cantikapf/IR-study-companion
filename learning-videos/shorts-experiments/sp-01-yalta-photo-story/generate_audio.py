"""SP-01 audio: Kokoro-82M voice-over + two press-camera shutter accents.

Replaces the earlier continuous radio-crackle bed (listener feedback: the
background texture was intrusive). The bed is gone entirely; what remains is
narration plus the two designed shutter accents that carry Concept A/D.

Outputs (audio/):
  voiceover.mp3   final mixed track for the render
  manifest.json   per-line start/end so the GSAP timeline stays in sync with the voice

Run:  python generate_audio.py
"""

import json
import math
import os
import re
import subprocess

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

SR = 24000
VOICE = "am_adam"
SPEED = 1.05
VO_START = 0.70  # let the shutter land first, then the first line
LINE_GAP = 0.45  # pause between lines
TAIL = 0.80
SHUTTER_GAIN = 0.55
SNAP_GAIN = 0.28
PEAK_TARGET_DBFS = -1.5  # leave real headroom; the raw mix summed past 0 dBFS

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
AUDIO_DIR = os.path.join(HERE, "audio")
MODEL = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
VOICES = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")

rng = np.random.default_rng(1945)


def db(x):
    return 20 * math.log10(max(float(np.sqrt(np.mean(np.square(x)))), 1e-9))


def bp_noise(n, lo, hi):
    """Band-limited white noise via FFT brickwall (no scipy)."""
    spec = rng.normal(0, 1, n) + 1j * rng.normal(0, 1, n)
    freqs = np.fft.rfftfreq(n, 1 / SR)
    spec = spec[: len(freqs)]
    spec[(freqs < lo) | (freqs > hi)] = 0
    out = np.fft.irfft(spec, n)
    peak = np.max(np.abs(out))
    return out / peak if peak else out


def env(n, attack, decay, curve=2.0):
    a = max(1, int(attack * SR))
    d = max(1, n - a)
    return np.concatenate([np.linspace(0, 1, a), np.exp(-np.linspace(0, curve * 4, d))])[:n]


def shutter(level, bright):
    """Mechanical focal-plane shutter: blade transient + body knock + low thump."""
    n = int(0.09 * SR)
    body = bp_noise(n, 1600, 7000) * env(n, 0.0008, 0.09, 2.6)
    knock = bp_noise(n, 300, 2200) * env(n, 0.002, 0.07, 3.2) * 0.55
    thump_n = int(0.05 * SR)
    thump = np.sin(2 * np.pi * 118 * np.arange(thump_n) / SR) * env(thump_n, 0.001, 0.05, 3.0)

    sig = np.zeros(n + int(0.05 * SR))
    sig[:n] += body + knock
    sig[:thump_n] += thump * 0.7

    gap = int(0.072 * SR)
    tail = bp_noise(n - gap, 500, 3000) * env(n - gap, 0.001, 0.05, 3.4) * 0.45
    sig[: len(tail)] += tail

    if bright:  # flash bulb: instantaneous arc pop with a hair of pre-click
        pre = bp_noise(int(0.004 * SR), 3000, 9000) * 0.5
        sig[: len(pre)] += pre
        f_n = int(0.05 * SR)
        sig[:f_n] += bp_noise(f_n, 2500, 11000) * env(f_n, 0.0003, 0.05, 5.5) * 1.15

    return (sig / np.max(np.abs(sig))) * level


# ---------------------------------------------------------------- narration
# One entry per on-screen line, in order. Beat boundaries drive the camera plan
# in index.html; keep the two in step when editing.
LINES = [
    ("B1", "One of these men will be dead in sixty days."),
    ("B1", "Guess which one."),
    ("B2", "Not the oldest."),
    ("B2", "The one in the middle."),
    ("B2", "Roosevelt was dying. His hands shook too badly to pour his own coffee."),
    # The photo has Churchill left, Roosevelt centre, Stalin right — so do NOT say
    # Stalin "sat in the center", which the frame visibly contradicts. What is true
    # and matches the crop is that Yalta was on Soviet soil and Stalin was the host.
    ("B3", "Stalin was the host. Not by accident."),
    ("B3", "He demanded Eastern Europe. He got it."),
    ("B4", "Churchill won the war."),
    ("B4", "Five months later, Britain voted him out."),
    ("B4", "He called it the ingratitude of the British people."),
    ("B5", "Roosevelt dead by April. Churchill out by July."),
    ("B5", "Stalin ruled for eight more years."),
    ("B5", "One photo. Three empires."),
]

# Kokoro mispronounces these; spell them the way they should sound.
FIXES = [
    (r"\b1945\b", "nineteen forty-five"),
    (r"\bYalta\b", "Yahl-ta"),
]


def spoken(text):
    for pat, rep in FIXES:
        text = re.sub(pat, rep, text)
    return text


print(f"Loading Kokoro-82M from {MODEL}")
kokoro = Kokoro(MODEL, VOICES)

# ------------------------------------------------------------------ render VO
clips, entries = [], []
cursor = VO_START
for beat, text in LINES:
    samples, _ = kokoro.create(spoken(text), voice=VOICE, speed=SPEED, lang="en-us")
    samples = np.asarray(samples, dtype=np.float32)
    start, end = cursor, cursor + len(samples) / SR
    entries.append(
        {
            "beat": beat,
            "text": text,
            "startSec": round(start, 3),
            "endSec": round(end, 3),
            "duration": round(end - start, 3),
        }
    )
    clips.append((start, samples))
    cursor = end + LINE_GAP

total = cursor - LINE_GAP + TAIL
N = int(total * SR)
track = np.zeros(N, dtype=np.float32)


def place(at, sig):
    i = int(at * SR)
    n = min(len(sig), N - i)
    track[i : i + n] += sig[:n]


# The shutter fires first (the photograph is taken), then the voice arrives.
place(0.0, shutter(SHUTTER_GAIN, bright=True))

# The second shutter marks the hard snap into Roosevelt, at the end of the hook.
snap_at = entries[1]["endSec"]
place(snap_at, shutter(SNAP_GAIN, bright=False))

for start, sig in clips:
    place(start, sig)

# 2 ms head ramp only — a longer fade would swallow the shutter transient.
head = int(0.002 * SR)
track[:head] *= np.linspace(0, 1, head)
tail_n = int(0.35 * SR)
track[-tail_n:] *= np.linspace(1, 0, tail_n)

# The raw sum of shutter + narration can exceed 0 dBFS, so scale the finished
# mix to a fixed peak instead of hard-clipping it.
raw_peak = float(np.max(np.abs(track)))
track *= (10 ** (PEAK_TARGET_DBFS / 20)) / max(raw_peak, 1e-9)

# -------------------------------------------------------------------- output
os.makedirs(AUDIO_DIR, exist_ok=True)
wav = os.path.join(AUDIO_DIR, "voiceover.wav")
mp3 = os.path.join(AUDIO_DIR, "voiceover.mp3")
sf.write(wav, track, SR)
subprocess.run(
    ["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-ar", "48000", "-b:a", "192k", mp3],
    check=True,
)
os.remove(wav)

with open(os.path.join(AUDIO_DIR, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(
        {
            "totalSec": round(total, 3),
            "voice": VOICE,
            "speed": SPEED,
            "snapSec": round(snap_at, 3),
            "lines": entries,
        },
        f,
        indent=2,
    )

print(f"\nwrote {mp3}")
print(f"total {total:.2f}s | peak {20*math.log10(np.max(np.abs(track))):.1f} dBFS | "
      f"vo rms {db(track[int(VO_START*SR):int((VO_START+8)*SR)]):.1f} dB")
print(f"snap (2nd shutter) at {snap_at:.2f}s\n")
for e in entries:
    print(f"  {e['beat']}  {e['startSec']:>6.2f} -> {e['endSec']:>6.2f}  ({e['duration']:>4.2f}s)  {e['text']}")
