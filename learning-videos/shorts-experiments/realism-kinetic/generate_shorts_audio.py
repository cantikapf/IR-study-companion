import os
import sys
import re
import json
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

# Ensure utf-8 output on Windows
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
model_path = os.path.join(repo_root, 'simulation', 'ir-motion-library', 'models', 'kokoro', 'kokoro-v1.0.onnx')
voices_path = os.path.join(repo_root, 'simulation', 'ir-motion-library', 'models', 'kokoro', 'voices-v1.0.bin')

script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'script', 'realism_shorts_script.json')
audio_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio')
os.makedirs(audio_dir, exist_ok=True)

def normalize_phonetics(text: str) -> str:
    text = re.sub(r'\b911\b', 'nine-one-one', text)
    text = re.sub(r'\bUN\b', 'U-N', text)
    text = re.sub(r'\bIR\b', 'I-R', text)
    text = re.sub(r'\b3 S\'s\b', 'three S-es', text)
    text = re.sub(r'@IRinANutshell', 'I-R in a Nutshell', text)
    return text

print(f"Loading Kokoro-82M ONNX from: {model_path}")
kokoro = Kokoro(model_path, voices_path)

# Voice: am_adam (clear, authoritative American male) or bm_george (British male)
VOICE = 'am_adam'
SPEED = 1.05
FPS = 30
SAMPLE_RATE = 24000

with open(script_path, 'r', encoding='utf-8') as f:
    beats = json.load(f)

all_audio_chunks = []
current_sample_idx = 0
subtitles = []
beat_timestamps = []
subtitle_counter = 1

pause_between_sentences = np.zeros(int(SAMPLE_RATE * 0.20), dtype=np.float32)
pause_between_beats = np.zeros(int(SAMPLE_RATE * 0.35), dtype=np.float32)

print("\nGenerating audio beat-by-beat...")
for beat_idx, b in enumerate(beats):
    beat_id = b["id"]
    beat_name = b["beat"]
    narration = b["narration"].strip()
    
    beat_start_sample = current_sample_idx
    beat_start_sec = current_sample_idx / SAMPLE_RATE
    beat_start_frame = int(round(beat_start_sec * FPS))
    
    # Split narration into sentences
    sentences = re.split(r'(?<=[.!?])\s+', narration)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    print(f"Beat {beat_id} ({beat_name}) [{len(sentences)} sentences]: {b['title']}")
    lang = 'en-us' if VOICE.startswith('a') else 'en-gb'
    
    for s_idx, sent in enumerate(sentences):
        sent_start_sample = current_sample_idx
        sent_start_sec = current_sample_idx / SAMPLE_RATE
        sent_start_frame = int(round(sent_start_sec * FPS))
        
        spoken = normalize_phonetics(sent)
        samples, sr = kokoro.create(spoken, voice=VOICE, speed=SPEED, lang=lang)
        all_audio_chunks.append(samples)
        current_sample_idx += len(samples)
        
        sent_end_sample = current_sample_idx
        sent_end_sec = current_sample_idx / SAMPLE_RATE
        sent_end_frame = int(round(sent_end_sec * FPS))
        
        subtitles.append({
            "id": subtitle_counter,
            "beatId": beat_id,
            "beatName": beat_name,
            "sentenceIndex": s_idx + 1,
            "startSec": round(sent_start_sec, 3),
            "endSec": round(sent_end_sec, 3),
            "startFrame": sent_start_frame,
            "endFrame": sent_end_frame,
            "text": sent,
            "visual_cues": b.get("visual_cues", {})
        })
        subtitle_counter += 1
        
        if s_idx < len(sentences) - 1:
            all_audio_chunks.append(pause_between_sentences)
            current_sample_idx += len(pause_between_sentences)
            
    beat_end_sample = current_sample_idx
    beat_end_sec = current_sample_idx / SAMPLE_RATE
    beat_end_frame = int(round(beat_end_sec * FPS))
    
    beat_timestamps.append({
        "id": beat_id,
        "beat": beat_name,
        "title": b["title"],
        "startSec": round(beat_start_sec, 3),
        "endSec": round(beat_end_sec, 3),
        "durationSec": round(beat_end_sec - beat_start_sec, 3),
        "startFrame": beat_start_frame,
        "endFrame": beat_end_frame,
        "durationFrames": beat_end_frame - beat_start_frame,
        "visual_cues": b.get("visual_cues", {})
    })
    
    if beat_idx < len(beats) - 1:
        all_audio_chunks.append(pause_between_beats)
        current_sample_idx += len(pause_between_beats)

# Add 0.5s padding at end
end_padding = np.zeros(int(SAMPLE_RATE * 0.5), dtype=np.float32)
all_audio_chunks.append(end_padding)
current_sample_idx += len(end_padding)

full_audio = np.concatenate(all_audio_chunks)
total_sec = len(full_audio) / SAMPLE_RATE
total_frames = int(round(total_sec * FPS))

print(f"\nTotal audio duration: {total_sec:.2f}s ({total_frames} frames @ {FPS}fps)")

wav_output = os.path.join(audio_dir, 'voiceover.wav')
mp3_output = os.path.join(audio_dir, 'voiceover.mp3')
sf.write(wav_output, full_audio, SAMPLE_RATE)
print(f"Wrote WAV: {wav_output}")

# Convert to MP3 via ffmpeg
import subprocess
cmd = [
    'ffmpeg', '-y', '-i', wav_output,
    '-codec:a', 'libmp3lame', '-b:a', '192k',
    mp3_output
]
subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"Wrote MP3: {mp3_output}")

# Write subtitles.json and timestamps.json
subtitles_path = os.path.join(audio_dir, 'subtitles.json')
timestamps_path = os.path.join(audio_dir, 'timestamps.json')

with open(subtitles_path, 'w', encoding='utf-8') as f:
    json.dump(subtitles, f, indent=2)
print(f"Wrote subtitles: {subtitles_path}")

timestamps_manifest = {
    "fps": FPS,
    "totalDurationSec": round(total_sec, 3),
    "totalFrames": total_frames,
    "beats": beat_timestamps
}
with open(timestamps_path, 'w', encoding='utf-8') as f:
    json.dump(timestamps_manifest, f, indent=2)
print(f"Wrote timestamps manifest: {timestamps_path}")
