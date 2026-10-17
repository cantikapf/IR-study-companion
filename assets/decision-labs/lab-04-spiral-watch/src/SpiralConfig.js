import { LearningSession } from '../../shared/learn/LearningSession.js';
import { chaptersFor, chapterUrl } from '../../shared/learn/ChapterLink.js';

export const LAB_ID = 'lab-04';

export const LEARNING_OBJECTIVES = [
  'Distinguish Jervis\'s spiral model from the deterrence model.',
  'Explain how offence–defence indistinguishability produces unintended escalation.',
  'Explain the function of CBMs and verification.'
];

export const MISCONCEPTIONS = {
  'more-arms-safer': {
    tag: 'more-arms-safer',
    label: 'Cumulative Arms Fallacy',
    remediation: 'In a security dilemma, unilateral military buildup reduces the rival\'s security, provoking reciprocal arms procurement that leaves both states more vulnerable than before.'
  },
  'capability-equals-intent': {
    tag: 'capability-equals-intent',
    label: 'Capability-Intent Equivalence Fallacy',
    remediation: 'Because defensive weapons often look offensive to a fearful neighbor (offence–defence indistinguishability), weapon capability does not directly prove hostile intent.'
  },
  'restraint-is-weakness': {
    tag: 'restraint-is-weakness',
    label: 'Restraint-as-Weakness Fallacy',
    remediation: 'Verifiable confidence-building measures (CBMs) signal benign defensive intent without surrendering deterrent capability, arresting tragic escalation spirals.'
  }
};

export const POSTURES = [
  {
    id: 'defensive-radar',
    title: 'Defensive Early-Warning Fortification',
    shortTitle: 'Defensive Fortification',
    desc: 'Construct hardened perimeter radar arrays and sensor outposts. Maximizes warning time with near-zero offensive projection capability.',
    type: 'DEFENSIVE',
    deltaAgainstCautious: 12,
    deltaAgainstOpportunist: 10,
    blipChange: 'DEFENSE_RADAR',
    feedback: {
      consequence: 'Early-warning radar perimeter established. Alpha reduces vulnerability to surprise attack without deploying weapons that threaten Beta\'s homeland.',
      mechanism: 'Offence–Defence Differentiation: Weapons with pure defensive utility enhance territorial defence without provoking reciprocal security dilemma spirals.',
      citation: 'Robert Jervis (1978), Cooperation Under the Security Dilemma, World Politics 30(2), pp. 186-214'
    }
  },
  {
    id: 'forward-strike',
    title: 'Forward Strike Missile Regiments',
    shortTitle: 'Forward Strike Missiles',
    desc: 'Deploy mobile theater ballistic missiles directly along the DMZ. Provides preemptive strike options, but shrinks rival decision warning time to 4 minutes.',
    type: 'OFFENSIVE',
    deltaAgainstCautious: -18,
    deltaAgainstOpportunist: -15,
    blipChange: 'OFFENSIVE_BLIP',
    feedback: {
      consequence: 'Forward strike regiments deployed. State Beta detects high-readiness offensive capability and initiates hair-trigger alert dispersal.',
      mechanism: 'The Spiral Model: When capabilities are offensive, the adversary interprets deployment as aggressive revisionism and mobilizes in self-defense.',
      citation: 'Robert Jervis (1976), Perception and Misperception in International Politics, ch. 3',
      misconception: MISCONCEPTIONS['more-arms-safer']
    }
  },
  {
    id: 'verified-cbm',
    title: 'Verified CBM Demilitarization Protocol',
    shortTitle: 'Verified CBM Protocol',
    desc: 'Pull heavy forces 50km back from the frontier, install open-skies observation flights, and activate direct bilateral military hotlines.',
    type: 'COOPERATIVE',
    deltaAgainstCautious: 16,
    deltaAgainstOpportunist: 14,
    blipChange: 'CLEAR_BLIP',
    feedback: {
      consequence: 'Confidence-Building Measures (CBMs) implemented. Joint aerial surveillance confirms troop withdrawal, dispelling worst-case assumptions.',
      mechanism: 'Institutional Verification: Costly signaling and transparency diminish information asymmetry under structural anarchy.',
      citation: 'Charles L. Glaser (1997), The Security Dilemma Revisited, World Politics 50(1), pp. 171-201',
      misconception: MISCONCEPTIONS['restraint-is-weakness']
    }
  }
];

