import os

OUT_HTML = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/composition.html"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920, initial-scale=1.0">
<title>The Suez Crisis 1956 - @IRinANutshell</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
  body {
    width: 1080px;
    height: 1920px;
    background-color: #060911;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  #viewport {
    position: relative;
    width: 1080px;
    height: 1920px;
    overflow: hidden;
  }

  /* Layer B: Adaptive 3D Staging Backgrounds */
  .stage-layer {
    position: absolute;
    inset: 0;
    width: 1080px;
    height: 1920px;
    background-size: cover;
    background-position: center;
    opacity: 0;
    display: none;
    z-index: 1;
  }
  #stage-1 { background-image: url('assets/stage_suez_map.png'); display: block; opacity: 1; }
  #stage-2 { background-image: url('assets/stage_suez_map.png'); }
  #stage-3 { background-image: url('assets/stage_pentagon.png'); }
  #stage-4 { background-image: url('assets/stage_treasury.png'); }
  #stage-5 { background-image: url('assets/stage_dispatch.png'); }

  /* Top Clean Human Context Header with Hard 0-blur Shadow */
  #top-hud {
    position: absolute;
    top: 100px;
    left: 60px;
    right: 60px;
    height: 64px;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 40;
  }
  .hud-pill {
    background: #000000;
    border: 3px solid #ffffff;
    border-radius: 32px;
    padding: 12px 38px;
    color: #ffffff;
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 8px 8px 0px #000000;
  }

  /* Layer C: Flat Vector HUD & Tactical Cards */
  #layer-c {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 15;
  }

  /* Operation Musketeer Stamp */
  #stamp-musketeer {
    position: absolute;
    top: 1080px;
    left: 540px;
    transform: translateX(-50%) scale(1.3) rotate(-2deg);
    width: 860px;
    padding: 20px 28px;
    background: #991b1b;
    border: 4px solid #ffffff;
    border-radius: 14px;
    color: #ffffff;
    font-size: 34px;
    font-weight: 900;
    letter-spacing: 3px;
    text-align: center;
    box-shadow: 12px 12px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }

  /* Canal Blocked Warning Card */
  #card-canal-blocked {
    position: absolute;
    top: 860px;
    left: 110px;
    width: 860px;
    background: #0f172a;
    border: 4px solid #ef4444;
    border-radius: 18px;
    padding: 24px 34px;
    color: #ffffff;
    box-shadow: 12px 12px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }
  .card-header-red {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #ef4444;
    margin-bottom: 8px;
  }
  .card-body-white {
    font-size: 36px;
    font-weight: 900;
    color: #ffffff;
  }

  /* Ultimatum Ceasefire Banner */
  #card-ultimatum {
    position: absolute;
    top: 960px;
    left: 100px;
    width: 880px;
    background: #111827;
    border: 4px solid #f59e0b;
    border-radius: 18px;
    padding: 26px 34px;
    box-shadow: 14px 14px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }
  .ultimatum-title {
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #f59e0b;
  }
  .ultimatum-text {
    font-size: 36px;
    font-weight: 900;
    color: #ffffff;
    margin-top: 6px;
  }

  /* SVG Crash Line Graph (Harmonious Vertical Distribution at top: 660px) */
  #crash-graph-container {
    position: absolute;
    top: 660px;
    left: 100px;
    width: 880px;
    background: rgba(11, 16, 26, 0.96);
    border: 3.5px solid #dc2626;
    border-radius: 18px;
    padding: 22px 26px;
    box-shadow: 14px 14px 0px #000000;
    display: none;
    opacity: 0;
    z-index: 26;
  }
  .graph-header {
    display: flex;
    justify-content: space-between;
    font-size: 24px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #f87171;
    text-transform: uppercase;
    margin-bottom: 10px;
  }

  /* Financial Ticker Card (Evenly spaced at top: 1010px) */
  #ticker-card {
    position: absolute;
    top: 1010px;
    left: 100px;
    width: 880px;
    background: #090d16;
    border: 3.5px solid #dc2626;
    border-radius: 18px;
    padding: 22px 30px;
    box-shadow: 14px 14px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }
  .ticker-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }
  .ticker-label {
    font-size: 24px;
    font-weight: 700;
    color: #94a3b8;
  }
  .ticker-val-red {
    font-size: 44px;
    font-weight: 900;
    color: #ef4444;
    letter-spacing: 1px;
  }

  /* Red Stamp: IMF Loan Blocked */
  #stamp-imf {
    position: absolute;
    top: 1220px;
    left: 120px;
    width: 840px;
    padding: 18px 26px;
    background: #b91c1c;
    border: 4px solid #ffffff;
    border-radius: 14px;
    color: #ffffff;
    font-size: 36px;
    font-weight: 900;
    letter-spacing: 3px;
    text-align: center;
    box-shadow: 12px 12px 0px #000000;
    opacity: 0;
    transform: scale(1.3) rotate(3deg);
    display: none;
    z-index: 28;
  }

  /* Outro Checkmate Stat Badge (Scene 5) */
  #outro-checkmate-card {
    position: absolute;
    top: 880px;
    left: 100px;
    width: 880px;
    background: #0f172a;
    border: 4px solid #fbbf24;
    border-radius: 20px;
    padding: 28px 36px;
    text-align: center;
    box-shadow: 14px 14px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 30;
  }
  .outro-badge-title {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #fbbf24;
    margin-bottom: 8px;
  }
  .outro-badge-sub {
    font-size: 38px;
    font-weight: 900;
    color: #ffffff;
  }

  /* Layer A: Photo Stickers & Cutouts */
  #layer-a {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 20;
  }

  /* Hook Ladder Blocks (0-3.5s) */
  .hook-block {
    position: absolute;
    left: 540px;
    transform: translateX(-50%);
    width: 880px;
    height: 98px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    border: 4px solid #000000;
    border-radius: 14px;
    box-shadow: 12px 12px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 35;
  }
  #hook-1 { top: 180px; background: #ffe600; color: #000000; }
  #hook-2 { top: 295px; background: #b91c1c; color: #ffffff; border-color: #ffffff; }
  #hook-3 { top: 410px; background: #ffffff; color: #000000; }

  /* Hero Stickers */
  .sticker-prop {
    position: absolute;
    opacity: 0;
    display: none;
    z-index: 22;
  }

  /* Eden Sticker */
  #sticker-eden {
    top: 500px;
    left: 540px;
    transform: translateX(-50%) rotate(-3deg);
    width: 780px;
    height: auto;
  }

  /* Tanker Ship */
  #sticker-tanker {
    top: 920px;
    left: 540px;
    transform: translateX(-50%) rotate(2deg);
    width: 700px;
    height: auto;
  }

  /* Nasser Bust */
  #sticker-nasser {
    top: 190px;
    left: 80px;
    transform: rotate(-3deg);
    width: 420px;
    height: auto;
  }

  /* Musketeer Dossier Card */
  #sticker-musketeer-card {
    top: 520px;
    left: 540px;
    transform: translateX(-50%) rotate(2deg);
    width: 760px;
    height: auto;
  }

  /* Eisenhower Oval Office Desk Plate (880px wide) */
  #sticker-ike {
    top: 260px;
    left: 540px;
    transform: translateX(-50%) rotate(1.5deg);
    width: 880px;
    height: auto;
  }

  /* Pound Cracked Banknote (top: 220px, evenly centered) */
  #sticker-pound {
    top: 220px;
    left: 540px;
    transform: translateX(-50%) rotate(-3deg);
    width: 660px;
    height: auto;
  }

  /* Safe Area Subtitle Box: bottom: 420px (Strictly safe above 0-380px mobile UI!) */
  #subtitle-box {
    position: absolute;
    bottom: 420px;
    left: 70px;
    right: 70px;
    min-height: 110px;
    padding: 22px 34px;
    background: rgba(8, 12, 20, 0.95);
    border: 3px solid rgba(255, 255, 255, 0.4);
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ffffff;
    font-size: 35px;
    line-height: 1.35;
    font-weight: 800;
    text-align: center;
    box-shadow: 0 16px 40px rgba(0,0,0,0.8);
    z-index: 50;
  }

  /* Channel Watermark Pill (Outro) */
  .channel-pill {
    position: absolute;
    top: 1140px;
    left: 540px;
    transform: translateX(-50%);
    background: #000000;
    border: 3.5px solid #ffffff;
    border-radius: 32px;
    padding: 16px 48px;
    color: #ffffff;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: 2px;
    box-shadow: 10px 10px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 55;
  }
