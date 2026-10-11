---
name: ir-mindmap-authoring
description: Author IR chapter mind maps via gated concept graph.
---

# IR Mind Map Authoring — Gated Chapter Concept Graph Pipeline

TRIGGER: user says anything like `buat mindmap CH070`, `mindmap chapter berikutnya`, `graph mind map CH080`, `revisi mindmap CH0XX`, `audit mindmap CH0XX`.

You are the **architect** for a chapter mind map in the IR Study Companion repo (`D:/PERSONAL PROJECT/IR-study-companion`, engine at `simulation/ir-motion-library`). You do NOT jump straight to nodes and coordinates. You run six phases, stopping at every ACC gate. This skill exists because a single-shot generation produced duplicate node titles, parent-child nesting of *contrast* pairs, label-less edges, and a near-linear chain masquerading as a mind map.

---

## Command surface (what the user types)

- `buat mindmap CH070` → Phase 1 for that chapter, present brief, STOP for ACC.
- `lanjut` / `ACC` → proceed to the next phase.
- `revisi: <catatan>` → apply user correction, re-present.
- `audit mindmap CH070` → run validator only, report defects, change nothing.

Source chapter lives in `_chapters/**/0NN-*.md` (find by numeric id, see `scripts/produce_video.py::find_chapter_markdown`).

---

## Phase 1 — Academic Concept Brief (STOP for ACC)

Read the chapter markdown. Produce ONLY a brief — no nodes, no coordinates, no timing:

```json
{
  "chapter": "CH070",
  "source_file": "_chapters/.../0NN-x.md",
  "thesis": {"text": "one sentence — the chapter's central claim", "quote": "verbatim substring of the chapter"},
  "learning_objectives": ["..."],
  "core_concepts": [{"id":"snake_case","term":"...","definition":"one sentence","kind":"definition|mechanism|example|critique|implication","quote":"verbatim substring"}],
  "contrasts": [{"a":"concept_id","b":"concept_id","axis":"dimension they differ on","quote":"verbatim substring"}],
  "causal_links": [{"from":"concept_id","to":"concept_id","relation":"...","why":"...","quote":"verbatim substring"}],
  "scholars": [{"name":"...","work":"...","claim":"...","quote":"verbatim substring"}],
  "limitations": [{"text":"one critique per major theory","quote":"verbatim substring"}],
  "source_claims": [{"claim":"...","locator":"_chapters/.../0NN-x.md § Heading","quote":"verbatim substring"}]
}
```

Rules:
- **EVERY substantive item carries a verbatim `quote` copied character-for-character from the chapter file.** Writing a quote from memory is how hallucination enters — read the file and copy. The whole point of the quote is that a machine can check it.
- Separate definition / mechanism / example / critique / implication via `kind`.
- Every important claim carries a `locator`. If you cannot locate it, mark `"NEEDS_VERIFICATION"` — never invent a source, date, scholar, or study.
- Every major theory gets ≥1 `limitation`.
- No absolutes (`proves`, `always`, `never`) unless the source says it; otherwise soften and say so.

### ⛔ MECHANICAL GATE — run before presenting the brief

```bash
python scripts/verify_brief_sources.py <path-to-brief.json>
```

This does not trust your claims. It checks every `quote` is a real substring of the chapter (whitespace/typography-normalised, with fuzzy tolerance for drift), and it independently flags **unsourced facts**: years, `et al.`, volume/page markers, DOI/ISBN, and scholar surnames that appear in the brief but NOT in the chapter. Those are the classic hallucination tells.

- Exit 0 = grounded → you may present the brief and ask for ACC.
- Exit 1 = NOT grounded → fix the quote or drop the claim, re-run. **Never present a brief that fails this gate.**
- `--allow-unquoted` downgrades a missing quote to a warning (use only while drafting, never for the ACC presentation).

Worked example of the gate doing its job: a brief that "remembered" John Searle and "money, national borders, state sovereignty" for CH060 failed instantly — the CH060 chapter never mentions Searle, brute facts, or that list. Reading from memory produced exactly the hallucination the gate exists to catch.

Present the brief readably (thesis → concepts by kind → contrasts → limitations → open questions) **with the gate output**. Then STOP and ask for ACC.

## Phase 2 — Academic Critic (STOP for ACC)

Critique Phase 1 as a skeptical IR professor. Find: conceptual conflation, unsupported claims, false dichotomies, missing counterarguments, overgeneralization, anachronism, misattributed scholars, example-used-instead-of-definition. Return corrections ONLY — do not rewrite the chapter. Answer every critique in the brief, then STOP for ACC.

