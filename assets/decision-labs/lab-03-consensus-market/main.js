import { WtoScene } from './src/scenes/WtoScene.js';
import {
  WtoState,
  COMPLEMENTARY_PACKAGES,
  PREDICTION_OPTIONS,
  MASTERY_CHECKS,
  TRANSFER_SCENARIO
} from './src/WtoConfig.js';
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
  scene: [WtoScene]
};

window.addEventListener('DOMContentLoaded', () => {
  game = new Phaser.Game(config);
  state = new WtoState();

  // Expose state for automated evaluation & testing
  window.wtoState = state;
  window.simGtState = state;

  game.events.once('ready', () => {
    scene = game.scene.getScene('WtoScene');
    initApp();
  });
});

function initApp() {
  bindGlobalControls();
  initOnboarding();
  updateHUD();
  if (scene) scene.updateState(state);
  openModal('modalBriefing');
}

function initOnboarding() {
  onboarding = new OnboardingModal({
    labId: 'lab-03',
    role: 'Director-General · WTO Ministerial Plenary',
    objective: 'Reconcile 8 sovereign trade blocs within a 10-capital budget using cross-sector issue logrolling under Single Undertaking rules.',
    steps: [
      {
        step: '1',
        title: 'HYPOTHESIZE & PREDICT',
        desc: 'Commit to an analytical expectation before negotiating. Test your understanding of multilateral trade bargaining.'
      },
      {
        step: '2',
        title: 'LOGROLL & BUILD CONSENSUS',
        desc: 'Link complementary packages across agriculture, NAMA, TRIPS, and services. Concede capital judiciously to satisfy all 8 blocs.'
      },
      {
        step: '3',
        title: 'AUDIT & MASTER SINGLE UNDERTAKING',
        desc: 'Verify that nothing is agreed until everything is agreed. Correct institutional misconceptions and solve a historical transfer case.'
      }
    ],
    controls: [
      { key: 'LINK', label: 'Link Packages (Cross-Sector Logrolling)' },
      { key: 'CONCEDE', label: 'Concede capital to sovereign trade blocs' },
      { key: 'SPACE', label: 'Roll-Call [SPACE] & plenary vote' },
      { key: 'M', label: 'Toggle sound synthesizer' }
    ],
    onStart: () => {
      if (scene && scene.playSignatureGavelMoment) {
        scene.playSignatureGavelMoment(820, 520);
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
  const hudCapital = document.getElementById('hudCapital');
  const hudSatisfied = document.getElementById('hudSatisfied');
  const hudPackages = document.getElementById('hudPackages');
  const hudRule = document.getElementById('hudRule');

  const satisfiedCount = state.blocs.filter(b => b.satisfied).length;

  if (hudCapital) hudCapital.innerText = `${state.capital} / 10 PTS`;
  if (hudSatisfied) hudSatisfied.innerText = `${satisfiedCount} / 8 BLOCS`;
  if (hudPackages) hudPackages.innerText = `${state.packages.length} / 4`;
  if (hudRule) {
    if (satisfiedCount === 8) {
      hudRule.innerText = 'UNLOCKED (FULL CONSENSUS)';
      hudRule.style.color = 'var(--accent-2)';
    } else {
      hudRule.innerText = `LOCKED (${8 - satisfiedCount} VETOES IN PLAY)`;
      hudRule.style.color = 'var(--accent)';
    }
  }
}

function bindGlobalControls() {
  const btnStart = document.getElementById('btnStartBriefing');
  const btnFeedbackNext = document.getElementById('btnFeedbackNext');
  const btnCloseSigint = document.getElementById('btnCloseSigint');
  const btnRestart = document.getElementById('btnRestartWto');
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

  if (btnCloseSigint) {
    btnCloseSigint.onclick = () => {
      audioEngine.playMechanicalClick();
      closeModal('modalSigint');
    };
  }

  if (btnFeedbackNext) {
    btnFeedbackNext.onclick = () => {
      audioEngine.playMechanicalClick();
      closeModal('modalFeedback');
      startMasteryPhase();
    };
  }

  if (btnRestart) {
    btnRestart.onclick = () => {
      audioEngine.playMechanicalClick();
      closeModal('modalDebrief');
      state.reset();
      updateHUD();
      if (scene) scene.updateState(state);
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

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (onboarding && onboarding.isOpen) return;

    if (e.code === 'Space') {
      const mb = document.getElementById('modalBriefing');
      const mf = document.getElementById('modalFeedback');
      const ms = document.getElementById('modalSigint');
      const md = document.getElementById('modalDebrief');

      if (mb && mb.classList.contains('active')) btnStart && btnStart.click();
      else if (mf && mf.classList.contains('active')) btnFeedbackNext && btnFeedbackNext.click();
      else if (ms && ms.classList.contains('active')) btnCloseSigint && btnCloseSigint.click();
      else if (md && md.classList.contains('active')) btnRestart && btnRestart.click();
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

  if (railIndicator) railIndicator.innerText = 'PHASE 2: PREDICT';
  if (railTitle) railTitle.innerText = 'PLENARY STRATEGY COMMITMENT';

  railContent.innerHTML = `
    <div class="rail-phase-badge">[PHASE 2: PREDICT]</div>
    <div class="rail-prompt-box">
      <strong>HYPOTHESIS COMMITMENT:</strong><br>
      Before committing your finite diplomatic capital (10 pts) across the room, commit to an operational hypothesis:
    </div>

    <div class="rail-options-grid">
      ${PREDICTION_OPTIONS.map((opt, idx) => `
        <button class="rail-choice-btn" data-pred-id="${opt.id}">
          <div class="btn-top-row">
            <span class="btn-key-tag">[HYPOTHESIS ${idx + 1}]</span>
          </div>
          <span class="btn-choice-desc" style="font-size:0.8rem; font-weight:700;">${opt.label}</span>
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

// Phase 3: DECIDE (Logroll packages + unlinked concessions + plenary roll-call)
function startDecidePhase() {
  state.phase = 'NEGOTIATING';
  const railIndicator = document.getElementById('railStepIndicator');
  const railTitle = document.getElementById('railTitle');

  if (railIndicator) railIndicator.innerText = 'PHASE 3: DECIDE';
  if (railTitle) railTitle.innerText = 'CROSS-SECTOR LOGROLLING FLOOR';

  renderNegotiationRail();
}

function renderNegotiationRail() {
  const railContent = document.getElementById('railContent');
  if (!railContent) return;

  const satisfiedCount = state.blocs.filter(b => b.satisfied).length;

  railContent.innerHTML = `
    <div class="rail-phase-badge">[PHASE 3: DECIDE]</div>
    <div class="remediation-box">
      <span class="remediation-title">ACTIVE HYPOTHESIS:</span>
      ${state.pendingPrediction === 'pred-logroll' ? 'Omnibus Logrolling Required' : (state.pendingPrediction === 'pred-individual' ? 'Unilateral Buying' : 'Majority Override')}
    </div>

    <button class="btn-link-package" id="btnOpenSigint" style="width:100%; border-color:var(--accent-2); color:var(--accent-2);">
      <span>🔍 INSPECT SECRETARIAT SIGINT (SOFT RED LINES)</span>
    </button>

    <div class="rail-prompt-box">
      <strong>COMPLEMENTARY LOGROLL PACKAGES:</strong><br>
      Link issue areas across sectors to satisfy both member blocs at package discounts:
    </div>

    <div class="rail-options-grid">
      ${COMPLEMENTARY_PACKAGES.map(pkg => {
        const isLinked = state.packages.some(p => p.id === pkg.id);
        return `
          <div class="package-card ${isLinked ? 'active' : ''}">
            <div class="package-header">
              <span class="package-title">${pkg.name}</span>
              <span class="package-cost">${isLinked ? 'LINKED ✓' : `COST: ${pkg.packageCost} PTS`}</span>
            </div>
            <p class="package-theory">${pkg.theory}</p>
            <button class="btn-link-package ${isLinked ? 'linked' : ''}" data-pkg-id="${pkg.id}">
              ${isLinked ? 'DISSOLVE PACKAGE' : `LINK PACKAGE (-${pkg.packageCost} PTS)`}
            </button>
          </div>
        `;
      }).join('')}
    </div>

    <div class="rail-prompt-box" style="margin-top:6px;">
      <strong>INDIVIDUAL UNLINKED CONCESSIONS:</strong><br>
      Direct concessions to single blocs without package linkages (High raw cost):
    </div>

    <div class="bloc-concede-strip">
      ${state.blocs.map(b => `
        <div class="bloc-mini-card ${b.satisfied ? 'satisfied' : ''}">
          <div style="font-size:0.75rem; font-weight:800; color:${b.satisfied ? 'var(--accent-2)' : 'var(--text)'};">
            ${b.name.length > 14 ? b.name.substring(0, 12) + '..' : b.name}
          </div>
          <button class="btn-mini-concede" data-bloc-id="${b.id}">
            ${b.satisfied ? 'REFUND' : `CONCEDE (-${b.cost}P)`}
          </button>
        </div>
      `).join('')}
    </div>

    <button class="btn-vote-plenary" id="btnCallVote">
      <span>CALL CONSENSUS ROLL-CALL</span>
      <span style="font-family:'Share Tech Mono',monospace; font-size:0.75rem;">(${satisfiedCount}/8 BLOCS)</span>
    </button>
  `;

  // Wire Sigint Modal
  const btnSig = document.getElementById('btnOpenSigint');
  if (btnSig) {
    btnSig.onclick = () => {
      audioEngine.playMechanicalClick();
      openModal('modalSigint');
    };
  }

  // Wire Package Links
  railContent.querySelectorAll('[data-pkg-id]').forEach(btn => {
    btn.onclick = () => {
      const pkgId = btn.getAttribute('data-pkg-id');
      audioEngine.init();
      audioEngine.playMechanicalClick();
      state.packageBloc(pkgId);
      updateHUD();
      if (scene) scene.updateState(state);
      renderNegotiationRail();
    };
  });

  // Wire Individual Concessions
  railContent.querySelectorAll('[data-bloc-id]').forEach(btn => {
    btn.onclick = () => {
      const blocId = btn.getAttribute('data-bloc-id');
      audioEngine.init();
      audioEngine.playMechanicalClick();
      state.concedeBloc(blocId);
      updateHUD();
      if (scene) scene.updateState(state);
      renderNegotiationRail();
    };
  });

  // Wire Vote Call
  const btnVote = document.getElementById('btnCallVote');
  if (btnVote) {
    btnVote.onclick = () => {
      btnVote.disabled = true;
      const res = state.executeConsensusVote();
      updateHUD();

      if (scene) {
        scene.playVoteAnimation(res, () => {
          showFeedbackModal(res.feedback);
        });
      } else {
        showFeedbackModal(res.feedback);
      }
    };
  }
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
    title.innerText = feedback.outcome === 'success' ? 'MULTILATERAL CONSENSUS ACHIEVED' : 'SINGLE UNDERTAKING VETO TRIGGERED';
  }

  if (matchChip) {
    if (feedback.predictionMatch) {
      matchChip.className = 'prediction-match-chip matched';
      matchChip.innerText = '✓ HYPOTHESIS CONFIRMED';
    } else {
      matchChip.className = 'prediction-match-chip refuted';
      matchChip.innerText = '✗ HYPOTHESIS REFUTED';
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
      <p style="font-size:0.78rem; margin:6px 0;">${q.prompt}</p>
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
            <strong style="color:var(--accent-2); font-size:0.78rem;">✓ CORRECT ANALYSIS</strong>
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
  localStorage.setItem('labs_completed_lab-03', 'true');
  localStorage.setItem('labs_completed_wto', 'true');

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
