/**
 * PutnamConfig — Configuration, Learning Objectives, Misconceptions,
 * Discrete Policy Clauses, and Two-Level State Machine for Lab 06.
 *
 * Single Source of Truth: EDUCATIONAL_DESIGN_BIBLE.md Section 3 (lab-06)
 */

export const PUTNAM_CONFIG = {
  TOTAL_ROUNDS: 4,
  ELECTORAL_SHOCK_ROUND: 4,
  DOMESTIC_RATIFICATION_THRESHOLD: 65,
  INTERNATIONAL_AGREEMENT_THRESHOLD: 65,
  WIN_SET_MIN_OVERLAP: 60
};

export const PUTNAM_OBJECTIVES = [
  'LO1: Explain two-level games: Level I negotiation constrained by Level II ratification.',
  'LO2: Explain how win-set size determines agreement probability.',
  'LO3: Explain the tied-hands advantage in international bargaining.'
];

export const PUTNAM_MISCONCEPTIONS = {
  DOMESTIC_MINIMISED: {
    tag: 'domestic-minimised',
    label: 'Domestic Politics is a Secondary Constraint',
    remediation: 'Domestic politics is not a secondary hurdle to minimize; Level II ratification defines the feasible win-set. A narrow domestic win-set can serve as a bargaining asset abroad (tied hands).'
  },
  WIDER_ALWAYS_BETTER: {
    tag: 'wider-always-better',
    label: 'A Wider Win-Set is Always Advantageous',
    remediation: 'A wider domestic win-set increases agreement probability but severely weakens bargaining leverage, inviting foreign counterparts to press for maximal concessions.'
  },
  SEPARATE_BARGAINING: {
    tag: 'separate-bargaining',
    label: 'International and Domestic Bargaining are Separate Arenas',
    remediation: 'Level I international agreements directly restructure Level II domestic coalitions, while Level II alignments bound feasible Level I outcomes.'
  }
};

