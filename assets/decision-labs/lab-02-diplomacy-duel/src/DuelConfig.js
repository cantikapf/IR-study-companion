import { LearningSession } from '../../shared/learn/LearningSession.js';
import { chaptersFor, chapterUrl } from '../../shared/learn/ChapterLink.js';

export const LAB_ID = 'lab-02';

export const LEARNING_OBJECTIVES = [
  'Explain why iteration sustains cooperation under international anarchy.',
  'Contrast Tit-for-Tat, Grim Trigger, Predator, Pavlov, and Wildcard doctrines.',
  'Apply Axelrod’s four properties: nice, provocable, forgiving, and clear.'
];

export const MISCONCEPTIONS = {
  'beat-rival': {
    tag: 'beat-the-rival',
    label: 'Zero-Sum Dominance / Beating Rival Fallacy',
    remediation: 'Axelrod proved Tit-for-Tat never outscores its partner in any encounter. Its evolutionary dominance comes from eliciting mutual cooperation (R=5), not maximizing relative exploitation (T=10).'
  },
  'always-defect': {
    tag: 'always-defect',
    label: 'Universal Defection Fallacy',
    remediation: 'In single-shot games, defection dominates. But iterated play introduces the shadow of the future (discount parameter δ), making mutual cooperation individually rational under anarchy.'
  },
  'forgiveness-weakness': {
    tag: 'forgiveness-weakness',
    label: 'Forgiveness Equals Weakness Fallacy',
    remediation: 'Grim Trigger retaliates forever, creating permanent deadlock (-2/-2). Forgiving strategies (TFT, Pavlov) escape echo-retaliation cascades once goodwill is restored while still penalizing betrayal.'
  }
};

export const PAYOFF = {
  CC: [5, 5],
  CD: [-10, 10],
  DC: [10, -10],
  DD: [-2, -2]
};

export const DIPLOMATIC_DOCTRINES = [
  {
    id: 'tft',
    name: 'Tit-for-Tat',
    archetype: 'Reciprocal Retaliator',
    sigint: "DECRYPT: 'Our doctrine is strictly reactive. We initiate with an open hand, mirror any aggressive provocation once, and reconcile immediately upon goodwill.'",
    theory: "Robert Axelrod's tournament champion (1984). Transparent, unforgiving of betrayal, yet instantly forgiving when cooperation is re-established.",
    makeDecision: (history) => history.length === 0 ? 'C' : history[history.length - 1].player
  },
  {
    id: 'grim',
    name: 'Grim Trigger',
    archetype: 'Deterrence Maximizer',
    sigint: "DECRYPT: 'Zero compromise. We remain peaceful until the very first hostile provocation. The instant trust is broken, negotiations are terminated permanently.'",
    theory: "Cold War strategic deterrence posture. Cooperates perpetually until a single betrayal occurs, triggering permanent, unyielding retaliation.",
    makeDecision: (history) => history.some(h => h.player === 'D') ? 'D' : 'C'
  },
  {
    id: 'predator',
    name: 'The Predator',
    archetype: 'Hawk Opportunist',
    sigint: "DECRYPT: 'All treaties are tactical delays. Power is zero-sum; weakness invites annexation. Deploy offensive posture across every round.'",
    theory: "Offensive Realism archetype. Assumes all actors will inevitably exploit; defects relentlessly regardless of counter-moves.",
    makeDecision: () => 'D'
  },
  {
    id: 'pavlov',
    name: 'Pavlov (Win-Stay / Lose-Shift)',
    archetype: 'Behaviorist Pragmatist',
    sigint: "DECRYPT: 'Assess the prior payoff outcome. If the yield was advantageous (both cooperated or we successfully exploited), maintain stance. Otherwise, shift.'",
    theory: "Nowak & Sigmund's evolutionary strategy. Capitalizes on cooperative partners and corrects quickly when counter-exploited.",
    makeDecision: (history) => {
      if (!history || history.length === 0) return 'C';
      const last = history[history.length - 1];
      const own = last.rival ?? 'C';
      const opp = last.player ?? 'C';
      // Win-Stay / Lose-Shift:
      // Reward (CC or DC: opp is C) -> repeat own last move
      // Loss (CD or DD: opp is D) -> flip own last move
      const isReward = opp === 'C';
      return isReward ? own : (own === 'C' ? 'D' : 'C');
    }
  },
  {
    id: 'wildcard',
    name: 'The Wildcard',
    archetype: 'Volatile Brinkmanship',
    sigint: "DECRYPT: 'Satellite surveillance detects chaotic domestic factional infighting. National signals are erratic and unpredictable (60% Coop / 40% Defect).'",
    theory: "Models internal domestic regime instability and erratic bureaucratic politics under Graham Allison's Model III.",
    makeDecision: () => Math.random() < 0.6 ? 'C' : 'D'
  }
];

