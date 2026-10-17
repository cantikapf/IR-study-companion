import { LearningSession } from '../../shared/learn/LearningSession.js';
import { chaptersFor, chapterUrl } from '../../shared/learn/ChapterLink.js';

export const LAB_ID = 'lab-01';

export const LEARNING_OBJECTIVES = [
  'Distinguish Allison Model I (Rational Actor), Model II (Organizational Routine), and Model III (Bureaucratic Politics).',
  'Explain how organisational routines and bureaucratic bargaining distort a rational strategy.',
  'Recognise time compression and incomplete information as structural features of crisis.'
];

export const MISCONCEPTIONS = {
  'model-hierarchy': {
    tag: 'model-hierarchy',
    label: 'Normative Model Hierarchy Fallacy',
    remediation: 'Allison models are analytical lenses, not a ranking of good and bad decisions. Model I clarifies strategic intent, Model II exposes standard routine rigidities, and Model III reveals political compromise.'
  },
  'unitary-actor': {
    tag: 'unitary-actor',
    label: 'Unitary Rational Actor Fallacy',
    remediation: 'States are not monolithic calculators. Military services execute inflexible pre-planned routines (Model II) and cabinet secretaries bargain over departmental turf (Model III).'
  },
  'costless-delay': {
    tag: 'costless-delay',
    label: 'Costless Delay Fallacy',
    remediation: 'In high-stakes crises, hesitation or decision delays do not freeze time; standard organizational momentum and adversary preemptive calculations fill the vacuum.'
  }
};

