import { LearningSession } from '../../shared/learn/LearningSession.js';
import { chaptersFor } from '../../shared/learn/ChapterLink.js';

export const UNSC_CONFIG = {
  REQUIRED_VOTES: 9,
  TOTAL_P5: 5,
  TOTAL_E10: 10,
  AMENDMENT_TOKENS: 5
};

export const UNSC_OBJECTIVES = [
  'State UNSC Article 27(3): 9 affirmative votes including concurring P5 votes.',
  'Explain why one P5 member holds unilateral negative power to terminate substantive resolutions.',
  'Explain how P5 structural divergence produces watered-down resolutions and institutional deadlock.'
];

export const P5_MEMBERS = [
  {
    id: 'usa',
    name: 'United States',
    flag: 'US',
    redLines: [
      'Must protect non-proliferation verification',
      'Cannot establish mandatory judicial referral to ICC'
    ],
    satisfied: false,
    demands: [
      { text: 'Add IAEA unannounced inspections protocol', fulfilled: false },
      { text: 'Preserve unilateral sovereign defense exceptions', fulfilled: false }
    ]
  },
  {
    id: 'gbr',
    name: 'United Kingdom',
    flag: 'GB',
    redLines: [
      'Must maintain maritime freedom of navigation',
      'Opposes vague sanctions enforcement language'
    ],
    satisfied: false,
    demands: [
      { text: 'Explicit UNCLOS maritime transit rights clause', fulfilled: false },
      { text: 'Targeted asset freezes instead of general embargo', fulfilled: false }
    ]
  },
  {
    id: 'fra',
    name: 'France',
    flag: 'FR',
    redLines: [
      'Must preserve humanitarian corridor access',
      'Requires multilateral consensus consultation'
    ],
    satisfied: false,
    demands: [
      { text: 'Independent UN humanitarian observer mission', fulfilled: false },
      { text: 'Regular 90-day Council mandate review', fulfilled: false }
    ]
  },
  {
    id: 'rus',
    name: 'Russian Federation',
    flag: 'RU',
    redLines: [
      'Zero Chapter VII military force authorization',
      'Opposes unilateral regime change language'
    ],
    satisfied: false,
    demands: [
      { text: 'Strike Chapter VII Article 42 armed intervention clause', fulfilled: false },
      { text: 'Affirm sovereign territorial integrity of host nation', fulfilled: false }
    ]
  },
  {
    id: 'chn',
    name: "People's Republic of China",
    flag: 'CN',
    redLines: [
      'Strict non-interference in internal affairs',
      'Opposes punitive sanctions harming civilians'
    ],
    satisfied: false,
    demands: [
      { text: 'Include formal non-interference in sovereign domestic jurisdiction clause', fulfilled: false },
      { text: 'Exempt civilian energy and food infrastructure from sanctions', fulfilled: false }
    ]
  }
];

export const AMENDMENT_TOKENS = [
  {
    id: 't1',
    name: 'IAEA Inspection Rigor',
    targetP5: 'usa',
    demandIdx: 0,
    text: 'Attaches stringent IAEA intrusive nuclear safeguard verifications.'
  },
  {
    id: 't2',
    name: 'Sovereign Integrity Clause',
    targetP5: 'rus',
    demandIdx: 1,
    text: 'Formally affirms sovereign territorial inviolability.'
  },
  {
    id: 't3',
    name: 'Civilian Humanitarian Exemption',
    targetP5: 'chn',
    demandIdx: 1,
    text: 'Guarantees food and medical aid exempt from trade restrictions.'
  },
  {
    id: 't4',
    name: 'Maritime Transit Rights',
    targetP5: 'gbr',
    demandIdx: 0,
    text: 'Reaffirms innocent passage and straits navigation under UNCLOS.'
  },
  {
    id: 't5',
    name: 'UN Observer Mandate',
    targetP5: 'fra',
    demandIdx: 0,
    text: 'Establishes civilian humanitarian monitoring presence.'
  }
];

