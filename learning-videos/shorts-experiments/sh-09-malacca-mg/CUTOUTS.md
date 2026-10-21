# Cutout system — @90secondslab `Deb39i_PLRE`

Extracted from full-res frames (`refs/hires/z*.png`) plus 2-second strips at
`$TMPDIR/ig90/ev/row0..7.png`. Every number below is read off the frames, not inferred from style words.

---

## 1. There are THREE layer classes, not one

The reel does not apply "paper cutout" to everything. It switches class per object type, and that switch is what keeps the frame readable. Getting this wrong is why paper-collage attempts look like a scrapbook instead of an explainer.

| Class | Applies to | Edge treatment | Shadow | Count in reel |
|---|---|---|---|---|
| **A · Photo sticker** | people, pond photo, portrait, feeder machine, cardboard box, gavel, cash stacks, pens, clock, envelope | Uniform **white contour stroke, 6–20 px** (scales with subject: 6–10 px on a person, 14–20 px on a machine or a prop) | Soft, directional, ~135° (light upper-left), blur 25–40 px, opacity 22–40%, offset +Y 2–15 px | ~14 objects |
| **B · 3D render** | the open hardcover book (every scene), the 400-cell capsule array at 52 s | **No white border.** Real geometry edge, visible page-block thickness | Physically rendered | 2 |
| **C · Flat vector** | waffle grids, bar charts, cash beaker, UI slider card, verdict card, stamps, ribbons, all type banners | **No white border.** Either a 2–3 px black stroke or a flat fill | Contact only (blur 12 px, +Y 6 px, 30%) or none | ~12 |

Rule that falls out of it: **anything that exists as a photograph gets a white sticker edge. Anything that exists only as a diagram is flat vector.** The book is the stage; the flat graphics lie on the book page; the sticker cutouts stand on it.

---

## 2. Class A — the sticker, measured

- Stroke sits **outside** the silhouette (path offset), join style rounded. White is `#FFFFFF`, fully opaque — it never blends into the background.
- Shadow is **not** an SVG drop-shadow of the stroke. It is a separate soft blur behind the object: `blur 25–40 px`, `rgba(0,0,0,.22–.40)`, offset `+Y 2–15 px`, always trailing to the **lower-right** (single consistent light from upper-left across the whole reel).
- Objects are **tilted** 3–8° in either direction, never axis-aligned. The tilt is what says "placed by hand".
- Contact shadow: a tighter, darker line directly under the bottom cut edge (`rgba(0,0,0,.5)`, blur 4 px, +Y 2 px) — this is what stops the object floating.

### Objects that actually get the sticker treatment

| Object | Scene | Stroke |
|---|---|---|
| Founder, standing, hands in pockets | 0–3 s | 6–10 px |
| Catfish (×3), floating diagonal | 2–3 s | 6–10 px |
| eFishery sign placard on a post | 1–7 s | thick, rounded corners |
| Pond photo (polaroid) + portrait (polaroid, black ID label) | 4–7 s | uniform polaroid frame |
| Automatic feeder machine | 6–7 s, 70–77 s | 14–18 px |
| Group of investors in suits | 10–11 s | one contour around the **collective** silhouette |
| Cash stacks, banded Rp100k | 24–28 s | 8 px |
| Floating banknotes (×2), tilted 5–10° | 28 s | **0 px** — deliberately unbordered, so they read as airborne |
| Cardboard supplier box `PEMASOK` | 54–59 s | 14–18 px |
| Judge gavel hitting the verdict card | 66–68 s | 6–10 px |
| Pen, alarm clock, kraft envelope | 12–16 s | 6–10 px |

Note the banknotes: **the one object with no border is the only one in the air.** Border = grounded. Absence of border = in flight. That is the whole grammar.

---

## 3. Class B — the book

- Isometric-ish 3D, ochre/mustard cover `#CCA01D`, page block `#E5E7EB`, visible spine crease and multi-page cut edge.
- It is the **stage**: every scene happens on its open page, and the page acts as the light-catching surface for the sticker shadows.
- At 52 s the book holds a 25-column × 32-row array of tiny translucent capsules in perspective — front rows are wireframe ghosts, rows behind are solid. It is a *perspective* array, not a flat grid. 400,000 is represented by ~800 visible objects, so the literal count is never claimable.
- **The book changes colour role per act**: ochre = the company's own records; grey slate = the real ledger (`ASLI`). Same object, different cover, no label needed after the first pairing.

---

## 4. Class C — flat vector diagrams

| Diagram | Construction | Motion |
|---|---|---|
| Cash beaker `KAS STARTUP` | Tall glass tube, 1–2 px black outline, filled from the bottom with Rp100k note bricks | Fill level rises — volume is shown as **liquid**, not as a number |
| Bar chart `ANGKA PENJUALAN` | 4 vertical bars, grey vs yellow | Bars grow |
| Two-bar comparison | Left yellow bar = 12 segments, right dark bar = 2.5 segments on the **same scale** | Both drawn on one shared baseline; upper 9.5 segments then get diagonal hatching + a dotted line at the real height |
| Waffle grid | **20 × 20 = 400 squares**, each square = 1,000 units | All 400 filled yellow → a grey band sweeps a row → grid drops to outline and only **6.3 squares** fill black. No second chart, no axis |
| UI slider `TAKARAN PAKAN` | White rounded card, 3 px black stroke, grey track, yellow rounded-square thumb | Thumb slides right; label flips `PAS` → `KEBANYAKAN` |
| Verdict card | White paper card, 2 px black stroke, red rectangular stamp, yellow highlight bar | Card slides in, stamp lands with a 4° rotation, highlight bar wipes under the charge text |
| Ribbon tags | Charcoal `#1A1A1A` angled ribbon, yellow `#FFC800` caps | Wraps over a book edge |