export const CRISIS_ACTS = [
  {
    act: 1,
    title: 'Act 1: Initial Discovery',
    date: 'October 16, 1962',
    brief: 'CIA U-2 photographic intelligence confirms operational Soviet SS-4 medium-range ballistic missile launch pads in San Cristóbal, Cuba. Warheads are en route. ExComm convenes under severe time compression.',
    sigint: 'SIGINT INTERCEPT: Soviet construction crews are working around the clock. Field commanders have operational autonomy over conventional defense, but nuclear release authority currently remains with Khrushchev in Moscow.',
    predictionQuestion: 'Before authorizing a response, predict the primary organizational friction that will strain executive command:',
    predictionOptions: [
      {
        id: 'pred-sop',
        text: 'Armed service commands will execute rigid pre-planned routines (Model II) that overshoot calibrated diplomatic goals.',
        expectedModel: 'II'
      },
      {
        id: 'pred-bargain',
        text: 'Cabinet department chiefs will pull and haul to protect institutional turf and political standing (Model III).',
        expectedModel: 'III'
      },
      {
        id: 'pred-rational',
        text: 'The government will act as a frictionless single actor executing pure strategic utility calculations (Model I).',
        expectedModel: 'I'
      }
    ],
    advisors: [
      {
        name: 'SecDef McNamara',
        lens: 'Model I (Rational Strategy)',
        quote: 'A blockade is a calibrated pressure point. It signals resolve while giving Khrushchev space and time to retreat without instant nuclear exchange.'
      },
      {
        name: 'Gen. Curtis LeMay',
        lens: 'Model II (Organizational Routine)',
        quote: 'Air Force standard operating doctrine mandates 500 sorties across the entire island. We execute the pre-planned strike package or we guarantee nothing.'
      },
      {
        name: 'Robert F. Kennedy',
        lens: 'Model III (Bureaucratic Politics)',
        quote: 'A surprise air strike is a Pearl Harbor in reverse. It will tear the administration apart and destroy our moral standing among allies.'
      }
    ],
    options: [
      {
        id: 'blockade',
        title: 'Naval Quarantine / Maritime Blockade',
        desc: 'Deploy US Navy warships along a 500-mile perimeter to intercept Soviet arms shipments while leaving diplomatic off-ramps open.',
        lens: 'Model I (Rational Actor Model)',
        lensShort: 'Model I',
        stabilityDelta: 0,
        defconDelta: 0,
        expectedPrediction: 'pred-rational',
        feedback: {
          outcome: 'success',
          consequence: 'Naval quarantine is declared. Soviet merchant ships alter course or decelerate outside the perimeter, purchasing a 48-hour negotiating window.',
          mechanism: 'Model I (Rational Actor Model): The state acts as a purposive unitary actor choosing a graduated option that balances deterrence against the risk of rapid escalation.',
          citation: 'Allison (1971), Essence of Decision, pp. 10-38',
          misconception: null
        },
        advisorReaction: 'McNamara nods: "Strategic flexibility maintained. The ball is in Khrushchev\'s court."',
        mapEffect: { type: 'arc', color: 'cyan', label: 'QUARANTINE ARC [500 NM]' }
      },
      {
        id: 'airstrike',
        title: 'Surgical Air Strike on Missile Sites',
        desc: 'Execute Tactical Air Command contingency strike plan against San Cristóbal launch batteries before they achieve operational readiness.',
        lens: 'Model II (Organizational Routine)',
        lensShort: 'Model II',
        stabilityDelta: -30,
        defconDelta: -1,
        expectedPrediction: 'pred-sop',
        feedback: {
          outcome: 'failure',
          consequence: 'Air Force sorties strike missile depots, killing Soviet technicians. Moscow responds by escalating alerts in West Berlin and placing Soviet tactical rockets in Cuba on hair-trigger readiness.',
          mechanism: 'Model II (Organizational Behavior): Large organizations execute existing operational routines rather than tailor surgical political messages. Standard strike packages maximize destructive coverage rather than diplomatic nuance.',
          citation: 'Allison (1971), Essence of Decision, pp. 67-143',
          misconception: MISCONCEPTIONS['unitary-actor']
        },
        advisorReaction: 'LeMay snaps: "The doctrine operated as designed, Mr. President. We hit the coordinates."',
        mapEffect: { type: 'crosshair', color: 'rose', label: 'AIR STRIKE ZONE [SAN CRISTOBAL]' }
      },
      {
        id: 'backchannel',
        title: 'Immediate Private Diplomatic Trade',
        desc: 'Send an informal envoy directly to Soviet Ambassador Dobrynin offering an unpublicized concession before consulting the Joint Chiefs or NATO.',
        lens: 'Model III (Bureaucratic Politics)',
        lensShort: 'Model III',
        stabilityDelta: -15,
        defconDelta: 0,
        expectedPrediction: 'pred-bargain',
        feedback: {
          outcome: 'partial',
          consequence: 'Informal channel opens dialogue, but military chiefs and congressional leaders leak rumors of executive vacillation, sparking fierce cabinet infighting.',
          mechanism: 'Model III (Governmental Politics): Foreign policy decisions are the result of pulling and hauling among bureaucratic players. Unilateral backchannels provoke backlash from excluded institutional actors.',
          citation: 'Allison (1971), Essence of Decision, pp. 144-210',
          misconception: MISCONCEPTIONS['model-hierarchy']
        },
        advisorReaction: 'RFK cautions: "We bypassed the Pentagon chiefs; they are preparing a public confrontation."',
        mapEffect: { type: 'vector', color: 'amber', label: 'BACKCHANNEL DISPATCH [WASHINGTON-MOSCOW]' }
      }
    ]
  },
  {
    act: 2,
    title: 'Act 2: The Blockade Confrontation',
    date: 'October 24, 1962',
    brief: 'Soviet submarine B-59 and merchant ships approach the quarantine perimeter line. Radio contact with Moscow is disrupted. A US destroyer USS Beale begins dropping signalling depth charges.',
    sigint: 'SIGINT INTERCEPT: Submarine B-59 captain believes war has started and considers launching a nuclear-tipped torpedo (Special Weapon). Authorization requires unanimous consent of three onboard officers.',
    predictionQuestion: 'Predict how frontline operational commanders will behave under communications isolation:',
    predictionOptions: [
      {
        id: 'pred-sub-sop',
        text: 'Commanders will adhere to standard tactical doctrine (Model II) even if it escalates the strategic confrontation.',
        expectedModel: 'II'
      },
      {
        id: 'pred-sub-bargain',
        text: 'Frontline officers will negotiate improvised political compromises with opposing captains (Model III).',
        expectedModel: 'III'
      },
      {
        id: 'pred-sub-rational',
        text: 'Local units will intuitively divine and execute the exact de-escalatory intent of the President (Model I).',
        expectedModel: 'I'
      }
    ],
    advisors: [
      {
        name: 'Chief of Naval Ops Anderson',
        lens: 'Model II (Organizational Routine)',
        quote: 'The Navy has known how to run a blockade since John Paul Jones. We follow Fleet ASW Instruction 10-A, not ad-hoc civilian instructions.'
      },
      {
        name: 'UN Amb. Adlai Stevenson',
        lens: 'Model III (Bureaucratic Politics)',
        quote: 'I need authority to confront Soviet Ambassador Zorin with U-2 photo boards at the Security Council today to consolidate world opinion.'
      },
      {
        name: 'Ted Sorensen',
        lens: 'Model I (Rational Strategy)',
        quote: 'The Trollope Ploy is our strongest rational maneuver: answer Khrushchev\'s first conciliatory letter offering withdrawal, and ignore his aggressive second broadcast.'
      }
    ],
    options: [
      {
        id: 'trollope',
        title: 'The Trollope Ploy: Answer Conciliatory Offer Only',
        desc: 'Ignore Khrushchev\'s militant Saturday letter; formally accept his private Friday letter agreeing to dismantle missiles in exchange for a non-invasion pledge.',
        lens: 'Model I (Rational Actor Model)',
        lensShort: 'Model I',
        stabilityDelta: 0,
        defconDelta: 0,
        expectedPrediction: 'pred-sub-rational',
        feedback: {
          outcome: 'success',
          consequence: 'Washington filters the incoming signal noise and commits to the constructive proposal, giving Khrushchev a face-saving diplomatic exit.',
          mechanism: 'Model I (Rational Actor Model): Rational information filtering allows the decision-maker to bypass tactical contradictions and focus on core strategic utility.',
          citation: 'Allison (1971), Essence of Decision, pp. 210-244',
          misconception: null
        },
        advisorReaction: 'Sorensen notes: "We have isolated the peace channel without conceding to threats."',
        mapEffect: { type: 'arc', color: 'cyan', label: 'TROLLOPE DIPLOMATIC CHANNEL [CONFIRMED]' }
      },
      {
        id: 'force-sub-surface',
        title: 'Force Submarine B-59 to Surface with Depth Charges',
        desc: 'Strictly enforce Navy ASW quarantine doctrine: deploy practice depth charges to force all submerged contacts to the surface.',
        lens: 'Model II (Organizational Routine)',
        lensShort: 'Model II',
        stabilityDelta: -25,
        defconDelta: -1,
        expectedPrediction: 'pred-sub-sop',
        feedback: {
          outcome: 'failure',
          consequence: 'Depth charges rock B-59. Captain Savitsky orders nuclear torpedo armed; only the courageous dissent of Flotilla Chief of Staff Vasili Arkhipov averts atomic detonation.',
          mechanism: 'Model II (Organizational Routine): Organizations rely on Standard Operating Procedures (SOPs). The US Navy followed standard ASW training routines unaware that Soviet submarines carried nuclear torpedoes.',
          citation: 'Allison & Zelikow (1999), Essence of Decision (2nd ed.), pp. 221-237',
          misconception: MISCONCEPTIONS['unitary-actor']
        },
        advisorReaction: 'Anderson insists: "Our ships executed standard doctrine, sir."',
        mapEffect: { type: 'crosshair', color: 'rose', label: 'DEPTH CHARGE ENGAGEMENT [SUB B-59]' }
      },
      {
        id: 'un-confrontation',
        title: 'Evidentiary Showdown at UN Security Council',
        desc: 'Direct Ambassador Stevenson to present enlarged U-2 photographic evidence live before the United Nations Security Council.',
        lens: 'Model III (Bureaucratic Politics)',
        lensShort: 'Model III',
        stabilityDelta: -10,
        defconDelta: 0,
        expectedPrediction: 'pred-sub-bargain',
        feedback: {
          outcome: 'partial',
          consequence: 'Stevenson delivers a public relations triumph ("Don\'t wait for the translation!"), rallying neutral states but locking Soviet delegates into rigid public defiance.',
          mechanism: 'Model III (Bureaucratic Politics): Key actors leverage public and institutional platforms to shift domestic and international bargaining leverage.',
          citation: 'Allison (1971), Essence of Decision, pp. 193-210',
          misconception: MISCONCEPTIONS['model-hierarchy']
        },
        advisorReaction: 'Stevenson radios: "Zorin is trapped on camera. The diplomatic coalition holds firm."',
        mapEffect: { type: 'vector', color: 'amber', label: 'UNSC PUBLIC FORUM [NEW YORK]' }
      }
    ]
  },
  {
    act: 3,
    title: 'Act 3: Endgame on Black Saturday',
    date: 'October 27, 1962',
    brief: 'Tension hits DEFCON 2. Major Rudolf Anderson\'s U-2 is shot down over Cuba by a Soviet SAM site. Radio Moscow demands the withdrawal of US Jupiter missiles stationed in Izmir, Turkey.',
    sigint: 'SIGINT INTERCEPT: Turkish leadership and NATO commanders warn that a public missile trade will destroy NATO\'s extended deterrence credibility across Europe.',
    predictionQuestion: 'Predict which political reality makes a public Jupiter missile trade explosive:',
    predictionOptions: [
      {
        id: 'pred-end-bargain',
        text: 'Inter-agency conflict and NATO alliance politics will punish any public concession (Model III).',
        expectedModel: 'III'
      },
      {
        id: 'pred-end-sop',
        text: 'Air Force missile maintenance routines in Turkey cannot be stopped by civilian order (Model II).',
        expectedModel: 'II'
      },
      {
        id: 'pred-end-rational',
        text: 'Both sides will calculate exact warhead exchange ratios without domestic political friction (Model I).',
        expectedModel: 'I'
      }
    ],
    advisors: [
      {
        name: 'Gen. Maxwell Taylor',
        lens: 'Model II (Organizational Routine)',
        quote: 'A pilot has been killed. Under ExComm pre-delegation guidance, an air reconnaissance attack requires instant retaliatory strikes on the SAM site tomorrow dawn.'
      },
      {
        name: 'Robert F. Kennedy',
        lens: 'Model III (Bureaucratic Politics)',
        quote: 'Dobrynin is at the Justice Department. We give him our private commitment: the Turkish Jupiters will be dismantled in 5 months, but never linked publicly.'
      },
      {
        name: 'National Security Adviser Bundy',
        lens: 'Model I (Rational Strategy)',
        quote: 'A public trade legitimizes blackmail. We must package deterrence and incentive: an ultimatum of strike in 24 hours, sweetened by a private mutual security concession.'
      }
    ],
    options: [
      {
        id: 'dual-track',
        title: 'Secret Quid-Pro-Quo via RFK & Dobrynin',
        desc: 'Offer a public non-invasion guarantee for Cuba coupled with an explicit, secret executive commitment to withdraw Jupiter missiles from Turkey within 5 months.',
        lens: 'Model I (Rational Strategic Action)',
        lensShort: 'Model I',
        stabilityDelta: 0,
        defconDelta: 0,
        expectedPrediction: 'pred-end-bargain',
        feedback: {
          outcome: 'success',
          consequence: 'Khrushchev announces Soviet missiles will be crated and returned. The Turkey withdrawal remains secret, preserving NATO coherence while resolving the immediate existential crisis.',
          mechanism: 'Model I & III Synthesis: Executive leadership resolves strategic deterrence requirements (Model I) while maneuvering around bureaucratic and alliance red lines (Model III).',
          citation: 'Allison & Zelikow (1999), pp. 366-378',
          misconception: null
        },
        advisorReaction: 'RFK confirms: "Dobrynin accepted. Moscow has cabled agreement."',
        mapEffect: { type: 'arc', color: 'cyan', label: 'IZMIR-CUBA MUTUAL PLEDGE [SEALED]' }
      },
      {
        id: 'ultimatum-strike',
        title: '24-Hour Military Strike Ultimatum',
        desc: 'Execute Joint Chiefs recommendation: demand immediate missile dismantling or launch full-scale OPLAN 316 air strikes and amphibious invasion on Monday morning.',
        lens: 'Model II (Organizational Routine)',
        lensShort: 'Model II',
        stabilityDelta: -35,
        defconDelta: -1,
        expectedPrediction: 'pred-end-sop',
        feedback: {
          outcome: 'failure',
          consequence: 'Ultimatum triggers Soviet field dispersal of tactical nuclear weapons (FKR cruise missiles) to Cuban frontline regiments. A catastrophic escalation cycle begins.',
          mechanism: 'Model II (Organizational Routine): Military contingency plans assume that escalating alert states deters the enemy, but adversary military routines respond symmetrically, generating an uncontrollable spiral.',
          citation: 'Allison (1971), pp. 110-143',
          misconception: MISCONCEPTIONS['costless-delay']
        },
        advisorReaction: 'Taylor salutes grimly: "SAC is at full alert. War plans are in motion."',
        mapEffect: { type: 'crosshair', color: 'rose', label: 'OPLAN 316 INVASION VECTORS' }
      },
      {
        id: 'public-trade',
        title: 'Public Acceptance of Turkey-Cuba Trade',
        desc: 'Broadcast an immediate acceptance of Moscow\'s public offer to trade Turkish Jupiter missiles for Cuban SS-4 missiles on Radio Moscow.',
        lens: 'Model III (Bureaucratic Politics)',
        lensShort: 'Model III',
        stabilityDelta: -15,
        defconDelta: 0,
        expectedPrediction: 'pred-end-bargain',
        feedback: {
          outcome: 'partial',
          consequence: 'Cuban missiles are dismantled, but NATO allies in Ankara and Bonn express profound outrage over perceived abandonment. Administration faces severe domestic backlash.',
          mechanism: 'Model III (Bureaucratic Politics): Compromises negotiated purely as transactional horse-trading undermine long-term bureaucratic and alliance consensus.',
          citation: 'Allison (1971), pp. 193-210',
          misconception: MISCONCEPTIONS['model-hierarchy']
        },
        advisorReaction: 'Bundy sighs: "The missiles leave Cuba, but NATO\'s confidence in the American nuclear umbrella is deeply cracked."',
        mapEffect: { type: 'vector', color: 'amber', label: 'PUBLIC ALLIANCE STRAIN [NATO]' }
      }
    ]
  }
];

