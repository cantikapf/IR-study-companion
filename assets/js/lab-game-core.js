/**
 * IR Study Companion — Shared Diplomatic Lab Game Core (M10 Game Layer)
 * Public API: window.LabGame
 * Pure ES6/vanilla JS, zero dependencies.
 */
(function(window) {
  'use strict';

  // --- RNG (mulberry32) ---
  function mulberry32(a) {
    var state = a >>> 0;
    return function() {
      var t = (state += 0x6D2B79F5);
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }

  function rng(seed) {
    if (typeof seed === 'number') {
      return mulberry32(seed);
    }
    return Math.random();
  }

  // --- Score module ---
  var _score = 0;
  var score = {
    add: function(n) {
      _score += (Number(n) || 0);
      return _score;
    },
    get: function() {
      return _score;
    },
    reset: function() {
      _score = 0;
      return _score;
    }
  };

  // --- Streak module ---
  var _streak = 0;
  var streak = {
    hit: function() {
      _streak++;
      return _streak;
    },
    break: function() {
      _streak = 0;
      return 0;
    },
    get: function() {
      return _streak;
    },
    mult: function() {
      if (_streak >= 5) return 2;
      if (_streak >= 3) return 1.5;
      return 1;
    }
  };

  // --- Stars evaluator ---
  function stars(val, par1, par2, par3) {
    var s = Number(val) || 0;
    if (s >= par3) return 3;
    if (s >= par2) return 2;
    if (s >= par1) return 1;
    return 0;
  }

  // --- Best score storage ---
  var best = {
    get: function(labId) {
      try {
        var raw = localStorage.getItem('labs_best_' + labId);
        if (raw === null) return 0;
        var parsed = parseInt(raw, 10);
        return isNaN(parsed) ? 0 : parsed;
      } catch (e) {
        return 0;
      }
    },
    submit: function(labId, scoreVal) {
      try {
        var s = parseInt(scoreVal, 10);
        if (isNaN(s)) return false;
        var existing = localStorage.getItem('labs_best_' + labId);
        var cur = existing !== null ? parseInt(existing, 10) : null;
        if (cur === null || isNaN(cur) || s > cur) {
          localStorage.setItem('labs_best_' + labId, String(s));
          return true;
        }
        return false;
      } catch (e) {
        return false;
      }
    }
  };

  // --- Completion flags ---
  var flags = {
    complete: function(labId) {
      try {
        localStorage.setItem('labs_completed_' + labId, 'true');
        return true;
      } catch (e) {
        return false;
      }
    },
    isComplete: function(labId) {
      try {
        return localStorage.getItem('labs_completed_' + labId) === 'true';
      } catch (e) {
        return false;
      }
    }
  };

  // --- SFX (WebAudio synth) ---
  var _actx = null;
  var _muted = false;
  try {
    _muted = localStorage.getItem('labs_muted_v1') === '1';
  } catch (e) {}

  function getAudioContext() {
    if (!_actx) {
      var AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {
        _actx = new AudioCtx();
      }
    }
    if (_actx && _actx.state === 'suspended') {
      _actx.resume().catch(function() {});
    }
    return _actx;
  }

  function beep(freq, dur, type, gainVal, when) {
    if (_muted) return;
    try {
      var ctx = getAudioContext();
      if (!ctx) return;
      var t = ctx.currentTime + (when || 0);
      var osc = ctx.createOscillator();
      var g = ctx.createGain();
      osc.type = type || 'sine';
      osc.frequency.setValueAtTime(freq, t);
      g.gain.setValueAtTime(gainVal || 0.05, t);
      g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
      osc.connect(g);
      g.connect(ctx.destination);
      osc.start(t);
      osc.stop(t + dur + 0.02);
    } catch (e) {}
  }

  var sfx = {
    click: function() {
      beep(560, 0.07, 'square', 0.03);
    },
    good: function() {
      beep(660, 0.09, 'sine', 0.05);
      beep(880, 0.12, 'sine', 0.05, 0.09);
    },
    bad: function() {
      beep(150, 0.22, 'sawtooth', 0.06);
    },
    reveal: function() {
      beep(440, 0.08, 'triangle', 0.05);
      beep(554, 0.08, 'triangle', 0.05, 0.07);
      beep(659, 0.14, 'triangle', 0.05, 0.14);
    },
    fanfare: function() {
      beep(523, 0.12, 'sine', 0.06);
      beep(659, 0.12, 'sine', 0.06, 0.12);
      beep(784, 0.22, 'sine', 0.06, 0.24);
    },
    muted: function() {
      return _muted;
    },
    toggleMute: function() {
      _muted = !_muted;
      try {
        localStorage.setItem('labs_muted_v1', _muted ? '1' : '0');
      } catch (e) {}
      return _muted;
    }
  };

  // --- Help Modal Module ---
  var _helpOpen = false;
  var _helpModalEl = null;

  function closeHelp() {
    if (_helpModalEl) {
      _helpModalEl.hidden = true;
      _helpModalEl.style.display = 'none';
    }
    _helpOpen = false;
  }

  function openHelp() {
    if (_helpModalEl) {
      _helpModalEl.hidden = false;
      _helpModalEl.style.display = 'flex';
      _helpOpen = true;
    }
  }

  // Key lock listener on window (capture phase to lock game keys while help is open)
  window.addEventListener('keydown', function(e) {
    if (_helpOpen) {
      if (e.key === 'Escape') {
        closeHelp();
        e.preventDefault();
        e.stopPropagation();
      } else {
        // Block C, D, space, enter from reaching game while modal is open
        var k = e.key ? e.key.toLowerCase() : '';
        if (k === 'c' || k === 'd' || k === ' ' || k === 'enter') {
          e.stopPropagation();
        }
      }
    }
  }, true);

  var help = {
    mount: function(opts) {
      opts = opts || {};
      if (_helpModalEl && _helpModalEl.parentNode) {
        _helpModalEl.parentNode.removeChild(_helpModalEl);
      }

      var modal = document.createElement('div');
      modal.className = 'lab-modal-back';
      modal.setAttribute('role', 'dialog');
      modal.setAttribute('aria-modal', 'true');
      modal.setAttribute('aria-label', 'Mission Help');
      modal.hidden = true;
      modal.style.display = 'none';

      var card = document.createElement('div');
      card.className = 'lab-modal-card';

      var header = '<div class="lab-modal-header">' +
        '<h4><i class="fa fa-question-circle" aria-hidden="true"></i> Classified Mission Help</h4>' +
        '<button type="button" class="lab-modal-close" aria-label="Close help">&times;</button>' +
        '</div>';

      var body = '<div class="lab-modal-body">';
      if (opts.objectiveHtml) {
        body += '<div class="lab-modal-section"><h5>🎯 Mission Objective</h5>' + opts.objectiveHtml + '</div>';
      }
      if (opts.howtoHtml) {
        body += '<div class="lab-modal-section"><h5>📖 How to Play</h5>' + opts.howtoHtml + '</div>';
      }
      if (opts.payoffHtml) {
        body += '<div class="lab-modal-section"><h5>⚖️ Payoff Matrix</h5>' + opts.payoffHtml + '</div>';
      }
      body += '</div>';

      var footer = '<div class="lab-modal-footer">' +
        '<button type="button" class="lab-btn lab-btn-primary lab-modal-dismiss-btn">' +
        '<i class="fa fa-check" aria-hidden="true"></i> Back to the Table</button>' +
        '</div>';

      card.innerHTML = header + body + footer;
      modal.appendChild(card);

      document.body.appendChild(modal);
      _helpModalEl = modal;

      modal.addEventListener('click', function(e) {
        if (e.target === modal) {
          closeHelp();
        }
      });

      var closeX = card.querySelector('.lab-modal-close');
      if (closeX) {
        closeX.addEventListener('click', closeHelp);
      }
      var dismissBtn = card.querySelector('.lab-modal-dismiss-btn');
      if (dismissBtn) {
        dismissBtn.addEventListener('click', closeHelp);
      }

      if (opts.triggerEl) {
        var trigger = typeof opts.triggerEl === 'string' ? document.querySelector(opts.triggerEl) : opts.triggerEl;
        if (trigger) {
          trigger.addEventListener('click', openHelp);
        }
      }

      return {
        open: openHelp,
        close: closeHelp,
        isOpen: function() { return _helpOpen; }
      };
    },
    open: openHelp,
    close: closeHelp,
    isOpen: function() {
      return _helpOpen;
    }
  };

  // --- Timer Module ---
  var _timerId = null;
  var _timerRemaining = 0;
  var _timerPaused = false;

  var timer = {
    start: function(ms, onTick, onExpire) {
      this.stop();
      var prefersReduced = false;
      try {
        prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      } catch (e) {}
      var untimed = document.querySelector('.lab-shell[data-untimed="true"]');
      if (prefersReduced || untimed) {
        if (typeof onTick === 'function') onTick(0, 0);
        return false;
      }
      _timerRemaining = ms;
      _timerPaused = false;
      var interval = 100;
      _timerId = setInterval(function() {
        if (_timerPaused) return;
        _timerRemaining -= interval;
        if (typeof onTick === 'function') onTick(_timerRemaining, ms);
        if (_timerRemaining <= 0) {
          clearInterval(_timerId);
          _timerId = null;
          if (typeof onExpire === 'function') onExpire();
        }
      }, interval);
      return true;
    },
    stop: function() {
      if (_timerId) {
        clearInterval(_timerId);
        _timerId = null;
      }
      _timerRemaining = 0;
      _timerPaused = false;
    },
    paused: function(val) {
      if (typeof val === 'boolean') {
        _timerPaused = val;
      }
      return _timerPaused;
    }
  };

  // Public object
  window.LabGame = {
    rng: rng,
    score: score,
    streak: streak,
    stars: stars,
    best: best,
    flags: flags,
    sfx: sfx,
    help: help,
    timer: timer
  };

})(typeof window !== 'undefined' ? window : this);
