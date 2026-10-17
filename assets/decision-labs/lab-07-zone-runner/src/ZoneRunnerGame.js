import * as THREE from '../../vendor/three.module.js';
import {
  UNCLOS_OBJECTIVES,
  UNCLOS_INCIDENTS,
  UNCLOS_MASTERY_QUESTIONS,
  UNCLOS_TRANSFER_SCENARIO,
  UnclosState
} from './UnclosConfig.js';
import { audioEngine } from '../../shared/core/AudioEngine.js';
import { renderDebrief } from '../../shared/learn/DebriefPanel.js';
import { OnboardingModal } from '../../shared/learn/OnboardingModal.js';

export class ZoneRunnerGame {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.state = new UnclosState();
    this.railCollapsed = false;
    this.initAudioExtensions();
    this.init3D();
    this.bindDOM();
    this.bindKeyboard();
    this.initOnboarding();
    this.triggerSignatureMoment();
    this.render();
  }

  initAudioExtensions() {
    this.playDepthSounding = () => {
      if (audioEngine.muted) return;
      audioEngine.init();
      const ctx = audioEngine.ctx;
      if (!ctx) return;
      const now = ctx.currentTime;

      // Sonar Depth Sounding Ping
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(880, now);
      osc.frequency.exponentialRampToValueAtTime(160, now + 0.65);
      gain.gain.setValueAtTime(0.3, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.7);

      // Resonant harmonic echo
      const echo = ctx.createOscillator();
      const echoGain = ctx.createGain();
      echo.type = 'triangle';
      echo.frequency.setValueAtTime(1320, now + 0.08);
      echo.frequency.exponentialRampToValueAtTime(220, now + 0.75);
      echoGain.gain.setValueAtTime(0.12, now + 0.08);
      echoGain.gain.exponentialRampToValueAtTime(0.001, now + 0.8);

      osc.connect(gain);
      gain.connect(ctx.destination);
      echo.connect(echoGain);
      echoGain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + 0.7);
      echo.start(now + 0.08);
      echo.stop(now + 0.8);
    };
  }

  init3D() {
    const width = this.container.clientWidth || 1024;
    const height = this.container.clientHeight || 520;

    // Scene & Camera
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x020d1a);
    this.scene.fog = new THREE.FogExp2(0x020d1a, 0.008);

    this.camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    this.camera.position.set(0, 52, 75);
    this.camera.lookAt(0, -4, 0);

    // Renderer
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.container.innerHTML = '';
    this.container.appendChild(this.renderer.domElement);

    // Lighting
    const ambient = new THREE.AmbientLight(0xd4eaf7, 0.65);
    this.scene.add(ambient);

    const sunLight = new THREE.DirectionalLight(0x0284c7, 1.4);
    sunLight.position.set(30, 80, 40);
    this.scene.add(sunLight);

    const warmFill = new THREE.DirectionalLight(0xf5e6c8, 0.5);
    warmFill.position.set(-40, 20, -30);
    this.scene.add(warmFill);

    this.buildBathymetricSeafloor();
    this.buildWaterSurface();
    this.buildMaritimeZones();
    this.buildDepthCrossSection();
    this.buildCutterVessel();
    this.buildTargetVessel();

    // Resize Handler
    this.handleResize = () => {
      if (!this.container || !this.renderer || !this.camera) return;
      const w = this.container.clientWidth;
      const h = this.container.clientHeight;
      this.camera.aspect = w / h;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(w, h);
    };
    window.addEventListener('resize', this.handleResize);

    // Animation Loop
    this.clock = new THREE.Clock();
    this.animate = this.animate.bind(this);
    requestAnimationFrame(this.animate);
  }

  buildBathymetricSeafloor() {
    // 3D Bathymetric Seafloor with depth contours and continental slope
    const width = 160;
    const depth = 90;
    const segX = 64;
    const segZ = 36;
    const geo = new THREE.PlaneGeometry(width, depth, segX, segZ);
    geo.rotateX(-Math.PI / 2);

    const pos = geo.attributes.position;
    for (let i = 0; i < pos.count; i++) {
      const x = pos.getX(i);
      const z = pos.getZ(i);

      let y = -4; // baseline depth
      if (x < -50) {
        // Internal waters / shallow coastal shelf
        y = -3 + Math.sin(x * 0.2) * 0.8 + Math.cos(z * 0.15) * 0.5;
      } else if (x < -20) {
        // Territorial Sea (gentle shelf slope)
        const t = (x + 50) / 30;
        y = -4 - t * 4 + Math.sin(z * 0.2) * 0.6;
      } else if (x < 15) {
        // Contiguous Zone to Continental Shelf break
        const t = (x + 20) / 35;
        y = -8 - t * 14 + Math.cos(x * 0.15) * 0.9;
      } else {
        // Continental Rise & Abyssal Plain (deep oceanic basin)
        const t = Math.min(1, (x - 15) / 30);
        y = -22 - t * 4 + Math.sin(x * 0.08) * 0.5 + Math.cos(z * 0.08) * 0.5;
      }
      pos.setY(i, y);
    }
    geo.computeVertexNormals();

    const mat = new THREE.MeshStandardMaterial({
      color: 0x05233d,
      roughness: 0.85,
      metalness: 0.1,
      wireframe: false,
      flatShading: true
    });
    this.seafloor = new THREE.Mesh(geo, mat);
    this.scene.add(this.seafloor);

    // Contour Lines (Isobaths: 50m, 200m shelf break, 1000m, 2500m)
    this.buildIsobathLines();
  }

  buildIsobathLines() {
    const isobathLevels = [
      { y: -4.5, color: 0x38bdf8, label: '50m Isobath' },
      { y: -10.0, color: 0x0284c7, label: '200m Shelf Break' },
      { y: -18.0, color: 0x075985, label: '1000m Continental Slope' },
      { y: -24.5, color: 0x033b5c, label: '2500m Abyssal Plain' }
    ];

    isobathLevels.forEach(iso => {
      const points = [];
      for (let x = -75; x <= 75; x += 3) {
        points.push(new THREE.Vector3(x, iso.y + 0.15, -40));
        points.push(new THREE.Vector3(x, iso.y + 0.15, 40));
      }
      const lineGeo = new THREE.BufferGeometry().setFromPoints(points);
      const lineMat = new THREE.LineBasicMaterial({
        color: iso.color,
        transparent: true,
        opacity: 0.35
      });
      const grid = new THREE.LineSegments(lineGeo, lineMat);
      this.scene.add(grid);
    });
  }

  buildWaterSurface() {
    const geo = new THREE.PlaneGeometry(160, 90, 48, 28);
    geo.rotateX(-Math.PI / 2);
    this.waterGeometry = geo;

    const mat = new THREE.MeshStandardMaterial({
      color: 0x0284c7,
      transparent: true,
      opacity: 0.55,
      roughness: 0.15,
      metalness: 0.25
    });
    this.waterMesh = new THREE.Mesh(geo, mat);
    this.waterMesh.position.y = 0;
    this.scene.add(this.waterMesh);
  }

  buildMaritimeZones() {
    // 6 Visible Zone demarcations with boundary fences & floating markers
    const zones = [
      { id: 'internal', xMin: -80, xMax: -55, label: 'INTERNAL WATERS (Art 8)', color: 0x075985 },
      { id: 'territorial', xMin: -55, xMax: -30, label: 'TERRITORIAL SEA · 12 NM (Art 17)', color: 0x0284c7 },
      { id: 'contiguous', xMin: -30, xMax: -5, label: 'CONTIGUOUS ZONE · 24 NM (Art 33)', color: 0x0e7490 },
      { id: 'eez', xMin: -5, xMax: 35, label: 'EXCLUSIVE ECONOMIC ZONE · 200 NM (Art 56)', color: 0x0369a1 },
      { id: 'shelf', xMin: 35, xMax: 60, label: 'EXTENDED CONTINENTAL SHELF · SEABED (Art 77)', color: 0x92400e },
      { id: 'highseas', xMin: 60, xMax: 80, label: 'HIGH SEAS · GLOBAL COMMONS (Art 87/110)', color: 0x1e3a8a }
    ];

    zones.forEach(z => {
      // Zone boundary divider line
      const linePoints = [
        new THREE.Vector3(z.xMax, -12, -45),
        new THREE.Vector3(z.xMax, 4, -45),
        new THREE.Vector3(z.xMax, 4, 45),
        new THREE.Vector3(z.xMax, -12, 45)
      ];
      const lineGeo = new THREE.BufferGeometry().setFromPoints(linePoints);
      const lineMat = new THREE.LineBasicMaterial({
        color: z.color,
        transparent: true,
        opacity: 0.8
      });
      const boundaryLine = new THREE.Line(lineGeo, lineMat);
      this.scene.add(boundaryLine);

      // Light fence plane
      const fenceGeo = new THREE.PlaneGeometry(0.1, 90);
      const fenceMat = new THREE.MeshBasicMaterial({
        color: z.color,
        transparent: true,
        opacity: 0.15,
        side: THREE.DoubleSide
      });
      const fence = new THREE.Mesh(fenceGeo, fenceMat);
      fence.rotation.y = Math.PI / 2;
      fence.position.set(z.xMax, -2, 0);
      this.scene.add(fence);
    });

    // Signature Moment Grid (Admiralty chart gridlines that unfurl)
    const gridPoints = [];
    for (let x = -75; x <= 75; x += 15) {
      gridPoints.push(new THREE.Vector3(x, 0.2, -42));
      gridPoints.push(new THREE.Vector3(x, 0.2, 42));
    }
    for (let z = -40; z <= 40; z += 10) {
      gridPoints.push(new THREE.Vector3(-75, 0.2, z));
      gridPoints.push(new THREE.Vector3(75, 0.2, z));
    }
    const chartGridGeo = new THREE.BufferGeometry().setFromPoints(gridPoints);
    this.chartGridMat = new THREE.LineBasicMaterial({
      color: 0xf5e6c8,
      transparent: true,
      opacity: 0.05
    });
    this.chartGrid = new THREE.LineSegments(chartGridGeo, this.chartGridMat);
    this.scene.add(this.chartGrid);
  }

  buildDepthCrossSection() {
    // Cross-Section that visually differentiates Water Column (Art 56) from Seabed (Art 77)
    this.crossSectionGroup = new THREE.Group();
    this.crossSectionGroup.position.set(0, -6, 44);

    // Water Column indicator block
    const waterColGeo = new THREE.BoxGeometry(150, 10, 0.5);
    this.waterColMat = new THREE.MeshStandardMaterial({
      color: 0x0284c7,
      transparent: true,
      opacity: 0.35,
      roughness: 0.4
    });
    this.waterColMesh = new THREE.Mesh(waterColGeo, this.waterColMat);
    this.waterColMesh.position.y = -2;
    this.crossSectionGroup.add(this.waterColMesh);

    // Seabed indicator block
    const seabedGeo = new THREE.BoxGeometry(150, 8, 0.5);
    this.seabedMat = new THREE.MeshStandardMaterial({
      color: 0x78350f,
      transparent: true,
      opacity: 0.55,
      roughness: 0.9
    });
    this.seabedMesh = new THREE.Mesh(seabedGeo, this.seabedMat);
    this.seabedMesh.position.y = -11;
    this.crossSectionGroup.add(this.seabedMesh);

    this.scene.add(this.crossSectionGroup);
  }

  buildCutterVessel() {
    this.cutter = new THREE.Group();

    // Hull (detailed wedge)
    const hullShape = new THREE.Shape();
    hullShape.moveTo(0, 0);
    hullShape.lineTo(7, 0);
    hullShape.lineTo(6.5, -2.5);
    hullShape.lineTo(-1.5, -2.5);
    hullShape.lineTo(-2, 0);
    hullShape.closePath();

    const hullExtrude = new THREE.ExtrudeGeometry(hullShape, {
      depth: 3.2,
      bevelEnabled: true,
      bevelSegments: 2,
      steps: 1,
      bevelSize: 0.3,
      bevelThickness: 0.3
    });
    hullExtrude.center();

    const hullMat = new THREE.MeshStandardMaterial({
      color: 0xe4f0fa,
      roughness: 0.4,
      metalness: 0.3
    });
    const hull = new THREE.Mesh(hullExtrude, hullMat);
    this.cutter.add(hull);

    // Coast Guard accent on bow
    const stripeGeo = new THREE.BoxGeometry(1.2, 2.4, 3.4);
    const stripeMat = new THREE.MeshStandardMaterial({ color: 0x0284c7 });
    const stripe = new THREE.Mesh(stripeGeo, stripeMat);
    stripe.position.set(1.5, 0.1, 0);
    this.cutter.add(stripe);

    // Superstructure & Bridge
    const bridgeGeo = new THREE.BoxGeometry(3.5, 2.2, 2.4);
    const bridgeMat = new THREE.MeshStandardMaterial({ color: 0x075985, roughness: 0.3 });
    const bridge = new THREE.Mesh(bridgeGeo, bridgeMat);
    bridge.position.set(-0.8, 1.8, 0);
    this.cutter.add(bridge);

    // Radar Mast & Rotating Scanner
    const mastGeo = new THREE.CylinderGeometry(0.12, 0.18, 3.5);
    const mastMat = new THREE.MeshStandardMaterial({ color: 0x334155 });
    const mast = new THREE.Mesh(mastGeo, mastMat);
    mast.position.set(-0.8, 4.2, 0);
    this.cutter.add(mast);

    const radarBarGeo = new THREE.BoxGeometry(1.8, 0.25, 0.3);
    const radarBarMat = new THREE.MeshStandardMaterial({ color: 0xf5e6c8 });
    this.radarBar = new THREE.Mesh(radarBarGeo, radarBarMat);
    this.radarBar.position.set(-0.8, 5.8, 0);
    this.cutter.add(this.radarBar);

    // Forward Deck Gun (Enforcement Symbol)
    const gunBase = new THREE.CylinderGeometry(0.5, 0.6, 0.6, 8);
    const gunMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
    const turret = new THREE.Mesh(gunBase, gunMat);
    turret.position.set(2.4, 1.0, 0);
    this.cutter.add(turret);

    const barrelGeo = new THREE.CylinderGeometry(0.08, 0.08, 1.8);
    const barrel = new THREE.Mesh(barrelGeo, gunMat);
    barrel.rotation.z = Math.PI / 2.3;
    barrel.position.set(3.1, 1.3, 0);
    this.cutter.add(barrel);

    // Position cutter in Internal Waters initially
    this.cutter.position.set(-65, 0.8, 0);
    this.cutterTargetX = -65;
    this.scene.add(this.cutter);
  }

  buildTargetVessel() {
    this.targetGroup = new THREE.Group();

    // Generic vessel hull
    const hullGeo = new THREE.BoxGeometry(6.5, 2.2, 2.8);
    this.targetHullMat = new THREE.MeshStandardMaterial({ color: 0xb45309 });
    this.targetHull = new THREE.Mesh(hullGeo, this.targetHullMat);
    this.targetGroup.add(this.targetHull);

    // Deck house
    const cabinGeo = new THREE.BoxGeometry(2.2, 2.0, 2.2);
    this.targetCabinMat = new THREE.MeshStandardMaterial({ color: 0x475569 });
    this.targetCabin = new THREE.Mesh(cabinGeo, this.targetCabinMat);
    this.targetCabin.position.set(-1.6, 1.8, 0);
    this.targetGroup.add(this.targetCabin);

    // Intercept coordinate beacon (3D tactical reticle)
    const ringGeo = new THREE.RingGeometry(3.5, 4.2, 32);
    ringGeo.rotateX(-Math.PI / 2);
    this.reticleMat = new THREE.MeshBasicMaterial({
      color: 0x0284c7,
      transparent: true,
      opacity: 0.8,
      side: THREE.DoubleSide
    });
    this.reticle = new THREE.Mesh(ringGeo, this.reticleMat);
    this.reticle.position.y = 0.2;
    this.targetGroup.add(this.reticle);

    this.targetGroup.position.set(-42, 0.8, -5);
    this.scene.add(this.targetGroup);
  }

  triggerSignatureMoment() {
    // Law 2: Signature Moment in first 3 seconds (chart grid unfurl + depth sounding)
    this.playDepthSounding();

    // Chart grid expands and unfurls across bathymetric surface
    let start = performance.now();
    const duration = 2400;

    const unfurlStep = (now) => {
      const elapsed = now - start;
      const progress = Math.min(1, elapsed / duration);
      if (this.chartGridMat) {
        this.chartGridMat.opacity = 0.05 + Math.sin(progress * Math.PI) * 0.45;
      }
      if (this.reticle) {
        this.reticle.scale.setScalar(1 + Math.sin(progress * Math.PI * 2) * 0.2);
      }
      if (progress < 1) {
        requestAnimationFrame(unfurlStep);
      } else if (this.chartGridMat) {
        this.chartGridMat.opacity = 0.2;
      }
    };
    requestAnimationFrame(unfurlStep);
  }

  animate() {
    requestAnimationFrame(this.animate);
    const time = this.clock.getElapsedTime();

    // Rotate radar scanner on cutter
    if (this.radarBar) {
      this.radarBar.rotation.y = time * 4.5;
    }

    // Gentle nautical bobbing
    if (this.cutter) {
      this.cutter.position.y = 0.8 + Math.sin(time * 2.2) * 0.25;
      this.cutter.rotation.z = Math.sin(time * 1.8) * 0.04;
      this.cutter.rotation.x = Math.cos(time * 1.5) * 0.03;

      // Smooth navigation towards target coordinate
      if (Math.abs(this.cutter.position.x - this.cutterTargetX) > 0.1) {
        this.cutter.position.x += (this.cutterTargetX - this.cutter.position.x) * 0.05;
      }
    }

    // Target vessel animation & reticle pulse
    if (this.targetGroup) {
      this.targetGroup.position.y = 0.8 + Math.cos(time * 2.0) * 0.2;
      if (this.reticle) {
        this.reticle.rotation.y = time * 0.8;
      }
    }

    // Undulating water surface vertices
    if (this.waterGeometry) {
      const pos = this.waterGeometry.attributes.position;
      for (let i = 0; i < pos.count; i++) {
        const u = pos.getX(i);
        const v = pos.getZ(i);
        const wave = Math.sin(u * 0.12 + time * 2.0) * 0.35 + Math.cos(v * 0.15 + time * 1.6) * 0.25;
        pos.setY(i, wave);
      }
      this.waterGeometry.computeVertexNormals();
      this.waterGeometry.attributes.position.needsUpdate = true;
    }

    this.renderer.render(this.scene, this.camera);
  }

  update3DIncident(inc) {
    if (!inc) return;

    // Reposition target vessel to incident coordinates
    const coords = inc.targetCoords || { x: 0, z: 0 };
    this.targetGroup.position.set(coords.x, 0.8, coords.z);
    this.cutterTargetX = coords.x - 10;

    // Differentiate vessel visual by domain / type
    if (inc.domain === 'seabed') {
      this.targetHullMat.color.setHex(0xb45309);
      this.targetCabinMat.color.setHex(0xf5e6c8);
      // Highlight Seabed cross-section (Art 77)
      this.seabedMat.opacity = 0.85;
      this.waterColMat.opacity = 0.15;
    } else {
      this.targetHullMat.color.setHex(0x0284c7);
      this.targetCabinMat.color.setHex(0x06182c);
      // Highlight Water Column cross-section (Art 56)
      this.waterColMat.opacity = 0.65;
      this.seabedMat.opacity = 0.3;
    }
  }

  bindDOM() {
    const btnMute = document.getElementById('btnAudioMute');
    if (btnMute) {
      btnMute.onclick = () => {
        const isMuted = audioEngine.toggleMute();
        btnMute.innerText = isMuted ? 'UNMUTE AUDIO' : 'MUTE AUDIO';
        audioEngine.playMechanicalClick();
      };
    }

    const btnRestart = document.getElementById('btnRestart');
    if (btnRestart) {
      btnRestart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.restartGame();
      };
    }

    const btnToggleRail = document.getElementById('btnToggleRail');
    if (btnToggleRail) {
      btnToggleRail.onclick = () => {
        this.toggleRail();
      };
    }
  }

  initOnboarding() {
    this.onboarding = new OnboardingModal({
      labId: 'lab-07',
      role: 'Coastal Patrol Commander · Cutter Warden-07',
      objective: 'Navigate graduated UNCLOS 1982 maritime regimes and execute lawful interdiction verbs (Seize, Board, Permit Transit) without infringing high-seas freedoms.',
      steps: [
        {
          step: '1',
          title: 'HYPOTHESIZE & PREDICT',
          desc: 'Commit to an analytical expectation before inspecting vessels. Test your understanding of maritime legal regimes.'
        },
        {
          step: '2',
          title: 'EXECUTE INTERDICTION VERB',
          desc: 'Evaluate nautical coordinates and vessel behavior: Seize [1], Board [2], or Permit Transit [3].'
        },
        {
          step: '3',
          title: 'AUDIT & MASTER UNCLOS',
          desc: 'Inspect legal consequences under UNCLOS Articles (8, 17, 33, 56, 77, 110), correct misconceptions, and solve a transfer case.'
        }
      ],
      controls: [
        { key: '1, 2, 3', label: 'Verbs (Seize, Board, Permit Transit)' },
        { key: 'SPACE / ENTER', label: 'Advance' },
        { key: 'TAB', label: 'Toggle operational side rail' },
        { key: 'M', label: 'Toggle audio synthesizer' }
      ],
      onStart: () => {
        this.triggerSignatureMoment();
      }
    });

    const btnHowToPlay = document.getElementById('btnHowToPlay');
    if (btnHowToPlay) {
      btnHowToPlay.onclick = () => {
        audioEngine.playMechanicalClick();
        this.onboarding.open();
      };
    }

    this.onboarding.open();
  }

  bindKeyboard() {
    window.addEventListener('keydown', (e) => {
      if (this.onboarding && this.onboarding.isOpen) return;
      // Avoid firing when user is typing in form controls
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

      if (e.key === 'm' || e.key === 'M') {
        const btnMute = document.getElementById('btnAudioMute');
        if (btnMute) btnMute.click();
        return;
      }
      if (e.key === 'r' || e.key === 'R') {
        const btnRestart = document.getElementById('btnRestart');
        if (btnRestart) btnRestart.click();
        return;
      }

      // Phase-specific number choices (1, 2, 3)
      if (this.state.phase === 'PREDICT') {
        if (e.key === '1') this.handlePredictionSelect('A');
        if (e.key === '2') this.handlePredictionSelect('B');
        if (e.key === '3') this.handlePredictionSelect('C');
      } else if (this.state.phase === 'DECIDE') {
        if (e.key === '1') this.handleDecisionAction('SEIZE_ARREST');
        if (e.key === '2') this.handleDecisionAction('BOARD_VERIFY');
        if (e.key === '3') this.handleDecisionAction('PERMIT_TRANSIT');
      } else if (this.state.phase === 'CONSEQUENCE') {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          this.handleAdvanceIncident();
        }
      } else if (this.state.phase === 'MASTERY') {
        if (e.key === '1') this.handleMasterySelect('A');
        if (e.key === '2') this.handleMasterySelect('B');
        if (e.key === '3') this.handleMasterySelect('C');
      } else if (this.state.phase === 'TRANSFER') {
        if (e.key === '1') this.handleTransferSelect('A');
        if (e.key === '2') this.handleTransferSelect('B');
        if (e.key === '3') this.handleTransferSelect('C');
      }
    });
  }

  toggleRail() {
    this.railCollapsed = !this.railCollapsed;
    const rail = document.getElementById('decisionRail');
    const btn = document.getElementById('btnToggleRail');
    if (rail) {
      if (this.railCollapsed) {
        rail.classList.add('collapsed');
        if (btn) btn.innerText = 'EXPAND RAIL';
      } else {
        rail.classList.remove('collapsed');
        if (btn) btn.innerText = 'COLLAPSE RAIL';
      }
    }
    setTimeout(() => this.handleResize(), 200);
  }

  restartGame() {
    this.state.reset();
    this.cutterTargetX = -65;
    if (this.cutter) this.cutter.position.x = -65;
    this.render();
  }

  render() {
    this.updateHUD();
    const railContent = document.getElementById('railScrollArea');
    if (!railContent) return;

    switch (this.state.phase) {
      case 'BRIEF':
        this.renderBriefing(railContent);
        break;
      case 'PREDICT':
        this.renderPrediction(railContent);
        break;
      case 'DECIDE':
        this.renderDecision(railContent);
        break;
      case 'CONSEQUENCE':
        this.renderConsequence(railContent);
        break;
      case 'MASTERY':
        this.renderMastery(railContent);
        break;
      case 'TRANSFER':
        this.renderTransfer(railContent);
        break;
      case 'DEBRIEF':
        this.renderDebrief(railContent);
        break;
    }
  }

  updateHUD() {
    const elIncident = document.getElementById('hudIncidentNum');
    const elZone = document.getElementById('hudZoneName');
    const elScore = document.getElementById('hudScore');
    const elTokens = document.getElementById('hudTokens');

    const inc = this.state.getCurrentIncident();
    if (elIncident) {
      elIncident.innerText = inc ? `INCIDENT ${this.state.incidentIndex + 1} / 10` : 'DEBRIEFING';
    }
    if (elZone) {
      elZone.innerText = inc ? `${inc.zoneName.toUpperCase()} (${inc.limit})` : 'COMPREHENSIVE AUDIT';
    }
    if (elScore) {
      elScore.innerText = `${this.state.score} PTS`;
    }
    if (elTokens) {
      elTokens.innerText = `${this.state.tokens} / 3 TOKENS`;
    }

    if (inc) {
      this.update3DIncident(inc);
    }
  }

  renderBriefing(container) {
    container.innerHTML = `
      <div class="card briefing-card" role="region" aria-label="Mission Briefing">
        <div class="card-badge">ADMIRALTY TACTICAL INSTRUCTION · UNCLOS 1982</div>
        <h2 class="card-heading">MARITIME ZONE INTERDICTION PATROL</h2>
        <p class="card-desc">
          Assume operational command of Coastal Patrol Cutter <em>Warden-07</em>.
          Sovereignty is not uniform across ocean space. As your vessel crosses seaward from internal waters to the high seas, legal authority transforms from absolute territorial sovereignty to functional sovereign rights and high-seas freedoms.
        </p>
        <div class="objectives-box">
          <div class="box-title">ASSESSED LEARNING OBJECTIVES:</div>
          <ol class="objectives-list">
            ${UNCLOS_OBJECTIVES.map(obj => `<li>${obj}</li>`).join('')}
          </ol>
        </div>
        <div class="briefing-rules">
          <p><strong>ENFORCEMENT VERBS:</strong> For each incident, select <code>SEIZE/ARREST</code>, <code>BOARD FOR VERIFICATION</code>, or <code>PERMIT TRANSIT</code>. Incorrect jurisdictional actions deplete patrol integrity tokens.</p>
        </div>
        <button id="btnStartBriefing" class="action-btn btn-primary" type="button">
          START PATROL DEPLOYMENT
        </button>
      </div>
    `;

    const btnStart = document.getElementById('btnStartBriefing');
    if (btnStart) {
      btnStart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.playDepthSounding();
        this.state.phase = 'PREDICT';
        this.render();
      };
    }
  }

  renderPrediction(container) {
    const inc = this.state.getCurrentIncident();
    if (!inc) return;

    container.innerHTML = `
      <div class="card prediction-card" role="region" aria-label="Prediction Hypothesis">
        <div class="card-badge">PHASE 1: HYPOTHESIS FORMATION</div>
        <h2 class="card-heading">PREDICT JURISDICTIONAL REGIME</h2>
        <div class="tactical-dossier">
          <div class="dossier-row"><span>TARGET:</span> <strong>${inc.vesselName} (${inc.vesselType})</strong></div>
          <div class="dossier-row"><span>POSITION:</span> <strong>${inc.location}</strong></div>
          <div class="dossier-row"><span>BATHYMETRY:</span> <strong>${inc.depth}m Depth (${inc.domain.toUpperCase()} DOMAIN)</strong></div>
        </div>
        <p class="scenario-summary">${inc.scenario}</p>
        <div class="prediction-prompt">
          <label><strong>HYPOTHESIS COMMITMENT:</strong> ${inc.predictionPrompt}</label>
        </div>
        <div class="options-stack">
          ${inc.predictionOptions.map(opt => `
            <button class="option-btn" type="button" data-key="${opt.key}">
              <span class="key-tag">[KEY ${opt.key}]</span>
              <span class="opt-text">${opt.text}</span>
            </button>
          `).join('')}
        </div>
      </div>
    `;

    container.querySelectorAll('.option-btn').forEach(btn => {
      btn.onclick = () => {
        const key = btn.getAttribute('data-key');
        this.handlePredictionSelect(key);
      };
    });
  }

  handlePredictionSelect(key) {
    audioEngine.playMechanicalClick();
    this.state.recordPrediction(key);
    this.render();
  }

  renderDecision(container) {
    const inc = this.state.getCurrentIncident();
    if (!inc) return;

    container.innerHTML = `
      <div class="card decision-card" role="region" aria-label="Operational Interdiction Decision">
        <div class="card-badge">PHASE 2: OPERATIONAL INTERDICTION</div>
        <h2 class="card-heading">${inc.zoneName.toUpperCase()} · ${inc.limit}</h2>
        <div class="tactical-dossier">
          <div class="dossier-row"><span>VESSEL:</span> <strong>${inc.vesselName} (${inc.vesselType})</strong></div>
          <div class="dossier-row"><span>COORDINATES:</span> <strong>${inc.location}</strong></div>
          <div class="dossier-row"><span>PREDICTION:</span> <strong>Option ${this.state.currentPrediction} Registered</strong></div>
        </div>
        <p class="scenario-text">${inc.scenario}</p>
        <div class="verb-prompt">
          <strong>${inc.question}</strong>
        </div>
        <div class="verbs-grid">
          <button class="verb-btn verb-seize" type="button" data-verb="SEIZE_ARREST">
            <span class="verb-key">[1]</span>
            <span class="verb-title">SEIZE / ARREST</span>
            <span class="verb-sub">Assert plenary custody or judicial arrest</span>
          </button>
          <button class="verb-btn verb-board" type="button" data-verb="BOARD_VERIFY">
            <span class="verb-key">[2]</span>
            <span class="verb-title">BOARD FOR VERIFICATION</span>
            <span class="verb-sub">Audit documents / sanitary inspection / Right of Visit</span>
          </button>
          <button class="verb-btn verb-transit" type="button" data-verb="PERMIT_TRANSIT">
            <span class="verb-key">[3]</span>
            <span class="verb-title">PERMIT TRANSIT</span>
            <span class="verb-sub">Honor innocent passage or high seas freedom</span>
          </button>
        </div>
      </div>
    `;

    container.querySelectorAll('.verb-btn').forEach(btn => {
      btn.onclick = () => {
        const verb = btn.getAttribute('data-verb');
        this.handleDecisionAction(verb);
      };
    });
  }

  handleDecisionAction(verb) {
    audioEngine.playMechanicalClick();
    const result = this.state.executeDecision(verb);

    if (result.isCorrect) {
      audioEngine.playChimeCooperation();
    } else {
      audioEngine.playBetrayalBoom();
    }

    this.render();
  }

  renderConsequence(container) {
    const inc = this.state.getCurrentIncident();
    const fb = this.state.currentFeedback;
    if (!inc || !fb) return;

    const isSuccess = fb.outcome === 'success';

    container.innerHTML = `
      <div class="card consequence-card ${isSuccess ? 'card-success' : 'card-failure'}" role="region" aria-label="Incident Consequence and Legal Explanation">
        <div class="feedback-header">
          <span class="badge ${isSuccess ? 'badge-success' : 'badge-failure'}">
            ${isSuccess ? 'LEGAL VERIFICATION CONFIRMED' : 'JURISDICTIONAL BREACH'}
          </span>
          <span class="hypothesis-match">
            ${fb.predictionMatch ? 'HYPOTHESIS CONFIRMED' : 'HYPOTHESIS DISPROVEN'}
          </span>
        </div>

        <div class="feedback-block">
          <div class="block-label">CAUSAL CONSEQUENCE:</div>
          <p class="block-content">${fb.consequence}</p>
        </div>

        <div class="feedback-block">
          <div class="block-label">LEGAL MECHANISM:</div>
          <p class="block-content">${fb.mechanism}</p>
        </div>

        <div class="feedback-block citation-block">
          <div class="block-label">TREATY CITATION:</div>
          <p class="citation-text"><strong>${fb.citation}</strong></p>
        </div>

        ${fb.misconception ? `
          <div class="misconception-box">
            <div class="misc-tag">[MISCONCEPTION RECTIFIED: ${fb.misconception.label}]</div>
            <p class="misc-remediation">${fb.misconception.remediation}</p>
          </div>
        ` : ''}

        <button id="btnAdvanceIncident" class="action-btn btn-primary" type="button">
          CONTINUE TO NEXT INCIDENT [SPACE / ENTER]
        </button>
      </div>
    `;

    const btnNext = document.getElementById('btnAdvanceIncident');
    if (btnNext) {
      btnNext.onclick = () => {
        this.handleAdvanceIncident();
      };
    }
  }

  handleAdvanceIncident() {
    audioEngine.playMechanicalClick();
    this.playDepthSounding();
    this.state.advanceIncident();
    this.render();
  }

  renderMastery(container) {
    const q = this.state.getCurrentMasteryQuestion();
    if (!q) return;

    container.innerHTML = `
      <div class="card mastery-card" role="region" aria-label="Mastery Check Concept Evaluation">
        <div class="card-badge">PHASE 6: MASTERY CHECK CONCEPT QUESTION ${this.state.masteryIndex + 1} / 3</div>
        <h2 class="card-heading">THEORETICAL MECHANICS EVALUATION</h2>
        <p class="mastery-prompt">${q.prompt}</p>
        <div class="options-stack">
          ${q.options.map(opt => `
            <button class="option-btn mastery-opt" type="button" data-key="${opt.key}">
              <span class="key-tag">[KEY ${opt.key}]</span>
              <span class="opt-text">${opt.text}</span>
            </button>
          `).join('')}
        </div>
        <div id="masteryFeedback" class="feedback-inline" style="display:none;"></div>
      </div>
    `;

    container.querySelectorAll('.mastery-opt').forEach(btn => {
      btn.onclick = () => {
        const key = btn.getAttribute('data-key');
        this.handleMasterySelect(key);
      };
    });
  }

  handleMasterySelect(key) {
    audioEngine.playMechanicalClick();
    const res = this.state.answerMasteryQuestion(key);
    const box = document.getElementById('masteryFeedback');

    if (box) {
      box.style.display = 'block';
      box.innerHTML = `
        <div class="mini-feedback ${res.isCorrect ? 'mini-success' : 'mini-failure'}">
          <strong>${res.isCorrect ? 'CORRECT EVALUATION' : 'CONCEPTUAL REMEDIATION'}:</strong>
          ${res.rationale} <br><em>${res.citation}</em>
        </div>
      `;
    }

    if (res.isCorrect) audioEngine.playChimeCooperation();
    else audioEngine.playAlarmKlaxon();

    setTimeout(() => {
      this.render();
    }, 2200);
  }

  renderTransfer(container) {
    const t = UNCLOS_TRANSFER_SCENARIO;

    container.innerHTML = `
      <div class="card transfer-card" role="region" aria-label="Transfer Scenario Case Evaluation">
        <div class="card-badge">PHASE 7: DIVERGENT CASE APPLICATION</div>
        <h2 class="card-heading">${t.title.toUpperCase()}</h2>
        <p class="transfer-prompt">${t.prompt}</p>
        <div class="options-stack">
          ${t.options.map(opt => `
            <button class="option-btn transfer-opt" type="button" data-key="${opt.key}">
              <span class="key-tag">[KEY ${opt.key}]</span>
              <span class="opt-text">${opt.text}</span>
            </button>
          `).join('')}
        </div>
        <div id="transferFeedback" class="feedback-inline" style="display:none;"></div>
      </div>
    `;

    container.querySelectorAll('.transfer-opt').forEach(btn => {
      btn.onclick = () => {
        const key = btn.getAttribute('data-key');
        this.handleTransferSelect(key);
      };
    });
  }

  handleTransferSelect(key) {
    audioEngine.playMechanicalClick();
    const res = this.state.answerTransfer(key);
    const box = document.getElementById('transferFeedback');

    if (box) {
      box.style.display = 'block';
      box.innerHTML = `
        <div class="mini-feedback ${res.isCorrect ? 'mini-success' : 'mini-failure'}">
          <strong>${res.isCorrect ? 'TRANSFER DEMONSTRATED' : 'TRANSFER REMEDIATION'}:</strong>
          ${res.rationale} <br><em>${res.citation}</em>
        </div>
      `;
    }

    if (res.isCorrect) audioEngine.playChimeCooperation();
    else audioEngine.playAlarmKlaxon();

    setTimeout(() => {
      this.render();
    }, 2600);
  }

  renderDebrief(container) {
    const report = this.state.getReport();
    container.innerHTML = `
      <div id="debriefMount"></div>
      <div class="debrief-actions">
        <button id="btnDebriefRestart" class="action-btn btn-primary" type="button">
          RESTART DECISION LAB RUN
        </button>
      </div>
    `;

    renderDebrief('#debriefMount', report);

    const btnRestart = document.getElementById('btnDebriefRestart');
    if (btnRestart) {
      btnRestart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.restartGame();
      };
    }
  }
}