export function getRandomDoctrine() {
  const idx = Math.floor(Math.random() * DIPLOMATIC_DOCTRINES.length);
  return DIPLOMATIC_DOCTRINES[idx];
}

export const PREDICTION_OPTIONS = [
  { id: 'CC', label: 'Mutual Cooperation (CC: Both Cooperate / Trust Expands)' },
  { id: 'DC', label: 'Unilateral Exploitation (DC: You Defect, Rival Cooperates / +10 Pts)' },
  { id: 'CD', label: 'Sucker Exploitation (CD: You Cooperate, Rival Defects / -10 Pts)' },
  { id: 'DD', label: 'Mutual Deterrence Conflict (DD: Both Defect / -2 Pts)' }
];

export const MASTERY_CHECKS = [
  {
    id: 'mc-01',
    title: 'Mastery Check 1: Doctrine Identification (History Alpha)',
    prompt: 'A rival delegation displays this 6-move interaction history against your dispatches:\nYour moves:  [C,  D,  D,  C,  C,  D]\nRival moves: [C,  C,  D,  D,  C,  C]\nWhich diplomatic doctrine is the rival executing?',
    choices: [
      { id: 'tft', text: 'Tit-for-Tat (Starts cooperative, then precisely mirrors your previous move)', correct: true },
      { id: 'grim', text: 'Grim Trigger (Cooperates until first betrayal, then defects forever)', correct: false, misconceptionTag: 'forgiveness-weakness' },
      { id: 'pavlov', text: 'Pavlov (Win-Stay / Lose-Shift based on payoff score)', correct: false },
      { id: 'predator', text: 'The Predator (Defects relentlessly across every round)', correct: false, misconceptionTag: 'always-defect' }
    ],
    remediation: 'Tit-for-Tat starts with cooperation and mirrors the opponent’s previous move on every subsequent turn.'
  },
  {
    id: 'mc-02',
    title: 'Mastery Check 2: Doctrine Identification (History Beta)',
    prompt: 'A rival delegation displays this 6-move interaction history:\nYour moves:  [C,  C,  D,  C,  C,  C]\nRival moves: [C,  C,  C,  D,  D,  D]\nAfter your single defection in Round 3, the rival never cooperated again despite your return to peaceful diplomacy. Which doctrine is this?',
    choices: [
      { id: 'grim', text: 'Grim Trigger (Unforgiving permanent retaliation upon the very first breach of trust)', correct: true },
      { id: 'tft', text: 'Tit-for-Tat (Would have forgiven and returned to cooperation in Round 5)', correct: false, misconceptionTag: 'forgiveness-weakness' },
      { id: 'wildcard', text: 'The Wildcard (Erratic domestic politics generating random stances)', correct: false },
      { id: 'pavlov', text: 'Pavlov (Would have shifted behavior after mutual defection)', correct: false }
    ],
    remediation: 'Grim Trigger maintains cooperation until a single betrayal occurs, triggering permanent, irreversible defection.'
  },
  {
    id: 'mc-03',
    title: 'Mastery Check 3: Doctrine Identification (History Gamma)',
    prompt: 'A rival delegation operates under these payoff responses:\n- Following mutual cooperation (CC, reward), it repeats C.\n- Following sucker payoff (CD, loss), it switches to D.\n- Following successful exploitation (DC, temptation), it repeats D.\n- Following mutual punishment (DD, loss), it switches back to C.\nWhich behavioral doctrine does this reflect?',
    choices: [
      { id: 'pavlov', text: 'Pavlov / Win-Stay, Lose-Shift (Repeats move if outcome was rewarding; flips move if outcome was punishing)', correct: true },
      { id: 'tft', text: 'Tit-for-Tat (Strictly mirrors opponent rather than evaluating payoff reward)', correct: false },
      { id: 'predator', text: 'The Predator (Never switches to cooperation regardless of payoff)', correct: false, misconceptionTag: 'always-defect' },
      { id: 'grim', text: 'Grim Trigger (Never returns to cooperation after mutual punishment DD)', correct: false, misconceptionTag: 'forgiveness-weakness' }
    ],
    remediation: 'Pavlov (Nowak & Sigmund 1993) embodies Win-Stay / Lose-Shift: repeat prior action if own payoff is R or T; switch action if own payoff is P or S.'
  }
];

