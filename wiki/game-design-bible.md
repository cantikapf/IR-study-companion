# Diplomatic Labs — Game Design Bible (M10 Game Layer)

---
type: director-handoff
version: 1.0
director: GLM 5.3 Flash (via 9router)
builder: Gemini 3.8 (via 9router, separate Hermes session)
status: G1 AUTHORIZED — G2/G3 pending user ACC after G1 review
ground-truth-prototype: "scratch (EPHEMERAL): C:/Users/xiyeo/AppData/Local/hermes/cache/scratch/minigame_diplomacy_duel.html — user-ACC'd feel. If pruned, the spec sheets in §6 are authoritative; never block on the missing file."
---

## 0. Roles & Reading Order

- **Director (GLM 5.3)** owns the 5 picks (§1), all spec sheets (§5–6), and final audit of the built result.
- **Builder (Gemini 3.8)** executes ONE phase per session turn, exactly as specified, with full verification.
- **User (producer)** holds ACC at every phase gate.

Reading order for Builder: `HERMES.md` → `PROJECT.md` (Feature #14 / M10) → this bible → `assets/css/lab-shell.css` → `_includes/sim_game_theory.html` (Fase 1 pilot) → execute.

## 1. The Five Director Picks (LOCKED — do not redesign)

| # | Pick | Decision |
|---|---|---|
| 1 | **Engine** | Vanilla ES6 shared game core (`assets/js/lab-game-core.js`) + `lab-shell.css` board. **Zero new dependencies. No framework. No three.js in G1/G2** (WebGL map pilot remains a separate deferred decision for the user). |
| 2 | **Path** | G1 (core + Lab 02 retrofit → user ACC) → G2 (9 labs, unique game verb each) → G3 (homepage stars + full QA). One gate between every phase. |
| 3 | **Look** | Mission Console **light, theme-aware** (lab-shell tokens, auto dark via `body.dark-theme`). Gold reserved for score/stars/intel. Juice = motion (score pops, shake on betrayal, meter pulses), not reskin. Respect `prefers-reduced-motion`. |
| 4 | **Story archetype** | **"Classified Case File"** — every lab is a mission from an academic case file: briefing = *dossier*, mid-game hint = *SIGINT intercept*, debrief = *after-action report*, opponent/obstacle = *classified*. Tone: cool intelligence-brief, never cartoon. |
| 5 | **Angle** | **"Theory is the strategy guide."** The only way to win is to understand the theory: streaks = shadow of the future, SIGINT = information asymmetry, vetoes = institutional constraints. Zero reflex mechanics; every mechanic maps to a citable concept revealed in the debrief. |

## 2. Non-Negotiable Guardrails (violating any = failed review)

1. English-only UI copy (project mandate). Academic tone, no AI-isms.
2. Zero external dependencies; vanilla ES6 + CSS only. CSS stays prefix-scoped per lab (existing `sim-xx-*` namespaces).
3. All game logic client-side, localStorage only (`labs_completed_*`, `labs_best_*`, `labs_muted_v1`). No accounts, no network.
4. Canonical academic content (theory citations, chapter concepts) stays grounded — no invented facts. The debrief reveal must cite the same scholars as the chapter (Jervis, Axelrod, Putnam, Schelling, Allison, Deutsch, etc.).
5. Logical changes to sim mechanics are authorized **only where a spec sheet says "Authorized change"** (§5–6). Everything else keeps its current behavior.
6. Verification gates per phase (§8) must all pass before commit. Commit one phase per commit, explicit `git add` paths only — never commit unrelated untracked files.
7. Builder does not edit §1/§5/§6 decisions. If something is ambiguous or impossible, STOP and record the question at the top of `wiki/hot.md` entry instead of improvising.

## 3. Shared Game Core — `assets/js/lab-game-core.js` (public API)

Loaded once in `_includes/head.html` (after lab-shell.css). All labs consume it; no lab reimplements these.

```js
window.LabGame = {
  rng(seed?),            // mulberry32; deterministic when seeded
  score: { add(n), get(), reset() },
  streak: { hit(), break(), mult() },   // mult(): 1 → 1.5 (3 consecutive) → 2 (5 consecutive)
  stars(score, par1, par2, par3),       // returns 0–3
  best: { get(labId), submit(labId, score) /* returns true if new record */ },
  flags: { complete(labId), isComplete(labId) },  // labs_completed_<labId>
  sfx: { click(), good(), bad(), reveal(), fanfare(), muted(), toggleMute() },
                        // WebAudio synth (see prototype §4); mute persisted as labs_muted_v1
  help: { mount({ objectiveHtml, howtoHtml, payoffHtml }) },
                        // renders ❓ chip + modal (Esc/backdrop close, locks C/D-style keys while open)
  timer: { start(ms, onTick, onExpire), stop(), paused() } // optional; auto-disabled when
                        // prefers-reduced-motion or data-untimed="true" on the lab root
};
```

Implementation notes: pure functions kept pure (unit-testable); no DOM access outside `help`/`timer`; no globals other than `window.LabGame`. ~250–350 lines expected.

## 4. Ground-Truth Feel (from the ACC'd prototype)

The scratch prototype validated: **hidden-personality draw → per-round simultaneous reveal with suspense beat (≈500 ms) → floating score pops → shake on betrayal → SIGINT card at a mid-point → 3-star end screen with rank + mechanics reveal + best-score**. Preserve this *rhythm* (not the dark theme) in the retrofit. Copy deck for Lab 02 is in §5.

## 5. Phase G1 — Game Core + Lab 02 Retrofit (AUTHORIZED SCOPE OF THE NEXT BUILD TURN)

**Deliverables**
1. `assets/js/lab-game-core.js` per §3.
2. `_includes/head.html`: one `<script defer src=...lab-game-core.js>` line.
3. `_includes/sim_game_theory.html` retrofitted to the ACC'd prototype, re-skinned to lab-shell light theme:
   - Dossier briefing: 🎯 Game Objective (stars ★1+/★2 15+/★3 40+, streak rule, negative = exploited, beat Best) + 📖 How to Play (6 numbered steps) + ⚖️ payoff matrix table + ❓ Help chip with in-game modal (Esc/backdrop close, keys locked).
   - Opponent roulette: 5 personalities — Tit-for-Tat, Grim Trigger, The Predator (always D), The Wildcard (60/40), Pavlov (win-stay/lose-shift). Drawn secretly each session; roulette "SCRAMBLING…" reveal; "STRATEGY: CLASSIFIED" tag; debrief names it with citation (Axelrod 1984).
   - Scoring: payoffs unchanged (+5/+5, +10/−10, −2/−2); mutual-cooperation streak ×1.5 at 3, ×2 at 5 (opponent score always unmultiplied).
   - SIGINT intercept card drops after Round 4 (personality-specific hint copy, §9).
   - 8 rounds → end screen: stars animation, rank (Master Diplomat / Seasoned Negotiator / Survivor / Exploited), final score vs Best (localStorage `labs_best_game_theory`), stats row (% cooperated, exploits landed, times betrayed), after-action reveal (personality + "how to face it" + CC Pareto-optimal / DD Nash framing), replay button (new secret draw).
   - Completed flag `labs_completed_game_theory` on session end (existing key kept).
   - Keyboard C/D; trust bar; muted-toggle persisted.
4. Remove nothing from the chapter page around it (quiz, flashcards untouched).

**Acceptance criteria (all must hold)**
- [ ] pytest 369/369 from repo root (§8 command).
- [ ] Jekyll build clean; `_site/game-theory-ir.html` contains briefing + roulette + help modal markup.
- [ ] Playwright E2E (channel msedge, http-server on `_site`): ≥20 checks incl. briefing visible→Begin→8 rounds (all-coop run scores 40 with streaks → 3 stars), SIGINT card appears after R4, help modal opens/closes and locks keys, completed flag set, 0 console errors.
- [ ] Visual gate: full-page screenshots (briefing / mid-game / end) — no overlap, no clipped text, light theme correct, dark theme correct.
- [ ] `grep -i "indonesian-stopword"` over the lab markup = 0 hits.
- [ ] `wiki/hot.md` G1 entry + commit `feat(labs): G1 game core + Lab 02 mini-game retrofit`.
- [ ] **STOP. Present evidence to user. No G2 work.**

## 6. Phase G2 — Spec Sheets for the Other 9 Labs (build ONLY after G1 ACC)

Common to all: dossier briefing (objective/how-to/payoff-or-legend/help modal), one SIGINT intercept mid-run, after-action reveal citing chapter scholars, stars + Best per lab (`labs_best_<id>`), core API only, reduced-motion respected. Star pars given as (★1/★2/★3). "Authorized change" = the only permitted deviation from current sim logic.

**Lab 01 — Crisis Command: Thirteen Days** (`sim_crisis.html`, FPA/Allison)
- Verb: decision-under-pressure across 3 acts. Authorized change: expand 1-choice sim into 3 decision beats (airstrike/blockade/backchannel → second letter response/Trollope ploy → Turkey-missiles quid-pro-quo), each with an optional 12s DEFCON timer (untimed when reduced-motion).
- Scoring: Stability 100 → start; each act deducts per escalation and per timeout (−10). End states: Nuclear War (≤0), Compromise Deal (≥40), Humiliating Backdown (1–39 mid-path errors).
- Stars: 100/85/70 remaining. SIGINT: "U-2 photos: launchers not yet operational — you have one quiet week."
- Reveal: your three choices mapped onto Allison's Model I/II/III.

**Lab 04 — Spiral Watch** (`sim_security_dilemma.html`)
- Verb: restraint-streak management on the existing 5-round core. Authorized change: Beta draws a hidden type per session — *Cautious Reactive* (existing logic) or *Opportunistic* (mirrors Build; punishes Reduce with Build) — disclosed in reveal; consecutive non-Build rounds add a CBM momentum bonus (extra −5 Beta threat from round 3).
- Scoring: outcomes unchanged (75/35 thresholds) + streak bonus influences them. Stars: Security Community = ★3; Détente = ★1; Spiral = 0.
- SIGINT (after R2): "Decrypt: Beta's planning posture this season is [cautious/opportunistic]."
- Reveal: Jervis Spiral Model; why type-uncertainty *is* the dilemma.

**Lab 03 — Consensus Market** (`sim_wto.html`)
- Verb: budgeted coalition-building. Authorized change: 8 member blocs with hidden red lines; 10 Diplomatic Capital points spent on concessions (1–3 each) before the single vote; leftovers = bonus.
- Stars: pass + ≥4 capital left ★3; pass + 1–3 ★2; pass + 0 ★1; fail 0. SIGINT: "Leak: the Agriculture bloc is bluffing about market-access red lines."
- Reveal: single undertaking / package-deal logic; consensus as vetopoint.

**Lab 05 — Veto Gauntlet** (`sim_unsc_veto.html`)
- Verb: persuasion puzzle. Authorized change: P5 members as cards with 2 hidden demands each; 5 Amendment Tokens to attach pre-vote; any P5 veto = instant fail; 10 E10 cards vote on final text quality.
- Stars: 15/9/6 surviving votes. SIGINT: "Aide-mémoire: [member]'s public demand masks [true demand]."
- Reveal: P5 institutional constraint; quiet diplomacy vs public drafting.

**Lab 06 — Two-Table Pressure** (`sim_treaty_negotiation.html`)
- Verb: twin-track resource allocation. Authorized change: 6 turns; each turn allocate 2 Action Points across International table / Domestic briefing; win-set meter fills only when both tracks advance in balance (max 1-table skew).
- Stars: ratify + ZOPA ≥ 70 ★3; ratify ★2; fail ★0–1. SIGINT: "Overnight poll: domestic swing bloc wavers if agriculture carve-out appears."
- Reveal: Putnam win-set; Level I vs Level II.

**Lab 07 — Zone Runner** (`sim_unclos_zones.html`)
- Verb: combo quiz climb. Authorized change: 3 Incident tokens (wrong answer = lose one + explanation); consecutive correct ×1.5 combo on zone-difficulty points; zone ladder fills visually per correct claim.
- Stars: finish 10 zones + 3/2/1 tokens left = ★3/★2/★1; out of tokens = fail. SIGINT: one free "discard the hardest zone" pass.
- Reveal: annotated zone chart of your two weakest zones (UNCLOS 1982 articles cited from chapter).

**Lab 08 — Equilibrium Keeper** (`sim_balance_of_power.html`)
- Verb: shock-absorbing scale puzzle. Authorized change: keep configurator; add 4 July-1914 crisis cards drawn in sequence; after each, blocs gain weight; you may reallocate 2 alignment points; war triggers if |A−B| > threshold twice.
- Stars: survive 4 crises + margin ≤10 ★3; survive ★2; cascade ★0–1. SIGINT: "Embassy cable: [bloc] will realign after the next shock."
- Reveal: balance vs bandwagoning; July 1914 cascade.

**Lab 09 — Chair's Gambit** (`sim_scs_dispute.html`)
- Verb: dual-objective juggling (keep 3 rounds). Authorized change: 6 faction meters (claimants, non-claimants, China, dialogue partners); each choice shifts them; final score = Agreement Value + Consensus Survival; hidden China pressure rises with legalistic choices.
- Stars: COC adopted + all meters ≥30 ★3; adopted ★2; collapse ★0–1. SIGINT: "Chair's note: non-claimants will walk if legalism dominates the text."
- Reveal: ASEAN Way trade-offs (consensus vs substance), 2016 arbitral ruling context.

**Lab 10 — Second-Strike Ledger** (`sim_nuclear_deterrence.html`)
- Verb: budget stress-test. Authorized change: 4 fiscal years; each year allocate budget across ICBM/SLBM/bomber/defense; each year-end a scenario stress-tests second-strike survivability; Stability meter; fail = first-strike temptation event.
- Stars: stable 4/4 years + ≥2 legs survivable ★3; stable ★2; spiral ★0–1. SIGINT: "Satellite: adversary is hardening silos, not building launchers."
- Reveal: MAD, Schelling's commitment problem, survivability logic (chapter 120).

## 7. Phase G3 — Homepage + QA (after G2 ACC)

- Homepage catalog cards: category accent, duration chip, ⭐ per-lab (from `labs_best_*`/`labs_completed_*`), "Completed ✓" state; featured sandbox upgraded to G1 form. Mirror every change into `prototype/home.html` (same session).
- Full QA: 10 chapters E2E (0 console errors), English-only grep over `_site`, dark/light screenshots, pytest + build, `sw.js` cache bump v4→v5.
- Sync `PROJECT.md` (M10 → DONE pending user), `wiki/hot.md`, `lessons-learned.md`.

## 8. Verification Protocol (every phase)

```bash
# tests (repo root)
"C:/Users/xiyeo/AppData/Local/Programs/Python/Python313/Scripts/pytest" -o pythonpath=scripts --ignore=_site tests/ -q   # expect 369 passed
# build (WindowsApps ruby shims are broken — use the direct path)
/d/Ruby32-x64/bin/ruby.exe "D:/Ruby32-x64/bin/bundle" exec jekyll build
# E2E: playwright chromium channel 'msedge' + `npx http-server _site -p <port>`
# built-output checks: grep _site/<chapter>.html for new briefing markup & old-copy residue
```

Visual gate = full-page screenshots at briefing / mid-game / end, light + dark, inspected (no overlap/clipping). Report all results in the turn's response; then sync `wiki/hot.md` (top entry, numbered, verification last) and commit with explicit paths.

## 9. Copy Deck — G1 strings (paste as-is; adapt pattern per lab in G2)

- Kicker: `CASE FILE · GAME THEORY` · Title: `Diplomacy Duel: The Prisoner's Dilemma`
- Objective panel: "Survive 8 rounds against a secret opponent and finish with the highest score you can. ★1+ Survivor · ★★ 15+ Negotiator · ★★★ 40+ Master Diplomat. The golden path: chain mutual-cooperation streaks (×1.5 at 3 in a row, ×2 at 5) without getting betrayed. Finish negative and you were exploited. Beat your saved Best."
- How to Play (6 steps): Begin → choose C/D (buttons or keys) → simultaneous reveal → study the rival's pattern → Round 4 SIGINT → reveal + replay with a new rival.
- Payoff note: "Mutual cooperation pays best over time — but every round, defection tempts you with +10. That tension *is* the Prisoner's Dilemma."
- Intel header: `INTEL · ROUND 5` — hints: TFT "Their last two moves exactly mirrored ours. Pattern lock likely — this is a mirror player." · Grim "After our one betrayal they went cold and never returned to the table. No recovery observed." · Predator "Every intercepted transmission mentions weapons. They have never once cooperated. Stop hoping." · Wildcard "Their moves defy every model we can fit. Analysts suspect coin-flip diplomacy." · Pavlov "They keep whichever stance won them the previous round. Habitual, not principled."
- Ranks: `Master Diplomat` (3★) · `Seasoned Negotiator` (2★) · `Survivor` (1★) · `Exploited` (0★)
- Reveal closer: "Continue to the **Knowledge Check** below to test the concept."

## 10. Handoff Protocol

Builder turn = read (HERMES.md → bible) → execute one authorized phase → verify (§8) → sync wiki → commit → **stop with evidence**. Producer relays ACC to Director session; Director audits diff + reruns gates before the next phase is authorized. Any deviation from bible = failed review, reverted at Builder's cost.
