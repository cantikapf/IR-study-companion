
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
        word_tweens.append(f'      tl.set("#cap{beat_num} .w:nth-child({word_num})", {{ color: "#F6E05E" }}, {w["start"]});')
        word_tweens.append(f'      tl.set("#cap{beat_num} .w:nth-child({word_num})", {{ color: "#ECECEE" }}, {w["end"]});')
    cap_spans[beat_num] = " ".join(spans)

word_tweens_code = "\n".join(word_tweens)

# Beat metadata
beats_info = [
    {
        "num": 1,
        "id": "beat1",
        "start": "0.000",
        "duration": "8.659",
        "kicker": "CLASSIFIED WAR PLAN · 1949",
        "headline": "A PLAN FOR TOTAL WAR",
        "docket": "WAR PLAN CONCEPTION · DOC REF JCS-1949",
        "c1_l": "ORIGINATING BODY",
        "c1_v": "US JOINT CHIEFS OF STAFF",
        "c2_l": "PLANNING DATE",
        "c2_v": "DECEMBER 1949",
        "dossier_id": "dossier1",
        "dossier_class": "dossier-card",
        "badge_class": "dossier-badge dossier-badge-us",
        "badge_txt": "US JCS // PENTAGON",
        "asset": "assets/jcs_bradley_swearing_in_1949.jpg",
        "name": "GEN. OMAR BRADLEY",
        "role": "CHAIRMAN, JOINT CHIEFS"
    },
    {
        "num": 2,
        "id": "beat2",
        "start": "8.659",
        "duration": "10.145",
        "kicker": "PROJECTED 1957 CAMPAIGN",
        "headline": "300 ATOMIC BOMBS · 100 CITIES",
        "docket": "TARGET LIST &amp; DAMAGE · DOC REF JCS-1949",
        "c1_l": "PLANNED WEAPONS",
        "c1_v": "300 ATOMIC · 29,000 HE BOMBS",
        "c2_l": "PLANNED TARGETS",
        "c2_v": "100 CITIES · 85% INDUSTRY",
        "dossier_id": "dossier2",
        "dossier_class": "dossier-card threat",
        "badge_class": "dossier-badge dossier-badge-soviet",
        "badge_txt": "TARGET LIST // 1949",
        "asset": "assets/soviet_strategic_urban_targets_1945.jpg",
        "name": "URBAN TARGET LIST",
        "role": "100 CITIES · 85% INDUSTRY"
    },
    {
        "num": 3,
        "id": "beat3",
        "start": "18.804",
        "duration": "8.474",
        "kicker": "STRATEGIC AIR COMMAND",
        "headline": "NO MISSILES · BOMBERS ONLY",
        "docket": "SAC FLIGHT PROFILES · DOC REF JCS-1949",
        "c1_l": "DELIVERY VEHICLE",
        "c1_v": "B-36 &amp; B-50 HEAVY BOMBERS",
        "c2_l": "STRIKE ROUTE",
        "c2_v": "ARCTIC POLAR CORRIDORS",
        "dossier_id": "dossier3",
        "dossier_class": "dossier-card",
        "badge_class": "dossier-badge dossier-badge-us",
        "badge_txt": "SAC HEAVY BOMBER",
        "asset": "assets/b36_peacemaker_flight_1949.jpg",
        "name": "B-36 PEACEMAKER",
        "role": "ARCTIC POLAR DELIVERY"
    },
    {
        "num": 4,
        "id": "beat4",
        "start": "27.278",
        "duration": "9.449",
        "kicker": "SOVIET ATOMIC BREAKTHROUGH",
        "headline": "THE MONOPOLY ENDS · RDS-1",
        "docket": "AFOAT-1 DETECTION · DOC REF EBB-286",
        "c1_l": "FIRST SOVIET TEST",
        "c1_v": "29 AUGUST 1949 · RDS-1",
        "c2_l": "TEST LOCATION",
        "c2_v": "SEMIPALATINSK, KAZAKHSTAN",
        "dossier_id": "dossier4",
        "dossier_class": "dossier-card threat",
        "badge_class": "dossier-badge dossier-badge-soviet",
        "badge_txt": "AFOAT-1 DETECTION",
        "asset": "assets/joe1_fallout_tracking_map_1949.jpg",
        "name": "RDS-1 TEST (JOE-1)",
        "role": "SEMIPALATINSK · 1949"
    },
    {
        "num": 5,
        "id": "beat5",
        "start": "36.727",
        "duration": "8.287",
        "kicker": "STRATEGIC REVISION",
        "headline": "WAR PLAN SHELVED",
        "docket": "STRATEGIC REVISION · DOC REF JCS-1951",
        "c1_l": "OPERATIONAL STATUS",
        "c1_v": "NEVER EXECUTED · WITHDRAWN 1951",
        "c2_l": "DOCTRINE SHIFT",
        "c2_v": "FIRST STRIKE TO DETERRENCE",
        "dossier_id": "dossier5",
        "dossier_class": "dossier-card amber",
        "badge_class": "dossier-badge dossier-badge-amber",
        "badge_txt": "STRATEGIC REVISION",
        "asset": "assets/buster_jangle_nuclear_test_1951.jpg",
        "name": "WAR PLAN SHELVED",
        "role": "WITHDRAWN FEB 1951"
    },
    {
        "num": 6,
        "id": "beat6",
        "start": "45.014",
        "duration": "11.274",
        "kicker": "DECLASSIFIED 1977",
        "headline": "THE PAPER ARSENAL",
        "docket": "DECLASSIFIED RECORD · DOC REF JCS-1977",
        "c1_l": "1949 US STOCKPILE",
        "c1_v": "~170 ATOMIC WARHEADS",
        "c2_l": "DECLASSIFICATION",
        "c2_v": "PUBLIC RELEASE IN 1977",
        "dossier_id": "dossier6",
        "dossier_class": "dossier-card",
        "badge_class": "dossier-badge dossier-badge-us",
        "badge_txt": "COMMANDER-IN-CHIEF",
        "asset": "assets/truman_oval_office_defense_1949.jpg",
        "name": "HARRY S. TRUMAN",
        "role": "1949: ~170 WARHEADS"
    }
]

