# Storyboard & Shot List: SH-01 "The Island Traded for Manhattan"

**Channel:** @IRinANutshell  
**Series:** Geopolitical Paradoxes  
**Slug:** `sh-01-pulau-run`  
**Canvas Resolution:** 1080 x 1920 px (9:16 Vertical)  
**Frame Rate:** 30 fps  
**Target Duration:** ~46.5 seconds provisional across 6 narrative beats (121 space-delimited words / 124 spoken words at standard 160 WPM educational cadence; exact timings provisional pending Phase 2 ElevenLabs neural speech synthesis)  
**Language:** Academic English exclusively across all layers.

---

## 1. Composition Architecture & Mobile Safe Zone Geometry

The visual presentation adheres to the 4-layer Archival Micro-Documentary standard defined in `viral-history-shorts`:

```
┌─────────────────────────────────────────────────────────────┐ 0px
│ [TOP MARGIN BUFFER: 170px]                                  │
│ ┌─────────────────────────────────────────────────────────┐ │ 170px
│ │ [KICKER] KICKER BADGE                    @IRinANutshell │ │
│ │ HEADLINE (42px Bold Uppercase, drop shadow)             │ │ 340px
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │ 360px
│ │ ARCHIVAL PLATE BOX (Gilded Border, 2px)                 │ │
│ │ • Frame-deterministic Ken Burns (1.04x -> 1.15x)        │ │
│ │ • Authentic period cartography / botanical engravings   │ │
│ │                                                         │ │
│ │ ─────────────────────────────────────────────────────── │ │ 1116px
│ │ [TOPIC] FOCUS TOPIC                DOC REF // VOC-1667  │ │ 1164px
│ └─────────────────────────────────────────────────────────┘ │ 1180px
│                                                             │
│ ┌───────────────────────────┬───────────────────────────┐   │ 1205px
│ │ DATA CHIP 1               │ DATA CHIP 2               │   │
│ │ Label / Metric Value      │ Label / Metric Value      │   │ 1310px
│ └───────────────────────────┴───────────────────────────┘   │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │ 1330px
│ │ FLOATING SUBTITLE CAPSULE (Dark Slate Container)        │ │
│ │ 27px font, 1.38 line-height, bold gold highlights       │ │ 1490px
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ [CLEAR MOBILE SAFE BUFFER: 430px HEIGHT]                    │
│ Completely free of critical content to clear:               │
│ • YouTube Shorts account handle, subscribe button, sound    │
│ • TikTok engagement footer and navigation controls          │
│ • Right margin (>135px) clears vertical engagement buttons  │
└─────────────────────────────────────────────────────────────┘ 1920px
```

### Mobile Safe Zone Specifications
1. **Vertical Bounds for Subtitles:** Fixed container at `top: 1330px`, `height: 140px – 160px` (span `y: 1330px – 1490px`).
2. **Bottom Clearance:** Canvas baseline is `1920px`. With subtitles terminating at `y <= 1490px`, the remaining bottom buffer is `430px` ($> 410\text{ px}$ requirement), guaranteeing zero overlap with native platform controls.
3. **Lateral Clearance:** Left padding is `65px`; right padding is `135px`. The expanded right margin ensures text and chips never collide with the vertical Shorts interaction column (Like, Dislike, Comment, Share).
4. **Motion Determinism:** Camera moves strictly use mathematical interpolation per frame (`progressInBeat / beatDuration`) rather than CSS transitions, ensuring 100% reproducible headless renders.

---

## 2. Beat-by-Beat Shot List

```
================================================================================
BEAT 1 · THE HOOK
================================================================================
```
- **Beat ID:** `b1_hook` (Beat 1 of 6)
- **Time Range:** `0.0s – 8.5s` (*Provisional pending Phase 2 speech measurement*)
- **Estimated Duration:** 8.5 seconds (Frames `0 – 255` at 30 fps)
- **Narration Text (English):**  
  > *"Thirty-nine men held a three-kilometre island against an empire for 1,540 days — for a spice the world could get nowhere else."*
