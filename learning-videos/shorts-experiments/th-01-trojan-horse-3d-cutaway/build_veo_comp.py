import os

OUT_HTML = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920, initial-scale=1.0">
<title>TH-01 Trojan Horse 3D Cutaway Explainer - @IRinANutshell</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
  body {
    width: 1080px;
    height: 1920px;
    background-color: #050811;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  #viewport {
    position: relative;
    width: 1080px;
    height: 1920px;
    overflow: hidden;
  }

  /* 3D Veo Video Plate Background */
  #bg-plate {
    position: absolute;
    top: 0;
    left: 0;
    width: 1080px;
    height: 1920px;
    object-fit: cover;
    z-index: 1;
    transform-origin: center center;
    transition: transform 0.4s ease-out;
  }

  /* Cinematic Vignette Overlay */
  #cinematic-vignette {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 45%, rgba(0,0,0,0) 40%, rgba(4, 7, 16, 0.65) 82%, rgba(2, 4, 10, 0.95) 100%);
    pointer-events: none;
    z-index: 2;
  }

  /* Top Tactical Clean HUD */
  #top-hud {
    position: absolute;
    top: 95px;
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
    border: 3.5px solid #ffffff;
    border-radius: 32px;
    padding: 12px 38px;
    color: #ffffff;
    font-size: 26px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 8px 8px 0px #000000;
  }

  /* Layer C: Flat Vector HUD & Data Cards */
  #layer-c {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 15;
  }

  /* Dimension Spec Card (Beat 2, positioned at top: 210px -> ZERO occlusion of horse!) */
  #card-dimension {
    position: absolute;
    top: 210px;
    left: 110px;
    width: 860px;
    background: #090e1c;
    border: 3.5px solid #38bdf8;
    border-radius: 18px;
    padding: 24px 32px;
    box-shadow: 14px 14px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }
  .spec-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .spec-label {
    font-size: 24px;
    font-weight: 700;
    color: #94a3b8;
    letter-spacing: 1px;
  }
  .spec-val-cyan {
    font-size: 38px;
    font-weight: 900;
    color: #38bdf8;
    letter-spacing: 1px;
  }
  .spec-val-yellow {
    font-size: 38px;
    font-weight: 900;
    color: #f59e0b;
    letter-spacing: 1px;
  }

  /* Temperature & Suffocation Alert Card (Beat 3, positioned at top: 210px -> ZERO occlusion!) */
  #card-temp {
    position: absolute;
    top: 210px;
    left: 110px;
    width: 860px;
    background: #160a0a;
    border: 3.5px solid #ef4444;
    border-radius: 18px;
    padding: 24px 32px;
    box-shadow: 14px 14px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }
  .temp-val-red {
    font-size: 42px;
    font-weight: 900;
    color: #ef4444;
    letter-spacing: 1px;
  }

  /* Microscopic Vents Badge (Beat 3, positioned at top: 410px -> CLEAN 50px gap below temp card!) */
  #badge-vents {
    position: absolute;
    top: 410px;
    left: 110px;
    width: 860px;
    padding: 20px 26px;
    background: #0284c7;
    border: 4px solid #ffffff;
    border-radius: 14px;
    color: #ffffff;
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 2px;
    text-align: center;
    box-shadow: 12px 12px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 26;
  }

  /* Outro Payoff Card (Beat 5) */
  #outro-payoff-card {
    position: absolute;
    top: 890px;
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
    font-size: 26px;
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

  /* Layer A: Photo Stickers & Archival Plates */
  #layer-a {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 20;
  }

  /* Hook Ladder Blocks (0-3.5s) */
  .hook-block {
    position: absolute;
    left: 100px;
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

  /* Archival Plates (Top centered, zero collision) */
  .sticker-prop {
    position: absolute;
    opacity: 0;
    display: none;
    z-index: 22;
    transform-origin: center top;
  }

  /* Tiepolo Trojan Horse (Beat 1) */
  #plate-tiepolo {
    top: 520px;
    left: 110px;
    width: 860px;
    height: auto;
  }

  /* Motte Night Descent (Beat 4) */
  #plate-motte {
    top: 200px;
    left: 110px;
    width: 860px;
    height: auto;
  }

  /* Mykonos Relief (Beat 5) */
  #plate-mykonos {
    top: 200px;
    left: 110px;
    width: 860px;
    height: auto;
  }

  /* Safe Area Subtitle Box: bottom: 420px (Safe from mobile UI!) */
  #subtitle-box {
    position: absolute;
    bottom: 420px;
    left: 110px;
    right: 110px;
    min-height: 110px;
    padding: 22px 34px;
    background: rgba(8, 12, 22, 0.95);
    border: 3px solid rgba(255, 255, 255, 0.4);
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #ffffff;
    font-size: 34px;
    line-height: 1.35;
    font-weight: 800;
    text-align: center;
    box-shadow: 0 16px 40px rgba(0,0,0,0.85);
    z-index: 50;
  }

  /* Channel Watermark Pill (Outro) */
  .channel-pill {
    position: absolute;
    top: 1180px;
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
  <audio id="master-audio" src="audio/final_soundtrack_master.wav" preload="auto"></audio>

  <!-- 3D Veo Simulation Background Plate -->
  <img id="bg-plate" src="assets/frames_s1/f_0001.jpg" alt="3D Simulation Plate">
  <div id="cinematic-vignette"></div>

  <!-- Top Tactical Clean HUD -->
  <div id="top-hud">
    <div class="hud-pill" id="hud-title">THE TROJAN HORSE (1184 BC)</div>
  </div>

  <!-- Layer C: Flat Vectors & Data Cards -->
  <div id="layer-c">
    <!-- Dimension Spec Card (Beat 2) -->
    <div id="card-dimension">
      <div class="spec-row">
        <span class="spec-label">HULL TIMBER THICKNESS</span>
        <span class="spec-val-cyan">18 CM (PINE)</span>
      </div>
      <div class="spec-row" style="margin-top:10px;">
        <span class="spec-label">SCAFFOLDING TIERS</span>
        <span class="spec-val-yellow">2 NARROW TIERS</span>
      </div>
      <div class="spec-row" style="margin-top:10px;">
        <span class="spec-label">INTERNAL CAPACITY</span>
        <span class="spec-val-cyan" style="color:#22c55e;">30 WARRIORS</span>
      </div>
    </div>

    <!-- Temperature & Suffocation Alert Card (Beat 3) -->
    <div id="card-temp">
      <div class="spec-row">
        <span class="spec-label">INTERNAL BELLY TEMP</span>
        <span class="temp-val-red" id="temp-stat">35°C / 95°F</span>
      </div>
      <div class="spec-row" style="margin-top:10px;">
        <span class="spec-label">SUFFOCATION THRESHOLD</span>
        <span class="temp-val-red" style="color:#f97316;">CRITICAL (3 HRS)</span>
      </div>
    </div>

    <!-- Microscopic Vents Badge (Beat 3) -->
    <div id="badge-vents">DISGUISED VENTILATION // NOSTRILS &amp; MANE CHANNELS</div>

    <!-- Outro Payoff Card (Beat 5) -->
    <div id="outro-payoff-card">
      <div class="outro-badge-title">STRATAGEM OF ODYSSEUS // THE SIEGE OF TROY</div>
      <div class="outro-badge-sub">HOW 30 MEN TOOK THE IMPREGNABLE CITY</div>
    </div>
  </div>

  <!-- Layer A: Photo Stickers & Archival Plates -->
  <div id="layer-a">
    <!-- Hook Ladder (0-3s) -->
    <div id="hook-1" class="hook-block">30 GREEK SOLDIERS</div>
    <div id="hook-2" class="hook-block">TRAPPED IN 35°C HEAT</div>
    <div id="hook-3" class="hook-block">HOW DID THEY SURVIVE?</div>

    <!-- Archival Plates -->
    <img id="plate-tiepolo" class="sticker-prop" src="assets/plate_trojan_horse.png" alt="Tiepolo Procession">
    <img id="plate-motte" class="sticker-prop" src="assets/plate_motte_night.png" alt="Motte Midnight Infiltration">
    <img id="plate-mykonos" class="sticker-prop" src="assets/plate_mykonos_pithos.png" alt="Mykonos Relief 670 BC">
  </div>

  <!-- Channel Watermark -->
  <div class="channel-pill" id="channel-badge">@IRinANutshell</div>

  <!-- Bottom Captions -->
  <div id="subtitle-box">
    <span id="subtitle-text">Could you guess how thirty Greek soldiers survived inside the Trojan Horse before Troy burned?</span>
  </div>
</div>

<script>
  // =================================================================
  // 3D VEO BACKGROUND PLATE CONTROLLER (24 FPS FRAMES EQUIVALENT)
  // =================================================================
  const bgImg = document.getElementById('bg-plate');

  function updateVideoPlate(timeSec) {
    let folder, frameNum, scale = 1.0, transY = 0;

    if (timeSec < 24.5) {
      // Beat 1, 2, 3: scene_1_cutaway (240 frames)
      folder = "assets/frames_s1/";
      const tMod = timeSec % 10.0;
      frameNum = Math.min(240, Math.max(1, Math.floor(tMod * 24) + 1));

      // Beat 3 macro zoom on upper mane & nostrils ventilation
      if (timeSec >= 15.5 && timeSec < 24.5) {
        bgImg.style.transformOrigin = "30% 25%";
        bgImg.style.transform = "scale(1.85)";
      } else {
        bgImg.style.transformOrigin = "center center";
        bgImg.style.transform = "scale(1.0)";
      }
    } else if (timeSec < 33.0) {
      // Beat 4: scene_4_trapdoor (240 frames)
      folder = "assets/frames_s4/";
      const tMod = (timeSec - 24.5) % 10.0;
      frameNum = Math.min(240, Math.max(1, Math.floor(tMod * 24) + 1));
    } else {
      // Beat 5 & Outro: scene_5_gates_outro (480 frames)
      folder = "assets/frames_s5/";
      const tMod = (timeSec - 33.0) % 20.0;
      frameNum = Math.min(480, Math.max(1, Math.floor(tMod * 24) + 1));
    }

    const pad = String(frameNum).padStart(4, "0");
    bgImg.src = `${folder}f_${pad}.jpg`;
  }

  // =================================================================
  // MASTER GSAP TIMELINE (Total 45.79s)
  // =================================================================
  const tl = gsap.timeline({ paused: true, onUpdate: () => updateVideoPlate(tl.time()) });
  window.masterTl = tl;

  const sub = document.getElementById('subtitle-text');
  const hudTitle = document.getElementById('hud-title');

  // =================================================================
  // BEAT 1: THE IMPOSSIBLE HOOK (0.0s - 5.56s)
  // Audio: Could you guess how thirty Greek soldiers survived inside the Trojan Horse before Troy burned?
  // =================================================================
  tl.set('#plate-tiepolo', { display: 'block', opacity: 1, top: '520px', scale: 0.98 }, 0);

  // Hook Ladder Slam-in (1.0s, 2.0s, 3.0s)
  tl.set('#hook-1', { display: 'flex' }, 1.0);
  tl.fromTo('#hook-1', { opacity: 0, scale: 1.4, y: -40 }, { opacity: 1, scale: 1, y: 0, duration: 0.28, ease: 'back.out(2)' }, 1.0);

  tl.set('#hook-2', { display: 'flex' }, 2.0);
  tl.fromTo('#hook-2', { opacity: 0, scale: 1.4, y: -40 }, { opacity: 1, scale: 1, y: 0, duration: 0.28, ease: 'back.out(2)' }, 2.0);

  tl.set('#hook-3', { display: 'flex' }, 3.0);
  tl.fromTo('#hook-3', { opacity: 0, scale: 1.4, y: -40 }, { opacity: 1, scale: 1, y: 0, duration: 0.28, ease: 'back.out(2)' }, 3.0);

  // Clear Hook Ladder
  tl.to(['#hook-1', '#hook-2', '#hook-3'], { opacity: 0, scale: 0.9, y: 20, duration: 0.25 }, 5.2);
  tl.set(['#hook-1', '#hook-2', '#hook-3'], { display: 'none' }, 5.5);

  // Wipe out Beat 1 plate
  tl.to('#plate-tiepolo', { opacity: 0, y: -80, duration: 0.35, ease: 'power2.in' }, 5.2);
  tl.set('#plate-tiepolo', { display: 'none' }, 5.56);

  // =================================================================
  // BEAT 2: THE TWO-TIER INTERIOR (5.56s - 15.16s)
  // Audio: Built from dismantled ship timber, the belly wasn't just a hollow box...
  // =================================================================
  tl.call(() => {
    sub.innerText = "Built from dismantled ship timber, the belly wasn't just a hollow box. It held two narrow scaffolding tiers where soldiers sat shoulder-to-shoulder in complete silence.";
    hudTitle.innerText = "INTERIOR SCAFFOLDING // 2 TIERS";
  }, null, 5.56);

  // Dimension Spec Card enters below at top: 210px
  tl.set('#card-dimension', { display: 'block', top: '210px' }, 6.2);
  tl.fromTo('#card-dimension', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.45, ease: 'power3.out' }, 6.2);

  // Clean Beat 2 Card
  tl.to('#card-dimension', { opacity: 0, y: -30, duration: 0.35, ease: 'power2.in' }, 14.8);
  tl.set('#card-dimension', { display: 'none' }, 15.16);

  // =================================================================
  // BEAT 3: THE 35°C SUFFOCATION CRISIS & VENTS (15.16s - 25.84s)
  // Audio: At thirty-five degrees Celsius, body heat alone would cause suffocation in hours...
  // =================================================================
  tl.call(() => {
    sub.innerText = "At thirty-five degrees Celsius, body heat alone would cause suffocation in hours. The builders hid microscopic air vents disguised inside the nostrils, ears, and horse mane.";
    hudTitle.innerText = "THERMAL HAZARD // 35°C (95°F)";
  }, null, 15.16);

  // Temperature alert card pops in at top: 210px
  tl.set('#card-temp', { display: 'block', top: '210px' }, 15.4);
  tl.fromTo('#card-temp', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power3.out' }, 15.4);

  // Disguised air vents badge slams down at top: 410px
  tl.set('#badge-vents', { display: 'block', top: '410px' }, 17.5);
  tl.fromTo('#badge-vents', { opacity: 0, scale: 1.4, rotation: -3 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.35, ease: 'back.out(2)' }, 17.5);

  // Clean Beat 3 Cards
  tl.to(['#card-temp', '#badge-vents'], { opacity: 0, y: -30, duration: 0.35, ease: 'power2.in' }, 25.4);
  tl.set(['#card-temp', '#badge-vents'], { display: 'none' }, 25.84);

  // =================================================================
  // BEAT 4: THE MIDNIGHT TRAPDOOR & ROPES (25.84s - 34.32s)
  // Audio: When night fell and Troy slept, Odysseus unlocked a spring-loaded trapdoor...
  // =================================================================
  tl.call(() => {
    sub.innerText = "When night fell and Troy slept, Odysseus unlocked a spring-loaded trapdoor beneath the horse's belly, dropping hemp ropes to the cobblestones below.";
    hudTitle.innerText = "MIDNIGHT DESCENT // HEMP ROPES";
  }, null, 25.84);

  // Motte Master Archival Plate enters at top: 200px
  tl.set('#plate-motte', { display: 'block', top: '200px', scale: 0.95 }, 26.2);
  tl.fromTo('#plate-motte', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: 'back.out(1.4)' }, 26.2);

  // Clean Beat 4 Plate
  tl.to('#plate-motte', { opacity: 0, y: -60, duration: 0.35, ease: 'power2.in' }, 34.0);
  tl.set('#plate-motte', { display: 'none' }, 34.32);

  // =================================================================
  // BEAT 5: THE CITY FALLS FROM THE INSIDE OUT (34.32s - 45.79s)
  // Audio: Within minutes, the gates were thrown wide open...
  // =================================================================
  tl.call(() => {
    sub.innerText = "Within minutes, the gates were thrown wide open. The city that resisted a ten-year siege fell in a single night... from the inside out.";
    hudTitle.innerText = "THE FALL OF TROY // 1184 BC";
  }, null, 34.32);

  // Mykonos Archaeological Relief plate enters at top: 200px (scale 0.92)
  tl.set('#plate-mykonos', { display: 'block', top: '200px', scale: 0.92 }, 34.6);
  tl.fromTo('#plate-mykonos', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: 'back.out(1.4)' }, 34.6);

  // Outro Payoff Card enters below at top: 890px
  tl.set('#outro-payoff-card', { display: 'block', top: '890px' }, 35.8);
  tl.fromTo('#outro-payoff-card', { opacity: 0, scale: 0.85, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: 'back.out(1.8)' }, 35.8);

  // CTA Beat 6 (42.34s)
  tl.call(() => {
    sub.innerText = "Discover more untold ancient geopolitics on IR in a Nutshell.";
    hudTitle.innerText = "SUBSCRIBE // @IRinANutshell";
  }, null, 42.34);

  // Channel badge pop-in below payoff card at top: 1180px
  tl.set('#channel-badge', { display: 'block', top: '1180px' }, 42.5);
  tl.fromTo('#channel-badge', { opacity: 0, scale: 0.7, y: 30 }, { opacity: 1, scale: 1, y: 0, duration: 0.4, ease: 'back.out(2)' }, 42.5);

  // Subtle pulse on badge
  tl.to('#channel-badge', { scale: 1.05, repeat: -1, yoyo: true, duration: 0.6, ease: 'power1.inOut' }, 43.0);
</script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"TH-01 Veo 3D Composition HTML written to {OUT_HTML}")
