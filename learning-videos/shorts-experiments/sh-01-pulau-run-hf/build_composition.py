"""Generate index.html for SH-01 from the Phase 2 audio manifest.
Deterministic: same manifest -> identical HTML.
"""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
MAN = json.load(open(os.path.join(HERE, "..", "sh-01-pulau-run", "audio", "manifest.json"), encoding="utf-8"))

ACCENT = "#F6E05E"
TOTAL = MAN["totalSec"]

# Ken Burns params per beat (px drift at 1080x1195 frame) -- from storyboard.md
KB = {
    1: (1.04, 1.15, 0, -25, 0, 20),
    2: (1.10, 1.22, -10, 15, 15, -20),
    3: (1.04, 1.15, 0, 15, 0, -30),
    4: (1.04, 1.15, 0, -25, 0, 20),
    5: (1.04, 1.15, 0, 20, 0, -25),
    6: (1.04, 1.15, 0, -15, 0, 20),
}
CHIPS = {
    1: ("ENGLISH DEFENDERS", "39 MEN ON RUN", "RESISTANCE DURATION", "1,540 CONSECUTIVE DAYS"),
    2: ("ISLAND DIMENSIONS", "3 KM LONG · 1 KM WIDE", "GLOBAL SUPPLY", "WORLD'S ONLY SOURCE (NUTMEG & MACE)"),
    3: ("ENGLISH COMMANDER", "CAPT. NATHANIEL COURTHOPE", "MISSION OBJECTIVE", "BREAK DUTCH VOC MONOPOLY"),
    4: ("LEGAL DOCTRINE", "UTI POSSIDETIS (STATUS QUO)", "TERRITORY IN DISPUTE", "MANHATTAN (NEW NETHERLAND)"),
    5: ("ENGLISH RETAINED", "MANHATTAN (NEW NETHERLAND)", "DUTCH RETAINED", "PULAU RUN (NUTMEG MONOPOLY)"),
    6: ("MANHATTAN TODAY", "GLOBAL FINANCIAL CAPITAL", "RUN TODAY", "POPULATION ~1,500 · NUTMEG"),
}
DOCKET = {
    1: "THE SPICE SIEGE · DOC REF VOC-1616",
    2: "BANDA ARCHIPELAGO & RUN · DOC REF VOC-1616",
    3: "COURTHOPE EXPEDITION 1616–1620 · DOC REF EIC-1616",
    4: "TREATY OF BREDA 1667 · DOC REF VOC-1667",
    5: "BREDA RATIFICATION · DOC REF VOC-1667",
    6: "MODERN CONTRAST & IR LEGACY · DOC REF VOC-1667",
}

beats = MAN["beats"]
# clip windows: hold from beat start to next beat start (no black gaps)
windows = []
for i, b in enumerate(beats):
    start = b["startSec"] if i else 0.0
    end = beats[i + 1]["startSec"] if i + 1 < len(beats) else TOTAL
    windows.append((start, end))

clips, tweens = [], []
for i, b in enumerate(beats):
    n = i + 1
    s0, s1 = windows[i]
    dur = s1 - s0
    sc0, sc1, px0, px1, py0, py1 = KB[n]
    c1l, c1v, c2l, c2v = CHIPS[n]

    # karaoke spans
    spans = []
    for w in b["words"]:
        t = html.escape(w["w"])
        spans.append(f'<span class="w" data-t="{w["start"]}" data-e="{w["end"]}">{t}</span>')
    caption = " ".join(spans)

    clips.append(f'''
    <section class="clip beat" id="beat{n}" data-start="{s0:.3f}" data-duration="{dur:.3f}" data-track-index="{n}">
      <div class="imwrap" data-layout-allow-overflow><img class="kb" id="kb{n}" src="assets/{b['asset']}" alt="{html.escape(b['headline'])}" /></div>
      <div class="topscrim"></div>
      <div class="botscrim"></div>
      <div class="tm">
        <div class="kicker">{html.escape(b['kicker'])}</div>
        <div class="headline">{html.escape(b['headline'])}</div>
      </div>
      <div class="wm">@IRinANutshell</div>
      <div class="docket">{html.escape(DOCKET[n])}</div>
      <div class="chips">
        <div class="chip"><span class="cl">{html.escape(c1l)}</span><span class="cv">{html.escape(c1v)}</span></div>
        <div class="chip"><span class="cl">{html.escape(c2l)}</span><span class="cv">{html.escape(c2v)}</span></div>
      </div>
      <div class="cap" id="cap{n}">{caption}</div>
    </section>''')

    # root-timeline tweens for this beat
    tweens.append(f'''
    // ---- beat {n} ----
    tl.fromTo("#kb{n}", {{ scale: {sc0}, x: {px0}, y: {py0} }},
      {{ scale: {sc1}, x: {px1}, y: {py1}, duration: {dur:.3f}, ease: "none" }}, {s0:.3f});
    tl.fromTo("#cap{n}", {{ opacity: 0, y: 18 }}, {{ opacity: 1, y: 0, duration: 0.40, ease: "power3.out" }}, {s0:.3f});
    tl.to("#cap{n}", {{ opacity: 0, duration: 0.25, ease: "power2.in" }}, {max(s0, b['endSec'] - 0.25):.3f});''')
    for k, w in enumerate(b["words"]):
        tweens.append(f'    tl.set(".beat:nth-of-type({n}) .w:nth-child({k+1})", {{ color: "{ACCENT}" }}, {w["start"]:.3f});')
        tweens.append(f'    tl.set(".beat:nth-of-type({n}) .w:nth-child({k+1})", {{ color: "#E8E8EC" }}, {w["end"]:.3f});')

