/**
 * IR Study Companion - Online Course Prototype Controller
 * Synthesizes:
 * - Instant Switcher (Quiet, Editorial, Utilitarian)
 * - Concentric & Interruptible UI Micro-Interactions (better-ui)
 * - Course Progress State & Completion Engine
 * - Interactive Quiz & Active Recall Flashcard
 */

document.addEventListener('DOMContentLoaded', () => {
  // State
  const state = {
    axis: localStorage.getItem('proto_axis') || 'quiet',
    completedLessons: JSON.parse(localStorage.getItem('proto_completed_lessons') || '["ch-01"]'),
    activeLesson: 'ch-02',
    drawerOpen: true
  };

  // DOM Elements
  const htmlRoot = document.documentElement;
  const switcherBtns = document.querySelectorAll('.harness-switcher-btn');
  const drawer = document.getElementById('curriculum-drawer');
  const toggleDrawerBtn = document.getElementById('btn-toggle-drawer');
  const progressFill = document.getElementById('progress-fill');
  const progressText = document.getElementById('progress-text');
  const flashcard = document.getElementById('active-flashcard');
  const quizCards = document.querySelectorAll('.quiz-option-card');
  const quizSubmitBtn = document.getElementById('quiz-submit-btn');
  const quizFeedback = document.getElementById('quiz-feedback');
  const btnCompleteContinue = document.getElementById('btn-complete-continue');
  const btnResetProgress = document.getElementById('btn-reset-progress');

  // 1. Initialize Axis (Quiet, Editorial, Utilitarian)
  function setAxis(newAxis) {
    state.axis = newAxis;
    htmlRoot.setAttribute('data-axis', newAxis);
    localStorage.setItem('proto_axis', newAxis);

    switcherBtns.forEach(btn => {
      if (btn.dataset.axis === newAxis) {
        btn.classList.add('active');
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.classList.remove('active');
        btn.setAttribute('aria-pressed', 'false');
      }
    });
  }

  switcherBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      setAxis(btn.dataset.axis);
    });
  });

  // Apply saved or default axis
  setAxis(state.axis);

  // 2. Drawer Toggle (Focus / Zen Mode)
  if (toggleDrawerBtn && drawer) {
    toggleDrawerBtn.addEventListener('click', () => {
      state.drawerOpen = !state.drawerOpen;
      drawer.classList.toggle('collapsed', !state.drawerOpen);
      toggleDrawerBtn.setAttribute('aria-expanded', state.drawerOpen);
      toggleDrawerBtn.innerHTML = state.drawerOpen
        ? `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg> Hide Syllabus`
        : `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg> Show Syllabus`;
    });
  }

  // 3. Update Progress UI
  function updateProgress() {
    const totalLessons = 5;
    const completedCount = state.completedLessons.length;
    const percentage = Math.round((completedCount / totalLessons) * 100);

    if (progressFill) {
      progressFill.style.width = `${percentage}%`;
    }
    if (progressText) {
      progressText.textContent = `${percentage}%`;
    }

    // Update lesson items in drawer
    document.querySelectorAll('.lesson-item').forEach(item => {
      const id = item.dataset.lessonId;
      if (state.completedLessons.includes(id)) {
        item.classList.add('completed');
        const icon = item.querySelector('.lesson-status-icon');
        if (icon) icon.textContent = '✓';
      } else {
        item.classList.remove('completed');
        const icon = item.querySelector('.lesson-status-icon');
        if (icon) icon.textContent = '';
      }
    });

    localStorage.setItem('proto_completed_lessons', JSON.stringify(state.completedLessons));
  }

  // 4. Interactive Quiz Logic
  let selectedOption = null;
  quizCards.forEach(card => {
    card.addEventListener('click', () => {
      // Clear previous selection
      quizCards.forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      selectedOption = card.dataset.value;
      card.querySelector('input[type="radio"]').checked = true;
      
      // Hide previous feedback if any
      if (quizFeedback) {
        quizFeedback.classList.remove('show', 'correct', 'incorrect');
      }
    });
  });

  if (quizSubmitBtn) {
    quizSubmitBtn.addEventListener('click', () => {
      if (!selectedOption) {
        alert('Please select an option first.');
        return;
      }

      // Option B is the correct answer
      const isCorrect = selectedOption === 'b';
      
      quizCards.forEach(card => {
        card.classList.remove('correct', 'incorrect');
        if (card.dataset.value === 'b') {
          card.classList.add('correct');
        } else if (card.dataset.value === selectedOption && !isCorrect) {
          card.classList.add('incorrect');
        }
      });

      if (quizFeedback) {
        quizFeedback.classList.remove('correct', 'incorrect');
        quizFeedback.classList.add('show', isCorrect ? 'correct' : 'incorrect');
        quizFeedback.innerHTML = isCorrect
          ? `<strong>Correct!</strong> Defensive Realism (Kenneth Waltz) argues that the international system incentivizes states to maintain their existing security and the balance of power, rather than pursuing reckless hegemony.`
          : `<strong>Incorrect.</strong> Option B is correct. Unlike offensive realism (Mearsheimer) which views states as power maximizers seeking regional hegemony, defensive realism (Waltz) views states as security seekers striving for status quo balance.`;
      }
    });
  }

  // 5. Active Recall Flashcard (Flip Interaction)
  if (flashcard) {
    flashcard.addEventListener('click', () => {
      flashcard.classList.toggle('flipped');
    });

    flashcard.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        flashcard.classList.toggle('flipped');
      }
    });
  }

  // 6. "Complete & Continue" Action
  if (btnCompleteContinue) {
    btnCompleteContinue.addEventListener('click', () => {
      if (!state.completedLessons.includes('ch-02')) {
        state.completedLessons.push('ch-02');
      }
      updateProgress();

      btnCompleteContinue.innerHTML = `✓ Completed! Loading Next Lesson...`;
      btnCompleteContinue.style.background = 'var(--semantic-success-ink)';

      setTimeout(() => {
        alert("🎉 Bravo! Lesson 2 completed. In the production course player, this automatically advances to Chapter 3: 'Structural Realism & International Anarchy'.");
        btnCompleteContinue.innerHTML = `Complete & Continue to Lesson 3 ➔`;
        btnCompleteContinue.style.background = 'var(--brand-accent)';
      }, 500);
    });
  }

  // 7. Reset Progress
  if (btnResetProgress) {
    btnResetProgress.addEventListener('click', () => {
      state.completedLessons = ['ch-01'];
      updateProgress();
      if (quizFeedback) quizFeedback.classList.remove('show', 'correct', 'incorrect');
      quizCards.forEach(c => c.classList.remove('selected', 'correct', 'incorrect'));
      selectedOption = null;
      if (flashcard) flashcard.classList.remove('flipped');
    });
  }

  // Initial Progress render
  updateProgress();
});
