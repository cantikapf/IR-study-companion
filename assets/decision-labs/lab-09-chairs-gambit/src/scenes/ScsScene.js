import { SCS_CONFIG, SCS_OBJECTIVES, SCS_ROUNDS, SCS_MASTERY_CHECKS, SCS_TRANSFER, ScsState } from '../ScsConfig.js';
import { audioEngine } from '../../../shared/core/AudioEngine.js';
import { LearningSession } from '../../../shared/learn/LearningSession.js';
import { DebriefPanel } from '../../../shared/learn/DebriefPanel.js';
import { OnboardingModal } from '../../../shared/learn/OnboardingModal.js';

export class ScsScene extends Phaser.Scene {
  constructor() {
    super('ScsScene');
    this.state = new ScsState();
    this.session = new LearningSession('lab-09', SCS_OBJECTIVES);
    this.pendingPrediction = null;
    this.masteryIndex = 0;
  }

  preload() {
    this.load.image('chamber_bg', '../assets/bg/chamber.png');
    this.load.image('table_wide', '../assets/sprites/table_wide.png');
    this.load.spritesheet('envoy', '../assets/sprites/diplomat_envoy.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('rival', '../assets/sprites/diplomat_rival.png', { frameWidth: 32, frameHeight: 48 });
  }

  create() {
    const W = 820;
    const H = 520;

    // Tropical Roundtable Plenary Backdrop: Teak, Rattan & Saffron/Indigo hints
    this.add.rectangle(W / 2, H / 2, W, H, 0x071318);

    // Warm Plenary Table Mat & Teak Wood Surface
    this.tableMat = this.add.rectangle(W / 2, 280, 790, 240, 0x121e20, 0.95).setStrokeStyle(2, 0x854d0e);
    this.innerMat = this.add.rectangle(W / 2, 280, 760, 200, 0x0a1418, 0.85).setStrokeStyle(1, 0x854d0e, 0.3);

    // Chairman Dais & Gavel Sound Block (Center Stage)
    this.dais = this.add.rectangle(W / 2, 175, 170, 48, 0x1d140a, 0.9).setStrokeStyle(2, 0xeab308);
    this.gavelBlock = this.add.rectangle(W / 2, 175, 50, 22, 0x451a03).setStrokeStyle(1.5, 0xd97706);
    this.gavelHead = this.add.rectangle(W / 2, 160, 30, 13, 0x78350f).setStrokeStyle(1, 0xfbbf24);
    this.gavelHandle = this.add.rectangle(W / 2 + 16, 160, 22, 5, 0x92400e);

    this.chairLabel = this.add.text(W / 2, 191, 'ASEAN SUMMIT CHAIR', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#eab308'
    }).setOrigin(0.5);

    // 4 Faction Delegation Monitors across Top Plenary
    this.factionMonitors = {};
    const factionConfigs = [
      { key: 'claimants', label: 'CLAIMANTS (VN/PH)', x: 106, color: 0x38bdf8, spriteKey: 'envoy' },
      { key: 'nonClaimants', label: 'NON-CLAIMANTS (KH/LA)', x: 309, color: 0x10b981, spriteKey: 'envoy' },
      { key: 'china', label: 'CHINA DELEGATION', x: 511, color: 0xf43f5e, spriteKey: 'rival' },
      { key: 'partners', label: 'PARTNERS (US/JP)', x: 714, color: 0xeab308, spriteKey: 'envoy' }
    ];

    factionConfigs.forEach(fc => {
      const card = this.add.rectangle(fc.x, 82, 192, 114, 0x09141a, 0.95).setStrokeStyle(1.5, 0x1e293b);
      const sprite = this.add.sprite(fc.x - 62, 80, fc.spriteKey, 0).setScale(1.9);
      
      const title = this.add.text(fc.x + 18, 38, fc.label, {
        fontFamily: '"Chakra Petch", sans-serif',
        fontSize: '11px',
        fontStyle: 'bold',
        color: '#ffffff'
      }).setOrigin(0.5, 0);

      const barBg = this.add.rectangle(fc.x + 18, 76, 92, 11, 0x0f1d24).setStrokeStyle(1, 0x1e293b);
      const barFill = this.add.rectangle(fc.x - 28, 76, 46, 11, fc.color).setOrigin(0, 0.5);
      
      const sentText = this.add.text(fc.x + 18, 100, 'SENTIMENT: 50%', {
        fontFamily: '"Chakra Petch", sans-serif',
        fontSize: '11px',
        fontStyle: 'bold',
        color: '#e2e8f0'
      }).setOrigin(0.5);

      const statusTag = this.add.text(fc.x + 18, 120, 'STATE: ALIGNED', {
        fontFamily: '"Chakra Petch", sans-serif',
        fontSize: '10px',
        fontStyle: 'bold',
        color: '#10b981'
      }).setOrigin(0.5);

      this.factionMonitors[fc.key] = {
        card, sprite, barFill, sentText, statusTag, color: fc.color
      };
    });

    // Top Telemetry Header
    this.add.rectangle(W / 2, 14, W, 28, 0x040b0e, 0.95).setStrokeStyle(1, 0x854d0e, 0.5);
    this.telRoundText = this.add.text(14, 7, 'ROUND 1 / 3: GEOGRAPHIC SCOPE', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#eab308'
    });

