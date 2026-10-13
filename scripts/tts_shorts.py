# Kokoro-82M TTS CLI for Shorts (ALTERNATE PATH)
#
# NOTE: The canonical Shorts pipeline for @IRinANutshell is the HyperFrames
# archival micro-documentary: ElevenLabs (word-level timestamps) -> manifest ->
# build_composition.py (see learning-videos/shorts-experiments/sh-01-pulau-run-hf/).
# This script is the Kokoro fallback (no network, local ONNX). It produces
# beat/caption timings WITHOUT word-level timestamps, so karaoke-style captions
# are unsupported. Prefer ElevenLabs for canonical productions.
import argparse
import json
import os
import re
import subprocess
import sys
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

# Ensure utf-8 output on Windows
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

DEFAULT_VOICE = "af_heart"
DEFAULT_SPEED = 1.08
SAMPLE_RATE = 24000
PAUSE_BETWEEN_SENTENCES = 0.28  # seconds between sentences inside a beat
PAUSE_BETWEEN_BEATS = 0.45      # seconds between beats (0.40 - 0.50s)

# Phonetic normalization rules (regex pattern -> spoken replacement).
# Applied to narration before speech synthesis ONLY; display captions remain unchanged.
PHONETIC_NORMALIZATION = {
    # Soviet devices / weapons
    r"\bRDS-1\b": "R-D-S-one",
    # Aircraft & military designations
    r"\bB-36\b": "B-thirty-six",
    r"\bB-29\b": "B-twenty-nine",
    r"\bB-52\b": "B-fifty-two",
    r"\bB-47\b": "B-forty-seven",
    r"\bB-59\b": "B-fifty-nine",
    r"\bU-2\b": "U-two",
    # Military / political acronyms
    r"\bSAC\b": "S-A-C",
    r"\bUSSR\b": "U-S-S-R",
    r"\bJCS\b": "J-C-S",
    r"\bICBM\b": "I-C-B-M",
    r"\bICBMs\b": "I-C-B-Ms",
    r"\bCIA\b": "C-I-A",
    r"\bKGB\b": "K-G-B",
    r"\bNATO\b": "NATO",
    r"\bUN\b": "U-N",
    r"\bU\.S\.\b": "U-S",
    r"\bUS\b": "U-S",
    # Explicit historical dates
    r"\b1949\b": "nineteen forty-nine",
    r"\b1957\b": "nineteen fifty-seven",
    r"\b1962\b": "nineteen sixty-two",
}