- **Hook Speed Analysis:**  
  The opening line delivers an arresting asymmetry of numbers and stakes (*"Thirty-nine men held a three-kilometre island against an empire for 1,540 days"*) in the first 2 seconds, opening an urgent historical question without prematurely revealing Manhattan, the island's identity, or the treaty payoff.
- **On-Screen Typography:**  
  - **Kicker:** `THE SPICE ISLAND SIEGE`
  - **Headline:** `39 MEN · 1,540 DAYS`
  - **Channel Watermark:** `@IRinANutshell`
- **Archival Visual Asset:**  
  `moluccas_map_17th.jpg` (Nicolas Sanson & Antoine Peyrounin mid-17th-century cartographic engraving of the Moluccas, Celebes, and Banda Sea).
- **Camera Treatment (Ken Burns):**  
  - Scale: `1.04x` $\rightarrow$ `1.15x`
  - Pan: Wide directional drift across the maritime theatre coordinates (`panY: 0px` $\rightarrow$ `+20px`, `panX: 0px` $\rightarrow$ `-25px`).
  - Transition: Smooth spring entrance damping 14, mass 0.6.
- **Contextual Data Chips (Layer 2):**  
  - **Chip 1:** `ENGLISH DEFENDERS` $\rightarrow$ `39 MEN ON RUN`
  - **Chip 2:** `RESISTANCE DURATION` $\rightarrow$ `1,540 CONSECUTIVE DAYS`
- **Archival Docket Badge:**  
  `🏛️ THE SPICE SIEGE  |  DOC REF // VOC-1616`
- **Subtitle Capsule & Safe Zone:**  
  - Position: `y: 1330px – 1490px`, left: `65px`, right: `135px`.
  - Content: "Thirty-nine men held a <span style=\"color:#F6E05E\"><u>three-kilometre island</u></span> against an empire for <span style=\"color:#F6E05E\"><u>1,540 days</u></span> — for a spice the world could get <span style=\"color:#F6E05E\"><u>nowhere else</u></span>."
  - Clearance: Bottom buffer is $430\text{ px}$, well above native mobile UI thresholds.

```
================================================================================
BEAT 2 · THE SPECK IN THE BANDA SEA
================================================================================
```
- **Beat ID:** `b2_the_island` (Beat 2 of 6)
- **Time Range:** `8.5s – 15.5s` (*Provisional pending Phase 2 speech measurement*)
- **Estimated Duration:** 7.0 seconds (Frames `255 – 465` at 30 fps)
- **Narration Text (English):**  
  > *"That island was Run, three kilometres long in the Banda archipelago — the world's only source of nutmeg and mace."*
- **On-Screen Typography:**  
  - **Kicker:** `BANDA SEA · MALUKU`
  - **Headline:** `PULAU RUN: 3-KM OUTPOST`
  - **Channel Watermark:** `@IRinANutshell`
- **Archival Visual Asset:**  
  `moluccas_map_17th.jpg` (Nicolas Sanson & Antoine Peyrounin 17th-century cartographic engraving of the Moluccas, Celebes, and Banda Sea).
- **Camera Treatment (Ken Burns):**  
  - Scale: `1.10x` $\rightarrow$ `1.22x`
  - Pan: Macro push-in focusing directly into the Banda archipelago coordinates (`panY: +15px` $\rightarrow$ `-20px`, `panX: -10px` $\rightarrow$ `+15px`).
- **Contextual Data Chips (Layer 2):**  
  - **Chip 1:** `ISLAND DIMENSIONS` $\rightarrow$ `3 KM LONG · 1 KM WIDE`
  - **Chip 2:** `GLOBAL SUPPLY` $\rightarrow$ `WORLD'S ONLY SOURCE (NUTMEG & MACE)`
- **Archival Docket Badge:**  
  `🏛️ BANDA ARCHIPELAGO & RUN  |  DOC REF // VOC-1616`
