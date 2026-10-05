import os
import re

CLUSTERS = {
    3: [
        "021-international-political-economy",
        "043-international-political-economy-of-development",
        "046-global-economic-architecture",
        "050-wto-and-trade-diplomacy"
    ]
}

def inspect():
    for mod in CLUSTERS[3]:
        mpath = os.path.join("_chapters", mod)
        print(f"\n=== Module {mod} ===")
        for f in sorted(os.listdir(mpath)):
            if not f.endswith(".md"):
                continue
            fpath = os.path.join(mpath, f)
            with open(fpath, "r", encoding="utf-8") as fp:
                txt = fp.read()
            m = re.search(r'simple_summary:\s*"([^"]+)"', txt)
            summary = m.group(1) if m else "NONE"
            print(f"  {f}: {summary[:80]}...")

if __name__ == "__main__":
    inspect()
