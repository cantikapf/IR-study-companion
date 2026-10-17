import { GameScene } from './src/scenes/GameScene.js';
import {
  DuelState,
  PREDICTION_OPTIONS,
  MASTERY_CHECKS,
  TRANSFER_SCENARIO,
  getRandomDoctrine
} from './src/DuelConfig.js';
import { DebriefPanel } from '../shared/learn/DebriefPanel.js';
import { audioEngine } from '../shared/core/AudioEngine.js';
import { OnboardingModal } from '../shared/learn/OnboardingModal.js';

let game = null;
let scene = null;
let state = null;
let onboarding = null;

const config = {
  type: Phaser.AUTO,
  parent: 'phaser-container',
  width: 820,
  height: 520,
  pixelArt: true,
  roundPixels: true,
  transparent: true,
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH
  },
  scene: [GameScene]
};

window.addEventListener('DOMContentLoaded', () => {
  game = new Phaser.Game(config);
  state = new DuelState();

  // Expose state for inspection & test suites
  window.duelState = state;
  window.simGtState = state;

  game.events.once('ready', () => {
    scene = game.scene.getScene('GameScene');
    initApp();
  });
});

function initApp() {
  bindGlobalControls();
  initOnboarding();
  updateHUD();
  openModal('modalBriefing');
}

function initOnboarding() {
  onboarding = new OnboardingModal({
    labId: 'lab-02',
    role: 'Chief Bilateral Envoy · Iterated Diplomatic Duel',
    objective: 'Establish sustainable cooperation and decode rival foreign doctrines without being exploited.',
    steps: [
      {
        step: '1',
        title: 'HYPOTHESIZE & PREDICT',
        desc: 'Commit to an analytical expectation before dispatching envoys. Test your anticipation of rival diplomatic posture.'
      },
      {
        step: '2',
        title: 'EXECUTE STRATEGIC DISPATCH',
        desc: 'Choose between Cooperation [C / 1] and Defection [D / 2]. Track mutual payoffs and watch the central trust filament respond.'
      },
      {
        step: '3',
        title: 'DECODE DOCTRINE & MASTER AXELROD',
        desc: 'Intercept SIGINT telemetry, identify rival doctrine (Tit-for-Tat, Grim Trigger, Pavlov, etc.), and solve a historical transfer dilemma.'
      }
    ],
    controls: [
      { key: 'C / 1', label: 'Cooperate [C / 1] (Mutual Gain & Trust)' },
      { key: 'D / 2', label: 'Defect [D / 2] (Temptation & Retaliate)' },
      { key: 'SPACE', label: 'Advance [SPACE] & confirm choices' },
      { key: 'M', label: 'Toggle sound synthesizer' }
    ],
    onStart: () => {
      if (scene && scene.playSignatureSealMoment) {
        scene.playSignatureSealMoment();
      }
    }
  });

  if (scene) scene.onboarding = onboarding;
  window.onboarding = onboarding;

  const btnHowToPlay = document.getElementById('btnHowToPlay');
  if (btnHowToPlay) {
    btnHowToPlay.onclick = () => {
      audioEngine.playMechanicalClick();
      onboarding.open();
    };
  }

  // Trigger onboarding.open() on initial boot
  onboarding.open();
}

function updateHUD() {
  const hudRound = document.getElementById('hudRound');
  const hudPayoff = document.getElementById('hudPayoff');
  const hudStreak = document.getElementById('hudStreak');
  const hudRival = document.getElementById('hudRival');

  if (hudRound) hudRound.innerText = `${String(state.round).padStart(2, '0')} / 08`;
  if (hudPayoff) hudPayoff.innerText = `${state.playerScore} PTS`;
  if (hudStreak) hudStreak.innerText = `${state.streak} (${state.getMultiplier().toFixed(1)}x)`;
  if (hudRival) {
    hudRival.innerText = state.round > 4 ? state.doctrine.name.toUpperCase() : 'ENCRYPTED';
  }
}

