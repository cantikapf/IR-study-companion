#!/usr/bin/env python3
"""
Sync Official YouTube Mindmap Video to IR Study Companion Platform.

Usage:
    python scripts/sync_youtube_video.py --chapter <chapter_query> --url <youtube_url_or_id>

Examples:
    python scripts/sync_youtube_video.py --chapter 080 --url https://youtu.be/example123
    python scripts/sync_youtube_video.py --chapter basic-marxism --url zJesX-ugSX4
"""

import os
import re
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def extract_youtube_id(url_or_id: str) -> str:
    s = url_or_id.strip()
    # Match youtu.be/<id>
    m = re.search(r'youtu\.be/([a-zA-Z0-9_-]{10,12})', s)
    if m:
        return m.group(1)
    # Match watch?v=<id>
    m = re.search(r'[?&]v=([a-zA-Z0-9_-]{10,12})', s)
    if m:
        return m.group(1)
    # Match embed/<id>
    m = re.search(r'embed/([a-zA-Z0-9_-]{10,12})', s)
    if m:
        return m.group(1)
    # Match bare id
    if re.match(r'^[a-zA-Z0-9_-]{10,12}$', s):
        return s
    raise ValueError(f"Could not extract valid YouTube ID from: '{url_or_id}'")

def find_chapter_file(query: str) -> Path:
    q = query.strip().lower()
    # Remove leading CH or M if present
    norm_num = re.sub(r'^(ch|m)', '', q)
    if norm_num.isdigit():
        padded = f"{int(norm_num):03d}"
    else:
        padded = ""

    chapters_dir = REPO_ROOT / "_chapters"
    matches = []

    for f in chapters_dir.rglob("*.md"):
        if f.name == "000-index.md" or "000-front" in f.parts:
            continue
        stem = f.stem.lower()
        if q == stem or (padded and stem.startswith(padded)):
            return f
        if q in stem:
            matches.append(f)

    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        # Prefer exact prefix
        for m in matches:
            if padded and m.name.startswith(padded):
                return m
        raise ValueError(f"Ambiguous query '{query}', multiple files found: {[m.name for m in matches]}")

    raise FileNotFoundError(f"No chapter file found matching query '{query}' in _chapters/")

