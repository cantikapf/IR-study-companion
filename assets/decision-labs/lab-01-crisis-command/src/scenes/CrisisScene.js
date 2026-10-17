import {
  CRISIS_ACTS,
  CrisisState,
  MASTERY_CHECKS,
  TRANSFER_SCENARIO,
  ALLISON_MATRIX
} from '../CrisisConfig.js';
import { audioEngine } from '../../../shared/core/AudioEngine.js';
import { renderDebrief } from '../../../shared/learn/DebriefPanel.js';
import { OnboardingModal } from '../../../shared/learn/OnboardingModal.js';

export class CrisisScene extends Phaser.Scene {
  constructor() {
    super('CrisisScene');
    this.state = new CrisisState();
    this.sweepX = 0;
    this.sweepActive = true;
    this.sweepTimer = 0;
  }

  preload() {
    this.load.image('chamber_bg', '../assets/bg/chamber.png');
    this.load.image('table_wide', '../assets/sprites/table_wide.png');
    this.load.spritesheet('envoy', '../assets/sprites/diplomat_envoy.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('rival', '../assets/sprites/diplomat_rival.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('spark', '../assets/fx/spark.png', { frameWidth: 32, frameHeight: 32 });
    this.load.spritesheet('pips', '../assets/ui/pips.png', { frameWidth: 16, frameHeight: 16 });
  }

  create() {
    // 1. Situation Room Backdrop
    this.bg = this.add.image(512, 300, 'chamber_bg').setDisplaySize(1024, 600);

    // 2. Backlit Acetate Situation Table
    this.table = this.add.image(512, 420, 'table_wide').setScale(3.3);

    // Illuminated Acetate Map Lightbox
    this.mapFelt = this.add.rectangle(512, 350, 680, 72, 0x071510, 0.95)
      .setStrokeStyle(2, 0x166534);

    // Phosphor Grid on the Lightbox
    this.grid = this.add.grid(512, 350, 670, 66, 24, 12, 0x000000, 0, 0x166534, 0.5);

    // Cuba Landmass Representation & Key Nav Points
    this.add.ellipse(450, 354, 90, 18, 0x14532d, 0.8).setStrokeStyle(1, 0x22c55e);
    this.add.text(450, 354, 'CUBA [SAN CRISTÓBAL]', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '10px',
      color: '#e7f5ec'
    }).setOrigin(0.5);

    // Florida / Key West coastline indicator
    this.add.ellipse(390, 326, 60, 12, 0x0f2d1e, 0.7);
    this.add.text(390, 326, 'FLORIDA STRAIT', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '8px',
      color: '#86efac'
    }).setOrigin(0.5);

    // Dynamic Grease-Pencil Annotation Graphics Layer
    this.pencilGfx = this.add.graphics();

