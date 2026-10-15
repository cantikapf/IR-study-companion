---
layout: default
title: IR Study Companion — A Free, Structured Course in International Relations
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
    --globe-line: #1e3a8a;
    --globe-line-opacity: 0.25;
    --globe-boundary-opacity: 0.55;
    --globe-node: #1e3a8a;
    --globe-route-oxford: #1e3a8a;
    --globe-route-crimson: #e11d48;
    --globe-route-gold: #d97706;
    --globe-sat: #d97706;
  }

  body.dark-theme .hero-motion-graphic {
    --globe-line: #60a5fa;
    --globe-line-opacity: 0.24;
    --globe-boundary-opacity: 0.45;
    --globe-node: #38bdf8;
    --globe-route-oxford: #38bdf8;
    --globe-route-crimson: #fb7185;
    --globe-route-gold: #fbbf24;
    --globe-sat: #fbbf24;
  }

  .motion-globe {
    width: 100%;
    max-width: 440px;
    height: auto;
    display: block;
    filter: drop-shadow(0 10px 25px rgba(0, 0, 0, 0.04));
  }
  body.dark-theme .motion-globe {
    filter: drop-shadow(0 0 35px rgba(56, 189, 248, 0.1));
  }

  .cxg-backdrop {
    fill: url(#mgBackdrop);
  }
  .cxg-stop-inner { stop-color: #1e3a8a; stop-opacity: 0.03; }
  .cxg-stop-outer { stop-color: #1e3a8a; stop-opacity: 0; }
  body.dark-theme .cxg-stop-inner { stop-color: #38bdf8; stop-opacity: 0.08; }
  body.dark-theme .cxg-stop-outer { stop-color: #38bdf8; stop-opacity: 0; }

  .cxg-graticule {
    fill: none;
    stroke: var(--globe-line);
    stroke-width: 1.25;
    opacity: var(--globe-line-opacity);
  }

  .cxg-boundary {
    fill: none;
    stroke: var(--globe-line);
    stroke-width: 2;
    opacity: var(--globe-boundary-opacity);
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
    opacity: 0.8;
    animation: cxg-dash 22s linear infinite;
  }
  .cxg-route.route-crimson { stroke: var(--globe-route-crimson); }
  .cxg-route.route-gold { stroke: var(--globe-route-gold); }
  .cxg-route.route-oxford { stroke: var(--globe-route-oxford); }

  .cxg-nodes {
    fill: var(--globe-node);
    stroke: var(--lms-surface);
    stroke-width: 1.6;
  }
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
    fill: var(--globe-sat);
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
    flex-direction: column;
    gap: 0.65rem;
    padding-bottom: 0.85rem;
    border-bottom: 1px solid var(--lms-hairline);
    margin-bottom: 1.25rem;
  }

  .sandbox-header-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 0.75rem;
    flex-wrap: wrap;
  }

  .sandbox-top-actions {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }

  .sandbox-tag {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #1e3a8a;
    white-space: nowrap;
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

  .labs-catalog-pane {
    display: flex;
    flex-direction: column;
    background: var(--lms-surface);
    border: 1px solid var(--lms-border-strong);
    border-radius: var(--lms-radius-lg);
    padding: 1.25rem 1.25rem 1rem;
    box-shadow: var(--lms-shadow-md);
  }

  .labs-catalog-header {
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
    padding-bottom: 0.85rem;
    border-bottom: 1px solid var(--lms-hairline);
    margin-bottom: 0.75rem;
  }

  .labs-catalog-head-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .labs-catalog-title {
    font-size: 0.875rem;
    font-weight: 750;
    color: var(--lms-ink-primary);
    display: flex;
    align-items: center;
    gap: 0.45rem;
  }

  .labs-counter-badge {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.6875rem;
    font-weight: 600;
    color: #1e3a8a;
    background: rgba(30, 58, 138, 0.08);
    border: 1px solid rgba(30, 58, 138, 0.2);
    border-radius: var(--lms-radius-sm);
    padding: 0.15rem 0.45rem;
  }

  .labs-filter-chips {
    display: flex;
    gap: 0.35rem;
    flex-wrap: wrap;
  }

  .labs-filter-btn {
    border: 1px solid var(--lms-hairline);
    background: var(--lms-subtle);
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--lms-ink-secondary);
    padding: 0.3rem 0.55rem;
    border-radius: var(--lms-radius-sm);
    cursor: pointer;
    transition: all 0.15s ease;
  }

  .labs-filter-btn:hover {
    background: var(--lms-hover);
    color: var(--lms-ink-primary);
  }

  .labs-filter-btn.is-active {
    background: #1e3a8a;
    color: #ffffff;
    border-color: #1e3a8a;
  }

  .labs-scroll-pane {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    max-height: 410px;
    overflow-y: auto;
    padding-right: 0.35rem;
    scrollbar-width: thin;
    scrollbar-color: var(--lms-border-strong) transparent;
  }

  .labs-scroll-pane::-webkit-scrollbar {
    width: 6px;
  }
  .labs-scroll-pane::-webkit-scrollbar-track {
    background: transparent;
  }
  .labs-scroll-pane::-webkit-scrollbar-thumb {
    background: var(--lms-border-strong);
    border-radius: 4px;
  }
  .labs-scroll-pane::-webkit-scrollbar-thumb:hover {
    background: var(--lms-ink-tertiary);
  }

  .lab-card-sm {
    background: var(--lms-surface);
    border: 1px solid var(--lms-border-strong);
    border-radius: var(--lms-radius-md);
    padding: 1rem 1.15rem;
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

  .lab-card-sm[data-cat="security"] {
    border-left: 3px solid #dc2626;
  }
  .lab-card-sm[data-cat="strategy"] {
    border-left: 3px solid #2563eb;
  }
  .lab-card-sm[data-cat="governance"] {
    border-left: 3px solid #7c3aed;
  }

  .lab-card-sm.is-featured-lab {
    border-left: 3px solid #059669;
    background: var(--lms-subtle);
  }

  .lab-card-sm.is-completed-lab {
    border-color: rgba(5, 150, 105, 0.4);
  }

  .lab-card-head-meta {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.35rem;
    flex-wrap: wrap;
  }

  .lab-card-meta-chips {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
  }

  .lab-card-chip {
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.6875rem;
    color: var(--lms-ink-tertiary);
    background: var(--lms-subtle);
    border: 1px solid var(--lms-hairline);
    padding: 0.15rem 0.4rem;
    border-radius: var(--lms-radius-sm);
  }

  .lab-card-status-row {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
  }

  .lab-card-badge-done {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.6875rem;
    font-weight: 700;
    color: #059669;
    background: rgba(5, 150, 105, 0.12);
    border: 1px solid rgba(5, 150, 105, 0.25);
    padding: 0.12rem 0.45rem;
    border-radius: var(--lms-radius-sm);
  }

  .lab-card-stars {
    color: #d97706;
    letter-spacing: 0.08em;
    font-size: 0.8rem;
    display: inline-flex;
    align-items: center;
  }

  .sandbox-hud-bar,
  .sandbox-hud-chips {
    display: flex;
    gap: 0.4rem;
    flex-wrap: wrap;
    align-items: center;
  }

  .sandbox-hud-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    padding: 0.2rem 0.5rem;
    border-radius: var(--lms-radius-sm);
    background: var(--lms-subtle);
    border: 1px solid var(--lms-hairline);
    color: var(--lms-ink-secondary);
  }

  .sandbox-hud-chip.is-streak {
    color: #d97706;
    background: rgba(217, 119, 6, 0.1);
    border-color: rgba(217, 119, 6, 0.25);
    font-weight: 700;
  }

  .sandbox-debrief-card {
    background: var(--lms-subtle);
    border: 1px solid var(--lms-border-strong);
    border-radius: var(--lms-radius-md);
    padding: 1.25rem;
    margin-bottom: 1.25rem;
    text-align: center;
  }

  .sandbox-debrief-stars {
    font-size: 1.8rem;
    color: #d97706;
    margin-bottom: 0.35rem;
    letter-spacing: 0.12em;
  }

  .sandbox-debrief-rank {
    font-size: 1.2rem;
    font-weight: 800;
    color: var(--lms-ink-primary);
    margin-bottom: 0.4rem;
  }

  .sandbox-debrief-reveal {
    font-size: 0.825rem;
    color: var(--lms-ink-secondary);
    line-height: 1.5;
    margin-bottom: 1rem;
    padding: 0.65rem 0.85rem;
    background: var(--lms-surface);
    border: 1px solid var(--lms-hairline);
    border-radius: var(--lms-radius-sm);
  }

  .sandbox-debrief-actions {
    display: flex;
    gap: 0.75rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  .lab-card-title {
    font-size: 1rem;
    font-weight: 700;
    color: var(--lms-ink-primary);
    margin: 0.2rem 0 0.3rem;
  }

  .lab-card-desc {
    font-size: 0.825rem;
    color: var(--lms-ink-secondary);
    line-height: 1.45;
    margin-bottom: 0.65rem;
  }

  .lab-card-link {
    font-size: 0.825rem;
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
    .labs-scroll-pane {
      max-height: 380px;
    }
  }

  /* ── Dark Mode Overrides ── */
  body.dark-theme .home-eyebrow { color: var(--lms-ink-tertiary); }
  body.dark-theme .home-title { color: var(--lms-ink-primary); }
  body.dark-theme .home-description { color: var(--lms-ink-secondary); }
  body.dark-theme .home-section-title { color: var(--lms-ink-primary); }
  body.dark-theme .home-section-subtitle { color: var(--lms-ink-tertiary); }
  body.dark-theme .metric-value { color: var(--lms-ink-primary); }
  body.dark-theme .metric-label { color: var(--lms-ink-tertiary); }
  body.dark-theme .resume-card {
    background: var(--lms-surface);
    border-color: var(--lms-border-strong);
  }
  body.dark-theme .resume-card .resume-title,
  body.dark-theme .resume-card .resume-lesson-title { color: var(--lms-ink-primary); }
  body.dark-theme .resume-card .resume-subtitle { color: var(--lms-ink-secondary); }
  body.dark-theme .resume-card .resume-progress-text,
  body.dark-theme .resume-card .resume-progress-caption { color: var(--lms-ink-tertiary); }
  body.dark-theme .resume-card .resume-cta,
  body.dark-theme .resume-action-btn {
    background: #f4f4f5;
    color: #09090b !important;
  }
  body.dark-theme .cx-panel-overview { color: #93c5fd; }
  body.dark-theme .cx-lesson:hover .cx-lesson-title { color: #93c5fd; }
  body.dark-theme .cx-mod.is-on {
    box-shadow: inset 3px 0 0 #60a5fa;
  }
  body.dark-theme .cx-mod.is-on .cx-mod-num {
    color: #93c5fd;
    border-color: #60a5fa;
  }
  body.dark-theme .cx-video-chip {
    color: #fb7185;
    background: rgba(251, 113, 133, 0.15);
  }
  body.dark-theme .cx-filter.is-on {
    background: var(--lms-subtle);
    color: var(--lms-ink-primary);
    border-color: var(--lms-border-strong);
  }
  body.dark-theme .sandbox-tag { color: #93c5fd; }
  body.dark-theme .sandbox-status-chip {
    color: #6ee7b7;
    background: rgba(110, 231, 183, 0.12);
  }
  body.dark-theme .sandbox-hud-chip.is-streak {
    color: #fbbf24;
    background: rgba(251, 191, 36, 0.12);
  }
  body.dark-theme .labs-counter-badge {
    color: #93c5fd;
    background: rgba(147, 197, 253, 0.12);
  }
  body.dark-theme .lab-card-link { color: #93c5fd; }
  body.dark-theme .lab-card-badge-done {
    color: #6ee7b7;
    background: rgba(110, 231, 183, 0.12);
  }
  body.dark-theme .btn-sim.btn-sim-coop {
    background: #059669;
    color: #ffffff;
  }


/* Interactive Globe Styles */
  .interactive-globe-container {
    position: relative;
    width: 100%;
    max-width: 480px;
    display: flex;
    flex-direction: column;
    align-items: center;
    user-select: none;
    -webkit-user-select: none;
    touch-action: pan-y;
  }

  .interactive-globe-svg {
    width: 100%;
    height: auto;
    display: block;
    touch-action: none;
  }

  .globe-sphere-bg {
    transition: fill 0.3s ease;
  }

  .globe-land-path {
    transition: fill 0.3s ease, stroke 0.3s ease;
  }

  :root {
    --land-fill: #e2e8f0;
    --land-stroke: #94a3b8;
  }

  body.dark-theme, [data-theme="dark"] {
    --land-fill: #1e293b;
    --land-stroke: #475569;
  }

  body.dark-theme .globe-sphere-bg,
  [data-theme="dark"] .globe-sphere-bg {
    fill: #0f172a;
  }

  .globe-drag-hint {
    margin-top: 0.65rem;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    background: var(--lms-surface-subtle, #f1f5f9);
    border: 1px solid var(--lms-border-hairline, #e2e8f0);
    font-family: ui-monospace, 'JetBrains Mono', monospace;
    font-size: 0.725rem;
    letter-spacing: 0.05em;
    color: var(--lms-ink-tertiary, #64748b);
    transition: all 0.2s ease;
  }

  .interactive-globe-container.is-dragging .globe-drag-hint {
    background: var(--lms-accent-oxford, #1e3a8a);
    color: #ffffff;
    border-color: var(--lms-accent-oxford, #1e3a8a);
  }

  .interactive-globe-container.is-dragging #ir-globe-hitbox,
  .interactive-globe-container.is-dragging {
    cursor: grabbing !important;
  }
</style>

<div class="home-viewport">

  <!-- Editorial Hero with Animated Motion Graphic -->
  <header class="home-hero-split">
    <div class="home-hero-text">
      <div class="home-eyebrow">The Structured Open-Access Curriculum in International Relations</div>
      <h1 class="home-title">World politics, taught from the ground up.</h1>
      <p class="home-description">
        It follows the sequence of a degree: theory first, then history, political economy, law, and diplomacy. Every module ends with an exam, and the labs drop you into real diplomatic dilemmas.
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
      <div class="interactive-globe-container" id="ir-globe-container">
        <svg class="motion-globe interactive-globe-svg" id="ir-globe-svg" viewBox="0 0 520 536" role="img" aria-label="Interactive 3D wireframe globe with sovereign nations and diplomatic routes. Click and drag horizontally to spin.">
          <defs>
            <clipPath id="mgClip">
              <circle cx="260" cy="268" r="208"/>
            </clipPath>
            <radialGradient id="globeSphereGrad" cx="35%" cy="32%" r="68%">
              <stop offset="0%" stop-color="#ffffff"/>
              <stop offset="70%" stop-color="#f8fafc"/>
              <stop offset="100%" stop-color="#e2e8f0"/>
            </radialGradient>
          </defs>

          <!-- Base Sphere Body -->
          <circle cx="260" cy="268" r="208" fill="url(#globeSphereGrad)" class="globe-sphere-bg"/>

          <!-- Real Continents Layer -->
          <path id="ir-globe-land" clip-path="url(#mgClip)" class="globe-land-path" d="M219.474,472.014L219.496,472.018L220.388,472.182L222.808,472.641L224.677,472.938L226.974,473.328L228.266,473.463L230.271,473.698L232.092,473.843L232.876,473.793L235.086,474.042L237.504,474.457L238.696,474.417L241.228,474.556L242.669,474.654L245.382,474.786L248.136,474.951L250.169,475.15L252.381,475.25L255.157,475.315L257.675,475.291L260,475.177L262.518,475.099L264.33,474.751L266.454,474.672L267.977,474.823L270.012,474.863L272.273,474.773L274.159,474.473L277.019,474.165L279.949,473.818L282.512,473.423L285.098,473.127L287.55,472.775L289.588,472.303L292.384,471.821L295.358,471.337L297.617,471.156L297.735,471.45L298.547,471.572L300.177,471.469L301.751,471.31L304.814,470.616L306.392,470.413L308.071,470.133L307.614,470.412L305.998,470.825L302.974,471.492L303.357,471.43L302.338,471.645L302.338,471.646L295.205,472.999L288.029,474.103L280.819,474.955L273.584,475.556L266.332,475.904L259.073,475.998L251.814,475.839L244.566,475.427L237.336,474.762L230.134,473.845L222.968,472.677ZM346.964,447.81L344.068,448.514L344.94,447.609L345.923,446.831L346.401,446.444L347.051,446.746L348.556,446.591L348.276,446.91ZM329.477,364.381L330.295,369.338L329.04,371.945L327.5,371.16L327.415,374.87L325.708,378.378L321.82,386.18L317.228,396.054L312.823,400.297L308.036,400.918L305.148,398.89L304.111,394.154L304.911,389.773L306.711,388.197L309.122,383.896L307.775,380.679L309.157,376.319L311.36,374.011L314.831,372.523L318.351,370.385L322.339,366.602L323.425,365.561L325.778,361.21L327.786,361.029ZM465.264,301.628L465.184,302.098L465.088,302.566L465.472,300.259L465.567,299.718L465.681,298.971L465.681,298.971ZM462.462,302.355L464.004,299.296L464.636,301.075L465.189,301.343L464.498,303.033L463.561,304.877L462.607,304.733L461.794,306.083L460.619,304.795L460.839,301.516L462.301,301.081ZM467.662,279.848L467.706,278.941L467.922,273.566L467.989,265.896L467.986,265.593L467.986,265.593L467.943,272.853ZM460.576,301.788L459.082,300.383L457.652,297.04L456.417,292.966L454.571,286.328L453.564,281.322L451.43,277.262L448.401,272.814L449.027,270.977L452.849,272.698L454.777,275.433L457.348,277.53L459.006,281.545L459.316,285.833L460.301,286.331L460.657,290.076L461.614,291.779ZM467.758,263.661L467.826,267.261L467.782,273.153L467.414,280.047L467.061,284.713L466.656,285.416L466.277,285.137L465.539,286.276L464.702,287.316L464.53,282.274L464.173,276.869L464.523,270.608L465.438,269.57L465.61,265.504L466.265,260.229L466.32,255.886L466.368,250.198L466.229,246.567L466.694,249.148L467.057,249.841L467.128,251.987L467.328,255.603L467.706,261.814ZM421.197,279.834L419.277,281.276L417.932,278.791L417.003,273.807L417.344,267.71L419.176,269.19L420.53,271.359L422.023,274.712L422.047,278.52ZM55.257,231.866L55.258,231.472L55.336,230.997L55.481,230.316L55.745,228.938L55.784,229.021L55.747,229.336ZM464.94,232.452L464.841,231.895L464.643,230.783L464.497,229.987L464.497,229.987ZM464.031,227.563L463.99,227.353L463.988,227.344L463.988,227.345ZM465.186,236.862L465.536,241.389L465.23,238.502L464.955,235.7L464.567,232.751L463.911,228.842L464.478,231.489L464.808,233.997ZM463.841,226.612L464.139,228.121L464.431,229.742L464.123,228.174L463.756,226.358L463.425,224.864L463.425,224.864L463.573,225.376L463.461,224.784L463.552,225.212L463.552,225.213ZM462.281,219.558L462.333,219.785L462.28,219.652L462.131,219.752L461.54,217.737L461.084,216.042L460.912,215.909L459.537,211.364L458.259,206.892L457.201,203.091L457.201,203.091L457.106,202.29L457.897,204.614L459.479,209.537L460.749,214.301L461.482,216.62L461.511,216.45L461.511,216.45ZM454.251,212.216L454.273,214.599L453.389,214.269L452.374,211.385L452.16,209.436L452.487,207.543L452.839,207.124L453.426,208.21L453.711,210.071ZM451.72,189.155L452.879,192.184L451.726,189.904L450.667,187.615L449.199,183.965L447.992,180.881L448.406,181.434L449.341,183.502ZM273.483,194.435L271.553,195.918L271.804,196.554L271.901,196.83L268.898,198.265L267.425,197.838L266.705,196.476L268.111,196.333L268.314,196.313L268.714,195.484L270.844,195.498ZM241.468,194.196L243.001,195.384L245.303,195.244L247.49,195.531L247.388,196.123L249.014,195.743L248.6,196.746L244.315,196.947L244.379,196.382L240.818,195.623ZM219.15,184.616L217.708,187.166L217.947,188.229L217.075,189.907L215.14,188.496L213.791,188.03L210.269,186.035L210.987,184.359L214.128,184.912L217.005,184.758ZM204.46,173.5L205.408,175.938L203.975,180.214L202.832,179.887L201.488,180.873L200.716,179.908L201.644,175.97L201.556,174.062L202.916,174.37ZM432.273,151.441L431.514,150.346L429.856,147.946L429.856,147.946ZM117.245,119.778L116.789,120.565L116.76,121.099L115.736,121.761L115.611,121.676L116.913,119.841L117.84,118.89L118.59,118.406ZM123.896,115.016L123.886,114.76L124.908,113.257L126.365,111.644L126.534,111.67L125.652,113.021L124.4,114.584ZM128.562,114.845L126.887,116.216L125.553,117.553L125.812,118.342L122.981,121.378L122.395,122.597L118.383,126.217L118.343,125.265L120.997,122.817L118.225,123.867L120.037,121.978L119.756,120.079L121.662,118.741L123.867,117.124L130.165,113.139L131.217,113.228ZM183.758,135.508L179.584,136.502L177.394,135.568L180.691,133.028L181.7,130.122L185.395,128.523L187.492,127.549L188.952,127.715L189.678,129.687L187.568,131.347L186.629,133.327ZM200.977,120.034L199.303,122.275L199.471,124.569L198.032,127.2L198.878,131.398L198.217,136.019L199.229,138.553L197.746,140.754L192.686,141.53L188.247,141.122L184.745,141.758L182.117,141.591L188.566,139.022L186.001,136.729L188.229,134.694L192.275,133.592L193.322,130.205L191.571,128.421L192.941,126.616L192.819,125.137L195.164,121.256L199.087,119.709ZM168.298,82.049L166.935,82.608L167.449,82.306L168.5,81.789L168.681,81.714L169.36,81.469L169.06,81.667ZM182.551,75.455L181.21,76.03L178.358,77.326L175.222,78.733L173.454,79.687L174.856,78.757L175.577,78.266L176.805,77.585L178.328,76.928L183.002,75.211ZM201.867,99.062L199.606,102.178L191.728,103.907L189.153,103.426L189.372,101.195L190.802,99.656L190.221,98.01L194.291,97.131L196.807,98.2L200.137,98.609ZM182.305,77.14L182.59,76.803L184.258,76.181L185.89,75.728L185.99,75.888L184.812,76.447L183.419,76.921L183.011,77.036ZM311.132,173.615L314.355,175.96L313.293,177.055L313.16,181.072L312.874,183.449L316.786,186.133L323.282,187.864L327.123,185.732L325.49,179.811L323.28,176.704L321.177,173.938L325.597,173.102L322.033,169.878L320.74,173.323L318.904,170.551L318.404,167.985L313.376,164.612L311.382,162.879L313.24,160.781L317.166,160.048L315.531,155.161L311.298,155.292L306.936,157.586L304.246,160.336L305.47,166.292L309.458,172.121ZM354.173,82.54L355.848,83.412L366.825,89.79L375.408,95.269L376.7,95.941L374.406,94.328L377.02,96.04L377.02,96.04L382.95,100.228L388.73,104.621L394.354,109.214L399.813,113.999L405.103,118.972L406.405,120.252L408.764,122.673L410.346,124.514L411.316,125.595L413.318,127.826L415.663,130.46L417.083,132.171L418.436,133.995L419.846,135.644L420.812,136.509L424.268,140.534L428.033,145.508L429.991,148.488L429.528,148.127L425.825,143.343L423.612,140.536L423.568,140.708L423.454,140.732L423.132,140.558L421.661,138.573L420.015,136.56L419.497,136.27L420.062,137.835L421.845,141.03L419.755,138.383L417.156,135.318L419.566,139.413L421.09,142.473L423.592,145.434L425.208,146.792L424.113,143.989L424.873,143.904L426.739,147.101L429.123,151.273L431.623,154.336L435.387,159.099L438.379,163.292L439.89,166.021L441.821,169.035L443.449,172.456L447.419,181.211L450.392,189.889L451.098,194.968L451.043,196.486L451.416,201.178L452.349,206.717L450.995,205.072L449.38,203.685L449.354,208.568L450.459,214.823L454.429,221.514L456.875,224.982L460.071,237.135L459.499,243.462L458.838,251.554L458.013,247.094L456.031,246.071L453.999,241.277L451.7,241.45L450.255,239.264L451.377,248.872L451.942,254.749L453.775,256.954L455.243,261.263L456.774,262.751L457.996,264.411L458.796,268.624L458.98,271.437L459.652,274.151L460.09,278.096L458.361,277.077L456.693,273.666L455.502,269.007L454.753,265.047L453.709,262.757L452.342,259.495L451.472,260.454L450.88,256.23L450.162,250.085L449.167,245.613L447.579,240.274L444.763,231.994L442.988,231.867L441.093,235.351L439.245,230.381L435.577,223.922L434.418,222.516L431.383,218.831L429.722,215.641L426.889,214.581L427.755,218.153L426.627,218.263L425.192,218.101L424.25,220.071L423.182,224.41L420.807,229.968L418.668,237.637L417.502,242.222L414.944,245.328L413.836,249.071L415.933,256.311L416.49,265.838L414.592,269.744L413.431,272.298L411.861,276.054L407.459,268.804L404.972,263.915L401.71,256.588L397.631,250.158L393.463,239.229L391.084,231.587L386.197,234.569L382.492,229.437L377.781,225.982L373.988,223.054L366.6,222.599L358.417,224.34L349.506,223.855L344.138,219.526L340.37,220.009L334.031,221.479L327.371,218.253L321.842,210.978L318.171,210.608L315.664,211.884L316.354,214.301L319.349,219.729L321.809,221.65L324.387,224.275L324.771,226.752L326.634,228.731L326.361,226.958L327.852,224.653L329.283,227.746L329.841,231.296L330.566,231.945L335.347,230.706L338.901,228.125L342.176,223.026L343.202,222.173L343.042,224.36L345.541,229.47L349.708,230.727L353.408,232.755L355.502,234.274L354.872,237.291L353.783,239.642L351.466,242.162L351.028,245.148L351.474,248.016L348.269,249.539L347.698,252.174L344.73,253.643L343.478,256.353L339.76,257.517L336.038,259.021L335.696,261.978L327.49,266.072L323.063,269.379L320.456,270.688L315.455,272.166L313.82,273.376L312.517,274.558L309.795,275.105L306.242,273.149L305.723,269.908L303.786,266.023L304.022,264.191L304.23,261.997L302.351,259.197L300.499,256.756L297.076,250.765L293.205,248.05L290.169,242.037L288.151,235.996L284.744,233.967L283.608,231.139L281.524,228.703L278.02,223.107L274.715,220.704L275.223,217.515L275.463,215.75L274.05,220.01L272.537,222.516L269.895,219.727L267.244,214.83L270.601,222.193L274.717,229.588L278.887,235.577L278.337,238.465L283.169,242.29L283.697,246.605L285.731,254.503L288.898,256.565L292.328,264.052L299.114,268.823L303.122,272.968L305.99,274.981L306.805,277.474L306.197,279.325L308.374,281.367L311.569,282.972L318.371,281.03L323.051,279.2L326.046,278.215L328.684,277.249L331.916,275.486L333.324,276.439L333.269,280.443L332.242,285.622L328.943,294.601L323.069,304.434L315.901,312.808L307.143,319.381L302.522,325.59L299.305,328.19L297.153,330.026L295.33,333.904L293.143,337.426L291.617,343.603L294.067,345.522L293.286,348.571L293.898,352.204L296.592,356.037L296.754,360.917L297.093,368.584L296.544,372.386L292.882,376.591L285.535,379.637L280.24,383.44L276.376,386.531L277.564,390.932L278.136,393.246L278.337,396.115L278.585,397.815L276.496,400.118L269.834,402.742L268.799,404.68L269.077,406.31L267.988,410.605L264.748,413.254L262.832,414.816L260.311,417.875L254.508,422.065L249.122,423.935L247.356,424.621L244.072,424.789L238.96,424.408L234.602,425.203L230.635,426.211L227.879,425.379L225.326,424.068L224.695,423.797L223.269,420.591L223.811,418.409L219.745,413.643L216.749,410.096L212.701,405.859L210.42,401.085L208.398,393.368L206.406,390.344L202.093,384.143L198.249,379.029L197.114,374.662L198.219,369.167L199.181,364.826L201.646,361.827L202.753,358.037L201.553,355.012L199.626,350.915L200.557,349.001L198.594,343.164L197.119,340.345L195.625,336.486L189.298,329.065L184.796,322.039L185.462,320.01L187.168,314.911L187.555,310.354L186.969,305.322L184.666,302.595L184.035,301.101L179.312,301.675L175.306,301.939L172.515,296.952L168.074,293.882L162.584,293.87L154.883,295.629L150.147,297.038L146.238,295.313L142.375,293.921L136.693,294.667L133.177,295.056L129.56,292.878L124.858,287.172L122.634,283.767L119.72,279.804L119.329,275.688L117.406,271.541L116.26,270.147L116.08,267.518L114.124,264.788L112.801,263.321L112.286,261.696L112.381,258L112.418,253.53L112.516,251.686L115.04,247.888L116.348,244.118L117.901,237.403L118.782,233.882L117.751,230.212L118.856,227.128L121.271,224.779L122.996,221.486L125.931,219.262L127.824,215.638L131.272,212.782L135.69,208.666L140.659,206.867L145.063,203.806L148.037,196.811L151.178,193.143L156.586,191.009L161.078,185.844L163.605,188.067L168.427,189.247L172.498,188.154L177.454,186.819L184.905,186.125L190.313,187.144L195.979,186.419L198.768,187.395L203.879,186.874L205.989,187.406L204.39,189.645L204.729,192.071L201.795,196.624L203.442,198.506L204.711,201.049L209.231,202.118L215.089,204.636L218.768,208.716L226.041,212.276L229.347,209.98L229.739,205.814L234.157,203.918L239.16,206.172L241.256,206.928L245.176,208.416L252.248,209.578L256.574,211.008L260.31,208.925L265.267,209.253L266.823,209.587L271.816,210.566L274.223,208.777L274.744,206.68L275.489,203.201L276.547,200.419L277.897,197.983L277.927,193.891L278.011,190.84L273.647,190.611L267.331,193.079L261.746,191.09L259.12,193.12L253.016,191.055L249.452,185.972L249.363,181.652L256.688,178.445L263.009,176.485L269.437,173.495L278.773,175.548L285.87,175.936L291.324,174.367L290.525,170.839L287.155,169.396L282.517,165.765L277.1,163.113L280.534,159.869L282.436,157.315L280.195,157.094L276.89,158.442L272.525,159.798L273.998,162.571L276.111,163.456L270.108,165.803L268.979,163.929L266.613,162.393L268.302,160.499L264.232,158.686L261.009,160.871L258.973,163.999L256.914,164.306L254.717,169.366L254.605,173.546L257.273,175.835L253.426,176.783L250.024,179.357L249.291,177.378L246.024,176.984L244.474,179.57L241.41,179.814L239.569,178.768L241.473,182.46L241.572,184.789L242.797,187.498L241.008,188.454L240.177,191.801L235.957,190.304L234.746,185.218L232.603,181.797L232.21,180.454L230.819,178.409L231.299,174.827L231.521,173.21L230.382,171.856L226.968,170.055L223.499,167.591L222.476,164.964L221.752,162.374L219.318,163.15L219.082,160.915L219.642,160.642L215.597,160.956L214.972,163.446L217.219,166.827L220.254,172.225L222.956,173.381L224.263,175.097L228.149,177.944L227.594,179.895L224.098,177.715L224.391,181.041L222.433,182.92L219.46,185.746L220.509,182.799L220.357,180.457L218.882,178.037L216.864,175.913L214.052,174.053L210.5,170.158L209.232,165.184L206.501,163.313L203.276,164.915L199.44,166.769L191.287,165.776L189.715,169.526L183.416,171.656L180.689,174.285L179.081,178.803L175.864,182.089L171.379,184.494L165.781,183.544L162.398,185.737L161.122,183.741L159.008,180.872L156.817,180.782L157.101,178.379L156.754,175.852L157.981,172.62L160.02,170.274L161.935,167.229L162.571,164.964L163.444,161.402L169.77,160.664L174.836,162.268L180.138,163.163L185.151,155.463L183.612,150.079L182.046,146.308L187.924,147.616L190.142,145.772L197.607,141.948L201.566,141.272L206.628,136.556L211.459,135.949L213.672,135.608L215.788,134.96L216.275,132.152L217.18,128.031L218.593,126.517L221.304,125.961L222.388,126.609L221.591,128.186L221.657,129.579L218.934,131.002L218.592,133.516L219.995,135.359L223.679,134.249L226.345,136.45L231.598,134.819L236.243,134.523L238.35,135.471L242.044,133.391L242.38,129.006L245.533,126.431L248.355,128.666L249.365,124.951L247.544,124.373L250.065,122.09L254.274,122.43L258.366,120.918L253.37,119.843L247.068,121.228L244.603,118.833L245.191,114.103L247.854,111.289L252.977,108.357L251.01,106.23L246.552,108.395L243.622,111.599L237.7,116.97L239.861,120.154L235.324,123.558L231.738,130.361L227.642,132.022L225.488,129.353L225.021,122.257L219.765,123.363L215.404,122.074L218.731,113.51L226.136,110.561L234.319,105.553L242.154,100.031L249.515,96.79L253.51,95.479L257.894,95.147L260,97.201L262.619,97.812L268.4,99.388L275.324,102.597L274.518,105.342L265.573,104.493L267.107,106.505L269.812,110.645L271.149,110.129L270.976,108.251L275.987,108.754L277.386,104.741L280.387,105.478L278.931,102.615L277.717,100.039L282.812,101.67L281.856,103.319L285.082,103.295L286.905,100.643L291.192,98.399L292.419,99.828L294.964,98.6L298.337,98.581L296.422,96.138L300.205,95.532L308.296,97.3L305.887,95.399L303.736,94.887L301.085,92.645L300.227,90.119L299.009,87.941L303.202,88.78L305.518,90.776L310.455,94.633L314.029,97.005L316.599,100.216L316.817,98.615L315.669,96.339L312.616,94.098L309.999,93.277L305.331,90.119L303.264,87.388L305.26,88.03L308.542,89.77L306.699,87.635L311.112,87.771L305.315,84.93L307.361,83.744L306.083,82.439L305.504,81.117L305.422,79.242L305.612,78.252L305.63,77.278L304.575,76.288L302.678,74.783L304.79,75.33L307.35,75.423L307.274,74.392L310.754,74.584L313.41,75.68L315.668,77.375L317.479,77.129L319.387,77.313L317.859,76.217L320.457,76.037L318.282,74.293L318.289,73.409L322.101,73.918L326.073,74.883L323.474,73.557L322.905,72.703L322.37,72.051L319.431,71.166L315.341,68.601L317.369,68.62L312.894,67.062L315.522,67.636L313.625,67.059L310.781,66.294L310.781,66.294L317.79,68.189L324.728,70.328L331.587,72.707L338.359,75.324L345.036,78.177L351.608,81.26ZM199.724,69.108L199.24,69.199L201.118,68.613L201.476,68.476L203.775,67.809L203.88,67.827L204.493,67.72L202.919,68.177L201.98,68.455L201.234,68.668ZM138.861,98.916L137.645,99.798L144.749,94.923L146.947,93.601L149.925,92.023L155.057,88.971L160.405,86.152L168.097,82.339L166.92,83.342L166.416,84.001L162.813,86.225L160.885,87.769L154.28,91.304L151.381,93.445L156.115,91.733L154.352,93.25L146.749,98.784L143.091,101.565L140.472,104.704L137.334,107.591L136.028,109.269L131.625,112.202L129.412,112.349L126.637,112.842L127.726,110.182L125.98,110.843L122.14,113.107L120.43,114.497L124.716,112.088L123.088,114.459L118.642,117.99L114.956,122.11L118.15,120.741L115.251,123.85L112.399,124.476L109.792,126.026L112.512,123.032L114.495,121.233L113.509,121.775L112.261,122.31L110.523,123.668L108.882,125.322L107.344,127.047L107.489,126.935L106.876,127.454L107.095,127.058L107.448,126.618L106.799,127.352L106.315,127.839L106.316,127.839L111.301,122.561L116.467,117.46L121.808,112.542L127.318,107.814L132.989,103.281L138.815,98.949ZM55.85,228.163L55.729,228.943L55.277,231.237L54.813,234.444L54.34,237.771L54.05,240.876L53.534,245.61L53.453,248.287L53.594,251.526L53.927,251.665L54.283,254.367L54.79,259.541L54.945,261.407L54.965,270.219L55.255,273.933L54.913,277.329L56.148,282.846L57.688,283.63L59.797,289.83L60.844,291.78L64.794,296.554L68.925,305.6L71.328,308.011L72.928,314.121L73.658,321.817L72.053,326.984L71.563,332.505L71.421,334.66L74.252,345.673L74.905,348.901L76.494,356.213L77.315,360.107L76.804,360.908L75.834,361.493L75.736,363.077L77.685,367.475L80.242,372.238L81.415,374.5L83.619,378.244L83.619,378.244L79.879,372.021L76.358,365.671L73.061,359.203L69.992,352.623L67.155,345.941L64.552,339.163L62.188,332.298L60.064,325.356L58.184,318.343L56.55,311.269L55.164,304.143L54.028,296.972L53.142,289.766L52.508,282.533L52.128,275.283L52,268.024L52.126,260.765L52.505,253.515L53.137,246.282L54.021,239.076L55.156,231.905ZM201.424,68.418L199.708,68.933L200.159,68.832L197.587,69.676L196.84,69.926L198.629,69.512L203.088,68.185L207.196,67.389L204.008,68.318L199.071,69.559L197.236,70.242L197.236,70.242L195.82,70.774L191.099,72.247L189.846,72.875L195.482,71.359L193.379,72.389L189.557,73.74L186.152,74.795L183.519,75.366L185.628,74.306L182.263,75.365L180.155,76.047L180.477,75.82L179.519,76.201L179.519,76.201L186.262,73.509L193.094,71.054L200.008,68.839ZM227.029,62.63L227.131,62.615L224.63,63.071L224.63,63.071L222.895,63.396L220.829,63.827L216.468,64.647L219.855,64.061L218.378,64.412L213.658,65.338L209.056,66.402L205.364,67.353L204.944,67.431L206.206,67.077L206.206,67.077L213.251,65.322L220.352,63.814ZM201.984,71.359L201.038,71.597L201.463,71.292L201.888,70.992L201.825,70.805L202.128,70.685L204.258,70.026L205.415,69.794L205.459,69.868L204.341,70.511ZM206.245,68.695L205.785,69.048L202.101,70.544L200.462,71.246L198.758,72.28L195.322,73.489L193.235,74.726L189.873,76.566L185.333,77.82L181.696,80.244L178.439,82.496L172.299,84.364L177.296,81.377L175.259,81.766L171.223,84.215L167.179,86.378L165.819,86.454L166.036,85.986L162.603,88.031L166.988,84.466L169.822,82.966L174.059,80.482L173.757,79.991L177.291,78.555L176.306,79.776L178.843,78.834L183.065,77.553L186.624,75.921L188.745,74.949L191.771,73.639L192.619,73.148L195.473,71.452L198.798,70.057L201.092,69.528L205.045,68.427L208.035,68.089ZM215.808,65.331L213.9,65.943L212.144,66.154L207.636,67.146L208.661,66.706L213.886,65.45L212.896,65.801ZM315.05,69.424L315.689,69.808L316.096,70.248L315.987,70.256L314.356,69.752L313.596,69.387L314.264,69.285ZM208.45,67.372L206.951,67.54L207.786,67.247L210.652,66.638L212.042,66.399L212.931,66.316L213.14,66.404L211.899,66.867L210.176,67.41L208.332,67.543ZM234.21,61.605L234.317,61.594L233.31,61.766L229.654,62.302L226.539,62.76L227.818,62.505L227.819,62.505ZM215.107,66.228L214.268,66.278L215.28,65.951L216.704,65.609L217.678,65.551L217.689,65.732L216.218,66.031ZM306.965,67.741L309.64,68.297L310.888,69.118L312.201,69.65L310.61,69.699L308.159,69.166L307.17,68.777L306.523,68.24ZM222.552,64.767L219.35,65.181L218.371,65.047L220.902,64.634L223.738,64.173L223.074,64.538ZM226.93,63.314L225.618,63.546L223.627,63.84L224.954,63.329L226.886,62.821L227.142,62.946L231.608,62.129L232.427,62.294L227.085,63.041L228.89,62.953L228.356,63.186ZM291.744,94.161L287.495,94.474L284.296,93.352L284.333,91.909L284.26,89.104L284.127,87.161L284.205,85.231L287.703,83.153L289.154,81.905L290.682,82.978L287.657,85.299L287.135,89.345L288.517,92.875ZM221.823,65.316L219.546,65.954L217.17,66.31L214.846,66.868L213.352,67.494L212.963,68.109L210.433,68.969L208.59,69.233L209.231,68.669L210.658,67.67L213.954,66.553L217.455,66.017L220.431,65.28L223.053,64.952ZM235.242,62.168L233.822,62.161L233.687,62.084L234.261,61.977L234.86,61.785L235.821,61.615L237.231,61.462L237.198,61.628L236.908,61.852L235.854,62.015ZM255.975,82.865L254.092,83.493L252.847,83.056L253.51,82.653L253.24,82.113L254.843,81.842L254.972,82.463ZM225.101,64.915L225.18,64.72L226.213,64.554L227.452,64.437L228.641,64.378L227.967,64.568L227.531,64.662L226.028,64.893ZM227.787,64.233L226.46,64.346L227.564,64.088L229.24,63.82L230.466,63.514L230.73,63.627L231.936,63.464L232.934,63.452L231.651,63.7L229.431,64.078ZM252.458,79.751L252.155,81.496L250.409,83.065L248.429,84.319L248.308,82.761L247.095,80.657L249.561,79.089L250.437,79.627L251.955,79.098ZM257.248,78.84L258.376,79.391L257.312,80.208L255.353,80.345L253.508,80.013L253.564,79.584L252.676,79.511L252.351,78.782L254.367,78.458L255.096,78.852L255.838,78.425ZM272.359,78.132L271.352,78.541L270.921,79.05L269.989,78.189L269.612,77.912L270.893,78.269L271.251,77.617ZM297.68,74.42L297.536,74.916L295.818,75.077L294.098,74.935L291.596,74.302L290.576,74.29L289.11,73.258L288.892,72.764L290.983,72.96L294.723,73.513ZM226.863,65.955L224.701,66.083L223.464,65.696L226.506,65.067L227.947,65.108L229.95,64.654L232.516,64.617L233.12,64.815L233.436,65.036L230.091,65.481ZM235.286,67.587L234.344,68.199L232.506,68.616L230.185,68.272L229.397,68.532L226.494,68.334L223.444,68.169L223.049,67.675L221.888,67.913L219.175,68.243L217.282,68.172L215.921,68.174L214.802,68.617L215.37,67.688L216.656,66.856L219.316,66.255L221.611,66.201L219.199,66.926L223.071,66.109L224.148,66.373L226.717,66.03L227.708,66.263L228.125,66.543L229.577,65.726L232.808,65.303L235.038,65.117L234.972,65.418L236.145,65.771L234.385,66.057L236.351,66.223L236.362,66.712L235.984,67.089ZM240.23,71.689L237.831,73.27L235.099,72.388L235.782,72.926L237.198,73.457L234.52,74.386L238.989,74.38L238.866,75.432L234.453,76.169L233.55,76.308L229.188,77.677L224.956,80.261L222.171,80.289L219.537,82.666L217.264,84.063L215.287,84.639L212.772,85.043L210.786,86.126L209.488,85.675L208.676,86.678L205.975,89.382L204.729,88.427L203.83,88.367L203.216,89.761L199.774,90.972L192.344,91.413L189.801,91.451L182.475,93.223L180.416,93.043L176.415,93.785L172.142,95.938L166.615,98.437L160.636,101.496L161.72,98.649L162.196,96.431L168.508,91.537L173.541,88.642L178.62,85.808L184.001,83.611L186.692,83.278L188.203,82.3L186.95,82.212L190.173,80.491L192.049,80.298L193.454,79.891L193.909,79.078L198.065,77.768L201.757,76.191L206.532,74.181L210.045,72.677L210.315,71.597L211.79,70.588L214.81,70.192L216.156,69.568L219.281,68.719L221.927,69.532L224.587,68.791L228.245,68.921L230.364,68.793L231.805,69.303L230.911,70.016L232.036,70.533L231.066,71.269L233.918,70.344L236.872,70.691L238.97,70.866Z" fill="var(--land-fill, #e2e8f0)" stroke="var(--land-stroke, #94a3b8)" stroke-width="0.7"/>

          <!-- 30-deg Graticule Layer -->
          <path id="ir-globe-grat" clip-path="url(#mgClip)" class="globe-grat-path" d="M290.74,62.284L275.545,62.376L260,67.087M260,60L260,67.087M229.26,62.284L244.455,62.376L260,67.087M174.914,78.199L195.035,70.901L216.137,66.58L237.902,65.303L260,67.087M52,268L53.002,248.307L55.997,228.804L60.956,209.678L67.833,191.114L76.56,173.29L87.054,156.379L99.214,140.542L112.922,125.933L128.046,112.692L144.441,100.947L161.949,90.811L180.402,82.381L199.621,75.739L219.421,70.948L239.612,68.055L260,67.087M174.914,457.801L154.341,446.509L135.685,431.974L119.287,414.463L105.445,394.292L94.408,371.828L86.379,347.478L81.502,321.685L79.867,294.917L80.734,275.095L83.328,255.204L87.623,235.436L93.579,215.982L101.137,197.029L110.225,178.76L120.755,161.35L132.627,144.967L145.725,129.769L159.923,115.902L175.086,103.5L191.066,92.682L207.71,83.552L224.858,76.199L242.344,70.693L260,67.087M229.26,473.716L213.932,468.778L199.763,458.785L187.112,443.988L176.295,424.76L167.586,401.586L161.204,375.048L157.309,345.814L156,314.622L157.998,274.53L163.917,234.187L173.527,195.144L186.461,158.9L202.221,126.849L220.201,100.222L239.711,80.043L249.806,72.625L260,67.087M260,476L260,464.961L260,433.017L260,383.559L260,321.834L260,240.851L260,164L260,102.983L260,67.087M290.74,473.716L306.068,468.778L320.237,458.785L332.888,443.988L343.705,424.76L352.414,401.586L358.796,375.048L362.691,345.814L364,314.622L362.002,274.53L356.083,234.187L346.473,195.144L333.539,158.9L317.779,126.849L299.799,100.222L280.289,80.043L270.194,72.625L260,67.087M345.086,457.801L365.659,446.509L384.315,431.974L400.713,414.463L414.555,394.292L425.592,371.828L433.621,347.478L438.498,321.685L440.133,294.917L439.266,275.095L436.672,255.204L432.377,235.436L426.421,215.982L418.863,197.029L409.775,178.76L399.245,161.35L387.373,144.967L374.275,129.769L360.077,115.902L344.914,103.5L328.934,92.682L312.29,83.552L295.142,76.199L277.656,70.693L260,67.087M468,268L466.998,248.307L464.003,228.804L459.044,209.678L452.167,191.114L443.44,173.29L432.946,156.379L420.786,140.542L407.078,125.933L391.954,112.692L375.559,100.947L358.051,90.811L339.598,82.381L320.379,75.739L300.579,70.948L280.388,68.055L260,67.087M345.086,78.199L324.965,70.901L303.863,66.58L282.098,65.303L260,67.087M167.884,454.49L169.933,455.454L172.287,456.458L174.808,457.434L177.491,458.382L180.331,459.297L183.323,460.18L186.461,461.029L189.739,461.841L193.15,462.615L196.689,463.35L200.348,464.045L204.121,464.697L208,465.306L211.978,465.871L216.048,466.391L220.201,466.864L224.43,467.289L228.727,467.667L233.083,467.995L237.49,468.275L241.941,468.504L246.425,468.682L250.936,468.81L255.464,468.887L260,468.913L264.536,468.887L269.064,468.81L273.575,468.682L278.059,468.504L282.51,468.275L286.917,467.995L291.273,467.667L295.57,467.289L299.799,466.864L303.952,466.391L308.022,465.871L312,465.306L315.879,464.697L319.652,464.045L323.311,463.35L326.85,462.615L330.261,461.841L333.539,461.029L336.677,460.18L339.669,459.297L342.509,458.382L345.192,457.434L347.713,456.458L350.067,455.454L352.116,454.49M82.047,375.688L82.603,376.552L84.137,378.547L86.005,380.523L88.204,382.476L90.73,384.402L93.579,386.298L96.744,388.16L100.22,389.984L104,391.767L108.077,393.506L112.443,395.198L117.091,396.838L122.01,398.424L127.192,399.954L132.627,401.423L138.304,402.83L144.213,404.171L150.342,405.444L156.68,406.647L163.214,407.777L169.933,408.832L176.824,409.81L183.872,410.71L191.066,411.529L198.391,412.267L205.833,412.92L213.378,413.49L221.012,413.973L228.72,414.37L236.488,414.679L244.3,414.901L252.143,415.034L260,415.078L267.857,415.034L275.7,414.901L283.512,414.679L291.28,414.37L298.988,413.973L306.622,413.49L314.167,412.92L321.609,412.267L328.934,411.529L336.128,410.71L343.176,409.81L350.067,408.832L356.786,407.777L363.32,406.647L369.658,405.444L375.787,404.171L381.696,402.83L387.373,401.423L392.808,399.954L397.99,398.424L402.909,396.838L407.557,395.198L411.923,393.506L416,391.767L419.78,389.984L423.256,388.16L426.421,386.298L429.27,384.402L431.796,382.476L433.995,380.523L435.863,378.547L437.397,376.552L437.953,375.688M52,268L52.198,270.348L52.792,272.692L53.779,275.027L55.16,277.348L56.93,279.652L59.087,281.933L61.627,284.188L64.544,286.412L67.833,288.602L71.488,290.751L75.502,292.858L79.867,294.917L84.575,296.925L89.616,298.878L94.983,300.772L100.663,302.604L106.646,304.37L112.922,306.067L119.477,307.691L126.3,309.24L133.378,310.71L140.696,312.099L148.242,313.403L156,314.622L163.956,315.752L172.095,316.791L180.402,317.736L188.86,318.588L197.453,319.343L206.166,320L214.981,320.558L223.881,321.016L232.851,321.374L241.872,321.63L250.927,321.783L260,321.834L269.073,321.783L278.128,321.63L287.149,321.374L296.119,321.016L305.019,320.558L313.834,320L322.547,319.343L331.14,318.588L339.598,317.736L347.905,316.791L356.044,315.752L364,314.622L371.758,313.403L379.304,312.099L386.622,310.71L393.7,309.24L400.523,307.691L407.078,306.067L413.354,304.37L419.337,302.604L425.017,300.772L430.384,298.878L435.425,296.925L440.133,294.917L444.498,292.858L448.512,290.751L452.167,288.602L455.456,286.412L458.373,284.188L460.913,281.933L463.07,279.652L464.84,277.348L466.221,275.027L467.208,272.692L467.802,270.348L468,268M82.047,160.312L81.408,161.458L80.552,163.48L80.038,165.51L79.867,167.544L80.038,169.577L80.552,171.607L81.408,173.629L82.603,175.64L84.137,177.635L86.005,179.61L88.204,181.563L90.73,183.489L93.579,185.385L96.744,187.247L100.22,189.071L104,190.855L108.077,192.594L112.443,194.285L117.091,195.925L122.01,197.512L127.192,199.041L132.627,200.51L138.304,201.917L144.213,203.258L150.342,204.531L156.68,205.734L163.214,206.864L169.933,207.919L176.824,208.898L183.872,209.798L191.066,210.617L198.391,211.354L205.833,212.008L213.378,212.577L221.012,213.061L228.72,213.457L236.488,213.767L244.3,213.988L252.143,214.121L260,214.166L267.857,214.121L275.7,213.988L283.512,213.767L291.28,213.457L298.988,213.061L306.622,212.577L314.167,212.008L321.609,211.354L328.934,210.617L336.128,209.798L343.176,208.898L350.067,207.919L356.786,206.864L363.32,205.734L369.658,204.531L375.787,203.258L381.696,201.917L387.373,200.51L392.808,199.041L397.99,197.512L402.909,195.925L407.557,194.285L411.923,192.594L416,190.855L419.78,189.071L423.256,187.247L426.421,185.385L429.27,183.489L431.796,181.563L433.995,179.61L435.863,177.635L437.397,175.64L438.592,173.629L439.448,171.607L439.962,169.577L440.133,167.544L439.962,165.51L439.448,163.48L438.592,161.458L437.953,160.312M167.884,81.51L167.751,81.576L165.744,82.629L163.917,83.704L162.272,84.798L160.813,85.91L159.544,87.038L158.465,88.179L157.58,89.33L156.89,90.491L156.396,91.659L156.099,92.83L156,94.005L156.099,95.179L156.396,96.351L156.89,97.518L157.58,98.679L158.465,99.831L159.544,100.971L160.813,102.099L162.272,103.211L163.917,104.305L165.744,105.38L167.751,106.434L169.933,107.463L172.287,108.467L174.808,109.444L177.491,110.391L180.331,111.307L183.323,112.19L186.461,113.038L189.739,113.85L193.15,114.624L196.689,115.359L200.348,116.054L204.121,116.706L208,117.316L211.978,117.88L216.048,118.4L220.201,118.873L224.43,119.298L228.727,119.676L233.083,120.005L237.49,120.284L241.941,120.513L246.425,120.692L250.936,120.819L255.464,120.896L260,120.922L264.536,120.896L269.064,120.819L273.575,120.692L278.059,120.513L282.51,120.284L286.917,120.005L291.273,119.676L295.57,119.298L299.799,118.873L303.952,118.4L308.022,117.88L312,117.316L315.879,116.706L319.652,116.054L323.311,115.359L326.85,114.624L330.261,113.85L333.539,113.038L336.677,112.19L339.669,111.307L342.509,110.391L345.192,109.444L347.713,108.467L350.067,107.463L352.249,106.434L354.256,105.38L356.083,104.305L357.728,103.211L359.187,102.099L360.456,100.971L361.535,99.831L362.42,98.679L363.11,97.518L363.604,96.351L363.901,95.179L364,94.005L363.901,92.83L363.604,91.659L363.11,90.491L362.42,89.33L361.535,88.179L360.456,87.038L359.187,85.91L357.728,84.798L356.083,83.704L354.256,82.629L352.249,81.576L352.116,81.51" fill="none" stroke="var(--globe-line, #1e3a8a)" stroke-width="0.6" opacity="0.22"/>

          <!-- Diplomatic Route Network Layer -->
          <g id="ir-globe-routes" clip-path="url(#mgClip)" fill="none" stroke-linecap="round" stroke-width="2">
            <path class="cxg-route route-crimson" d="M107.014,127.077L112.314,123.566L119.773,122.165L129.28,122.895L140.697,125.745L168.569,137.609L201.765,157.066"/><path class="cxg-route route-oxford" d="M201.765,157.066L241.125,238.191L284.694,325.963"/><path class="cxg-route route-gold" d="M201.765,157.066L243.019,159.794L284.989,167.089L325.904,178.643L364.038,193.967L397.782,212.416L425.711,233.21L437.116,244.215L446.647,255.472L454.203,266.862L459.706,278.264"/><path class="cxg-route route-gold" d="M459.706,278.264L462.489,250.167L460.733,222.471L454.476,195.795L443.859,170.738"/><path class="cxg-route route-oxford" d="M195.024,139.752L217.353,140.585L240.246,143.1L263.399,147.263L286.507,153.019L309.266,160.293L331.374,168.988L352.54,178.99L372.485,190.167L390.946,202.37L407.679,215.44L422.462,229.203L435.102,243.479L445.431,258.077L453.313,272.807L458.644,287.474L461.353,301.883"/><path class="cxg-route route-crimson" d="M69.69,184.06L62.824,201.872L57.677,220.261L54.293,239.066L52.702,258.122L52.918,277.265L54.939,296.328L58.748,315.143L64.31,333.547"/><path class="cxg-route route-oxford" d="M461.353,301.883L451.858,308.996L437.897,315.155L419.796,320.216L397.975,324.061L372.943,326.602L345.281,327.779L284.694,325.963"/>
          </g>

          <!-- Sovereign Capital Nodes Layer -->
          <g id="ir-globe-nodes" clip-path="url(#mgClip)" stroke="var(--lms-surface, #ffffff)" stroke-width="1.8">
            <circle class="cxg-node" cx="105.2" cy="129.6" r="4.8" fill="var(--globe-route-crimson, #e11d48)" style=""/><circle class="cxg-node" cx="201.8" cy="157.1" r="4.8" fill="var(--globe-route-oxford, #1e3a8a)" style=""/><circle class="cxg-node" cx="419.1" cy="136.1" r="4.8" fill="var(--globe-route-gold, #d97706)" style=""/><circle class="cxg-node" cx="284.7" cy="326.0" r="4.8" fill="var(--globe-route-oxford, #1e3a8a)" style=""/><circle class="cxg-node" cx="64.3" cy="333.5" r="4.8" fill="var(--globe-route-crimson, #e11d48)" style=""/><circle class="cxg-node" cx="459.7" cy="278.3" r="4.8" fill="var(--globe-route-gold, #d97706)" style=""/><circle class="cxg-node" cx="195.0" cy="139.8" r="4.8" fill="var(--globe-route-oxford, #1e3a8a)" style=""/><circle class="cxg-node" cx="461.4" cy="301.9" r="4.8" fill="var(--globe-route-gold, #d97706)" style=""/>
          </g>

          <!-- Precision Outer Rim -->
          <circle cx="260" cy="268" r="208" fill="none" stroke="var(--globe-line, #1e3a8a)" stroke-width="2.2" opacity="0.65"/>
          <circle cx="260" cy="268" r="206.5" fill="none" stroke="var(--lms-border-strong, #d1d5db)" stroke-width="0.6" opacity="0.45"/>

          <!-- Interactive Drag Hitbox Overlay -->
          <circle id="ir-globe-hitbox" cx="260" cy="268" r="212" fill="#000000" fill-opacity="0.0001" style="cursor: grab; pointer-events: all;"/>
        </svg>

        <!-- Live telemetry & Drag Affordance Tag -->
        <div class="globe-drag-hint" id="globe-drag-hint">
          <span class="globe-hint-icon">✥</span>
          <span class="globe-hint-text" id="globe-telemetry">Click &amp; drag to spin &bull; 0&deg;</span>
        </div>
      </div>
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
      <!-- Live Playable Sandbox: Prisoner's Dilemma (G1 Retrofit) -->
      <div class="playable-sandbox" id="game-theory-sim">
        <div class="sandbox-header">
          <div class="sandbox-header-top">
            <span class="sandbox-tag"><i class="fa fa-gamepad"></i> Interactive Lab 02 &bull; Game Theory</span>
            <div class="sandbox-top-actions">
              <span class="sandbox-status-chip">&bull; Live Arena</span>
              <button type="button" class="sandbox-hud-chip" id="gt-mute-toggle" title="Toggle audio" style="cursor: pointer; border: 1px solid var(--lms-hairline);">
                <i class="fa fa-volume-up" id="gt-mute-icon"></i>
              </button>
            </div>
          </div>
          <div class="sandbox-hud-bar">
            <span class="sandbox-hud-chip" id="gt-round-chip">Round: <b id="gt-round-val">1</b> / 8</span>
            <span class="sandbox-hud-chip is-streak" id="gt-streak-chip">Streak: <b id="gt-streak-val">0</b> (<b id="gt-mult-val">×1</b>)</span>
            <span class="sandbox-hud-chip" id="gt-best-chip">Best: <b id="gt-best-val">0</b> pts</span>
          </div>
        </div>

        <h3 class="sandbox-title">Diplomacy Duel: The Prisoner's Dilemma</h3>
        <p class="sandbox-prompt" id="gt-prompt-text">
          Survive 8 rounds against a classified rival doctrine. Mutual cooperation (+5) earns streak multipliers (&times;1.5 at 3, &times;2 at 5) &mdash; but unilateral defection tempts with +10. Beware betrayal (&minus;10/+10) and mutual defection (&minus;2/&minus;2).
        </p>

        <!-- Active Duel Grid -->
        <div class="sandbox-duel-grid" id="gt-duel-grid">
          <div class="duel-card">
            <span class="duel-role">Your Score (State A)</span>
            <div class="duel-score" id="gt-score-a">0</div>
            <div class="duel-actions" id="gt-actions-row">
              <button type="button" class="btn-sim btn-sim-coop" id="btn-gt-coop" onclick="playGameTheory('cooperate')">🤝 Cooperate (C)</button>
              <button type="button" class="btn-sim btn-sim-defect" id="btn-gt-defect" onclick="playGameTheory('defect')">⚔️ Defect (D)</button>
            </div>
          </div>

          <div class="duel-card">
            <span class="duel-role">Classified Rival (State B)</span>
            <div class="duel-score" id="gt-score-b" style="color: #1e3a8a;">0</div>
            <div style="font-size: 0.775rem; color: var(--lms-ink-tertiary); margin-top: 0.85rem;" id="gt-opp-status">
              Awaiting opening move...
            </div>
          </div>
        </div>

        <!-- Session Debrief Box (Hidden during play) -->
        <div class="sandbox-debrief-card" id="gt-debrief-box" style="display: none;">
          <div class="sandbox-debrief-stars" id="gt-debrief-stars">★★★</div>
          <div class="sandbox-debrief-rank" id="gt-debrief-rank">Master Diplomat</div>
          <div class="sandbox-debrief-reveal" id="gt-debrief-reveal">
            <strong>Rival Declassified:</strong> Tit-for-Tat (Axelrod 1984). Cooperates initially, then replicates your previous move.
          </div>
          <div class="sandbox-debrief-actions">
            <button type="button" class="btn-sim btn-sim-coop" style="flex: initial; padding: 0.5rem 1.25rem;" onclick="resetGameTheorySandbox()">
              <i class="fa fa-refresh"></i> Play Again ↺
            </button>
            <a href="{{ site.baseurl }}/game-theory-ir.html#game-theory-sim" class="btn-sim btn-sim-defect" style="flex: initial; padding: 0.5rem 1.25rem; text-decoration: none; text-align: center; background: #1e3a8a;">
              Full Theory Lesson ➔
            </a>
          </div>
        </div>

        <div class="sandbox-log" id="gt-log" aria-live="polite">
          <div class="sandbox-log-line">&gt; Session initialized. Rival doctrine locked under classified protocol. Choose opening stance.</div>
        </div>
      </div>

      <!-- Complete 10 Diplomatic Decision Labs Catalog with Category Filtering (Option B) -->
      <div class="labs-catalog-pane">
        <div class="labs-catalog-header">
          <div class="labs-catalog-head-row">
            <div class="labs-catalog-title">
              <i class="fa fa-cubes" style="color: #1e3a8a;"></i> Diplomatic Simulation Catalog
            </div>
            <span class="labs-counter-badge" id="labs-active-count">10 Labs</span>
          </div>
          <div class="labs-filter-chips" role="tablist" aria-label="Filter diplomatic labs by category">
            <button type="button" class="labs-filter-btn is-active" data-filter="all">All (10)</button>
            <button type="button" class="labs-filter-btn" data-filter="security">Security (4)</button>
            <button type="button" class="labs-filter-btn" data-filter="strategy">Strategy (3)</button>
            <button type="button" class="labs-filter-btn" data-filter="governance">Governance (3)</button>
          </div>
        </div>

        <div class="labs-scroll-pane" id="labs-scroll-pane">
          <!-- Lab 01 -->
          <article class="lab-card-sm" data-cat="security" data-lab-id="crisis">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #dc2626;">Lab 01 &bull; FPA Model</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 3-4 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="crisis"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Crisis Command: Thirteen Days</h4>
              <p class="lab-card-desc">Navigate Graham Allison's bureaucratic models in a naval missile crisis across 3 decision acts with DEFCON timers.</p>
            </div>
            <a href="{{ site.baseurl }}/models-fpdm.html#crisis-sim" class="lab-card-link">Launch Simulator ➔</a>
          </article>

          <!-- Lab 02 -->
          <article class="lab-card-sm is-featured-lab" data-cat="strategy" data-lab-id="game_theory">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #059669;">Lab 02 &bull; Game Theory &bull; Featured Live</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 4 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="game_theory"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Diplomacy Duel: Prisoner's Dilemma</h4>
              <p class="lab-card-desc">8-round strategic duel against classified rival doctrines. Chain cooperation streaks, decode SIGINT, and beat your best score.</p>
            </div>
            <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
              <a href="#game-theory-sim" class="lab-card-link" onclick="document.getElementById('game-theory-sim').scrollIntoView({behavior:'smooth'}); return false;">Play Live Sandbox ↰</a>
              <a href="{{ site.baseurl }}/game-theory-ir.html#game-theory-sim" class="lab-card-link" style="color: var(--lms-ink-tertiary); font-size: 0.78rem;">Full Lesson ➔</a>
            </div>
          </article>

          <!-- Lab 03 -->
          <article class="lab-card-sm" data-cat="governance" data-lab-id="wto">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #7c3aed;">Lab 03 &bull; Trade Dispute</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 3 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="wto"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Consensus Market: Doha Round Trap</h4>
              <p class="lab-card-desc">Broker package deals across 8 voting blocs with 10 Diplomatic Capital points under WTO Single Undertaking rules.</p>
            </div>
            <a href="{{ site.baseurl }}/wto-decision-making.html#wto-sim" class="lab-card-link">Enter Panel ➔</a>
          </article>

          <!-- Lab 04 -->
          <article class="lab-card-sm" data-cat="security" data-lab-id="security_dilemma">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #dc2626;">Lab 04 &bull; Security Studies</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 3 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="security_dilemma"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Spiral Watch: Security Dilemma Matrix</h4>
              <p class="lab-card-desc">Test Jervis's Spiral Model across 5 rounds of arms competition against a secret Cautious or Opportunistic adversary.</p>
            </div>
            <a href="{{ site.baseurl }}/realism-security.html#security-dilemma-sim" class="lab-card-link">Run Simulator ➔</a>
          </article>

          <!-- Lab 05 -->
          <article class="lab-card-sm" data-cat="governance" data-lab-id="unsc_veto">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #7c3aed;">Lab 05 &bull; Global Governance</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 3 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="unsc_veto"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Veto Gauntlet: UNSC Resolution Chamber</h4>
              <p class="lab-card-desc">Draft Chapter VII resolutions and neutralize P5 red lines with 5 Amendment Tokens under UN Charter Article 27(3).</p>
            </div>
            <a href="{{ site.baseurl }}/un-security.html#unsc-veto-sim" class="lab-card-link">Enter Chamber ➔</a>
          </article>

          <!-- Lab 06 -->
          <article class="lab-card-sm" data-cat="strategy" data-lab-id="treaty_negotiation">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #2563eb;">Lab 06 &bull; Diplomacy</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 4 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="treaty_negotiation"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Two-Table Pressure: Treaty Ratification</h4>
              <p class="lab-card-desc">Putnam's Two-Level Games in action: balance international concessions against domestic ratification to expand the ZOPA.</p>
            </div>
            <a href="{{ site.baseurl }}/tools-diplomacy.html#treaty-negotiation-sim" class="lab-card-link">Negotiate Treaty ➔</a>
          </article>

          <!-- Lab 07 -->
          <article class="lab-card-sm" data-cat="governance" data-lab-id="unclos_zones">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #7c3aed;">Lab 07 &bull; Law of the Sea</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 3 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="unclos_zones"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Zone Runner: UNCLOS Maritime Delimiter</h4>
              <p class="lab-card-desc">Adjudicate 10 maritime sovereignty incidents with 3 tokens. Map rights from Territorial Sea to High Seas.</p>
            </div>
            <a href="{{ site.baseurl }}/law-of-the-sea.html#unclos-zones-sim" class="lab-card-link">Map Maritime Zones ➔</a>
          </article>

          <!-- Lab 08 -->
          <article class="lab-card-sm" data-cat="security" data-lab-id="balance_of_power">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #dc2626;">Lab 08 &bull; Modern History</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 4 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="balance_of_power"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Equilibrium Keeper: 1914 Alliance Scale</h4>
              <p class="lab-card-desc">Absorb 4 July 1914 crisis shocks by reallocating diplomatic alignment to prevent an uncontrollable war cascade.</p>
            </div>
            <a href="{{ site.baseurl }}/road-to-ww1.html#balance-power-sim" class="lab-card-link">Configure Alliances ➔</a>
          </article>

          <!-- Lab 09 -->
          <article class="lab-card-sm" data-cat="strategy" data-lab-id="scs_dispute">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #2563eb;">Lab 09 &bull; ASEAN Regionalism</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 4 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="scs_dispute"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Chair's Gambit: South China Sea Code</h4>
              <p class="lab-card-desc">Chair the ASEAN summit across 3 drafting rounds. Balance claimant sovereignty against regional consensus.</p>
            </div>
            <a href="{{ site.baseurl }}/asean-community.html#scs-dispute-sim" class="lab-card-link">Chair Meeting ➔</a>
          </article>

          <!-- Lab 10 -->
          <article class="lab-card-sm" data-cat="security" data-lab-id="nuclear_deterrence">
            <div>
              <div class="lab-card-head-meta">
                <div class="lab-card-meta-chips">
                  <span class="sandbox-tag" style="color: #dc2626;">Lab 10 &bull; Nuclear Strategy</span>
                  <span class="lab-card-chip"><i class="fa fa-clock-o"></i> ≈ 4 min</span>
                </div>
                <div class="lab-card-status-row">
                  <span class="lab-card-badge-done" hidden><i class="fa fa-check"></i> Completed</span>
                  <span class="lab-card-stars" data-stars-for="nuclear_deterrence"></span>
                </div>
              </div>
              <h4 class="lab-card-title">Second-Strike Ledger: Nuclear Triad Calculator</h4>
              <p class="lab-card-desc">Allocate defense budgets across 4 fiscal years to sustain a survivable second-strike triad under Brodie & Schelling.</p>
            </div>
            <a href="{{ site.baseurl }}/domino-cold-war.html#nuclear-deterrence-sim" class="lab-card-link">Calculate Deterrence ➔</a>
          </article>
        </div>
      </div>
    </div>
  </section>

  <!-- Master Video Companion Channel Showcase -->
  <section style="margin-bottom: 4rem;" id="video-companion">
    <div class="home-section-header">
      <div>
        <h2 class="home-section-title">Official Video Course Companion</h2>
        <div class="home-section-subtitle">Visual mind map explainers and animated concept breakdowns</div>
      </div>
    </div>
    <div style="background: var(--lms-surface); border: 1px solid var(--lms-border-strong); border-radius: var(--lms-radius-lg); padding: 2rem; display: flex; align-items: center; justify-content: space-between; gap: 2rem; flex-wrap: wrap; box-shadow: var(--lms-shadow-md);">
      <div style="flex: 1; min-width: 280px;">
        <span style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--lms-ink-tertiary);">YouTube Channel</span>
        <h3 style="font-size: 1.4rem; font-weight: 750; color: var(--lms-ink-primary); margin: 0.35rem 0 0.5rem;">@IRinANutshell</h3>
        <p style="font-size: 0.95rem; color: var(--lms-ink-secondary); line-height: 1.6; margin: 0 0 1.25rem;">
          Curriculum-aligned animated mind maps and visual explainers accompanying core International Relations modules. Watch our video breakdown of Realism in Global Politics, or explore our growing library of concept deep-dives.
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
      <a href="https://www.youtube.com/watch?v=3VDcQVYty5M" target="_blank" rel="noopener noreferrer" style="width: 320px; background: var(--lms-subtle); border: 1px solid var(--lms-border-strong); border-radius: var(--lms-radius-md); padding: 1rem; display: flex; flex-direction: column; gap: 0.65rem; text-decoration: none; color: inherit; transition: transform 0.2s, box-shadow 0.2s;">
        <div style="width: 100%; height: 170px; border-radius: var(--lms-radius-sm); overflow: hidden; position: relative; background: #000000;">
          <img src="{{ site.baseurl }}/learning-videos/posters/IR_M01_CH030_Basic_Explanation_of_Realism_in_IR_Thumbnail.png" alt="@IRinANutshell Video Poster" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.95;" onerror="this.onerror=null; this.src='https://img.youtube.com/vi/3VDcQVYty5M/maxresdefault.jpg';">
          <div style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; pointer-events: none;">
            <div style="width: 44px; height: 44px; border-radius: 50%; background: rgba(239, 68, 68, 0.9); color: #ffffff; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
              <i class="fa fa-play" style="margin-left: 3px;"></i>
            </div>
          </div>
        </div>
        <div style="font-family: ui-monospace, 'JetBrains Mono', monospace; font-size: 0.75rem; color: var(--lms-ink-tertiary); display: flex; justify-content: space-between;">
          <span>CH030 &bull; Realism in Global Politics</span>
          <span style="color: #ef4444; font-weight: 600;"><i class="fa fa-youtube-play"></i> Watch Now</span>
        </div>
      </a>
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

    const VIDEO_SLUGS = new Set([
      {% for chapter in site.chapters %}
        {% if chapter.youtube_id or chapter.explanatory_video %}
          "{{ chapter.slug }}",
        {% endif %}
      {% endfor %}
    ]);

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
    const CX_DATA = {"series":{"01":"Foundation Series","02":"Core Discipline","03":"Applications & Method","04":"Law, Region & Society","05":"Global Architecture"},"modules":[{"num":"010","name":"Introduction to International Relations","overview":{"slug":"introduction-to-international-relations","title":"Introduction to International Relations"},"lessons":[{"slug":"study-of-international-relations","title":"Study Of International Relations","v":true},{"slug":"globalization-and-global-politics","title":"Globalization And Global Politics","v":true},{"slug":"basic-realism","title":"Basic Explanation of Realism in IR","v":true},{"slug":"basic-liberalism","title":"Basic Explanation of Liberalism in IR","v":true},{"slug":"basic-marxism","title":"Basic Explanation of Marxism in IR","v":true},{"slug":"basic-constructivism","title":"Basic Explanation of Constructivism in IR","v":true},{"slug":"global-finance-and-global-trade-as-agendas","title":"Global Finance And Global Trade As Agendas","v":true},{"slug":"global-environment-as-agendas","title":"Global Environment As Agendas","v":true},{"slug":"global-security-issues","title":"Global Security Issues","v":true},{"slug":"regionalism-in-international-affairs","title":"Regionalism In International Affairs","v":false}]},{"num":"011","name":"Introduction To Social Science","overview":{"slug":"introduction-to-social-science","title":"Introduction To Social Science"},"lessons":[{"slug":"social-science-concept","title":"Social Science Concepts and Epistemology","v":false},{"slug":"history-social-science-role","title":"History and Its Role in Social Science","v":false},{"slug":"culture-social-science","title":"Culture and Social Science","v":false},{"slug":"state-in-society","title":"State in Society","v":false},{"slug":"politics-and-power","title":"Politics, Power, and Authority","v":false},{"slug":"understanding-social-change","title":"Understanding Social Change","v":false}]},{"num":"012","name":"Modern World History","overview":{"slug":"modern-world-history","title":"Modern World History"},"lessons":[{"slug":"history-matters","title":"Why History Matters?","v":false},{"slug":"rennaissance","title":"The Renaissance and the Reformation in Europe","v":false},{"slug":"westphalia","title":"'The Emergence of the Modern Interstate System: The Thirty Years War and Peace of Westphalia'","v":false},{"slug":"road-to-ww1","title":"The Road to the First World War","v":false},{"slug":"after-the-first-world-war","title":"After The First World War","v":false},{"slug":"great-depression","title":"The Great Depression","v":false},{"slug":"twenty-year-crisis","title":"The Twenty-Year Crisis","v":false},{"slug":"brink-ww2","title":"On the Brink of the Second World War","v":false},{"slug":"end-ww2","title":"The Ending of The Second World War","v":true},{"slug":"post-ww","title":"'The Post-War World Order'","v":false},{"slug":"bretton-woods","title":"The Rise of the Bretton Woods Institutions","v":false},{"slug":"domino-cold-war","title":"'When One Falls, They All Will Follow: The Domino Theory and the Cold War'","v":false},{"slug":"cuban-missile-crisis","title":"Cuban Missile Crisis","v":false},{"slug":"detente","title":"Détente of the 1970-1990","v":false},{"slug":"decolonization","title":"Decolonization and Development","v":false},{"slug":"birth-prc","title":"The Birth and Rise of the People’s Republic of China","v":false},{"slug":"end-cold-war","title":"The End of the Cold War","v":false},{"slug":"world-order","title":"The Post-Cold War World Order","v":false},{"slug":"us-hegemony","title":"'Challenges to US Hegemony: Rising China and Russian Resurgence'","v":false}]},{"num":"013","name":"Indonesia Political Perspective","overview":{"slug":"indonesia-political-perspective","title":"Indonesia Political Perspective"},"lessons":[{"slug":"basic-political","title":"Basic Poilitical Concepts","v":false},{"slug":"political-institution","title":"Indonesia Political Institutions, Political Party, And Interest Group","v":false},{"slug":"evolution-party","title":"The Evolution of Indonesia's Political Party System","v":false},{"slug":"civil-military","title":"Civil-Military Relations in Indonesia","v":false},{"slug":"electoral-indonesia","title":"Indonesia's Electoral Landscape","v":false},{"slug":"democracy-indonesia","title":"'Democracy In Indonesia: Decentralization'","v":false},{"slug":"women-indonesia","title":"Women In Indonesian Politics","v":false},{"slug":"religion-society","title":"Religion, Society And Politics","v":false}]},{"num":"021","name":"International Political Economy","overview":{"slug":"introduction-to-international-political-economy","title":"International Political Economy"},"lessons":[{"slug":"introduction-ipe","title":"Introduction To International Trade And Economy","v":false},{"slug":"merchantilism-liberalism","title":"'Approaches to IPE: Mercantilism vs. Liberalism'","v":false},{"slug":"constructivism-marxist","title":"'Approaches to IPE: Constructivism vs. Marxism'","v":false},{"slug":"gatt","title":"'The World Trade Organization: From GATT to Global Trade Guardian'","v":false},{"slug":"tpp-rcep","title":"'Beyond Tariffs: The Deeper Impacts of the TPP and RCEP Agreements'","v":false},{"slug":"trade-politics","title":"The Politics of Trade","v":false},{"slug":"ISI-export","title":"'From ISI to Export Orientation: How Developing Countries Navigated Trade Strategy'","v":false},{"slug":"monetary-system","title":"International Monetary System","v":false},{"slug":"exchange-rates","title":"'The Tug-of-War Over Exchange Rates: Political Interests vs. Economic Welfare'","v":false},{"slug":"neoliberalism-ipe","title":"'Neoliberalism 101: Understanding the Ideology That Dominates Global Trade'","v":false},{"slug":"neoliberalism-policy","title":"'Neoliberalism Explained: The Ideology That Transformed Modern Capitalism'","v":false}]},{"num":"022","name":"Introduction To Security Studies","overview":{"slug":"introduction-to-security-studies","title":"Introduction To Security Studies"},"lessons":[{"slug":"introduction-security","title":"Introduction To Security Studies","v":false},{"slug":"realism-security","title":"Realism In Security Studies","v":false},{"slug":"liberalism-security","title":"Liberalism In Security Studies","v":false},{"slug":"constructivism-others","title":"Constructivism And Other Approach In Security Studies","v":false},{"slug":"institution-security","title":"Institution In International Security","v":false},{"slug":"peace-operations","title":"Peace Operations","v":false},{"slug":"crime-terrorism-insurgency","title":"Crime, Terrorism, And Insurgency","v":false},{"slug":"energy-security","title":"Energy Security","v":false},{"slug":"human-security","title":"Human Security","v":false}]},{"num":"023","name":"Theories Of International Relations","overview":{"slug":"theories-of-international-relations","title":"Theories Of International Relations"},"lessons":[{"slug":"introduction-ir-theories","title":"Introduction To International Relations Theories","v":false},{"slug":"classical-realism","title":"Classical Realism","v":true},{"slug":"liberalism-ir","title":"Liberalism","v":false},{"slug":"neorealism-ir","title":"Neorealism","v":false},{"slug":"neoliberalism-ir","title":"Neoliberalism","v":false},{"slug":"dependency-theory","title":"Dependency Theory","v":false},{"slug":"constructivism-ir","title":"Constructivism","v":false},{"slug":"domestic-politics","title":"'Domestic Politics: Two Level Games'","v":false},{"slug":"feminism-ir","title":"Feminism In International Relations","v":false},{"slug":"rational-choice-theory","title":"Rational Choice Theory","v":false},{"slug":"game-theory-ir","title":"Game Theory","v":false},{"slug":"critical-theory","title":"Critical Theory","v":false}]},{"num":"031","name":"International Relations Research Method","overview":{"slug":"international-relations-research-method","title":"International Relations Research Method"},"lessons":[{"slug":"social-reserach-method","title":"Social Research Methods in International Relations","v":false},{"slug":"research-ir-study","title":"Research Method in International Relations Study","v":false},{"slug":"research-process","title":"Research Process","v":false},{"slug":"qualitative","title":"'Research Method: Qualitative'","v":false},{"slug":"quantitative","title":"'Research Method: Quantitative'","v":false},{"slug":"research-question","title":"Research Question","v":false},{"slug":"literature-review","title":"Literature Review","v":false},{"slug":"observation-method","title":"'IR Research Method: Participant Observation and Focus Group'","v":false},{"slug":"interview-survey","title":"'IR Research Methods: Elite Interviews and Survey Research'","v":false}]},{"num":"032","name":"Diplomacy And International Politics","overview":{"slug":"diplomacy-and-international-politics","title":"Diplomacy And International Politics"},"lessons":[{"slug":"intro-diplo","title":"Introduction To Diplomacy And International Politics","v":false},{"slug":"history-diplomacy","title":"History Of Diplomacy","v":false},{"slug":"modes-diplomacy","title":"Modes of Diplomacy","v":false},{"slug":"actors-diplomacy","title":"The Actors of Diplomacy","v":false},{"slug":"tools-diplomacy","title":"Tools and Instruments Of Diplomacy","v":false},{"slug":"inter-politics","title":"Understanding Issues of International Politics","v":false}]},{"num":"033","name":"Foreign Policy Analysis In International Relations","overview":{"slug":"foreign-policy-analysis-ir","title":"Foreign Policy Analysis In International Relations"},"lessons":[{"slug":"intro-fpa","title":"Introduction To Foreign Policy Analysis And Foreign Policy In International Relations","v":false},{"slug":"level-of-analysis-fpdm","title":"Level Of Analysis In Foreign Policy Decision Making","v":false},{"slug":"models-fpdm","title":"Understanding Models Of Decision Making In Foreign Policy Analysis","v":false},{"slug":"factors-fpdm","title":"Factor Affecting Foreign Policy Decision","v":false},{"slug":"public-opinion-media-fpdm","title":"Public Opinion, Media And Foreign Policy","v":false}]},{"num":"034","name":"Contemporary Issues In Global Politics","overview":{"slug":"contemporary-issues-in-global-politics","title":"Contemporary issues in global politics"},"lessons":[{"slug":"theoritical-perspective","title":"Theoretical Perspectives in Global Politics","v":false},{"slug":"poverty-development-aid","title":"Poverty, Development, and International Aid","v":false},{"slug":"failed-state","title":"Failed State And State-building Interventions","v":false},{"slug":"media-politics","title":"Alternative Media and International Politics","v":false},{"slug":"cyber-warfare","title":"Cyber Warfare","v":false},{"slug":"multiculturalism","title":"Politics Of Multiculturalism","v":false},{"slug":"political-populism","title":"Political Populism","v":false},{"slug":"natural-disaster","title":"Natural Disaster And Global Politics","v":false}]},{"num":"041","name":"Foreign Policy Of Developed Countries","overview":{"slug":"foreign-policy-of-developed-countries","title":"Foreign Policy Of Developed Countries"},"lessons":[{"slug":"history-fpa","title":"The History And Evolution Of Foreign Policy Analysis","v":false},{"slug":"economic-statecraft","title":"Economic Statecraft","v":false},{"slug":"women-foreign-policy","title":"'Women And Foreign Policy: Swedish Feminist Foreign Policy'","v":false},{"slug":"eu-foreign-policy","title":"EU Foreign Policy and Energy Security","v":false},{"slug":"australia-foreign-policy","title":"Australia Foreign Policy and Current Issues","v":false},{"slug":"us-foreign-policy","title":"U.S. Foreign Policy","v":false},{"slug":"japan-foreign-policy","title":"Japan Foreign Policy","v":false}]},{"num":"042","name":"International Law Issues And International Dispute Settlement","overview":{"slug":"international-law-issues-and-international-dispute-settlement","title":"International Law Issues And International Dispute Settlement"},"lessons":[{"slug":"basic-inter-law","title":"Basic Understanding Of International Law","v":false},{"slug":"international-treaties","title":"International Treaties","v":false},{"slug":"subjects-of-international-law","title":"The Subjects Of International Law","v":false},{"slug":"state-and-international-law","title":"State And International Law","v":false},{"slug":"io-law","title":"International Organization","v":false},{"slug":"customary-international-law","title":"Customary International Law","v":false},{"slug":"ngo-and-international-law","title":"NGO And International Law","v":false},{"slug":"territory-law","title":"Territory and International Law","v":false},{"slug":"dispute-settlement","title":"Dispute Settlement","v":false},{"slug":"law-of-the-sea","title":"The Law Of The Sea","v":false},{"slug":"international-criminal-law-and-dispute-settlement","title":"International Criminal Law And Dispute Settlement","v":false},{"slug":"international-courts-and-tribunal","title":"International Courts and Tribunal","v":false},{"slug":"the-use-of-force-in-international-law","title":"The Use Of Force In International Law","v":false},{"slug":"international-human-right-law","title":"International Human Right Law","v":false},{"slug":"international-humanitarian-law","title":"International Humanitarian Law","v":false},{"slug":"international-law-for-environmental-protection","title":"International Law For Environmental Protection","v":false}]},{"num":"043","name":"International Political Economy Of Development","overview":{"slug":"international-political-economy-of-development","title":"International Political Economy Of Development"},"lessons":[{"slug":"study-of-development","title":"Study Of Development","v":false},{"slug":"fifty-years-economic-growth","title":"Fifty Years Of Economic Growth And Development Strategy","v":false},{"slug":"inequality-development","title":"'Inequality And Development: An Overview'","v":false},{"slug":"women-economic-role","title":"Women's Economic Roles And The Development Paradigm","v":false},{"slug":"asian-model","title":"The Asian Model Of Development","v":false},{"slug":"development-in-china-india-chile-african-arab","title":"Development In China, India, Chile, The African And Arab Region","v":false}]},{"num":"044","name":"Regionalism In Southeast Asia Asean Community","overview":{"slug":"regionalism-in-southeast-asia-asean-community","title":"Regionalism In Southeast Asia ASEAN Community"},"lessons":[{"slug":"basic-regionalism","title":"The Basics Of Regionalism","v":false},{"slug":"southeast-asia-region","title":"Southeast Asia As a Region","v":false},{"slug":"the-establishment-of-asean","title":"The Establishment Of ASEAN","v":false},{"slug":"asean-chapter","title":"Understanding the ASEAN Charter","v":false},{"slug":"asean-community","title":"Understanding ASEAN Community","v":false}]},{"num":"045","name":"International Organization In International Relations","overview":{"slug":"international-organization-in-international-relations","title":"International Organization In International Relations"},"lessons":[{"slug":"intro-international-organization","title":"Introduction To International Organization (IO) In IR","v":false},{"slug":"theory-international-organizaton","title":"Theory And Methods of International Organization","v":false},{"slug":"evolution-internationa-organizations","title":"The Evolution of International Organizations","v":false},{"slug":"un-administration","title":"'The United Nations: Introduction'","v":false},{"slug":"un-security","title":"'The United Nations: Maintaining International Peace And Security'","v":false},{"slug":"imf-world-bank","title":"The IMF And The World Bank","v":false}]},{"num":"046","name":"Global Economic Architecture","overview":{"slug":"global-economic-architecture","title":"Global Economic Architecture"},"lessons":[{"slug":"introduction-to-global-economic-architecture","title":"Introduction To Global Economic Architecture","v":false},{"slug":"evolution-global-economic-architecture","title":"The Evolution of the Global Economic Architecture","v":false},{"slug":"economic-hegemony","title":"'Global Economic Architecture: The View on Global Economic Hegemony'","v":false},{"slug":"world-trading-system","title":"World Trading System In The 20th Century And Beyond","v":false},{"slug":"european-economic","title":"The Rise of the European Economic Giant","v":false},{"slug":"global-financial-system","title":"Global Financial System In The 20th Century And Beyond","v":false}]},{"num":"050","name":"Wto And Trade Diplomacy","overview":{"slug":"wto-and-trade-diplomacy","title":"WTO And Trade Diplomacy"},"lessons":[{"slug":"international-trade-as-diplomacy","title":"International Trade As Diplomacy","v":false},{"slug":"transformation-diplomacy-trade","title":"Three Transformation of Diplomacy and International Trade","v":false},{"slug":"industrial-revolution","title":"The Industrial Revolution That Changed Trade Forever","v":false},{"slug":"evolution-global-trade","title":"'From Silk Road to Superhighway: The Evolution of Global Trade Diplomacy'","v":false},{"slug":"pillars-wto","title":"'The 3 Pillars of the WTO: How Law, Economics, and Politics Shaped Global Trade'","v":false},{"slug":"judicial-procedure-wto","title":"'When Negotiations Fail: The Rise of Judicial Procedures in Trade Agreements'","v":false},{"slug":"wto-dispute-settlement","title":"WTO Dispute Settlement Mechanism","v":false},{"slug":"wto-decision-making","title":"How the WTO Makes Decisions","v":false}]}]};
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
      const hasVideo = l.v || (typeof VIDEO_SLUGS !== 'undefined' && VIDEO_SLUGS.has(l.slug));
      const chip = hasVideo ? ' <span class="cx-video-chip">VIDEO</span>' : "";
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

    // Diplomatic Labs Catalog Category Filter Logic (Option B)
    const labFilterBtns = document.querySelectorAll('.labs-filter-btn');
    const labCards = document.querySelectorAll('.labs-scroll-pane .lab-card-sm');
    const labsCountEl = document.getElementById('labs-active-count');

    labFilterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.dataset.filter;
        labFilterBtns.forEach(b => b.classList.remove('is-active'));
        btn.classList.add('is-active');

        let visibleCount = 0;
        labCards.forEach(card => {
          const match = (filter === 'all') || (card.dataset.cat === filter);
          card.style.display = match ? 'flex' : 'none';
          if (match) visibleCount++;
        });

        if (labsCountEl) {
          labsCountEl.textContent = `${visibleCount} Labs`;
        }
      });
    });

    // Dynamic Diplomatic Labs Progress & Stars Hydration (Phase G3)
    function getLabStars(labId, bestScore, isDone) {
      const s = parseInt(bestScore || '0', 10);
      let count = 0;
      switch (labId) {
        case 'crisis':
          count = s >= 100 ? 3 : (s >= 85 ? 2 : (s >= 70 ? 1 : 0));
          break;
        case 'game_theory':
          count = s >= 40 ? 3 : (s >= 15 ? 2 : (s >= 1 ? 1 : 0));
          break;
        case 'wto':
          count = s >= 4 ? 3 : (s >= 1 ? 2 : (s >= 0 && isDone ? 1 : 0));
          break;
        case 'security_dilemma':
          count = s >= 100 ? 3 : (s >= 50 ? 1 : 0);
          break;
        case 'unsc_veto':
          count = s >= 15 ? 3 : (s >= 9 ? 2 : (s >= 6 ? 1 : 0));
          break;
        case 'treaty_negotiation':
          count = s >= 70 ? 3 : (s >= 30 ? 2 : 0);
          break;
        case 'unclos_zones':
          count = s >= 25 ? 3 : (s >= 15 ? 2 : (s >= 5 ? 1 : 0));
          break;
        case 'balance_of_power':
          count = s >= 70 ? 3 : (s >= 40 ? 2 : 0);
          break;
        case 'scs_dispute':
          count = s >= 60 ? 3 : (s >= 30 ? 2 : 0);
          break;
        case 'nuclear_deterrence':
          count = s >= 80 ? 3 : (s >= 50 ? 2 : 0);
          break;
        default:
          count = 0;
      }
      return (count === 0 && isDone) ? 1 : count;
    }

    function renderStarsHtml(count) {
      let html = '';
      for (let i = 1; i <= 3; i++) {
        if (i <= count) {
          html += '<i class="fa fa-star" style="color: #d97706; margin-right: 2px;"></i>';
        } else {
          html += '<i class="fa fa-star is-empty" style="color: var(--lms-ink-muted, #94a3b8); opacity: 0.35; margin-right: 2px;"></i>';
        }
      }
      return html;
    }

    window.renderLabCardsProgress = function() {
      const cards = document.querySelectorAll('.labs-scroll-pane .lab-card-sm');
      cards.forEach(card => {
        const labId = card.dataset.labId;
        if (!labId) return;
        const isDone = localStorage.getItem('labs_completed_' + labId) === 'true';
        const best = localStorage.getItem('labs_best_' + labId);
        const stars = getLabStars(labId, best, isDone);

        const doneBadge = card.querySelector('.lab-card-badge-done');
        if (doneBadge) {
          doneBadge.hidden = !isDone;
        }

        const starsEl = card.querySelector('.lab-card-stars');
        if (starsEl) {
          starsEl.innerHTML = renderStarsHtml(stars);
        }

        if (isDone) {
          card.classList.add('is-completed-lab');
        }
      });
    };

    window.renderLabCardsProgress();
    initGameTheorySandbox();
});

// =============================================================================
// Upgraded Playable Prisoner's Dilemma Simulator Logic (Phase G1 & G3 Standard)
// =============================================================================
const GT_RIVALS = [
  { id: 'tft', name: 'Tit-for-Tat', cite: 'Axelrod 1984', desc: 'Starts cooperative, then exactly mirrors your previous action.', hint: 'SIGINT Intercept: Rival transmissions mirror our exact previous posture. A mirror doctrine is confirmed.' },
  { id: 'grim', name: 'Grim Trigger', cite: 'Friedman 1971', desc: 'Cooperates indefinitely until provoked once, then defects irreversibly.', hint: 'SIGINT Intercept: Hostile red-lines detected. One defection triggers permanent retaliatory lockout.' },
  { id: 'predator', name: 'The Predator', cite: 'Structural Realism', desc: 'Unconditionally defects to maximize relative gains and exploit sucker payoffs.', hint: 'SIGINT Intercept: Offensive naval posture intercepted. Rival has zero intention of disarmament.' },
  { id: 'wildcard', name: 'The Wildcard', cite: 'Stochastic Model', desc: 'Stochastic behavior alternating between 60% defection and 40% cooperation.', hint: 'SIGINT Intercept: Chaotic diplomatic signals. Rival decision-making exhibits coin-flip stochastic drift.' },
  { id: 'pavlov', name: 'Pavlov (Win-Stay / Lose-Shift)', cite: 'Nowak & Sigmund 1993', desc: 'Repeats recent choice if rewarded (+5 or +10); shifts choice if penalized.', hint: 'SIGINT Intercept: Behavioral pattern confirms habituation. Rival switches only after adverse payoffs.' }
];

let gtState = {
  round: 1,
  scoreA: 0,
  scoreB: 0,
  streak: 0,
  rival: null,
  history: [],
  hasDefected: false,
  muted: false
};

function initGameTheorySandbox() {
  const rivalIdx = Math.floor(Math.random() * GT_RIVALS.length);
  gtState.rival = GT_RIVALS[rivalIdx];
  gtState.round = 1;
  gtState.scoreA = 0;
  gtState.scoreB = 0;
  gtState.streak = 0;
  gtState.history = [];
  gtState.hasDefected = false;

  try {
    gtState.muted = localStorage.getItem('labs_muted_v1') === '1';
  } catch(e) {}

  const muteBtn = document.getElementById('gt-mute-toggle');
  const muteIcon = document.getElementById('gt-mute-icon');
  if (muteBtn && muteIcon) {
    muteIcon.className = gtState.muted ? 'fa fa-volume-off' : 'fa fa-volume-up';
    muteBtn.onclick = function() {
      gtState.muted = !gtState.muted;
      localStorage.setItem('labs_muted_v1', gtState.muted ? '1' : '0');
      muteIcon.className = gtState.muted ? 'fa fa-volume-off' : 'fa fa-volume-up';
    };
  }

  updateSandboxHUD();
}

function updateSandboxHUD() {
  const roundVal = document.getElementById('gt-round-val');
  const streakVal = document.getElementById('gt-streak-val');
  const multVal = document.getElementById('gt-mult-val');
  const bestVal = document.getElementById('gt-best-val');
  const scoreA = document.getElementById('gt-score-a');
  const scoreB = document.getElementById('gt-score-b');

  const mult = gtState.streak >= 5 ? 2 : (gtState.streak >= 3 ? 1.5 : 1);
  if (roundVal) roundVal.textContent = Math.min(gtState.round, 8);
  if (streakVal) streakVal.textContent = gtState.streak;
  if (multVal) multVal.textContent = '×' + mult;
  if (scoreA) scoreA.textContent = gtState.scoreA;
  if (scoreB) scoreB.textContent = gtState.scoreB;

  const savedBest = localStorage.getItem('labs_best_game_theory') || '0';
  if (bestVal) bestVal.textContent = savedBest;
}

function getRivalMove(playerMove) {
  const r = gtState.rival.id;
  const h = gtState.history;

  if (r === 'predator') return 'defect';
  if (r === 'wildcard') return Math.random() < 0.6 ? 'defect' : 'cooperate';

  if (h.length === 0) return 'cooperate'; // Opening round friendly
  const last = h[h.length - 1];

  if (r === 'tft') {
    return last.player;
  }
  if (r === 'grim') {
    return gtState.hasDefected ? 'defect' : 'cooperate';
  }
  if (r === 'pavlov') {
    // Win (CC or DC) -> stay with last move; Lose (CD or DD) -> switch
    const won = (last.player === 'cooperate' && last.opp === 'cooperate') ||
                (last.player === 'cooperate' && last.opp === 'defect');
    return won ? last.opp : (last.opp === 'cooperate' ? 'defect' : 'cooperate');
  }
  return 'cooperate';
}

function playSandboxSound(type) {
  if (gtState.muted) return;
  if (window.LabGame && window.LabGame.sfx && typeof window.LabGame.sfx[type] === 'function') {
    window.LabGame.sfx[type]();
  }
}

window.playGameTheory = function(playerMove) {
  if (gtState.round > 8) return;

  const currentRound = gtState.round;
  const oppMove = getRivalMove(playerMove);
  if (playerMove === 'defect') gtState.hasDefected = true;

  let changeA = 0, changeB = 0;
  let mult = gtState.streak >= 5 ? 2 : (gtState.streak >= 3 ? 1.5 : 1);
  let roundDesc = '';

  if (playerMove === 'cooperate' && oppMove === 'cooperate') {
    gtState.streak++;
    mult = gtState.streak >= 5 ? 2 : (gtState.streak >= 3 ? 1.5 : 1);
    changeA = Math.round(5 * mult);
    changeB = 5;
    roundDesc = `Mutual Cooperation (+${changeA}, +5) — ${mult > 1 ? 'STREAK ×' + mult + '!' : 'Pareto optimal'}`;
    playSandboxSound('good');
  } else if (playerMove === 'defect' && oppMove === 'cooperate') {
    gtState.streak = 0;
    changeA = 10;
    changeB = -10;
    roundDesc = 'Temptation exploitation (+10, −10). Opponent betrayed.';
    playSandboxSound('click');
  } else if (playerMove === 'cooperate' && oppMove === 'defect') {
    gtState.streak = 0;
    changeA = -10;
    changeB = 10;
    roundDesc = "Sucker's payoff (−10, +10). Rival exploited your disarmament!";
    playSandboxSound('bad');
  } else {
    gtState.streak = 0;
    changeA = -2;
    changeB = -2;
    roundDesc = 'Mutual Defection (−2, −2) — Nash equilibrium trap.';
    playSandboxSound('bad');
  }

  gtState.scoreA += changeA;
  gtState.scoreB += changeB;
  gtState.history.push({ player: playerMove, opp: oppMove });

  const statusEl = document.getElementById('gt-opp-status');
  if (statusEl) {
    statusEl.textContent = `Round ${currentRound}: Rival played ${oppMove.toUpperCase()}`;
  }

  const log = document.getElementById('gt-log');
  if (log) {
    const newLine = document.createElement('div');
    newLine.className = 'sandbox-log-line';
    newLine.innerHTML = `<strong>R${currentRound}:</strong> You [${playerMove.toUpperCase()}], Rival [${oppMove.toUpperCase()}] &bull; ${roundDesc}`;
    log.insertBefore(newLine, log.firstChild);

    // Round 4 SIGINT Intercept card drop
    if (currentRound === 4) {
      const intelLine = document.createElement('div');
      intelLine.className = 'sandbox-log-line';
      intelLine.style.background = 'rgba(217, 119, 6, 0.08)';
      intelLine.style.color = '#b45309';
      intelLine.style.fontWeight = '700';
      intelLine.innerHTML = `<i class="fa fa-shield"></i> <strong>INTEL &bull; ROUND 5:</strong> ${gtState.rival.hint}`;
      log.insertBefore(intelLine, log.firstChild);
    }
  }

  gtState.round++;
  updateSandboxHUD();

  if (gtState.round > 8) {
    finishGameTheorySandbox();
  }
};

function finishGameTheorySandbox() {
  const duelGrid = document.getElementById('gt-duel-grid');
  const debriefBox = document.getElementById('gt-debrief-box');
  const promptText = document.getElementById('gt-prompt-text');
  const starsEl = document.getElementById('gt-debrief-stars');
  const rankEl = document.getElementById('gt-debrief-rank');
  const revealEl = document.getElementById('gt-debrief-reveal');

  const score = gtState.scoreA;
  let stars = 0, rank = '';
  if (score >= 40) {
    stars = 3; rank = 'Master Diplomat';
  } else if (score >= 15) {
    stars = 2; rank = 'Seasoned Negotiator';
  } else if (score > 0) {
    stars = 1; rank = 'Survivor';
  } else {
    stars = 0; rank = 'Exploited';
  }

  if (starsEl) starsEl.textContent = stars === 3 ? '★★★' : (stars === 2 ? '★★☆' : (stars === 1 ? '★☆☆' : '☆☆☆'));
  if (rankEl) rankEl.textContent = `${rank} (${score} pts)`;
  if (revealEl) {
    revealEl.innerHTML = `<strong>Rival Declassified: ${gtState.rival.name}</strong> (${gtState.rival.cite}). ${gtState.rival.desc}`;
  }

  if (promptText) {
    promptText.textContent = `Session Debrief & After-Action Report. You achieved ${stars} / 3 stars with a final score of ${score} pts.`;
  }

  if (duelGrid) duelGrid.style.display = 'none';
  if (debriefBox) debriefBox.style.display = 'block';

  // Persistence to localStorage & shared LabGame core
  try {
    localStorage.setItem('labs_completed_game_theory', 'true');
    const prevBest = parseInt(localStorage.getItem('labs_best_game_theory') || '0', 10);
    if (score > prevBest) {
      localStorage.setItem('labs_best_game_theory', String(score));
    }
    if (window.LabGame) {
      if (window.LabGame.flags) window.LabGame.flags.complete('game_theory');
      if (window.LabGame.best) window.LabGame.best.submit('game_theory', score);
    }
  } catch(e) {}

  playSandboxSound(stars === 3 ? 'fanfare' : 'reveal');

  // Immediately reflect update on the catalog cards to the right
  if (typeof window.renderLabCardsProgress === 'function') {
    window.renderLabCardsProgress();
  }
}

window.resetGameTheorySandbox = function() {
  const duelGrid = document.getElementById('gt-duel-grid');
  const debriefBox = document.getElementById('gt-debrief-box');
  const promptText = document.getElementById('gt-prompt-text');
  const log = document.getElementById('gt-log');

  if (duelGrid) duelGrid.style.display = 'grid';
  if (debriefBox) debriefBox.style.display = 'none';
  if (promptText) {
    promptText.textContent = "Survive 8 rounds against a classified rival doctrine. Mutual cooperation (+5) earns streak multipliers (\u00D71.5 at 3, \u00D72 at 5) — but unilateral defection tempts with +10. Beware betrayal (−10/+10) and mutual defection (−2/−2).";
  }
  if (log) {
    log.innerHTML = '<div class="sandbox-log-line">&gt; New session initialized. Rival doctrine locked under classified protocol. Choose opening stance.</div>';
  }

  initGameTheorySandbox();
};


// Interactive 3D Vector Globe Controller
  (function() {
    // https://d3js.org/d3-array/ v3.2.4 Copyright 2010-2023 Mike Bostock
!function(t,n){"object"==typeof exports&&"undefined"!=typeof module?n(exports):"function"==typeof define&&define.amd?define(["exports"],n):n((t="undefined"!=typeof globalThis?globalThis:t||self).d3=t.d3||{})}(this,(function(t){"use strict";function n(t,n){return null==t||null==n?NaN:t<n?-1:t>n?1:t>=n?0:NaN}function r(t,n){return null==t||null==n?NaN:n<t?-1:n>t?1:n>=t?0:NaN}function e(t){let e,f,i;function u(t,n,r=0,o=t.length){if(r<o){if(0!==e(n,n))return o;do{const e=r+o>>>1;f(t[e],n)<0?r=e+1:o=e}while(r<o)}return r}return 2!==t.length?(e=n,f=(r,e)=>n(t(r),e),i=(n,r)=>t(n)-r):(e=t===n||t===r?t:o,f=t,i=t),{left:u,center:function(t,n,r=0,e=t.length){const o=u(t,n,r,e-1);return o>r&&i(t[o-1],n)>-i(t[o],n)?o-1:o},right:function(t,n,r=0,o=t.length){if(r<o){if(0!==e(n,n))return o;do{const e=r+o>>>1;f(t[e],n)<=0?r=e+1:o=e}while(r<o)}return r}}}function o(){return 0}function f(t){return null===t?NaN:+t}const i=e(n),u=i.right,l=i.left,c=e(f).center;var s=u;const a=d(m),h=d((function(t){const n=m(t);return(t,r,e,o,f)=>{n(t,r,(e<<=2)+0,(o<<=2)+0,f<<=2),n(t,r,e+1,o+1,f),n(t,r,e+2,o+2,f),n(t,r,e+3,o+3,f)}}));function d(t){return function(n,r,e=r){if(!((r=+r)>=0))throw new RangeError("invalid rx");if(!((e=+e)>=0))throw new RangeError("invalid ry");let{data:o,width:f,height:i}=n;if(!((f=Math.floor(f))>=0))throw new RangeError("invalid width");if(!((i=Math.floor(void 0!==i?i:o.length/f))>=0))throw new RangeError("invalid height");if(!f||!i||!r&&!e)return n;const u=r&&t(r),l=e&&t(e),c=o.slice();return u&&l?(p(u,c,o,f,i),p(u,o,c,f,i),p(u,c,o,f,i),y(l,o,c,f,i),y(l,c,o,f,i),y(l,o,c,f,i)):u?(p(u,o,c,f,i),p(u,c,o,f,i),p(u,o,c,f,i)):l&&(y(l,o,c,f,i),y(l,c,o,f,i),y(l,o,c,f,i)),n}}function p(t,n,r,e,o){for(let f=0,i=e*o;f<i;)t(n,r,f,f+=e,1)}function y(t,n,r,e,o){for(let f=0,i=e*o;f<e;++f)t(n,r,f,f+i,e)}function m(t){const n=Math.floor(t);if(n===t)return function(t){const n=2*t+1;return(r,e,o,f,i)=>{if(!((f-=i)>=o))return;let u=t*e[o];const l=i*t;for(let t=o,n=o+l;t<n;t+=i)u+=e[Math.min(f,t)];for(let t=o,c=f;t<=c;t+=i)u+=e[Math.min(f,t+l)],r[t]=u/n,u-=e[Math.max(o,t-l)]}}(t);const r=t-n,e=2*t+1;return(t,o,f,i,u)=>{if(!((i-=u)>=f))return;let l=n*o[f];const c=u*n,s=c+u;for(let t=f,n=f+c;t<n;t+=u)l+=o[Math.min(i,t)];for(let n=f,a=i;n<=a;n+=u)l+=o[Math.min(i,n+c)],t[n]=(l+r*(o[Math.max(f,n-s)]+o[Math.min(i,n+s)]))/e,l-=o[Math.max(f,n-c)]}}function g(t,n){let r=0;if(void 0===n)for(let n of t)null!=n&&(n=+n)>=n&&++r;else{let e=-1;for(let o of t)null!=(o=n(o,++e,t))&&(o=+o)>=o&&++r}return r}function v(t){return 0|t.length}function M(t){return!(t>0)}function w(t){return"object"!=typeof t||"length"in t?t:Array.from(t)}function b(t,n){let r,e=0,o=0,f=0;if(void 0===n)for(let n of t)null!=n&&(n=+n)>=n&&(r=n-o,o+=r/++e,f+=r*(n-o));else{let i=-1;for(let u of t)null!=(u=n(u,++i,t))&&(u=+u)>=u&&(r=u-o,o+=r/++e,f+=r*(u-o))}if(e>1)return f/(e-1)}function A(t,n){const r=b(t,n);return r?Math.sqrt(r):r}function x(t,n){let r,e;if(void 0===n)for(const n of t)null!=n&&(void 0===r?n>=n&&(r=e=n):(r>n&&(r=n),e<n&&(e=n)));else{let o=-1;for(let f of t)null!=(f=n(f,++o,t))&&(void 0===r?f>=f&&(r=e=f):(r>f&&(r=f),e<f&&(e=f)))}return[r,e]}class N{constructor(){this._partials=new Float64Array(32),this._n=0}add(t){const n=this._partials;let r=0;for(let e=0;e<this._n&&e<32;e++){const o=n[e],f=t+o,i=Math.abs(t)<Math.abs(o)?t-(f-o):o-(f-t);i&&(n[r++]=i),t=f}return n[r]=t,this._n=r+1,this}valueOf(){const t=this._partials;let n,r,e,o=this._n,f=0;if(o>0){for(f=t[--o];o>0&&(n=f,r=t[--o],f=n+r,e=r-(f-n),!e););o>0&&(e<0&&t[o-1]<0||e>0&&t[o-1]>0)&&(r=2*e,n=f+r,r==n-f&&(f=n))}return f}}class InternMap extends Map{constructor(t,n=k){if(super(),Object.defineProperties(this,{_intern:{value:new Map},_key:{value:n}}),null!=t)for(const[n,r]of t)this.set(n,r)}get(t){return super.get(E(this,t))}has(t){return super.has(E(this,t))}set(t,n){return super.set(_(this,t),n)}delete(t){return super.delete(S(this,t))}}class InternSet extends Set{constructor(t,n=k){if(super(),Object.defineProperties(this,{_intern:{value:new Map},_key:{value:n}}),null!=t)for(const n of t)this.add(n)}has(t){return super.has(E(this,t))}add(t){return super.add(_(this,t))}delete(t){return super.delete(S(this,t))}}function E({_intern:t,_key:n},r){const e=n(r);return t.has(e)?t.get(e):r}function _({_intern:t,_key:n},r){const e=n(r);return t.has(e)?t.get(e):(t.set(e,r),r)}function S({_intern:t,_key:n},r){const e=n(r);return t.has(e)&&(r=t.get(e),t.delete(e)),r}function k(t){return null!==t&&"object"==typeof t?t.valueOf():t}function T(t){return t}function F(t,...n){return U(t,T,T,n)}function I(t,...n){return U(t,Array.from,T,n)}function j(t,n){for(let r=1,e=n.length;r<e;++r)t=t.flatMap((t=>t.pop().map((([n,r])=>[...t,n,r]))));return t}function q(t,n,...r){return U(t,T,n,r)}function R(t,n,...r){return U(t,Array.from,n,r)}function O(t){if(1!==t.length)throw new Error("duplicate key");return t[0]}function U(t,n,r,e){return function t(o,f){if(f>=e.length)return r(o);const i=new InternMap,u=e[f++];let l=-1;for(const t of o){const n=u(t,++l,o),r=i.get(n);r?r.push(t):i.set(n,[t])}for(const[n,r]of i)i.set(n,t(r,f));return n(i)}(t,0)}function L(t,n){return Array.from(n,(n=>t[n]))}function P(t,...n){if("function"!=typeof t[Symbol.iterator])throw new TypeError("values is not iterable");t=Array.from(t);let[r]=n;if(r&&2!==r.length||n.length>1){const e=Uint32Array.from(t,((t,n)=>n));return n.length>1?(n=n.map((n=>t.map(n))),e.sort(((t,r)=>{for(const e of n){const n=C(e[t],e[r]);if(n)return n}}))):(r=t.map(r),e.sort(((t,n)=>C(r[t],r[n])))),L(t,e)}return t.sort(z(r))}function z(t=n){if(t===n)return C;if("function"!=typeof t)throw new TypeError("compare is not a function");return(n,r)=>{const e=t(n,r);return e||0===e?e:(0===t(r,r))-(0===t(n,n))}}function C(t,n){return(null==t||!(t>=t))-(null==n||!(n>=n))||(t<n?-1:t>n?1:0)}var D=Array.prototype.slice;function G(t){return()=>t}const B=Math.sqrt(50),H=Math.sqrt(10),J=Math.sqrt(2);function K(t,n,r){const e=(n-t)/Math.max(0,r),o=Math.floor(Math.log10(e)),f=e/Math.pow(10,o),i=f>=B?10:f>=H?5:f>=J?2:1;let u,l,c;return o<0?(c=Math.pow(10,-o)/i,u=Math.round(t*c),l=Math.round(n*c),u/c<t&&++u,l/c>n&&--l,c=-c):(c=Math.pow(10,o)*i,u=Math.round(t/c),l=Math.round(n/c),u*c<t&&++u,l*c>n&&--l),l<u&&.5<=r&&r<2?K(t,n,2*r):[u,l,c]}function Q(t,n,r){if(!((r=+r)>0))return[];if((t=+t)===(n=+n))return[t];const e=n<t,[o,f,i]=e?K(n,t,r):K(t,n,r);if(!(f>=o))return[];const u=f-o+1,l=new Array(u);if(e)if(i<0)for(let t=0;t<u;++t)l[t]=(f-t)/-i;else for(let t=0;t<u;++t)l[t]=(f-t)*i;else if(i<0)for(let t=0;t<u;++t)l[t]=(o+t)/-i;else for(let t=0;t<u;++t)l[t]=(o+t)*i;return l}function V(t,n,r){return K(t=+t,n=+n,r=+r)[2]}function W(t,n,r){let e;for(;;){const o=V(t,n,r);if(o===e||0===o||!isFinite(o))return[t,n];o>0?(t=Math.floor(t/o)*o,n=Math.ceil(n/o)*o):o<0&&(t=Math.ceil(t*o)/o,n=Math.floor(n*o)/o),e=o}}function X(t){return Math.max(1,Math.ceil(Math.log(g(t))/Math.LN2)+1)}function Y(){var t=T,n=x,r=X;function e(e){Array.isArray(e)||(e=Array.from(e));var o,f,i,u=e.length,l=new Array(u);for(o=0;o<u;++o)l[o]=t(e[o],o,e);var c=n(l),a=c[0],h=c[1],d=r(l,a,h);if(!Array.isArray(d)){const t=h,r=+d;if(n===x&&([a,h]=W(a,h,r)),(d=Q(a,h,r))[0]<=a&&(i=V(a,h,r)),d[d.length-1]>=h)if(t>=h&&n===x){const t=V(a,h,r);isFinite(t)&&(t>0?h=(Math.floor(h/t)+1)*t:t<0&&(h=(Math.ceil(h*-t)+1)/-t))}else d.pop()}for(var p=d.length,y=0,m=p;d[y]<=a;)++y;for(;d[m-1]>h;)--m;(y||m<p)&&(d=d.slice(y,m),p=m-y);var g,v=new Array(p+1);for(o=0;o<=p;++o)(g=v[o]=[]).x0=o>0?d[o-1]:a,g.x1=o<p?d[o]:h;if(isFinite(i)){if(i>0)for(o=0;o<u;++o)null!=(f=l[o])&&a<=f&&f<=h&&v[Math.min(p,Math.floor((f-a)/i))].push(e[o]);else if(i<0)for(o=0;o<u;++o)if(null!=(f=l[o])&&a<=f&&f<=h){const t=Math.floor((a-f)*i);v[Math.min(p,t+(d[t]<=f))].push(e[o])}}else for(o=0;o<u;++o)null!=(f=l[o])&&a<=f&&f<=h&&v[s(d,f,0,p)].push(e[o]);return v}return e.value=function(n){return arguments.length?(t="function"==typeof n?n:G(n),e):t},e.domain=function(t){return arguments.length?(n="function"==typeof t?t:G([t[0],t[1]]),e):n},e.thresholds=function(t){return arguments.length?(r="function"==typeof t?t:G(Array.isArray(t)?D.call(t):t),e):r},e}function Z(t,n){let r;if(void 0===n)for(const n of t)null!=n&&(r<n||void 0===r&&n>=n)&&(r=n);else{let e=-1;for(let o of t)null!=(o=n(o,++e,t))&&(r<o||void 0===r&&o>=o)&&(r=o)}return r}function $(t,n){let r,e=-1,o=-1;if(void 0===n)for(const n of t)++o,null!=n&&(r<n||void 0===r&&n>=n)&&(r=n,e=o);else for(let f of t)null!=(f=n(f,++o,t))&&(r<f||void 0===r&&f>=f)&&(r=f,e=o);return e}function tt(t,n){let r;if(void 0===n)for(const n of t)null!=n&&(r>n||void 0===r&&n>=n)&&(r=n);else{let e=-1;for(let o of t)null!=(o=n(o,++e,t))&&(r>o||void 0===r&&o>=o)&&(r=o)}return r}function nt(t,n){let r,e=-1,o=-1;if(void 0===n)for(const n of t)++o,null!=n&&(r>n||void 0===r&&n>=n)&&(r=n,e=o);else for(let f of t)null!=(f=n(f,++o,t))&&(r>f||void 0===r&&f>=f)&&(r=f,e=o);return e}function rt(t,n,r=0,e=1/0,o){if(n=Math.floor(n),r=Math.floor(Math.max(0,r)),e=Math.floor(Math.min(t.length-1,e)),!(r<=n&&n<=e))return t;for(o=void 0===o?C:z(o);e>r;){if(e-r>600){const f=e-r+1,i=n-r+1,u=Math.log(f),l=.5*Math.exp(2*u/3),c=.5*Math.sqrt(u*l*(f-l)/f)*(i-f/2<0?-1:1);rt(t,n,Math.max(r,Math.floor(n-i*l/f+c)),Math.min(e,Math.floor(n+(f-i)*l/f+c)),o)}const f=t[n];let i=r,u=e;for(et(t,r,n),o(t[e],f)>0&&et(t,r,e);i<u;){for(et(t,i,u),++i,--u;o(t[i],f)<0;)++i;for(;o(t[u],f)>0;)--u}0===o(t[r],f)?et(t,r,u):(++u,et(t,u,e)),u<=n&&(r=u+1),n<=u&&(e=u-1)}return t}function et(t,n,r){const e=t[n];t[n]=t[r],t[r]=e}function ot(t,r=n){let e,o=!1;if(1===r.length){let f;for(const i of t){const t=r(i);(o?n(t,f)>0:0===n(t,t))&&(e=i,f=t,o=!0)}}else for(const n of t)(o?r(n,e)>0:0===r(n,n))&&(e=n,o=!0);return e}function ft(t,n,r){if(t=Float64Array.from(function*(t,n){if(void 0===n)for(let n of t)null!=n&&(n=+n)>=n&&(yield n);else{let r=-1;for(let e of t)null!=(e=n(e,++r,t))&&(e=+e)>=e&&(yield e)}}(t,r)),(e=t.length)&&!isNaN(n=+n)){if(n<=0||e<2)return tt(t);if(n>=1)return Z(t);var e,o=(e-1)*n,f=Math.floor(o),i=Z(rt(t,f).subarray(0,f+1));return i+(tt(t.subarray(f+1))-i)*(o-f)}}function it(t,n,r=f){if(!isNaN(n=+n)){if(e=Float64Array.from(t,((n,e)=>f(r(t[e],e,t)))),n<=0)return nt(e);if(n>=1)return $(e);var e,o=Uint32Array.from(t,((t,n)=>n)),i=e.length-1,u=Math.floor(i*n);return rt(o,u,0,i,((t,n)=>C(e[t],e[n]))),(u=ot(o.subarray(0,u+1),(t=>e[t])))>=0?u:-1}}function ut(t,n){return[t,n]}function lt(t,r=n){if(1===r.length)return nt(t,r);let e,o=-1,f=-1;for(const n of t)++f,(o<0?0===r(n,n):r(n,e)<0)&&(e=n,o=f);return o}var ct=st(Math.random);function st(t){return function(n,r=0,e=n.length){let o=e-(r=+r);for(;o;){const e=t()*o--|0,f=n[o+r];n[o+r]=n[e+r],n[e+r]=f}return n}}function at(t){if(!(o=t.length))return[];for(var n=-1,r=tt(t,ht),e=new Array(r);++n<r;)for(var o,f=-1,i=e[n]=new Array(o);++f<o;)i[f]=t[f][n];return e}function ht(t){return t.length}function dt(t){return t instanceof InternSet?t:new InternSet(t)}function pt(t,n){const r=t[Symbol.iterator](),e=new Set;for(const t of n){const n=yt(t);if(e.has(n))continue;let o,f;for(;({value:o,done:f}=r.next());){if(f)return!1;const t=yt(o);if(e.add(t),Object.is(n,t))break}}return!0}function yt(t){return null!==t&&"object"==typeof t?t.valueOf():t}t.Adder=N,t.InternMap=InternMap,t.InternSet=InternSet,t.ascending=n,t.bin=Y,t.bisect=s,t.bisectCenter=c,t.bisectLeft=l,t.bisectRight=u,t.bisector=e,t.blur=function(t,n){if(!((n=+n)>=0))throw new RangeError("invalid r");let r=t.length;if(!((r=Math.floor(r))>=0))throw new RangeError("invalid length");if(!r||!n)return t;const e=m(n),o=t.slice();return e(t,o,0,r,1),e(o,t,0,r,1),e(t,o,0,r,1),t},t.blur2=a,t.blurImage=h,t.count=g,t.cross=function(...t){const n="function"==typeof t[t.length-1]&&function(t){return n=>t(...n)}(t.pop()),r=(t=t.map(w)).map(v),e=t.length-1,o=new Array(e+1).fill(0),f=[];if(e<0||r.some(M))return f;for(;;){f.push(o.map(((n,r)=>t[r][n])));let i=e;for(;++o[i]===r[i];){if(0===i)return n?f.map(n):f;o[i--]=0}}},t.cumsum=function(t,n){var r=0,e=0;return Float64Array.from(t,void 0===n?t=>r+=+t||0:o=>r+=+n(o,e++,t)||0)},t.descending=r,t.deviation=A,t.difference=function(t,...n){t=new InternSet(t);for(const r of n)for(const n of r)t.delete(n);return t},t.disjoint=function(t,n){const r=n[Symbol.iterator](),e=new InternSet;for(const n of t){if(e.has(n))return!1;let t,o;for(;({value:t,done:o}=r.next())&&!o;){if(Object.is(n,t))return!1;e.add(t)}}return!0},t.every=function(t,n){if("function"!=typeof n)throw new TypeError("test is not a function");let r=-1;for(const e of t)if(!n(e,++r,t))return!1;return!0},t.extent=x,t.fcumsum=function(t,n){const r=new N;let e=-1;return Float64Array.from(t,void 0===n?t=>r.add(+t||0):o=>r.add(+n(o,++e,t)||0))},t.filter=function(t,n){if("function"!=typeof n)throw new TypeError("test is not a function");const r=[];let e=-1;for(const o of t)n(o,++e,t)&&r.push(o);return r},t.flatGroup=function(t,...n){return j(I(t,...n),n)},t.flatRollup=function(t,n,...r){return j(R(t,n,...r),r)},t.fsum=function(t,n){const r=new N;if(void 0===n)for(let n of t)(n=+n)&&r.add(n);else{let e=-1;for(let o of t)(o=+n(o,++e,t))&&r.add(o)}return+r},t.greatest=ot,t.greatestIndex=function(t,r=n){if(1===r.length)return $(t,r);let e,o=-1,f=-1;for(const n of t)++f,(o<0?0===r(n,n):r(n,e)>0)&&(e=n,o=f);return o},t.group=F,t.groupSort=function(t,r,e){return(2!==r.length?P(q(t,r,e),(([t,r],[e,o])=>n(r,o)||n(t,e))):P(F(t,e),(([t,e],[o,f])=>r(e,f)||n(t,o)))).map((([t])=>t))},t.groups=I,t.histogram=Y,t.index=function(t,...n){return U(t,T,O,n)},t.indexes=function(t,...n){return U(t,Array.from,O,n)},t.intersection=function(t,...n){t=new InternSet(t),n=n.map(dt);t:for(const r of t)for(const e of n)if(!e.has(r)){t.delete(r);continue t}return t},t.least=function(t,r=n){let e,o=!1;if(1===r.length){let f;for(const i of t){const t=r(i);(o?n(t,f)<0:0===n(t,t))&&(e=i,f=t,o=!0)}}else for(const n of t)(o?r(n,e)<0:0===r(n,n))&&(e=n,o=!0);return e},t.leastIndex=lt,t.map=function(t,n){if("function"!=typeof t[Symbol.iterator])throw new TypeError("values is not iterable");if("function"!=typeof n)throw new TypeError("mapper is not a function");return Array.from(t,((r,e)=>n(r,e,t)))},t.max=Z,t.maxIndex=$,t.mean=function(t,n){let r=0,e=0;if(void 0===n)for(let n of t)null!=n&&(n=+n)>=n&&(++r,e+=n);else{let o=-1;for(let f of t)null!=(f=n(f,++o,t))&&(f=+f)>=f&&(++r,e+=f)}if(r)return e/r},t.median=function(t,n){return ft(t,.5,n)},t.medianIndex=function(t,n){return it(t,.5,n)},t.merge=function(t){return Array.from(function*(t){for(const n of t)yield*n}(t))},t.min=tt,t.minIndex=nt,t.mode=function(t,n){const r=new InternMap;if(void 0===n)for(let n of t)null!=n&&n>=n&&r.set(n,(r.get(n)||0)+1);else{let e=-1;for(let o of t)null!=(o=n(o,++e,t))&&o>=o&&r.set(o,(r.get(o)||0)+1)}let e,o=0;for(const[t,n]of r)n>o&&(o=n,e=t);return e},t.nice=W,t.pairs=function(t,n=ut){const r=[];let e,o=!1;for(const f of t)o&&r.push(n(e,f)),e=f,o=!0;return r},t.permute=L,t.quantile=ft,t.quantileIndex=it,t.quantileSorted=function(t,n,r=f){if((e=t.length)&&!isNaN(n=+n)){if(n<=0||e<2)return+r(t[0],0,t);if(n>=1)return+r(t[e-1],e-1,t);var e,o=(e-1)*n,i=Math.floor(o),u=+r(t[i],i,t);return u+(+r(t[i+1],i+1,t)-u)*(o-i)}},t.quickselect=rt,t.range=function(t,n,r){t=+t,n=+n,r=(o=arguments.length)<2?(n=t,t=0,1):o<3?1:+r;for(var e=-1,o=0|Math.max(0,Math.ceil((n-t)/r)),f=new Array(o);++e<o;)f[e]=t+e*r;return f},t.rank=function(t,r=n){if("function"!=typeof t[Symbol.iterator])throw new TypeError("values is not iterable");let e=Array.from(t);const o=new Float64Array(e.length);2!==r.length&&(e=e.map(r),r=n);const f=(t,n)=>r(e[t],e[n]);let i,u;return(t=Uint32Array.from(e,((t,n)=>n))).sort(r===n?(t,n)=>C(e[t],e[n]):z(f)),t.forEach(((t,n)=>{const r=f(t,void 0===i?t:i);r>=0?((void 0===i||r>0)&&(i=t,u=n),o[t]=u):o[t]=NaN})),o},t.reduce=function(t,n,r){if("function"!=typeof n)throw new TypeError("reducer is not a function");const e=t[Symbol.iterator]();let o,f,i=-1;if(arguments.length<3){if(({done:o,value:r}=e.next()),o)return;++i}for(;({done:o,value:f}=e.next()),!o;)r=n(r,f,++i,t);return r},t.reverse=function(t){if("function"!=typeof t[Symbol.iterator])throw new TypeError("values is not iterable");return Array.from(t).reverse()},t.rollup=q,t.rollups=R,t.scan=function(t,n){const r=lt(t,n);return r<0?void 0:r},t.shuffle=ct,t.shuffler=st,t.some=function(t,n){if("function"!=typeof n)throw new TypeError("test is not a function");let r=-1;for(const e of t)if(n(e,++r,t))return!0;return!1},t.sort=P,t.subset=function(t,n){return pt(n,t)},t.sum=function(t,n){let r=0;if(void 0===n)for(let n of t)(n=+n)&&(r+=n);else{let e=-1;for(let o of t)(o=+n(o,++e,t))&&(r+=o)}return r},t.superset=pt,t.thresholdFreedmanDiaconis=function(t,n,r){const e=g(t),o=ft(t,.75)-ft(t,.25);return e&&o?Math.ceil((r-n)/(2*o*Math.pow(e,-1/3))):1},t.thresholdScott=function(t,n,r){const e=g(t),o=A(t);return e&&o?Math.ceil((r-n)*Math.cbrt(e)/(3.49*o)):1},t.thresholdSturges=X,t.tickIncrement=V,t.tickStep=function(t,n,r){r=+r;const e=(n=+n)<(t=+t),o=e?V(n,t,r):V(t,n,r);return(e?-1:1)*(o<0?1/-o:o)},t.ticks=Q,t.transpose=at,t.union=function(...t){const n=new InternSet;for(const r of t)for(const t of r)n.add(t);return n},t.variance=b,t.zip=function(){return at(arguments)}}));

    // https://d3js.org/d3-geo/ v3.1.1 Copyright 2010-2024 Mike Bostock, 2008-2012 Charles Karney
!function(n,t){"object"==typeof exports&&"undefined"!=typeof module?t(exports,require("d3-array")):"function"==typeof define&&define.amd?define(["exports","d3-array"],t):t((n="undefined"!=typeof globalThis?globalThis:n||self).d3=n.d3||{},n.d3)}(this,(function(n,t){"use strict";var r=1e-6,e=1e-12,i=Math.PI,o=i/2,u=i/4,a=2*i,c=180/i,l=i/180,f=Math.abs,p=Math.atan,s=Math.atan2,h=Math.cos,g=Math.ceil,d=Math.exp,v=Math.hypot,E=Math.log,y=Math.pow,S=Math.sin,m=Math.sign||function(n){return n>0?1:n<0?-1:0},M=Math.sqrt,w=Math.tan;function x(n){return n>1?0:n<-1?i:Math.acos(n)}function _(n){return n>1?o:n<-1?-o:Math.asin(n)}function N(n){return(n=S(n/2))*n}function A(){}function R(n,t){n&&P.hasOwnProperty(n.type)&&P[n.type](n,t)}var C={Feature:function(n,t){R(n.geometry,t)},FeatureCollection:function(n,t){for(var r=n.features,e=-1,i=r.length;++e<i;)R(r[e].geometry,t)}},P={Sphere:function(n,t){t.sphere()},Point:function(n,t){n=n.coordinates,t.point(n[0],n[1],n[2])},MultiPoint:function(n,t){for(var r=n.coordinates,e=-1,i=r.length;++e<i;)n=r[e],t.point(n[0],n[1],n[2])},LineString:function(n,t){$(n.coordinates,t,0)},MultiLineString:function(n,t){for(var r=n.coordinates,e=-1,i=r.length;++e<i;)$(r[e],t,0)},Polygon:function(n,t){q(n.coordinates,t)},MultiPolygon:function(n,t){for(var r=n.coordinates,e=-1,i=r.length;++e<i;)q(r[e],t)},GeometryCollection:function(n,t){for(var r=n.geometries,e=-1,i=r.length;++e<i;)R(r[e],t)}};function $(n,t,r){var e,i=-1,o=n.length-r;for(t.lineStart();++i<o;)e=n[i],t.point(e[0],e[1],e[2]);t.lineEnd()}function q(n,t){var r=-1,e=n.length;for(t.polygonStart();++r<e;)$(n[r],t,1);t.polygonEnd()}function j(n,t){n&&C.hasOwnProperty(n.type)?C[n.type](n,t):R(n,t)}var z,b,L,T,G,O,k,F,H,I,W,X,Y,B,D,U,Z=new t.Adder,J=new t.Adder,K={point:A,lineStart:A,lineEnd:A,polygonStart:function(){Z=new t.Adder,K.lineStart=Q,K.lineEnd=V},polygonEnd:function(){var n=+Z;J.add(n<0?a+n:n),this.lineStart=this.lineEnd=this.point=A},sphere:function(){J.add(a)}};function Q(){K.point=nn}function V(){tn(z,b)}function nn(n,t){K.point=tn,z=n,b=t,L=n*=l,T=h(t=(t*=l)/2+u),G=S(t)}function tn(n,t){var r=(n*=l)-L,e=r>=0?1:-1,i=e*r,o=h(t=(t*=l)/2+u),a=S(t),c=G*a,f=T*o+c*h(i),p=c*e*S(i);Z.add(s(p,f)),L=n,T=o,G=a}function rn(n){return[s(n[1],n[0]),_(n[2])]}function en(n){var t=n[0],r=n[1],e=h(r);return[e*h(t),e*S(t),S(r)]}function on(n,t){return n[0]*t[0]+n[1]*t[1]+n[2]*t[2]}function un(n,t){return[n[1]*t[2]-n[2]*t[1],n[2]*t[0]-n[0]*t[2],n[0]*t[1]-n[1]*t[0]]}function an(n,t){n[0]+=t[0],n[1]+=t[1],n[2]+=t[2]}function cn(n,t){return[n[0]*t,n[1]*t,n[2]*t]}function ln(n){var t=M(n[0]*n[0]+n[1]*n[1]+n[2]*n[2]);n[0]/=t,n[1]/=t,n[2]/=t}var fn,pn,sn,hn,gn,dn,vn,En,yn,Sn,mn,Mn,wn,xn,_n,Nn,An={point:Rn,lineStart:Pn,lineEnd:$n,polygonStart:function(){An.point=qn,An.lineStart=jn,An.lineEnd=zn,B=new t.Adder,K.polygonStart()},polygonEnd:function(){K.polygonEnd(),An.point=Rn,An.lineStart=Pn,An.lineEnd=$n,Z<0?(O=-(F=180),k=-(H=90)):B>r?H=90:B<-r&&(k=-90),U[0]=O,U[1]=F},sphere:function(){O=-(F=180),k=-(H=90)}};function Rn(n,t){D.push(U=[O=n,F=n]),t<k&&(k=t),t>H&&(H=t)}function Cn(n,t){var r=en([n*l,t*l]);if(Y){var e=un(Y,r),i=un([e[1],-e[0],0],e);ln(i),i=rn(i);var o,u=n-I,a=u>0?1:-1,p=i[0]*c*a,s=f(u)>180;s^(a*I<p&&p<a*n)?(o=i[1]*c)>H&&(H=o):s^(a*I<(p=(p+360)%360-180)&&p<a*n)?(o=-i[1]*c)<k&&(k=o):(t<k&&(k=t),t>H&&(H=t)),s?n<I?bn(O,n)>bn(O,F)&&(F=n):bn(n,F)>bn(O,F)&&(O=n):F>=O?(n<O&&(O=n),n>F&&(F=n)):n>I?bn(O,n)>bn(O,F)&&(F=n):bn(n,F)>bn(O,F)&&(O=n)}else D.push(U=[O=n,F=n]);t<k&&(k=t),t>H&&(H=t),Y=r,I=n}function Pn(){An.point=Cn}function $n(){U[0]=O,U[1]=F,An.point=Rn,Y=null}function qn(n,t){if(Y){var r=n-I;B.add(f(r)>180?r+(r>0?360:-360):r)}else W=n,X=t;K.point(n,t),Cn(n,t)}function jn(){K.lineStart()}function zn(){qn(W,X),K.lineEnd(),f(B)>r&&(O=-(F=180)),U[0]=O,U[1]=F,Y=null}function bn(n,t){return(t-=n)<0?t+360:t}function Ln(n,t){return n[0]-t[0]}function Tn(n,t){return n[0]<=n[1]?n[0]<=t&&t<=n[1]:t<n[0]||n[1]<t}var Gn={sphere:A,point:On,lineStart:Fn,lineEnd:Wn,polygonStart:function(){Gn.lineStart=Xn,Gn.lineEnd=Yn},polygonEnd:function(){Gn.lineStart=Fn,Gn.lineEnd=Wn}};function On(n,t){n*=l;var r=h(t*=l);kn(r*h(n),r*S(n),S(t))}function kn(n,t,r){++fn,sn+=(n-sn)/fn,hn+=(t-hn)/fn,gn+=(r-gn)/fn}function Fn(){Gn.point=Hn}function Hn(n,t){n*=l;var r=h(t*=l);xn=r*h(n),_n=r*S(n),Nn=S(t),Gn.point=In,kn(xn,_n,Nn)}function In(n,t){n*=l;var r=h(t*=l),e=r*h(n),i=r*S(n),o=S(t),u=s(M((u=_n*o-Nn*i)*u+(u=Nn*e-xn*o)*u+(u=xn*i-_n*e)*u),xn*e+_n*i+Nn*o);pn+=u,dn+=u*(xn+(xn=e)),vn+=u*(_n+(_n=i)),En+=u*(Nn+(Nn=o)),kn(xn,_n,Nn)}function Wn(){Gn.point=On}function Xn(){Gn.point=Bn}function Yn(){Dn(Mn,wn),Gn.point=On}function Bn(n,t){Mn=n,wn=t,n*=l,t*=l,Gn.point=Dn;var r=h(t);xn=r*h(n),_n=r*S(n),Nn=S(t),kn(xn,_n,Nn)}function Dn(n,t){n*=l;var r=h(t*=l),e=r*h(n),i=r*S(n),o=S(t),u=_n*o-Nn*i,a=Nn*e-xn*o,c=xn*i-_n*e,f=v(u,a,c),p=_(f),s=f&&-p/f;yn.add(s*u),Sn.add(s*a),mn.add(s*c),pn+=p,dn+=p*(xn+(xn=e)),vn+=p*(_n+(_n=i)),En+=p*(Nn+(Nn=o)),kn(xn,_n,Nn)}function Un(n){return function(){return n}}function Zn(n,t){function r(r,e){return r=n(r,e),t(r[0],r[1])}return n.invert&&t.invert&&(r.invert=function(r,e){return(r=t.invert(r,e))&&n.invert(r[0],r[1])}),r}function Jn(n,t){return f(n)>i&&(n-=Math.round(n/a)*a),[n,t]}function Kn(n,t,r){return(n%=a)?t||r?Zn(Vn(n),nt(t,r)):Vn(n):t||r?nt(t,r):Jn}function Qn(n){return function(t,r){return f(t+=n)>i&&(t-=Math.round(t/a)*a),[t,r]}}function Vn(n){var t=Qn(n);return t.invert=Qn(-n),t}function nt(n,t){var r=h(n),e=S(n),i=h(t),o=S(t);function u(n,t){var u=h(t),a=h(n)*u,c=S(n)*u,l=S(t),f=l*r+a*e;return[s(c*i-f*o,a*r-l*e),_(f*i+c*o)]}return u.invert=function(n,t){var u=h(t),a=h(n)*u,c=S(n)*u,l=S(t),f=l*i-c*o;return[s(c*i+l*o,a*r+f*e),_(f*r-a*e)]},u}function tt(n){function t(t){return(t=n(t[0]*l,t[1]*l))[0]*=c,t[1]*=c,t}return n=Kn(n[0]*l,n[1]*l,n.length>2?n[2]*l:0),t.invert=function(t){return(t=n.invert(t[0]*l,t[1]*l))[0]*=c,t[1]*=c,t},t}function rt(n,t,r,e,i,o){if(r){var u=h(t),c=S(t),l=e*r;null==i?(i=t+e*a,o=t-l/2):(i=et(u,i),o=et(u,o),(e>0?i<o:i>o)&&(i+=e*a));for(var f,p=i;e>0?p>o:p<o;p-=l)f=rn([u,-c*h(p),-c*S(p)]),n.point(f[0],f[1])}}function et(n,t){(t=en(t))[0]-=n,ln(t);var e=x(-t[1]);return((-t[2]<0?-e:e)+a-r)%a}function it(){var n,t=[];return{point:function(t,r,e){n.push([t,r,e])},lineStart:function(){t.push(n=[])},lineEnd:A,rejoin:function(){t.length>1&&t.push(t.pop().concat(t.shift()))},result:function(){var r=t;return t=[],n=null,r}}}function ot(n,t){return f(n[0]-t[0])<r&&f(n[1]-t[1])<r}function ut(n,t,r,e){this.x=n,this.z=t,this.o=r,this.e=e,this.v=!1,this.n=this.p=null}function at(n,t,e,i,o){var u,a,c=[],l=[];if(n.forEach((function(n){if(!((t=n.length-1)<=0)){var t,e,i=n[0],a=n[t];if(ot(i,a)){if(!i[2]&&!a[2]){for(o.lineStart(),u=0;u<t;++u)o.point((i=n[u])[0],i[1]);return void o.lineEnd()}a[0]+=2*r}c.push(e=new ut(i,n,null,!0)),l.push(e.o=new ut(i,null,e,!1)),c.push(e=new ut(a,n,null,!1)),l.push(e.o=new ut(a,null,e,!0))}})),c.length){for(l.sort(t),ct(c),ct(l),u=0,a=l.length;u<a;++u)l[u].e=e=!e;for(var f,p,s=c[0];;){for(var h=s,g=!0;h.v;)if((h=h.n)===s)return;f=h.z,o.lineStart();do{if(h.v=h.o.v=!0,h.e){if(g)for(u=0,a=f.length;u<a;++u)o.point((p=f[u])[0],p[1]);else i(h.x,h.n.x,1,o);h=h.n}else{if(g)for(f=h.p.z,u=f.length-1;u>=0;--u)o.point((p=f[u])[0],p[1]);else i(h.x,h.p.x,-1,o);h=h.p}f=(h=h.o).z,g=!g}while(!h.v);o.lineEnd()}}}function ct(n){if(t=n.length){for(var t,r,e=0,i=n[0];++e<t;)i.n=r=n[e],r.p=i,i=r;i.n=r=n[0],r.p=i}}function lt(n){return f(n[0])<=i?n[0]:m(n[0])*((f(n[0])+i)%a-i)}function ft(n,c){var l=lt(c),f=c[1],p=S(f),g=[S(l),-h(l),0],d=0,v=0,E=new t.Adder;1===p?f=o+r:-1===p&&(f=-o-r);for(var y=0,m=n.length;y<m;++y)if(w=(M=n[y]).length)for(var M,w,x=M[w-1],N=lt(x),A=x[1]/2+u,R=S(A),C=h(A),P=0;P<w;++P,N=q,R=z,C=b,x=$){var $=M[P],q=lt($),j=$[1]/2+u,z=S(j),b=h(j),L=q-N,T=L>=0?1:-1,G=T*L,O=G>i,k=R*z;if(E.add(s(k*T*S(G),C*b+k*h(G))),d+=O?L+T*a:L,O^N>=l^q>=l){var F=un(en(x),en($));ln(F);var H=un(g,F);ln(H);var I=(O^L>=0?-1:1)*_(H[2]);(f>I||f===I&&(F[0]||F[1]))&&(v+=O^L>=0?1:-1)}}return(d<-r||d<r&&E<-e)^1&v}function pt(n,r,e,i){return function(o){var u,a,c,l=r(o),f=it(),p=r(f),s=!1,h={point:g,lineStart:v,lineEnd:E,polygonStart:function(){h.point=y,h.lineStart=S,h.lineEnd=m,a=[],u=[]},polygonEnd:function(){h.point=g,h.lineStart=v,h.lineEnd=E,a=t.merge(a);var n=ft(u,i);a.length?(s||(o.polygonStart(),s=!0),at(a,ht,n,e,o)):n&&(s||(o.polygonStart(),s=!0),o.lineStart(),e(null,null,1,o),o.lineEnd()),s&&(o.polygonEnd(),s=!1),a=u=null},sphere:function(){o.polygonStart(),o.lineStart(),e(null,null,1,o),o.lineEnd(),o.polygonEnd()}};function g(t,r){n(t,r)&&o.point(t,r)}function d(n,t){l.point(n,t)}function v(){h.point=d,l.lineStart()}function E(){h.point=g,l.lineEnd()}function y(n,t){c.push([n,t]),p.point(n,t)}function S(){p.lineStart(),c=[]}function m(){y(c[0][0],c[0][1]),p.lineEnd();var n,t,r,e,i=p.clean(),l=f.result(),h=l.length;if(c.pop(),u.push(c),c=null,h)if(1&i){if((t=(r=l[0]).length-1)>0){for(s||(o.polygonStart(),s=!0),o.lineStart(),n=0;n<t;++n)o.point((e=r[n])[0],e[1]);o.lineEnd()}}else h>1&&2&i&&l.push(l.pop().concat(l.shift())),a.push(l.filter(st))}return h}}function st(n){return n.length>1}function ht(n,t){return((n=n.x)[0]<0?n[1]-o-r:o-n[1])-((t=t.x)[0]<0?t[1]-o-r:o-t[1])}Jn.invert=Jn;var gt=pt((function(){return!0}),(function(n){var t,e=NaN,u=NaN,a=NaN;return{lineStart:function(){n.lineStart(),t=1},point:function(c,l){var s=c>0?i:-i,g=f(c-e);f(g-i)<r?(n.point(e,u=(u+l)/2>0?o:-o),n.point(a,u),n.lineEnd(),n.lineStart(),n.point(s,u),n.point(c,u),t=0):a!==s&&g>=i&&(f(e-a)<r&&(e-=a*r),f(c-s)<r&&(c-=s*r),u=function(n,t,e,i){var o,u,a=S(n-e);return f(a)>r?p((S(t)*(u=h(i))*S(e)-S(i)*(o=h(t))*S(n))/(o*u*a)):(t+i)/2}(e,u,c,l),n.point(a,u),n.lineEnd(),n.lineStart(),n.point(s,u),t=0),n.point(e=c,u=l),a=s},lineEnd:function(){n.lineEnd(),e=u=NaN},clean:function(){return 2-t}}}),(function(n,t,e,u){var a;if(null==n)a=e*o,u.point(-i,a),u.point(0,a),u.point(i,a),u.point(i,0),u.point(i,-a),u.point(0,-a),u.point(-i,-a),u.point(-i,0),u.point(-i,a);else if(f(n[0]-t[0])>r){var c=n[0]<t[0]?i:-i;a=e*c/2,u.point(-c,a),u.point(0,a),u.point(c,a)}else u.point(t[0],t[1])}),[-i,-o]);function dt(n){var t=h(n),e=2*l,o=t>0,u=f(t)>r;function a(n,r){return h(n)*h(r)>t}function c(n,e,o){var u=[1,0,0],a=un(en(n),en(e)),c=on(a,a),l=a[0],p=c-l*l;if(!p)return!o&&n;var s=t*c/p,h=-t*l/p,g=un(u,a),d=cn(u,s);an(d,cn(a,h));var v=g,E=on(d,v),y=on(v,v),S=E*E-y*(on(d,d)-1);if(!(S<0)){var m=M(S),w=cn(v,(-E-m)/y);if(an(w,d),w=rn(w),!o)return w;var x,_=n[0],N=e[0],A=n[1],R=e[1];N<_&&(x=_,_=N,N=x);var C=N-_,P=f(C-i)<r;if(!P&&R<A&&(x=A,A=R,R=x),P||C<r?P?A+R>0^w[1]<(f(w[0]-_)<r?A:R):A<=w[1]&&w[1]<=R:C>i^(_<=w[0]&&w[0]<=N)){var $=cn(v,(-E+m)/y);return an($,d),[w,rn($)]}}}function p(t,r){var e=o?n:i-n,u=0;return t<-e?u|=1:t>e&&(u|=2),r<-e?u|=4:r>e&&(u|=8),u}return pt(a,(function(n){var t,r,e,l,f;return{lineStart:function(){l=e=!1,f=1},point:function(s,h){var g,d=[s,h],v=a(s,h),E=o?v?0:p(s,h):v?p(s+(s<0?i:-i),h):0;if(!t&&(l=e=v)&&n.lineStart(),v!==e&&(!(g=c(t,d))||ot(t,g)||ot(d,g))&&(d[2]=1),v!==e)f=0,v?(n.lineStart(),g=c(d,t),n.point(g[0],g[1])):(g=c(t,d),n.point(g[0],g[1],2),n.lineEnd()),t=g;else if(u&&t&&o^v){var y;E&r||!(y=c(d,t,!0))||(f=0,o?(n.lineStart(),n.point(y[0][0],y[0][1]),n.point(y[1][0],y[1][1]),n.lineEnd()):(n.point(y[1][0],y[1][1]),n.lineEnd(),n.lineStart(),n.point(y[0][0],y[0][1],3)))}!v||t&&ot(t,d)||n.point(d[0],d[1]),t=d,e=v,r=E},lineEnd:function(){e&&n.lineEnd(),t=null},clean:function(){return f|(l&&e)<<1}}}),(function(t,r,i,o){rt(o,n,e,i,t,r)}),o?[0,-n]:[-i,n-i])}var vt,Et,yt,St,mt=1e9,Mt=-mt;function wt(n,e,i,o){function u(t,r){return n<=t&&t<=i&&e<=r&&r<=o}function a(t,r,u,a){var l=0,f=0;if(null==t||(l=c(t,u))!==(f=c(r,u))||p(t,r)<0^u>0)do{a.point(0===l||3===l?n:i,l>1?o:e)}while((l=(l+u+4)%4)!==f);else a.point(r[0],r[1])}function c(t,o){return f(t[0]-n)<r?o>0?0:3:f(t[0]-i)<r?o>0?2:1:f(t[1]-e)<r?o>0?1:0:o>0?3:2}function l(n,t){return p(n.x,t.x)}function p(n,t){var r=c(n,1),e=c(t,1);return r!==e?r-e:0===r?t[1]-n[1]:1===r?n[0]-t[0]:2===r?n[1]-t[1]:t[0]-n[0]}return function(r){var c,f,p,s,h,g,d,v,E,y,S,m=r,M=it(),w={point:x,lineStart:function(){w.point=_,f&&f.push(p=[]);y=!0,E=!1,d=v=NaN},lineEnd:function(){c&&(_(s,h),g&&E&&M.rejoin(),c.push(M.result()));w.point=x,E&&m.lineEnd()},polygonStart:function(){m=M,c=[],f=[],S=!0},polygonEnd:function(){var e=function(){for(var t=0,r=0,e=f.length;r<e;++r)for(var i,u,a=f[r],c=1,l=a.length,p=a[0],s=p[0],h=p[1];c<l;++c)i=s,u=h,s=(p=a[c])[0],h=p[1],u<=o?h>o&&(s-i)*(o-u)>(h-u)*(n-i)&&++t:h<=o&&(s-i)*(o-u)<(h-u)*(n-i)&&--t;return t}(),i=S&&e,u=(c=t.merge(c)).length;(i||u)&&(r.polygonStart(),i&&(r.lineStart(),a(null,null,1,r),r.lineEnd()),u&&at(c,l,e,a,r),r.polygonEnd());m=r,c=f=p=null}};function x(n,t){u(n,t)&&m.point(n,t)}function _(t,r){var a=u(t,r);if(f&&p.push([t,r]),y)s=t,h=r,g=a,y=!1,a&&(m.lineStart(),m.point(t,r));else if(a&&E)m.point(t,r);else{var c=[d=Math.max(Mt,Math.min(mt,d)),v=Math.max(Mt,Math.min(mt,v))],l=[t=Math.max(Mt,Math.min(mt,t)),r=Math.max(Mt,Math.min(mt,r))];!function(n,t,r,e,i,o){var u,a=n[0],c=n[1],l=0,f=1,p=t[0]-a,s=t[1]-c;if(u=r-a,p||!(u>0)){if(u/=p,p<0){if(u<l)return;u<f&&(f=u)}else if(p>0){if(u>f)return;u>l&&(l=u)}if(u=i-a,p||!(u<0)){if(u/=p,p<0){if(u>f)return;u>l&&(l=u)}else if(p>0){if(u<l)return;u<f&&(f=u)}if(u=e-c,s||!(u>0)){if(u/=s,s<0){if(u<l)return;u<f&&(f=u)}else if(s>0){if(u>f)return;u>l&&(l=u)}if(u=o-c,s||!(u<0)){if(u/=s,s<0){if(u>f)return;u>l&&(l=u)}else if(s>0){if(u<l)return;u<f&&(f=u)}return l>0&&(n[0]=a+l*p,n[1]=c+l*s),f<1&&(t[0]=a+f*p,t[1]=c+f*s),!0}}}}}(c,l,n,e,i,o)?a&&(m.lineStart(),m.point(t,r),S=!1):(E||(m.lineStart(),m.point(c[0],c[1])),m.point(l[0],l[1]),a||m.lineEnd(),S=!1)}d=t,v=r,E=a}return w}}var xt={sphere:A,point:A,lineStart:function(){xt.point=Nt,xt.lineEnd=_t},lineEnd:A,polygonStart:A,polygonEnd:A};function _t(){xt.point=xt.lineEnd=A}function Nt(n,t){Et=n*=l,yt=S(t*=l),St=h(t),xt.point=At}function At(n,t){n*=l;var r=S(t*=l),e=h(t),i=f(n-Et),o=h(i),u=e*S(i),a=St*r-yt*e*o,c=yt*r+St*e*o;vt.add(s(M(u*u+a*a),c)),Et=n,yt=r,St=e}function Rt(n){return vt=new t.Adder,j(n,xt),+vt}var Ct=[null,null],Pt={type:"LineString",coordinates:Ct};function $t(n,t){return Ct[0]=n,Ct[1]=t,Rt(Pt)}var qt={Feature:function(n,t){return zt(n.geometry,t)},FeatureCollection:function(n,t){for(var r=n.features,e=-1,i=r.length;++e<i;)if(zt(r[e].geometry,t))return!0;return!1}},jt={Sphere:function(){return!0},Point:function(n,t){return bt(n.coordinates,t)},MultiPoint:function(n,t){for(var r=n.coordinates,e=-1,i=r.length;++e<i;)if(bt(r[e],t))return!0;return!1},LineString:function(n,t){return Lt(n.coordinates,t)},MultiLineString:function(n,t){for(var r=n.coordinates,e=-1,i=r.length;++e<i;)if(Lt(r[e],t))return!0;return!1},Polygon:function(n,t){return Tt(n.coordinates,t)},MultiPolygon:function(n,t){for(var r=n.coordinates,e=-1,i=r.length;++e<i;)if(Tt(r[e],t))return!0;return!1},GeometryCollection:function(n,t){for(var r=n.geometries,e=-1,i=r.length;++e<i;)if(zt(r[e],t))return!0;return!1}};function zt(n,t){return!(!n||!jt.hasOwnProperty(n.type))&&jt[n.type](n,t)}function bt(n,t){return 0===$t(n,t)}function Lt(n,t){for(var r,i,o,u=0,a=n.length;u<a;u++){if(0===(i=$t(n[u],t)))return!0;if(u>0&&(o=$t(n[u],n[u-1]))>0&&r<=o&&i<=o&&(r+i-o)*(1-Math.pow((r-i)/o,2))<e*o)return!0;r=i}return!1}function Tt(n,t){return!!ft(n.map(Gt),Ot(t))}function Gt(n){return(n=n.map(Ot)).pop(),n}function Ot(n){return[n[0]*l,n[1]*l]}function kt(n,e,i){var o=t.range(n,e-r,i).concat(e);return function(n){return o.map((function(t){return[n,t]}))}}function Ft(n,e,i){var o=t.range(n,e-r,i).concat(e);return function(n){return o.map((function(t){return[t,n]}))}}function Ht(){var n,e,i,o,u,a,c,l,p,s,h,d,v=10,E=v,y=90,S=360,m=2.5;function M(){return{type:"MultiLineString",coordinates:w()}}function w(){return t.range(g(o/y)*y,i,y).map(h).concat(t.range(g(l/S)*S,c,S).map(d)).concat(t.range(g(e/v)*v,n,v).filter((function(n){return f(n%y)>r})).map(p)).concat(t.range(g(a/E)*E,u,E).filter((function(n){return f(n%S)>r})).map(s))}return M.lines=function(){return w().map((function(n){return{type:"LineString",coordinates:n}}))},M.outline=function(){return{type:"Polygon",coordinates:[h(o).concat(d(c).slice(1),h(i).reverse().slice(1),d(l).reverse().slice(1))]}},M.extent=function(n){return arguments.length?M.extentMajor(n).extentMinor(n):M.extentMinor()},M.extentMajor=function(n){return arguments.length?(o=+n[0][0],i=+n[1][0],l=+n[0][1],c=+n[1][1],o>i&&(n=o,o=i,i=n),l>c&&(n=l,l=c,c=n),M.precision(m)):[[o,l],[i,c]]},M.extentMinor=function(t){return arguments.length?(e=+t[0][0],n=+t[1][0],a=+t[0][1],u=+t[1][1],e>n&&(t=e,e=n,n=t),a>u&&(t=a,a=u,u=t),M.precision(m)):[[e,a],[n,u]]},M.step=function(n){return arguments.length?M.stepMajor(n).stepMinor(n):M.stepMinor()},M.stepMajor=function(n){return arguments.length?(y=+n[0],S=+n[1],M):[y,S]},M.stepMinor=function(n){return arguments.length?(v=+n[0],E=+n[1],M):[v,E]},M.precision=function(t){return arguments.length?(m=+t,p=kt(a,u,90),s=Ft(e,n,m),h=kt(l,c,90),d=Ft(o,i,m),M):m},M.extentMajor([[-180,-90+r],[180,90-r]]).extentMinor([[-180,-80-r],[180,80+r]])}var It,Wt,Xt,Yt,Bt=n=>n,Dt=new t.Adder,Ut=new t.Adder,Zt={point:A,lineStart:A,lineEnd:A,polygonStart:function(){Zt.lineStart=Jt,Zt.lineEnd=Vt},polygonEnd:function(){Zt.lineStart=Zt.lineEnd=Zt.point=A,Dt.add(f(Ut)),Ut=new t.Adder},result:function(){var n=Dt/2;return Dt=new t.Adder,n}};function Jt(){Zt.point=Kt}function Kt(n,t){Zt.point=Qt,It=Xt=n,Wt=Yt=t}function Qt(n,t){Ut.add(Yt*n-Xt*t),Xt=n,Yt=t}function Vt(){Qt(It,Wt)}var nr=1/0,tr=nr,rr=-nr,er=rr,ir={point:function(n,t){n<nr&&(nr=n);n>rr&&(rr=n);t<tr&&(tr=t);t>er&&(er=t)},lineStart:A,lineEnd:A,polygonStart:A,polygonEnd:A,result:function(){var n=[[nr,tr],[rr,er]];return rr=er=-(tr=nr=1/0),n}};var or,ur,ar,cr,lr=0,fr=0,pr=0,sr=0,hr=0,gr=0,dr=0,vr=0,Er=0,yr={point:Sr,lineStart:mr,lineEnd:xr,polygonStart:function(){yr.lineStart=_r,yr.lineEnd=Nr},polygonEnd:function(){yr.point=Sr,yr.lineStart=mr,yr.lineEnd=xr},result:function(){var n=Er?[dr/Er,vr/Er]:gr?[sr/gr,hr/gr]:pr?[lr/pr,fr/pr]:[NaN,NaN];return lr=fr=pr=sr=hr=gr=dr=vr=Er=0,n}};function Sr(n,t){lr+=n,fr+=t,++pr}function mr(){yr.point=Mr}function Mr(n,t){yr.point=wr,Sr(ar=n,cr=t)}function wr(n,t){var r=n-ar,e=t-cr,i=M(r*r+e*e);sr+=i*(ar+n)/2,hr+=i*(cr+t)/2,gr+=i,Sr(ar=n,cr=t)}function xr(){yr.point=Sr}function _r(){yr.point=Ar}function Nr(){Rr(or,ur)}function Ar(n,t){yr.point=Rr,Sr(or=ar=n,ur=cr=t)}function Rr(n,t){var r=n-ar,e=t-cr,i=M(r*r+e*e);sr+=i*(ar+n)/2,hr+=i*(cr+t)/2,gr+=i,dr+=(i=cr*n-ar*t)*(ar+n),vr+=i*(cr+t),Er+=3*i,Sr(ar=n,cr=t)}function Cr(n){this._context=n}Cr.prototype={_radius:4.5,pointRadius:function(n){return this._radius=n,this},polygonStart:function(){this._line=0},polygonEnd:function(){this._line=NaN},lineStart:function(){this._point=0},lineEnd:function(){0===this._line&&this._context.closePath(),this._point=NaN},point:function(n,t){switch(this._point){case 0:this._context.moveTo(n,t),this._point=1;break;case 1:this._context.lineTo(n,t);break;default:this._context.moveTo(n+this._radius,t),this._context.arc(n,t,this._radius,0,a)}},result:A};var Pr,$r,qr,jr,zr,br=new t.Adder,Lr={point:A,lineStart:function(){Lr.point=Tr},lineEnd:function(){Pr&&Gr($r,qr),Lr.point=A},polygonStart:function(){Pr=!0},polygonEnd:function(){Pr=null},result:function(){var n=+br;return br=new t.Adder,n}};function Tr(n,t){Lr.point=Gr,$r=jr=n,qr=zr=t}function Gr(n,t){jr-=n,zr-=t,br.add(M(jr*jr+zr*zr)),jr=n,zr=t}let Or,kr,Fr,Hr;class Ir{constructor(n){this._append=null==n?Wr:function(n){const t=Math.floor(n);if(!(t>=0))throw new RangeError(`invalid digits: ${n}`);if(t>15)return Wr;if(t!==Or){const n=10**t;Or=t,kr=function(t){let r=1;this._+=t[0];for(const e=t.length;r<e;++r)this._+=Math.round(arguments[r]*n)/n+t[r]}}return kr}(n),this._radius=4.5,this._=""}pointRadius(n){return this._radius=+n,this}polygonStart(){this._line=0}polygonEnd(){this._line=NaN}lineStart(){this._point=0}lineEnd(){0===this._line&&(this._+="Z"),this._point=NaN}point(n,t){switch(this._point){case 0:this._append`M${n},${t}`,this._point=1;break;case 1:this._append`L${n},${t}`;break;default:if(this._append`M${n},${t}`,this._radius!==Fr||this._append!==kr){const n=this._radius,t=this._;this._="",this._append`m0,${n}a${n},${n} 0 1,1 0,${-2*n}a${n},${n} 0 1,1 0,${2*n}z`,Fr=n,kr=this._append,Hr=this._,this._=t}this._+=Hr}}result(){const n=this._;return this._="",n.length?n:null}}function Wr(n){let t=1;this._+=n[0];for(const r=n.length;t<r;++t)this._+=arguments[t]+n[t]}function Xr(n){return function(t){var r=new Yr;for(var e in n)r[e]=n[e];return r.stream=t,r}}function Yr(){}function Br(n,t,r){var e=n.clipExtent&&n.clipExtent();return n.scale(150).translate([0,0]),null!=e&&n.clipExtent(null),j(r,n.stream(ir)),t(ir.result()),null!=e&&n.clipExtent(e),n}function Dr(n,t,r){return Br(n,(function(r){var e=t[1][0]-t[0][0],i=t[1][1]-t[0][1],o=Math.min(e/(r[1][0]-r[0][0]),i/(r[1][1]-r[0][1])),u=+t[0][0]+(e-o*(r[1][0]+r[0][0]))/2,a=+t[0][1]+(i-o*(r[1][1]+r[0][1]))/2;n.scale(150*o).translate([u,a])}),r)}function Ur(n,t,r){return Dr(n,[[0,0],t],r)}function Zr(n,t,r){return Br(n,(function(r){var e=+t,i=e/(r[1][0]-r[0][0]),o=(e-i*(r[1][0]+r[0][0]))/2,u=-i*r[0][1];n.scale(150*i).translate([o,u])}),r)}function Jr(n,t,r){return Br(n,(function(r){var e=+t,i=e/(r[1][1]-r[0][1]),o=-i*r[0][0],u=(e-i*(r[1][1]+r[0][1]))/2;n.scale(150*i).translate([o,u])}),r)}Yr.prototype={constructor:Yr,point:function(n,t){this.stream.point(n,t)},sphere:function(){this.stream.sphere()},lineStart:function(){this.stream.lineStart()},lineEnd:function(){this.stream.lineEnd()},polygonStart:function(){this.stream.polygonStart()},polygonEnd:function(){this.stream.polygonEnd()}};var Kr=16,Qr=h(30*l);function Vr(n,t){return+t?function(n,t){function e(i,o,u,a,c,l,p,h,g,d,v,E,y,S){var m=p-i,w=h-o,x=m*m+w*w;if(x>4*t&&y--){var N=a+d,A=c+v,R=l+E,C=M(N*N+A*A+R*R),P=_(R/=C),$=f(f(R)-1)<r||f(u-g)<r?(u+g)/2:s(A,N),q=n($,P),j=q[0],z=q[1],b=j-i,L=z-o,T=w*b-m*L;(T*T/x>t||f((m*b+w*L)/x-.5)>.3||a*d+c*v+l*E<Qr)&&(e(i,o,u,a,c,l,j,z,$,N/=C,A/=C,R,y,S),S.point(j,z),e(j,z,$,N,A,R,p,h,g,d,v,E,y,S))}}return function(t){var r,i,o,u,a,c,l,f,p,s,h,g,d={point:v,lineStart:E,lineEnd:S,polygonStart:function(){t.polygonStart(),d.lineStart=m},polygonEnd:function(){t.polygonEnd(),d.lineStart=E}};function v(r,e){r=n(r,e),t.point(r[0],r[1])}function E(){f=NaN,d.point=y,t.lineStart()}function y(r,i){var o=en([r,i]),u=n(r,i);e(f,p,l,s,h,g,f=u[0],p=u[1],l=r,s=o[0],h=o[1],g=o[2],Kr,t),t.point(f,p)}function S(){d.point=v,t.lineEnd()}function m(){E(),d.point=M,d.lineEnd=w}function M(n,t){y(r=n,t),i=f,o=p,u=s,a=h,c=g,d.point=y}function w(){e(f,p,l,s,h,g,i,o,r,u,a,c,Kr,t),d.lineEnd=S,S()}return d}}(n,t):function(n){return Xr({point:function(t,r){t=n(t,r),this.stream.point(t[0],t[1])}})}(n)}var ne=Xr({point:function(n,t){this.stream.point(n*l,t*l)}});function te(n,t,r,e,i,o){if(!o)return function(n,t,r,e,i){function o(o,u){return[t+n*(o*=e),r-n*(u*=i)]}return o.invert=function(o,u){return[(o-t)/n*e,(r-u)/n*i]},o}(n,t,r,e,i);var u=h(o),a=S(o),c=u*n,l=a*n,f=u/n,p=a/n,s=(a*r-u*t)/n,g=(a*t+u*r)/n;function d(n,o){return[c*(n*=e)-l*(o*=i)+t,r-l*n-c*o]}return d.invert=function(n,t){return[e*(f*n-p*t+s),i*(g-p*n-f*t)]},d}function re(n){return ee((function(){return n}))()}function ee(n){var t,r,e,i,o,u,a,f,p,s,h=150,g=480,d=250,v=0,E=0,y=0,S=0,m=0,w=0,x=1,_=1,N=null,A=gt,R=null,C=Bt,P=.5;function $(n){return f(n[0]*l,n[1]*l)}function q(n){return(n=f.invert(n[0],n[1]))&&[n[0]*c,n[1]*c]}function j(){var n=te(h,0,0,x,_,w).apply(null,t(v,E)),e=te(h,g-n[0],d-n[1],x,_,w);return r=Kn(y,S,m),a=Zn(t,e),f=Zn(r,a),u=Vr(a,P),z()}function z(){return p=s=null,$}return $.stream=function(n){return p&&s===n?p:p=ne(function(n){return Xr({point:function(t,r){var e=n(t,r);return this.stream.point(e[0],e[1])}})}(r)(A(u(C(s=n)))))},$.preclip=function(n){return arguments.length?(A=n,N=void 0,z()):A},$.postclip=function(n){return arguments.length?(C=n,R=e=i=o=null,z()):C},$.clipAngle=function(n){return arguments.length?(A=+n?dt(N=n*l):(N=null,gt),z()):N*c},$.clipExtent=function(n){return arguments.length?(C=null==n?(R=e=i=o=null,Bt):wt(R=+n[0][0],e=+n[0][1],i=+n[1][0],o=+n[1][1]),z()):null==R?null:[[R,e],[i,o]]},$.scale=function(n){return arguments.length?(h=+n,j()):h},$.translate=function(n){return arguments.length?(g=+n[0],d=+n[1],j()):[g,d]},$.center=function(n){return arguments.length?(v=n[0]%360*l,E=n[1]%360*l,j()):[v*c,E*c]},$.rotate=function(n){return arguments.length?(y=n[0]%360*l,S=n[1]%360*l,m=n.length>2?n[2]%360*l:0,j()):[y*c,S*c,m*c]},$.angle=function(n){return arguments.length?(w=n%360*l,j()):w*c},$.reflectX=function(n){return arguments.length?(x=n?-1:1,j()):x<0},$.reflectY=function(n){return arguments.length?(_=n?-1:1,j()):_<0},$.precision=function(n){return arguments.length?(u=Vr(a,P=n*n),z()):M(P)},$.fitExtent=function(n,t){return Dr($,n,t)},$.fitSize=function(n,t){return Ur($,n,t)},$.fitWidth=function(n,t){return Zr($,n,t)},$.fitHeight=function(n,t){return Jr($,n,t)},function(){return t=n.apply(this,arguments),$.invert=t.invert&&q,j()}}function ie(n){var t=0,r=i/3,e=ee(n),o=e(t,r);return o.parallels=function(n){return arguments.length?e(t=n[0]*l,r=n[1]*l):[t*c,r*c]},o}function oe(n,t){var e=S(n),o=(e+S(t))/2;if(f(o)<r)return function(n){var t=h(n);function r(n,r){return[n*t,S(r)/t]}return r.invert=function(n,r){return[n/t,_(r*t)]},r}(n);var u=1+e*(2*o-e),a=M(u)/o;function c(n,t){var r=M(u-2*o*S(t))/o;return[r*S(n*=o),a-r*h(n)]}return c.invert=function(n,t){var r=a-t,e=s(n,f(r))*m(r);return r*o<0&&(e-=i*m(n)*m(r)),[e/o,_((u-(n*n+r*r)*o*o)/(2*o))]},c}function ue(){return ie(oe).scale(155.424).center([0,33.6442])}function ae(){return ue().parallels([29.5,45.5]).scale(1070).translate([480,250]).rotate([96,0]).center([-.6,38.7])}function ce(n){return function(t,r){var e=h(t),i=h(r),o=n(e*i);return o===1/0?[2,0]:[o*i*S(t),o*S(r)]}}function le(n){return function(t,r){var e=M(t*t+r*r),i=n(e),o=S(i),u=h(i);return[s(t*o,e*u),_(e&&r*o/e)]}}var fe=ce((function(n){return M(2/(1+n))}));fe.invert=le((function(n){return 2*_(n/2)}));var pe=ce((function(n){return(n=x(n))&&n/S(n)}));function se(n,t){return[n,E(w((o+t)/2))]}function he(n){var t,r,e,o=re(n),u=o.center,a=o.scale,c=o.translate,l=o.clipExtent,f=null;function p(){var u=i*a(),c=o(tt(o.rotate()).invert([0,0]));return l(null==f?[[c[0]-u,c[1]-u],[c[0]+u,c[1]+u]]:n===se?[[Math.max(c[0]-u,f),t],[Math.min(c[0]+u,r),e]]:[[f,Math.max(c[1]-u,t)],[r,Math.min(c[1]+u,e)]])}return o.scale=function(n){return arguments.length?(a(n),p()):a()},o.translate=function(n){return arguments.length?(c(n),p()):c()},o.center=function(n){return arguments.length?(u(n),p()):u()},o.clipExtent=function(n){return arguments.length?(null==n?f=t=r=e=null:(f=+n[0][0],t=+n[0][1],r=+n[1][0],e=+n[1][1]),p()):null==f?null:[[f,t],[r,e]]},p()}function ge(n){return w((o+n)/2)}function de(n,t){var e=h(n),u=n===t?S(n):E(e/h(t))/E(ge(t)/ge(n)),a=e*y(ge(n),u)/u;if(!u)return se;function c(n,t){a>0?t<-o+r&&(t=-o+r):t>o-r&&(t=o-r);var e=a/y(ge(t),u);return[e*S(u*n),a-e*h(u*n)]}return c.invert=function(n,t){var r=a-t,e=m(u)*M(n*n+r*r),c=s(n,f(r))*m(r);return r*u<0&&(c-=i*m(n)*m(r)),[c/u,2*p(y(a/e,1/u))-o]},c}function ve(n,t){return[n,t]}function Ee(n,t){var e=h(n),o=n===t?S(n):(e-h(t))/(t-n),u=e/o+n;if(f(o)<r)return ve;function a(n,t){var r=u-t,e=o*n;return[r*S(e),u-r*h(e)]}return a.invert=function(n,t){var r=u-t,e=s(n,f(r))*m(r);return r*o<0&&(e-=i*m(n)*m(r)),[e/o,u-m(o)*M(n*n+r*r)]},a}pe.invert=le((function(n){return n})),se.invert=function(n,t){return[n,2*p(d(t))-o]},ve.invert=ve;var ye=1.340264,Se=-.081106,me=893e-6,Me=.003796,we=M(3)/2;function xe(n,t){var r=_(we*S(t)),e=r*r,i=e*e*e;return[n*h(r)/(we*(ye+3*Se*e+i*(7*me+9*Me*e))),r*(ye+Se*e+i*(me+Me*e))]}function _e(n,t){var r=h(t),e=h(n)*r;return[r*S(n)/e,S(t)/e]}function Ne(n,t){var r=t*t,e=r*r;return[n*(.8707-.131979*r+e*(e*(.003971*r-.001529*e)-.013791)),t*(1.007226+r*(.015085+e*(.028874*r-.044475-.005916*e)))]}function Ae(n,t){return[h(t)*S(n),S(t)]}function Re(n,t){var r=h(t),e=1+h(n)*r;return[r*S(n)/e,S(t)/e]}function Ce(n,t){return[E(w((o+t)/2)),-n]}xe.invert=function(n,t){for(var r,i=t,o=i*i,u=o*o*o,a=0;a<12&&(u=(o=(i-=r=(i*(ye+Se*o+u*(me+Me*o))-t)/(ye+3*Se*o+u*(7*me+9*Me*o)))*i)*o*o,!(f(r)<e));++a);return[we*n*(ye+3*Se*o+u*(7*me+9*Me*o))/h(i),_(S(i)/we)]},_e.invert=le(p),Ne.invert=function(n,t){var e,i=t,o=25;do{var u=i*i,a=u*u;i-=e=(i*(1.007226+u*(.015085+a*(.028874*u-.044475-.005916*a)))-t)/(1.007226+u*(.045255+a*(.259866*u-.311325-.005916*11*a)))}while(f(e)>r&&--o>0);return[n/(.8707+(u=i*i)*(u*(u*u*u*(.003971-.001529*u)-.013791)-.131979)),i]},Ae.invert=le(_),Re.invert=le((function(n){return 2*p(n)})),Ce.invert=function(n,t){return[-t,2*p(d(n))-o]},n.geoAlbers=ae,n.geoAlbersUsa=function(){var n,t,e,i,o,u,a=ae(),c=ue().rotate([154,0]).center([-2,58.5]).parallels([55,65]),l=ue().rotate([157,0]).center([-3,19.9]).parallels([8,18]),f={point:function(n,t){u=[n,t]}};function p(n){var t=n[0],r=n[1];return u=null,e.point(t,r),u||(i.point(t,r),u)||(o.point(t,r),u)}function s(){return n=t=null,p}return p.invert=function(n){var t=a.scale(),r=a.translate(),e=(n[0]-r[0])/t,i=(n[1]-r[1])/t;return(i>=.12&&i<.234&&e>=-.425&&e<-.214?c:i>=.166&&i<.234&&e>=-.214&&e<-.115?l:a).invert(n)},p.stream=function(r){return n&&t===r?n:(e=[a.stream(t=r),c.stream(r),l.stream(r)],i=e.length,n={point:function(n,t){for(var r=-1;++r<i;)e[r].point(n,t)},sphere:function(){for(var n=-1;++n<i;)e[n].sphere()},lineStart:function(){for(var n=-1;++n<i;)e[n].lineStart()},lineEnd:function(){for(var n=-1;++n<i;)e[n].lineEnd()},polygonStart:function(){for(var n=-1;++n<i;)e[n].polygonStart()},polygonEnd:function(){for(var n=-1;++n<i;)e[n].polygonEnd()}});var e,i},p.precision=function(n){return arguments.length?(a.precision(n),c.precision(n),l.precision(n),s()):a.precision()},p.scale=function(n){return arguments.length?(a.scale(n),c.scale(.35*n),l.scale(n),p.translate(a.translate())):a.scale()},p.translate=function(n){if(!arguments.length)return a.translate();var t=a.scale(),u=+n[0],p=+n[1];return e=a.translate(n).clipExtent([[u-.455*t,p-.238*t],[u+.455*t,p+.238*t]]).stream(f),i=c.translate([u-.307*t,p+.201*t]).clipExtent([[u-.425*t+r,p+.12*t+r],[u-.214*t-r,p+.234*t-r]]).stream(f),o=l.translate([u-.205*t,p+.212*t]).clipExtent([[u-.214*t+r,p+.166*t+r],[u-.115*t-r,p+.234*t-r]]).stream(f),s()},p.fitExtent=function(n,t){return Dr(p,n,t)},p.fitSize=function(n,t){return Ur(p,n,t)},p.fitWidth=function(n,t){return Zr(p,n,t)},p.fitHeight=function(n,t){return Jr(p,n,t)},p.scale(1070)},n.geoArea=function(n){return J=new t.Adder,j(n,K),2*J},n.geoAzimuthalEqualArea=function(){return re(fe).scale(124.75).clipAngle(179.999)},n.geoAzimuthalEqualAreaRaw=fe,n.geoAzimuthalEquidistant=function(){return re(pe).scale(79.4188).clipAngle(179.999)},n.geoAzimuthalEquidistantRaw=pe,n.geoBounds=function(n){var t,r,e,i,o,u,a;if(H=F=-(O=k=1/0),D=[],j(n,An),r=D.length){for(D.sort(Ln),t=1,o=[e=D[0]];t<r;++t)Tn(e,(i=D[t])[0])||Tn(e,i[1])?(bn(e[0],i[1])>bn(e[0],e[1])&&(e[1]=i[1]),bn(i[0],e[1])>bn(e[0],e[1])&&(e[0]=i[0])):o.push(e=i);for(u=-1/0,t=0,e=o[r=o.length-1];t<=r;e=i,++t)i=o[t],(a=bn(e[1],i[0]))>u&&(u=a,O=i[0],F=e[1])}return D=U=null,O===1/0||k===1/0?[[NaN,NaN],[NaN,NaN]]:[[O,k],[F,H]]},n.geoCentroid=function(n){fn=pn=sn=hn=gn=dn=vn=En=0,yn=new t.Adder,Sn=new t.Adder,mn=new t.Adder,j(n,Gn);var i=+yn,o=+Sn,u=+mn,a=v(i,o,u);return a<e&&(i=dn,o=vn,u=En,pn<r&&(i=sn,o=hn,u=gn),(a=v(i,o,u))<e)?[NaN,NaN]:[s(o,i)*c,_(u/a)*c]},n.geoCircle=function(){var n,t,r=Un([0,0]),e=Un(90),i=Un(2),o={point:function(r,e){n.push(r=t(r,e)),r[0]*=c,r[1]*=c}};function u(){var u=r.apply(this,arguments),a=e.apply(this,arguments)*l,c=i.apply(this,arguments)*l;return n=[],t=Kn(-u[0]*l,-u[1]*l,0).invert,rt(o,a,c,1),u={type:"Polygon",coordinates:[n]},n=t=null,u}return u.center=function(n){return arguments.length?(r="function"==typeof n?n:Un([+n[0],+n[1]]),u):r},u.radius=function(n){return arguments.length?(e="function"==typeof n?n:Un(+n),u):e},u.precision=function(n){return arguments.length?(i="function"==typeof n?n:Un(+n),u):i},u},n.geoClipAntimeridian=gt,n.geoClipCircle=dt,n.geoClipExtent=function(){var n,t,r,e=0,i=0,o=960,u=500;return r={stream:function(r){return n&&t===r?n:n=wt(e,i,o,u)(t=r)},extent:function(a){return arguments.length?(e=+a[0][0],i=+a[0][1],o=+a[1][0],u=+a[1][1],n=t=null,r):[[e,i],[o,u]]}}},n.geoClipRectangle=wt,n.geoConicConformal=function(){return ie(de).scale(109.5).parallels([30,30])},n.geoConicConformalRaw=de,n.geoConicEqualArea=ue,n.geoConicEqualAreaRaw=oe,n.geoConicEquidistant=function(){return ie(Ee).scale(131.154).center([0,13.9389])},n.geoConicEquidistantRaw=Ee,n.geoContains=function(n,t){return(n&&qt.hasOwnProperty(n.type)?qt[n.type]:zt)(n,t)},n.geoDistance=$t,n.geoEqualEarth=function(){return re(xe).scale(177.158)},n.geoEqualEarthRaw=xe,n.geoEquirectangular=function(){return re(ve).scale(152.63)},n.geoEquirectangularRaw=ve,n.geoGnomonic=function(){return re(_e).scale(144.049).clipAngle(60)},n.geoGnomonicRaw=_e,n.geoGraticule=Ht,n.geoGraticule10=function(){return Ht()()},n.geoIdentity=function(){var n,t,r,e,i,o,u,a=1,f=0,p=0,s=1,g=1,d=0,v=null,E=1,y=1,m=Xr({point:function(n,t){var r=x([n,t]);this.stream.point(r[0],r[1])}}),M=Bt;function w(){return E=a*s,y=a*g,o=u=null,x}function x(r){var e=r[0]*E,i=r[1]*y;if(d){var o=i*n-e*t;e=e*n+i*t,i=o}return[e+f,i+p]}return x.invert=function(r){var e=r[0]-f,i=r[1]-p;if(d){var o=i*n+e*t;e=e*n-i*t,i=o}return[e/E,i/y]},x.stream=function(n){return o&&u===n?o:o=m(M(u=n))},x.postclip=function(n){return arguments.length?(M=n,v=r=e=i=null,w()):M},x.clipExtent=function(n){return arguments.length?(M=null==n?(v=r=e=i=null,Bt):wt(v=+n[0][0],r=+n[0][1],e=+n[1][0],i=+n[1][1]),w()):null==v?null:[[v,r],[e,i]]},x.scale=function(n){return arguments.length?(a=+n,w()):a},x.translate=function(n){return arguments.length?(f=+n[0],p=+n[1],w()):[f,p]},x.angle=function(r){return arguments.length?(t=S(d=r%360*l),n=h(d),w()):d*c},x.reflectX=function(n){return arguments.length?(s=n?-1:1,w()):s<0},x.reflectY=function(n){return arguments.length?(g=n?-1:1,w()):g<0},x.fitExtent=function(n,t){return Dr(x,n,t)},x.fitSize=function(n,t){return Ur(x,n,t)},x.fitWidth=function(n,t){return Zr(x,n,t)},x.fitHeight=function(n,t){return Jr(x,n,t)},x},n.geoInterpolate=function(n,t){var r=n[0]*l,e=n[1]*l,i=t[0]*l,o=t[1]*l,u=h(e),a=S(e),f=h(o),p=S(o),g=u*h(r),d=u*S(r),v=f*h(i),E=f*S(i),y=2*_(M(N(o-e)+u*f*N(i-r))),m=S(y),w=y?function(n){var t=S(n*=y)/m,r=S(y-n)/m,e=r*g+t*v,i=r*d+t*E,o=r*a+t*p;return[s(i,e)*c,s(o,M(e*e+i*i))*c]}:function(){return[r*c,e*c]};return w.distance=y,w},n.geoLength=Rt,n.geoMercator=function(){return he(se).scale(961/a)},n.geoMercatorRaw=se,n.geoNaturalEarth1=function(){return re(Ne).scale(175.295)},n.geoNaturalEarth1Raw=Ne,n.geoOrthographic=function(){return re(Ae).scale(249.5).clipAngle(90+r)},n.geoOrthographicRaw=Ae,n.geoPath=function(n,t){let r,e,i=3,o=4.5;function u(n){return n&&("function"==typeof o&&e.pointRadius(+o.apply(this,arguments)),j(n,r(e))),e.result()}return u.area=function(n){return j(n,r(Zt)),Zt.result()},u.measure=function(n){return j(n,r(Lr)),Lr.result()},u.bounds=function(n){return j(n,r(ir)),ir.result()},u.centroid=function(n){return j(n,r(yr)),yr.result()},u.projection=function(t){return arguments.length?(r=null==t?(n=null,Bt):(n=t).stream,u):n},u.context=function(n){return arguments.length?(e=null==n?(t=null,new Ir(i)):new Cr(t=n),"function"!=typeof o&&e.pointRadius(o),u):t},u.pointRadius=function(n){return arguments.length?(o="function"==typeof n?n:(e.pointRadius(+n),+n),u):o},u.digits=function(n){if(!arguments.length)return i;if(null==n)i=null;else{const t=Math.floor(n);if(!(t>=0))throw new RangeError(`invalid digits: ${n}`);i=t}return null===t&&(e=new Ir(i)),u},u.projection(n).digits(i).context(t)},n.geoProjection=re,n.geoProjectionMutator=ee,n.geoRotation=tt,n.geoStereographic=function(){return re(Re).scale(250).clipAngle(142)},n.geoStereographicRaw=Re,n.geoStream=j,n.geoTransform=function(n){return{stream:Xr(n)}},n.geoTransverseMercator=function(){var n=he(Ce),t=n.center,r=n.rotate;return n.center=function(n){return arguments.length?t([-n[1],n[0]]):[(n=t())[1],-n[0]]},n.rotate=function(n){return arguments.length?r([n[0],n[1],n.length>2?n[2]+90:90]):[(n=r())[0],n[1],n[2]-90]},r([0,0,90]).scale(159.155)},n.geoTransverseMercatorRaw=Ce}));


    const LAND = {"type":"Feature","geometry":{"type":"MultiPolygon","coordinates":[[[[-59.6,-80],[-60.2,-81],[-64.5,-80.9],[-65.7,-80.5],[-64,-80.3],[-61.1,-80],[-59.6,-80]]],[[[-159.20979209792097,-79.49720865796587],[-161.12861128611286,-79.63430590483577],[-162.4390243902439,-79.2822537153427],[-163.0258302583026,-78.92850896724632],[-163.06543065430654,-78.8692694161297],[-163.71343713437133,-78.59507492238991],[-163.10503105031052,-78.22271202965688],[-161.2438124381244,-78.38011997976675],[-160.24660246602465,-78.69324332138316],[-159.48339483394835,-79.04698806947955],[-159.20979209792097,-79.49720865796587]]],[[[-45.2,-78],[-43.5,-79.1],[-43.3,-80],[-46.5,-80.6],[-50.5,-81],[-54.2,-80.6],[-51.9,-79.9],[-50.4,-79.2],[-49.3,-78.5],[-48.2,-78],[-45.2,-78]]],[[[-121.21141211412115,-73.50047352636057],[-119.9189991899919,-73.65788147647044],[-118.72378723787239,-73.4818553817239],[-119.29259292592926,-73.83390757121697],[-120.23220232202323,-74.0894839203201],[-121.62181621816218,-74.0099336659635],[-122.62262622626227,-73.65788147647044],[-122.40662406624065,-73.32444743161403],[-121.21141211412115,-73.50047352636057]]],[[[-99,-71.9],[-96.8,-72],[-97,-72.4],[-99.4,-72.4],[-101.8,-72.3],[-101.7,-71.7],[-99,-71.9]]],[[[-68.5,-71],[-68.5,-71.8],[-70,-72.3],[-72.4,-72.5],[-73.1,-72.2],[-75,-72.1],[-73.9,-71.3],[-72.1,-71.2],[-71.7,-70.3],[-71.2,-69],[-69.7,-69.3],[-69.1,-70.1],[-68.5,-71]]],[[[-180,-84.7],[-179.1,-84.1],[-177.1,-84.4],[-176.5,-84.2],[-176.1,-84.1],[-175.8,-84.1],[-173.1,-84.1],[-170,-83.9],[-168.5,-84.2],[-164.2,-84.8],[-158.1,-85.4],[-150.9,-85.3],[-145.9,-85.3],[-142.9,-84.6],[-150.1,-84.3],[-153.6,-83.7],[-153,-82.8],[-152.9,-82],[-155.3,-81.4],[-154.4,-81.2],[-150.6,-81.3],[-147.2,-80.7],[-146.8,-79.9],[-149.5,-79.4],[-153.4,-79.2],[-156,-78.7],[-158.1,-78],[-157.9,-77],[-155.3,-77.2],[-152.9,-77.5],[-150,-77.2],[-147.6,-76.6],[-146.1,-76.1],[-146.2,-75.4],[-144.3,-75.5],[-141.6,-75.1],[-138.9,-75],[-136.4,-74.5],[-134.4,-74.4],[-132.3,-74.3],[-129.6,-74.5],[-126.9,-74.4],[-124,-74.5],[-121.1,-74.5],[-118.7,-74.2],[-116.2,-74.2],[-113.9,-73.7],[-112.9,-74.4],[-111.3,-74.4],[-108.7,-74.9],[-106.1,-75.1],[-103.4,-75],[-100.6,-75.3],[-100.8,-74.5],[-102.5,-74.1],[-103.3,-73.4],[-102.9,-72.8],[-100.3,-72.8],[-98.1,-73.2],[-96.3,-73.6],[-93.7,-73.3],[-91.4,-73.4],[-89.2,-72.6],[-87.3,-73.2],[-85.2,-73.5],[-82.7,-73.6],[-80.7,-73.5],[-79.3,-73.5],[-76.9,-73.6],[-74.9,-73.9],[-72.8,-73.4],[-70.2,-73.1],[-68,-72.8],[-67.1,-72],[-67.6,-71.2],[-68.2,-70.5],[-68.5,-69.7],[-68,-69],[-67.4,-68.2],[-67.7,-67.3],[-66.7,-66.6],[-65.4,-65.9],[-64.2,-65.2],[-63,-64.6],[-61.4,-64.3],[-59.9,-64],[-58.6,-63.4],[-57.2,-63.5],[-58.6,-64.2],[-59.8,-64.2],[-61.3,-64.5],[-62.5,-65.1],[-62.6,-65.9],[-62.8,-66.4],[-64.3,-66.8],[-65.5,-67.6],[-65.3,-68.4],[-64,-68.9],[-62.8,-69.6],[-62.3,-70.4],[-61.5,-71.1],[-61.1,-72.4],[-60.7,-73.2],[-61.4,-74.1],[-63.3,-74.6],[-64.4,-75.3],[-67.2,-75.8],[-69.8,-76.2],[-72.2,-76.7],[-75.6,-76.7],[-76.9,-77.1],[-74.3,-77.6],[-74.8,-78.2],[-77.9,-78.4],[-78,-79.2],[-76.6,-79.9],[-73.2,-80.4],[-70,-81],[-65.7,-81.5],[-61.6,-82],[-58.7,-82.8],[-57,-82.9],[-53.6,-82.3],[-49.8,-81.7],[-44.8,-81.8],[-42.2,-81.7],[-38.2,-81.3],[-34.4,-80.9],[-30.1,-80.6],[-29.3,-80],[-29.7,-79.3],[-33.7,-79.5],[-35.9,-79.1],[-35.3,-78.1],[-32.2,-77.7],[-29.8,-77.1],[-27.5,-76.5],[-25.5,-76.3],[-22.5,-76.1],[-20,-75.7],[-17.5,-75.1],[-15.7,-74.5],[-16.5,-73.9],[-15.4,-73.1],[-13.3,-72.7],[-11.5,-72],[-10.3,-71.3],[-8.6,-71.7],[-7.4,-71.3],[-5.8,-71],[-4.3,-71.5],[-1.8,-71.2],[-0.2,-71.6],[1.9,-71.1],[4.1,-70.9],[6.3,-70.5],[7.7,-69.9],[9.5,-70],[10.8,-70.8],[12.4,-70.2],[14.7,-70],[15.9,-70],[18.2,-69.9],[20.4,-70],[21.9,-70.4],[23.7,-70.5],[26,-70.5],[28.1,-70.3],[30,-69.9],[32,-69.7],[33.3,-68.8],[34.9,-68.7],[36.2,-69.2],[37.9,-69.5],[39.7,-69.5],[40.9,-68.9],[42.9,-68.5],[44.9,-68.1],[46.5,-67.6],[48.3,-67.4],[49.9,-67.1],[50.9,-66.5],[52.6,-66.1],[54.5,-65.8],[56.4,-66],[57.3,-66.7],[58.7,-67.3],[60.6,-67.7],[62.4,-68],[64.1,-67.4],[66,-67.7],[67.9,-67.9],[69.7,-69],[69.6,-69.7],[67.8,-70.3],[69.1,-70.7],[68.4,-71.4],[68.7,-72.2],[71,-72.1],[71.9,-71.3],[73.1,-70.7],[73.9,-69.9],[75.6,-69.7],[77.6,-69.5],[78.4,-68.7],[80.1,-68.1],[81.5,-67.5],[82.8,-67.2],[84.7,-67.2],[86.8,-67.1],[88,-66.2],[88.8,-67],[90.6,-67.2],[92.6,-67.2],[94.2,-67.1],[95.8,-67.4],[97.8,-67.2],[99.7,-67.2],[100.9,-66.6],[102.8,-65.6],[104.2,-66],[106.2,-66.9],[108.1,-67],[110.2,-66.7],[111.7,-66.1],[113.6,-65.9],[114.9,-66.4],[116.7,-66.7],[118.6,-67.2],[120.9,-67.2],[122.3,-66.6],[124.1,-66.6],[126.1,-66.6],[127.9,-66.7],[129.7,-66.6],[131.8,-66.4],[133.9,-66.3],[135,-65.7],[135.7,-65.6],[136.2,-66.4],[137.5,-67],[139.9,-66.9],[142.1,-66.8],[144.4,-66.8],[146.2,-67.2],[146.6,-67.9],[148.8,-68.4],[151.5,-68.7],[153.6,-68.9],[155.2,-68.8],[156.8,-69.4],[159.2,-69.6],[160.8,-70.2],[162.7,-70.7],[164.9,-70.8],[167.3,-70.8],[169.5,-71.2],[171.2,-71.7],[170.6,-72.4],[169.8,-73.2],[168,-73.8],[166.1,-74.4],[165,-75.1],[163.8,-75.9],[163.5,-76.7],[164.1,-77.5],[164.7,-78.2],[167,-78.8],[163.7,-79.1],[160.9,-79.7],[160.3,-80.6],[161.1,-81.3],[162.5,-82.1],[165.1,-82.7],[168.9,-83.3],[172.3,-84],[173.2,-84.4],[178.3,-84.5],[-180,-84.7]]],[[[-67.8,-53.8],[-65.1,-54.7],[-66.5,-55.2],[-67.3,-55.3],[-69.2,-55.5],[-71,-55.1],[-73.3,-54],[-73.8,-53],[-71.1,-54.1],[-70.3,-52.9],[-68.6,-52.6],[-67.8,-53.8]]],[[[-58.549185491854914,-51.09946041126139],[-57.749977499775,-51.54968099974771],[-58.048780487804876,-51.900040630637434],[-59.39879398793987,-52.1996235034272],[-59.84879848798488,-51.84926387253747],[-60.698406984069834,-52.29948446102379],[-61.19881198811987,-51.84926387253747],[-60,-51.25009812695794],[-59.15039150391503,-51.50059680025108],[-58.549185491854914,-51.09946041126139]]],[[[70.28170281702819,-49.70986979792581],[68.74448744487447,-49.774187024852424],[68.71928719287195,-49.24272362340618],[68.8668886688867,-48.82973932419316],[68.93528935289353,-48.62493973318999],[69.57969579695799,-48.939755633409746],[70.52650526505266,-49.065004970056314],[70.55890558905591,-49.2545715336295],[70.28170281702819,-49.70986979792581]]],[[[145.4,-40.8],[146.9,-41],[148.3,-40.9],[148,-42.4],[147.6,-42.9],[146.7,-43.6],[145.4,-42.7],[144.7,-41.2],[145.4,-40.8]]],[[[173,-40.9],[174,-40.9],[174.2,-41.8],[173.2,-43],[173.1,-43.9],[171.5,-44.2],[170.6,-45.9],[169.3,-46.6],[167.8,-46.3],[166.5,-45.9],[168.3,-44.1],[169.7,-43.6],[171.1,-42.5],[172,-41.5],[172.8,-40.5],[173,-40.9]]],[[[174.6,-36.2],[175.4,-36.5],[176,-37.6],[177.4,-38],[178.5,-37.7],[178,-39.2],[176.9,-39.4],[176.9,-40.1],[176,-41.3],[175.1,-41.4],[175.2,-40.5],[173.8,-39.5],[174.6,-38.8],[174.7,-37.4],[174.3,-36.5],[173.1,-35.2],[173,-34.5],[174.3,-35.3],[174.6,-36.2]]],[[[167.1,-22.2],[166.2,-22.1],[164.8,-21.1],[164,-20.1],[165,-20.5],[165.8,-21.1],[167.1,-22.2]]],[[[178.37278372783732,-17.3396865092011],[178.71838718387187,-17.62911403037087],[178.5527855278553,-18.15042208019713],[177.93357933579335,-18.287519327067017],[177.38277382773828,-18.163962549023793],[177.28557285572856,-17.72389731215746],[177.67077670776712,-17.380307915681072],[178.12438124381248,-17.505557252327634],[178.37278372783732,-17.3396865092011]]],[[[-180,-16.55603187585838],[179.3627936279363,-16.801452873341518],[178.7255872558726,-17.011330140154683],[178.5959859598596,-16.638967247421647],[179.09639096390964,-16.434167656418467],[179.41319413194134,-16.37831322250851],[-180,-16.06688243949543],[-179.79479794797948,-16.02118335720546],[-179.9171991719917,-16.501870000551747],[-180,-16.55603187585838]]],[[[50.1,-13.6],[50.5,-15.2],[50.2,-16],[49.7,-15.7],[49.8,-16.9],[49.4,-18],[48.5,-20.5],[47.5,-23.8],[46.3,-25.2],[44.8,-25.3],[43.8,-24.5],[43.3,-22.8],[43.4,-21.3],[43.9,-20.8],[44.5,-19.4],[44,-18.3],[44.3,-16.9],[44.9,-16.2],[45.9,-15.8],[46.9,-15.2],[48,-14.1],[48.3,-13.8],[48.9,-12.5],[49.5,-12.5],[50.1,-13.6]]],[[[143.6,-13.8],[144.6,-14.2],[145.4,-15],[145.5,-16.3],[145.9,-16.9],[146.1,-18.3],[147.5,-19.5],[148.8,-20.4],[149.3,-21.3],[150.1,-22.1],[150.7,-22.4],[151.6,-24.1],[152.9,-25.3],[153.2,-26.6],[153.6,-28.1],[153.3,-29.5],[153.1,-30.9],[152.4,-32.6],[151.3,-33.8],[150.7,-35.2],[150.1,-36.4],[150,-37.4],[148.3,-37.8],[146.9,-38.6],[145.5,-38.6],[145,-37.9],[143.6,-38.8],[142.2,-38.4],[140.6,-38],[139.8,-36.6],[139.1,-35.7],[138.4,-35.1],[137.7,-35.1],[137.4,-34.7],[137.9,-33.6],[137,-33.8],[136,-34.9],[135.2,-33.9],[134.1,-32.8],[133,-32],[131.3,-31.5],[128.2,-31.9],[126.1,-32.2],[124.2,-33],[123.7,-33.9],[122.2,-34],[120.6,-33.9],[119.3,-34.5],[118.5,-34.7],[117.3,-35],[115.6,-34.4],[115,-33.6],[115.7,-33.3],[115.8,-32.2],[115.2,-30.6],[115,-29.5],[114.6,-28.5],[114,-27.3],[113.3,-26.1],[113.4,-25.6],[114.2,-26.3],[113.7,-25],[113.4,-24.4],[113.7,-23.6],[113.7,-22.5],[114.2,-22.5],[115.5,-21.5],[116.7,-20.7],[117.4,-20.7],[118.8,-20.3],[119.3,-20],[120.9,-19.7],[121.7,-18.7],[122.3,-17.8],[123,-16.4],[123.9,-17.1],[123.8,-16.1],[124.4,-15.6],[125.2,-14.7],[125.7,-14.2],[126.1,-14.1],[127.1,-13.8],[128.4,-14.9],[129.6,-15],[129.9,-13.6],[130.2,-13.1],[131.2,-12.2],[132.6,-12.1],[131.8,-11.3],[133,-11.4],[134.4,-12],[135.3,-12.2],[136.3,-12],[137,-12.4],[136.3,-13.3],[136.1,-13.7],[135.4,-14.7],[136.3,-15.6],[137.6,-16.2],[138.6,-16.8],[139.3,-17.4],[140.9,-17.4],[141.3,-16.4],[141.7,-15],[141.6,-14.3],[141.7,-12.9],[141.7,-12.4],[142.1,-11.3],[142.5,-10.7],[142.9,-11.8],[143.2,-12.3],[143.6,-13.4],[143.6,-13.8]]],[[[160.85140851408516,-9.872117951300268],[160.4626046260463,-9.895813771746916],[159.8505985059851,-9.794260255546988],[159.6417964179642,-9.640237422643779],[159.70299702997033,-9.242486150860756],[160.36180361803622,-9.399894100970627],[160.68940689406895,-9.609771367783807],[160.85140851408516,-9.872117951300268]]],[[[124.4,-10.1],[123.5,-10.2],[124,-9.3],[125.1,-8.7],[126.6,-8.4],[127.3,-8.4],[125.9,-9.1],[124.4,-10.1]]],[[[117.89937899378992,-8.094931417801646],[118.25938259382593,-8.362355677128107],[118.87858878588787,-8.281112864168179],[119.12699126991271,-8.70594507360451],[117.97137971379715,-8.907359547401015],[117.27657276572768,-9.041071677064252],[116.740167401674,-9.03260888404759],[117.08217082170825,-8.457138958914697],[117.63297632976332,-8.44867616589805],[117.89937899378992,-8.094931417801646]]],[[[122.90342903429035,-8.094931417801646],[122.7558275582756,-8.650090639694554],[121.25461254612549,-8.934440485054324],[119.92259922599226,-8.810883707011087],[119.92259922599226,-8.445291048691374],[120.71460714607144,-8.237106340481546],[121.34101341013411,-8.536689213271302],[122.00702007020072,-8.460524076121374],[122.90342903429035,-8.094931417801646]]],[[[159.87579875798758,-8.336967298078136],[159.9189991899919,-8.53838177187464],[159.13419134191344,-8.113549562438308],[158.58698586985872,-7.754727138531919],[158.21258212582126,-7.421293093675516],[158.360183601836,-7.319739577475588],[158.8209882098821,-7.560082899148739],[159.6417964179642,-8.020458839255042],[159.87579875798758,-8.336967298078136]]],[[[108.6,-6.8],[110.8,-6.5],[113,-7.6],[115.7,-8.4],[113.5,-8.3],[111.5,-8.3],[109.4,-7.7],[108.3,-7.8],[106.3,-6.9],[106.1,-5.9],[108.1,-6.3],[108.6,-6.8]]],[[[155.879758797588,-6.820434789492651],[155.5989559895599,-6.9202957470892414],[155.16695166951672,-6.536084944132867],[154.72774727747276,-5.901375467883369],[154.51534515345156,-5.139724096383958],[154.65214652146523,-5.04324825599403],[154.76014760147604,-5.339446011577138],[155.06255062550628,-5.566248864423628],[155.54855548555486,-6.200958340673125],[156.02016020160204,-6.539470061339529],[155.879758797588,-6.820434789492651]]],[[[152,-5.5],[151.3,-5.8],[150.2,-6.3],[148.9,-6],[148.4,-5.4],[149.8,-5.5],[150.1,-5],[150.8,-5.5],[151.6,-4.8],[152.1,-4.1],[152.3,-4.9],[152,-5.5]]],[[[130.4707047070471,-3.0934207449555657],[130.83430834308342,-3.8584572336616247],[129.9918999189992,-3.445472934448617],[129.1566915669157,-3.3625375628853504],[128.59148591485916,-3.428547348415293],[127.90027900279006,-3.3930036177453218],[128.13428134281344,-2.8429220716624286],[129.37269372693726,-2.8023006651824574],[130.4707047070471,-3.0934207449555657]]],[[[153.1,-4.5],[152.6,-4.2],[152,-3.5],[150.7,-2.7],[151.5,-2.8],[152.2,-3.2],[153,-4],[153.1,-4.5]]],[[[134.1,-1.2],[135.5,-3.4],[137.4,-1.7],[139.2,-2.1],[141,-2.6],[144.6,-3.9],[145.8,-4.9],[147.6,-6.1],[147,-6.7],[148.1,-8],[149.3,-9.1],[150,-9.7],[150.8,-10.3],[150,-10.7],[148.9,-10.3],[147.1,-9.5],[146,-8.1],[143.9,-7.9],[143.4,-9],[142.1,-9.2],[140.1,-8.3],[138.9,-8.4],[138,-7.6],[138.4,-6.2],[136,-4.5],[133.7,-3.5],[133,-4.1],[132.8,-3.3],[133.1,-2.5],[133.7,-2.2],[131.8,-1.6],[130.5,-0.9],[132.4,-0.4],[134.1,-1.2]]],[[[125.2,1.4],[123.7,0.2],[121.1,0.4],[120,-0.5],[121.5,-1],[123.3,-1.1],[122.4,-1.5],[122.5,-3.2],[123.2,-4.7],[122.6,-5.6],[122.7,-4.5],[121.5,-4.6],[120.9,-3.6],[120.3,-2.9],[120.4,-5.5],[119.4,-5.4],[119.5,-3.5],[118.8,-2.8],[119.3,-1.4],[120,0.6],[121.7,1],[124.1,0.9],[125.2,1.4]]],[[[128.7,1.1],[128.1,0.4],[128.4,-0.8],[127.7,-0.3],[127.6,1.8],[128,1.6],[128.7,1.1]]],[[[105.8,-5.9],[103.9,-5],[102.2,-3.6],[100.9,-2.1],[99.3,0.2],[98.6,1.8],[97.2,3.3],[95.4,5],[95.9,5.4],[98.4,4.3],[99.7,3.2],[101.7,2.1],[103.1,0.6],[103.4,-0.7],[104.4,-1.1],[104.9,-2.3],[106.1,-3.1],[105.8,-5.9]]],[[[117.9,1.8],[117.8,0.8],[117.5,-0.8],[116.5,-2.5],[116,-3.7],[114.5,-3.5],[113.3,-3.1],[111.7,-3],[110.2,-2.9],[109.6,-1.3],[109,0.4],[109.7,2],[111.2,1.9],[111.8,2.9],[113.7,3.9],[114.6,4.9],[116.2,6.1],[117.1,6.9],[117.7,6],[119.2,5.4],[118.4,5],[117.9,4.1],[118,2.3],[117.9,1.8]]],[[[126.4,8.4],[126.5,7.2],[125.8,7.3],[125.7,6],[124.2,6.2],[124.2,7.4],[123.3,7.4],[122.1,6.9],[122.3,8],[123.5,8.7],[124.6,8.5],[125.5,9],[126.2,9.3],[126.4,8.4]]],[[[81.21861218612185,6.197033428733846],[80.34740347403476,5.9685380172840325],[79.87219872198722,6.764040560850077],[79.6957969579696,8.201022815078957],[80.14940149401497,9.824186515674356],[80.84060840608407,9.269027293781448],[81.30501305013053,8.564922914795332],[81.78741787417874,7.522306815142812],[81.63621636216362,6.481383274093631],[81.21861218612185,6.197033428733846]]],[[[-60.93600936009359,10.110228919637464],[-61.77121771217712,10.000212610420874],[-61.951219512195124,10.089918216397479],[-61.65961659616596,10.365805268740587],[-61.68121681216812,10.760171423316947],[-61.10521105211052,10.890498435773523],[-60.89640896408963,10.854954705103538],[-60.93600936009359,10.110228919637464]]],[[[123.98343983439838,10.279484779970659],[123.62343623436237,9.949435852320917],[123.31023310233104,9.318111493278082],[122.9970299702997,9.021913737694973],[122.38142381423813,9.714170206457766],[122.58662586625866,9.981594465784227],[122.83862838628386,10.260866635334011],[122.94662946629467,10.882035642756861],[123.49743497434974,10.94127519387348],[123.3390333903339,10.267636869747335],[124.07704077040773,11.232395273646588],[123.98343983439838,10.279484779970659]]],[[[118.5041850418504,9.316418934674743],[117.1757717577176,8.36689355820549],[117.66537665376654,9.067612819984944],[118.38538385383856,9.683704151597794],[118.98658986589868,10.375960620360587],[119.51219512195121,11.369492520516474],[119.68859688596888,10.553679273710443],[119.02979029790299,10.003597727627536],[118.5041850418504,9.316418934674743]]],[[[121.88461884618846,11.892493128946072],[122.48222482224821,11.582754904536316],[123.11943119431197,11.58444746313964],[123.10143101431015,11.166385488116632],[122.6370263702637,10.7415532786803],[122.00342003420036,10.440277847287206],[121.96741967419678,10.905731463203509],[122.03942039420394,11.415191602806445],[121.88461884618846,11.892493128946072]]],[[[125.5,12.2],[125,11.3],[125.3,10.4],[124.8,10.8],[124.3,11.5],[124.9,11.8],[125.2,12.5],[125.5,12.2]]],[[[121.3,18.5],[122.2,18.5],[122.2,17.8],[122.3,16.3],[121.5,15.1],[122.3,14.2],[124,13.8],[124.2,13],[123.3,13],[122.7,13.2],[121.1,13.6],[120.7,14.3],[120.7,14.8],[120.1,15],[119.9,16.4],[120.4,17.6],[121.3,18.5]]],[[[-65.59085590855908,18.22773998121778],[-65.84645846458464,17.97554874932132],[-66.59886598865988,17.982318983734643],[-67.18567185671856,17.946775253064672],[-67.24327243272432,18.374992579707666],[-67.09927099270992,18.520552619594227],[-66.2820628206282,18.515474943784227],[-65.77085770857708,18.42746189641096],[-65.59085590855908,18.22773998121778]]],[[[-76.90216902169021,17.86891755731139],[-77.20457204572045,17.701354255581535],[-77.76617766177661,17.862147322898068],[-78.33858338583386,18.226047422614457],[-78.21618216182162,18.45454283406427],[-77.79857798577986,18.52393773680089],[-77.56817568175681,18.49008656473424],[-76.8949689496895,18.40038095875765],[-76.36576365763658,18.1600376370845],[-76.20016200162001,17.887535701948053],[-76.90216902169021,17.86891755731139]]],[[[-72.6,19.9],[-71.6,19.9],[-70.2,19.6],[-69.8,19.3],[-69.3,19],[-68.3,18.6],[-69.2,18.4],[-70,18.4],[-70.5,18.2],[-71,18.3],[-71.7,17.8],[-72.4,18.2],[-73.5,18.2],[-74.5,18.3],[-73.4,18.5],[-72.3,18.7],[-72.8,19.5],[-73.2,19.9],[-72.6,19.9]]],[[[110.33930339303396,18.677960569704098],[109.47529475294755,18.19727392635781],[108.65448654486545,18.507012150767565],[108.6256862568626,19.368524479863567],[109.1188911889119,19.820437626953208],[110.21330213302133,20.101402355106316],[110.78570785707859,20.07770653465967],[111.00891008910088,19.695188290306632],[110.56970569705697,19.255123053440315],[110.33930339303396,18.677960569704098]]],[[[-155.5,19.1],[-155.9,19.1],[-156.1,19.7],[-155.9,20],[-155.9,20.3],[-155.4,20.1],[-155.1,19.9],[-154.8,19.5],[-155.5,19.1]]],[[[-156.07776077760778,20.6447136667759],[-156.4161641616416,20.57193364683262],[-156.58536585365854,20.783503472249123],[-156.70056700567005,20.86474628520905],[-156.71136711367114,20.927370953532346],[-156.61416614166143,21.011998883698936],[-156.25776257762578,20.917215601912346],[-155.9949599495995,20.764885327612475],[-156.07776077760778,20.6447136667759]]],[[[-157.65457654576545,21.321737108108707],[-157.70857708577086,21.26419011559541],[-157.7769777697777,21.277730584422073],[-158.12618126181263,21.313274315092045],[-158.2521825218252,21.538384609335196],[-158.29178291782918,21.579006015815168],[-158.02538025380255,21.71779582128839],[-157.94257942579426,21.653478594361772],[-157.65457654576545,21.321737108108707]]],[[[-79.7,22.8],[-78.3,22.5],[-77.1,21.7],[-76.2,21.2],[-75.7,20.7],[-74.2,20.3],[-75,19.9],[-76.3,20],[-77.1,20.4],[-78.1,20.7],[-78.7,21.6],[-80.2,21.8],[-81.8,22.2],[-81.8,22.6],[-83.5,22.2],[-84.1,21.9],[-85,21.9],[-84.2,22.6],[-83.3,23],[-82.3,23.2],[-80.6,23.1],[-79.7,22.8]]],[[[-77.53577535775358,23.759021496906797],[-77.78057780577805,23.709937297410164],[-78.03258032580325,24.285407222543057],[-78.40698406984069,24.574834743712827],[-78.1909819098191,25.209544219962325],[-77.88857888578886,25.17061537208569],[-77.53937539375393,24.339569097849676],[-77.53577535775358,23.759021496906797]]],[[[121.17541175411753,22.790877975800882],[120.74700747007472,21.969987053184866],[120.22140221402213,22.81457379624753],[120.10620106201065,23.555914464506955],[120.69300693006932,24.539291013042856],[121.4958149581496,25.295864708732267],[121.95301953019532,24.997974394545835],[121.77661776617765,24.393730973156295],[121.17541175411753,22.790877975800882]]],[[[134.63954639546398,34.14963876276201],[134.76554765547655,33.80604936628562],[134.20394203942038,33.20180594489608],[133.7935379353794,33.521699520925836],[133.2787327873279,33.289818992269346],[133.0159301593016,32.70419371551648],[132.36432364323645,32.98854356087625],[132.37152371523717,33.464152528412555],[132.92592925929262,34.05993315678542],[133.49473494734946,33.944839171758844],[133.9051390513905,34.364593705385175],[134.63954639546398,34.14963876276201]]],[[[34.57654576545767,35.671248947157494],[33.89973899738999,35.24641673772116],[33.97533975339755,35.058542732751306],[34.00414004140043,34.97729991979136],[32.97812978129781,34.57108585499168],[32.488524885248864,34.701412867448255],[32.25812258122582,35.10254925643794],[32.73332733327334,35.139785545711234],[32.80172801728017,35.144863221521234],[32.94572945729459,35.38689910179771],[33.66573665736658,35.37335863297106],[34.57654576545767,35.671248947157494]]],[[[23.700837008370087,35.70510011922413],[24.2480424804248,35.36828095716106],[25.02565025650256,35.42582794967434],[25.770857708577097,35.3547404883344],[25.745657456574577,35.180406952191206],[26.289262892628926,35.30057861302778],[26.163261632616326,35.00438085744467],[24.723247232472346,34.91975292727808],[24.73404734047341,35.085623670404615],[23.513635136351382,35.280267909787796],[23.700837008370087,35.70510011922413]]],[[[15.521555215552155,38.2303975553955],[15.161551615516174,37.4433578048461],[15.30915309153093,37.133619580436346],[15.100351003510042,36.62077432362675],[14.333543335433347,36.99652233356646],[13.82593825938261,37.1048460841797],[12.432724327243278,37.61261366517931],[12.56952569525697,38.12715148059223],[13.739537395373958,38.035753316012304],[14.761947619476189,38.144077066625556],[15.521555215552155,38.2303975553955]]],[[[9.210692106921073,41.209300697259835],[9.808298082980826,40.50011864246372],[9.667896678966798,39.17653781465809],[9.214292142921437,39.24085504158471],[8.807488074880752,38.90742099672829],[8.42948429484295,39.17146013884809],[8.389883898839003,40.37825442302382],[8.159481594815958,40.950339230950036],[8.710287102871035,40.89956247285008],[9.210692106921073,41.209300697259835]]],[[[141,37.1],[140.8,35.8],[139,34.7],[135.8,33.5],[135.1,34.6],[132.2,33.9],[132,33.1],[130.7,31],[130.4,32.3],[129.4,33.3],[130.9,34.2],[132.6,35.4],[135.7,35.5],[137.4,36.8],[139.4,38.2],[139.9,40.6],[141.4,41.4],[141.9,39.2],[141,37.1]]],[[[143.9,44.2],[145.3,44.4],[144.1,43],[141.6,42.7],[140,41.6],[140.3,43.3],[141.7,44.8],[143.1,44.5],[143.9,44.2]]],[[[-63.664836648366474,46.54932309077233],[-62.937629376293756,46.41561096110911],[-62.01242012420124,46.442691898762405],[-62.505625056250565,46.03309271675607],[-62.872828728287274,45.968775489829454],[-64.14364143641436,46.39191514066246],[-64.3920439204392,46.727041744122175],[-64.0140401404014,47.03677996853196],[-63.664836648366474,46.54932309077233]]],[[[-61.80721807218072,49.105086581803675],[-62.29322293222931,49.086468437167014],[-63.589235892358914,49.401284337386755],[-64.51804518045181,49.873508187716396],[-64.17244172441724,49.95644355927968],[-62.85842858428583,49.705944885986526],[-61.8360183601836,49.28788291096353],[-61.80721807218072,49.105086581803675]]],[[[-123.5,48.5],[-125.7,48.8],[-126.8,49.5],[-128.1,50],[-128.4,50.8],[-126.7,50.4],[-125.4,49.9],[-123.9,49.1],[-123.5,48.5]]],[[[-56.1,50.7],[-56.1,50.1],[-55.8,49.6],[-54.5,49.6],[-53.8,48.5],[-53,48.2],[-53.1,46.7],[-54.2,46.8],[-54.2,47.8],[-56,46.9],[-56.3,47.6],[-59.3,47.6],[-58.8,48.3],[-58.4,49.1],[-56.7,51.3],[-55.4,51.6],[-56.1,50.7]]],[[[-132.709927099271,54.0405874691198],[-131.74871748717487,54.120137723476404],[-132.0511205112051,52.98443090064063],[-131.17991179911797,52.180465564057926],[-131.57951579515796,52.182158122661264],[-132.18072180721808,52.63914894556089],[-132.55152551525515,53.09952488566722],[-133.05553055530555,53.41095566868029],[-133.23913239132392,53.85102090554662],[-133.18153181531815,54.16922192297304],[-132.709927099271,54.0405874691198]]],[[[143.6,50.7],[143.2,49.3],[143.5,46.8],[142.7,46.7],[141.9,46.8],[141.9,48.9],[142.2,51],[141.7,53.3],[142.2,54.2],[142.9,53.7],[143.2,51.8],[143.6,50.7]]],[[[-6.787867878678782,52.26001581841453],[-8.56268562685625,51.66931286585165],[-9.977499774997739,51.8199505815482],[-9.167491674916732,52.864259239804056],[-9.689496894968954,53.88148696040659],[-8.32868328683287,54.665141593749325],[-7.572675726757268,55.13228776826895],[-6.733867338673377,55.17290917474892],[-5.661056610566106,54.55512528453275],[-6.197461974619728,53.86794649157994],[-6.031860318603179,53.15368676097384],[-6.787867878678782,52.26001581841453]]],[[[-153.0069300693007,57.11596645137408],[-154.0041400414004,56.73514076562438],[-154.51534515345153,56.992409673330826],[-154.67014670146702,57.46124840645379],[-153.7629376293763,57.81668571315353],[-153.230132301323,57.96901598745342],[-152.5641256412564,57.90131364332012],[-152.14292142921428,57.59157541891037],[-153.0069300693007,57.11596645137408]]],[[[-3,58.6],[-3.1,57.7],[-2.2,56.9],[-2.1,55.9],[-0.4,54.5],[0.5,52.9],[1.6,52.1],[1.4,51.3],[-0.8,50.8],[-3,50.7],[-4.5,50.3],[-5.8,50.2],[-3.4,51.4],[-5.3,52],[-4.8,52.8],[-3.1,53.4],[-3.6,54.6],[-5.1,55.1],[-5,55.8],[-5.6,56.3],[-5.8,57.8],[-4.2,58.6],[-3,58.6]]],[[[-79.26739267392674,62.15809853070013],[-79.65619656196561,61.63340536366721],[-80.0990009900099,61.7180332938338],[-80.36180361803618,62.015923608020245],[-80.3150031500315,62.08531851075685],[-79.92979929799297,62.384901383546634],[-79.51939519395194,62.362898121703296],[-79.26739267392674,62.15809853070013]]],[[[-171.73071730717308,63.78295478989887],[-171.1151111511115,63.59169566772235],[-170.49230492304923,63.6949417425256],[-169.68229682296823,63.4309026004058],[-168.68868688686888,63.29719047074258],[-168.77148771487714,63.18886672012934],[-169.5310953109531,62.97729689471282],[-170.29070290702907,63.193944395939326],[-170.67230672306724,63.375048166495844],[-171.55431554315544,63.31750117398255],[-171.79191791917918,63.405514221355816],[-171.73071730717308,63.78295478989887]]],[[[-85.2,65.7],[-84.5,65.4],[-82.8,64.8],[-81.6,64],[-80.1,63.7],[-82.5,63.7],[-84.1,63.6],[-85.9,63.6],[-86.4,64],[-85.9,65.7],[-85.2,65.7]]],[[[-14.5,66.5],[-13.6,65.1],[-17.8,63.7],[-20,63.6],[-21.8,64.4],[-22.2,65.1],[-24.3,65.6],[-22.1,66.4],[-19.1,66.3],[-16.2,66.5],[-14.5,66.5]]],[[[-75.86535865358653,67.14945385192624],[-76.98856988569885,67.09867709382627],[-77.23697236972369,67.58782653018923],[-76.81216812168121,68.14806342789211],[-75.89415894158941,68.28685323336535],[-75.11295112951129,68.01096618102224],[-75.10215102151021,67.58274885437922],[-75.21735217352173,67.44395904890601],[-75.86535865358653,67.14945385192624]]],[[[-180,69],[-174.9,67.2],[-174.3,66.3],[-171.9,66.9],[-170.9,65.5],[-172.6,64.5],[-173.9,64.3],[-176,64.9],[-177.2,65.5],[-178.9,65.7],[-179.9,65.9],[-180,65],[178.7,64.5],[178.3,64.1],[179.4,63],[179.2,62.3],[174.6,61.8],[172.1,60.9],[170.3,59.9],[166.3,59.8],[164.9,59.7],[163.2,59.2],[162.1,57.8],[163.1,56.2],[161.7,55.3],[160.4,54.3],[158.5,53],[156.8,51],[156,53.2],[155.9,56.8],[156.8,57.8],[160.1,59.3],[163.7,61.1],[163.3,62.5],[160.1,60.5],[156.7,61.4],[155,59.1],[151.3,58.8],[149.8,59.7],[145.5,59.3],[139,57.1],[136.7,54.6],[138.2,53.8],[139.9,54.2],[141.4,52.2],[140.5,50],[138.6,47],[136.9,45.1],[134.9,43.4],[132.9,42.8],[130.9,42.6],[130.4,42.3],[129.7,41.6],[129.2,40.7],[128.6,40.2],[127.5,39.8],[127.4,39.2],[128.4,38.6],[129.5,36.8],[129.1,35.1],[127.4,34.5],[126.4,34.9],[126.1,36.7],[126.2,37.7],[125.6,37.8],[125.2,37.9],[124.7,38.1],[125.2,38.7],[125.4,39.4],[124.7,39.7],[122.9,39.6],[121.1,38.9],[121.4,39.8],[121.6,40.9],[119.6,39.9],[118,39.2],[118.1,38.1],[118.9,37.4],[120.8,37.9],[122.4,37.5],[121.1,36.7],[119.7,35.6],[120.2,34.4],[121.2,32.5],[121.9,30.9],[121.5,30.1],[121.9,29],[121.1,28.1],[119.6,25.7],[117.3,23.6],[114.8,22.7],[113.8,22.5],[111.8,21.6],[110.4,20.3],[109.6,21],[108.5,21.7],[106.7,20.7],[105.7,19.1],[107.4,16.7],[108.9,15.3],[109.2,11.7],[107.2,10.4],[105.2,8.6],[105.1,9.9],[103.5,10.6],[102.6,12.2],[100.8,12.6],[100.1,13.4],[99.5,10.8],[99.2,9.2],[100.3,8.3],[101,6.9],[102.1,6.2],[103,5.5],[103.4,4.2],[103.4,3.4],[103.9,2.5],[104.2,1.3],[102.6,2],[101.3,3.3],[100.6,4.8],[100.3,6],[99.7,6.8],[99,7.9],[98.3,7.8],[98.3,9],[98.5,10.7],[98.4,12],[98.1,13.6],[97.6,16.1],[96.5,16.4],[94.8,15.8],[94.5,17.3],[93.5,19.4],[93.1,19.9],[92.1,21.2],[91.8,22.2],[90.5,22.8],[90.3,21.8],[89.7,21.9],[89,22.1],[88.2,21.7],[87,20.7],[85.1,19.5],[83.2,17.7],[82.2,16.6],[80.8,16],[80,15.1],[80.3,13],[79.9,10.4],[78.9,9.5],[78.3,8.9],[77.5,8],[76.1,10.3],[75.4,11.8],[74.6,14],[73.5,16],[72.8,19.2],[72.6,21.4],[70.5,20.9],[69.6,22.5],[68.2,23.7],[67.1,24.7],[64.5,25.2],[61.5,25.1],[58.5,25.6],[57,27],[55.7,27],[53.5,26.8],[51.5,27.9],[50.1,30.1],[48.9,30.3],[48,30],[48.1,29.3],[48.8,27.7],[49.5,27.1],[50.2,26.3],[50.2,25.6],[50.7,25],[50.7,25.5],[51.3,26.1],[51.6,25.2],[51.6,24.2],[51.8,24],[53.4,24.2],[54.7,24.8],[56.1,26.1],[56.5,26.3],[56.3,25.7],[56.8,24.2],[58.1,23.7],[59.2,23],[59.8,22.5],[59.4,21.7],[58.9,21.1],[58,20.5],[57.7,19.7],[57.7,18.9],[56.6,18.6],[56.3,17.9],[55.3,17.6],[54.8,16.9],[53.6,16.7],[52.4,16.4],[52.2,15.6],[49.6,14.7],[48.2,13.9],[47.4,13.6],[45.9,13.3],[45.4,13],[45,12.7],[44.2,12.6],[43.2,13.2],[43.1,14.1],[42.6,15.2],[42.7,15.7],[42.8,16.3],[42.3,17.1],[41.8,17.8],[40.9,19.5],[39.8,20.3],[39,22],[38.5,23.7],[37.5,24.3],[37.2,25.1],[36.6,25.8],[35.6,27.4],[34.6,28.1],[34.8,29],[34.9,29.5],[34.4,28.3],[33.9,27.6],[33.1,28.4],[32.3,29.8],[33.3,27.7],[34.5,25.6],[35.7,23.9],[35.5,23.1],[36.9,22],[37,20.8],[37.5,18.6],[38.4,18],[39.3,15.9],[41.2,14.5],[42.3,13.3],[43.1,12.7],[43.3,12],[43.1,11.5],[43.7,10.9],[44.6,10.4],[46.6,10.8],[48,11.2],[48.9,11.4],[49.7,11.6],[50.7,12],[51.1,11.7],[51,10.6],[50.6,9.2],[49.5,6.8],[47.7,4.2],[45.6,2],[43.1,0.3],[41.8,-1.4],[40.9,-2.1],[40.3,-2.6],[39.8,-3.7],[39.2,-4.7],[38.8,-6.5],[39.5,-7.1],[39.3,-8],[39.5,-9.1],[40.3,-10.3],[40.4,-11.8],[40.6,-14.2],[40.5,-15.4],[39.5,-16.7],[37.4,-17.6],[35.9,-18.8],[34.8,-19.8],[35.2,-21.3],[35.4,-22.1],[35.5,-23.1],[35.6,-23.7],[35,-24.5],[33,-25.4],[32.7,-26.1],[32.8,-26.7],[32.5,-28.3],[31.5,-29.3],[30.9,-29.9],[30.1,-31.1],[28.2,-32.8],[26.4,-33.6],[25.8,-33.9],[24.7,-34],[23,-33.9],[21.5,-34.3],[20.1,-34.8],[19.2,-34.5],[18.4,-34],[18.2,-33.9],[17.9,-32.6],[18.2,-31.7],[17.1,-29.9],[16.3,-28.6],[15.2,-27.1],[14.7,-25.4],[14.4,-22.7],[13.9,-21.7],[12.8,-19.7],[11.8,-18.1],[11.6,-16.7],[12.1,-14.9],[12.5,-13.5],[13.3,-12.5],[13.7,-11.3],[13.4,-10.4],[12.9,-9.2],[13.2,-8.6],[12.7,-6.9],[12.3,-6.1],[11.9,-5],[10.1,-3],[8.8,-1.1],[9,-0.5],[9.5,1],[9.6,2.3],[9.4,3.7],[8.7,4.4],[8.5,4.8],[7.1,4.5],[5.9,4.3],[5,5.6],[3.6,6.3],[1.9,6.1],[-0.5,5.3],[-2,4.7],[-3.3,5],[-4.6,5.2],[-6.5,4.7],[-7.7,4.4],[-9,4.8],[-10.8,6.1],[-11.7,6.9],[-12.9,7.8],[-13.2,8.9],[-14.1,9.9],[-14.6,10.2],[-14.8,10.9],[-15.7,11.5],[-16.3,11.8],[-16.6,12.2],[-16.8,13.2],[-17.1,14.4],[-17.2,14.9],[-16.5,16.1],[-16.3,17.2],[-16.3,19.1],[-16.3,20.1],[-17.1,21],[-17,21.9],[-16.3,22.7],[-16,23.7],[-15.1,24.5],[-14.8,25.6],[-13.8,26.6],[-12.6,28],[-10.9,28.8],[-9.6,29.9],[-9.4,32],[-8.7,33.2],[-6.9,34.1],[-5.9,35.8],[-4.6,35.3],[-2.6,35.2],[-1.2,35.7],[0.5,36.3],[3.2,36.8],[5.3,36.7],[7.3,37.1],[8.4,36.9],[10.2,37.2],[11,37.1],[10.6,36.4],[10.9,35.7],[10.2,34.3],[10.9,33.8],[11.5,33.1],[13.1,32.9],[15.2,32.3],[16.6,31.2],[19.1,30.3],[20.1,31],[20.1,32.2],[21.5,32.8],[23.2,32.2],[23.9,32],[25.2,31.6],[27.5,31.3],[28.9,30.9],[30.1,31.5],[31.7,31.4],[32.2,31.3],[33.8,31],[34.6,31.5],[34.8,32.1],[35.1,33.1],[35.5,33.9],[36,34.6],[36.1,35.8],[36.2,36.7],[34.7,36.8],[32.5,36.1],[30.6,36.7],[29.7,36.1],[27.6,36.7],[26.3,38.2],[26.2,39.5],[28.8,40.5],[31.1,41.1],[33.5,42],[36.9,41.3],[39.5,41.1],[41.6,41.5],[41.5,42.6],[40.3,43.1],[38.7,44.3],[36.7,45.2],[38.2,46.2],[39.1,47],[38.2,47.1],[36.8,46.7],[35,46.3],[35.5,45.4],[36.3,45.1],[33.9,44.4],[33.5,45],[32.6,45.5],[33.3,46.1],[31.7,46.7],[30.4,46],[29.6,45],[28.8,44.9],[28,43.3],[28,42],[29,41.3],[27.6,41],[26.4,40.2],[26.1,40.8],[24.9,40.9],[24.4,40.1],[23.3,40],[22.6,40.3],[23.4,39.2],[23.5,38.5],[24,37.7],[23.4,37.4],[23.2,36.4],[21.7,36.8],[21.1,38.3],[20.2,39.3],[20,39.7],[19.4,40.3],[19.4,41.4],[19.4,41.9],[18.9,42.3],[17.5,42.8],[16,43.5],[15.4,44.3],[14.9,45.1],[14,44.8],[13.7,45.5],[13.9,45.6],[12.3,45.4],[12.3,44.6],[13.5,43.6],[15.1,42],[16.2,41.7],[16.8,41.2],[18.4,40.4],[18.3,39.8],[16.9,40.4],[17.2,39.4],[16.6,38.8],[15.7,37.9],[15.9,38.8],[15.7,39.5],[15,40.2],[14.1,40.8],[12.9,41.3],[11.2,42.4],[10.2,43.9],[8.9,44.4],[7.8,43.8],[6.5,43.1],[3.1,43.1],[3,41.9],[0.8,41],[0.1,40.1],[0.1,38.7],[-0.7,37.6],[-2.1,36.7],[-4.4,36.7],[-5.4,35.9],[-6.2,36.4],[-7.5,37.1],[-8.4,37],[-8.7,37.7],[-9.3,38.4],[-9.4,39.4],[-9,40.2],[-8.8,41.2],[-9,41.9],[-9.4,43],[-6.8,43.6],[-4.3,43.4],[-1.9,43.4],[-1.2,46],[-3,47.6],[-4.6,48.7],[-1.6,48.6],[-1,49.3],[1.6,50.9],[3.3,51.3],[4.7,53.1],[6.9,53.5],[7.9,53.7],[8.8,54],[8.5,55],[8.1,56.5],[8.5,57.1],[9.8,57.4],[10.5,57.2],[10.4,56.6],[10.7,56.1],[9.6,55.5],[9.9,54.6],[10.9,54],[12.5,54.5],[14.1,53.8],[16.4,54.5],[18.6,54.7],[19.7,54.4],[21.3,55.2],[21.1,56.8],[22.5,57.8],[24.1,57],[24.4,58.4],[23.4,58.6],[24.6,59.5],[26.9,59.4],[29.1,60],[26.3,60.4],[22.9,59.8],[21.3,60.7],[21.1,62.6],[22.4,63.8],[25.4,65.1],[23.9,66],[21.2,65],[19.8,63.6],[17.1,61.3],[18.8,60.1],[16.8,58.7],[15.9,56.1],[14.1,55.4],[12.6,56.3],[11,58.9],[8.4,58.3],[5.7,58.6],[5,62],[8.6,63.5],[12.4,65.9],[16.4,68.6],[21.4,70.3],[24.5,71],[28.2,71.2],[30,70.2],[32.1,69.9],[36.5,69.1],[41.1,67.5],[40,66.3],[33.9,66.8],[34.8,65.9],[36.2,64.1],[37.1,64.3],[37.2,65.1],[40.4,64.8],[42.1,66.5],[44,66.1],[43.7,67.4],[43.5,68.6],[46.8,67.7],[45.6,67],[47.9,66.9],[50.2,68],[54.5,68.8],[54.7,68.1],[57.3,68.5],[59.9,68.3],[60,69.5],[63.5,69.5],[68.5,68.1],[68.2,69.1],[66.9,69.5],[66.7,70.7],[68.5,71.9],[69.9,73],[72.8,72.2],[72.5,71.1],[72.6,69],[73.2,67.7],[72.4,66.2],[73.9,66.8],[75.1,67.8],[74.9,69],[73.6,69.6],[73.1,71.4],[74.7,72.8],[75.7,72.3],[76.4,71.2],[77.6,72.3],[81.5,71.7],[80.5,73.6],[84.7,73.8],[86,74.5],[88.3,75.1],[92.9,75.8],[95.9,76.1],[98.9,76.4],[101,76.9],[104.4,77.7],[104.7,77.1],[107.2,76.5],[111.1,76.7],[114.1,75.8],[112.8,75],[109.4,74.2],[112.1,73.8],[113.5,73.3],[115.6,73.8],[119,73.1],[123.3,73.7],[127,73.6],[129.1,72.4],[129.7,71.2],[132.3,71.8],[135.6,71.7],[138.2,71.6],[139.1,72.4],[149.5,72.2],[153,70.8],[159,70.9],[159.7,69.7],[162.3,69.6],[165.9,69.5],[169.6,68.7],[170,69.7],[173.6,69.8],[178.6,69.4],[-180,69]],[[49.1,41.3],[50.1,40.5],[49.6,40.2],[49.2,39],[48.9,38.3],[50.1,37.4],[52.3,36.7],[53.9,37.2],[53.9,39],[53.4,40],[52.9,40.9],[54.7,41],[53.7,42.1],[52.8,41.1],[52.4,42],[52.5,42.8],[50.9,44],[50.3,44.6],[51.3,45.2],[53,45.3],[53,46.9],[51.2,47],[49.1,46.4],[47.7,45.6],[47.6,43.7],[48.6,41.8],[49.1,41.3]]],[[[-95.64755647556476,69.10774415598138],[-96.27036270362703,68.75738452509165],[-97.61677616776167,69.06035251508808],[-98.43038430384304,68.95033620587148],[-99.79839798397984,69.40055679435781],[-98.91638916389164,69.71029501876757],[-98.21798217982179,70.14359002122058],[-97.1559715597156,69.85924017586078],[-96.55836558365583,69.6798289639076],[-96.25596255962559,69.49026240033442],[-95.64755647556476,69.10774415598138]]],[[[-180,71.51625504852282],[-179.87039870398704,71.5568764550028],[-179.02439024390245,71.55518389639946],[-177.5771757717577,71.26914149243635],[-177.66357663576636,71.13204424556645],[-178.69318693186932,70.89339348249663],[-180,70.83246137277669],[-180,71.51625504852282]]],[[[-90.5,69.5],[-89.2,69.3],[-88.3,67.9],[-86.3,67.9],[-85.5,69.9],[-82.6,69.7],[-81.2,68.7],[-81.3,67.6],[-83.3,66.4],[-85.8,66.6],[-87,65.2],[-88.5,64.1],[-90.7,63.6],[-91.9,62.8],[-94.2,60.9],[-94.7,58.9],[-92.8,57.8],[-90.9,57.3],[-88,56.5],[-86.1,55.7],[-83.4,55.2],[-82.4,54.3],[-81.4,52.2],[-79.1,51.5],[-79.1,54.1],[-78.2,55.1],[-76.5,56.5],[-77.3,58.1],[-77.3,59.9],[-78.1,62.3],[-75.7,62.3],[-73.8,62.4],[-71.7,61.5],[-69.6,61.1],[-69.3,59],[-67.7,58.2],[-65.2,59.9],[-63.8,59.4],[-61.4,57],[-60.5,55.8],[-58,54.9],[-56.9,53.8],[-55.8,53.3],[-56.4,51.8],[-58.8,51.1],[-61.7,50.1],[-65.4,50.3],[-67.2,49.5],[-70,47.7],[-70.3,47],[-66.6,49.1],[-64.2,48.7],[-64.8,47],[-63.2,45.7],[-60.5,47],[-59.8,45.9],[-63.3,44.7],[-65.4,43.5],[-66.2,44.5],[-66,45.3],[-67,44.8],[-69.1,44],[-70.7,43],[-70.8,42.3],[-70.1,41.8],[-69.9,41.9],[-70.6,41.5],[-71.9,41.3],[-72.9,41.2],[-72.2,41.1],[-73.3,40.6],[-74,40.8],[-74,40.4],[-74.9,38.9],[-75.2,39.2],[-75.3,39],[-75.1,38.4],[-75.9,37.2],[-75.7,37.9],[-76.4,39.1],[-76.3,38.1],[-76.3,37.9],[-76,36.9],[-75.7,35.6],[-77.4,34.5],[-78.6,33.9],[-79.2,33.2],[-80.9,32],[-81.5,30.7],[-81,29.2],[-80.5,28],[-80.1,26.2],[-80.4,25.2],[-81.2,25.2],[-81.7,25.9],[-82.7,27.5],[-82.7,28.6],[-83.7,29.9],[-85.1,29.6],[-85.8,30.2],[-87.5,30.3],[-89.2,30.3],[-89.4,29.9],[-89.2,29.3],[-89.8,29.3],[-90.9,29.1],[-92.5,29.6],[-93.8,29.7],[-95.6,28.7],[-97.1,27.8],[-97.4,26.7],[-97.1,25.9],[-97.1,25.9],[-97.7,24.3],[-97.9,22.4],[-97.4,21.4],[-96.5,19.9],[-95.9,18.8],[-94.4,18.1],[-92.8,18.5],[-91.4,18.9],[-90.5,19.9],[-90.3,21],[-88.5,21.5],[-87.1,21.5],[-86.8,20.8],[-87.6,19.6],[-87.6,19],[-88.1,18.5],[-88.3,18.4],[-88.1,18.1],[-88.2,17.5],[-88.2,17],[-88.6,16.3],[-88.9,15.9],[-88.5,15.9],[-88.1,15.7],[-87.6,15.9],[-87.4,15.8],[-86.4,15.8],[-86,16],[-85.4,15.9],[-85,16],[-84.4,15.8],[-83.8,15.4],[-83.1,15],[-83.3,14.7],[-83.4,14],[-83.6,13.1],[-83.5,12.4],[-83.7,11.9],[-83.9,11.4],[-83.7,10.9],[-83,10],[-82.2,9.2],[-81.8,9],[-81.4,8.8],[-80.5,9.1],[-79.6,9.6],[-79.1,9.5],[-78.1,9.2],[-77.4,8.7],[-76.1,9.3],[-75.7,9.8],[-74.9,11.1],[-74.2,11.3],[-72.6,11.7],[-71.8,12.4],[-71.1,12.1],[-71.4,11.5],[-71.6,11],[-72.1,9.9],[-71.3,9.1],[-71.4,10.2],[-70.2,11.4],[-69.9,12.2],[-68.9,11.4],[-68.2,10.6],[-66.2,10.6],[-64.9,10.1],[-64.3,10.6],[-61.9,10.7],[-62.4,9.9],[-60.8,9.4],[-60.2,8.6],[-59.1,8],[-58.5,6.8],[-57.5,6.3],[-55.9,5.8],[-55,6],[-53.6,5.6],[-51.8,4.6],[-51.3,4.2],[-50.5,1.9],[-49.9,1],[-50.4,-0.1],[-48.6,-1.2],[-46.6,-0.9],[-44.4,-2.1],[-43.4,-2.4],[-40,-2.9],[-37.2,-4.8],[-35.6,-5.1],[-34.9,-6.7],[-35.1,-9],[-37,-11],[-38.4,-13],[-39,-13.8],[-39.2,-17.2],[-39.6,-18.3],[-40.8,-20.9],[-41.8,-22.4],[-43.1,-23],[-45.4,-23.8],[-47.6,-24.9],[-48.6,-26.6],[-48.7,-28.2],[-49.6,-29.2],[-51.6,-31.8],[-52.7,-33.2],[-53.8,-34.4],[-55.7,-34.8],[-57.1,-34.4],[-58.4,-33.9],[-57.2,-35.3],[-56.7,-36.4],[-57.7,-38.2],[-61.2,-38.9],[-62.1,-39.4],[-62.1,-40.7],[-63.8,-41.2],[-65.1,-41.1],[-64.3,-42.4],[-63.5,-42.6],[-65.2,-43.5],[-65.6,-45],[-67.3,-45.6],[-66.6,-47],[-66,-48.1],[-67.8,-49.9],[-69.1,-50.7],[-68.2,-52.4],[-69.5,-52.3],[-70.8,-52.9],[-71.4,-53.9],[-73.7,-52.8],[-75.3,-51.6],[-75.5,-50.4],[-75.2,-47.7],[-75.6,-46.6],[-74.4,-44.1],[-72.7,-42.4],[-73.7,-43.4],[-74,-41.8],[-73.2,-39.3],[-73.6,-37.2],[-72.6,-35.5],[-71.4,-32.4],[-71.4,-30.1],[-70.9,-27.6],[-70.4,-23.6],[-70.2,-19.8],[-71.4,-17.8],[-73.4,-16.4],[-76,-14.6],[-76.3,-13.5],[-78.1,-10.4],[-79.4,-7.9],[-80.5,-6.5],[-80.9,-5.7],[-81.1,-4],[-79.8,-2.7],[-80.4,-2.7],[-80.8,-2],[-80.6,-0.9],[-80,0.4],[-79.5,1],[-79,1.7],[-78.7,2.3],[-77.9,2.7],[-77.1,3.8],[-77.3,4.7],[-77.3,5.8],[-77.9,7.2],[-78.4,8.1],[-78.4,8.4],[-79.1,9],[-79.8,8.6],[-80.4,8.3],[-80,7.5],[-80.4,7.3],[-81.1,7.8],[-81.5,7.7],[-82.1,8.2],[-82.8,8.3],[-83,8.2],[-83.7,8.7],[-83.6,9.1],[-84.3,9.5],[-84.7,9.9],[-84.9,9.8],[-85.3,9.8],[-85.8,10.1],[-85.7,10.8],[-85.7,11.1],[-86.5,11.8],[-87.2,12.5],[-87.6,13.1],[-87.3,13],[-87.8,13.4],[-88.5,13.2],[-89.3,13.5],[-90.1,13.7],[-91.2,13.9],[-92.2,14.5],[-93.9,15.9],[-95.3,16.1],[-96.6,15.7],[-98,16.1],[-99.7,16.7],[-101.7,17.6],[-102.5,18],[-103.9,18.7],[-105.5,19.9],[-105.4,20.5],[-105.3,21.1],[-105.6,21.9],[-106,22.8],[-107.9,24.5],[-109.3,25.6],[-109.3,26.4],[-110.4,27.2],[-111.2,27.9],[-112.2,29],[-112.8,30],[-113.1,31.2],[-114.2,31.5],[-114.9,31.4],[-114.7,30.2],[-113.6,29.1],[-113.3,28.8],[-113,28.4],[-112.5,27.5],[-111.6,26.7],[-111,25.3],[-110.7,24.3],[-109.8,23.8],[-109.4,23.2],[-110,22.8],[-111,24],[-112.2,24.7],[-112.3,26],[-113.5,26.8],[-113.8,26.9],[-115.1,27.7],[-114.6,27.7],[-114.2,28.6],[-115.5,29.6],[-116.3,30.8],[-117.1,32.5],[-117.9,33.6],[-118.5,34],[-119.4,34.3],[-120.6,34.6],[-121.7,36.2],[-122.5,37.8],[-123.7,39],[-124.4,40.3],[-124.2,42],[-124.1,43.7],[-124.1,46.9],[-124.7,48.2],[-123.1,48],[-122.3,47.4],[-122.8,49],[-124.9,50],[-127.4,50.8],[-127.8,52.3],[-129.3,53.6],[-130.5,54.8],[-132,55.5],[-133.5,57.2],[-135,58.2],[-137.8,58.5],[-140.8,59.7],[-144,60],[-147.1,60.9],[-148,60],[-149.7,59.7],[-151.7,59.2],[-151.4,60.7],[-150.6,61.3],[-152.6,60.1],[-153.3,58.9],[-155.3,57.7],[-156.6,57],[-158.4,56],[-160.3,55.6],[-162.2,55],[-164.8,54.4],[-163.8,55],[-161.8,55.9],[-160.1,56.4],[-158.5,57.2],[-157.6,58.3],[-158.2,58.6],[-159.1,58.4],[-160,58.6],[-161.4,58.7],[-162.1,59.3],[-162.5,60],[-164.7,60.3],[-165.4,61.1],[-165.7,62.1],[-164.6,63.1],[-163.1,63.1],[-161.5,63.5],[-161,64.2],[-160.8,64.8],[-162.5,64.6],[-163.5,64.6],[-166.4,64.7],[-168.1,65.7],[-164.5,66.6],[-163.8,66.1],[-162.5,66.7],[-164.4,67.6],[-166.8,68.4],[-164.4,68.9],[-162.9,69.9],[-160.9,70.4],[-158.1,70.8],[-155.1,71.1],[-153.9,70.9],[-152.3,70.6],[-149.7,70.5],[-145.7,70.1],[-143.6,70.2],[-141,69.7],[-137.5,69],[-135.6,69.3],[-132.9,69.5],[-129.8,70.2],[-128.4,70],[-127.4,70.4],[-124.4,70.2],[-123.1,69.6],[-121.5,69.8],[-117.6,69],[-115.2,68.9],[-115.3,67.9],[-110.8,67.8],[-108.9,67.4],[-108.8,68.3],[-107,68.7],[-105.3,68.6],[-103.2,68.1],[-99.9,67.8],[-98.6,68.4],[-96.1,68.2],[-95.5,68.1],[-94.2,69.1],[-96.5,70.1],[-95.2,71.9],[-92.9,71.3],[-92.4,69.7],[-90.5,69.5]]],[[[-114.2,73.1],[-112.4,73],[-109.9,73],[-108.2,71.7],[-108.4,73.1],[-106.5,73.1],[-104.8,71.7],[-102.8,70.5],[-101.1,69.6],[-102.1,69.1],[-104.2,68.9],[-107.1,69.1],[-112,68.6],[-113.9,69],[-116.1,69.2],[-116.7,70.1],[-113.7,70.2],[-114.3,70.6],[-117.9,70.5],[-116.1,71.3],[-119.4,71.6],[-117.9,72.7],[-114.2,73.1]]],[[[-76.34056340563406,73.10218245984493],[-76.25056250562506,72.82629540750179],[-77.31617316173161,72.85506890375845],[-78.39258392583926,72.87707216560176],[-79.4869948699487,72.7416674773352],[-79.7749977499775,72.80259958705514],[-80.87660876608766,73.33237042989808],[-80.83340833408333,73.69288541240778],[-80.35460354603546,73.75889519793773],[-78.0649806498065,73.65226400592783],[-76.34056340563406,73.10218245984493]]],[[[-86.6,73.2],[-84.9,73.3],[-80.6,72.7],[-78.8,72.4],[-75.6,72.2],[-74.1,71.3],[-71.2,70.9],[-67.9,70.1],[-68.8,68.7],[-64.9,67.8],[-61.9,66.9],[-63.9,65],[-66.7,66.4],[-68.1,65.7],[-65.7,64.6],[-64.7,63.4],[-66.3,62.9],[-67.4,62.9],[-66.2,61.9],[-71,62.9],[-71.9,63.7],[-74.8,64.7],[-77.7,64.2],[-77.9,65.3],[-74,65.5],[-73.9,66.3],[-72.9,67.7],[-74.8,68.6],[-76.2,69.1],[-78.2,69.8],[-79.5,69.9],[-84.9,70],[-88.7,70.4],[-88.5,71.2],[-90.2,72.2],[-88.4,73.5],[-86.6,73.2]]],[[[-100.4,73.8],[-97.4,73.8],[-98.1,73],[-96.7,71.7],[-99.3,71.4],[-102.5,72.5],[-100.4,72.7],[-100.4,73.8]]],[[[143.6036360363604,73.2121987690615],[142.08802088020883,73.20542853464818],[140.03960039600395,73.31713740246809],[139.86319863198634,73.36960671917137],[140.810008100081,73.76566543235106],[142.06282062820628,73.857063596931],[143.48123481234813,73.47454535257796],[143.6036360363604,73.2121987690615]]],[[[-93.1959319593196,72.77213353219517],[-94.26874268742687,72.02402262952242],[-95.409954099541,72.06125891879574],[-96.03276032760327,72.93969683392504],[-96.01836018360183,73.43730906330467],[-95.49635496354963,73.86214127274098],[-94.50274502745027,74.13464320787745],[-92.41832418324184,74.1007920358108],[-90.51030510305102,73.857063596931],[-92.00432004320042,72.96677777157836],[-93.1959319593196,72.77213353219517]]],[[[-120.5,71.4],[-123.6,71.3],[-125.6,72.2],[-123.9,73.7],[-121.5,74.4],[-117.6,74.2],[-115.5,73.5],[-119.2,72.5],[-120.5,71.4]]],[[[-93.61353613536136,74.97922995094012],[-94.1571415714157,74.5916340307771],[-95.6079560795608,74.66610660932369],[-96.82116821168212,74.92845319284015],[-96.28836288362884,75.37867378132648],[-94.85194851948519,75.64779059925627],[-93.97713977139772,75.2957384097632],[-93.61353613536136,74.97922995094012]]],[[[145.0868508685087,75.56316266908965],[144.29844298442987,74.82012944222691],[140.61560615606157,74.84721037988021],[138.9559895598956,74.61194473401707],[136.9759697596976,75.26188723769656],[137.51237512375127,75.94906603064936],[138.82998829988298,76.1369400356192],[141.47241472414726,76.09293351193259],[145.0868508685087,75.56316266908965]]],[[[-98.5,76.7],[-97.7,75.7],[-99.8,74.9],[-100.9,75.6],[-102.6,76.3],[-100,76.6],[-98.5,76.7]]],[[[-108.2,76.2],[-106.9,76],[-105.7,75.5],[-109.7,74.9],[-113.7,74.4],[-111.8,75.2],[-117.7,75.2],[-115.4,76.5],[-110.8,75.5],[-110.5,76.4],[-108.6,76.7],[-108.2,76.2]]],[[[57.5,70.7],[53.7,70.8],[51.6,71.5],[52.5,72.2],[54.4,73.6],[55.9,74.6],[57.9,75.6],[64.5,76.4],[68.2,76.9],[68.2,76.2],[61.6,75.3],[57,73.3],[55.6,71.5],[57.5,70.7]]],[[[-94.7,77.1],[-91.6,76.8],[-91,76.1],[-89.2,75.6],[-86.4,75.5],[-82.8,75.8],[-80.1,75.3],[-80.5,74.7],[-83.2,74.6],[-88.1,74.4],[-92.4,74.8],[-92.9,75.9],[-96,76.4],[-96.7,77.2],[-94.7,77.1]]],[[[-116.20016200162001,77.64500975118804],[-116.3369633696337,76.87658814527529],[-117.10737107371074,76.52961363159224],[-118.03978039780398,76.48052943209561],[-119.9009990099901,76.05400466405595],[-121.49941499414993,75.89998183115273],[-122.85662856628566,76.11662933237923],[-121.15741157411574,76.86474023505198],[-119.10539105391054,77.51299018012813],[-117.57177571775718,77.49775715269814],[-116.20016200162001,77.64500975118804]]],[[[24.723247232472346,77.85319445939788],[22.491224912249123,77.44528783599486],[20.727207272072718,77.67716836465135],[21.414814148141488,77.9344372723578],[20.81360813608137,78.25433084838755],[22.88362883628838,78.45574532218407],[23.279632796327974,78.07999731224436],[24.723247232472346,77.85319445939788]]],[[[-95.83115831158311,78.05630149179771],[-97.31077310773108,77.84980934219121],[-98.12438124381244,78.08338242945104],[-98.55278552785528,78.45743788078741],[-98.6319863198632,78.87211473860376],[-97.3359733597336,78.83149333212378],[-96.75276752767527,78.76548354659383],[-95.55755557555575,78.41850903291078],[-95.83115831158311,78.05630149179771]]],[[[-100.06120061200612,78.3254183097275],[-99.67239672396724,77.9073563347045],[-101.30321303213032,78.01906520252442],[-102.94842948429483,78.34403645436416],[-105.17685176851768,78.37958018503411],[-104.2120421204212,78.67747049922056],[-105.4180541805418,78.91781382089371],[-105.49365493654936,79.30202462385009],[-103.5280352803528,79.16492737698019],[-100.82440824408243,78.80102727726378],[-100.06120061200612,78.3254183097275]]],[[[18.3,79.7],[19,78.6],[17.6,77.6],[15.9,76.8],[14.7,77.7],[11.2,78.9],[13.2,80],[15.1,79.7],[17,80.1],[18.3,79.7]]],[[[25.4468544685447,80.40726539182589],[27.4088740887409,80.05690576093616],[25.92565925659258,79.51867212507656],[23.02403024030241,79.40019302284333],[20.07560075600756,79.56606376596986],[19.895598955989556,79.841950818313],[18.462784627846275,79.86056896294963],[17.36837368373685,80.31925234445262],[20.457204572045725,80.5985245140024],[21.908019080190797,80.35818119232925],[22.919629196291964,80.65776406511901],[25.4468544685447,80.40726539182589]]],[[[51.1,80.5],[48.9,80.3],[47.6,80],[47.1,80.6],[46.8,80.8],[48.5,80.5],[50,80.9],[51.1,80.5]]],[[[99.93879938799387,78.88057753162039],[97.75717757177574,78.75702075357717],[94.97434974349744,79.04475571614361],[93.31113311133112,79.42727396049665],[92.54432544325442,80.14322624970609],[91.17991179911797,80.34125560629593],[93.77913779137793,81.02504928204206],[95.93915939159393,81.25015957628523],[97.88317883178831,80.74746967109562],[100.1872018720187,79.77932614998971],[99.93879938799387,78.88057753162039]]],[[[-87,79.7],[-87.2,79],[-90.8,78.2],[-94,78.8],[-93.1,79.4],[-96.1,79.7],[-96,80.6],[-94.3,81],[-92.4,81.3],[-89.4,80.5],[-87,79.7]]],[[[-68.5,83.1],[-63.7,82.9],[-61.9,82.4],[-66.8,81.7],[-65.5,81.5],[-69.5,80.6],[-73.2,79.6],[-76.9,79.3],[-76.2,79],[-76.3,78.2],[-78.4,77.5],[-79.6,77],[-77.9,76.8],[-83.2,76.5],[-87.6,76.4],[-89.6,77],[-88.3,77.9],[-85,77.5],[-88,78.4],[-85.4,79],[-86.5,79.7],[-84.2,80.2],[-81.8,80.5],[-87.6,80.5],[-90.2,81.3],[-91.6,81.9],[-88.9,82.1],[-85.5,82.7],[-83.2,82.3],[-81.1,83],[-76.3,83.2],[-72.8,83.2],[-68.5,83.1]]],[[[-27.1,83.5],[-22.7,82.3],[-31.9,82.2],[-27.9,82.1],[-22.9,82.1],[-23.2,81.2],[-15.8,81.9],[-12.2,81.3],[-16.8,80.3],[-17.7,80.1],[-19.7,78.8],[-18.5,77],[-21.7,76.6],[-19.6,75.2],[-19.4,74.3],[-20.4,73.8],[-22.2,73.3],[-22.3,72.6],[-24.3,72.6],[-23.4,72.1],[-21.8,70.7],[-24.3,70.9],[-25.2,70.8],[-23.7,70.2],[-25,69.3],[-30.7,68.1],[-32.8,67.7],[-36.4,66],[-38.4,65.7],[-40.7,64.8],[-41.2,63.5],[-42.4,61.9],[-43.4,60.1],[-46.3,60.9],[-49.2,61.4],[-51.6,63.6],[-52.3,65.2],[-53.3,66.8],[-53,68.4],[-51.1,69.1],[-52,69.6],[-53.5,69.3],[-54.8,70.3],[-53.4,70.8],[-53.1,71.2],[-55,71.4],[-54.7,72.6],[-56.1,73.7],[-58.6,75.1],[-61.3,76.1],[-66.1,76.1],[-69.7,76.4],[-68.8,77.3],[-71,77.6],[-73.2,78.4],[-65.7,79.4],[-68,80.1],[-63.7,81.2],[-62.6,81.8],[-57.2,82.2],[-53,81.9],[-48,82.1],[-44.5,81.7],[-46.8,82.6],[-39.9,83.2],[-35.1,83.6],[-27.1,83.5]]]]}};
    const NATIONS = [{"id":"wash","name":"Washington","lon":-77.03,"lat":38.9,"color":"var(--globe-route-crimson, #e11d48)"},{"id":"geneva","name":"Geneva","lon":6.14,"lat":46.2,"color":"var(--globe-route-oxford, #1e3a8a)"},{"id":"tokyo","name":"Tokyo","lon":139.69,"lat":35.68,"color":"var(--globe-route-gold, #d97706)"},{"id":"nairobi","name":"Nairobi","lon":36.82,"lat":-1.29,"color":"var(--globe-route-oxford, #1e3a8a)"},{"id":"brasilia","name":"Brasilia","lon":-47.88,"lat":-15.79,"color":"var(--globe-route-crimson, #e11d48)"},{"id":"singapore","name":"Singapore","lon":103.82,"lat":1.35,"color":"var(--globe-route-gold, #d97706)"},{"id":"london","name":"London","lon":-0.12,"lat":51.5,"color":"var(--globe-route-oxford, #1e3a8a)"},{"id":"jakarta","name":"Jakarta","lon":106.84,"lat":-6.2,"color":"var(--globe-route-gold, #d97706)"}];
    const ROUTES = [{"from":0,"to":1,"cls":"route-crimson"},{"from":1,"to":3,"cls":"route-oxford"},{"from":1,"to":5,"cls":"route-gold"},{"from":5,"to":2,"cls":"route-gold"},{"from":6,"to":7,"cls":"route-oxford"},{"from":0,"to":4,"cls":"route-crimson"},{"from":7,"to":3,"cls":"route-oxford"}];

    const container = document.getElementById("ir-globe-container");
    const svg = document.getElementById("ir-globe-svg");
    const hitbox = document.getElementById("ir-globe-hitbox");
    const landEl = document.getElementById("ir-globe-land");
    const gratEl = document.getElementById("ir-globe-grat");
    const routeEls = Array.from(document.querySelectorAll("#ir-globe-routes path"));
    const nodeEls = Array.from(document.querySelectorAll("#ir-globe-nodes circle"));
    const telemetry = document.getElementById("globe-telemetry");

    if (!container || !svg || !landEl) return;

    // D3 Orthographic Projection: scale 208, center [260, 268]
    const proj = d3.geoOrthographic()
      .scale(208)
      .translate([260, 268])
      .clipAngle(90);

    const pathGen = d3.geoPath(proj);
    const graticuleData = d3.geoGraticule().step([30, 30])();

    let yawDeg = -30;
    let pitchDeg = -15;
    let autoSpinSpeed = 10.0;
    let currentSpeed = 10.0;
    let isDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;
    let dragStartYaw = 0;
    let dragStartPitch = 0;
    let lastX = 0;
    let lastTime = 0;
    let flingVelocity = 0;
    let lastFrameTime = performance.now();

    function render() {
      proj.rotate([yawDeg, pitchDeg, 0]);

      // 1. Render continents
      const landD = pathGen(LAND);
      if (landD) landEl.setAttribute("d", landD);

      // 2. Render graticule
      const gratD = pathGen(graticuleData);
      if (gratD) gratEl.setAttribute("d", gratD);

      // 3. Render routes
      for (let i = 0; i < ROUTES.length; i++) {
        const r = ROUTES[i];
        const geo = {
          type: "LineString",
          coordinates: [[NATIONS[r.from].lon, NATIONS[r.from].lat], [NATIONS[r.to].lon, NATIONS[r.to].lat]]
        };
        const d = pathGen(geo);
        routeEls[i].setAttribute("d", d || "");
      }

      // 4. Render nodes
      for (let i = 0; i < NATIONS.length; i++) {
        const pt = proj([NATIONS[i].lon, NATIONS[i].lat]);
        if (pt) {
          nodeEls[i].setAttribute("cx", pt[0].toFixed(1));
          nodeEls[i].setAttribute("cy", pt[1].toFixed(1));
          nodeEls[i].style.display = "";
        } else {
          nodeEls[i].style.display = "none";
        }
      }

      // 5. Update telemetry display
      if (telemetry) {
        const normYaw = Math.round(((yawDeg % 360) + 360) % 360);
        telemetry.textContent = (isDragging ? "Rotating " : "Click & drag to spin • ") + normYaw + "°";
      }
    }

    function loop(now) {
      const dt = Math.min((now - lastFrameTime) / 1000, 1 / 20);
      lastFrameTime = now;

      if (!isDragging) {
        currentSpeed += (autoSpinSpeed - currentSpeed) * (1 - Math.exp(-dt / 0.7));
        yawDeg += currentSpeed * dt;
        render();
      }

      requestAnimationFrame(loop);
    }

    function onPointerDown(e) {
      if (e.button !== undefined && e.button !== 0) return;
      isDragging = true;
      dragStartX = e.clientX;
      dragStartY = e.clientY;
      dragStartYaw = yawDeg;
      dragStartPitch = pitchDeg;
      lastX = e.clientX;
      lastTime = performance.now();
      flingVelocity = 0;

      container.classList.add("is-dragging");
      try {
        hitbox.setPointerCapture(e.pointerId);
      } catch (err) {}

      if (e.preventDefault) e.preventDefault();
      render();
    }

    function onPointerMove(e) {
      if (!isDragging) return;
      const now = performance.now();
      const dt = Math.max(0.001, (now - lastTime) / 1000);
      const dx = e.clientX - dragStartX;
      const dy = e.clientY - dragStartY;

      yawDeg = dragStartYaw + dx * 0.35;
      pitchDeg = Math.max(-55, Math.min(55, dragStartPitch - dy * 0.2));

      const instantV = ((e.clientX - lastX) / dt) * 0.35;
      flingVelocity = flingVelocity * 0.3 + instantV * 0.7;

      lastX = e.clientX;
      lastTime = now;

      render();
    }

    function onPointerUp(e) {
      if (!isDragging) return;
      isDragging = false;
      container.classList.remove("is-dragging");

      try {
        hitbox.releasePointerCapture(e.pointerId);
      } catch (err) {}

      if (Math.abs(flingVelocity) > 25) {
        currentSpeed = Math.max(-180, Math.min(180, flingVelocity));
      } else {
        currentSpeed = autoSpinSpeed;
      }

      render();
    }

    hitbox.addEventListener("pointerdown", onPointerDown);
    hitbox.addEventListener("pointermove", onPointerMove);
    hitbox.addEventListener("pointerup", onPointerUp);
    hitbox.addEventListener("pointercancel", onPointerUp);

    render();
    requestAnimationFrame(loop);
  })();
</script>
