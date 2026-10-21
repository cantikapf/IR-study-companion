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
  camera.position.set(0, 40, 720);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
  scene.add(ambientLight);

  const sunLight = new THREE.DirectionalLight(0xffedd5, 2.5);
  sunLight.position.set(300, 400, 500);
  scene.add(sunLight);

  const rimLight = new THREE.DirectionalLight(0x38bdf8, 1.5);
  rimLight.position.set(-400, -200, 400);
  scene.add(rimLight);

  const torchLight = new THREE.PointLight(0xf97316, 0.8, 900);
  torchLight.position.set(0, -40, 250);
  scene.add(torchLight);

  // Courtyard Stone Ground Grid (Layer B Stage)
  const gridHelper = new THREE.GridHelper(800, 16, 0x38bdf8, 0x1e293b);
  gridHelper.position.y = -180;
  scene.add(gridHelper);

  // Materials
  const woodMat = new THREE.MeshStandardMaterial({ color: 0x8b5a2b, roughness: 0.6 });
  const darkWood = new THREE.MeshStandardMaterial({ color: 0x5c3a21, roughness: 0.7 });
  const cutEdgeMat = new THREE.MeshBasicMaterial({ color: 0xf59e0b });
  const bronzeMat = new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.3, metalness: 0.8 });
  const airFlowMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.75 });

  // Group: Trojan Horse Root
  const horse = new THREE.Group();
  horse.scale.set(0.78, 0.78, 0.78);
  horse.position.set(0, -20, 0);
  scene.add(horse);

  // 1. Platform on wheels
  const plat = new THREE.Mesh(new THREE.BoxGeometry(260, 20, 380), darkWood);
  plat.position.y = -140;
  horse.add(plat);

  const wheelGeo = new THREE.CylinderGeometry(40, 40, 18, 24);
  wheelGeo.rotateZ(Math.PI / 2);
  [[-130, -145, 120], [130, -145, 120], [-130, -145, -120], [130, -145, -120]].forEach(p => {
    const w = new THREE.Mesh(wheelGeo, darkWood);
    w.position.set(...p);
    horse.add(w);
    const hub = new THREE.Mesh(new THREE.CylinderGeometry(10, 10, 24, 16), bronzeMat);
    hub.rotateZ(Math.PI / 2);
    hub.position.set(...p);
    horse.add(hub);
  });

  // 2. Legs (4 posts)
  const legGeo = new THREE.BoxGeometry(26, 140, 30);
  [[-80, -60, 100], [80, -60, 100], [-80, -60, -100], [80, -60, -100]].forEach(p => {
    const l = new THREE.Mesh(legGeo, darkWood);
    l.position.set(...p);
    horse.add(l);
  });

  // 3. HOLLOW CUTAWAY BELLY (Right side wide open at x = 50!)
  // Back wall (far side, x = -50)
  const backWall = new THREE.Mesh(new THREE.BoxGeometry(8, 170, 270), woodMat);
  backWall.position.set(-50, 60, 0);
  horse.add(backWall);

  // Floor (bottom of belly)
  const bellyFloor = new THREE.Mesh(new THREE.BoxGeometry(100, 8, 270), woodMat);
  bellyFloor.position.set(0, -25, 0);
  horse.add(bellyFloor);

  // Roof (top of spine)
  const bellyRoof = new THREE.Mesh(new THREE.BoxGeometry(100, 8, 270), woodMat);
  bellyRoof.position.set(0, 145, 0);
  horse.add(bellyRoof);

  // Chest (front wall)
  const chest = new THREE.Mesh(new THREE.BoxGeometry(100, 170, 8), woodMat);
  chest.position.set(0, 60, 135);
  horse.add(chest);

  // Rump (rear wall)
  const rump = new THREE.Mesh(new THREE.BoxGeometry(100, 170, 8), woodMat);
  rump.position.set(0, 60, -135);
  horse.add(rump);

  // Cutaway golden glowing edge frame on the open right side (x = 50)
  const edgeTop = new THREE.Mesh(new THREE.BoxGeometry(8, 12, 274), cutEdgeMat);
  edgeTop.position.set(50, 145, 0);
  horse.add(edgeTop);

  const edgeBottom = new THREE.Mesh(new THREE.BoxGeometry(8, 12, 274), cutEdgeMat);
  edgeBottom.position.set(50, -25, 0);
  horse.add(edgeBottom);

  const edgeFront = new THREE.Mesh(new THREE.BoxGeometry(8, 170, 12), cutEdgeMat);
  edgeFront.position.set(50, 60, 135);
  horse.add(edgeFront);

  const edgeBack = new THREE.Mesh(new THREE.BoxGeometry(8, 170, 12), cutEdgeMat);
  edgeBack.position.set(50, 60, -135);
  horse.add(edgeBack);

  // 4. Scaffolding Tiers inside
  const tierLower = new THREE.Mesh(new THREE.BoxGeometry(88, 8, 260), darkWood);
  tierLower.position.set(-2, 20, 0);
  horse.add(tierLower);

  const tierUpper = new THREE.Mesh(new THREE.BoxGeometry(88, 8, 260), darkWood);
  tierUpper.position.set(-2, 85, 0);
  horse.add(tierUpper);

  // Internal Warm Spotlight
  const inLight = new THREE.PointLight(0xffb703, 3.2, 450);
  inLight.position.set(20, 60, 0);
  horse.add(inLight);

  // 5. Greek Hoplite Soldiers seated in rows
  const helmGeo = new THREE.SphereGeometry(8, 16, 16);
  const crestGeo = new THREE.BoxGeometry(3, 8, 14);
  const crestMat = new THREE.MeshBasicMaterial({ color: 0xef4444 });
  const shieldGeo = new THREE.CylinderGeometry(11, 11, 4, 16);
  shieldGeo.rotateX(Math.PI / 2);
  const bodyGeo = new THREE.CylinderGeometry(8, 8, 22, 12);

  function makeHoplite(x, y, z) {
    const g = new THREE.Group();
    g.position.set(x, y, z);
    
    const b = new THREE.Mesh(bodyGeo, bronzeMat);
    b.position.y = 11;
    g.add(b);

    const h = new THREE.Mesh(helmGeo, bronzeMat);
    h.position.y = 26;
    g.add(h);

    const c = new THREE.Mesh(crestGeo, crestMat);
    c.position.set(0, 32, 0);
    g.add(c);

    const sh = new THREE.Mesh(shieldGeo, bronzeMat);
    sh.position.set(12, 14, 0);
    g.add(sh);

    return g;
  }

  // Lower tier: 16 soldiers (2 rows x 8)
  for (let r = 0; r < 2; r++) {
    for (let c = 0; c < 8; c++) {
      horse.add(makeHoplite(-30 + r * 35, 20, -100 + c * 28));
    }
  }

  // Upper tier: 14 soldiers (2 rows x 7)
  for (let r = 0; r < 2; r++) {
    for (let c = 0; c < 7; c++) {
      horse.add(makeHoplite(-30 + r * 35, 85, -90 + c * 28));
    }
  }

  // 6. Neck and Head
  const neck = new THREE.Mesh(new THREE.BoxGeometry(60, 160, 70), woodMat);
  neck.rotateX(-Math.PI / 5);
  neck.position.set(0, 175, 115);
  horse.add(neck);

  const head = new THREE.Mesh(new THREE.BoxGeometry(50, 65, 95), woodMat);
  head.position.set(0, 240, 155);
  horse.add(head);

  const mane = new THREE.Mesh(new THREE.BoxGeometry(16, 180, 30), darkWood);
  mane.position.set(0, 190, 85);
  horse.add(mane);

  // 7. Microscopic Air Ventilation Conduit Stream (Glowing Blue Tubes & Flow)
  const ventPathGroup = new THREE.Group();
  horse.add(ventPathGroup);

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
  const trapdoor = new THREE.Mesh(trapdoorGeo, darkWood);
  trapdoor.position.set(0, -28, -30);
  horse.add(trapdoor);

  // Hemp Ropes (dropping down to ground)
  const ropeGeo = new THREE.CylinderGeometry(2.5, 2.5, 125, 8);
  const ropeMat = new THREE.MeshStandardMaterial({ color: 0xd4a373, roughness: 0.9 });
  const ropeLeft = new THREE.Mesh(ropeGeo, ropeMat);
  ropeLeft.position.set(-20, -90, -30);
  horse.add(ropeLeft);

  const ropeRight = new THREE.Mesh(ropeGeo, ropeMat);
  ropeRight.position.set(20, -90, -30);
  horse.add(ropeRight);

  ropeLeft.visible = false;
  ropeRight.visible = false;

  // 3D Scene Camera State variables
  // Facing directly into the open cutaway flank (-Math.PI/2 + 0.25)
  const horseState = {
    rotY: -1.35,
    rotX: 0.12,
    camZ: 720,
    camY: 40,
    camX: 0
  };

  function updateScene() {
    horse.rotation.y = horseState.rotY;
    horse.rotation.x = horseState.rotX;
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

  // 3D Camera slow orbit around cutaway horse
  tl.to(horseState, { rotY: -1.25, rotX: 0.15, camZ: 700, duration: 5.56, ease: 'none' }, 0);

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

  // 3D Camera deep zoom directly into cutaway interior (camZ: 560, angle -1.35)
  tl.to(horseState, { rotY: -1.35, rotX: 0.16, camZ: 560, camY: 45, duration: 9.6, ease: 'power1.inOut' }, 5.56);

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

  // 3D Camera pivots to show airflow from head/nostrils down into belly
  tl.to(horseState, { rotY: -1.15, rotX: 0.24, camZ: 600, camY: 65, duration: 10.68, ease: 'power1.inOut' }, 15.16);

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
  tl.to(ambientLight, { intensity: 0.6, duration: 1.0 }, 25.84);
  tl.to(torchLight, { intensity: 2.2, duration: 1.0 }, 25.84);

  // Camera angles down to view underside of horse belly and falling ropes
  tl.to(horseState, { rotY: -1.35, rotX: -0.10, camZ: 620, camY: -15, duration: 8.48, ease: 'power1.inOut' }, 25.84);

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
    ambientLight.intensity = 1.2;
    torchLight.intensity = 0.8;
  }, null, 34.32);

  // Camera pulls back to majestic panoramic view
  tl.to(horseState, { rotY: -1.40, rotX: 0.15, camZ: 780, camY: 35, duration: 11.4, ease: 'power2.out' }, 34.32);

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

print(f"TH-01 Master Composition HTML V3 written to {OUT_HTML}")
