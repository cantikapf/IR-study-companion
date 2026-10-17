import assert from 'node:assert/strict';
import { OnboardingModal } from './OnboardingModal.js';

// Setup minimal DOM mocks for Node test environment
global.document = {
  head: {
    appendChild: () => {}
  },
  body: {
    appendChild: (el) => {
      global.document._lastAppended = el;
    }
  },
  getElementById: (id) => null,
  createElement: (tag) => {
    return {
      tagName: tag.toUpperCase(),
      classList: {
        _classes: new Set(),
        add(c) { this._classes.add(c); },
        remove(c) { this._classes.delete(c); },
        contains(c) { return this._classes.has(c); }
      },
      setAttribute: () => {},
      appendChild: () => {},
      querySelector: (sel) => ({
        onclick: null
      })
    };
  }
};

global.window = {
  addEventListener: () => {}
};

console.log('[OnboardingModal Self-Check] Initializing test...');

let started = false;
const modal = new OnboardingModal({
  labId: 'lab-01',
  role: 'Presidential National Security Advisor',
  objective: 'De-escalate the Cuban Missile Crisis while navigating bureaucratic resistance.',
  onStart: () => { started = true; }
});

assert.ok(modal.modalEl, 'modalEl must be created');
assert.equal(modal.isOpen, false, 'Modal should start closed');

modal.open();
assert.equal(modal.isOpen, true, 'Modal should open');
assert.ok(modal.modalEl.classList.contains('active'), 'active class should be added on open');

modal.start();
assert.equal(modal.isOpen, false, 'Modal should close on start');
assert.equal(started, true, 'onStart callback should be triggered');

console.log('[OnboardingModal Self-Check] ALL ASSERTIONS PASSED!');