export const MASTERY_CHECKS = [
  {
    id: 'mc-01',
    question: 'A US naval destroyer drops signaling depth charges on a Soviet submarine strictly adhering to Fleet Training Manual instructions, unaware that civilian ExComm leadership ordered utmost restraint. Which Allison model best explains this outcome?',
    choices: [
      { id: 'c1', text: 'Model I (Rational Actor Model)', correct: false },
      { id: 'c2', text: 'Model II (Organizational Behavior / Routine)', correct: true },
      { id: 'c3', text: 'Model III (Governmental / Bureaucratic Politics)', correct: false }
    ],
    objectiveIndex: 1,
    explanation: 'Model II explains that organizations operate via pre-established Standard Operating Procedures (SOPs). Military units execute their established routines even when those routines contradict presidential diplomatic goals.',
    misconception: MISCONCEPTIONS['unitary-actor']
  },
  {
    id: 'mc-02',
    question: 'During crisis meetings, the Air Force Chief insists on an immediate air strike to validate service prestige and doctrine, while the State Department urges a United Nations compromise to safeguard European alliances. Which Allison model explains this institutional division?',
    choices: [
      { id: 'c1', text: 'Model I (Rational Actor Model)', correct: false },
      { id: 'c2', text: 'Model II (Organizational Behavior / Routine)', correct: false },
      { id: 'c3', text: 'Model III (Governmental / Bureaucratic Politics)', correct: true }
    ],
    objectiveIndex: 1,
    explanation: 'Model III emphasizes that "where you stand depends on where you sit." Decisions reflect pulling and hauling among bureaucratic players with differing organizational interests and priorities.',
    misconception: MISCONCEPTIONS['model-hierarchy']
  },
  {
    id: 'mc-03',
    question: 'An analyst asserts: "The United States government as a single rational actor methodically evaluated all options, calculated cost-benefit trade-offs, and chose the naval quarantine because it maximized deterrence utility while minimizing nuclear risk." Which model is the analyst using?',
    choices: [
      { id: 'c1', text: 'Model I (Rational Actor Model)', correct: true },
      { id: 'c2', text: 'Model II (Organizational Behavior / Routine)', correct: false },
      { id: 'c3', text: 'Model III (Governmental / Bureaucratic Politics)', correct: false }
    ],
    objectiveIndex: 0,
    explanation: 'Model I treats the state as a unitary, value-maximizing actor with consistent strategic goals and calculated optimization across policy alternatives.',
    misconception: MISCONCEPTIONS['unitary-actor']
  }
];