function bindGlobalControls() {
  const btnStart = document.getElementById('btnStartBriefing');
  const btnResumeSigint = document.getElementById('btnResumeSigint');
  const btnFeedbackNext = document.getElementById('btnFeedbackNext');
  const btnRestart = document.getElementById('btnRestartDuel');
  const btnAudio = document.getElementById('btnAudioToggle');
  const btnRules = document.getElementById('btnRulesModal');

  if (btnStart) {
    btnStart.onclick = () => {
      audioEngine.init();
      audioEngine.playMechanicalClick();
      closeModal('modalBriefing');
      startPredictPhase();
    };
  }

  if (btnResumeSigint) {
    btnResumeSigint.onclick = () => {
      audioEngine.playMechanicalClick();
      closeModal('modalSigint');
      state.round++;
      updateHUD();
      if (scene) scene.updateRivalTag(state.doctrine.name);
      startPredictPhase();
    };
  }

  if (btnFeedbackNext) {
    btnFeedbackNext.onclick = () => {
      audioEngine.playMechanicalClick();
      closeModal('modalFeedback');

      if (state.round === 4) {
        // Trigger SIGINT Intercept
        audioEngine.playAlarmKlaxon();
        const sigintBox = document.getElementById('sigintDecryptText');
        if (sigintBox) {
          sigintBox.innerHTML = `
            <strong>DOCTRINE: ${state.doctrine.name.toUpperCase()}</strong><br>
            <em>${state.doctrine.sigint}</em><br><br>
            <span style="font-size:0.75rem; color:var(--accent);">${state.doctrine.theory}</span>
          `;
        }
        openModal('modalSigint');
      } else if (state.round < 8) {
        state.round++;
        updateHUD();
        startPredictPhase();
      } else {
        // Rounds finished -> Start Mastery Checks (Phase 6)
        startMasteryPhase();
      }
    };
  }

  if (btnRestart) {
    btnRestart.onclick = () => {
      audioEngine.playMechanicalClick();
      closeModal('modalDebrief');
      state.reset();
      state.doctrine = getRandomDoctrine();
      updateHUD();
      if (scene) {
        scene.resetDiplomats();
        scene.updateTrustFilament(0, 1.0);
      }
      startPredictPhase();
    };
  }

  if (btnAudio) {
    btnAudio.onclick = () => {
      const isMuted = audioEngine.toggleMute();
      btnAudio.innerText = isMuted ? 'AUDIO: MUTED' : 'AUDIO: ON';
    };
  }

  if (btnRules) {
    btnRules.onclick = () => {
      openModal('modalBriefing');
    };
  }

  // Keyboard Navigation
  window.addEventListener('keydown', (e) => {
    if (onboarding && onboarding.isOpen) return;

    if (e.code === 'Space') {
      const mb = document.getElementById('modalBriefing');
      const mf = document.getElementById('modalFeedback');
      const ms = document.getElementById('modalSigint');
      const md = document.getElementById('modalDebrief');

      if (mb && mb.classList.contains('active')) btnStart && btnStart.click();
      else if (mf && mf.classList.contains('active')) btnFeedbackNext && btnFeedbackNext.click();
      else if (ms && ms.classList.contains('active')) btnResumeSigint && btnResumeSigint.click();
      else if (md && md.classList.contains('active')) btnRestart && btnRestart.click();
    } else if (e.key === 'c' || e.key === 'C' || e.key === '1') {
      const btnC = document.querySelector('[data-choice="C"]');
      if (btnC) btnC.click();
    } else if (e.key === 'd' || e.key === 'D' || e.key === '2') {
      const btnD = document.querySelector('[data-choice="D"]');
      if (btnD) btnD.click();
    }
  });
}

// 7-PHASE LEARNING LOOP ORCHESTRATION

