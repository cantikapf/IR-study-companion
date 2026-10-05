import os
import re

MOD_DIR = os.path.join("_chapters", "043-international-political-economy-of-development")

CHAPTER_UPDATES = {
    "010-study-of-development.md": {
        "summary": "Examines the epistemological evolution of development studies from post-World War II modernization theory (W.W. Rostow) and structural dependency critiques (Raúl Prebisch, Arturo Escobar) to the multidimensional human capabilities approach of Amartya Sen and the UN Sustainable Development Goals (SDGs).",
        "text_replacements": [
            ("The chapter also delves into development thought and how it shapes societies and policies.",
             "The chapter also critically examines developmental theory and its role in shaping governance institutions and socioeconomic policies.")
        ]
    },
    "020-fifthy-years-economic-growth.md": {
        "summary": "Reviews five decades of global economic growth and development paradigms, assessing the shift from post-war state-led Keynesian and dual-sector models (Arthur Lewis) to structural adjustment and Dani Rodrik's diagnostic approach to institutional reform.",
        "text_replacements": []
    },
    "030-inequality-development.md": {
        "summary": "Analyzes theoretical measures and empirical trajectories of inequality in economic development, examining the Kuznets curve hypothesis, Thomas Piketty's capital accumulation dynamics (r > g), Branko Milanovic's elephant curve of global income distribution, and Frances Stewart's horizontal inequality framework.",
        "text_replacements": [
            ("**Inequality** is a complex and multifaceted issue that persists within countries and across the global landscape.",
             "**Inequality** constitutes a systemic structural disparity in resource allocation, wealth, and institutional access that persists within countries and across the global landscape (Kuznets, 1955; Piketty, 2014; Milanovic, 2016).")
        ]
    },
    "040-women-economic-role.md": {
        "summary": "Examines feminist international political economy and gendered development paradigms, analyzing Ester Boserup's foundational critique of agricultural modernization, Diane Elson's unpaid care economy, Naila Kabeer's empowerment framework, and structural gender disparities across global value chains.",
        "text_replacements": []
    },
    "050-asian-model.md": {
        "summary": "Investigates the East Asian developmental state model, evaluating the institutional synergy of state intervention and export promotion across Japan, South Korea, Taiwan, and Singapore through Chalmers Johnson's pilot agencies, Alice Amsden's reciprocal performance standards, and Robert Wade's 'governing the market' thesis.",
        "text_replacements": []
    },
    "060-dev-china-india-chile-african-arab.md": {
        "summary": "Compares divergent national development trajectories across the Global South, evaluating China's state-capitalist transition under Deng Xiaoping, India's post-1991 service-led liberalization, Chile's neoliberal structural experiment under the Chicago Boys, and institutional bottlenecks across Sub-Saharan Africa and the Arab region.",
        "text_replacements": []
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_043():
    print("=== Remediating Module 043 (IPE of Development) ===")
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
    remediate_module_043()