export const BETA_ARCHETYPES = [
  {
    type: 'CAUTIOUS_REACTIVE',
    name: 'Cautious Reactive (Spiral Model / Defensive Realism)',
    theory: 'State Beta operates purely under defensive security dilemma logic (Robert Jervis). It is motivated by fear of surprise attack, not territorial conquest. It mirrors de-escalation when reassurance is verifiable, but mobilizes aggressively if it perceives offensive threats.',
    sigint: 'SIGINT DECRYPT: Beta General Staff doctrine prioritizes homeland survival. If Alpha adopts non-threatening defensive postures or CBMs, Beta will stand down. Avoid forward offensive missile deployments.',
    expectedAttribution: 'FEAR',
    makeDecision: (alphaChoice, history) => {
      if (alphaChoice === 'forward-strike') {
        return {
          postureId: 'forward-strike',
          name: 'Forward Strike Mobilization',
          reason: 'Fearing preemptive destruction, Beta scrambles counterforce missile regiments in self-defense.'
        };
      }
      if (alphaChoice === 'verified-cbm') {
        return {
          postureId: 'verified-cbm',
          name: 'Verified De-escalation Protocol',
          reason: 'Beta verifies Alpha\'s troop pull-back and reciprocates with mutual demilitarization.'
        };
      }
      // defensive-radar
      return {
        postureId: 'verified-cbm',
        name: 'Defensive Stand-Down',
        reason: 'Beta notes Alpha\'s radar poses zero offensive invasion threat and reduces alert readiness.'
      };
    }
  },
  {
    type: 'OPPORTUNISTIC',
    name: 'Opportunistic Revisionist (Deterrence Model / Offensive Realism)',
    theory: 'State Beta views peace as an exploitable opening (John Mearsheimer / Deterrence Model). It expands into power vacuums when Alpha unilateral disarms, but is firmly deterred when Alpha maintains resolute defensive fortifications combined with verifiable CBMs.',
    sigint: 'SIGINT DECRYPT: Beta High Command directive: "Probe Alpha\'s frontier. If Alpha leaves the border unfortified without deterrence, advance missile units. If Alpha maintains impenetrable defenses, accept bilateral treaty."',
    expectedAttribution: 'REVISIONIST',
    makeDecision: (alphaChoice, history) => {
      if (alphaChoice === 'forward-strike') {
        return {
          postureId: 'forward-strike',
          name: 'Symmetric Arms Race Escalation',
          reason: 'Beta matches Alpha\'s offensive missile escalation to preserve competitive parity.'
        };
      }
      if (alphaChoice === 'defensive-radar') {
        return {
          postureId: 'verified-cbm',
          name: 'Deterred Restraint Protocol',
          reason: 'Faced with Alpha\'s unbreachable defensive warning perimeter, Beta abandons expansion and accepts verification.'
        };
      }
      // verified-cbm
      const hadDefensivePrep = history.some(h => h.playerChoice === 'defensive-radar');
      if (hadDefensivePrep) {
        return {
          postureId: 'verified-cbm',
          name: 'Verified Treaty Ratification',
          reason: 'Respecting Alpha\'s underlying defensive readiness, Beta commits to mutual buffer inspections.'
        };
      }
      // Unilateral concession without defense -> Opportunistic exploit
      return {
        postureId: 'forward-strike',
        name: 'Opportunistic Forward Deployment',
        reason: 'Beta exploits Alpha\'s unfortified border by moving missile regiments into the DMZ buffer.'
      };
    }
  }
];