// Phase 2: PREDICT
function startPredictPhase() {
  state.phase = 'PREDICTING';
  const railIndicator = document.getElementById('railStepIndicator');
  const railTitle = document.getElementById('railTitle');
  const railContent = document.getElementById('railContent');

  if (railIndicator) railIndicator.innerText = `ROUND ${state.round} · PHASE 2: PREDICT`;
  if (railTitle) railTitle.innerText = `ROUND ${state.round} DISPATCH PROBE`;

  railContent.innerHTML = `
    <div class="rail-phase-badge">[PHASE 2: PREDICT]</div>
    <div class="rail-prompt-box">
      <strong>HYPOTHESIS COMMITMENT:</strong><br>
      Before transmitting your dispatch, formulate an expectation of how this bilateral interaction will resolve:
    </div>

    <div class="rail-options-grid">
      ${PREDICTION_OPTIONS.map((opt, idx) => `
        <button class="rail-choice-btn" data-pred-id="${opt.id}">
          <div class="btn-top-row">
            <span class="btn-key-tag">[OPTION ${idx + 1}]</span>
            <span class="btn-choice-title">${opt.id}</span>
          </div>
          <span class="btn-choice-desc">${opt.label}</span>
        </button>
      `).join('')}
    </div>
  `;

  railContent.querySelectorAll('.rail-choice-btn').forEach(btn => {
    btn.onclick = () => {
      audioEngine.init();
      audioEngine.playMechanicalClick();
      const predId = btn.getAttribute('data-pred-id');
      state.recordPrediction(predId);
      startDecidePhase();
    };
  });
}

// Phase 3: DECIDE
function startDecidePhase() {
  state.phase = 'DECIDING';
  const railIndicator = document.getElementById('railStepIndicator');
  const railContent = document.getElementById('railContent');

  if (railIndicator) railIndicator.innerText = `ROUND ${state.round} · PHASE 3: DECIDE`;

  railContent.innerHTML = `
    <div class="rail-phase-badge">[PHASE 3: DECIDE]</div>
    <div class="remediation-box">
      <span class="remediation-title">ACTIVE HYPOTHESIS:</span>
      Predicted Outcome: <strong>${state.pendingPrediction}</strong>
    </div>

    <div class="rail-prompt-box">
      <strong>SELECT DISPATCH POSTURE:</strong><br>
      Authorize the strategic posture to deliver to the rival plenipotentiary:
    </div>

    <div class="rail-options-grid">
      <button class="rail-choice-btn" data-choice="C" style="border-left: 3px solid var(--accent-2);">
        <div class="btn-top-row">
          <span class="btn-key-tag">[KEY C]</span>
          <span class="btn-choice-title" style="color:var(--text);">COOPERATE (C)</span>
        </div>
        <span class="btn-choice-desc">Transmit signed bilateral compliance treaty. Seeks mutual trust and multiplier accumulation.</span>
      </button>

      <button class="rail-choice-btn" data-choice="D" style="border-left: 3px solid var(--accent);">
        <div class="btn-top-row">
          <span class="btn-key-tag">[KEY D]</span>
          <span class="btn-choice-title" style="color:var(--accent);">DEFECT (D)</span>
        </div>
        <span class="btn-choice-desc">Deploy unilateral exploitative probe / border build-up. Sacrifices trust for short-term leverage.</span>
      </button>
    </div>
  `;

  railContent.querySelectorAll('[data-choice]').forEach(btn => {
    btn.onclick = () => {
      // Disable buttons to prevent double click
      railContent.querySelectorAll('[data-choice]').forEach(b => { b.disabled = true; });

      const choice = btn.getAttribute('data-choice');
      const feedback = state.applyDecision(choice);

      updateHUD();
      if (scene) {
        scene.updateTrustFilament(state.streak, state.getMultiplier());
        scene.playTurnAnimation(feedback.playerMove, feedback.rivalMove, feedback, () => {
          showFeedbackModal(feedback);
        });
      } else {
        showFeedbackModal(feedback);
      }
    };
  });
}

