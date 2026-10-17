/**
 * ScsConfig — Configuration, Learning Objectives, Misconceptions,
 * ASEAN Way Consensus Mechanics, Faction Dials, and Live Communiqué Pipeline.
 *
 * Single Source of Truth: EDUCATIONAL_DESIGN_BIBLE.md Section 3 (lab-09)
 */

export const SCS_CONFIG = {
  TOTAL_ROUNDS: 3,
  COLLAPSE_THRESHOLD: 25,
  THREE_STAR_AGREEMENT: 65,
  THREE_STAR_MIN_FACTION: 40,
  TWO_STAR_AGREEMENT: 45,
  TWO_STAR_MIN_FACTION: 30
};

export const SCS_OBJECTIVES = [
  'LO1: Explain the ASEAN Way: consensus (musyawarah-mufakat), non-interference, informality.',
  'LO2: Explain the tension between legal enforceability and consensus survival.',
  'LO3: Explain the chair\'s role in shaping outcomes.'
];

export const SCS_MISCONCEPTIONS = {
  CONSENSUS_IS_UNANIMITY: {
    tag: 'consensus-is-unanimity',
    label: 'Consensus Equals Unanimity of Preference',
    remediation: 'Consensus in ASEAN requires the absence of formal open dissent or veto, not identical preferences. Members accommodate, abstain, or bracket divisive clauses to preserve collective solidarity.'
  },
  BINDING_ALWAYS_BETTER: {
    tag: 'binding-always-better',
    label: 'A Legally Binding Code is Always Superior',
    remediation: 'Demanding immediate supranational legal enforceability can shatter the fragile coalition under great-power asymmetric pressure, resulting in total summit collapse and worse anarchy.'
  },
  CHAIR_IS_NEUTRAL: {
    tag: 'chair-is-neutral',
    label: 'The ASEAN Chair is Merely a Neutral Referee',
    remediation: 'The ASEAN Chair controls draft joint text, sequences ministerial consultations, and conducts shuttle diplomacy, actively determining whether consensus survives or fractures.'
  }
};

