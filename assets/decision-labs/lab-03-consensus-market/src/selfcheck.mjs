import assert from 'node:assert/strict';
import {
  LAB_ID,
  LEARNING_OBJECTIVES,
  MISCONCEPTIONS,
  WTO_CONFIG,
  MEMBER_BLOCS,
  COMPLEMENTARY_PACKAGES,
  MASTERY_CHECKS,
  TRANSFER_SCENARIO,
  WtoState
} from './WtoConfig.js';

console.log('[Lab 03 Self-Check] Starting verification...');

// 1. Assert structure & constants
assert.equal(LAB_ID, 'lab-03', 'LAB_ID must be lab-03');
assert.equal(LEARNING_OBJECTIVES.length, 3, 'Must have 3 learning objectives');
assert.equal(MEMBER_BLOCS.length, 8, 'Must have 8 regional member blocs');
assert.equal(COMPLEMENTARY_PACKAGES.length, 4, 'Must have 4 complementary logroll packages');
assert.equal(MASTERY_CHECKS.length, 3, 'Must have 3 concept mastery checks');
assert.ok(TRANSFER_SCENARIO.id, 'Transfer scenario must exist');
assert.equal(WTO_CONFIG.STARTING_CAPITAL, 10, 'Starting capital must be 10');

// 2. Assert Fresh State starts at 0 stars (no auto-win)
const freshState = new WtoState();
assert.equal(freshState.getStars(), 0, 'Must NOT auto-win on boot (0 stars)');
assert.equal(freshState.session.masteryScore, 0, 'Mastery score starts at 0%');

// 3. Test Naive Individual Concession Run (Exhausts capital -> Single Undertaking Veto)
const naiveState = new WtoState();
naiveState.recordPrediction('pred-individual');

// Concede blocs individually until capital runs out
naiveState.concedeBloc('us_eu');      // cost 2 -> cap 8
naiveState.concedeBloc('g20_ag');     // cost 3 -> cap 5
naiveState.concedeBloc('china_east'); // cost 2 -> cap 3
naiveState.concedeBloc('african_ldc'); // cost 1 -> cap 2
naiveState.concedeBloc('cairns');     // cost 2 -> cap 0

// Now capital is 0, cannot satisfy remaining 3 blocs
const naiveVote = naiveState.executeConsensusVote();
assert.equal(naiveVote.passed, false, 'Unlinked individual concessions must fail consensus vote');
assert.equal(naiveVote.dissentingBlocs.length, 3, 'Must have 3 dissenting holdout blocs');
assert.equal(naiveState.getStars(), 0, 'Failed consensus must receive 0 stars');
assert.ok(naiveVote.feedback.misconception, 'Must emit misconception on unlinked concession failure');
assert.equal(naiveVote.feedback.misconception.tag, 'buy-everyone', 'Must register buy-everyone misconception');

const naiveReport = naiveState.getReport();
assert.ok(naiveReport.misconceptions.some(m => m.tag === 'buy-everyone'), 'Session report must track buy-everyone fallacy');
console.log('PASS Gate 1: Naive unlinked buying fails with 0 stars and logs buy-everyone misconception.');

// 4. Test Disciplined Logrolling Winning Run (All 4 packages -> 4 Capital Left -> 3 Stars)
const winState = new WtoState();
winState.recordPrediction('pred-logroll');

// Link all 4 complementary packages
assert.ok(winState.packageBloc('pkg_agri_services'), 'Package 1 (Agri-Services) should link');
assert.ok(winState.packageBloc('pkg_fisheries_env'), 'Package 2 (Fisheries-Env) should link');
assert.ok(winState.packageBloc('pkg_agri_export'), 'Package 3 (Agri-Export) should link');
assert.ok(winState.packageBloc('pkg_ind_ldc'), 'Package 4 (Ind-LDC) should link');

assert.equal(winState.packages.length, 4, 'All 4 packages must be active');
assert.equal(winState.capital, 4, 'Disciplined logrolling should preserve exactly 4 capital');

const winVote = winState.executeConsensusVote();
assert.equal(winVote.passed, true, 'Disciplined logrolling must achieve full consensus');
assert.equal(winVote.dissentingBlocs.length, 0, 'Zero dissenting blocs on full consensus');
assert.equal(winVote.feedback.outcome, 'success', 'Feedback outcome must be success');
assert.equal(winVote.feedback.predictionMatch, true, 'Prediction match must be confirmed');
assert.ok(winVote.feedback.consequence && winVote.feedback.mechanism && winVote.feedback.citation, 'Feedback payload must contain consequence, mechanism, citation');

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
assert.equal(winState.getStars(), 3, 'Must earn 3 stars with full consensus and 4 capital preserved');
assert.ok(winReport.chapters.length >= 2, 'Report must contain canonical curriculum chapter links');
assert.ok(winReport.chapters.some(c => c.slug === 'wto-decision-making'), 'Must include wto-decision-making chapter');
assert.ok(winReport.chapters.some(c => c.slug === 'world-trading-system'), 'Must include world-trading-system chapter');
console.log('PASS Gate 2: Disciplined omnibus logrolling achieves 3 stars with full consensus and canonical debrief report.');

// 5. Test Majority Override Fallacy & Transfer Distractor Remediation
const errState = new WtoState();
errState.recordPrediction('pred-majority');
errState.concedeBloc('us_eu');
errState.concedeBloc('g20_ag');
errState.concedeBloc('china_east');
const errVote = errState.executeConsensusVote();
assert.equal(errVote.passed, false);
assert.equal(errVote.feedback.misconception.tag, 'holdout-irrational');

// Mastery check error registration
errState.masteryIndex = 0;
const wrongM = errState.answerMastery('c'); // Threaten to expel LDC
assert.equal(wrongM.isCorrect, false);

// Transfer error registration
const wrongT = errState.answerTransfer('opt_majority'); // Call snap vote
assert.equal(wrongT.isCorrect, false);

const errReport = errState.getReport();
assert.ok(errReport.misconceptions.some(m => m.tag === 'holdout-irrational'), 'Report must track holdout-irrational misconception');
assert.ok(errState.getStars() < 3, 'Flawed strategy must NOT earn 3 stars');
console.log('PASS Gate 3: Majority override fallacy and non-triviality verified.');

console.log('[Lab 03 Self-Check] ALL GATES PASSED! Educational Design Bible compliant.');
