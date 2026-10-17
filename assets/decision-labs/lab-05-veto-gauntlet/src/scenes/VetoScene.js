import {
  UNSC_CONFIG,
  UNSC_OBJECTIVES,
  UNSC_CLAUSES,
  UNSC_MASTERY_QUESTIONS,
  UNSC_TRANSFER_SCENARIO,
  VetoState
} from '../VetoConfig.js';
import { audioEngine } from '../../../shared/core/AudioEngine.js';
import { renderDebrief } from '../../../shared/learn/DebriefPanel.js';
import { OnboardingModal } from '../../../shared/learn/OnboardingModal.js';

export class VetoScene extends Phaser.Scene {
  constructor() {
    super('VetoScene');
    this.state = new VetoState();
    this.railCollapsed = false;
  }

  preload() {
    this.load.spritesheet('envoy', '../assets/sprites/diplomat_envoy.png', { frameWidth: 32, frameHeight: 48 });
    this.load.spritesheet('rival', '../assets/sprites/diplomat_rival.png', { frameWidth: 32, frameHeight: 48 });
  }

  create() {
    this.initAudioExtensions();
    this.buildChamberEnvironment();
    this.buildP5Delegates();
    this.buildE10Delegates();
    this.buildDraftParchment();
    this.buildPresidentialPodium();
    this.bindDOM();
    this.bindKeyboard();
    this.initOnboarding();
    this.triggerSignatureMoment();
    this.renderRail();
  }