// Phase 4 & 5: CONSEQUENCE & EXPLAIN
function showFeedbackModal(feedback) {
  state.phase = 'EXPLAIN';

  const modal = document.getElementById('modalFeedback');
  const banner = document.getElementById('feedbackBanner');
  const title = document.getElementById('feedbackOutcomeText');
  const matchChip = document.getElementById('feedbackMatchChip');
  const consequence = document.getElementById('feedbackConsequence');
  const mechanism = document.getElementById('feedbackMechanism');
  const citation = document.getElementById('feedbackCitation');
  const remBox = document.getElementById('feedbackRemediationBox');
  const remTitle = document.getElementById('feedbackRemediationTitle');
  const remText = document.getElementById('feedbackRemediationText');

  if (banner) {
    banner.className = `feedback-banner outcome-${feedback.outcome}`;
  }

  if (title) {
    const outcomeLabels = {
      success: `MUTUAL COOPERATION (+${feedback.pDelta} PTS)`,
      partial: `TACTICAL EXPLOITATION (+${feedback.pDelta} PTS)`,
      failure: feedback.key === 'CD' ? `SUCKER BETRAYAL (${feedback.pDelta} PTS)` : `DETERRENCE DEADLOCK (${feedback.pDelta} PTS)`
    };
    title.innerText = outcomeLabels[feedback.outcome] || 'DISPATCH RESOLUTION';
  }

  if (matchChip) {
    if (feedback.predictionMatch) {
      matchChip.className = 'prediction-match-chip matched';
      matchChip.innerText = `✓ HYPOTHESIS CONFIRMED [${feedback.key}]`;
    } else {
      matchChip.className = 'prediction-match-chip refuted';
      matchChip.innerText = `✗ HYPOTHESIS REFUTED (Expected ${state.pendingPrediction}, Got ${feedback.key})`;
    }
  }

  if (consequence) consequence.innerText = feedback.consequence;
  if (mechanism) mechanism.innerText = feedback.mechanism;
  if (citation) citation.innerText = feedback.citation;

  if (feedback.misconception && remBox && remText) {
    remBox.style.display = 'flex';
    if (remTitle) remTitle.innerText = `MISCONCEPTION: ${feedback.misconception.label.toUpperCase()}`;
    remText.innerText = feedback.misconception.remediation;
  } else if (remBox) {
    remBox.style.display = 'none';
  }

  openModal('modalFeedback');
}

// Phase 6: MASTERY CHECK (3 Items)
function startMasteryPhase() {
  state.phase = 'MASTERY';
  const railIndicator = document.getElementById('railStepIndicator');
  const railTitle = document.getElementById('railTitle');
  const railContent = document.getElementById('railContent');

  if (railIndicator) railIndicator.innerText = `PHASE 6: MASTERY CHECK (${state.masteryIndex + 1} / 3)`;
  if (railTitle) railTitle.innerText = 'CONCEPT MASTERY VERIFICATION';

  const q = MASTERY_CHECKS[state.masteryIndex];
  if (!q) {
    startTransferPhase();
    return;
  }

  railContent.innerHTML = `
    <div class="rail-phase-badge">[PHASE 6: MASTERY CHECK]</div>
    <div class="rail-prompt-box">
      <strong>${q.title.toUpperCase()}:</strong><br>
      <pre style="font-family:'Share Tech Mono',monospace; font-size:0.75rem; color:var(--accent); margin:6px 0; white-space:pre-wrap;">${q.prompt}</pre>
    </div>

    <div class="rail-options-grid">
      ${q.choices.map((c, idx) => `
        <button class="rail-choice-btn" data-choice-id="${c.id}">
          <div class="btn-top-row">
            <span class="btn-key-tag">[OPTION ${idx + 1}]</span>
            <span class="btn-choice-title">${c.text}</span>
          </div>
        </button>
      `).join('')}
    </div>
    <div id="masteryFeedbackArea" style="margin-top:6px;"></div>
  `;

  railContent.querySelectorAll('.rail-choice-btn').forEach(btn => {
    btn.onclick = () => {
      const choiceId = btn.getAttribute('data-choice-id');
      const res = state.answerMastery(choiceId);
      const fbArea = document.getElementById('masteryFeedbackArea');

      if (res.isCorrect) {
        audioEngine.playChimeCooperation();
        btn.style.borderColor = 'var(--accent-2)';
        fbArea.innerHTML = `
          <div class="feedback-banner outcome-success" style="padding:8px 10px;">
            <strong style="color:var(--accent-2); font-size:0.78rem;">✓ CORRECT IDENTIFICATION</strong>
            <p style="font-size:0.72rem;">${res.remediation}</p>
          </div>
        `;
        setTimeout(() => {
          state.masteryIndex++;
          if (state.masteryIndex < MASTERY_CHECKS.length) {
            startMasteryPhase();
          } else {
            startTransferPhase();
          }
        }, 1100);
      } else {
        audioEngine.playBetrayalBoom();
        btn.style.borderColor = 'var(--accent)';
        fbArea.innerHTML = `
          <div class="remediation-box" style="margin-top:6px;">
            <span class="remediation-title">INCORRECT ANALYSIS:</span>
            ${res.remediation}
          </div>
        `;
      }
    };
  });
}