export const MASTERY_CHECKS = [
  {
    id: 'mc-04-01',
    question: 'State Beta installs short-range surface-to-air missile radar batteries stationed 100km behind its international frontier with fixed defensive geography. An intelligence memo argues this proves Beta intends to invade tomorrow. Why is this reasoning flawed under Jervis\'s security dilemma?',
    choices: [
      {
        id: 'c1',
        text: 'Air-defense radars possess high defensive utility and near-zero offensive projection; assuming offensive intent confuses defensive capability with aggression.',
        correct: true
      },
      {
        id: 'c2',
        text: 'Any military procurement of any kind is always an offensive preparation for war.',
        correct: false
      },
      {
        id: 'c3',
        text: 'State Beta signed a television interview declaring eternal friendship.',
        correct: false
      }
    ],
    objectiveIndex: 1,
    explanation: 'Robert Jervis emphasizes offence–defence differentiation: weapons that defend sovereign airspace without the capability to seize enemy territory do not threaten neighbors and therefore avoid security dilemma spirals.',
    misconception: MISCONCEPTIONS['capability-equals-intent']
  },
  {
    id: 'mc-04-02',
    question: 'State Beta begins deploying road-mobile counterforce ballistic missiles with 4-minute flight times to our silos, while simultaneously expelling neutral border monitors. How should an analyst classify this strategic posture?',
    choices: [
      {
        id: 'c1',
        text: 'Revisionist / Offensive posture: Deterrence model applies because short flight-time counterforce weapons threaten second-strike survivability.',
        correct: true
      },
      {
        id: 'c2',
        text: 'Purely benign defensive posturing that should be met with complete unilateral disarmament.',
        correct: false
      },
      {
        id: 'c3',
        text: 'An organizational accounting error with no strategic consequence.',
        correct: false
      }
    ],
    objectiveIndex: 0,
    explanation: 'Under the Deterrence Model, capabilities tailored for preemptive first strikes create offensive advantages that encourage aggression unless deterred by robust defense and secure retaliation.',
    misconception: MISCONCEPTIONS['more-arms-safer']
  },
  {
    id: 'mc-04-03',
    question: 'Following an unannounced, unscheduled military exercise along the frontier, State Beta mobilizes border reserves. Our field commander argues: "Beta is executing an unprovoked blitzkrieg." What does Jervis\'s spiral model explain about Beta\'s action?',
    choices: [
      {
        id: 'c1',
        text: 'Beta\'s mobilization is a fear-driven reaction to our unannounced maneuvers; ambiguous signals provoke defensive counter-escalation.',
        correct: true
      },
      {
        id: 'c2',
        text: 'Beta has unlimited military reserves and was going to mobilize regardless of our actions.',
        correct: false
      },
      {
        id: 'c3',
        text: 'Unannounced troop maneuvers are completely invisible to adversary radar.',
        correct: false
      }
    ],
    objectiveIndex: 2,
    explanation: 'The Spiral Model shows how uncoordinated or ambiguous military moves trigger acute fear in an adversary. Bilateral Confidence-Building Measures (CBMs), such as advance notification of military exercises, prevent these spirals.',
    misconception: MISCONCEPTIONS['restraint-is-weakness']
  }
];

export const TRANSFER_SCENARIO = {
  id: 'transfer-india-pakistan',
  title: 'Transfer Case: India–Pakistan 1998–2002 Crisis Stability',
  historicalContext: 'Following the May 1998 Pokhran-II and Chagai-I nuclear tests, India and Pakistan faced severe security dilemma risks. In 1999, the Kargil conflict erupted along the Line of Control, and in 2002 (Operation Parakram), nearly 1 million troops mobilized along the international frontier. With flight times for ballistic missiles (Prithvi and Ghauri) under 5 minutes and high offence-defence ambiguity, false radar contacts risked accidental nuclear escalation.',
  question: 'Apply Jervis\'s security dilemma framework: In an environment characterized by offence–defence indistinguishability and compressed warning times, which institutional mechanism proved most effective in preventing catastrophic escalation?',
  choices: [
    {
      id: 'tf-cbm',
      text: 'Bilateral verifiable Confidence-Building Measures (CBMs) — including mandatory advance notification of ballistic missile flight tests, dedicated military DGMO hotlines, and nuclear non-attack agreements.',
      correct: true
    },
    {
      id: 'tf-strike',
      text: 'Unilateral preemptive strike doctrines targeting rival command bunkers during peak border tensions.',
      correct: false
    },
    {
      id: 'tf-blackout',
      text: 'Severing all direct communication lines and maintaining maximum secrecy regarding missile deployments.',
      correct: false
    }
  ],
  objectiveIndex: 2,
  explanation: 'Under acute crisis instability and compressed decision horizons, verifiable CBMs (such as the Lahore Declaration protocols and missile test notification pacts) separate defensive readiness from surprise attack preparation, providing the vital institutional insulation necessary to survive security dilemma spirals.',
  citation: 'Sumit Ganguly (2008), Nuclear Stability in South Asia; Robert Jervis (1978), Cooperation Under the Security Dilemma'
};

