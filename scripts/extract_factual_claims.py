import os
import re
import json

chapters_root = "_chapters"
modules = [d for d in sorted(os.listdir(chapters_root)) if os.path.isdir(os.path.join(chapters_root, d)) and not d.startswith("000") and not d.startswith("999")]

findings = []

# Regex patterns for factual claims:
# 1. Member counts (e.g. "193 member states", "10 members", "28 member countries")
# 2. Specific article citations (e.g. "Article 2(4)", "Article 51", "Chapter VII")
# 3. Casualty / percentage / numerical claims (e.g. "50 million", "25%", "$13 billion")
# 4. Dates with events

for mod in modules:
    mpath = os.path.join(chapters_root, mod)
    for cfile in sorted(os.listdir(mpath)):
        if not cfile.endswith(".md") or cfile.startswith("000"):
            continue
        cpath = os.path.join(mpath, cfile)
        with open(cpath, "r", encoding="utf-8") as f:
            text = f.read()
            lines = text.splitlines()

        for lnum, line in enumerate(lines, 1):
            # Check UN member count claims
            un_m = re.findall(r'(\d+)\s+(?:UN|United Nations)\s+member\s+states', line, re.IGNORECASE)
            for m in un_m:
                findings.append({
                    "type": "UN Member Count",
                    "file": f"{mod}/{cfile}",
                    "line": lnum,
                    "claim": f"{m} UN member states",
                    "context": line.strip()[:120]
                })

            # Check WTO member count
            wto_m = re.findall(r'(\d+)\s+(?:members|countries)\s+in\s+(?:the\s+)?WTO', line, re.IGNORECASE)
            for m in wto_m:
                findings.append({
                    "type": "WTO Member Count",
                    "file": f"{mod}/{cfile}",
                    "line": lnum,
                    "claim": f"{m} members in WTO",
                    "context": line.strip()[:120]
                })

            # Check ASEAN member count
            asean_m = re.findall(r'(\d+)\s+(?:member\s+states|members|countries)\s+(?:in|of)\s+ASEAN', line, re.IGNORECASE)
            for m in asean_m:
                findings.append({
                    "type": "ASEAN Member Count",
                    "file": f"{mod}/{cfile}",
                    "line": lnum,
                    "claim": f"{m} members in ASEAN",
                    "context": line.strip()[:120]
                })

            # Check Article citations (International Law / UN Charter)
            art_m = re.findall(r'(Article\s+\d+(?:\(\d+\))?|Chapter\s+[IVXLCDM]+)', line)
            for a in art_m:
                findings.append({
                    "type": "Legal Article / Chapter",
                    "file": f"{mod}/{cfile}",
                    "line": lnum,
                    "claim": a,
                    "context": line.strip()[:120]
                })

            # Check dates like 19xx or 20xx with bold or specific treaty events
            treaty_dates = re.findall(r'((?:Treaty|Peace|Convention|Protocol|Accord|Pact)\s+of\s+[A-Za-z]+(?:\s+in\s+\d{4})?|\b\d{4}\b\s+(?:Treaty|Peace|Convention|Protocol|Accord|Pact))', line)
            for td in treaty_dates:
                findings.append({
                    "type": "Treaty Reference",
                    "file": f"{mod}/{cfile}",
                    "line": lnum,
                    "claim": td,
                    "context": line.strip()[:120]
                })

print(f"Total extracted factual markers: {len(findings)}")
type_counts = {}
for f in findings:
    type_counts[f["type"]] = type_counts.get(f["type"], 0) + 1
for k, v in type_counts.items():
    print(f"  {k}: {v}")

with open("wiki/factual_claims_sample.json", "w", encoding="utf-8") as out:
    json.dump(findings, out, indent=2)
