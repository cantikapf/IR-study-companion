import * as THREE from '../../vendor/three.module.js';
import {
  NUCLEAR_CONFIG,
  NUCLEAR_OBJECTIVES,
  NUCLEAR_SCENARIOS,
  NUCLEAR_MASTERY_QUESTIONS,
  NUCLEAR_TRANSFER_SCENARIO,
  NuclearState
} from './NuclearConfig.js';
import { audioEngine } from '../../shared/core/AudioEngine.js';
import { renderDebrief } from '../../shared/learn/DebriefPanel.js';
import { OnboardingModal } from '../../shared/learn/OnboardingModal.js';

export class NuclearTriadGame {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.state = new NuclearState();
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
    this.playNoradSweep = () => {
      if (audioEngine.muted) return;
      audioEngine.init();
      const ctx = audioEngine.ctx;
      if (!ctx) return;
      const now = ctx.currentTime;

      // Radar sweep oscillation
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(440, now);
      osc.frequency.exponentialRampToValueAtTime(1760, now + 0.35);
      gain.gain.setValueAtTime(0.2, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);

      // Low sub bass radar hum
      const sub = ctx.createOscillator();
      const subGain = ctx.createGain();
      sub.type = 'sine';
      sub.frequency.setValueAtTime(90, now);
      sub.frequency.exponentialRampToValueAtTime(30, now + 0.5);
      subGain.gain.setValueAtTime(0.3, now);
      subGain.gain.exponentialRampToValueAtTime(0.001, now + 0.55);

      osc.connect(gain);
      gain.connect(ctx.destination);
      sub.connect(subGain);
      subGain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + 0.4);
      sub.start(now);
      sub.stop(now + 0.55);
    };
  }

  init3D() {
    const width = this.container.clientWidth || 1024;
    const height = this.container.clientHeight || 520;

    // Scene & Camera
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x030712);
    this.scene.fog = new THREE.FogExp2(0x030712, 0.007);

    this.camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    this.camera.position.set(0, 16, 52);
    this.camera.lookAt(0, 0, 0);

    // Renderer
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.container.innerHTML = '';
    this.container.appendChild(this.renderer.domElement);

    // Lighting
    const ambient = new THREE.AmbientLight(0xdbeafe, 0.7);
    this.scene.add(ambient);

    const keyLight = new THREE.DirectionalLight(0xf59e0b, 1.4);
    keyLight.position.set(35, 40, 35);
    this.scene.add(keyLight);

    const fillLight = new THREE.DirectionalLight(0x38bdf8, 0.8);
    fillLight.position.set(-35, -15, -25);
    this.scene.add(fillLight);

    // Globe Group
    this.globeGroup = new THREE.Group();
    this.scene.add(this.globeGroup);

    this.buildTacticalGlobe();
    this.buildTriadPins();
    this.buildAbmShieldDome();
    this.buildThreatArcs();

    // Window Resize
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

  buildTacticalGlobe() {
    const radius = 15;

    // 1. Deep Oceanic Core
    const globeGeo = new THREE.SphereGeometry(radius, 36, 36);
    this.globeMat = new THREE.MeshStandardMaterial({
      color: 0x071329,
      roughness: 0.85,
      metalness: 0.2
    });
    this.globeMesh = new THREE.Mesh(globeGeo, this.globeMat);
    this.globeGroup.add(this.globeMesh);

    // 2. Graticule / Wireframe Grid
    const wireMat = new THREE.MeshBasicMaterial({
      color: 0x0284c7,
      wireframe: true,
      transparent: true,
      opacity: 0.2
    });
    const wireMesh = new THREE.Mesh(globeGeo, wireMat);
    this.globeGroup.add(wireMesh);

    // 3. Polar Tactical Latitude Rings
    const ringGeo = new THREE.RingGeometry(15.05, 15.15, 64);
    const ringMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.35
    });

    const eqRing = new THREE.Mesh(ringGeo, ringMat);
    eqRing.rotation.x = Math.PI / 2;
    this.globeGroup.add(eqRing);

    // 4. Atmosphere Glow Shell
    const atmoGeo = new THREE.SphereGeometry(radius * 1.06, 32, 32);
    const atmoMat = new THREE.MeshBasicMaterial({
      color: 0x0ea5e9,
      transparent: true,
      opacity: 0.08,
      side: THREE.BackSide
    });
    const atmoMesh = new THREE.Mesh(atmoGeo, atmoMat);
    this.globeGroup.add(atmoMesh);
  }

  buildTriadPins() {
    // 1. ICBM Silo Pins (Land-based, North America region)
    this.icbmPins = [];
    const icbmCoords = [
      { x: -5, y: 7.5, z: 12.2 },
      { x: -2, y: 8.8, z: 11.8 },
      { x: -7, y: 6.2, z: 12.0 },
      { x: -4, y: 9.5, z: 11.2 }
    ];

    icbmCoords.forEach(c => {
      const pinGroup = new THREE.Group();
      pinGroup.position.set(c.x, c.y, c.z);

      // Silo well
      const wellGeo = new THREE.CylinderGeometry(0.8, 0.9, 0.4, 8);
      const wellMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
      const well = new THREE.Mesh(wellGeo, wellMat);
      pinGroup.add(well);

      // Missile silo pin
      const coneGeo = new THREE.ConeGeometry(0.65, 2.6, 8);
      const coneMat = new THREE.MeshStandardMaterial({
        color: 0xf59e0b,
        emissive: 0xf59e0b,
        emissiveIntensity: 0.5
      });
      const cone = new THREE.Mesh(coneGeo, coneMat);
      cone.position.y = 1.3;
      pinGroup.add(cone);

      this.globeGroup.add(pinGroup);
      this.icbmPins.push({ group: pinGroup, cone, well, basePos: pinGroup.position.clone() });
    });

    // 2. SLBM Submarine Pins (Deep-ocean patrol corridors: North Atlantic & Pacific)
    this.slbmPins = [];
    const slbmCoords = [
      { x: -12.5, y: 3.5, z: 7.2 },
      { x: -10.2, y: -4.5, z: 9.8 },
      { x: 3.5, y: 4.2, z: 14.2 }
    ];

    slbmCoords.forEach(c => {
      const subGroup = new THREE.Group();
      subGroup.position.set(c.x, c.y, c.z);

      // Submarine Hull
      const hullGeo = new THREE.CylinderGeometry(0.4, 0.4, 2.4, 8);
      const hullMat = new THREE.MeshStandardMaterial({
        color: 0x06b6d4,
        emissive: 0x06b6d4,
        emissiveIntensity: 0.6
      });
      const hull = new THREE.Mesh(hullGeo, hullMat);
      hull.rotation.z = Math.PI / 3;
      subGroup.add(hull);

      // Sonar Acoustic Ring
      const sonarGeo = new THREE.RingGeometry(0.8, 1.2, 16);
      const sonarMat = new THREE.MeshBasicMaterial({
        color: 0x06b6d4,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.4
      });
      const sonar = new THREE.Mesh(sonarGeo, sonarMat);
      sonar.rotation.x = Math.PI / 2;
      subGroup.add(sonar);

      this.globeGroup.add(subGroup);
      this.slbmPins.push({ group: subGroup, hull, sonar, basePos: subGroup.position.clone() });
    });

    // 3. Strategic Bomber Aircraft Pins (High-altitude Arctic and maritime patrol)
    this.bomberPins = [];
    const bomberCoords = [
      { x: 7.5, y: 11.2, z: 7.8 },
      { x: 10.5, y: 8.5, z: 8.2 },
      { x: 5.2, y: 12.8, z: 6.2 }
    ];

    bomberCoords.forEach(c => {
      const planeGroup = new THREE.Group();
      planeGroup.position.set(c.x, c.y, c.z);

      // Delta-wing bomber model
      const wingGeo = new THREE.ConeGeometry(0.9, 2.2, 3);
      const wingMat = new THREE.MeshStandardMaterial({
        color: 0x10b981,
        emissive: 0x10b981,
        emissiveIntensity: 0.5
      });
      const wing = new THREE.Mesh(wingGeo, wingMat);
      wing.rotation.x = Math.PI / 2;
      planeGroup.add(wing);

      this.globeGroup.add(planeGroup);
      this.bomberPins.push({ group: planeGroup, wing, basePos: planeGroup.position.clone() });
    });
  }

  buildAbmShieldDome() {
    // Geodesic Northern Hemisphere ABM Shield Dome
    const domeGeo = new THREE.SphereGeometry(16.5, 24, 16, 0, Math.PI * 2, 0, Math.PI / 2.3);
    this.abmMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      wireframe: true,
      transparent: true,
      opacity: 0.18,
      side: THREE.DoubleSide
    });
    this.abmDome = new THREE.Mesh(domeGeo, this.abmMat);
    this.globeGroup.add(this.abmDome);
  }

  buildThreatArcs() {
    this.threatArcsGroup = new THREE.Group();
    this.globeGroup.add(this.threatArcsGroup);
    this.threatCurves = [];

    // Create 3 parabolic trajectory threat curves originating from adversary hemisphere (Eastern Hemisphere)
    const targets = [
      new THREE.Vector3(-4, 9, 11),   // ICBM silo region
      new THREE.Vector3(-11, 2, 9),   // SLBM oceanic patrol
      new THREE.Vector3(7, 10, 8)     // Bomber Arctic flight path
    ];

    targets.forEach((tgt, i) => {
      const start = new THREE.Vector3(12, 6, -8); // Adversary launch bastion
      const mid = new THREE.Vector3(2 + i * 2, 22, 4); // Apex in space

      const curve = new THREE.QuadraticBezierCurve3(start, mid, tgt);
      const points = curve.getPoints(32);
      const arcGeo = new THREE.BufferGeometry().setFromPoints(points);
      const arcMat = new THREE.LineBasicMaterial({
        color: 0xf43f5e,
        transparent: true,
        opacity: 0.15,
        linewidth: 1
      });
      const line = new THREE.Line(arcGeo, arcMat);
      this.threatArcsGroup.add(line);
      this.threatCurves.push({ line, arcMat });
    });
  }

  triggerSignatureMoment() {
    this.playNoradSweep();
    audioEngine.playMechanicalClick();

    // Cascade NORAD alert lamps
    const lamps = document.querySelectorAll('.norad-lamp');
    lamps.forEach((lamp, idx) => {
      setTimeout(() => {
        lamp.classList.add('active');
        setTimeout(() => lamp.classList.remove('active'), 450);
      }, idx * 100);
    });

    // Rapid vector map scan pulse
    if (this.abmMat) {
      this.abmMat.opacity = 0.6;
      setTimeout(() => {
        if (this.abmMat) this.abmMat.opacity = 0.18;
      }, 700);
    }
  }

  animate() {
    requestAnimationFrame(this.animate);
    const delta = this.clock.getDelta();
    const time = this.clock.getElapsedTime();

    if (this.globeGroup) {
      this.globeGroup.rotation.y += 0.0035;
    }

    // Pulse Sonar rings on SLBMs
    if (this.slbmPins) {
      this.slbmPins.forEach((p, idx) => {
        if (p.sonar && p.sonar.material) {
          const s = 1 + Math.sin(time * 3 + idx) * 0.25;
          p.sonar.scale.set(s, s, s);
        }
      });
    }

    // Gentle banking on Bombers
    if (this.bomberPins) {
      this.bomberPins.forEach((p, idx) => {
        if (p.wing) {
          p.wing.rotation.z = Math.sin(time * 2 + idx) * 0.15;
        }
      });
    }

    // Threat arc pulse
    if (this.threatCurves && this.threatCurves.length > 0) {
      const arcPulse = 0.2 + Math.sin(time * 4) * 0.15;
      this.threatCurves.forEach(c => {
        if (c.arcMat) c.arcMat.opacity = arcPulse;
      });
    }

    this.renderer.render(this.scene, this.camera);
  }

  update3DState(simResult) {
    const sc = NUCLEAR_SCENARIOS[this.state.year - 1];
    const stress = sc ? sc.stressLeg : null;

    // 1. Update ICBM Silo Pins
    const icbmSurv = this.state.alloc.icbm >= (stress === 'icbm' ? 30 : 20);
    this.icbmPins.forEach(p => {
      if (icbmSurv) {
        p.cone.material.color.setHex(0xf59e0b);
        p.cone.material.emissive.setHex(0xf59e0b);
        p.cone.material.emissiveIntensity = 0.6;
        p.group.position.copy(p.basePos);
      } else {
        // Dims to burnt crimson and retracts downward
        p.cone.material.color.setHex(0x450a0a);
        p.cone.material.emissive.setHex(0xef4444);
        p.cone.material.emissiveIntensity = 0.15;
        p.group.position.y = p.basePos.y - 1.2;
      }
    });

    // 2. Update SLBM Submarine Pins
    const slbmSurv = this.state.alloc.slbm >= (stress === 'slbm' ? 40 : 30);
    this.slbmPins.forEach(p => {
      if (slbmSurv) {
        p.hull.material.color.setHex(0x06b6d4);
        p.hull.material.emissive.setHex(0x06b6d4);
        p.hull.material.emissiveIntensity = 0.6;
        if (p.sonar) p.sonar.visible = true;
      } else {
        // Murky dead dark-blue, disabled sonar
        p.hull.material.color.setHex(0x1e293b);
        p.hull.material.emissive.setHex(0x000000);
        p.hull.material.emissiveIntensity = 0.0;
        if (p.sonar) p.sonar.visible = false;
      }
    });

    // 3. Update Strategic Bomber Pins
    const bomberSurv = this.state.alloc.bomber >= (stress === 'bomber' ? 25 : 15);
    this.bomberPins.forEach(p => {
      if (bomberSurv) {
        p.wing.material.color.setHex(0x10b981);
        p.wing.material.emissive.setHex(0x10b981);
        p.wing.material.emissiveIntensity = 0.6;
      } else {
        p.wing.material.color.setHex(0x7f1d1d);
        p.wing.material.emissive.setHex(0xef4444);
        p.wing.material.emissiveIntensity = 0.2;
      }
    });

    // 4. Update ABM Dome & Schelling Destabilization Alert
    if (this.state.abmDestabilized) {
      this.abmMat.color.setHex(0xef4444);
      this.abmMat.opacity = 0.75;
      this.globeMat.color.setHex(0x2d0b12);
    } else {
      this.abmMat.color.setHex(0x38bdf8);
      this.abmMat.opacity = 0.18;
      this.globeMat.color.setHex(0x071329);
    }

    // 5. Light up adversary counterforce trajectory threat arcs
    if (this.threatCurves) {
      this.threatCurves.forEach(c => {
        if (simResult && simResult.crisis) {
          c.arcMat.color.setHex(0xf43f5e);
          c.arcMat.opacity = 0.85;
        } else {
          c.arcMat.color.setHex(0x38bdf8);
          c.arcMat.opacity = 0.25;
        }
      });
    }
  }

  bindDOM() {
    const btnToggle = document.getElementById('btnToggleRail');
    const btnMute = document.getElementById('btnAudioMute');
    const btnRestart = document.getElementById('btnRestart');

    if (btnToggle) {
      btnToggle.onclick = () => {
        audioEngine.playMechanicalClick();
        const rail = document.getElementById('decisionRail');
        if (rail) {
          this.railCollapsed = !this.railCollapsed;
          rail.classList.toggle('collapsed', this.railCollapsed);
          btnToggle.innerText = this.railCollapsed ? 'EXPAND RAIL' : 'COLLAPSE RAIL';
        }
      };
    }

    if (btnMute) {
      btnMute.onclick = () => {
        const isMuted = audioEngine.toggleMute();
        btnMute.innerText = isMuted ? 'UNMUTE AUDIO' : 'MUTE AUDIO';
      };
    }

    if (btnRestart) {
      btnRestart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.restartGame();
      };
    }
  }

  initOnboarding() {
    this.onboarding = new OnboardingModal({
      labId: 'lab-10',
      role: 'Strategic Air Command · Nuclear Triad Comptroller',
      objective: 'Allocate the defense budget across ICBMs, SLBMs, Bombers, and ABM defense to guarantee assured second-strike retaliatory capability without destabilizing MAD.',
      steps: [
        {
          step: '1',
          title: 'PREDICT DETERRENCE OUTCOME',
          desc: 'Analyze fiscal year threat scenarios and predict how budget imbalances or first-strike vulnerabilities affect stability.'
        },
        {
          step: '2',
          title: 'ALLOCATE TRIAD DEFENSE BUDGET',
          desc: 'Distribute $100B across ICBMs, SLBMs, Bombers, and ABM defense to guarantee survivable second-strike retaliation.'
        },
        {
          step: '3',
          title: 'AUDIT & MASTER SCHELLING MAD',
          desc: 'Inspect crisis stability feedback, correct deterrence misconceptions (e.g. ABM defense dilemma), and solve a transfer dilemma.'
        }
      ],
      controls: [
        { key: 'SLIDERS / INPUTS', label: 'Allocate defense budget across Triad legs & ABM' },
        { key: 'SPACE / ENTER', label: 'Simulate Year / Advance' },
        { key: '1, 2, 3', label: 'Select prediction & mastery responses' },
        { key: 'TAB', label: 'Toggle operational side rail' }
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
      if (['1', '2', '3'].includes(e.key)) {
        const opt = e.key === '1' ? 'A' : (e.key === '2' ? 'B' : 'C');
        const btn = document.querySelector(`[data-key="${opt}"]`);
        if (btn && !btn.disabled) btn.click();
      } else if (e.code === 'Space' || e.key === 'Enter') {
        const actionBtn = document.querySelector('.action-btn:not(:disabled)');
        if (actionBtn) actionBtn.click();
      }
    });
  }

  restartGame() {
    this.state.reset();
    if (this.globeMat) this.globeMat.color.setHex(0x071329);
    if (this.abmMat) {
      this.abmMat.color.setHex(0x38bdf8);
      this.abmMat.opacity = 0.18;
    }
    this.update3DState(null);
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
    const elYear = document.getElementById('hudYear');
    const elBudget = document.getElementById('hudBudget');
    const elStability = document.getElementById('hudStability');
    const elScore = document.getElementById('hudScore');

    if (elYear) {
      const sc = NUCLEAR_SCENARIOS[this.state.year - 1];
      elYear.innerText = sc ? `FY 0${this.state.year} / 04` : 'HISTORICAL AUDIT';
    }

    if (elBudget) {
      const total = this.state.getTotalBudget();
      elBudget.innerText = `$${total}B / $100B`;
      elBudget.style.color = total > 100 ? 'var(--accent-2)' : 'var(--accent)';
    }

    if (elStability) {
      elStability.innerText = `${this.state.stability}% MAD STABILITY`;
      elStability.style.color = this.state.stability >= 70 ? 'var(--accent-2)' : (this.state.stability >= 40 ? 'var(--accent)' : 'var(--border)');
    }

    if (elScore) {
      const stars = this.state.getStars();
      elScore.innerText = `${stars} / 3 STARS`;
    }
  }

  renderBriefing(container) {
    container.innerHTML = `
      <div class="card briefing-card" role="region" aria-label="Nuclear Command Mandate">
        <div class="card-badge">DEFENSE SCIENCE BOARD · STRATEGIC TRIAD MANDATE</div>
        <h2 class="card-heading">SECOND-STRIKE LEDGER: NUCLEAR DETERRENCE</h2>
        <p class="card-desc">
          As Secretary of Defense, you manage a fixed <strong>$100 Billion nuclear procurement budget</strong> across 4 fiscal years. Your mandate is to maintain <strong>Mutual Assured Destruction (MAD)</strong> stability by guaranteeing an invulnerable second-strike retaliatory capability against targeted adversary counterforce breakthroughs.
        </p>
        <div class="objectives-box">
          <div class="box-title">PEDAGOGICAL OBJECTIVES</div>
          <ul class="objectives-list">
            ${NUCLEAR_OBJECTIVES.map(obj => `<li>${obj}</li>`).join('')}
          </ul>
        </div>
        <div class="tactical-dossier">
          <div class="dossier-row"><strong>ICBM SILOS:</strong> <span>Target sponge absorbing adversary warheads ($20B base)</span></div>
          <div class="dossier-row"><strong>SLBM SUBMARINES:</strong> <span>Invulnerable second-strike retaliatory anchor ($30B base)</span></div>
          <div class="dossier-row"><strong>HEAVY BOMBERS:</strong> <span>Flexible crisis signaling & recallability ($15B base)</span></div>
          <div class="dossier-row"><strong>MISSILE DEFENSE:</strong> <span>ABM shield — destabilizes MAD if > $25B safe ceiling</span></div>
        </div>
        <button id="btnCommenceBriefing" class="action-btn btn-primary" type="button">
          COMMENCE FISCAL YEAR RECONNAISSANCE [SPACE]
        </button>
      </div>
    `;

    const btnStart = document.getElementById('btnCommenceBriefing');
    if (btnStart) {
      btnStart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.playNoradSweep();
        this.state.phase = 'PREDICT';
        this.render();
      };
    }
  }

  renderPrediction(container) {
    const sc = NUCLEAR_SCENARIOS[this.state.year - 1];
    if (!sc) return;

    container.innerHTML = `
      <div class="card prediction-card" role="region" aria-label="Hypothesis Commitment">
        <div class="card-badge">PREDICTION PHASE · FISCAL YEAR 0${this.state.year} / 04</div>
        <h2 class="card-heading">${sc.title}</h2>
        <p class="scenario-text">${sc.desc}</p>
        <div class="tactical-dossier" style="margin: 8px 0;">
          <div class="dossier-row"><strong>STRESSED TRIAD LEG:</strong> <span style="color:var(--accent);">${sc.stressLeg.toUpperCase()} (+ $10B requirement)</span></div>
          <div class="dossier-row"><strong>THEORETICAL DILEMMA:</strong> <span>${sc.theory}</span></div>
        </div>
        <div class="prediction-box">
          <p class="prediction-prompt"><strong>HYPOTHESIS COMMITMENT:</strong> ${sc.predictionPrompt}</p>
          <div class="options-stack">
            ${sc.predictionOptions.map(opt => `
              <button class="option-btn" data-key="${opt.key}" type="button">
                <span class="key-tag">[KEY ${opt.key}]</span>
                <span class="opt-text">${opt.text}</span>
              </button>
            `).join('')}
          </div>
        </div>
      </div>
    `;

    container.querySelectorAll('.option-btn').forEach(btn => {
      btn.onclick = (e) => {
        audioEngine.playMechanicalClick();
        const key = e.currentTarget.getAttribute('data-key');
        this.state.recordPrediction(key);
        this.render();
      };
    });
  }

  renderDecision(container) {
    const sc = NUCLEAR_SCENARIOS[this.state.year - 1];
    const total = this.state.getTotalBudget();
    const isOverBudget = total > 100;

    const stress = sc.stressLeg;
    const reqs = {
      icbm: stress === 'icbm' ? '30B (STRESSED)' : '20B',
      slbm: stress === 'slbm' ? '40B (STRESSED)' : '30B',
      bomber: stress === 'bomber' ? '25B (STRESSED)' : '15B',
      defense: stress === 'defense' ? '25B (MAX SAFE CAP: $25B)' : '15B (MAX SAFE: $25B)'
    };

    container.innerHTML = `
      <div class="card decision-card" role="region" aria-label="Nuclear Triad Budget Allocation">
        <div class="card-badge">ALLOCATION CONSOLE · FY 0${this.state.year} / 04</div>
        <h2 class="card-heading">${sc.title}</h2>
        <div class="hud-stat" style="justify-content:space-between; margin-bottom: 8px;">
          <span style="font-size:0.8rem; font-weight:800;">BUDGET CAP: $100 BILLION</span>
          <span id="railBudgetDisplay" style="font-weight:800; font-size:0.88rem; color:${isOverBudget ? 'var(--accent-2)' : 'var(--accent)'};">
            TOTAL: $${total}B / $100B
          </span>
        </div>

        <div class="sliders-stack" style="display:flex; flex-direction:column; gap:12px;">
          <!-- ICBM Slider -->
          <div class="slider-group">
            <div style="display:flex; justify-content:space-between; font-size:0.78rem;">
              <strong>1. LAND ICBM SILOS</strong>
              <span id="disp_icbm" style="color:var(--accent);">$${this.state.alloc.icbm}B (Req: ${reqs.icbm})</span>
            </div>
            <input type="range" class="procure-slider" id="sl_icbm" min="10" max="50" step="5" value="${this.state.alloc.icbm}">
          </div>

          <!-- SLBM Slider -->
          <div class="slider-group">
            <div style="display:flex; justify-content:space-between; font-size:0.78rem;">
              <strong>2. UNDERSEA SLBM SUBMARINES</strong>
              <span id="disp_slbm" style="color:var(--accent);">$${this.state.alloc.slbm}B (Req: ${reqs.slbm})</span>
            </div>
            <input type="range" class="procure-slider" id="sl_slbm" min="15" max="55" step="5" value="${this.state.alloc.slbm}">
          </div>

          <!-- Bomber Slider -->
          <div class="slider-group">
            <div style="display:flex; justify-content:space-between; font-size:0.78rem;">
              <strong>3. STRATEGIC HEAVY BOMBERS</strong>
              <span id="disp_bomber" style="color:var(--accent);">$${this.state.alloc.bomber}B (Req: ${reqs.bomber})</span>
            </div>
            <input type="range" class="procure-slider" id="sl_bomber" min="10" max="45" step="5" value="${this.state.alloc.bomber}">
          </div>

          <!-- ABM Defense Slider -->
          <div class="slider-group">
            <div style="display:flex; justify-content:space-between; font-size:0.78rem;">
              <strong>4. ABM MISSILE DEFENSE SHIELD</strong>
              <span id="disp_defense" style="color:var(--accent);">$${this.state.alloc.defense}B (Req: ${reqs.defense})</span>
            </div>
            <input type="range" class="procure-slider" id="sl_defense" min="10" max="40" step="5" value="${this.state.alloc.defense}">
          </div>
        </div>

        <button id="btnExecuteSimulate" class="action-btn btn-primary" type="button" ${isOverBudget ? 'disabled' : ''}>
          EXECUTE ALLOCATION & SIMULATE STABILITY [SPACE]
        </button>
      </div>
    `;

    // Bind sliders
    ['icbm', 'slbm', 'bomber', 'defense'].forEach(leg => {
      const input = document.getElementById(`sl_${leg}`);
      if (input) {
        input.oninput = (e) => {
          const val = parseInt(e.target.value, 10);
          this.state.setAllocation(leg, val);
          const disp = document.getElementById(`disp_${leg}`);
          if (disp) disp.innerText = `$${val}B (Req: ${reqs[leg]})`;

          const curTotal = this.state.getTotalBudget();
          const budgetDisp = document.getElementById('railBudgetDisplay');
          const btnExec = document.getElementById('btnExecuteSimulate');

          if (budgetDisp) {
            budgetDisp.innerText = `TOTAL: $${curTotal}B / $100B`;
            budgetDisp.style.color = curTotal > 100 ? 'var(--accent-2)' : 'var(--accent)';
          }

          if (btnExec) {
            btnExec.disabled = curTotal > 100;
          }

          this.updateHUD();
          this.update3DState(null);
        };
      }
    });

    const btnExec = document.getElementById('btnExecuteSimulate');
    if (btnExec) {
      btnExec.onclick = () => {
        audioEngine.playMechanicalClick();
        const simRes = this.state.simulateYearEnd();
        this.update3DState(simRes);

        if (simRes.crisis) {
          audioEngine.playBetrayalBoom();
        } else {
          audioEngine.playChimeCooperation();
        }

        this.render();
      };
    }
  }

  renderConsequence(container) {
    const fb = this.state.lastFeedback;
    const isSuccess = fb && fb.outcome === 'success';

    container.innerHTML = `
      <div class="card consequence-card ${isSuccess ? 'card-success' : 'card-failure'}" role="region" aria-label="Fiscal Year Evaluation">
        <div class="feedback-header">
          <span class="badge ${isSuccess ? 'badge-success' : 'badge-failure'}">
            ${isSuccess ? '✓ SECOND-STRIKE DETERRENCE ASSURED' : '⚠ CRISIS INSTABILITY TRIGGERED'}
          </span>
          <span class="hypothesis-match">
            ${fb.predictionMatch ? 'HYPOTHESIS CONFIRMED ✓' : 'HYPOTHESIS DIVERGENCE'}
          </span>
        </div>
        <div class="feedback-block">
          <div class="block-label">CONSEQUENCE:</div>
          <div class="block-content">${fb.consequence}</div>
        </div>
        <div class="feedback-block">
          <div class="block-label">INSTITUTIONAL MECHANISM:</div>
          <div class="block-content">${fb.mechanism}</div>
        </div>
        <div class="feedback-block citation-block">
          <div class="block-label">ACADEMIC CITATION:</div>
          <div class="citation-text"><em>${fb.citation}</em></div>
        </div>
        ${fb.misconception ? `
          <div class="misconception-box">
            <div class="misc-tag">[MISCONCEPTION: ${fb.misconception.label}]</div>
            <div class="misc-remediation">${fb.misconception.remediation}</div>
          </div>
        ` : ''}
        <button id="btnAdvanceFY" class="action-btn btn-primary" type="button">
          ${this.state.year < 4 ? 'PROCEED TO NEXT FISCAL YEAR [SPACE]' : 'PROCEED TO CONCEPT MASTERY CHECK [SPACE]'}
        </button>
      </div>
    `;

    const btnAdv = document.getElementById('btnAdvanceFY');
    if (btnAdv) {
      btnAdv.onclick = () => {
        audioEngine.playMechanicalClick();
        const hasNext = this.state.advanceYear();
        this.render();
      };
    }
  }

  renderMastery(container) {
    const q = this.state.getCurrentMasteryQuestion();
    if (!q) {
      this.state.phase = 'TRANSFER';
      this.render();
      return;
    }

    container.innerHTML = `
      <div class="card mastery-card" role="region" aria-label="Concept Mastery Check">
        <div class="card-badge">MASTERY CHECK · ITEM ${this.state.masteryIndex + 1} OF ${NUCLEAR_MASTERY_QUESTIONS.length}</div>
        <h2 class="card-heading">DETERRENCE THEORY MASTERY</h2>
        <p class="mastery-prompt">${q.prompt}</p>
        <div class="options-stack">
          ${q.options.map(opt => `
            <button class="option-btn" data-key="${opt.key}" type="button">
              <span class="key-tag">[KEY ${opt.key}]</span>
              <span class="opt-text">${opt.text}</span>
            </button>
          `).join('')}
        </div>
      </div>
    `;

    container.querySelectorAll('.option-btn').forEach(btn => {
      btn.onclick = (e) => {
        audioEngine.playMechanicalClick();
        const key = e.currentTarget.getAttribute('data-key');
        const res = this.state.answerMasteryQuestion(key);
        this.renderMasteryFeedback(container, res);
      };
    });
  }

  renderMasteryFeedback(container, res) {
    const isCorrect = res.isCorrect;
    container.innerHTML = `
      <div class="card consequence-card ${isCorrect ? 'card-success' : 'card-failure'}" role="region" aria-label="Mastery Feedback">
        <div class="feedback-header">
          <span class="badge ${isCorrect ? 'badge-success' : 'badge-failure'}">
            ${isCorrect ? '✓ CONCEPT DEMONSTRATED' : '✕ CONCEPT DRIFT'}
          </span>
        </div>
        <div class="feedback-block">
          <div class="block-label">EXPLANATION:</div>
          <div class="block-content">${res.rationale}</div>
        </div>
        <div class="feedback-block citation-block">
          <div class="block-label">THEORETICAL CITATION:</div>
          <div class="citation-text"><em>${res.citation}</em></div>
        </div>
        ${res.misconception ? `
          <div class="misconception-box">
            <div class="misc-tag">[REMEDIATION: ${res.misconception.label}]</div>
            <div class="misc-remediation">${res.misconception.remediation}</div>
          </div>
        ` : ''}
        <button id="btnNextMastery" class="action-btn btn-primary" type="button">
          CONTINUE [SPACE]
        </button>
      </div>
    `;

    if (isCorrect) audioEngine.playChimeCooperation();
    else audioEngine.playAlarmKlaxon();

    const btnNext = document.getElementById('btnNextMastery');
    if (btnNext) {
      btnNext.onclick = () => {
        audioEngine.playMechanicalClick();
        this.render();
      };
    }
  }

  renderTransfer(container) {
    const sc = NUCLEAR_TRANSFER_SCENARIO;

    container.innerHTML = `
      <div class="card transfer-card" role="region" aria-label="Transfer Scenario Evaluation">
        <div class="card-badge">TRANSFER EVALUATION · HISTORICAL CRISIS STABILITY</div>
        <h2 class="card-heading">${sc.title}</h2>
        <p class="scenario-text">${sc.context}</p>
        <p class="transfer-prompt"><strong>QUESTION:</strong> ${sc.prompt}</p>
        <div class="options-stack">
          ${sc.options.map(opt => `
            <button class="option-btn" data-key="${opt.key}" type="button">
              <span class="key-tag">[KEY ${opt.key}]</span>
              <span class="opt-text">${opt.text}</span>
            </button>
          `).join('')}
        </div>
      </div>
    `;

    container.querySelectorAll('.option-btn').forEach(btn => {
      btn.onclick = (e) => {
        audioEngine.playMechanicalClick();
        const key = e.currentTarget.getAttribute('data-key');
        const res = this.state.answerTransfer(key);
        this.renderTransferFeedback(container, res);
      };
    });
  }

  renderTransferFeedback(container, res) {
    const isCorrect = res.isCorrect;
    container.innerHTML = `
      <div class="card consequence-card ${isCorrect ? 'card-success' : 'card-failure'}" role="region" aria-label="Transfer Feedback">
        <div class="feedback-header">
          <span class="badge ${isCorrect ? 'badge-success' : 'badge-failure'}">
            ${isCorrect ? '✓ HISTORICAL TRANSFER DEMONSTRATED' : '✕ TRANSFER DRIFT'}
          </span>
        </div>
        <div class="feedback-block">
          <div class="block-label">ANALYSIS:</div>
          <div class="block-content">${res.rationale}</div>
        </div>
        <div class="feedback-block citation-block">
          <div class="block-label">ACADEMIC CITATION:</div>
          <div class="citation-text"><em>${res.citation}</em></div>
        </div>
        <button id="btnProceedDebrief" class="action-btn btn-primary" type="button">
          VIEW FULL LAB DEBRIEF [SPACE]
        </button>
      </div>
    `;

    if (isCorrect) audioEngine.playChimeCooperation();
    else audioEngine.playAlarmKlaxon();

    const btnNext = document.getElementById('btnProceedDebrief');
    if (btnNext) {
      btnNext.onclick = () => {
        audioEngine.playMechanicalClick();
        this.render();
      };
    }
  }

  renderDebrief(container) {
    const report = this.state.getReport();
    localStorage.setItem('labs_completed_nuclear_deterrence', 'true');

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
