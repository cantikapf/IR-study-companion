import { PUTNAM_CONFIG, PUTNAM_OBJECTIVES, PUTNAM_ROUNDS, PUTNAM_MASTERY_CHECKS, PUTNAM_TRANSFER, PutnamState } from '../PutnamConfig.js';
import { audioEngine } from '../../../shared/core/AudioEngine.js';
import { LearningSession } from '../../../shared/learn/LearningSession.js';
import { DebriefPanel } from '../../../shared/learn/DebriefPanel.js';
import { OnboardingModal } from '../../../shared/learn/OnboardingModal.js';

export class PutnamScene extends Phaser.Scene {
  constructor() {
    super('PutnamScene');
    this.state = new PutnamState();
    this.session = new LearningSession('lab-06', PUTNAM_OBJECTIVES);
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

    // Split Stage Backdrop: Geneva (Left) vs Parliament (Right)
    this.leftBg = this.add.rectangle(W / 4, H / 2, W / 2, H, 0x081024);
    this.rightBg = this.add.rectangle((3 * W) / 4, H / 2, W / 2, H, 0x141a12);

    // Subtle table backdrops
    this.add.rectangle(205, 310, 360, 95, 0x0f1d38, 0.7).setStrokeStyle(1.5, 0x1e3a5f);
    this.add.rectangle(615, 310, 360, 95, 0x222216, 0.7).setStrokeStyle(1.5, 0x42381e);

    // Center divider
    this.divider = this.add.line(W / 2, H / 2, 0, -H / 2, 0, H / 2, 0x06b6d4, 0.5).setLineWidth(2);

    // Top Banners
    this.add.rectangle(205, 24, 380, 32, 0x060e1d, 0.9).setStrokeStyle(1, 0x1e293b);
    this.intlHeader = this.add.text(205, 24, 'LEVEL I: GENEVA NEGOTIATION TABLE', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '12px',
      fontStyle: 'bold',
      color: '#38bdf8'
    }).setOrigin(0.5);

