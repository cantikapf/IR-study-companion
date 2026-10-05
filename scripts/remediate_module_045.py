import os
import re

MOD_DIR = os.path.join("_chapters", "045-international-organization-in-international-relations")

CHAPTER_UPDATES = {
    "010-intro-IO.md": {
        "summary": "Examines the classification, legal mandate, and institutional typology of International Organizations (IOs), distinguishing intergovernmental organizations (IGOs) from international non-governmental organizations (INGOs).",
        "text_replacements": [
            ("International organizations (IO) and intergovernmental organizations (IGOs) play a crucial role in international relations, facilitating cooperation between states and addressing global challenges.",
             "International organizations (IOs) and intergovernmental organizations (IGOs) serve as central institutional mechanisms in international relations, facilitating interstate cooperation and mitigating collective action problems.")
        ]
    },
    "020-theory-IO.md": {
        "summary": "Analyzes theoretical perspectives on International Organizations, contrasting realist instrumentalism (arenas of state power), neoliberal institutionalism (reducing transaction costs and information asymmetries), and constructivist authority (bureaucratic culture and norm diffusion).",
        "text_replacements": []
    },
    "030-evolution-IO.md": {
        "summary": "Traces the historical evolution of multilateral institutions from 19th-century public international unions and the Concert of Europe, through the structural demise of the League of Nations, to the post-WWII United Nations system.",
        "text_replacements": []
    },
    "040-UN-administration.md": {
        "summary": "Analyzes the administrative architecture and bureaucratic governance of the United Nations, evaluating the role of the UN Secretariat, Secretary-General diplomatic agency under Article 99, budget constraints, and structural reform challenges.",
        "text_replacements": []
    },
    "050-UN-security.md": {
        "summary": "Investigates the collective security architecture of the UN Security Council under Chapter VII of the UN Charter, evaluating the P5 veto mechanism, peace operations, sanctions regimes, and geopolitical deadlock.",
        "text_replacements": []
    },
    "060-IMF-world-bank.md": {
        "summary": "Analyzes the governance structures, lending instruments, and institutional mandates of the Bretton Woods institutions (IMF and World Bank), evaluating structural adjustment conditionality, quota voting power, and contestation from emerging economies.",
        "text_replacements": []
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_045():
    print("=== Remediating Module 045 (International Organizations) ===")
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
    remediate_module_045()
