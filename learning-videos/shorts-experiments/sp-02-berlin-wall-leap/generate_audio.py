"""SP-02 audio: Kokoro-82M voice-over + two press-camera shutter accents.
Topic: Checkpoint Charlie 1961 Standoff
Outputs (audio/):
  voiceover.mp3   final mixed track for render
  manifest.json   per-line start/end for GSAP timeline sync
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
VO_START = 0.70  # let the shutter land first, then line 1
LINE_GAP = 0.42  # crisp pause between lines
TAIL = 0.85
SHUTTER_GAIN = 0.55
SNAP_GAIN = 0.28
PEAK_TARGET_DBFS = -1.5

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
AUDIO_DIR = os.path.join(HERE, "audio")
MODEL = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
VOICES = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")

rng = np.random.default_rng(1961)


def db(x):
    return 20 * math.log10(max(float(np.sqrt(np.mean(np.square(x)))), 1e-9))


def bp_noise(n, lo, hi):
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

    if bright:
        pre = bp_noise(int(0.004 * SR), 3000, 9000) * 0.5
        sig[: len(pre)] += pre
        f_n = int(0.05 * SR)
        sig[:f_n] += bp_noise(f_n, 2500, 11000) * env(f_n, 0.0003, 0.05, 5.5) * 1.15

    return (sig / np.max(np.abs(sig))) * level


# ---------------------------------------------------------------- narration lines
# 5 Beats designed for retention & exact camera framing
LINES = [
    ("B1", "These two tanks are seventy-five yards apart."),
    ("B1", "Both had orders to fire if the other moved."),
    ("B2", "October twenty-seventh, nineteen sixty-one."),
    ("B2", "Checkpoint Charlie, Berlin."),
    ("B3", "American M-forty-eights in the foreground."),
    ("B3", "Soviet T-fifty-fives waiting across the line."),
    ("B3", "Engines idling for sixteen hours straight."),
    ("B4", "One nervous nineteen-year-old on a trigger..."),
    ("B4", "would have triggered full thermonuclear war."),
    ("B5", "Behind closed doors, Kennedy and Khrushchev blinked."),
    ("B5", "One by one, the tanks backed away."),
    ("B5", "One photo. The closest humanity ever came to the brink."),
]

FIXES = [
    (r"\b1961\b", "nineteen sixty-one"),
    (r"\bM-48s\b", "M-forty-eights"),
    (r"\bT-55s\b", "T-fifty-fives"),
]


def spoken(text):
    for pat, rep in FIXES:
        text = re.sub(pat, rep, text)
    return text


print(f"Loading Kokoro-82M from {MODEL}")
kokoro = Kokoro(MODEL, VOICES)

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


# Shutter 1: head transient (photo taken)
place(0.0, shutter(SHUTTER_GAIN, bright=True))

# Shutter 2: snap at the end of hook line 2
snap_at = entries[1]["endSec"]
place(snap_at, shutter(SNAP_GAIN, bright=False))

for start, sig in clips:
    place(start, sig)

head = int(0.002 * SR)
track[:head] *= np.linspace(0, 1, head)
tail_n = int(0.35 * SR)
track[-tail_n:] *= np.linspace(1, 0, tail_n)

raw_peak = float(np.max(np.abs(track)))
track *= (10 ** (PEAK_TARGET_DBFS / 20)) / max(raw_peak, 1e-9)

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
print(f"total {total:.2f}s | peak {20*math.log10(np.max(np.abs(track))):.1f} dBFS")
print(f"snap (2nd shutter) at {snap_at:.2f}s\n")
for e in entries:
    print(f"  {e['beat']}  {e['startSec']:>6.2f} -> {e['endSec']:>6.2f}  ({e['duration']:>4.2f}s)  {e['text']}")
