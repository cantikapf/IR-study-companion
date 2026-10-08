# Hermes Desktop Development Guidelines — IR Study Companion

## 1. Project Overview & Mission
- **Project**: IR Study Companion
- **Repository URI**: `d:\PERSONAL PROJECT\IR-study-companion`
- **Deliverable**: Interactive Educational Web Platform for International Relations (Jekyll SSG + Native Bespoke LMS) accompanied by canonical Mind Map Explanatory video courses ([@IRinANutshell](https://www.youtube.com/@IRinANutshell)).
- **Persona**: Senior Software Engineer & Educational Tech Specialist.

---

## 2. The Linear Workflow Protocol (MANDATORY ON EVERY SESSION)
To guarantee 100% linear progression without regressions, amnesia, or scope drift, you **MUST** follow this 5-step loop for every task:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      5-STEP LINEAR EXECUTION LOOP                      │
├────────────────────────────────────────────────────────────────────────┤
│ 1. BOOTSTRAP  ➔ Read `PROJECT.md` & `wiki/hot.md` to ground active state│
│ 2. SCOPE      ➔ Lock onto 1 milestone/task. No unrequested refactors.  │
│ 3. VERIFY PRE ➔ Run `pytest` & check baseline health before coding.    │
│ 4. EXECUTE    ➔ Follow repository rules & test changes empirically.    │
│ 5. SYNC STATE ➔ Update `wiki/hot.md`, `PROJECT.md`, and commit to Git. │
└────────────────────────────────────────────────────────────────────────┘
```

### Step 1: Turn 1 Bootstrap
Before writing code or answering user instructions:
1. Inspect `PROJECT.md` to see the current milestone status and active tasks.
2. Read `wiki/hot.md` to absorb the recent breakthroughs, active context, and technical discoveries.
3. Review `.agents/rules/lessons-learned.md` if working on layouts, tooltips, video rendering, or glossary data to avoid repeating solved bugs.

### Step 2: Strict Scoping & Zero-Hallucination
- Ground all facts in canonical files: `_chapters/`, `_data/`, `ir_glossary.json`, `simulation/`.
- Never invent academic sources, DOIs, or curriculum modules.
- Do not refactor untouched modules unless requested.

### Step 3: Verification & QA Gatekeeping
Run tests to guarantee zero regressions:
```bash
# Python unit tests (must pass 369/369)
pytest -o pythonpath=scripts --ignore=_site tests/

# Jekyll static build test
bundle exec jekyll build

# Remotion TypeScript check (if touching video/motion engine)
cd simulation/ir-motion-library && npx tsc --noEmit
```

### Step 4: State Synchronization
When a task finishes:
1. Append bullet points to `## Recent Context` in `wiki/hot.md`.
2. Check off items in `PROJECT.md` if milestone deliverables were achieved.
3. Log technical discoveries in `.agents/rules/lessons-learned.md`.

### Step 5: Linear Git Commits
Commit with clear conventional messages:
- `feat(m9): ...`
- `fix(player): ...`
- `test(qa): ...`
- `docs(wiki): ...`

---

## 3. Critical Repository Guardrails (DO NOT BREAK)

1. **English-Only Mandate Across All Platform UI & Videos**:
   - All user-facing UI, tooltips, quiz cards, certificate text, video overlays, and badges MUST be in academic English. No bilingual leaks in the frontend. (Local Indonesian notes are strictly reserved for `plain_id` in the internal glossary dataset).

2. **Preservation of 10 Diplomatic Labs**:
   - 10 chapters contain interactive simulation labs (`sim_*.html`). These must remain intact.
   - All 155 chapters (10 simulation + 145 non-simulation) have had redundant dividers and `### Interactive Learning` headers cleaned up intentionally. Do not re-inject them.

3. **Official Video Explanatory Standard (Mind Map Explanatory)**:
   - Educational videos for `@IRinANutshell` use the **Mind Map Explanatory** engine in `simulation/ir-motion-library/` (Remotion + RoughJS + Google Font `Patrick Hand` + Kokoro-82M neural TTS).
   - **MANDATORY REVIEW GATE**: Setelah Fase 1 (ekstraksi naskah & mind map graf), agen **WAJIB** mempresentasikan preview rancangan mind map kepada pengguna dan **BERHENTI**. Fase 2 s.d. 5 HANYA boleh dieksekusi setelah pengguna memberikan **ACC / persetujuan**.
   - Strict 3-Pillar Camera Law:
     - Deep Zoom-In (1.95x – 2.05x) during concept explanation.
     - Stationary Hold ($v = 0$) during voiceover sentences.
     - Contextual Zoom-Out (1.15x – 1.25x) during paradigm transitions & Panorama pull-back (0.39x) at the end.
   - Large MP4 exports (>50 MB) must strictly reside in `learning-videos/exports/` and are excluded from Git commits via `.gitignore`.
   - **Canonical YouTube Thumbnail Standard**: Setiap rilis video wajib memproduksi YouTube thumbnail 1080p via `scripts/generate_thumbnail.py` menggunakan template torehan kuas (split-screen brush mask, Archivo Black, Space Mono, red-white contrast, dan channel CTA) tersimpan di `learning-videos/posters/*_Thumbnail.png`.

4. **Bespoke LMS Architecture**:
   - The platform uses a custom Native LMS engine (`_layouts/chapter.html`, `_layouts/default.html`, `assets/js/course-player.js`). Legacy GitBook markup has been completely eliminated.

---

## 4. Key CLI Commands
- `make test` : Runs full pytest test suite (369 tests).
- `make serve` : Runs local Jekyll development server (`localhost:4000`).
- `make clean` : Cleans `_site/` build artifacts.
