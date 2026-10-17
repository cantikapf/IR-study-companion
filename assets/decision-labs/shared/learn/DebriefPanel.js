/**
 * DebriefPanel — Renders educational debrief reports for Decision Labs.
 * Formats mastery scores, decision histories, misconception remediation,
 * transfer evaluations, and curriculum chapter references.
 *
 * All styling strictly consumes CSS custom properties from the active lab theme.
 * Zero hardcoded hex colours. Complete keyboard accessibility and academic English copy.
 */

function escapeHtml(value) {
  if (value === null || value === undefined) return '';
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function renderStarSvg(filled) {
  if (filled) {
    return `<svg class="debrief-star debrief-star-filled" viewBox="0 0 24 24" aria-hidden="true" width="22" height="22">
      <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26" />
    </svg>`;
  }
  return `<svg class="debrief-star debrief-star-empty" viewBox="0 0 24 24" aria-hidden="true" width="22" height="22">
    <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26" fill="none" stroke="currentColor" stroke-width="1.8" />
  </svg>`;
}

const DEBRIEF_STYLE_ID = 'ir-debrief-panel-styles';

const DEBRIEF_CSS = `
.debrief-panel {
  background-color: var(--panel);
  color: var(--text);
  border: 1px solid var(--border);
  font-family: var(--font-display, monospace);
  padding: 24px;
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  gap: 24px;
  box-sizing: border-box;
  width: 100%;
}

.debrief-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border);
  padding-bottom: 16px;
  gap: 16px;
  flex-wrap: wrap;
}

.debrief-title-block {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.debrief-title {
  font-size: 1.25rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text);
  margin: 0;
}

.debrief-subtitle {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--text);
  opacity: 0.75;
  margin: 0;
}

.debrief-score-summary {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
}

.debrief-stars-row {
  display: flex;
  align-items: center;
  gap: 4px;
}

.debrief-star-filled {
  color: var(--accent);
  fill: currentColor;
}

.debrief-star-empty {
  color: var(--border);
  fill: none;
  stroke: currentColor;
}

.debrief-stars-text {
  font-size: 0.85rem;
  font-weight: 800;
  color: var(--accent);
  margin-left: 6px;
}

.debrief-score-metric {
  display: flex;
  align-items: center;
  gap: 10px;
}

.debrief-score-num {
  font-size: 1.75rem;
  font-weight: 900;
  color: var(--text);
  line-height: 1;
}

.debrief-badge {
  display: inline-flex;
  align-items: center;
  padding: 3px 8px;
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  border: 1px solid var(--border);
  background-color: var(--bg-void);
  color: var(--text);
  border-radius: 2px;
}

.debrief-badge-success {
  border-color: var(--accent);
  color: var(--accent);
}

.debrief-badge-partial {
  border-color: var(--accent-2);
  color: var(--accent-2);
}

.debrief-badge-failure {
  border-color: var(--border);
  color: var(--text);
  opacity: 0.85;
}

.debrief-badge-neutral {
  border-color: var(--border);
  color: var(--text);
  opacity: 0.7;
}

.debrief-section {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.debrief-section-heading {
  font-size: 0.95rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent);
  margin: 0;
  border-bottom: 1px solid var(--border);
  padding-bottom: 6px;
}

.debrief-table-scroll {
  overflow-x: auto;
  border: 1px solid var(--border);
  background-color: var(--bg-void);
}

.debrief-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.82rem;
}

.debrief-table th {
  background-color: var(--panel);
  color: var(--text);
  border-bottom: 1px solid var(--border);
  padding: 10px 12px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
}

.debrief-table td {
  padding: 10px 12px;
  border-bottom: 1px solid var(--border);
  color: var(--text);
  vertical-align: top;
}

.debrief-table tr:last-child td {
  border-bottom: none;
}

.debrief-decision-rationale {
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--text);
  opacity: 0.85;
  margin-top: 4px;
}

.debrief-misconceptions-grid {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.debrief-card {
  background-color: var(--bg-void);
  border: 1px solid var(--border);
  padding: 12px 16px;
  border-radius: 3px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  box-sizing: border-box;
}

.debrief-card:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.debrief-card-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.75rem;
}

.debrief-tag {
  font-size: 0.72rem;
  color: var(--accent-2);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.debrief-hits-counter {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--text);
  opacity: 0.75;
}

.debrief-card-title {
  font-size: 0.92rem;
  font-weight: 800;
  color: var(--text);
  margin: 0;
}

.debrief-card-desc {
  font-size: 0.82rem;
  line-height: 1.5;
  color: var(--text);
  opacity: 0.9;
  margin: 0;
}

.debrief-transfer-card {
  background-color: var(--bg-void);
  border: 1px solid var(--border);
  padding: 14px 18px;
  border-radius: 3px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.debrief-transfer-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.debrief-chapters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 12px;
}

.debrief-chapter-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 8px;
  padding: 12px 16px;
  background-color: var(--bg-void);
  border: 1px solid var(--border);
  color: var(--text);
  text-decoration: none;
  border-radius: 3px;
  transition: border-color 0.15s ease, background-color 0.15s ease;
}

.debrief-chapter-card:hover {
  border-color: var(--accent);
  background-color: var(--panel);
}

.debrief-chapter-card:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-color: var(--accent);
}

.debrief-chapter-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.debrief-chapter-slug {
  font-size: 0.72rem;
  color: var(--accent-2);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.debrief-chapter-arrow {
  color: var(--accent);
  font-weight: 800;
  font-size: 0.85rem;
}

.debrief-chapter-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--text);
  line-height: 1.4;
}

.debrief-empty-note {
  font-size: 0.82rem;
  color: var(--text);
  opacity: 0.75;
  margin: 0;
  font-style: italic;
}
`;

function ensureStylesInjected() {
  if (typeof document === 'undefined') return;
  if (document.getElementById(DEBRIEF_STYLE_ID)) return;
  const styleEl = document.createElement('style');
  styleEl.id = DEBRIEF_STYLE_ID;
  styleEl.textContent = DEBRIEF_CSS;
  document.head.appendChild(styleEl);
}

export class DebriefPanel {
  /**
   * @param {HTMLElement|string} [container]
   * @param {Object} [report]
   */
  constructor(container = null, report = null) {
    this.container = typeof container === 'string' && typeof document !== 'undefined'
      ? document.querySelector(container)
      : container;
    this.report = report;
    ensureStylesInjected();
    if (this.container && this.report) {
      this.render();
    }
  }

  /**
   * Generates debrief HTML from report payload.
   * @param {Object} report
   * @returns {string}
   */
  getHtml(report = this.report) {
    if (!report) return '';

    const {
      labId = 'lab',
      masteryScore = 0,
      stars = 0,
      decisions = [],
      misconceptions = [],
      transfer = { attempted: false, correct: false },
      chapters = []
    } = report;

    // Evaluate overall mastery level paired with explicit text label
    let masteryLabel = 'FAILURE';
    let masteryBadgeVariant = 'failure';
    if (masteryScore >= 85) {
      masteryLabel = 'SUCCESS';
      masteryBadgeVariant = 'success';
    } else if (masteryScore >= 60) {
      masteryLabel = 'PARTIAL';
      masteryBadgeVariant = 'partial';
    }

    const starIcons = [1, 2, 3].map(i => renderStarSvg(i <= stars)).join('');

    // Decisions rows
    const decisionRows = decisions.map((d, idx) => {
      const decisionNum = idx + 1;
      const isChoiceCorrect = (d.choice !== undefined && d.correctChoice !== undefined)
        ? (d.choice === d.correctChoice)
        : null;

      let rowOutcomeLabel = 'FAILURE';
      let rowBadgeVariant = 'failure';
      if (isChoiceCorrect === true) {
        rowOutcomeLabel = 'SUCCESS';
        rowBadgeVariant = 'success';
      } else if (d.matched === true && isChoiceCorrect === false) {
        rowOutcomeLabel = 'PARTIAL';
        rowBadgeVariant = 'partial';
      }

      let predActualText = 'Not Hypothesized';
      if (d.predicted !== undefined && d.actual !== undefined) {
        const matchLabel = d.matched ? 'MATCH' : 'MISMATCH';
        predActualText = `Hypothesis: ${escapeHtml(d.predicted)} | Result: ${escapeHtml(d.actual)} [${matchLabel}]`;
      } else if (d.actual !== undefined) {
        predActualText = `Result: ${escapeHtml(d.actual)}`;
      }

      return `
        <tr>
          <td>
            <strong>#${decisionNum}</strong>
            <div style="font-size:0.75rem; opacity:0.75;">${escapeHtml(d.decisionId || `Decision ${decisionNum}`)}</div>
          </td>
          <td><code>${escapeHtml(d.choice ?? 'N/A')}</code></td>
          <td><code>${escapeHtml(d.correctChoice ?? 'N/A')}</code></td>
          <td>
            <div>${predActualText}</div>
            ${d.rationale ? `<div class="debrief-decision-rationale">${escapeHtml(d.rationale)}</div>` : ''}
          </td>
          <td>
            <span class="debrief-badge debrief-badge-${rowBadgeVariant}">[${rowOutcomeLabel}]</span>
          </td>
        </tr>
      `;
    }).join('');

    // Misconceptions
    const misconceptionsHtml = misconceptions.length > 0
      ? `<div class="debrief-misconceptions-grid">
          ${misconceptions.map(m => `
            <article class="debrief-card" tabindex="0" aria-label="Misconception: ${escapeHtml(m.label)}">
              <div class="debrief-card-meta">
                <span class="debrief-badge debrief-badge-partial">[MISCONCEPTION]</span>
                <span class="debrief-tag">TAG: ${escapeHtml(m.tag)}</span>
                <span class="debrief-hits-counter">OBSERVED HITS: ${escapeHtml(m.hits)}</span>
              </div>
              <h4 class="debrief-card-title">${escapeHtml(m.label)}</h4>
              <p class="debrief-card-desc">
                <strong>Pedagogical Remediation:</strong> ${escapeHtml(m.remediation || 'Consult theoretical chapter literature to resolve conceptual divergence.')}
              </p>
            </article>
          `).join('')}
        </div>`
      : `<p class="debrief-empty-note">No conceptual misconceptions recorded. Systematic analytical consistency demonstrated.</p>`;

    // Transfer result
    let transferBadgeLabel = 'NOT ATTEMPTED';
    let transferBadgeVariant = 'neutral';
    let transferDescription = 'No secondary transfer scenario was evaluated in this session.';
    if (transfer.attempted) {
      if (transfer.correct) {
        transferBadgeLabel = 'SUCCESS';
        transferBadgeVariant = 'success';
        transferDescription = 'Secondary scenario resolved successfully. Conceptual transfer demonstrated across divergent institutional or historical contexts.';
      } else {
        transferBadgeLabel = 'FAILURE';
        transferBadgeVariant = 'failure';
        transferDescription = 'Secondary scenario exposed transfer limitations. The core theoretical mechanism was not sustained in the alternative case.';
      }
    }

    // Chapters
    const chaptersHtml = chapters.length > 0
      ? `<div class="debrief-chapters-grid">
          ${chapters.map(ch => `
            <a href="${escapeHtml(ch.url)}" target="_blank" rel="noopener noreferrer" class="debrief-chapter-card" aria-label="Open chapter ${escapeHtml(ch.title)} in new tab">
              <div class="debrief-chapter-top">
                <span class="debrief-chapter-slug">${escapeHtml(ch.slug)}</span>
                <span class="debrief-chapter-arrow" aria-hidden="true">&rarr;</span>
              </div>
              <div class="debrief-chapter-title">${escapeHtml(ch.title)}</div>
            </a>
          `).join('')}
        </div>`
      : `<p class="debrief-empty-note">No curriculum chapter bindings registered for ${escapeHtml(labId)}.</p>`;

    return `
      <section class="debrief-panel" role="region" aria-label="Educational Debrief and Performance Analysis">
        <header class="debrief-header">
          <div class="debrief-title-block">
            <h2 class="debrief-title">DECISION LAB DEBRIEF · ${escapeHtml(labId.toUpperCase())}</h2>
            <p class="debrief-subtitle">Pedagogical Evaluation and Concept Mastery Audit</p>
          </div>
          <div class="debrief-score-summary">
            <div class="debrief-stars-row" aria-label="Performance Stars: ${stars} of 3">
              ${starIcons}
              <span class="debrief-stars-text">${stars} / 3 STARS</span>
            </div>
            <div class="debrief-score-metric">
              <span class="debrief-score-num">${masteryScore}%</span>
              <span class="debrief-badge debrief-badge-${masteryBadgeVariant}">[${masteryLabel}]</span>
            </div>
          </div>
        </header>

        <div class="debrief-section">
          <h3 class="debrief-section-heading">DECISION RECORD</h3>
          <div class="debrief-table-scroll">
            <table class="debrief-table" role="table">
              <thead>
                <tr>
                  <th scope="col">Case</th>
                  <th scope="col">Choice</th>
                  <th scope="col">Benchmark</th>
                  <th scope="col">Hypothesis Alignment</th>
                  <th scope="col">Outcome</th>
                </tr>
              </thead>
              <tbody>
                ${decisionRows || '<tr><td colspan="5" style="text-align:center; padding:16px;">No decisions logged.</td></tr>'}
              </tbody>
            </table>
          </div>
        </div>

        <div class="debrief-section">
          <h3 class="debrief-section-heading">CONCEPTUAL REMEDIATION</h3>
          ${misconceptionsHtml}
        </div>

        <div class="debrief-section">
          <h3 class="debrief-section-heading">TRANSFER SCENARIO EVALUATION</h3>
          <div class="debrief-transfer-card">
            <div class="debrief-transfer-header">
              <span class="debrief-badge debrief-badge-${transferBadgeVariant}">[${transferBadgeLabel}]</span>
              <span style="font-size:0.82rem; font-weight:700;">CROSS-DOMAIN APPLICATION</span>
            </div>
            <p class="debrief-card-desc">${escapeHtml(transferDescription)}</p>
          </div>
        </div>

        <div class="debrief-section">
          <h3 class="debrief-section-heading">CURRICULUM REFERENCES</h3>
          ${chaptersHtml}
        </div>
      </section>
    `;
  }

  /**
   * Renders HTML into target container.
   * @param {HTMLElement|string} [container]
   * @param {Object} [report]
   * @returns {string} Rendered HTML string
   */
  render(container = this.container, report = this.report) {
    const target = typeof container === 'string' && typeof document !== 'undefined'
      ? document.querySelector(container)
      : container;
    const html = this.getHtml(report);
    if (target && 'innerHTML' in target) {
      target.innerHTML = html;
    }
    return html;
  }
}

/**
 * Functional entry point for rendering debrief panel.
 * @param {HTMLElement|string} container
 * @param {Object} report
 * @returns {DebriefPanel}
 */
export function renderDebrief(container, report) {
  return new DebriefPanel(container, report);
}

export default DebriefPanel;
