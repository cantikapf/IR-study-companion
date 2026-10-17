import assert from 'node:assert/strict';
import {
  UNCLOS_OBJECTIVES,
  UNCLOS_INCIDENTS,
  UNCLOS_MASTERY_QUESTIONS,
  UNCLOS_TRANSFER_SCENARIO,
  UnclosState
} from './UnclosConfig.js';

console.log('[Lab-07 Selfcheck] Beginning verification...');

// 1. Incident Count & Structure
assert.equal(UNCLOS_INCIDENTS.length, 10, 'Must have exactly 10 incidents');
console.log('-> Assertion passed: exactly 10 incidents defined.');

// 2. Enforcement Verbs Distribution (no YES bias, >=2 of each verb)
const verbCounts = {
  SEIZE_ARREST: 0,
  BOARD_VERIFY: 0,
  PERMIT_TRANSIT: 0
};

UNCLOS_INCIDENTS.forEach((inc, idx) => {
  assert.ok(inc.correctAction in verbCounts, `Incident ${idx + 1} has invalid action ${inc.correctAction}`);
  verbCounts[inc.correctAction]++;
});

console.log('-> Enforcement Verbs Distribution:', verbCounts);
assert.ok(verbCounts.SEIZE_ARREST >= 2, 'SEIZE_ARREST must appear at least twice');
assert.ok(verbCounts.BOARD_VERIFY >= 2, 'BOARD_VERIFY must appear at least twice');
assert.ok(verbCounts.PERMIT_TRANSIT >= 2, 'PERMIT_TRANSIT must appear at least twice');

// Assert balanced distribution: no single verb exceeds 50%
Object.entries(verbCounts).forEach(([verb, count]) => {
  assert.ok(count <= 5, `Verb ${verb} has count ${count}, which exceeds 50% response bias ceiling`);
});
console.log('-> Assertion passed: balanced verb distribution, no response bias.');

// 3. Mandatory UNCLOS Articles coverage: 8, 17, 33, 56, 77, 110
const citations = UNCLOS_INCIDENTS.map(i => i.citation).join(' ');
const mandatoryArticles = ['Article 8', 'Article 17', 'Article 33', 'Article 56', 'Article 77', 'Article 110'];
mandatoryArticles.forEach(art => {
  assert.ok(citations.includes(art), `Mandatory citation ${art} missing from incidents`);
});
console.log('-> Assertion passed: mandatory UNCLOS Articles (8, 17, 33, 56, 77, 110) fully covered.');

// 4. Misconceptions Mappings
UNCLOS_INCIDENTS.forEach((inc, idx) => {
  assert.ok(inc.misconceptions, `Incident ${idx + 1} must define misconceptions`);
  assert.ok(inc.predictionOptions.length >= 2, `Incident ${idx + 1} must have prediction options`);
  assert.ok(inc.expectedPrediction, `Incident ${idx + 1} must have expected prediction`);
});
console.log('-> Assertion passed: prediction prompts and misconceptions defined for all incidents.');

// 5. Mastery Check (3 items) & Transfer Scenario
assert.equal(UNCLOS_MASTERY_QUESTIONS.length, 3, 'Must have exactly 3 mastery check questions');
assert.ok(UNCLOS_TRANSFER_SCENARIO.title.includes('South China Sea'), 'Transfer scenario must cover South China Sea 2016');
console.log('-> Assertion passed: mastery check (3 items) and transfer scenario verified.');

// 6. Complete Learning Loop Simulation (Ideal Run -> 3 Stars)
const state = new UnclosState();
assert.equal(state.phase, 'BRIEF');

for (let i = 0; i < UNCLOS_INCIDENTS.length; i++) {
  const inc = state.getCurrentIncident();
  assert.ok(inc, `Incident ${i} should be active`);

  // PREDICT phase
  state.recordPrediction(inc.expectedPrediction);
  assert.equal(state.phase, 'DECIDE');

  // DECIDE & CONSEQUENCE phase
  const outcome = state.executeDecision(inc.correctAction);
  assert.equal(outcome.isCorrect, true);
  assert.equal(outcome.payload.outcome, 'success');
  assert.equal(outcome.payload.predictionMatch, true);
  assert.ok(outcome.payload.citation);
  assert.ok(outcome.payload.mechanism);
  assert.equal(state.phase, 'CONSEQUENCE');

  state.advanceIncident();
}

assert.equal(state.phase, 'MASTERY');
for (let i = 0; i < UNCLOS_MASTERY_QUESTIONS.length; i++) {
  const q = state.getCurrentMasteryQuestion();
  const res = state.answerMasteryQuestion(q.correct);
  assert.equal(res.isCorrect, true);
}

assert.equal(state.phase, 'TRANSFER');
const trans = state.answerTransfer(UNCLOS_TRANSFER_SCENARIO.correct);
assert.equal(trans.isCorrect, true);
assert.equal(state.phase, 'DEBRIEF');

const report = state.getReport();
assert.equal(report.masteryScore, 100);
assert.equal(report.stars, 3);
assert.equal(report.decisions.length, 10);
assert.ok(report.chapters.length >= 2);
console.log('-> Assertion passed: ideal playthrough achieves 100% mastery, 3 stars, and full debrief payload.');

// 7. Misconception Capture Verification (Flawed Run)
const flawedState = new UnclosState();
const flawedInc = flawedState.getCurrentIncident();
flawedState.recordPrediction('A'); // Wrong hypothesis
// Wrong action
const wrongAction = flawedInc.correctAction === 'SEIZE_ARREST' ? 'PERMIT_TRANSIT' : 'SEIZE_ARREST';
const flawedRes = flawedState.executeDecision(wrongAction);
assert.equal(flawedRes.isCorrect, false);
assert.equal(flawedRes.payload.outcome, 'failure');
assert.ok(flawedRes.payload.misconception, 'Misconception must be populated on flawed answer');
const flawedReport = flawedState.getReport();
assert.ok(flawedReport.misconceptions.length > 0, 'Misconceptions must be aggregated in report');
console.log('-> Assertion passed: erroneous decisions capture misconceptions and populate remediation.');

console.log('[Lab-07 Selfcheck] All assertions passed successfully!');
