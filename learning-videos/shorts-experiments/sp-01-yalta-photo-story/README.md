# SP-01 · Yalta Photo Story

Pilot of the **SP-xx "Single Photo, Single Story"** format: one authentic archival
photograph, editorial Ken Burns camera work, a Kokoro-82M voice-over, and two
synthesised press-camera shutter accents. No vector graphics, no stock footage.

- **Export:** `learning-videos/exports/SP01_Yalta_Photo_Story_Short_1080p.mp4`
- **Spec:** 1080×1920 · 30 fps · 33.18 s · H.264 + AAC 48 kHz stereo
- **Source photo:** NARA 111-SC-260486, Public Domain (see `SOURCES.md`)

## Concepts Applied

**A — Hook with stakes, camera frozen.** The print is a full-bleed 2332×1920 element
(no letterboxing, no background band). The camera holds still for the first 1.2 s —
there is no camera *motion* — but the information is not frozen: the hook line
*"One of these men will be dead in 60 days."* is up by **0.45 s** (frame 14), so frame 0
stays a clean poster frame while the viewer is never left with a silent, unexplained
photograph. A press-camera shutter + flash bulb fires at 0.00 s, the frame hard-snaps
to Roosevelt at 1.20 s (the double-take), snaps back out at 2.92 s so the question
*"Guess which one."* lands on all three faces, and at **4.39 s** the second shutter
fires as the camera snaps back onto Roosevelt — the payoff of the wrong guess.

**B — Voice-over (Kokoro-82M, `am_adam`, speed 1.05).** The narration drives the edit:
`generate_audio.py` renders each line, writes the exact start/end of every line to
`audio/manifest.json`, and the GSAP timeline in `index.html` is derived from those
numbers. Captions are one element per spoken line, so the caption track *is* the
transcript. Total 33.55 s across five beats.

**D — Archival soundscape, reduced.** The first cut carried a continuous radio-crackle
and film-projector bed. It read as intrusive on playback, so the bed is gone: what
remains is the two momentary shutter accents (90 ms each) that carry Concept A's
double-take. Synthesised from noise and sine maths in `generate_audio.py` — no music,
no third-party samples, zero licence surface.

These remove the "made by AI" tells of the first cut (which opened on a passive caption
over an already-moving letterboxed frame with nothing at stake in the first 3 s).

## Framing & Grading Notes (the "empty bottom" fix)

- The 2720×2239 print is rendered at 2332×1920 (matches the frame aspect to 0.02 %),
  so at `scale 1, ty 0` the photograph fills the canvas edge to edge; `transform-origin`
  is `0 0` and camera moves are `translate(tx,ty) scale(s)` with an explicit subject
  centring formula documented in `index.html`.
- The vertical luminance profile of the print was measured before choosing scrim
  numbers: the last rows (v1800–1920) still carry ~77 % of pixels above luma 45. The
  bottom scrim therefore concentrates density ON the text band (y~1150–1550) and falls
  away below it, and the vignette is a weak large ellipse — a band measuring 0–2 % of
  pixels above luma 45 in the rendered frame is treated as a bug, not a style.
- Film grain (feTurbulence data-URI, opacity 0.085, overlay blend) over the frame so
  the scrim's flat gradient reads as archival film.

## Camera Timing Rule

Each subject pan **arrives before the caption that names its subject**: the sweep to
Stalin runs 10.20 → 12.00 s so the frame is on him when *"Stalin sat in the center."*
lands at 12.12 s, and the sweep to Churchill runs 15.89 → 17.89 s for the same reason.
Starting a pan on its own caption leaves the previous man on screen while the text
names the next one — a mismatch that neither `hyperframes check` nor a pixel diff
catches, only looking at the frame at the caption's onset does.

## Beat Sheet

Beat times are the voice-over line windows from `audio/manifest.json`; the camera plan
in `index.html` is keyed to them.

| Beat | Time | Camera | Voice-over |
|---|---|---|---|
| 1 — Hook | 0.00–4.39 | frozen 0–1.20, snap to 1.62× at 1.20, snap back to 1.0× at 2.92, snap in again at 4.39 (2nd shutter) | "One of these men will be dead in 60 days." (0.70) → "Guess which one." (3.45) |
| 2 — Roosevelt | 4.39–12.12 | hold at 1.68× on the centre figure | "Not the oldest." → "The one in the middle." → "Roosevelt was dying. His hands shook too badly to pour his own coffee." |
| 3 — Stalin | 12.12–17.52 | pan right, 1.68× | "Stalin was the host. Not by accident." → "He demanded Eastern Europe. He got it." |
| 4 — Churchill | 17.52–24.72 | pan left, 1.68× | "Churchill won the war." → "Five months later, Britain voted him out." → "…the ingratitude of the British people." |
| 5 — Reveal | 24.72–33.18 | pull back to 1.0× | "Roosevelt dead by April. Churchill out by July." → "Stalin ruled for eight more years." → "One photo. Three empires." |

Beat 2 deliberately opens with the two lines that pay off a *wrong guess*, so the
hook's open question resolves into a small "oh" before the facts land. The closing line
holds on screen to the final frame.

## Reproduce

```bash
python generate_audio.py           # Kokoro VO + shutter accents -> audio/voiceover.mp3 + manifest.json
npx --yes hyperframes@0.8.150 check
npx --yes hyperframes@0.8.150 render -q delivery \
  -o "../../exports/SP01_Yalta_Photo_Story_Short_1080p.mp4"
```

## QA evidence (this build)

- `hyperframes check` — 0 errors, 0 warnings, 0 layout issues across 9 samples,
  5/5 text checks pass WCAG AA.
- `check_sync.py` — 13 captions, every fade-in completes within 0.02 s of its VO
  onset in `audio/manifest.json`; no two captions overlap on screen.
- Voice-over: Kokoro-82M `am_adam` at speed 1.05, 13 lines, 33.18 s total.
- Mix peak **−1.74 dBFS** in the delivered MP4, 0 clipped samples (scaled, not
  clipped — the raw sum of shutters + narration exceeds 0 dBFS, which an earlier
  build hard-clipped).
- Continuous ambience bed removed; only the two 90 ms shutter accents remain.
- Camera-vs-caption audit: frame at each subject's caption onset was read back with
  vision QA — the pan to Stalin has landed by 12.00 s and the pan to Churchill by
  17.50 s, so the frame never names a man it is not showing.
- Copy-vs-crop audit: vision QA flagged the original line *"Stalin sat in the center"*
  as contradicted by the photograph (Churchill left, Roosevelt centre, Stalin right).
  Rewritten to *"Stalin was the host."* — true, and supported by the crop.
- Frame 0 vs 1.0 s: 0.3 % pixel change → the print really is frozen (camera hold).
- Flash bloom at 0.15 s: 99.3 % pixels changed.
- Snap at 1.6 s: 48.4 % changed, max delta 222 → re-frame + text land.
- Vertical density (content > luma 45 per 160 px band): bottom band y1760–1920 went
  from **0 % (letterboxed first cut) to 61 %**; every band now shows photographic
  content; near-black(<32) ~24–26 % (was 39.7 %).
- Bottom third confirmed by vision QA as recognisable photographic detail (hands,
  hat, coat, chair, stone floor) — not a flat dark band.
- Hook text legibility confirmed by vision QA as **Clear**; the scrim reads as a
  deliberate design plate, not a mistake.
- `pytest` 373/373 PASS.

`qa_stills/` holds the extracted evidence frames for the beats above.
