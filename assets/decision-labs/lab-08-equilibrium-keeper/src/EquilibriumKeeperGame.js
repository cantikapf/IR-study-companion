import * as THREE from '../../vendor/three.module.js';
import {
  BOP_OBJECTIVES,
  BOP_CRISES,
  BOP_MASTERY_QUESTIONS,
  BOP_TRANSFER_SCENARIO,
  BopState
} from './BopConfig.js';
import { audioEngine } from '../../shared/core/AudioEngine.js';
import { renderDebrief } from '../../shared/learn/DebriefPanel.js';
import { OnboardingModal } from '../../shared/learn/OnboardingModal.js';

export class EquilibriumKeeperGame {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.state = new BopState();
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
    this.playWaxSealAndGears = () => {
      if (audioEngine.muted) return;
      audioEngine.init();
      const ctx = audioEngine.ctx;
      if (!ctx) return;
      const now = ctx.currentTime;

      // Heavy wax seal mechanical thump
      const thump = ctx.createOscillator();
      const thumpGain = ctx.createGain();
      thump.type = 'triangle';
      thump.frequency.setValueAtTime(140, now);
      thump.frequency.exponentialRampToValueAtTime(28, now + 0.35);
      thumpGain.gain.setValueAtTime(0.45, now);
      thumpGain.gain.exponentialRampToValueAtTime(0.001, now + 0.38);

      thump.connect(thumpGain);
      thumpGain.connect(ctx.destination);
      thump.start(now);
      thump.stop(now + 0.38);

      // Brass Orrery Ratchet Clicks (3 successive mechanical teeth ticks)
      [0.08, 0.16, 0.24].forEach((offset, idx) => {
        const tick = ctx.createOscillator();
        const tickGain = ctx.createGain();
        tick.type = 'sawtooth';
        tick.frequency.setValueAtTime(900 + idx * 250, now + offset);
        tick.frequency.exponentialRampToValueAtTime(120, now + offset + 0.04);
        tickGain.gain.setValueAtTime(0.18, now + offset);
        tickGain.gain.exponentialRampToValueAtTime(0.001, now + offset + 0.04);

        tick.connect(tickGain);
        tickGain.connect(ctx.destination);
        tick.start(now + offset);
        tick.stop(now + offset + 0.04);
      });
    };
  }

  init3D() {
    const width = this.container.clientWidth || 1024;
    const height = this.container.clientHeight || 520;

    // Scene & Camera
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x080604);
    this.scene.fog = new THREE.FogExp2(0x080604, 0.009);

    this.camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    this.camera.position.set(0, 48, 62);
    this.camera.lookAt(0, 2, -2);

    // Renderer
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.container.innerHTML = '';
    this.container.appendChild(this.renderer.domElement);

    // Lighting (Edwardian archive warm tungsten / sepia / oxblood tones)
    const ambient = new THREE.AmbientLight(0xf7efe3, 0.65);
    this.scene.add(ambient);

    const goldKey = new THREE.DirectionalLight(0xd97706, 1.4);
    goldKey.position.set(35, 60, 25);
    this.scene.add(goldKey);

    const oxbloodRim = new THREE.DirectionalLight(0x7f1d1d, 0.85);
    oxbloodRim.position.set(-35, 20, -35);
    this.scene.add(oxbloodRim);

    this.buildEuropeTerrain();
    this.buildCapitals();
    this.buildAllianceArcs();
    this.buildMobilisationVectors();
    this.buildBrassOrrery();
    this.buildWaxSealSignature();

    // Resize
    this.handleResize = () => {
      if (!this.container || !this.renderer || !this.camera) return;
      const w = this.container.clientWidth;
      const h = this.container.clientHeight;
      this.camera.aspect = w / h;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(w, h);
    };
    window.addEventListener('resize', this.handleResize);

    this.clock = new THREE.Clock();
    this.animate = this.animate.bind(this);
    requestAnimationFrame(this.animate);
  }

  buildEuropeTerrain() {
    // 3D European relief map plate with elevated mountain ranges (Alps, Carpathians, Pyrenees)
    const width = 110;
    const depth = 75;
    const segX = 54;
    const segZ = 36;
    const geo = new THREE.PlaneGeometry(width, depth, segX, segZ);
    geo.rotateX(-Math.PI / 2);

    const pos = geo.attributes.position;
    for (let i = 0; i < pos.count; i++) {
      const x = pos.getX(i);
      const z = pos.getZ(i);

      let y = 0;
      // Alps (Central Europe: x in [-12, 12], z in [-4, 6])
      const distAlps = Math.hypot(x - 2, z - 2);
      if (distAlps < 16) {
        y += Math.cos((distAlps / 16) * Math.PI) * 5.2;
      }

      // Carpathians (East-Central: x in [16, 32], z in [4, 18])
      const distCarp = Math.hypot(x - 22, z - 10);
      if (distCarp < 14) {
        y += Math.cos((distCarp / 14) * Math.PI) * 4.2;
      }

      // Pyrenees (South-West: x in [-38, -24], z in [-18, -10])
      const distPyr = Math.hypot(x + 30, z + 14);
      if (distPyr < 12) {
        y += Math.cos((distPyr / 12) * Math.PI) * 3.6;
      }

      // British Channel depression (Water bodies: z in [10, 20], x in [-40, -20])
      const distChan = Math.hypot(x + 28, z - 10);
      if (distChan < 10) {
        y -= 1.8;
      }

      pos.setY(i, y);
    }
    geo.computeVertexNormals();

    const mat = new THREE.MeshStandardMaterial({
      color: 0x1c140d,
      roughness: 0.8,
      metalness: 0.15,
      flatShading: true
    });
    this.terrainMesh = new THREE.Mesh(geo, mat);
    this.scene.add(this.terrainMesh);

    // Map Border & Parchment Margin
    const baseBox = new THREE.BoxGeometry(114, 3, 79);
    const borderMat = new THREE.MeshStandardMaterial({
      color: 0x78350f,
      roughness: 0.7,
      metalness: 0.3
    });
    const baseBorder = new THREE.Mesh(baseBox, borderMat);
    baseBorder.position.y = -1.6;
    this.scene.add(baseBorder);
  }

  buildCapitals() {
    this.capitals = {
      london: { name: 'London', pos: new THREE.Vector3(-32, 2.5, 12), color: 0x3b82f6 },
      paris: { name: 'Paris', pos: new THREE.Vector3(-22, 2.5, 2), color: 0x2563eb },
      berlin: { name: 'Berlin', pos: new THREE.Vector3(-2, 2.5, 12), color: 0xd97706 },
      vienna: { name: 'Vienna', pos: new THREE.Vector3(10, 2.5, 2), color: 0xb45309 },
      st_petersburg: { name: 'St. Petersburg', pos: new THREE.Vector3(30, 2.5, 24), color: 0x1d4ed8 },
      belgrade: { name: 'Belgrade', pos: new THREE.Vector3(16, 2.5, -12), color: 0xef4444 },
      brussels: { name: 'Brussels', pos: new THREE.Vector3(-18, 2.5, 7), color: 0xf59e0b }
    };

    this.capitalMeshes = {};

    Object.entries(this.capitals).forEach(([key, cap]) => {
      const group = new THREE.Group();
      group.position.copy(cap.pos);

      // Brass base pedestal
      const pedGeo = new THREE.CylinderGeometry(1.6, 2.0, 1.2, 12);
      const pedMat = new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.3, metalness: 0.6 });
      const ped = new THREE.Mesh(pedGeo, pedMat);
      group.add(ped);

      // Architectural spire / obelisk
      const spireGeo = new THREE.ConeGeometry(1.0, 3.8, 8);
      const spireMat = new THREE.MeshStandardMaterial({ color: cap.color, roughness: 0.4 });
      const spire = new THREE.Mesh(spireGeo, spireMat);
      spire.position.y = 2.4;
      group.add(spire);

      // Glowing status ring
      const ringGeo = new THREE.RingGeometry(2.2, 2.7, 24);
      ringGeo.rotateX(-Math.PI / 2);
      const ringMat = new THREE.MeshBasicMaterial({
        color: cap.color,
        transparent: true,
        opacity: 0.7,
        side: THREE.DoubleSide
      });
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.position.y = 0.1;
      group.add(ring);

      this.scene.add(group);
      this.capitalMeshes[key] = { group, ring, ringMat, spireMat };
    });
  }

  buildAllianceArcs() {
    this.arcCurves = [
      { id: 'dual_alliance', from: 'berlin', to: 'vienna', height: 9, color: 0xd97706, label: 'Dual Alliance (1879)' },
      { id: 'franco_russian', from: 'paris', to: 'st_petersburg', height: 16, color: 0x3b82f6, label: 'Franco-Russian Alliance (1894)' },
      { id: 'entente_cordiale', from: 'london', to: 'paris', height: 7, color: 0x60a5fa, label: 'Entente Cordiale (1904)' },
      { id: 'balkan_crisis', from: 'vienna', to: 'belgrade', height: 6, color: 0xef4444, label: 'Austro-Serbian Confrontation' },
      { id: 'slavic_pledge', from: 'st_petersburg', to: 'belgrade', height: 14, color: 0x93c5fd, label: 'Russian Slavic Commitment' }
    ];

    this.arcMeshes = [];

    this.arcCurves.forEach(arc => {
      const p1 = this.capitals[arc.from].pos;
      const p2 = this.capitals[arc.to].pos;
      const mid = new THREE.Vector3().addVectors(p1, p2).multiplyScalar(0.5);
      mid.y += arc.height;

      const curve = new THREE.QuadraticBezierCurve3(p1, mid, p2);
      const tubeGeo = new THREE.TubeGeometry(curve, 32, 0.45, 8, false);
      const tubeMat = new THREE.MeshStandardMaterial({
        color: arc.color,
        emissive: arc.color,
        emissiveIntensity: 0.35,
        roughness: 0.3,
        metalness: 0.5,
        transparent: true,
        opacity: 0.85
      });
      const mesh = new THREE.Mesh(tubeGeo, tubeMat);
      this.scene.add(mesh);
      this.arcMeshes.push({ id: arc.id, mesh, tubeMat, curve, height: arc.height, baseColor: arc.color });
    });
  }

  buildMobilisationVectors() {
    this.vectorsGroup = new THREE.Group();

    // 1. Schlieffen Corridor (Berlin -> Belgium -> Paris)
    const schlieffenPoints = [
      new THREE.Vector3(-2, 3, 12),
      new THREE.Vector3(-14, 3, 8),
      new THREE.Vector3(-18, 3, 6),
      new THREE.Vector3(-22, 3, 2)
    ];
    this.schlieffenLine = this.createPulsingVector(schlieffenPoints, 0xd97706);
    this.vectorsGroup.add(this.schlieffenLine);

    // 2. Russian Mobilisation Vector (St. Petersburg -> Frontier)
    const russiaPoints = [
      new THREE.Vector3(30, 3, 24),
      new THREE.Vector3(18, 3, 18),
      new THREE.Vector3(6, 3, 14)
    ];
    this.russiaLine = this.createPulsingVector(russiaPoints, 0x3b82f6);
    this.vectorsGroup.add(this.russiaLine);

    // 3. Austrian Assault Vector (Vienna -> Belgrade)
    const austriaPoints = [
      new THREE.Vector3(10, 3, 2),
      new THREE.Vector3(13, 3, -6),
      new THREE.Vector3(16, 3, -12)
    ];
    this.austriaLine = this.createPulsingVector(austriaPoints, 0xef4444);
    this.vectorsGroup.add(this.austriaLine);

    this.scene.add(this.vectorsGroup);
  }

  createPulsingVector(points, colorHex) {
    const geo = new THREE.BufferGeometry().setFromPoints(points);
    const mat = new THREE.LineBasicMaterial({
      color: colorHex,
      linewidth: 3,
      transparent: true,
      opacity: 0.4
    });
    return new THREE.Line(geo, mat);
  }

  buildBrassOrrery() {
    this.orreryGroup = new THREE.Group();
    this.orreryGroup.position.set(0, 24, -18);

    // Central Brass Axle Pillar
    const axleGeo = new THREE.CylinderGeometry(0.8, 1.2, 16, 16);
    const brassMat = new THREE.MeshStandardMaterial({
      color: 0xd97706,
      roughness: 0.25,
      metalness: 0.75
    });
    const axle = new THREE.Mesh(axleGeo, brassMat);
    this.orreryGroup.add(axle);

    // Interlocking Gear Cogs
    this.gear1 = this.createCog(4.5, 0.4, 16, 0xd97706);
    this.gear1.position.y = 4;
    this.orreryGroup.add(this.gear1);

    this.gear2 = this.createCog(3.0, 0.35, 12, 0x78350f);
    this.gear2.position.set(3.2, 4, 0);
    this.orreryGroup.add(this.gear2);

    // Balancing Crossbeam
    this.balanceBeam = new THREE.Group();
    this.balanceBeam.position.y = 7;
    const beamGeo = new THREE.BoxGeometry(34, 0.8, 1.2);
    const beam = new THREE.Mesh(beamGeo, brassMat);
    this.balanceBeam.add(beam);

    // Left Counterweight Sphere (Triple Entente)
    const sphereL = new THREE.SphereGeometry(2.2, 16, 16);
    const matL = new THREE.MeshStandardMaterial({ color: 0x3b82f6, metalness: 0.5, roughness: 0.3 });
    this.orbEntente = new THREE.Mesh(sphereL, matL);
    this.orbEntente.position.set(-16, -3, 0);
    this.balanceBeam.add(this.orbEntente);

    // Right Counterweight Sphere (Central Powers)
    const sphereR = new THREE.SphereGeometry(2.2, 16, 16);
    const matR = new THREE.MeshStandardMaterial({ color: 0xd97706, metalness: 0.5, roughness: 0.3 });
    this.orbCentral = new THREE.Mesh(sphereR, matR);
    this.orbCentral.position.set(16, -3, 0);
    this.balanceBeam.add(this.orbCentral);

    this.orreryGroup.add(this.balanceBeam);
    this.scene.add(this.orreryGroup);
  }

  createCog(radius, thickness, teethCount, colorHex) {
    const group = new THREE.Group();
    const diskGeo = new THREE.CylinderGeometry(radius, radius, thickness, 32);
    const mat = new THREE.MeshStandardMaterial({
      color: colorHex,
      roughness: 0.3,
      metalness: 0.7
    });
    const disk = new THREE.Mesh(diskGeo, mat);
    group.add(disk);

    for (let i = 0; i < teethCount; i++) {
      const angle = (i / teethCount) * Math.PI * 2;
      const toothGeo = new THREE.BoxGeometry(radius * 0.25, thickness, radius * 0.15);
      const tooth = new THREE.Mesh(toothGeo, mat);
      tooth.position.set(Math.cos(angle) * (radius + 0.1), 0, Math.sin(angle) * (radius + 0.1));
      tooth.rotation.y = -angle;
      group.add(tooth);
    }
    return group;
  }

  buildWaxSealSignature() {
    // Signature Moment Law: Imperial Wax Seal emblem on parchment
    this.waxSealGroup = new THREE.Group();
    this.waxSealGroup.position.set(38, 12, -22);

    const sealDisk = new THREE.CylinderGeometry(3.6, 3.8, 0.7, 24);
    const waxMat = new THREE.MeshStandardMaterial({
      color: 0x7f1d1d,
      roughness: 0.45,
      metalness: 0.2
    });
    const seal = new THREE.Mesh(sealDisk, waxMat);
    this.waxSealGroup.add(seal);

    const heraldicCrest = new THREE.CylinderGeometry(2.2, 2.2, 0.9, 8);
    const crestMat = new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.3, metalness: 0.6 });
    const crest = new THREE.Mesh(heraldicCrest, crestMat);
    this.waxSealGroup.add(crest);

    this.scene.add(this.waxSealGroup);
  }

  triggerSignatureMoment() {
    // Law 2: Signature Moment in first 3 seconds (wax seal press + orrery gear turn)
    this.playWaxSealAndGears();

    let start = performance.now();
    const duration = 2200;

    const signatureStep = (now) => {
      const elapsed = now - start;
      const progress = Math.min(1, elapsed / duration);

      // Wax seal presses down onto parchment
      if (this.waxSealGroup) {
        this.waxSealGroup.position.y = 12 - Math.sin(progress * Math.PI * 0.5) * 8.5;
        this.waxSealGroup.rotation.y = progress * Math.PI * 0.5;
      }

      // Orrery gears rotate and balance beam aligns
      if (this.gear1) this.gear1.rotation.y = progress * Math.PI * 2;
      if (this.gear2) this.gear2.rotation.y = -progress * Math.PI * 3;
      if (this.balanceBeam) this.balanceBeam.rotation.z = Math.sin(progress * Math.PI) * 0.15;

      if (progress < 1) {
        requestAnimationFrame(signatureStep);
      }
    };
    requestAnimationFrame(signatureStep);
  }

  animate() {
    requestAnimationFrame(this.animate);
    const time = this.clock.getElapsedTime();

    // Constant gear turning
    if (this.gear1) this.gear1.rotation.y += 0.01;
    if (this.gear2) this.gear2.rotation.y -= 0.015;

    // Beam tilt tracks system tension
    if (this.balanceBeam) {
      // In equilibrium: gentle oscillation; in high tension / chain-ganging: severe tilt
      const tensionFactor = (this.state.systemTension - 25) / 60;
      const targetTilt = tensionFactor * 0.45;
      this.balanceBeam.rotation.z += (targetTilt - this.balanceBeam.rotation.z) * 0.06;
    }

    // Alliance Arcs dynamic pulse and thickness based on chain-ganging
    this.arcMeshes.forEach(arc => {
      if (arc.tubeMat) {
        const pulse = 0.35 + Math.sin(time * 3 + arc.height) * 0.25;
        arc.tubeMat.emissiveIntensity = pulse * (1 + this.state.chainGangingCount * 0.4);
      }
    });

    // Mobilisation vectors pulsing
    if (this.schlieffenLine) {
      this.schlieffenLine.material.opacity = 0.3 + Math.sin(time * 4) * 0.35;
    }
    if (this.russiaLine) {
      this.russiaLine.material.opacity = 0.3 + Math.cos(time * 3.5) * 0.35;
    }

    // Capital city status pulse
    Object.values(this.capitalMeshes).forEach(mesh => {
      if (mesh.ring) {
        mesh.ring.rotation.z = time * 0.8;
      }
    });

    this.renderer.render(this.scene, this.camera);
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
      labId: 'lab-08',
      role: 'Foreign Office Permanent Under-Secretary · July 1914',
      objective: 'Absorb sequential Great Power alliance shocks on the European balance of power without triggering chain-ganging or total systemic collapse.',
      steps: [
        {
          step: '1',
          title: 'HYPOTHESIZE & PREDICT',
          desc: 'Forecast how great power alliances and military mobilizations will shift systemic balance of power dynamics.'
        },
        {
          step: '2',
          title: 'MANAGE ALLIANCE COMMITMENTS',
          desc: 'Execute strategic diplomatic maneuvers: Commit [1], Withhold [2], or Mediate [3] to prevent catastrophic chain-ganging.'
        },
        {
          step: '3',
          title: 'AUDIT & MASTER BALANCE OF POWER',
          desc: 'Analyze multipolar consequences, correct structural realism misconceptions, and resolve historical transfer dilemmas.'
        }
      ],
      controls: [
        { key: '1, 2, 3', label: 'Alignment (Commit, Withhold, Mediate)' },
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

      if (this.state.phase === 'PREDICT') {
        if (e.key === '1') this.handlePredictionSelect('A');
        if (e.key === '2') this.handlePredictionSelect('B');
        if (e.key === '3') this.handlePredictionSelect('C');
      } else if (this.state.phase === 'DECIDE') {
        if (e.key === '1') this.handleDecisionAction('COMMIT');
        if (e.key === '2') this.handleDecisionAction('WITHHOLD');
        if (e.key === '3') this.handleDecisionAction('MEDIATE');
      } else if (this.state.phase === 'CONSEQUENCE') {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          this.handleAdvanceCrisis();
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
    this.triggerSignatureMoment();
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
    const elCrisis = document.getElementById('hudCrisisNum');
    const elTension = document.getElementById('hudSystemTension');
    const elChain = document.getElementById('hudChainGanging');
    const elScore = document.getElementById('hudScore');

    const c = this.state.getCurrentCrisis();
    if (elCrisis) {
      elCrisis.innerText = c ? `CRISIS ${this.state.crisisIndex + 1} / 5` : 'SYSTEM COLLAPSE / AUDIT';
    }
    if (elTension) {
      elTension.innerText = `${this.state.systemTension}% TENSION`;
      if (this.state.systemTension >= 70) {
        elTension.style.color = 'var(--accent-2)';
      } else {
        elTension.style.color = 'var(--accent)';
      }
    }
    if (elChain) {
      elChain.innerText = `CHAIN-GANG: ${this.state.chainGangingCount} · BUCK-PASS: ${this.state.buckPassingCount}`;
    }
    if (elScore) {
      elScore.innerText = `${this.state.score} PTS`;
    }
  }

  renderBriefing(container) {
    container.innerHTML = `
      <div class="card briefing-card" role="region" aria-label="Imperial Diplomatic Instruction">
        <div class="card-badge">EDWARDIAN FOREIGN OFFICE ARCHIVE · JULY 1914</div>
        <h2 class="card-heading">EQUILIBRIUM KEEPER: BALANCE OF POWER</h2>
        <p class="card-desc">
          You direct the foreign policy of a Great Power during the 1914 July Crisis.
          In a multipolar system under anarchy, alliances can provide collective security or become deadly traps. Unconditional commitments create <strong>chain-ganging</strong> where reckless allies drag you to war. Conversely, shirking responsibility creates <strong>buck-passing</strong>, enabling hegemonic overreach.
        </p>
        <div class="objectives-box">
          <div class="box-title">ASSESSED LEARNING OBJECTIVES:</div>
          <ol class="objectives-list">
            ${BOP_OBJECTIVES.map(obj => `<li>${obj}</li>`).join('')}
          </ol>
        </div>
        <div class="briefing-rules">
          <p><strong>ALIGNMENT VERB:</strong> For each crisis, choose to <code>COMMIT</code> (tight alliance solidarity), <code>WITHHOLD</code> (buck-pass deterrence), or <code>MEDIATE</code> (conditional restraint & balance). Prevent systemic tension from exceeding 85%.</p>
        </div>
        <button id="btnStartBriefing" class="action-btn btn-primary" type="button">
          OPEN CRISIS DISPATCH
        </button>
      </div>
    `;

    const btnStart = document.getElementById('btnStartBriefing');
    if (btnStart) {
      btnStart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.playWaxSealAndGears();
        this.state.phase = 'PREDICT';
        this.render();
      };
    }
  }

  renderPrediction(container) {
    const c = this.state.getCurrentCrisis();
    if (!c) return;

    container.innerHTML = `
      <div class="card prediction-card" role="region" aria-label="Analytical Hypothesis Formation">
        <div class="card-badge">PHASE 1: SYSTEMIC HYPOTHESIS</div>
        <h2 class="card-heading">${c.title.toUpperCase()}</h2>
        <div class="tactical-dossier">
          <div class="dossier-row"><span>POWERS INVOLVED:</span> <strong>${c.powers}</strong></div>
          <div class="dossier-row"><span>FLASHPOINT:</span> <strong>${c.flashpoint}</strong></div>
          <div class="dossier-row"><span>CURRENT SYSTEM TENSION:</span> <strong>${this.state.systemTension}%</strong></div>
        </div>
        <p class="scenario-summary">${c.context}</p>
        <div class="prediction-prompt">
          <label><strong>PREDICT SYSTEMIC IMPACT:</strong> ${c.predictionPrompt}</label>
        </div>
        <div class="options-stack">
          ${c.predictionOptions.map(opt => `
            <button class="option-btn" type="button" data-key="${opt.key}">
              <span class="key-tag">[OPTION ${opt.key}]</span>
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
    const c = this.state.getCurrentCrisis();
    if (!c) return;

    container.innerHTML = `
      <div class="card decision-card" role="region" aria-label="Alliance Alignment Decision">
        <div class="card-badge">PHASE 2: ALLIANCE ALIGNMENT (VERB: ALIGN)</div>
        <h2 class="card-heading">${c.title.toUpperCase()}</h2>
        <div class="tactical-dossier">
          <div class="dossier-row"><span>DIPLOMATIC CABLE:</span> <strong>${c.powers}</strong></div>
          <div class="dossier-row"><span>REGISTERED HYPOTHESIS:</span> <strong>Option ${this.state.currentPrediction}</strong></div>
        </div>
        <p class="scenario-text">${c.context}</p>
        <div class="verb-prompt">
          <strong>${c.question}</strong>
        </div>
        <div class="verbs-grid">
          ${c.choices.map((ch, idx) => `
            <button class="verb-btn verb-align-${ch.action.toLowerCase()}" type="button" data-action="${ch.action}">
              <span class="verb-key">[${idx + 1}] ALIGN: ${ch.action}</span>
              <span class="verb-title">${ch.title}</span>
              <span class="verb-sub">${ch.sub}</span>
            </button>
          `).join('')}
        </div>
      </div>
    `;

    container.querySelectorAll('.verb-btn').forEach(btn => {
      btn.onclick = () => {
        const action = btn.getAttribute('data-action');
        this.handleDecisionAction(action);
      };
    });
  }

  handleDecisionAction(action) {
    audioEngine.playMechanicalClick();
    const result = this.state.executeDecision(action);

    if (result.isCorrect) {
      audioEngine.playChimeCooperation();
    } else {
      audioEngine.playBetrayalBoom();
    }

    this.render();
  }

  renderConsequence(container) {
    const c = this.state.getCurrentCrisis();
    const fb = this.state.currentFeedback;
    if (!c || !fb) return;

    const isSuccess = fb.outcome === 'success';

    container.innerHTML = `
      <div class="card consequence-card ${isSuccess ? 'card-success' : 'card-failure'}" role="region" aria-label="Crisis Consequence and Academic Rationale">
        <div class="feedback-header">
          <span class="badge ${isSuccess ? 'badge-success' : 'badge-failure'}">
            ${isSuccess ? 'EQUILIBRIUM PRESERVED' : (this.state.collapse ? 'SYSTEMIC COLLAPSE' : 'CRISIS ESCALATION')}
          </span>
          <span class="hypothesis-match">
            ${fb.predictionMatch ? 'HYPOTHESIS CONFIRMED' : 'HYPOTHESIS DISPROVEN'}
          </span>
        </div>

        ${this.state.collapse ? `
          <div class="collapse-alert-box">
            <strong>${this.state.collapseReason}</strong>
          </div>
        ` : ''}

        <div class="feedback-block">
          <div class="block-label">HISTORICAL CAUSAL CONSEQUENCE:</div>
          <p class="block-content">${fb.consequence}</p>
        </div>

        <div class="feedback-block">
          <div class="block-label">NEOREALIST MECHANISM:</div>
          <p class="block-content">${fb.mechanism}</p>
        </div>

        <div class="feedback-block citation-block">
          <div class="block-label">ACADEMIC ANCHOR:</div>
          <p class="citation-text"><strong>${fb.citation}</strong></p>
        </div>

        ${fb.misconception ? `
          <div class="misconception-box">
            <div class="misc-tag">[MISCONCEPTION RECTIFIED: ${fb.misconception.label}]</div>
            <p class="misc-remediation">${fb.misconception.remediation}</p>
          </div>
        ` : ''}

        <button id="btnAdvanceCrisis" class="action-btn btn-primary" type="button">
          ${this.state.collapse ? 'PROCEED TO SYSTEMIC DEBRIEF' : 'ADVANCE TO NEXT CRISIS [SPACE / ENTER]'}
        </button>
      </div>
    `;

    const btnNext = document.getElementById('btnAdvanceCrisis');
    if (btnNext) {
      btnNext.onclick = () => {
        this.handleAdvanceCrisis();
      };
    }
  }

  handleAdvanceCrisis() {
    audioEngine.playMechanicalClick();
    this.playWaxSealAndGears();
    this.state.advanceCrisis();
    this.render();
  }

  renderMastery(container) {
    const q = this.state.getCurrentMasteryQuestion();
    if (!q) return;

    container.innerHTML = `
      <div class="card mastery-card" role="region" aria-label="Mastery Check Concept Evaluation">
        <div class="card-badge">PHASE 6: MASTERY CHECK CONCEPT QUESTION ${this.state.masteryIndex + 1} / 3</div>
        <h2 class="card-heading">BALANCE OF POWER CONCEPTUAL AUDIT</h2>
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
          <strong>${res.isCorrect ? 'THEORETICAL MASTERY DEMONSTRATED' : 'CONCEPTUAL REMEDIATION'}:</strong>
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
    const t = BOP_TRANSFER_SCENARIO;

    container.innerHTML = `
      <div class="card transfer-card" role="region" aria-label="Divergent Historical Transfer Scenario">
        <div class="card-badge">PHASE 7: DIVERGENT HISTORICAL CASE APPLICATION</div>
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
          <strong>${res.isCorrect ? 'TRANSFER EVALUATION CONFIRMED' : 'TRANSFER REMEDIATION'}:</strong>
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
          RESTART CRISIS SIMULATION
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

