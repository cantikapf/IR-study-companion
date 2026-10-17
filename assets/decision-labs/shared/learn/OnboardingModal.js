/**
 * OnboardingModal — Universal interactive operational guide & tutorial component.
 * Conforms to the Educational Design Bible contract and CSS token scopes.
 */

export class OnboardingModal {
  /**
   * @param {Object} config
   * @param {string} config.labId - e.g. 'lab-01'
   * @param {string} config.role - Player operational identity
   * @param {string} config.objective - What player is trying to achieve
   * @param {Array<{ step: string, title: string, desc: string }>} config.steps - 3-step loop
   * @param {Array<{ key: string, label: string }>} config.controls - Hotkeys & mouse interactions
   * @param {Function} [config.onStart] - Callback when player dismisses onboarding
   */
  constructor(config) {
    this.config = Object.assign({
      labId: 'lab-01',
      role: 'Operational Commander',
      objective: 'Master curriculum concepts through tactical decision making.',
      steps: [
        { step: '1', title: 'HYPOTHESIZE & PREDICT', desc: 'Commit to an analytical expectation before acting. This tests your understanding of the underlying causal mechanism.' },
        { step: '2', title: 'EXECUTE STRATEGIC ACTION', desc: 'Deploy state power, diplomatic concessions, or crisis maneuvers. Watch the simulated system react in real time.' },
        { step: '3', title: 'AUDIT & MASTER', desc: 'Inspect real-world academic feedback, correct theoretical misconceptions, and solve a historical transfer dilemma.' }
      ],
      controls: [
        { key: '1, 2, 3', label: 'Select tactical options & answers' },
        { key: 'SPACE / ENTER', label: 'Advance dialog & confirm choices' },
        { key: 'TAB', label: 'Toggle operational side rail' },
        { key: 'M', label: 'Toggle synthesizer audio' }
      ],
      onStart: () => {}
    }, config);

    this.isOpen = false;
    this.modalEl = null;
    this.injectStyles();
    this.buildDOM();
    this.bindEvents();
  }