export class SpiralState {
  constructor(forcedArchetype = null) {
    this.forcedArchetype = forcedArchetype;
    this.reset();
  }

  reset() {
    this.round = 1;
    this.stability = 50; // starts at 50%
    this.phase = 'BRIEF'; // BRIEF, PREDICT, DECIDE, CONSEQUENCE, EXPLAIN, ATTRIBUTION, MASTERY, TRANSFER, DEBRIEF
    this.session = new LearningSession(LAB_ID, LEARNING_OBJECTIVES);
    this.betaArchetype = this.forcedArchetype || BETA_ARCHETYPES[Math.floor(Math.random() * BETA_ARCHETYPES.length)];
    this.history = [];
    this.radarBlips = [
      { id: 'init-1', x: -60, y: -25, type: 'strike', alpha: 0.8 },
      { id: 'init-2', x: 45, y: 35, type: 'strike', alpha: 0.6 }
    ];
    this.currentPrediction = null;
    this.lastTurnFeedback = null;
    this.masteryIndex = 0;
    this.transferAnswered = false;
  }

  recordPrediction(predictionId) {
    const decisionId = `round-${this.round}`;
    this.currentPrediction = predictionId;
    this.session.recordPrediction(decisionId, predictionId);
  }

  applyTurn(playerChoiceId) {
    const posture = POSTURES.find(p => p.id === playerChoiceId) || POSTURES[0];
    const betaResponse = this.betaArchetype.makeDecision(playerChoiceId, this.history);

    // Calculate stability impact
    let delta = 0;
    const isCautious = (this.betaArchetype.type === 'CAUTIOUS_REACTIVE');
    if (playerChoiceId === 'forward-strike' && betaResponse.postureId === 'forward-strike') {
      delta = -22; // mutual spiral
    } else if (playerChoiceId === 'verified-cbm' && betaResponse.postureId === 'verified-cbm') {
      delta = 18; // mutual CBM
    } else if (playerChoiceId === 'defensive-radar' && betaResponse.postureId === 'verified-cbm') {
      delta = 14; // defensive deterrence success
    } else if (playerChoiceId === 'verified-cbm' && betaResponse.postureId === 'forward-strike') {
      delta = -16; // unfortified concession exploited
    } else {
      delta = isCautious ? posture.deltaAgainstCautious : posture.deltaAgainstOpportunist;
    }

    this.stability = Math.max(0, Math.min(100, this.stability + delta));

    // Update real-state radar blips
    if (posture.blipChange === 'OFFENSIVE_BLIP' || betaResponse.postureId === 'forward-strike') {
      // Accumulate red strike blips along DMZ
      this.radarBlips.push({
        id: `blip-${Date.now()}-${Math.random()}`,
        x: (Math.random() * 80) - 40,
        y: (Math.random() * 80) - 40,
        type: 'strike',
        alpha: 0.95
      });
    }

    if (posture.blipChange === 'CLEAR_BLIP' && betaResponse.postureId === 'verified-cbm') {
      // Clear offensive strike blips on verified CBM
      this.radarBlips = this.radarBlips.filter(b => b.type !== 'strike');
      // Add peaceful sensor beacon
      this.radarBlips.push({
        id: `cbm-${Date.now()}`,
        x: 0,
        y: -10,
        type: 'cbm',
        alpha: 0.9
      });
    }

    if (posture.blipChange === 'DEFENSE_RADAR') {
      this.radarBlips.push({
        id: `def-${Date.now()}`,
        x: -55,
        y: 20,
        type: 'defense',
        alpha: 0.85
      });
    }

    // Evaluate prediction match
    const decisionId = `round-${this.round}`;
    const predicted = this.currentPrediction;
    let actual = 'pred-spiral';
    if (betaResponse.postureId === 'forward-strike' && playerChoiceId === 'forward-strike') {
      actual = 'pred-spiral';
    } else if (betaResponse.postureId === 'forward-strike' && playerChoiceId === 'verified-cbm') {
      actual = 'pred-exploit';
    } else {
      actual = 'pred-mirror';
    }

    const predictionMatch = (predicted === actual);
    const isSuccess = (delta > 0);

    const feedbackPayload = {
      decisionId,
      choice: playerChoiceId,
      correctChoice: 'defensive-radar',
      outcome: isSuccess ? 'success' : (delta >= -10 ? 'partial' : 'failure'),
      consequence: `${posture.feedback.consequence} State Beta responded with: ${betaResponse.name}. (${betaResponse.reason})`,
      mechanism: posture.feedback.mechanism,
      citation: posture.feedback.citation,
      misconception: isSuccess ? null : posture.feedback.misconception,
      misconceptionTag: (!isSuccess && posture.feedback.misconception) ? posture.feedback.misconception.tag : null,
      predicted,
      actual,
      predictionMatch,
      objectiveIndex: (this.round - 1) % 3
    };

    const turnRecord = {
      round: this.round,
      playerChoice: playerChoiceId,
      playerPosture: posture.shortTitle,
      betaPosture: betaResponse.name,
      delta,
      stability: this.stability,
      feedback: feedbackPayload
    };

    this.history.push(turnRecord);
    this.lastTurnFeedback = feedbackPayload;
    this.session.recordDecision(feedbackPayload);
    return turnRecord;
  }