export const PUTNAM_ROUNDS = [
  {
    round: 1,
    title: 'Round 1: Tariff Schedules & Industrial Subsidies',
    topic: 'Manufacturing and Industrial Goods Schedules',
    brief: 'Geneva foreign negotiators demand a 30% tariff reduction on industrial imports. Your domestic manufacturing and labor caucus threatens a legislative revolt if domestic producers face sudden foreign competition.',
    predictPrompt: 'Hypothesize outcome: How will tariff policy choices impact cross-table alignment?',
    predictions: [
      { id: 'intl_surge', label: 'Conceding to Geneva will satisfy foreign partners but trigger domestic backlash.' },
      { id: 'dom_surge', label: 'Protecting domestic industry will satisfy parliament but deadlock the Geneva table.' },
      { id: 'balanced', label: 'Phased reciprocal concessions will expand the overlapping bilateral win-set.' }
    ],
    choices: [
      {
        id: 'unilateral_cuts',
        title: 'Deep Unilateral Tariff Reductions across Manufacturing',
        desc: 'Offer 35% tariff cuts to secure a rapid breakthrough at Level I. Foreign partners are elated, but domestic industry launches a nationwide anti-ratification campaign.',
        level1Delta: 25,
        level2Delta: -25,
        caucuses: { hawks: -15, doves: 15, business: -25 },
        predictedAlignment: 'intl_surge',
        misconception: PUTNAM_MISCONCEPTIONS.DOMESTIC_MINIMISED,
        objectiveIndex: 0,
        outcome: 'partial',
        consequence: 'Geneva delegation welcomes your generosity (+25% Level I), but domestic industrial representatives walk out of parliamentary committee briefings (-25% Level II).',
        mechanism: 'Level I commitments made without regard to domestic ratification coalitions produce severe involuntary defection risk.',
        citation: 'Putnam (1988), Two-Level Games'
      },
      {
        id: 'strict_protectionism',
        title: 'Strict Protectionist Safeguards & Complete Import Quotas',
        desc: 'Refuse all tariff cuts to protect domestic producers and ensure parliamentary approval. Geneva warns that talks are in jeopardy.',
        level1Delta: -25,
        level2Delta: 20,
        caucuses: { hawks: 20, doves: -20, business: 20 },
        predictedAlignment: 'dom_surge',
        misconception: PUTNAM_MISCONCEPTIONS.SEPARATE_BARGAINING,
        objectiveIndex: 1,
        outcome: 'partial',
        consequence: 'Parliamentary trade hawks cheer national protection (+20% Level II), but foreign envoys threaten to abandon the Geneva plenary (-25% Level I).',
        mechanism: 'A domestic win-set with zero overlap with foreign minimum acceptable terms precludes any international agreement.',
        citation: 'Putnam (1988), Two-Level Games'
      },
      {
        id: 'reciprocal_phasing',
        title: 'Reciprocal Tariff Phasing with Adjustment Assistance Fund',
        desc: 'Propose a 10-year phased tariff reduction linked to foreign market access, funded by an industrial worker transition program.',
        level1Delta: 15,
        level2Delta: 15,
        caucuses: { hawks: 5, doves: 15, business: 15 },
        predictedAlignment: 'balanced',
        misconception: null,
        objectiveIndex: 0,
        outcome: 'success',
        consequence: 'Both tables advance in synergy (+15% Level I, +15% Level II). Foreign partners gain predictable market access, while transition funding secures domestic swing-votes.',
        mechanism: 'Synergistic issue-linkage and domestic side-payments expand the overlapping win-set between Level I and Level II.',
        citation: 'Putnam (1988), Two-Level Games'
      }
    ]
  },
  {
    round: 2,
    title: 'Round 2: Environmental & Carbon Regulatory Standards',
    topic: 'Carbon Border Adjustments and Regulatory Harmonization',
    brief: 'Geneva proposes strict supranational emissions standards and border carbon penalties. Domestic energy producers and manufacturing lobbies argue compliance will destroy export competitiveness.',
    predictPrompt: 'Hypothesize outcome: How will environmental commitments reshape domestic ratification?',
    predictions: [
      { id: 'intl_surge', label: 'Supranational standards will satisfy foreign green blocs but trigger parliamentary veto.' },
      { id: 'dom_surge', label: 'Exempting domestic industry will alienate Geneva environmental coalitions.' },
      { id: 'balanced', label: 'A joint clean-technology transition fund will maintain bilateral alignment.' }
    ],
    choices: [
      {
        id: 'supranational_caps',
        title: 'Mandatory Supranational Emission Caps & Immediate Carbon Penalties',
        desc: 'Accept binding international environmental enforcement to lead global climate standards. Domestic energy caucuses organize a formal blocking minority.',
        level1Delta: 25,
        level2Delta: -25,
        caucuses: { hawks: -20, doves: 25, business: -25 },
        predictedAlignment: 'intl_surge',
        misconception: PUTNAM_MISCONCEPTIONS.DOMESTIC_MINIMISED,
        objectiveIndex: 0,
        outcome: 'partial',
        consequence: 'Geneva partners hail the landmark climate treaty (+25% Level I), but domestic parliamentary energy caucuses table a motion of disapproval (-25% Level II).',
        mechanism: 'Agreements exceeding the domestic ratification threshold cannot become law, producing ratification collapse.',
        citation: 'Putnam (1988), Two-Level Games'
      },
      {
        id: 'full_exemption',
        title: 'Full Environmental Carve-Out & National Exemption Clause',
        desc: 'Insist on total exemption from carbon standards to shield domestic industry. Foreign delegations call the carve-out a bad-faith retreat.',
        level1Delta: -25,
        level2Delta: 15,
        caucuses: { hawks: 15, doves: -25, business: 15 },
        predictedAlignment: 'dom_surge',
        misconception: PUTNAM_MISCONCEPTIONS.SEPARATE_BARGAINING,
        objectiveIndex: 1,
        outcome: 'partial',
        consequence: 'Domestic industrial lobbies are pacified (+15% Level II), but foreign delegations suspend technical working groups in protest (-25% Level I).',
        mechanism: 'Unilateral domestic insulation shrinks foreign interest, collapsing the Level I negotiating zone.',
        citation: 'Putnam (1988), Two-Level Games'
      },
      {
        id: 'joint_cleantech',
        title: 'Joint Clean-Technology Innovation Pool with Phased Benchmarks',
        desc: 'Negotiate mutual patent-sharing for clean technologies and establish flexible 8-year decarbonization milestones.',
        level1Delta: 15,
        level2Delta: 15,
        caucuses: { hawks: 10, doves: 20, business: 10 },
        predictedAlignment: 'balanced',
        misconception: null,
        objectiveIndex: 1,
        outcome: 'success',
        consequence: 'Both tables align constructively (+15% Level I, +15% Level II). Clean-tech export credits win over domestic business while meeting foreign environmental benchmarks.',
        mechanism: 'Constructing positive-sum side-payments transforms a potential domestic veto into an offensive export coalition.',
        citation: 'Putnam (1988), Two-Level Games'
      }
    ]
  },
  {
    round: 3,
    title: 'Round 3: Dispute Settlement & Judicial Sovereignty',
    topic: 'Supranational Arbitration vs Sovereign Domestic Courts',
    brief: 'Foreign trading partners demand an investor-state dispute settlement (ISDS) tribunal with binding authority. Domestic constitutional scholars and nationalist hawks declare external tribunals an intolerable erosion of sovereignty.',
    predictPrompt: 'Hypothesize outcome: How does institutional dispute design affect ratification feasibility?',
    predictions: [
      { id: 'intl_surge', label: 'Supranational binding tribunals satisfy investors but ignite constitutional revolt.' },
      { id: 'dom_surge', label: 'Rejecting external dispute settlement causes foreign partners to withhold investments.' },
      { id: 'balanced', label: 'Exhaustion of local remedies paired with bilateral appellate review preserves consensus.' }
    ],
    choices: [
      {
        id: 'supranational_isds',
        title: 'Binding Supranational ISDS Tribunal with Direct Effect',
        desc: 'Grant foreign corporations direct standing to sue in international arbitration. National sovereign caucuses brand this an infringement of constitutionality.',
        level1Delta: 25,
        level2Delta: -30,
        caucuses: { hawks: -30, doves: 10, business: 15 },
        predictedAlignment: 'intl_surge',
        misconception: PUTNAM_MISCONCEPTIONS.WIDER_ALWAYS_BETTER,
        objectiveIndex: 1,
        outcome: 'partial',
        consequence: 'Multinational corporations and foreign partners celebrate full legal protection (+25% Level I), but parliamentary constitutional committees issue an adverse report (-30% Level II).',
        mechanism: 'Ceding sovereign jurisdictional authority generates intense Level II ratification friction that cannot be bought off with modest economic gains.',
        citation: 'Putnam (1988), Two-Level Games'
      },
      {
        id: 'sole_domestic_courts',
        title: 'Sole Domestic Court Adjudication with Zero External Recourse',
        desc: 'Refuse all external dispute mechanisms. Foreign counterparts insist they cannot trust domestic courts to protect foreign assets.',
        level1Delta: -25,
        level2Delta: 20,
        caucuses: { hawks: 25, doves: -15, business: -15 },
        predictedAlignment: 'dom_surge',
        misconception: PUTNAM_MISCONCEPTIONS.SEPARATE_BARGAINING,
        objectiveIndex: 0,
        outcome: 'partial',
        consequence: 'Nationalist hawks celebrate sovereign independence (+20% Level II), but foreign delegations warn that without dispute mechanisms, the treaty is unenforceable (-25% Level I).',
        mechanism: 'Credible commitment failure at Level I prevents foreign principals from ratifying agreements on their own Level II tables.',
        citation: 'Putnam (1988), Two-Level Games'
      },
      {
        id: 'exhaustion_appellate',
        title: 'Exhaustion of Domestic Remedies with Joint Bilateral Appellate Panel',
        desc: 'Require foreign claimants to exhaust domestic court remedies first, backed by a balanced bilateral state-to-state appellate body.',
        level1Delta: 15,
        level2Delta: 15,
        caucuses: { hawks: 15, doves: 10, business: 15 },
        predictedAlignment: 'balanced',
        misconception: null,
        objectiveIndex: 1,
        outcome: 'success',
        consequence: 'Balanced institutional design protects domestic judicial primacy while providing foreign partners an ultimate recourse (+15% Level I, +15% Level II).',
        mechanism: 'Institutional checks that reconcile domestic constitutional sovereignty with reciprocal dispute resolution preserve win-set overlap.',
        citation: 'Putnam (1988), Two-Level Games'
      }
    ]
  },
  {
    round: 4,
    title: 'Round 4: Parliamentary Electoral Shock & The Tied-Hands Gambit',
    topic: 'Snap Election Shocks the Domestic Chamber and Shrinks the Win-Set',
    brief: 'DOMESTIC ELECTORAL SHOCK! A sudden parliamentary snap election elevates nationalist hawks. Ratification threshold surges to 65%! The domestic win-set violently contracts. Foreign counterparts in Geneva demand final concessions before signing.',
    predictPrompt: 'Hypothesize outcome: Can presenting domestic constraint (tied hands) extract concessions from Geneva?',
    predictions: [
      { id: 'intl_capitulate', label: 'Conceding to Geneva will sign the treaty abroad but cause involuntary defection at home.' },
      { id: 'walk_away', label: 'Walking away will please domestic hawks but result in total diplomatic collapse.' },
      { id: 'tied_hands', label: 'Presenting domestic deadlock abroad (tied hands) will compel Geneva to make the concession.' }
    ],
    choices: [
      {
        id: 'concede_to_geneva',
        title: 'Concede to Geneva Demands with Unilateral Agricultural Quotas',
        desc: 'Yield to Geneva pressure to finalize the signature abroad. The new parliamentary majority declares the concession an outrage.',
        level1Delta: 20,
        level2Delta: -35,
        caucuses: { hawks: -40, doves: -10, business: -20 },
        predictedAlignment: 'intl_capitulate',
        misconception: PUTNAM_MISCONCEPTIONS.WIDER_ALWAYS_BETTER,
        objectiveIndex: 2,
        outcome: 'failure',
        consequence: 'INVOLUNTARY DEFECTION OCCURS! You triumphantly sign the treaty in Geneva, but the new parliamentary chamber votes it down 68% to 32% (Level II collapses).',
        mechanism: 'Classic involuntary defection: a negotiator reaches a Level I deal abroad that falls completely outside the contracted domestic win-set, resulting in humiliating parliamentary rejection.',
        citation: 'Putnam (1988), Two-Level Games'
      },
      {
        id: 'abandon_geneva',
        title: 'Declare Diplomatic Impasse and Walk Out of Geneva Plenary',
        desc: 'Bow to hawkish domestic pressure and abandon the international treaty altogether.',
        level1Delta: -45,
        level2Delta: 10,
        caucuses: { hawks: 20, doves: -40, business: -30 },
        predictedAlignment: 'walk_away',
        misconception: PUTNAM_MISCONCEPTIONS.DOMESTIC_MINIMISED,
        objectiveIndex: 2,
        outcome: 'failure',
        consequence: 'Complete negotiation breakdown. Geneva talks terminate in recrimination (-45% Level I), leaving both nations trapped in a tariff spiral.',
        mechanism: 'Treating domestic political resistance as an insurmountable barrier rather than a bargaining lever forfeits all gains from international cooperation.',
        citation: 'Putnam (1988), Two-Level Games'
      },
      {
        id: 'tied_hands_gambit',
        title: 'Deploy the Tied-Hands Gambit: Present Domestic Deadlock to Force Foreign Concessions',
        desc: 'Putnam / Schelling Tied-Hands strategy: Lay parliament’s strict 65% threshold directly before Geneva envoys, demonstrating that unless Geneva concessions expand, treaty ratification is mathematically impossible.',
        level1Delta: 15,
        level2Delta: 20,
        caucuses: { hawks: 25, doves: 10, business: 20 },
        predictedAlignment: 'tied_hands',
        misconception: null,
        objectiveIndex: 2,
        outcome: 'success',
        consequence: 'THE TIED-HANDS MASTERSTROKE! Faced with undeniable evidence of domestic legislative deadlock, Geneva realizes you cannot budge and concedes key agricultural provisions to save the deal (+15% Level I, +20% Level II).',
        mechanism: 'The Schelling-Putnam Paradox: a narrower domestic win-set strengthens bargaining leverage at Level I when foreign counterparts understand that domestic ratification constraints are credible and binding.',
        citation: 'Putnam (1988), Two-Level Games'
      }
    ]
  }
];

