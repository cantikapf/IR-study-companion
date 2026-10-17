/**
 * Constants — Zero magic numbers. Centralized balance, styling, and timing.
 */
export const CONSTANTS = {
  CANVAS: {
    WIDTH: 1024,
    HEIGHT: 600,
    PIXEL_SCALE: 4
  },

  ROUNDS: {
    TOTAL: 8,
    SIGINT_ROUND: 4
  },

  PAYOFF: {
    CC: [5, 5],     // Mutual Cooperation
    DC: [10, -10],  // Temptation to Exploit
    CD: [-10, 10],  // Sucker's Payoff
    DD: [-2, -2]    // Mutual Defection (Nash)
  },

  STREAK: {
    THRESHOLD_MID: 3,
    MULT_MID: 1.5,
    THRESHOLD_HIGH: 5,
    MULT_HIGH: 2.0
  },

  STARS: {
    THREE: 40,
    TWO: 15,
    ONE: 1
  },

  TIMING: {
    ENVELOPE_REVEAL_MS: 700,
    SCRAMBLE_DURATION_MS: 800,
    TURN_DIGEST_MS: 1600,
    SCREEN_FLASH_MS: 250,
    SCREEN_SHAKE_MS: 300
  },

  COLORS: {
    BG_VOID: 0x040711,
    BG_PANEL: 0x080d1a,
    ACCENT_CYAN: 0x06b6d4,
    ACCENT_EMERALD: 0x10b981,
    ACCENT_ROSE: 0xf43f5e,
    ACCENT_AMBER: 0xf59e0b,
    ACCENT_PURPLE: 0xc084fc,
    TEXT_MAIN: '#f8fafc',
    TEXT_MUTED: '#94a3b8',
    TEXT_DIM: '#64748b'
  },

  STORAGE_KEYS: {
    BEST_SCORE: 'labs_best_game_theory',
    COMPLETED: 'labs_completed_game_theory',
    MUTED: 'labs_muted_v1'
  },

  SPECTACLE: {
    COMBO: 'spectacle:combo',
    HIT_FREEZE: 'spectacle:hit_freeze',
    SHAKE: 'spectacle:shake',
    THEME_FLASH: 'spectacle:theme_flash',
    EXPRESSION_UPDATE: 'spectacle:expression_update'
  }
};

export const SPECTACLE_COMBO = 'spectacle:combo';
export const SPECTACLE_HIT_FREEZE = 'spectacle:hit_freeze';
export const SPECTACLE_SHAKE = 'spectacle:shake';
export const SPECTACLE_THEME_FLASH = 'spectacle:theme_flash';
export const SPECTACLE_EXPRESSION_UPDATE = 'spectacle:expression_update';