export const UNSC_CLAUSES = [
  {
    id: 'clause-1',
    title: 'Operative Paragraph 1: Mandate & Enforcement Authority',
    context: 'The Council must define the legal basis for international action in the escalating border war. The Western allies insist on Chapter VII enforcement teeth, while Moscow and Beijing strictly reject any authorization of armed force.',
    predictionPrompt: 'Which P5 power will immediately issue a veto threat if the draft authorizes Chapter VII Article 42 armed military intervention without host-nation consent?',
    predictionOptions: [
      { key: 'A', text: 'Russian Federation and China will issue an immediate veto threat.' },
      { key: 'B', text: 'The United States will veto to protect unilateral defense discretion.' },
      { key: 'C', text: 'France will veto due to budgetary concerns over peacekeeping costs.' }
    ],
    expectedPrediction: 'A',
    choices: [
      {
        id: 'A',
        title: 'Authorize Article 42 Armed Military Force (Chapter VII)',
        summary: 'Authorizes Member States to use all necessary military means to suppress hostile actions.',
        correct: false,
        p5Votes: { usa: 'YES', gbr: 'YES', fra: 'YES', rus: 'VETO', chn: 'VETO' },
        e10Votes: 8,
        consequence: 'Russian Federation and China announce immediate veto threats. Moscow denounces the clause as an unlawful mandate for external regime change.',
        mechanism: 'Unilateral P5 Negative Power under UN Charter Article 27(3)',
        citation: 'UN Charter Art. 27(3) / Hurd (2007), After Anarchy',
        misconception: {
          tag: 'misc-majority',
          label: 'Supermajority Fallacy',
          remediation: 'Even if a supermajority of 13 of 15 Security Council members favor military action, a single negative vote from any permanent member terminates the draft under Article 27(3).'
        }
      },
      {
        id: 'B',
        title: 'Restrict to Chapter VI Pacific Settlement of Disputes',
        summary: 'Limits UN role to voluntary non-binding mediation, conciliation, and good offices with zero coercive sanctions.',
        correct: false,
        p5Votes: { usa: 'VETO', gbr: 'VETO', fra: 'ABSTAIN', rus: 'YES', chn: 'YES' },
        e10Votes: 6,
        consequence: 'United States and United Kingdom object vigorously and threaten a veto, refusing to support a toothless resolution while civilian atrocities continue.',
        mechanism: 'Great Power Dissensus & Watered-Down Resolution Impasse',
        citation: 'UN Charter Chapter VI vs VII / Hurd (2007)',
        misconception: {
          tag: 'misc-threat-only',
          label: 'Rhetorical Veto Assumption',
          remediation: 'P5 veto threats are not hollow posturing; drafts that fail to meet minimum security requirements of major powers are routinely vetoed or killed in informal consultations.'
        }
      },
      {
        id: 'C',
        title: 'Adopt Chapter VII Article 41 Targeted Measures with Civilian Humanitarian Carve-Out',
        summary: 'Imposes mandatory targeted financial/arms embargoes under Art. 41 while explicitly guaranteeing sovereign integrity and civilian aid carve-outs.',
        correct: true,
        p5Votes: { usa: 'YES', gbr: 'YES', fra: 'YES', rus: 'ABSTAIN', chn: 'YES' },
        e10Votes: 9,
        consequence: 'All five permanent members clear the clause: US and UK accept economic enforcement, Russia abstains after armed intervention is omitted, and China concurs due to humanitarian protections.',
        mechanism: 'Strategic Compromise & Constructive Abstention under Article 27(3)',
        citation: 'UN Charter Art. 27(3) & Art. 41 / Hurd (2007)',
        misconception: null
      }
    ]
  },
  {
    id: 'clause-2',
    title: 'Operative Paragraph 2: Judicial Accountability & War Crimes Jurisdiction',
    context: 'Evidence of mass civilian atrocities has surfaced. European members demand formal legal accountability, while Washington opposes foreign jurisdiction over non-signatory defense personnel, and Moscow/Beijing defend domestic courts.',
    predictionPrompt: 'How will the United States react if the draft includes an unconditional, mandatory referral to the International Criminal Court (ICC)?',
    predictionOptions: [
      { key: 'A', text: 'The US will issue a veto threat to protect sovereign jurisdiction over non-signatory personnel.' },
      { key: 'B', text: 'The US will enthusiastically vote yes because ICC jurisdiction is universal.' },
      { key: 'C', text: 'The US will be outvoted by a majority of the Security Council.' }
    ],
    expectedPrediction: 'A',
    choices: [
      {
        id: 'A',
        title: 'Mandate Automatic Referral to the International Criminal Court (ICC)',
        summary: 'Transfers universal criminal jurisdiction over all belligerent forces directly to the ICC Prosecutor in The Hague.',
        correct: false,
        p5Votes: { usa: 'VETO', gbr: 'YES', fra: 'YES', rus: 'ABSTAIN', chn: 'ABSTAIN' },
        e10Votes: 8,
        consequence: 'The United States issues a firm veto threat, asserting that non-signatory sovereign defense personnel cannot be subjected to external international courts without treaty consent.',
        mechanism: 'P5 Sovereign Jurisdiction Red Lines',
        citation: 'UN Charter Art. 27(3) / Rome Statute Art. 13(b) / Hurd (2007)',
        misconception: {
          tag: 'misc-majority',
          label: 'Universal Norm Misconception',
          remediation: 'International humanitarian norms cannot override P5 institutional veto prerogatives under Article 27(3); major powers consistently veto jurisdiction that threatens their sovereignty.'
        }
      },
      {
        id: 'B',
        title: 'Grant Total Blanket Immunity to All Combatants and Commanders',
        summary: 'Provides an unconditional legal shield against all international and domestic war-crime prosecutions to facilitate immediate ceasefire.',
        correct: false,
        p5Votes: { usa: 'ABSTAIN', gbr: 'VETO', fra: 'VETO', rus: 'YES', chn: 'YES' },
        e10Votes: 4,
        consequence: 'France and the United Kingdom threaten an immediate veto, stating that a resolution legalizing impunity for war crimes violates core international law and credibility.',
        mechanism: 'Normative Veto Constraints in Multilateral Diplomacy',
        citation: 'Geneva Conventions / Bass (2000), Stay the Hand of Vengeance',
        misconception: {
          tag: 'misc-threat-only',
          label: 'Capitulation Fallacy',
          remediation: 'Appeasing one faction by dismantling core legal principles triggers retaliatory vetoes from opposing P5 members.'
        }
      },
      {
        id: 'C',
        title: 'Establish Independent UN Fact-Finding Commission with Hybrid Special Tribunal',
        summary: 'Authorizes UN fact-finding documentation while rooting criminal prosecutions in national courts supplemented by international jurists.',
        correct: true,
        p5Votes: { usa: 'YES', gbr: 'YES', fra: 'YES', rus: 'ABSTAIN', chn: 'YES' },
        e10Votes: 9,
        consequence: 'The Council reaches consensus: US concurs due to sovereign jurisdiction protections, France and UK gain independent UN documentation, and Russia/China accept the primacy of domestic courts.',
        mechanism: 'Jurisdictional Carve-Outs & P5 Consensus Building',
        citation: 'UN Charter Art. 27(3) / Hurd (2007)',
        misconception: null
      }
    ]
  },
  {
    id: 'clause-3',
    title: 'Operative Paragraph 3: Maritime Verification & Interdiction Regime',
    context: 'Heavy weapons are arriving via coastal shipping lanes. The Council debates how to interdict illicit vessels without violating maritime law or escalating naval standoffs.',
    predictionPrompt: 'Which international maritime principle will China invoke to oppose blanket high-seas naval blockades?',
    predictionOptions: [
      { key: 'A', text: 'UNCLOS commercial freedom of navigation and innocent passage protections.' },
      { key: 'B', text: 'The Warsaw Pact collective defense maritime charter.' },
      { key: 'C', text: 'Exclusive trade monopolies under the World Trade Organization.' }
    ],
    expectedPrediction: 'A',
    choices: [
      {
        id: 'A',
        title: 'Authorize Total High-Seas Interdiction and Indiscriminate Naval Blockade',
        summary: 'Permits coalition warships to intercept, board, and redirect all commercial and sovereign vessels without flag-state notification.',
        correct: false,
        p5Votes: { usa: 'YES', gbr: 'YES', fra: 'YES', rus: 'VETO', chn: 'VETO' },
        e10Votes: 7,
        consequence: 'China and Russia announce immediate veto threats. Beijing denounces unrestricted maritime interdiction as a violation of UNCLOS freedom of navigation and commercial shipping routes.',
        mechanism: 'UNCLOS Sovereign Rights vs Coercive Interdiction',
        citation: 'UNCLOS Art. 87 & 110 / UN Charter Art. 27(3)',
        misconception: {
          tag: 'misc-majority',
          label: 'Maritime Coercion Assumption',
          remediation: 'Broad high-seas blockades without precise flag-state safeguards provoke P5 maritime vetoes, even when endorsed by Western naval powers.'
        }
      },
      {
        id: 'B',
        title: 'Eliminate Maritime Interdiction (Rely on Voluntary Self-Declarations)',
        summary: 'Omits any at-sea boarding verification mechanism, relying entirely on port-state manifest self-audits.',
        correct: false,
        p5Votes: { usa: 'VETO', gbr: 'VETO', fra: 'ABSTAIN', rus: 'YES', chn: 'YES' },
        e10Votes: 5,
        consequence: 'United Kingdom and United States threaten an immediate veto, stating that unenforceable maritime corridors allow unchecked shipments of heavy munitions.',
        mechanism: 'Verification Credibility Deficit',
        citation: 'UN Charter Chapter VII / Hurd (2007)',
        misconception: {
          tag: 'misc-threat-only',
          label: 'Passive Consensus Trap',
          remediation: 'Omitting verification mechanisms to avoid controversy destroys the credibility of the resolution, triggering vetoes from security guarantors.'
        }
      },
      {
        id: 'C',
        title: 'Targeted Flag-State Interdiction under UNCLOS Art. 110 with Innocent Passage Protected',
        summary: 'Restricts boardings to verified suspicious vessels with flag-state consultation under UNCLOS Art. 110, exempting all legitimate civilian commerce.',
        correct: true,
        p5Votes: { usa: 'YES', gbr: 'YES', fra: 'YES', rus: 'YES', chn: 'YES' },
        e10Votes: 9,
        consequence: 'Unanimous P5 concurrence achieved: UK and US secure lawful interdiction for verified illicit weapons shipments, while China and Russia concur after commercial freedom of navigation is codified.',
        mechanism: 'Functional Specialization & Treaty Harmonization (UNCLOS/UNSC)',
        citation: 'UNCLOS Art. 110 / UN Charter Art. 27(3)',
        misconception: null
      }
    ]
  },
  {
    id: 'clause-4',
    title: 'Operative Paragraph 4: Humanitarian Corridors & Sovereignty Safeguards',
    context: 'Hundreds of thousands of civilians are trapped in combat zones. The Council must establish humanitarian aid corridors while resolving fierce clashes over state sovereignty and border authorization.',
    predictionPrompt: 'What structural tension arises between French humanitarian imperatives and Russian sovereignty doctrines?',
    predictionOptions: [
      { key: 'A', text: 'Article 2(7) non-interference (Russia) vs Humanitarian protection imperative (France).' },
      { key: 'B', text: 'Disputes over currency exchange rates in multilateral relief tenders.' },
      { key: 'C', text: 'Territorial disputes over deep-sea mineral rights in the Atlantic.' }
    ],
    expectedPrediction: 'A',
    choices: [
      {
        id: 'A',
        title: 'Mandate Unilateral Cross-Border Aid Deliveries Without Host Consent',
        summary: 'Empowers international NGOs and military convoys to cross sovereign borders and distribute relief without host-state permission.',
        correct: false,
        p5Votes: { usa: 'YES', gbr: 'YES', fra: 'YES', rus: 'VETO', chn: 'VETO' },
        e10Votes: 8,
        consequence: 'Russian Federation declares an unconditional veto, condemning cross-border operations without host-state consent as a dangerous breach of Article 2(7) sovereign inviolability.',
        mechanism: 'Article 2(7) Domestic Sovereignty Defense',
        citation: 'UN Charter Art. 2(7) & Art. 27(3) / Krasner (1999)',
        misconception: {
          tag: 'misc-majority',
          label: 'Humanitarian Hegemony Fallacy',
          remediation: 'Moral urgency does not legally bypass Article 2(7) or Article 27(3) in the Security Council; sovereignty-defending P5 members routinely veto unilateral cross-border mandates.'
        }
      },
      {
        id: 'B',
        title: 'Subordinate All Aid Exclusively to Host Government Distribution Channels',
        summary: 'Prohibits any independent international aid delivery, granting host military authorities sole control over all supplies.',
        correct: false,
        p5Votes: { usa: 'VETO', gbr: 'VETO', fra: 'VETO', rus: 'YES', chn: 'YES' },
        e10Votes: 4,
        consequence: 'France and the UK threaten an immediate veto, warning that granting sole aid distribution to abusive host military forces facilitates the weaponization of starvation.',
        mechanism: 'Humanitarian Red Lines in Western Diplomacy',
        citation: 'Geneva Conventions Additional Protocol I / Hurd (2007)',
        misconception: {
          tag: 'misc-threat-only',
          label: 'Host Capitulation Fallacy',
          remediation: 'Handing monopolistic control of relief to combatants triggers decisive vetoes from Western permanent members.'
        }
      },
      {
        id: 'C',
        title: 'UN OCHA-Coordinated Humanitarian Corridors with 90-Day Mandate Review',
        summary: 'Establishes neutral UN OCHA-administered humanitarian corridors with host-government co-notification and mandatory 90-day Council mandate reviews.',
        correct: true,
        p5Votes: { usa: 'YES', gbr: 'YES', fra: 'YES', rus: 'ABSTAIN', chn: 'YES' },
        e10Votes: 9,
        consequence: 'Consensus finalized: France secures protected humanitarian corridors, Russia abstains without blocking after sunset review provisions are included, and China concurs.',
        mechanism: 'Iterated Mandate Review & Sovereignty Balancing',
        citation: 'UN Charter Art. 27(3) / Hurd (2007), After Anarchy',
        misconception: null
      }
    ]
  }
];

