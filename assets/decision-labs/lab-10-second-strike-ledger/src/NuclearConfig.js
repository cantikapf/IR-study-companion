import { LearningSession } from '../../shared/learn/LearningSession.js';
import { chaptersFor } from '../../shared/learn/ChapterLink.js';

export const NUCLEAR_CONFIG = {
  TOTAL_YEARS: 4,
  MAX_BUDGET: 100
};

export const NUCLEAR_OBJECTIVES = [
  'Explain the strategic triad rationale: silo dispersal, submarine survivability, and bomber flexibility.',
  'Explain why a secure, invulnerable second strike underwrites Mutual Assured Destruction (MAD).',
  'Explain how Anti-Ballistic Missile (ABM) defenses destabilize deterrence under the Schelling defense dilemma.'
];

export const NUCLEAR_SCENARIOS = [
  {
    year: 1,
    id: 'fy-1974',
    title: 'FY 1974: Hypersonic Counterforce Upgrade',
    desc: 'The adversary deploys high-accuracy MIRVed SS-18 Satan ICBMs targeted directly at land-based silo fields.',
    stressLeg: 'icbm',
    theory: 'Vulnerability of land-based silos creates a "use-them-or-lose-them" first-strike temptation.',
    predictionPrompt: 'Which leg of the strategic triad is acutely threatened by adversary high-accuracy MIRVed counterforce missiles, creating a severe "use-them-or-lose-them" crisis dilemma?',
    predictionOptions: [
      { key: 'A', text: 'Land-based ICBM silos due to their fixed, known geographic coordinates.' },
      { key: 'B', text: 'Deep-ocean SSBN ballistic submarines operating under silent thermal layers.' },
      { key: 'C', text: 'Strategic interceptor airfields stationed along the coastal rim.' }
    ],
    expectedPrediction: 'A'
  },
  {
    year: 2,
    id: 'fy-1975',
    title: 'FY 1975: Ocean Bastion Anti-Submarine Sonar Barrier',
    desc: 'Adversary deploys passive SOSUS undersea hydrophone arrays and hunter-killer attack submarines along patrol corridors.',
    stressLeg: 'slbm',
    theory: 'Submarine survivability is the ultimate pillar of assured second-strike retaliation.',
    predictionPrompt: 'Why does the adversary prioritize deep-sea SOSUS acoustic arrays and hunter-killer submarines in forward patrol zones?',
    predictionOptions: [
      { key: 'A', text: 'To strip away the ultimate invulnerable pillar of assured retaliatory second-strike capability (SLBMs).' },
      { key: 'B', text: 'To enforce commercial fishing exclusive economic zone boundaries.' },
      { key: 'C', text: 'To detect and shoot down high-altitude subsonic heavy bombers.' }
    ],
    expectedPrediction: 'A'
  },
  {
    year: 3,
    id: 'fy-1976',
    title: 'FY 1976: Strategic Air Defense Interceptor Radar Wall',
    desc: 'Adversary erects dense S-200 surface-to-air missile belts and MiG-25 Foxbat high-altitude interceptor squadrons.',
    stressLeg: 'bomber',
    theory: 'Heavy bombers provide visible crisis signaling and recallability, but suffer high attrition against modern IADS.',
    predictionPrompt: 'Despite heavy air defense attrition against modern IADS radar belts, what unique strategic utility does the manned bomber leg provide in nuclear crises?',
    predictionOptions: [
      { key: 'A', text: 'Bombers provide visible crisis signaling, airborne dispersal, and human recallability prior to weapon release.' },
      { key: 'B', text: 'Bombers are completely undetectable by any radar or thermal detection arrays.' },
      { key: 'C', text: 'Bombers incur zero maintenance, fuel, or personnel budget costs.' }
    ],
    expectedPrediction: 'A'
  },
  {
    year: 4,
    id: 'fy-1977',
    title: 'FY 1977: Anti-Ballistic Missile (ABM) Radar Shield',
    desc: 'Adversary tests exo-atmospheric ABM interceptors capable of neutralizing thin retaliatory strikes.',
    stressLeg: 'defense',
    theory: 'Strategic defenses destabilize MAD: a state with missile defense may believe it can survive a retaliatory second strike.',
    predictionPrompt: 'According to Thomas Schelling, what dangerous paradox occurs if either superpower heavily expands its ABM missile defense shield (> $25B)?',
    predictionOptions: [
      { key: 'A', text: 'It creates a first-strike incentive: the defender may believe its shield can absorb a ragged retaliatory strike, provoking preemptive attack.' },
      { key: 'B', text: 'It guarantees permanent, risk-free peace by eliminating all offensive threats.' },
      { key: 'C', text: 'It automatically halts adversary counterforce missile modernization spending.' }
    ],
    expectedPrediction: 'A'
  }
];