  injectStyles() {
    if (document.getElementById('onboarding-modal-styles')) return;

    const style = document.createElement('style');
    style.id = 'onboarding-modal-styles';
    style.textContent = `
      .ob-backdrop {
        position: fixed;
        inset: 0;
        background: rgba(4, 7, 17, 0.88);
        backdrop-filter: blur(8px);
        z-index: 10000;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 16px;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        font-family: var(--font-display, 'Chakra Petch', sans-serif);
      }

      .ob-backdrop.active {
        opacity: 1;
        pointer-events: auto;
      }

      .ob-card {
        background: var(--panel, #080d1a);
        border: 2px solid var(--border, #1e293b);
        border-radius: 8px;
        width: 100%;
        max-width: 680px;
        max-height: 90vh;
        overflow-y: auto;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 30px color-mix(in srgb, var(--accent, #06b6d4) 15%, transparent);
        display: flex;
        flex-direction: column;
        transform: scale(0.96) translateY(8px);
        transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      }

      .ob-backdrop.active .ob-card {
        transform: scale(1) translateY(0);
      }

      .ob-header {
        background: color-mix(in srgb, var(--bg-void, #040711) 60%, var(--panel, #080d1a));
        border-bottom: 1px solid var(--border, #1e293b);
        padding: 16px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }

      .ob-kicker {
        font-family: var(--font-mono, monospace);
        font-size: 0.72rem;
        color: var(--accent, #06b6d4);
        letter-spacing: 0.1em;
        text-transform: uppercase;
        font-weight: 700;
      }

      .ob-title {
        font-size: 1.25rem;
        font-weight: 800;
        color: var(--text, #f8fafc);
        text-transform: uppercase;
        margin-top: 2px;
      }

      .ob-close-btn {
        background: transparent;
        border: 1px solid var(--border, #1e293b);
        color: var(--text, #f8fafc);
        width: 32px;
        height: 32px;
        border-radius: 4px;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: var(--font-mono, monospace);
        font-size: 1.1rem;
        transition: all 0.15s ease;
      }

      .ob-close-btn:hover {
        background: var(--accent, #06b6d4);
        color: var(--bg-void, #040711);
        border-color: var(--accent, #06b6d4);
      }

      .ob-body {
        padding: 20px;
        display: flex;
        flex-direction: column;
        gap: 16px;
      }

      .ob-role-box {
        background: color-mix(in srgb, var(--bg-void, #040711) 80%, var(--panel, #080d1a));
        border-left: 4px solid var(--accent, #06b6d4);
        padding: 12px 14px;
        border-radius: 3px;
        display: flex;
        flex-direction: column;
        gap: 4px;
      }

      .ob-role-label {
        font-family: var(--font-mono, monospace);
        font-size: 0.68rem;
        font-weight: 800;
        color: var(--accent-2, #f59e0b);
        letter-spacing: 0.08em;
      }

      .ob-role-text {
        font-size: 0.92rem;
        font-weight: 700;
        color: var(--text, #f8fafc);
        line-height: 1.35;
      }

      .ob-objective-text {
        font-size: 0.82rem;
        color: var(--text, #f8fafc);
        opacity: 0.85;
        line-height: 1.4;
      }

      .ob-section-title {
        font-size: 0.76rem;
        font-weight: 800;
        letter-spacing: 0.08em;
        color: var(--accent, #06b6d4);
        text-transform: uppercase;
        border-bottom: 1px solid var(--border, #1e293b);
        padding-bottom: 4px;
      }

      .ob-steps-grid {
        display: flex;
        flex-direction: column;
        gap: 10px;
      }

      .ob-step-card {
        background: color-mix(in srgb, var(--bg-void, #040711) 60%, var(--panel, #080d1a));
        border: 1px solid var(--border, #1e293b);
        border-radius: 4px;
        padding: 10px 14px;
        display: flex;
        gap: 14px;
        align-items: flex-start;
      }

      .ob-step-num {
        width: 26px;
        height: 26px;
        border-radius: 50%;
        background: color-mix(in srgb, var(--accent, #06b6d4) 20%, transparent);
        border: 1.5px solid var(--accent, #06b6d4);
        color: var(--accent, #06b6d4);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: var(--font-mono, monospace);
        font-size: 0.82rem;
        font-weight: 800;
        flex-shrink: 0;
      }

      .ob-step-meta {
        display: flex;
        flex-direction: column;
        gap: 2px;
      }

      .ob-step-title {
        font-size: 0.85rem;
        font-weight: 800;
        color: var(--text, #f8fafc);
        text-transform: uppercase;
      }

      .ob-step-desc {
        font-size: 0.78rem;
        color: var(--text, #f8fafc);
        opacity: 0.85;
        line-height: 1.4;
      }

      .ob-controls-row {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 8px;
      }

      @media (max-width: 600px) {
        .ob-controls-row {
          grid-template-columns: 1fr;
        }
      }

      .ob-ctrl-pill {
        background: color-mix(in srgb, var(--bg-void, #040711) 70%, var(--panel, #080d1a));
        border: 1px solid var(--border, #1e293b);
        border-radius: 4px;
        padding: 6px 10px;
        display: flex;
        align-items: center;
        gap: 8px;
      }

      .ob-key-badge {
        font-family: var(--font-mono, monospace);
        font-size: 0.72rem;
        font-weight: 800;
        background: var(--panel, #080d1a);
        border: 1px solid var(--accent, #06b6d4);
        color: var(--accent, #06b6d4);
        padding: 2px 6px;
        border-radius: 3px;
        white-space: nowrap;
      }

      .ob-key-desc {
        font-size: 0.74rem;
        color: var(--text, #f8fafc);
        opacity: 0.9;
        line-height: 1.25;
      }

      .ob-footer {
        background: color-mix(in srgb, var(--bg-void, #040711) 60%, var(--panel, #080d1a));
        border-top: 1px solid var(--border, #1e293b);
        padding: 14px 20px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        gap: 12px;
      }

      .ob-start-btn {
        background: var(--accent, #06b6d4);
        color: var(--bg-void, #040711);
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        font-family: var(--font-display, 'Chakra Petch', sans-serif);
        font-size: 0.9rem;
        font-weight: 800;
        text-transform: uppercase;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
        box-shadow: 0 4px 15px color-mix(in srgb, var(--accent, #06b6d4) 40%, transparent);
        transition: all 0.15s ease;
      }

      .ob-start-btn:hover {
        filter: brightness(1.15);
        transform: translateY(-1px);
      }
    `;
    document.head.appendChild(style);
  }

