import { LearningSession } from '../../shared/learn/LearningSession.js';
import { chaptersFor, chapterUrl } from '../../shared/learn/ChapterLink.js';

export const LAB_ID = 'lab-03';

export const LEARNING_OBJECTIVES = [
  'Explain Single Undertaking: nothing is agreed until everything is agreed.',
  'Explain why consensus grants every member a sovereign veto point.',
  'Apply cross-sector logrolling to construct a viable omnibus agreement within diplomatic capital constraints.'
];

export const MISCONCEPTIONS = {
  'buy-everyone': {
    tag: 'buy-everyone',
    label: 'Unlinked Buying / Individual Concession Fallacy',
    remediation: 'Individual unilateral concessions cost 15 points, exceeding your 10-capital budget. Consensus under the Single Undertaking requires cross-sector logrolling—linking complementary issues into omnibus packages to reduce net political costs.'
  },
  'holdout-irrational': {
    tag: 'holdout-irrational',
    label: 'Holdouts are Simply Irrational Fallacy',
    remediation: 'Under WTO consensus rules, every member holds a sovereign veto. Blocs hold out not out of obstinacy, but because domestic constituents (e.g., smallholder farmers, manufacturing lobbies) punish uncompensated unilateral losses.'
  },
  'issue-linkage-invalid': {
    tag: 'issue-linkage-invalid',
    label: 'Issue Linkage Distorts Pure Trade Fallacy',
    remediation: 'Cross-issue logrolling (e.g., trading Western agricultural subsidy cuts for emerging market IP and services access) is the structural engine that makes multilateral agreements possible across asymmetric economies.'
  }
};

export const WTO_CONFIG = {
  STARTING_CAPITAL: 10,
  TOTAL_BLOCS: 8
};

export const MEMBER_BLOCS = [
  {
    id: 'us_eu',
    name: 'US-EU Agro-Industrial',
    flag: 'US/EU',
    stance: 'Demands strict intellectual property & digital tariff moratoriums.',
    cost: 2,
    satisfied: false,
    redLine: 'Opposes unconditional agricultural subsidy cuts without reciprocal services access.'
  },
  {
    id: 'g20_ag',
    name: 'G20 Agricultural Exporters',
    flag: 'BRA/IND',
    stance: 'Demands deep cuts to Western domestic farm subsidies and tariff peaks.',
    cost: 3,
    satisfied: false,
    redLine: 'Will veto any deal that ignores agricultural domestic support ceilings.'
  },
  {
    id: 'china_east',
    name: 'East Asian Manufacturing',
    flag: 'CHN/KOR',
    stance: 'Prioritizes tariff reductions on industrial intermediate manufactured goods.',
    cost: 2,
    satisfied: false,
    redLine: 'Rejects mandatory labor standard conditionality attached to trade.'
  },
  {
    id: 'african_ldc',
    name: 'African LDC Group',
    flag: 'LDC/AFR',
    stance: 'Demands permanent Special and Differential Treatment (S&DT) and capacity aid.',
    cost: 1,
    satisfied: false,
    redLine: 'Rejects binding dispute settlement sanctions against small economies.'
  },
  {
    id: 'cairns',
    name: 'Cairns Group Cairns',
    flag: 'AUS/ARG',
    stance: 'Pushes for complete elimination of all agricultural export subsidies.',
    cost: 2,
    satisfied: false,
    redLine: 'Will not accept green-box subsidy loopholes that distort world commodity prices.'
  },
  {
    id: 'small_island',
    name: 'Small Vulnerable Economies (SVE)',
    flag: 'SVE/PAC',
    stance: 'Seeks climate-trade transition exemptions and fisheries subsidies carve-outs.',
    cost: 1,
    satisfied: false,
    redLine: 'Opposes blanket bans on artisanal coastal fisheries subsidies.'
  },
  {
    id: 'latam',
    name: 'Latin America Mercosur',
    flag: 'ARG/BRA',
    stance: 'Demands expanded European beef and bio-fuel quota allocations.',
    cost: 2,
    satisfied: false,
    redLine: 'Rejects environmental non-tariff barriers used for disguised protectionism.'
  },
  {
    id: 'nordic',
    name: 'Friends of Fish / Nordic',
    flag: 'NOR/NZL',
    stance: 'Demands strict multilateral discipline against illegal and overfished fleets.',
    cost: 2,
    satisfied: false,
    redLine: 'Vetoes packages that fail to eliminate harmful fuel and vessel capacity subsidies.'
  }
];