  initAudioExtensions() {
    this.playGavelCrack = () => {
      if (audioEngine.muted) return;
      audioEngine.init();
      const ctx = audioEngine.ctx;
      if (!ctx) return;
      const now = ctx.currentTime;

      // Primary wooden strike
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(320, now);
      osc.frequency.exponentialRampToValueAtTime(55, now + 0.12);
      gain.gain.setValueAtTime(0.55, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);

      // Resonant chamber body
      const res = ctx.createOscillator();
      const resGain = ctx.createGain();
      res.type = 'sine';
      res.frequency.setValueAtTime(140, now);
      res.frequency.exponentialRampToValueAtTime(40, now + 0.22);
      resGain.gain.setValueAtTime(0.35, now);
      resGain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);

      osc.connect(gain);
      gain.connect(ctx.destination);
      res.connect(resGain);
      resGain.connect(ctx.destination);

      osc.start(now);
      osc.stop(now + 0.16);
      res.start(now);
      res.stop(now + 0.26);
    };
  }

  buildChamberEnvironment() {
    // 1024x520 Main Chamber Canvas
    const bg = this.add.rectangle(512, 260, 1024, 520, 0x07131e);

    // Per Krohg Mural Wash & Ceiling Arc Lighting
    const muralArc = this.add.arc(512, -40, 560, 0, 180, false, 0x0f2334, 0.45);
    const innerArc = this.add.arc(512, -20, 480, 0, 180, false, 0x0369a1, 0.15);

    // Teak Horseshoe Dais Outer Border
    const teakOuter = this.add.arc(512, 280, 440, 20, 160, false, 0x0f2334).setStrokeStyle(3, 0x0369a1);
    const teakInner = this.add.arc(512, 270, 360, 25, 155, false, 0x07131e).setStrokeStyle(2, 0x0284c7, 0.4);

    // Top Telemetry Header
    this.topHud = this.add.rectangle(512, 20, 1024, 38, 0x0f2334, 0.95).setStrokeStyle(1, 0x0369a1);
    this.titleText = this.add.text(20, 11, 'UNITED NATIONS SECURITY COUNCIL · 8482ND FORMAL MEETING', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '13px',
      fontStyle: 'bold',
      color: '#e7f1f8'
    });

    this.statusPill = this.add.text(820, 11, 'POSTURE: CONSENSUS HUNT', {
      fontFamily: '"Share Tech Mono", monospace',
      fontSize: '12px',
      color: '#fbbf24'
    });
  }

  buildP5Delegates() {
    this.p5Cards = [];
    const p5Coords = [
      { id: 'usa', name: 'USA', flag: '🇺🇸', x: 160, y: 120 },
      { id: 'gbr', name: 'GBR', flag: '🇬🇧', x: 336, y: 92 },
      { id: 'fra', name: 'FRA', flag: '🇫🇷', x: 512, y: 82 },
      { id: 'rus', name: 'RUS', flag: '🇷🇺', x: 688, y: 92 },
      { id: 'chn', name: 'CHN', flag: '🇨🇳', x: 864, y: 120 }
    ];

    p5Coords.forEach((p, idx) => {
      const container = this.add.container(p.x, p.y);

      // Desk plinth with teak finish
      const desk = this.add.rectangle(0, 0, 134, 98, 0x0f2334)
        .setStrokeStyle(1.5, 0x0369a1);

      // Diplomat character
      const sprite = this.add.sprite(0, -18, idx < 3 ? 'envoy' : 'rival', 0).setScale(1.7);

      // Brass Desk Microphone
      const micStem = this.add.line(0, 0, -25, 20, -20, 6, 0xfbbf24, 0.8).setLineWidth(1.5);
      const micHead = this.add.circle(-20, 5, 2.5, 0xfbbf24);

      // Country Flag & Label
      const label = this.add.text(0, 14, `${p.flag} ${p.name}`, {
        fontFamily: '"Chakra Petch", sans-serif',
        fontSize: '12px',
        fontStyle: 'bold',
        color: '#e7f1f8'
      }).setOrigin(0.5);

      // Voting Status LED Light
      const ledBulb = this.add.circle(46, -34, 5, 0x0369a1);
      const ledHalo = this.add.circle(46, -34, 9, 0x0369a1, 0.25);

      // Dynamic Status Badge
      const statusBadge = this.add.text(0, 32, 'PENDING', {
        fontFamily: '"Chakra Petch", sans-serif',
        fontSize: '10px',
        fontStyle: 'bold',
        color: '#fbbf24',
        backgroundColor: '#07131e',
        padding: { x: 5, y: 2 }
      }).setOrigin(0.5);

      container.add([desk, sprite, micStem, micHead, label, ledHalo, ledBulb, statusBadge]);
      this.p5Cards.push({
        id: p.id,
        container,
        desk,
        sprite,
        ledBulb,
        ledHalo,
        statusBadge,
        member: this.state.p5[idx]
      });
    });
  }

  buildE10Delegates() {
    this.e10Lamps = [];
    const e10X = [130, 210, 295, 385, 470, 555, 640, 725, 810, 895];
    const e10Y = [365, 400, 428, 444, 450, 450, 444, 428, 400, 365];

    for (let i = 0; i < 10; i++) {
      const container = this.add.container(e10X[i], e10Y[i]);

      const desk = this.add.rectangle(0, 0, 48, 30, 0x0f2334, 0.85)
        .setStrokeStyle(1, 0x0369a1);

      const label = this.add.text(0, -4, `E${i + 1}`, {
        fontFamily: '"Share Tech Mono", monospace',
        fontSize: '9px',
        color: '#e7f1f8'
      }).setOrigin(0.5);

      const lamp = this.add.circle(0, 8, 3.5, 0x0369a1);
      const halo = this.add.circle(0, 8, 6, 0x0369a1, 0.2);

      container.add([desk, label, halo, lamp]);
      this.e10Lamps.push({ container, desk, lamp, halo });
    }
  }

  buildDraftParchment() {
    this.parchmentContainer = this.add.container(512, 240);

    const boardBg = this.add.rectangle(0, 0, 460, 140, 0x0b1d2c)
      .setStrokeStyle(1.5, 0x0284c7);

    const title = this.add.text(0, -52, 'COUNCIL DRAFT RESOLUTION 2410 · OPERATIVE CLAUSES', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '11px',
      fontStyle: 'bold',
      color: '#0284c7'
    }).setOrigin(0.5);

    this.clauseRows = [];
    const clauseTitles = [
      'OP 1: Mandate & Enforcement Authority',
      'OP 2: Judicial Accountability & Atrocities',
      'OP 3: Maritime Verification & Interdiction',
      'OP 4: Humanitarian Corridors & Sovereignty'
    ];

    clauseTitles.forEach((t, i) => {
      const yPos = -26 + i * 24;
      const rowText = this.add.text(-210, yPos, t, {
        fontFamily: '"Share Tech Mono", monospace',
        fontSize: '11px',
        color: '#e7f1f8'
      });

      const badge = this.add.text(145, yPos - 1, '[BRACKETED]', {
        fontFamily: '"Chakra Petch", sans-serif',
        fontSize: '10px',
        fontStyle: 'bold',
        color: '#fbbf24',
        backgroundColor: '#07131e',
        padding: { x: 4, y: 1 }
      });

      this.clauseRows.push({ rowText, badge });
    });

    this.parchmentContainer.add([boardBg, title, ...this.clauseRows.flatMap(r => [r.rowText, r.badge])]);
  }

  buildPresidentialPodium() {
    this.podiumContainer = this.add.container(512, 350);

    const plinth = this.add.rectangle(0, 0, 110, 42, 0x0f2334)
      .setStrokeStyle(1.5, 0xfbbf24);

    const label = this.add.text(0, -9, 'PRESIDENT', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '10px',
      fontStyle: 'bold',
      color: '#fbbf24'
    }).setOrigin(0.5);

    // Gavel Icon
    this.gavel = this.add.text(0, 9, '🔨 GAVEL', {
      fontFamily: '"Chakra Petch", sans-serif',
      fontSize: '10px',
      fontStyle: 'bold',
      color: '#e7f1f8'
    }).setOrigin(0.5);

    this.podiumContainer.add([plinth, label, this.gavel]);
  }

  triggerSignatureMoment() {
    this.time.delayedCall(700, () => {
      this.playGavelCrack();
      this.cameras.main.flash(180, 2, 132, 199, false);

      // Sequential cascade of vote lights across all 15 member stations
      const allStations = [...this.p5Cards, ...this.e10Lamps];
      allStations.forEach((st, idx) => {
        this.time.delayedCall(idx * 75, () => {
          if (st.ledBulb) {
            st.ledBulb.setFillStyle(0x0284c7);
            st.ledHalo.setFillStyle(0x0284c7, 0.7);
          } else if (st.lamp) {
            st.lamp.setFillStyle(0x0284c7);
            st.halo.setFillStyle(0x0284c7, 0.7);
          }
        });

        // Reset to idle
        this.time.delayedCall(idx * 75 + 320, () => {
          if (st.ledBulb) {
            st.ledBulb.setFillStyle(0x0369a1);
            st.ledHalo.setFillStyle(0x0369a1, 0.25);
          } else if (st.lamp) {
            st.lamp.setFillStyle(0x0369a1);
            st.halo.setFillStyle(0x0369a1, 0.2);
          }
        });
      });
    });
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
        this.state.reset();
        this.resetVisuals();
        this.renderRail();
      };
    }
  }

  bindKeyboard() {
    this.input.keyboard.on('keydown', (e) => {
      if (this.onboarding && this.onboarding.isOpen) return;
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

  initOnboarding() {
    this.onboarding = new OnboardingModal({
      labId: 'lab-05',
      role: 'President of the UN Security Council',
      objective: 'Draft Chapter VII enforcement clauses that circumvent Permanent Five (P5) unilateral vetoes while assembling at least 9 affirmative votes.',
      steps: [
        {
          step: '1',
          title: 'HYPOTHESIZE & PREDICT',
          desc: 'Analyze P5 strategic interests and commit to an analytical prediction before introducing draft enforcement clauses.'
        },
        {
          step: '2',
          title: 'DRAFT RESOLUTION & CALL VOTE',
          desc: 'Toggle draft clauses [1-4] to balance P5 redlines and secure E10 affirmative votes, then call the vote [SPACE].'
        },
        {
          step: '3',
          title: 'AUDIT & MASTER VETO DYNAMICS',
          desc: 'Examine voting tallies, evaluate UN Charter Art. 27(3) rules, remediate misconceptions, and resolve the transfer case.'
        }
      ],
      controls: [
        { key: 'KEYS 1-4', label: 'Clause toggles [1-4]' },
        { key: 'SPACEBAR', label: 'Call Vote [SPACE]' },
        { key: 'TAB', label: 'Toggle decision rail' },
        { key: 'KEY M', label: 'Toggle audio' }
      ],
      onStart: () => {
        audioEngine.playMechanicalClick();
        if (this.state.phase === 'BRIEF') {
          const btnStart = document.getElementById('btnStartBriefing');
          if (btnStart) btnStart.click();
        }
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

  resetVisuals() {
    this.p5Cards.forEach((c, idx) => {
      c.member = this.state.p5[idx];
      c.statusBadge.setText('PENDING').setColor('#fbbf24');
      c.ledBulb.setFillStyle(0x0369a1);
      c.ledHalo.setFillStyle(0x0369a1, 0.25);
      c.desk.setStrokeStyle(1.5, 0x0369a1);
      c.sprite.setTexture(idx < 3 ? 'envoy' : 'rival', 0);
    });

    this.e10Lamps.forEach(el => {
      el.lamp.setFillStyle(0x0369a1);
      el.halo.setFillStyle(0x0369a1, 0.2);
    });

    this.clauseRows.forEach(r => {
      r.badge.setText('[BRACKETED]').setColor('#fbbf24');
    });

    this.statusPill.setText('POSTURE: CONSENSUS HUNT').setColor('#fbbf24');
  }

  renderRail() {
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
      case 'VOTE':
        this.renderVoteCall(railContent);
        break;
      case 'VOTING':
        this.renderVotingInProgress(railContent);
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
    const elClause = document.getElementById('hudClauseNum');
    const elConsensus = document.getElementById('hudConsensus');
    const elVotes = document.getElementById('hudVoteTally');
    const elScore = document.getElementById('hudScore');

    const clause = this.state.getCurrentClause();
    if (elClause) {
      elClause.innerText = clause ? `OP ${this.state.currentClauseIndex + 1} / 04` : 'FINAL PLENARY';
    }

    if (elConsensus) {
      const satisfiedP5 = this.state.p5.filter(m => m.satisfied).length;
      elConsensus.innerText = `${satisfiedP5} / 5 P5 CONCURRING`;
    }

    if (elVotes) {
      elVotes.innerText = this.state.voteResult ? `${this.state.voteResult.totalYes} / 15 AFFIRMATIVE` : 'TALLY PENDING';
    }

    if (elScore) {
      elScore.innerText = `${this.state.score} PTS`;
    }
  }

  renderBriefing(container) {
    container.innerHTML = `
      <div class="card briefing-card" role="region" aria-label="UNSC Mission Briefing">
        <div class="card-badge">UNSC SANCTIONS COMMITTEE · MANDATE 2410</div>
        <h2 class="card-heading">THE VETO GAUNTLET: CHAPTER VII PLENARY</h2>
        <p class="card-desc">
          As Penholder at the United Nations Security Council, you must draft a binding Chapter VII resolution addressing an escalating international crisis. Under Article 27(3), you require <strong>9 affirmative votes</strong> and <strong>zero negative votes from the Permanent Five (USA, UK, France, Russia, China)</strong>.
        </p>
        <div class="objectives-box">
          <div class="box-title">PEDAGOGICAL OBJECTIVES</div>
          <ul class="objectives-list">
            ${UNSC_OBJECTIVES.map(obj => `<li>${obj}</li>`).join('')}
          </ul>
        </div>
        <div class="tactical-dossier">
          <div class="dossier-row"><strong>USA:</strong> <span>Protect verification & non-proliferation</span></div>
          <div class="dossier-row"><strong>GBR:</strong> <span>Maintain UNCLOS freedom of navigation</span></div>
          <div class="dossier-row"><strong>FRA:</strong> <span>Preserve civilian humanitarian corridors</span></div>
          <div class="dossier-row"><strong>RUS:</strong> <span>Reject Chapter VII Article 42 armed force</span></div>
          <div class="dossier-row"><strong>CHN:</strong> <span>Strict sovereign non-interference in internal affairs</span></div>
        </div>
        <button id="btnStartBriefing" class="action-btn btn-primary" type="button">
          ENTER COUNCIL CHAMBER & DRAFT [SPACE]
        </button>
      </div>
    `;

    const btnStart = document.getElementById('btnStartBriefing');
    if (btnStart) {
      btnStart.onclick = () => {
        audioEngine.playMechanicalClick();
        this.playGavelCrack();
        this.state.phase = 'PREDICT';
        this.renderRail();
      };
    }
  }

  renderPrediction(container) {
    const clause = this.state.getCurrentClause();
    if (!clause) return;

    container.innerHTML = `
      <div class="card prediction-card" role="region" aria-label="Hypothesis Commitment">
        <div class="card-badge">HYPOTHESIS PHASE · CLAUSE ${this.state.currentClauseIndex + 1} OF 4</div>
        <h2 class="card-heading">${clause.title}</h2>
        <p class="scenario-text">${clause.context}</p>
        <div class="prediction-box">
          <p class="prediction-prompt"><strong>HYPOTHESIS COMMITMENT:</strong> ${clause.predictionPrompt}</p>
          <div class="options-stack">
            ${clause.predictionOptions.map(opt => `
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
        this.renderRail();
      };
    });
  }

  renderDecision(container) {
    const clause = this.state.getCurrentClause();
    if (!clause) return;

    container.innerHTML = `
      <div class="card decision-card" role="region" aria-label="Diplomatic Clause Drafting">
        <div class="card-badge">DECISION PHASE · OPERATIVE CLAUSE ${this.state.currentClauseIndex + 1} OF 4</div>
        <h2 class="card-heading">${clause.title}</h2>
        <p class="scenario-summary">Select the formulation to table before the Security Council:</p>
        <div class="verbs-grid">
          ${clause.choices.map(ch => `
            <button class="verb-btn" data-key="${ch.id}" type="button">
              <div class="verb-key">[OPTION ${ch.id}]</div>
              <div class="verb-title">${ch.title}</div>
              <div class="verb-sub">${ch.summary}</div>
            </button>
          `).join('')}
        </div>
      </div>
    `;

    container.querySelectorAll('.verb-btn').forEach(btn => {
      btn.onclick = (e) => {
        audioEngine.playMechanicalClick();
        const choiceId = e.currentTarget.getAttribute('data-key');
        const res = this.state.executeClauseDecision(choiceId);
        this.updateClauseVisuals(res);
        this.renderRail();
      };
    });
  }

  updateClauseVisuals(res) {
    const choice = res.choice;
    const clauseIdx = this.state.currentClauseIndex;

    // Update Parchment badge
    if (this.clauseRows[clauseIdx]) {
      if (res.isCorrect) {
        this.clauseRows[clauseIdx].badge.setText('[RATIFIED]').setColor('#10b981');
      } else {
        this.clauseRows[clauseIdx].badge.setText('[VETO RED-LINE]').setColor('#f43f5e');
      }
    }

    // Update P5 delegate desk indicators
    Object.entries(choice.p5Votes).forEach(([p5Id, vote]) => {
      const card = this.p5Cards.find(c => c.id === p5Id);
      if (card) {
        if (vote === 'YES') {
          card.statusBadge.setText('CONCUR (YES)').setColor('#10b981');
          card.ledBulb.setFillStyle(0x10b981);
          card.ledHalo.setFillStyle(0x10b981, 0.45);
          card.desk.setStrokeStyle(1.5, 0x10b981);
          card.sprite.setTexture(card.sprite.texture.key, 5); // happy
        } else if (vote === 'ABSTAIN') {
          card.statusBadge.setText('ABSTAIN').setColor('#fbbf24');
          card.ledBulb.setFillStyle(0xfbbf24);
          card.ledHalo.setFillStyle(0xfbbf24, 0.4);
          card.desk.setStrokeStyle(1.5, 0xfbbf24);
          card.sprite.setTexture(card.sprite.texture.key, 0); // neutral
        } else if (vote === 'VETO') {
          card.statusBadge.setText('VETO THREAT').setColor('#f43f5e');
          card.ledBulb.setFillStyle(0xf43f5e);
          card.ledHalo.setFillStyle(0xf43f5e, 0.6);
          card.desk.setStrokeStyle(1.5, 0xf43f5e);
          card.sprite.setTexture(card.sprite.texture.key, 6); // angry
        }
      }
    });

    if (res.isCorrect) {
      audioEngine.playChimeCooperation();
    } else {
      audioEngine.playBetrayalBoom();
      this.cameras.main.shake(250, 0.015);
    }
  }

  renderConsequence(container) {
    const fb = this.state.lastFeedback;
    const isSuccess = fb && fb.outcome === 'success';

    container.innerHTML = `
      <div class="card consequence-card ${isSuccess ? 'card-success' : 'card-failure'}" role="region" aria-label="Decision Consequence">
        <div class="feedback-header">
          <span class="badge ${isSuccess ? 'badge-success' : 'badge-failure'}">
            ${isSuccess ? '✓ CLAUSE ADAPTED (NO VETO)' : '⚠ P5 VETO THREAT TRIGGERED'}
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
        <button id="btnAdvanceClause" class="action-btn btn-primary" type="button">
          ${this.state.currentClauseIndex < 3 ? 'PROCEED TO NEXT OPERATIVE PARAGRAPH [SPACE]' : 'CALL FORMAL COUNCIL VOTE [SPACE]'}
        </button>
      </div>
    `;

    const btnAdv = document.getElementById('btnAdvanceClause');
    if (btnAdv) {
      btnAdv.onclick = () => {
        audioEngine.playMechanicalClick();
        const hasNext = this.state.advanceClause();
        this.renderRail();
      };
    }
  }

  renderVoteCall(container) {
    container.innerHTML = `
      <div class="card vote-call-card" role="region" aria-label="Call for Roll-Call Vote">
        <div class="card-badge">COUNCIL FORMAL VOTING · ARTICLE 27(3)</div>
        <h2 class="card-heading">DRAFT RESOLUTION TABLING</h2>
        <p class="scenario-text">
          All four operative paragraphs have been finalized. The President of the Security Council now calls for a formal roll-call vote by show of hands.
        </p>
        <div class="tactical-dossier">
          <div class="dossier-row"><strong>STATUTORY THRESHOLD:</strong> <span>9 Affirmative Votes</span></div>
          <div class="dossier-row"><strong>PERMANENT FIVE RULE:</strong> <span>Zero Negative Votes</span></div>
          <div class="dossier-row"><strong>ABSTENTION STATUS:</strong> <span>Does Not Invalidate Adoption</span></div>
        </div>
        <button id="btnCallCouncilVote" class="action-btn btn-primary" type="button">
          STRIKE GAVEL & EXECUTE ROLL-CALL VOTE [SPACE]
        </button>
      </div>
    `;

    const btnVote = document.getElementById('btnCallCouncilVote');
    if (btnVote) {
      btnVote.onclick = () => {
        this.handleFormalCouncilVote();
      };
    }
  }

  handleFormalCouncilVote() {
    this.playGavelCrack();
    this.state.phase = 'VOTING';
    this.renderRail();

    const voteRes = this.state.executeFinalVote();

    // Animate gavel
    this.tweens.add({
      targets: this.gavel,
      rotation: -0.4,
      duration: 80,
      yoyo: true,
      repeat: 1
    });

    // Cascade voting lights across P5 and E10
    this.p5Cards.forEach((c, idx) => {
      this.time.delayedCall(idx * 140, () => {
        const vote = c.member.finalVote || 'YES';
        if (vote === 'VETO') {
          c.statusBadge.setText('CAST VETO').setColor('#f43f5e');
          c.ledBulb.setFillStyle(0xf43f5e);
          c.ledHalo.setFillStyle(0xf43f5e, 0.8);
          c.desk.setStrokeStyle(2, 0xf43f5e);
        } else if (vote === 'ABSTAIN') {
          c.statusBadge.setText('ABSTAINED').setColor('#fbbf24');
          c.ledBulb.setFillStyle(0xfbbf24);
          c.ledHalo.setFillStyle(0xfbbf24, 0.5);
          c.desk.setStrokeStyle(1.5, 0xfbbf24);
        } else {
          c.statusBadge.setText('VOTED YES').setColor('#10b981');
          c.ledBulb.setFillStyle(0x10b981);
          c.ledHalo.setFillStyle(0x10b981, 0.6);
          c.desk.setStrokeStyle(1.5, 0x10b981);
        }
      });
    });

    const e10YesCount = voteRes.e10Yes;
    this.e10Lamps.forEach((el, idx) => {
      this.time.delayedCall(700 + idx * 80, () => {
        if (idx < e10YesCount) {
          el.lamp.setFillStyle(0x10b981);
          el.halo.setFillStyle(0x10b981, 0.5);
        } else {
          el.lamp.setFillStyle(0xfbbf24);
          el.halo.setFillStyle(0xfbbf24, 0.3);
        }
      });
    });

    this.time.delayedCall(1800, () => {
      if (voteRes.passed) {
        audioEngine.playChimeCooperation();
        this.cameras.main.flash(250, 16, 185, 129, false);
        this.statusPill.setText('RESOLUTION ADOPTED ✓').setColor('#10b981');
      } else {
        audioEngine.playBetrayalBoom();
        this.cameras.main.shake(350, 0.02);
        this.cameras.main.flash(300, 244, 63, 94);
        this.statusPill.setText('RESOLUTION VETOED ✕').setColor('#f43f5e');
      }
      this.renderVoteOutcome(voteRes);
    });
  }

  renderVotingInProgress(container) {
    container.innerHTML = `
      <div class="card vote-progress-card">
        <div class="card-badge">ROLL-CALL IN PROGRESS...</div>
        <h2 class="card-heading">RECORDING DELEGATE VOTES</h2>
        <p class="scenario-text">Tallying affirmative votes across 15 Member States under Article 27(3)...</p>
      </div>
    `;
  }

  renderVoteOutcome(voteRes) {
    const container = document.getElementById('railScrollArea');
    if (!container) return;

    container.innerHTML = `
      <div class="card consequence-card ${voteRes.passed ? 'card-success' : 'card-failure'}" role="region" aria-label="Vote Outcome">
        <div class="feedback-header">
          <span class="badge ${voteRes.passed ? 'badge-success' : 'badge-failure'}">
            ${voteRes.passed ? '✓ RESOLUTION ADOPTED' : '✕ TERMINATED BY P5 VETO'}
          </span>
          <span style="font-size:0.82rem; font-weight:800;">
            ${voteRes.totalYes} / 15 VOTES
          </span>
        </div>
        <div class="feedback-block">
          <div class="block-label">VOTE BREAKDOWN:</div>
          <div class="block-content">
            Permanent Five: ${voteRes.p5Yes} Affirmative, ${voteRes.abstainingMembers.length} Abstentions, ${voteRes.vetoingMembers.length} Negative Vetoes.<br>
            Non-Permanent (E10): ${voteRes.e10Yes} Affirmative Votes.
          </div>
        </div>
        <div class="feedback-block">
          <div class="block-label">LEGAL STATUS:</div>
          <div class="block-content">
            ${voteRes.passed
              ? 'The resolution satisfies Article 27(3): clears the 9-vote affirmative threshold without any negative votes from permanent members.'
              : `Under Article 27(3), negative votes cast by permanent members (${voteRes.vetoingMembers.map(m => m.name).join(', ')}) immediately terminate the resolution.`
            }
          </div>
        </div>
        <button id="btnProceedToMastery" class="action-btn btn-primary" type="button">
          PROCEED TO CONCEPT MASTERY CHECK [SPACE]
        </button>
      </div>
    `;

    const btnNext = document.getElementById('btnProceedToMastery');
    if (btnNext) {
      btnNext.onclick = () => {
        audioEngine.playMechanicalClick();
        this.state.phase = 'MASTERY';
        this.renderRail();
      };
    }
  }

  renderMastery(container) {
    const q = this.state.getCurrentMasteryQuestion();
    if (!q) {
      this.state.phase = 'TRANSFER';
      this.renderRail();
      return;
    }

    container.innerHTML = `
      <div class="card mastery-card" role="region" aria-label="Concept Mastery Question">
        <div class="card-badge">MASTERY CHECK · ITEM ${this.state.masteryIndex + 1} OF ${UNSC_MASTERY_QUESTIONS.length}</div>
        <h2 class="card-heading">UNSC INSTITUTIONAL LAW</h2>
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
          <div class="block-label">STATUTORY CITATION:</div>
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
        this.renderRail();
      };
    }
  }

  renderTransfer(container) {
    const sc = UNSC_TRANSFER_SCENARIO;

    container.innerHTML = `
      <div class="card transfer-card" role="region" aria-label="Transfer Scenario Evaluation">
        <div class="card-badge">TRANSFER EVALUATION · HISTORICAL APPLICATION</div>
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
        this.renderRail();
      };
    }
  }

  renderDebrief(container) {
    const report = this.state.getReport();
    localStorage.setItem('labs_completed_unsc_veto', 'true');

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
        this.state.reset();
        this.resetVisuals();
        this.renderRail();
      };
    }
  }
}
