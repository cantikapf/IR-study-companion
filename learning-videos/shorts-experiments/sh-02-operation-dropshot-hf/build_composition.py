"""Generate index.html for SH-02 (Operation Dropshot) from audio manifest.
Deterministic: same manifest -> identical HTML.
"""
import argparse, html, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_MANIFEST = os.path.join(HERE, "..", "sh-02-operation-dropshot", "audio", "manifest.json")

ACCENT = "#F6E05E"

# Ken Burns params cycle (px drift at 1080x1195 frame) -- deterministic cycle by beat index
KB_CYCLE = [
    (1.04, 1.15, 0, -25, 0, 20),
    (1.10, 1.22, -10, 15, 15, -20),
    (1.04, 1.15, 0, 15, 0, -30),
    (1.04, 1.15, 0, -25, 0, 20),
    (1.04, 1.15, 0, 20, 0, -25),
    (1.04, 1.15, 0, -15, 0, 20),
]


def main():
    parser = argparse.ArgumentParser(description="Generate index.html for SH-02 from audio manifest.")
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST, help="Path to manifest.json")
    args = parser.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        man = json.load(f)

    total = float(man["totalSec"])
    beats = man["beats"]

    # clip windows: hold from beat start to next beat start (no black gaps)
    windows = []
    for i, b in enumerate(beats):
        start = float(b["startSec"]) if i else 0.0
        end = float(beats[i + 1]["startSec"]) if i + 1 < len(beats) else total
        windows.append((start, end))

    clips, tweens = [], []
    for i, b in enumerate(beats):
        n = i + 1
        s0, s1 = windows[i]
        dur = s1 - s0
        sc0, sc1, px0, px1, py0, py1 = KB_CYCLE[i % len(KB_CYCLE)]

        kicker = b.get("kicker", "")
        headline = b.get("headline", "")
        docket = b.get("docket", "")
        c1l = b.get("chip1_label", "")
        c1v = b.get("chip1_value", "")
        c2l = b.get("chip2_label", "")
        c2v = b.get("chip2_value", "")

        # karaoke spans
        spans = []
        for w in b.get("words", []):
            t = html.escape(w["w"])
            spans.append(f'<span class="w" data-t="{w["start"]}" data-e="{w["end"]}">{t}</span>')
        caption = " ".join(spans)

        clips.append(f'''
    <section class="clip beat" id="beat{n}" data-start="{s0:.3f}" data-duration="{dur:.3f}" data-track-index="{n}">
      <div class="imwrap" data-layout-allow-overflow><img class="kb" id="kb{n}" src="assets/{b['asset']}" alt="{html.escape(headline)}" /></div>
      <div class="topscrim"></div>
      <div class="botscrim"></div>
      <div class="tm">
        <div class="kicker">{html.escape(kicker)}</div>
        <div class="headline">{html.escape(headline)}</div>
      </div>
      <div class="wm">@IRinANutshell</div>
      <div class="docket">{html.escape(docket)}</div>
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
    tl.to("#cap{n}", {{ opacity: 0, duration: 0.25, ease: "power2.in" }}, {max(s0, float(b['endSec']) - 0.25):.3f});''')
        for k, w in enumerate(b.get("words", [])):
            tweens.append(f'\n    tl.set(".beat:nth-of-type({n}) .w:nth-child({k+1})", {{ color: "{ACCENT}" }}, {w["start"]:.3f});')
            tweens.append(f'\n    tl.set(".beat:nth-of-type({n}) .w:nth-child({k+1})", {{ color: "#E8E8EC" }}, {w["end"]:.3f});')

    html_out = f'''<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>SH-02 · Operation Dropshot — The War Plan That Never Happened</title>
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
      /* Scrim Window Transparency Rule: topscrim height <= 480px, botscrim top >= 1100px (>= 600px middle band transparent) */
      .topscrim {{ position: absolute; top: 0; left: 0; width: 1080px; height: 480px;
        background: linear-gradient(to bottom, rgba(4,4,6,0.97) 0%, rgba(4,4,6,0.88) 30%, rgba(4,4,6,0.55) 62%, rgba(4,4,6,0.14) 86%, rgba(4,4,6,0) 100%); }}
      .botscrim {{ position: absolute; top: 1100px; left: 0; width: 1080px; height: 820px;
        background: linear-gradient(to bottom, rgba(4,4,6,0) 0%, rgba(4,4,6,0.82) 5%, rgba(4,4,6,0.96) 12%, rgba(4,4,6,0.99) 30%, rgba(4,4,6,0.995) 100%); }}
      .tm {{ position: absolute; top: 200px; left: 70px; width: 940px; }}
      .kicker {{ font-size: 30px; letter-spacing: 0.20em; color: {ACCENT}; font-weight: 700;
        text-shadow: 0 2px 14px rgba(0,0,0,0.95); }}
      .headline {{ margin-top: 16px; font-family: "Archivo Black", sans-serif; font-size: 86px; line-height: 1.02;
        color: #ffffff; letter-spacing: -0.01em; text-shadow: 0 4px 22px rgba(0,0,0,0.95), 0 1px 3px rgba(0,0,0,0.95); }}
      .wm {{ position: absolute; top: 210px; right: 70px; font-size: 28px; letter-spacing: 0.06em;
        color: rgba(255,255,255,0.88); text-shadow: 0 2px 10px rgba(0,0,0,0.95); }}
      .docket {{ position: absolute; top: 1146px; left: 70px; width: 940px; font-size: 22px; font-weight: 700; letter-spacing: 0.05em;
        color: #ffffff; white-space: nowrap; overflow: hidden;
        text-shadow: 0 2px 8px rgba(0,0,0,0.95); }}
      .chips {{ position: absolute; top: 1186px; left: 70px; width: 940px; }}
      .chip {{ display: flex; justify-content: space-between; align-items: center; height: 50px; margin-bottom: 8px;
        border-left: 4px solid {ACCENT}; padding-left: 16px; }}
      .cl {{ font-size: 25px; letter-spacing: 0.08em; color: #b4b4be; line-height: 1;
        text-shadow: 0 2px 8px rgba(0,0,0,0.9); }}
      .cv {{ font-size: 27px; font-weight: 700; letter-spacing: 0.03em; color: #ffffff; line-height: 1;
        text-shadow: 0 2px 8px rgba(0,0,0,0.9); }}
      /* Mobile safe zone: bottom edge at 1320+168=1488px (>= 430px clear from bottom 1920px). No backdrop-filter. */
      .cap {{ position: absolute; top: 1320px; left: 55px; width: 970px; height: 168px;
        display: flex; flex-wrap: wrap; align-content: center; justify-content: center;
        background: rgba(9,12,20,0.96); border: 1px solid rgba(246,224,94,0.30); border-radius: 18px;
        padding: 14px 24px; }}
      .w {{ font-size: 31px; line-height: 1.26; color: #ECECEE; font-weight: 700; padding: 0 6px; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{total:.3f}"
         data-width="1080" data-height="1920">
      <audio id="vo" src="audio/vo_full.mp3" data-start="0" data-duration="{total:.3f}"></audio>
{''.join(clips)}
    </div>
    <script>
      const tl = gsap.timeline({{ paused: true }});
{''.join(tweens)}
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''

    out = os.path.join(HERE, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"wrote {out} ({len(html_out)} bytes, {len(beats)} beats, total {total:.3f}s)")


if __name__ == "__main__":
    main()
