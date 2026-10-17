import { CONSTANTS } from './Constants.js';
import { eventBus, Events } from './EventBus.js';

/**
 * GameState — Centralized single source of truth for Lab 02.
 */
export class GameState {
  constructor() {
    this.reset();
  }

  reset() {
    this.round = 1;
    this.playerScore = 0;
    this.rivalScore = 0;
    this.streak = 0;
    this.maxStreak = 0;
    this.history = [];
    this.playerMove = null;
    this.rivalMove = null;
    this.phase = 'BOOT'; // BOOT, BRIEFING, CHOOSING, DECRYPTING, REVEALED, SIGINT, GAMEOVER
    this.doctrine = null;
  }

  getMultiplier() {
    if (this.streak >= CONSTANTS.STREAK.THRESHOLD_HIGH) {
      return CONSTANTS.STREAK.MULT_HIGH;
    }
    if (this.streak >= CONSTANTS.STREAK.THRESHOLD_MID) {
      return CONSTANTS.STREAK.MULT_MID;
    }
    return 1.0;
  }

  applyTurnResult(playerMove, rivalMove) {
    this.playerMove = playerMove;
    this.rivalMove = rivalMove;

    let pDelta = 0;
    let rDelta = 0;
    const mult = this.getMultiplier();
    const key = `${playerMove}${rivalMove}`;
    const base = CONSTANTS.PAYOFF[key];

    if (key === 'CC') {
      pDelta = Math.round(base[0] * mult);
      rDelta = base[1];
      this.streak++;
      if (this.streak > this.maxStreak) this.maxStreak = this.streak;
    } else if (key === 'DC') {
      pDelta = base[0];
      rDelta = base[1];
      this.streak = 0;
    } else if (key === 'CD') {
      pDelta = base[0];
      rDelta = base[1];
      this.streak = 0;
    } else {
      // DD
      pDelta = base[0];
      rDelta = base[1];
      this.streak = 0;
    }

    this.playerScore += pDelta;
    this.rivalScore += rDelta;

    const roundData = {
      round: this.round,
      player: playerMove,
      rival: rivalMove,
      pDelta,
      rDelta,
      mult,
      cumulativePlayer: this.playerScore,
      cumulativeRival: this.rivalScore
    };

    this.history.push(roundData);

    eventBus.emit(Events.SCORE_UPDATE, {
      playerScore: this.playerScore,
      rivalScore: this.rivalScore,
      pDelta,
      rDelta,
      streak: this.streak,
      mult
    });

    return roundData;
  }

  getStars() {
    if (this.playerScore >= CONSTANTS.STARS.THREE) return 3;
    if (this.playerScore >= CONSTANTS.STARS.TWO) return 2;
    if (this.playerScore >= CONSTANTS.STARS.ONE) return 1;
    return 0;
  }

  getRank() {
    const stars = this.getStars();
    if (stars === 3) return 'MASTER DIPLOMAT';
    if (stars === 2) return 'SEASONED NEGOTIATOR';
    if (stars === 1) return 'SURVIVOR ENVOY';
    return 'EXPLOITED REGIME';
  }
}

export const gameState = new GameState();
