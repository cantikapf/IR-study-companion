# Baseline: motion-prompt mapping for IR Shorts

Repo baseline adopted 2026-10-19. Source library: `github.com/showheyohtaki/motion-prompt` (MIT).
Local copies in this folder: `catalog-en.tsv`, `SKILL-motion-prompt.md`, `porting.md`.

Rule: every motion in a Short is named by its library ID before it is built. If a move is not in the library, it is described in the same format (what moves, duration, easing, amount) and marked `[not in library]`.

## SH-08 Malacca Chokepoint — v2 motion plan

| Beat | Time | Move (ID) | What it does here |
|---|---|---|---|
| 1 Funnel | 0.0–2.2 | `#028` Zoom in | Camera group scale 1.0 → 1.08, no parallax (map is flat). |
| 1 Funnel | 1.0–2.2 | `#004` Line draw | Corridor outline draws on from northwest to southeast. |
| 1 Funnel | 1.6 / 1.9 | `#002` Stagger | MALAYSIA then SUMATRA pins, 0.3 s apart. |
| 1 Choke | 3.2–5.6 | `#027` Dolly in | Camera pushes toward the choke; position and scale both change (parallax on the map). |
| 1 Choke | 4.9–5.6 | `#005` Mask reveal | Caliper overlay rises into view behind a clipped edge. |
| 2 Section | 6.9–11.3 | `#017` Mask transition | Bathymetric card expands from a small rect to full card. |
| 2 Section | 7.6–8.75 | `#037` Slow motion | VLCC hull descends through the water column at 0.45× apparent speed. |
| 2 Section | 8.9–9.4 | `#010` Overshoot | Draft caliper lands, 8% past then settles. |
| 3 Volume | 12.4–16.0 | `#007` Count-up | 0 → 94,200, cubic ease-out, tabular numerals. |
| 3 Volume | 13.2–15.6 | `#004` Line draw | Oil share bar fills left to right to 60%. |
| 4 Silicon | 20.4 / 21.3 | `#002` Stagger | Two connector arrows, 0.9 s apart, matching the spoken order. |
| 5 Detour | 27.0–28.6 | `#004` Line draw | Sunda route draws from the choke southwest. |
| 5 Detour | 28.0–29.9 | `#004` Line draw | Lombok route draws from the choke southeast. |
| 5 Detour | 29.2–30.4 | `#024` Impact shake | Badge lands with a 0.4 s settle. |
| 6 Payoff | 35.0–38.0 | `#031` Crane up | Camera pulls back and up to the full theatre. |
| 6 Payoff | 36.4��37.4 | `#005` Mask reveal | Endcard headline rises line by line. |
| 6 Payoff | 36.9–37.5 | `#004` Line draw | Accent rule draws under the kicker. |

Easing family: `power2` / `power3` only. `back.out` allowed for the two landing beats (#010, #024). No bounce, no elastic elsewhere.

## Determinism requirements

- No `Math.random()` at draw time. All particle seeds come from `mulberry32(<constant>)`.
- No wall-clock reads. All motion is a pure function of the timeline `t`; stills seek with `timeline.seek(t)`.
- QA stills must be re-renderable to the identical pixel.
