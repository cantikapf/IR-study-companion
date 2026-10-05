import os
import re

MOD_DIR = os.path.join("_chapters", "044-regionalism-in-southeast-asia-asean-community")

CHAPTER_UPDATES = {
    "010-basic-regionalism.md": {
        "summary": "Examines theories of regionalism and regional integration, contrasting European neo-functionalism (Ernst Haas) and intergovernmentalism (Stanley Hoffmann) against the non-coercive, sovereignty-preserving modalities of Asia-Pacific and Global South regionalism.",
        "text_replacements": []
    },
    "020-southeast-asia-region.md": {
        "summary": "Analyzes the geopolitical construction and historical geography of Southeast Asia, evaluating how post-colonial nation-building, geographical fragmentation, and Cold War ideological conflicts shaped regional security dynamics.",
        "text_replacements": []
    },
    "030-establishment-asean.md": {
        "summary": "Investigates the genesis and institutional founding of the Association of Southeast Asian Nations via the 1967 Bangkok Declaration, examining its origins in conflict resolution following Konfrontasi and the creation of regional confidence-building norms.",
        "text_replacements": []
    },
    "040-asean-chapter.md": {
        "summary": "Analyzes the constitutional codification of ASEAN through the 2007 ASEAN Charter, evaluating the formalization of legal personality, institutional organs (Summits, CPR, AICHR), and the tension between legalized compliance and the non-binding 'ASEAN Way'.",
        "text_replacements": [
            ("title: Understanding ASEAN Chapter", "title: Understanding the ASEAN Charter")
        ]
    },
    "050-asean-community.md": {
        "summary": "Critically examines the ASEAN Community architecture established in 2015, evaluating progress and institutional deficits across its three pillars: the Political-Security Community (APSC), Economic Community (AEC), and Socio-Cultural Community (ASCC).",
        "text_replacements": []
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_044():
    print("=== Remediating Module 044 (Regionalism in Southeast Asia / ASEAN) ===")
    for fname, data in CHAPTER_UPDATES.items():
        fpath = os.path.join(MOD_DIR, fname)
        if not os.path.exists(fpath):
            print(f"File not found: {fpath}")
            continue
        
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()
            
        # 1. Update simple_summary
        new_summary = data["summary"]
        if 'simple_summary:' in content:
            content = re.sub(r'simple_summary:\s*"[^"]+"', f'simple_summary: "{new_summary}"', content)
        else:
            content = re.sub(r'(---\n)', f'simple_summary: "{new_summary}"\n\\1', content, count=1)
        
        # 2. Text replacements
        for target, replacement in data["text_replacements"]:
            if target in content:
                content = content.replace(target, replacement)
                print(f"  Replaced target text in {fname}")
            else:
                print(f"  WARNING: Target text not found in {fname}: {target[:50]}...")
                
        # 3. Clean duplicate dividers
        content = clean_duplicate_dividers(content)
        
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(content)
            
        print(f"  Updated {fname} successfully.")

if __name__ == "__main__":
    remediate_module_044()
