import os

OUT_HTML = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/composition.html"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1080, height=1920, initial-scale=1.0">
<title>SH-11 Ghost Army D-Day 1944 - @IRinANutshell</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="assets/three.min.js"></script>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
  body {
    width: 1080px;
    height: 1920px;
    background-color: #03060c;
    overflow: hidden;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }

  #viewport {
    position: relative;
    width: 1080px;
    height: 1920px;
    overflow: hidden;
  }

  /* Pillar 1: Base Layer 3D WebGL Globe */
  #webgl-canvas {
    position: absolute;
    inset: 0;
    width: 1080px;
    height: 1920px;
    z-index: 1;
  }

  /* Atmospheric Space Starfield & Vignette Overlay */
  #space-vignette {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 50%, rgba(0,0,0,0) 38%, rgba(3, 6, 14, 0.78) 82%, rgba(2, 4, 10, 0.98) 100%);
    pointer-events: none;
    z-index: 2;
  }

  /* Top Clean Human Context Header with Hard 0-blur Shadow */
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

  /* Tactical Deception Radio Arc SVG Overlay (Scene 3 & 4) */
  #deception-svg {
    position: absolute;
    top: 860px;
    left: 100px;
    width: 880px;
    height: 180px;
    opacity: 0;
    display: none;
    z-index: 24;
  }

  /* Ghost Radio Broadcast Stamp (Scene 3) */
  #stamp-radio {
    position: absolute;
    top: 1040px;
    left: 110px;
    width: 860px;
    padding: 18px 24px;
    background: #991b1b;
    border: 4px solid #ffffff;
    border-radius: 14px;
    color: #ffffff;
    font-size: 28px;
    font-weight: 900;
    letter-spacing: 2px;
    text-align: center;
    box-shadow: 12px 12px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }

  /* Deception Mileage Counter Card (Scene 4) */
  #card-counter {
    position: absolute;
    top: 960px;
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
  .counter-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .counter-label {
    font-size: 24px;
    font-weight: 700;
    color: #94a3b8;
  }
  .counter-val-red {
    font-size: 46px;
    font-weight: 900;
    color: #ef4444;
    letter-spacing: 1px;
  }

  /* Outro Hoax Payoff Card (Scene 5) */
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

  /* Hero Stickers & Archival Plates (Robust centering via left: 110px) */
  .sticker-prop {
    position: absolute;
    opacity: 0;
    display: none;
    z-index: 22;
  }

  /* Patton Master Plate (top: 210px avoids any marker overlap) */
  #plate-patton {
    top: 210px;
    left: 110px;
    width: 860px;
    height: auto;
  }

  /* Inflatable Tank Plate (Scene 3) */
  #plate-tank {
    top: 210px;
    left: 110px;
    width: 860px;
    height: auto;
  }

  /* Rommel Atlantikwall Plate (Scene 4) */
  #plate-rommel {
    top: 210px;
    left: 110px;
    width: 860px;
    height: auto;
  }

  /* Dummy Tank Cutout Sticker (Outro / Scene 5) */
  #sticker-tank-cutout {
    top: 250px;
    left: 140px;
    width: 800px;
    height: auto;
  }

  /* Safe Area Subtitle Box: bottom: 420px (Strictly safe from mobile UI!) */
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
    top: 1160px;
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

  <!-- Pillar 1: Base Layer Three.js 3D WebGL Canvas -->
  <canvas id="webgl-canvas"></canvas>
  <div id="space-vignette"></div>

  <!-- Top Tactical Clean HUD -->
  <div id="top-hud">
    <div class="hud-pill" id="hud-title">OPERATION FORTITUDE (1944)</div>
  </div>

  <!-- Layer C: Flat Vectors & Data Stamps -->
  <div id="layer-c">
    <!-- Tactical Deception Arc SVG (Motion Prompt #004 Line Draw) -->
    <svg id="deception-svg" viewBox="0 0 880 180">
      <defs>
        <filter id="glow-filter" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="4" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>
      <!-- Base tactical card plate -->
      <rect x="0" y="0" width="880" height="180" rx="16" fill="#0b1120" stroke="#38bdf8" stroke-width="3" filter="drop-shadow(8px 8px 0px #000)"/>
      <!-- Dover Origin Node -->
      <circle cx="140" cy="90" r="14" fill="#38bdf8" filter="url(#glow-filter)"/>
      <circle cx="140" cy="90" r="28" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
      <text x="140" y="145" fill="#38bdf8" font-size="20" font-weight="900" text-anchor="middle" letter-spacing="2">DOVER (HQ)</text>
      
      <!-- Pas-de-Calais Target Node -->
      <circle cx="740" cy="90" r="14" fill="#ef4444" filter="url(#glow-filter)"/>
      <circle cx="740" cy="90" r="28" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
      <text x="740" y="145" fill="#ef4444" font-size="20" font-weight="900" text-anchor="middle" letter-spacing="2">PAS-DE-CALAIS</text>
      
      <!-- Deception Arc Line Draw (Motion Prompt #004) -->
      <path id="radio-arc" d="M 160 85 Q 440 20 720 85" fill="none" stroke="#fbbf24" stroke-width="6" stroke-dasharray="600" stroke-dashoffset="600" stroke-linecap="round"/>
      <text x="440" y="45" fill="#fbbf24" font-size="22" font-weight="900" text-anchor="middle" letter-spacing="2">PHANTOM RADIO TRAFFIC</text>
    </svg>

    <div id="stamp-radio">GHOST RADIO NETWORKS // DECEPTION BROADCAST</div>

    <div id="card-counter">
      <div class="counter-row">
        <span class="counter-label">PANZER UNITS DIVERTED TO CALAIS</span>
        <span class="counter-val-red" id="counter-val">15 DIVISIONS</span>
      </div>
      <div class="counter-row" style="margin-top:8px;">
        <span class="counter-label">DISTANCE FROM REAL BEACHES</span>
        <span class="counter-val-red" style="color:#f59e0b;" id="counter-dist">200 MILES</span>
      </div>
    </div>

    <div id="outro-payoff-card">
      <div class="outro-badge-title">OPERATION FORTITUDE SOUTH // SUCCESS</div>
      <div class="outro-badge-sub">HOW INFLATABLES SAVED D-DAY</div>
    </div>
  </div>

  <!-- Layer A: Photo Stickers & Archival Plates -->
  <div id="layer-a">
    <!-- Hook Ladder (0-3s) -->
    <div id="hook-1" class="hook-block">15 PANZER DIVISIONS</div>
    <div id="hook-2" class="hook-block">HELD 200 MILES AWAY</div>
    <div id="hook-3" class="hook-block">BY INFLATABLE TANKS</div>

    <!-- Archival Plates -->
    <img id="plate-patton" class="sticker-prop" src="assets/plate_patton.png" alt="General George S. Patton">
    <img id="plate-tank" class="sticker-prop" src="assets/plate_inflatable_tank.png" alt="Inflatable Dummy Tank">
    <img id="plate-rommel" class="sticker-prop" src="assets/plate_rommel_calais.png" alt="Field Marshal Erwin Rommel">
    <img id="sticker-tank-cutout" class="sticker-prop" src="assets/sticker_dummy_tank.png" alt="M4 Sherman Inflatable Cutout">
  </div>

  <!-- Channel Watermark -->
  <div class="channel-pill" id="channel-badge">@IRinANutshell</div>

  <!-- Bottom Captions -->
  <div id="subtitle-box">
    <span id="subtitle-text">Could you guess what stopped 15 Nazi Panzer divisions 200 miles before D-Day failed?</span>
  </div>
</div>

<script>
  // =================================================================
  // THREE.JS 3D WEBGL GLOBE MAP ENGINE (WESTERN EUROPE FOCUS)
  // =================================================================
  const canvas = document.getElementById('webgl-canvas');
  const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
  renderer.setSize(1080, 1920);
  renderer.setPixelRatio(1);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(45, 1080 / 1920, 1, 3000);
  camera.position.set(0, 0, 750);

  // Lighting
  const ambientLight = new THREE.AmbientLight(0x445577, 1.1);
  scene.add(ambientLight);

  const sunLight = new THREE.DirectionalLight(0xfff8ee, 2.4);
  sunLight.position.set(400, 300, 600);
  scene.add(sunLight);

  const rimLight = new THREE.DirectionalLight(0x38bdf8, 1.5);
  rimLight.position.set(-600, -200, -200);
  scene.add(rimLight);

  // Earth Sphere
  const textureLoader = new THREE.TextureLoader();
  const earthTexture = textureLoader.load('assets/earth_map_2048.jpg');
  earthTexture.anisotropy = 4;

  const globeRadius = 280;
  const globeGeo = new THREE.SphereGeometry(globeRadius, 64, 64);
  const globeMat = new THREE.MeshStandardMaterial({
    map: earthTexture,
    roughness: 0.65,
    metalness: 0.15
  });
  const earthMesh = new THREE.Mesh(globeGeo, globeMat);
  scene.add(earthMesh);

  // Glowing Latitude/Longitude Graticule Wireframe
  const wireGeo = new THREE.SphereGeometry(globeRadius + 1.5, 36, 18);
  const wireMat = new THREE.MeshBasicMaterial({
    color: 0x38bdf8,
    wireframe: true,
    transparent: true,
    opacity: 0.16
  });
  const wireMesh = new THREE.Mesh(wireGeo, wireMat);
  scene.add(wireMesh);

  // Atmospheric Glow Ring
  const atmosGeo = new THREE.SphereGeometry(globeRadius + 8, 48, 48);
  const atmosMat = new THREE.MeshBasicMaterial({
    color: 0x0ea5e9,
    transparent: true,
    opacity: 0.08,
    side: THREE.BackSide
  });
  const atmosMesh = new THREE.Mesh(atmosGeo, atmosMat);
  scene.add(atmosMesh);

  // Coordinate helper: Lat/Lon to Vector3
  function latLonToVector3(lat, lon, radius) {
    const phi = (90 - lat) * (Math.PI / 180);
    const theta = (lon + 180) * (Math.PI / 180);
    const x = -(radius * Math.sin(phi) * Math.cos(theta));
    const z = (radius * Math.sin(phi) * Math.sin(theta));
    const y = (radius * Math.cos(phi));
    return new THREE.Vector3(x, y, z);
  }

  // Tactical Pin Maker
  function createPin(lat, lon, colorHex) {
    const group = new THREE.Group();
    const pos = latLonToVector3(lat, lon, globeRadius + 2);
    group.position.copy(pos);
    group.lookAt(0, 0, 0);

    const pinGeo = new THREE.SphereGeometry(5, 16, 16);
    const pinMat = new THREE.MeshBasicMaterial({ color: colorHex });
    const pinMesh = new THREE.Mesh(pinGeo, pinMat);
    group.add(pinMesh);

    // Glowing ring
    const ringGeo = new THREE.RingGeometry(6, 11, 32);
    const ringMat = new THREE.MeshBasicMaterial({ color: colorHex, side: THREE.DoubleSide });
    const ringMesh = new THREE.Mesh(ringGeo, ringMat);
    ringMesh.position.z = 1;
    group.add(ringMesh);

    earthMesh.add(group);
    return group;
  }

  // Tactical Pins: Dover (UK), Pas-de-Calais (France), Normandy (France)
  const pinDover = createPin(51.1279, 1.3134, 0x38bdf8);    // Cyan Pin for Dover Allied HQ
  const pinCalais = createPin(50.9513, 1.8587, 0xef4444);   // Red Pin for Pas-de-Calais
  const pinNormandy = createPin(49.3333, -0.5667, 0x22c55e);// Green Pin for Normandy

  // 3D Globe camera state variables: Initialized to WESTERN EUROPE / ENGLISH CHANNEL CENTER (-1.57, 0.88)
  const globeState = {
    rotX: 0.88,
    rotY: -1.57,
    camZ: 750,
    camY: 50,
    camX: 0
  };

  function updateGlobe() {
    earthMesh.rotation.x = globeState.rotX;
    earthMesh.rotation.y = globeState.rotY;
    wireMesh.rotation.x = globeState.rotX;
    wireMesh.rotation.y = globeState.rotY;
    camera.position.z = globeState.camZ;
    camera.position.y = globeState.camY;
    camera.position.x = globeState.camX;
    camera.lookAt(0, -30, 0);
    renderer.render(scene, camera);
  }

  updateGlobe();

  // =================================================================
  // MASTER GSAP TIMELINE (Total 42.62s)
  // =================================================================
  const tl = gsap.timeline({ paused: true, onUpdate: updateGlobe });
  window.masterTl = tl;

  const sub = document.getElementById('subtitle-text');
  const hudTitle = document.getElementById('hud-title');

  // =================================================================
  // SCENE 1: THE IMPOSSIBLE HOOK (0.0s - 6.20s)
  // Audio Line 1: Could you guess what stopped 15 Nazi Panzer divisions 200 miles before D-Day failed?
  // =================================================================
  tl.set('#plate-patton', { display: 'block', opacity: 1, top: '530px', scale: 0.98 }, 0);

  // Globe slow orbital drift centered on Western Europe
  tl.to(globeState, { rotY: -1.63, rotX: 0.90, camZ: 720, camY: 50, duration: 6.2, ease: 'none' }, 0);

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

  // Wipe out Scene 1
  tl.to('#plate-patton', { opacity: 0, y: -80, duration: 0.35, ease: 'power2.in' }, 5.8);
  tl.set('#plate-patton', { display: 'none' }, 6.2);

  // =================================================================
  // SCENE 2: THE GHOST ARMY & FUSAG (6.20s - 15.13s)
  // Audio Line 2: In 1944, the Allies created a completely fake military force: the First US Army Group, commanded by General George Patton.
  // =================================================================
  tl.call(() => {
    sub.innerText = "In 1944, the Allies created a completely fake military force: the First US Army Group, commanded by General George Patton.";
    hudTitle.innerText = "DOVER & LONDON // JUNE 1944";
  }, null, 6.20);

  // 3D Camera zooms in toward English Channel (Dover & Pas-de-Calais)
  tl.to(globeState, { rotY: -1.58, rotX: 0.92, camZ: 560, camY: 70, duration: 8.9, ease: 'power1.inOut' }, 6.20);

  // General Patton Master Archival Plate enters center (top: 210px -> zero marker overlap!)
  tl.set('#plate-patton', { display: 'block', top: '210px' }, 6.4);
  tl.fromTo('#plate-patton', { opacity: 0, scale: 1.15, y: 40 }, { opacity: 1, scale: 1.0, y: 0, duration: 0.55, ease: 'back.out(1.4)' }, 6.4);

  // Wipe out Scene 2 assets at 14.7s
  tl.to('#plate-patton', { opacity: 0, y: -80, duration: 0.35, ease: 'power2.in' }, 14.7);
  tl.set('#plate-patton', { display: 'none' }, 15.1);

  // =================================================================
  // SCENE 3: THE INFLATABLE DECEPTION (15.13s - 22.67s)
  // Audio Line 3: Across the coast of Dover, soldiers inflated dummy rubber tanks, parked wooden aircraft, and broadcasted ghost radio chatter.
  // =================================================================
  tl.call(() => {
    sub.innerText = "Across the coast of Dover, soldiers inflated dummy rubber tanks, parked wooden aircraft, and broadcasted ghost radio chatter.";
    hudTitle.innerText = "OPERATION FORTITUDE // DOVER DECOYS";
  }, null, 15.13);

  // Camera focuses tightly on Dover staging grounds
  tl.to(globeState, { rotY: -1.55, rotX: 0.90, camZ: 500, camY: 80, duration: 7.5, ease: 'power1.out' }, 15.13);

  // Inflatable Dummy Tank Master Plate enters at top: 210px
  tl.set('#plate-tank', { display: 'block', top: '210px' }, 15.2);
  tl.fromTo('#plate-tank', { opacity: 0, scale: 1.15, y: 40 }, { opacity: 1, scale: 1.0, y: 0, duration: 0.5, ease: 'power3.out' }, 15.2);

  // Tactical Deception Arc SVG enters at top: 840px (Motion Prompt #004 Line Draw)
  tl.set('#deception-svg', { display: 'block' }, 16.8);
  tl.fromTo('#deception-svg', { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.4 }, 16.8);
  tl.to('#radio-arc', { strokeDashoffset: 0, duration: 1.4, ease: 'power1.inOut' }, 17.2);

  // Ghost Radio Stamp slams down at bottom at top: 1040px
  tl.set('#stamp-radio', { display: 'block' }, 18.2);
  tl.fromTo('#stamp-radio', { opacity: 0, scale: 1.6, rotation: -6 }, { opacity: 1, scale: 1, rotation: -1.5, duration: 0.35, ease: 'back.out(2.2)' }, 18.2);

  // Wipe out Scene 3
  tl.to(['#plate-tank', '#deception-svg', '#stamp-radio'], { opacity: 0, y: -60, duration: 0.35, ease: 'power2.in' }, 22.2);
  tl.set(['#plate-tank', '#deception-svg', '#stamp-radio'], { display: 'none' }, 22.6);

  // =================================================================
  // SCENE 4: HITLER'S BLUNDER (22.67s - 31.82s)
  // Audio Line 4: German reconnaissance fell for the trap. Hitler became convinced the real invasion would land at Pas-de-Calais, holding his best tanks 200 miles away.
  // =================================================================
  tl.call(() => {
    sub.innerText = "German reconnaissance fell for the trap. Hitler became convinced the real invasion would land at Pas-de-Calais, holding his best tanks 200 miles away.";
    hudTitle.innerText = "PAS-DE-CALAIS // 15TH PANZER ARMY";
  }, null, 22.67);

  // 3D Camera pivots across English Channel toward Pas-de-Calais
  tl.to(globeState, { rotY: -1.52, rotX: 0.88, camZ: 520, camY: 70, duration: 9.1, ease: 'power1.inOut' }, 22.67);

  // Rommel Atlantikwall Plate enters at top: 210px
  tl.set('#plate-rommel', { display: 'block', top: '210px' }, 22.8);
  tl.fromTo('#plate-rommel', { opacity: 0, scale: 1.15, y: 40 }, { opacity: 1, scale: 1.0, y: 0, duration: 0.5, ease: 'power3.out' }, 22.8);

  // Counter Card enters below Rommel plate at top: 960px
  tl.set('#card-counter', { display: 'block' }, 24.5);
  tl.fromTo('#card-counter', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.4, ease: 'power3.out' }, 24.5);

  // Clean Scene 4
  tl.to(['#plate-rommel', '#card-counter'], { opacity: 0, y: -40, duration: 0.35, ease: 'power2.in' }, 31.4);
  tl.set(['#plate-rommel', '#card-counter'], { display: 'none' }, 31.8);

  // =================================================================
  // SCENE 5: THE PAYOFF & OUTRO (31.82s - 42.62s)
  // Audio Line 5 & 6: By the time Berlin realized Normandy was the real assault, it was too late...
  // =================================================================
  tl.call(() => {
    sub.innerText = "By the time Berlin realized Normandy was the real assault, it was too late. An army of rubber balloons saved the Western world.";
    hudTitle.innerText = "D-DAY VICTORY // JUNE 6, 1944";
  }, null, 31.82);

  // 3D Camera pulls back to panoramic space orbit view of entire globe
  tl.to(globeState, { rotY: -1.65, rotX: 0.78, camZ: 780, camY: 40, duration: 10.8, ease: 'power2.out' }, 31.82);

  // Sherman Inflatable Decoy Cutout Sticker enters center (top: 250px)
  tl.set('#sticker-tank-cutout', { display: 'block', top: '250px' }, 31.9);
  tl.fromTo('#sticker-tank-cutout', { opacity: 0, scale: 1.2, rotation: 8 }, { opacity: 1, scale: 1.0, rotation: 2, duration: 0.5, ease: 'back.out(1.5)' }, 31.9);

  // Outro Payoff Card enters below tank at top: 890px
  tl.set('#outro-payoff-card', { display: 'block', top: '890px' }, 33.2);
  tl.fromTo('#outro-payoff-card', { opacity: 0, scale: 0.85, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: 'back.out(1.8)' }, 33.2);

  // Line 6 Call-To-Action (39.60s)
  tl.call(() => {
    sub.innerText = "Discover more untold geopolitics on IR in a Nutshell.";
    hudTitle.innerText = "SUBSCRIBE // @IRinANutshell";
  }, null, 39.60);

  // Channel badge pop-in below payoff card at top: 1160px
  tl.set('#channel-badge', { display: 'block', top: '1160px' }, 39.8);
  tl.fromTo('#channel-badge', { opacity: 0, scale: 0.7, y: 30 }, { opacity: 1, scale: 1, y: 0, duration: 0.4, ease: 'back.out(2)' }, 39.8);

  // Continuous subtle pulse on channel badge
  tl.to('#channel-badge', { scale: 1.05, repeat: -1, yoyo: true, duration: 0.6, ease: 'power1.inOut' }, 40.3);
</script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"SH-11 Composition HTML V3 written to {OUT_HTML}")