    this.add.rectangle(615, 24, 380, 32, 0x0f150f, 0.9).setStrokeStyle(1, 0x1e293b);
    this.domHeader = this.add.text(615, 24, 'LEVEL II: DOMESTIC PARLIAMENTARY CHAMBER', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '12px',
      fontStyle: 'bold',
      color: '#eab308'
    }).setOrigin(0.5);

    // Left Diplomatic Delegation (Geneva)
    this.intlEnvoy = this.add.sprite(150, 270, 'envoy', 0).setScale(2.8);
    this.intlRival = this.add.sprite(260, 270, 'rival', 0).setScale(2.8);
    this.intlTableLabel = this.add.text(205, 325, 'BILATERAL DRAFT DESK', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#cbd5e1'
    }).setOrigin(0.5);

    // Level I Progress Bar
    this.add.rectangle(205, 375, 320, 14, 0x0f172a).setStrokeStyle(1, 0x1e293b);
    this.intlBarFill = this.add.rectangle(45, 375, 112, 14, 0x06b6d4).setOrigin(0, 0.5);
    this.intlProgressText = this.add.text(205, 402, 'GENEVA ACCORD PROGRESS: 35%', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '12px',
      fontStyle: 'bold',
      color: '#38bdf8'
    }).setOrigin(0.5);

    // Right Parliamentary Delegation (Westminster)
    this.domEnvoy = this.add.sprite(560, 270, 'envoy', 0).setScale(2.8);
    this.domRival = this.add.sprite(670, 270, 'rival', 0).setScale(2.8);
    this.domTableLabel = this.add.text(615, 325, 'HOUSE RATIFICATION BENCH', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#cbd5e1'
    }).setOrigin(0.5);

    // Level II Progress Bar
    this.add.rectangle(615, 375, 320, 14, 0x0f172a).setStrokeStyle(1, 0x1e293b);
    this.domBarFill = this.add.rectangle(455, 375, 112, 14, 0xeab308).setOrigin(0, 0.5);
    this.domProgressText = this.add.text(615, 402, 'PARLIAMENTARY RATIFICATION: 35%', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '12px',
      fontStyle: 'bold',
      color: '#eab308'
    }).setOrigin(0.5);

    // Central Venn Overlap Mechanism (Center Stage, X=410, Y=145)
    this.vennBox = this.add.rectangle(410, 145, 196, 138, 0x060b17, 0.95).setStrokeStyle(1.5, 0x06b6d4);
    this.vennLeftCircle = this.add.circle(388, 140, 42, 0x06b6d4, 0.3);
    this.vennRightCircle = this.add.circle(432, 140, 42, 0xeab308, 0.3);
    this.vennOverlapGlow = this.add.circle(410, 140, 22, 0x10b981, 0.45);

    this.vennTitle = this.add.text(410, 88, 'WIN-SET OVERLAP', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#ffffff'
    }).setOrigin(0.5);

    this.vennPercentText = this.add.text(410, 140, '35%', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '22px',
      fontStyle: 'bold',
      color: '#ffffff'
    }).setOrigin(0.5);

    this.vennStatusLabel = this.add.text(410, 194, 'ZOPA: VIABLE', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#10b981'
    }).setOrigin(0.5);

    // Domestic Caucus Breakdown Bar (Bottom Stage Right)
    this.add.rectangle(615, 458, 360, 42, 0x091016, 0.9).setStrokeStyle(1, 0x1e293b);
    this.caucusText = this.add.text(615, 458, 'HAWKS: 45% · DOVES: 50% · BUSINESS: 50%', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#e2e8f0'
    }).setOrigin(0.5);

    // Round Telemetry Bar (Bottom Stage Left)
    this.add.rectangle(205, 458, 360, 42, 0x060e1d, 0.9).setStrokeStyle(1, 0x1e293b);
    this.intlTelemetryText = this.add.text(205, 458, 'ROUND 1 / 4: TARIFFS & SUBSIDIES', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#38bdf8'
    }).setOrigin(0.5);

    // Electoral Shock Alert Indicator (Hidden initially)
    this.shockBanner = this.add.rectangle(410, 235, 540, 32, 0xe11d48, 0.95).setVisible(false);
    this.shockText = this.add.text(410, 235, 'ELECTORAL SHOCK: HAWKS SURGE! RATIFICATION THRESHOLD RAISED TO 65%', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#ffffff'
    }).setOrigin(0.5).setVisible(false);

    // Involuntary Defection Warning
    this.involuntaryBanner = this.add.rectangle(410, 235, 540, 32, 0x991b1b, 0.95).setVisible(false);
    this.involuntaryText = this.add.text(410, 235, 'INVOLUNTARY DEFECTION: LEVEL I AGREED BUT PARLIAMENT REJECTED!', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#ffffff'
    }).setOrigin(0.5).setVisible(false);

    // Execute Signature Moment in first 3 seconds
    this.triggerSignatureMoment();

    this.bindDOM();
    this.updateHUD();
    this.initOnboarding();
    this.startRound(1);
  }

  triggerSignatureMoment() {
    audioEngine.init();
    audioEngine.playMechanicalClick();

    // 1. Order Papers flying across the parliamentary chamber (Right)
    const paperCount = 12;
    for (let i = 0; i < paperCount; i++) {
      const startX = 490 + Math.random() * 290;
      const startY = 440 + Math.random() * 40;
      const paper = this.add.rectangle(startX, startY, 12, 16, 0xe2e8f0, 0.85);
      paper.setAngle(Phaser.Math.Between(-35, 35));

      this.tweens.add({
        targets: paper,
        x: startX + Phaser.Math.Between(-60, 60),
        y: startY - Phaser.Math.Between(150, 280),
        angle: paper.angle + Phaser.Math.Between(-140, 140),
        alpha: { from: 0.9, to: 0 },
        duration: 1600 + Math.random() * 600,
        ease: 'Cubic.easeOut',
        onComplete: () => paper.destroy()
      });
    }

    // 2. Ratification sparks bursting at central Venn intersection
    for (let i = 0; i < 20; i++) {
      const angle = Math.random() * Math.PI * 2;
      const speed = 35 + Math.random() * 85;
      const color = (i % 2 === 0) ? 0x06b6d4 : 0xeab308;
      const spark = this.add.circle(410, 140, 3, color, 1);

      this.tweens.add({
        targets: spark,
        x: 410 + Math.cos(angle) * speed,
        y: 140 + Math.sin(angle) * speed,
        alpha: { from: 1, to: 0 },
        scale: { from: 1, to: 0.2 },
        duration: 500 + Math.random() * 300,
        ease: 'Quad.easeOut',
        onComplete: () => spark.destroy()
      });
    }

    // 3. Central Venn pulse
    this.tweens.add({
      targets: [this.vennLeftCircle, this.vennRightCircle],
      scale: 1.2,
      yoyo: true,
      duration: 450,
      repeat: 1
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
        this.session = new LearningSession('lab-06', PUTNAM_OBJECTIVES);
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
      labId: 'lab-06',
      role: 'Chief Treaty Negotiator · Putnam Two-Level Table',
      objective: 'Synchronize international Level I concessions with domestic Level II legislative ratification factions to expand the overlapping win-set (ZOPA).',
      steps: [
        {
          step: '1',
          title: 'PREDICT DOMESTIC REACTION',
          desc: 'Before making concessions in Geneva, commit to an analytical prediction of how parliamentary factions will shift.'
        },
        {
          step: '2',
          title: 'CALCULATE TWO-LEVEL TRADEOFFS',
          desc: 'Balance Level I international bargaining with Level II domestic ratification using Actions [1-3] to keep the ZOPA positive.'
        },
        {
          step: '3',
          title: 'AUDIT & MASTER RATIFICATION',
          desc: 'Survive the Turn 4 electoral shock, prevent involuntary defection, complete mastery questions, and resolve the transfer case.'
        }
      ],
      controls: [
        { key: 'KEYS 1-3', label: 'Actions [1-3]' },
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
      const decBtns = document.querySelectorAll('.clause-opt-btn');
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
    const roundData = PUTNAM_ROUNDS[roundNum - 1];

    if (roundNum === PUTNAM_CONFIG.ELECTORAL_SHOCK_ROUND) {
      audioEngine.playAlarmKlaxon();
      this.cameras.main.shake(350, 0.015);
      this.shockBanner.setVisible(true);
      this.shockText.setVisible(true);
    } else {
      this.shockBanner.setVisible(false);
      this.shockText.setVisible(false);
    }

    this.intlTelemetryText.setText(`ROUND ${roundNum} / 4: ${roundData.topic.toUpperCase()}`);
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
        <strong>HYPOTHESIS COMMITMENT:</strong><br>
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
      <p class="rail-instruction-text">Select a policy clause to bind both Geneva and Parliament:</p>

      <div class="rail-options-grid">
        ${roundData.choices.map((c, idx) => `
          <button class="lab-button clause-opt-btn" data-choice-id="${c.id}" tabindex="0">
            <div class="btn-top-row">
              <span class="btn-idx-tag">[KEY ${idx + 1}]</span>
              <strong class="btn-choice-title">${c.title}</strong>
            </div>
            <p class="btn-choice-desc">${c.desc}</p>
            <div class="btn-deltas-row">
              <span class="delta-badge delta-intl">LEVEL I: ${c.level1Delta >= 0 ? '+' : ''}${c.level1Delta}%</span>
              <span class="delta-badge delta-dom">LEVEL II: ${c.level2Delta >= 0 ? '+' : ''}${c.level2Delta}%</span>
            </div>
          </button>
        `).join('')}
      </div>
    `;

    const choiceBtns = railContainer.querySelectorAll('.clause-opt-btn');
    choiceBtns.forEach((btn, idx) => {
      btn.onclick = () => {
        const choice = roundData.choices[idx];
        this.commitDecision(choice, roundData);
      };
    });
  }

  commitDecision(choice, roundData) {
    this.state.phase = 'CONSEQUENCE';
    this.state.applyPolicyChoice(choice);
    this.updateHUD();

    const decisionId = `round-${this.state.round}`;
    const isCorrect = (choice.outcome === 'success');
    const predMatched = (choice.predictedAlignment === this.pendingPrediction);

    this.session.recordDecision({
      decisionId,
      choice: choice.id,
      correctChoice: roundData.choices.find(c => c.outcome === 'success')?.id || choice.id,
      rationale: choice.consequence,
      misconceptionTag: choice.misconception,
      predicted: this.pendingPrediction,
      actual: choice.predictedAlignment,
      outcome: choice.outcome,
      consequence: choice.consequence,
      mechanism: choice.mechanism,
      citation: choice.citation,
      objectiveIndex: choice.objectiveIndex
    });

    if (isCorrect) {
      audioEngine.playChimeCooperation();
      this.intlEnvoy.setTint(0x38bdf8);
      this.domEnvoy.setTint(0x34d399);
      this.time.delayedCall(700, () => {
        this.intlEnvoy.clearTint();
        this.domEnvoy.clearTint();
      });
    } else {
      audioEngine.playBetrayalBoom();
      this.cameras.main.shake(200, 0.01);
      this.domRival.setTint(0xe11d48);
      this.time.delayedCall(700, () => this.domRival.clearTint());
    }

    if (this.state.involuntaryDefection) {
      this.involuntaryBanner.setVisible(true);
      this.involuntaryText.setVisible(true);
    } else {
      this.involuntaryBanner.setVisible(false);
      this.involuntaryText.setVisible(false);
    }

    this.showFeedbackModal({
      outcome: choice.outcome,
      consequence: choice.consequence,
      mechanism: choice.mechanism,
      citation: choice.citation,
      misconception: choice.misconception,
      predictionMatch: predMatched,
      onNext: () => {
        this.hideModal('modalFeedback');
        if (this.state.round < PUTNAM_CONFIG.TOTAL_ROUNDS) {
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
    let outcomeText = '[OUTCOME: SUCCESS]';
    if (outcome === 'partial') {
      badgeClass = 'feedback-badge-partial';
      outcomeText = '[OUTCOME: ASYMMETRIC FRICTION]';
    } else if (outcome === 'failure') {
      badgeClass = 'feedback-badge-failure';
      outcomeText = '[OUTCOME: RATIFICATION BREAKDOWN]';
    }

    titleEl.innerHTML = `<span class="${badgeClass}">${outcomeText}</span>`;
    matchEl.innerHTML = predictionMatch
      ? `<span style="color:var(--accent);">HYPOTHESIS ALIGNED: Your prediction matched system mechanics.</span>`
      : `<span style="color:var(--accent-2);">HYPOTHESIS DIVERGENCE: System reacted differently than anticipated.</span>`;

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
    const q = PUTNAM_MASTERY_CHECKS[this.masteryIndex];
    const railContainer = document.getElementById('sideRailContent');
    if (!railContainer || !q) return;

    railContainer.innerHTML = `
      <div class="rail-phase-badge">[PHASE 3: MASTERY CHECK ${this.masteryIndex + 1} / 3]</div>
      <h3 class="rail-round-title">Conceptual Verification</h3>
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
            <div class="mastery-msg-success">CORRECT: Theoretical mechanics verified.</div>
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
          if (this.masteryIndex < PUTNAM_MASTERY_CHECKS.length) {
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
    const tr = PUTNAM_TRANSFER;
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
    this.intlBarFill.setScale(this.state.table1Progress / 100, 1);
    this.intlProgressText.setText(`GENEVA ACCORD PROGRESS: ${this.state.table1Progress}%`);

    this.domBarFill.setScale(this.state.table2Progress / 100, 1);
    this.domProgressText.setText(`PARLIAMENTARY RATIFICATION: ${this.state.table2Progress}%`);

    this.vennPercentText.setText(`${this.state.winSetOverlap}%`);

    const skew = Math.abs(this.state.table1Progress - this.state.table2Progress);
    const separation = Math.min(60, 22 + (skew * 0.5));
    this.vennLeftCircle.setX(410 - separation / 2);
    this.vennRightCircle.setX(410 + separation / 2);

    if (this.state.involuntaryDefection) {
      this.vennOverlapGlow.setFillStyle(0xe11d48, 0.6);
      this.vennBox.setStrokeStyle(1.5, 0xe11d48);
      this.vennStatusLabel.setText('ZOPA: COLLAPSED');
      this.vennStatusLabel.setColor('#e11d48');
    } else if (this.state.winSetOverlap >= 65) {
      this.vennOverlapGlow.setFillStyle(0x10b981, 0.5);
      this.vennBox.setStrokeStyle(1.5, 0x10b981);
      this.vennStatusLabel.setText('ZOPA: BROAD RATIFICATION');
      this.vennStatusLabel.setColor('#10b981');
    } else if (this.state.winSetOverlap >= 45) {
      this.vennOverlapGlow.setFillStyle(0xeab308, 0.4);
      this.vennBox.setStrokeStyle(1.5, 0xeab308);
      this.vennStatusLabel.setText('ZOPA: NARROW / VULNERABLE');
      this.vennStatusLabel.setColor('#eab308');
    } else {
      this.vennOverlapGlow.setFillStyle(0xe11d48, 0.4);
      this.vennBox.setStrokeStyle(1.5, 0xe11d48);
      this.vennStatusLabel.setText('ZOPA: DEADLOCK HAZARD');
      this.vennStatusLabel.setColor('#e11d48');
    }

    this.caucusText.setText(
      `HAWKS: ${this.state.caucuses.hawks}% · DOVES: ${this.state.caucuses.doves}% · BUSINESS: ${this.state.caucuses.business}%`
    );
  }

  showDebrief() {
    this.state.phase = 'DEBRIEF';
    const report = this.session.getReport();

    const debriefContainer = document.getElementById('debriefPanelContainer');
    if (debriefContainer) {
      const panel = new DebriefPanel(debriefContainer, report);
      panel.render();
    }

    localStorage.setItem('labs_completed_putnam_pressure', 'true');
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