export const PUTNAM_MASTERY_CHECKS = [
  {
    questionId: 'putnam-mc-01',
    question: 'According to Robert Putnam, what constitutes "involuntary defection" in a two-level game?',
    objectiveIndex: 0,
    options: [
      { id: 'a', text: 'A state secretly violates an agreement after ratification to gain competitive advantage.' },
      { id: 'b', text: 'A chief negotiator reaches an international agreement (Level I), but domestic institutions refuse to ratify it (Level II).', correct: true },
      { id: 'c', text: 'A weaker state breaks an alliance when an adversary offers economic incentives.' },
      { id: 'd', text: 'A regional trading bloc collapses due to external monetary shocks.' }
    ],
    misconception: PUTNAM_MISCONCEPTIONS.DOMESTIC_MINIMISED
  },
  {
    questionId: 'putnam-mc-02',
    question: 'How can a domestically constrained negotiator ("tied hands") achieve greater bargaining advantage at Level I?',
    objectiveIndex: 2,
    options: [
      { id: 'a', text: 'Domestic strikes distract foreign intelligence services from assessing true costs.' },
      { id: 'b', text: 'Foreign counterparts make concessions because they recognize the negotiator genuinely lacks domestic power to ratify a weaker compromise.', correct: true },
      { id: 'c', text: 'A narrow domestic win-set allows the chief negotiator to unilaterally rewrite international law.' },
      { id: 'd', text: 'Constitutional constraints legally prohibit foreign envoys from walking away from negotiations.' }
    ],
    misconception: PUTNAM_MISCONCEPTIONS.WIDER_ALWAYS_BETTER
  },
  {
    questionId: 'putnam-mc-03',
    question: 'Why does an excessively wide domestic win-set (Level II) sometimes disadvantage a chief negotiator in international bargaining?',
    objectiveIndex: 1,
    options: [
      { id: 'a', text: 'Foreign counterparts recognize the negotiator has broad legislative leeway and push for maximal concessions.', correct: true },
      { id: 'b', text: 'Broad domestic support automatically triggers supranational anti-trust investigations.' },
      { id: 'c', text: 'A large ratification coalition legally requires unanimous parliamentary voting.' },
      { id: 'd', text: 'International courts refuse to certify treaties supported by broad majorities.' }
    ],
    misconception: PUTNAM_MISCONCEPTIONS.WIDER_ALWAYS_BETTER
  }
];