- **Subtitle Capsule & Safe Zone:**  
  - Position: `y: 1330px – 1490px`.
  - Content: "That island was <span style=\"color:#F6E05E\"><u>Run</u></span>, three kilometres long in the Banda archipelago — the world's only source of <span style=\"color:#F6E05E\"><u>nutmeg and mace</u></span>."
  - Clearance: Bottom buffer $430\text{ px}$ clear.

```
================================================================================
BEAT 3 · THE SIEGE & COMMODITY VALUE
================================================================================
```
- **Beat ID:** `b3_the_siege` (Beat 3 of 6)
- **Time Range:** `15.5s – 23.5s` (*Provisional pending Phase 2 speech measurement*)
- **Estimated Duration:** 8.0 seconds (Frames `465 – 705` at 30 fps)
- **Narration Text (English):**  
  > *"In sixteen sixteen, English captain Nathaniel Courthope arrived to break the Dutch monopoly, holding out until his death in sixteen twenty."*
- **On-Screen Typography:**  
  - **Kicker:** `1616–1620 RESISTANCE`
  - **Headline:** `COURTHOPE'S STAND`
  - **Channel Watermark:** `@IRinANutshell`
- **Archival Visual Asset:**  
  `nutmeg_vintage_1599.jpg` (Rijksmuseum RP-P-OB-75.396, 1599 engraving showing peeled nutmeg seeds, mace lattice, and cross-section).
- **Camera Treatment (Ken Burns):**  
  - Scale: `1.04x` $\rightarrow$ `1.15x`
  - Pan: Concentrated push towards the central dissected nut and husk (`panY: 0px` $\rightarrow$ `-30px`, `panX: 0px` $\rightarrow$ `+15px`).
- **Contextual Data Chips (Layer 2):**  
  - **Chip 1:** `ENGLISH COMMANDER` $\rightarrow$ `CAPT. NATHANIEL COURTHOPE`
  - **Chip 2:** `MISSION OBJECTIVE` $\rightarrow$ `BREAK DUTCH VOC MONOPOLY`
- **Archival Docket Badge:**  
  `🏛️ COURTHOPE EXPEDITION 1616–1620  |  DOC REF // EIC-1616`
- **Subtitle Capsule & Safe Zone:**  
  - Position: `y: 1330px – 1490px`.
  - Content: "In sixteen sixteen, English captain <span style=\"color:#F6E05E\"><u>Nathaniel Courthope</u></span> arrived to break the Dutch monopoly, holding out until his death in <span style=\"color:#F6E05E\"><u>sixteen twenty</u></span>."
  - Clearance: Bottom buffer $430\text{ px}$ clear.

```
================================================================================
BEAT 4 · WAR IN THE ATLANTIC & UTI POSSIDETIS
================================================================================
```
- **Beat ID:** `b4_the_treaty` (Beat 4 of 6)
- **Time Range:** `23.5s – 32.0s` (*Provisional pending Phase 2 speech measurement*)
- **Estimated Duration:** 8.5 seconds (Frames `705 – 960` at 30 fps)
- **Narration Text (English):**  
  > *"After England seized Manhattan, the sixteen sixty-seven Treaty of Breda ended their war under uti possidetis: each side kept what it already held."*
- **On-Screen Typography:**  
  - **Kicker:** `1667 TREATY OF BREDA`
  - **Headline:** `THE ATLANTIC SETTLEMENT`
  - **Channel Watermark:** `@IRinANutshell`
- **Archival Visual Asset:**  
  `castello_plan_manhattan_1660.jpg` (John Wolcott Adams 1660 Castello Plan redraft showing early New Amsterdam / Manhattan fortifications).
- **Camera Treatment (Ken Burns):**  
  - Scale: `1.04x` $\rightarrow$ `1.15x`
  - Pan: Slow westward drift along the East River docks towards Fort Amsterdam (`panY: 0px` $\rightarrow$ `+20px`, `panX: 0px` $\rightarrow$ `-25px`).
