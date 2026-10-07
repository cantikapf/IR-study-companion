/**
 * IR Study Companion - Bespoke LMS Engine
 * Focus View, Curriculum Drawer, Progress Synchronization
 */

(function() {
  'use strict';

  function initLMS() {
    initDrawer();
    initProgress();
    initReadingTime();
    initSearchFilter();
    initKeyboardShortcuts();
    initSyncModal();
    initBookmarks();
    initCelebration();
    initTermNotes();
  }

  // --- Curriculum Drawer Controls ---
  function initDrawer() {
    const drawer = document.getElementById('curriculum-drawer');
    const backdrop = document.getElementById('curriculum-drawer-backdrop');
    const openBtns = document.querySelectorAll('.js-open-drawer');
    const closeBtn = document.getElementById('drawer-close-btn');

    if (!drawer) return;

    function openDrawer() {
      drawer.classList.add('is-open');
      if (backdrop) backdrop.classList.add('is-visible');
      drawer.setAttribute('aria-hidden', 'false');
      document.body.classList.add('lms-drawer-locked');
      const searchInput = document.getElementById('drawer-search-input');
      if (searchInput) setTimeout(() => searchInput.focus(), 150);
    }

    function closeDrawer() {
      drawer.classList.remove('is-open');
      if (backdrop) backdrop.classList.remove('is-visible');
      drawer.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('lms-drawer-locked');
    }

    openBtns.forEach(btn => btn.addEventListener('click', (e) => {
      e.preventDefault();
      openDrawer();
    }));

    if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
    if (backdrop) backdrop.addEventListener('click', closeDrawer);

    // Expose globally
    window.lmsOpenDrawer = openDrawer;
    window.lmsCloseDrawer = closeDrawer;
  }

  // --- Progress Sync across Topbar, Action Bar, and Drawer ---
  function initProgress() {
    function updateState() {
      const items = document.querySelectorAll('.drawer-lesson-item[data-slug]');
      let completedCount = 0;
      const totalCount = items.length || 157;

      items.forEach(item => {
        const slug = item.getAttribute('data-slug');
        const isDone = localStorage.getItem('chapter_read_' + slug) === 'true';
        if (isDone) {
          item.classList.add('is-completed');
          completedCount++;
        } else {
          item.classList.remove('is-completed');
        }
      });

      const pct = Math.round((completedCount / totalCount) * 100);

      // Topbar Indicators
      const topbarPct = document.getElementById('topbar-progress-pct');
      const topbarFill = document.getElementById('topbar-progress-fill');
      if (topbarPct) topbarPct.textContent = pct + '%';
      if (topbarFill) topbarFill.style.width = pct + '%';

      // Drawer Indicators
      const drawerDone = document.getElementById('drawer-completed-count');
      const drawerTotal = document.getElementById('drawer-total-count');
      if (drawerDone) drawerDone.textContent = completedCount;
      if (drawerTotal) drawerTotal.textContent = totalCount;

      // Update per-module progress pills in Curriculum Drawer
      const moduleGroups = document.querySelectorAll('.drawer-module-group');
      moduleGroups.forEach(group => {
        const pill = group.querySelector('.drawer-module-progress-pill');
        if (!pill) return;
        const modLessons = group.querySelectorAll('.drawer-lesson-item');
        let modDone = 0;
        modLessons.forEach(l => {
          if (l.classList.contains('is-completed')) modDone++;
        });
        const modPct = modLessons.length ? Math.round((modDone / modLessons.length) * 100) : 0;
        pill.textContent = modPct + '%';
        if (modPct === 100 && modLessons.length > 0) {
          pill.classList.add('is-complete');
          pill.textContent = '✓ 100%';
        } else {
          pill.classList.remove('is-complete');
        }
      });
    }

    updateState();
    window.addEventListener('chapter_read', updateState);
    window.addEventListener('storage', updateState);
  }

  // --- Automatic Estimated Reading Time ---
  function initReadingTime() {
    const article = document.querySelector('.course-prose-body');
    const targetEl = document.getElementById('lesson-reading-time');
    if (!article || !targetEl) return;

    const words = article.innerText.trim().split(/\s+/).length;
    const minutes = Math.max(1, Math.ceil(words / 200));
    targetEl.textContent = minutes + ' min read';
  }

  // --- Drawer Deep Curriculum Search ---
  function initSearchFilter() {
    const searchInput = document.getElementById('drawer-search-input');
    if (!searchInput) return;

    let searchIndex = null;
    const indexBySlug = {};

    function fetchIndex() {
      if (searchIndex) return;
      const base = window.__siteBaseurl || '';
      fetch(base + '/assets/data/search_index.json')
        .then(res => res.json())
        .then(data => {
          searchIndex = data;
          data.forEach(item => {
            if (item.slug) indexBySlug[item.slug] = item;
          });
        })
        .catch(() => {});
    }

    // Preload index on focus
    searchInput.addEventListener('focus', fetchIndex, { once: true });

    searchInput.addEventListener('input', (e) => {
      fetchIndex();
      const query = e.target.value.toLowerCase().trim();
      const groups = document.querySelectorAll('.drawer-module-group');

      groups.forEach(group => {
        const lessons = group.querySelectorAll('.drawer-lesson-item');
        let hasMatchInGroup = false;

        lessons.forEach(lesson => {
          const slug = lesson.getAttribute('data-slug');
          const titleText = lesson.textContent.toLowerCase();
          let isMatch = false;

          if (query === '') {
            isMatch = true;
          } else if (titleText.includes(query)) {
            isMatch = true;
          } else if (slug && indexBySlug[slug]) {
            const entry = indexBySlug[slug];
            const inAbstract = entry.abstract && entry.abstract.toLowerCase().includes(query);
            const inHeadings = entry.headings && entry.headings.some(h => h.toLowerCase().includes(query));
            const inKeywords = entry.keywords && entry.keywords.some(k => k.toLowerCase().includes(query));
            if (inAbstract || inHeadings || inKeywords) {
              isMatch = true;
            }
          }

          if (isMatch) {
            lesson.style.display = '';
            hasMatchInGroup = true;
          } else {
            lesson.style.display = 'none';
          }
        });

        group.style.display = hasMatchInGroup ? '' : 'none';
      });
    });
  }

  // --- Keyboard Accessibility ---
  function initKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
      // ESC closes drawer
      if (e.key === 'Escape') {
        if (typeof window.lmsCloseDrawer === 'function') {
          window.lmsCloseDrawer();
        }
      }
      // Pressing 's' or 'S' when not focused on input opens Syllabus
      if ((e.key === 's' || e.key === 'S') && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
        if (!document.getElementById('curriculum-drawer')?.classList.contains('is-open')) {
          if (typeof window.lmsOpenDrawer === 'function') {
            e.preventDefault();
            window.lmsOpenDrawer();
          }
        }
      }
    });
  }

  // --- Progress Sync Manager (Export/Import/Reset) ---
  function initSyncModal() {
    const modal = document.getElementById('progress-sync-modal');
    const backdrop = document.getElementById('progress-sync-backdrop');
    const openBtns = document.querySelectorAll('.js-open-sync');
    const closeBtn = document.getElementById('sync-modal-close');
    const exportBtn = document.getElementById('btn-export-progress');
    const importInput = document.getElementById('input-import-progress');
    const resetBtn = document.getElementById('btn-reset-progress');
    const feedback = document.getElementById('sync-feedback');

    if (!modal) return;

    function getStats() {
      let lessons = 0, quizzes = 0, exams = 0;
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith('chapter_read_') && localStorage.getItem(k) === 'true') lessons++;
        if (k && k.startsWith('quiz_') && k.endsWith('_completed') && localStorage.getItem(k) === 'true') quizzes++;
        if (k && k.startsWith('exam_module_') && k.endsWith('_passed') && localStorage.getItem(k) === 'true') exams++;
      }
      return { lessons, quizzes, exams };
    }

    function updateModalStats() {
      const stats = getStats();
      const elLessons = document.getElementById('sync-stat-lessons');
      const elQuizzes = document.getElementById('sync-stat-quizzes');
      const elExams = document.getElementById('sync-stat-exams');
      if (elLessons) elLessons.textContent = stats.lessons;
      if (elQuizzes) elQuizzes.textContent = stats.quizzes;
      if (elExams) elExams.textContent = stats.exams;
    }

    function openModal() {
      updateModalStats();
      if (feedback) feedback.style.display = 'none';
      modal.classList.add('is-open');
      if (backdrop) backdrop.classList.add('is-visible');
      modal.setAttribute('aria-hidden', 'false');
    }

    function closeModal() {
      modal.classList.remove('is-open');
      if (backdrop) backdrop.classList.remove('is-visible');
      modal.setAttribute('aria-hidden', 'true');
    }

    openBtns.forEach(btn => btn.addEventListener('click', (e) => {
      e.preventDefault();
      openModal();
    }));

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (backdrop) backdrop.addEventListener('click', closeModal);

    // Export progress to JSON file
    if (exportBtn) {
      exportBtn.addEventListener('click', () => {
        const payload = {
          app: "IR Study Companion",
          version: "1.0",
          exportDate: new Date().toISOString(),
          stats: getStats(),
          storage: {}
        };
        for (let i = 0; i < localStorage.length; i++) {
          const k = localStorage.key(i);
          if (k && (k.startsWith('chapter_read_') || k.startsWith('quiz_') || k.startsWith('exam_') || k.startsWith('bookmark_'))) {
            payload.storage[k] = localStorage.getItem(k);
          }
        }
        const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        const dateStr = new Date().toISOString().slice(0, 10);
        a.href = url;
        a.download = `ir-study-progress-${dateStr}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        if (feedback) {
          feedback.innerHTML = "<strong>Backup exported successfully!</strong> Keep this file safe or transfer it to another browser/device.";
          feedback.className = "lms-sync-feedback is-success";
          feedback.style.display = "block";
        }
      });
    }

    // Import progress from JSON file
    if (importInput) {
      importInput.addEventListener('change', (e) => {
        const file = e.target.files && e.target.files[0];
        if (!file) return;

        const reader = new FileReader();
        reader.onload = (event) => {
          try {
            const data = JSON.parse(event.target.result);
            if (!data || !data.storage) {
              throw new Error("Invalid format. Missing storage payload.");
            }
            let restoredKeys = 0;
            Object.keys(data.storage).forEach(k => {
              if (k.startsWith('chapter_read_') || k.startsWith('quiz_') || k.startsWith('exam_') || k.startsWith('bookmark_')) {
                localStorage.setItem(k, data.storage[k]);
                restoredKeys++;
              }
            });
            updateModalStats();
            window.dispatchEvent(new Event('chapter_read'));
            window.dispatchEvent(new Event('quiz_completed'));
            if (feedback) {
              feedback.innerHTML = `<strong>Progress restored successfully!</strong> Restored ${restoredKeys} items. Your course progress is now updated.`;
              feedback.className = "lms-sync-feedback is-success";
              feedback.style.display = "block";
            }
          } catch (err) {
            if (feedback) {
              feedback.innerHTML = `<strong>Import failed:</strong> Could not parse JSON file. Please ensure it is a valid backup.`;
              feedback.className = "lms-sync-feedback is-error";
              feedback.style.display = "block";
            }
          }
        };
        reader.readAsText(file);
      });
    }

    // Reset progress
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        const confirmed = window.confirm("Are you sure you want to reset all your learning progress? This will clear all completed lessons, quiz scores, and bookmarks.");
        if (confirmed) {
          const keysToRemove = [];
          for (let i = 0; i < localStorage.length; i++) {
            const k = localStorage.key(i);
            if (k && (k.startsWith('chapter_read_') || k.startsWith('quiz_') || k.startsWith('exam_') || k.startsWith('bookmark_'))) {
              keysToRemove.push(k);
            }
          }
          keysToRemove.forEach(k => localStorage.removeItem(k));
          updateModalStats();
          window.dispatchEvent(new Event('chapter_read'));
          window.dispatchEvent(new Event('quiz_completed'));
          if (feedback) {
            feedback.innerHTML = "<strong>All progress has been reset.</strong> You can now start learning anew.";
            feedback.className = "lms-sync-feedback is-success";
            feedback.style.display = "block";
          }
        }
      });
    }

    window.lmsOpenSyncModal = openModal;
    window.lmsCloseSyncModal = closeModal;
  }

  // --- Bookmark Lesson Manager ---
  function initBookmarks() {
    const bookmarkBtn = document.getElementById('lesson-bookmark-btn');
    if (!bookmarkBtn) return;

    const slug = bookmarkBtn.getAttribute('data-slug');
    if (!slug) return;

    const key = 'bookmark_' + slug;
    const label = bookmarkBtn.querySelector('.bookmark-label');
    const icon = bookmarkBtn.querySelector('i');

    function updateBtn(isSaved) {
      if (isSaved) {
        bookmarkBtn.classList.add('is-bookmarked');
        if (label) label.textContent = 'Saved';
        if (icon) icon.className = 'fa fa-bookmark';
      } else {
        bookmarkBtn.classList.remove('is-bookmarked');
        if (label) label.textContent = 'Bookmark';
        if (icon) icon.className = 'fa fa-bookmark-o';
      }
    }

    updateBtn(localStorage.getItem(key) === 'true');

    bookmarkBtn.addEventListener('click', () => {
      const currentState = localStorage.getItem(key) === 'true';
      const newState = !currentState;
      if (newState) {
        localStorage.setItem(key, 'true');
      } else {
        localStorage.removeItem(key);
      }
      updateBtn(newState);
    });
  }

  // --- Milestone Celebration Micro-Interaction ---
  function initCelebration() {
    function launchConfetti() {
      const canvas = document.createElement('canvas');
      canvas.style.position = 'fixed';
      canvas.style.inset = '0';
      canvas.style.width = '100vw';
      canvas.style.height = '100vh';
      canvas.style.pointerEvents = 'none';
      canvas.style.zIndex = '99999';
      document.body.appendChild(canvas);

      const ctx = canvas.getContext('2d');
      const w = canvas.width = window.innerWidth;
      const h = canvas.height = window.innerHeight;

      const particles = [];
      const colors = ['#10b981', '#6366f1', '#f59e0b', '#ec4899', '#3b82f6'];

      for (let i = 0; i < 60; i++) {
        particles.push({
          x: w / 2 + (Math.random() - 0.5) * 200,
          y: h * 0.7,
          vx: (Math.random() - 0.5) * 12,
          vy: -Math.random() * 14 - 6,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          vRot: (Math.random() - 0.5) * 10,
          opacity: 1
        });
      }

      let start = null;
      function frame(ts) {
        if (!start) start = ts;
        const elapsed = ts - start;
        ctx.clearRect(0, 0, w, h);

        particles.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.4;
          p.rotation += p.vRot;
          p.opacity = Math.max(0, 1 - (elapsed / 2500));

          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rotation * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.globalAlpha = p.opacity;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
          ctx.restore();
        });

        if (elapsed < 2500) {
          requestAnimationFrame(frame);
        } else {
          canvas.remove();
        }
      }
      requestAnimationFrame(frame);
    }

    window.addEventListener('exam_passed', launchConfetti);
  }

  // --- Global Specialized Terminology Notes & Popover System ---
  function initTermNotes() {
    const article = document.getElementById('course-article-body');
    const digestSection = document.getElementById('lesson-terms-digest');
    const digestGrid = document.getElementById('lesson-terms-grid');
    const countBadge = document.getElementById('lesson-terms-count-badge');

    if (!article) return;

    const base = window.__siteBaseurl || '';
    const glossaryUrl = base + '/assets/data/ir_glossary.json';

    fetch(glossaryUrl)
      .then(res => {
        if (!res.ok) throw new Error('Glossary network error');
        return res.json();
      })
      .then(glossary => {
        if (!Array.isArray(glossary) || glossary.length === 0) return;
        setupTerminologyEngine(glossary, article, digestSection, digestGrid, countBadge, base);
      })
      .catch(err => {
        console.warn('Terminology Engine: Note data unavailable', err);
      });
  }

  function setupTerminologyEngine(glossary, article, digestSection, digestGrid, countBadge, base) {
    const termLookup = [];
    glossary.forEach((item, index) => {
      const aliases = new Set();
      const rawTerm = item.term.trim();
      aliases.add(rawTerm);

      const match = rawTerm.match(/^(.*?)\s*\((.*?)\)$/);
      if (match) {
        aliases.add(match[1].trim());
        const paren = match[2].trim();
        if (paren.includes('/')) {
          paren.split('/').forEach(p => aliases.add(p.trim()));
        } else {
          aliases.add(paren);
        }
      }

      const cleanTerm = rawTerm.replace(/\s*\(.*?\)/g, '').trim();
      if (cleanTerm.length >= 3) {
        aliases.add(cleanTerm);
        if (cleanTerm.endsWith('s')) {
          aliases.add(cleanTerm.slice(0, -1));
        } else {
          aliases.add(cleanTerm + 's');
        }
        if (cleanTerm.includes('Realism')) aliases.add(cleanTerm.replace('Realism', 'Realist'));
        if (cleanTerm.includes('Constructivism')) aliases.add(cleanTerm.replace('Constructivism', 'Constructivist'));
        if (cleanTerm.includes('Institutionalism')) aliases.add(cleanTerm.replace('Institutionalism', 'Institutionalist'));
        if (cleanTerm.includes('Liberalism')) aliases.add(cleanTerm.replace('Liberalism', 'Liberalist'));
        if (cleanTerm.includes('Mercantilism')) aliases.add(cleanTerm.replace('Mercantilism', 'Mercantilist'));
      }

      aliases.forEach(alias => {
        if (alias.length >= 3) {
          termLookup.push({
            alias: alias,
            length: alias.length,
            glossaryIndex: index,
            item: item
          });
        }
      });
    });

    termLookup.sort((a, b) => b.length - a.length);

    const matchedTermsMap = new Map();
    const annotatedTerms = new Set();

    const walker = document.createTreeWalker(
      article,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function(node) {
          const parent = node.parentElement;
          if (!parent) return NodeFilter.FILTER_REJECT;
          const tag = parent.tagName.toLowerCase();
          if (['script', 'style', 'code', 'pre', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'button', 'input'].includes(tag)) {
            return NodeFilter.FILTER_REJECT;
          }
          if (parent.closest('.simple-words-box, .quiz-container, .flashcards-container, .sim-container, .lesson-terms-digest')) {
            return NodeFilter.FILTER_REJECT;
          }
          if (node.nodeValue.trim().length < 4) {
            return NodeFilter.FILTER_REJECT;
          }
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    const textNodes = [];
    let currentNode;
    while ((currentNode = walker.nextNode())) {
      textNodes.push(currentNode);
    }

    textNodes.forEach(node => {
      let text = node.nodeValue;
      for (let i = 0; i < termLookup.length; i++) {
        const entry = termLookup[i];
        if (annotatedTerms.has(entry.item.term)) continue;

        const escaped = entry.alias.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const regex = new RegExp('\\b(' + escaped + ')\\b', 'i');
        const match = regex.exec(text);

        if (match) {
          const matchIndex = match.index;
          const matchLength = match[0].length;
          const matchedText = text.substring(matchIndex, matchIndex + matchLength);

          const beforeText = text.substring(0, matchIndex);
          const afterText = text.substring(matchIndex + matchLength);

          const span = document.createElement('span');
          span.className = 'ir-term-mention';
          span.setAttribute('tabindex', '0');
          span.setAttribute('role', 'button');
          span.setAttribute('aria-haspopup', 'dialog');
          span.setAttribute('data-term-index', entry.glossaryIndex);

          span.appendChild(document.createTextNode(matchedText));

          const indicator = document.createElement('span');
          indicator.className = 'ir-term-indicator';
          indicator.textContent = 'ℹ';
          span.appendChild(indicator);

          const parent = node.parentNode;
          if (!parent) break;

          const fragment = document.createDocumentFragment();
          if (beforeText) fragment.appendChild(document.createTextNode(beforeText));
          fragment.appendChild(span);
          if (afterText) fragment.appendChild(document.createTextNode(afterText));

          parent.replaceChild(fragment, node);

          annotatedTerms.add(entry.item.term);
          matchedTermsMap.set(entry.item.term, entry.item);
          break;
        }
      }
    });

    let popover = document.getElementById('ir-floating-popover');
    if (!popover) {
      popover = document.createElement('div');
      popover.id = 'ir-floating-popover';
      popover.className = 'ir-term-popover';
      popover.setAttribute('role', 'dialog');
      popover.setAttribute('aria-hidden', 'true');
      document.body.appendChild(popover);
    }

    let hideTimeout = null;

    function showPopover(mentionEl, itemIndex) {
      if (hideTimeout) clearTimeout(hideTimeout);
      const item = glossary[itemIndex];
      if (!item) return;

      popover.innerHTML = `
        <div class="ir-popover-header">
          <h4 class="ir-popover-title">${item.term}</h4>
          <span class="ir-popover-badge">${item.category}</span>
        </div>
        ${(item.plain_en || item.plain_id) ? `
          <div class="ir-popover-plain-box">
            <span class="ir-popover-plain-label"><i class="fa fa-lightbulb-o"></i> In Simple Terms</span>
            <p class="ir-popover-plain-text">${item.plain_en || item.plain_id}</p>
          </div>
        ` : ''}
        <p class="ir-popover-academic-text"><strong>Definition:</strong> ${item.definition}</p>
        <div class="ir-popover-footer">
          <span class="ir-popover-scholars" title="${item.scholars || ''}">${item.scholars || ''}</span>
          <a href="${base}/glossary.html" class="ir-popover-link">Glossary <i class="fa fa-arrow-right"></i></a>
        </div>
      `;

      const rect = mentionEl.getBoundingClientRect();
      const popoverWidth = 320;
      let left = rect.left + (rect.width / 2) - (popoverWidth / 2);
      left = Math.max(16, Math.min(window.innerWidth - popoverWidth - 16, left));

      const popoverHeight = 220;
      let top;
      if (rect.top > popoverHeight + 20) {
        top = rect.top - popoverHeight - 8;
      } else {
        top = rect.bottom + 8;
      }

      popover.style.left = left + 'px';
      popover.style.top = top + 'px';
      popover.classList.add('is-visible');
      popover.setAttribute('aria-hidden', 'false');
      mentionEl.classList.add('is-active');
    }

    function hidePopover() {
      hideTimeout = setTimeout(() => {
        popover.classList.remove('is-visible');
        popover.setAttribute('aria-hidden', 'true');
        document.querySelectorAll('.ir-term-mention.is-active').forEach(el => el.classList.remove('is-active'));
      }, 200);
    }

    popover.addEventListener('mouseenter', () => {
      if (hideTimeout) clearTimeout(hideTimeout);
    });
    popover.addEventListener('mouseleave', hidePopover);

    const mentions = article.querySelectorAll('.ir-term-mention');
    mentions.forEach(el => {
      const idx = parseInt(el.getAttribute('data-term-index'), 10);
      el.addEventListener('mouseenter', () => showPopover(el, idx));
      el.addEventListener('mouseleave', hidePopover);
      el.addEventListener('focus', () => showPopover(el, idx));
      el.addEventListener('blur', hidePopover);
      el.addEventListener('click', (e) => {
        e.preventDefault();
        showPopover(el, idx);
      });
    });

    document.addEventListener('click', (e) => {
      if (!e.target.closest('.ir-term-mention') && !e.target.closest('#ir-floating-popover')) {
        popover.classList.remove('is-visible');
        popover.setAttribute('aria-hidden', 'true');
        document.querySelectorAll('.ir-term-mention.is-active').forEach(el => el.classList.remove('is-active'));
      }
    });

    if (digestSection && digestGrid) {
      const matchedList = Array.from(matchedTermsMap.values()).sort((a, b) => a.term.localeCompare(b.term));
      if (matchedList.length > 0) {
        digestGrid.innerHTML = '';
        matchedList.forEach(item => {
          const card = document.createElement('article');
          card.className = 'lesson-term-card';
          card.innerHTML = `
            <div class="lesson-term-card-top">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.25rem;">
                <h4 class="lesson-term-card-name">${item.term}</h4>
                <span class="lesson-term-card-category">${item.category}</span>
              </div>
              ${(item.plain_en || item.plain_id) ? `
                <div class="lesson-term-card-plain">
                  <span class="lesson-term-card-plain-title"><i class="fa fa-lightbulb-o"></i> In Simple Terms:</span>
                  <p class="lesson-term-card-plain-text">${item.plain_en || item.plain_id}</p>
                </div>
              ` : ''}
              <p class="lesson-term-card-academic"><strong>Definition:</strong> ${item.definition}</p>
            </div>
            <div class="lesson-term-card-footer">
              <span class="lesson-term-card-scholars">${item.scholars || ''}</span>
              <a href="${base}/glossary.html" class="lesson-term-card-link">Full Glossary <i class="fa fa-arrow-right"></i></a>
            </div>
          `;
          digestGrid.appendChild(card);
        });

        if (countBadge) countBadge.textContent = matchedList.length + ' Key Terms';
        digestSection.style.display = 'block';
      }
    }
  }

  // Self execute on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLMS);
  } else {
    initLMS();
  }
})();