    // 3. Situation Room Participants (Avatars)
    // Left: JFK (Executive Command)
    this.jfk = this.add.sprite(280, 275, 'envoy', 0).setScale(3.8);
    this.add.text(280, 335, 'PRES. KENNEDY', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '11px',
      color: '#86efac',
      backgroundColor: '#0a1610',
      padding: { x: 4, y: 2 }
    }).setOrigin(0.5);

    // Center-Right: Gen. Curtis LeMay (Model II SOP Voice)
    this.lemay = this.add.sprite(690, 275, 'rival', 0).setScale(3.8);
    this.add.text(690, 335, 'GEN. LEMAY (JCS)', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '11px',
      color: '#fca5a5',
      backgroundColor: '#1c0a0a',
      padding: { x: 4, y: 2 }
    }).setOrigin(0.5);

    // Center-Left: SecDef McNamara (Model I Strategic Calculus)
    this.mcnamara = this.add.sprite(440, 265, 'envoy', 4).setScale(3.2).setAlpha(0.9);
    this.add.text(440, 318, 'SECDEF MCNAMARA', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '9px',
      color: '#93c5fd',
      backgroundColor: '#081426',
      padding: { x: 3, y: 1 }
    }).setOrigin(0.5);

    // Right: Robert F. Kennedy (Model III Cabinet Bargaining)
    this.rfk = this.add.sprite(780, 275, 'rival', 4).setScale(3.2).setAlpha(0.9);
    this.add.text(780, 335, 'RFK (ATTORNEY GEN)', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '9px',
      color: '#fde047',
      backgroundColor: '#1f1b07',
      padding: { x: 3, y: 1 }
    }).setOrigin(0.5);

    // 4. In-Scene Advisor Callout Banner
    this.advisorBanner = this.add.container(512, 420);
    const bannerBg = this.add.rectangle(0, 0, 720, 36, 0x0b1712, 0.92)
      .setStrokeStyle(1, 0x22c55e);
    this.advisorBannerText = this.add.text(0, 0, 'EXCOMM CONVENED: Standing by for presidential strategic authorization...', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '12px',
      color: '#e7f5ec'
    }).setOrigin(0.5);
    this.advisorBanner.add([bannerBg, this.advisorBannerText]);

    // 5. DEFCON Nixie Tube Panel (Top Right)
    this.defconPanel = this.add.container(910, 60);
    const defconBg = this.add.rectangle(0, 0, 150, 70, 0x0b1712, 0.95)
      .setStrokeStyle(2, 0x22c55e);
    const defconTitle = this.add.text(0, -20, 'READINESS STATUS', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '10px',
      color: '#86efac'
    }).setOrigin(0.5);
    this.defconValue = this.add.text(0, 8, 'DEFCON 3', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '26px',
      fontStyle: 'bold',
      color: '#f59e0b'
    }).setOrigin(0.5);
    this.defconPanel.add([defconBg, defconTitle, this.defconValue]);

    // 6. SAC Strategic Alert Lamps
    this.alertLamps = [];
    const lampX = 40;
    for (let i = 0; i < 4; i++) {
      const c = this.add.circle(lampX + i * 22, 60, 6, i < 2 ? 0x22c55e : 0x166534);
      this.alertLamps.push(c);
    }
    this.add.text(lampX, 38, 'SAC ALERT ARRAY', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '9px',
      color: '#86efac'
    });

    // 7. Signature Moment: Phosphor sweep line across situation table
    this.sweepGfx = this.add.graphics();
    this.triggerSignatureSweep();

    // 8. Bind DOM & Start
    this.bindDOM();
    this.initOnboarding();
    this.renderBriefing();
  }

  triggerSignatureSweep() {
    this.sweepX = 172;
    this.sweepActive = true;
    this.sweepTimer = 0;

    // Teletype audio sequence
    audioEngine.init();
    audioEngine.playMechanicalClick();
    this.time.delayedCall(160, () => audioEngine.playMechanicalClick());
    this.time.delayedCall(320, () => audioEngine.playMechanicalClick());
    this.time.delayedCall(480, () => audioEngine.playMechanicalClick());
  }

  update(time, delta) {
    if (this.sweepActive) {
      this.sweepTimer += delta;
      this.sweepX += (680 / 1800) * delta;
      this.sweepGfx.clear();

      if (this.sweepX < 852) {
        // Bright phosphor vertical line with gradient trail
        this.sweepGfx.lineStyle(2, 0x22c55e, 0.95);
        this.sweepGfx.lineBetween(this.sweepX, 314, this.sweepX, 386);

        this.sweepGfx.fillStyle(0x22c55e, 0.18);
        this.sweepGfx.fillRect(Math.max(172, this.sweepX - 40), 314, 40, 72);
      } else {
        this.sweepActive = false;
        this.sweepGfx.clear();
      }
    }
  }

  drawMapAnnotations() {
    this.pencilGfx.clear();

    this.state.greasePencilArcs.forEach((item, idx) => {
      if (item.type === 'arc') {
        // Quarantine naval perimeter arc
        this.pencilGfx.lineStyle(3, 0x38bdf8, 0.85);
        this.pencilGfx.strokeCircle(520, 350, 80 + idx * 12);
        this.pencilGfx.lineStyle(1, 0x38bdf8, 0.4);
        this.pencilGfx.strokeCircle(520, 350, 95 + idx * 12);
      } else if (item.type === 'crosshair') {
        // Air strike target markers
        this.pencilGfx.lineStyle(2, 0xf43f5e, 0.9);
        this.pencilGfx.strokeCircle(450, 354, 18);
        this.pencilGfx.lineBetween(425, 354, 475, 354);
        this.pencilGfx.lineBetween(450, 335, 450, 373);
      } else if (item.type === 'vector') {
        // Backchannel dispatch vector
        this.pencilGfx.lineStyle(2, 0xf59e0b, 0.9);
        this.pencilGfx.lineBetween(320, 350, 680, 350);
        this.pencilGfx.strokeCircle(680, 350, 6);
      }
    });
  }

  updateReadinessDisplays() {
    const d = this.state.defcon;
    const s = this.state.stability;

    this.defconValue.setText(`DEFCON ${d}`);
    if (d === 4) {
      this.defconValue.setColor('#22c55e');
    } else if (d === 3) {
      this.defconValue.setColor('#f59e0b');
    } else if (d === 2) {
      this.defconValue.setColor('#ea580c');
    } else {
      this.defconValue.setColor('#ef4444');
    }

    // Alert lamps reflect stability
    this.alertLamps.forEach((lamp, idx) => {
      const active = (s >= (100 - idx * 25));
      lamp.setFillStyle(active ? 0x22c55e : 0xef4444);
    });

    const statusEl = document.getElementById('railStatusStrip');
    if (statusEl) {
      statusEl.innerHTML = `
        <div class="rail-stat"><span class="stat-lbl">DEFCON:</span> <span class="stat-val defcon-val">${d}</span></div>
        <div class="rail-stat"><span class="stat-lbl">STABILITY:</span> <span class="stat-val">${s}%</span></div>
        <div class="rail-stat"><span class="stat-lbl">PHASE:</span> <span class="stat-val">${this.state.phase}</span></div>
      `;
    }
  }

  initOnboarding() {
    this.onboarding = new OnboardingModal({
      labId: 'lab-01',
      role: 'Presidential National Security Advisor · ExComm Director',
      objective: 'Deconflict military Standard Operating Procedures (Model II) and cabinet political infighting (Model III) to resolve the Cuban Missile Crisis without triggering nuclear escalation.',
      steps: [
        {
          step: '1',
          title: 'FORMULATE HYPOTHESIS (PREDICT)',
          desc: 'Before reading tactical options, commit to how Soviet or US bureaucratic organs will react under crisis conditions.'
        },
        {
          step: '2',
          title: 'DECONFLICT & AUTHORIZE (DECIDE)',
          desc: 'Listen to ExComm advisors (General LeMay, SecDef McNamara, RFK) and choose your strategic directive using Keys [1, 2, 3].'
        },
        {
          step: '3',
          title: 'AUDIT & MASTER ALLISON LENSES',
          desc: 'Analyze causal consequences via Model I, II, and III lenses, correct academic misconceptions, and solve a historical transfer case.'
        }
      ],
      controls: [
        { key: 'KEYS 1, 2, 3', label: 'Select tactical options & answers' },
        { key: 'SPACEBAR', label: 'Advance dialog & confirm choices' },
        { key: 'TAB', label: 'Toggle operational side rail' },
        { key: 'KEY M', label: 'Toggle sound synthesizer' }
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

  bindDOM() {
    // Rail toggle
    const btnToggleRail = document.getElementById('btnToggleRail');
    const sideRail = document.getElementById('sideRail');
    if (btnToggleRail && sideRail) {
      btnToggleRail.onclick = () => {
        sideRail.classList.toggle('collapsed');
      };
    }

    // Audio mute toggle
    const btnAudio = document.getElementById('btnAudioToggle');
    if (btnAudio) {
      btnAudio.onclick = () => {
        const muted = audioEngine.toggleMute();
        btnAudio.innerText = muted ? 'AUDIO: OFF' : 'AUDIO: ON';
      };
    }

    // Keyboard controls
    this.input.keyboard.on('keydown-ONE', () => this.handleKeyChoice(0));
    this.input.keyboard.on('keydown-TWO', () => this.handleKeyChoice(1));
    this.input.keyboard.on('keydown-THREE', () => this.handleKeyChoice(2));
    this.input.keyboard.on('keydown-SPACE', () => this.handleSpaceKey());
    this.input.keyboard.on('keydown-M', () => { if (btnAudio) btnAudio.click(); });
    this.input.keyboard.on('keydown-TAB', (e) => {
      e.preventDefault();
      if (btnToggleRail) btnToggleRail.click();
    });
  }

  handleKeyChoice(index) {
    if (this.state.phase === 'PREDICT') {
      const actData = CRISIS_ACTS[this.state.act - 1];
      if (actData && actData.predictionOptions[index]) {
        this.submitPrediction(actData.predictionOptions[index].id);
      }
    } else if (this.state.phase === 'DECIDE') {
      const actData = CRISIS_ACTS[this.actIndex() - 1];
      if (actData && actData.options[index]) {
        this.submitDecision(actData.options[index].id);
      }
    } else if (this.state.phase === 'MASTERY') {
      const q = MASTERY_CHECKS[this.state.masteryIndex];
      if (q && q.choices[index]) {
        this.submitMastery(q.choices[index].id);
      }
    } else if (this.state.phase === 'TRANSFER') {
      if (!this.state.transferAnswered && TRANSFER_SCENARIO.choices[index]) {
        this.submitTransfer(TRANSFER_SCENARIO.choices[index].id);
      }
    }
  }

  handleSpaceKey() {
    const btnNext = document.getElementById('btnPhaseAdvance');
    if (btnNext) btnNext.click();
  }

  actIndex() {
    return this.state.act;
  }

  appendLog(msg, tag = 'EXCOMM') {
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
        <div class="phase-badge">PHASE 1 / 7 · STRATEGIC BRIEFING</div>
        <h2 class="phase-title">Operation Thirteen Days: ExComm</h2>
        <p class="phase-desc">
          October 16, 1962. Medium-range Soviet ballistic missiles have been discovered in Cuba.
          You preside over the Executive Committee of the National Security Council (ExComm).
        </p>

        <div class="callout-box">
          <div class="callout-heading">CURRICULUM OBJECTIVES</div>
          <ul class="learning-objectives-list">
            <li><strong>Model I (Rational Actor):</strong> Evaluate strategic utility, value-maximizing choices, and calibrated signaling.</li>
            <li><strong>Model II (Organizational Routine):</strong> Unpack how rigid military Standard Operating Procedures (SOPs) constrain policy.</li>
            <li><strong>Model III (Bureaucratic Politics):</strong> Trace how cabinet pulling and hauling ("where you stand depends on where you sit") shapes outcomes.</li>
          </ul>
        </div>

        <button class="lab-btn lab-btn-primary" id="btnPhaseAdvance">
          CONVENE EXCOMM [START ACT 1]
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
    const actData = CRISIS_ACTS[this.state.act - 1];
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    this.advisorBannerText.setText(`ACT ${this.state.act}: ${actData.title.toUpperCase()} · Formulate strategic prediction.`);
    this.appendLog(`Act ${this.state.act} initiated: ${actData.brief}`, 'INTEL');

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 2 / 7 · HYPOTHESIS &amp; PREDICTION</div>
        <h2 class="phase-title">${actData.title}</h2>
        <div class="historical-date">${actData.date}</div>
        <p class="phase-desc">${actData.brief}</p>

        <div class="sigint-banner">
          <span class="sigint-tag">SATELLITE INTEL:</span> ${actData.sigint}
        </div>

        <div class="prompt-box">
          <div class="prompt-question">${actData.predictionQuestion}</div>
          <div class="choices-stack">
            ${actData.predictionOptions.map((opt, i) => `
              <button class="choice-btn" data-id="${opt.id}">
                <span class="choice-num">[${i + 1}]</span>
                <span class="choice-text">${opt.text}</span>
              </button>
            `).join('')}
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
    this.appendLog(`Player recorded hypothesis: [${predictionId}]`, 'ANALYSIS');
    this.startDecidePhase();
  }

  startDecidePhase() {
    this.state.phase = 'DECIDE';
    this.updateReadinessDisplays();
    const actData = CRISIS_ACTS[this.state.act - 1];
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    // Update character avatars and show advisor voices
    this.jfk.setTexture('envoy', 4);
    this.lemay.setTexture('rival', 0);

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 3 / 7 · EXCOMM DELIBERATION</div>
        <h2 class="phase-title">Executive Directive: Act ${this.state.act}</h2>

        <div class="advisors-grid">
          ${actData.advisors.map(adv => `
            <div class="advisor-item">
              <div class="advisor-name">${adv.name}</div>
              <div class="advisor-lens">${adv.lens}</div>
              <div class="advisor-quote">"${adv.quote}"</div>
            </div>
          `).join('')}
        </div>

        <div class="prompt-box">
          <div class="prompt-question">Select your course of action as President:</div>
          <div class="choices-stack">
            ${actData.options.map((opt, i) => `
              <button class="choice-btn decision-btn" data-id="${opt.id}">
                <div class="choice-top">
                  <span class="choice-num">[${i + 1}]</span>
                  <span class="choice-title">${opt.title}</span>
                  <span class="choice-tag">${opt.lensShort}</span>
                </div>
                <div class="choice-desc">${opt.desc}</div>
              </button>
            `).join('')}
          </div>
        </div>
      </div>
    `;

    panel.querySelectorAll('.decision-btn').forEach(btn => {
      btn.onclick = () => this.submitDecision(btn.dataset.id);
    });
  }

  submitDecision(optionId) {
    audioEngine.init();
    audioEngine.playMechanicalClick();

    const actData = CRISIS_ACTS[this.state.act - 1];
    const opt = actData.options.find(o => o.id === optionId);
    const feedback = this.state.applyDecision(optionId);

    this.drawMapAnnotations();
    this.updateReadinessDisplays();

    // Visual & audio reaction
    if (feedback.outcome === 'success') {
      audioEngine.playChimeCooperation();
      this.jfk.setTexture('envoy', 5);
      this.advisorBannerText.setText(opt.advisorReaction);
      this.appendLog(`Order issued: ${opt.title} [SUCCESS]`, 'DECISION');
    } else if (feedback.outcome === 'partial') {
      this.jfk.setTexture('envoy', 4);
      this.advisorBannerText.setText(opt.advisorReaction);
      this.appendLog(`Order issued: ${opt.title} [COMPROMISE FRICTION]`, 'DECISION');
    } else {
      audioEngine.playBetrayalBoom();
      this.cameras.main.shake(200, 0.012);
      this.jfk.setTexture('envoy', 7);
      this.lemay.setTexture('rival', 6);
      this.advisorBannerText.setText(opt.advisorReaction);
      this.appendLog(`Order issued: ${opt.title} [ESCALATION WARNING]`, 'DECISION');
    }

    this.renderConsequenceAndExplain(feedback);
  }

  renderConsequenceAndExplain(feedback) {
    this.state.phase = 'EXPLAIN';
    this.updateReadinessDisplays();
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    const matchBadge = feedback.predictionMatch
      ? '<span class="match-badge match-yes">HYPOTHESIS CONFIRMED</span>'
      : '<span class="match-badge match-no">HYPOTHESIS REFUTED</span>';

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 4 / 7 · CONSEQUENCE &amp; EXPLANATION</div>
        <div class="outcome-header outcome-${feedback.outcome}">
          OUTCOME: ${feedback.outcome.toUpperCase()} · ${matchBadge}
        </div>

        <div class="feedback-block">
          <div class="feedback-row">
            <span class="fb-label">SYSTEMIC CONSEQUENCE:</span>
            <span class="fb-text">${feedback.consequence}</span>
          </div>

          <div class="feedback-row">
            <span class="fb-label">IR MECHANISM:</span>
            <span class="fb-text">${feedback.mechanism}</span>
          </div>

          <div class="feedback-row">
            <span class="fb-label">ACADEMIC CITATION:</span>
            <span class="fb-text citation-text">${feedback.citation}</span>
          </div>

          ${feedback.misconception ? `
            <div class="misconception-card">
              <div class="misc-tag">MISCONCEPTION IDENTIFIED: ${feedback.misconception.label}</div>
              <div class="misc-remediation">${feedback.misconception.remediation}</div>
            </div>
          ` : ''}
        </div>

        <button class="lab-btn lab-btn-primary" id="btnPhaseAdvance">
          ${this.state.act < 3 ? `ADVANCE TO ACT ${this.state.act + 1}` : 'PROCEED TO CONCEPT MASTERY CHECK'}
        </button>
      </div>
    `;

    document.getElementById('btnPhaseAdvance').onclick = () => {
      audioEngine.playMechanicalClick();
      if (this.state.act < 3) {
        this.state.act++;
        this.startPredictPhase();
      } else {
        this.startMasteryCheck();
      }
    };
  }

  startMasteryCheck() {
    this.state.phase = 'MASTERY';
    this.updateReadinessDisplays();
    const q = MASTERY_CHECKS[this.state.masteryIndex];
    const panel = document.getElementById('phaseContent');
    if (!panel) return;

    this.advisorBannerText.setText(`CONCEPT MASTERY EVALUATION: Item ${this.state.masteryIndex + 1} of 3.`);

    panel.innerHTML = `
      <div class="phase-card">
        <div class="phase-badge">PHASE 5 / 7 · CONCEPT MASTERY CHECK (${this.state.masteryIndex + 1} / 3)</div>
        <h2 class="phase-title">Analytical Classification</h2>
        <p class="phase-desc">Evaluate the following crisis scenario through Graham Allison\'s FPA framework:</p>

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

    this.advisorBannerText.setText('TRANSFER SCENARIO: Applying Allison Models to 1914 July Crisis.');

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
            GENERATE FULL EXCOMM DEBRIEF &amp; ALLISON MATRIX
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

    // Render shared DebriefPanel component
    renderDebrief(panel, report);

    // Append Allison Comparative Matrix
    const matrixEl = document.createElement('div');
    matrixEl.className = 'allison-matrix-container';
    matrixEl.innerHTML = `
      <div class="matrix-heading">GRAHAM ALLISON'S THREE MODELS: COMPARATIVE LENS MATRIX</div>
      <table class="allison-matrix-table">
        <thead>
          <tr>
            <th>Analytical Model</th>
            <th>Primary Focus</th>
            <th>1962 Thirteen Days Lens</th>
            <th>Core Analytical Insight</th>
          </tr>
        </thead>
        <tbody>
          ${ALLISON_MATRIX.map(row => `
            <tr>
              <td class="matrix-model-name">${row.model}</td>
              <td>${row.focus}</td>
              <td>${row.perspective1962}</td>
              <td class="matrix-insight">${row.coreInsight}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
      <div style="margin-top:16px; text-align:center;">
        <button class="lab-btn lab-btn-secondary" id="btnRestartGame">RESTART LAB</button>
      </div>
    `;

    panel.appendChild(matrixEl);

    document.getElementById('btnRestartGame').onclick = () => {
      audioEngine.playMechanicalClick();
      this.state.reset();
      this.pencilGfx.clear();
      this.triggerSignatureSweep();
      this.renderBriefing();
    };
  }
}
