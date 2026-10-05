import os
import re
import sys

CLUSTERS = {
    1: [
        "010-Introduction-to-IR",
        "011-introduction-to-social-science",
        "023-theories-of-international-relations",
        "031-international-relations-research-method",
        "033-foreign-policy-analysis-in-international-relations"
    ],
    2: [
        "012-modern-world-history",
        "022-introduction-to-security-studies",
        "032-diplomacy-and-international-politics",
        "034-Contemporary Issues In Global Politics"
    ],
    3: [
        "021-international-political-economy",
        "043-international-political-economy-of-development",
        "046-global-economic-architecture",
        "050-wto-and-trade-diplomacy"
    ],
    4: [
        "013-indonesia-political-perspective",
        "041-foreign-policy-of-developed-countries",
        "042-international-law-issues-and-international-dispute-settlement",
        "044-regionalism-in-southeast-asia-asean-community",
        "045-international-organization-in-international-relations"
    ]
}

AI_CLICHES = [
    (r"\bin\s+today'?s\s+(?:increasingly\s+)?(?:interconnected|globalized|complex)\s+world\b", "in today's interconnected/globalized world"),
    (r"\bplays?\s+a\s+(?:crucial|vital|pivotal|critical|key)\s+role\s+in\s+shaping\b", "plays a crucial/vital role in shaping"),
    (r"\bdelves?\s+(?:deep\s+)?into\b", "delves into"),
    (r"\brich\s+tapestry\s+of\b", "rich tapestry of"),
    (r"\bis\s+a\s+complex\s+and\s+multifaceted\b", "is a complex and multifaceted"),
    (r"\bserves?\s+as\s+a\s+testament\s+to\b", "serves as a testament to"),
    (r"\bbeacon\s+of\b", "beacon of"),
    (r"\bcrucible\s+of\b", "crucible of"),
    (r"\bpaves?\s+the\s+way\s+for\b", "paves the way for"),
    (r"\bever-(?:evolving|changing)\s+landscape\b", "ever-evolving/changing landscape"),
    (r"\bfosters?\s+a\s+deeper\s+understanding\b", "fosters a deeper understanding"),
    (r"\bcornerstone\s+of\b", "cornerstone of"),
    (r"\bit\s+is\s+(?:important|crucial|essential)\s+to\s+(?:note|remember|recognize)\s+that\b", "it is important to note/remember that")
]

def scan_cluster(cluster_id):
    mods = CLUSTERS.get(cluster_id, [])
    print(f"=== Scanning Cluster {cluster_id} ({len(mods)} modules) ===")
    
    findings = []
    total_chapters = 0
    
    for mod in mods:
        mpath = os.path.join("_chapters", mod)
        if not os.path.exists(mpath):
            continue
        cfiles = sorted([f for f in os.listdir(mpath) if f.endswith(".md")])
        total_chapters += len(cfiles)
        
        for cfile in cfiles:
            cpath = os.path.join(mpath, cfile)
            with open(cpath, "r", encoding="utf-8", errors="replace") as fp:
                text = fp.read()
                lines = text.splitlines()
                
            for lnum, l in enumerate(lines, 1):
                for pat, label in AI_CLICHES:
                    m = re.search(pat, l, re.IGNORECASE)
                    if m:
                        findings.append({
                            "file": f"{mod}/{cfile}",
                            "line": lnum,
                            "label": label,
                            "match": m.group(0),
                            "context": l.strip()
                        })
                        
    print(f"Total chapters scanned: {total_chapters}")
    print(f"Total AI cliché findings: {len(findings)}\n")
    for f in findings:
        print(f"[{f['file']}:{f['line']}] ({f['label']}) -> \"{f['match']}\"")
        print(f"   Context: {f['context'][:110]}")
        print()

if __name__ == "__main__":
    cid = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    scan_cluster(cid)
