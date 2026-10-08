---
layout: default
title: IR Study Companion — Master International Relations with Rigor & Clarity
permalink: /
---

<style>
  /* ==========================================================================
     Homepage Editorial & Motion Graphic Styles
     ========================================================================== */
  .home-hero-split {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 3rem;
    align-items: center;
    margin-bottom: 3.5rem;
  }

  .home-hero-text {
    max-width: 650px;
  }

  /* Motion graphic: animated editorial globe */
  .hero-motion-graphic {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    position: relative;
  }

  .motion-globe {
    width: 100%;
    max-width: 440px;
    height: auto;
    display: block;
    filter: drop-shadow(0 10px 25px rgba(0, 0, 0, 0.04));
  }

  .motion-caption {
    text-align: center;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .motion-caption-label {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.6875rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--lms-ink-tertiary);
  }

  .motion-caption-title {
    font-family: Georgia, 'Newsreader', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: var(--lms-ink-secondary);
  }

  .cxg-route {
    stroke-dasharray: 1 7;
    opacity: 0.75;
    animation: cxg-dash 22s linear infinite;
  }
  .cxg-route.route-crimson { stroke: #e11d48; }
  .cxg-route.route-gold { stroke: #d97706; }
  .cxg-route.route-oxford { stroke: #1e3a8a; }

  .cxg-node {
    animation: cxg-pulse 3.2s ease-in-out infinite;
  }
  .cxg-node:nth-of-type(2n) { animation-delay: 1.1s; }
  .cxg-node:nth-of-type(3n) { animation-delay: 2.2s; }

  .cxg-orbit {
    transform-origin: 260px 268px;
    animation: cxg-spin 80s linear infinite;
  }
  .cxg-sat {
    fill: #d97706;
    animation: cxg-pulse 3.2s ease-in-out infinite;
  }

  @keyframes cxg-dash { to { stroke-dashoffset: -240; } }
  @keyframes cxg-pulse {
    0%, 100% { opacity: 0.45; }
    50% { opacity: 1; }
  }
  @keyframes cxg-spin { to { transform: rotate(360deg); } }

  @media (prefers-reduced-motion: reduce) {
    .cxg-route, .cxg-node, .cxg-orbit, .cxg-sat { animation: none; }
  }

  /* ==========================================================================
     Curriculum Explorer (ReUI cascader columns + deep-search adaptation)
     ========================================================================== */
  .explorer {
    margin-bottom: 4.5rem;
  }

  .explorer-shell {
    display: grid;
    grid-template-columns: 260px 1fr;
    background: var(--lms-surface);
    border: 1px solid var(--lms-border-strong);
    border-radius: var(--lms-radius-lg);
    box-shadow: var(--lms-shadow-md);
    overflow: hidden;
  }

  .explorer-side {
    border-right: 1px solid var(--lms-hairline);
    background: var(--lms-subtle);
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .explorer-search {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--lms-surface);
    border: 1px solid var(--lms-border-strong);
    border-radius: var(--lms-radius-sm);
    padding: 0.55rem 0.75rem;
    color: var(--lms-ink-tertiary);
  }

  .explorer-search:focus-within {
    border-color: #1e3a8a;
  }

  .explorer-search svg { flex: none; }

  .explorer-search input {
    border: none;
    outline: none;
    background: transparent;
    width: 100%;
    font-size: 0.85rem;
    color: var(--lms-ink-primary);
    font-family: inherit;
  }

  .cx-filters {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .cx-filter {
    text-align: left;
    border: none;
    background: transparent;
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.04em;
    color: var(--lms-ink-secondary);
    padding: 0.5rem 0.7rem;
    border-radius: var(--lms-radius-sm);
    cursor: pointer;
    transition: background 0.15s ease, color 0.15s ease;
  }

  .cx-filter:hover {
    background: var(--lms-hover);
    color: var(--lms-ink-primary);
  }

  .cx-filter.is-on {
    background: var(--lms-ink-primary);
    color: var(--lms-canvas);
  }

  .explorer-hint {
    margin-top: auto;
    font-size: 0.75rem;
    color: var(--lms-ink-tertiary);
    line-height: 1.5;
    border-top: 1px solid var(--lms-hairline);
    padding-top: 0.85rem;
  }

  .explorer-columns {
    display: grid;
    grid-template-columns: 280px 1fr;
    min-height: 440px;
  }

  .cx-col {
    overflow-y: auto;
    max-height: 500px;
  }

  .cx-col-modules {
    border-right: 1px solid var(--lms-hairline);
    padding: 0.6rem;
  }

  .cx-series-label {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--lms-ink-tertiary);
    padding: 0.65rem 0.7rem 0.25rem;
  }

  .cx-mod {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    width: 100%;
    text-align: left;
    border: none;
    background: transparent;
    padding: 0.55rem 0.7rem;
    border-radius: var(--lms-radius-sm);
    cursor: pointer;
    font-family: inherit;
    transition: background 0.15s ease;
  }

  .cx-mod:hover {
    background: var(--lms-hover);
  }

  .cx-mod.is-on {
    background: var(--lms-subtle);
    box-shadow: inset 3px 0 0 #1e3a8a;
  }

  .cx-mod-num {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.6875rem;
    font-weight: 600;
    color: var(--lms-ink-tertiary);
    border: 1px solid var(--lms-hairline);
    border-radius: var(--lms-radius-sm);
    padding: 0.1rem 0.35rem;
    flex: none;
  }

  .cx-mod.is-on .cx-mod-num {
    color: #1e3a8a;
    border-color: #1e3a8a;
  }

  .cx-mod-name {
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--lms-ink-primary);
    line-height: 1.35;
    flex: 1;
  }

  .cx-mod-count {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.6875rem;
    color: var(--lms-ink-tertiary);
    flex: none;
  }

  .cx-panel {
    padding: 1.25rem 1.5rem;
  }

  .cx-panel-head {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 1rem;
    padding-bottom: 0.85rem;
    margin-bottom: 0.65rem;
    border-bottom: 1px solid var(--lms-hairline);
  }

  .cx-panel-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--lms-ink-primary);
  }

  .cx-panel-overview {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #1e3a8a;
    text-decoration: none;
    white-space: nowrap;
    font-weight: 600;
  }

  .cx-panel-overview:hover {
    text-decoration: underline;
  }

  .cx-lesson {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.55rem 0.5rem;
    border-bottom: 1px solid var(--lms-hairline);
    text-decoration: none;
    border-radius: var(--lms-radius-sm);
    transition: background 0.15s ease;
  }

  .cx-lesson:last-child {
    border-bottom: none;
  }

  .cx-lesson:hover {
    background: var(--lms-hover);
  }

  .cx-lesson-title {
    font-size: 0.9rem;
    color: var(--lms-ink-primary);
    flex: 1;
    line-height: 1.4;
  }

  .cx-lesson:hover .cx-lesson-title {
    color: #1e3a8a;
  }

  .cx-lesson-path {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.6875rem;
    color: var(--lms-ink-tertiary);
    white-space: nowrap;
  }

  .cx-video-chip {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: #e11d48;
    background: rgba(225, 29, 72, 0.1);
    border-radius: 4px;
    padding: 0.12rem 0.4rem;
    flex: none;
    margin-left: 0.35rem;
  }

  .cx-empty {
    padding: 3rem 1.5rem;
    text-align: center;
    color: var(--lms-ink-tertiary);
    font-size: 0.9rem;
  }

  .cx-empty strong {
    color: var(--lms-ink-primary);
  }

  /* ==========================================================================
     Diplomatic Labs Split Layout
     ========================================================================== */
  .labs-showcase-split {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 2rem;
    margin-bottom: 4rem;
  }

  .playable-sandbox {
    background: var(--lms-surface);
    border: 1px solid var(--lms-border-strong);
    border-radius: var(--lms-radius-lg);
    padding: 1.75rem;
    box-shadow: var(--lms-shadow-md);
  }

  .sandbox-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 0.85rem;
    border-bottom: 1px solid var(--lms-hairline);
    margin-bottom: 1.25rem;
  }

  .sandbox-tag {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #1e3a8a;
  }

  .sandbox-status-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.72rem;
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    color: #059669;
    background: rgba(5, 150, 105, 0.1);
    padding: 0.2rem 0.5rem;
    border-radius: var(--lms-radius-sm);
  }

  .sandbox-title {
    font-size: 1.25rem;
    font-weight: 750;
    color: var(--lms-ink-primary);
    margin: 0 0 0.5rem;
  }

  .sandbox-prompt {
    font-size: 0.875rem;
    color: var(--lms-ink-secondary);
    line-height: 1.55;
    margin-bottom: 1.25rem;
  }

  .sandbox-duel-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1.25rem;
  }

  .duel-card {
    background: var(--lms-subtle);
    border: 1px solid var(--lms-hairline);
    border-radius: var(--lms-radius-md);
    padding: 1rem;
    text-align: center;
  }

  .duel-role {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--lms-ink-tertiary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .duel-score {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 2.25rem;
    font-weight: 700;
    color: var(--lms-ink-primary);
    margin: 0.35rem 0;
  }

  .duel-actions {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.75rem;
  }

  .btn-sim {
    flex: 1;
    padding: 0.5rem;
    border-radius: var(--lms-radius-sm);
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    border: 1px solid transparent;
    transition: all 0.15s ease;
  }

  .btn-sim-coop {
    background: #059669;
    color: #ffffff;
  }
  .btn-sim-coop:hover { opacity: 0.9; }

  .btn-sim-defect {
    background: #e11d48;
    color: #ffffff;
  }
  .btn-sim-defect:hover { opacity: 0.9; }

  .sandbox-log {
    background: var(--lms-subtle);
    border: 1px solid var(--lms-hairline);
    border-radius: var(--lms-radius-sm);
    padding: 0.75rem 1rem;
    height: 90px;
    overflow-y: auto;
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--lms-ink-secondary);
    line-height: 1.5;
  }

  .sandbox-log-line {
    border-bottom: 1px dashed var(--lms-hairline);
    padding-bottom: 0.25rem;
    margin-bottom: 0.25rem;
  }

  .labs-compact-grid {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .lab-card-sm {
    background: var(--lms-surface);
    border: 1px solid var(--lms-border-strong);
    border-radius: var(--lms-radius-md);
    padding: 1.25rem;
    box-shadow: var(--lms-shadow-sm);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.15s ease, border-color 0.15s ease;
  }

  .lab-card-sm:hover {
    border-color: #1e3a8a;
    transform: translateY(-2px);
    box-shadow: var(--lms-shadow-md);
  }

  .lab-card-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--lms-ink-primary);
    margin: 0.25rem 0 0.35rem;
  }

  .lab-card-desc {
    font-size: 0.85rem;
    color: var(--lms-ink-secondary);
    line-height: 1.45;
    margin-bottom: 0.75rem;
  }

  .lab-card-link {
    font-size: 0.85rem;
    font-weight: 700;
    color: #1e3a8a;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
  }

  .lab-card-link:hover {
    text-decoration: underline;
  }

  @media (max-width: 960px) {
    .home-hero-split {
      grid-template-columns: 1fr;
      gap: 2.5rem;
    }
    .hero-motion-graphic .motion-globe {
      max-width: 320px;
    }
    .explorer-shell {
      grid-template-columns: 1fr;
    }
    .explorer-side {
      border-right: none;
      border-bottom: 1px solid var(--lms-hairline);
    }
    .explorer-columns {
      grid-template-columns: 1fr;
      min-height: 0;
    }
    .cx-col-modules {
      border-right: none;
      border-bottom: 1px solid var(--lms-hairline);
      max-height: 240px;
    }
    .labs-showcase-split {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="home-viewport">

  <!-- Editorial Hero with Animated Motion Graphic -->
  <header class="home-hero-split">
    <div class="home-hero-text">
      <div class="home-eyebrow">The Structured Open-Access Curriculum in International Relations</div>
      <h1 class="home-title">Understanding Global Politics with <em>Rigor</em>, <em>Structure</em>, and <em>Clarity</em></h1>
      <p class="home-description">
        An academically rigorous self-study companion covering foundational paradigms, geopolitical history, international political economy, and diplomatic statecraft. Grounded in active recall checkpoints and interactive decision-making labs.
      </p>
      <div style="margin-top: 2rem; display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="#explore" class="sync-btn sync-btn-primary" style="text-decoration: none;">
          Explore Curriculum ➔
        </a>
        <a href="#simulations" class="sync-btn sync-btn-secondary" style="text-decoration: none;">
          Try Decision Lab
        </a>
        <a href="{{ site.baseurl }}/glossary.html" class="sync-btn sync-btn-secondary" style="text-decoration: none;">
          Glossary (122 Terms)
        </a>
      </div>
    </div>

    <!-- Motion Graphic: Animated Wireframe Globe & Diplomatic Routes -->
    <div class="hero-motion-graphic" aria-hidden="true">
      <svg class="motion-globe" viewBox="0 0 520 536" role="img" aria-label="Animated wireframe globe with animated diplomatic routes between nations">
        <defs>
          <clipPath id="mgClip"><circle cx="260" cy="268" r="208"/></clipPath>
        </defs>
        <!-- Rotating orbit ring -->
        <g class="cxg-orbit">
          <ellipse cx="260" cy="268" rx="242" ry="242" fill="none" stroke="var(--lms-border-strong)" stroke-width="1" stroke-dasharray="1 6" opacity="0.65"/>
          <circle class="cxg-sat" cx="502" cy="268" r="3.5"/>
        </g>
        <!-- Globe graticule -->
        <g clip-path="url(#mgClip)" fill="none" stroke="#1e3a8a" stroke-width="1.25" opacity="0.25">
          <ellipse cx="260" cy="123.9" rx="104.0" ry="31.2"/>
          <ellipse cx="260" cy="184.8" rx="180.1" ry="54.0"/>
          <ellipse cx="260" cy="268.0" rx="208.0" ry="62.4"/>
          <ellipse cx="260" cy="351.2" rx="180.1" ry="54.0"/>
          <ellipse cx="260" cy="412.1" rx="104.0" ry="31.2"/>
          <ellipse cx="260" cy="268" rx="41.6" ry="208.0"/>
          <ellipse cx="260" cy="268" rx="93.6" ry="208.0"/>
          <ellipse cx="260" cy="268" rx="149.8" ry="208.0"/>
          <ellipse cx="260" cy="268" rx="208.0" ry="208.0"/>
        </g>
        <circle cx="260" cy="268" r="208" fill="none" stroke="#1e3a8a" stroke-width="2" opacity="0.55"/>
        <!-- Animated diplomatic routes -->
        <g fill="none" stroke-linecap="round" stroke-width="2">
          <path class="cxg-route route-crimson" d="M120,250 Q240,90 365,175"/>
          <path class="cxg-route route-gold" d="M205,130 Q130,300 155,385"/>
          <path class="cxg-route route-crimson" d="M365,175 Q385,265 330,345"/>
          <path class="cxg-route route-oxford" d="M155,385 Q205,320 262,262"/>
          <path class="cxg-route route-gold" d="M330,345 Q235,300 120,250"/>
        </g>
        <!-- Pulsing capital nodes -->
        <g fill="#1e3a8a" stroke="var(--lms-surface)" stroke-width="1.6">
          <circle class="cxg-node" cx="120" cy="250" r="4.5"/>
          <circle class="cxg-node" cx="205" cy="130" r="4.5"/>
          <circle class="cxg-node" cx="365" cy="175" r="4.5"/>
          <circle class="cxg-node" cx="330" cy="345" r="4.5"/>
          <circle class="cxg-node" cx="155" cy="385" r="4.5"/>
          <circle class="cxg-node" cx="262" cy="262" r="4.5"/>
        </g>
      </svg>
      <div class="motion-caption">
        <span class="motion-caption-label">170+ nations &bull; 18 modules &bull; one discipline</span>
        <span class="motion-caption-title">The study of how the world negotiates itself</span>
      </div>
    </div>
  </header>

  <!-- Command Center: Dynamic Resume Learning Card -->
  <div class="resume-card" id="home-resume-widget">
    <div class="resume-content">
      <div class="resume-header-meta">
        <span class="resume-tag" id="resume-status-tag">In Progress</span>
        <span class="tabular-number" id="resume-time-est" style="color: var(--lms-ink-tertiary);">Est. 12 min</span>
      </div>
      <div class="resume-lesson-title" id="resume-lesson-title">Module 010 • Study of International Relations</div>
      <div class="resume-progress-container">
        <div class="resume-progress-track">
          <div class="resume-progress-fill" id="resume-fill-bar" style="width: 15%;"></div>
        </div>
        <div class="resume-progress-caption" id="resume-progress-caption">
          <span class="tabular-number" id="resume-stat-num">0</span> of <span class="tabular-number">157</span> lessons completed (<span class="tabular-number" id="resume-pct">0%</span>)
        </div>
      </div>
    </div>
    <a href="{{ site.baseurl }}/study-of-international-relations.html" class="resume-action-btn" id="resume-target-btn">
      <span id="resume-btn-label">Start Learning</span> ➔
    </a>
  </div>

  <!-- Curriculum Metrics Strip -->
  <div class="metrics-strip">
    <div class="metric-cell">
      <span class="metric-value tabular-number">18</span>
      <span class="metric-label">Core Modules</span>
    </div>
    <div class="metric-cell">
      <span class="metric-value tabular-number">157</span>
      <span class="metric-label">Structured Lessons</span>
    </div>
    <div class="metric-cell">
      <span class="metric-value tabular-number">156</span>
      <span class="metric-label">Active Checkpoints</span>
    </div>
    <div class="metric-cell">
      <span class="metric-value tabular-number">10</span>
      <span class="metric-label">Simulation Labs</span>
    </div>
  </div>

  <!-- Curriculum Explorer (ReUI cascader columns + deep search) -->
  <section class="explorer" id="explore">
    <div class="home-section-header">
      <div>
        <div class="home-eyebrow">Explore The Full Library</div>
        <h2 class="home-section-title">Every Module. Every Lesson. One Click Away.</h2>
        <div class="home-section-subtitle">Browse 157 lessons across 18 modules, or search any topic to jump directly into the reading.</div>
      </div>
    </div>

    <div class="explorer-shell">
      <aside class="explorer-side">
        <label class="explorer-search">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width:14px;height:14px"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
          <input id="cx-search" type="search" placeholder="Search 157 lessons..." aria-label="Search lessons" autocomplete="off">
        </label>
        <div class="cx-filters" id="cx-filters" aria-label="Filter by series"></div>
        <p class="explorer-hint">Pick a module on the left to browse its curriculum. Click any lesson to start reading &mdash; progress is saved automatically.</p>
      </aside>
      <div class="explorer-columns">
        <nav class="cx-col cx-col-modules" id="cx-modules" aria-label="Modules List"></nav>
        <div class="cx-col" id="cx-lessons" aria-label="Lessons List"></div>
      </div>
    </div>
  </section>

  <!-- Interactive Diplomatic Decision Labs -->
  <section class="labs-section" id="simulations">
    <div class="home-section-header">
      <div>
        <h2 class="home-section-title">Interactive Diplomatic Decision Labs</h2>
        <div class="home-section-subtitle">Test theoretical paradigms against realistic crisis constraints in zero-dependency sandboxes</div>
      </div>
    </div>

    <div class="labs-showcase-split">
      <!-- Live Playable Sandbox: Prisoner's Dilemma -->
      <div class="playable-sandbox" id="game-theory-sim">
        <div class="sandbox-header">
          <span class="sandbox-tag"><i class="fa fa-gamepad"></i> Interactive Lab 02 &bull; Game Theory</span>
          <span class="sandbox-status-chip">&bull; Live Simulation Sandbox</span>
        </div>

        <h3 class="sandbox-title">The Prisoner's Dilemma Strategic Arena</h3>
        <p class="sandbox-prompt">
          You represent State A. State B is an AI opponent playing Axelrod's <strong>'Tit-for-Tat'</strong> strategy. Will you seek mutual disarmament (Cooperate) or clandestinely militarize (Defect)?
        </p>

        <div class="sandbox-duel-grid">
          <div class="duel-card">
            <span class="duel-role">Your Payoff (State A)</span>
            <div class="duel-score" id="gt-score-a">0</div>
            <div class="duel-actions">
              <button type="button" class="btn-sim btn-sim-coop" onclick="playGameTheory('cooperate')">🤝 Cooperate</button>
              <button type="button" class="btn-sim btn-sim-defect" onclick="playGameTheory('defect')">⚔️ Defect</button>
            </div>
          </div>

          <div class="duel-card">
            <span class="duel-role">Opponent (State B AI)</span>
            <div class="duel-score" id="gt-score-b" style="color: #1e3a8a;">0</div>
            <div style="font-size: 0.775rem; color: var(--lms-ink-tertiary); margin-top: 0.85rem;" id="gt-opp-status">
              Waiting for move...
            </div>
          </div>
        </div>

        <div class="sandbox-log" id="gt-log" aria-live="polite">
          <div class="sandbox-log-line">&gt; Simulation initialized. Opponent memory cleared. Choose your strategy.</div>
        </div>
      </div>

      <!-- 3 Highlighted Labs from the Catalog of 10 -->
      <div class="labs-compact-grid">
        <article class="lab-card-sm">
          <div>
            <div class="sandbox-tag" style="margin-bottom: 0.35rem;">Lab 01 &bull; FPA Model</div>
            <h4 class="lab-card-title">Crisis Escalation Matrix</h4>
            <p class="lab-card-desc">Simulate Graham Allison's bureaucratic models in a naval standoff. Balance brinkmanship against accidental war.</p>
          </div>
          <a href="{{ site.baseurl }}/models-fpdm.html#crisis-sim" class="lab-card-link">Launch Simulator ➔</a>
        </article>

        <article class="lab-card-sm">
          <div>
            <div class="sandbox-tag" style="margin-bottom: 0.35rem;">Lab 07 &bull; Law of the Sea</div>
            <h4 class="lab-card-title">UNCLOS Maritime Zone Delimiter</h4>
            <p class="lab-card-desc">Classify jurisdictional limits from Territorial Sea (12 nm) to the high seas Continental Shelf.</p>
          </div>
          <a href="{{ site.baseurl }}/law-of-the-sea.html#unclos-zones-sim" class="lab-card-link">Map Maritime Zones ➔</a>
        </article>

        <article class="lab-card-sm">
          <div>
            <div class="sandbox-tag" style="margin-bottom: 0.35rem;">Lab 05 &bull; Global Governance</div>
            <h4 class="lab-card-title">UNSC Veto Chamber</h4>
            <p class="lab-card-desc">Draft a peacekeeping resolution and survive the P5 veto gauntlet across Chapter VII enforcement.</p>
          </div>
          <a href="{{ site.baseurl }}/un-security.html#unsc-veto-sim" class="lab-card-link">Enter Chamber ➔</a>
        </article>
      </div>
    </div>
  </section>

  <!-- Master Video Companion Channel Showcase -->
  <section style="margin-bottom: 4rem;" id="video-companion">
    <div class="home-section-header">
      <div>
        <h2 class="home-section-title">Official Video Course Companion</h2>
        <div class="home-section-subtitle">Visual explainers, 10-minute master episodes, and animated concept deep-dives</div>
      </div>
    </div>
    <div style="background: var(--lms-surface); border: 1px solid var(--lms-border-strong); border-radius: var(--lms-radius-lg); padding: 2rem; display: flex; align-items: center; justify-content: space-between; gap: 2rem; flex-wrap: wrap; box-shadow: var(--lms-shadow-md);">
      <div style="flex: 1; min-width: 280px;">
        <span style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--lms-ink-tertiary);">YouTube Channel</span>
        <h3 style="font-size: 1.4rem; font-weight: 750; color: var(--lms-ink-primary); margin: 0.35rem 0 0.5rem;">@IRinANutshell</h3>
        <p style="font-size: 0.95rem; color: var(--lms-ink-secondary); line-height: 1.6; margin: 0 0 1.25rem;">
          Produced with local Kokoro-82M neural voices and rapid-fire visual beats. Watch our flagship 10-minute master episode: <em>"The Anarchy Problem — Who's in Charge of the Planet?"</em>, or explore mini-documentaries accompanying each core module.
        </p>
        <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
          <a href="https://www.youtube.com/@IRinANutshell" target="_blank" rel="noopener noreferrer" class="sync-btn sync-btn-primary" style="text-decoration: none;">
            <i class="fa fa-youtube-play" style="color: #ef4444;"></i> Visit @IRinANutshell ➔
          </a>
          <a href="{{ site.baseurl }}/glossary.html" class="sync-btn sync-btn-secondary" style="text-decoration: none;">
            <i class="fa fa-book"></i> Curated Glossary (122 Terms)
          </a>
        </div>
      </div>

      <!-- Video Thumbnail Visual Card -->
      <div style="width: 320px; background: var(--lms-subtle); border: 1px solid var(--lms-border-strong); border-radius: var(--lms-radius-md); padding: 1rem; display: flex; flex-direction: column; gap: 0.65rem;">
        <div style="width: 100%; height: 170px; border-radius: var(--lms-radius-sm); overflow: hidden; position: relative; background: #000000;">
          <img src="{{ site.baseurl }}/learning-videos/posters/IR_M01_CH030_Basic_Explanation_of_Realism_in_IR_Poster.png" alt="@IRinANutshell Video Poster" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.92;" onerror="this.src='{{ site.baseurl }}/assets/images/mindmap_chapter_010_poster.png'">
          <div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; pointer-events: none;">
            <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(239, 68, 68, 0.9); color: #ffffff; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
              <i class="fa fa-play" style="margin-left: 3px;"></i>
            </div>
          </div>
        </div>
        <div style="font-family: ui-monospace, 'JetBrains Mono', monospace; font-size: 0.75rem; color: var(--lms-ink-tertiary); display: flex; justify-content: space-between;">
          <span>CH030 &bull; Basic Realism</span>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--lms-hairline); display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; color: var(--lms-ink-tertiary);">
    <div>IR Study Companion &copy; 2026. Rigorous Open-Access Course Platform.</div>
    <div>
      <a href="https://github.com/cantikapf/IR-study-companion" target="_blank" rel="noopener noreferrer" style="color: var(--lms-ink-secondary); text-decoration: none;">GitHub</a>
    </div>
  </footer>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const siteBase = "{{ site.baseurl }}";

    // Dynamic Resume Learning Logic based on user progress in localStorage
    const chapters = [
      {% for chapter in site.chapters %}
        {% if chapter.layout != 'part' and chapter.slug %}
        { 
          slug: "{{ chapter.slug }}", 
          title: "{{ chapter.title | escape }}", 
          url: "{{ site.baseurl }}{{ chapter.url }}",
          relPath: "{{ chapter.relative_path }}"
        },
        {% endif %}
      {% endfor %}
    ];

    let completed = 0;
    let lastActive = null;

    chapters.forEach(c => {
        const isDone = localStorage.getItem('chapter_read_' + c.slug) === 'true';
        if(isDone) {
            completed++;
        } else if(!lastActive) {
            lastActive = c;
        }
    });

    const total = chapters.length || 157;
    const pct = Math.round((completed / total) * 100);

    const statNumEl = document.getElementById('resume-stat-num');
    const pctEl = document.getElementById('resume-pct');
    const fillEl = document.getElementById('resume-fill-bar');
    const lessonTitleEl = document.getElementById('resume-lesson-title');
    const targetBtnEl = document.getElementById('resume-target-btn');
    const btnLabelEl = document.getElementById('resume-btn-label');
    const statusTagEl = document.getElementById('resume-status-tag');

    if(statNumEl) statNumEl.textContent = completed;
    if(pctEl) pctEl.textContent = pct + '%';
    if(fillEl) fillEl.style.width = Math.max(pct, 4) + '%';

    if(completed > 0 && lastActive) {
        if(lessonTitleEl) lessonTitleEl.textContent = lastActive.title;
        if(targetBtnEl) targetBtnEl.href = lastActive.url;
        if(btnLabelEl) btnLabelEl.textContent = "Continue Lesson";
        if(statusTagEl) statusTagEl.textContent = "Resume Course";
    } else if (completed === total && total > 0) {
        if(lessonTitleEl) lessonTitleEl.textContent = "Curriculum Completed! Review Your Notes & Labs.";
        if(btnLabelEl) btnLabelEl.textContent = "Review Course";
        if(statusTagEl) statusTagEl.textContent = "Mastered ✓";
    }

    // ---------- Curriculum Explorer (ReUI cascader columns + deep-search adaptation) ----------
    const CX_DATA = {"series":{"01":"Foundation Series","02":"Core Discipline","03":"Applications & Method","04":"Law, Region & Society","05":"Global Architecture"},"modules":[{"num":"010","name":"Introduction To Ir","overview":{"slug":"introduction-to-international-relations","title":"Introduction To IR"},"lessons":[{"slug":"study-of-international-relations","title":"Study Of International Relations","v":true},{"slug":"globalization-and-global-politics","title":"Globalization And Global Politics","v":true},{"slug":"basic-realism","title":"Basic Explanation of Realism in IR","v":true},{"slug":"basic-liberalism","title":"Basic Explanation of Liberalism in IR","v":true},{"slug":"basic-marxism","title":"Basic Explanation of Marxism in IR","v":false},{"slug":"basic-constructivism","title":"Basic Explanation of Constructivism in IR","v":false},{"slug":"global-finance-and-global-trade-as-agendas","title":"Global Finance And Global Trade As Agendas","v":false},{"slug":"global-environment-as-agendas","title":"Global Environment As Agendas","v":false},{"slug":"global-security-issues","title":"Global Security Issues","v":false},{"slug":"regionalism-in-international-affairs","title":"Regionalism In International Affairs","v":false}]},{"num":"011","name":"Introduction To Social Science","overview":{"slug":"introduction-to-social-science","title":"Introduction To Social Science"},"lessons":[{"slug":"social-science-concept","title":"Social Science Concepts and Epistemology","v":false},{"slug":"history-social-science-role","title":"History and Its Role in Social Science","v":false},{"slug":"culture-social-science","title":"Culture and Social Science","v":false},{"slug":"state-in-society","title":"State in Society","v":false},{"slug":"politics-and-power","title":"Politics, Power, and Authority","v":false},{"slug":"understanding-social-change","title":"Understanding Social Change","v":false}]},{"num":"012","name":"Modern World History","overview":{"slug":"modern-world-history","title":"Modern World History"},"lessons":[{"slug":"history-matters","title":"Why History Matters?","v":false},{"slug":"rennaissance","title":"The Renaissance and the Reformation in Europe","v":false},{"slug":"westphalia","title":"'The Emergence of the Modern Interstate System: The Thirty Years War and Peace of Westphalia'","v":false},{"slug":"road-to-ww1","title":"The Road to the First World War","v":false},{"slug":"after-the-first-world-war","title":"After The First World War","v":false},{"slug":"great-depression","title":"The Great Depression","v":false},{"slug":"twenty-year-crisis","title":"The Twenty-Year Crisis","v":false},{"slug":"brink-ww2","title":"On the Brink of the Second World War","v":false},{"slug":"end-ww2","title":"The Ending of The Second World War","v":false},{"slug":"post-ww","title":"'The Post-War World Order'","v":false},{"slug":"bretton-woods","title":"The Rise of the Bretton Woods Institutions","v":false},{"slug":"domino-cold-war","title":"'When One Falls, They All Will Follow: The Domino Theory and the Cold War'","v":false},{"slug":"cuban-missile-crisis","title":"Cuban Missile Crisis","v":false},{"slug":"detente","title":"Détente of the 1970-1990","v":false},{"slug":"decolonization","title":"Decolonization and Development","v":false},{"slug":"birth-prc","title":"The Birth and Rise of the People’s Republic of China","v":false},{"slug":"end-cold-war","title":"The End of the Cold War","v":false},{"slug":"world-order","title":"The Post-Cold War World Order","v":false},{"slug":"us-hegemony","title":"'Challenges to US Hegemony: Rising China and Russian Resurgence'","v":false}]},{"num":"013","name":"Indonesia Political Perspective","overview":{"slug":"indonesia-political-perspective","title":"Indonesia Political Perspective"},"lessons":[{"slug":"basic-political","title":"Basic Poilitical Concepts","v":false},{"slug":"political-institution","title":"Indonesia Political Institutions, Political Party, And Interest Group","v":false},{"slug":"evolution-party","title":"The Evolution of Indonesia's Political Party System","v":false},{"slug":"civil-military","title":"Civil-Military Relations in Indonesia","v":false},{"slug":"electoral-indonesia","title":"Indonesia's Electoral Landscape","v":false},{"slug":"democracy-indonesia","title":"'Democracy In Indonesia: Decentralization'","v":false},{"slug":"women-indonesia","title":"Women In Indonesian Politics","v":false},{"slug":"religion-society","title":"Religion, Society And Politics","v":false}]},{"num":"021","name":"International Political Economy","overview":{"slug":"introduction-to-international-political-economy","title":"International Political Economy"},"lessons":[{"slug":"introduction-ipe","title":"Introduction To International Trade And Economy","v":false},{"slug":"merchantilism-liberalism","title":"'Approaches to IPE: Mercantilism vs. Liberalism'","v":false},{"slug":"constructivism-marxist","title":"'Approaches to IPE: Constructivism vs. Marxism'","v":false},{"slug":"gatt","title":"'The World Trade Organization: From GATT to Global Trade Guardian'","v":false},{"slug":"tpp-rcep","title":"'Beyond Tariffs: The Deeper Impacts of the TPP and RCEP Agreements'","v":false},{"slug":"trade-politics","title":"The Politics of Trade","v":false},{"slug":"ISI-export","title":"'From ISI to Export Orientation: How Developing Countries Navigated Trade Strategy'","v":false},{"slug":"monetary-system","title":"International Monetary System","v":false},{"slug":"exchange-rates","title":"'The Tug-of-War Over Exchange Rates: Political Interests vs. Economic Welfare'","v":false},{"slug":"neoliberalism-ipe","title":"'Neoliberalism 101: Understanding the Ideology That Dominates Global Trade'","v":false},{"slug":"neoliberalism-policy","title":"'Neoliberalism Explained: The Ideology That Transformed Modern Capitalism'","v":false}]},{"num":"022","name":"Introduction To Security Studies","overview":{"slug":"introduction-to-security-studies","title":"Introduction To Security Studies"},"lessons":[{"slug":"introduction-security","title":"Introduction To Security Studies","v":false},{"slug":"realism-security","title":"Realism In Security Studies","v":false},{"slug":"liberalism-security","title":"Liberalism In Security Studies","v":false},{"slug":"constructivism-others","title":"Constructivism And Other Approach In Security Studies","v":false},{"slug":"institution-security","title":"Institution In International Security","v":false},{"slug":"peace-operations","title":"Peace Operations","v":false},{"slug":"crime-terrorism-insurgency","title":"Crime, Terrorism, And Insurgency","v":false},{"slug":"energy-security","title":"Energy Security","v":false},{"slug":"human-security","title":"Human Security","v":false}]},{"num":"023","name":"Theories Of International Relations","overview":{"slug":"theories-of-international-relations","title":"Theories Of International Relations"},"lessons":[{"slug":"introduction-ir-theories","title":"Introduction To International Relations Theories","v":false},{"slug":"classical-realism","title":"Classical Realism","v":false},{"slug":"liberalism-ir","title":"Liberalism","v":false},{"slug":"neorealism-ir","title":"Neorealism","v":false},{"slug":"neoliberalism-ir","title":"Neoliberalism","v":false},{"slug":"dependency-theory","title":"Dependency Theory","v":false},{"slug":"constructivism-ir","title":"Constructivism","v":false},{"slug":"domestic-politics","title":"'Domestic Politics: Two Level Games'","v":false},{"slug":"feminism-ir","title":"Feminism In International Relations","v":false},{"slug":"rational-choice-theory","title":"Rational Choice Theory","v":false},{"slug":"game-theory-ir","title":"Game Theory","v":false},{"slug":"critical-theory","title":"Critical Theory","v":false}]},{"num":"031","name":"International Relations Research Method","overview":{"slug":"international-relations-research-method","title":"International Relations Research Method"},"lessons":[{"slug":"social-reserach-method","title":"Social Research Methods in International Relations","v":false},{"slug":"research-ir-study","title":"Research Method in International Relations Study","v":false},{"slug":"research-process","title":"Research Process","v":false},{"slug":"qualitative","title":"'Research Method: Qualitative'","v":false},{"slug":"quantitative","title":"'Research Method: Quantitative'","v":false},{"slug":"research-question","title":"Research Question","v":false},{"slug":"literature-review","title":"Literature Review","v":false},{"slug":"observation-method","title":"'IR Research Method: Participant Observation and Focus Group'","v":false},{"slug":"interview-survey","title":"'IR Research Methods: Elite Interviews and Survey Research'","v":false}]},{"num":"032","name":"Diplomacy And International Politics","overview":{"slug":"diplomacy-and-international-politics","title":"Diplomacy And International Politics"},"lessons":[{"slug":"intro-diplo","title":"Introduction To Diplomacy And International Politics","v":false},{"slug":"history-diplomacy","title":"History Of Diplomacy","v":false},{"slug":"modes-diplomacy","title":"Modes of Diplomacy","v":false},{"slug":"actors-diplomacy","title":"The Actors of Diplomacy","v":false},{"slug":"tools-diplomacy","title":"Tools and Instruments Of Diplomacy","v":false},{"slug":"inter-politics","title":"Understanding Issues of International Politics","v":false}]},{"num":"033","name":"Foreign Policy Analysis In International Relations","overview":{"slug":"foreign-policy-analysis-ir","title":"Foreign Policy Analysis In International Relations"},"lessons":[{"slug":"intro-fpa","title":"Introduction To Foreign Policy Analysis And Foreign Policy In International Relations","v":false},{"slug":"level-of-analysis-fpdm","title":"Level Of Analysis In Foreign Policy Decision Making","v":false},{"slug":"models-fpdm","title":"Understanding Models Of Decision Making In Foreign Policy Analysis","v":false},{"slug":"factors-fpdm","title":"Factor Affecting Foreign Policy Decision","v":false},{"slug":"public-opinion-media-fpdm","title":"Public Opinion, Media And Foreign Policy","v":false}]},{"num":"034","name":"Contemporary Issues In Global Politics","overview":{"slug":"contemporary-issues-in-global-politics","title":"Contemporary issues in global politics"},"lessons":[{"slug":"theoritical-perspective","title":"Theoretical Perspectives in Global Politics","v":false},{"slug":"poverty-development-aid","title":"Poverty, Development, and International Aid","v":false},{"slug":"failed-state","title":"Failed State And State-building Interventions","v":false},{"slug":"media-politics","title":"Alternative Media and International Politics","v":false},{"slug":"cyber-warfare","title":"Cyber Warfare","v":false},{"slug":"multiculturalism","title":"Politics Of Multiculturalism","v":false},{"slug":"political-populism","title":"Political Populism","v":false},{"slug":"natural-disaster","title":"Natural Disaster And Global Politics","v":false}]},{"num":"041","name":"Foreign Policy Of Developed Countries","overview":{"slug":"foreign-policy-of-developed-countries","title":"Foreign Policy Of Developed Countries"},"lessons":[{"slug":"history-fpa","title":"The History And Evolution Of Foreign Policy Analysis","v":false},{"slug":"economic-statecraft","title":"Economic Statecraft","v":false},{"slug":"women-foreign-policy","title":"'Women And Foreign Policy: Swedish Feminist Foreign Policy'","v":false},{"slug":"eu-foreign-policy","title":"EU Foreign Policy and Energy Security","v":false},{"slug":"australia-foreign-policy","title":"Australia Foreign Policy and Current Issues","v":false},{"slug":"us-foreign-policy","title":"U.S. Foreign Policy","v":false},{"slug":"japan-foreign-policy","title":"Japan Foreign Policy","v":false}]},{"num":"042","name":"International Law Issues And International Dispute Settlement","overview":{"slug":"international-law-issues-and-international-dispute-settlement","title":"International Law Issues And International Dispute Settlement"},"lessons":[{"slug":"basic-inter-law","title":"Basic Understanding Of International Law","v":false},{"slug":"international-treaties","title":"International Treaties","v":false},{"slug":"subjects-of-international-law","title":"The Subjects Of International Law","v":false},{"slug":"state-and-international-law","title":"State And International Law","v":false},{"slug":"io-law","title":"International Organization","v":false},{"slug":"customary-international-law","title":"Customary International Law","v":false},{"slug":"ngo-and-international-law","title":"NGO And International Law","v":false},{"slug":"territory-law","title":"Territory and International Law","v":false},{"slug":"dispute-settlement","title":"Dispute Settlement","v":false},{"slug":"law-of-the-sea","title":"The Law Of The Sea","v":false},{"slug":"international-criminal-law-and-dispute-settlement","title":"International Criminal Law And Dispute Settlement","v":false},{"slug":"international-courts-and-tribunal","title":"International Courts and Tribunal","v":false},{"slug":"the-use-of-force-in-international-law","title":"The Use Of Force In International Law","v":false},{"slug":"international-human-right-law","title":"International Human Right Law","v":false},{"slug":"international-humanitarian-law","title":"International Humanitarian Law","v":false},{"slug":"international-law-for-environmental-protection","title":"International Law For Environmental Protection","v":false}]},{"num":"043","name":"International Political Economy Of Development","overview":{"slug":"international-political-economy-of-development","title":"International Political Economy Of Development"},"lessons":[{"slug":"study-of-development","title":"Study Of Development","v":false},{"slug":"fifty-years-economic-growth","title":"Fifty Years Of Economic Growth And Development Strategy","v":false},{"slug":"inequality-development","title":"'Inequality And Development: An Overview'","v":false},{"slug":"women-economic-role","title":"Women's Economic Roles And The Development Paradigm","v":false},{"slug":"asian-model","title":"The Asian Model Of Development","v":false},{"slug":"development-in-china-india-chile-african-arab","title":"Development In China, India, Chile, The African And Arab Region","v":false}]},{"num":"044","name":"Regionalism In Southeast Asia Asean Community","overview":{"slug":"regionalism-in-southeast-asia-asean-community","title":"Regionalism In Southeast Asia ASEAN Community"},"lessons":[{"slug":"basic-regionalism","title":"The Basics Of Regionalism","v":false},{"slug":"southeast-asia-region","title":"Southeast Asia As a Region","v":false},{"slug":"the-establishment-of-asean","title":"The Establishment Of ASEAN","v":false},{"slug":"asean-chapter","title":"Understanding the ASEAN Charter","v":false},{"slug":"asean-community","title":"Understanding ASEAN Community","v":false}]},{"num":"045","name":"International Organization In International Relations","overview":{"slug":"international-organization-in-international-relations","title":"International Organization In International Relations"},"lessons":[{"slug":"intro-international-organization","title":"Introduction To International Organization (IO) In IR","v":false},{"slug":"theory-international-organizaton","title":"Theory And Methods of International Organization","v":false},{"slug":"evolution-internationa-organizations","title":"The Evolution of International Organizations","v":false},{"slug":"un-administration","title":"'The United Nations: Introduction'","v":false},{"slug":"un-security","title":"'The United Nations: Maintaining International Peace And Security'","v":false},{"slug":"imf-world-bank","title":"The IMF And The World Bank","v":false}]},{"num":"046","name":"Global Economic Architecture","overview":{"slug":"global-economic-architecture","title":"Global Economic Architecture"},"lessons":[{"slug":"introduction-to-global-economic-architecture","title":"Introduction To Global Economic Architecture","v":false},{"slug":"evolution-global-economic-architecture","title":"The Evolution of the Global Economic Architecture","v":false},{"slug":"economic-hegemony","title":"'Global Economic Architecture: The View on Global Economic Hegemony'","v":false},{"slug":"world-trading-system","title":"World Trading System In The 20th Century And Beyond","v":false},{"slug":"european-economic","title":"The Rise of the European Economic Giant","v":false},{"slug":"global-financial-system","title":"Global Financial System In The 20th Century And Beyond","v":false}]},{"num":"050","name":"Wto And Trade Diplomacy","overview":{"slug":"wto-and-trade-diplomacy","title":"WTO And Trade Diplomacy"},"lessons":[{"slug":"international-trade-as-diplomacy","title":"International Trade As Diplomacy","v":false},{"slug":"transformation-diplomacy-trade","title":"Three Transformation of Diplomacy and International Trade","v":false},{"slug":"industrial-revolution","title":"The Industrial Revolution That Changed Trade Forever","v":false},{"slug":"evolution-global-trade","title":"'From Silk Road to Superhighway: The Evolution of Global Trade Diplomacy'","v":false},{"slug":"pillars-wto","title":"'The 3 Pillars of the WTO: How Law, Economics, and Politics Shaped Global Trade'","v":false},{"slug":"judicial-procedure-wto","title":"'When Negotiations Fail: The Rise of Judicial Procedures in Trade Agreements'","v":false},{"slug":"wto-dispute-settlement","title":"WTO Dispute Settlement Mechanism","v":false},{"slug":"wto-decision-making","title":"How the WTO Makes Decisions","v":false}]}]};
    const cxState = { mod: null, series: null, q: "" };
    const cxModsEl = document.getElementById('cx-modules');
    const cxFiltersEl = document.getElementById('cx-filters');
    const cxLessonsEl = document.getElementById('cx-lessons');

    function cxGrouped() {
      const groups = new Map();
      CX_DATA.modules.forEach(m => {
        const g = m.num.slice(0, 2);
        if (!groups.has(g)) groups.set(g, []);
        groups.get(g).push(m);
      });
      return [...groups.entries()].sort((a, b) => a[0].localeCompare(b[0]));
    }

    function esc(t) { return t.replace(/&/g, "&amp;").replace(/</g, "&lt;"); }

    function modButton(m, on) {
      return '<button type="button" class="cx-mod' + (on ? " is-on" : "") + '" data-mod="' + m.num + '">' +
             '<span class="cx-mod-num">M' + m.num + '</span>' +
             '<span class="cx-mod-name">' + esc(m.name) + '</span>' +
             '<span class="cx-mod-count">' + m.lessons.length + '</span></button>';
    }

    function renderFilters() {
      cxFiltersEl.innerHTML = '<button type="button" class="cx-filter is-on" data-s="">All Series</button>' +
        Object.entries(CX_DATA.series).map(([k, v]) =>
          '<button type="button" class="cx-filter" data-s="' + k + '">' + v + '</button>').join("");
    }

    function renderModules() {
      let html = "";
      cxGrouped().forEach(([g, mods]) => {
        html += '<div class="cx-series-label">' + (CX_DATA.series[g] || ("Series " + g)) + '</div>';
        mods.forEach(m => { html += modButton(m, cxState.mod === m.num); });
      });
      cxModsEl.innerHTML = html;
      bindModules();
    }

    function bindModules() {
      cxModsEl.querySelectorAll(".cx-mod").forEach(btn => {
        btn.addEventListener("click", () => {
          cxState.mod = btn.dataset.mod;
          cxState.q = "";
          document.getElementById("cx-search").value = "";
          renderModules(); renderLessons();
        });
      });
    }

    function lessonRow(l, pathLabel) {
      const chip = l.v ? ' <span class="cx-video-chip">VIDEO</span>' : "";
      const href = siteBase + "/" + l.slug + ".html";
      return '<a class="cx-lesson" href="' + href + '">' +
             '<span class="cx-lesson-title">' + esc(l.title) + chip + '</span>' +
             '<span class="cx-lesson-path">' + esc(pathLabel) + '</span></a>';
    }

    function renderLessons() {
      if (cxState.q) {
        const q = cxState.q.toLowerCase();
        const hits = [];
        CX_DATA.modules.forEach(m => m.lessons.forEach(l => {
          if ((l.title + " " + m.name).toLowerCase().includes(q)) {
            hits.push(lessonRow(l, "M" + m.num + " \u00B7 " + m.name));
          }
        }));
        cxLessonsEl.innerHTML = hits.length
          ? '<div class="cx-panel"><div class="cx-panel-head"><span class="cx-panel-title">' + hits.length +
            ' result' + (hits.length === 1 ? "" : "s") + ' for "' + esc(cxState.q) + '"</span></div>' + hits.join("") + '</div>'
          : '<div class="cx-empty">No lessons match <strong>"' + esc(cxState.q) + '"</strong>.<br>Try another topic.</div>';
        return;
      }
      const m = CX_DATA.modules.find(x => x.num === cxState.mod);
      if (!m) {
        cxLessonsEl.innerHTML = '<div class="cx-empty">Select a module on the left to browse its lessons.</div>';
        return;
      }
      const ov = m.overview ? '<a class="cx-panel-overview" href="' + siteBase + '/' + m.overview.slug + '.html">Module Overview &rarr;</a>' : "";
      cxLessonsEl.innerHTML = '<div class="cx-panel"><div class="cx-panel-head"><span class="cx-panel-title">' +
        esc(m.name) + '</span>' + ov + '</div>' +
        m.lessons.map(l => lessonRow(l, "M" + m.num)).join("") + '</div>';
    }

    cxFiltersEl.addEventListener("click", e => {
      const btn = e.target.closest(".cx-filter");
      if (!btn) return;
      cxState.series = btn.dataset.s || null;
      cxFiltersEl.querySelectorAll(".cx-filter").forEach(b => b.classList.toggle("is-on", b === btn));
      cxState.mod = null;
      cxState.q = "";
      document.getElementById("cx-search").value = "";
      let html = "";
      cxGrouped().forEach(([g, mods]) => {
        if (cxState.series && g !== cxState.series) return;
        html += '<div class="cx-series-label">' + (CX_DATA.series[g] || ("Series " + g)) + '</div>';
        mods.forEach(m => { html += modButton(m, false); });
      });
      cxModsEl.innerHTML = html;
      bindModules();
      renderLessons();
    });

    document.getElementById("cx-search").addEventListener("input", e => {
      cxState.q = e.target.value.trim();
      renderLessons();
    });

    renderFilters();
    renderModules();
    cxState.mod = CX_DATA.modules[0].num;
    renderLessons();
});

