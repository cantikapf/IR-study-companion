import assert from 'node:assert/strict';
import { chapterUrl, chaptersFor, CHAPTER_BASE, LAB_CHAPTERS } from './ChapterLink.js';
import { LearningSession } from './LearningSession.js';
import { DebriefPanel } from './DebriefPanel.js';
import { Events, eventBus, SPECTACLE_COMBO, SPECTACLE_HIT_FREEZE, SPECTACLE_SHAKE, SPECTACLE_THEME_FLASH, SPECTACLE_EXPRESSION_UPDATE } from '../core/EventBus.js';
import { CONSTANTS, SPECTACLE_COMBO as C_COMBO } from '../core/Constants.js';

// --- Verification Gate 1: ChapterLink bindings and URL building ---
assert.equal(typeof CHAPTER_BASE, 'string');
assert.equal(CHAPTER_BASE, 'https://ir-guide.netlify.app');

const lab01Chapters = chaptersFor('lab-01');
assert.ok(Array.isArray(lab01Chapters));
assert.ok(lab01Chapters.length >= 2);
assert.equal(lab01Chapters[0].slug, 'models-fpdm');
assert.equal(chapterUrl(lab01Chapters[0].slug), 'https://ir-guide.netlify.app/models-fpdm.html');

for (let i = 1; i <= 10; i++) {
  const labId = `lab-${String(i).padStart(2, '0')}`;
  const chapters = chaptersFor(labId);
  assert.ok(chapters.length >= 2, `Expected at least 2 bound chapters for ${labId}`);
  for (const ch of chapters) {
    assert.ok(ch.slug, `Missing slug in ${labId}`);
    assert.ok(ch.title, `Missing title in ${labId}`);
    assert.equal(chapterUrl(ch.slug), `${CHAPTER_BASE}/${ch.slug}.html`);
  }
}

// --- Verification Gate 2: Spectacle Events in EventBus & Constants ---
assert.equal(Events.SPECTACLE_COMBO, 'spectacle:combo');
assert.equal(Events.SPECTACLE_HIT_FREEZE, 'spectacle:hit_freeze');
assert.equal(Events.SPECTACLE_SHAKE, 'spectacle:shake');
assert.equal(Events.SPECTACLE_THEME_FLASH, 'spectacle:theme_flash');
assert.equal(Events.SPECTACLE_EXPRESSION_UPDATE, 'spectacle:expression_update');

assert.equal(SPECTACLE_COMBO, 'spectacle:combo');
assert.equal(SPECTACLE_HIT_FREEZE, 'spectacle:hit_freeze');
assert.equal(SPECTACLE_SHAKE, 'spectacle:shake');
assert.equal(SPECTACLE_THEME_FLASH, 'spectacle:theme_flash');
assert.equal(SPECTACLE_EXPRESSION_UPDATE, 'spectacle:expression_update');

assert.equal(CONSTANTS.SPECTACLE.COMBO, 'spectacle:combo');
assert.equal(C_COMBO, 'spectacle:combo');

// Verify unhandled spectacle events are clean no-ops
eventBus.emit(Events.SPECTACLE_COMBO, { combo: 3 });
eventBus.emit('spectacle:unknown', { test: true });

// --- Verification Gate 3: LearningSession Scripted Scenario ---
const objectives = [
  'LO1: Distinguish Allison Model I / II / III',
  'LO2: Explain organisational routines and bureaucratic bargaining',
  'LO3: Recognise time compression and incomplete information'
];

const session = new LearningSession('lab-01', objectives);

// Initial state assertions
assert.equal(session.masteryScore, 0);
assert.equal(session.stars, 0);
assert.equal(session.getStars(), 0);
assert.deepEqual(session.misconceptions, []);
assert.equal(session.objectives.length, 3);

// Phase 1: PREDICT — Record player hypotheses
session.recordPrediction('decision-1', 'cooperation');
session.recordPrediction('decision-2', 'immediate-deescalation');

// Phase 2: DECIDE & EXPLAIN — Decision 1: Correct (demonstrates objective index 0)
const d1 = session.recordDecision({
  decisionId: 'decision-1',
  choice: 'sop-naval-quarantine',
  correctChoice: 'sop-naval-quarantine',
  rationale: 'Naval quarantine leverages pre-existing organizational routines.',
  actual: 'cooperation',
  objectiveIndex: 0
});

assert.equal(d1.isCorrect, true);
assert.equal(d1.matched, true);
assert.equal(session.masteryScore, 33); // 1 of 3 demonstrated
assert.equal(session.stars, 1);        // >0 -> 1 star
assert.equal(session.getStars(), 1);