export const TRANSFER_SCENARIO = {
  id: 'transfer-1914',
  title: 'Transfer Case: The 1914 July Crisis and the Imperial Railway Timetables',
  historicalContext: 'On August 1, 1914, Kaiser Wilhelm II received an ambiguous diplomatic dispatch suggesting Britain might guarantee French neutrality if Germany refrained from attacking France. The Kaiser ordered Chief of the General Staff Helmuth von Moltke to immediately halt the German advance into France and redirect the entire army eastward against Russia. Moltke refused, declaring: "Your Majesty, it cannot be done. The deployment of an army of a million men cannot be improvised. If Your Majesty insists on leading the whole army to the East, it will not be an army ready for battle, but a disorganized mob of armed men."',
  question: 'Apply Allison\'s three models to 1914: Moltke\'s refusal to halt the westward deployment because the imperial railway mobilization schedule could not be re-engineered on short notice is the classic historical manifestation of which model?',
  choices: [
    {
      id: 'tf-m2',
      text: 'Model II (Organizational Routine): Rigid military mobilization timetables (SOPs) constrained executive command and transformed a regional crisis into world war.',
      correct: true
    },
    {
      id: 'tf-m1',
      text: 'Model I (Rational Actor Model): A unitary calculation that conquering Belgium and France maximized long-term German economic utility.',
      correct: false
    },
    {
      id: 'tf-m3',
      text: 'Model III (Bureaucratic Politics): A corrupt financial trade between Prussian railway magnates and Bavarian diplomats.',
      correct: false
    }
  ],
  objectiveIndex: 2,
  explanation: 'Moltke\'s mobilization plan was the ultimate Model II organizational routine. Decades of planning locked the German military into inflexible railway schedules that civilian political leaders could not redirect, demonstrating how organizational standard procedures dictate state action under severe time compression.',
  citation: 'Graham Allison (1971), Essence of Decision; Barbara Tuchman (1962), The Guns of August'
};

