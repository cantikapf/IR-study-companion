# SH-01 · Phase 1 Audit Rubric (Orchestrator-owned)

Owner: **Director / Orchestrator (vikey)**. Executor: subagent `sa-0-00c4ac15` (agy gemini-3.8-flash-high).
Rule: no Phase 1 deliverable reaches the user until it passes every check below. Fail any row → revise via subagent, re-audit.

---

## A. Completeness (does the artifact exist at all?)

| # | Check | How verified |
|---|---|---|
| A1 | `sh-01-pulau-run/brief.md` exists and is non-empty | read_file, file size > 0 |
| A2 | `sh-01-pulau-run/storyboard.md` exists, non-empty | read_file |
| A3 | `sh-01-pulau-run/script/script.json` exists and parses as JSON | `python -c "import json;json.load(open(...))"` |
| A4 | script.json has exactly 6 beat objects | assert `len(arr) == 6` |
| A5 | Each beat has all 7 keys: id, beat, asset, kicker, headline, text, focus | assert key set equality |
| A6 | No Phase 2+ artifact created (no audio/, no *.tsx, no *.mp4) | directory listing |

## B. Factual integrity (the highest-risk area)

| # | Check | How verified |
|---|---|---|
| B1 | brief.md contains a fact table with columns claim / value / source URL / checked | read_file |
| B2 | Run island dimensions + area cited to a real source | open the URL, confirm the number matches |
| B3 | Banda = world's only nutmeg source until mid-19th c. | open source |
| B4 | Courthope 1616 landing + 1,540-day siege | open source; confirm the day count is the sourced figure |
| B5 | 1664 English seizure of Nieuw Amsterdam | open source |
| B6 | 31 July 1667 Treaty of Breda + *uti possidetis* stated **accurately** (not a whimsical swap) | read narration text; doctrine named correctly |
| B7 | Run population figure + nutmeg still grows there | open source |
| B8 | The disputed "$24 for Manhattan" figure does **NOT** appear anywhere | grep for `24` / `dollar` / `$` |
| B9 | Every URL in the fact table actually resolves (no invented/404 sources) | HTTP status check on each |
| B10 | Unverifiable claims are listed under "unverified claims dropped" rather than silently used | read_file |
| B11 | No Indonesian text anywhere in narration or on-screen strings | grep for Indonesian markers (yang, dan, dengan, pulau as body text, etc.) |

## C. Format contract compliance

| # | Check | How verified |
|---|---|---|
| C1 | 6 beats, target ~40-45 s total, per-beat durations stated | read storyboard |
| C2 | Per-beat durations flagged as provisional pending Phase 2 measurement | read storyboard |
| C3 | Hook lands inside the first 2 seconds | read beat 1 narration |
| C4 | Every `asset` filename in script.json exists in `.../archival-run/assets/` | filesystem check per filename |
| C5 | Asset licences recorded; CC BY-SA 4.0 credit obligation for `nutmeg_fruit_fresh.jpg` flagged in brief.md | read MANIFEST.json vs brief.md |
| C6 | Subtitle position stated per beat inside the safe zone (y≈1330-1490 on 1080x1920), bottom ~360 px clear | read storyboard |
| C7 | Ken Burns treatment per beat within 1.04x-1.15x with pan direction, frame-deterministic (no CSS transitions) | read storyboard |
| C8 | Tone = paradox / asymmetric leverage, not dry chronology | read narration |
| C9 | English-only in all on-screen text (headline, kicker, data chips) | read storyboard |

## D. Architectural fit (orchestrator judgement)

| # | Check | How verified |
|---|---|---|
| D1 | Consistent with the 4-layer archival layout in the `viral-history-shorts` skill | compare storyboard to skill spec |
| D2 | Does not reintroduce a rejected approach (kinetic typography w/o artefact; modern-border map colouring) | read storyboard |
| D3 | Reuses the proven asset set rather than inventing new unverified sources | asset check |
| D4 | Nothing outside `sh-01-pulau-run/` was modified | `git status --short` |
| D5 | No git commit was made | `git log -1` unchanged |

## E. Verdict output to user

Report format: verdict (APPROVED / REVISE), then per-row evidence, then the ACC gate questions the user must answer.
Do not forward the subagent's self-report as fact — re-derive every claim from the files on disk.
