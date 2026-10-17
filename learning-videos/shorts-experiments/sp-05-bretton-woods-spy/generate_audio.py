"""SP-05 audio: Kokoro-82M voice-over + two press-camera shutter accents.
Topic: The Soviet Spy Who Built the Global Economy (Harry Dexter White, Bretton Woods 1944)
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
VO_START = 0.70  # head shutter hits at 0.0, line 1 starts at 0.70s
LINE_GAP = 0.38  # natural, crisp pause between lines
TAIL = 0.90
SHUTTER_GAIN = 0.55
SNAP_GAIN = 0.28
PEAK_TARGET_DBFS = -1.5

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
AUDIO_DIR = os.path.join(HERE, "audio")
MODEL = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
VOICES = os.path.join(REPO, "simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")

rng = np.random.default_rng(1944)


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
# 5 Beats designed for high retention, doubt/irony hook & precise Ken Burns cues
LINES = [
    ("B1", "This quiet bureaucrat created the modern financial world."),
    ("B1", "And he was secretly working for Joseph Stalin."),
    ("B2", "His name was Harry Dexter White, top economist at the U.S. Treasury."),
    ("B2", "In nineteen forty-four, world leaders met at Bretton Woods to rebuild global trade."),
    ("B3", "British genius John Maynard Keynes brought his own grand vision."),
    ("B3", "Look at White pointing to his charts: he completely outmaneuvered Keynes."),
    ("B3", "White dethroned the British Pound and crowned the U.S. Dollar world king."),
    ("B4", "He founded the International Monetary Fund and the World Bank."),
    ("B4", "What Washington didn't know was his Soviet codename: Jurist."),
    ("B4", "For years, White funneled confidential Treasury intelligence straight to Moscow."),
    ("B5", "Exposed in nineteen forty-eight, he died of a heart attack three days after testifying."),
    ("B5", "Leaving behind the capitalist empire he built... and betrayed."),
]

FIXES = [
    (r"\bU\.S\.\b", "U S"),
    (r"\bKeynes\b", "Kaynz"),
    (r"\bSoviet\b", "Soh-vee-et"),
    (r"\bMoscow\b", "Moss-co"),
    (r"\bJurist\b", "Joo-rist"),
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

# Shutter 2: snap at the end of hook line 1
snap_at = entries[0]["endSec"]
place(snap_at, shutter(SNAP_GAIN, bright=False))

for start, sig in clips:
    place(start, sig)

head = int(0.002 * SR)
track[:head] *= np.linspace(0, 1, head)
tail_n = int(0.35 * SR)
track[-tail_n:] *= np.linspace(1, 0, tail_n)

raw_peak = float(np.max(np.abs(track)))
track *= (10 ** (PEAK_TARGET_DBFS / 20)) / max(raw_peak, 1e-9)

wav_out = os.path.join(AUDIO_DIR, "voiceover.wav")
mp3_out = os.path.join(AUDIO_DIR, "voiceover.mp3")
sf.write(wav_out, track, SR)

# convert to mp3 via ffmpeg
cmd = ["ffmpeg", "-y", "-i", wav_out, "-b:a", "192k", mp3_out]
subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if os.path.exists(wav_out):
    os.remove(wav_out)

manifest_out = os.path.join(AUDIO_DIR, "manifest.json")
with open(manifest_out, "w", encoding="utf-8") as f:
    json.dump({"lines": entries, "totalSec": round(total, 3)}, f, indent=2)

print(f"Generated {mp3_out} ({round(total, 2)}s)")
print(f"Manifest written to {manifest_out}")