export const NUCLEAR_MASTERY_QUESTIONS = [
  {
    id: 'mastery-1',
    prompt: 'Under neorealist deterrence theory, why is a survivable second-strike capability — rather than numerical warhead superiority — considered the bedrock of strategic stability?',
    options: [
      { key: 'A', text: 'It enables a state to launch a surprise decapitation strike without fear of international diplomatic condemnation.' },
      { key: 'B', text: 'It guarantees that even after absorbing an adversary\'s all-out surprise first strike, the surviving retaliatory force will inflict unacceptable destruction, removing any rational incentive to attack.' },
      { key: 'C', text: 'It eliminates the financial need to maintain standing conventional army and naval forces.' },
      { key: 'D', text: 'It ensures complete diplomatic cooperation between ideological adversaries.' }
    ],
    correct: 'B',
    rationale: 'Under Waltz (1981) and Jervis (1989), deterrence depends not on the ability to win a war, but on the certainty that the victim of a first strike can still retaliate with unacceptable devastating punishment.',
    citation: 'Waltz (1981), The Spread of Nuclear Weapons / Jervis (1989), The Meaning of the Nuclear Revolution'
  },
  {
    id: 'mastery-2',
    prompt: 'Which leg of the Strategic Triad provides the most invulnerable second-strike insurance against a counterforce attack, and which leg provides unique operational recallability and flexible signaling in an escalating crisis?',
    options: [
      { key: 'A', text: 'ICBM silos are the most survivable; SLBM submarines provide the greatest recallability.' },
      { key: 'B', text: 'Ballistic missile submarines (SLBMs) provide the ultimate survivable retaliatory reserve; strategic bombers provide human recallability and de-escalatory signaling flexibility.' },
      { key: 'C', text: 'Fixed land-based silos provide both the greatest survivability and greatest crisis signaling flexibility.' },
      { key: 'D', text: 'Ballistic missile defense interceptors provide both second-strike retaliation and recallability.' }
    ],
    correct: 'B',
    rationale: 'SSBN submarines are virtually untargetable when submerged on deep-ocean patrol, guaranteeing retaliation. Strategic bombers can be launched to signal readiness and recalled if diplomacy succeeds, unlike ballistic missiles which cannot be recalled once fired.',
    citation: 'Freedman (2003), The Evolution of Nuclear Strategy / Jervis (1989)',
    misconception: {
      tag: 'misc-triad-redundancy',
      label: 'Triad Homogeneity Assumption',
      remediation: 'The triad is intentionally asymmetric: silos draw adversary warheads away from cities, submarines ensure retaliation, and bombers provide crisis signaling.'
    }
  },
  {
    id: 'mastery-3',
    prompt: 'According to Thomas Schelling and crisis stability theory, why did the 1972 ABM Treaty ban extensive ballistic missile defense shields?',
    options: [
      { key: 'A', text: 'Strategic defenses were recognized as destabilizing: a state possessing an ABM shield might believe it could launch a counterforce first strike and intercept the adversary\'s degraded retaliatory strike, creating severe preemption panic.' },
      { key: 'B', text: 'Both superpowers lacked the technological capacity to build radar detection equipment.' },
      { key: 'C', text: 'Missile defense shields were considered offensive weapons under the Geneva Conventions.' },
      { key: 'D', text: 'The United Nations Charter forbids states from intercepting ballistic projectiles.' }
    ],
    correct: 'A',
    rationale: 'Schelling showed that defense and offense are intertwined in nuclear strategy: a defense that cannot stop a first strike CAN stop a ragged retaliatory second strike, which tempts a first strike and panics the adversary into preemption.',
    citation: 'Schelling (1960), The Strategy of Conflict / Jervis (1989)',
    misconception: {
      tag: 'misc-defense-always-good',
      label: 'Defensive Advantage Fallacy',
      remediation: 'In a MAD world, mutual vulnerability is what preserves peace; attempting to eliminate vulnerability threatens the rival\'s deterrent and sparks preemption.'
    }
  }
];

