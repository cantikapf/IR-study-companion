import os
import re

MOD_DIR = os.path.join("_chapters", "050-wto-and-trade-diplomacy")

CHAPTER_UPDATES = {
    "010-international-trade.md": {
        "summary": "Analyzes the foundational principles and macroeconomic drivers of international trade, examining classical comparative advantage, contemporary intra-industry trade patterns, and the socio-political debates surrounding economic interdependence.",
        "text_replacements": []
    },
    "020-transformation-diplomacy-trade.md": {
        "summary": "Traces the structural transformation of trade diplomacy from bilateral sovereign commercial bargaining to legalized, institutionalized multilateralism under the GATT/WTO framework and contemporary preferential trade agreements (PTAs).",
        "text_replacements": []
    },
    "030-industrial-revolution.md": {
        "summary": "Examines the impact of the Industrial Revolution on the global political economy, analyzing how technological innovations in production, steam navigation, and telegraphy catalyzed the first wave of modern trade globalization and colonial division of labor.",
        "text_replacements": []
    },
    "040-evolution-global-trade.md": {
        "summary": "Surveys the historical trajectory of global trade across the 19th and 20th centuries, contrasting the Pax Britannica free-trade era and interwar protectionist collapse with the post-WWII multilateral resurgence.",
        "text_replacements": []
    },
    "050-pillars-wto.md": {
        "summary": "Examines the legal, economic, and political foundations of the World Trade Organization (WTO), analyzing the three core pillars: non-discrimination (MFN and National Treatment), reciprocal market access commitments, and binding dispute settlement.",
        "text_replacements": []
    },
    "060-judicial-procedure-wto.md": {
        "summary": "Analyzes the judicialization of international trade diplomacy, exploring how the shift from diplomatic consensus bargaining to formal third-party adjudication impacts state compliance, national sovereignty, and trade litigation strategy.",
        "text_replacements": []
    },
    "070-wto-dispute-settlement.md": {
        "summary": "Investigates the mechanics of the WTO Dispute Settlement Mechanism under the Dispute Settlement Understanding (DSU), detailing consultations, panel establishment, reverse consensus adoption, compliance surveillance, and the Appellate Body crisis.",
        "text_replacements": []
    },
    "080-wto-decision-making.md": {
        "summary": "Examines the institutional decision-making architecture of the WTO, analyzing consensus-based governance across Ministerial Conferences and the General Council, the 'single undertaking' dilemma, and paralysis in the Doha Development Agenda.",
        "text_replacements": [
            ("the WTO currently has 164 members that represent nearly all of global commerce.",
             "the WTO has 166 members (following the accessions of Timor-Leste and Comoros at MC13 in 2024), representing over 98% of global commerce.")
        ]
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_050():
    print("=== Remediating Module 050 (WTO and Trade Diplomacy) ===")
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
    remediate_module_050()