export const UNSC_MASTERY_QUESTIONS = [
  {
    id: 'mastery-1',
    prompt: 'Under UN Charter Article 27(3), what exact voting majority is legally required for a substantive Security Council resolution to pass?',
    options: [
      { key: 'A', text: 'A simple majority of 8 out of 15 members, provided no P5 member objects.' },
      { key: 'B', text: '9 affirmative votes out of 15, including the concurring (or abstaining) votes of all 5 permanent members.' },
      { key: 'C', text: '12 affirmative votes including a 2/3 majority of the UN General Assembly.' },
      { key: 'D', text: 'Unanimous consensus of all 15 Security Council members.' }
    ],
    correct: 'B',
    rationale: 'Article 27(3) explicitly mandates nine affirmative votes including the concurring votes of the Permanent Five (or voluntary abstentions), creating the institutional veto hurdle.',
    citation: 'UN Charter Article 27(3)'
  },
  {
    id: 'mastery-2',
    prompt: 'If a Permanent Member (P5) disagrees with a resolution but chooses to ABSTAIN rather than cast a negative vote, what is the legal outcome under established UN practice?',
    options: [
      { key: 'A', text: 'The abstention counts as a constructive veto and terminates the resolution immediately.' },
      { key: 'B', text: 'The resolution can still be adopted provided it receives at least 9 affirmative votes, because an abstention is not a negative vote under Art. 27(3).' },
      { key: 'C', text: 'The resolution is automatically deferred to the International Court of Justice for advisory review.' },
      { key: 'D', text: 'The member is sanctioned and loses its voting rights for subsequent sessions.' }
    ],
    correct: 'B',
    rationale: 'Since the 1950 Korean Crisis and ICJ jurisprudence (Namibia Advisory Opinion 1971), a P5 abstention does not prevent the adoption of a resolution that meets the 9-vote affirmative threshold.',
    citation: 'ICJ Namibia Advisory Opinion (1971) / UN Charter Art. 27(3)',
    misconception: {
      tag: 'misc-abstention',
      label: 'Abstention Equals Veto Fallacy',
      remediation: 'Abstention is a deliberate diplomatic tool allowing a P5 member to register dissent without killing an initiative that commands broad international support.'
    }
  },
  {
    id: 'mastery-3',
    prompt: 'Why does authorizing military enforcement under Chapter VII (Article 42) represent the most frequent flashpoint for P5 vetoes?',
    options: [
      { key: 'A', text: 'Chapter VII operations must be funded entirely out of the vetoing member\'s national defense budget.' },
      { key: 'B', text: 'Article 42 overrides domestic sovereignty and authorizes coercive violence without host-state consent, triggering deep geopolitical resistance from rival permanent powers.' },
      { key: 'C', text: 'The UN Charter prohibits any use of armed force under all circumstances.' },
      { key: 'D', text: 'Only the UN Secretary-General has the legal authority to introduce Chapter VII resolutions.' }
    ],
    correct: 'B',
    rationale: 'Article 42 authorizes the ultimate coercive mechanism in international law—overriding sovereign non-interference under Art. 2(7). Great powers routinely veto such mandates to prevent rivals from establishing coercive military precedents.',
    citation: 'UN Charter Chapter VII (Arts. 39, 41, 42) / Hurd (2007)'
  }
];