def update_chapter_frontmatter(file_path: Path, yt_id: str) -> tuple[str, str]:
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"Invalid markdown frontmatter in {file_path}")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"Malformed frontmatter in {file_path}")

    fm = parts[1]
    body = parts[2]

    # Extract title and slug
    title_m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    title = title_m.group(1) if title_m else file_path.stem
    slug_m = re.search(r'^slug:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    slug = slug_m.group(1) if slug_m else file_path.stem

    # Update or add youtube_id at root frontmatter
    if re.search(r'^youtube_id:', fm, re.MULTILINE):
        fm = re.sub(r'^youtube_id:\s*["\']?.*?["\']?\s*$', f'youtube_id: "{yt_id}"', fm, flags=re.MULTILINE)
    else:
        fm = f'\nyoutube_id: "{yt_id}"' + fm

    # Update or add explanatory_video block
    if re.search(r'^explanatory_video:', fm, re.MULTILINE):
        # Update status and youtube_id inside explanatory_video block
        if re.search(r'^\s+youtube_id:', fm, re.MULTILINE):
            fm = re.sub(r'^(\s+youtube_id:\s*)["\']?.*?["\']?\s*$', f'\\g<1>"{yt_id}"', fm, flags=re.MULTILINE)
        else:
            fm = re.sub(r'^(explanatory_video:\s*\n)', f'\\g<1>  youtube_id: "{yt_id}"\n', fm, flags=re.MULTILINE)

        if re.search(r'^\s+status:', fm, re.MULTILINE):
            fm = re.sub(r'^(\s+status:\s*)["\']?.*?["\']?\s*$', '\\g<1>"Published"', fm, flags=re.MULTILINE)
        else:
            fm = re.sub(r'^(explanatory_video:\s*\n)', '\\g<1>  status: "Published"\n', fm, flags=re.MULTILINE)
    else:
        new_block = (
            f'\nexplanatory_video:\n'
            f'  title: "Mind Map Explanatory: {title}"\n'
            f'  desc: "Watch this animated concept map first to explore key actors, systemic dynamics, and theoretical paradigms before exploring the academic chapter text."\n'
            f'  format: "Mind Map Explanatory (@IRinANutshell)"\n'
            f'  engine: "Remotion + RoughJS + Kokoro-82M"\n'
            f'  status: "Published"\n'
            f'  youtube_id: "{yt_id}"\n'
        )
        fm = fm.rstrip() + new_block

    new_content = f"---{fm}\n---{body}"
    file_path.write_text(new_content, encoding="utf-8")
    return title, slug

def update_catalog_json(chapter_num: str, slug: str, yt_id: str):
    catalog_path = REPO_ROOT / "learning-videos" / "catalog.json"
    if not catalog_path.exists():
        return False

    with open(catalog_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = False
    for item in data.get("videos", []):
        if item.get("chapter_num") == chapter_num or item.get("chapter_slug") == slug:
            item["status"] = "Published"
            if "youtube" not in item:
                item["youtube"] = {"channel": "@IRinANutshell"}
            item["youtube"]["youtube_id"] = yt_id
            item["youtube"]["status"] = "Published"
            item["last_updated"] = datetime.now().strftime("%Y-%m-%d")
            updated = True
            break

    if updated:
        with open(catalog_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
    return updated

def update_learning_videos_readme(chapter_num: str, yt_id: str):
    readme_path = REPO_ROOT / "learning-videos" / "README.md"
    if not readme_path.exists():
        return False

    text = readme_path.read_text(encoding="utf-8")
    # Pattern for inventory table row matching CH{chapter_num}
    pattern = rf'(\|\s*`IR-[^`]+-CH{chapter_num}`\s*\|.*?\|)(.*?)(\|.*?)(\[[a-zA-Z0-9_-]+\]\(https://youtu\.be/[a-zA-Z0-9_-]+\)|`-`|\s*)\s*\|'
    
    # Check if row exists
    if re.search(pattern, text):
        def repl(m):
            prefix = m.group(1)
            # update render status column to published if not already
            status_col = " 🟢 PUBLISHED "
            after_status = m.group(3)
            yt_link = f" [{yt_id}](https://youtu.be/{yt_id}) "
            return f"{prefix}{status_col}{after_status}{yt_link}|"

        new_text = re.sub(pattern, repl, text)
        readme_path.write_text(new_text, encoding="utf-8")
        return True
    return False

def update_cx_data_files(slug: str):
    targets = [REPO_ROOT / "_pages" / "index.md", REPO_ROOT / "prototype" / "home.html"]
    updated_files = []
    
    # Look for {"slug":"<slug>",...,"v":false}
    pattern = rf'({{\s*"slug"\s*:\s*"{re.escape(slug)}"[^}}]*?"v"\s*:\s*)false(\s*}})'
    
    for path in targets:
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        if re.search(pattern, content):
            new_content = re.sub(pattern, r'\g<1>true\g<2>', content)
            path.write_text(new_content, encoding="utf-8")
            updated_files.append(path.name)
            
    return updated_files

def main():
    parser = argparse.ArgumentParser(description="Sync Official YouTube Video to IR Study Companion")
    parser.add_argument("--chapter", "-c", required=True, help="Chapter identifier (e.g. 050, 080-global-environment, basic-marxism)")
    parser.add_argument("--url", "-u", required=True, help="YouTube video URL or Video ID")
    args = parser.parse_args()

    yt_id = extract_youtube_id(args.url)
    chapter_file = find_chapter_file(args.chapter)
    
    # Extract chapter number prefix if exists (e.g. '050' from '050-basic-marxism.md')
    m_num = re.match(r'^(\d{3})', chapter_file.stem)
    chapter_num = m_num.group(1) if m_num else ""

    print(f"Target Chapter File : {chapter_file.relative_to(REPO_ROOT)}")
    print(f"Extracted YouTube ID: {yt_id}")

    title, slug = update_chapter_frontmatter(chapter_file, yt_id)
    print(f"Updated Frontmatter : {title} (slug: {slug})")

    cat_ok = update_catalog_json(chapter_num, slug, yt_id)
    print(f"Updated catalog.json: {'YES' if cat_ok else 'SKIPPED (entry not found)'}")

    readme_ok = update_learning_videos_readme(chapter_num, yt_id)
    print(f"Updated README.md   : {'YES' if readme_ok else 'SKIPPED (entry not found)'}")

    cx_files = update_cx_data_files(slug)
    print(f"Updated CX_DATA     : {', '.join(cx_files) if cx_files else 'Already synced or dynamic'}")

    print("\nSUCCESS: Official YouTube video linked and dynamic badges active.")

if __name__ == "__main__":
    main()
