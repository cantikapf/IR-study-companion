# SH-09 · Malacca Strait — motion-graphics plan

New build. Previous `sh-08` assets are abandoned (not deleted, just not referenced).

Route: `/motion-graphics` → category `maps` (vector lane) + `stat` + `kinetic-type`.
Baseline form: `instagram.com/p/Deb39i_PLRE` (@90secondslab, eFishery). Evidence frames: `.agents/motion-prompt/refs/90sl_{0,1,2,3,30,62}s.jpg`.

---

## 1. What is copied from the baseline, and what is not

| Baseline element | Adopt? | How it becomes ours |
|---|---|---|
| Hook ladder: one tilted text block per second | **Yes** | `1.5 NAUTICAL MILES` → `ONE GATE` → `NO SECOND ROUTE` |
| Alternating block fill (dark → gold → light) | **Yes** | exact same rhythm, warm paper palette |
| Ultra-condensed ultra-bold caps, hard offset shadow (8/10px, zero blur) | **Yes** | Archivo Black, `box-shadow:8px 10px 0` |
| Physicalised quantity instead of a counter | **Yes** | 1.5 NM drawn as a real gauge between two coastlines; 20.5 m drawn as a hull in a water column |
| Paper cutout / die-cut white border | **Yes**, as a *device* | every landmass gets a 6px cream die-cut edge + soft shadow → reads as paper cut on a desk |
| Warm palette (`#F4F1EA` paper, `#0B0D11` charcoal, `#FFC822` gold, `#C81E1E` red) | **Yes** | replaces the dark-cyan intel HUD entirely |
| 85 s runtime, Indonesian VO, karaoke subtitles | **No** | motion-graphics is unnarrated; 18 s; English-only per HERMES.md |
| Consumer-shock framing (`JAGO NGARANG?`) | **No** | IR framing: structural geography, not accusation |

**Deliberate conflict to flag:** the baseline is a *narrated* reel. `/motion-graphics` is defined as unnarrated, motion-is-the-message, ~10–30 s. This plan follows the skill (no VO). If you want the baseline's voice-over back, the route changes to `/explainer-video`, not this one.

---

## 2. Assets — what will actually be used

`asset_needs: []` — the `maps` **vector lane** needs no sourced imagery. Every element is code.

| # | Asset | Type | Source | Status |
|---|---|---|---|---|
| 1 | Country geometry | data (GeoJSON, 177 features) | `learning-videos/shorts-experiments/sh-05-cuban-crisis-map-animation/data/countries.js` → copy into `data/` | exists |
| 2 | `Archivo Black` | font | repo copy `sh-01-pulau-run-hf/fonts/ArchivoBlack-Regular.ttf` | exists |
| 3 | `Space Mono` reg+bold | font | same folder | exists |
| 4 | Paper grain | procedural | SVG `feTurbulence baseFrequency=.9 numOctaves=3` + `feComposite` — no image file | to build |
| 5 | Die-cut edge + shadow | procedural | SVG `stroke:#F4F1EA; stroke-width:6` + `filter:drop-shadow(0 18px 22px rgba(0,0,0,.18))` | to build |
| 6 | Gold route "tape" | procedural | stroked path, `stroke-linecap:square`, `stroke-dasharray` draw-on | to build |
| 7 | Water column / hull section | procedural | SVG rect + polygon, no 3D engine | to build |

No archival photos, no basemap tiles, no generated images. Attribution obligations: none (all code + fonts already in repo; Archivo Black OFL, Space Mono OFL).

---

## 3. Facts allowed on screen (fact gate)

| Claim | Value | Status |
|---|---|---|
| Phillips Channel minimum width | 1.5 NM / 2.8 km | VERIFIED 2026-10-19 |
| Malaccamax max draft | 20.5 m (333 m × 60 m, ~300k DWT) | VERIFIED |
| Malacca seabed depth | ~25 m | VERIFIED |
| Sunda controlling depth | ~20 m, >100k DWT excluded | VERIFIED |
| Deep-draft detour | Lombok → Dewakang Sill → Makassar | VERIFIED (route) |
| Vessel counts, oil share, day/money cost of detour | — | **NOT USED.** No primary source; banned from screen. |

Rule from `BRIEF_SH08_v2.md` still applies: a claim that fails the gate is deleted, not softened.

---

## 4. Scene sheet — 18.0 s, 1080×1920, 30 fps