export const ALLISON_MATRIX = [
  {
    model: 'Model I: Rational Actor Model (RAM)',
    focus: 'Strategic Intent & Optimization',
    perspective1962: 'ExComm as unitary decision-maker balancing deterrence against nuclear catastrophe; quarantine chosen as graduated pressure point.',
    coreInsight: 'Explains what the state was trying to achieve in strategic terms.'
  },
  {
    model: 'Model II: Organizational Behavior',
    focus: 'Standard Operating Procedures & Capabilities',
    perspective1962: 'Navy blockade doctrine, U-2 overflight schedules, and tactical missile alert routines executing with organizational inflexibility.',
    coreInsight: 'Explains why actual operations differed from civilian intent.'
  },
  {
    model: 'Model III: Bureaucratic Politics',
    focus: 'Inter-Agency Bargaining & Positions',
    perspective1962: 'Hawks (LeMay, Taylor) vs Doves (RFK, McNamara, Stevenson); secret Turkey Jupiter concession used to build consensus.',
    coreInsight: 'Explains who bargained to craft the political outcome.'
  }
];

export class CrisisState {
  constructor() {
    this.reset();
  }

  reset() {
    this.act = 1;
    this.stability = 100;
    this.defcon = 3;
    this.phase = 'BRIEF'; // BRIEF, PREDICT, DECIDE, CONSEQUENCE, EXPLAIN, MASTERY, TRANSFER, DEBRIEF
    this.session = new LearningSession(LAB_ID, LEARNING_OBJECTIVES);
    this.currentPrediction = null;
    this.lastDecisionFeedback = null;
    this.greasePencilArcs = [];
    this.masteryIndex = 0;
    this.transferAnswered = false;
  }