The waffle grid is the strongest idea in the reel: **one grid carries both the claim and the refutation**, by changing what is filled. It costs one element and answers the whole objection.

---

## 5. Type system

| Role | Spec |
|---|---|
| Hook / headline | Ultra-condensed ultra-bold caps, ≈62 px at 1080 wide, `letter-spacing −1 px`, hard shadow `8px 10px 0 rgba(0,0,0,.85)` — **zero blur** |
| Headline blocks | Solid fill + **−2° rotation**, stacked downward one per second, alternating dark → gold → light |
| Subtitle | Rounded geometric sans ~52 px, white `#FFFFFF`, dark soft shadow, one word under a yellow marker block |
| Small labels / units | Mono, tracked out, 13–15 px, muted |
| Stamp | Impact-style, double concentric rounded frame (outer ~10 px, 5 px white gap, inner 3 px), rotated −4° |

The hook ladder's alternating fill is doing real work: dark → gold → light makes three stacked lines read as **three separate thoughts** instead of one paragraph.

---

## 6. Backgrounds — three, each with a job

| Background | Palette | Used for |
|---|---|---|
| Wood desk, top-down | oak `#C8A882`, warm wall `#E5DFD5` | physical scenes: founder, books, props |
| Dot-grid paper | cream `#F5F5ED`, grid `#D6D6CE` | diagram scenes: beaker, waffle, verdict, feeder gauge |
| Split wall (grey / yellow) | `#E5DFD5` + gold block | only the opening hook |

Switching background = switching register: **physical evidence vs. abstract diagram.** The reel never mixes them inside one shot.

---

## 7. Transition devices (all physical, zero cross-dissolves)

1. **Paper slide wipe** — a cream sheet with a dark leading edge crosses the frame, 0.2–0.4 s.
2. **Object drop-in** — the next prop falls into place from above with `power4.out`, lands, settles.
3. **State morph on the same object** — grid 400 → 6.3; book cover ochre → grey; tag `PAS` → `KEBANYAKAN`.
4. **Hard cut on a beat**, no transition at all, when the next scene is a new register.

---

## 8. Corrections to my earlier read (evidence-driven)

Two things I stated before checking full-res frames were wrong:

1. **The 52 s "waffle grid" is not flat.** It is a perspective array of ~800 translucent capsules on a 3D book — not 400 flat squares. The **flat** 400-square waffle appears later, at 54–59 s, with the supplier box. Two different graphics, same concept, escalating.
2. **The 80–84 s ending is not a cash waterfall.** At 83 s the object is a white fibrous sphere wrapped in a yellow face mask with black ear loops, tagged `DIPOLES` / `Rp12 T`, with the small grey `ASLI` ledger at the lower left. I described a "cash waterfall" from a 4-second grid frame; the full-res frame does not support it. **My earlier description was wrong and is retracted.**

Also: my 4-second grid timestamps drifted up to ~4 s against the file (scene cuts detected at 3.97 s, 16.40 s, 38.20 s). The sequence ordering in `RESEARCH.md` is right; individual timestamps there should be treated as ±4 s until re-measured.

---

## 9. What SH-09 adopts

| Class A (sticker) | Class B (stage) | Class C (flat) |
|---|---|---|
| Nothing — we have no photographs, and generating fake archival imagery is banned | The **paper-cut atlas** is our stage: charcoal landmasses on cream, with a die-cut cream edge and contact shadow | Caliper, scale ticks, water column, route tapes, sticker type, `HYPOTHETICAL SCENARIO` flag |
| — | Landmasses carry the *grounded* role the book has in the reel: everything else lies on top of them | All numbers stay flat vector — no fake-photo instruments |

Adopted grammar, precisely:

- **Die-cut edge instead of white sticker:** landmass fill `#171A1F`, stroke `#F4F1EA` at 6 px, `drop-shadow(0 18px 22px rgba(0,0,0,.18))`. Same visual logic as the reel's sticker, applied to geography.
- **One consistent light, upper-left.** Every shadow in the composition offsets lower-right. No exceptions.
- **Border = grounded, no border = in flight.** The caliper and route tapes are flat (they are measurement, not objects). The two detour route labels are stickered (they sit on the map).
- **One grid carries claim and refutation:** our water column carries 20.5 m hull, ~25 m seabed, and 4.5 m clearance in a single object — same economy as the 400 → 6.3 squares trick.
- **Hook ladder:** three stickered type blocks, 1 per second, −2°, dark → gold → light, hard 8/10 px shadow, zero blur.
