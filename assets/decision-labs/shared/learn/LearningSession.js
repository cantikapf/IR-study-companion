import { chapterUrl, chaptersFor } from './ChapterLink.js';

/**
 * LearningSession — Tracks player hypothesis, decision fidelity, concept mastery,
 * misconception manifestations, and transfer scenarios across a decision lab run.
 */
export class LearningSession {
  /**
   * @param {string} labId - Canonical lab identifier (e.g., 'lab-01').
   * @param {string[]} [objectives=[]] - Specific learning objectives assessed in this lab.
   */
  constructor(labId, objectives = []) {
    this.labId = labId;
    this._objectives = Array.isArray(objectives) ? [...objectives] : [];
    this._predictions = new Map();
    this._decisions = [];
    this._masteryChecks = [];
    this._transfers = [];
    this._misconceptions = new Map();
    this._demonstratedObjectives = new Set();
    this._itemSequence = 0;
    this._fallbackCorrectCount = 0;
    this._fallbackTotalAssessments = 0;
  }

  /**
   * PREDICT phase — Records player hypothesis prior to observing systemic consequences.
   * @param {string} decisionId
   * @param {any} predictedOutcome
   */
  recordPrediction(decisionId, predictedOutcome) {
    if (!decisionId) return;
    this._predictions.set(decisionId, predictedOutcome);
  }

  /**
   * EXPLAIN phase — Records turn outcome and verifies hypothesis.
   * @param {Object} params
   * @param {string} params.decisionId
   * @param {any} params.choice
   * @param {any} params.correctChoice
   * @param {string} [params.rationale]
   * @param {string|Object} [params.misconceptionTag]
   * @param {string|Object} [params.misconception]
   * @param {any} [params.predicted]
   * @param {any} [params.actual]
   * @param {string} [params.outcome] - 'success' | 'partial' | 'failure'
   * @param {string} [params.consequence]
   * @param {string} [params.mechanism]
   * @param {string} [params.citation]
   * @param {number|string} [params.objectiveIndex]
   * @param {number|string} [params.objective]
   * @returns {Object} Recorded decision entry
   */
  recordDecision({
    decisionId,
    choice,
    correctChoice,
    rationale = '',
    misconceptionTag = null,
    misconception = null,
    predicted,
    actual,
    outcome,
    consequence,
    mechanism,
    citation,
    objectiveIndex,
    objective
  } = {}) {
    this._fallbackTotalAssessments += 1;

    // Resolve prediction and hypothesis alignment
    const predictedVal = predicted !== undefined ? predicted : this._predictions.get(decisionId);
    let matched = null;
    if (predictedVal !== undefined && actual !== undefined) {
      matched = (predictedVal === actual);
    } else if (predictedVal !== undefined && actual === undefined) {
      matched = null;
    }

    // Determine decision correctness
    let isCorrect = false;
    if (choice !== undefined && correctChoice !== undefined) {
      isCorrect = (choice === correctChoice);
    } else if (outcome !== undefined) {
      isCorrect = (outcome === 'success');
    }

    if (isCorrect) {
      this._fallbackCorrectCount += 1;
      this._creditObjective({
        objectiveIndex,
        objective,
        defaultIndex: this._itemSequence++
      });
    } else {
      this._itemSequence++;
    }

    // Record misconception if provided
    const miscData = misconception || misconceptionTag;
    if (miscData) {
      this._recordMisconception(miscData);
    }

    const decisionRecord = {
      decisionId,
      choice,
      correctChoice,
      rationale: rationale || mechanism || consequence || '',
      predicted: predictedVal,
      actual,
      matched,
      outcome: outcome || (isCorrect ? 'success' : 'failure'),
      isCorrect,
      consequence,
      mechanism,
      citation
    };

    this._decisions.push(decisionRecord);
    return decisionRecord;
  }

  /**
   * MASTERY CHECK — Short concept question evaluating theoretical mechanics distinct from game move.
   * @param {Object} params
   * @param {string} params.questionId
   * @param {any} params.chosen
   * @param {any} params.correct
   * @param {string|Object} [params.misconceptionTag]
   * @param {string|Object} [params.misconception]
   * @param {number|string} [params.objectiveIndex]
   * @param {number|string} [params.objective]
   * @returns {Object} Recorded check entry
   */
  recordMasteryCheck({
    questionId,
    chosen,
    correct,
    misconceptionTag = null,
    misconception = null,
    objectiveIndex,
    objective
  } = {}) {
    this._fallbackTotalAssessments += 1;

    let isCorrect = false;
    if (typeof correct === 'boolean') {
      isCorrect = correct;
    } else if (chosen !== undefined && correct !== undefined) {
      isCorrect = (chosen === correct);
    }

    if (isCorrect) {
      this._fallbackCorrectCount += 1;
      this._creditObjective({
        objectiveIndex,
        objective,
        defaultIndex: this._itemSequence++
      });
    } else {
      this._itemSequence++;
      const miscData = misconception || misconceptionTag;
      if (miscData) {
        this._recordMisconception(miscData);
      }
    }

    const checkRecord = {
      questionId,
      chosen,
      correct,
      isCorrect
    };

    this._masteryChecks.push(checkRecord);
    return checkRecord;
  }