  recordPrediction(predictionId) {
    const decisionId = `act-${this.act}`;
    this.currentPrediction = predictionId;
    this.session.recordPrediction(decisionId, predictionId);
  }

  applyDecision(optionId) {
    const actData = CRISIS_ACTS[this.act - 1];
    const opt = actData.options.find(o => o.id === optionId) || actData.options[0];

    this.stability = Math.max(0, Math.min(100, this.stability + opt.stabilityDelta));
    if (opt.defconDelta !== 0) {
      this.defcon = Math.max(1, Math.min(4, this.defcon + opt.defconDelta));
    }

    if (opt.mapEffect) {
      this.greasePencilArcs.push(opt.mapEffect);
    }

    const decisionId = `act-${this.act}`;
    const predicted = this.currentPrediction;
    const actual = opt.expectedPrediction;
    const predictionMatch = (predicted === actual);

    const feedbackPayload = {
      decisionId,
      choice: opt.id,
      correctChoice: 'blockade',
      outcome: opt.feedback.outcome,
      consequence: opt.feedback.consequence,
      mechanism: opt.feedback.mechanism,
      citation: opt.feedback.citation,
      misconception: opt.feedback.misconception,
      misconceptionTag: opt.feedback.misconception ? opt.feedback.misconception.tag : null,
      predicted,
      actual,
      predictionMatch,
      objectiveIndex: this.act - 1
    };

    this.lastDecisionFeedback = feedbackPayload;
    this.session.recordDecision(feedbackPayload);
    return feedbackPayload;
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