// Playable Prisoner's Dilemma Simulator Logic
let gtScoreA = 0;
let gtScoreB = 0;
let lastOpponentMove = 'cooperate'; // Tit for Tat starts friendly
let roundNum = 1;

window.playGameTheory = function(playerMove) {
  const oppMove = lastOpponentMove;
  let changeA = 0, changeB = 0;
  let roundDesc = "";

  if (playerMove === 'cooperate' && oppMove === 'cooperate') {
    changeA = 3; changeB = 3;
    roundDesc = "Mutual Cooperation (+3, +3) — Pareto optimal outcome.";
  } else if (playerMove === 'defect' && oppMove === 'cooperate') {
    changeA = 5; changeB = 0;
    roundDesc = "Temptation payoff! You defected while opponent cooperated (+5, 0).";
  } else if (playerMove === 'cooperate' && oppMove === 'defect') {
    changeA = 0; changeB = 5;
    roundDesc = "Sucker's payoff! Opponent exploited your cooperation (0, +5).";
  } else {
    changeA = 1; changeB = 1;
    roundDesc = "Mutual Defection (+1, +1) — Nash equilibrium trap.";
  }

  gtScoreA += changeA;
  gtScoreB += changeB;
  lastOpponentMove = playerMove; // Tit for Tat mimics player's last action

  const scoreAEl = document.getElementById('gt-score-a');
  const scoreBEl = document.getElementById('gt-score-b');
  const statusEl = document.getElementById('gt-opp-status');
  if (scoreAEl) scoreAEl.textContent = gtScoreA;
  if (scoreBEl) scoreBEl.textContent = gtScoreB;
  if (statusEl) statusEl.textContent = `Round ${roundNum}: Opponent played ${oppMove.toUpperCase()}`;

  const log = document.getElementById('gt-log');
  if (log) {
    const newLine = document.createElement('div');
    newLine.className = 'sandbox-log-line';
    newLine.textContent = `> R${roundNum}: You: ${playerMove.toUpperCase()}, Opp: ${oppMove.toUpperCase()} | ${roundDesc}`;
    log.insertBefore(newLine, log.firstChild);
  }
  roundNum++;
};
</script>
