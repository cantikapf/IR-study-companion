import os
import re

MOD_DIR = os.path.join("_chapters", "021-international-political-economy")

CHAPTER_UPDATES = {
    "010-intro-IPE.md": {
        "summary": "Examines the foundational concepts and ontological debates of International Political Economy (IPE), exploring the reciprocal interaction between states and markets, wealth and power, grounded in Susan Strange's structural power framework and Robert Gilpin's political economy taxonomy.",
        "text_replacements": [
            ("In the realm of Comparative Politics, International Political Economy delves into political institutions' ability to respond to unemployment",
             "In the realm of Comparative Politics, International Political Economy investigates institutional responsiveness to unemployment"),
            ("Macro-economics delves into the balance of payments, exchange rate determination, international policy coordination, and the international capital market.",
             "Macro-economics systematically investigates the balance of payments, exchange rate determination, international policy coordination, and the international capital market.")
        ]
    },
    "020-merchantilism-liberalism-.md": {
        "summary": "Analyzes the classical paradigms of mercantilism/economic nationalism and classical liberalism, contrasting Friedrich List's and Alexander Hamilton's infant-industry protectionism against Adam Smith's absolute advantage and David Ricardo's comparative advantage.",
        "text_replacements": []
    },
    "030-constructivism-marxist.md": {
        "summary": "Investigates critical and heterodox perspectives in IPE, comparing Marxist historical materialism and Wallerstein's World-Systems analysis with John Ruggie's constructivist framework of embedded liberalism.",
        "text_replacements": [
            ("Constructivism contends that **ideas**, values, norms, and identities play a critical role in shaping actors' behaviors and influencing international political and economic dynamics.",
             "Constructivism contends that **ideas**, values, norms, and intersubjective identities actively constitute and shape actors' preferences, behaviors, and international political-economic institutions.")
        ]
    },
    "040-GATT.md": {
        "summary": "Traces the institutional evolution of the multilateral trading regime from the 1947 General Agreement on Tariffs and Trade (GATT) to the 1995 establishment of the World Trade Organization (WTO), highlighting reciprocity, MFN status, and the shift from positive to negative consensus.",
        "text_replacements": []
    },
    "050-TPP-RCEP.md": {
        "summary": "Examines mega-regional trade agreements in the Asia-Pacific, evaluating the Comprehensive and Progressive Agreement for Trans-Pacific Partnership (CPTPP) and the Regional Comprehensive Economic Partnership (RCEP) amid Jagdish Bhagwati's 'spaghetti bowl' phenomenon.",
        "text_replacements": []
    },
    "060-trade-politics.md": {
        "summary": "Explores the domestic political economy of trade policy, contrasting the factor-endowment Stolper-Samuelson theorem and class-conflict model (Rogowski) against the specific-factors Ricardo-Viner industry model and collective action dynamics.",
        "text_replacements": []
    },
    "070-ISI-export.md": {
        "summary": "Compares developmental trade strategies in the Global South, evaluating the structuralist Import Substitution Industrialization (ISI) grounded in the Prebisch-Singer thesis against the East Asian Export-Oriented Industrialization (EOI) developmental state model.",
        "text_replacements": []
    },
    "080-monetary-system.md": {
        "summary": "Examines the historical evolution of the international monetary system from the classical Gold Standard through the Bretton Woods par value regime to post-1971 floating currencies, analyzing Robert Triffin's dilemma and international liquidity management.",
        "text_replacements": []
    },
    "090-exchange-rates.md": {
        "summary": "Analyzes exchange rate policy choices and structural constraints through the Mundell-Fleming Inconsistent Trilemma (Impossible Trinity), evaluating societal distributional conflict and partisan institutional preferences across fixed and floating regimes.",
        "text_replacements": []
    },
    "095-neoliberalism-ipe.md": {
        "summary": "Critically evaluates neoliberal economic orthodoxy in global political economy, assessing its theoretical roots in Friedrich Hayek and Milton Friedman, deregulation, privatization, and structural critiques by David Harvey and Joseph Stiglitz.",
        "text_replacements": []
    },
    "099-neoliberalism-policy.md": {
        "summary": "Examines the policy architecture of neoliberal globalization, analyzing John Williamson's 1990 Washington Consensus, structural adjustment programs (SAPs), capital account liberalization, and post-Washington Consensus institutional reforms.",
        "text_replacements": [
            ("A cornerstone of neoliberal thought is the minimal intervention of the state in economic affairs.",
             "A foundational pillar of neoliberal thought is the minimal intervention of the state in economic affairs.")
        ]
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    # Also clean consecutive '---' lines separated only by whitespace or blank lines
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_021():
    print("=== Remediating Module 021 (International Political Economy) ===")
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
    remediate_module_021()
