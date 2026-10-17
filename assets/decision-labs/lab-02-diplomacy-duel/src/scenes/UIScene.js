import { CONSTANTS } from '../../../shared/core/Constants.js';
import { eventBus, Events } from '../../../shared/core/EventBus.js';
import { gameState } from '../../../shared/core/GameState.js';
import { audioEngine } from '../../../shared/core/AudioEngine.js';

/**
 * UIScene — HTML/DOM & Canvas HUD Overlay.
 */
export class UIScene extends Phaser.Scene {
  constructor() {
    super('UIScene');
  }

  create() {
    // 1. Top Telemetry Bar
    this.add.rectangle(CONSTANTS.CANVAS.WIDTH / 2, 22, CONSTANTS.CANVAS.WIDTH, 44, 0x050914, 0.9)
      .setStrokeStyle(1, 0x1e293b);

    this.roundText = this.add.text(24, 12, 'ROUND: 01 / 08', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '15px',
      color: '#38bdf8'
    });

    this.scoreText = this.add.text(280, 12, 'PAYOFF: 0 PTS', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '15px',
      color: '#ffffff'
    });

    this.streakText = this.add.text(540, 12, 'TRUST CAPACITOR: 0/3 (1.0x)', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '15px',
      color: '#10b981'
    });

    const bestScore = localStorage.getItem(CONSTANTS.STORAGE_KEYS.BEST_SCORE) || 0;
    this.bestText = this.add.text(860, 12, `BEST: ${bestScore} PTS`, {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '15px',
      color: '#f59e0b'
    });

    // 2. Chronological Mission Pips Bar (bottom of table)
    this.pips = [];
    const pipsStartX = CONSTANTS.CANVAS.WIDTH / 2 - (CONSTANTS.ROUNDS.TOTAL * 36) / 2 + 18;
    for (let i = 0; i < CONSTANTS.ROUNDS.TOTAL; i++) {
      const pip = this.add.sprite(pipsStartX + i * 36, 490, 'pips', i === 0 ? 6 : 0);
      pip.setScale(2);
      this.pips.push(pip);
    }

    // 3. Status Ticker Line
    this.tickerText = this.add.text(CONSTANTS.CANVAS.WIDTH / 2, 530, 'Standing by for executive diplomatic posture...', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '14px',
      color: '#94a3b8'
    }).setOrigin(0.5);

    // 4. Wire DOM Buttons
    this.setupDOMControls();

    // 5. Wire EventBus
    this.unsubs = [
      eventBus.on(Events.SCORE_UPDATE, (d) => this.onScoreUpdate(d)),
      eventBus.on(Events.ROUND_RESOLVE, (d) => this.onRoundResolve(d)),
      eventBus.on(Events.ROUND_NEXT, (d) => this.onRoundNext(d)),
      eventBus.on(Events.BRIEFING_OPEN, () => this.showModal('modalBriefing')),
      eventBus.on(Events.SIGINT_TRIGGER, (d) => this.showSigintModal(d)),
      eventBus.on(Events.DEBRIEF_OPEN, () => this.showDebriefModal())
    ];

    // Keyboard Shortcuts
    this.input.keyboard.on('keydown-C', () => this.triggerMove('C'));
    this.input.keyboard.on('keydown-D', () => this.triggerMove('D'));
    this.input.keyboard.on('keydown-SPACE', () => this.handleSpaceKey());
  }

  setupDOMControls() {
    this.btnCoop = document.getElementById('btnCoop');
    this.btnDefect = document.getElementById('btnDefect');
    this.btnStartBriefing = document.getElementById('btnStartBriefing');
    this.btnResumeSigint = document.getElementById('btnResumeSigint');
    this.btnRestart = document.getElementById('btnRestart');
    this.btnSound = document.getElementById('btnSound');
    this.btnRules = document.getElementById('btnRules');

    if (this.btnCoop) {
      this.btnCoop.onclick = () => this.triggerMove('C');
    }
    if (this.btnDefect) {
      this.btnDefect.onclick = () => this.triggerMove('D');
    }
    if (this.btnStartBriefing) {
      this.btnStartBriefing.onclick = () => {
        audioEngine.init();
        audioEngine.playMechanicalClick();
        this.hideModal('modalBriefing');
        gameState.phase = 'CHOOSING';
        this.setSwitchesEnabled(true);
        this.tickerText.setText('Decision channel cleared. Transmit executive posture...');
      };
    }
    if (this.btnResumeSigint) {
      this.btnResumeSigint.onclick = () => {
        audioEngine.playMechanicalClick();
        this.hideModal('modalSigint');
        gameState.round++;
        gameState.phase = 'CHOOSING';
        this.onRoundNext({ round: gameState.round });
        this.setSwitchesEnabled(true);
      };
    }
    if (this.btnRestart) {
      this.btnRestart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.hideModal('modalDebrief');
        eventBus.emit(Events.GAME_RESTART);
        this.setSwitchesEnabled(true);
      };
    }
    if (this.btnSound) {
      this.btnSound.onclick = () => {
        audioEngine.init();
        const muted = audioEngine.toggleMute();
        document.getElementById('soundStatusText').innerText = muted ? 'AUDIO: MUTED' : 'AUDIO: ACTIVE';
      };
    }
    if (this.btnRules) {
      this.btnRules.onclick = () => {
        this.showModal('modalBriefing');
      };
    }
  }

  triggerMove(choice) {
    if (gameState.phase !== 'CHOOSING') return;
    this.setSwitchesEnabled(false);
    this.tickerText.setText(`Posture transmitted: ${choice === 'C' ? 'COOPERATION' : 'DEFECT'}. Awaiting foreign decrypt...`);
    eventBus.emit(Events.PLAYER_MOVE, { choice });
  }

  setSwitchesEnabled(enabled) {
    if (this.btnCoop) this.btnCoop.disabled = !enabled;
    if (this.btnDefect) this.btnDefect.disabled = !enabled;
  }

  onScoreUpdate(data) {
    this.scoreText.setText(`PAYOFF: ${data.playerScore} PTS`);
    const streakStr = data.streak >= 5 ? '5/5 (2.0x BOOST)' : (data.streak >= 3 ? `${data.streak}/5 (1.5x BOOST)` : `${data.streak}/3 (1.0x)`);
    this.streakText.setText(`TRUST CAPACITOR: ${streakStr}`);
    const best = Math.max(data.playerScore, parseInt(localStorage.getItem(CONSTANTS.STORAGE_KEYS.BEST_SCORE) || '0', 10));
    this.bestText.setText(`BEST: ${best} PTS`);
  }

  onRoundResolve(result) {
    const curPip = this.pips[result.round - 1];
    if (curPip) {
      // 2: playerC, 3: playerD
      curPip.setFrame(result.player === 'C' ? 2 : 3);
    }
    if (result.player === 'C' && result.rival === 'C') {
      this.tickerText.setText(`MUTUAL COOPERATION (+${result.pDelta} PTS). Reciprocal trust fortified.`);
    } else if (result.player === 'D' && result.rival === 'C') {
      this.tickerText.setText(`TACTICAL EXPLOITATION (+${result.pDelta} PTS). Adversary breached.`);
    } else if (result.player === 'C' && result.rival === 'D') {
      this.tickerText.setText(`BETRAYAL DETECTED (${result.pDelta} PTS). Sucker's payoff suffered.`);
    } else {
      this.tickerText.setText(`MUTUAL DEFECT (${result.pDelta} PTS). Deadlock Nash Equilibrium.`);
    }
  }

  onRoundNext({ round }) {
    this.roundText.setText(`ROUND: 0${round} / 0${CONSTANTS.ROUNDS.TOTAL}`);
    this.pips.forEach((p, idx) => {
      if (idx === round - 1) p.setFrame(6); // active
      else if (idx >= round) p.setFrame(0); // empty
    });
    this.setSwitchesEnabled(true);
    this.tickerText.setText('Decision channel cleared. Transmit executive posture...');
  }

  showModal(id) {
    const el = document.getElementById(id);
    if (el) el.classList.add('active');
  }

  hideModal(id) {
    const el = document.getElementById(id);
    if (el) el.classList.remove('active');
  }

  showSigintModal({ intel }) {
    document.getElementById('sigintMessage').innerText = intel;
    this.showModal('modalSigint');
  }

  showDebriefModal() {
    const stars = gameState.getStars();
    const rank = gameState.getRank();

    document.getElementById('debriefStars').innerText = '★'.repeat(stars) + '☆'.repeat(3 - stars);
    document.getElementById('debriefRank').innerText = rank;
    document.getElementById('statScore').innerText = `${gameState.playerScore} PTS`;

    const coops = gameState.history.filter(h => h.player === 'C').length;
    const rate = Math.round((coops / CONSTANTS.ROUNDS.TOTAL) * 100);
    document.getElementById('statCoop').innerText = `${rate}% (${coops} / ${CONSTANTS.ROUNDS.TOTAL} Rounds)`;
    document.getElementById('statStreak').innerText = `${gameState.maxStreak} Consecutive Rounds`;
    document.getElementById('statDoctrine').innerText = `${gameState.doctrine.name.toUpperCase()} [${gameState.doctrine.archetype}]`;

    document.getElementById('debriefTheoryText').innerHTML = `
      <strong>THEORETICAL EXPOSITION · ${gameState.doctrine.name}:</strong><br>
      ${gameState.doctrine.theory}<br><br>
      <em>Key Takeaway:</em> When the shadow of the future is long, mutual cooperation generates Pareto-optimal welfare that outcompetes unilateral defection.
    `;

    const oldBest = parseInt(localStorage.getItem(CONSTANTS.STORAGE_KEYS.BEST_SCORE) || '0', 10);
    if (gameState.playerScore > oldBest) {
      localStorage.setItem(CONSTANTS.STORAGE_KEYS.BEST_SCORE, gameState.playerScore);
    }
    localStorage.setItem(CONSTANTS.STORAGE_KEYS.COMPLETED, 'true');

    this.showModal('modalDebrief');
  }

  handleSpaceKey() {
    const mB = document.getElementById('modalBriefing');
    const mS = document.getElementById('modalSigint');
    const mD = document.getElementById('modalDebrief');

    if (mB && mB.classList.contains('active')) {
      if (this.btnStartBriefing) this.btnStartBriefing.click();
    } else if (mS && mS.classList.contains('active')) {
      if (this.btnResumeSigint) this.btnResumeSigint.click();
    } else if (mD && mD.classList.contains('active')) {
      if (this.btnRestart) this.btnRestart.click();
    }
  }

  destroy() {
    if (this.unsubs) this.unsubs.forEach(fn => fn());
    super.destroy();
  }
}
