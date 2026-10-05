import os
import re

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

CHILDISH_PATTERNS = [
    "trading snacks",
    "magic glasses",
    "pillow forts",
    "rules of a playground",
    "important puzzle piece",
    "school club",
    "the world is shrinking!",
    "hop in a time machine"
]

def audit_full_repo():
    print("=======================================================")
    print("=== FULL REPOSITORY AUDIT (ALL 18 MODULES) ===")
    print("=======================================================\n")
    
    total_chapters = 0
    total_cliches = []
    total_childish = []
    total_duplicate_dividers = []
    
    for mod in sorted(os.listdir("_chapters")):
        mpath = os.path.join("_chapters", mod)
        if not os.path.isdir(mpath):
            continue
        cfiles = sorted([f for f in os.listdir(mpath) if f.endswith(".md") and not f.startswith("000")])
        for cfile in cfiles:
            total_chapters += 1
            fpath = os.path.join(mpath, cfile)
            with open(fpath, "r", encoding="utf-8", errors="replace") as fp:
                text = fp.read()
                lines = text.splitlines()
                
            # 1. Check AI cliches
            for lnum, l in enumerate(lines, 1):
                for pat, label in AI_CLICHES:
                    m = re.search(pat, l, re.IGNORECASE)
                    if m:
                        total_cliches.append({
                            "file": f"{mod}/{cfile}",
                            "line": lnum,
                            "label": label,
                            "match": m.group(0),
                            "context": l.strip()
                        })
                        
            # 2. Check childish analogies
            for cp in CHILDISH_PATTERNS:
                if cp in text.lower():
                    total_childish.append({
                        "file": f"{mod}/{cfile}",
                        "pattern": cp
                    })
                    
            # 3. Check duplicate dividers
            if "\n---\n\n---\n" in text or "\n---\n---\n" in text:
                total_duplicate_dividers.append(f"{mod}/{cfile}")
                
    print(f"Total core chapters audited: {total_chapters}")
    print(f"Total AI cliché findings: {len(total_cliches)}")
    for c in total_cliches:
        print(f"  [{c['file']}:{c['line']}] ({c['label']}) -> '{c['match']}'")
        
    print(f"\nTotal childish analogies findings: {len(total_childish)}")
    for ch in total_childish:
        print(f"  [{ch['file']}] contains '{ch['pattern']}'")
        
    print(f"\nTotal duplicate divider issues: {len(total_duplicate_dividers)}")
    for d in total_duplicate_dividers:
        print(f"  [{d}] duplicate divider")
        
    if not total_cliches and not total_childish and not total_duplicate_dividers:
        print("\n>>> CONGRATULATIONS: 100% REPOSITORY CLEAN! ZERO AI FORMULAS OR ARTIFACTS FOUND! <<<")

if __name__ == "__main__":
    audit_full_repo()