export const COMPLEMENTARY_PACKAGES = [
  {
    id: 'pkg_agri_services',
    name: 'Agro-Industrial Market Access Omnibus',
    blocs: ['us_eu', 'g20_ag'],
    packageCost: 2,
    theory: 'Single Undertaking linkage: Western farm subsidy discipline paired with emerging market IP & services access.'
  },
  {
    id: 'pkg_fisheries_env',
    name: 'Fisheries Subsidies & SVE Exemption Package',
    blocs: ['small_island', 'nordic'],
    packageCost: 1,
    theory: 'Disciplines industrial IUU fishing fleets while preserving artisanal coastal livelihoods.'
  },
  {
    id: 'pkg_agri_export',
    name: 'Cairns-Mercosur Agricultural Export Coalition',
    blocs: ['cairns', 'latam'],
    packageCost: 2,
    theory: 'Harmonizes export subsidy abolition with European beef and bio-fuel quota expansions.'
  },
  {
    id: 'pkg_ind_ldc',
    name: 'East Asia-African LDC Trade & Development Pact',
    blocs: ['china_east', 'african_ldc'],
    packageCost: 1,
    theory: 'Couples manufactured goods tariff cuts with Special & Differential Treatment (S&DT) capacity aid.'
  }
];

export const PREDICTION_OPTIONS = [
  {
    id: 'pred-logroll',
    label: 'Omnibus Logrolling Required: Individual concessions exhaust capital (15 pts); cross-sector linkages are mandatory.'
  },
  {
    id: 'pred-individual',
    label: 'Unilateral Buying: Granting concessions individually to major powers will create sufficient momentum to force consensus.'
  },
  {
    id: 'pred-majority',
    label: 'Majority Override: Securing a supermajority of blocs will legally override holdout developing nation vetoes.'
  }
];

export const MASTERY_CHECKS = [
  {
    id: 'mc-01',
    title: 'Mastery Check 1: Identifying Soft Red Lines & Capacity Constraints',
    prompt: 'In a multilateral trade round, the African LDC Group threatens to veto the entire agreement over dispute settlement rules. Intelligence reveals their domestic legal capacity cannot sustain complex WTO litigation. Which strategy resolves this holdout without depleting the diplomatic budget?',
    choices: [
      { id: 'a', text: 'Package an exemption with targeted technical capacity-building assistance (S&DT) linked to market access.', correct: true },
      { id: 'b', text: 'Offer raw cash concessions equivalent to G20 industrial domestic farm subsidies.', correct: false, misconceptionTag: 'buy-everyone' },
      { id: 'c', text: 'Threaten to expel the LDC group from the multilateral round.', correct: false, misconceptionTag: 'holdout-irrational' },
      { id: 'd', text: 'Ignore their objection and proceed to a majority plenary vote.', correct: false, misconceptionTag: 'issue-linkage-invalid' }
    ],
    remediation: 'Soft red lines rooted in capacity deficits are best resolved through targeted Special & Differential Treatment (S&DT) linkages rather than expensive unilateral concessions.'
  },
  {
    id: 'mc-02',
    title: 'Mastery Check 2: Cross-Sector Logrolling Dynamics',
    prompt: 'Why is cross-sector logrolling (linking non-separable issues like agriculture, TRIPS, and services) necessary to conclude a comprehensive WTO round?',
    choices: [
      { id: 'a', text: 'It allows asymmetric states to trade concessions in areas of low domestic cost for gains in areas of high domestic priority.', correct: true },
      { id: 'b', text: 'It conceals the true cost of trade liberalization from domestic voters.', correct: false, misconceptionTag: 'issue-linkage-invalid' },
      { id: 'c', text: 'It enables large trading powers to buy individual votes sequentially.', correct: false, misconceptionTag: 'buy-everyone' },
      { id: 'd', text: 'It transforms consensus voting into a binding majority rule mechanism.', correct: false }
    ],
    remediation: 'Logrolling creates value across asymmetric economies by allowing nations to concede in sectors where domestic costs are low while gaining in sectors of high national priority.'
  },
  {
    id: 'mc-03',
    title: 'Mastery Check 3: The Single Undertaking and Sovereign Vetoes',
    prompt: 'What is the precise legal and strategic meaning of the WTO "Single Undertaking" principle?',
    choices: [
      { id: 'a', text: '"Nothing is agreed until everything is agreed" — every member must ratify the entire package, giving each state an effective veto.', correct: true },
      { id: 'b', text: 'Agreements take effect immediately once a simple majority of founding members signs.', correct: false },
      { id: 'c', text: 'Nations may pick and choose specific chapters to ratify (a la carte multilateralism).', correct: false, misconceptionTag: 'issue-linkage-invalid' },
      { id: 'd', text: 'Only states with more than 1% of world trade volume possess veto power.', correct: false, misconceptionTag: 'holdout-irrational' }
    ],
    remediation: 'The Single Undertaking dictates that all agreements form an indivisible omnibus package: "Nothing is agreed until everything is agreed," guaranteeing every member an implicit veto.'
  }
];

