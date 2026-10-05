import os
import re

MOD_DIR = os.path.join("_chapters", "041-foreign-policy-of-developed-countries")

CHAPTER_UPDATES = {
    "010-history-evolution-fpa.md": {
        "summary": "Examines the epistemological and historical evolution of Foreign Policy Analysis (FPA) as an empirical subfield of IR, evaluating the transition from rational unitary actor models to actor-specific behavioral frameworks.",
        "text_replacements": []
    },
    "020-economic-statecraft.md": {
        "summary": "Analyzes the instruments and strategic utility of economic statecraft (David Baldwin), examining positive incentives, negative sanctions, asset freezes, and trade embargoes within asymmetric economic interdependence.",
        "text_replacements": []
    },
    "030-women-foreign-policy.md": {
        "summary": "Investigates feminist foreign policy (FFP) frameworks, evaluating Sweden's 2014 pioneering model (Rights, Resources, Representation) and the systemic underrepresentation of women in national security and diplomatic leadership.",
        "text_replacements": [
            ("Their successes pave the way for future women leaders.",
             "Their demonstrated institutional effectiveness establishes precedents that institutionalize expanded access for subsequent cohorts of women leaders.")
        ]
    },
    "040-EU-foreign-policy.md": {
        "summary": "Analyzes European Union foreign policy and external energy governance, examining the Common Foreign and Security Policy (CFSP), the role of the High Representative, structural power, and the geopolitical vulnerabilities of external energy dependencies.",
        "text_replacements": []
    },
    "050-australia-foreign-policy.md": {
        "summary": "Examines the institutional drivers and strategic dilemmas of Australian foreign policy, analyzing the structural tension between its historical security alliance (ANZUS / AUKUS) and economic trade interdependence in the Indo-Pacific.",
        "text_replacements": []
    },
    "060-us-foreign-policy.md": {
        "summary": "Surveys the historical trajectory and institutional architecture of United States foreign policy, examining the constitutional struggle between the executive branch and Congress, isolationist vs. internationalist traditions, and grand strategy from the Cold War to great power competition.",
        "text_replacements": [
            ("Congress plays a key role in shaping U.S. foreign policy.",
             "Congress exercises substantial constitutional authority in checking and directing U.S. foreign policy.")
        ]
    },
    "070-japan-foreign-policy.md": {
        "summary": "Investigates Japanese foreign policy decision-making, evaluating the Yoshida Doctrine, Article 9 of the Peace Constitution, bureaucratic fragmentation, and contemporary security normalisation under the Free and Open Indo-Pacific (FOIP) framework.",
        "text_replacements": []
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_041():
    print("=== Remediating Module 041 (Foreign Policy of Developed Countries) ===")
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
            content = re.sub(r'simple_summary:\s*"[^"]*"', f'simple_summary: "{new_summary}"', content)
        else:
            # Add simple_summary before closing frontmatter
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
    remediate_module_041()
