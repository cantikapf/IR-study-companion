import assert from 'node:assert/strict';
import {
  BOP_OBJECTIVES,
  BOP_CRISES,
  BOP_MASTERY_QUESTIONS,
  BOP_TRANSFER_SCENARIO,
  BopState
} from './BopConfig.js';

console.log('[Lab-08 Selfcheck] Beginning verification...');

// 1. Objectives & Crises Structure
assert.equal(BOP_OBJECTIVES.length, 3, 'Must have 3 learning objectives');
assert.ok(BOP_CRISES.length >= 4, 'Must have at least 4 crises');
console.log(`-> Assertion passed: ${BOP_CRISES.length} crises defined with 3 learning objectives.`);

// 2. Misconceptions & Options Verification
BOP_CRISES.forEach((c, idx) => {
  assert.equal(c.choices.length, 3, `Crisis ${idx + 1} must have 3 choices (COMMIT, WITHHOLD, MEDIATE)`);
  assert.ok(c.predictionOptions.length >= 2, `Crisis ${idx + 1} must have prediction options`);
  assert.ok(c.expectedPrediction, `Crisis ${idx + 1} must have expected prediction`);
  c.choices.forEach(ch => {
    assert.ok(ch.consequence, `Choice ${ch.action} must have consequence`);
    assert.ok(ch.mechanism, `Choice ${ch.action} must name IR mechanism`);
    assert.ok(ch.citation, `Choice ${ch.action} must provide academic citation`);
  });
});
console.log('-> Assertion passed: all crises have full consequence, mechanism, and citation definitions.');

// 3. Naive Strategy 1: Blind Unconditional Commitment (All COMMIT)
// Asserts that naive aggressive commitment fails due to chain-ganging collapse
const naiveCommitState = new BopState();
for (let i = 0; i < BOP_CRISES.length; i++) {
  if (naiveCommitState.collapse) break;
  naiveCommitState.recordPrediction('A');
  naiveCommitState.executeDecision('COMMIT');
  naiveCommitState.advanceCrisis();
}
assert.equal(naiveCommitState.collapse, true, 'Naive commitment strategy must trigger systemic collapse');
assert.equal(naiveCommitState.getStars(), 0, 'Collapsed run must earn 0 stars');
assert.ok(naiveCommitState.chainGangingCount >= 2, 'Must record chain-ganging events');
console.log('-> Assertion passed: Naive COMMIT strategy collapses system through chain-ganging (0 stars).');

// 4. Naive Strategy 2: Blind Buck-Passing (All WITHHOLD)
// Asserts that naive buck-passing fails to preserve balance
const naiveBuckState = new BopState();
for (let i = 0; i < BOP_CRISES.length; i++) {
  if (naiveBuckState.collapse) break;
  naiveBuckState.recordPrediction('C');
  naiveBuckState.executeDecision('WITHHOLD');
  naiveBuckState.advanceCrisis();
}
assert.ok(naiveBuckState.getStars() < 3, 'Naive buck-passing strategy must not win 3 stars');
console.log('-> Assertion passed: Naive WITHHOLD strategy fails to achieve 3 stars.');

// 5. Reasoned Strategy: Disciplined Balancing & Strategic Restraint
// Asserts that thoughtful policy choices navigate the crises, preserve equilibrium, and achieve 3 stars
const reasonedState = new BopState();
assert.equal(reasonedState.phase, 'BRIEF');

const reasonedMoves = [
  { pred: 'B', act: 'MEDIATE' },
  { pred: 'A', act: 'MEDIATE' },
  { pred: 'B', act: 'MEDIATE' },
  { pred: 'A', act: 'COMMIT' },
  { pred: 'A', act: 'MEDIATE' }
];

for (let i = 0; i < BOP_CRISES.length; i++) {
  const move = reasonedMoves[i];
  reasonedState.recordPrediction(move.pred);
  const res = reasonedState.executeDecision(move.act);
  assert.equal(res.isCorrect, true, `Move ${i + 1} should be successful under reasoned strategy`);
  assert.equal(res.collapse, false, `System must not collapse on reasoned move ${i + 1}`);
  reasonedState.advanceCrisis();
}

assert.equal(reasonedState.phase, 'MASTERY');
for (let i = 0; i < BOP_MASTERY_QUESTIONS.length; i++) {
  const q = reasonedState.getCurrentMasteryQuestion();
  const res = reasonedState.answerMasteryQuestion(q.correct);
  assert.equal(res.isCorrect, true);
}

assert.equal(reasonedState.phase, 'TRANSFER');
const transRes = reasonedState.answerTransfer(BOP_TRANSFER_SCENARIO.correct);
assert.equal(transRes.isCorrect, true);
assert.equal(reasonedState.phase, 'DEBRIEF');

const report = reasonedState.getReport();
assert.equal(report.masteryScore, 100);
assert.equal(report.stars, 3);
assert.ok(report.chapters.length >= 2);
console.log('-> Assertion passed: reasoned strategy preserves equilibrium, earning 100% mastery and 3 stars.');

// 6. Misconception Capture Verification
const flawedState = new BopState();
flawedState.recordPrediction('A');
const flawedRes = flawedState.executeDecision('COMMIT');
assert.ok(flawedRes.payload.misconception, 'Flawed decision must capture misconception');
assert.equal(flawedRes.payload.misconception.tag, 'misc_alliances_deter');
const flawedReport = flawedState.getReport();
assert.ok(flawedReport.misconceptions.some(m => m.tag === 'misc_alliances_deter'));
console.log('-> Assertion passed: misconceptions are captured and aggregated in debrief report.');

console.log('[Lab-08 Selfcheck] All assertions passed successfully!');
