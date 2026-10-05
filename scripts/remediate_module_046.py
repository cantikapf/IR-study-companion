import os
import re

MOD_DIR = os.path.join("_chapters", "046-global-economic-architecture")

CHAPTER_UPDATES = {
    "010-intro-global-economic-architecture.md": {
        "summary": "Examines the systemic foundations and institutional pillars of the global economic architecture, analyzing the governance mechanisms established by the Bretton Woods institutions (IMF, World Bank, WTO) and their role in managing macroeconomic stability, trade openness, and financial integration.",
        "text_replacements": []
    },
    "020-evolution-global-economic-architecture.md": {
        "summary": "Traces the structural evolution and contested legitimacy of international economic institutions (IEIs), evaluating the transition from post-war Western dominance to multipolar contestation, Southern representation demands, and the rise of alternative multilateral lending frameworks.",
        "text_replacements": []
    },
    "030-economic-hegemony.md": {
        "summary": "Analyzes Hegemonic Stability Theory (Kindleberger, Gilpin, Keohane) within global economic governance, evaluating whether an open, liberal economic order requires a single dominant power to supply international public goods, and assessing contemporary US-China geo-economic rivalry.",
        "text_replacements": []
    },
    "040-world-trading-system.md": {
        "summary": "Surveys the 20th-century multilateral trading regime, analyzing the transition from bilateral interwar protectionism (Smoot-Hawley) to GATT reciprocal tariff reductions, structural dispute settlement, and 21st-century trade governance challenges.",
        "text_replacements": []
    },
    "050-european-economic.md": {
        "summary": "Examines the economic integration and institutional development of the European Union, analyzing the progression from the European Coal and Steel Community (ECSC) and Single European Act to the Economic and Monetary Union (EMU), the Eurozone, and the EU's 'Brussels Effect' regulatory power.",
        "text_replacements": []
    },
    "060-global-financial-system.md": {
        "summary": "Analyzes the 20th and 21st-century evolution of the global financial system, tracing the rise and fall of Bretton Woods gold-convertibility, capital account liberalization, financial globalization, cross-border banking contagion, and systemic reform after the 2008 Global Financial Crisis.",
        "text_replacements": [
            ("Overall, the supreme position of the dollar was a cornerstone of American hegemony in the postwar era.",
             "Overall, the supreme reserve position of the dollar constituted an indispensable structural pillar of American hegemony in the postwar era (Gilpin, 1987; Strange, 1988).")
        ]
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_046():
    print("=== Remediating Module 046 (Global Economic Architecture) ===")
    for fname, data in CHAPTER_UPDATES.items():
        fpath = os.path.join(MOD_DIR, fname)
        if not os.path.exists(fpath):
            print(f"File not found: {fpath}")
            continue
        
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()
            
        # 1. Update simple_summary
        new_summary = data["summary"]
        content = re.sub(r'simple_summary:\s*"[^"]+"', f'simple_summary: "{new_summary}"', content)
        
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
    remediate_module_046()