// Phase 7: TRANSFER SCENARIO
function startTransferPhase() {
  state.phase = 'TRANSFER';
  const railIndicator = document.getElementById('railStepIndicator');
  const railTitle = document.getElementById('railTitle');
  const railContent = document.getElementById('railContent');

  if (railIndicator) railIndicator.innerText = 'PHASE 7: TRANSFER CHALLENGE';
  if (railTitle) railTitle.innerText = 'CROSS-DOMAIN TRANSFER';

  const tf = TRANSFER_SCENARIO;

  railContent.innerHTML = `
    <div class="rail-phase-badge">[PHASE 7: TRANSFER]</div>
    <div class="rail-prompt-box">
      <strong>${tf.title.toUpperCase()}:</strong><br>
      <p style="font-size:0.76rem; opacity:0.9; margin:4px 0;">${tf.context}</p>
      <strong style="color:var(--accent); font-size:0.76rem;">${tf.prompt}</strong>
    </div>

    <div class="rail-options-grid">
      ${tf.choices.map((c, idx) => `
        <button class="rail-choice-btn" data-transfer-id="${c.id}">
          <div class="btn-top-row">
            <span class="btn-key-tag">[STRATEGY ${idx + 1}]</span>
            <span class="btn-choice-title">${c.text}</span>
          </div>
        </button>
      `).join('')}
    </div>
    <div id="transferFeedbackArea" style="margin-top:8px;"></div>
  `;

  railContent.querySelectorAll('.rail-choice-btn').forEach(btn => {
    btn.onclick = () => {
      const choiceId = btn.getAttribute('data-transfer-id');
      const res = state.answerTransfer(choiceId);
      const fbArea = document.getElementById('transferFeedbackArea');

      if (res.isCorrect) {
        audioEngine.playChimeCooperation();
        btn.style.borderColor = 'var(--accent-2)';
      } else {
        audioEngine.playBetrayalBoom();
        btn.style.borderColor = 'var(--accent)';
      }

      fbArea.innerHTML = `
        <div class="remediation-box" style="margin-top:6px;">
          <span class="remediation-title">${res.isCorrect ? 'TRANSFER EVALUATION: EXCELLENT' : 'TRANSFER REMEDIATION:'}</span>
          ${res.feedback}
        </div>
        <button class="btn-command-execute" id="btnGoToDebrief" style="margin-top:10px; width:100%;">
          <span>VIEW AFTER-ACTION DEBRIEF REPORT</span>
        </button>
      `;

      const btnDebrief = document.getElementById('btnGoToDebrief');
      if (btnDebrief) {
        btnDebrief.onclick = () => showDebrief();
      }
    };
  });
}

function showDebrief() {
  state.phase = 'DEBRIEF';
  const mount = document.getElementById('debriefPanelMount');
  if (mount) {
    const report = state.getReport();
    DebriefPanel.render(report, mount);
  }

  // Completion marker
  localStorage.setItem('labs_completed_lab-02', 'true');
  localStorage.setItem('labs_completed_game-theory', 'true');

  openModal('modalDebrief');
}

function openModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('active');
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.remove('active');
}
