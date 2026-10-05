import os
import re

CLUSTERS = {
    4: [
        "013-indonesia-political-perspective",
        "041-foreign-policy-of-developed-countries",
        "042-international-law-issues-and-international-dispute-settlement",
        "044-regionalism-in-southeast-asia-asean-community",
        "045-international-organization-in-international-relations"
    ]
}

def inspect():
    for mod in CLUSTERS[4]:
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
