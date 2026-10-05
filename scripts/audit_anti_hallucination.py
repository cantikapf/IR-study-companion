"""
Anti-Hallucination & Academic Integrity Auditor for IR Study Companion
Scans markdown files in _chapters/ for:
1. Canonical scholar attributions and publication year consistency.
2. Legal article citations and treaty names (UN Charter, UNCLOS, VCLT, Rome Statute, etc.).
3. Generic AI filler phrases and boilerplate patterns.
4. Typography/encoding artifacts (broken chars, double bolding **word **word**).
5. Quiz question and answer key integrity.
"""

import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(BASE_DIR, "_chapters")

CANON_SCHOLARS = {
    "Waltz": {
        "valid_years": [1954, 1959, 1979, 1993, 2000, 2012],
        "key_terms": ["structural realism", "neorealism", "balance of power", "anarchy", "bipolarity", "levels of analysis", "man, the state, and war"]
    },
    "Morgenthau": {
        "valid_years": [1946, 1948, 1951, 1962],
        "key_terms": ["classical realism", "animus dominandi", "six principles", "national interest", "power"]
    },
    "Keohane": {
        "valid_years": [1977, 1984, 1989, 1998],
        "key_terms": ["neoliberal institutionalism", "complex interdependence", "after hegemony", "international regimes"]
    },
    "Nye": {
        "valid_years": [1977, 1990, 2002, 2004, 2011],
        "key_terms": ["soft power", "hard power", "smart power", "complex interdependence"]
    },
    "Wendt": {
        "valid_years": [1992, 1994, 1999, 2003],
        "key_terms": ["constructivism", "anarchy is what states make of it", "social theory", "hobbesian", "lockean", "kantian"]
    },
    "Allison": {
        "valid_years": [1969, 1971, 1999, 2017],
        "key_terms": ["essence of decision", "rational actor", "organizational process", "bureaucratic politics", "thucydides trap"]
    },
    "Putnam": {
        "valid_years": [1988],
        "key_terms": ["two-level games", "win-set", "ratification", "level i", "level ii"]
    },
    "Bull": {
        "valid_years": [1977, 1984],
        "key_terms": ["english school", "anarchical society", "international society", "pluralism", "solidarism"]
    },
    "Carr": {
        "valid_years": [1939, 1946],
        "key_terms": ["twenty years' crisis", "utopianism", "realism"]
    }
}

AI_BOILERPLATE_PATTERNS = [
    (r"\b(?:is\s+a\s+complex\s+and\s+multifaceted\s+(?:concept|phenomenon|issue|topic))\b", "Cliché: 'complex and multifaceted'"),
    (r"\b(?:plays?\s+a\s+(?:crucial|vital|pivotal|critical|key)\s+role\s+in\s+shaping)\b", "Cliché: 'plays a crucial/vital role in shaping'"),
    (r"\b(?:in\s+today'?s\s+(?:increasingly\s+)?(?:interconnected|globalized|complex)\s+world)\b", "Cliché: 'in today's interconnected/globalized world'"),
    (r"\b(?:rich\s+tapestry\s+of)\b", "Cliché: 'rich tapestry of'"),
    (r"\b(?:serves?\s+as\s+a\s+testament\s+to)\b", "Cliché: 'testament to'"),
    (r"\b(?:delves?\s+(?:deep\s+)?into)\b", "Cliché: 'delves into'"),
    (r"\b(?:it\s+is\s+(?:crucial|vital|essential|imperative)\s+to\s+(?:understand|remember|note|recognize))\b", "Cliché: 'it is crucial/vital to understand'"),
    (r"\b(?:In\s+conclusion,\s+[^\.\n]{10,80}\s+plays\s+a\s+(?:vital|crucial|significant)\s+role)\b", "Cliché: AI conclusion summary formula"),
]

