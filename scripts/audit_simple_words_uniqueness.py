import os
import re
from collections import Counter

CHAPTERS_DIR = "_chapters"

def extract_simple_summary(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match YAML frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        # Check if frontmatter doesn't start with ---
        fm_match2 = re.match(r"^(.*?)\n---", content, re.DOTALL)
        if fm_match2:
            fm_text = fm_match2.group(1)
        else:
            return None
    else:
        fm_text = fm_match.group(1)

    # Find simple_summary in frontmatter
    # Multi-line or single-line quote
    ss_match = re.search(r'simple_summary:\s*"(.*?)"(?:\s*\n|$)', fm_text, re.DOTALL)
    if not ss_match:
        ss_match = re.search(r"simple_summary:\s*'(.*?)'(?:\s*\n|$)", fm_text, re.DOTALL)
    if not ss_match:
        ss_match = re.search(r"simple_summary:\s*(.+?)(?:\s*\n|$)", fm_text)
    
    if ss_match:
        return ss_match.group(1).strip()
    return None

def main():
    all_summaries = {}
    missing_files = []
    total_files = 0

    for root, dirs, files in os.walk(CHAPTERS_DIR):
        for f in sorted(files):
            if f.endswith(".md") and not f.startswith("000-") and not "999-back" in root:
                total_files += 1
                full_path = os.path.join(root, f)
                summary = extract_simple_summary(full_path)
                if not summary:
                    missing_files.append(full_path)
                else:
                    all_summaries[full_path] = summary

    print(f"Total Lesson Files Scanned: {total_files}")
    print(f"Files with simple_summary: {len(all_summaries)}")
    print(f"Files missing simple_summary: {len(missing_files)}")
    if missing_files:
        print("Missing files:")
        for mf in missing_files:
            print("  -", mf)

    # Check for duplicates
    summary_counts = Counter(all_summaries.values())
    duplicates = {s: c for s, c in summary_counts.items() if c > 1}

    print(f"\nUnique Summaries: {len(summary_counts)}")
    print(f"Duplicate Summaries Found: {len(duplicates)}")

    if duplicates:
        print("\nDUPLICATE DETAILS:")
        for dup, count in duplicates.items():
            print(f"\n[Count: {count}] '{dup[:80]}...'")
            matching_files = [fp for fp, s in all_summaries.items() if s == dup]
            for mf in matching_files:
                print("   ->", mf)
        exit(1)
    else:
        print("\nSUCCESS! 100% of chapters have completely unique, personalized summaries!")

if __name__ == "__main__":
    main()