clips_html_list = []
for b in beats_info:
    n = b["num"]
    clip_str = f'''    <section class="clip beat" id="{b["id"]}" data-start="{b["start"]}" data-duration="{b["duration"]}" data-track-index="{n}">
      <div class="top-telemetry">
        <span>GEOPOLITICAL MAPPING // 1949</span>
        <span class="badge">TOP SECRET · DROPSHOT</span>
      </div>
      <div class="tm">
        <div class="kicker">{b["kicker"]}</div>
        <div class="headline">{b["headline"]}</div>
      </div>
      <div class="{b["dossier_class"]}" id="{b["dossier_id"]}">
        <div class="{b["badge_class"]}">{b["badge_txt"]}</div>
        <div class="dossier-frame">
          <img src="{b["asset"]}" class="dossier-img" alt="{b["name"]}" />
        </div>
        <div class="dossier-info">
          <div class="dossier-name">{b["name"]}</div>
          <div class="dossier-role">{b["role"]}</div>
        </div>
      </div>
      <div class="docket">{b["docket"]}</div>
      <div class="chips">
        <div class="chip"><span class="cl">{b["c1_l"]}</span><span class="cv">{b["c1_v"]}</span></div>
        <div class="chip"><span class="cl">{b["c2_l"]}</span><span class="cv">{b["c2_v"]}</span></div>
      </div>
      <div class="cap" id="cap{n}">{cap_spans[n]}</div>
    </section>'''
    clips_html_list.append(clip_str)

clips_html = "\n".join(clips_html_list)