export const NUCLEAR_TRANSFER_SCENARIO = {
  id: 'transfer-abm-withdrawal',
  title: '1972 ABM Treaty & the 2002 US Withdrawal',
  context: 'In 1972, Washington and Moscow codified the Anti-Ballistic Missile (ABM) Treaty to intentionally preserve mutual second-strike vulnerability. In June 2002, the United States formally withdrew from the treaty to construct national missile defenses in Alaska and Poland. In response, Russia and China accelerated development of hypersonic glide vehicles (Avangard, DF-17) and underwater nuclear drones (Poseidon).',
  prompt: 'How does structural deterrence theory explain why the 2002 ABM Treaty withdrawal triggered major counter-balancing weapons programs by rival nuclear powers?',
  options: [
    { key: 'A', text: 'Rival powers feared that future US missile defense could neutralize their second-strike deterrent, prompting them to develop hypersonic penetration weapons to restore assured retaliation, as predicted by the security dilemma.' },
    { key: 'B', text: 'Rival powers completely disarmed their nuclear arsenals because US missile defenses made nuclear weapons technologically obsolete.' },
    { key: 'C', text: 'The withdrawal immediately led to a binding multilateral disarmament treaty under the UN Security Council.' },
    { key: 'D', text: 'Rival states shifted their procurement entirely into conventional tank formations.' }
  ],
  correct: 'A',
  rationale: 'The 2002 ABM withdrawal validated Jervis\'s security dilemma: US efforts to increase security through defense were perceived by Russia and China as a bid for first-strike impunity, forcing them to engineer hypersonic penetration weapons to restore second-strike certainty.',
  citation: 'Jervis (1989), The Meaning of the Nuclear Revolution / Lieber & Press (2006), The Rise of U.S. Nuclear Primacy'
};

export class NuclearState {
  constructor() {
    this.learningSession = new LearningSession('lab-10', NUCLEAR_OBJECTIVES);
    this.reset();
  }

  reset() {
    this.year = 1;
    this.alloc = {
      icbm: 25,
      slbm: 35,
      bomber: 20,
      defense: 20
    };
    this.stability = 75;
    this.history = [];
    this.phase = 'BRIEF'; // BRIEF, PREDICT, DECIDE, CONSEQUENCE, MASTERY, TRANSFER, DEBRIEF
    this.crisisTriggered = false;
    this.abmDestabilized = false;
    this.lastFeedback = null;
    this.masteryIndex = 0;
    this.masteryAnswers = [];
    this.transferAnswer = null;
  }

  setAllocation(leg, value) {
    this.alloc[leg] = value;
  }

  getTotalBudget() {
    return Object.values(this.alloc).reduce((a, b) => a + b, 0);
  }

  recordPrediction(choiceKey) {
    const sc = NUCLEAR_SCENARIOS[this.year - 1];
    if (!sc) return;
    this.learningSession.recordPrediction(sc.id, choiceKey);
    this.phase = 'DECIDE';
  }

