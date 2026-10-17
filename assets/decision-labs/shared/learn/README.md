# Decision Labs Educational Runtime Foundation (`shared/learn/`)

## Overview

The `shared/learn/` package implements the runtime educational foundation for the 10 Diplomatic Decision Labs in `prototype/decision-labs/`. It operationalizes the learning loop specified in `EDUCATIONAL_DESIGN_BIBLE.md`:

```
BRIEF  →  PREDICT  →  DECIDE  →  CONSEQUENCE  →  EXPLAIN  →  MASTERY CHECK  →  TRANSFER
```

This runtime separates pedagogical instrumentation from game engines (Phaser 3 / Three.js), ensuring uniform learning outcome tracking, objective-based scoring, misconception remediation, and direct integration with canonical curriculum chapters.

---

## Architecture & Modules

### 1. `ChapterLink.js`
Canonical curriculum chapter registry and URL resolution service.
- **Base URL:** `https://ir-guide.netlify.app`
- **Exports:**
  - `CHAPTER_BASE`: Canonical base URL.
  - `LAB_CHAPTERS`: Mapping of all 10 decision labs to primary and supporting curriculum chapters with verified slugs.
  - `chapterUrl(slug)`: Generates canonical URL for any given chapter slug (`/:slug.html`).
  - `chaptersFor(labId)`: Retrieves bound chapter descriptors (`[{ slug, title }]`) for a given lab identifier (`lab-01` to `lab-10`).

### 2. `LearningSession.js`
Stateful pedagogical session manager tracking player hypothesis formation, decision choices, misconception manifestations, mastery questions, and transfer application.
- **Constructor:** `new LearningSession(labId, objectives /* string[] */)`
- **Key Methods:**
  - `recordPrediction(decisionId, predictedOutcome)`: Captures player hypothesis before consequences are revealed.
  - `recordDecision({ decisionId, choice, correctChoice, rationale, misconceptionTag, predicted, actual, outcome, ... })`: Logs turn decisions, checks hypothesis alignment, assesses correctness against learning objectives, and logs misconceptions.
  - `recordMasteryCheck({ questionId, chosen, correct, misconceptionTag, ... })`: Evaluates dedicated theoretical concept questions separate from the game verb.
  - `recordTransfer({ scenarioId, choice, correct, ... })`: Evaluates application of learned principles to secondary historical or regional domains.
- **Getters:**
  - `objectives`: Array of learning objective strings.
  - `masteryScore`: Normalized score (0–100) reflecting demonstrated learning objectives.
  - `stars`: Quantitative performance tier:
    - `>= 85`: 3 Stars
    - `>= 60`: 2 Stars
    - `> 0`: 1 Star
    - `0`: 0 Stars
  - `misconceptions`: Aggregated array of `{ tag, label, remediation, hits }`.
  - `chapterLinks`: Array of `{ slug, title, url }` bound to the current lab.
  - `getReport()` / `report`: Canonical debrief payload for `DebriefPanel`.

### 3. `DebriefPanel.js`
Lab-agnostic, accessible DOM renderer for post-run evaluation.
- **Contract:** Accepts a target container element and a `getReport()` payload.
- **Features:**
  - Displays mastery percentage and star rating.
  - Tabulates decision records with player choices, benchmark options, hypothesis verification, and outcome classifications.
  - Surfaces targeted remedial guidance for any triggered misconception tags.
  - Evaluates cross-domain concept transfer.
  - Renders outbound links to curriculum chapters opening in new tabs (`target="_blank"`, `rel="noopener noreferrer"`).
  - Uses CSS custom properties exclusively (`--bg-void`, `--panel`, `--accent`, `--accent-2`, `--border`, `--text`, `--font-display`).
  - Keyboard accessible with semantic markup and explicit text outcome pairing (`[SUCCESS]`, `[PARTIAL]`, `[FAILURE]`).

---

## Theme Integration (`shared/theme/lab-themes.css`)

Labs define their visual identity via `[data-lab-theme="lab-0N"]` on `<html>` or their root container. The shared stylesheet provides scoped tokens and reusable classes (`.lab-panel`, `.lab-rail`, `.lab-button`, `.lab-badge`, `.lab-meter`) driven entirely by CSS custom properties without hardcoded hex colors.

---

## Verification

Run the headless verification suite:

```bash
node prototype/decision-labs/shared/learn/selfcheck.mjs
```
