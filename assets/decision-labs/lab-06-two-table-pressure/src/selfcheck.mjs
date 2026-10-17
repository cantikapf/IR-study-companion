import assert from 'node:assert/strict';
import {
  PUTNAM_CONFIG,
  PUTNAM_OBJECTIVES,
  PUTNAM_MISCONCEPTIONS,
  PUTNAM_ROUNDS,
  PUTNAM_MASTERY_CHECKS,
  PUTNAM_TRANSFER,
  PutnamState
} from './PutnamConfig.js';
import { LearningSession } from '../../shared/learn/LearningSession.js';
import { DebriefPanel } from '../../shared/learn/DebriefPanel.js';

console.log('--- LAB-06 SELF-CHECK SUITE ---');

// 1. Assert Naive Strategy Fails
const naiveState = new PutnamState();
// Naive play: blind unilateral concessions (choice 0)
for (let r = 0; r < PUTNAM_ROUNDS.length; r++) {
  naiveState.round = r + 1;
  const choice = PUTNAM_ROUNDS[r].choices[0]; // naive choice
  naiveState.applyPolicyChoice(choice);
}

assert.equal(naiveState.involuntaryDefection, true, 'Naive strategy must trigger involuntary defection');
assert.equal(naiveState.getStars(), 0, 'Naive strategy must receive 0 stars');
console.log('PASS Gate 1: Naive dominant strategy fails with 0 stars and involuntary defection.');

// 2. Assert Reasoned Strategy Wins 3 Stars
const reasonedState = new PutnamState();
for (let r = 0; r < PUTNAM_ROUNDS.length; r++) {
  reasonedState.round = r + 1;
  const choice = PUTNAM_ROUNDS[r].choices[2]; // balanced & tied-hands gambit
  reasonedState.applyPolicyChoice(choice);
}

assert.equal(reasonedState.involuntaryDefection, false, 'Reasoned strategy must avoid involuntary defection');
assert.ok(reasonedState.winSetOverlap >= 70, `Win-set overlap must be >= 70% (got ${reasonedState.winSetOverlap})`);
assert.ok(reasonedState.table1Progress >= 65, 'Level I progress must clear threshold');
assert.ok(reasonedState.table2Progress >= 65, 'Level II progress must clear threshold');
assert.equal(reasonedState.getStars(), 3, 'Reasoned strategy must achieve 3 stars');
assert.equal(reasonedState.getOutcome().rank, 'BILATERAL MASTER');
console.log('PASS Gate 2: Reasoned strategy achieves 3 stars (Bilateral Master).');

// 3. LearningSession Mastery, Predictions, Misconceptions
const session = new LearningSession('lab-06', PUTNAM_OBJECTIVES);
assert.equal(session.masteryScore, 0);

// Round 1: Predict & Decide (Flawed decision logs misconception)
session.recordPrediction('round-1', 'intl_surge');
const d1 = session.recordDecision({
  decisionId: 'round-1',
  choice: 'unilateral_cuts',
  correctChoice: 'reciprocal_phasing',
  rationale: 'Deep tariff cuts caused domestic revolt.',
  misconceptionTag: PUTNAM_MISCONCEPTIONS.DOMESTIC_MINIMISED,
  predicted: 'intl_surge',
  actual: 'intl_surge',
  outcome: 'partial',
  consequence: 'Geneva welcomed cuts, domestic industry revolted.',
  mechanism: 'Agreements without domestic support produce defection.',
  citation: 'Putnam (1988), Two-Level Games',
  objectiveIndex: 0
});

assert.equal(d1.isCorrect, false);
assert.equal(d1.matched, true);
assert.equal(session.misconceptions.length, 1);
assert.equal(session.misconceptions[0].tag, 'domestic-minimised');
assert.equal(session.misconceptions[0].hits, 1);

// Mastery Check 1 (Repeat error increments hits)
session.recordMasteryCheck({
  questionId: 'putnam-mc-01',
  chosen: 'a',
  correct: 'b',
  misconceptionTag: PUTNAM_MISCONCEPTIONS.DOMESTIC_MINIMISED,
  objectiveIndex: 0
});
assert.equal(session.misconceptions[0].hits, 2);

// Mastery Check 1 Corrected (credits objective index 0)
session.recordMasteryCheck({
  questionId: 'putnam-mc-01-retry',
  chosen: 'b',
  correct: 'b',
  objectiveIndex: 0
});
assert.ok(session.masteryScore > 0);

// Mastery Check 2 & 3
session.recordMasteryCheck({
  questionId: 'putnam-mc-02',
  chosen: 'b',
  correct: 'b',
  objectiveIndex: 2
});

session.recordMasteryCheck({
  questionId: 'putnam-mc-03',
  chosen: 'a',
  correct: 'a',
  objectiveIndex: 1
});

// Transfer Scenario
session.recordTransfer({
  scenarioId: PUTNAM_TRANSFER.scenarioId,
  choice: 'opt_b',
  correct: 'opt_b',
  objectiveIndex: 0
});

assert.equal(session.masteryScore, 100);
assert.equal(session.stars, 3);
assert.equal(session.getStars(), 3);
console.log('PASS Gate 3: Mastery scoring and misconception remediation verified.');

// 4. Debrief Report & Curriculum Chapter Bindings
const report = session.getReport();
assert.equal(report.labId, 'lab-06');
assert.equal(report.masteryScore, 100);
assert.equal(report.stars, 3);
assert.equal(report.chapters.length, 2);
assert.equal(report.chapters[0].slug, 'level-of-analysis-fpdm');
assert.equal(report.chapters[1].slug, 'factors-fpdm');

const debriefHtml = new DebriefPanel().getHtml(report);
assert.ok(debriefHtml.includes('DECISION LAB DEBRIEF · LAB-06'));
assert.ok(debriefHtml.includes('level-of-analysis-fpdm'));
assert.ok(debriefHtml.includes('factors-fpdm'));
assert.ok(debriefHtml.includes('domestic-minimised'));
console.log('PASS Gate 4: Debrief panel and chapter bindings verified.');

console.log('ALL LAB-06 SELF-CHECKS PASSED.');
