"""SP-01 archival soundscape generator (Concept D).

Builds the complete 45 s SFX bed for the Yalta photo-story short:
  - 0.00 s : large-format press-camera flash pop + shutter (the "photo taken" beat)
  - 1.20 s : softer second shutter (the snap re-frame / replay-bait cut)
  - 45.00 s: continuous radio-crackle + film-projector flutter ambience bed

No TTS, no music, no third-party samples -> zero licence surface, fully reproducible.
Run:  python make_sfx.py     (writes audio/sfx_track.mp3)
"""

import math
import os
import subprocess
import wave

import numpy as np

SR = 48000
DUR = 45.0
AMB_TARGET_DBFS = -38.0  # ambience bed loudness; the shutter sits ~30 dB above it
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")
WAV = os.path.join(OUT_DIR, "sfx_track.wav")
MP3 = os.path.join(OUT_DIR, "sfx_track.mp3")

rng = np.random.default_rng(1945)  # Yalta, for luck
N = int(SR * DUR)
events = np.zeros(N)
amb = np.zeros(N)


def db(x):
    return 20 * math.log10(max(float(np.sqrt(np.mean(np.square(x)))), 1e-9))


def add(dest, sig, at):
    i = int(at * SR)
    n = min(len(sig), N - i)
    dest[i : i + n] += sig[:n]


def env(n, attack, decay, curve=2.0):
    a = max(1, int(attack * SR))
    d = max(1, n - a)
    return np.concatenate(
        [np.linspace(0, 1, a), np.exp(-np.linspace(0, curve * 4, d))]
    )[:n]


def bp_noise(n, lo, hi):
    """Band-limited white noise via FFT brickwall (no scipy dependency)."""
    spec = rng.normal(0, 1, n) + 1j * rng.normal(0, 1, n)
    freqs = np.fft.rfftfreq(n, 1 / SR)
    spec = spec[: len(freqs)]
    spec[(freqs < lo) | (freqs > hi)] = 0
    out = np.fft.irfft(spec, n)
    peak = np.max(np.abs(out))
    return out / peak if peak else out


def shutter(level, bright):
    """Mechanical focal-plane shutter: blade transient + body knock + low thump."""
    n = int(0.09 * SR)
    body = bp_noise(n, 1600, 7000) * env(n, 0.0008, 0.09, 2.6)
    knock = bp_noise(n, 300, 2200) * env(n, 0.002, 0.07, 3.2) * 0.55
    thump_n = int(0.05 * SR)
    thump = np.sin(2 * np.pi * 118 * np.arange(thump_n) / SR) * env(
        thump_n, 0.001, 0.05, 3.0
    )
    click = body + knock
    # second blade closes ~72 ms later, softer and darker
    gap = int(0.072 * SR)
    tail = np.zeros(n)
    tail[gap:] = (bp_noise(n - gap, 500, 3000) * env(n - gap, 0.001, 0.05, 3.4)) * 0.45
    sig = np.zeros(n + int(0.05 * SR))
    sig[: len(click)] += click
    sig[: len(thump)] += thump * 0.7
    sig[: len(tail)] += tail * 0.9

    if bright:  # flash bulb: instantaneous arc pop, tiny pre-click
        f_n = int(0.05 * SR)
        pop = bp_noise(f_n, 2500, 12000) * env(f_n, 0.0003, 0.05, 5.5)
        pre = bp_noise(int(0.004 * SR), 3000, 9000) * 0.5
        sig[: len(pre)] += pre
        sig[: len(pop)] += pop * 1.15

    peak = np.max(np.abs(sig))
    return (sig / peak) * level


# ------------------------------------------------------------------ events
add(events, shutter(0.72, bright=True), 0.0)  # the photograph is taken
add(events, shutter(0.40, bright=False), 1.2)  # re-frame snap

# ---------------------------------------------------------------- ambience
n = N
t = np.arange(n) / SR

# film projector flutter (24 Hz sprocket + 48 Hz harmonic), faint and drifting
flutter = (
    np.sin(2 * np.pi * 24.0 * t + rng.uniform(0, 6)) * 0.5
    + np.sin(2 * np.pi * 48.0 * t + rng.uniform(0, 6)) * 0.25
)
flutter *= 1.0 + 0.35 * np.sin(2 * np.pi * 0.31 * t)
add(amb, flutter * 0.010, 0.0)

# radio crackle: band-limited noise, impulse-modulated, slowly breathing
bed = bp_noise(n, 300, 4200) * 0.5 + bp_noise(n, 60, 900) * 0.5
mod = np.ones(n)
for _ in range(900):  # sparse pops
    p = rng.integers(0, n - 200)
    mod[p : p + rng.integers(40, 200)] += rng.uniform(1.5, 6.0)
mod *= 1.0 + 0.5 * np.sin(2 * np.pi * 0.07 * t + 1.1)
add(amb, bed * mod * 0.30, 0.0)

# mains hum, barely there
add(amb, np.sin(2 * np.pi * 60.0 * t) * 0.004, 0.0)

# normalise the bed to a fixed loudness, then let the room arrive over 0.8 s
amb *= 10 ** (AMB_TARGET_DBFS / 20) / max(np.sqrt(np.mean(amb**2)), 1e-9)
fi = int(0.8 * SR)
amb[:fi] *= np.linspace(0, 1, fi) ** 1.6

# -------------------------------------------------------------------- mix
buf = events + amb
head = int(0.002 * SR)  # 2 ms only: must not eat the shutter transient
tail = int(0.4 * SR)
buf[:head] *= np.linspace(0, 1, head)
buf[-tail:] *= np.linspace(1, 0, tail)
buf = np.clip(buf, -1.0, 1.0)

# ----------------------------------------------------------------- output
os.makedirs(OUT_DIR, exist_ok=True)
stereo = np.stack([buf, buf], axis=1)
pcm = (stereo * 32767.0).astype("<i2").tobytes()

with wave.open(WAV, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm)

subprocess.run(
    ["ffmpeg", "-y", "-loglevel", "error", "-i", WAV, "-b:a", "192k", MP3], check=True
)
os.remove(WAV)

print(f"wrote {MP3}")
print(
    f"peak {20*math.log10(max(np.max(np.abs(buf)),1e-9)):.1f} dBFS @ "
    f"{int(np.argmax(np.abs(buf)))/SR:.3f}s | "
    f"shutter1 {db(buf[: int(0.2*SR)]):.1f} | "
    f"shutter2 {db(buf[int(1.2*SR) : int(1.4*SR)]):.1f} | "
    f"ambience {db(buf[int(5*SR) : int(40*SR)]):.1f} dBFS rms"
)
