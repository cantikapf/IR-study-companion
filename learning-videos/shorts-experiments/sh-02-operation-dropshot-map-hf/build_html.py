import json, os

manifest_path = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-02-operation-dropshot/audio/manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    mf = json.load(f)

# Word highlights
word_tweens = []
cap_spans = {}
for b_idx, b in enumerate(mf["beats"]):
    beat_num = b_idx + 1
    spans = []
    for w_idx, w in enumerate(b["words"]):
        word_num = w_idx + 1
        word_text = w["w"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        spans.append(f'<span class="w">{word_text}</span>')
        word_tweens.append(f'      tl.set("#cap{beat_num} .w:nth-child({word_num})", {{ color: "#FFE619" }}, {w["start"]});')
        word_tweens.append(f'      tl.set("#cap{beat_num} .w:nth-child({word_num})", {{ color: "#cbd5e1" }}, {w["end"]});')
    cap_spans[beat_num] = " ".join(spans)

word_tweens_code = "\n".join(word_tweens)

# Beat metadata - Balanced 9:16 Vertical Composition
beats_info = [
    {
        "num": 1,
        "id": "beat1",
        "start": "0.000",
        "duration": "8.659",
        "kicker": "COLD WAR THEATER · 1949",
        "headline": "A PLAN FOR TOTAL WAR",
        "dossier_id": "dossier1",
        "dock_side": "left",
        "ref_code": "DECLASSIFIED · JCS-1949",
        "asset": "assets/jcs_bradley_swearing_in_1949.jpg",
        "name": "GEN. OMAR BRADLEY",
        "role": "CHAIRMAN, JOINT CHIEFS OF STAFF",
        "stat_l": "PLANNING BODY: US JCS",
        "stat_r": "ORIGIN DATE: DECEMBER 1949"
    },
    {
        "num": 2,
        "id": "beat2",
        "start": "8.659",
        "duration": "10.145",
        "kicker": "PROJECTED 1957 CAMPAIGN",
        "headline": "300 ATOMIC BOMBS · 100 CITIES",
        "dossier_id": "dossier2",
        "dock_side": "left",
        "ref_code": "DECLASSIFIED · NARA-1945",
        "asset": "assets/soviet_strategic_urban_targets_1945.jpg",
        "name": "STRATEGIC TARGET LIST",
        "role": "100 CITIES · 85% SOVIET INDUSTRY",
        "stat_l": "TARGET LIST: 100 URBAN CENTERS",
        "stat_r": "PROJECTED IMPACT: 85% INDUSTRY"
    },
    {
        "num": 3,
        "id": "beat3",
        "start": "18.804",
        "duration": "8.474",
        "kicker": "STRATEGIC AIR COMMAND",
        "headline": "NO MISSILES · BOMBERS ONLY",
        "dossier_id": "dossier3",
        "dock_side": "right",
        "ref_code": "DECLASSIFIED · SAC-7BW",
        "asset": "assets/b36_peacemaker_flight_1949.jpg",
        "name": "CONVAIR B-36 PEACEMAKER",
        "role": "10,000-MILE ARCTIC DELIVERY",
        "stat_l": "DELIVERY VEHICLE: B-36 & B-50",
        "stat_r": "STRIKE ROUTE: ARCTIC CORRIDORS"
    },
    {
        "num": 4,
        "id": "beat4",
        "start": "27.278",
        "duration": "9.449",
        "kicker": "SOVIET ATOMIC BREAKTHROUGH",
        "headline": "THE MONOPOLY ENDS · RDS-1",
        "dossier_id": "dossier4",
        "dock_side": "left",
        "ref_code": "DECLASSIFIED · AFOAT-1",
        "asset": "assets/joe1_fallout_tracking_map_1949.jpg",
        "name": "FIRST SOVIET TEST (RDS-1)",
        "role": "SEMIPALATINSK · 29 AUGUST 1949",
        "stat_l": "FIRST SOVIET DETONATION: RDS-1",
        "stat_r": "MONOPOLY: ENDED AUG 1949"
    },
    {
        "num": 5,
        "id": "beat5",
        "start": "36.727",
        "duration": "8.287",
        "kicker": "STRATEGIC REVISION",
        "headline": "WAR PLAN SHELVED",
        "dossier_id": "dossier5",
        "dock_side": "right",
        "ref_code": "DECLASSIFIED · DOD-1951",
        "asset": "assets/buster_jangle_nuclear_test_1951.jpg",
        "name": "NUCLEAR DETERRENCE",
        "role": "FIRST STRIKE RENDERED OBSOLETE",
        "stat_l": "OPERATIONAL STATUS: WITHDRAWN",
        "stat_r": "DOCTRINE: MUTUAL DETERRENCE"
    },
    {
        "num": 6,
        "id": "beat6",
        "start": "45.014",
        "duration": "11.274",
        "kicker": "DECLASSIFIED 1977",
        "headline": "THE PAPER ARSENAL",
        "dossier_id": "dossier6",
        "dock_side": "left",
        "ref_code": "DECLASSIFIED · NSA-1977",
        "asset": "assets/truman_oval_office_defense_1949.jpg",
        "name": "HARRY S. TRUMAN",
        "role": "1949 STOCKPILE: ~170 WARHEADS",
        "stat_l": "1949 US STOCKPILE: ~170 WARHEADS",
        "stat_r": "DROPSHOT PLAN: 300 BOMBS"
    }
]

clips_html_list = []
for b in beats_info:
    n = b["num"]
    dossier_side_class = "right-dock" if b["dock_side"] == "right" else "left-dock"
    clip_str = f'''    <section class="clip beat" id="{b["id"]}" data-start="{b["start"]}" data-duration="{b["duration"]}" data-track-index="{n}">
      <!-- TOP DOCUMENTARY HEADLINE -->
      <div class="tm">
        <div class="kicker">{b["kicker"]}</div>
        <div class="headline">{b["headline"]}</div>
      </div>

      <!-- TACTILE ARCHIVAL EXHIBIT CARD -->
      <div class="dossier-card {dossier_side_class}" id="{b["dossier_id"]}">
        <div class="dossier-header-bar">
          <span class="dossier-stamp">TOP SECRET</span>
          <span class="dossier-ref">{b["ref_code"]}</span>
        </div>
        <div class="dossier-frame">
          <img src="{b["asset"]}" class="dossier-img" alt="{b["name"]}" />
        </div>
        <div class="dossier-info">
          <div class="dossier-name">{b["name"]}</div>
          <div class="dossier-role">{b["role"]}</div>
        </div>
      </div>

      <!-- LOWER DATA STRIP (BRIDGES MAP & SUBTITLES, KILLS DEAD SPACE) -->
      <div class="stat-strip">
        <span class="stat-l">{b["stat_l"]}</span>
        <span class="stat-r">{b["stat_r"]}</span>
      </div>

      <!-- BOTTOM CAPTION CONTAINER (MOBILE SAFE ZONE) -->
      <div class="cap" id="cap{n}">{cap_spans[n]}</div>
    </section>'''
    clips_html_list.append(clip_str)

clips_html = "\n".join(clips_html_list)

html_content = f'''<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>SH-02 · Operation Dropshot — Cold War Geopolitical Map Animation (1949)</title>
    <script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script src="data/countries.js"></script>
    <style>
      @font-face {{
        font-family: "Archivo Black";
        src: url("fonts/ArchivoBlack-Regular.ttf") format("truetype");
        font-weight: 400;
      }}
      @font-face {{
        font-family: "Space Mono";
        src: url("fonts/SpaceMono-Regular.ttf") format("truetype");
        font-weight: 400;
      }}
      @font-face {{
        font-family: "Space Mono";
        src: url("fonts/SpaceMono-Bold.ttf") format("truetype");
        font-weight: 700;
      }}

      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{
        margin: 0;
        width: 1080px;
        height: 1920px;
        overflow: hidden;
        background: #080c14;
        font-family: "Space Mono", monospace;
        color: #ffffff;
      }}

      #root {{
        position: absolute;
        inset: 0;
        width: 1080px;
        height: 1920px;
        overflow: hidden;
        background: radial-gradient(circle at 50% 50%, #141c2b 0%, #0a0e18 65%, #05070c 100%);
        box-shadow: inset 0 0 160px 40px rgba(4, 6, 10, 0.95);
      }}

      /* UNTIMED PERSISTENT MAP STAGE (EXPANDED TO OCCUPY 1200PX VERTICAL CANVAS) */
      #map-stage {{
        position: absolute;
        inset: 0;
        width: 1080px;
        height: 1920px;
        pointer-events: none;
        z-index: 20;
        overflow: hidden;
      }}
      #map-svg {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1080px;
        height: 1920px;
      }}

      /* SOFT GRADIENT SCRIMS */
      .topscrim {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1080px;
        height: 300px;
        background: linear-gradient(to bottom, rgba(5, 7, 12, 0.98) 0%, rgba(5, 7, 12, 0.85) 50%, rgba(5, 7, 12, 0.30) 80%, rgba(5, 7, 12, 0) 100%);
        pointer-events: none;
        z-index: 25;
      }}
      .botscrim {{
        position: absolute;
        top: 1400px;
        left: 0;
        width: 1080px;
        height: 520px;
        background: linear-gradient(to bottom, rgba(5, 7, 12, 0) 0%, rgba(5, 7, 12, 0.85) 15%, rgba(5, 7, 12, 0.98) 35%, #05070c 100%);
        pointer-events: none;
        z-index: 25;
      }}

      /* CLIPS (TIMED BY TIMELINE DISPLAY TOGGLE, z-index 30) */
      .clip.beat {{
        position: absolute;
        inset: 0;
        width: 1080px;
        height: 1920px;
        pointer-events: none;
        background: transparent;
        z-index: 30;
        display: none;
      }}

      /* TOP DOCUMENTARY HEADLINE */
      .tm {{
        position: absolute;
        top: 80px;
        left: 60px;
        width: 960px;
      }}
      .kicker {{
        font-size: 24px;
        font-weight: 700;
        letter-spacing: 0.18em;
        color: #FFE619;
        text-shadow: 0 2px 14px rgba(0, 0, 0, 0.95);
        text-transform: uppercase;
      }}
      .headline {{
        margin-top: 10px;
        font-family: "Archivo Black", sans-serif;
        font-size: 68px;
        line-height: 1.05;
        color: #ffffff;
        letter-spacing: -0.01em;
        text-shadow: 0 4px 24px rgba(0, 0, 0, 0.98);
      }}

      /* TACTILE ARCHIVAL EXHIBIT CARD */
      .dossier-card {{
        position: absolute;
        top: 340px;
        width: 350px;
        background: #0f1523;
        border: 1.5px solid rgba(255, 255, 255, 0.22);
        border-radius: 12px;
        padding: 12px;
        box-shadow: 0 24px 60px rgba(0, 0, 0, 0.95), 0 0 1px 1px rgba(255, 255, 255, 0.08);
        pointer-events: none;
      }}
      .dossier-card.left-dock {{
        left: 60px;
      }}
      .dossier-card.right-dock {{
        right: 60px;
        left: auto;
      }}
      .dossier-header-bar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
        padding: 0 2px;
      }}
      .dossier-stamp {{
        font-family: "Space Mono", monospace;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.14em;
        color: #f87171;
        border: 1.5px solid #f87171;
        border-radius: 3px;
        padding: 2px 6px;
        text-transform: uppercase;
        transform: rotate(-3deg);
        display: inline-block;
      }}
      .dossier-ref {{
        font-family: "Space Mono", monospace;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: #94a3b8;
      }}
      .dossier-frame {{
        position: relative;
        width: 100%;
        height: 250px;
        border-radius: 6px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.15);
        background: #000000;
      }}
      .dossier-img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(20%) contrast(1.15) brightness(0.98);
      }}
      .dossier-info {{
        margin-top: 10px;
        text-align: left;
        padding: 0 2px;
      }}
      .dossier-name {{
        font-family: "Archivo Black", sans-serif;
        font-size: 17px;
        line-height: 1.25;
        color: #ffffff;
        letter-spacing: 0.02em;
      }}
      .dossier-role {{
        font-family: "Space Mono", monospace;
        font-size: 11.5px;
        font-weight: 700;
        color: #FFE619;
        letter-spacing: 0.06em;
        margin-top: 4px;
      }}

      /* LOWER DATA STRIP (BRIDGES MAP & SUBTITLES, ELIMINATES DEAD SPACE) */
      .stat-strip {{
        position: absolute;
        top: 1475px;
        left: 60px;
        width: 960px;
        height: 44px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 18px;
        background: rgba(14, 20, 34, 0.96);
        border: 1px solid rgba(255, 230, 25, 0.40);
        border-radius: 8px;
        font-family: "Space Mono", monospace;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.05em;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.85);
      }}
      .stat-l {{
        color: #FFE619;
      }}
      .stat-r {{
        color: #f8fafc;
      }}

      /* CAPTIONS (POSITIONED DIRECTLY ABOVE MOBILE UI, NO DEAD VOID) */
      .cap {{
        position: absolute;
        top: 1535px;
        left: 60px;
        width: 960px;
        min-height: 140px;
        max-height: 180px;
        display: flex;
        flex-wrap: wrap;
        align-content: center;
        justify-content: center;
        background: rgba(10, 14, 24, 0.98);
        border: 1.5px solid rgba(255, 230, 25, 0.35);
        border-radius: 18px;
        padding: 16px 28px;
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.98);
      }}
      .w {{
        font-size: 32px;
        line-height: 1.35;
        color: #cbd5e1;
        font-weight: 700;
        padding: 0 6px;
      }}

      /* TACTICAL CARTOGRAPHY PALETTE */
      .country-land {{
        fill: #111827;
        stroke: #283344;
        stroke-width: 1.2px;
      }}
      .country-allied {{
        fill: #192436;
        stroke: #94a3b8;
        stroke-width: 1.6px;
      }}
      .country-ussr {{
        fill: #3b0f15;
        stroke: #dc2626;
        stroke-width: 2.0px;
      }}
      .graticule {{
        fill: none;
        stroke: rgba(148, 163, 184, 0.12);
        stroke-width: 1.2px;
        stroke-dasharray: 6 6;
      }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="56.288" data-width="1080" data-height="1920">
      <audio id="vo" src="audio/vo_full.mp3" data-start="0" data-duration="56.288"></audio>

      <!-- SHARED VECTOR MAP BACKGROUND (EXPANDED TO FILL VERTICAL VIEWPORT) -->
      <div id="map-stage" data-layout-allow-overflow>
        <svg id="map-svg" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg" data-layout-allow-overflow>
          <defs>
            <radialGradient id="grad-fireball" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#ffffff" />
              <stop offset="20%" stop-color="#fef08a" />
              <stop offset="50%" stop-color="#facc15" />
              <stop offset="80%" stop-color="#dc2626" stop-opacity="0.9" />
              <stop offset="100%" stop-color="#7f1d1d" stop-opacity="0" />
            </radialGradient>
            <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="6" result="blur" />
              <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
            </filter>

            <!-- B-36 PEACEMAKER SILHOUETTE ICON -->
            <g id="icon-b36">
              <path d="M0,-30 L3,-22 L3,24 L0,30 L-3,24 L-3,-22 Z" fill="#e2e8f0" stroke="#475569" stroke-width="1.2" />
              <polygon points="0,-6 72,6 72,12 8,6 0,6 -8,6 -72,12 -72,6" fill="#cbd5e1" stroke="#475569" stroke-width="1.2" />
              <polygon points="0,22 24,27 24,30 0,28 -24,30 -24,27" fill="#94a3b8" stroke="#475569" stroke-width="1" />
              <circle cx="20" cy="7" r="2" fill="#38bdf8" />
              <circle cx="38" cy="8.5" r="2" fill="#38bdf8" />
              <circle cx="56" cy="10" r="2" fill="#38bdf8" />
              <circle cx="-20" cy="7" r="2" fill="#38bdf8" />
              <circle cx="-38" cy="8.5" r="2" fill="#38bdf8" />
              <circle cx="-56" cy="10" r="2" fill="#38bdf8" />
            </g>

            <!-- BASE PIN (WHITE/STEEL DIAMOND) -->
            <g id="icon-base-pin">
              <polygon points="0,-12 12,0 0,12 -12,0" fill="#1e293b" stroke="#f8fafc" stroke-width="2" />
              <circle cx="0" cy="0" r="3" fill="#FFE619" />
            </g>

            <!-- TARGET CROSSHAIR PIN (RED) -->
            <g id="icon-target-pin">
              <circle cx="0" cy="0" r="8" fill="none" stroke="#dc2626" stroke-width="2" />
              <circle cx="0" cy="0" r="2" fill="#dc2626" />
              <line x1="-12" y1="0" x2="-4" y2="0" stroke="#dc2626" stroke-width="1.8" />
              <line x1="4" y1="0" x2="12" y2="0" stroke="#dc2626" stroke-width="1.8" />
              <line x1="0" y1="-12" x2="0" y2="-4" stroke="#dc2626" stroke-width="1.8" />
              <line x1="0" y1="4" x2="0" y2="12" stroke="#dc2626" stroke-width="1.8" />
            </g>

            <!-- RADIATION TREFOIL ICON -->
            <g id="icon-radiation">
              <circle cx="0" cy="0" r="14" fill="#dc2626" />
              <circle cx="0" cy="0" r="8" fill="#0a0e18" />
              <path d="M-8,-14 L-26,-46 A52,52 0 0,1 26,-46 L8,-14 Z" fill="#dc2626" />
              <path d="M13,6 L45,24 A52,52 0 0,1 19,52 L2,15 Z" fill="#dc2626" />
              <path d="M-13,6 L-45,24 A52,52 0 0,0 -19,52 L-2,15 Z" fill="#dc2626" />
              <circle cx="0" cy="0" r="4.5" fill="#FFE619" />
            </g>
          </defs>

          <!-- MAP CAMERA GROUP (TRANSFORMED BY GSAP 2D MATRIX) -->
          <g id="map-camera-group" data-layout-allow-overflow>
            <path id="map-graticule" class="graticule" />
            <g id="countries-layer"></g>

            <!-- BEAT 1 OVERLAYS -->
            <g id="b1-overlays" opacity="1">
              <g transform="translate(106, 1041.5)">
                <circle id="b1-pulse-wash" r="25" fill="none" stroke="#94a3b8" stroke-width="2" opacity="0.6" />
                <use href="#icon-base-pin" />
              </g>
              <g transform="translate(61.4, 879.9)">
                <circle id="b1-pulse-omaha" r="30" fill="none" stroke="#94a3b8" stroke-width="2" opacity="0.6" />
                <use href="#icon-base-pin" />
              </g>
              <path id="b1-threat-arc" d="M 106 1041.5 Q 480 650 832.8 945.7" fill="none" stroke="#dc2626" stroke-width="3" stroke-dasharray="10 8" opacity="0.85" />
            </g>

            <!-- BEAT 2 OVERLAYS -->
            <g id="b2-overlays" opacity="0">
              <circle id="b2-target-ring-1" cx="832.8" cy="945.7" r="80" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="8 6" opacity="0.7" />
              <circle id="b2-target-ring-2" cx="832.8" cy="945.7" r="160" fill="none" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="10 8" opacity="0.5" />
              <circle id="b2-target-ring-3" cx="888.7" cy="812.7" r="120" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="8 6" opacity="0.6" />

              <g transform="translate(832.8, 945.7)"><use href="#icon-target-pin" /></g> <!-- Moscow -->
              <g transform="translate(774.3, 954.3)"><use href="#icon-target-pin" /></g> <!-- Leningrad -->
              <g transform="translate(888.7, 812.7)"><use href="#icon-target-pin" /></g> <!-- Chelyabinsk -->
              <g transform="translate(871.2, 814.8)"><use href="#icon-target-pin" /></g> <!-- Sverdlovsk -->
              <g transform="translate(846.4, 909.5)"><use href="#icon-target-pin" /></g> <!-- Gorky -->
              <g transform="translate(885.2, 680.7)"><use href="#icon-target-pin" /></g> <!-- Novosibirsk -->
              <g transform="translate(1011.4, 932.9)"><use href="#icon-target-pin" /></g> <!-- Baku -->
            </g>

            <!-- BEAT 3 OVERLAYS -->
            <g id="b3-overlays" opacity="0">
              <g transform="translate(338.5, 604.2)"><use href="#icon-base-pin" /></g> <!-- Alaska -->
              <g transform="translate(437.6, 850)"><use href="#icon-base-pin" /></g> <!-- Thule -->
              <g transform="translate(673.7, 1117.5)"><use href="#icon-base-pin" /></g> <!-- UK -->

              <path id="route-alaska" d="M 338.5 604.2 Q 520 540 888.7 812.7" fill="none" stroke="#f8fafc" stroke-width="3.5" stroke-dasharray="12 8" opacity="0.9" />
              <path id="route-thule" d="M 437.6 850 Q 600 920 832.8 945.7" fill="none" stroke="#f8fafc" stroke-width="3.5" stroke-dasharray="12 8" opacity="0.9" />
              <path id="route-uk" d="M 673.7 1117.5 Q 730 1020 774.3 954.3" fill="none" stroke="#f8fafc" stroke-width="3" stroke-dasharray="10 8" opacity="0.8" />

              <g id="bomber-rig-alaska" transform="translate(338.5, 604.2)">
                <use href="#icon-b36" transform="scale(0.8) rotate(70)" />
              </g>
              <g id="bomber-rig-thule" transform="translate(437.6, 850)">
                <use href="#icon-b36" transform="scale(0.8) rotate(100)" />
              </g>
              <g id="bomber-rig-uk" transform="translate(673.7, 1117.5)">
                <use href="#icon-b36" transform="scale(0.8) rotate(55)" />
              </g>
            </g>

            <!-- BEAT 4 OVERLAYS -->
            <g id="b4-overlays" opacity="0">
              <g transform="translate(936, 698.5)">
                <circle id="b4-fireball" r="10" fill="url(#grad-fireball)" />
                <circle id="b4-shock-1" r="25" fill="none" stroke="#FFE619" stroke-width="4" opacity="0.9" />
                <circle id="b4-shock-2" r="50" fill="none" stroke="#dc2626" stroke-width="3" opacity="0.7" />
                <circle id="b4-shock-3" r="85" fill="none" stroke="#f87171" stroke-width="2" opacity="0.5" />
                <g id="b4-radiation-icon" transform="translate(0, -50) scale(0.6)">
                  <use href="#icon-radiation" />
                </g>
              </g>
              <path id="b4-fallout-plume" d="M 936 698.5 Q 780 500 520 480" fill="none" stroke="#FFE619" stroke-width="3.5" stroke-dasharray="10 8" opacity="0.85" />
            </g>

            <!-- BEAT 5 OVERLAYS -->
            <g id="b5-overlays" opacity="0">
              <path d="M 106 1041.5 Q 540 580 832.8 945.7" fill="none" stroke="#94a3b8" stroke-width="3" stroke-dasharray="12 10" opacity="0.75" />
              <path d="M 832.8 945.7 Q 540 720 106 1041.5" fill="none" stroke="#dc2626" stroke-width="3" stroke-dasharray="12 10" opacity="0.75" />
              <circle cx="280" cy="850" r="60" fill="none" stroke="#94a3b8" stroke-width="2.5" opacity="0.6" />
              <circle cx="780" cy="850" r="60" fill="none" stroke="#dc2626" stroke-width="2.5" opacity="0.6" />
            </g>

            <!-- BEAT 6 OVERLAYS -->
            <g id="b6-overlays" opacity="0" data-layout-allow-overflow data-layout-allow-occlusion>
              <g transform="translate(460, 680)">
                <rect x="0" y="0" width="360" height="150" rx="8" fill="#080c16" stroke="#FFE619" stroke-width="1.8" opacity="0.95" />
                <text x="180" y="28" fill="#FFE619" font-size="12" font-weight="bold" letter-spacing="1" text-anchor="middle" font-family="'Space Mono', monospace">1949 ATOMIC ARSENAL GAP</text>
                
                <rect x="25" y="45" width="310" height="22" rx="4" fill="#330d14" stroke="#dc2626" stroke-width="1.2" />
                <rect id="b6-bar-planned" x="25" y="45" width="310" height="22" rx="4" fill="#dc2626" opacity="0.75" />
                <text x="35" y="60" fill="#ffffff" font-size="10" font-weight="bold" font-family="'Space Mono', monospace">DROPSHOT PLAN: 300 BOMBS</text>

                <rect x="25" y="76" width="310" height="22" rx="4" fill="#1e2230" stroke="#FFE619" stroke-width="1.2" />
                <rect id="b6-bar-actual" x="25" y="76" width="175" height="22" rx="4" fill="#FFE619" opacity="0.85" />
                <text x="35" y="91" fill="#080c16" font-size="10" font-weight="bold" font-family="'Space Mono', monospace">ACTUAL STOCKPILE: ~170</text>

                <rect x="25" y="108" width="310" height="26" rx="4" fill="#140608" stroke="#dc2626" stroke-width="1" />
                <text x="180" y="125" fill="#f87171" font-size="10.5" font-weight="bold" letter-spacing="0.5" text-anchor="middle" font-family="'Space Mono', monospace">DEFICIT: -130 WARHEADS SHORT</text>
              </g>
            </g>

            <!-- TACTICAL LABELS LAYER (LAST CHILD OF SVG) -->
            <g id="tactical-labels-layer">
              <!-- Beat 1: Washington DC -->
              <g id="label-washington" opacity="1" transform="translate(106, 1065)" data-layout-allow-overflow data-layout-allow-occlusion>
                <rect x="0" y="0" width="175" height="22" rx="3" fill="#0a0e18" stroke="#94a3b8" stroke-width="1.2" />
                <text x="87" y="15" fill="#f8fafc" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">WASHINGTON · JCS</text>
              </g>
              <!-- Beat 1: Omaha Offutt AFB -->
              <g id="label-omaha" opacity="1" transform="translate(95, 895)" data-layout-allow-overflow data-layout-allow-occlusion>
                <rect x="0" y="0" width="175" height="22" rx="3" fill="#0a0e18" stroke="#94a3b8" stroke-width="1.2" />
                <text x="87" y="15" fill="#f8fafc" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">OMAHA · SAC HQ</text>
              </g>

              <!-- Beat 2: Moscow -->
              <g id="label-moscow" opacity="0" transform="translate(660, 935)" data-layout-allow-overflow data-layout-allow-occlusion>
                <rect x="0" y="0" width="160" height="22" rx="3" fill="#0a0e18" stroke="#dc2626" stroke-width="1.2" />
                <text x="80" y="15" fill="#f8fafc" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">MOSCOW · TARGET 1</text>
              </g>
              <!-- Beat 2: Chelyabinsk Urals -->
              <g id="label-chelyabinsk" opacity="0" transform="translate(700, 802)" data-layout-allow-overflow data-layout-allow-occlusion>
                <rect x="0" y="0" width="175" height="22" rx="3" fill="#0a0e18" stroke="#dc2626" stroke-width="1.2" />
                <text x="87" y="15" fill="#f8fafc" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">CHELYABINSK · URALS</text>
              </g>

              <!-- Beat 3: Alaska Eielson -->
              <g id="label-alaska" opacity="0" transform="translate(338, 565)" data-layout-allow-overflow data-layout-allow-occlusion>
                <rect x="0" y="0" width="175" height="22" rx="3" fill="#0a0e18" stroke="#94a3b8" stroke-width="1.2" />
                <text x="87" y="15" fill="#f8fafc" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">ALASKA · SAC BASE</text>
              </g>
              <!-- Beat 3: Thule Greenland -->
              <g id="label-thule" opacity="0" transform="translate(438, 815)" data-layout-allow-overflow data-layout-allow-occlusion>
                <rect x="0" y="0" width="165" height="22" rx="3" fill="#0a0e18" stroke="#94a3b8" stroke-width="1.2" />
                <text x="82" y="15" fill="#f8fafc" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">THULE · GREENLAND</text>
              </g>

              <!-- Beat 4: Semipalatinsk -->
              <g id="label-semipalatinsk" opacity="0" transform="translate(860, 740)" data-layout-allow-overflow data-layout-allow-occlusion>
                <rect x="0" y="0" width="170" height="22" rx="3" fill="#0a0e18" stroke="#FFE619" stroke-width="1.2" />
                <text x="85" y="15" fill="#FFE619" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">SEMIPALATINSK · RDS-1</text>
              </g>
            </g>
          </g>
        </svg>
      </div>

      <!-- GRADIENT SCRIMS FOR CLEAN CONTRAST -->
      <div class="topscrim" data-layout-allow-overflow data-layout-allow-occlusion></div>
      <div class="botscrim" data-layout-allow-overflow data-layout-allow-occlusion></div>

{clips_html}

    </div>

    <!-- CARTOGRAPHY & CONTINUOUS GSAP TIMELINE ENGINE -->
    <script>
      const width = 1080;
      const height = 1920;

      const baseProjection = d3.geoAzimuthalEquidistant()
        .rotate([20, -90, 0])
        .scale(620)
        .clipAngle(110)
        .translate([width / 2, 840]);

      const pathGenerator = d3.geoPath(baseProjection);

      const ussrIds = new Set(["643", "398", "804", "112", "860", "795", "051", "498", "440", "428", "233", "031", "268", "762", "417"]);
      const alliedIds = new Set(["840", "124", "826"]);

      const countriesG = d3.select("#countries-layer");
      if (window.WORLD_GEOJSON) {{
        countriesG.selectAll("path")
          .data(window.WORLD_GEOJSON.features)
          .enter()
          .append("path")
          .attr("class", d => {{
            if (alliedIds.has(d.id)) return "country-path country-land country-allied";
            if (ussrIds.has(d.id)) return "country-path country-land country-ussr";
            return "country-path country-land";
          }})
          .attr("d", pathGenerator);
      }}

      const graticuleGeo = d3.geoGraticule().step([15, 15])();
      d3.select("#map-graticule").attr("d", pathGenerator(graticuleGeo));

      const camera = {{
        x: 540,
        y: 860,
        scale: 1.15
      }};

      const mapCameraGroup = document.getElementById("map-camera-group");

      function updateCamera() {{
        const s = camera.scale;
        const tx = 540 - camera.x * s;
        const ty = 840 - camera.y * s;
        mapCameraGroup.setAttribute("transform", `translate(${{tx}}, ${{ty}}) scale(${{s}})`);
      }}
      updateCamera();

      // Standalone browser preview helper (does not touch GSAP timeline, safe for HyperFrames)
      function syncClipsForTime(t) {{
        document.querySelectorAll(".clip.beat").forEach(clip => {{
          const s = parseFloat(clip.dataset.start);
          const d = parseFloat(clip.dataset.duration);
          clip.style.display = (t >= s && t < s + d) ? "block" : "none";
        }});
      }}

      const tl = gsap.timeline({{
        paused: true,
        onUpdate: () => {{
          updateCamera();
          syncClipsForTime(tl.time());
        }}
      }});

      // BEAT 1 (0.000s -> 8.659s)
      tl.set(camera, {{ x: 540, y: 860, scale: 1.15 }}, 0.00);
      tl.fromTo("#b1-pulse-wash", {{ r: 15, opacity: 0.9 }}, {{ r: 55, opacity: 0, duration: 1.8, repeat: 4, ease: "power1.out" }}, 0.20);
      tl.fromTo("#b1-pulse-omaha", {{ r: 15, opacity: 0.9 }}, {{ r: 60, opacity: 0, duration: 2.0, repeat: 3, ease: "power1.out" }}, 0.30);
      tl.fromTo("#b1-threat-arc", {{ strokeDashoffset: 500 }}, {{ strokeDashoffset: 0, duration: 3.5, ease: "power2.out" }}, 0.80);
      tl.fromTo("#dossier1", {{ opacity: 0, x: -35 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 0.50);

      // BEAT 2 (8.659s -> 18.804s)
      tl.to(camera, {{ x: 840, y: 920, scale: 1.65, duration: 2.2, ease: "power2.inOut" }}, 8.659);
      tl.to(["#b1-overlays", "#label-washington", "#label-omaha"], {{ opacity: 0, duration: 0.5 }}, 8.659);
      tl.to("#b2-overlays", {{ opacity: 1, duration: 0.8 }}, 9.20);
      tl.to(["#label-moscow", "#label-chelyabinsk"], {{ opacity: 1, duration: 0.6 }}, 9.80);
      tl.fromTo("#b2-target-ring-1", {{ r: 20, opacity: 0.9 }}, {{ r: 140, opacity: 0.2, duration: 2.4, repeat: 3, ease: "power1.out" }}, 9.50);
      tl.fromTo("#b2-target-ring-3", {{ r: 20, opacity: 0.9 }}, {{ r: 150, opacity: 0.2, duration: 2.6, repeat: 3, ease: "power1.out" }}, 9.80);
      tl.fromTo("#dossier2", {{ opacity: 0, x: -35 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 9.00);

      // BEAT 3 (18.804s -> 27.278s)
      tl.to(camera, {{ x: 500, y: 820, scale: 1.35, duration: 2.0, ease: "power2.inOut" }}, 18.804);
      tl.to(["#b2-overlays", "#label-moscow", "#label-chelyabinsk"], {{ opacity: 0, duration: 0.5 }}, 18.804);
      tl.to("#b3-overlays", {{ opacity: 1, duration: 0.8 }}, 19.30);
      tl.to(["#label-alaska", "#label-thule"], {{ opacity: 1, duration: 0.6 }}, 19.80);
      tl.fromTo("#route-alaska", {{ strokeDashoffset: 800 }}, {{ strokeDashoffset: 0, duration: 4.5, ease: "none" }}, 19.40);
      tl.fromTo("#route-thule", {{ strokeDashoffset: 700 }}, {{ strokeDashoffset: 0, duration: 4.5, ease: "none" }}, 19.60);
      tl.fromTo("#route-uk", {{ strokeDashoffset: 500 }}, {{ strokeDashoffset: 0, duration: 4.0, ease: "none" }}, 19.80);
      tl.fromTo("#bomber-rig-alaska", {{ x: 0, y: 0 }}, {{ x: 420, y: 160, duration: 6.5, ease: "none" }}, 19.50);
      tl.fromTo("#bomber-rig-thule", {{ x: 0, y: 0 }}, {{ x: 300, y: 70, duration: 6.5, ease: "none" }}, 19.60);
      tl.fromTo("#dossier3", {{ opacity: 0, x: 35 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 19.10);

      // BEAT 4 (27.278s -> 36.727s)
      tl.to(camera, {{ x: 920, y: 760, scale: 2.10, duration: 2.0, ease: "power3.inOut" }}, 27.278);
      tl.to(["#b3-overlays", "#label-alaska", "#label-thule"], {{ opacity: 0, duration: 0.5 }}, 27.278);
      tl.to("#b4-overlays", {{ opacity: 1, duration: 0.6 }}, 27.80);
      tl.to("#label-semipalatinsk", {{ opacity: 1, duration: 0.5 }}, 28.30);
      tl.fromTo("#b4-fireball", {{ r: 6, opacity: 1 }}, {{ r: 65, opacity: 0.75, duration: 1.2, ease: "power2.out" }}, 28.50);
      tl.fromTo("#b4-shock-1", {{ r: 15, opacity: 1 }}, {{ r: 160, opacity: 0, duration: 1.8, repeat: 3, ease: "power1.out" }}, 28.60);
      tl.fromTo("#b4-shock-2", {{ r: 30, opacity: 0.9 }}, {{ r: 240, opacity: 0, duration: 2.2, repeat: 2, ease: "power1.out" }}, 28.80);
      tl.to("#b4-radiation-icon", {{ rotation: 360, duration: 7.0, ease: "none" }}, 28.50);
      tl.to("#label-semipalatinsk", {{ opacity: 0, duration: 0.4 }}, 33.50);
      tl.fromTo("#b4-fallout-plume", {{ strokeDashoffset: 600 }}, {{ strokeDashoffset: 0, duration: 4.5, ease: "power2.out" }}, 29.50);
      tl.fromTo("#dossier4", {{ opacity: 0, x: -35 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 27.60);

      // BEAT 5 (36.727s -> 45.014s)
      tl.to(camera, {{ x: 560, y: 880, scale: 1.20, duration: 2.0, ease: "power2.inOut" }}, 36.727);
      tl.to(["#b4-overlays", "#label-semipalatinsk"], {{ opacity: 0, duration: 0.5 }}, 36.727);
      tl.to("#b5-overlays", {{ opacity: 1, duration: 0.8 }}, 37.30);
      tl.fromTo("#dossier5", {{ opacity: 0, x: 35 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 37.00);

      // BEAT 6 (45.014s -> 56.288s)
      tl.to(camera, {{ x: 540, y: 860, scale: 1.15, duration: 2.2, ease: "power2.inOut" }}, 45.014);
      tl.to("#b5-overlays", {{ opacity: 0, duration: 0.5 }}, 45.014);
      tl.to("#b6-overlays", {{ opacity: 1, duration: 0.8 }}, 45.60);
      tl.fromTo("#dossier6", {{ opacity: 0, x: -35 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 45.40);

      // Word-level karaoke tweens
{word_tweens_code}

      // ROOT TIMELINE EXPORT FOR HYPERFRAMES RUNNER
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
'''

out_path = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-02-operation-dropshot-map-hf/index.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated clean documentary index.html at {out_path} ({len(html_content)} bytes)")