  simulateYearEnd() {
    const sc = NUCLEAR_SCENARIOS[this.year - 1];

    const thresholds = {
      icbm: 20,
      slbm: 30,
      bomber: 15,
      defense: 15
    };

    if (sc && sc.stressLeg && thresholds[sc.stressLeg] !== undefined) {
      thresholds[sc.stressLeg] += 10;
    }

    const icbmSurv = this.alloc.icbm >= thresholds.icbm;
    const slbmSurv = this.alloc.slbm >= thresholds.slbm;
    const bomberSurv = this.alloc.bomber >= thresholds.bomber;
    const defSurv = this.alloc.defense >= thresholds.defense;

    let survivingLegs = 0;
    if (icbmSurv) survivingLegs++;
    if (slbmSurv) survivingLegs++;
    if (bomberSurv) survivingLegs++;

    const isAbmDestabilized = this.alloc.defense > 25;
    this.abmDestabilized = isAbmDestabilized;

    const stressedSurv = sc && sc.stressLeg ? (
      sc.stressLeg === 'defense' ? defSurv : (
        sc.stressLeg === 'icbm' ? icbmSurv : (
          sc.stressLeg === 'slbm' ? slbmSurv : bomberSurv
        )
      )
    ) : true;

    // Calculate stability
    let delta = 0;
    const isSuccess = survivingLegs >= 2 && slbmSurv && stressedSurv && defSurv && !isAbmDestabilized;

    if (isSuccess) {
      delta = 10;
      this.crisisTriggered = false;
    } else {
      delta = -20;
      this.crisisTriggered = true;
    }

    this.stability = Math.max(0, Math.min(100, this.stability + delta));

    // Construct full educational feedback payload
    const predicted = sc ? this.learningSession._predictions.get(sc.id) : undefined;
    const predictionMatch = (predicted === (sc ? sc.expectedPrediction : 'A'));

    let consequence = '';
    let mechanism = '';
    let citation = 'Schelling (1960), The Strategy of Conflict / Jervis (1989), The Meaning of the Nuclear Revolution';
    let misconception = null;

    if (isSuccess) {
      consequence = `Mutual Assured Destruction (MAD) preserved (+10% Stability). Triad redundancy and secure second-strike posture successfully deter adversary counterforce options.`;
      mechanism = 'Mutual Assured Destruction & Second-Strike Inviolability';
    } else {
      if (isAbmDestabilized) {
        consequence = `CRITICAL CRISIS INSTABILITY! Heavy missile defense spending ($${this.alloc.defense}B > $25B safe ceiling) triggers the Schelling defense dilemma. The adversary perceives a US bid for first-strike impunity (-20% Stability).`;
        mechanism = 'Schelling ABM Defense Dilemma & Preemption Panic';
        misconception = {
          tag: 'misc-defense-always-good',
          label: 'Defensive Advantage Fallacy',
          remediation: 'In a MAD environment, extensive missile defense destabilizes deterrence because it blunts the adversary\'s retaliatory second strike, incentivizing preemptive first-strike desperation.'
        };
      } else if (!slbmSurv) {
        consequence = `CATASTROPHIC DETERRENCE COLLAPSE! Undersea SLBM allocation ($${this.alloc.slbm}B < $${thresholds.slbm}B) compromised by adversary SOSUS arrays. Without invulnerable submarine survivability, second-strike deterrence disintegrates (-20% Stability).`;
        mechanism = 'Submarine Invisibility & Assured Retaliation Pillar';
        misconception = {
          tag: 'misc-triad-redundancy',
          label: 'Leg Equivalence Fallacy',
          remediation: 'SLBMs are the indispensable, untargetable anchor of the nuclear triad; losing submarine survivability destroys second-strike deterrence regardless of silo numbers.'
        };
      } else if (!stressedSurv) {
        consequence = `COUNTERFORCE BREACH! Stressed leg (${sc.stressLeg.toUpperCase()}: $${this.alloc[sc.stressLeg]}B < $${thresholds[sc.stressLeg]}B) neutralized by adversary modernization breakthroughs (-20% Stability).`;
        mechanism = 'Counterforce Vulnerability & Use-Them-or-Lose-Them Dynamic';
        misconception = {
          tag: 'misc-warhead-count',
          label: 'Gross Parity Illusion',
          remediation: 'Deterrence stability is not about raw warhead counts; targeted adversary breakthroughs must be actively met with survivability investments.'
        };
      } else {
        consequence = `TRIAD REDUNDANCY ATTRITION! Insufficient surviving legs to guarantee a survivable counter-value retaliation (-20% Stability).`;
        mechanism = 'Triad Redundancy Breakdown';
      }
    }

    const payload = {
      outcome: isSuccess ? 'success' : 'failure',
      consequence,
      mechanism,
      citation,
      misconception,
      predictionMatch
    };

    if (sc) {
      this.learningSession.recordDecision({
        decisionId: sc.id,
        choice: `ICBM:${this.alloc.icbm}/SLBM:${this.alloc.slbm}/BOMBER:${this.alloc.bomber}/DEF:${this.alloc.defense}`,
        correctChoice: 'BALANCED_TRIAD_WITH_RESTRICTED_ABM',
        rationale: consequence,
        misconception,
        predicted,
        actual: sc.expectedPrediction,
        outcome: payload.outcome,
        consequence,
        mechanism,
        citation,
        objectiveIndex: Math.min(this.year - 1, NUCLEAR_OBJECTIVES.length - 1)
      });
    }

    this.lastFeedback = payload;
    this.phase = 'CONSEQUENCE';

    this.history.push({
      year: this.year,
      scenario: sc ? sc.title : `FY ${this.year}`,
      survivingLegs,
      slbmSurv,
      defSurv,
      stressedSurv,
      abmDestabilized: isAbmDestabilized,
      stability: this.stability
    });

    return {
      sc,
      survivingLegs,
      slbmSurv,
      defSurv,
      stability: this.stability,
      crisis: this.crisisTriggered,
      abmDestabilized: isAbmDestabilized,
      payload
    };
  }

