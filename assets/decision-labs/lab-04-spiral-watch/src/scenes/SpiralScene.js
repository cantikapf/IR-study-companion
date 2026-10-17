import {
  POSTURES,
  SpiralState,
  MASTERY_CHECKS,
  TRANSFER_SCENARIO
} from '../SpiralConfig.js';
import { audioEngine } from '../../../shared/core/AudioEngine.js';
import { renderDebrief } from '../../../shared/learn/DebriefPanel.js';
import { OnboardingModal } from '../../../shared/learn/OnboardingModal.js';

export class SpiralScene extends Phaser.Scene {
  constructor() {
    super('SpiralScene');
    this.state = new SpiralState();
    this.radarAngle = 0;
    this.sweepTrail = [];
    this.deSyncActive = false;
    this.signaturePingPlayed = false;
  }

  preload() {
    this.load.image('chamber_bg', '../assets/bg/chamber.png');
    this.load.image('table_wide', '../assets/sprites/table_wide.png');
    this.load.spritesheet('envoy', '../assets/sprites/diplomat_envoy.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('rival', '../assets/sprites/diplomat_rival.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('pips', '../assets/ui/pips.png', { frameWidth: 16, frameHeight: 16 });
  }

  create() {
    // 1. Polar Radome Background
    this.add.rectangle(512, 300, 1024, 600, 0x020617);

    // 2. Arctic Grid Floor & Control Dials
    this.gridGfx = this.add.graphics();
    this.gridGfx.lineStyle(1, 0x0ea5e9, 0.15);
    for (let x = 0; x < 1024; x += 40) {
      this.gridGfx.lineBetween(x, 0, x, 600);
    }
    for (let y = 0; y < 600; y += 40) {
      this.gridGfx.lineBetween(0, y, 1024, y);
    }

    // 3. Central PPI Radome Scope
    this.radarCenterX = 512;
    this.radarCenterY = 280;
    this.radarRadius = 210;

    // Outer Bezel
    this.add.circle(this.radarCenterX, this.radarCenterY, this.radarRadius + 14, 0x08172e)
      .setStrokeStyle(3, 0x0ea5e9);
    this.add.circle(this.radarCenterX, this.radarCenterY, this.radarRadius + 4, 0x030a18)
      .setStrokeStyle(1, 0x38bdf8);

    this.radarGfx = this.add.graphics();
    this.phosphorTrailGfx = this.add.graphics();
    this.deSyncGfx = this.add.graphics();

    // 4. Border DMZ Meridian (Vertical Meridian dividing Alpha & Beta)
    this.dmzLineGfx = this.add.graphics();

    // 5. Alpha & Beta Command Outposts (Avatars)
    // Left: Alpha Command Post
    this.alphaEnvoy = this.add.sprite(150, 270, 'envoy', 0).setScale(4);
    this.alphaLabel = this.add.text(150, 345, 'STATE ALPHA [OUR BORDER]', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '11px',
      color: '#0ea5e9',
      backgroundColor: '#030a1a',
      padding: { x: 6, y: 3 }
    }).setOrigin(0.5);

    // Right: Beta Command Post
    this.betaEnvoy = this.add.sprite(874, 270, 'rival', 0).setScale(4);
    this.betaLabel = this.add.text(874, 345, 'STATE BETA [RIVAL INTEL]', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '11px',
      color: '#f59e0b',
      backgroundColor: '#1c1005',
      padding: { x: 6, y: 3 }
    }).setOrigin(0.5);

