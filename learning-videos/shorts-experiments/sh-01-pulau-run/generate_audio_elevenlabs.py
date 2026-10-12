"""
Phase 2 audio synthesis for SH-01 (Pulau Run).
ElevenLabs with-timestamps -> per-beat mp3 + word-level manifest.json.

Run from anywhere:  python generate_audio_elevenlabs.py
Requires ELEVENLABS_API_KEY in ~/.hermes/.env and ffmpeg on PATH.
"""
import os, sys, json, base64, subprocess, urllib.request, urllib.error

sys.stdout.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "script", "script.json")
AUDIO_DIR = os.path.join(HERE, "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # George - Captivating Storyteller
MODEL_ID = "eleven_multilingual_v2"
FPS = 30
GAP_MP3 = 0.30  # silence inserted between beats, seconds
VOICE_SETTINGS = {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True}


def load_key():
    env = os.path.join(os.path.expanduser("~"), "AppData", "Local", "hermes", ".env")
    with open(env, encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("ELEVENLABS_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("ELEVENLABS_API_KEY not found in " + env)


def synth(key, text):
    url = (f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
           f"/with-timestamps?output_format=mp3_44100_128")
    body = json.dumps({"text": text, "model_id": MODEL_ID, "voice_settings": VOICE_SETTINGS}).encode()
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "xi-api-key": key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ElevenLabs HTTP {e.code}: {e.read().decode()[:400]}")


def dur(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
                                   "format=duration", "-of", "csv=p=0", path])
    return float(out.strip())


def main():
    key = load_key()
    with open(SCRIPT, encoding="utf-8") as f:
        beats = json.load(f)

    gap = os.path.join(AUDIO_DIR, "_gap.mp3")
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i",
                    f"anullsrc=r=44100:cl=mono", "-t", str(GAP_MP3),
                    "-q:a", "9", gap], check=True, capture_output=True)

    offset = 0.0
    manifest_beats = []
    concat_list = []
    for b in beats:
        data = synth(key, b["text"])
        mp3 = os.path.join(AUDIO_DIR, f"{b['id']}.mp3")
        with open(mp3, "wb") as f:
            f.write(base64.b64decode(data["audio_base64"]))
        d = dur(mp3)
        al = data.get("alignment") or {}
        chars = al.get("characters", [])
        cs = al.get("character_start_times_seconds", [])
        ce = al.get("character_end_times_seconds", [])
        # group chars into words for subtitle karaoke
        words, cur, wstart = [], "", None
        for ch, s, e in zip(chars, cs, ce):
            if ch.isspace():
                if cur:
                    words.append({"w": cur, "start": round(wstart + offset, 3),
                                  "end": round(e + offset, 3)})
                    cur, wstart = "", None
            else:
                if wstart is None:
                    wstart = s
                cur += ch
        if cur:
            words.append({"w": cur, "start": round(wstart + offset, 3),
                          "end": round(ce[-1] + offset, 3)})

        start, end = offset, offset + d
        manifest_beats.append({
            "id": b["id"], "beat": b["beat"], "asset": b["asset"],
            "kicker": b["kicker"], "headline": b["headline"], "text": b["text"],
            "focus": b.get("focus", ""),
            "startSec": round(start, 3), "endSec": round(end, 3),
            "startFrame": int(round(start * FPS)), "endFrame": int(round(end * FPS)),
            "words": words,
        })
        concat_list += [mp3, gap]
        offset = end + GAP_MP3
        print(f"  {b['id']}: {d:.2f}s  ({len(words)} words)")

    full = os.path.join(AUDIO_DIR, "vo_full.mp3")
    lst = os.path.join(AUDIO_DIR, "_concat.txt")
    with open(lst, "w", encoding="utf-8") as f:
        for p in concat_list[:-1]:  # drop trailing gap
            f.write(f"file '{p.replace(os.sep, '/')}'\n")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c", "copy", full], check=True, capture_output=True)
    total = dur(full)

    manifest = {"title": "The Island Traded for Manhattan: Pulau Run & The 1667 Treaty of Breda",
                "voice": "George - Captivating Storyteller", "voiceId": VOICE_ID,
                "model": MODEL_ID, "fps": FPS,
                "totalSec": round(total, 3), "totalFrames": int(round(total * FPS)),
                "beats": manifest_beats}
    with open(os.path.join(AUDIO_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f"\nTOTAL: {total:.2f}s / {int(round(total*FPS))} frames -> audio/manifest.json")


if __name__ == "__main__":
    main()
