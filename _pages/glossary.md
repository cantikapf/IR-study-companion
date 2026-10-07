---
layout: default
title: Academic Glossary of International Relations
permalink: /glossary.html
---

<div class="home-viewport" style="max-width: 960px;">
  <header class="home-hero" style="margin-bottom: 2rem;">
    <div class="home-eyebrow">Academic Reference &bull; {{ site.data.ir_glossary | size }} Curated Concepts</div>
    <h1 class="home-title">Curated IR Glossary</h1>
    <p class="home-description">
      An academic reference glossary of International Relations featuring <strong>intuitive plain-language breakdowns</strong> designed to make complex theoretical frameworks, strategic security dilemmas, political economy structures, international law, diplomacy, and regionalism clear and accessible.
    </p>
  </header>

  <!-- Interactive Search & Category Filter -->
  <div style="background: var(--lms-surface); border: 1px solid var(--lms-hairline); border-radius: var(--lms-radius-lg); padding: 1.25rem 1.5rem; margin-bottom: 2rem; box-shadow: var(--lms-shadow-sm);">
    <div style="display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1rem; background: var(--lms-subtle); padding: 0.75rem 1rem; border-radius: var(--lms-radius-md); border: 1px solid var(--lms-hairline);">
      <i class="fa fa-search" aria-hidden="true" style="color: var(--lms-ink-tertiary);"></i>
      <input type="text" id="glossary-search" placeholder="Search concepts, terms, key scholars, or plain-language definitions..." style="background: transparent; border: none; outline: none; width: 100%; font-size: 0.95rem; color: var(--lms-ink-primary);">
    </div>

    <!-- Category Filter Pills -->
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;" id="glossary-category-pills">
      <button class="glossary-filter-pill is-active" data-cat="all">All Concepts ({{ site.data.ir_glossary | size }})</button>
      <button class="glossary-filter-pill" data-cat="Theory & Epistemology">Theories & Epistemology</button>
      <button class="glossary-filter-pill" data-cat="Security & Strategy">Security & Strategy</button>
      <button class="glossary-filter-pill" data-cat="Political Economy">Political Economy (IPE)</button>
      <button class="glossary-filter-pill" data-cat="International Law">International Law & IOs</button>
      <button class="glossary-filter-pill" data-cat="Diplomacy & FPA">Diplomacy & FPA</button>
      <button class="glossary-filter-pill" data-cat="Regionalism & Indonesia">Regionalism & Indonesia</button>
    </div>
  </div>

  <div style="font-size: 0.85rem; color: var(--lms-ink-tertiary); margin-bottom: 1.5rem; font-variant-numeric: tabular-nums;">
    Showing <span id="glossary-visible-count">{{ site.data.ir_glossary | size }}</span> concepts
  </div>

  <!-- Glossary Cards Container -->
  <div id="glossary-container" style="display: flex; flex-direction: column; gap: 1.25rem;">
    {% for item in site.data.ir_glossary %}
      <article class="glossary-item-card" data-cat="{{ item.category }}" data-term="{{ item.term | downcase }}" data-scholars="{{ item.scholars | downcase }}" data-def="{{ item.definition | downcase }}" data-plain="{{ item.plain_en | default: item.plain_id | downcase }}">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 1rem; margin-bottom: 0.4rem;">
          <h2 style="font-size: 1.25rem; font-weight: 750; margin: 0; color: var(--lms-ink-primary);">
            {{ item.term }}
          </h2>
          <span style="font-size: 0.7rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; padding: 0.2rem 0.55rem; border-radius: var(--lms-radius-pill); background: var(--lms-subtle); border: 1px solid var(--lms-hairline); color: var(--lms-ink-secondary); white-space: nowrap;">
            {{ item.category }}
          </span>
        </div>

        {% if item.scholars %}
          <div style="font-size: 0.825rem; font-weight: 600; color: var(--lms-ink-tertiary); margin-bottom: 0.75rem;">
            <i class="fa fa-book" aria-hidden="true"></i> Key Scholars & Sources: {{ item.scholars }}
          </div>
        {% endif %}

        {% if item.plain_en %}
          <div class="glossary-plain-note">
            <span class="glossary-plain-label"><i class="fa fa-lightbulb-o" aria-hidden="true"></i> In Simple Terms (Plain-Language Note)</span>
            <p class="glossary-plain-text">{{ item.plain_en }}</p>
          </div>
        {% elsif item.plain_id %}
          <div class="glossary-plain-note">
            <span class="glossary-plain-label"><i class="fa fa-lightbulb-o" aria-hidden="true"></i> In Simple Terms (Plain-Language Note)</span>
            <p class="glossary-plain-text">{{ item.plain_id }}</p>
          </div>
        {% endif %}

        <p style="font-size: 0.92rem; line-height: 1.6; color: var(--lms-ink-secondary); margin: 0 0 1rem;">
          <strong style="color: var(--lms-ink-primary);">Academic Definition:</strong> {{ item.definition }}
        </p>

        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 0.75rem; border-top: 1px solid var(--lms-hairline); font-size: 0.825rem;">
          <span style="color: var(--lms-ink-tertiary);">Module {{ item.module }}</span>
          {% if item.chapter_slug %}
            <a href="{{ site.baseurl }}/{{ item.chapter_slug }}.html" style="font-weight: 600; color: var(--lms-ink-primary); text-decoration: none; display: inline-flex; align-items: center; gap: 0.35rem;">
              <span>Study in Lesson</span> <i class="fa fa-arrow-right"></i>
            </a>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </div>