export const UNSC_TRANSFER_SCENARIO = {
  id: 'transfer-kosovo',
  title: '1999 Kosovo Crisis: The Humanitarian Intervention Impasse',
  context: 'In March 1999, escalating ethnic cleansing in Kosovo prompted Western powers to seek UN Security Council authorization for military action against the Federal Republic of Yugoslavia. However, the Russian Federation and China made it clear that any Chapter VII draft authorizing armed intervention without Yugoslav consent would be met with an immediate P5 veto.',
  prompt: 'Facing an inevitable Russian veto under Article 27(3), how does institutional veto theory explain the resulting diplomatic and military outcome?',
  options: [
    { key: 'A', text: 'The Security Council overruled the Russian veto using a 10-vote majority under Chapter VII Article 42.' },
    { key: 'B', text: 'Because Article 27(3) makes a P5 negative vote an absolute legal barrier, NATO bypassed the deadlocked Council entirely and intervened without UN authorization, sparking enduring debates over humanitarian legitimacy versus international legality.' },
    { key: 'C', text: 'The UN General Assembly suspended Russia and China from the Security Council to enable a unanimous vote.' },
    { key: 'D', text: 'The P5 members agreed to submit the Kosovo crisis to binding compulsory arbitration by the International Court of Justice.' }
  ],
  correct: 'B',
  rationale: 'The 1999 Kosovo crisis is the quintessential case of P5 veto deadlock leading to institutional bypass: NATO concluded that legal authorization under Art. 27(3) was impossible due to Russia\'s veto, choosing to launch Operation Allied Force outside the UN Charter framework.',
  citation: 'Independent International Commission on Kosovo (2000) / Hurd (2007), After Anarchy: Legitimacy & Power in the UN Security Council'
};

