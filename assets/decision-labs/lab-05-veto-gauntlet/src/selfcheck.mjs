import assert from 'node:assert/strict';
import {
  UNSC_OBJECTIVES,
  UNSC_CLAUSES,
  UNSC_MASTERY_QUESTIONS,
  UNSC_TRANSFER_SCENARIO,
  VetoState
} from './VetoConfig.js';

console.log('[Lab-05 Selfcheck] Beginning verification...');

// 1. Objectives & Clauses Structure
assert.equal(UNSC_OBJECTIVES.length, 3, 'Must have exactly 3 learning objectives');
assert.equal(UNSC_CLAUSES.length, 4, 'Must have exactly 4 draft resolution clauses');
console.log('-> Assertion passed: 3 learning objectives and 4 draft clauses defined.');

// 2. Cross-Veto Tensions & Full Feedback Payloads
UNSC_CLAUSES.forEach((clause, idx) => {
  assert.equal(clause.choices.length, 3, `Clause ${idx + 1} must have 3 choices`);
  assert.ok(clause.predictionOptions.length >= 2, `Clause ${idx + 1} must have prediction options`);
  assert.ok(clause.expectedPrediction, `Clause ${idx + 1} must define expected prediction`);

  let vetoChoices = 0;
  let successChoices = 0;

  clause.choices.forEach(ch => {
    assert.ok(ch.consequence, `Choice ${ch.id} must have consequence`);
    assert.ok(ch.mechanism, `Choice ${ch.id} must name IR mechanism`);
    assert.ok(ch.citation, `Choice ${ch.id} must include academic citation`);

    const hasVeto = Object.values(ch.p5Votes).includes('VETO');
    if (hasVeto) vetoChoices++;
    if (ch.correct) successChoices++;
  });

  // Ensure non-trivial cross-veto tensions: at least one veto choice and exactly one consensus choice
  assert.ok(vetoChoices >= 1, `Clause ${idx + 1} must feature at least one P5 veto option`);
  assert.equal(successChoices, 1, `Clause ${idx + 1} must feature exactly one viable compromise choice`);
});
console.log('-> Assertion passed: clauses embed real cross-veto tensions and complete feedback payloads.');

// 3. Mandatory UNSC Article & Author Citations Coverage
const allCitations = [
  ...UNSC_CLAUSES.flatMap(c => c.choices.map(ch => ch.citation)),
  ...UNSC_MASTERY_QUESTIONS.map(q => q.citation),
  UNSC_TRANSFER_SCENARIO.citation
].join(' ');

assert.ok(allCitations.includes('Art. 27(3)'), 'Must cite UN Charter Art. 27(3)');
assert.ok(allCitations.includes('Hurd'), 'Must cite Hurd (2007)');
console.log('-> Assertion passed: mandatory citations (UN Charter Art. 27(3) / Hurd 2007) verified.');

// 4. Mastery Check (3 items) & Transfer Scenario Verification
assert.equal(UNSC_MASTERY_QUESTIONS.length, 3, 'Must have exactly 3 mastery check questions');
assert.ok(UNSC_TRANSFER_SCENARIO.title.includes('Kosovo'), 'Transfer scenario must cover 1999 Kosovo Crisis');
console.log('-> Assertion passed: mastery check (3 items) and 1999 Kosovo transfer scenario verified.');

// 5. Complete 7-Phase Learning Loop Simulation (Ideal Run -> 3 Stars)
const idealState = new VetoState();
assert.equal(idealState.phase, 'BRIEF');

// Traverse all 4 clauses
for (let i = 0; i < UNSC_CLAUSES.length; i++) {
  const clause = idealState.getCurrentClause();
  assert.ok(clause, `Clause ${i + 1} must be active`);

  // PREDICT phase
  idealState.recordPrediction(clause.expectedPrediction);
  assert.equal(idealState.phase, 'DECIDE');

  // DECIDE phase with compromise choice 'C'
  const outcome = idealState.executeClauseDecision('C');
  assert.equal(outcome.isCorrect, true);
  assert.equal(outcome.payload.outcome, 'success');
  assert.equal(outcome.payload.predictionMatch, true);
  assert.equal(idealState.phase, 'CONSEQUENCE');

  idealState.advanceClause();
}

assert.equal(idealState.phase, 'VOTE');
const voteRes = idealState.executeFinalVote();
assert.equal(voteRes.passed, true, 'Compromise draft resolution must pass');
assert.equal(voteRes.p5Vetoed, false, 'Zero P5 vetoes in compromise draft');
assert.ok(voteRes.totalYes >= 9, 'Must achieve at least 9 affirmative votes');

// MASTERY CHECK phase
assert.equal(idealState.phase, 'VOTING');
idealState.phase = 'MASTERY';

for (let i = 0; i < UNSC_MASTERY_QUESTIONS.length; i++) {
  const q = idealState.getCurrentMasteryQuestion();
  const res = idealState.answerMasteryQuestion(q.correct);
  assert.equal(res.isCorrect, true, `Mastery question ${i + 1} must be correct`);
}

assert.equal(idealState.phase, 'TRANSFER');
const transferRes = idealState.answerTransfer(UNSC_TRANSFER_SCENARIO.correct);
assert.equal(transferRes.isCorrect, true, 'Transfer scenario must be correct');
assert.equal(idealState.phase, 'DEBRIEF');

const report = idealState.getReport();
assert.equal(report.masteryScore, 100, 'Ideal run must achieve 100% mastery score');
assert.equal(report.stars, 3, 'Ideal run must earn 3 stars');
assert.equal(report.decisions.length, 4, 'Must log 4 decisions in report');
assert.ok(report.chapters.length >= 2, 'Must bind curriculum chapters');
console.log('-> Assertion passed: ideal playthrough achieves 100% mastery, 3 stars, and full debrief report.');

// 6. Flawed Strategy Simulation & Misconception Logging
const flawedState = new VetoState();
// Make a flawed decision triggering Russian/Chinese veto on Clause 1
flawedState.recordPrediction('B'); // Wrong prediction
const flawedDecision = flawedState.executeClauseDecision('A'); // Clause 1 Option A: Armed force -> Veto!
assert.equal(flawedDecision.isCorrect, false);
assert.equal(flawedDecision.payload.outcome, 'failure');
assert.ok(flawedDecision.payload.misconception, 'Flawed decision must capture misconception payload');
assert.equal(flawedDecision.payload.misconception.tag, 'misc-majority');

const flawedVote = flawedState.executeFinalVote();
assert.equal(flawedVote.passed, false, 'Draft with unaddressed P5 veto must fail');
assert.equal(flawedVote.p5Vetoed, true, 'P5 veto must be logged');

// Answer mastery question with misconception
const q2 = UNSC_MASTERY_QUESTIONS[1];
flawedState.masteryIndex = 1;
const flawedMastery = flawedState.answerMasteryQuestion('A'); // Wrong: thinks abstention is a veto
assert.equal(flawedMastery.isCorrect, false);
assert.ok(flawedMastery.misconception);
assert.equal(flawedMastery.misconception.tag, 'misc-abstention');

const flawedReport = flawedState.getReport();
assert.ok(flawedReport.misconceptions.length >= 2, 'Misconceptions must be aggregated in report');
console.log('-> Assertion passed: flawed run triggers P5 veto failure and logs misconceptions.');

console.log('[Lab-05 Selfcheck] All assertions passed successfully!');
