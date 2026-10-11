#!/usr/bin/env python3
"""
verify_brief_sources.py

Gate: prove a mind-map concept brief is GROUNDED in its chapter file, not
hallucinated. This does NOT trust the model's claims — it demands a verbatim
`quote` for every substantive item and then mechanically checks that quote is a
real substring of the chapter markdown.

It also flags UNSOURCED FACTS: years, "et al.", volume/page markers, and
initialised scholar names that the brief asserts but the chapter never contains.
Those are the classic hallucination tells (invented citations, dates, studies).

Usage:
    python scripts/verify_brief_sources.py <path-to-brief.json>
    python scripts/verify_brief_sources.py <path-to-brief.json> --allow-unquoted

Exit 0 = every quoted item matched the chapter and no unsourced fact found.
Exit 1 = at least one defect.

Stdlib only.
"""

import os
import re
import sys
import json
import argparse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Hard rules
MIN_QUOTE_CHARS = 12          # a quote shorter than this is not evidence
MIN_QUOTE_RATIO = 0.60        # >=60% of substantive items must carry a quote
FUZZY_MIN_RATIO = 0.88        # normalised-quote must match this much of some window


def norm(s: str) -> str:
    """Collapse whitespace, unify dashes/quotes, lowercase — for comparison only."""
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"[\u2010-\u2015]", "-", s)   # all dashes -> '-'
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def load_chapter(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def chapter_headings(text: str):
    return [h.strip() for h in re.findall(r"^#{1,4}\s+(.+)$", text, re.M)]


def quote_found(quote: str, hay_norm: str) -> bool:
    """Is `quote` a substring of the chapter (whitespace/typography-normalised)?"""
    q = norm(quote)
    if len(q) < MIN_QUOTE_CHARS:
        return False
    if q in hay_norm:
        return True
    # tolerate small drift: longest-prefix / sliding window fuzzy match
    words = q.split()
    if len(words) < 4:
        return False
    win = len(q) + 8
    step = max(1, len(hay_norm) // 4000)
    best = 0.0
    for i in range(0, max(1, len(hay_norm) - win), step):
        window = hay_norm[i:i + win]
        if q[:20] not in window and q[-20:] not in window:
            continue
        # cheap similarity: shared-char ratio
        common = sum(1 for ch in set(q) if ch in window)
        ratio = common / max(1, len(set(q)))
        best = max(best, ratio)
        if ratio >= FUZZY_MIN_RATIO:
            return True
    return best >= FUZZY_MIN_RATIO


YEAR_RE = re.compile(r"\b(1[89]\d\d|20\d\d)\b")
UNSOURCED_PATTERNS = [
    (re.compile(r"\bet\s+al\.?", re.I), "'et al.' attribution"),
    (re.compile(r"\b(?:vol|no|pp?|p)\.\s*\d+", re.I), "volume/page citation"),
    (re.compile(r"\b[A-Z]\.\s?[A-Z][a-z]{2,}\b"), "initialised scholar name"),
    (re.compile(r"\b(?:doi|isbn|issn)\b", re.I), "identifier"),
    (re.compile(r"\b\d{1,2}\s*\(\d+\)\s*,?\s*\d+[-–]\d+", re.I), "journal issue-page range"),
]


def collect_items(brief: dict):
    """Yield (path, text, quote) for every substantive item that SHOULD be quoted."""
    items = []

    def push(path, obj, text_key="text"):
        if isinstance(obj, dict):
            items.append((path, obj.get(text_key, ""), obj.get("quote", None)))

    push("thesis", brief.get("thesis", {}))
    for i, c in enumerate(brief.get("core_concepts", []) or []):
        push(f"core_concepts[{i}]", c, "definition")
    for i, c in enumerate(brief.get("contrasts", []) or []):
        push(f"contrasts[{i}]", c, "axis")
    for i, c in enumerate(brief.get("causal_links", []) or []):
        push(f"causal_links[{i}]", c, "why")
    for i, s in enumerate(brief.get("scholars", []) or []):
        push(f"scholars[{i}]", s, "claim")
    for i, l in enumerate(brief.get("limitations", []) or []):
        if isinstance(l, dict):
            push(f"limitations[{i}]", l, "text")
        else:
            items.append((f"limitations[{i}]", str(l), None))
    for i, sc in enumerate(brief.get("source_claims", []) or []):
        push(f"source_claims[{i}]", sc, "claim")
    return items


def run(brief_path: str, allow_unquoted: bool):
    with open(brief_path, "r", encoding="utf-8") as f:
        brief = json.load(f)

    chapter_rel = brief.get("source_file", "")
    chapter_abs = os.path.join(BASE_DIR, chapter_rel)

    print("=" * 62)
    print(" BRIEF SOURCE VERIFICATION")
    print("=" * 62)
    print(f" brief        : {brief_path if os.path.isabs(brief_path) else os.path.relpath(brief_path, BASE_DIR)}")
    print(f" source_file  : {chapter_rel or '(MISSING)'}")

    if not chapter_rel:
        print("\n❌ DEFECT: brief has no 'source_file' — cannot verify provenance.")
        return 1
    if not os.path.isfile(chapter_abs):
        print(f"\n❌ DEFECT: source_file does not exist: {chapter_abs}")
        return 1
    if not os.path.abspath(chapter_abs).startswith(os.path.join(BASE_DIR, "_chapters")):
        print("\n❌ DEFECT: source_file is outside _chapters/ — briefs must cite the canonical chapter.")
        return 1

    raw = load_chapter(chapter_abs)
    hay = norm(raw)
    headings = [norm(h) for h in chapter_headings(raw)]
    print(f" chapter bytes: {len(raw)}   headings: {len(chapter_headings(raw))}")

    defects = []
    warnings = []

    items = collect_items(brief)
    if not items:
        print("\n❌ DEFECT: brief has no substantive items to verify.")
        return 1

    quoted = 0
    for path, text, quote in items:
        if quote and str(quote).strip():
            quoted += 1
            if not quote_found(str(quote), hay):
                defects.append(f"QUOTE_NOT_IN_CHAPTER  {path}: quote not found in chapter -> {str(quote)[:90]!r}")
        else:
            label = "WARN" if allow_unquoted else "DEFECT"
            msg = f"{label}: {path} has no verbatim 'quote' (text: {str(text)[:70]!r})"
            (warnings if allow_unquoted else defects).append(msg)

    ratio = quoted / max(1, len(items))
    print(f" quoted items : {quoted}/{len(items)} ({ratio:.0%})")
    if ratio < MIN_QUOTE_RATIO:
        defects.append(f"LOW_QUOTE_RATIO: only {ratio:.0%} of items carry a verbatim quote (min {MIN_QUOTE_RATIO:.0%})")

    # locator headings must exist in the chapter
    for i, sc in enumerate(brief.get("source_claims", []) or []):
        loc = sc.get("locator", "")
        if loc:
            core = norm(re.sub(r"^[^A-Za-z0-9]*", "", loc))
            core = core.split("§")[-1].strip()
            if core and not any(core in h or h in core for h in headings):
                warnings.append(f"LOCATOR_NOT_A_HEADING source_claims[{i}]: {loc!r} not found in chapter headings")

    # unsourced facts: numbers / citations / initials asserted but absent from chapter
    def scan_facts(path, text):
        if not text:
            return
        for m in YEAR_RE.finditer(text):
            y = m.group(1)
            if y not in raw:
                defects.append(f"UNSOURCED_YEAR {path}: year {y} appears in brief but NOT in the chapter")
        for pat, label in UNSOURCED_PATTERNS:
            for m in pat.finditer(text):
                frag = norm(m.group(0))
                if frag and frag not in hay:
                    defects.append(f"UNSOURCED_FACT {path}: {label} {m.group(0)!r} not present in the chapter")

    for path, text, quote in items:
        scan_facts(path, text)
    for name in [s.get("name", "") for s in brief.get("scholars", []) or []]:
        if name and norm(name.split()[-1]) not in hay:
            defects.append(f"UNSOURCED_SCHOLAR: {name!r} does not appear in the chapter text")

    print()
    for w in warnings:
        print(f"  ~ {w}")
    if not defects:
        print(f"✅ GROUNDED — all {quoted} quotes verified against the chapter, no unsourced facts.")
        return 0
    print(f"❌ {len(defects)} DEFECT(S) — brief is NOT fully grounded:")
    for d in defects:
        print(f"  - {d}")
    return 1


def main():
    ap = argparse.ArgumentParser(description="Verify a mind-map brief is grounded in its chapter source.")
    ap.add_argument("brief", help="path to brief JSON")
    ap.add_argument("--allow-unquoted", action="store_true",
                    help="treat a missing quote as a warning instead of a defect")
    args = ap.parse_args()
    sys.exit(run(args.brief, args.allow_unquoted))


if __name__ == "__main__":
    main()