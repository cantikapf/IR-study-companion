# -*- coding: utf-8 -*-
"""
Helper to inspect sentence timings and group them into 65+ high-density visual beats.
"""
import json

with open("simulation/openmontage_repo/sentence_timings.json", "r", encoding="utf-8") as f:
    timings = json.load(f)

acts = {}
for t in timings:
    acts.setdefault(t["act"], []).append(t)

for act_num, s_list in sorted(acts.items()):
    act_start = s_list[0]["start_frame"]
    act_end = s_list[-1]["end_frame"]
    print(f"Act {act_num}: Start {act_start} -> End {act_end} ({len(s_list)} sentences)")