// Phase 3: DECIDE & EXPLAIN — Decision 2: Wrong (fails objective index 1, logs misconception)
const d2 = session.recordDecision({
  decisionId: 'decision-2',
  choice: 'assume-unitary-state',
  correctChoice: 'broker-cabinet-bargain',
  rationale: 'States are not unitary; departmental competition influences decisions.',
  misconceptionTag: {
    tag: 'unitary-actor-fallacy',
    label: 'Unitary Rational Actor Fallacy',
    remediation: 'Internal bureaucratic politics fracture rational unitary strategy.'
  },
  actual: 'stalemate',
  objectiveIndex: 1
});

assert.equal(d2.isCorrect, false);
assert.equal(d2.matched, false);
assert.equal(session.masteryScore, 33); // Still 1 of 3 demonstrated
assert.equal(session.stars, 1);
assert.equal(session.misconceptions.length, 1);
assert.equal(session.misconceptions[0].tag, 'unitary-actor-fallacy');
assert.equal(session.misconceptions[0].hits, 1);

// Phase 4: MASTERY CHECK — Test misconception aggregation (same tag on failed attempt)
session.recordMasteryCheck({
  questionId: 'check-concept-01',
  chosen: 'unitary-rational-choice',
  correct: 'bureaucratic-politics-model',
  misconceptionTag: 'unitary-actor-fallacy',
  objectiveIndex: 1
});

// Assert misconception aggregation: hits incremented to 2
assert.equal(session.misconceptions.length, 1);
assert.equal(session.misconceptions[0].hits, 2);
assert.equal(session.misconceptions[0].tag, 'unitary-actor-fallacy');

// Phase 5: MASTERY CHECK (Passed) — Remediates and demonstrates objective index 1
session.recordMasteryCheck({
  questionId: 'check-concept-02',
  chosen: 'bureaucratic-politics-model',
  correct: 'bureaucratic-politics-model',
  objectiveIndex: 1
});

assert.equal(session.masteryScore, 67); // 2 of 3 demonstrated
assert.equal(session.stars, 2);        // >=60 -> 2 stars
assert.equal(session.getStars(), 2);

// Phase 6: TRANSFER — Demonstrates objective index 2 in secondary scenario (July 1914)
session.recordTransfer({
  scenarioId: 'transfer-july-1914',
  choice: 'railway-timetable-mobilisation',
  correct: 'railway-timetable-mobilisation',
  objectiveIndex: 2
});

assert.equal(session.masteryScore, 100); // 3 of 3 demonstrated
assert.equal(session.stars, 3);         // >=85 -> 3 stars
assert.equal(session.getStars(), 3);

// Verify report structure
const report = session.getReport();
assert.equal(report.labId, 'lab-01');
assert.equal(report.masteryScore, 100);
assert.equal(report.stars, 3);
assert.equal(report.decisions.length, 2);
assert.equal(report.decisions[0].matched, true);
assert.equal(report.decisions[1].matched, false);
assert.equal(report.misconceptions.length, 1);
assert.equal(report.misconceptions[0].hits, 2);
assert.equal(report.transfer.attempted, true);
assert.equal(report.transfer.correct, true);
assert.equal(report.chapters.length, 2);
assert.equal(report.chapters[0].slug, 'models-fpdm');
assert.equal(report.chapters[0].url, 'https://ir-guide.netlify.app/models-fpdm.html');

// --- Verification Gate 4: DebriefPanel HTML Rendering ---
const panel = new DebriefPanel();
const html = panel.getHtml(report);

assert.ok(html.includes('DECISION LAB DEBRIEF · LAB-01'));
assert.ok(html.includes('100%'));
assert.ok(html.includes('[SUCCESS]'));
assert.ok(html.includes('3 / 3 STARS'));
assert.ok(html.includes('unitary-actor-fallacy'));
assert.ok(html.includes('OBSERVED HITS: 2'));
assert.ok(html.includes('https://ir-guide.netlify.app/models-fpdm.html'));
assert.ok(html.includes('target="_blank"'));
assert.ok(html.includes('rel="noopener noreferrer"'));

// Assert zero hardcoded hex colors in rendered HTML
const hexMatches = html.match(/#[0-9a-fA-F]{3,8}\b/g) || [];
assert.deepEqual(hexMatches, [], `Found hardcoded hex colors in DebriefPanel output: ${hexMatches.join(', ')}`);

console.log('PASS: All educational runtime verification assertions passed successfully.');
