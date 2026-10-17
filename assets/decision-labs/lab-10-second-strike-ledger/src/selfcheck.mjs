import assert from 'node:assert/strict';
import {
  NUCLEAR_OBJECTIVES,
  NUCLEAR_SCENARIOS,
  NUCLEAR_MASTERY_QUESTIONS,
  NUCLEAR_TRANSFER_SCENARIO,
  NuclearState
} from './NuclearConfig.js';

console.log('[Lab-10 Selfcheck] Beginning verification...');

// 1. Objectives & Scenarios Structure
assert.equal(NUCLEAR_OBJECTIVES.length, 3, 'Must have exactly 3 learning objectives');
assert.equal(NUCLEAR_SCENARIOS.length, 4, 'Must have exactly 4 fiscal year scenarios');
console.log('-> Assertion passed: 3 learning objectives and 4 fiscal year scenarios defined.');

// 2. Scenario Details & Prediction Prompts
NUCLEAR_SCENARIOS.forEach((sc, idx) => {
  assert.ok(sc.stressLeg, `FY ${idx + 1} must define stressLeg`);
  assert.ok(sc.theory, `FY ${idx + 1} must include theoretical rationale`);
  assert.ok(sc.predictionPrompt, `FY ${idx + 1} must include prediction prompt`);
  assert.ok(sc.predictionOptions.length >= 2, `FY ${idx + 1} must have prediction options`);
  assert.ok(sc.expectedPrediction, `FY ${idx + 1} must have expected prediction`);
});
console.log('-> Assertion passed: all scenarios contain stressLeg, theory, and prediction prompts.');

// 3. Mandatory Citations Verification
const allCitations = [
  ...NUCLEAR_MASTERY_QUESTIONS.map(q => q.citation),
  NUCLEAR_TRANSFER_SCENARIO.citation
].join(' ');
assert.ok(allCitations.includes('Schelling'), 'Must cite Thomas Schelling');
assert.ok(allCitations.includes('Jervis'), 'Must cite Robert Jervis');
console.log('-> Assertion passed: mandatory citations (Schelling 1960 / Jervis 1989) verified.');

// 4. Non-Triviality Check 1: Default Allocation (Zero Player Input) Must Fail
const defaultState = new NuclearState();
for (let y = 1; y <= 4; y++) {
  const sim = defaultState.simulateYearEnd();
  assert.equal(sim.crisis, true, `Default allocation must trigger crisis in FY ${y}`);
  if (y < 4) defaultState.advanceYear();
}
assert.equal(defaultState.stability, 0, 'Default path must reduce stability to 0%');
assert.equal(defaultState.getStars(), 0, 'Default zero-input path must yield 0 stars');
console.log('-> Assertion passed: Default no-input allocation collapses deterrence (0 stars).');

// 5. Non-Triviality Check 2: Schelling ABM Defense Dilemma (> $25B Defense Destabilizes)
const abmTestState = new NuclearState();
abmTestState.setAllocation('defense', 30); // Excessive defense spending
abmTestState.setAllocation('icbm', 25);
abmTestState.setAllocation('slbm', 35);
abmTestState.setAllocation('bomber', 10);
const abmSim = abmTestState.simulateYearEnd();
assert.equal(abmSim.crisis, true, 'Heavy defense >25 must trigger crisis');
assert.equal(abmSim.abmDestabilized, true, 'abmDestabilized flag must be true');
assert.ok(abmSim.payload.misconception, 'Must attach misconception payload');
assert.equal(abmSim.payload.misconception.tag, 'misc-defense-always-good');
console.log('-> Assertion passed: Schelling ABM defense dilemma triggers preemption panic and logs misconception.');

// 6. Complete 7-Phase Learning Loop Simulation (Reasoned Strategy -> 3 Stars)
const reasonedState = new NuclearState();
assert.equal(reasonedState.phase, 'BRIEF');
reasonedState.phase = 'PREDICT';