</style>
</head>
<body>
<div id="viewport">
  <audio id="master-audio" src="audio/voiceover_master.wav" preload="auto"></audio>

  <!-- Layer B: Adaptive 3D Staging -->
  <div id="stage-1" class="stage-layer"></div>
  <div id="stage-2" class="stage-layer"></div>
  <div id="stage-3" class="stage-layer"></div>
  <div id="stage-4" class="stage-layer"></div>
  <div id="stage-5" class="stage-layer"></div>

  <!-- Top Tactical Clean HUD -->
  <div id="top-hud">
    <div class="hud-pill" id="hud-title">THE SUEZ CRISIS (1956)</div>
  </div>

  <!-- Layer C: Flat Vectors & Data Stamps -->
  <div id="layer-c">
    <div id="card-canal-blocked">
      <div class="card-header-red">STRATEGIC CHOKEPOINT SEIZED</div>
      <div class="card-body-white">CANAL CLOSED // 40+ SHIPS TRAPPED</div>
    </div>

    <div id="stamp-musketeer">OPERATION MUSKETEER // SECRET PROTOCOL</div>

    <div id="card-ultimatum">
      <div class="ultimatum-title">WASHINGTON ULTIMATUM // POTUS 34</div>
      <div class="ultimatum-text">IMMEDIATE UNCONDITIONAL CEASEFIRE</div>
    </div>

    <!-- SVG Crash Line Draw Container -->
    <div id="crash-graph-container">
      <div class="graph-header">
        <span>STERLING LIQUIDATION CURVE</span>
        <span style="color:#ef4444;">RUN IN PROGRESS</span>
      </div>
      <svg id="crash-svg" width="830" height="220" viewBox="0 0 830 220">
        <line x1="20" y1="30" x2="810" y2="30" stroke="rgba(255,255,255,0.12)" stroke-dasharray="6,6" stroke-width="2"/>
        <line x1="20" y1="100" x2="810" y2="100" stroke="rgba(255,255,255,0.12)" stroke-dasharray="6,6" stroke-width="2"/>
        <line x1="20" y1="170" x2="810" y2="170" stroke="rgba(255,255,255,0.12)" stroke-dasharray="6,6" stroke-width="2"/>
        
        <path id="crash-area" d="M 30,35 L 230,50 L 440,110 L 630,175 L 800,195 L 800,210 L 30,210 Z" fill="url(#red-fade)" opacity="0"/>
        <path id="crash-line" d="M 30,35 L 230,50 L 440,110 L 630,175 L 800,195" fill="none" stroke="#ef4444" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
        <circle id="crash-dot" cx="800" cy="195" r="10" fill="#ffffff" stroke="#ef4444" stroke-width="5" opacity="0"/>
        
        <defs>
          <linearGradient id="red-fade" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#ef4444" stop-opacity="0.45"/>
            <stop offset="100%" stop-color="#ef4444" stop-opacity="0.0"/>
          </linearGradient>
        </defs>
      </svg>
    </div>

    <div id="ticker-card">
      <div class="ticker-row">
        <span class="ticker-label">BANK OF ENGLAND GOLD RESERVES</span>
        <span class="ticker-val-red" id="ticker-loss">-15%</span>
      </div>
      <div class="ticker-row" style="margin-bottom:0;">
        <span class="ticker-label">STERLING RUN DRAINAGE</span>
        <span class="ticker-val-red" id="ticker-drain" style="color:#f59e0b;">$279M</span>
      </div>
    </div>

    <div id="stamp-imf">IMF EMERGENCY LOAN BLOCKED</div>

    <div id="outro-checkmate-card">
      <div class="outro-badge-title">SUPERPOWER SUCCESSION CONFIRMED</div>
      <div class="outro-badge-sub">THE END OF THE BRITISH EMPIRE</div>
    </div>
  </div>

  <!-- Layer A: Photo Stickers & Cutouts -->
  <div id="layer-a">
    <!-- Hook Ladder (0-3s) -->
    <div id="hook-1" class="hook-block">DEFEATED AN EMPIRE</div>
    <div id="hook-2" class="hook-block">ZERO BULLETS</div>
    <div id="hook-3" class="hook-block">ONE PHONE CALL</div>

    <!-- Hero Archival Cutout Stickers -->
    <img id="sticker-eden" class="sticker-prop" src="assets/sticker_anthony_eden.png" alt="Anthony Eden">
    <img id="sticker-tanker" class="sticker-prop" src="assets/sticker_tanker.png" alt="Tanker Ship">
    <img id="sticker-nasser" class="sticker-prop" src="assets/sticker_nasser.png" alt="Gamal Abdel Nasser">
    <img id="sticker-musketeer-card" class="sticker-prop" src="assets/sticker_musketeer_card.png" alt="Operation Musketeer">
    <img id="sticker-ike" class="sticker-prop" src="assets/sticker_eisenhower_plate.png" alt="Dwight Eisenhower Oval Office">
    <img id="sticker-pound" class="sticker-prop" src="assets/sticker_pound_cracked.png" alt="Cracked Pound Banknote">
  </div>

  <!-- Channel Watermark -->
  <div class="channel-pill" id="channel-badge">@IRinANutshell</div>

  <!-- Bottom Captions -->
  <div id="subtitle-box">
    <span id="subtitle-text">In 1956, America defeated the British Empire... without firing a single bullet.</span>
  </div>
