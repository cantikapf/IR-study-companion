/**
 * EventBus — Decoupled event-driven communication for Decision Labs.
 * Domain:action pattern.
 */
class EventBus {
  constructor() {
    this.listeners = new Map();
  }

  on(event, callback) {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, new Set());
    }
    this.listeners.get(event).add(callback);
    return () => this.off(event, callback);
  }

  once(event, callback) {
    const unsub = this.on(event, (...args) => {
      unsub();
      callback(...args);
    });
    return unsub;
  }

  off(event, callback) {
    const set = this.listeners.get(event);
    if (set) {
      set.delete(callback);
      if (set.size === 0) this.listeners.delete(event);
    }
  }

  emit(event, data = {}) {
    const set = this.listeners.get(event);
    if (set) {
      set.forEach(cb => {
        try {
          cb(data);
        } catch (err) {
          console.error(`[EventBus] Error in handler for "${event}":`, err);
        }
      });
    }
  }

  clear() {
    this.listeners.clear();
  }
}

export const eventBus = new EventBus();

export const Events = {
  // Game Lifecycle
  GAME_BOOT: 'game:boot',
  GAME_START: 'game:start',
  GAME_PAUSE: 'game:pause',
  GAME_RESUME: 'game:resume',
  GAME_OVER: 'game:over',
  GAME_RESTART: 'game:restart',

  // Player & Turn Actions
  PLAYER_MOVE: 'player:move',
  RIVAL_REVEAL: 'rival:reveal',
  ROUND_RESOLVE: 'round:resolve',
  ROUND_NEXT: 'round:next',

  // Telemetry & Score
  SCORE_UPDATE: 'score:update',
  STREAK_CHANGE: 'streak:change',
  STREAK_MILESTONE: 'streak:milestone',

  // Intel & Narrative
  SIGINT_TRIGGER: 'sigint:trigger',
  SIGINT_DISMISS: 'sigint:dismiss',
  BRIEFING_OPEN: 'briefing:open',
  BRIEFING_CLOSE: 'briefing:close',
  DEBRIEF_OPEN: 'debrief:open',

  // Audio & Juice
  AUDIO_PLAY: 'audio:play',
  AUDIO_TOGGLE_MUTE: 'audio:toggle_mute',
  SCREEN_SHAKE: 'screen:shake',
  SCREEN_FLASH: 'screen:flash',
  PARTICLE_BURST: 'particle:burst',
  TEXT_POP: 'text:pop',

  // Spectacle & Juice Events (additive SSOT §1)
  SPECTACLE_COMBO: 'spectacle:combo',
  SPECTACLE_HIT_FREEZE: 'spectacle:hit_freeze',
  SPECTACLE_SHAKE: 'spectacle:shake',
  SPECTACLE_THEME_FLASH: 'spectacle:theme_flash',
  SPECTACLE_EXPRESSION_UPDATE: 'spectacle:expression_update'
};

export const SPECTACLE_COMBO = Events.SPECTACLE_COMBO;
export const SPECTACLE_HIT_FREEZE = Events.SPECTACLE_HIT_FREEZE;
export const SPECTACLE_SHAKE = Events.SPECTACLE_SHAKE;
export const SPECTACLE_THEME_FLASH = Events.SPECTACLE_THEME_FLASH;
export const SPECTACLE_EXPRESSION_UPDATE = Events.SPECTACLE_EXPRESSION_UPDATE;