template_head = """<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>SH-02 · Operation Dropshot — Geopolitical Map Animation (1949)</title>
    <script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <script src="data/countries.js"></script>
    <style>
      @font-face {
        font-family: "Archivo Black";
        src: url("fonts/ArchivoBlack-Regular.ttf") format("truetype");
        font-weight: 400;
      }
      @font-face {
        font-family: "Space Mono";
        src: url("fonts/SpaceMono-Regular.ttf") format("truetype");
        font-weight: 400;
      }
      @font-face {
        font-family: "Space Mono";
        src: url("fonts/SpaceMono-Bold.ttf") format("truetype");
        font-weight: 700;
      }

      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body {
        margin: 0;
        width: 1080px;
        height: 1920px;
        overflow: hidden;
        background: #080c16;
        font-family: "Space Mono", monospace;
        color: #ffffff;
      }

      #root {
        position: absolute;
        inset: 0;
        width: 1080px;
        height: 1920px;
        overflow: hidden;
        background: radial-gradient(circle at 50% 40%, #0d1527 0%, #080c16 65%, #04060a 100%);
      }

      /* UNTIMED PERSISTENT MAP STAGE (z-index 20, no occluding div on top) */
      #map-stage {
        position: absolute;
        inset: 0;
        width: 1080px;
        height: 1920px;
        pointer-events: none;
        z-index: 20;
        overflow: hidden;
      }
      #map-svg {
        position: absolute;
        top: 0;
        left: 0;
        width: 1080px;
        height: 1920px;
      }

      /* SCRIMS: PREVENT MAP VECTORS FROM CLASHING WITH TOP HEADERS AND BOTTOM TELEMETRY */
      .topscrim {
        position: absolute;
        top: 0;
        left: 0;
        width: 1080px;
        height: 380px;
        background: linear-gradient(to bottom, rgba(4, 6, 10, 0.96) 0%, rgba(4, 6, 10, 0.85) 45%, rgba(4, 6, 10, 0.40) 75%, rgba(4, 6, 10, 0) 100%);
        pointer-events: none;
        z-index: 25;
      }
      .botscrim {
        position: absolute;
        top: 1100px;
        left: 0;
        width: 1080px;
        height: 820px;
        background: linear-gradient(to bottom, rgba(4, 6, 10, 0) 0%, rgba(4, 6, 10, 0.92) 8%, rgba(4, 6, 10, 0.99) 20%, #04060a 100%);
        pointer-events: none;
        z-index: 25;
      }

      /* CLIPS (TIMED BY HYPERFRAMES, z-index 30) */
      .clip.beat {
        position: absolute;
        inset: 0;
        width: 1080px;
        height: 1920px;
        pointer-events: none;
        background: transparent;
        z-index: 30;
      }

      /* TOP TELEMETRY */
      .top-telemetry {
        position: absolute;
        top: 60px;
        left: 60px;
        right: 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: 0.12em;
        color: #94a3b8;
        border-bottom: 2px solid rgba(255, 255, 255, 0.14);
        padding-bottom: 14px;
      }
      .badge {
        background: #b91c1c;
        color: #ffffff;
        padding: 4px 14px;
        border-radius: 4px;
        font-size: 16px;
        letter-spacing: 0.15em;
        font-weight: 700;
      }

      /* TACTICAL HEADER */
      .tm {
        position: absolute;
        top: 130px;
        left: 60px;
        width: 960px;
      }
      .kicker {
        font-size: 26px;
        font-weight: 700;
        letter-spacing: 0.20em;
        color: #F6E05E;
        text-shadow: 0 2px 14px rgba(0, 0, 0, 0.95);
      }
      .headline {
        margin-top: 10px;
        font-family: "Archivo Black", sans-serif;
        font-size: 68px;
        line-height: 1.05;
        color: #ffffff;
        letter-spacing: -0.01em;
        text-shadow: 0 4px 22px rgba(0, 0, 0, 0.95);
      }

      /* SMALL INSET DOSSIER PHOTO CARDS */
      .dossier-card {
        position: absolute;
        top: 480px;
        left: 60px;
        width: 260px;
        background: #080c16;
        border: 2px solid rgba(56, 189, 248, 0.75);
        border-radius: 12px;
        padding: 10px;
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.95), 0 0 20px rgba(56, 189, 248, 0.25);
        pointer-events: none;
      }
      .dossier-card.threat {
        border-color: rgba(239, 68, 68, 0.85);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.95), 0 0 20px rgba(239, 68, 68, 0.25);
      }
      .dossier-card.amber {
        border-color: rgba(246, 224, 94, 0.85);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.95), 0 0 20px rgba(246, 224, 94, 0.25);
      }
      .dossier-badge {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.12em;
        padding: 4px 8px;
        border-radius: 4px;
        margin-bottom: 8px;
        text-align: center;
      }
      .dossier-badge-us {
        background: rgba(56, 189, 248, 0.18);
        border: 1px solid #38bdf8;
        color: #38bdf8;
      }
      .dossier-badge-soviet {
        background: rgba(239, 68, 68, 0.18);
        border: 1px solid #ef4444;
        color: #fca5a5;
      }
      .dossier-badge-amber {
        background: rgba(246, 224, 94, 0.18);
        border: 1px solid #F6E05E;
        color: #F6E05E;
      }
      .dossier-frame {
        position: relative;
        width: 100%;
        height: 220px;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.2);
        background: #000000;
      }
      .dossier-img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(35%) contrast(1.12);
      }
      .dossier-info {
        margin-top: 10px;
        text-align: center;
      }
      .dossier-name {
        font-family: "Archivo Black", sans-serif;
        font-size: 16px;
        color: #ffffff;
        letter-spacing: 0.05em;
      }
      .dossier-role {
        font-size: 11px;
        font-weight: 700;
        color: #F6E05E;
        letter-spacing: 0.08em;
        margin-top: 3px;
      }

      /* DOCKET & TELEMETRY CHIPS (100% OPAQUE TO PREVENT VECTOR BLEED) */
      .docket {
        position: absolute;
        top: 1165px;
        left: 60px;
        width: 960px;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: 0.06em;
        color: #ffffff;
        white-space: nowrap;
        overflow: hidden;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.95);
        padding: 4px 12px;
        background: #080c16;
        border-radius: 4px;
        border-left: 3px solid rgba(255, 255, 255, 0.4);
      }
      .chips {
        position: absolute;
        top: 1210px;
        left: 60px;
        width: 960px;
      }
      .chip {
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 46px;
        margin-bottom: 6px;
        border-left: 4px solid #F6E05E;
        padding-left: 16px;
        padding-right: 16px;
        background: #080c16;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-left: 4px solid #F6E05E;
        border-radius: 0 8px 8px 0;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.95);
      }
      .cl {
        font-size: 21px;
        letter-spacing: 0.08em;
        color: #b4b4be;
      }
      .cv {
        font-size: 23px;
        font-weight: 700;
        letter-spacing: 0.03em;
        color: #ffffff;
      }

      /* CAPTIONS (MOBILE SAFE ZONE: BOTTOM <= 1490PX, >430PX FROM BOTTOM, 100% OPAQUE) */
      .cap {
        position: absolute;
        top: 1330px;
        left: 60px;
        width: 960px;
        min-height: 140px;
        max-height: 180px;
        display: flex;
        flex-wrap: wrap;
        align-content: center;
        justify-content: center;
        background: #060912;
        border: 1.5px solid rgba(246, 224, 94, 0.4);
        border-radius: 18px;
        padding: 14px 22px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.98);
      }
      .w {
        font-size: 29px;
        line-height: 1.30;
        color: #ECECEE;
        font-weight: 700;
        padding: 0 5px;
      }

      /* MAP VECTOR STYLING (NO CSS TRANSITIONS!) */
      .country-land {
        fill: #0c1220;
        stroke: #1e293b;
        stroke-width: 1.2px;
      }
      .country-allied {
        fill: #14223d;
        stroke: #38bdf8;
        stroke-width: 1.8px;
      }
      .country-ussr {
        fill: #330d14;
        stroke: #ef4444;
        stroke-width: 2.0px;
      }
      .graticule {
        fill: none;
        stroke: rgba(56, 189, 248, 0.14);
        stroke-width: 1.2px;
        stroke-dasharray: 6 6;
      }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="56.288" data-width="1080" data-height="1920">
      <audio id="vo" src="audio/vo_full.mp3" data-start="0" data-duration="56.288"></audio>

      <!-- SHARED VECTOR MAP BACKGROUND (UNTIMED FULL BLEED) -->
      <div id="map-stage" data-layout-allow-overflow>
        <svg id="map-svg" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg" data-layout-allow-overflow>
          <defs>
            <radialGradient id="grad-fireball" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#ffffff" />
              <stop offset="20%" stop-color="#fef08a" />
              <stop offset="50%" stop-color="#facc15" />
              <stop offset="80%" stop-color="#ef4444" stop-opacity="0.9" />
              <stop offset="100%" stop-color="#7f1d1d" stop-opacity="0" />
            </radialGradient>
            <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="5" result="blur" />
              <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
            </filter>
            <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="6" result="blur" />
              <feMerge><feMergeNode in="blur" /><feMergeNode in="SourceGraphic" /></feMerge>
            </filter>

            <!-- B-36 PEACEMAKER SILHOUETTE ICON -->
            <g id="icon-b36">
              <path d="M0,-30 L3,-22 L3,24 L0,30 L-3,24 L-3,-22 Z" fill="#e2e8f0" stroke="#0284c7" stroke-width="1.2" />
              <polygon points="0,-6 72,6 72,12 8,6 0,6 -8,6 -72,12 -72,6" fill="#cbd5e1" stroke="#0284c7" stroke-width="1.2" />
              <polygon points="0,22 24,27 24,30 0,28 -24,30 -24,27" fill="#94a3b8" stroke="#0284c7" stroke-width="1" />
              <circle cx="20" cy="7" r="2" fill="#38bdf8" />
              <circle cx="38" cy="8.5" r="2" fill="#38bdf8" />
              <circle cx="56" cy="10" r="2" fill="#38bdf8" />
              <circle cx="-20" cy="7" r="2" fill="#38bdf8" />
              <circle cx="-38" cy="8.5" r="2" fill="#38bdf8" />
              <circle cx="-56" cy="10" r="2" fill="#38bdf8" />
            </g>

            <!-- BASE PIN (CYAN DIAMOND) -->
            <g id="icon-base-pin">
              <polygon points="0,-12 12,0 0,12 -12,0" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
              <circle cx="0" cy="0" r="3" fill="#ffffff" />
            </g>

            <!-- TARGET CROSSHAIR PIN (RED) -->
            <g id="icon-target-pin">
              <circle cx="0" cy="0" r="8" fill="none" stroke="#ef4444" stroke-width="2" />
              <circle cx="0" cy="0" r="2" fill="#ef4444" />
              <line x1="-12" y1="0" x2="-4" y2="0" stroke="#ef4444" stroke-width="1.8" />
              <line x1="4" y1="0" x2="12" y2="0" stroke="#ef4444" stroke-width="1.8" />
              <line x1="0" y1="-12" x2="0" y2="-4" stroke="#ef4444" stroke-width="1.8" />
              <line x1="0" y1="4" x2="0" y2="12" stroke="#ef4444" stroke-width="1.8" />
            </g>

            <!-- RADIATION TREFOIL ICON -->
            <g id="icon-radiation">
              <circle cx="0" cy="0" r="14" fill="#ef4444" />
              <circle cx="0" cy="0" r="8" fill="#080c16" />
              <path d="M-8,-14 L-26,-46 A52,52 0 0,1 26,-46 L8,-14 Z" fill="#ef4444" />
              <path d="M13,6 L45,24 A52,52 0 0,1 19,52 L2,15 Z" fill="#ef4444" />
              <path d="M-13,6 L-45,24 A52,52 0 0,0 -19,52 L-2,15 Z" fill="#ef4444" />
              <circle cx="0" cy="0" r="4.5" fill="#facc15" />
            </g>
          </defs>

          <!-- MAP CAMERA GROUP (TRANSFORMED BY GSAP 2D MATRIX) -->
          <g id="map-camera-group" data-layout-allow-overflow>
            <path id="map-graticule" class="graticule" />
            <g id="countries-layer"></g>

            <!-- BEAT 1 OVERLAYS -->
            <g id="b1-overlays" opacity="1">
              <g transform="translate(106, 1041.5)">
                <circle id="b1-pulse-wash" r="25" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.6" />
                <use href="#icon-base-pin" />
              </g>
              <g transform="translate(61.4, 879.9)">
                <circle id="b1-pulse-omaha" r="30" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.6" />
                <use href="#icon-base-pin" />
              </g>
              <path id="b1-threat-arc" d="M 106 1041.5 Q 480 650 832.8 945.7" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="10 8" opacity="0.8" />
            </g>

            <!-- BEAT 2 OVERLAYS -->
            <g id="b2-overlays" opacity="0">
              <circle id="b2-target-ring-1" cx="832.8" cy="945.7" r="80" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="8 6" opacity="0.7" />
              <circle id="b2-target-ring-2" cx="832.8" cy="945.7" r="160" fill="none" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="10 8" opacity="0.5" />
              <circle id="b2-target-ring-3" cx="888.7" cy="812.7" r="120" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="8 6" opacity="0.6" />

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

              <path id="route-alaska" d="M 338.5 604.2 Q 520 540 888.7 812.7" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-dasharray="12 8" opacity="0.85" />
              <path id="route-thule" d="M 437.6 850 Q 600 920 832.8 945.7" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-dasharray="12 8" opacity="0.85" />
              <path id="route-uk" d="M 673.7 1117.5 Q 730 1020 774.3 954.3" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="10 8" opacity="0.8" />

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
                <circle id="b4-shock-1" r="25" fill="none" stroke="#facc15" stroke-width="4" opacity="0.9" />
                <circle id="b4-shock-2" r="50" fill="none" stroke="#ef4444" stroke-width="3" opacity="0.7" />
                <circle id="b4-shock-3" r="85" fill="none" stroke="#f87171" stroke-width="2" opacity="0.5" />
                <g id="b4-radiation-icon" transform="translate(0, -50) scale(0.6)">
                  <use href="#icon-radiation" />
                </g>
              </g>
              <path id="b4-fallout-plume" d="M 936 698.5 Q 780 500 520 480" fill="none" stroke="#facc15" stroke-width="3.5" stroke-dasharray="10 8" opacity="0.85" />
            </g>

            <!-- BEAT 5 OVERLAYS -->
            <g id="b5-overlays" opacity="0">
              <path d="M 106 1041.5 Q 540 580 832.8 945.7" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="12 10" opacity="0.75" />
              <path d="M 832.8 945.7 Q 540 720 106 1041.5" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="12 10" opacity="0.75" />
              <circle cx="280" cy="850" r="60" fill="none" stroke="#38bdf8" stroke-width="2.5" opacity="0.6" />
              <circle cx="780" cy="850" r="60" fill="none" stroke="#ef4444" stroke-width="2.5" opacity="0.6" />
            </g>

            <!-- BEAT 6 OVERLAYS -->
            <g id="b6-overlays" opacity="0">
              <g transform="translate(360, 680)">
                <rect x="0" y="0" width="360" height="150" rx="8" fill="#080c16" stroke="#facc15" stroke-width="1.8" opacity="0.95" />
                <text x="180" y="28" fill="#F6E05E" font-size="12" font-weight="bold" letter-spacing="1" text-anchor="middle" font-family="'Space Mono', monospace">1949 NUCLEAR WEAPONS GAP</text>
                
                <rect x="25" y="45" width="310" height="22" rx="4" fill="#330d14" stroke="#ef4444" stroke-width="1.2" />
                <rect id="b6-bar-planned" x="25" y="45" width="310" height="22" rx="4" fill="#ef4444" opacity="0.75" />
                <text x="35" y="60" fill="#ffffff" font-size="10" font-weight="bold" font-family="'Space Mono', monospace">DROPSHOT PLAN: 300 BOMBS</text>

                <rect x="25" y="76" width="310" height="22" rx="4" fill="#1e2230" stroke="#facc15" stroke-width="1.2" />
                <rect id="b6-bar-actual" x="25" y="76" width="175" height="22" rx="4" fill="#facc15" opacity="0.85" />
                <text x="35" y="91" fill="#080c16" font-size="10" font-weight="bold" font-family="'Space Mono', monospace">US STOCKPILE: ~170</text>

                <rect x="25" y="108" width="310" height="26" rx="4" fill="#140608" stroke="#ef4444" stroke-width="1" />
                <text x="180" y="125" fill="#f87171" font-size="10.5" font-weight="bold" letter-spacing="0.5" text-anchor="middle" font-family="'Space Mono', monospace">DEFICIT: -130 WARHEADS SHORT</text>
              </g>
            </g>

            <!-- TACTICAL LABELS LAYER (LAST CHILD OF SVG) -->
            <g id="tactical-labels-layer">
              <!-- Beat 1: Washington DC (x: 106, y: 1041.5) -->
              <g id="label-washington" opacity="1" transform="translate(106, 1065)">
                <rect x="0" y="0" width="175" height="22" rx="3" fill="#060912" stroke="#38bdf8" stroke-width="1.2" />
                <text x="87" y="15" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">WASHINGTON // JCS</text>
              </g>
              <!-- Beat 1: Omaha Offutt AFB (x: 61.4, y: 879.9) -->
              <g id="label-omaha" opacity="1" transform="translate(62, 905)">
                <rect x="0" y="0" width="175" height="22" rx="3" fill="#060912" stroke="#38bdf8" stroke-width="1.2" />
                <text x="87" y="15" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">OMAHA // SAC HQ</text>
              </g>

              <!-- Beat 2: Moscow (x: 832.8, y: 945.7) -> anchored westward (x > 750) -->
              <g id="label-moscow" opacity="0" transform="translate(660, 935)">
                <rect x="0" y="0" width="160" height="22" rx="3" fill="#060912" stroke="#ef4444" stroke-width="1.2" />
                <text x="80" y="15" fill="#ef4444" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">MOSCOW // TARGET 1</text>
              </g>
              <!-- Beat 2: Chelyabinsk Urals (x: 888.7, y: 812.7) -> anchored westward -->
              <g id="label-chelyabinsk" opacity="0" transform="translate(700, 802)">
                <rect x="0" y="0" width="175" height="22" rx="3" fill="#060912" stroke="#ef4444" stroke-width="1.2" />
                <text x="87" y="15" fill="#ef4444" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">CHELYABINSK // URALS</text>
              </g>

              <!-- Beat 3: Alaska Eielson (x: 338.5, y: 604.2) -->
              <g id="label-alaska" opacity="0" transform="translate(338, 565)">
                <rect x="0" y="0" width="175" height="22" rx="3" fill="#060912" stroke="#38bdf8" stroke-width="1.2" />
                <text x="87" y="15" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">ALASKA // SAC BASE</text>
              </g>
              <!-- Beat 3: Thule Greenland (x: 437.6, y: 850) -->
              <g id="label-thule" opacity="0" transform="translate(438, 815)">
                <rect x="0" y="0" width="165" height="22" rx="3" fill="#060912" stroke="#38bdf8" stroke-width="1.2" />
                <text x="82" y="15" fill="#38bdf8" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">THULE // GREENLAND</text>
              </g>

              <!-- Beat 4: Semipalatinsk (x: 936, y: 698.5) -> anchored clearly right of dossier card -->
              <g id="label-semipalatinsk" opacity="0" transform="translate(860, 740)">
                <rect x="0" y="0" width="170" height="22" rx="3" fill="#060912" stroke="#facc15" stroke-width="1.2" />
                <text x="85" y="15" fill="#facc15" font-size="8.5" font-weight="bold" text-anchor="middle" font-family="'Space Mono', monospace">SEMIPALATINSK // RDS-1</text>
              </g>
            </g>
          </g>
        </svg>
      </div>

      <!-- GRADIENT SCRIMS FOR CLEAN CONTRAST -->
      <div class="topscrim" data-layout-allow-overflow data-layout-allow-occlusion></div>
      <div class="botscrim" data-layout-allow-overflow data-layout-allow-occlusion></div>

"""