- **Contextual Data Chips (Layer 2):**  
  - **Chip 1:** `LEGAL DOCTRINE` $\rightarrow$ `UTI POSSIDETIS (STATUS QUO)`
  - **Chip 2:** `TERRITORY IN DISPUTE` $\rightarrow$ `MANHATTAN (NEW NETHERLAND)`
- **Archival Docket Badge:**  
  `🏛️ TREATY OF BREDA 1667  |  DOC REF // VOC-1667`
- **Subtitle Capsule & Safe Zone:**  
  - Position: `y: 1330px – 1490px`.
  - Content: "After England seized <span style=\"color:#F6E05E\"><u>Manhattan</u></span>, the sixteen sixty-seven <span style=\"color:#F6E05E\"><u>Treaty of Breda</u></span> ended their war under <span style=\"color:#F6E05E\"><u>uti possidetis</u></span>: each side kept what it already held."
  - Clearance: Bottom buffer $430\text{ px}$ clear.

```
================================================================================
BEAT 5 · THE MONOPOLY CALCULATION
================================================================================
```
- **Beat ID:** `b5_the_deal` (Beat 5 of 6)
- **Time Range:** `32.0s – 38.5s` (*Provisional pending Phase 2 speech measurement*)
- **Estimated Duration:** 6.5 seconds (Frames `960 – 1155` at 30 fps)
- **Narration Text (English):**  
  > *"England kept Manhattan; the Dutch kept Run, which completed their grip on the world's nutmeg trade."*
- **On-Screen Typography:**  
  - **Kicker:** `1667 GLOBAL SETTLEMENT`
  - **Headline:** `THE MONOPOLY LOCK`
  - **Channel Watermark:** `@IRinANutshell`
- **Archival Visual Asset:**  
  `treaty_of_breda_1667.jpg` (Rijksmuseum RP-P-OB-82.067, grand baroque engraving commemorating the swearing of peace at Breda Castle).
- **Camera Treatment (Ken Burns):**  
  - Scale: `1.04x` $\rightarrow$ `1.15x`
  - Pan: Slow dramatic push inward into the central negotiating delegation table (`panY: 0px` $\rightarrow$ `-25px`, `panX: 0px` $\rightarrow$ `+20px`).
- **Contextual Data Chips (Layer 2):**  
  - **Chip 1:** `ENGLISH RETAINED` $\rightarrow$ `MANHATTAN (NEW NETHERLAND)`
  - **Chip 2:** `DUTCH RETAINED` $\rightarrow$ `PULAU RUN (NUTMEG MONOPOLY)`
- **Archival Docket Badge:**  
  `🏛️ BREDA RATIFICATION  |  DOC REF // VOC-1667`
- **Subtitle Capsule & Safe Zone:**  
  - Position: `y: 1330px – 1490px`.
  - Content: "England kept <span style=\"color:#F6E05E\"><u>Manhattan</u></span>; the Dutch kept <span style=\"color:#F6E05E\"><u>Run</u></span>, which completed their grip on the world's <span style=\"color:#F6E05E\"><u>nutmeg trade</u></span>."
  - Clearance: Bottom buffer $430\text{ px}$ clear.

```
================================================================================
BEAT 6 · THE GEOPOLITICAL PARADOX
================================================================================
```
- **Beat ID:** `b6_the_paradox` (Beat 6 of 6)
- **Time Range:** `38.5s – 46.5s` (*Provisional pending Phase 2 speech measurement*)
- **Estimated Duration:** 8.0 seconds (Frames `1155 – 1395` at 30 fps)
- **Narration Text (English):**  
  > *"Today, Manhattan is a global financial capital. And Run? A quiet island of about fifteen hundred people, where nutmeg still grows."*
- **On-Screen Typography:**  
  - **Kicker:** `THE GEOPOLITICAL IRONY`
  - **Headline:** `MANHATTAN VS RUN`
  - **Channel Watermark:** `@IRinANutshell`
