"""
Build a lightweight, client-side full-text search index for all 157 IR Study Companion lessons.
Indexes: slug, title, module, url, abstract, headings, and keywords.
"""

import json
import re
from pathlib import Path

def extract_headings(text):
    headings = []
    for line in text.splitlines():
        if line.startswith("## ") or line.startswith("### "):
            h = re.sub(r'^[#\s]+', '', line).strip()
            headings.append(h)
    return headings

def extract_frontmatter(content):
    meta = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_fm = parts[1]
            body = parts[2]
            for line in raw_fm.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            return meta, body
    return meta, content

def build_index():
    chapters_dir = Path("_chapters")
    index = []

    for f in sorted(chapters_dir.glob("**/*.md")):
        if f.name.startswith("000-index"):
            continue
        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue

        fm, body = extract_frontmatter(content)
        title = fm.get("title", f.stem)
        slug = fm.get("slug", f.stem)
        abstract = fm.get("abstract", "")
        keywords = fm.get("keywords", "")
        headings = extract_headings(body)

        # Get parent folder part label
        parent = f.parent.name
        module_num = parent[:3]

        # Extract top 50 unique substantive words from body
        words = re.findall(r'\b[A-Za-z]{4,}\b', body)
        common_stops = {
            "this", "that", "with", "from", "have", "were", "which", "their", "there", "about",
            "would", "these", "other", "into", "more", "also", "some", "time", "been", "through",
            "between", "after", "before", "should", "could", "while", "during", "where", "under"
        }
        filtered_words = [w.lower() for w in words if w.lower() not in common_stops]
        top_words = list(dict.fromkeys(filtered_words))[:40]

        index.append({
            "slug": slug,
            "title": title,
            "module_num": module_num,
            "url": f"/{slug}.html",
            "abstract": abstract,
            "headings": headings[:8],
            "keywords": top_words
        })

    out_file = Path("assets/data/search_index.json")
    with open(out_file, "w", encoding="utf-8") as out:
        json.dump(index, out, indent=2, ensure_ascii=False)

    print(f"Indexed {len(index)} lessons into {out_file}")

if __name__ == "__main__":
    build_index()
