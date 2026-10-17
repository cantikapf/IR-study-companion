import assert from 'node:assert/strict';
import {
  LAB_ID,
  LEARNING_OBJECTIVES,
  MISCONCEPTIONS,
  DIPLOMATIC_DOCTRINES,
  PAYOFF,
  MASTERY_CHECKS,
  TRANSFER_SCENARIO,
  DuelState
} from './DuelConfig.js';

console.log('[Lab 02 Self-Check] Starting verification...');

// 1. Assert structure & constants
assert.equal(LAB_ID, 'lab-02', 'LAB_ID must be lab-02');
assert.equal(LEARNING_OBJECTIVES.length, 3, 'Must have 3 learning objectives');
assert.equal(DIPLOMATIC_DOCTRINES.length, 5, 'Must have 5 diplomatic doctrines');
assert.equal(MASTERY_CHECKS.length, 3, 'Must have 3 concept mastery checks');
assert.ok(TRANSFER_SCENARIO.id, 'Transfer scenario must exist');
assert.equal(PAYOFF.CC[0], 5, 'CC payoff should be 5');
assert.equal(PAYOFF.DC[0], 10, 'DC payoff should be 10');
assert.equal(PAYOFF.CD[0], -10, 'CD payoff should be -10');
assert.equal(PAYOFF.DD[0], -2, 'DD payoff should be -2');

// 2. Test Pavlov Win-Stay / Lose-Shift logic
const pavlov = DIPLOMATIC_DOCTRINES.find(d => d.id === 'pavlov');
assert.ok(pavlov, 'Pavlov doctrine must exist');

// CC -> own R (Win) -> stay C
assert.equal(pavlov.makeDecision([{ player: 'C', rival: 'C' }]), 'C', 'Pavlov: Win on CC should stay C');
// DC -> own T (Win) -> stay D
assert.equal(pavlov.makeDecision([{ player: 'C', rival: 'D' }]), 'D', 'Pavlov: Win on DC (own D, opp C) should stay D');
// CD -> own S (Loss) -> flip C to D
assert.equal(pavlov.makeDecision([{ player: 'D', rival: 'C' }]), 'D', 'Pavlov: Loss on CD (own C, opp D) should shift to D');
// DD -> own P (Loss) -> flip D to C
assert.equal(pavlov.makeDecision([{ player: 'D', rival: 'D' }]), 'C', 'Pavlov: Loss on DD (own D, opp D) should shift to C');
console.log('PASS Gate 1: Pavlov Win-Stay / Lose-Shift logic strictly verified.');

// 3. Assert Fresh State starts at 0 stars (no auto-win)
const freshState = new DuelState();
assert.equal(freshState.getStars(), 0, 'Must NOT auto-win on boot (0 stars)');
assert.equal(freshState.session.masteryScore, 0, 'Mastery score starts at 0%');

// 4. Test Full Cooperative Winning Learning Loop Run (Against TFT -> 3 Stars)
const tftDoctrine = DIPLOMATIC_DOCTRINES.find(d => d.id === 'tft');
const winState = new DuelState(tftDoctrine);

for (let r = 1; r <= 8; r++) {
  winState.round = r;
  winState.recordPrediction('CC');
  const fb = winState.applyDecision('C');

  assert.equal(fb.outcome, 'success', `Round ${r} mutual cooperation should be success`);
  assert.equal(fb.predictionMatch, true, `Round ${r} prediction should match actual CC`);
  assert.ok(fb.consequence && fb.mechanism && fb.citation, 'Feedback payload must contain consequence, mechanism, citation');
  assert.equal(fb.citation, 'Axelrod (1984), The Evolution of Cooperation');
}

// Answer all 3 Mastery Checks correctly
for (let i = 0; i < MASTERY_CHECKS.length; i++) {
  winState.masteryIndex = i;
  const q = MASTERY_CHECKS[i];
  const correctChoice = q.choices.find(c => c.correct);
  const mRes = winState.answerMastery(correctChoice.id);
  assert.equal(mRes.isCorrect, true, `Mastery check ${i + 1} must be answered correctly`);
}

// Answer Transfer Scenario correctly
const tfCorrect = TRANSFER_SCENARIO.choices.find(c => c.correct);
const tfRes = winState.answerTransfer(tfCorrect.id);
assert.equal(tfRes.isCorrect, true, 'Transfer scenario must be answered correctly');

// Assert 3 Stars & Mastery Report
const winReport = winState.getReport();
assert.ok(winReport.masteryScore >= 85, `Mastery score must be >= 85 (got ${winReport.masteryScore})`);
assert.equal(winState.getStars(), 3, 'Cooperative run with full concept mastery must achieve 3 stars');
assert.ok(winReport.chapters.length >= 2, 'Report must contain canonical curriculum chapter links');
assert.ok(winReport.chapters.some(c => c.slug === 'game-theory-ir'), 'Must include game-theory-ir chapter');
assert.ok(winReport.chapters.some(c => c.slug === 'rational-choice-theory'), 'Must include rational-choice-theory chapter');
console.log('PASS Gate 2: Cooperative run + Mastery + Transfer achieves 3 stars with canonical debrief report.');

// 5. Test Suboptimal Defection Run logging Misconceptions
const errState = new DuelState(tftDoctrine);
errState.round = 1;
errState.recordPrediction('DC');
const fbDefect = errState.applyDecision('D'); // Defect on Round 1

assert.equal(fbDefect.outcome, 'partial', 'Unilateral defection yields partial outcome');
assert.ok(fbDefect.misconception, 'Must emit misconception payload on betrayal');
assert.equal(fbDefect.misconception.tag, 'beat-the-rival', 'Must catch zero-sum rival dominance fallacy');
assert.ok(fbDefect.misconception.remediation.length > 20, 'Must provide detailed academic remediation');

// Round 2: TFT retaliates with D. Player defects again (DD).
errState.round = 2;
errState.recordPrediction('DD');
const fbDD = errState.applyDecision('D');
assert.equal(fbDD.outcome, 'failure', 'Mutual defection must be failure');
assert.equal(fbDD.misconception.tag, 'always-defect', 'Must catch universal defection fallacy');

const errReport = errState.getReport();
assert.ok(errReport.misconceptions.some(m => m.tag === 'beat-the-rival'), 'Session report must track beat-the-rival misconception');
assert.ok(errReport.misconceptions.some(m => m.tag === 'always-defect'), 'Session report must track always-defect misconception');
assert.ok(errState.getStars() < 3, 'Defective play must NOT achieve 3 stars without concept mastery');
console.log('PASS Gate 3: Misconception tracking and non-triviality verified.');

console.log('[Lab 02 Self-Check] ALL GATES PASSED! Educational Design Bible compliant.');
