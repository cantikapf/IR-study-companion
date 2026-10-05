import sys
import json
import os

# Ensure repo root is in python path
sys.path.insert(0, os.path.abspath("."))

with open('simulation/openmontage_repo/remotion-composer/public/assets/crashcourse_10min_words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

from simulation.openmontage_repo.generate_10min_kokoro import ACTS

w_idx = 0
act_timings = []
for act in ACTS:
    act_num = act["act"]
    title = act["title"]
    
    start_word = words[w_idx]
    start_ms = start_word["startMs"]
    
    act_word_count = sum(len(s.strip().split()) for s in act["sentences"] if s.strip())
    end_word = words[w_idx + act_word_count - 1]
    end_ms = end_word["endMs"]
    
    act_timings.append({
        "act": act_num,
        "title": title,
        "startMs": start_ms,
        "endMs": end_ms,
        "startFrame": int(round((start_ms / 1000) * 30)),
        "endFrame": int(round((end_ms / 1000) * 30)),
        "wordCount": act_word_count
    })
    w_idx += act_word_count

print(f"Total Words Processed: {w_idx} / {len(words)}")
for t in act_timings:
    dur_frames = t["endFrame"] - t["startFrame"]
    dur_sec = (t["endMs"] - t["startMs"]) / 1000
    print(f"Act {t['act']}: {t['title']}")
    print(f"  Start: {t['startMs']}ms (Frame {t['startFrame']}) -> End: {t['endMs']}ms (Frame {t['endFrame']})")
    print(f"  Duration: {dur_sec:.2f}s ({dur_frames} frames), Words: {t['wordCount']}")