export const TRANSFER_SCENARIO = {
  id: 'transfer-tariff-retaliation',
  title: 'Transfer Challenge: US-EU Tariff Retaliation Duel',
  context: 'In 2018, the United States imposed unilateral 25% tariffs on European steel and 10% on aluminium under Section 232 (a surprise defection from WTO norms). As the European Union Trade Commissioner, you must architect the European response under iterated game-theoretic principles.',
  prompt: 'Which strategic retaliation doctrine best embodies Axelrod’s four core properties (nice, provocable, forgiving, clear) to restore trade cooperation under international anarchy?',
  choices: [
    {
      id: 'opt_tft',
      text: 'Proportionate Rebalancing (Tit-for-Tat): Impose immediate, equivalent rebalancing tariffs on politically sensitive US exports (Harley-Davidson, bourbon, cranberries), with a legally binding commitment to lift tariffs the moment US tariffs are rescinded.',
      correct: true,
      feedback: 'Correct! This strategy satisfies all 4 of Axelrod’s axioms: nice (did not initiate defection), provocable (retaliated immediately, imposing political costs), forgiving (clear legal sunset upon compliance), and clear (transparent rules of engagement).'
    },
    {
      id: 'opt_grim',
      text: 'Prohibitive Embargo (Grim Trigger): Slap 100% tariffs across all US exports and indefinitely terminate all transatlantic trade negotiations.',
      correct: false,
      misconceptionTag: 'forgiveness-weakness',
      feedback: 'Incorrect. Grim Trigger destroys the possibility of reconciliation, locking both global superpowers into a permanent, welfare-destroying trade war.'
    },
    {
      id: 'opt_appease',
      text: 'Unilateral Concession (Sucker Stance): Absorb the tariffs with zero retaliation to preserve diplomatic goodwill and avoid escalation.',
      correct: false,
      misconceptionTag: 'beat-rival',
      feedback: 'Incorrect. In an anarchic system, unconditional cooperation invites continuous exploitation by opportunistic rivals.'
    },
    {
      id: 'opt_random',
      text: 'Erratic Volatility (Wildcard): Impose unpredictable, shifting weekly quotas to destabilize US financial markets.',
      correct: false,
      misconceptionTag: 'always-defect',
      feedback: 'Incorrect. Axelrod emphasizes that clarity is essential; unpredictable behavior prevents the opponent from recognizing the causal link between cooperation and reward.'
    }
  ]
};

export class DuelState {
  constructor(doctrine = null) {
    this.session = new LearningSession(LAB_ID, LEARNING_OBJECTIVES);
    this.doctrine = doctrine || getRandomDoctrine();
    this.reset();
  }

  reset() {
    this.round = 1;
    this.totalRounds = 8;
    this.sigintRound = 4;
    this.playerScore = 0;
    this.rivalScore = 0;
    this.streak = 0;
    this.maxStreak = 0;
    this.history = [];
    this.phase = 'BRIEFING'; // BRIEFING, PREDICTING, DECIDING, CONSEQUENCE, EXPLAIN, SIGINT, MASTERY, TRANSFER, DEBRIEF
    this.pendingPrediction = null;
    this.masteryIndex = 0;
    this.lastFeedback = null;
  }

  getMultiplier() {
    if (this.streak >= 4) return 2.0;
    if (this.streak >= 2) return 1.5;
    return 1.0;
  }

  recordPrediction(predictionKey) {
    this.pendingPrediction = predictionKey;
    this.session.recordPrediction(`round-${this.round}`, predictionKey);
    return predictionKey;
  }