  buildDOM() {
    this.modalEl = document.createElement('div');
    this.modalEl.className = 'ob-backdrop';
    this.modalEl.id = 'onboardingModalBackdrop';
    this.modalEl.setAttribute('role', 'dialog');
    this.modalEl.setAttribute('aria-modal', 'true');
    this.modalEl.setAttribute('aria-labelledby', 'obTitle');

    const stepsHTML = this.config.steps.map(s => `
      <div class="ob-step-card">
        <div class="ob-step-num">${s.step}</div>
        <div class="ob-step-meta">
          <div class="ob-step-title">${s.title}</div>
          <div class="ob-step-desc">${s.desc}</div>
        </div>
      </div>
    `).join('');

    const controlsHTML = this.config.controls.map(c => `
      <div class="ob-ctrl-pill">
        <span class="ob-key-badge">${c.key}</span>
        <span class="ob-key-desc">${c.label}</span>
      </div>
    `).join('');

    this.modalEl.innerHTML = `
      <div class="ob-card">
        <div class="ob-header">
          <div>
            <div class="ob-kicker">OPERATIONAL FIELD MANUAL · ${this.config.labId.toUpperCase()}</div>
            <h2 class="ob-title" id="obTitle">Mission Onboarding Protocol</h2>
          </div>
          <button class="ob-close-btn" id="obBtnClose" aria-label="Close Manual">&times;</button>
        </div>

        <div class="ob-body">
          <div class="ob-role-box">
            <span class="ob-role-label">YOUR OPERATIONAL ASSIGNMENT:</span>
            <div class="ob-role-text">${this.config.role}</div>
            <div class="ob-objective-text">${this.config.objective}</div>
          </div>

          <div class="ob-section-title">THE 3-STEP DECISION LOOP</div>
          <div class="ob-steps-grid">
            ${stepsHTML}
          </div>

          <div class="ob-section-title">TACTICAL COMMAND SHORTCUTS</div>
          <div class="ob-controls-row">
            ${controlsHTML}
          </div>
        </div>

        <div class="ob-footer">
          <button class="ob-start-btn" id="obBtnStart">
            <span>BEGIN MISSION</span>
            <span style="font-family:var(--font-mono, monospace); font-size:0.75rem; opacity:0.8;">[SPACE]</span>
          </button>
        </div>
      </div>
    `;

    document.body.appendChild(this.modalEl);
  }

  bindEvents() {
    const btnClose = this.modalEl.querySelector('#obBtnClose');
    const btnStart = this.modalEl.querySelector('#obBtnStart');

    if (btnClose) btnClose.onclick = () => this.close();
    if (btnStart) btnStart.onclick = () => this.start();

    // Backdrop click dismisses
    this.modalEl.onclick = (e) => {
      if (e.target === this.modalEl) this.close();
    };

    // Keyboard bindings for onboarding
    window.addEventListener('keydown', (e) => {
      if (!this.isOpen) return;

      if (e.key === 'Escape') {
        e.preventDefault();
        this.close();
      } else if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.start();
      }
    });
  }

  open() {
    this.isOpen = true;
    this.modalEl.classList.add('active');
  }

  close() {
    this.isOpen = false;
    this.modalEl.classList.remove('active');
  }

  start() {
    this.close();
    if (typeof this.config.onStart === 'function') {
      this.config.onStart();
    }
  }
}