export class VetoState {
  constructor() {
    this.learningSession = new LearningSession('lab-05', UNSC_OBJECTIVES);
    this.reset();
  }

  reset() {
    this.tokensLeft = 5;
    this.attachedTokens = [];
    this.p5 = JSON.parse(JSON.stringify(P5_MEMBERS));
    this.tokens = JSON.parse(JSON.stringify(AMENDMENT_TOKENS));
    this.clauses = JSON.parse(JSON.stringify(UNSC_CLAUSES));
    this.currentClauseIndex = 0;
    this.selectedClauseChoices = [];
    this.phase = 'BRIEF'; // BRIEF, PREDICT, DECIDE, CONSEQUENCE, VOTE, MASTERY, TRANSFER, DEBRIEF
    this.voteResult = null;
    this.masteryIndex = 0;
    this.masteryAnswers = [];
    this.transferAnswer = null;
    this.lastFeedback = null;
    this.score = 0;
  }

  // Legacy method for test_gameplay_fixes.mjs backwards compatibility
  attachToken(tokenId, p5Id) {
    const token = this.tokens.find(t => t.id === tokenId);
    const member = this.p5.find(m => m.id === p5Id);
    if (!token || !member || this.tokensLeft <= 0) return false;

    if (token.targetP5 === p5Id) {
      member.demands[token.demandIdx].fulfilled = true;
    }
    member.satisfied = member.demands.some(d => d.fulfilled);

    this.tokensLeft--;
    this.attachedTokens.push({ token, member });
    return true;
  }