export const SCS_ROUNDS = [
  {
    round: 1,
    title: 'Round 1: Maritime Scope & Geographic Delimitation',
    topic: 'Defining Geographic Scope of the Code of Conduct (COC)',
    brief: 'The Summit opens on geographic scope. Claimant states (Vietnam, Philippines) demand explicit coverage of the Spratly and Paracel archipelagos. Non-claimants (Cambodia, Laos) warn that naming specific features will provoke an immediate Chinese walkout.',
    predictPrompt: 'Hypothesize outcome: How will naming specific disputed archipelagos affect summit cohesion?',
    predictions: [
      { id: 'legal_push', label: 'Naming specific archipelagos will appease claimants but push China toward a veto.' },
      { id: 'capitulate', label: 'Recognizing historic rights will satisfy Beijing but trigger claimant walkout.' },
      { id: 'normative_unclos', label: 'Grounding scope in 1982 UNCLOS without naming disputed features will preserve consensus.' }
    ],
    choices: [
      {
        id: 'explicit_archipelagos',
        title: 'Explicit Spratly & Paracel Archipelagos Coverage',
        desc: 'Insist on naming all contested features. Satisfies claimants (+25) and Western partners (+15), but triggers severe resistance from China (-30) and non-claimants (-20).',
        shifts: { claimants: 25, nonClaimants: -20, china: -30, partners: 15 },
        agreementDelta: 15,
        clauseTitle: 'Clause 1: Geographic Scope',
        clauseText: 'Article 1: Scope strictly encompasses all features within the Spratly and Paracel Archipelagos.',
        clauseStatus: 'contested',
        predictedAlignment: 'legal_push',
        misconception: SCS_MISCONCEPTIONS.BINDING_ALWAYS_BETTER,
        objectiveIndex: 1,
        outcome: 'partial',
        consequence: 'Claimants celebrate legal precision, but Chinese delegates signal a potential veto and non-claimants express deep unease.',
        mechanism: 'Directly challenging territorial claims in draft text breaches informal ASEAN norms and provokes great-power rejection.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      },
      {
        id: 'historic_rights',
        title: 'Bilateral Historical Rights & Sovereign Exclusions',
        desc: 'Exclude multilateral jurisdiction and recognize historic rights. Pacifies Beijing (+25) and non-claimants (+20), but shatters claimant solidarity (-35 Claimants).',
        shifts: { claimants: -35, nonClaimants: 20, china: 25, partners: -25 },
        agreementDelta: 10,
        clauseTitle: 'Clause 1: Geographic Scope',
        clauseText: 'Article 1: Maritime jurisdiction shall be settled strictly through bilateral channels respecting historic titles.',
        clauseStatus: 'vetoed',
        predictedAlignment: 'capitulate',
        misconception: SCS_MISCONCEPTIONS.CHAIR_IS_NEUTRAL,
        objectiveIndex: 0,
        outcome: 'failure',
        consequence: 'Vietnam and the Philippines condemn the draft as total capitulation, threatening an immediate summit walkout.',
        mechanism: 'Ignoring core security interests of littoral members forces them to exercise their informal veto, destroying consensus.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      },
      {
        id: 'unclos_demilitarized',
        title: 'UNCLOS 1982 Legal Regime with Functional Safety Buffers',
        desc: 'Anchor geographic scope in universal maritime regimes under 1982 UNCLOS and establish demilitarized safety buffers without prejudicing sovereignty.',
        shifts: { claimants: 15, nonClaimants: 10, china: 10, partners: 15 },
        agreementDelta: 25,
        clauseTitle: 'Clause 1: Geographic Scope',
        clauseText: 'Article 1: The Parties reaffirm adherence to 1982 UNCLOS maritime zones and establish demilitarized navigation safety buffers.',
        clauseStatus: 'accepted',
        predictedAlignment: 'normative_unclos',
        misconception: null,
        objectiveIndex: 0,
        outcome: 'success',
        consequence: 'Superb consensus drafting! Universal international legal framing protects claimant rights while remaining acceptable to Beijing.',
        mechanism: 'Constructive normative framing enables consensus by rooting agreements in universally recognized international conventions.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      }
    ]
  },
  {
    round: 2,
    title: 'Round 2: Dispute Settlement & Legal Bindingness',
    topic: 'Mandatory Third-Party Arbitration vs Informal Conciliation',
    brief: 'The critical institutional crossroad: Should the Code of Conduct enforce mandatory third-party arbitration under UNCLOS Part XV, or rely on informal ASEAN consultations under the Treaty of Amity and Cooperation (TAC)?',
    predictPrompt: 'Hypothesize outcome: What occurs if the Chair enforces mandatory binding arbitration?',
    predictions: [
      { id: 'mandatory_shock', label: 'Mandatory arbitration will rally claimants but push China and non-claimants into the collapse threshold.' },
      { id: 'toothless_talks', label: 'Toothless non-binding consultations will cause claimant walkout.' },
      { id: 'fact_finding', label: 'A Joint Maritime Fact-Finding Commission will institutionalize monitoring without triggering a walkout.' }
    ],
    choices: [
      {
        id: 'mandatory_arbitration',
        title: 'Mandatory Third-Party Arbitration under UNCLOS Part XV',
        desc: 'BIBLE REBALANCED: Maximum legal enforceability. Claimants (+30) and Western partners (+30) rejoice, but China (-40) and non-claimants (-30) plummet toward the collapse threshold!',
        shifts: { claimants: 30, nonClaimants: -30, china: -40, partners: 30 },
        agreementDelta: 25,
        clauseTitle: 'Clause 2: Dispute Settlement',
        clauseText: 'Article 2: All disputes shall be subject to mandatory, binding third-party arbitration under UNCLOS Part XV.',
        clauseStatus: 'contested',
        predictedAlignment: 'mandatory_shock',
        misconception: SCS_MISCONCEPTIONS.BINDING_ALWAYS_BETTER,
        objectiveIndex: 1,
        outcome: 'partial',
        consequence: 'Western allies applaud legal enforcement, but Chinese envoys slam their briefing folders and prepare to abort the summit!',
        mechanism: 'The tension between enforceability and consensus: attempting to bind a great power without consent breaches ASEAN consensus norms.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      },
      {
        id: 'toothless_dialogue',
        title: 'Confidential Bilateral Talks with Zero Multilateral Reporting',
        desc: 'Revert to pure non-binding bilateral discussions. China is delighted (+20), but claimants (-35) and dialogue partners (-30) declare the Code utterly worthless.',
        shifts: { claimants: -35, nonClaimants: 15, china: 20, partners: -30 },
        agreementDelta: 5,
        clauseTitle: 'Clause 2: Dispute Settlement',
        clauseText: 'Article 2: Disputes shall be addressed strictly through confidential, bilateral talks with zero multilateral reporting.',
        clauseStatus: 'vetoed',
        predictedAlignment: 'toothless_talks',
        misconception: SCS_MISCONCEPTIONS.CONSENSUS_IS_UNANIMITY,
        objectiveIndex: 1,
        outcome: 'failure',
        consequence: 'Claimants walk toward the microphones to declare ASEAN Centrality dead, rejecting the entire communiqué draft.',
        mechanism: 'Surrendering multilateral dispute oversight destroys claimant confidence in ASEAN as a credible security platform.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      },
      {
        id: 'tac_fact_finding',
        title: 'Multilateral Fact-Finding Commission under ASEAN High Council',
        desc: 'Establish a joint technical monitoring commission and voluntary conciliation protocol under the Treaty of Amity and Cooperation (TAC).',
        shifts: { claimants: 15, nonClaimants: 15, china: 10, partners: 10 },
        agreementDelta: 25,
        clauseTitle: 'Clause 2: Dispute Settlement',
        clauseText: 'Article 2: Establish a Joint Fact-Finding Group and technical conciliation protocol under the Treaty of Amity and Cooperation (TAC).',
        clauseStatus: 'accepted',
        predictedAlignment: 'fact_finding',
        misconception: null,
        objectiveIndex: 0,
        outcome: 'success',
        consequence: 'A brilliant diplomatic compromise! Informal conciliation creates verified transparency without humiliating sovereign participants.',
        mechanism: 'The ASEAN Way favors peer consultation (musyawarah) and quiet diplomacy over adversarial legal litigation.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      }
    ]
  },
  {
    round: 3,
    title: 'Round 3: Military Exercises & External Defense Partnerships',
    topic: 'Freedom of Navigation, Foreign Drills, and Sovereign Alliances',
    brief: 'Final ministerial drafting: China proposes prohibiting naval exercises with non-regional navies (e.g. US, Japan) without unanimous consent. The Philippines and Vietnam insist their bilateral defense pacts are non-negotiable sovereign rights.',
    predictPrompt: 'Hypothesize outcome: Can operational safety be enhanced without restricting sovereign alliances?',
    predictions: [
      { id: 'ban_foreign', label: 'Banning non-regional drills will appease China but trigger a claimant veto.' },
      { id: 'multilateral_patrols', label: 'Mandating joint patrols with external allies will cause Chinese walkout.' },
      { id: 'cues_advance_notice', label: 'Adopting CUES and 30-day advance notification will balance transparency with defense rights.' }
    ],
    choices: [
      {
        id: 'ban_non_regional',
        title: 'Prohibit Military Exercises with Non-Regional Powers',
        desc: 'Accede to China’s proposal. China (+25) and non-claimants (+15) approve, but claimants (-35) and dialogue partners (-35) veto the communiqué.',
        shifts: { claimants: -35, nonClaimants: 15, china: 25, partners: -35 },
        agreementDelta: 10,
        clauseTitle: 'Clause 3: Naval Exercises',
        clauseText: 'Article 3: Military exercises with non-regional navies are prohibited without unanimous consensus of littoral states.',
        clauseStatus: 'vetoed',
        predictedAlignment: 'ban_foreign',
        misconception: SCS_MISCONCEPTIONS.CHAIR_IS_NEUTRAL,
        objectiveIndex: 2,
        outcome: 'failure',
        consequence: 'The Philippines invokes its Mutual Defense Treaty with the US, exercising a formal veto over the draft communiqué.',
        mechanism: 'Attempting to dismantle member states’ sovereign external alliances fractures regional cohesion irrecoverably.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      },
      {
        id: 'mandate_patrols',
        title: 'Mandate Coordinated Naval Patrols with External Partners',
        desc: 'Institutionalize joint freedom-of-navigation patrols with US and Quad navies. Partners (+30) and claimants (+20) agree, but China (-40) walks out.',
        shifts: { claimants: 20, nonClaimants: -25, china: -40, partners: 30 },
        agreementDelta: 15,
        clauseTitle: 'Clause 3: Naval Exercises',
        clauseText: 'Article 3: ASEAN littoral navies shall conduct joint freedom-of-navigation exercises with external dialogue partners.',
        clauseStatus: 'contested',
        predictedAlignment: 'multilateral_patrols',
        misconception: SCS_MISCONCEPTIONS.BINDING_ALWAYS_BETTER,
        objectiveIndex: 1,
        outcome: 'partial',
        consequence: 'China denounces the communiqué as an anti-China military bloc, declaring the summit terminated.',
        mechanism: 'Transforming ASEAN into a containment instrument against a neighboring great power violates regional neutrality.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      },
      {
        id: 'cues_notification',
        title: 'Code for Unplanned Encounters at Sea (CUES) & Advance Notice',
        desc: 'Operationalize CUES protocols across all navies and coast guards, requiring 30-day advance notification for large-scale drills without sovereign exclusions.',
        shifts: { claimants: 15, nonClaimants: 15, china: 10, partners: 15 },
        agreementDelta: 25,
        clauseTitle: 'Clause 3: Naval Exercises',
        clauseText: 'Article 3: Operationalize CUES protocols and require 30-day advance notice for major naval drills without restricting sovereign defense alliances.',
        clauseStatus: 'accepted',
        predictedAlignment: 'cues_advance_notice',
        misconception: null,
        objectiveIndex: 2,
        outcome: 'success',
        consequence: 'Consensus preserved! Confidence-building measures (CBMs) reduce collision risks while respecting every nation’s defense autonomy.',
        mechanism: 'Functional security cooperation succeeds in Southeast Asia when pragmatic operational rules are separated from sovereignty disputes.',
        citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia'
      }
    ]
  }
];

export const SCS_MASTERY_CHECKS = [
  {
    questionId: 'scs-mc-01',
    question: 'In ASEAN diplomatic practice, what distinguishes "consensus" (musyawarah-mufakat) from "unanimity"?',
    objectiveIndex: 0,
    options: [
      { id: 'a', text: 'Every member state must cast a formal affirmative vote on identical treaty language.' },
      { id: 'b', text: 'Consensus requires the absence of formal open dissent or veto, allowing flexible accommodation without identical preferences.', correct: true },
      { id: 'c', text: 'A two-thirds supermajority overrides dissenting member reservations.' },
      { id: 'd', text: 'The ASEAN Secretary-General possesses unilateral executive authority to certify consensus.' }
    ],
    misconception: SCS_MISCONCEPTIONS.CONSENSUS_IS_UNANIMITY
  },
  {
    questionId: 'scs-mc-02',
    question: 'Why has ASEAN historically favored non-binding normative declarations (like the 2002 DOC) over supranational legal arbitration in the South China Sea?',
    objectiveIndex: 1,
    options: [
      { id: 'a', text: 'Non-binding declarations cannot be referenced in United Nations General Assembly resolutions.' },
      { id: 'b', text: 'Rigid supranational enforcement mechanisms would trigger great-power vetoes and destroy member cohesion under external pressure.', correct: true },
      { id: 'c', text: 'The 1982 UNCLOS legally forbids regional bodies from resolving maritime boundary disputes.' },
      { id: 'd', text: 'ASEAN member constitutions prohibit diplomats from entering into multilateral treaties.' }
    ],
    misconception: SCS_MISCONCEPTIONS.BINDING_ALWAYS_BETTER
  },
  {
    questionId: 'scs-mc-03',
    question: 'How does the ASEAN Chair exercise institutional leadership despite the principle of sovereign equality among members?',
    objectiveIndex: 2,
    options: [
      { id: 'a', text: 'The Chair holds two votes in ministerial roll-calls and can expel uncooperative members.' },
      { id: 'b', text: 'The Chair exercises agenda-setting authority, controls draft text formulations, and conducts informal shuttle diplomacy.', correct: true },
      { id: 'c', text: 'The Chair commands the ASEAN regional peacekeeping standby brigade.' },
      { id: 'd', text: 'The Chair can unilaterally impose economic tariffs on non-compliant dialogue partners.' }
    ],
    misconception: SCS_MISCONCEPTIONS.CHAIR_IS_NEUTRAL
  }
];

export const SCS_TRANSFER = {
  scenarioId: 'transfer-asean-2012-phnom-penh',
  title: 'Transfer Case: The 2012 Phnom Penh ASEAN Summit Breakdown',
  context: 'In July 2012 at the 45th ASEAN Ministerial Meeting in Phnom Penh, host nation Cambodia (acting as ASEAN Chair) refused to permit any reference to Scarborough Shoal or exclusive economic zone disputes in the draft joint communiqué, despite impassioned pleas from the Philippines and Vietnam. For the first time in ASEAN’s 45-year history, the summit adjourned with NO joint communiqué issued.',
  prompt: 'Applying Amitav Acharya\'s analysis of the ASEAN Way, what structural vulnerability caused the 2012 breakdown, and how was ASEAN unity restored shortly thereafter?',
  objectiveIndex: 0,
  options: [
    {
      id: 'opt_a',
      text: 'The failure proved that ASEAN had been formally dissolved under international law.'
    },
    {
      id: 'opt_b',
      text: 'Great-power bilateral leverage fractured member solidarity, and the Chair\'s refusal to accommodate claimant concerns broke the consensus norm; Indonesian FM Marty Natalegawa salvaged unity through shuttle diplomacy resulting in the Six-Point Principles.',
      correct: true
    },
    {
      id: 'opt_c',
      text: 'The breakdown happened because ASEAN had never previously engaged in multilateral diplomacy with China.'
    },
    {
      id: 'opt_d',
      text: 'The failure occurred because the ASEAN Charter legally mandates binding third-party arbitration in all maritime incidents.'
    }
  ]
};

export class ScsState {
  constructor() {
    this.reset();
  }

  reset() {
    this.round = 1;
    this.agreementValue = 20;
    this.factions = {
      claimants: 50,
      nonClaimants: 50,
      china: 50,
      partners: 50
    };
    this.communiqueClauses = [
      { title: 'Clause 1: Geographic Scope', text: '[DRAFT PENDING]', status: 'pending' },
      { title: 'Clause 2: Dispute Settlement', text: '[DRAFT PENDING]', status: 'pending' },
      { title: 'Clause 3: Naval Exercises', text: '[DRAFT PENDING]', status: 'pending' }
    ];
    this.history = [];
    this.phase = 'BRIEFING';
  }

  applyChoice(choice) {
    this.agreementValue = Math.min(100, this.agreementValue + choice.agreementDelta);
    Object.keys(choice.shifts).forEach(k => {
      this.factions[k] = Math.max(0, Math.min(100, this.factions[k] + choice.shifts[k]));
    });

    if (this.communiqueClauses[this.round - 1]) {
      this.communiqueClauses[this.round - 1] = {
        title: choice.clauseTitle,
        text: choice.clauseText,
        status: choice.clauseStatus
      };
    }

    this.history.push({
      round: this.round,
      choiceId: choice.id,
      choiceTitle: choice.title,
      factions: { ...this.factions },
      agreementValue: this.agreementValue,
      collapsed: this.isCollapsed()
    });
  }

  isCollapsed() {
    return Object.values(this.factions).some(v => v < SCS_CONFIG.COLLAPSE_THRESHOLD);
  }

  getCollapsedFaction() {
    for (const [key, val] of Object.entries(this.factions)) {
      if (val < SCS_CONFIG.COLLAPSE_THRESHOLD) return key;
    }
    return null;
  }

  getStars() {
    if (this.isCollapsed()) return 0;
    const minFaction = Math.min(...Object.values(this.factions));
    if (this.agreementValue >= SCS_CONFIG.THREE_STAR_AGREEMENT && minFaction >= SCS_CONFIG.THREE_STAR_MIN_FACTION) {
      return 3;
    }
    if (this.agreementValue >= SCS_CONFIG.TWO_STAR_AGREEMENT && minFaction >= SCS_CONFIG.TWO_STAR_MIN_FACTION) {
      return 2;
    }
    return 1;
  }

  getOutcome() {
    if (this.isCollapsed()) {
      const failed = this.getCollapsedFaction();
      return {
        rank: 'COMMUNIQUÉ COLLAPSE',
        heading: 'Summit Deadlock: Joint Communiqué Vetoed (0★)',
        text: `Consensus broken: Faction [${failed.toUpperCase()}] sentiment dropped below the 25% threshold, triggering an immediate walkout. Akin to the 2012 Phnom Penh failure, the summit concluded without a joint statement.`
      };
    }
    const stars = this.getStars();
    if (stars === 3) {
      return {
        rank: 'CHAIR\'S MASTERPIECE',
        heading: 'Historic Code of Conduct Adopted (★3)',
        text: 'Superb diplomatic navigation of the ASEAN Way! You maintained indivisible consensus across claimants, non-claimants, China, and external partners while securing substantive maritime discipline.'
      };
    }
    if (stars === 2) {
      return {
        rank: 'WATERED-DOWN COMPROMISE',
        heading: 'Consensus Communiqué Signed with Reservations (★2)',
        text: 'The summit preserved ASEAN centrality and avoided public collapse, but substantive legal discipline was sacrificed in favor of non-binding generalities.'
      };
    }
    return {
      rank: 'FRAGILE COMMUNIQUÉ',
      heading: 'Minimal Joint Statement Signed (★1)',
      text: 'A skeletal communiqué was signed, but severe factional friction leaves the regional maritime order precarious.'
    };
  }
}
