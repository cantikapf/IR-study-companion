/**
 * Diplomatic Doctrines (AI FSM) for Lab 02.
 */
export const DIPLOMATIC_DOCTRINES = [
  {
    id: 'tft',
    name: 'Tit-for-Tat',
    archetype: 'Reciprocal Retaliator',
    sigint: "DECRYPT: 'Our doctrine is strictly reactive. We initiate with an open hand, mirror any aggressive provocation once, and reconcile immediately upon goodwill.'",
    theory: "Robert Axelrod's tournament champion (1984). Transparent, unforgiving of betrayal, yet instantly forgiving when cooperation is re-established.",
    makeDecision: (history) => history.length === 0 ? 'C' : history[history.length - 1].player
  },
  {
    id: 'grim',
    name: 'Grim Trigger',
    archetype: 'Deterrence Maximizer',
    sigint: "DECRYPT: 'Zero compromise. We remain peaceful until the very first hostile provocation. The instant trust is broken, negotiations are terminated permanently.'",
    theory: "Cold War strategic deterrence posture. Cooperates perpetually until a single betrayal occurs, triggering permanent, unyielding retaliation.",
    makeDecision: (history) => history.some(h => h.player === 'D') ? 'D' : 'C'
  },
  {
    id: 'predator',
    name: 'The Predator',
    archetype: 'Hawk Opportunist',
    sigint: "DECRYPT: 'All treaties are tactical delays. Power is zero-sum; weakness invites annexation. Deploy offensive posture across every round.'",
    theory: "Offensive Realism archetype. Assumes all actors will inevitably exploit; defects relentlessly regardless of counter-moves.",
    makeDecision: () => 'D'
  },
  {
    id: 'pavlov',
    name: 'Pavlov (Win-Stay / Lose-Shift)',
    archetype: 'Behaviorist Pragmatist',
    sigint: "DECRYPT: 'Assess the prior payoff outcome. If the yield was advantageous (both cooperated or we successfully exploited), maintain stance. Otherwise, shift.'",
    theory: "Nowak & Sigmund's evolutionary strategy. Capitalizes on cooperative partners and corrects quickly when counter-exploited.",
    makeDecision: (history) => {
      if (!history || history.length === 0) return 'C';
      const last = history[history.length - 1];
      const own = last.rival ?? 'C';
      const opp = last.player ?? 'C';
      // Win-Stay / Lose-Shift:
      // Reward (CC or DC: own receives 5 or 10) -> repeat own last move
      // Loss (CD or DD: own receives -10 or -2) -> flip own last move
      const isReward = opp === 'C';
      return isReward ? own : (own === 'C' ? 'D' : 'C');
    }
  },
  {
    id: 'wildcard',
    name: 'The Wildcard',
    archetype: 'Volatile Brinkmanship',
    sigint: "DECRYPT: 'Satellite surveillance detects chaotic domestic factional infighting. National signals are erratic and unpredictable (60% Coop / 40% Defect).'",
    theory: "Models internal domestic regime instability and erratic bureaucratic politics under Graham Allison's Model III.",
    makeDecision: () => Math.random() < 0.6 ? 'C' : 'D'
  }
];

export function getRandomDoctrine() {
  const idx = Math.floor(Math.random() * DIPLOMATIC_DOCTRINES.length);
  return DIPLOMATIC_DOCTRINES[idx];
}