def _year_to_words(match: re.Match) -> str:
    val = int(match.group(0))
    if 1800 <= val <= 1999:
        century = "eighteen" if val < 1900 else "nineteen"
        rem = val % 100
        ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
                "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        if rem == 0:
            return f"{century} hundred"
        elif rem < 10:
            return f"{century} oh-{ones[rem]}"
        elif rem < 20:
            return f"{century} {ones[rem]}"
        else:
            t = tens[rem // 10]
            o = rem % 10
            return f"{century} {t}-{ones[o]}" if o else f"{century} {t}"
    return match.group(0)

def normalize_phonetics(text: str) -> str:
    for pattern, repl in PHONETIC_NORMALIZATION.items():
        text = re.sub(pattern, repl, text)
    # Fallback for any other 4-digit historical year (1800-1999)
    text = re.sub(r"\b(18\d{2}|19\d{2})\b", _year_to_words, text)
    return text

def find_models():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    model_path = os.path.join(repo_root, "simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
    voices_path = os.path.join(repo_root, "simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")
    if os.path.exists(model_path) and os.path.exists(voices_path):
        return model_path, voices_path

    cwd_model = os.path.join("simulation", "ir-motion-library", "models", "kokoro", "kokoro-v1.0.onnx")
    cwd_voices = os.path.join("simulation", "ir-motion-library", "models", "kokoro", "voices-v1.0.bin")
    if os.path.exists(cwd_model) and os.path.exists(cwd_voices):
        return os.path.abspath(cwd_model), os.path.abspath(cwd_voices)

    raise FileNotFoundError(f"Kokoro ONNX models not found at {model_path}")

def allocate_caption_timings(captions: list, beat_id: str, beat_start: float, beat_end: float, min_dur: float = 0.55) -> list:
    k = len(captions)
    if k == 0:
        return []

    total_dur = beat_end - beat_start
    if total_dur <= 0:
        raise ValueError(f"Beat {beat_id}: invalid duration {total_dur:.3f}s")

    texts = [c if isinstance(c, str) else c.get("text", "") for c in captions]
    lengths = [max(1, len(t.strip())) for t in texts]

    # ponytail: Water-filling proportional allocation without acoustic phoneme alignment; upgrade to whisper-timestamped if word-level karaoke is needed.
    if k == 1:
        durations = [total_dur]
    elif total_dur < k * min_dur:
        total_len = sum(lengths)
        durations = [total_dur * (l / total_len) for l in lengths]
    else:
        durations = [0.0] * k
        fixed = [False] * k
        while True:
            unfixed = [i for i in range(k) if not fixed[i]]
            if not unfixed:
                break
            alloc_fixed = sum(durations[i] for i in range(k) if fixed[i])
            rem_dur = total_dur - alloc_fixed
            rem_len = sum(lengths[i] for i in unfixed)
            violation = False
            for i in unfixed:
                prop_d = rem_dur * (lengths[i] / rem_len)
                if prop_d < min_dur:
                    durations[i] = min_dur
                    fixed[i] = True
                    violation = True
                    break
            if not violation:
                for i in unfixed:
                    durations[i] = rem_dur * (lengths[i] / rem_len)
                break

    b_start = round(beat_start, 3)
    b_end = round(beat_end, 3)
    can_enforce = (total_dur >= k * min_dur)

    res = []
    cur = b_start
    for i in range(k):
        if i == k - 1:
            nxt = b_end
        else:
            tentative = round(cur + durations[i], 3)
            if can_enforce:
                min_n = round(cur + min_dur, 3)
                max_n = round(b_end - (k - 1 - i) * min_dur, 3)
                nxt = max(min_n, min(tentative, max_n))
            else:
                nxt = max(round(cur + 0.001, 3), tentative)

        res.append({
            "startSec": cur,
            "endSec": nxt,
            "beatId": beat_id,
            "text": texts[i],
        })
        cur = nxt

    return res

def main():
    parser = argparse.ArgumentParser(description="Kokoro-82M TTS CLI for Shorts videos")
    parser.add_argument("--script", required=True, help="Path to input script.json")
    parser.add_argument("--out-dir", required=True, help="Output directory for audio and manifest")
    parser.add_argument("--voice", default=None, help=f"Kokoro voice (default: {DEFAULT_VOICE})")
    parser.add_argument("--speed", type=float, default=None, help=f"Speech speed multiplier (default: {DEFAULT_SPEED})")
    args = parser.parse_args()

    script_path = os.path.abspath(args.script)
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script file not found: {script_path}")

    with open(script_path, "r", encoding="utf-8") as f:
        script_data = json.load(f)

    # CLI args override script.json, which overrides defaults
    voice = args.voice or script_data.get("voice") or DEFAULT_VOICE
    speed = args.speed if args.speed is not None else script_data.get("speed", DEFAULT_SPEED)

    out_dir = os.path.abspath(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)

    model_path, voices_path = find_models()
    print(f"Loading Kokoro ONNX model from: {model_path}")
    kokoro = Kokoro(model_path, voices_path)
    lang = "en-gb" if voice.startswith("b") else "en-us"
    print(f"Ready. Voice: {voice}, Speed: {speed}, Lang: {lang}")

    beats = script_data.get("beats", [])
    if not beats:
        raise ValueError("script.json contains no beats")

    pause_sent_samples = np.zeros(int(SAMPLE_RATE * PAUSE_BETWEEN_SENTENCES), dtype=np.float32)
    pause_beat_samples = np.zeros(int(SAMPLE_RATE * PAUSE_BETWEEN_BEATS), dtype=np.float32)

    chunks = []
    current_sample = 0
    manifest_beats = []
    manifest_captions = []
    total_words = 0

    for b_idx, b in enumerate(beats):
        b_id = b.get("id", f"beat_{b_idx + 1}")
        narration = b.get("narration", "").strip()
        total_words += len(narration.split())

        beat_start_sample = current_sample
        spoken_narration = normalize_phonetics(narration)

        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', spoken_narration) if s.strip()]
        if not sentences and spoken_narration:
            sentences = [spoken_narration]

        print(f"Beat {b_idx + 1}/{len(beats)} [{b_id}]: {len(sentences)} sentence(s)")

        for s_idx, sent in enumerate(sentences):
            samples, _ = kokoro.create(sent, voice=voice, speed=speed, lang=lang)
            chunks.append(samples)
            current_sample += len(samples)

            if s_idx < len(sentences) - 1:
                chunks.append(pause_sent_samples)
                current_sample += len(pause_sent_samples)

        if b_idx < len(beats) - 1:
            chunks.append(pause_beat_samples)
            current_sample += len(pause_beat_samples)

        beat_end_sample = current_sample
        beat_start_sec = beat_start_sample / SAMPLE_RATE
        beat_end_sec = beat_end_sample / SAMPLE_RATE
        beat_dur = beat_end_sec - beat_start_sec

        b_meta = {k: v for k, v in b.items() if k not in ("narration", "captions")}
        b_meta["startSec"] = round(beat_start_sec, 3)
        b_meta["endSec"] = round(beat_end_sec, 3)
        b_meta["duration"] = round(beat_dur, 3)
        manifest_beats.append(b_meta)

        raw_captions = b.get("captions")
        if not raw_captions:
            raw_captions = [s.strip() for s in re.split(r'(?<=[.!?])\s+', narration) if s.strip()]
            if not raw_captions and narration:
                raw_captions = [narration]

        beat_caps = allocate_caption_timings(raw_captions, b_id, beat_start_sec, beat_end_sec)
        manifest_captions.extend(beat_caps)

    full_audio = np.concatenate(chunks)
    total_sec = len(full_audio) / SAMPLE_RATE
    total_sec_round = round(total_sec, 3)

    # Assertions: sum of beat durations equals totalSec within 0.05s
    sum_beat_dur = sum(bm["duration"] for bm in manifest_beats)
    assert abs(sum_beat_dur - total_sec_round) <= 0.05, (
        f"Sum of beat durations ({sum_beat_dur:.3f}s) does not match totalSec ({total_sec_round:.3f}s) within 0.05s"
    )

    # Assertions: caption times are monotonic and valid
    for c_idx, cap in enumerate(manifest_captions):
        assert cap["startSec"] < cap["endSec"], (
            f"Caption {c_idx} has invalid interval: {cap['startSec']} -> {cap['endSec']}"
        )
        if c_idx > 0:
            prev = manifest_captions[c_idx - 1]
            assert cap["startSec"] >= prev["endSec"] - 1e-4, (
                f"Caption {c_idx} startSec ({cap['startSec']}) before prev endSec ({prev['endSec']})"
            )

    wav_path = os.path.join(out_dir, "voiceover.wav")
    mp3_path = os.path.join(out_dir, "voiceover.mp3")
    manifest_path = os.path.join(out_dir, "manifest.json")

    sf.write(wav_path, full_audio, SAMPLE_RATE)

    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", wav_path,
        "-codec:a", "libmp3lame", "-b:a", "192k",
        mp3_path
    ]
    subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    manifest_data = {}
    if "episode" in script_data:
        manifest_data["episode"] = script_data["episode"]
    if "title" in script_data:
        manifest_data["title"] = script_data["title"]
    manifest_data["totalSec"] = total_sec_round
    manifest_data["voice"] = voice
    manifest_data["speed"] = speed
    manifest_data["sampleRate"] = SAMPLE_RATE
    manifest_data["beats"] = manifest_beats
    manifest_data["captions"] = manifest_captions

    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)

    wps = total_words / total_sec if total_sec > 0 else 0.0
    print(f"\nSynthesis complete.")
    print(f"Total duration: {total_sec_round}s ({len(full_audio)} samples @ {SAMPLE_RATE}Hz)")
    print(f"Total words: {total_words}")
    print(f"Rate: {wps:.2f} words/sec ({(wps * 60):.1f} WPM)")
    print(f"WAV: {wav_path}")
    print(f"MP3: {mp3_path}")
    print(f"Manifest: {manifest_path}")

if __name__ == "__main__":
    main()