export const PUTNAM_TRANSFER = {
  scenarioId: 'transfer-eu-uk-withdrawal',
  title: 'Transfer Case: The EU–UK Withdrawal Agreement & Northern Ireland Protocol',
  context: 'In November 2018, UK Prime Minister Theresa May concluded the Withdrawal Agreement in Brussels (Level I), featuring the Northern Ireland "backstop". However, in Westminster (Level II), the Democratic Unionist Party (DUP) and European Research Group (ERG) backbenchers formed an unyielding blocking coalition, rejecting the treaty three times in Parliament.',
  prompt: 'Analyze this historical impasse using Putnam\'s Two-Level Games framework. What structural failure caused the 2019 impasse, and how was ratification ultimately unlocked in late 2019?',
  objectiveIndex: 0,
  options: [
    {
      id: 'opt_a',
      text: 'Brussels had an empty win-set, so any treaty signed was legally null and void under EU law.'
    },
    {
      id: 'opt_b',
      text: 'Classic Involuntary Defection: May negotiated a Level I deal outside her domestic Level II win-set. Ratification required restructuring Level II through a general election and altering the Northern Ireland customs frontier.',
      correct: true
    },
    {
      id: 'opt_c',
      text: 'Westminster was acting as a unitary rational actor (Allison Model I) seeking to maximize tariff revenues.'
    },
    {
      id: 'opt_d',
      text: 'The failure occurred because international treaties require 100% legislative unanimity under British common law.'
    }
  ]
};