</div>

<style>
.glossary-filter-pill {
  background: var(--lms-subtle);
  border: 1px solid var(--lms-hairline);
  color: var(--lms-ink-secondary);
  font-size: 0.775rem;
  font-weight: 600;
  padding: 0.35rem 0.75rem;
  border-radius: var(--lms-radius-pill);
  cursor: pointer;
  transition: all var(--lms-duration) var(--lms-ease);
}
.glossary-filter-pill:hover {
  background: var(--lms-hover);
  color: var(--lms-ink-primary);
}
.glossary-filter-pill.is-active {
  background: var(--lms-ink-primary);
  color: var(--lms-canvas);
  border-color: var(--lms-ink-primary);
}
body.dark-theme .glossary-filter-pill.is-active {
  background: #f4f4f5;
  color: #09090b;
}
.glossary-item-card {
  background: var(--lms-surface);
  border: 1px solid var(--lms-hairline);
  border-radius: var(--lms-radius-md);
  padding: 1.35rem 1.65rem;
  transition: all var(--lms-duration) var(--lms-ease);
  box-shadow: var(--lms-shadow-sm);
}
.glossary-item-card:hover {
  border-color: var(--lms-border-strong);
  transform: translateY(-1px);
  box-shadow: var(--lms-shadow-md);
}
.glossary-plain-note {
  background: rgba(16, 185, 129, 0.08);
  border-left: 3px solid #10b981;
  padding: 0.65rem 0.95rem;
  border-radius: 0 var(--lms-radius-sm) var(--lms-radius-sm) 0;
  margin-bottom: 0.85rem;
}
body.dark-theme .glossary-plain-note {
  background: rgba(16, 185, 129, 0.14);
  border-left-color: #34d399;
}
.glossary-plain-label {
  display: block;
  font-size: 0.775rem;
  font-weight: 750;
  color: #059669;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.25rem;
}
body.dark-theme .glossary-plain-label {
  color: #34d399;
}
.glossary-plain-text {
  font-size: 0.9rem;
  line-height: 1.55;
  color: var(--lms-ink-primary);
  margin: 0;
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('glossary-search');
    const pills = document.querySelectorAll('.glossary-filter-pill');
    const cards = document.querySelectorAll('.glossary-item-card');
    const countEl = document.getElementById('glossary-visible-count');

    let currentCat = 'all';
    let currentQuery = '';

    function filterCards() {
        let visible = 0;
        cards.forEach(card => {
            const cat = card.getAttribute('data-cat');
            const term = card.getAttribute('data-term') || '';
            const scholars = card.getAttribute('data-scholars') || '';
            const def = card.getAttribute('data-def') || '';
            const plain = card.getAttribute('data-plain') || '';

            const matchesCat = (currentCat === 'all') || (cat === currentCat) || (currentCat === 'Regionalism & Indonesia' && (cat === 'Regionalism & ASEAN' || cat === 'Indonesian Diplomacy'));
            const matchesQuery = !currentQuery || term.includes(currentQuery) || scholars.includes(currentQuery) || def.includes(currentQuery) || plain.includes(currentQuery);

            if (matchesCat && matchesQuery) {
                card.style.display = '';
                visible++;
            } else {
                card.style.display = 'none';
            }
        });
        if (countEl) countEl.textContent = visible;
    }

    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            currentQuery = e.target.value.toLowerCase().trim();
            filterCards();
        });
    }

    pills.forEach(pill => {
        pill.addEventListener('click', () => {
            pills.forEach(p => p.classList.remove('is-active'));
            pill.classList.add('is-active');
            currentCat = pill.getAttribute('data-cat');
            filterCards();
        });
    });
});
</script>
