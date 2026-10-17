import assert from 'node:assert';
import {
  LAB_ID,
  LEARNING_OBJECTIVES,
  CRISIS_ACTS,
  MASTERY_CHECKS,
  TRANSFER_SCENARIO,
  ALLISON_MATRIX,
  MISCONCEPTIONS,
  CrisisState
} from './CrisisConfig.js';

console.log('[Lab 01 Self-Check] Starting verification...');

// 1. Assert structure & constants
assert.strictEqual(LAB_ID, 'lab-01', 'LAB_ID must be lab-01');
assert.strictEqual(LEARNING_OBJECTIVES.length, 3, 'Must have 3 learning objectives');
assert.strictEqual(CRISIS_ACTS.length, 3, 'Must have 3 crisis acts');
assert.strictEqual(MASTERY_CHECKS.length, 3, 'Must have 3 concept mastery checks');
assert.ok(TRANSFER_SCENARIO.id, 'Transfer scenario must exist');
assert.strictEqual(ALLISON_MATRIX.length, 3, 'Allison matrix must define all 3 models');

// 2. Assert Not Auto-Winning on fresh state
const freshState = new CrisisState();
assert.strictEqual(freshState.getStars(), 0, 'Must NOT auto-win (0 stars on boot)');
assert.strictEqual(freshState.session.masteryScore, 0, 'Mastery score starts at 0%');

// 3. Test Full Winning Learning Loop Run (Demonstrates all objectives -> 3 Stars)
const winState = new CrisisState();

// Act 1: Predict & Decide
winState.recordPrediction('pred-rational');
const fb1 = winState.applyDecision('blockade');
assert.strictEqual(fb1.outcome, 'success', 'Act 1 blockade should be success');
assert.strictEqual(fb1.predictionMatch, true, 'Prediction match should be true');
assert.ok(fb1.consequence && fb1.mechanism && fb1.citation, 'Feedback payload must have consequence, mechanism, citation');

// Act 2: Predict & Decide
winState.act = 2;
winState.recordPrediction('pred-sub-rational');
const fb2 = winState.applyDecision('trollope');
assert.strictEqual(fb2.outcome, 'success');
assert.strictEqual(fb2.predictionMatch, true);

// Act 3: Predict & Decide
winState.act = 3;
winState.recordPrediction('pred-end-bargain');
const fb3 = winState.applyDecision('dual-track');
assert.strictEqual(fb3.outcome, 'success');

// Mastery Checks (All correct)
for (let i = 0; i < MASTERY_CHECKS.length; i++) {
  const q = MASTERY_CHECKS[i];
  const correctChoice = q.choices.find(c => c.correct);
  const mRes = winState.answerMastery(correctChoice.id);
  assert.strictEqual(mRes.isCorrect, true, `Mastery question ${i + 1} must be answered correctly`);
}

// Transfer Scenario (Correct)
const tfCorrect = TRANSFER_SCENARIO.choices.find(c => c.correct);
const tfRes = winState.answerTransfer(tfCorrect.id);
assert.strictEqual(tfRes.isCorrect, true, 'Transfer scenario must be answered correctly');

// Assert Report & 3 Stars
const winReport = winState.getReport();
assert.ok(winReport.masteryScore >= 85, `Mastery score must be >=85 (actual: ${winReport.masteryScore})`);
assert.strictEqual(winState.getStars(), 3, 'Must earn 3 stars with full mastery');
assert.ok(winReport.chapters.length >= 2, 'Report must contain canonical chapter bindings');

// 4. Test Suboptimal Run with Misconception Registration
const subState = new CrisisState();
subState.recordPrediction('pred-rational');
// Choose airstrike (Model II SOP routine with misconception)
const fbErr = subState.applyDecision('airstrike');
assert.strictEqual(fbErr.outcome, 'failure', 'Airstrike leads to military escalation failure');
assert.ok(fbErr.misconception, 'Must emit misconception payload on error');
assert.strictEqual(fbErr.misconception.tag, 'unitary-actor');
assert.ok(fbErr.misconception.remediation.length > 10, 'Must provide actionable remediation');

const errReport = subState.getReport();
assert.ok(errReport.misconceptions.some(m => m.tag === 'unitary-actor'), 'Session must record misconception with remediation');

// 5. Test Unwinnable check: Bad play should NOT achieve 3 stars
assert.ok(subState.getStars() < 3, 'Bad choices must NOT reach 3 stars');

console.log('[Lab 01 Self-Check] ALL 5 TEST SUITES PASSED! Learning loop and pedagogy verified.');