- **Visual Asset (Modern Photograph):**  
  `nutmeg_fruit_fresh.jpg` (Modern macro photograph by Jeevan Jose, Kerala, India, CC BY-SA 4.0, showing ripe fruit revealing crimson mace aril).
- **Camera Treatment (Ken Burns):**  
  - Scale: `1.04x` $\rightarrow$ `1.15x`
  - Pan: Slow diagonal pan across the split husk and seed (`panY: 0px` $\rightarrow$ `+20px`, `panX: 0px` $\rightarrow$ `-15px`).
- **Contextual Data Chips (Layer 2):**  
  - **Chip 1:** `MANHATTAN TODAY` $\rightarrow$ `GLOBAL FINANCIAL CAPITAL`
  - **Chip 2:** `RUN TODAY` $\rightarrow$ `POPULATION ~1,500 · NUTMEG`
- **Archival Docket Badge:**  
  `🏛️ MODERN CONTRAST & IR LEGACY  |  DOC REF // VOC-1667`
- **Subtitle Capsule & Safe Zone:**  
  - Position: `y: 1330px – 1490px`.
  - Content: "Today, Manhattan is a <span style=\"color:#F6E05E\"><u>global financial capital</u></span>. And Run? A quiet island of about fifteen hundred people, where <span style=\"color:#F6E05E\"><u>nutmeg still grows</u></span>."
  - Clearance: Bottom buffer $430\text{ px}$ clear.

---

## 3. Summary of Provisional Timing Matrix

| Beat | ID | Asset Filename | Voiceover Text Words | Measured Duration | Measured Range (s) | Measured Frames (30 fps) |
|---|---|---|---|---|---|---|
| 1 | `b1_hook` | `moluccas_map_17th.jpg` | 22 | 9.20s | 0.00s – 9.20s | 0 – 276 |
| 2 | `b2_the_island` | `moluccas_map_17th.jpg` | 20 | 7.11s | 9.49s – 16.60s | 285 – 498 |
| 3 | `b3_the_siege` | `nutmeg_vintage_1599.jpg` | 21 | 8.08s | 16.90s – 24.98s | 507 – 749 |
| 4 | `b4_the_treaty` | `castello_plan_manhattan_1660.jpg` | 23 | 9.66s | 25.28s – 34.94s | 758 – 1048 |
| 5 | `b5_the_deal` | `treaty_of_breda_1667.jpg` | 16 | 5.99s | 35.24s – 41.23s | 1057 – 1237 |
| 6 | `b6_the_paradox` | `nutmeg_fruit_fresh.jpg` | 21 | 8.82s | 41.53s – 50.35s | 1246 – 1511 |
| **Total** | — | — | **123 words** | **50.72s** | **0.00s – 50.72s** | **0 – 1522 frames** |

> **Phase 2 update — measured, not estimated.** These timings come from the ElevenLabs `with-timestamps` response for the rendered narration (`audio/manifest.json`), with a 0.30 s silence inserted between beats. Each beat's `words` array carries per-word start/end times for karaoke subtitles. The earlier ~46.5 s provisional estimate was a projection; the real synthesis runs 50.72 s.

### Pacing Assumptions & Word Count Audit
- **Speech Rate Assumption:** Standard educational voiceover pacing of 160 words per minute (~2.67 words/second, ~0.375s per word).
- **Word Counts:** 121 space-delimited words / 124 spoken words (accounting for compound numerals "Thirty-nine", "three-kilometre", "fifteen forty", and "sixteen sixty-seven").
- **Duration Alignment:** At 160 WPM, 124 spoken words yield ~46.5 seconds (at 155 WPM: 48.0s; at 165 WPM: 45.1s), squarely satisfying the updated ~44–50 second window.
- *Caveat: All frame boundaries and timestamps are provisional pending Phase 2 neural audio synthesis using ElevenLabs ('George - Captivating Storyteller') and exact word-level time alignment in `manifest.json`.*
