import os

content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SH-08 Malacca Chokepoint - Living 3D Globe & Dynamic Tactical Map</title>
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
      background: #060912;
      color: #fff;
      font-family: 'Space Mono', monospace;
    }

    #stage {
      position: relative;
      width: 1080px;
      height: 1920px;
      background: #060912;
      overflow: hidden;
    }

    /* TOP INTEL HUD BAR */
    .intel-header {
      position: absolute;
      top: 60px;
      left: 60px;
      right: 60px;
      height: 70px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(6, 9, 18, 0.88);
      border: 1px solid rgba(0, 240, 255, 0.3);
      border-radius: 8px;
      padding: 0 24px;
      z-index: 100;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
    }
    .intel-title {
      font-size: 20px;
      letter-spacing: 2px;
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
      background: rgba(230, 57, 70, 0.2);
      border: 1.5px solid #e63946;
      color: #ff4d5e;
      padding: 6px 16px;
      font-size: 16px;
      letter-spacing: 2px;
      border-radius: 4px;
      font-weight: bold;
    }

    /* 3D WEBGL GLOBE CANVAS (ORTHOGRAPHIC PERSPECTIVE) */
    #three-globe-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 1080px;
      height: 1920px;
      z-index: 10;
      opacity: 0;
      pointer-events: none;
    }

    /* PRIMARY 2D VECTOR GEOPOLITICAL MAP */
    #map-svg {
      position: absolute;
      top: 0;
      left: 0;
      width: 1080px;
      height: 1920px;
      z-index: 15;
    }

    .ocean { fill: #060912; }
    .land { fill: #141c2e; stroke: #1e293b; stroke-width: 1.5px; }
    .focus-malaysia { fill: #1a2942; stroke: #38bdf8; stroke-width: 2.2px; }
    .focus-indonesia { fill: #1e2638; stroke: #2a3d58; stroke-width: 2.0px; }
    .focus-singapore { fill: #e63946; stroke: #ff4d5e; stroke-width: 3.0px; }
    .graticule { fill: none; stroke: rgba(148, 163, 184, 0.08); stroke-width: 0.8px; }

    /* HIGH-CONTRAST MARITIME LANES */
    .traffic-lane-glow {
      fill: none;
      stroke: rgba(0, 240, 255, 0.4);
      stroke-width: 10px;
      stroke-linecap: round;
      filter: drop-shadow(0 0 12px rgba(0, 240, 255, 0.7));
    }
    .traffic-core {
      fill: none;
      stroke: #00f0ff;
      stroke-width: 3px;
      stroke-dasharray: 8 8;
    }
    .bypass-lane {
      fill: none;
      stroke: #f59e0b;
      stroke-width: 5px;
      stroke-dasharray: 8 6;
      opacity: 0;
      filter: drop-shadow(0 0 10px rgba(245, 158, 11, 0.6));
    }

    /* PARTICLES CANVAS (Moving AIS Ships) */
    #particles-canvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 1080px;
      height: 1920px;
      z-index: 25;
      pointer-events: none;
    }

    /* GEOGRAPHIC LABELS (HIGH VISIBILITY) */
    .geo-label {
      font-family: 'Archivo Black', sans-serif;
      text-anchor: middle;
      fill: #ffffff;
      paint-order: stroke;
      stroke: #060912;
      stroke-width: 4px;
      stroke-linejoin: round;
      pointer-events: none;
    }
    .geo-label-sub {
      font-family: 'Space Mono', monospace;
      font-size: 14px;
      fill: #94a3b8;
      text-anchor: middle;
      paint-order: stroke;
      stroke: #060912;
      stroke-width: 3px;
    }

    /* CHOKEPOINT RETICLE & CALIPER BADGE */
    #choke-reticle {
      position: absolute;
      top: 920px;
      left: 540px;
      transform: translate(-50%, -50%);
      width: 260px;
      height: 260px;
      border: 1.5px dashed rgba(230, 57, 70, 0.8);
      border-radius: 50%;
      pointer-events: none;
      opacity: 0;
      z-index: 40;
    }
    .reticle-corner {
      position: absolute;
      width: 28px;
      height: 28px;
      border: 3px solid #e63946;
    }
    .rc-tl { top: -2px; left: -2px; border-right: none; border-bottom: none; }
    .rc-tr { top: -2px; right: -2px; border-left: none; border-bottom: none; }
    .rc-bl { bottom: -2px; left: -2px; border-right: none; border-top: none; }
    .rc-br { bottom: -2px; right: -2px; border-left: none; border-top: none; }

    #caliper-badge {
      position: absolute;
      top: 740px;
      left: 540px;
      transform: translate(-50%, -50%);
      background: rgba(230, 57, 70, 0.96);
      border: 2px solid #ff4d5e;
      color: #ffffff;
      padding: 12px 28px;
      border-radius: 8px;
      font-size: 22px;
      font-weight: bold;
      letter-spacing: 2px;
      box-shadow: 0 0 30px rgba(230, 57, 70, 0.8);
      opacity: 0;
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* TELEMETRY OVERLAY CARD */
    #telemetry-box {
      position: absolute;
      top: 170px;
      left: 60px;
      background: rgba(6, 11, 24, 0.94);
      border: 1.5px solid rgba(0, 240, 255, 0.4);
      border-left: 6px solid #00f0ff;
      border-radius: 8px;
      padding: 24px 32px;
      backdrop-filter: blur(14px);
      z-index: 90;
      opacity: 0;
      transform: translateX(-40px);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.9);
    }
    .tel-metric {
      font-size: 14px;
      color: #94a3b8;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }
    .tel-counter {
      font-family: 'Archivo Black', sans-serif;
      font-size: 46px;
      color: #ffffff;
      line-height: 1.1;
    }
    .tel-counter span { color: #00f0ff; }

    /* FLOATING INSET CARD: BATHYMETRIC PROFILE (TOP RIGHT, NON-BLOCKING) */
    #bathymetry-inset {
      position: absolute;
      top: 260px;
      right: 60px;
      width: 480px;
      height: 380px;
      background: rgba(6, 11, 24, 0.94);
      border: 1.5px solid rgba(0, 240, 255, 0.4);
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.95);
      backdrop-filter: blur(14px);
      z-index: 80;
      opacity: 0;
      pointer-events: none;
    }
    .inset-header {
      font-size: 13px;
      letter-spacing: 1.5px;
      color: #00f0ff;
      font-weight: bold;
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
      padding-bottom: 8px;
      margin-bottom: 14px;
      display: flex;
      justify-content: space-between;
    }

    /* FLOATING INSET CARD: SUPPLY CHAIN FLOW (TOP RIGHT, NON-BLOCKING) */
    #supply-chain-inset {
      position: absolute;
      top: 260px;
      right: 60px;
      width: 480px;
      height: 380px;
      background: rgba(6, 11, 24, 0.94);
      border: 1.5px solid rgba(0, 240, 255, 0.4);
      border-radius: 12px;
      padding: 20px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.95);
      backdrop-filter: blur(14px);
      z-index: 85;
      opacity: 0;
      pointer-events: none;
    }

    /* SAFE ZONE CAPTION OVERLAY (Bottom > 380px) */
    #caption-bar {
      position: absolute;
      bottom: 420px;
      left: 60px;
      right: 60px;
      background: rgba(6, 9, 18, 0.95);
      border: 2px solid rgba(0, 240, 255, 0.4);
      border-radius: 14px;
      padding: 26px 36px;
      backdrop-filter: blur(20px);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95);
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
        <span>GEOPOLITICAL MAPPING // MALACCA STRAIT</span>
      </div>
      <div class="intel-badge">CHOKEPOINT: CRITICAL</div>
    </div>

    <!-- 3D THREE.JS GLOBE CONTAINER (FOR OUTRO PANORAMA) -->
    <div id="three-globe-container"></div>

    <!-- PRIMARY 2D VECTOR MAP -->
    <svg id="map-svg" viewBox="0 0 1080 1920">
      <g id="map-camera">
        <path id="ocean-bg" class="ocean" d=""></path>
        <path id="graticule-lines" class="graticule" d=""></path>
        <g id="land-layer"></g>
        
        <!-- HIGH-TECH LANES -->
        <path id="traffic-glow" class="traffic-lane-glow" d=""></path>
        <path id="traffic-core" class="traffic-core" d=""></path>
        <path id="sunda-bypass" class="bypass-lane" d=""></path>
        
        <!-- GEOGRAPHIC LABELS -->
        <g id="geo-labels">
          <text class="geo-label" x="420" y="740" font-size="28">MALAYSIA</text>
          <text class="geo-label" x="320" y="1120" font-size="34">SUMATRA (INDONESIA)</text>
          <text class="geo-label" x="720" y="930" font-size="22" fill="#ff4d5e">SINGAPORE</text>
          <text class="geo-label-sub" x="480" y="860">STRAIT OF MALACCA</text>
        </g>

        <!-- DYNAMIC AIS RADAR RINGS -->
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
      <span style="color: #ffdd00;">CHOKEPOINT:</span> 1.5 NAUTICAL MILES (2.8 KM)
    </div>

    <!-- TELEMETRY BOX -->
    <div id="telemetry-box">
      <div class="tel-metric">ANNUAL TRANSIT VOLUME</div>
      <div class="tel-counter"><span id="counter-ships">0</span> VESSELS</div>
      <div style="font-size: 14px; color: #94a3b8; margin-top: 4px;">60% OF WORLD MARITIME CRUDE OIL</div>
    </div>

    <!-- FLOATING INSET 1: BATHYMETRIC PROFILE (TOP RIGHT) -->
    <div id="bathymetry-inset">
      <div class="inset-header">
        <span>BATHYMETRIC PROFILE // PHILLIPS CHANNEL</span>
        <span style="color: #e63946;">DRAFT CLEARANCE</span>
      </div>
      <svg viewBox="0 0 440 280" style="width: 100%; height: 280px;">
        <!-- Sea Level -->
        <line x1="20" y1="40" x2="420" y2="40" stroke="#00f0ff" stroke-width="2" stroke-dasharray="6 4" />
        <text x="25" y="32" fill="#00f0ff" font-size="11" font-family="'Space Mono'">SEA LEVEL 0.0M</text>

        <!-- Shallow Reef Ridge -->
        <path d="M 20 220 Q 140 210, 220 170 T 320 155 T 420 220 L 420 270 L 20 270 Z" fill="#141c2e" stroke="#e63946" stroke-width="2" />
        <text x="25" y="255" fill="#e63946" font-size="11" font-family="'Space Mono'">REEF SEABED (DEPTH: 23M)</text>

        <!-- 3D Tanker Hull -->
        <g transform="translate(180, 39)">
          <path d="M 0 0 L 130 0 L 125 105 L 15 105 Z" fill="#1e293b" stroke="#64748b" stroke-width="1.5" />
          <path d="M 130 0 L 148 -14 L 143 90 L 125 105 Z" fill="#131b26" stroke="#475569" stroke-width="1" />
          <path d="M 0 0 L 18 -14 L 148 -14 L 130 0 Z" fill="#334155" stroke="#64748b" stroke-width="1" />
          <rect x="15" y="105" width="110" height="5" fill="#e63946" />
          <text x="20" y="55" fill="#ffffff" font-size="11" font-weight="bold" font-family="'Archivo Black'">VLCC SUPERTANKER</text>
          <text x="20" y="72" fill="#94a3b8" font-size="9" font-family="'Space Mono'">DRAFT: 20.5 METERS</text>
        </g>

        <!-- Caliper Clearance -->
        <g transform="translate(315, 142)">
          <line x1="0" y1="0" x2="0" y2="18" stroke="#ffdd00" stroke-width="2.5" />
          <line x1="-8" y1="0" x2="8" y2="0" stroke="#ffdd00" stroke-width="2" />
          <line x1="-8" y1="18" x2="8" y2="18" stroke="#ffdd00" stroke-width="2" />
          <text x="14" y="12" fill="#ffdd00" font-size="11" font-weight="bold" font-family="'Space Mono'">CLEARANCE: 2.8M</text>
          <text x="14" y="26" fill="#e63946" font-size="9" font-family="'Space Mono'">GROUNDING RISK</text>
        </g>
      </svg>
    </div>

    <!-- FLOATING INSET 2: SILICON SUPPLY CHAIN (TOP RIGHT) -->
    <div id="supply-chain-inset">
      <div class="inset-header">
        <span>SILICON ARTERY FLOW // CASCADE TEST</span>
        <span style="color: #ffdd00;">RISK: HIGH</span>
      </div>
      <svg viewBox="0 0 440 280" style="width: 100%; height: 280px;">
        <!-- TSMC Node -->
        <g transform="translate(70, 90)">
          <circle r="22" fill="rgba(0, 240, 255, 0.2)" stroke="#00f0ff" stroke-width="2" />
          <circle r="6" fill="#00f0ff" />
          <text x="0" y="38" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">TSMC TAIWAN</text>
        </g>
        <!-- Malacca Choke Node -->
        <g transform="translate(220, 150)">
          <circle r="26" fill="rgba(230, 57, 70, 0.25)" stroke="#e63946" stroke-width="2.5" />
          <circle r="8" fill="#e63946" />
          <text x="0" y="44" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">MALACCA CHOKE</text>
        </g>
        <!-- Western Assembly Node -->
        <g transform="translate(370, 90)">
          <circle r="22" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2" />
          <circle r="6" fill="#f59e0b" />
          <text x="0" y="38" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">WESTERN PLANTS</text>
        </g>

        <!-- Connectors -->
        <path d="M 92 90 Q 150 100, 194 150" fill="none" stroke="#00f0ff" stroke-width="3" stroke-dasharray="6 4" />
        <path d="M 246 150 Q 290 100, 348 90" fill="none" stroke="#e63946" stroke-width="3" stroke-dasharray="6 4" />

        <!-- Loss Metric Box -->
        <g transform="translate(220, 240)">
          <rect x="-130" y="-18" width="260" height="36" rx="6" fill="rgba(230, 57, 70, 0.25)" stroke="#e63946" stroke-width="1.2" />
          <text x="0" y="5" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold" font-family="'Archivo Black'">FACTORY BUFFER: &lt; 72 HRS</text>
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

    // --- THREE.JS 3D GLOBE RIG (FOR OUTRO PANORAMA) ---
    let scene3D, camera3D, renderer3D, globeMesh;
    const globeContainer = document.getElementById("three-globe-container");

    function init3DGlobe() {
      scene3D = new THREE.Scene();
      camera3D = new THREE.PerspectiveCamera(40, 1080 / 1920, 0.1, 1000);
      camera3D.position.set(0, 0, 480);

      renderer3D = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      renderer3D.setSize(1080, 1920);
      renderer3D.setPixelRatio(1);
      globeContainer.appendChild(renderer3D.domElement);

      const sphereGeo = new THREE.SphereGeometry(150, 48, 48);
      const sphereMat = new THREE.MeshBasicMaterial({ color: 0x071120 });
      globeMesh = new THREE.Mesh(sphereGeo, sphereMat);
      scene3D.add(globeMesh);

      const wireMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        wireframe: true,
        transparent: true,
        opacity: 0.15
      });
      const wireMesh = new THREE.Mesh(new THREE.SphereGeometry(150.8, 32, 32), wireMat);
      globeMesh.add(wireMesh);

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

      // Map Center on Strait of Malacca / Singapore: [102.0, 2.5]
      const projection = d3.geoMercator()
        .center([102.5, 2.8])
        .scale(1450)
        .translate([540, 960]);

      const path = d3.geoPath().projection(projection);

      // Graticule
      const graticule = d3.geoGraticule10();
      d3.select("#graticule-lines").attr("d", path(graticule));

      // Landmass with Clear Country Differentiation
      const landLayer = d3.select("#land-layer");
      landLayer.selectAll("path")
        .data(countries.features)
        .enter()
        .append("path")
        .attr("class", d => {
          const id = Number(d.id);
          if (id === 458) return "focus-malaysia";
          if (id === 360) return "focus-indonesia";
          if (id === 702) return "focus-singapore";
          return "land";
        })
        .attr("d", path);

      // Trade Routes
      const tradeCoords = [
        [88.0, 5.5], [95.0, 5.8], [98.5, 4.0], [100.5, 3.0],
        [102.5, 2.0], [103.8, 1.25], [104.8, 1.6], [107.0, 3.5], [112.0, 7.0]
      ];
      const sundaCoords = [
        [90.0, -2.0], [98.0, -4.5], [104.0, -5.8], [106.0, -5.8],
        [108.5, -3.5], [112.0, 0.5], [116.0, 5.0]
      ];

      d3.select("#traffic-glow").attr("d", path({ type: "LineString", coordinates: tradeCoords }));
      d3.select("#traffic-core").attr("d", path({ type: "LineString", coordinates: tradeCoords }));
      d3.select("#sunda-bypass").attr("d", path({ type: "LineString", coordinates: sundaCoords }));

      screenRoute = tradeCoords.map(coord => projection(coord));

      for (let i = 0; i < TOTAL_PARTICLES; i++) {
        particles.push({
          progress: i / TOTAL_PARTICLES,
          speed: 0.0014 + Math.random() * 0.0006,
          size: 3.0 + Math.random() * 2,
          color: Math.random() > 0.25 ? "#00f0ff" : "#ffdd00"
        });
      }

      // Chokepoint Radar at Phillips Channel [103.8, 1.25]
      const chokePt = projection([103.8, 1.25]);
      const radarG = d3.select("#choke-radar-rings");
      radarG.append("circle")
        .attr("cx", chokePt[0])
        .attr("cy", chokePt[1])
        .attr("r", 20)
        .attr("fill", "none")
        .attr("stroke", "#e63946")
        .attr("stroke-width", "3.5px");
      radarG.append("circle")
        .attr("cx", chokePt[0])
        .attr("cy", chokePt[1])
        .attr("r", 48)
        .attr("fill", "none")
        .attr("stroke", "#e63946")
        .attr("stroke-width", "2px")
        .attr("stroke-dasharray", "5 5");

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
        ctx.shadowBlur = 10;
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
        globeMesh.rotation.y = -Math.PI / 1.35 + (t * 0.1);
      }
      if (renderer3D && scene3D && camera3D) {
        renderer3D.render(scene3D, camera3D);
      }
    }

    function buildTimeline() {
      const tl = window.__timeline;

      // BEAT 1: 0.0s - 6.64s (Clear Geopolitical Vector Map Zoom to Phillips Channel)
      tl.set("#map-svg", { opacity: 1 })
        .set("#map-camera", { transformOrigin: "540px 960px", scale: 1.0, x: 0, y: 0 })
        .to("#map-camera", {
          scale: 3.4,
          x: -160,
          y: -100,
          duration: 4.8,
          ease: "power3.inOut"
        }, 0.4)
        .to("#choke-reticle", { opacity: 1, duration: 0.4 }, 3.0)
        .to("#caliper-badge", { opacity: 1, scale: 1.05, duration: 0.5, ease: "back.out(1.5)" }, 3.2)
        .to(["#choke-reticle", "#caliper-badge"], { opacity: 0, duration: 0.4 }, 6.2);

      // BEAT 2: 6.64s - 12.10s (Floating Inset 1: Bathymetric Profile)
      tl.addLabel("bathy_beat", 6.64)
        .call(() => window.updateCaptionsAtTime(6.65), null, 6.64)
        .to("#bathymetry-inset", { opacity: 1, duration: 0.6 }, 6.8)
        .from("#bathymetry-inset", { scale: 0.9, duration: 0.6, ease: "power2.out" }, 6.8)
        .to("#bathymetry-inset", { opacity: 0, duration: 0.5 }, 11.8);

      // BEAT 3: 12.10s - 19.26s (Volume Telemetry 94,000 Ships Counter on Living Map)
      tl.addLabel("telemetry_beat", 12.10)
        .call(() => window.updateCaptionsAtTime(12.15), null, 12.10)
        .to("#map-camera", { scale: 2.4, x: -80, y: -40, duration: 2.0, ease: "power2.out" }, 12.1)
        .to("#telemetry-box", { opacity: 1, x: 0, duration: 0.6, ease: "back.out(1.2)" }, 12.4)
        .to({ val: 0 }, {
          val: 94200,
          duration: 3.5,
          ease: "power2.out",
          onUpdate: function() {
            document.getElementById("counter-ships").innerText = Math.floor(this.targets()[0].val).toLocaleString();
          }
        }, 12.5)
        .to("#telemetry-box", { opacity: 0, x: -40, duration: 0.5 }, 18.5);

      // BEAT 4: 19.26s - 26.51s (Floating Inset 2: Silicon Supply Chain Network)
      tl.addLabel("supply_beat", 19.26)
        .call(() => window.updateCaptionsAtTime(19.3), null, 19.26)
        .to("#supply-chain-inset", { opacity: 1, duration: 0.6 }, 19.3)
        .from("#supply-chain-inset", { scale: 0.9, duration: 0.6, ease: "power2.out" }, 19.3)
        .to("#supply-chain-inset", { opacity: 0, duration: 0.5 }, 25.8);

      // BEAT 5: 26.51s - 35.10s (Bypass Detour Penalty: Sunda Strait +3 Days & $5B)
      tl.addLabel("detour_beat", 26.51)
        .call(() => window.updateCaptionsAtTime(26.55), null, 26.51)
        .to("#map-camera", { scale: 1.4, x: -40, y: 160, duration: 3.0, ease: "power2.inOut" }, 26.5)
        .to("#sunda-bypass", { opacity: 1, strokeWidth: 7, duration: 1.5, ease: "power2.out" }, 27.5);

      // BEAT 6: 35.10s - 40.77s (Pullback to 3D Globe Outro)
      tl.addLabel("outro_beat", 35.10)
        .call(() => window.updateCaptionsAtTime(35.15), null, 35.10)
        .to("#map-svg", { opacity: 0.2, duration: 1.5 }, 35.2)
        .to("#three-globe-container", { opacity: 1, duration: 1.5 }, 35.2)
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
print("Successfully updated index.html with Living Geopolitical Map Priority")