| # | Time | Shot | On-screen | Motion (named) |
|---|---|---|---|---|
| S1 | 0.00–1.00 | Cream desk, paper map of the strait already there. Zero text. | — | `hold_breath` only. Subject visible before any word. |
| S2 | 1.00–2.00 | First sticker drops | `1.5 NAUTICAL MILES` (charcoal block, cream type, −2°) | `slam` |
| S3 | 2.00–3.00 | Second sticker | `ONE GATE` (gold block, charcoal type, −2°) | `slam` |
| S4 | 3.00–4.00 | Third sticker | `NO SECOND ROUTE` (cream block, charcoal type, −1.2°) | `slam` |
| S5 | 4.00–9.00 | Gauge shot. Camera pushes into the Phillips Channel; a gold caliper spans the gap and a **physical scale bar** (10 dashed ticks) makes 1.5 NM countable. | `1.5 NM · 2.8 KM` pinned at the caliper | `viewBox` push + `bar_wipe` on the caliper |
| S6 | 9.00–14.00 | Water-column shot. The map tilts out; a paper cross-section drops in: sea surface, 20.5 m hull, ~25 m seabed. Hull descends and stops with **4.5 m of clearance** under the keel. | `DRAFT 20.5 M` inside hull, `SEABED ~25 M` on the floor, `CLEARANCE 4.5 M` in red | `slide_bottom` + `count_up` on 20.5 |
| S7 | 14.00–18.00 | Pull back. Two gold/red tape lines draw the detours — Sunda (amber, light draft) and Lombok–Makassar (red, loaded tankers). Endcard. | `LIGHT DRAFT → SUNDA` / `LOADED TANKERS → LOMBOK` then `YOU CANNOT WIDEN A STRAIT` + `@IRinANutshell` | `stroke-dashoffset` draw-on, then `fade_out` to endcard |

`HYPOTHETICAL SCENARIO` sticker stays on from 14.0 to 17.2 — the detour is a simulation, not a forecast.

Every scene boundary is a **paper-slide wipe** (0.25 s): an oversized cream rect with a charcoal leading edge slides over the stage. Not a cross-dissolve — the baseline's transition device.

---

## 5. Dispatch prompt (paste-ready for the Builder subagent)

> Build a single 1080×1920, 30 fps, 18.0 s HyperFrames composition at `videos/sh-09-malacca-mg/compositions/index.html`.
>
> **Look:** paper-cut atlas on a cream desk. Ground `#F4F1EA` with an SVG `feTurbulence` grain at 4% opacity. Sea is the cream ground; every landmass is a charcoal `#171A1F` fill with a 6 px `#F4F1EA` die-cut stroke and `drop-shadow(0 18px 22px rgba(0,0,0,.18))` — it must read as a physical cut-out, not a flat SVG. Route is a gold `#FFC822` tape strip. Red `#C81E1E` is reserved for exactly three things: the chokepoint dot, the clearance gap, and the Lombok detour.
>
> **Type:** Archivo Black for every headline, all-caps, letterspacing −1 px, hard shadow `8px 10px 0 rgba(0,0,0,.85)` — zero blur. Space Mono for coordinates and small labels only. No thin type anywhere; it dies on phone recompression.
>
> **Hook:** three tilted stickers at 1.0 / 2.0 / 3.0 s — `1.5 NAUTICAL MILES` (charcoal block), `ONE GATE` (gold block), `NO SECOND ROUTE` (cream block). Alternate the fill; rotate −2°, −2°, −1.2°. Slam each in with `power4.out`, 0.42 s. No text at all for the first second.
>
> **Beats:** 4–9 s gauge, 9–14 s water column, 14–18 s detours + endcard, per the scene sheet in `PLAN.md`.
>
> **Motion rules (non-negotiable):** everything is a pure function of the paused GSAP timeline on `window.__timelines`; no `Date.now()`, no `setInterval`, no `Math.random()` at draw time; counters use a proxy tween with `onUpdate`; SVG zoom animates `viewBox` only; centred elements animate opacity only. Every number on screen comes from the fact gate — do not invent vessel counts, oil shares, or day/money costs.
>
> **Text safety:** nothing inside the top 200 px or bottom 330 px. Every label offset from every other label and clamped inside the safe area. The `HYPOTHETICAL SCENARIO` sticker is visible for the entire detour beat.

---

## 6. Gates before render

1. `npx hyperframes check .` clean.
2. Proof snapshots at 0.5 / 1.5 / 3.5 / 6.5 / 11.5 / 16.0 / 17.8 s — inspect the contact sheet.
3. A text-safe-area assertion: no `getBoundingClientRect()` top < 200 or bottom > 1590 for any caption node at any of those times.
4. You (Cantikaputri) approve the preview still before any MP4 is rendered.