    this.telAgreementText = this.add.text(806, 7, 'COMMUNIQUE SUBSTANCE: 20%', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#10b981'
    }).setOrigin(1, 0);

    // Live Communiqué Draft Board on Stage (Bottom Half)
    this.draftBoard = this.add.rectangle(W / 2, 355, 780, 145, 0x060f14, 0.94).setStrokeStyle(1.5, 0x854d0e);
    this.draftHeader = this.add.text(W / 2, 296, 'LIVE COMMUNIQUE DRAFT · CODE OF CONDUCT ON THE SOUTH CHINA SEA', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#eab308'
    }).setOrigin(0.5);

    this.clause1Text = this.add.text(35, 325, 'Clause 1: Scope: [PENDING] Standing by for geographic scope clause...', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      color: '#cbd5e1'
    });

    this.clause2Text = this.add.text(35, 365, 'Clause 2: Disputes: [PENDING] Standing by for dispute settlement clause...', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      color: '#cbd5e1'
    });

    this.clause3Text = this.add.text(35, 405, 'Clause 3: Exercises: [PENDING] Standing by for naval exercises clause...', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      color: '#cbd5e1'
    });

    // Collapse Warning Banner
    this.collapseBanner = this.add.rectangle(W / 2, 235, 680, 32, 0xe11d48, 0.95).setVisible(false);
    this.collapseText = this.add.text(W / 2, 235, 'SUMMIT DEADLOCK: FACTION WALKOUT BREACHED 25% CONSENSUS TOLERANCE!', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#ffffff'
    }).setOrigin(0.5).setVisible(false);

    // Ceiling Fan Shadow Overlay for Tropical Atmosphere
    this.createCeilingFanShadow();

    // Trigger Signature Moment (Gavel Crack + Fan Shadow Sweep)
    this.triggerSignatureMoment();

    this.bindDOM();
    this.updateHUD();
    this.initOnboarding();
    this.startRound(1);
  }

  createCeilingFanShadow() {
    this.fanContainer = this.add.container(410, 260);
    const blade1 = this.add.rectangle(0, -120, 32, 150, 0x000000, 0.15);
    const blade2 = this.add.rectangle(0, 120, 32, 150, 0x000000, 0.15);
    const blade3 = this.add.rectangle(-120, 0, 150, 32, 0x000000, 0.15);
    const blade4 = this.add.rectangle(120, 0, 150, 32, 0x000000, 0.15);
    const hub = this.add.circle(0, 0, 28, 0x000000, 0.2);
    this.fanContainer.add([blade1, blade2, blade3, blade4, hub]);

    this.tweens.add({
      targets: this.fanContainer,
      angle: 360,
      duration: 12000,
      repeat: -1,
      ease: 'Linear'
    });
  }

  triggerSignatureMoment() {
    audioEngine.init();

    audioEngine.playMechanicalClick();
    this.tweens.add({
      targets: [this.gavelHead, this.gavelHandle],
      y: '+=8',
      yoyo: true,
      duration: 110,
      repeat: 1,
      onRepeat: () => {
        audioEngine.playMechanicalClick();
        this.cameras.main.shake(120, 0.008);
      }
    });

    const shockwave = this.add.circle(410, 175, 8, 0xeab308, 0.7);
    this.tweens.add({
      targets: shockwave,
      radius: 70,
      alpha: 0,
      duration: 650,
      ease: 'Cubic.easeOut',
      onComplete: () => shockwave.destroy()
    });

    this.tweens.add({
      targets: this.fanContainer,
      x: { from: 340, to: 410 },
      alpha: { from: 0.05, to: 0.16 },
      duration: 1600,
      ease: 'Sine.easeOut'
    });
  }

  bindDOM() {
    const btnRestart = document.getElementById('btnRestart');
    const muteBtn = document.getElementById('btnMuteToggle');

    if (btnRestart) {
      btnRestart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.hideModal('modalDebrief');
        this.state.reset();
        this.session = new LearningSession('lab-09', SCS_OBJECTIVES);
        this.masteryIndex = 0;
        this.startRound(1);
      };
    }

    if (muteBtn) {
      muteBtn.onclick = () => {
        const isMuted = audioEngine.toggleMute();
        muteBtn.innerText = isMuted ? 'AUDIO: MUTED' : 'AUDIO: ON';
      };
    }

    // Keyboard bindings
    this.input.keyboard.on('keydown-ONE', () => {
      if (this.onboarding && this.onboarding.isOpen) return;
      this.handleKeyNumber(0);
    });
    this.input.keyboard.on('keydown-TWO', () => {
      if (this.onboarding && this.onboarding.isOpen) return;
      this.handleKeyNumber(1);
    });
    this.input.keyboard.on('keydown-THREE', () => {
      if (this.onboarding && this.onboarding.isOpen) return;
      this.handleKeyNumber(2);
    });
    this.input.keyboard.on('keydown-M', () => {
      const isMuted = audioEngine.toggleMute();
      if (muteBtn) muteBtn.innerText = isMuted ? 'AUDIO: MUTED' : 'AUDIO: ON';
    });
    this.input.keyboard.on('keydown-SPACE', () => {
      if (this.onboarding && this.onboarding.isOpen) return;
      const mf = document.getElementById('modalFeedback');
      const md = document.getElementById('modalDebrief');
      if (mf && mf.classList.contains('active')) {
        const btnNext = document.getElementById('btnFeedbackNext');
        btnNext && btnNext.click();
      } else if (md && md.classList.contains('active')) {
        btnRestart && btnRestart.click();
      }
    });
  }

  initOnboarding() {
    this.onboarding = new OnboardingModal({
      labId: 'lab-09',
      role: 'ASEAN Summit Chair · Regional Peacemaker',
      objective: 'Sequence multilateral consultations and draft a consensus South China Sea Communiqué without triggering claimant or great-power walkouts.',
      steps: [
        {
          step: '1',
          title: 'PREDICT DIPLOMATIC ALIGNMENT',
          desc: 'Before taking a chairman initiative, commit to an analytical prediction of claimant sensitivity and Chinese resistance.'
        },
        {
          step: '2',
          title: 'SEQUENCE MULTILATERAL CONSULTATION',
          desc: 'Select Chair Actions [1-3] to draft consensus communiqué language while preserving ASEAN centrality and preventing walkouts.'
        },
        {
          step: '3',
          title: 'AUDIT & MASTER CONSENSUS NORMS',
          desc: 'Evaluate how UNCLOS citations, bilateral pressure, and the ASEAN Way shape outcomes, then resolve the mastery and transfer cases.'
        }
      ],
      controls: [
        { key: 'KEYS 1-3', label: 'Chair Actions [1-3]' },
        { key: 'SPACEBAR', label: 'Advance [SPACE]' },
        { key: 'KEY M', label: 'Toggle audio' },
        { key: 'ESC', label: 'Dismiss briefing' }
      ],
      onStart: () => {
        audioEngine.init();
        audioEngine.playMechanicalClick();
      }
    });

    const btnHowToPlay = document.getElementById('btnHowToPlay');
    if (btnHowToPlay) {
      btnHowToPlay.onclick = () => {
        audioEngine.playMechanicalClick();
        this.onboarding.open();
      };
    }

    // Auto-open on initial boot
    this.onboarding.open();
  }

  handleKeyNumber(index) {
    if (this.state.phase === 'PREDICTING') {
      const predBtns = document.querySelectorAll('.pred-opt-btn');
      if (predBtns[index]) predBtns[index].click();
    } else if (this.state.phase === 'DECIDING') {
      const decBtns = document.querySelectorAll('.scs-opt-btn');
      if (decBtns[index]) decBtns[index].click();
    } else if (this.state.phase === 'MASTERY') {
      const mcBtns = document.querySelectorAll('.mastery-opt-btn');
      if (mcBtns[index]) mcBtns[index].click();
    } else if (this.state.phase === 'TRANSFER') {
      const trBtns = document.querySelectorAll('.transfer-opt-btn');
      if (trBtns[index]) trBtns[index].click();
    }
  }

  startRound(roundNum) {
    this.state.round = roundNum;
    const roundData = SCS_ROUNDS[roundNum - 1];

    this.telRoundText.setText(`ROUND ${roundNum} / 3: ${roundData.topic.toUpperCase()}`);
    this.updateHUD();

    this.renderPredictPhase(roundData);
  }

  renderPredictPhase(roundData) {
    this.state.phase = 'PREDICTING';
    const railContainer = document.getElementById('sideRailContent');
    if (!railContainer) return;

    railContainer.innerHTML = `
      <div class="rail-phase-badge">[PHASE 1: PREDICT]</div>
      <h3 class="rail-round-title">${roundData.title}</h3>
      <p class="rail-round-brief">${roundData.brief}</p>
      
      <div class="rail-prompt-box">
        <strong>CHAIR HYPOTHESIS:</strong><br>
        ${roundData.predictPrompt}
      </div>

      <div class="rail-options-grid">
        ${roundData.predictions.map((p, idx) => `
          <button class="lab-button pred-opt-btn" data-pred-id="${p.id}" tabindex="0">
            <span class="btn-idx-tag">[KEY ${idx + 1}]</span>
            <span class="btn-label-text">${p.label}</span>
          </button>
        `).join('')}
      </div>
    `;

    const predBtns = railContainer.querySelectorAll('.pred-opt-btn');
    predBtns.forEach(btn => {
      btn.onclick = () => {
        const predId = btn.getAttribute('data-pred-id');
        this.pendingPrediction = predId;
        this.session.recordPrediction(`round-${this.state.round}`, predId);
        audioEngine.playMechanicalClick();
        this.renderDecidePhase(roundData);
      };
    });
  }

  renderDecidePhase(roundData) {
    this.state.phase = 'DECIDING';
    const railContainer = document.getElementById('sideRailContent');
    if (!railContainer) return;

    railContainer.innerHTML = `
      <div class="rail-phase-badge">[PHASE 2: DECIDE]</div>
      <h3 class="rail-round-title">${roundData.title}</h3>
      <div class="rail-hypothesis-tag">ACTIVE HYPOTHESIS: ${this.pendingPrediction.toUpperCase()}</div>
      <p class="rail-instruction-text">Select draft clause language to table before the ministers:</p>

      <div class="rail-options-grid">
        ${roundData.choices.map((c, idx) => `
          <button class="lab-button scs-opt-btn" data-choice-id="${c.id}" tabindex="0">
            <div class="btn-top-row">
              <span class="btn-idx-tag">[KEY ${idx + 1}]</span>
              <strong class="btn-choice-title">${c.title}</strong>
            </div>
            <p class="btn-choice-desc">${c.desc}</p>
            <div class="btn-shifts-row">
              <span class="shift-chip">VN/PH: ${c.shifts.claimants >= 0 ? '+' : ''}${c.shifts.claimants}%</span>
              <span class="shift-chip">KH/LA: ${c.shifts.nonClaimants >= 0 ? '+' : ''}${c.shifts.nonClaimants}%</span>
              <span class="shift-chip">CN: ${c.shifts.china >= 0 ? '+' : ''}${c.shifts.china}%</span>
              <span class="shift-chip">US/JP: ${c.shifts.partners >= 0 ? '+' : ''}${c.shifts.partners}%</span>
            </div>
          </button>
        `).join('')}
      </div>
    `;

    const choiceBtns = railContainer.querySelectorAll('.scs-opt-btn');
    choiceBtns.forEach((btn, idx) => {
      btn.onclick = () => {
        const choice = roundData.choices[idx];
        this.commitDecision(choice, roundData);
      };
    });
  }

  commitDecision(choice, roundData) {
    this.state.phase = 'CONSEQUENCE';
    this.state.applyChoice(choice);
    this.updateHUD();

    const decisionId = `round-${this.state.round}`;
    const isCorrect = (choice.outcome === 'success');
    const predMatched = (choice.predictedAlignment === this.pendingPrediction);
    const isCollapsed = this.state.isCollapsed();

    this.session.recordDecision({
      decisionId,
      choice: choice.id,
      correctChoice: roundData.choices.find(c => c.outcome === 'success')?.id || choice.id,
      rationale: choice.consequence,
      misconceptionTag: choice.misconception,
      predicted: this.pendingPrediction,
      actual: choice.predictedAlignment,
      outcome: isCollapsed ? 'failure' : choice.outcome,
      consequence: choice.consequence,
      mechanism: choice.mechanism,
      citation: choice.citation,
      objectiveIndex: choice.objectiveIndex
    });

    if (isCollapsed) {
      audioEngine.playBetrayalBoom();
      this.cameras.main.shake(350, 0.02);
      this.cameras.main.flash(200, 225, 29, 72);
      this.collapseBanner.setVisible(true);
      this.collapseText.setVisible(true);
    } else if (isCorrect) {
      audioEngine.playChimeCooperation();
    } else {
      audioEngine.playAlarmKlaxon();
    }

    this.showFeedbackModal({
      outcome: isCollapsed ? 'failure' : choice.outcome,
      consequence: isCollapsed ? 'CONSENSUS COLLAPSE! Faction sentiment dropped below the 25% threshold, triggering an immediate walkout and ending the summit without a joint statement.' : choice.consequence,
      mechanism: choice.mechanism,
      citation: choice.citation,
      misconception: choice.misconception,
      predictionMatch: predMatched,
      onNext: () => {
        this.hideModal('modalFeedback');
        if (isCollapsed) {
          this.showDebrief();
        } else if (this.state.round < SCS_CONFIG.TOTAL_ROUNDS) {
          this.startRound(this.state.round + 1);
        } else {
          this.startMasteryCheckPhase();
        }
      }
    });
  }

  showFeedbackModal({ outcome, consequence, mechanism, citation, misconception, predictionMatch, onNext }) {
    const modal = document.getElementById('modalFeedback');
    const titleEl = document.getElementById('feedbackTitle');
    const matchEl = document.getElementById('feedbackPredictionStatus');
    const bodyEl = document.getElementById('feedbackBody');
    const btnNext = document.getElementById('btnFeedbackNext');

    if (!modal) return;

    let badgeClass = 'feedback-badge-success';
    let outcomeText = '[OUTCOME: CONSENSUS ADVANCED]';
    if (outcome === 'partial') {
      badgeClass = 'feedback-badge-partial';
      outcomeText = '[OUTCOME: FRICTION & WARNING]';
    } else if (outcome === 'failure') {
      badgeClass = 'feedback-badge-failure';
      outcomeText = '[OUTCOME: DEADLOCK / COLLAPSE]';
    }

    titleEl.innerHTML = `<span class="${badgeClass}">${outcomeText}</span>`;
    matchEl.innerHTML = predictionMatch
      ? `<span style="color:var(--accent);">HYPOTHESIS ALIGNED: Faction reactions confirmed your expectation.</span>`
      : `<span style="color:var(--accent-2);">HYPOTHESIS DIVERGENCE: Diplomatic reaction differed from expectation.</span>`;

    bodyEl.innerHTML = `
      <div class="feedback-block">
        <strong>CONSEQUENCE:</strong>
        <p>${consequence}</p>
      </div>
      <div class="feedback-block">
        <strong>THEORETICAL MECHANISM:</strong>
        <p>${mechanism}</p>
      </div>
      <div class="feedback-block">
        <strong>CANONICAL CITATION:</strong>
        <p><em>${citation}</em></p>
      </div>
      ${misconception ? `
        <div class="feedback-remediation-box">
          <strong>CONCEPTUAL REMEDIATION (${misconception.label}):</strong>
          <p>${misconception.remediation}</p>
        </div>
      ` : ''}
    `;

    btnNext.onclick = onNext;
    this.showModal('modalFeedback');
  }

  startMasteryCheckPhase() {
    this.state.phase = 'MASTERY';
    this.masteryIndex = 0;
    this.renderCurrentMasteryQuestion();
  }

  renderCurrentMasteryQuestion() {
    const q = SCS_MASTERY_CHECKS[this.masteryIndex];
    const railContainer = document.getElementById('sideRailContent');
    if (!railContainer || !q) return;

    railContainer.innerHTML = `
      <div class="rail-phase-badge">[PHASE 3: MASTERY CHECK ${this.masteryIndex + 1} / 3]</div>
      <h3 class="rail-round-title">Normative Verification</h3>
      <p class="rail-question-text">${q.question}</p>

      <div class="rail-options-grid">
        ${q.options.map((opt, idx) => `
          <button class="lab-button mastery-opt-btn" data-opt-id="${opt.id}" tabindex="0">
            <span class="btn-idx-tag">[KEY ${idx + 1}]</span>
            <span class="btn-choice-desc">${opt.text}</span>
          </button>
        `).join('')}
      </div>
      <div id="masteryFeedbackArea"></div>
    `;

    const mcBtns = railContainer.querySelectorAll('.mastery-opt-btn');
    mcBtns.forEach((btn, idx) => {
      btn.onclick = () => {
        const chosenOpt = q.options[idx];
        const isCorrect = !!chosenOpt.correct;

        this.session.recordMasteryCheck({
          questionId: q.questionId,
          chosen: chosenOpt.id,
          correct: q.options.find(o => o.correct)?.id || 'b',
          misconceptionTag: isCorrect ? null : q.misconception,
          objectiveIndex: q.objectiveIndex
        });

        const feedbackArea = document.getElementById('masteryFeedbackArea');
        if (isCorrect) {
          audioEngine.playChimeCooperation();
          feedbackArea.innerHTML = `
            <div class="mastery-msg-success">CORRECT: ASEAN Way normative doctrine verified.</div>
            <button class="lab-button" id="btnNextMc" style="margin-top:8px; width:100%;">CONTINUE &rarr;</button>
          `;
        } else {
          audioEngine.playAlarmKlaxon();
          feedbackArea.innerHTML = `
            <div class="mastery-msg-error">
              <strong>CONCEPTUAL MISCONCEPTION:</strong> ${q.misconception.label}<br>
              ${q.misconception.remediation}
            </div>
            <button class="lab-button" id="btnNextMc" style="margin-top:8px; width:100%;">CONTINUE &rarr;</button>
          `;
        }

        document.getElementById('btnNextMc').onclick = () => {
          this.masteryIndex++;
          if (this.masteryIndex < SCS_MASTERY_CHECKS.length) {
            this.renderCurrentMasteryQuestion();
          } else {
            this.startTransferPhase();
          }
        };
      };
    });
  }

  startTransferPhase() {
    this.state.phase = 'TRANSFER';
    const tr = SCS_TRANSFER;
    const railContainer = document.getElementById('sideRailContent');
    if (!railContainer) return;

    railContainer.innerHTML = `
      <div class="rail-phase-badge">[PHASE 4: TRANSFER SCENARIO]</div>
      <h3 class="rail-round-title">${tr.title}</h3>
      <p class="rail-round-brief">${tr.context}</p>
      <div class="rail-prompt-box"><strong>TRANSFER PROMPT:</strong><br>${tr.prompt}</div>

      <div class="rail-options-grid">
        ${tr.options.map((opt, idx) => `
          <button class="lab-button transfer-opt-btn" data-opt-id="${opt.id}" tabindex="0">
            <span class="btn-idx-tag">[KEY ${idx + 1}]</span>
            <span class="btn-choice-desc">${opt.text}</span>
          </button>
        `).join('')}
      </div>
    `;

    const trBtns = railContainer.querySelectorAll('.transfer-opt-btn');
    trBtns.forEach((btn, idx) => {
      btn.onclick = () => {
        const chosen = tr.options[idx];
        const isCorrect = !!chosen.correct;

        this.session.recordTransfer({
          scenarioId: tr.scenarioId,
          choice: chosen.id,
          correct: tr.options.find(o => o.correct)?.id || 'opt_b',
          objectiveIndex: tr.objectiveIndex
        });

        if (isCorrect) audioEngine.playChimeCooperation();
        else audioEngine.playBetrayalBoom();

        this.showDebrief();
      };
    });
  }

  updateHUD() {
    this.telAgreementText.setText(`COMMUNIQUE SUBSTANCE: ${this.state.agreementValue}%`);

    Object.keys(this.factionMonitors).forEach(k => {
      const mon = this.factionMonitors[k];
      const val = this.state.factions[k];

      mon.barFill.setScale(val / 100, 1);
      mon.sentText.setText(`SENTIMENT: ${val}%`);

      if (val < SCS_CONFIG.COLLAPSE_THRESHOLD) {
        mon.card.setStrokeStyle(2, 0xe11d48);
        mon.sentText.setColor('#e11d48');
        mon.statusTag.setText('STATE: WALKOUT / COLLAPSED');
        mon.statusTag.setColor('#e11d48');
        mon.sprite.setTint(0xe11d48);
      } else if (val < 40) {
        mon.card.setStrokeStyle(1.5, 0xeab308);
        mon.sentText.setColor('#eab308');
        mon.statusTag.setText('STATE: VULNERABLE');
        mon.statusTag.setColor('#eab308');
        mon.sprite.setTint(0xeab308);
      } else {
        mon.card.setStrokeStyle(1.5, 0x1e293b);
        mon.sentText.setColor('#e2e8f0');
        mon.statusTag.setText('STATE: ALIGNED');
        mon.statusTag.setColor('#10b981');
        mon.sprite.clearTint();
      }
    });

    const c1 = this.state.communiqueClauses[0];
    const c2 = this.state.communiqueClauses[1];
    const c3 = this.state.communiqueClauses[2];

    const formatClause = (c) => {
      const badge = c.status === 'accepted' ? '[ACCEPTED]' : c.status === 'contested' ? '[CONTESTED]' : c.status === 'vetoed' ? '[VETOED]' : '[PENDING]';
      return `${c.title}: ${badge} ${c.text}`;
    };

    this.clause1Text.setText(formatClause(c1));
    this.clause1Text.setColor(c1.status === 'accepted' ? '#10b981' : c1.status === 'contested' ? '#eab308' : c1.status === 'vetoed' ? '#e11d48' : '#cbd5e1');

    this.clause2Text.setText(formatClause(c2));
    this.clause2Text.setColor(c2.status === 'accepted' ? '#10b981' : c2.status === 'contested' ? '#eab308' : c2.status === 'vetoed' ? '#e11d48' : '#cbd5e1');

    this.clause3Text.setText(formatClause(c3));
    this.clause3Text.setColor(c3.status === 'accepted' ? '#10b981' : c3.status === 'contested' ? '#eab308' : c3.status === 'vetoed' ? '#e11d48' : '#cbd5e1');
  }

  showDebrief() {
    this.state.phase = 'DEBRIEF';
    const report = this.session.getReport();

    const debriefContainer = document.getElementById('debriefPanelContainer');
    if (debriefContainer) {
      const panel = new DebriefPanel(debriefContainer, report);
      panel.render();
    }

    localStorage.setItem('labs_completed_chairs_gambit', 'true');
    this.showModal('modalDebrief');
  }

  showModal(id) {
    const el = document.getElementById(id);
    if (el) el.classList.add('active');
  }

  hideModal(id) {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  }
}
