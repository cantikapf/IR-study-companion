import assert from 'node:assert/strict';
import {
  SCS_CONFIG,
  SCS_OBJECTIVES,
  SCS_MISCONCEPTIONS,
  SCS_ROUNDS,
  SCS_MASTERY_CHECKS,
  SCS_TRANSFER,
  ScsState
} from './ScsConfig.js';
import { LearningSession } from '../../shared/learn/LearningSession.js';
import { DebriefPanel } from '../../shared/learn/DebriefPanel.js';

console.log('--- LAB-09 SELF-CHECK SUITE ---');

// 1. Assert Naive Strategy Triggers Immediate Collapse
const naiveState = new PutnamLikeScsState();
function PutnamLikeScsState() {
  return new ScsState();
}

// Player picks Choice 0 (naive maximal legalistic arbitration push)
naiveState.round = 1;
naiveState.applyChoice(SCS_ROUNDS[0].choices[0]);

assert.equal(naiveState.isCollapsed(), true, 'Choice 0 in Round 1 must drop China below 25% collapse threshold');
assert.ok(naiveState.factions.china < 25, `China sentiment must be < 25 (got ${naiveState.factions.china})`);
assert.equal(naiveState.getStars(), 0, 'Collapsed summit must receive 0 stars');
assert.equal(naiveState.getOutcome().rank, 'COMMUNIQUÉ COLLAPSE');
console.log('PASS Gate 1A: Naive aggressive strategy triggers instant Chinese walkout and 0-star collapse.');

// Player picks Choice 1 in Round 1 (naive complete capitulation)
const capitulateState = new ScsState();
capitulateState.round = 1;
capitulateState.applyChoice(SCS_ROUNDS[0].choices[1]);
assert.equal(capitulateState.isCollapsed(), true, 'Choice 1 in Round 1 must drop Claimants below 25% collapse threshold');
assert.ok(capitulateState.factions.claimants < 25, `Claimant sentiment must be < 25 (got ${capitulateState.factions.claimants})`);
assert.equal(capitulateState.getStars(), 0, 'Capitulation must receive 0 stars');
console.log('PASS Gate 1B: Naive capitulation triggers instant Claimant walkout and 0-star collapse.');

// 2. Assert Reasoned Consensus Strategy Achieves 3 Stars
const reasonedState = new ScsState();
for (let r = 0; r < SCS_ROUNDS.length; r++) {
  reasonedState.round = r + 1;
  const choice = SCS_ROUNDS[r].choices[2]; // Consensus-building option
  reasonedState.applyChoice(choice);
}

assert.equal(reasonedState.isCollapsed(), false, 'Reasoned strategy must prevent collapse');
assert.ok(reasonedState.agreementValue >= 65, `Agreement value must be >= 65% (got ${reasonedState.agreementValue})`);
const minFaction = Math.min(...Object.values(reasonedState.factions));
assert.ok(minFaction >= 40, `All factions must be >= 40% (min got ${minFaction})`);
assert.equal(reasonedState.getStars(), 3, 'Reasoned consensus strategy must earn 3 stars');
assert.equal(reasonedState.getOutcome().rank, "CHAIR'S MASTERPIECE");
console.log("PASS Gate 2: Reasoned strategy achieves 3 stars (Chair's Masterpiece).");

// 3. LearningSession Mastery, Predictions, Misconceptions
const session = new LearningSession('lab-09', SCS_OBJECTIVES);
assert.equal(session.masteryScore, 0);

session.recordPrediction('round-1', 'legal_push');
const d1 = session.recordDecision({
  decisionId: 'round-1',
  choice: 'explicit_archipelagos',
  correctChoice: 'unclos_demilitarized',
  rationale: 'Legalistic naming triggered Chinese protest.',
  misconceptionTag: SCS_MISCONCEPTIONS.BINDING_ALWAYS_BETTER,
  predicted: 'legal_push',
  actual: 'legal_push',
  outcome: 'partial',
  consequence: 'Claimants cheered, China threatened walkout.',
  mechanism: 'Territorial naming violates ASEAN informal consensus norms.',
  citation: 'Acharya (2001), Constructing a Security Community in Southeast Asia',
  objectiveIndex: 1
});

assert.equal(d1.isCorrect, false);
assert.equal(d1.matched, true);
assert.equal(session.misconceptions.length, 1);
assert.equal(session.misconceptions[0].tag, 'binding-always-better');
assert.equal(session.misconceptions[0].hits, 1);

// Mastery Check 1 (wrong answer increments hits)
session.recordMasteryCheck({
  questionId: 'scs-mc-02',
  chosen: 'a',
  correct: 'b',
  misconceptionTag: SCS_MISCONCEPTIONS.BINDING_ALWAYS_BETTER,
  objectiveIndex: 1
});
assert.equal(session.misconceptions[0].hits, 2);

// Mastery Check 1 Corrected
session.recordMasteryCheck({
  questionId: 'scs-mc-02-retry',
  chosen: 'b',
  correct: 'b',
  objectiveIndex: 1
});
assert.ok(session.masteryScore > 0);

// Mastery Check 2 & 3
session.recordMasteryCheck({
  questionId: 'scs-mc-01',
  chosen: 'b',
  correct: 'b',
  objectiveIndex: 0
});

session.recordMasteryCheck({
  questionId: 'scs-mc-03',
  chosen: 'b',
  correct: 'b',
  objectiveIndex: 2
});

// Transfer Scenario (Phnom Penh 2012)
session.recordTransfer({
  scenarioId: SCS_TRANSFER.scenarioId,
  choice: 'opt_b',
  correct: 'opt_b',
  objectiveIndex: 0
});

assert.equal(session.masteryScore, 100);
assert.equal(session.stars, 3);
assert.equal(session.getStars(), 3);
console.log('PASS Gate 3: Mastery scoring and misconception aggregation verified.');

// 4. Debrief Report & Curriculum Chapter Bindings
const report = session.getReport();
assert.equal(report.labId, 'lab-09');
assert.equal(report.masteryScore, 100);
assert.equal(report.stars, 3);
assert.equal(report.chapters.length, 2);
assert.equal(report.chapters[0].slug, 'asean-chapter');
assert.equal(report.chapters[1].slug, 'asean-community');

const debriefHtml = new DebriefPanel().getHtml(report);
assert.ok(debriefHtml.includes('DECISION LAB DEBRIEF · LAB-09'));
assert.ok(debriefHtml.includes('asean-chapter'));
assert.ok(debriefHtml.includes('asean-community'));
assert.ok(debriefHtml.includes('binding-always-better'));
console.log('PASS Gate 4: Debrief panel and chapter bindings verified.');

console.log('ALL LAB-09 SELF-CHECKS PASSED.');