export class PutnamState {
  constructor() {
    this.reset();
  }

  reset() {
    this.round = 1;
    this.table1Progress = 35;
    this.table2Progress = 35;
    this.winSetOverlap = 35;
    this.caucuses = {
      hawks: 45,
      doves: 50,
      business: 50
    };
    this.history = [];
    this.phase = 'BRIEFING';
    this.involuntaryDefection = false;
  }

  calculateWinSet() {
    const skew = Math.abs(this.table1Progress - this.table2Progress);
    const avg = (this.table1Progress + this.table2Progress) / 2;

    const threshold = this.round >= PUTNAM_CONFIG.ELECTORAL_SHOCK_ROUND
      ? PUTNAM_CONFIG.DOMESTIC_RATIFICATION_THRESHOLD
      : 50;

    if (this.table1Progress >= 60 && this.table2Progress < threshold) {
      this.involuntaryDefection = true;
      this.winSetOverlap = Math.max(0, Math.round(this.table2Progress - 15));
      return;
    }

    this.involuntaryDefection = false;
    if (skew <= 15) {
      this.winSetOverlap = Math.min(100, Math.round(avg));
    } else {
      this.winSetOverlap = Math.max(0, Math.round(Math.min(this.table1Progress, this.table2Progress) - (skew * 0.45)));
    }
  }