export const TRANSFER_SCENARIO = {
  id: 'transfer-climate-cop',
  title: 'Transfer Challenge: Climate COP Final Plenary Consensus',
  context: 'At the UN Climate Change Conference (COP), decision-making operates strictly by consensus under UNFCCC rules. At 3:00 AM on the final scheduled day, negotiations on the global energy package are paralyzed: the Alliance of Small Island States (AOSIS) demands an unconditional "phase-out of all fossil fuels", while major fossil-fuel exporting petrostates declare that any reference to "phase-out" is an existential red line that will trigger an immediate formal veto.',
  prompt: 'As the COP President, which multilateral consensus-building strategy breaks the deadlock without triggering a formal veto?',
  choices: [
    {
      id: 'opt_logroll',
      text: 'Cross-Sector Logroll: Replace binary "phase-out" with "transitioning away from fossil fuels in energy systems" (substantive mitigation direction), while simultaneously locking in a fully capitalized Loss and Damage Fund and technology transfer financing for vulnerable states.',
      correct: true,
      feedback: 'Correct! By shifting the language from an existential zero-sum binary to a managed transition while providing tangible compensatory financing (Loss & Damage), both coalitions preserve their core domestic mandates without exercising a veto.'
    },
    {
      id: 'opt_majority',
      text: 'Call a snap plenary vote under simple majority rules to isolate and defeat the petrostates.',
      correct: false,
      misconceptionTag: 'issue-linkage-invalid',
      feedback: 'Incorrect. UNFCCC rules require consensus; attempting to force a majority vote violates procedural rules and causes the entire treaty framework to collapse.'
    },
    {
      id: 'opt_appease_petro',
      text: 'Strip all energy transition clauses entirely from the final text to satisfy the petrostates.',
      correct: false,
      misconceptionTag: 'holdout-irrational',
      feedback: 'Incorrect. Removing all mitigation language causes AOSIS and the High Ambition Coalition to veto the agreement.'
    },
    {
      id: 'opt_bilateral',
      text: 'Offer secret bilateral cash payments to each dissenting delegate individually.',
      correct: false,
      misconceptionTag: 'buy-everyone',
      feedback: 'Incorrect. Individual bilateral bribes cannot resolve structural domestic policy contradictions in a public multilateral plenary.'
    }
  ]
};

export class WtoState {
  constructor() {
    this.session = new LearningSession(LAB_ID, LEARNING_OBJECTIVES);
    this.reset();
  }

  reset() {
    this.capital = WTO_CONFIG.STARTING_CAPITAL;
    this.blocs = JSON.parse(JSON.stringify(MEMBER_BLOCS));
    this.phase = 'BRIEFING'; // BRIEFING, PREDICTING, NEGOTIATING, VOTING, EXPLAIN, MASTERY, TRANSFER, DEBRIEF
    this.voteResult = null;
    this.packages = [];
    this.pendingPrediction = null;
    this.masteryIndex = 0;
  }

  recordPrediction(predictionId) {
    this.pendingPrediction = predictionId;
    this.session.recordPrediction('wto-consensus-vote', predictionId);
    return predictionId;
  }

  packageBloc(idA, idB) {
    let pkg = null;
    if (idA && !idB) {
      pkg = COMPLEMENTARY_PACKAGES.find(p => p.id === idA || p.blocs.includes(idA));
      if (pkg) {
        if (idA === pkg.id) {
          idA = pkg.blocs[0];
          idB = pkg.blocs[1];
        } else {
          idB = pkg.blocs.find(id => id !== idA) || pkg.blocs[1];
        }
      }
    } else if (idA && idB) {
      pkg = COMPLEMENTARY_PACKAGES.find(p => p.blocs.includes(idA) && p.blocs.includes(idB));
    }

    const b1 = this.blocs.find(b => b.id === idA);
    const b2 = this.blocs.find(b => b.id === idB);
    if (!b1 || !b2 || b1.id === b2.id) return false;

    const cost = pkg ? pkg.packageCost : Math.max(1, (b1.cost + b2.cost) - 2);

    const existingPkgIdx = this.packages.findIndex(p => p.blocs.includes(b1.id) && p.blocs.includes(b2.id));
    if (existingPkgIdx !== -1) {
      this.capital += cost;
      b1.satisfied = false;
      b2.satisfied = false;
      delete b1.packageId;
      delete b2.packageId;
      this.packages.splice(existingPkgIdx, 1);
      return true;
    }

    let needed = cost;
    if (b1.satisfied && !b1.packageId) needed -= b1.cost;
    if (b2.satisfied && !b2.packageId) needed -= b2.cost;

    if (this.capital < needed) return false;

    this.capital -= needed;
    b1.satisfied = true;
    b2.satisfied = true;
    const pkgId = pkg ? pkg.id : `${b1.id}_${b2.id}`;
    b1.packageId = pkgId;
    b2.packageId = pkgId;
    this.packages.push({
      id: pkgId,
      name: pkg ? pkg.name : `Linked Package: ${b1.name} & ${b2.name}`,
      blocs: [b1.id, b2.id],
      cost
    });
    return true;
  }