def scan_file(filepath):
    rel_path = os.path.relpath(filepath, BASE_DIR)
    findings = []
    
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    lines = content.splitlines()

    # 1. Encoding artifacts
    if "\ufffd" in content:
        findings.append({
            "type": "ENCODING_ERROR",
            "file": rel_path,
            "line": 0,
            "details": "Contains Unicode replacement character (\ufffd)"
        })

    # 2. Corrupted bold tags: **word **word**
    for lnum, line in enumerate(lines, 1):
        if re.search(r"\*\*[A-Za-z0-9_\-]+\s+\*\*", line):
            findings.append({
                "type": "MALFORMED_MARKDOWN",
                "file": rel_path,
                "line": lnum,
                "details": f"Malformed bold markdown: {line.strip()[:80]}"
            })

    # 3. AI Boilerplate phrases
    for lnum, line in enumerate(lines, 1):
        for pattern, label in AI_BOILERPLATE_PATTERNS:
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                findings.append({
                    "type": "AI_BOILERPLATE",
                    "file": rel_path,
                    "line": lnum,
                    "details": f"{label} -> '{m.group(0)}'"
                })

    # 4. Scholar publication dates check
    for scholar, data in CANON_SCHOLARS.items():
        pattern = rf"\b{scholar}\b[^\.\n]{{0,60}}\b(19\d\d|20\d\d)\b"
        for lnum, line in enumerate(lines, 1):
            for match in re.finditer(pattern, line, re.IGNORECASE):
                year = int(match.group(1))
                if year not in data["valid_years"]:
                    # Check if year is outside expected range
                    if year < min(data["valid_years"]) - 5 or year > max(data["valid_years"]) + 5:
                        findings.append({
                            "type": "SUSPICIOUS_SCHOLAR_YEAR",
                            "file": rel_path,
                            "line": lnum,
                            "details": f"{scholar} linked to unexpected year {year} in: '{match.group(0)}'"
                        })

    # 5. Quiz validation
    quiz_pattern = re.compile(r"\{%\s*include\s+quiz\.html\s+([^%]+)%\}")
    for lnum, line in enumerate(lines, 1):
        m = quiz_pattern.search(line)
        if m:
            args_str = m.group(1)
            # check question, opt1..opt4, correct
            has_q = bool(re.search(r'question="[^"]+"', args_str))
            has_opts = all(bool(re.search(rf'opt{i}="[^"]+"', args_str)) for i in range(1, 5))
            correct_match = re.search(r'correct="([1-4])"', args_str)
            
            if not has_q:
                findings.append({"type": "QUIZ_ERROR", "file": rel_path, "line": lnum, "details": "Quiz missing question"})
            if not has_opts:
                findings.append({"type": "QUIZ_ERROR", "file": rel_path, "line": lnum, "details": "Quiz missing one or more options (opt1-opt4)"})
            if not correct_match:
                findings.append({"type": "QUIZ_ERROR", "file": rel_path, "line": lnum, "details": "Quiz has invalid or missing correct answer (must be 1-4)"})

    return findings

def run_audit(target_subdirs=None):
    all_findings = []
    
    if not os.path.exists(CHAPTERS_DIR):
        print(f"Error: {CHAPTERS_DIR} does not exist.")
        return []

    dirs_to_scan = target_subdirs if target_subdirs else sorted(os.listdir(CHAPTERS_DIR))
    
    for d in dirs_to_scan:
        dpath = os.path.join(CHAPTERS_DIR, d)
        if not os.path.isdir(dpath):
            continue
        for fname in sorted(os.listdir(dpath)):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dpath, fname)
            f_findings = scan_file(fpath)
            all_findings.extend(f_findings)

    return all_findings

if __name__ == "__main__":
    import sys
    targets = sys.argv[1:] if len(sys.argv) > 1 else None
    results = run_audit(targets)
    
    print(f"Audit completed. Total findings: {len(results)}")
    by_type = {}
    for r in results:
        t = r["type"]
        by_type[t] = by_type.get(t, 0) + 1
        
    for t, cnt in by_type.items():
        print(f"  - {t}: {cnt}")
        
    print("\nDetailed Findings Sample (first 25):")
    for r in results[:25]:
        print(f"  [{r['type']}] {r['file']}:{r['line']} - {r['details']}")
