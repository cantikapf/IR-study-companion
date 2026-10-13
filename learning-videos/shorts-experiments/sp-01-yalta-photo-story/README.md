# SP-01 · Yalta Photo Story

Pilot of the **SP-xx "Single Photo, Single Story"** format: one authentic archival
photograph, editorial Ken Burns camera work, text-only narrative, and a synthesised
archival soundscape. No TTS, no vector graphics, no stock footage.

- **Export:** `learning-videos/exports/SP01_Yalta_Photo_Story_Short_1080p.mp4`
- **Spec:** 1080×1920 · 30 fps · 45.000 s · H.264 + AAC 48 kHz stereo
- **Source photo:** NARA 111-SC-260486, Public Domain (see `SOURCES.md`)

## Concept: A + D

**A — Double-Take / Replay Bait.** The first 1.2 s are a *frozen* print with no text
and no camera motion. A press-camera shutter + flash bulb fires at 0.00 s, then the
frame snaps to a mid crop at 1.20 s with a second, softer shutter. The viewer's first
thought is "did I miss something?" — which is what drives a rewatch.

**D — Archival Soundscape.** Sound does the work a voice-over would normally do:
shutter/flash at the head, radio crackle + film-projector flutter underneath. All
synthesised from noise and sine maths by `make_sfx.py` — no TTS, no samples, no
licence surface.

Both were chosen to remove the "made by AI" tells of the previous cut: the old hook
opened on a passive caption (*"Three men sat for this photo."*) over an already-moving
frame, so nothing was at stake in the first three seconds.

## Beat Sheet

| Beat | Time | Camera | Key line |
|---|---|---|---|
| 1 — Hook | 0.0–5.0 | **frozen 0–1.2**, then snap to 1.55× and drift | "Look at this photo again." → "One of these men will be dead in 60 days." |
| 2 — Roosevelt | 5.0–15.0 | push to 2.2× on the centre figure | "Not the oldest." → "The one in the middle." → "Roosevelt was dying." |
| 3 — Stalin | 15.0–25.0 | pan right, 2.05× | "Stalin sat in the center. Not by accident." → "He got it." |
| 4 — Churchill | 25.0–35.0 | pan left, 2.05× | "Churchill won the war." → "…the ingratitude of the British people." |
| 5 — Reveal | 35.0–45.0 | pull back to 1.0× | "One photo. Three empires." |

Beat 2 deliberately opens with the two lines that pay off a *wrong guess*, so the
hook's open question resolves into a small "oh" before the facts land.

## Reproduce

```bash
python make_sfx.py                 # rebuilds audio/sfx_track.mp3 (numpy + ffmpeg)
npx --yes hyperframes@0.8.150 check
npx --yes hyperframes@0.8.150 render -q delivery \
  -o "../../exports/SP01_Yalta_Photo_Story_Short_1080p.mp4"
```

## QA evidence (this build)

- `hyperframes check` — 0 errors, 0 warnings, 5/5 text passes WCAG AA.
- Audio stream present: AAC, 48 kHz, stereo; head envelope spikes at 0.00 s (−29 dB)
  and 1.20 s (−31 dB) over a −39 dB ambience floor.
- Frame 0 vs 1.0 s: mean pixel delta 0.62, 0.3 % changed → the print really is frozen.
- Frame 0 vs 0.15 s: 99.3 % changed → flash bloom fires.
- Frame 0 vs 1.6 s: 48.4 % changed, max delta 222 → snap + text land.
- Bright-pixel count in the text band (y 1300–1700) at 0.0 / 0.15 / 1.0 s = **0** —
  frame 0 is a clean, text-free poster frame.
- `pytest` 373/373 PASS.

`qa_stills/` holds the extracted evidence frames for the beats above.
