import os
import re

MOD_DIR = os.path.join("_chapters", "013-indonesia-political-perspective")

CHAPTER_UPDATES = {
    "010-basic-political.md": {
        "summary": "Examines the constitutional foundations, state ideology (Pancasila), and institutional dynamics of Indonesian politics, analyzing power distribution and the evolution of political authority from the 1945 Constitution through the post-Suharto constitutional amendments.",
        "text_replacements": []
    },
    "020-political-institution.md": {
        "summary": "Analyzes the architecture of Indonesian democratic institutions following the four constitutional amendments (1999–2002), examining the separation of powers between the executive presidency, the bicameral legislature (DPR and DPD), and judicial oversight by the Constitutional Court (Mahkamah Konstitusi).",
        "text_replacements": []
    },
    "030-evolution-party.md": {
        "summary": "Traces the historical trajectory of Indonesia's political party system, from the ideological aliran politics of the 1950s parliamentary era, through New Order forced party fusion (PPP, Golkar, PDI), to post-1998 cartelized multiparty competition.",
        "text_replacements": []
    },
    "040-civil-military.md": {
        "summary": "Investigates civil-military relations in Indonesia, evaluating the dismantling of the New Order's Dual Function of ABRI (Dwifungsi), the institutional separation of TNI and Polri, and contemporary debates on civilian democratic control and territorial commands.",
        "text_replacements": []
    },
    "050-electoral-indonesia.md": {
        "summary": "Examines Indonesia's electoral architecture, analyzing open-list proportional representation, simultaneous legislative and presidential elections (Pemilu Serentak), the presidential threshold mechanism, and electoral management by KPU and Bawaslu.",
        "text_replacements": [
            ("with a population of over 260 million people across over 17,000 islands.",
             "with a population of over 278 million people across an archipelago of more than 17,000 islands.")
        ]
    },
    "060-democracy-indonesia.md": {
        "summary": "Critically assesses the trajectory of Indonesian democracy, evaluating regional decentralization ('Big Bang' autonomy laws), oligarchic continuity, money politics, and debates surrounding democratic regression versus democratic resilience.",
        "text_replacements": []
    },
    "070-women-indonesia.md": {
        "summary": "Analyzes women's political participation and descriptive representation in Indonesia, evaluating the impact of the 30% gender candidate quota (UU No. 10/2008), patriarchal institutional bottlenecks, and gendered dynastic politics.",
        "text_replacements": []
    },
    "080-religion-society.md": {
        "summary": "Examines the intersection of religion, identity politics, and civil society in Indonesia, assessing the role of mass Islamic organizations (Nahdlatul Ulama and Muhammadiyah), the rise of conservative mobilization (212 movement), and constitutional protection of religious pluralism.",
        "text_replacements": []
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_013():
    print("=== Remediating Module 013 (Indonesia Political Perspective) ===")
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
            # Add simple_summary before closing ---
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
    remediate_module_013()
