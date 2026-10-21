import os

content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SH-08 Malacca Chokepoint - 3D Tactical Globe & Bathymetric Matrix</title>
  <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
  <script src="https://cdn.jsdelivr.net/npm/topojson-client@3"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="data/countries.js"></script>
  <style>
    @font-face {
      font-family: 'Archivo Black';
      src: url('fonts/ArchivoBlack-Regular.ttf') format('truetype');
    }
    @font-face {
      font-family: 'Space Mono';
      src: url('fonts/SpaceMono-Regular.ttf') format('truetype');
      font-weight: normal;
    }
    @font-face {
      font-family: 'Space Mono';
      src: url('fonts/SpaceMono-Bold.ttf') format('truetype');
      font-weight: bold;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body, html {
      width: 1080px;
      height: 1920px;
      overflow: hidden;
      background: #04060d;
      color: #fff;
      font-family: 'Space Mono', monospace;
    }

    #stage {
      position: relative;
      width: 1080px;
      height: 1920px;
      background: radial-gradient(circle at 50% 45%, #081122 0%, #03050a 100%);
      overflow: hidden;
      perspective: 1400px;
    }

    /* TOP INTEL HUD */
    .intel-header {
      position: absolute;
      top: 50px;
      left: 60px;
      right: 60px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1.5px solid rgba(0, 240, 255, 0.25);
      padding-bottom: 20px;
      z-index: 100;
    }
    .intel-title {
      font-size: 22px;
      letter-spacing: 3px;
      color: #00f0ff;
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: bold;
    }
    .intel-dot {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #00f0ff;
      box-shadow: 0 0 12px #00f0ff;
    }
    .intel-badge {
      background: rgba(230, 57, 70, 0.15);
      border: 1.5px solid #e63946;
      color: #ff4d5e;
      padding: 6px 16px;
      font-size: 16px;
      letter-spacing: 2px;
      border-radius: 4px;
      font-weight: bold;
    }

    /* 3D WEBGL GLOBE CANVAS */
    #three-globe-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 1080px;
      height: 1920px;
      z-index: 10;
    }

    /* 2D TACTICAL MAP SVG VIEWPORT (FOR DEEP ZOOM) */
    #map-svg {
      position: absolute;
      top: 0;
      left: 0;
      width: 1080px;
      height: 1920px;
      z-index: 20;
      opacity: 0;
      pointer-events: none;
    }
    .ocean { fill: none; }
    .land { fill: #0e1726; stroke: #1b2a42; stroke-width: 1.2px; }
    .focus-land { fill: #16243b; stroke: #2a4166; stroke-width: 1.8px; }
    .graticule { fill: none; stroke: rgba(148, 163, 184, 0.05); stroke-width: 0.8px; }

    .traffic-lane {
      fill: none;
      stroke: rgba(0, 240, 255, 0.35);
      stroke-width: 8px;
      stroke-linecap: round;
    }
    .traffic-core {
      fill: none;
      stroke: #00f0ff;
      stroke-width: 2.5px;
      stroke-dasharray: 6 10;
    }
    .bypass-lane {
      fill: none;
      stroke: rgba(245, 158, 11, 0.8);
      stroke-width: 5px;
      stroke-dasharray: 8 6;
      opacity: 0;
    }

    /* PARTICLES CANVAS */
    #particles-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 1080px;
      height: 1920px;
      z-index: 25;
      pointer-events: none;
    }

    /* 3D ISOMETRIC BATHYMETRIC TANK MODULE */
    #bathy-3d-scene {
      position: absolute;
      top: 360px;
      left: 60px;
      right: 60px;
      height: 700px;
      background: rgba(5, 10, 22, 0.96);
      border: 1.5px solid rgba(0, 240, 255, 0.45);
      border-radius: 12px;
      padding: 28px;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.95);
      backdrop-filter: blur(16px);
      z-index: 80;
      opacity: 0;
      pointer-events: none;
    }
    .module-header {
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
      padding-bottom: 12px;
      margin-bottom: 20px;
    }
    .module-title {
      font-size: 17px;
      letter-spacing: 2px;
      color: #00f0ff;
      font-weight: bold;
    }
    .module-sub {
      font-size: 14px;
      color: #e63946;
      letter-spacing: 1.5px;
      font-weight: bold;
    }
    .bathy-svg {
      width: 100%;
      height: 580px;
    }

    /* 3D KINETIC SUPPLY CHAIN MODULE */
    #supply-3d-scene {
      position: absolute;
      top: 360px;
      left: 60px;
      right: 60px;
      height: 700px;
      background: rgba(5, 10, 22, 0.96);
      border: 1.5px solid rgba(0, 240, 255, 0.45);
      border-radius: 12px;
      padding: 28px;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.95);
      backdrop-filter: blur(16px);
      z-index: 85;
      opacity: 0;
      pointer-events: none;
    }

    /* CHOKEPOINT TARGETING RETICLE & CALIPER */
    #choke-reticle {
      position: absolute;
      top: 920px;
      left: 540px;
      transform: translate(-50%, -50%);
      width: 220px;
      height: 220px;
      border: 1px dashed rgba(230, 57, 70, 0.6);
      border-radius: 50%;
      pointer-events: none;
      opacity: 0;
      z-index: 40;
    }
    .reticle-corner {
      position: absolute;
      width: 24px;
      height: 24px;
      border: 2px solid #e63946;
    }
    .rc-tl { top: -2px; left: -2px; border-right: none; border-bottom: none; }
    .rc-tr { top: -2px; right: -2px; border-left: none; border-bottom: none; }
    .rc-bl { bottom: -2px; left: -2px; border-right: none; border-top: none; }
    .rc-br { bottom: -2px; right: -2px; border-left: none; border-top: none; }

    #caliper-badge {
      position: absolute;
      top: 760px;
      left: 540px;
      transform: translate(-50%, -50%);
      background: rgba(230, 57, 70, 0.95);
      border: 1.5px solid #ff4d5e;
      color: #ffffff;
      padding: 10px 24px;
      border-radius: 6px;
      font-size: 20px;
      font-weight: bold;
      letter-spacing: 2px;
      box-shadow: 0 0 25px rgba(230, 57, 70, 0.6);
      opacity: 0;
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* TELEMETRY OVERLAY CARD */
    #telemetry-box {
      position: absolute;
      top: 180px;
      left: 60px;
      background: rgba(6, 11, 24, 0.92);
      border: 1px solid rgba(0, 240, 255, 0.35);
      border-left: 5px solid #00f0ff;
      border-radius: 8px;
      padding: 22px 30px;
      backdrop-filter: blur(12px);
      z-index: 90;
      opacity: 0;
      transform: translateX(-30px);
    }
    .tel-metric {
      font-size: 14px;
      color: #94a3b8;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .tel-counter {
      font-family: 'Archivo Black', sans-serif;
      font-size: 44px;
      color: #ffffff;
      line-height: 1.1;
    }
    .tel-counter span { color: #00f0ff; }

    /* SAFE ZONE CAPTION OVERLAY (Bottom > 380px) */
    #caption-bar {
      position: absolute;
      bottom: 420px;
      left: 60px;
      right: 60px;
      background: rgba(4, 7, 16, 0.96);
      border: 2px solid rgba(0, 240, 255, 0.35);
      border-radius: 14px;
      padding: 28px 36px;
      backdrop-filter: blur(20px);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
      z-index: 100;
      text-align: center;
    }
    .caption-tag {
      font-size: 16px;
      color: #00f0ff;
      letter-spacing: 3px;
      font-weight: bold;
      margin-bottom: 8px;
    }
    .caption-headline {
      font-family: 'Archivo Black', sans-serif;
      font-size: 36px;
      line-height: 1.28;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    /* BOTTOM TELEMETRY FOOTER */
    .hud-footer {
      position: absolute;
      bottom: 220px;
      left: 60px;
      right: 60px;
      display: flex;
      justify-content: space-between;
      color: rgba(148, 163, 184, 0.7);
      font-size: 14px;
      letter-spacing: 2px;
      z-index: 50;
    }
  </style>
</head>
<body>
  <div id="stage">
    <!-- TOP INTEL BAR -->
    <div class="intel-header">
      <div class="intel-title">
        <div class="intel-dot"></div>
        <span>3D MARITIME RADAR // MALACCA AIS</span>
      </div>
      <div class="intel-badge">SECTOR: HIGH THREAT</div>
    </div>

    <!-- 3D THREE.JS GLOBE CONTAINER -->
    <div id="three-globe-container"></div>

    <!-- 2D VECTOR MAP FOR DEEP ZOOM -->
    <svg id="map-svg" viewBox="0 0 1080 1920">
      <g id="map-camera">
        <path id="ocean-bg" class="ocean" d=""></path>
        <path id="graticule-lines" class="graticule" d=""></path>
        <g id="land-layer"></g>
        <path id="traffic-glow" class="traffic-lane" d=""></path>
        <path id="traffic-core" class="traffic-core" d=""></path>
        <path id="sunda-bypass" class="bypass-lane" d=""></path>
        <g id="choke-radar-rings"></g>
      </g>
    </svg>

    <!-- LIVING PARTICLES CANVAS -->
    <canvas id="particles-canvas" width="1080" height="1920"></canvas>

    <!-- CHOKEPOINT TARGETING RETICLE & CALIPER -->
    <div id="choke-reticle">
      <div class="reticle-corner rc-tl"></div>
      <div class="reticle-corner rc-tr"></div>
      <div class="reticle-corner rc-bl"></div>
      <div class="reticle-corner rc-br"></div>
    </div>
    <div id="caliper-badge">
      <span style="color: #ffdd00;">GAP:</span> 1.5 NAUTICAL MILES (2.8 KM)
    </div>

    <!-- TELEMETRY BOX -->
    <div id="telemetry-box">
      <div class="tel-metric">ANNUAL TRANSIT VOLUME</div>
      <div class="tel-counter"><span id="counter-ships">0</span> VESSELS</div>
      <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">60% WORLD CRUDE OIL TRANSIT</div>
    </div>

    <!-- 3D ISOMETRIC BATHYMETRY MODULE -->
    <div id="bathy-3d-scene">
      <div class="module-header">
        <div class="module-title">STRAIT BATHYMETRIC PROFILE // PHILLIPS CHANNEL</div>
        <div class="module-sub">CRITICAL UNDER-KEEL CLEARANCE</div>
      </div>
      <svg class="bathy-svg" viewBox="0 0 880 500">
        <rect x="40" y="80" width="800" height="300" fill="rgba(0, 240, 255, 0.06)" stroke="rgba(0, 240, 255, 0.2)" />
        <line x1="40" y1="80" x2="840" y2="80" stroke="#00f0ff" stroke-width="2" stroke-dasharray="8 4" />
        <text x="50" y="65" fill="#00f0ff" font-size="14" font-family="'Space Mono'">SEA LEVEL 0.0M</text>

        <path d="M 40 380 Q 240 370, 360 330 T 520 305 T 680 340 T 840 380 L 840 460 L 40 460 Z" fill="#141c2e" stroke="#e63946" stroke-width="2.5" />
        <text x="50" y="440" fill="#e63946" font-size="14" font-family="'Space Mono'">SHALLOW REEF SEABED (DEPTH: 23M)</text>

        <!-- 3D Extruded Hull -->
        <g id="tanker-hull" transform="translate(320, 78)">
          <path d="M 0 0 L 240 0 L 230 195 L 30 195 Z" fill="#1e293b" stroke="#64748b" stroke-width="2" />
          <path d="M 240 0 L 270 -25 L 260 170 L 230 195 Z" fill="#131b26" stroke="#475569" stroke-width="1.5" />
          <path d="M 0 0 L 30 -25 L 270 -25 L 240 0 Z" fill="#334155" stroke="#64748b" stroke-width="1.5" />
          <rect x="25" y="195" width="190" height="8" fill="#e63946" />
          <text x="35" y="100" fill="#ffffff" font-size="16" font-weight="bold" font-family="'Archivo Black'">VLCC SUPERTANKER</text>
          <text x="35" y="130" fill="#94a3b8" font-size="13" font-family="'Space Mono'">DRAFT: 20.5 METERS</text>
        </g>

        <!-- Dynamic Clearance Gap Caliper -->
        <g id="clearance-caliper" transform="translate(565, 275)">
          <line x1="0" y1="0" x2="0" y2="30" stroke="#ffdd00" stroke-width="3" />
          <line x1="-12" y1="0" x2="12" y2="0" stroke="#ffdd00" stroke-width="3" />
          <line x1="-12" y1="30" x2="12" y2="30" stroke="#ffdd00" stroke-width="3" />
          <text x="20" y="20" fill="#ffdd00" font-size="16" font-weight="bold" font-family="'Space Mono'">CLEARANCE: 2.8M</text>
          <text x="20" y="42" fill="#e63946" font-size="13" font-family="'Space Mono'">GROUNDING HAZARD</text>
        </g>
      </svg>
    </div>

    <!-- 3D KINETIC SUPPLY CHAIN MODULE -->
    <div id="supply-3d-scene">
      <div class="module-header">
        <div class="module-title">GLOBAL SILICON FLOW // ARTERY DEPENDENCY</div>
        <div class="module-sub">CHOKEPOINT CASCADE SIMULATION</div>
      </div>
      <svg class="bathy-svg" viewBox="0 0 880 500">
        <!-- Node 1: Taiwan/Hsinchu -->
        <g transform="translate(140, 160)">
          <circle r="36" fill="rgba(0, 240, 255, 0.15)" stroke="#00f0ff" stroke-width="2.5" />
          <circle r="8" fill="#00f0ff" />
          <text x="0" y="60" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="bold">TSMC / TAIWAN</text>
          <text x="0" y="80" text-anchor="middle" fill="#00f0ff" font-size="12">3nm - 5nm DIES</text>
        </g>

        <!-- Node 2: The Bottleneck (Malacca) -->
        <g transform="translate(440, 260)">
          <circle r="44" fill="rgba(230, 57, 70, 0.2)" stroke="#e63946" stroke-width="3" />
          <circle r="12" fill="#e63946" />
          <text x="0" y="70" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">PHILLIPS CHANNEL</text>
          <text x="0" y="92" text-anchor="middle" fill="#ff4d5e" font-size="12">CRITICAL CONVERGENCE</text>
        </g>

        <!-- Node 3: Western Assembly & Auto -->
        <g transform="translate(740, 160)">
          <circle r="36" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="2.5" />
          <circle r="8" fill="#f59e0b" />
          <text x="0" y="60" text-anchor="middle" fill="#ffffff" font-size="15" font-weight="bold">WESTERN ASSEMBLY</text>
          <text x="0" y="80" text-anchor="middle" fill="#f59e0b" font-size="12">EU & US FACTORIES</text>
        </g>

        <!-- Interconnecting High-Energy Laser Beams -->
        <path id="flow-line-1" d="M 176 160 Q 300 180, 396 260" fill="none" stroke="#00f0ff" stroke-width="4" stroke-dasharray="10 8" />
        <path id="flow-line-2" d="M 484 260 Q 600 200, 704 160" fill="none" stroke="#e63946" stroke-width="4" stroke-dasharray="10 8" />

        <g transform="translate(440, 420)">
          <rect x="-180" y="-30" width="360" height="60" rx="8" fill="rgba(230, 57, 70, 0.25)" stroke="#e63946" stroke-width="1.5" />
          <text x="0" y="8" text-anchor="middle" fill="#ffffff" font-size="20" font-weight="bold" font-family="'Archivo Black'">OUTAGE BUFFER: &lt; 72 HRS</text>
        </g>
      </svg>
    </div>

    <!-- CAPTIONS SAFE-ZONE (Bottom > 380px) -->
    <div id="caption-bar">
      <div id="caption-tag" class="caption-tag">TACTICAL ALERT // CHOKEPOINT</div>
      <div id="caption-text" class="caption-headline">COULD YOU LOSE YOUR PHONE IF THIS STRAIT CLOSES?</div>
    </div>

    <!-- BOTTOM TELEMETRY FOOTER -->
    <div class="hud-footer">
      <div>COORD: 01°15'N 103°50'E</div>
      <div>EIA ENERGY SECURITY REPORT // REF. CH-08</div>
    </div>
  </div>

  <script>
    window.__timeline = gsap.timeline({ paused: true });

    // --- THREE.JS 3D GLOBE RIG ---
    let scene3D, camera3D, renderer3D, globeMesh, globeGlow;
    const globeContainer = document.getElementById("three-globe-container");

    function init3DGlobe() {
      scene3D = new THREE.Scene();
      camera3D = new THREE.PerspectiveCamera(40, 1080 / 1920, 0.1, 1000);
      camera3D.position.set(0, 0, 480);

      renderer3D = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer3D.setSize(1080, 1920);
      renderer3D.setPixelRatio(1);
      globeContainer.appendChild(renderer3D.domElement);

      // Dark Tech Globe Sphere
      const sphereGeo = new THREE.SphereGeometry(150, 48, 48);
      const sphereMat = new THREE.MeshBasicMaterial({
        color: 0x071120,
        wireframe: false
      });
      globeMesh = new THREE.Mesh(sphereGeo, sphereMat);
      scene3D.add(globeMesh);

      // Wireframe Graticule Outer Ring
      const wireMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        wireframe: true,
        transparent: true,
        opacity: 0.12
      });
      const wireMesh = new THREE.Mesh(new THREE.SphereGeometry(150.8, 32, 32), wireMat);
      globeMesh.add(wireMesh);

      // Outer Atmosphere Glow
      const glowGeo = new THREE.SphereGeometry(154, 32, 32);
      const glowMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        transparent: true,
        opacity: 0.08,
        side: THREE.BackSide
      });
      globeGlow = new THREE.Mesh(glowGeo, glowMat);
      scene3D.add(globeGlow);

      // Malacca Chokepoint 3D Beacon (Lat 1.25, Lon 103.8)
      const phi = (90 - 1.25) * (Math.PI / 180);
      const theta = (103.8 + 180) * (Math.PI / 180);
      const bx = -(150 * Math.sin(phi) * Math.cos(theta));
      const by = 150 * Math.cos(phi);
      const bz = 150 * Math.sin(phi) * Math.sin(theta);

      const beaconGeo = new THREE.CylinderGeometry(0.5, 3, 24, 8);
      const beaconMat = new THREE.MeshBasicMaterial({ color: 0xe63946 });
      const beacon = new THREE.Mesh(beaconGeo, beaconMat);
      beacon.position.set(bx, by, bz);
      beacon.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), new THREE.Vector3(bx, by, bz).normalize());
      globeMesh.add(beacon);

      // Set initial rotation so Malacca faces camera
      globeMesh.rotation.y = -Math.PI / 1.35;
      globeMesh.rotation.x = 0.25;

      renderer3D.render(scene3D, camera3D);
    }

    // --- AIS PARTICLES RIG ---
    const canvas = document.getElementById("particles-canvas");
    const ctx = canvas.getContext("2d");
    const TOTAL_PARTICLES = 65;
    let particles = [];
    let isChoked = false;
    let screenRoute = [];

    async function init() {
      init3DGlobe();

      const world = window.__WORLD_DATA;
      const countries = topojson.feature(world, world.objects.countries);

      const projection = d3.geoMercator()
        .center([103.5, 1.8])
        .scale(920)
        .translate([540, 960]);

      const path = d3.geoPath().projection(projection);

      const graticule = d3.geoGraticule10();
      d3.select("#graticule-lines").attr("d", path(graticule));

      const landLayer = d3.select("#land-layer");
      landLayer.selectAll("path")
        .data(countries.features)
        .enter()
        .append("path")
        .attr("class", d => {
          if ([360, 458, 702].includes(Number(d.id))) return "focus-land";
          return "land";
        })
        .attr("d", path);

      const tradeCoords = [
        [80.0, 5.0], [90.0, 5.5], [95.0, 5.8], [98.5, 4.0], [101.0, 2.5],
        [103.5, 1.2], [104.5, 1.5], [108.0, 4.0], [115.0, 10.0], [120.0, 15.0]
      ];
      const sundaCoords = [
        [85.0, -3.0], [95.0, -5.0], [105.0, -6.0], [106.0, -5.8],
        [108.0, -3.0], [112.0, 2.0], [118.0, 10.0]
      ];

      d3.select("#traffic-glow").attr("d", path({ type: "LineString", coordinates: tradeCoords }));
      d3.select("#traffic-core").attr("d", path({ type: "LineString", coordinates: tradeCoords }));
      d3.select("#sunda-bypass").attr("d", path({ type: "LineString", coordinates: sundaCoords }));

      screenRoute = tradeCoords.map(coord => projection(coord));

      for (let i = 0; i < TOTAL_PARTICLES; i++) {
        particles.push({
          progress: i / TOTAL_PARTICLES,
          speed: 0.0012 + Math.random() * 0.0006,
          size: 2.5 + Math.random() * 2,
          color: Math.random() > 0.3 ? "#00f0ff" : "#ffdd00"
        });
      }

      const chokePt = projection([103.8, 1.25]);
      const radarG = d3.select("#choke-radar-rings");
      radarG.append("circle")
        .attr("cx", chokePt[0])
        .attr("cy", chokePt[1])
        .attr("r", 18)
        .attr("fill", "none")
        .attr("stroke", "#e63946")
        .attr("stroke-width", "3px");
      radarG.append("circle")
        .attr("cx", chokePt[0])
        .attr("cy", chokePt[1])
        .attr("r", 40)
        .attr("fill", "none")
        .attr("stroke", "#e63946")
        .attr("stroke-width", "1.5px")
        .attr("stroke-dasharray", "4 4");

      buildTimeline();
      drawParticles(0);
    }

    function getPointOnRoute(pts, t) {
      if (!pts || pts.length < 2) return [0, 0];
      const totalSegs = pts.length - 1;
      const idx = Math.min(totalSegs - 1, Math.floor(t * totalSegs));
      const segT = (t * totalSegs) - idx;
      const p1 = pts[idx];
      const p2 = pts[idx + 1];
      return [
        p1[0] + (p2[0] - p1[0]) * segT,
        p1[1] + (p2[1] - p1[1]) * segT
      ];
    }

    function drawParticles(timelineTime) {
      ctx.clearRect(0, 0, 1080, 1920);

      isChoked = (timelineTime >= 6.64 && timelineTime <= 19.26);

      particles.forEach((p, idx) => {
        let currentT = (p.progress + timelineTime * p.speed * 4) % 1.0;

        if (isChoked && currentT > 0.42 && currentT < 0.58) {
          currentT = 0.5 + (Math.sin(idx + timelineTime * 3) * 0.02);
        }

        const pos = getPointOnRoute(screenRoute, currentT);

        ctx.beginPath();
        ctx.arc(pos[0], pos[1], isChoked && currentT >= 0.48 && currentT <= 0.52 ? p.size * 2 : p.size, 0, Math.PI * 2);
        ctx.fillStyle = isChoked && currentT >= 0.48 && currentT <= 0.52 ? "#e63946" : p.color;
        ctx.shadowColor = ctx.fillStyle;
        ctx.shadowBlur = 8;
        ctx.fill();
        ctx.shadowBlur = 0;
      });
    }

    const captionsManifest = [
      { start: 0.0, end: 6.64, tag: "GEO-STRATEGIC RISK", text: "COULD YOU LOSE YOUR PHONE IF THIS STRAIT CLOSES?" },
      { start: 6.64, end: 12.10, tag: "CHOKEPOINT TELEMETRY", text: "PHILLIPS CHANNEL: WORLD'S DENSEST MARITIME BOTTLENECK" },
      { start: 12.10, end: 19.26, tag: "GLOBAL OIL ARTERY", text: "94,000+ VESSELS / YEAR · 60% OF WORLD MARITIME OIL" },
      { start: 19.26, end: 26.51, tag: "SILICON DEPENDENCY", text: "CRITICAL SEMICONDUCTORS TRANSIT THROUGH THIS EXACT CHOKE" },
      { start: 26.51, end: 35.10, tag: "LOGISTIC SHOCK", text: "DETOUR ADDS 3 FULL DAYS & $5 BILLION IN FREIGHT SURCHARGES" },
      { start: 35.10, end: 41.50, tag: "GEOPOLITICAL REALITY", text: "THE GLOBAL ECONOMY ANCHORED TO 1.5 MILES OF WATER" }
    ];

    window.updateCaptionsAtTime = function(t) {
      for (const c of captionsManifest) {
        if (t >= c.start && t < c.end) {
          document.getElementById("caption-tag").innerText = c.tag;
          document.getElementById("caption-text").innerText = c.text;
          break;
        }
      }
      drawParticles(t);
    };

    function render3D(t) {
      if (globeMesh) {
        globeMesh.rotation.y = -Math.PI / 1.35 + (t * 0.08);
      }
      if (renderer3D && scene3D && camera3D) {
        renderer3D.render(scene3D, camera3D);
      }
    }

    function buildTimeline() {
      const tl = window.__timeline;

      // BEAT 1: 0.0s - 6.64s (3D Space Globe -> Dive-in to Phillips Channel)
      tl.set("#three-globe-container", { opacity: 1, scale: 1.0 })
        .set("#map-svg", { opacity: 0 })
        .to(camera3D.position, {
          z: 180,
          duration: 3.2,
          ease: "power3.in",
          onUpdate: () => render3D(tl.time())
        }, 0.2)
        .to("#three-globe-container", {
          opacity: 0,
          scale: 1.8,
          duration: 0.8,
          ease: "power2.in"
        }, 3.0)
        .to("#map-svg", {
          opacity: 1,
          duration: 0.8,
          ease: "power2.out"
        }, 3.2)
        .to("#map-camera", {
          scale: 4.8,
          x: -180,
          y: -120,
          duration: 2.8,
          ease: "power3.out"
        }, 3.2)
        .to("#choke-reticle", { opacity: 1, duration: 0.4 }, 3.6)
        .to("#caliper-badge", { opacity: 1, scale: 1.05, duration: 0.5, ease: "back.out(1.5)" }, 3.8)
        .to(["#choke-reticle", "#caliper-badge"], { opacity: 0, duration: 0.4 }, 6.2);

      // BEAT 2: 6.64s - 12.10s (Bathymetric Cross-Section Vector Engineering)
      tl.addLabel("bathy_beat", 6.64)
        .call(() => window.updateCaptionsAtTime(6.65), null, 6.64)
        .to("#map-svg", { opacity: 0.18, duration: 0.8 }, 6.8)
        .to("#bathy-3d-scene", { opacity: 1, duration: 0.8 }, 6.8)
        .from("#bathy-3d-scene", { scale: 0.95, duration: 0.8, ease: "power2.out" }, 6.8)
        .to("#bathy-3d-scene", { opacity: 0, duration: 0.5 }, 11.8);

      // BEAT 3: 12.10s - 19.26s (Volume Telemetry 94,000 Ships Counter)
      tl.addLabel("telemetry_beat", 12.10)
        .call(() => window.updateCaptionsAtTime(12.15), null, 12.10)
        .to("#map-svg", { opacity: 0.9, duration: 0.6 }, 12.0)
        .to("#map-camera", { scale: 3.2, x: -100, y: -60, duration: 2.0, ease: "power2.out" }, 12.1)
        .to("#telemetry-box", { opacity: 1, x: 0, duration: 0.6, ease: "back.out(1.2)" }, 12.4)
        .to({ val: 0 }, {
          val: 94200,
          duration: 3.5,
          ease: "power2.out",
          onUpdate: function() {
            document.getElementById("counter-ships").innerText = Math.floor(this.targets()[0].val).toLocaleString();
          }
        }, 12.5)
        .to("#telemetry-box", { opacity: 0, x: -30, duration: 0.5 }, 18.5);

      // BEAT 4: 19.26s - 26.51s (3D Supply Chain Network Module)
      tl.addLabel("supply_beat", 19.26)
        .call(() => window.updateCaptionsAtTime(19.3), null, 19.26)
        .to("#map-svg", { opacity: 0.18, duration: 0.6 }, 19.3)
        .to("#supply-3d-scene", { opacity: 1, duration: 0.8 }, 19.3)
        .from("#supply-3d-scene", { scale: 0.95, duration: 0.8, ease: "power2.out" }, 19.3)
        .to("#supply-3d-scene", { opacity: 0, duration: 0.5 }, 25.8);

      // BEAT 5: 26.51s - 35.10s (Bypass Detour Penalty: +3 Days & $5B)
      tl.addLabel("detour_beat", 26.51)
        .call(() => window.updateCaptionsAtTime(26.55), null, 26.51)
        .to("#map-svg", { opacity: 1.0, duration: 0.6 }, 26.2)
        .to("#map-camera", { scale: 1.9, x: -60, y: 130, duration: 3.0, ease: "power2.inOut" }, 26.5)
        .to("#sunda-bypass", { opacity: 1, strokeWidth: 8, duration: 1.5, ease: "power2.out" }, 27.5);

      // BEAT 6: 35.10s - 40.77s (Pullback to 3D Globe Outro)
      tl.addLabel("outro_beat", 35.10)
        .call(() => window.updateCaptionsAtTime(35.15), null, 35.10)
        .to("#map-svg", { opacity: 0, duration: 1.5 }, 35.2)
        .to("#three-globe-container", { opacity: 1, scale: 1.0, duration: 1.5 }, 35.2)
        .fromTo(camera3D.position, { z: 220 }, {
          z: 480,
          duration: 4.5,
          ease: "expo.out",
          onUpdate: () => render3D(tl.time())
        }, 35.2);

      console.log("Timeline generated. Duration:", tl.duration());
      window.__ready = true;
    }

    window.onload = init;
  </script>
</body>
</html>
"""

target_path = os.path.join("learning-videos", "shorts-experiments", "sh-08-malacca-chokepoint", "index.html")
with open(target_path, "w", encoding="utf-8") as f:
    f.write(content.strip())
print("Successfully updated index.html with 3D Globe & Bathymetric Matrix")