HTML = f'''<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>SH-01 · Pulau Run — The Island Traded for Manhattan</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      @font-face {{ font-family: "Archivo Black"; src: url("fonts/ArchivoBlack-Regular.ttf") format("truetype"); font-weight: 400; }}
      @font-face {{ font-family: "Space Mono"; src: url("fonts/SpaceMono-Regular.ttf") format("truetype"); font-weight: 400; }}
      @font-face {{ font-family: "Space Mono"; src: url("fonts/SpaceMono-Bold.ttf") format("truetype"); font-weight: 700; }}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #0a0a0c;
        font-family: "Space Mono", monospace; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; background: #06060a; }}
      .beat {{ position: absolute; inset: 0; }}
      .imwrap {{ position: absolute; top: 0; left: 0; width: 1080px; height: 1920px; overflow: hidden; background: #06060a; }}
      .kb {{ position: absolute; top: 0; left: 0; width: 1080px; height: 1920px; object-fit: cover; will-change: transform; }}
      /* top scrim for headline; bottom scrim carries the info block and fades into the UI zone */
      .topscrim {{ position: absolute; top: 0; left: 0; width: 1080px; height: 900px;
        background: linear-gradient(to bottom, rgba(4,4,6,0.97) 0%, rgba(4,4,6,0.88) 26%, rgba(4,4,6,0.62) 55%, rgba(4,4,6,0.14) 84%, rgba(4,4,6,0) 100%); }}
      .botscrim {{ position: absolute; top: 980px; left: 0; width: 1080px; height: 940px;
        background: linear-gradient(to bottom, rgba(4,4,6,0) 0%, rgba(4,4,6,0.55) 10%, rgba(4,4,6,0.94) 18%, rgba(4,4,6,0.98) 32%, rgba(4,4,6,0.99) 100%); }}
      .tm {{ position: absolute; top: 200px; left: 70px; width: 940px; }}
      .kicker {{ font-size: 30px; letter-spacing: 0.20em; color: {ACCENT}; font-weight: 700;
        text-shadow: 0 2px 14px rgba(0,0,0,0.95); }}
      .headline {{ margin-top: 16px; font-family: "Archivo Black", sans-serif; font-size: 86px; line-height: 1.02;
        color: #ffffff; letter-spacing: -0.01em; text-shadow: 0 4px 22px rgba(0,0,0,0.95), 0 1px 3px rgba(0,0,0,0.95); }}
      .wm {{ position: absolute; top: 210px; right: 70px; font-size: 28px; letter-spacing: 0.06em;
        color: rgba(255,255,255,0.88); text-shadow: 0 2px 10px rgba(0,0,0,0.95); }}
      .docket {{ position: absolute; top: 1146px; left: 70px; width: 940px; font-size: 22px; letter-spacing: 0.05em;
        color: #d8d8e0; white-space: nowrap; overflow: hidden;
        text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
      .chips {{ position: absolute; top: 1186px; left: 70px; width: 940px; }}
      .chip {{ display: flex; justify-content: space-between; align-items: center; height: 50px; margin-bottom: 8px;
        border-left: 4px solid {ACCENT}; padding-left: 16px; }}
      .cl {{ font-size: 25px; letter-spacing: 0.08em; color: #b4b4be; line-height: 1;
        text-shadow: 0 2px 8px rgba(0,0,0,0.9); }}
      .cv {{ font-size: 27px; font-weight: 700; letter-spacing: 0.03em; color: #ffffff; line-height: 1;
        text-shadow: 0 2px 8px rgba(0,0,0,0.9); }}
      .cap {{ position: absolute; top: 1322px; left: 55px; width: 970px; height: 188px;
        display: flex; flex-wrap: wrap; align-content: center; justify-content: center;
        background: #0b0b10; border: 1px solid rgba(246,224,94,0.30); border-radius: 18px;
        padding: 16px 26px; }}
      .w {{ font-size: 31px; line-height: 1.26; color: #ECECEE; font-weight: 700; padding: 0 6px; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL:.3f}"
         data-width="1080" data-height="1920">
      <audio id="vo" src="audio/vo_full.mp3" data-start="0" data-duration="{TOTAL:.3f}"></audio>
{''.join(clips)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{''.join(tweens)}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''

out = os.path.join(HERE, "index.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"wrote {out}  ({len(HTML)} bytes, {len(beats)} beats, total {TOTAL}s)")