  // Legacy executeVote() for test_gameplay_fixes.mjs backwards compatibility
  executeVote() {
    this.phase = 'VOTING';
    const vetoingMembers = this.p5.filter(m => !m.satisfied);
    const p5Vetoed = vetoingMembers.length > 0;

    const e10Yes = Math.floor(Math.random() * 3 + 7);
    const p5Yes = 5 - vetoingMembers.length;
    const totalYes = p5Yes + e10Yes;
    const passed = !p5Vetoed && totalYes >= 9;

    this.voteResult = {
      passed,
      p5Vetoed,
      vetoingMembers,
      totalYes,
      e10Yes,
      p5Yes
    };
    return this.voteResult;
  }

  getStars() {
    // If running full learning session
    if (this.phase === 'DEBRIEF' && this.learningSession) {
      return this.learningSession.getStars();
    }
    // Fallback to legacy voteResult scoring
    if (!this.voteResult || !this.voteResult.passed) return 0;
    if (this.voteResult.totalYes >= 13) return 3;
    if (this.voteResult.totalYes >= 11) return 2;
    return 1;
  }

  // 7-Phase Learning Loop methods
  getCurrentClause() {
    return this.clauses[this.currentClauseIndex] || null;
  }

  recordPrediction(predictedChoiceKey) {
    const clause = this.getCurrentClause();
    if (!clause) return;
    this.learningSession.recordPrediction(clause.id, predictedChoiceKey);
    this.phase = 'DECIDE';
  }