  applyDecision(playerMove) {
    const rivalMove = this.doctrine.makeDecision(this.history);
    const key = `${playerMove}${rivalMove}`;
    const base = PAYOFF[key] || [0, 0];
    const mult = this.getMultiplier();

    let pDelta = 0;
    let rDelta = base[1];

    if (key === 'CC') {
      pDelta = Math.round(base[0] * mult);
      this.streak++;
      if (this.streak > this.maxStreak) this.maxStreak = this.streak;
    } else {
      pDelta = base[0];
      this.streak = 0;
    }

    this.playerScore += pDelta;
    this.rivalScore += rDelta;

    const roundData = {
      round: this.round,
      player: playerMove,
      rival: rivalMove,
      pDelta,
      rDelta,
      mult,
      key,
      cumulativePlayer: this.playerScore,
      cumulativeRival: this.rivalScore
    };
    this.history.push(roundData);

    // Pedagogical Feedback Assembly
    let outcome = 'success';
    let consequence = '';
    let mechanism = '';
    let citation = 'Axelrod (1984), The Evolution of Cooperation';
    let misconception = null;

    if (key === 'CC') {
      outcome = 'success';
      consequence = 'Both delegations ratified the bilateral treaty protocol. Trust capacitor surges, establishing a durable cooperative norm.';
      mechanism = 'Shadow of the Future: The expectation of ongoing interaction discounts short-term defection incentives, sustaining Pareto-optimal cooperation under anarchy.';
    } else if (key === 'DC') {
      outcome = 'partial';
      consequence = 'Your surprise defection secured short-term unilateral gains (+10 Pts), but shattered the diplomatic trust capacitor and provoked rival retaliatory postures.';
      mechanism = 'Temptation to Defect (T > R): Unilateral defection yields temporary advantage under single-round incentives, but destroys mutual goodwill in repeated play.';
      misconception = MISCONCEPTIONS['beat-rival'];
    } else if (key === 'CD') {
      outcome = 'failure';
      consequence = 'Your cooperative concession was exploited by an aggressive rival probe (-10 Pts), inflicting severe sucker payoff losses.';
      mechanism = 'Sucker Payoff (S < P): Altruism without provocability invites predation in an anarchic environment lacking centralized supranational enforcement.';
      misconception = MISCONCEPTIONS['forgiveness-weakness'];
    } else {
      // DD
      outcome = 'failure';
      consequence = 'Both delegations defected into mutual deterrence deadlock (-2 Pts). Bilateral diplomatic relations remain frozen in a low-yield conflict trap.';
      mechanism = 'Security Dilemma / Nash Equilibrium: In the absence of enforceable trust or calibrated forgiveness, mutual fear locks rational actors into Pareto-suboptimal conflict.';
      misconception = MISCONCEPTIONS['always-defect'];
    }

    const predictionMatch = (this.pendingPrediction === key);

    // Optimal choice depends on opponent doctrine: against cooperative doctrines (TFT, Grim, Pavlov), C is optimal. Against Predator, D is defensive minimax.
    const correctChoice = (this.doctrine.id === 'predator') ? 'D' : 'C';

    this.session.recordDecision({
      decisionId: `round-${this.round}`,
      choice: playerMove,
      correctChoice: correctChoice,
      rationale: mechanism,
      misconceptionTag: misconception ? misconception.tag : null,
      misconception: misconception,
      predicted: this.pendingPrediction,
      actual: key,
      outcome: outcome,
      consequence: consequence,
      mechanism: mechanism,
      citation: citation,
      objectiveIndex: (this.round <= 4 ? 0 : 2)
    });

    this.lastFeedback = {
      outcome,
      consequence,
      mechanism,
      citation,
      misconception,
      predictionMatch,
      playerMove,
      rivalMove,
      key,
      pDelta,
      rDelta,
      round: this.round
    };

    return this.lastFeedback;
  }

  answerMastery(choiceId) {
    const q = MASTERY_CHECKS[this.masteryIndex];
    if (!q) return null;
    const choice = q.choices.find(c => c.id === choiceId);
    const isCorrect = choice ? !!choice.correct : false;

    this.session.recordMasteryCheck({
      questionId: q.id,
      chosen: choiceId,
      correct: q.choices.find(c => c.correct)?.id,
      misconceptionTag: choice?.misconceptionTag ? MISCONCEPTIONS[choice.misconceptionTag] : null,
      objectiveIndex: 1
    });

    return {
      isCorrect,
      remediation: q.remediation,
      questionId: q.id,
      masteryIndex: this.masteryIndex
    };
  }

  answerTransfer(choiceId) {
    const choice = TRANSFER_SCENARIO.choices.find(c => c.id === choiceId);
    const isCorrect = choice ? !!choice.correct : false;

    this.session.recordTransfer({
      scenarioId: TRANSFER_SCENARIO.id,
      choice: choiceId,
      correct: TRANSFER_SCENARIO.choices.find(c => c.correct)?.id,
      objectiveIndex: 2
    });

    return {
      isCorrect,
      feedback: choice?.feedback || '',
      scenarioId: TRANSFER_SCENARIO.id
    };
  }

  getStars() {
    return this.session.getStars();
  }

  getReport() {
    return this.session.getReport();
  }
}
