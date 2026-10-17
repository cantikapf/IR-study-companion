import assert from 'node:assert';
import {
  LAB_ID,
  LEARNING_OBJECTIVES,
  POSTURES,
  BETA_ARCHETYPES,
  MASTERY_CHECKS,
  TRANSFER_SCENARIO,
  SpiralState
} from './SpiralConfig.js';

console.log('[Lab 04 Self-Check] Starting verification...');

// 1. Assert structure & constants
assert.strictEqual(LAB_ID, 'lab-04', 'LAB_ID must be lab-04');
assert.strictEqual(LEARNING_OBJECTIVES.length, 3, 'Must have 3 learning objectives');
assert.strictEqual(POSTURES.length, 3, 'Must define 3 distinguishable postures');
assert.strictEqual(BETA_ARCHETYPES.length, 2, 'Must define Cautious and Opportunistic archetypes');
assert.strictEqual(MASTERY_CHECKS.length, 3, 'Must have 3 concept mastery checks');
assert.ok(TRANSFER_SCENARIO.id, 'Transfer scenario must exist');

// 2. Assert Not Auto-Winning on fresh state
const freshState = new SpiralState();
assert.strictEqual(freshState.getStars(), 0, 'Must NOT auto-win (0 stars on boot)');
assert.strictEqual(freshState.session.masteryScore, 0, 'Mastery score starts at 0%');

// 3. Test Full Winning Learning Loop Run (Demonstrates all objectives -> 3 Stars)
// Force Cautious Reactive archetype to test predictable cooperative de-escalation
const cautiousArch = BETA_ARCHETYPES.find(a => a.type === 'CAUTIOUS_REACTIVE');
const winState = new SpiralState(cautiousArch);

// Round 1: Predict & Decide Defensive Radar
winState.recordPrediction('pred-mirror');
const t1 = winState.applyTurn('defensive-radar');
assert.strictEqual(t1.feedback.outcome, 'success', 'Defensive radar should yield positive de-escalation');
assert.ok(t1.feedback.consequence && t1.feedback.mechanism && t1.feedback.citation, 'Feedback payload complete');

// Round 2: Predict & Decide Verified CBM
winState.round = 2;
winState.recordPrediction('pred-mirror');
const t2 = winState.applyTurn('verified-cbm');
assert.strictEqual(t2.feedback.outcome, 'success');

// Round 3: Predict & Decide Verified CBM
winState.round = 3;
winState.recordPrediction('pred-mirror');
const t3 = winState.applyTurn('verified-cbm');
assert.strictEqual(t3.feedback.outcome, 'success');

// Attribution prompt test
const attRes = winState.evaluateAttribution('FEAR');
assert.strictEqual(attRes.isCorrect, true, 'Cautious rival must be attributed to FEAR');

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

// 4. Test Radar Blip Real-State Dynamics
const blipState = new SpiralState(cautiousArch);
const initBlipCount = blipState.radarBlips.length;

// Deploying forward strike should increase alert blips
blipState.applyTurn('forward-strike');
assert.ok(blipState.radarBlips.length > initBlipCount, 'Offensive build must accumulate real radar blips');

// Deploying verified CBM should clear offensive strike blips
blipState.applyTurn('verified-cbm');
assert.ok(!blipState.radarBlips.some(b => b.type === 'strike'), 'Verified CBM must clear strike blips');

// 5. Test Suboptimal Run with Misconception Registration
const subState = new SpiralState(cautiousArch);
subState.recordPrediction('pred-mirror');
// Choose forward-strike (triggers offensive spiral & misconception)
const errTurn = subState.applyTurn('forward-strike');
assert.strictEqual(errTurn.feedback.outcome, 'failure', 'Forward strike against cautious causes escalation');
assert.ok(errTurn.feedback.misconception, 'Must emit misconception payload on error');
assert.strictEqual(errTurn.feedback.misconception.tag, 'more-arms-safer');
assert.ok(errTurn.feedback.misconception.remediation.length > 10, 'Must provide actionable remediation');

const errReport = subState.getReport();
assert.ok(errReport.misconceptions.some(m => m.tag === 'more-arms-safer'), 'Session must record misconception with remediation');

// 6. Test Unwinnable check: Bad play should NOT achieve 3 stars
assert.ok(subState.getStars() < 3, 'Suboptimal run must NOT reach 3 stars');

console.log('[Lab 04 Self-Check] ALL 6 TEST SUITES PASSED! Learning loop and real-state radar verified.');
