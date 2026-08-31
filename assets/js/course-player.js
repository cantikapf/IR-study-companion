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

  // --- Drawer Instant Search ---
  function initSearchFilter() {
    const searchInput = document.getElementById('drawer-search-input');
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.toLowerCase().trim();
      const groups = document.querySelectorAll('.drawer-module-group');

      groups.forEach(group => {
        const lessons = group.querySelectorAll('.drawer-lesson-item');
        let hasMatchInGroup = false;

        lessons.forEach(lesson => {
          const text = lesson.textContent.toLowerCase();
          if (query === '' || text.includes(query)) {
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

  // Self execute on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLMS);
  } else {
    initLMS();
  }
})();