  evaluateAttribution(playerChoice) {
    const expected = this.betaArchetype.expectedAttribution;
    const isCorrect = (playerChoice === expected);
    return {
      isCorrect,
      expected,
      archetypeName: this.betaArchetype.name,
      explanation: isCorrect
        ? `Accurate Attribution: State Beta's actions reflect ${this.betaArchetype.name}. As Robert Jervis noted, discerning whether an adversary is motivated by insecurity (fear) or expansionism (revisionism) is the quintessential challenge of security policy.`
        : `Attribution Misperception: State Beta's doctrine is ${this.betaArchetype.name}. Mischaracterizing a fear-driven rival as revisionist provokes unnecessary arms races, whereas mischaracterizing an opportunist as fear-driven invites aggression.`
    };
  }

  answerMastery(choiceId) {
    const check = MASTERY_CHECKS[this.masteryIndex];
    if (!check) return null;

    const chosenOption = check.choices.find(c => c.id === choiceId);
    const isCorrect = chosenOption ? chosenOption.correct : false;

    this.session.recordMasteryCheck({
      questionId: check.id,
      chosen: choiceId,
      correct: isCorrect,
      misconception: isCorrect ? null : check.misconception,
      objectiveIndex: check.objectiveIndex
    });

    const res = {
      isCorrect,
      explanation: check.explanation,
      nextIndex: this.masteryIndex + 1
    };
    this.masteryIndex++;
    return res;
  }

  answerTransfer(choiceId) {
    const chosen = TRANSFER_SCENARIO.choices.find(c => c.id === choiceId);
    const isCorrect = chosen ? chosen.correct : false;

    this.session.recordTransfer({
      scenarioId: TRANSFER_SCENARIO.id,
      choice: choiceId,
      correct: isCorrect,
      objectiveIndex: TRANSFER_SCENARIO.objectiveIndex
    });

    this.transferAnswered = true;
    return {
      isCorrect,
      explanation: TRANSFER_SCENARIO.explanation,
      citation: TRANSFER_SCENARIO.citation
    };
  }

  getStars() {
    return this.session.getStars();
  }

  getReport() {
    const rep = this.session.getReport();
    rep.chapters = chaptersFor(LAB_ID).map(c => ({
      slug: c.slug,
      title: c.title,
      url: chapterUrl(c.slug)
    }));
    return rep;
  }
}
