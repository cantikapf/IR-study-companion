import { LearningSession } from '../../shared/learn/LearningSession.js';

export const BOP_OBJECTIVES = [
  'Explain how alliance commitments reduce strategic flexibility and increase chain-ganging risk.',
  'Differentiate chain-ganging from buck-passing under multipolar balance of power systems.',
  'Demonstrate how the cult of the offensive converts local diplomatic crises into systemic war.'
];

export const BOP_CRISES = [
  {
    id: 'crisis-01',
    title: 'The Sarajevo Crisis & the Austrian Ultimatum (July 5-23, 1914)',
    powers: 'Berlin · Vienna · St. Petersburg · Belgrade',
    flashpoint: 'Balkans / Danube Frontier',
    context: 'Following the assassination of Archduke Franz Ferdinand in Sarajevo, Austria-Hungary resolves to eliminate Serbia as a political factor. Vienna requests unconditional German backing before presenting an ultimatum designed for Serbian rejection.',
    predictionPrompt: 'Predict the systemic consequence of Germany issuing an unconditional "Blank Check" to Vienna under multipolar balance of power:',
    predictionOptions: [
      { key: 'A', text: 'It deters Russian intervention by demonstrating unbreakable Central alliance solidarity.' },
      { key: 'B', text: 'It chain-gangs Germany to Austrian recklessness, eliminating diplomatic flexibility and prompting Russian counter-mobilization.' },
      { key: 'C', text: 'It permits Germany to pass the buck of balancing to Italy.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Foreign Office Alignment Action (Verb: ALIGN):',
    choices: [
      {
        action: 'COMMIT',
        title: 'ISSUE THE BLANK CHECK',
        sub: 'Unconditional military backing to Austria-Hungary',
        tensionDelta: 35,
        chainDelta: 1,
        buckDelta: 0,
        outcome: 'failure',
        consequence: 'Vienna interprets the unconditional guarantee as a mandate for aggression, rejects Serbian concessions, and bombards Belgrade. Russia initiates mobilization preparations.',
        mechanism: 'Chain-ganging under multipolarity: unconditional alliance guarantees bind a great power to a reckless junior partner.',
        citation: 'Waltz (1979), Theory of International Politics, ch. 8; Christensen & Snyder (1990), pp. 138-142.',
        misconception: {
          tag: 'misc_alliances_deter',
          label: 'The Alliance Deterrence Fallacy',
          remediation: 'In multipolarity, unconditional commitments do not deter rivals; they entrap allies into reckless escalation by eliminating defensive restraint.'
        }
      },
      {
        action: 'WITHHOLD',
        title: 'BUCK-PASS TO BALKAN DIPLOMACY',
        sub: 'Sever alliance ties; treat as isolated regional dispute',
        tensionDelta: 20,
        chainDelta: 0,
        buckDelta: 1,
        outcome: 'partial',
        consequence: 'Germany signals passivity. Austria feels isolated and panics, while Russia assumes Germany is weak and begins unilateral pressure in the Balkans.',
        mechanism: 'Buck-passing instability: attempting to shirk balancing responsibilities invites revisionist aggression and panic.',
        citation: 'Christensen & Snyder (1990), Chain Gangs and Passed Bucks, pp. 140-144.',
        misconception: {
          tag: 'misc_buck_passing_chain_ganging',
          label: 'Buck-Passing Shirk Fallacy',
          remediation: 'Withholding all commitment does not stabilize a multipolar crisis; it creates dangerous power vacuums and miscalculating aggressors.'
        }
      },
      {
        action: 'MEDIATE',
        title: 'CONDITIONAL RESTRAINT ("HALT IN BELGRADE")',
        sub: 'Guarantee Austrian territory if attacked, but condition aid on diplomatic mediation',
        tensionDelta: -10,
        chainDelta: 0,
        buckDelta: 0,
        outcome: 'success',
        consequence: 'Berlin makes military assistance strictly conditional on Vienna halting troops at Belgrade and submitting to four-power conference mediation. Systemic escalation is checked.',
        mechanism: 'Strategic restraint and conditional deterrence: firm defensive balancing coupled with strict ally restraint.',
        citation: 'Waltz (1979), ch. 8; Jervis (1978), Cooperation Under the Security Dilemma, pp. 186-192.',
        misconception: null
      }
    ],
    objectiveIndex: 0
  },
  {
    id: 'crisis-02',
    title: 'Russian Mobilization & Franco-Russian Consultation (July 24-28, 1914)',
    powers: 'St. Petersburg · Paris · Berlin · London',
    flashpoint: 'Galicia / East Prussian Border',
    context: 'Austria bombards Belgrade. In St. Petersburg, military chiefs urge Tsar Nicholas II to order mobilization. In Paris, Ambassador Paléologue assures Russian Foreign Minister Sazonov of unqualified French solidarity.',
    predictionPrompt: 'Predict why partial mobilization against Austria failed to maintain crisis stability in July 1914:',
    predictionOptions: [
      { key: 'A', text: 'Russian railway timetables had no independent operational plan for partial mobilization; beginning it created chaotic vulnerability that forced general mobilization.' },
      { key: 'B', text: 'Great Britain immediately declared war on Russia.' },
      { key: 'C', text: 'Austria-Hungary demobilized upon seeing Russian troops.' }
    ],
    expectedPrediction: 'A',
    question: 'Select Foreign Office Alignment Action (Verb: ALIGN):',
    choices: [
      {
        action: 'COMMIT',
        title: 'UNCONDITIONAL ENTENTE ENTRAPMENT',
        sub: 'Pledge total French military backing for Russian general mobilization',
        tensionDelta: 30,
        chainDelta: 1,
        buckDelta: 0,
        outcome: 'failure',
        consequence: 'Reassured by unconditional French backing, St. Petersburg orders full general mobilization. The German General Staff declares a state of imminent danger of war.',
        mechanism: 'Alliance entrapment: tight bilateral ties allow the revisionist moves of one power to dictate the military commitment of its partner.',
        citation: 'Christensen & Snyder (1990), p. 140; Snyder (1984), The Alliance Politics of International Security.',
        misconception: {
          tag: 'misc_alliances_deter',
          label: 'Unconditional Entente Solidarity Fallacy',
          remediation: 'Backing an ally unconditionally during mobilization removes their incentive to negotiate, triggering opposing mobilization.'
        }
      },
      {
        action: 'WITHHOLD',
        title: 'BUCK-PASS TO LONDON MEDIATION',
        sub: 'Declare France neutral in Balkan quarrels and refuse to mobilize',
        tensionDelta: 25,
        chainDelta: 0,
        buckDelta: 1,
        outcome: 'partial',
        consequence: 'France passes the buck to London. Russia feels betrayed and considers a desperate unilateral gamble, while Berlin assumes the Entente has dissolved.',
        mechanism: 'Buck-passing destabilization under multipolar crisis conditions.',
        citation: 'Waltz (1979), ch. 8; Mearsheimer (2001), The Tragedy of Great Power Politics.',
        misconception: {
          tag: 'misc_buck_passing_chain_ganging',
          label: 'Buck-Passing Asymmetry',
          remediation: 'Failing to balance when an ally faces an existential challenge destroys the coalition and tempts the adversary to strike.'
        }
      },
      {
        action: 'MEDIATE',
        title: 'DEFENSIVE DISSUASION & FRONTIER PAUSE',
        sub: 'Pledge defense against direct attack, but condition aid on halting rail deployment at the frontier',
        tensionDelta: -10,
        chainDelta: 0,
        buckDelta: 0,
        outcome: 'success',
        consequence: 'France affirms defensive protection against invasion, but strictly conditions support on Russian trains stopping 50km from the German border to allow diplomatic talks.',
        mechanism: 'Conditional balancing: providing security reassurance while forbidding offensive or provocative mobilization.',
        citation: 'Jervis (1978), pp. 186-190; Waltz (1979).',
        misconception: null
      }
    ],
    objectiveIndex: 1
  },
  {
    id: 'crisis-03',
    title: 'The Cult of the Offensive & Railway Timetable Friction (July 30-31, 1914)',
    powers: 'Berlin · St. Petersburg · Vienna · Paris',
    flashpoint: 'Continental Railway Junctions',
    context: 'Tsar Nicholas signs the general mobilization decree. German Chief of General Staff Moltke warns Chancellor Bethmann-Hollweg: under the Schlieffen Plan, every hour of delay before attacking France guarantees a catastrophic two-front war.',
    predictionPrompt: 'Predict why the "cult of the offensive" made military mobilization synonymous with war in 1914:',
    predictionOptions: [
      { key: 'A', text: 'Railway timetables were easily reversible without military disadvantage.' },
      { key: 'B', text: 'Belief in decisive offensive advantage meant whoever mobilized first won; mobilization could not be halted without risking destruction.' },
      { key: 'C', text: 'Diplomats had no telegraph access to military headquarters.' }
    ],
    expectedPrediction: 'B',
    question: 'Select Foreign Office Alignment Action (Verb: ALIGN):',
    choices: [
      {
        action: 'COMMIT',
        title: 'LAUNCH PRE-EMPTIVE MOBILIZATION',
        sub: 'Authorize Schlieffen Plan railway deployment immediately',
        tensionDelta: 35,
        chainDelta: 1,
        buckDelta: 0,
        outcome: 'failure',
        consequence: '11,000 military trains begin rolling. Diplomacy is superseded by rigid railway logistics. General war becomes irreversible.',
        mechanism: 'The cult of the offensive converts defensive mobilization into immediate offensive war.',
        citation: 'Van Evera (1984), The Cult of the Offensive and the Origins of the First World War, pp. 58-65.',
        misconception: {
          tag: 'misc_mobilisation_reversible',
          label: 'The Mobilization Reversibility Myth',
          remediation: 'In 1914, military staffs believed mobilization was war. Halting train schedules risked disorganizing armies at the frontier.'
        }
      },
      {
        action: 'WITHHOLD',
        title: 'UNILATERAL RAILWAY FREEZE',
        sub: 'Order troops to stay in barracks while adversary mobilizes',
        tensionDelta: 20,
        chainDelta: 0,
        buckDelta: 1,
        outcome: 'partial',
        consequence: 'Freezing mobilization while the rival mobilizes creates acute vulnerability, causing military staff panic.',
        mechanism: 'Window of vulnerability under perceived offensive advantage.',
        citation: 'Van Evera (1984), pp. 62-67.',
        misconception: {
          tag: 'misc_mobilisation_reversible',
          label: 'Unilateral Vulnerability Risk',
          remediation: 'Unilateral restraint under offensive doctrines invites preemption unless verified by mutual standstill agreements.'
        }
      },
      {
        action: 'MEDIATE',
        title: 'RECIPROCAL 48-HOUR STANDSTILL AGREEMENT',
        sub: 'Offer immediate bilateral freeze at frontier depots backed by direct telegraph verification',
        tensionDelta: -15,
        chainDelta: 0,
        buckDelta: 0,
        outcome: 'success',
        consequence: 'Civilian chancellors enforce a 48-hour standstill order on general staffs. Mutual telegraph verification confirms frontier halts, preserving diplomatic breathing room.',
        mechanism: 'Crisis de-escalation: severing the link between mobilization and immediate attack through verifiable standstills.',
        citation: 'Van Evera (1984); Christensen & Snyder (1990).',
        misconception: null
      }
    ],
    objectiveIndex: 2
  },
  {
    id: 'crisis-04',
    title: 'The Schlieffen Corridor & Belgian Neutrality (August 1-3, 1914)',
    powers: 'London · Brussels · Berlin · Paris',
    flashpoint: 'River Meuse / Low Countries',
    context: 'German armies deliver an ultimatum to Brussels demanding transit to encircle French fortifications. British Foreign Secretary Sir Edward Grey faces a divided Cabinet. Liberal ministers urge neutrality, while realists warn that German control of Antwerp destroys the continental balance.',
    predictionPrompt: 'Predict how British strategic ambiguity affected German decision-making in August 1914:',
    predictionOptions: [
      { key: 'A', text: 'Ambiguity encouraged the German gamble that Britain would buck-pass and stay neutral, lowering the perceived cost of invading Belgium.' },
      { key: 'B', text: 'Ambiguity successfully deterred German generals from invading Belgium.' },
      { key: 'C', text: 'Britain had no legal treaty obligations in western Europe.' }
    ],
    expectedPrediction: 'A',
    question: 'Select Foreign Office Alignment Action (Verb: ALIGN):',
    choices: [
      {
        action: 'COMMIT',
        title: 'UPHOLD 1839 TREATY OF LONDON',
        sub: 'Deliver immediate ultimatum guaranteeing Belgian neutrality and continental balance',
        tensionDelta: -10,
        chainDelta: 0,
        buckDelta: 0,
        outcome: 'success',
        consequence: 'Britain clearly commits its naval, economic, and imperial weight to defend Belgian neutrality. Germany realizes Britain will fight, halting reckless unilateral gambles and balancing continental power.',
        mechanism: 'External balancing: clear, credible commitments prevent revisionist powers from gambling on cheap victories.',
        citation: 'Waltz (1979), ch. 8; Mearsheimer (2001), ch. 8.',
        misconception: null
      },
      {
        action: 'WITHHOLD',
        title: 'BUCK-PASS TO FRANCE & BELGIUM',
        sub: 'Remain neutral; let the continental powers fight alone',
        tensionDelta: 35,
        chainDelta: 0,
        buckDelta: 1,
        outcome: 'failure',
        consequence: 'Britain remains aloof. German armies overrun Belgium and northern France, establishing hegemony over the Channel ports and permanently destroying the European equilibrium.',
        mechanism: 'Buck-passing failure: when an offshore balancer refuses to commit, a continental hegemon overruns the system.',
        citation: 'Mearsheimer (2001), The Tragedy of Great Power Politics, ch. 8.',
        misconception: {
          tag: 'misc_buck_passing_chain_ganging',
          label: 'The Offshore Buck-Passing Trap',
          remediation: 'Buck-passing fails when the defending coalition cannot defeat the aggressor alone. Refusing to balance creates hegemony.'
        }
      },
      {
        action: 'MEDIATE',
        title: 'AMBIGUOUS CONDITIONAL ULTIMATUM',
        sub: 'Offer vague diplomatic warnings without committing British military forces',
        tensionDelta: 20,
        chainDelta: 0,
        buckDelta: 0,
        outcome: 'partial',
        consequence: 'Ambiguity confuses both allies and adversaries. Berlin gambles that Britain will not fight over "a scrap of paper".',
        mechanism: 'Deterrence failure through commitment ambiguity.',
        citation: 'Jervis (1978); Waltz (1979).',
        misconception: {
          tag: 'misc_alliances_deter',
          label: 'Ambiguity as Deterrence Fallacy',
          remediation: 'Strategic ambiguity weakens deterrence. Aggressors interpret ambiguity as permission to strike.'
        }
      }
    ],
    objectiveIndex: 1
  },
  {
    id: 'crisis-05',
    title: 'Systemic Reckoning: Multipolar War vs Armed Equilibrium (August 1914)',
    powers: 'Great Power System (Multipolar Europe)',
    flashpoint: 'European Continent',
    context: 'The final phase of the July Crisis: can multipolar Europe preserve an armed equilibrium, or does the structural interaction of chain-ganging, buck-passing, and the cult of the offensive trigger total systemic conflagration?',
    predictionPrompt: 'Predict what structural condition made 1914 multipolarity so vulnerable to catastrophic chain-ganging compared to 1938:',
    predictionOptions: [
      { key: 'A', text: 'Perceptions of offensive dominance made states fear that losing any single ally would be fatal, triggering unconditional chain-ganging.' },
      { key: 'B', text: '1914 was a unipolar system with a dominant global hegemon.' },
      { key: 'C', text: 'All alliances in 1914 were non-binding economic treaties.' }
    ],
    expectedPrediction: 'A',
    question: 'Select Final Foreign Office Alignment Action (Verb: ALIGN):',
    choices: [
      {
        action: 'COMMIT',
        title: 'UNCONDITIONAL COALITION WAR',
        sub: 'Surrender all diplomatic initiative to military general staffs',
        tensionDelta: 30,
        chainDelta: 1,
        buckDelta: 0,
        outcome: 'failure',
        consequence: 'Total alliance conflagration. Five great empires enter total war, producing millions of casualties and four collapsed dynasties.',
        mechanism: 'Systemic chain-ganging collapse under multipolar anarchy.',
        citation: 'Waltz (1979), ch. 8; Christensen & Snyder (1990).',
        misconception: {
          tag: 'misc_balance_is_number',
          label: 'The Mechanical Balance Fallacy',
          remediation: 'Balance of power is not an arithmetic equation of weights; it requires active diplomatic management to prevent alliance entrapment.'
        }
      },
      {
        action: 'WITHHOLD',
        title: 'TOTAL DISENGAGEMENT & CHAOS',
        sub: 'Withdraw from all alliance commitments and abandon the continent',
        tensionDelta: 25,
        chainDelta: 0,
        buckDelta: 1,
        outcome: 'partial',
        consequence: 'Systemic breakdown. The collapse of balancing institutions leads to swift continental hegemony and permanent instability.',
        mechanism: 'Systemic vacuum and hegemonic revisionism under failed multipolar balancing.',
        citation: 'Waltz (1979); Mearsheimer (2001).',
        misconception: {
          tag: 'misc_buck_passing_chain_ganging',
          label: 'Isolationist Illusion',
          remediation: 'Great powers in an anarchic system cannot isolate themselves from hegemonic threats without forfeiting security.'
        }
      },
      {
        action: 'MEDIATE',
        title: 'RESTORATION OF CONCERT EQUILIBRIUM',
        sub: 'Enforce multilateral conference diplomacy backed by reciprocal balancing',
        tensionDelta: -15,
        chainDelta: 0,
        buckDelta: 0,
        outcome: 'success',
        consequence: 'The Concert of Europe re-asserts diplomatic supremacy over railway timetables. Great powers maintain mutual deterrence while resolving the Balkan crisis through binding multilateral arbitration.',
        mechanism: 'Systemic equilibrium: combining robust balancing deterrence with alliance restraint.',
        citation: 'Waltz (1979), ch. 8; Christensen & Snyder (1990), pp. 165-168.',
        misconception: null
      }
    ],
    objectiveIndex: 2
  }
];

export const BOP_MASTERY_QUESTIONS = [
  {
    questionId: 'bop-mc-01',
    prompt: 'What is the defining characteristic of "chain-ganging" in neorealist alliance theory (Christensen & Snyder 1990)?',
    options: [
      { key: 'A', text: 'A state assumes its allies will handle an adversary alone without its assistance.' },
      { key: 'B', text: 'A state binds its own security unconditionally to an ally, allowing the ally\'s recklessness to drag it into an unwanted systemic war.' },
      { key: 'C', text: 'A state switches sides during a crisis to join the winning coalition.' }
    ],
    correct: 'B',
    objectiveIndex: 0,
    rationale: 'In a multipolar system where states perceive an offensive advantage, the survival of any single ally is seen as vital. States chain-gang by offering unconditional support, thereby ceding their own decision-making freedom to the most reckless partner.',
    citation: 'Christensen & Snyder (1990), Chain Gangs and Passed Bucks, pp. 138-142',
    misconceptionTag: 'misc_alliances_deter'
  },
  {
    questionId: 'bop-mc-02',
    prompt: 'How does "buck-passing" differ from "balancing" under a multipolar balance of power?',
    options: [
      { key: 'A', text: 'Buck-passing involves waiting for another threatened great power to bear the heavy blood and treasure of checking an aggressor, while balancing directly confronts the threat.' },
      { key: 'B', text: 'Buck-passing is only possible in a bipolar system where superpowers dominate.' },
      { key: 'C', text: 'Buck-passing means unconditionally subsidizing an ally\'s military mobilization.' }
    ],
    correct: 'A',
    objectiveIndex: 1,
    rationale: 'Buck-passing is the attempt by a threatened great power to shirk the burden of balancing by getting another state to stand in the path of the aggressor. Balancing, in contrast, commits resources directly to contain the threat.',
    citation: 'Mearsheimer (2001), The Tragedy of Great Power Politics, ch. 8; Waltz (1979)',
    misconceptionTag: 'misc_buck_passing_chain_ganging'
  },
  {
    questionId: 'bop-mc-03',
    prompt: 'According to Stephen Van Evera (1984), how did the "cult of the offensive" destabilize the 1914 balance of power?',
    options: [
      { key: 'A', text: 'It convinced military leaders that defense was dominant, encouraging prolonged diplomatic negotiations.' },
      { key: 'B', text: 'It fostered the doctrine that whoever attacked first held a decisive advantage, making mobilization tantamount to war and window of vulnerability intolerable.' },
      { key: 'C', text: 'It eliminated the need for railway logistics in military planning.' }
    ],
    correct: 'B',
    objectiveIndex: 2,
    rationale: 'The cult of the offensive created extreme first-mover incentives. Believing defense was impossible, general staffs operated on rigid railway timetables where even a 24-hour delay was viewed as fatal, converting political crises into military stampedes.',
    citation: 'Van Evera (1984), The Cult of the Offensive and the Origins of the First World War, pp. 58-65',
    misconceptionTag: 'misc_mobilisation_reversible'
  }
];

export const BOP_TRANSFER_SCENARIO = {
  scenarioId: 'transfer-1914-vs-1938',
  title: 'Multipolar Alliance Dynamics: 1914 vs 1938',
  prompt: 'Both 1914 and 1938 were multipolar systems containing several great powers. Yet in 1914, states chain-ganged into world war within weeks over a local Balkan crisis. In 1938, facing aggressive Nazi expansion in Czechoslovakia, Britain and France did not chain-gang with Prague or Moscow; instead they engaged in appeasement. According to Christensen and Snyder (1990), what structural variable explains this dramatic divergence?',
  options: [
    { key: 'A', text: 'In 1914, offense was perceived to dominate, so states feared losing an ally above all else (triggering chain-ganging); in 1938, defense was perceived to dominate (memories of WWI trenches), so Britain and France believed they could safely pass the buck to the Soviet Union.' },
    { key: 'B', text: '1938 was a unipolar system controlled by the League of Nations.' },
    { key: 'C', text: 'In 1914 states had no written alliances, whereas in 1938 all treaties were automatic.' }
  ],
  correct: 'A',
  objectiveIndex: 1,
  rationale: 'Christensen and Snyder (1990) explain that perceived offense-defense balance mediates multipolar behavior. When offense is perceived dominant (1914), states fear allies will be quickly crushed and chain-gang unconditionally. When defense is perceived dominant (1938), states believe allies can absorb punishment and attempt to pass the buck of deterrence to other powers (e.g., Britain and France hoping the USSR would fight Germany).',
  citation: 'Christensen & Snyder (1990), Chain Gangs and Passed Bucks: Predicting Alliance Patterns in Multipolarity, International Organization 44(2), pp. 137-168.'
};

export class BopState {
  constructor() {
    this.session = new LearningSession('lab-08', BOP_OBJECTIVES);
    this.reset();
  }

  reset() {
    this.session = new LearningSession('lab-08', BOP_OBJECTIVES);
    this.crisisIndex = 0;
    this.systemTension = 25; // 0..100 (equilibrium corridor 10..60)
    this.chainGangingCount = 0;
    this.buckPassingCount = 0;
    this.score = 0;
    this.streak = 0;
    this.currentPrediction = null;
    this.currentFeedback = null;
    this.collapse = false;
    this.collapseReason = null;
    this.phase = 'BRIEF'; // BRIEF, PREDICT, DECIDE, CONSEQUENCE, MASTERY, TRANSFER, DEBRIEF
    this.masteryIndex = 0;
  }

  getCurrentCrisis() {
    return BOP_CRISES[this.crisisIndex] || null;
  }

  recordPrediction(predictionKey) {
    const c = this.getCurrentCrisis();
    if (!c) return;
    this.currentPrediction = predictionKey;
    this.session.recordPrediction(c.id, predictionKey);
    this.phase = 'DECIDE';
  }

  executeDecision(actionVerb) {
    const c = this.getCurrentCrisis();
    if (!c) return null;

    const choiceObj = c.choices.find(ch => ch.action === actionVerb);
    if (!choiceObj) return null;

    const isCorrect = (choiceObj.outcome === 'success');
    const predictedMatch = (this.currentPrediction === c.expectedPrediction);

    this.systemTension = Math.max(0, Math.min(100, this.systemTension + choiceObj.tensionDelta));
    this.chainGangingCount += choiceObj.chainDelta;
    this.buckPassingCount += choiceObj.buckDelta;

    if (this.systemTension >= 85) {
      this.collapse = true;
      if (this.chainGangingCount >= 3) {
        this.collapseReason = 'SYSTEMIC COLLAPSE: Catastrophic World War triggered by alliance chain-ganging and rigid railway mobilizations.';
      } else {
        this.collapseReason = 'SYSTEMIC COLLAPSE: Hegemonic breakdown triggered by cumulative buck-passing and deterrence failure.';
      }
    }

    if (isCorrect) {
      this.streak++;
      const multiplier = this.streak >= 3 ? 1.5 : 1.0;
      this.score += Math.round(20 * multiplier);
    } else {
      this.streak = 0;
      this.score = Math.max(0, this.score - 5);
    }

    const payload = {
      outcome: choiceObj.outcome,
      consequence: choiceObj.consequence,
      mechanism: choiceObj.mechanism,
      citation: choiceObj.citation,
      misconception: choiceObj.misconception,
      predictionMatch: predictedMatch
    };

    this.session.recordDecision({
      decisionId: c.id,
      choice: actionVerb,
      correctChoice: 'MEDIATE',
      rationale: choiceObj.consequence,
      misconceptionTag: choiceObj.misconception ? choiceObj.misconception.tag : null,
      misconception: choiceObj.misconception,
      predicted: this.currentPrediction,
      actual: c.expectedPrediction,
      outcome: payload.outcome,
      consequence: payload.consequence,
      mechanism: payload.mechanism,
      citation: payload.citation,
      objectiveIndex: c.objectiveIndex
    });

    this.currentFeedback = payload;
    this.phase = 'CONSEQUENCE';

    return {
      isCorrect,
      payload,
      systemTension: this.systemTension,
      collapse: this.collapse,
      collapseReason: this.collapseReason,
      score: this.score
    };
  }

  advanceCrisis() {
    this.crisisIndex++;
    this.currentPrediction = null;
    this.currentFeedback = null;

    if (this.collapse) {
      this.phase = 'DEBRIEF';
      return false;
    }

    if (this.crisisIndex < BOP_CRISES.length) {
      this.phase = 'PREDICT';
      return true;
    }
    this.phase = 'MASTERY';
    return false;
  }

  getCurrentMasteryQuestion() {
    return BOP_MASTERY_QUESTIONS[this.masteryIndex] || null;
  }

  answerMasteryQuestion(chosenKey) {
    const q = this.getCurrentMasteryQuestion();
    if (!q) return null;

    const isCorrect = (chosenKey === q.correct);
    this.session.recordMasteryCheck({
      questionId: q.questionId,
      chosen: chosenKey,
      correct: q.correct,
      misconceptionTag: !isCorrect ? q.misconceptionTag : null,
      objectiveIndex: q.objectiveIndex
    });

    this.masteryIndex++;
    const hasMore = this.masteryIndex < BOP_MASTERY_QUESTIONS.length;
    if (!hasMore) {
      this.phase = 'TRANSFER';
    }

    return {
      isCorrect,
      hasMore,
      rationale: q.rationale,
      citation: q.citation
    };
  }

  answerTransfer(chosenKey) {
    const t = BOP_TRANSFER_SCENARIO;
    const isCorrect = (chosenKey === t.correct);

    this.session.recordTransfer({
      scenarioId: t.scenarioId,
      choice: chosenKey,
      correct: t.correct,
      objectiveIndex: t.objectiveIndex
    });

    this.phase = 'DEBRIEF';
    return {
      isCorrect,
      rationale: t.rationale,
      citation: t.citation
    };
  }

  getReport() {
    return this.session.getReport();
  }

  getStars() {
    if (this.collapse) return 0;
    return this.session.getStars();
  }
}