</div>

<script>
  // Master GSAP Timeline (Total 40.21s)
  const tl = gsap.timeline({ paused: true });
  window.masterTl = tl;

  const sub = document.getElementById('subtitle-text');
  const hudTitle = document.getElementById('hud-title');

  // Pre-calculate SVG path stroke length for Motion Prompt #004 line draw
  const crashPath = document.querySelector('#crash-line');
  const pathLen = crashPath.getTotalLength();
  crashPath.style.strokeDasharray = pathLen;
  crashPath.style.strokeDashoffset = pathLen;

  // =================================================================
  // SCENE 1: THE IMPOSSIBLE STANDOFF (0.0s - 6.30s)
  // Audio Line 1: In 1956, America defeated the British Empire... without firing a single bullet.
  // =================================================================
  tl.set('#stage-1', { display: 'block', opacity: 1 }, 0);
  tl.set('#sticker-eden', { display: 'block', opacity: 1, top: '500px', scale: 1.0 }, 0);

  // Hook Ladder Slam-in (1.0s, 2.0s, 3.0s)
  tl.set('#hook-1', { display: 'flex' }, 1.0);
  tl.fromTo('#hook-1', { opacity: 0, scale: 1.4, y: -40 }, { opacity: 1, scale: 1, y: 0, duration: 0.28, ease: 'back.out(2)' }, 1.0);

  tl.set('#hook-2', { display: 'flex' }, 2.0);
  tl.fromTo('#hook-2', { opacity: 0, scale: 1.4, y: -40 }, { opacity: 1, scale: 1, y: 0, duration: 0.28, ease: 'back.out(2)' }, 2.0);

  tl.set('#hook-3', { display: 'flex' }, 3.0);
  tl.fromTo('#hook-3', { opacity: 0, scale: 1.4, y: -40 }, { opacity: 1, scale: 1, y: 0, duration: 0.28, ease: 'back.out(2)' }, 3.0);

  // Clear Hook Ladder before scene transition
  tl.to(['#hook-1', '#hook-2', '#hook-3'], { opacity: 0, scale: 0.9, y: 20, duration: 0.25 }, 5.8);
  tl.set(['#hook-1', '#hook-2', '#hook-3'], { display: 'none' }, 6.1);

  // Clean wipe out Eden for Scene 2
  tl.to('#sticker-eden', { opacity: 0, x: -150, duration: 0.35, ease: 'power2.in' }, 5.9);
  tl.set('#sticker-eden', { display: 'none' }, 6.3);

  // =================================================================
  // SCENE 2: OPERATION MUSKETEER (6.30s - 13.71s)
  // Audio Line 2: When Egypt nationalized the Suez Canal, Britain, France, and Israel launched a secret invasion: Operation Musketeer.
  // =================================================================
  tl.call(() => {
    sub.innerText = "When Egypt nationalized the Suez Canal, Britain, France, and Israel launched a secret invasion: Operation Musketeer.";
    hudTitle.innerText = "PORT SAID // NOVEMBER 1956";
  }, null, 6.30);

  // Nasser Bust enters top-left
  tl.set('#sticker-nasser', { display: 'block' }, 6.35);
  tl.fromTo('#sticker-nasser', { opacity: 0, x: -100, scale: 0.9 }, { opacity: 1, x: 0, scale: 1, duration: 0.45, ease: 'back.out(1.5)' }, 6.35);

  // Tanker ship enters on canal stage at top: 740px
  tl.set('#sticker-tanker', { display: 'block', top: '740px', scale: 0.92 }, 6.4);
  tl.fromTo('#sticker-tanker', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power3.out' }, 6.4);

  // Canal Blocked Card enters below tanker at top: 960px
  tl.set('#card-canal-blocked', { display: 'block', top: '960px' }, 6.8);
  tl.fromTo('#card-canal-blocked', { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power3.out' }, 6.8);

  // At 9.0s: Canal Blocked card & tanker slide out to make room for Operation Musketeer Dossier Card
  tl.to(['#card-canal-blocked', '#sticker-tanker'], { opacity: 0, y: 40, duration: 0.3, ease: 'power2.in' }, 9.0);
  tl.set(['#card-canal-blocked', '#sticker-tanker'], { display: 'none' }, 9.3);

  // Operation Musketeer Dossier Card enters at top: 520px
  tl.set('#sticker-musketeer-card', { display: 'block' }, 9.2);
  tl.fromTo('#sticker-musketeer-card', { opacity: 0, scale: 1.2, y: -40 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: 'back.out(1.8)' }, 9.2);

  // Stamp slams down at bottom at top: 1080px
  tl.set('#stamp-musketeer', { display: 'block' }, 9.8);
  tl.fromTo('#stamp-musketeer', { opacity: 0, scale: 1.6, rotation: -6 }, { opacity: 1, scale: 1, rotation: -2, duration: 0.3, ease: 'back.out(2.2)' }, 9.8);

  // Clean Scene 2 assets
  tl.to(['#sticker-nasser', '#sticker-musketeer-card', '#stamp-musketeer'], {
    opacity: 0,
    y: 40,
    duration: 0.35,
    ease: 'power2.in'
  }, 13.3);
  tl.set(['#sticker-nasser', '#sticker-musketeer-card', '#stamp-musketeer'], { display: 'none' }, 13.68);

  // =================================================================
  // SCENE 3: THE EISENHOWER ULTIMATUM (13.71s - 21.53s)
  // Audio Line 3: They expected American backing. Instead, President Eisenhower was furious. He demanded an immediate unconditional ceasefire.
  // =================================================================
  tl.call(() => {
    sub.innerText = "They expected American backing. Instead, President Eisenhower was furious. He demanded an immediate unconditional ceasefire.";
    hudTitle.innerText = "THE WHITE HOUSE // NOV 6, 1956";
  }, null, 13.71);

  tl.set('#stage-3', { display: 'block', opacity: 0 }, 13.71);
  tl.to('#stage-3', { opacity: 1, duration: 0.3 }, 13.71);

  // Eisenhower enters at CENTER (top: 260px, width: 880px)
  tl.set('#sticker-ike', { display: 'block', top: '260px', scale: 1.0 }, 13.75);
  tl.fromTo('#sticker-ike', { opacity: 0, scale: 1.15, y: 40 }, { opacity: 1, scale: 1.0, y: 0, duration: 0.5, ease: 'power3.out' }, 13.75);

  // Eisenhower shifts up slightly at 17.2s
  tl.to('#sticker-ike', { top: '190px', scale: 0.94, duration: 0.5, ease: 'power2.inOut' }, 17.2);

  // Ultimatum Card enters below Eisenhower at top: 960px (zero collision, 100px gap!)
  tl.set('#card-ultimatum', { display: 'block', top: '960px' }, 17.6);
  tl.fromTo('#card-ultimatum', { opacity: 0, scale: 0.85, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: 'back.out(1.8)' }, 17.6);

  // Clean Scene 3 assets
  tl.to(['#sticker-ike', '#card-ultimatum'], { opacity: 0, x: -100, duration: 0.35, ease: 'power2.in' }, 21.1);
  tl.set(['#sticker-ike', '#card-ultimatum'], { display: 'none' }, 21.5);

  // =================================================================
  // SCENE 4: THE FINANCIAL JUGULAR (21.53s - 29.30s)
  // Audio Line 4: When London refused, Washington hit their financial jugular: dumping British pounds and blocking emergency IMF loans.
  // =================================================================
  tl.call(() => {
    sub.innerText = "When London refused, Washington hit their financial jugular: dumping British pounds and blocking emergency IMF loans.";
    hudTitle.innerText = "US TREASURY // RUN ON STERLING";
  }, null, 21.53);

  tl.set('#stage-4', { display: 'block', opacity: 0 }, 21.53);
  tl.to('#stage-4', { opacity: 1, duration: 0.3 }, 21.53);

  // Cracked Pound Banknote enters at top: 220px (width 660px)
  tl.set('#sticker-pound', { display: 'block', top: '220px' }, 21.6);
  tl.fromTo('#sticker-pound', { opacity: 0, scale: 1.05, rotation: -6 }, { opacity: 1, scale: 0.90, rotation: -3, duration: 0.5, ease: 'back.out(1.5)' }, 21.6);

  // SVG Crash Line Draw Container enters at top: 660px (90px gap below banknote!)
  tl.set('#crash-graph-container', { display: 'block', top: '660px' }, 22.2);
  tl.fromTo('#crash-graph-container', { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.35, ease: 'power2.out' }, 22.2);

  // Kinetic Crash Line Plunge Animation (#004 Line Draw)
  tl.to('#crash-line', { strokeDashoffset: 0, duration: 1.1, ease: 'power2.inOut' }, 22.5);
  tl.to(['#crash-area', '#crash-dot'], { opacity: 1, duration: 0.35 }, 23.4);

  // Ticker Card enters below crash line at top: 1010px (90px gap below crash graph!)
  tl.set('#ticker-card', { display: 'block', top: '1010px' }, 23.6);
  tl.fromTo('#ticker-card', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power3.out' }, 23.6);

  // IMF Stamp Slams Down at top: 1220px
  tl.set('#stamp-imf', { display: 'block', top: '1220px' }, 25.5);
  tl.fromTo('#stamp-imf', { opacity: 0, scale: 1.6, rotation: 10 }, { opacity: 1, scale: 1, rotation: 3, duration: 0.35, ease: 'back.out(2.4)' }, 25.5);

  // Clean Scene 4 assets
  tl.to(['#sticker-pound', '#crash-graph-container', '#ticker-card', '#stamp-imf'], { opacity: 0, y: -40, duration: 0.35, ease: 'power2.in' }, 28.9);
  tl.set(['#sticker-pound', '#crash-graph-container', '#ticker-card', '#stamp-imf'], { display: 'none' }, 29.28);

  // =================================================================
  // SCENE 5: FINANCIAL CHECKMATE & OUTRO (29.30s - 40.21s)
  // Audio Line 5 & 6: Facing total currency collapse within days, London surrendered...
  // =================================================================
  tl.call(() => {
    sub.innerText = "Facing total currency collapse within days, London surrendered. The empire died not by gunfire, but by financial checkmate.";
    hudTitle.innerText = "10 DOWNING ST // RESIGNATION";
  }, null, 29.30);

  tl.set('#stage-5', { display: 'block', opacity: 0 }, 29.30);
  tl.to('#stage-5', { opacity: 1, duration: 0.3 }, 29.30);

  // Anthony Eden returns at top: 220px (scale 0.82, centered)
  tl.set('#sticker-eden', { display: 'block', top: '220px', scale: 0.82 }, 29.35);
  tl.fromTo('#sticker-eden', { opacity: 0, scale: 0.95, y: 30 }, { opacity: 1, scale: 0.82, y: 0, duration: 0.5, ease: 'power3.out' }, 29.35);

  // Outro Checkmate Stat Badge enters at top: 880px (width 880px)
  tl.set('#outro-checkmate-card', { display: 'block', top: '880px' }, 31.0);
  tl.fromTo('#outro-checkmate-card', { opacity: 0, scale: 0.85, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: 'back.out(1.8)' }, 31.0);

  // Line 6 Call-To-Action (37.19s)
  tl.call(() => {
    sub.innerText = "Discover more untold geopolitics on IR in a Nutshell.";
    hudTitle.innerText = "THE DEATH OF AN EMPIRE";
  }, null, 37.19);

  // Channel badge pop-in below checkmate card at top: 1140px
  tl.set('#channel-badge', { display: 'block', top: '1140px' }, 37.3);
  tl.fromTo('#channel-badge', { opacity: 0, scale: 0.7, y: 30 }, { opacity: 1, scale: 1, y: 0, duration: 0.4, ease: 'back.out(2)' }, 37.3);

  // Continuous subtle pulse on channel badge
  tl.to('#channel-badge', { scale: 1.05, repeat: -1, yoyo: true, duration: 0.6, ease: 'power1.inOut' }, 37.8);
</script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Composition HTML written to {OUT_HTML}")