  advanceYear() {
    this.year++;
    this.crisisTriggered = false;
    if (this.year <= NUCLEAR_CONFIG.TOTAL_YEARS && this.stability > 0) {
      this.phase = 'PREDICT';
      return true;
    }
    this.phase = 'MASTERY';
    return false;
  }

  getCurrentMasteryQuestion() {
    return NUCLEAR_MASTERY_QUESTIONS[this.masteryIndex] || null;
  }

  answerMasteryQuestion(chosenKey) {
    const q = this.getCurrentMasteryQuestion();
    if (!q) return null;

    const isCorrect = (chosenKey === q.correct);
    this.learningSession.recordMasteryCheck({
      questionId: q.id,
      chosen: chosenKey,
      correct: q.correct,
      misconceptionTag: isCorrect ? null : (q.misconception ? q.misconception.tag : 'misc-nuclear')
    });

    this.masteryAnswers.push({
      questionId: q.id,
      chosen: chosenKey,
      isCorrect,
      rationale: q.rationale,
      citation: q.citation,
      misconception: isCorrect ? null : q.misconception
    });

    this.masteryIndex++;
    if (this.masteryIndex >= NUCLEAR_MASTERY_QUESTIONS.length) {
      this.phase = 'TRANSFER';
    }

    return { isCorrect, rationale: q.rationale, citation: q.citation, misconception: q.misconception };
  }

  answerTransfer(chosenKey) {
    const isCorrect = (chosenKey === NUCLEAR_TRANSFER_SCENARIO.correct);
    this.learningSession.recordTransfer({
      scenarioId: NUCLEAR_TRANSFER_SCENARIO.id,
      choice: chosenKey,
      correct: NUCLEAR_TRANSFER_SCENARIO.correct
    });

    this.transferAnswer = {
      chosen: chosenKey,
      isCorrect,
      rationale: NUCLEAR_TRANSFER_SCENARIO.rationale,
      citation: NUCLEAR_TRANSFER_SCENARIO.citation
    };

    this.phase = 'DEBRIEF';
    return {
      isCorrect,
      rationale: NUCLEAR_TRANSFER_SCENARIO.rationale,
      citation: NUCLEAR_TRANSFER_SCENARIO.citation
    };
  }

  getStars() {
    if (this.phase === 'DEBRIEF' && this.learningSession) {
      return this.learningSession.getStars();
    }
    if (this.stability <= 0) return 0;
    if (this.stability >= 80) return 3;
    if (this.stability >= 50) return 2;
    return 1;
  }

  getReport() {
    return this.learningSession.getReport();
  }
}