  executeClauseDecision(choiceId) {
    const clause = this.getCurrentClause();
    if (!clause) return null;

    const choice = clause.choices.find(c => c.id === choiceId);
    if (!choice) return null;

    const predicted = this.learningSession._predictions.get(clause.id);
    const predictionMatch = (predicted === clause.expectedPrediction);

    // Update P5 states based on votes
    Object.entries(choice.p5Votes).forEach(([p5Id, vote]) => {
      const member = this.p5.find(m => m.id === p5Id);
      if (member) {
        member.currentVote = vote;
        member.satisfied = (vote === 'YES' || vote === 'ABSTAIN');
      }
    });

    const isCorrect = choice.correct;
    if (isCorrect) {
      this.score += 25;
    }

    const payload = {
      outcome: isCorrect ? 'success' : 'failure',
      consequence: choice.consequence,
      mechanism: choice.mechanism,
      citation: choice.citation,
      misconception: isCorrect ? null : choice.misconception,
      predictionMatch
    };

    this.learningSession.recordDecision({
      decisionId: clause.id,
      choice: choice.id,
      correctChoice: 'C',
      rationale: choice.consequence,
      misconception: payload.misconception,
      predicted,
      actual: clause.expectedPrediction,
      outcome: payload.outcome,
      consequence: payload.consequence,
      mechanism: payload.mechanism,
      citation: payload.citation,
      objectiveIndex: Math.min(this.currentClauseIndex, UNSC_OBJECTIVES.length - 1)
    });

    this.selectedClauseChoices.push({
      clauseId: clause.id,
      choice
    });

    this.lastFeedback = payload;
    this.phase = 'CONSEQUENCE';
    return { choice, isCorrect, payload };
  }