## Phase 3 — Typed Concept Graph (STOP for ACC)

Convert the ACC'd brief into a graph. No coordinates yet. Allowed relations (closed set — do not invent): `contains`, `contrasts`, `causes`, `enables`, `constrains`, `constitutes`, `illustrates`, `criticizes`, `applies_to`.

```json
{
  "chapter":"CH070",
  "root":"concept_id",
  "acts":[{"id":"act_1","title":"...","hub":"concept_id","scope":"one line"}],
  "nodes":[{"id":"concept_id","title":"unique human title","subtitle":"...","kind":"hub|concept|evidence|transition","bullets":["..."]}],
  "edges":[{"from":"id","to":"id","relation":"contains","label":"short edge label"}]
}
```

Graph laws (the validator enforces these; do not hand-wave):
1. Exactly ONE root (in-degree 0).
2. Every `act` has a `hub` node; acts are siblings under the root.
3. **`contrasts` pairs MUST be siblings.** Never make A a parent of B when the brief lists them as a contrast. (This is the `Regulative → Constitutive` bug.)
4. Max depth 3 from root. No chain longer than 4 nodes.
5. **Every edge has a non-empty `label`.** A relation without a visible label is a defect.
6. **Node `title` is unique within the chapter.** If a term genuinely recurs, qualify it (`X (ontology)` vs `X (hub)`) or rename.
7. A node with children has ≥2 children, or it is a chain link (flag it).
8. Every `concept` node has ≥1 bullet OR a substantive subtitle. Hub/transition nodes may be lighter. No decorative empty nodes.
9. No orphans: every non-root node has an in-edge; every non-leaf has an out-edge.
10. Every narrated concept (Phase 4) exists in the graph, and every graph node is narrated — no orphans in either direction.

## Phase 4 — Narration from the Graph (STOP for ACC)

Write narration FROM the approved graph, never the reverse. Per act: hook/puzzle → definition → mechanism → example → limitation or contrast → transition.

- 90–130 words per act, 2–4 core concepts per act, ≤3 visual bullets per node.
- One sentence = one main claim. Do not read node text verbatim.
- Produce `public/data/ch{NNN}/slides.json` (id, category, title, subtitle, narration, bullets[{headline,detail}]) and aligned `subtitles.json`.
- Emit narration and graph from ONE source of truth; never hand-write slides.json parallel to the graph data.

## Phase 5 — Visual Builder (no concept changes)

Coordinates, colors, node sizes, camera holds, reveal frames, arrow routes, subtitle timing. At this phase you may NOT change concepts or relations. If layout fails, fix layout — do not silently alter the graph. Follow the camera/color/engagement laws in the `ir-video-director` skill. Then run the validator.

## Phase 6 — Validator Gate (0 defects before render)

```bash
cd simulation/ir-motion-library && npx tsx scripts/validate_mindmap.ts ch{NNN}
```
Rejects: duplicate titles, unlabeled edges, orphans, disconnected graph, contrast-as-parent, chain >4, depth >3, empty nodes, narration/graph mismatch. Then `npx tsx scripts/audit_frames.ts ch{NNN}` (0 defects) before any render.

---

## Report format

After each phase report: which phase, the artifact path, the gate status (with the command's real output), and one line of what changed. Never claim a gate passed without the command's actual output.

## Gates (both must exit 0)

| Gate | Command | Catches |
|---|---|---|
| Phase 1 grounding | `python scripts/verify_brief_sources.py <brief.json>` | hallucinated quotes, invented years/citations/scholars |
| Phase 6 structure | `npx tsx scripts/validate_mindmap.ts ch{NNN}` | duplicate titles, label-less edges, orphans, contrast-as-parent, chain/depth |

Then `npx tsx scripts/audit_frames.ts ch{NNN}` (0 defects) before any render.

## Pitfalls (learned)

- Writing a `quote` from memory is exactly how hallucination enters. Copy it from the chapter file. A human/agent that "remembers" a chapter will invent scholars and facts it never contained.
- Do NOT start from "make 36 nodes". Start from `thesis → acts → concepts → relations → narration → visual nodes`.
- "Every node needs 2 bullets" is WRONG and over-rigid; the real rule is every node needs a semantic function.
- A model generating content + graph + coordinates + timing in one shot is the root cause of every defect. Keep phases separate.
- Old, already-published chapters are frozen — this pipeline applies to NEW chapters only. Never retro-edit shipped datasets.
- Windows/MSYS: pass `C:/...` forward-slash paths to native tools; never `/tmp`.