template_foot = f"""
    </div>

    <!-- CARTOGRAPHY & CONTINUOUS GSAP TIMELINE ENGINE -->
    <script>
      const width = 1080;
      const height = 1920;

      const baseProjection = d3.geoAzimuthalEquidistant()
        .rotate([20, -90, 0])
        .scale(580)
        .clipAngle(110)
        .translate([width / 2, 760]);

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
        y: 820,
        scale: 1.05
      }};

      const mapCameraGroup = document.getElementById("map-camera-group");

      function updateCamera() {{
        const s = camera.scale;
        const tx = 540 - camera.x * s;
        const ty = 760 - camera.y * s;
        mapCameraGroup.setAttribute("transform", `translate(${{tx}}, ${{ty}}) scale(${{s}})`);
      }}
      updateCamera();

      const tl = gsap.timeline({{
        paused: true,
        onUpdate: updateCamera
      }});

      // BEAT 1 (0.000s -> 8.659s)
      tl.set(camera, {{ x: 540, y: 820, scale: 1.05 }}, 0.00);
      tl.fromTo("#b1-pulse-wash", {{ r: 15, opacity: 0.9 }}, {{ r: 55, opacity: 0, duration: 1.8, repeat: 4, ease: "power1.out" }}, 0.20);
      tl.fromTo("#b1-pulse-omaha", {{ r: 15, opacity: 0.9 }}, {{ r: 60, opacity: 0, duration: 2.0, repeat: 3, ease: "power1.out" }}, 0.30);
      tl.fromTo("#b1-threat-arc", {{ strokeDashoffset: 500 }}, {{ strokeDashoffset: 0, duration: 3.5, ease: "power2.out" }}, 0.80);
      tl.fromTo("#dossier1", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 0.50);

      // BEAT 2 (8.659s -> 18.804s)
      tl.to(camera, {{ x: 840, y: 880, scale: 1.55, duration: 2.2, ease: "power2.inOut" }}, 8.659);
      tl.to("#b1-overlays", {{ opacity: 0, duration: 0.6 }}, 8.659);
      tl.to("#b2-overlays", {{ opacity: 1, duration: 0.8 }}, 9.20);
      tl.to(["#label-moscow", "#label-chelyabinsk"], {{ opacity: 1, duration: 0.6 }}, 9.80);
      tl.fromTo("#b2-target-ring-1", {{ r: 20, opacity: 0.9 }}, {{ r: 140, opacity: 0.2, duration: 2.4, repeat: 3, ease: "power1.out" }}, 9.50);
      tl.fromTo("#b2-target-ring-3", {{ r: 20, opacity: 0.9 }}, {{ r: 150, opacity: 0.2, duration: 2.6, repeat: 3, ease: "power1.out" }}, 9.80);
      tl.fromTo("#dossier2", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 9.00);

      // BEAT 3 (18.804s -> 27.278s)
      tl.to(camera, {{ x: 560, y: 800, scale: 1.25, duration: 2.0, ease: "power2.inOut" }}, 18.804);
      tl.to(["#b2-overlays", "#label-moscow", "#label-chelyabinsk"], {{ opacity: 0, duration: 0.5 }}, 18.804);
      tl.to("#b3-overlays", {{ opacity: 1, duration: 0.8 }}, 19.30);
      tl.to(["#label-alaska", "#label-thule"], {{ opacity: 1, duration: 0.6 }}, 19.80);
      tl.fromTo("#route-alaska", {{ strokeDashoffset: 800 }}, {{ strokeDashoffset: 0, duration: 4.5, ease: "none" }}, 19.40);
      tl.fromTo("#route-thule", {{ strokeDashoffset: 700 }}, {{ strokeDashoffset: 0, duration: 4.5, ease: "none" }}, 19.60);
      tl.fromTo("#route-uk", {{ strokeDashoffset: 500 }}, {{ strokeDashoffset: 0, duration: 4.0, ease: "none" }}, 19.80);
      tl.fromTo("#bomber-rig-alaska", {{ x: 0, y: 0 }}, {{ x: 420, y: 160, duration: 6.5, ease: "none" }}, 19.50);
      tl.fromTo("#bomber-rig-thule", {{ x: 0, y: 0 }}, {{ x: 300, y: 70, duration: 6.5, ease: "none" }}, 19.60);
      tl.fromTo("#dossier3", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 19.10);

      // BEAT 4 (27.278s -> 36.727s)
      tl.to(camera, {{ x: 920, y: 720, scale: 2.05, duration: 2.0, ease: "power3.inOut" }}, 27.278);
      tl.to(["#b3-overlays", "#label-alaska", "#label-thule"], {{ opacity: 0, duration: 0.5 }}, 27.278);
      tl.to("#b4-overlays", {{ opacity: 1, duration: 0.6 }}, 27.80);
      tl.to("#label-semipalatinsk", {{ opacity: 1, duration: 0.5 }}, 28.30);
      tl.fromTo("#b4-fireball", {{ r: 6, opacity: 1 }}, {{ r: 65, opacity: 0.75, duration: 1.2, ease: "power2.out" }}, 28.50);
      tl.fromTo("#b4-shock-1", {{ r: 15, opacity: 1 }}, {{ r: 160, opacity: 0, duration: 1.8, repeat: 3, ease: "power1.out" }}, 28.60);
      tl.fromTo("#b4-shock-2", {{ r: 30, opacity: 0.9 }}, {{ r: 240, opacity: 0, duration: 2.2, repeat: 2, ease: "power1.out" }}, 28.80);
      tl.to("#b4-radiation-icon", {{ rotation: 360, duration: 7.0, ease: "none" }}, 28.50);
      tl.fromTo("#b4-fallout-plume", {{ strokeDashoffset: 600 }}, {{ strokeDashoffset: 0, duration: 4.5, ease: "power2.out" }}, 29.50);
      tl.fromTo("#dossier4", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 27.60);

      // BEAT 5 (36.727s -> 45.014s)
      tl.to(camera, {{ x: 560, y: 840, scale: 1.15, duration: 2.0, ease: "power2.inOut" }}, 36.727);
      tl.to(["#b4-overlays", "#label-semipalatinsk"], {{ opacity: 0, duration: 0.5 }}, 36.727);
      tl.to("#b5-overlays", {{ opacity: 1, duration: 0.8 }}, 37.30);
      tl.fromTo("#dossier5", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 37.00);

      // BEAT 6 (45.014s -> 56.288s)
      tl.to(camera, {{ x: 540, y: 800, scale: 1.05, duration: 1.8, ease: "power2.inOut" }}, 45.014);
      tl.to("#b5-overlays", {{ opacity: 0, duration: 0.5 }}, 45.014);
      tl.to("#b6-overlays", {{ opacity: 1, duration: 0.8 }}, 45.60);
      tl.fromTo("#b6-bar-actual", {{ width: 0 }}, {{ width: 175, duration: 1.8, ease: "power2.out" }}, 46.50);
      tl.fromTo("#dossier6", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.60, ease: "power2.out" }}, 45.30);

      // WORD-LEVEL CAPTION HIGHLIGHTS
{word_tweens_code}

      // REGISTER TIMELINE ON GLOBAL
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>"""

full_html = template_head + clips_html + template_foot

target_index = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-02-operation-dropshot-map-hf/index.html"
with open(target_index, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated index.html with shifted projection and clean layering!")