    // 6. Perimeter Radar Banner (Bottom)
    this.banner = this.add.container(512, 530);
    const bBg = this.add.rectangle(0, 0, 780, 42, 0x0b1528, 0.95)
      .setStrokeStyle(1, 0x0ea5e9);
    this.bannerText = this.add.text(0, 0, 'RADOME ACTIVE: Arctic PPI scope tracking frontier deployments...', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '12px',
      color: '#e8eef8'
    }).setOrigin(0.5);
    this.banner.add([bBg, this.bannerText]);

    // 7. Signature Moment: rotating PPI sweep + radar chimes in first 3 seconds
    this.triggerSignatureSweep();

    // 8. Bind DOM & Start
    this.bindDOM();
    this.initOnboarding();
    this.renderBriefing();
  }

  triggerSignatureSweep() {
    this.radarAngle = 0;
    this.sweepTrail = [];
    audioEngine.init();
    audioEngine.playMechanicalClick();
    this.time.delayedCall(200, () => audioEngine.playMechanicalClick());
    this.time.delayedCall(450, () => audioEngine.playChimeCooperation());
  }

  update(time, delta) {
    this.radarAngle += 0.025;
    if (this.radarAngle > Math.PI * 2) {
      this.radarAngle -= Math.PI * 2;
    }

    // Phosphor sweep persistence trail
    this.sweepTrail.push({
      angle: this.radarAngle,
      time: time
    });
    // Prune trail older than 800ms
    this.sweepTrail = this.sweepTrail.filter(t => (time - t.time) < 800);

    const cx = this.radarCenterX;
    const cy = this.radarCenterY;
    const r = this.radarRadius;

    // Render DMZ Meridian
    this.dmzLineGfx.clear();
    const s = this.state.stability;
    const dmzColor = s >= 70 ? 0x10b981 : (s >= 40 ? 0xf59e0b : 0xef4444);
    this.dmzLineGfx.lineStyle(1.5, dmzColor, 0.7);
    this.dmzLineGfx.lineBetween(cx, cy - r, cx, cy + r);

    // Render Scope Rings & Compass Reticles
    this.radarGfx.clear();
    this.radarGfx.lineStyle(1, 0x0ea5e9, 0.25);
    this.radarGfx.strokeCircle(cx, cy, r * 0.25);
    this.radarGfx.strokeCircle(cx, cy, r * 0.5);
    this.radarGfx.strokeCircle(cx, cy, r * 0.75);
    this.radarGfx.strokeCircle(cx, cy, r);

    this.radarGfx.lineBetween(cx - r, cy, cx + r, cy);
    this.radarGfx.lineBetween(cx, cy - r, cx, cy + r);

    // Phosphor Sweep Trail
    this.phosphorTrailGfx.clear();
    this.sweepTrail.forEach(item => {
      const age = time - item.time;
      const alpha = (1 - (age / 800)) * 0.25;
      const sx = cx + Math.cos(item.angle) * r;
      const sy = cy + Math.sin(item.angle) * r;
      this.phosphorTrailGfx.lineStyle(2, 0x0ea5e9, alpha);
      this.phosphorTrailGfx.lineBetween(cx, cy, sx, sy);
    });

    // Primary Sweep Beam
    const hx = cx + Math.cos(this.radarAngle) * r;
    const hy = cy + Math.sin(this.radarAngle) * r;
    this.radarGfx.lineStyle(2, 0x38bdf8, 0.95);
    this.radarGfx.lineBetween(cx, cy, hx, hy);

    // REAL-STATE DRIVEN BLIPS
    // Draw blips according to state.radarBlips
    this.state.radarBlips.forEach(b => {
      const bx = cx + (b.x * (r / 90));
      const by = cy + (b.y * (r / 90));

      if (b.type === 'strike') {
        // Red pulsating offensive strike missile contact
        this.radarGfx.fillStyle(0xef4444, b.alpha);
        this.radarGfx.fillCircle(bx, by, 5);
        this.radarGfx.lineStyle(1, 0xfca5a5, 0.8);
        this.radarGfx.strokeCircle(bx, by, 8);
      } else if (b.type === 'defense') {
        // Amber defensive radar sensor outpost
        this.radarGfx.fillStyle(0xf59e0b, b.alpha);
        this.radarGfx.fillRect(bx - 4, by - 4, 8, 8);
        this.radarGfx.lineStyle(1, 0xfde68a, 0.8);
        this.radarGfx.strokeRect(bx - 6, by - 6, 12, 12);
      } else if (b.type === 'cbm') {
        // Cyan peaceful verified de-escalation beacon
        this.radarGfx.fillStyle(0x10b981, b.alpha);
        this.radarGfx.fillCircle(bx, by, 6);
        this.radarGfx.lineStyle(2, 0x34d399, 0.9);
        this.radarGfx.strokeCircle(bx, by, 12);
      }
    });

    // De-sync Tear / Glitch Visual (triggers if stability <= 35%)
    this.deSyncGfx.clear();
    if (this.state.stability <= 35) {
      this.deSyncGfx.fillStyle(0xef4444, 0.08);
      for (let i = 0; i < 3; i++) {
        const tearY = cy - r + Math.random() * (r * 2);
        const tearH = 4 + Math.random() * 8;
        this.deSyncGfx.fillRect(cx - r, tearY, r * 2, tearH);
      }
    }
  }

  updateReadinessDisplays() {
    const s = this.state.stability;
    const strip = document.getElementById('railStatusStrip');
    if (strip) {
      strip.innerHTML = `
        <div class="rail-stat"><span class="stat-lbl">STABILITY:</span> <span class="stat-val ${s <= 35 ? 'val-danger' : ''}">${s}%</span></div>
        <div class="rail-stat"><span class="stat-lbl">SEASON:</span> <span class="stat-val">0${this.state.round} / 05</span></div>
        <div class="rail-stat"><span class="stat-lbl">BLIPS:</span> <span class="stat-val">${this.state.radarBlips.length}</span></div>
      `;
    }
  }

  bindDOM() {
    const btnToggleRail = document.getElementById('btnToggleRail');
    const sideRail = document.getElementById('sideRail');
    if (btnToggleRail && sideRail) {
      btnToggleRail.onclick = () => {
        sideRail.classList.toggle('collapsed');
      };
    }

    const btnAudio = document.getElementById('btnAudioToggle');
    if (btnAudio) {
      btnAudio.onclick = () => {
        const muted = audioEngine.toggleMute();
        btnAudio.innerText = muted ? 'AUDIO: OFF' : 'AUDIO: ON';
      };
    }

    // Keyboard shortcuts
    this.input.keyboard.on('keydown-ONE', () => this.handleKey(0));
    this.input.keyboard.on('keydown-TWO', () => this.handleKey(1));
    this.input.keyboard.on('keydown-THREE', () => this.handleKey(2));
    this.input.keyboard.on('keydown-SPACE', () => this.handleSpace());
    this.input.keyboard.on('keydown-M', () => { if (btnAudio) btnAudio.click(); });
    this.input.keyboard.on('keydown-TAB', (e) => {
      e.preventDefault();
      if (btnToggleRail) btnToggleRail.click();
    });
  }

  initOnboarding() {
    this.onboarding = new OnboardingModal({
      labId: 'lab-04',
      role: 'Early Warning Sector Commander · Arctic Radome',
      objective: 'Dampen mutual security dilemma escalation spirals by calibrating defensive postures vs verifiable CBMs without inviting surprise attack.',
      steps: [
        {
          step: '1',
          title: 'HYPOTHESIZE & PREDICT',
          desc: 'Commit to an analytical expectation before acting. Anticipate how State Beta will interpret your border radar posture.'
        },
        {
          step: '2',
          title: 'CALIBRATE BORDER POSTURES',
          desc: 'Deploy distinguishable defensive postures or verified CBMs [1, 2, 3]. Monitor DMZ stability and radar blips in real time.'
        },
        {
          step: '3',
          title: 'AUDIT & MASTER JERVIS LENSES',
          desc: 'Analyze offense-defense balance and distinguishability, correct security dilemma misconceptions, and solve a historical transfer case.'
        }
      ],
      controls: [
        { key: '1, 2, 3', label: 'Postures [1, 2, 3] (Radar, Perimeter, CBMs)' },
        { key: 'SPACE', label: 'Advance [SPACE] & confirm choices' },
        { key: 'TAB', label: 'Toggle operational side rail' },
        { key: 'M', label: 'Toggle sound synthesizer' }
      ],
      onStart: () => {
        this.triggerSignatureSweep();
      }
    });

    const btnHowToPlay = document.getElementById('btnHowToPlay');
    if (btnHowToPlay) {
      btnHowToPlay.onclick = () => {
        audioEngine.playMechanicalClick();
        this.onboarding.open();
      };
    }

    // Auto-open on initial session boot
    this.onboarding.open();
  }

  handleKey(index) {
    if (this.onboarding && this.onboarding.isOpen) return;

    if (this.state.phase === 'PREDICT') {
      const opts = ['pred-mirror', 'pred-spiral', 'pred-exploit'];
      if (opts[index]) this.submitPrediction(opts[index]);
    } else if (this.state.phase === 'DECIDE') {
      if (POSTURES[index]) this.submitDecision(POSTURES[index].id);
    } else if (this.state.phase === 'ATTRIBUTION') {
      const atts = ['FEAR', 'REVISIONIST'];
      if (atts[index]) this.submitAttribution(atts[index]);
    } else if (this.state.phase === 'MASTERY') {
      const q = MASTERY_CHECKS[this.state.masteryIndex];
      if (q && q.choices[index]) this.submitMastery(q.choices[index].id);
    } else if (this.state.phase === 'TRANSFER') {
      if (!this.state.transferAnswered && TRANSFER_SCENARIO.choices[index]) {
        this.submitTransfer(TRANSFER_SCENARIO.choices[index].id);
      }
    }
  }

  handleSpace() {
    if (this.onboarding && this.onboarding.isOpen) return;
    const btn = document.getElementById('btnPhaseAdvance');
    if (btn) btn.click();
  }

  appendLog(msg, tag = 'RADOME') {
    const logEl = document.getElementById('tacticalLog');
    if (!logEl) return;
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    const time = new Date().toISOString().substring(11, 19);
    entry.innerHTML = `<span class="log-time">[${time}Z]</span> <span class="log-tag">[${tag}]:</span> ${msg}`;
    logEl.prepend(entry);
  }

  renderBriefing() {
    this.state.phase = 'BRIEF';
    this.updateReadinessDisplays();
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 1 / 7 · OPERATIONAL BRIEFING</div>
        <h2 class="phase-title">Arctic Early-Warning Radome</h2>
        <p class="phase-desc">
          You command frontier early-warning defense along an unfortified DMZ separating State Alpha and State Beta.
          Both states operate under structural anarchy where weapons procured for defense can easily appear offensive.
        </p>

        <div class="callout-box">
          <div class="callout-heading">CURRICULUM OBJECTIVES</div>
          <ul class="learning-objectives-list">
            <li><strong>Spiral vs Deterrence:</strong> Learn when military expansion triggers a counter-spiral vs when it deters aggression.</li>
            <li><strong>Offence–Defence Indistinguishability:</strong> Discover why weapons with offensive reach provoke adversary panic.</li>
            <li><strong>Verified CBMs:</strong> Master how transparency and verification dismantle security dilemmas.</li>
          </ul>
        </div>

        <button class="lab-btn lab-btn-primary" id="btnPhaseAdvance">
          INITIALIZE PPI RADOME [BEGIN OPERATIONS]
        </button>
      </div>
    `;

    document.getElementById('btnPhaseAdvance').onclick = () => {
      audioEngine.init();
      audioEngine.playMechanicalClick();
      this.triggerSignatureSweep();
      this.startPredictPhase();
    };
  }

  startPredictPhase() {
    this.state.phase = 'PREDICT';
    this.updateReadinessDisplays();
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    this.bannerText.setText(`SEASON ${this.state.round} / 05 · Formulate rival reaction hypothesis.`);
    this.appendLog(`Season ${this.state.round} surveillance sweep active.`, 'RADOME');

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 2 / 7 · HYPOTHESIS &amp; PREDICTION (ROUND ${this.state.round}/5)</div>
        <h2 class="phase-title">Frontier Perimeter Calibration</h2>
        <p class="phase-desc">Before locking in our frontier posture, formulate your theoretical expectation of State Beta's reaction:</p>

        <div class="sigint-banner">
          <span class="sigint-tag">INTEL INTERCEPT:</span> ${this.state.betaArchetype.sigint}
        </div>

        <div class="prompt-box">
          <div class="prompt-question">Predict how State Beta will respond to our deployment:</div>
          <div class="choices-stack">
            <button class="choice-btn" data-id="pred-mirror">
              <span class="choice-num">[1]</span>
              <span class="choice-text">Beta will reciprocate restraint if our posture is unthreatening (Spiral Model).</span>
            </button>
            <button class="choice-btn" data-id="pred-spiral">
              <span class="choice-num">[2]</span>
              <span class="choice-text">Beta will misinterpret any military build as offensive and counter-escalate (Indistinguishability).</span>
            </button>
            <button class="choice-btn" data-id="pred-exploit">
              <span class="choice-num">[3]</span>
              <span class="choice-text">Beta will view unilateral restraint as weakness and deploy offensive missiles (Deterrence Model).</span>
            </button>
          </div>
        </div>
      </div>
    `;

    panel.querySelectorAll('.choice-btn').forEach(btn => {
      btn.onclick = () => this.submitPrediction(btn.dataset.id);
    });
  }

  submitPrediction(predictionId) {
    audioEngine.playMechanicalClick();
    this.state.recordPrediction(predictionId);
    this.appendLog(`Prediction recorded: [${predictionId}]`, 'ANALYSIS');
    this.startDecidePhase();
  }

  startDecidePhase() {
    this.state.phase = 'DECIDE';
    this.updateReadinessDisplays();
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 3 / 7 · POSTURE CALIBRATION (ROUND ${this.state.round}/5)</div>
        <h2 class="phase-title">Select State Alpha Posture</h2>
        <p class="phase-desc">Calibrate our defensive posture along the DMZ:</p>

        <div class="choices-stack">
          ${POSTURES.map((p, i) => `
            <button class="choice-btn decision-btn" data-id="${p.id}">
              <div class="choice-top">
                <span class="choice-num">[${i + 1}]</span>
                <span class="choice-title">${p.title}</span>
                <span class="choice-tag">${p.type}</span>
              </div>
              <div class="choice-desc">${p.desc}</div>
            </button>
          `).join('')}
        </div>
      </div>
    `;

    panel.querySelectorAll('.decision-btn').forEach(btn => {
      btn.onclick = () => this.submitDecision(btn.dataset.id);
    });
  }

  submitDecision(postureId) {
    audioEngine.init();
    audioEngine.playMechanicalClick();

    const result = this.state.applyTurn(postureId);
    this.updateReadinessDisplays();

    if (result.delta > 0) {
      audioEngine.playChimeCooperation();
      this.alphaEnvoy.setTexture('envoy', 5);
      this.betaEnvoy.setTexture('rival', 5);
      this.bannerText.setText(`DE-ESCALATION SUCCESS: Stability increased (+${result.delta}%).`);
      this.appendLog(`Alpha deployed ${result.playerPosture} -> Beta responded with ${result.betaPosture} (+${result.delta}%)`, 'COOPERATION');
    } else {
      audioEngine.playBetrayalBoom();
      this.cameras.main.shake(200, 0.012);
      this.alphaEnvoy.setTexture('envoy', 7);
      this.betaEnvoy.setTexture('rival', 6);
      this.bannerText.setText(`SECURITY SPIRAL ALERT: Stability degraded (${result.delta}%).`);
      this.appendLog(`Alpha deployed ${result.playerPosture} -> Beta responded with ${result.betaPosture} (${result.delta}%)`, 'ESCALATION');
    }

    this.renderConsequenceAndExplain(result);
  }

  renderConsequenceAndExplain(turnResult) {
    this.state.phase = 'EXPLAIN';
    this.updateReadinessDisplays();
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    const fb = turnResult.feedback;
    const matchBadge = fb.predictionMatch
      ? '<span class="match-badge match-yes">HYPOTHESIS CONFIRMED</span>'
      : '<span class="match-badge match-no">HYPOTHESIS REFUTED</span>';

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 4 / 7 · CONSEQUENCE &amp; EXPLANATION</div>
        <div class="outcome-header outcome-${fb.outcome}">
          OUTCOME: ${fb.outcome.toUpperCase()} · ${matchBadge}
        </div>

        <div class="feedback-block">
          <div class="feedback-row">
            <span class="fb-label">SYSTEMIC CONSEQUENCE:</span>
            <span class="fb-text">${fb.consequence}</span>
          </div>

          <div class="feedback-row">
            <span class="fb-label">IR MECHANISM:</span>
            <span class="fb-text">${fb.mechanism}</span>
          </div>

          <div class="feedback-row">
            <span class="fb-label">ACADEMIC CITATION:</span>
            <span class="fb-text citation-text">${fb.citation}</span>
          </div>

          ${fb.misconception ? `
            <div class="misconception-card">
              <div class="misc-tag">MISCONCEPTION IDENTIFIED: ${fb.misconception.label}</div>
              <div class="misc-remediation">${fb.misconception.remediation}</div>
            </div>
          ` : ''}
        </div>

        <button class="lab-btn lab-btn-primary" id="btnPhaseAdvance">
          PROCEED TO POST-ROUND ATTRIBUTION
        </button>
      </div>
    `;

    document.getElementById('btnPhaseAdvance').onclick = () => {
      audioEngine.playMechanicalClick();
      this.startAttributionPhase(turnResult);
    };
  }

  startAttributionPhase(turnResult) {
    this.state.phase = 'ATTRIBUTION';
    this.updateReadinessDisplays();
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    this.bannerText.setText(`ATTRIBUTION PROMPT: Diagnose State Beta's underlying motivation.`);

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">POST-ROUND ATTRIBUTION · ROBERT JERVIS PARADIGM</div>
        <h2 class="phase-title">Diagnose Rival Intent</h2>
        <p class="phase-desc">
          State Beta deployed: <strong>${turnResult.betaPosture}</strong>.<br>
          Based on the observed evidence and intelligence telemetry, what is State Beta's underlying motivation?
        </p>

        <div class="choices-stack">
          <button class="choice-btn attribution-btn" data-choice="FEAR">
            <div class="choice-title">[1] Fear-Driven (Security Dilemma / Spiral Model)</div>
            <div class="choice-desc">Beta acts out of vulnerability and seeks survival, but misperceives our signals as offensive threats.</div>
          </button>
          <button class="choice-btn attribution-btn" data-choice="REVISIONIST">
            <div class="choice-title">[2] Revisionist / Opportunistic (Deterrence Model)</div>
            <div class="choice-desc">Beta seeks tactical advantage or territorial expansion, viewing unfortified restraint as weakness.</div>
          </button>
        </div>
        <div id="attributionFeedbackZone"></div>
      </div>
    `;

    panel.querySelectorAll('.attribution-btn').forEach(btn => {
      btn.onclick = () => this.submitAttribution(btn.dataset.choice);
    });
  }

  submitAttribution(playerAttribution) {
    audioEngine.playMechanicalClick();
    const evalRes = this.state.evaluateAttribution(playerAttribution);

    if (evalRes.isCorrect) {
      audioEngine.playChimeCooperation();
    } else {
      audioEngine.playAlarmKlaxon();
    }

    const zone = document.getElementById('attributionFeedbackZone');
    if (zone) {
      zone.innerHTML = `
        <div class="feedback-block ${evalRes.isCorrect ? 'outcome-success' : 'outcome-partial'}" style="margin-top:10px;">
          <div class="fb-label">${evalRes.isCorrect ? 'ACCURATE ATTRIBUTION' : 'ATTRIBUTION MISPERCEPTION'}</div>
          <div class="fb-text">${evalRes.explanation}</div>
          <button class="lab-btn lab-btn-primary" id="btnNextRound" style="margin-top:12px;">
            ${this.state.round < 5 ? `ADVANCE TO ROUND ${this.state.round + 1}` : 'PROCEED TO CONCEPT MASTERY CHECK'}
          </button>
        </div>
      `;

      document.getElementById('btnNextRound').onclick = () => {
        audioEngine.playMechanicalClick();
        if (this.state.round < 5) {
          this.state.round++;
          this.startPredictPhase();
        } else {
          this.startMasteryCheck();
        }
      };
    }
  }

  startMasteryCheck() {
    this.state.phase = 'MASTERY';
    this.updateReadinessDisplays();
    const q = MASTERY_CHECKS[this.state.masteryIndex];
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    this.bannerText.setText(`CONCEPT MASTERY CHECK: Item ${this.state.masteryIndex + 1} of 3.`);

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 5 / 7 · CONCEPT MASTERY CHECK (${this.state.masteryIndex + 1} / 3)</div>
        <h2 class="phase-title">Security Dilemma Classification</h2>
        <p class="phase-desc">Evaluate the tactical deployment using Robert Jervis\'s core security dilemma models:</p>

        <div class="prompt-box">
          <div class="prompt-question">${q.question}</div>
          <div class="choices-stack">
            ${q.choices.map((c, i) => `
              <button class="choice-btn mastery-btn" data-id="${c.id}">
                <span class="choice-num">[${i + 1}]</span>
                <span class="choice-text">${c.text}</span>
              </button>
            `).join('')}
          </div>
        </div>
        <div id="masteryFeedbackZone"></div>
      </div>
    `;

    panel.querySelectorAll('.mastery-btn').forEach(btn => {
      btn.onclick = () => this.submitMastery(btn.dataset.id);
    });
  }

  submitMastery(choiceId) {
    audioEngine.playMechanicalClick();
    const res = this.state.answerMastery(choiceId);
    if (!res) return;

    if (res.isCorrect) {
      audioEngine.playChimeCooperation();
    } else {
      audioEngine.playAlarmKlaxon();
    }

    const zone = document.getElementById('masteryFeedbackZone');
    if (zone) {
      zone.innerHTML = `
        <div class="feedback-block ${res.isCorrect ? 'outcome-success' : 'outcome-failure'}">
          <div class="fb-label">${res.isCorrect ? 'CORRECT CLASSIFICATION' : 'INCORRECT CLASSIFICATION'}</div>
          <div class="fb-text">${res.explanation}</div>
          <button class="lab-btn lab-btn-primary" id="btnNextMastery" style="margin-top:12px;">
            ${res.nextIndex < MASTERY_CHECKS.length ? 'NEXT QUESTION' : 'ADVANCE TO TRANSFER CASE'}
          </button>
        </div>
      `;
      document.getElementById('btnNextMastery').onclick = () => {
        if (res.nextIndex < MASTERY_CHECKS.length) {
          this.startMasteryCheck();
        } else {
          this.startTransferPhase();
        }
      };
    }
  }

  startTransferPhase() {
    this.state.phase = 'TRANSFER';
    this.updateReadinessDisplays();
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    this.bannerText.setText('TRANSFER SCENARIO: India–Pakistan 1998–2002 Nuclear Crisis Stability.');

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 6 / 7 · CROSS-CASE TRANSFER EVALUATION</div>
        <h2 class="phase-title">${TRANSFER_SCENARIO.title}</h2>
        <div class="callout-box">
          <div class="callout-heading">HISTORICAL CONTEXT</div>
          <p class="phase-desc" style="margin:0;">${TRANSFER_SCENARIO.historicalContext}</p>
        </div>

        <div class="prompt-box">
          <div class="prompt-question">${TRANSFER_SCENARIO.question}</div>
          <div class="choices-stack">
            ${TRANSFER_SCENARIO.choices.map((c, i) => `
              <button class="choice-btn transfer-btn" data-id="${c.id}">
                <span class="choice-num">[${i + 1}]</span>
                <span class="choice-text">${c.text}</span>
              </button>
            `).join('')}
          </div>
        </div>
        <div id="transferFeedbackZone"></div>
      </div>
    `;

    panel.querySelectorAll('.transfer-btn').forEach(btn => {
      btn.onclick = () => this.submitTransfer(btn.dataset.id);
    });
  }

  submitTransfer(choiceId) {
    audioEngine.playMechanicalClick();
    const res = this.state.answerTransfer(choiceId);
    if (!res) return;

    if (res.isCorrect) {
      audioEngine.playChimeCooperation();
    } else {
      audioEngine.playAlarmKlaxon();
    }

    const zone = document.getElementById('transferFeedbackZone');
    if (zone) {
      zone.innerHTML = `
        <div class="feedback-block ${res.isCorrect ? 'outcome-success' : 'outcome-failure'}">
          <div class="fb-label">${res.isCorrect ? 'TRANSFER DEMONSTRATED' : 'TRANSFER GAP DETECTED'}</div>
          <div class="fb-text">${res.explanation}</div>
          <div class="citation-text" style="margin-top:6px;">${res.citation}</div>
          <button class="lab-btn lab-btn-primary" id="btnGoDebrief" style="margin-top:12px;">
            GENERATE FULL SPIRAL WATCH DEBRIEF
          </button>
        </div>
      `;
      document.getElementById('btnGoDebrief').onclick = () => {
        audioEngine.playMechanicalClick();
        this.renderDebriefPhase();
      };
    }
  }

  renderDebriefPhase() {
    this.state.phase = 'DEBRIEF';
    this.updateReadinessDisplays();
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    const report = this.state.getReport();
    renderDebrief(panel, report);

    const restartBox = document.createElement('div');
    restartBox.style.marginTop = '16px';
    restartBox.style.textAlign = 'center';
    restartBox.innerHTML = `
      <button class="lab-btn lab-btn-secondary" id="btnRestartLab">RESTART SPIRAL WATCH</button>
    `;
    panel.appendChild(restartBox);

    document.getElementById('btnRestartLab').onclick = () => {
      audioEngine.playMechanicalClick();
      this.state.reset();
      this.triggerSignatureSweep();
      this.renderBriefing();
    };
  }
}