  applyPolicyChoice(choice) {
    this.table1Progress = Math.max(0, Math.min(100, this.table1Progress + choice.level1Delta));
    this.table2Progress = Math.max(0, Math.min(100, this.table2Progress + choice.level2Delta));

    if (choice.caucuses) {
      this.caucuses.hawks = Math.max(0, Math.min(100, this.caucuses.hawks + choice.caucuses.hawks));
      this.caucuses.doves = Math.max(0, Math.min(100, this.caucuses.doves + choice.caucuses.doves));
      this.caucuses.business = Math.max(0, Math.min(100, this.caucuses.business + choice.caucuses.business));
    }

    this.calculateWinSet();

    this.history.push({
      round: this.round,
      choiceId: choice.id,
      choiceTitle: choice.title,
      level1: this.table1Progress,
      level2: this.table2Progress,
      winSet: this.winSetOverlap,
      involuntaryDefection: this.involuntaryDefection
    });
  }

  getStars() {
    if (this.involuntaryDefection) return 0;
    if (this.winSetOverlap >= 70 && this.table1Progress >= 65 && this.table2Progress >= 65) return 3;
    if (this.winSetOverlap >= 50 && this.table2Progress >= 50) return 2;
    if (this.winSetOverlap >= 30) return 1;
    return 0;
  }

  getOutcome() {
    if (this.involuntaryDefection) {
      return {
        rank: 'INVOLUNTARY DEFECTION',
        heading: 'Treaty Rejected by Domestic Parliament (0★)',
        text: 'Classic Putnam Level II failure: You signed a wide agreement in Geneva, but it fell outside the domestic parliamentary win-set. Domestic caucuses revolted and refused ratification.'
      };
    }
    const stars = this.getStars();
    if (stars === 3) {
      return {
        rank: 'BILATERAL MASTER',
        heading: 'Bilateral Ratification Triumph (★3)',
        text: 'You mastered Robert Putnam\'s Two-Level Game! By deploying the tied-hands gambit and harmonizing Level I concessions with Level II legislative caucuses, the treaty achieved formal ratification at both tables.'
      };
    }
    if (stars === 2) {
      return {
        rank: 'RATIFIED WITH FRICTION',
        heading: 'Narrow Ratification with Reservations (★2)',
        text: 'The treaty passed, but persistent domestic friction and tight margins limited bilateral trade expansion.'
      };
    }
    return {
      rank: 'FRAGILE COMPROMISE',
      heading: 'Minimal Accords Reached (★1)',
      text: 'A skeletal accord was ratified, but substantive economic and environmental clauses were stripped.'
    };
  }
}