  /**
   * TRANSFER — Secondary scenario testing analytical application to a divergent historical or regional case.
   * @param {Object} params
   * @param {string} params.scenarioId
   * @param {any} params.choice
   * @param {any} params.correct
   * @param {number|string} [params.objectiveIndex]
   * @param {number|string} [params.objective]
   * @returns {Object} Recorded transfer entry
   */
  recordTransfer({
    scenarioId,
    choice,
    correct,
    objectiveIndex,
    objective
  } = {}) {
    this._fallbackTotalAssessments += 1;

    let isCorrect = false;
    if (typeof correct === 'boolean') {
      isCorrect = correct;
    } else if (choice !== undefined && correct !== undefined) {
      isCorrect = (choice === correct);
    }

    if (isCorrect) {
      this._fallbackCorrectCount += 1;
      this._creditObjective({
        objectiveIndex,
        objective,
        defaultIndex: this._itemSequence++
      });
    } else {
      this._itemSequence++;
    }

    const transferRecord = {
      scenarioId,
      choice,
      correct,
      isCorrect
    };

    this._transfers.push(transferRecord);
    return transferRecord;
  }

  /**
   * Internal helper to credit mastery for learning objectives.
   * @private
   */
  _creditObjective({ objectiveIndex, objective, defaultIndex = null }) {
    if (typeof objectiveIndex === 'number' && objectiveIndex >= 0) {
      this._demonstratedObjectives.add(objectiveIndex);
      return;
    }
    if (typeof objective === 'number' && objective >= 0) {
      this._demonstratedObjectives.add(objective);
      return;
    }
    if (typeof objective === 'string') {
      const idx = this._objectives.indexOf(objective);
      if (idx !== -1) {
        this._demonstratedObjectives.add(idx);
      } else {
        this._demonstratedObjectives.add(objective);
      }
      return;
    }
    if (this._objectives.length > 0 && typeof defaultIndex === 'number') {
      const idx = defaultIndex % this._objectives.length;
      this._demonstratedObjectives.add(idx);
    }
  }

  /**
   * Internal helper to record and aggregate misconceptions.
   * @private
   */
  _recordMisconception(data) {
    if (!data) return;
    let tag = '';
    let label = '';
    let remediation = '';

    if (typeof data === 'string') {
      tag = data.trim();
    } else if (typeof data === 'object') {
      tag = data.tag ? String(data.tag).trim() : '';
      label = data.label || '';
      remediation = data.remediation || '';
    }

    if (!tag) return;

    if (!label) {
      label = tag
        .split(/[-_]/)
        .map(w => w.charAt(0).toUpperCase() + w.slice(1))
        .join(' ');
    }

    if (this._misconceptions.has(tag)) {
      const existing = this._misconceptions.get(tag);
      existing.hits += 1;
      if (!existing.remediation && remediation) {
        existing.remediation = remediation;
      }
      if ((!existing.label || existing.label === tag) && label) {
        existing.label = label;
      }
    } else {
      this._misconceptions.set(tag, {
        tag,
        label,
        remediation,
        hits: 1
      });
    }
  }

  /**
   * List of learning objectives defined for this lab.
   * @returns {string[]}
   */
  get objectives() {
    return [...this._objectives];
  }

  /**
   * Mastery score 0..100 computed from demonstrated objectives.
   * @returns {number}
   */
  get masteryScore() {
    if (this._objectives.length === 0) {
      if (this._fallbackTotalAssessments === 0) return 0;
      return Math.round((this._fallbackCorrectCount / this._fallbackTotalAssessments) * 100);
    }
    const demonstrated = this._demonstratedObjectives.size;
    const total = this._objectives.length;
    const score = Math.round((demonstrated / total) * 100);
    return Math.min(100, Math.max(0, score));
  }

  /**
   * Aggregated misconceptions with hit count and targeted remediation.
   * @returns {Array<{ tag: string, label: string, remediation: string, hits: number }>}
   */
  get misconceptions() {
    return Array.from(this._misconceptions.values());
  }

  /**
   * Bound curriculum chapters for this lab.
   * @returns {Array<{ slug: string, title: string, url: string }>}
   */
  get chapterLinks() {
    return chaptersFor(this.labId).map(ch => ({
      slug: ch.slug,
      title: ch.title,
      url: chapterUrl(ch.slug)
    }));
  }

  /**
   * Stars earned based on mastery score: >=85 -> 3, >=60 -> 2, >0 -> 1, else 0.
   * @returns {number}
   */
  get stars() {
    return this.getStars();
  }

  /**
   * Stars method matching Bible §1 specification.
   * @returns {number}
   */
  getStars() {
    const score = this.masteryScore;
    if (score >= 85) return 3;
    if (score >= 60) return 2;
    if (score > 0) return 1;
    return 0;
  }

  /**
   * Full debrief payload getter.
   */
  get report() {
    return this.getReport();
  }

  /**
   * Returns complete debrief report payload matching SSOT contract.
   * @returns {Object}
   */
  getReport() {
    return {
      labId: this.labId,
      objectives: this.objectives,
      masteryScore: this.masteryScore,
      stars: this.getStars(),
      decisions: this._decisions.map(d => ({
        decisionId: d.decisionId,
        choice: d.choice,
        correctChoice: d.correctChoice,
        rationale: d.rationale,
        predicted: d.predicted,
        actual: d.actual,
        matched: d.matched
      })),
      misconceptions: this.misconceptions,
      transfer: {
        attempted: this._transfers.length > 0,
        correct: this._transfers.length > 0 && this._transfers.every(t => t.isCorrect)
      },
      chapters: this.chapterLinks
    };
  }
}