  advanceClause() {
    this.currentClauseIndex++;
    if (this.currentClauseIndex < this.clauses.length) {
      this.phase = 'PREDICT';
      return true;
    }
    this.phase = 'VOTE';
    return false;
  }

  executeFinalVote() {
    this.phase = 'VOTING';
    const hasVetoClause = this.selectedClauseChoices.some(sc => !sc.choice.correct);

    const p5Vetoing = [];
    const p5YesMembers = [];
    const p5Abstaining = [];

    this.p5.forEach(m => {
      // Determine final vote from selected clauses
      const negativeVotes = this.selectedClauseChoices.filter(sc => sc.choice.p5Votes[m.id] === 'VETO');
      if (negativeVotes.length > 0) {
        p5Vetoing.push(m);
        m.finalVote = 'VETO';
      } else {
        const abstains = this.selectedClauseChoices.filter(sc => sc.choice.p5Votes[m.id] === 'ABSTAIN');
        if (abstains.length > 0) {
          p5Abstaining.push(m);
          m.finalVote = 'ABSTAIN';
        } else {
          p5YesMembers.push(m);
          m.finalVote = 'YES';
        }
      }
    });

    const p5Vetoed = p5Vetoing.length > 0;
    const e10Yes = hasVetoClause ? 6 : 9;
    const p5Yes = p5YesMembers.length;
    const totalYes = p5Yes + e10Yes;
    const passed = !p5Vetoed && totalYes >= 9;

    this.voteResult = {
      passed,
      p5Vetoed,
      vetoingMembers: p5Vetoing,
      abstainingMembers: p5Abstaining,
      yesMembers: p5YesMembers,
      totalYes,
      e10Yes,
      p5Yes
    };

    return this.voteResult;
  }

  getCurrentMasteryQuestion() {
    return UNSC_MASTERY_QUESTIONS[this.masteryIndex] || null;
  }

  answerMasteryQuestion(chosenKey) {
    const q = this.getCurrentMasteryQuestion();
    if (!q) return null;

    const isCorrect = (chosenKey === q.correct);
    this.learningSession.recordMasteryCheck({
      questionId: q.id,
      chosen: chosenKey,
      correct: q.correct,
      misconceptionTag: isCorrect ? null : (q.misconception ? q.misconception.tag : 'misc-unsc')
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
    if (this.masteryIndex >= UNSC_MASTERY_QUESTIONS.length) {
      this.phase = 'TRANSFER';
    }

    return { isCorrect, rationale: q.rationale, citation: q.citation, misconception: q.misconception };
  }

  answerTransfer(chosenKey) {
    const isCorrect = (chosenKey === UNSC_TRANSFER_SCENARIO.correct);
    this.learningSession.recordTransfer({
      scenarioId: UNSC_TRANSFER_SCENARIO.id,
      choice: chosenKey,
      correct: UNSC_TRANSFER_SCENARIO.correct
    });

    this.transferAnswer = {
      chosen: chosenKey,
      isCorrect,
      rationale: UNSC_TRANSFER_SCENARIO.rationale,
      citation: UNSC_TRANSFER_SCENARIO.citation
    };

    this.phase = 'DEBRIEF';
    return {
      isCorrect,
      rationale: UNSC_TRANSFER_SCENARIO.rationale,
      citation: UNSC_TRANSFER_SCENARIO.citation
    };
  }

  getReport() {
    return this.learningSession.getReport();
  }
}