  concedeBloc(blocId) {
    const bloc = this.blocs.find(b => b.id === blocId);
    if (!bloc) return false;

    if (!bloc.satisfied) {
      const pkg = COMPLEMENTARY_PACKAGES.find(p => p.blocs.includes(blocId));
      const partnerId = pkg ? pkg.blocs.find(id => id !== blocId) : null;
      const partner = partnerId ? this.blocs.find(b => b.id === partnerId) : null;

      if (partner && partner.satisfied && !partner.packageId) {
        return this.packageBloc(partner.id, bloc.id);
      }

      if (this.capital < bloc.cost) return false;
      this.capital -= bloc.cost;
      bloc.satisfied = true;
      return true;
    } else {
      if (bloc.packageId) {
        const pkg = COMPLEMENTARY_PACKAGES.find(p => p.id === bloc.packageId);
        const partnerId = pkg ? pkg.blocs.find(id => id !== bloc.id) : null;
        return this.packageBloc(bloc.id, partnerId);
      }
      this.capital += bloc.cost;
      bloc.satisfied = false;
      return true;
    }
  }

  executeConsensusVote() {
    this.phase = 'VOTING';
    const dissentingBlocs = this.blocs.filter(b => !b.satisfied);
    const passed = dissentingBlocs.length === 0;

    let misconception = null;
    if (!passed) {
      if (this.pendingPrediction === 'pred-individual' || (this.packages.length < 4 && this.capital < 3)) {
        misconception = MISCONCEPTIONS['buy-everyone'];
      } else if (this.pendingPrediction === 'pred-majority') {
        misconception = MISCONCEPTIONS['holdout-irrational'];
      } else {
        misconception = MISCONCEPTIONS['issue-linkage-invalid'];
      }
    }

    const predictionMatch = this.pendingPrediction ? (this.pendingPrediction === 'pred-logroll' ? passed : !passed) : null;

    const consequence = passed
      ? `Full consensus achieved! All 8 regional blocs ratified the multilateral package, preserving ${this.capital} diplomatic capital.`
      : `Single Undertaking veto triggered! ${dissentingBlocs.length} dissenting bloc(s) (${dissentingBlocs.map(b => b.name).join(', ')}) exercised sovereign veto power. The entire round is deadlocked.`;

    const mechanism = 'WTO Single Undertaking & Cross-Sector Logrolling: Multilateral consensus requires linking non-separable issue areas so that losses in one sector (agriculture) are compensated by gains in another (services/IP), achieving unanimity under sovereign equality.';
    const citation = 'Mansfield & Busch (2000), The WTO Decision Rules / Odell (2000)';

    this.session.recordDecision({
      decisionId: 'wto-consensus-vote',
      choice: passed ? 'omnibus_consensus' : 'veto_collapse',
      correctChoice: 'omnibus_consensus',
      rationale: mechanism,
      misconceptionTag: misconception ? misconception.tag : null,
      misconception,
      predicted: this.pendingPrediction,
      actual: passed ? 'consensus' : 'veto',
      outcome: passed ? 'success' : 'failure',
      consequence,
      mechanism,
      citation,
      objectiveIndex: 0
    });

    this.voteResult = {
      passed,
      dissentingBlocs,
      concededCount: this.blocs.length - dissentingBlocs.length,
      capitalLeft: this.capital,
      packages: [...this.packages],
      linkedPackages: [...this.packages],
      feedback: {
        outcome: passed ? 'success' : 'failure',
        consequence,
        mechanism,
        citation,
        misconception,
        predictionMatch
      }
    };

    return this.voteResult;
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
    if (!this.voteResult || !this.voteResult.passed) return 0;
    if (this.voteResult.capitalLeft >= 4) return 3;
    if (this.voteResult.capitalLeft >= 1) return 2;
    return 1;
  }

  getReport() {
    return this.session.getReport();
  }
}
