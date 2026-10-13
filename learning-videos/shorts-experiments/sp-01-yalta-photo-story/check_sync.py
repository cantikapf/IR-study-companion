"""Self-check: every caption must reach full opacity exactly when its voice line starts.

Parses the caption tweens out of index.html and compares them against
audio/manifest.json, so a retime that drifts out of sync fails loudly instead of
being caught by eye in the render.

Run:  python check_sync.py
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

html = open(os.path.join(HERE, "index.html"), encoding="utf-8").read()
manifest = json.load(open(os.path.join(HERE, "audio", "manifest.json"), encoding="utf-8"))

# tl.to("#tN", { opacity: 1, duration: D, ... }, T);
TWEEN = re.compile(
    r'tl\.to\("#(t\d+)",\s*\{\s*opacity:\s*([01]),\s*duration:\s*([\d.]+)[^}]*\},\s*([\d.]+)\)'
)

fade_in, fade_out = {}, {}
for el, op, dur, at in TWEEN.findall(html):
    if op == "1":
        assert el not in fade_in, f"{el} fades in twice"
        fade_in[el] = (float(at), float(at) + float(dur))
    else:
        assert el not in fade_out, f"{el} fades out twice"
        fade_out[el] = float(at)

lines = manifest["lines"]
assert len(fade_in) == len(lines), f"{len(fade_in)} fade-ins vs {len(lines)} VO lines"

for i, line in enumerate(lines, start=1):
    el = f"t{i}"
    assert el in fade_in, f"{el} has no fade-in"
    start, full = fade_in[el]
    # The caption must be fully readable the moment the voice starts — not after.
    assert abs(full - line["startSec"]) <= 0.02, (
        f"{el} reaches full opacity at {full:.2f}s but the VO starts at "
        f"{line['startSec']:.2f}s (off by {full - line['startSec']:+.2f}s)"
    )
    if el in fade_out:
        assert abs(fade_out[el] - line["endSec"]) <= 0.02, (
            f"{el} starts fading at {fade_out[el]:.2f}s but the VO ends at "
            f"{line['endSec']:.2f}s"
        )
    else:
        assert i == len(lines), f"{el} never fades out and is not the closing line"

# Only one caption may be on screen at a time (otherwise two lines overlap visually).
for i, line in enumerate(lines, start=1):
    visible_until = fade_out.get(f"t{i}", manifest["totalSec"])
    nxt = fade_in.get(f"t{i + 1}")
    if nxt:
        assert nxt[0] >= visible_until, (
            f"t{i} is still fading until {visible_until:.2f}s when t{i+1} starts at {nxt[0]:.2f}s"
        )

print(f"OK — {len(lines)} captions, all in sync with audio/manifest.json "
      f"({manifest['totalSec']:.2f}s total)")
