import os

OUT_HTML = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920, initial-scale=1.0">
<title>TH-01 Trojan Horse 3D Cutaway Explainer - @IRinANutshell</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="assets/three.min.js"></script>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
  body {
    width: 1080px;
    height: 1920px;
    background-color: #070b16;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  #viewport {
    position: relative;
    width: 1080px;
    height: 1920px;
    overflow: hidden;
  }

  /* Base 3D WebGL Cutaway Canvas */
  #webgl-canvas {
    position: absolute;
    inset: 0;
    width: 1080px;
    height: 1920px;
    z-index: 1;
  }

  /* Cinematic Vignette */
  #cinematic-vignette {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 45%, rgba(0,0,0,0) 45%, rgba(4, 7, 16, 0.65) 85%, rgba(2, 4, 10, 0.95) 100%);
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

  /* Dimension Spec Card (Beat 2) */
  #card-dimension {
    position: absolute;
    top: 930px;
    left: 100px;
    width: 880px;
    background: #090e1c;
    border: 3.5px solid #38bdf8;
    border-radius: 18px;
    padding: 22px 30px;
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
    font-size: 23px;
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

  /* Temperature & Suffocation Alert Card (Beat 3) */
  #card-temp {
    position: absolute;
    top: 930px;
    left: 100px;
    width: 880px;
    background: #160a0a;
    border: 3.5px solid #ef4444;
    border-radius: 18px;
    padding: 22px 30px;
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

  /* Microscopic Vents Badge (Beat 3) */
  #badge-vents {
    position: absolute;
    top: 1080px;
    left: 110px;
    width: 860px;
    padding: 18px 24px;
    background: #0284c7;
    border: 4px solid #ffffff;
    border-radius: 14px;
    color: #ffffff;
    font-size: 26px;
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
    top: 900px;
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
    top: 530px;
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
    left: 70px;
    right: 70px;
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

  <!-- 3D WebGL Cutaway Scene -->
  <canvas id="webgl-canvas"></canvas>
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
        <span class="spec-val-yellow">2 COMPACT TIERS</span>
      </div>
      <div class="spec-row" style="margin-top:10px;">
        <span class="spec-label">CREW CAPACITY</span>
        <span class="spec-val-cyan" style="color:#22c55e;">30 HOPLITES</span>
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
  // THREE.JS 3D STYLIZED CUTAWAY TROJAN HORSE ENGINE
  // =================================================================
  const canvas = document.getElementById('webgl-canvas');
  const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: false });
  renderer.setSize(1080, 1920);
  renderer.setPixelRatio(1);

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0a1020);
  scene.fog = new THREE.FogExp2(0x0a1020, 0.0009);

  const camera = new THREE.PerspectiveCamera(45, 1080 / 1920, 1, 3000);
  camera.position.set(0, 30, 850);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0x4a5568, 1.4);
  scene.add(ambientLight);

  const keyLight = new THREE.DirectionalLight(0xfff1dc, 2.8);
  keyLight.position.set(400, 500, 600);
  scene.add(keyLight);

  const fillLight = new THREE.DirectionalLight(0x38bdf8, 1.6);
  fillLight.position.set(-500, -200, 400);
  scene.add(fillLight);

  const torchLight = new THREE.PointLight(0xf97316, 1.2, 900);
  torchLight.position.set(0, -40, 250);
  scene.add(torchLight);

  // Courtyard Stone Ground Grid (Layer B Stage)
  const gridHelper = new THREE.GridHelper(900, 18, 0x38bdf8, 0x1e293b);
  gridHelper.position.y = -190;
  scene.add(gridHelper);

  // Materials
  const woodDarkMat = new THREE.MeshStandardMaterial({
    color: 0x6b4423,
    roughness: 0.65,
    metalness: 0.1
  });

  const woodLightMat = new THREE.MeshStandardMaterial({
    color: 0xa06d3b,
    roughness: 0.6,
    metalness: 0.05
  });

  const cutEdgeMat = new THREE.MeshBasicMaterial({
    color: 0xf59e0b
  });

  const bronzeMat = new THREE.MeshStandardMaterial({
    color: 0xdf8a1e,
    roughness: 0.35,
    metalness: 0.85
  });

  const airFlowMat = new THREE.MeshBasicMaterial({
    color: 0x38bdf8,
    transparent: true,
    opacity: 0.75
  });

  // Group: Trojan Horse Root (Scale calibrated to 0.74 so entire model fits!)
  const horseGroup = new THREE.Group();
  horseGroup.scale.set(0.74, 0.74, 0.74);
  horseGroup.position.set(0, -30, 0);
  scene.add(horseGroup);

  // 1. Wheeled Wooden Platform
  const platformGeo = new THREE.BoxGeometry(260, 22, 400);
  const platformMesh = new THREE.Mesh(platformGeo, woodDarkMat);
  platformMesh.position.y = -140;
  horseGroup.add(platformMesh);

  // 4 Giant Heavy Spoked Wheels
  const wheelGeo = new THREE.CylinderGeometry(42, 42, 20, 24);
  wheelGeo.rotateZ(Math.PI / 2);
  const wheelPositions = [
    [-135, -145, 130],
    [135, -145, 130],
    [-135, -145, -130],
    [135, -145, -130]
  ];
  wheelPositions.forEach(pos => {
    const wheel = new THREE.Mesh(wheelGeo, woodDarkMat);
    wheel.position.set(...pos);
    horseGroup.add(wheel);

    // Bronze wheel hub
    const hub = new THREE.Mesh(new THREE.CylinderGeometry(12, 12, 26, 16), bronzeMat);
    hub.rotateZ(Math.PI / 2);
    hub.position.set(...pos);
    horseGroup.add(hub);
  });

  // 2. Horse Legs (4 sturdy pillars)
  const legGeo = new THREE.BoxGeometry(28, 140, 32);
  const legPositions = [
    [-80, -60, 110],
    [80, -60, 110],
    [-80, -60, -110],
    [80, -60, -110]
  ];
  legPositions.forEach(pos => {
    const leg = new THREE.Mesh(legGeo, woodDarkMat);
    leg.position.set(...pos);
    horseGroup.add(leg);
  });

  // 3. Hollow Belly Hull & Cutaway
  // Left half of hull (solid outer wood)
  const hullLeftGeo = new THREE.BoxGeometry(100, 170, 270);
  const hullLeftMesh = new THREE.Mesh(hullLeftGeo, woodLightMat);
  hullLeftMesh.position.set(-50, 60, 0);
  horseGroup.add(hullLeftMesh);

  // Back panel of right side (giving cutaway cross-section)
  const hullRightGeo = new THREE.BoxGeometry(16, 170, 270);
  const hullRightMesh = new THREE.Mesh(hullRightGeo, woodDarkMat);
  hullRightMesh.position.set(50, 60, 0);
  horseGroup.add(hullRightMesh);

  // Cutaway golden edge frame
  const edgeTop = new THREE.Mesh(new THREE.BoxGeometry(12, 10, 272), cutEdgeMat);
  edgeTop.position.set(50, 145, 0);
  horseGroup.add(edgeTop);

  const edgeBottom = new THREE.Mesh(new THREE.BoxGeometry(12, 10, 272), cutEdgeMat);
  edgeBottom.position.set(50, -25, 0);
  horseGroup.add(edgeBottom);

  // 4. Interior Scaffolding Tiers (Upper & Lower)
  const scaffoldGeo = new THREE.BoxGeometry(94, 10, 250);
  
  // Lower Tier Platform
  const tierLower = new THREE.Mesh(scaffoldGeo, woodDarkMat);
  tierLower.position.set(0, 15, 0);
  horseGroup.add(tierLower);

  // Upper Tier Platform
  const tierUpper = new THREE.Mesh(scaffoldGeo, woodDarkMat);
  tierUpper.position.set(0, 85, 0);
  horseGroup.add(tierUpper);

  // Interior Structural Ribs (3 vertical wooden frames)
  [-75, 0, 75].forEach(z => {
    const rib = new THREE.Mesh(new THREE.BoxGeometry(96, 150, 10), woodDarkMat);
    rib.position.set(0, 60, z);
    horseGroup.add(rib);
  });

  // 5. Stylized 30 Greek Hoplite Soldiers inside the tiers
  const soldierGroup = new THREE.Group();
  horseGroup.add(soldierGroup);

  const helmetGeo = new THREE.SphereGeometry(8, 16, 16);
  const shieldGeo = new THREE.CylinderGeometry(10, 10, 4, 16);
  shieldGeo.rotateX(Math.PI / 2);
  const bodyGeo = new THREE.CylinderGeometry(7, 7, 18, 12);

  function createSoldier(x, y, z) {
    const s = new THREE.Group();
    s.position.set(x, y, z);
    
    // Body / Cuirass
    const b = new THREE.Mesh(bodyGeo, bronzeMat);
    b.position.y = 9;
    s.add(b);

    // Helmet with crest
    const h = new THREE.Mesh(helmetGeo, bronzeMat);
    h.position.y = 22;
    s.add(h);

    // Red Horsehair crest
    const crest = new THREE.Mesh(new THREE.BoxGeometry(3, 7, 12), new THREE.MeshBasicMaterial({ color: 0xef4444 }));
    crest.position.set(0, 27, 0);
    s.add(crest);

    // Bronze Shield
    const sh = new THREE.Mesh(shieldGeo, bronzeMat);
    sh.position.set(10, 12, 0);
    s.add(sh);

    return s;
  }

  // Populate Lower Tier (16 soldiers, 2 rows of 8)
  for (let r = 0; r < 2; r++) {
    for (let c = 0; c < 8; c++) {
      const x = -20 + r * 30;
      const z = -90 + c * 26;
      soldierGroup.add(createSoldier(x, 20, z));
    }
  }

  // Populate Upper Tier (14 soldiers, 2 rows of 7)
  for (let r = 0; r < 2; r++) {
    for (let c = 0; c < 7; c++) {
      const x = -20 + r * 30;
      const z = -80 + c * 26;
      soldierGroup.add(createSoldier(x, 90, z));
    }
  }

  // 6. Horse Neck, Head, and Mane
  const neckGeo = new THREE.BoxGeometry(65, 160, 75);
  neckGeo.rotateX(-Math.PI / 5);
  const neckMesh = new THREE.Mesh(neckGeo, woodLightMat);
  neckMesh.position.set(0, 175, 115);
  horseGroup.add(neckMesh);

  const headGeo = new THREE.BoxGeometry(54, 65, 95);
  const headMesh = new THREE.Mesh(headGeo, woodLightMat);
  headMesh.position.set(0, 240, 155);
  horseGroup.add(headMesh);

  // Mane (stepped crest)
  const maneGeo = new THREE.BoxGeometry(18, 180, 32);
  const maneMesh = new THREE.Mesh(maneGeo, woodDarkMat);
  maneMesh.position.set(0, 190, 85);
  horseGroup.add(maneMesh);

  // 7. Microscopic Air Ventilation Conduit Stream (Glowing Blue Tubes & Flow)
  const ventPathGroup = new THREE.Group();
  horseGroup.add(ventPathGroup);

  const ventGeo = new THREE.CylinderGeometry(4, 4, 150, 12);
  const ventTube = new THREE.Mesh(ventGeo, airFlowMat);
  ventTube.position.set(0, 170, 115);
  ventTube.rotateX(-Math.PI / 5);
  ventPathGroup.add(ventTube);

  const particleGeo = new THREE.SphereGeometry(3.5, 8, 8);
  for (let p = 0; p < 24; p++) {
    const part = new THREE.Mesh(particleGeo, airFlowMat);
    part.position.set(-25 + Math.random() * 50, 30 + Math.random() * 80, -90 + Math.random() * 180);
    ventPathGroup.add(part);
  }
  ventPathGroup.visible = false;

  // 8. Trapdoor Mechanism beneath Belly
  const trapdoorGeo = new THREE.BoxGeometry(65, 8, 85);
  const trapdoor = new THREE.Mesh(trapdoorGeo, woodDarkMat);
  trapdoor.position.set(0, -25, -30);
  horseGroup.add(trapdoor);

  // Hemp Ropes (dropping down to ground)
  const ropeGeo = new THREE.CylinderGeometry(2.5, 2.5, 125, 8);
  const ropeMat = new THREE.MeshStandardMaterial({ color: 0xd4a373, roughness: 0.9 });
  const ropeLeft = new THREE.Mesh(ropeGeo, ropeMat);
  ropeLeft.position.set(-20, -90, -30);
  horseGroup.add(ropeLeft);

  const ropeRight = new THREE.Mesh(ropeGeo, ropeMat);
  ropeRight.position.set(20, -90, -30);
  horseGroup.add(ropeRight);

  ropeLeft.visible = false;
  ropeRight.visible = false;

  // 3D Scene Camera State variables
  const horseState = {
    rotY: 0.65,
    rotX: 0.14,
    camZ: 820,
    camY: 35,
    camX: 0
  };

  function updateScene() {
    horseGroup.rotation.y = horseState.rotY;
    horseGroup.rotation.x = horseState.rotX;
    camera.position.z = horseState.camZ;
    camera.position.y = horseState.camY;
    camera.position.x = horseState.camX;
    camera.lookAt(0, 35, 0);
    renderer.render(scene, camera);
  }

  updateScene();

  // =================================================================
  // MASTER GSAP TIMELINE (Total 45.79s)
  // =================================================================
  const tl = gsap.timeline({ paused: true, onUpdate: updateScene });
  window.masterTl = tl;

  const sub = document.getElementById('subtitle-text');
  const hudTitle = document.getElementById('hud-title');

  // =================================================================
  // BEAT 1: THE IMPOSSIBLE HOOK (0.0s - 5.56s)
  // Audio: Could you guess how thirty Greek soldiers survived inside the Trojan Horse before Troy burned?
  // =================================================================
  tl.set('#plate-tiepolo', { display: 'block', opacity: 1, top: '530px', scale: 0.98 }, 0);

  // 3D Camera slow orbit around the cutaway wooden horse
  tl.to(horseState, { rotY: 0.85, rotX: 0.16, camZ: 780, duration: 5.56, ease: 'none' }, 0);

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

  // 3D Camera deep zoom directly into cutaway interior (angle 1.25, camZ: 580)
  tl.to(horseState, { rotY: 1.30, rotX: 0.20, camZ: 580, camY: 55, duration: 9.6, ease: 'power1.inOut' }, 5.56);

  // Dimension Spec Card enters below at top: 930px
  tl.set('#card-dimension', { display: 'block' }, 6.2);
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
    ventPathGroup.visible = true;
  }, null, 15.16);

  // 3D Camera pivots to show airflow from head/nostrils down to belly
  tl.to(horseState, { rotY: 1.10, rotX: 0.28, camZ: 620, camY: 75, duration: 10.68, ease: 'power1.inOut' }, 15.16);

  // Temperature alert card pops in at top: 930px
  tl.set('#card-temp', { display: 'block' }, 15.4);
  tl.fromTo('#card-temp', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power3.out' }, 15.4);

  // Disguised air vents badge slams down at top: 1080px
  tl.set('#badge-vents', { display: 'block' }, 17.5);
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
    ventPathGroup.visible = false;
    ropeLeft.visible = true;
    ropeRight.visible = true;
    trapdoor.rotation.x = Math.PI / 3; // Trapdoor swings down
  }, null, 25.84);

  // Lighting shifts to night mode: lower ambient, increase warm torchlight
  tl.to(ambientLight, { intensity: 0.8, duration: 1.0 }, 25.84);
  tl.to(torchLight, { intensity: 2.2, duration: 1.0 }, 25.84);

  // Camera angles down to view underside of horse belly and falling ropes
  tl.to(horseState, { rotY: 0.88, rotX: -0.12, camZ: 640, camY: -20, duration: 8.48, ease: 'power1.inOut' }, 25.84);

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
    ambientLight.intensity = 1.4;
    torchLight.intensity = 1.2;
  }, null, 34.32);

  // Camera pulls back to majestic panoramic view
  tl.to(horseState, { rotY: 0.60, rotX: 0.16, camZ: 850, camY: 40, duration: 11.4, ease: 'power2.out' }, 34.32);

  // Mykonos Archaeological Relief plate enters at top: 200px (scale 0.92)
  tl.set('#plate-mykonos', { display: 'block', top: '200px', scale: 0.92 }, 34.6);
  tl.fromTo('#plate-mykonos', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: 'back.out(1.4)' }, 34.6);

  // Outro Payoff Card enters below at top: 900px
  tl.set('#outro-payoff-card', { display: 'block', top: '900px' }, 35.8);
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

print(f"TH-01 Composition HTML V2 written to {OUT_HTML}")