// FY 1: Stressed ICBM (30)
reasonedState.recordPrediction('A');
assert.equal(reasonedState.phase, 'DECIDE');
reasonedState.setAllocation('icbm', 30);
reasonedState.setAllocation('slbm', 35);
reasonedState.setAllocation('bomber', 20);
reasonedState.setAllocation('defense', 15);
assert.equal(reasonedState.getTotalBudget(), 100);
const sim1 = reasonedState.simulateYearEnd();
assert.equal(sim1.crisis, false);
assert.equal(sim1.payload.outcome, 'success');
assert.equal(sim1.payload.predictionMatch, true);
assert.equal(reasonedState.stability, 85);
assert.equal(reasonedState.phase, 'CONSEQUENCE');
reasonedState.advanceYear();

// FY 2: Stressed SLBM (40)
assert.equal(reasonedState.phase, 'PREDICT');
reasonedState.recordPrediction('A');
reasonedState.setAllocation('icbm', 25);
reasonedState.setAllocation('slbm', 40);
reasonedState.setAllocation('bomber', 20);
reasonedState.setAllocation('defense', 15);
assert.equal(reasonedState.getTotalBudget(), 100);
const sim2 = reasonedState.simulateYearEnd();
assert.equal(sim2.crisis, false);
assert.equal(reasonedState.stability, 95);
reasonedState.advanceYear();

// FY 3: Stressed Bomber (25)
assert.equal(reasonedState.phase, 'PREDICT');
reasonedState.recordPrediction('A');
reasonedState.setAllocation('icbm', 25);
reasonedState.setAllocation('slbm', 35);
reasonedState.setAllocation('bomber', 25);
reasonedState.setAllocation('defense', 15);
assert.equal(reasonedState.getTotalBudget(), 100);
const sim3 = reasonedState.simulateYearEnd();
assert.equal(sim3.crisis, false);
assert.equal(reasonedState.stability, 100);
reasonedState.advanceYear();

// FY 4: Stressed Defense (25, safe ceiling <= 25)
assert.equal(reasonedState.phase, 'PREDICT');
reasonedState.recordPrediction('A');
reasonedState.setAllocation('icbm', 25);
reasonedState.setAllocation('slbm', 35);
reasonedState.setAllocation('bomber', 15);
reasonedState.setAllocation('defense', 25);
assert.equal(reasonedState.getTotalBudget(), 100);
const sim4 = reasonedState.simulateYearEnd();
assert.equal(sim4.crisis, false);
assert.equal(reasonedState.stability, 100);
const hasNext = reasonedState.advanceYear();
assert.equal(hasNext, false, 'FY 4 is the final fiscal year');

// Mastery Check Phase
assert.equal(reasonedState.phase, 'MASTERY');
for (let i = 0; i < NUCLEAR_MASTERY_QUESTIONS.length; i++) {
  const q = reasonedState.getCurrentMasteryQuestion();
  assert.ok(q, `Mastery question ${i + 1} must exist`);
  const ansRes = reasonedState.answerMasteryQuestion(q.correct);
  assert.equal(ansRes.isCorrect, true);
}

// Transfer Scenario Phase
assert.equal(reasonedState.phase, 'TRANSFER');
const transRes = reasonedState.answerTransfer(NUCLEAR_TRANSFER_SCENARIO.correct);
assert.equal(transRes.isCorrect, true);
assert.equal(reasonedState.phase, 'DEBRIEF');

const report = reasonedState.getReport();
assert.equal(report.masteryScore, 100, 'Ideal playthrough must achieve 100% mastery');
assert.equal(report.stars, 3, 'Ideal playthrough must earn 3 stars');
assert.equal(report.decisions.length, 4, 'Must log 4 fiscal year decisions');
assert.ok(report.chapters.length >= 2, 'Must include canonical chapters');
console.log('-> Assertion passed: reasoned strategy achieves 100% mastery, 3 stars, and full debrief report.');

// 7. Flawed Mastery Check Logging
const flawedMasteryState = new NuclearState();
flawedMasteryState.masteryIndex = 1;
const flawedRes = flawedMasteryState.answerMasteryQuestion('A'); // Wrong choice: silos most survivable
assert.equal(flawedRes.isCorrect, false);
assert.ok(flawedRes.misconception);
assert.equal(flawedRes.misconception.tag, 'misc-triad-redundancy');
console.log('-> Assertion passed: flawed mastery check captures targeted misconception remediation.');

console.log('[Lab-10 Selfcheck] All assertions passed successfully!');
