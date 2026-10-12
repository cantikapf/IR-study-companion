import json
import glob
import re
import os

def load_real_slugs():
    file_to_slug = {}
    slug_to_file = {}
    pattern = re.compile(r"^slug:\s*['\"]?([^'\"\s]+)['\"]?", re.MULTILINE)
    for path in glob.glob("_chapters/**/*.md", recursive=True):
        norm = path.replace(os.sep, "/")
        with open(norm, "r", encoding="utf-8") as f:
            content = f.read()
        sm = pattern.search(content)
        if sm:
            slug = sm.group(1).strip()
            file_to_slug[norm] = slug
            stem = norm.replace(".md", "")
            file_to_slug[stem] = slug
            slug_to_file[slug] = norm
    return file_to_slug, slug_to_file

CLASS_B_MAP = {
    # Prompt explicit examples
    "Balance of Power": "basic-realism",
    "CPTPP": "tpp-rcep",
    "Norm Life Cycle": "basic-constructivism",
    "RCEP": "tpp-rcep",

    # realism-in-ir entries
    "Bandwagoning": "basic-realism",
    "Revisionist State": "basic-realism",
    "Status Quo State": "basic-realism",

    # Module 010
    "Bipolarity": "study-of-international-relations",
    "Hierarchy in International Relations": "study-of-international-relations",
    "Levels of Analysis": "study-of-international-relations",
    "Multipolarity": "study-of-international-relations",
    "Transnational Advocacy Network (TAN)": "study-of-international-relations",
    "Unipolarity": "study-of-international-relations",

    # Module 011
    "Interpretivism": "social-science-concept",

    # Module 012
    "Containment": "domino-cold-war",

    # Module 013
    "Bandung Spirit": "basic-political",
    "Non-Aligned Movement (NAM)": "basic-political",

    # Module 021
    "Comparative Advantage": "merchantilism-liberalism",
    "Embedded Liberalism": "monetary-system",
    "Hegemonic Stability Theory": "gatt",
    "World-Systems Theory": "constructivism-marxist",

    # Module 022
    "Asymmetric Warfare": "crime-terrorism-insurgency",
    "Brinkmanship": "introduction-security",
    "Collective Defense": "institution-security",
    "Democratic Peace Theory": "liberalism-security",
    "Deterrence": "introduction-security",
    "Extended Deterrence": "institution-security",
    "First-Strike Capability": "institution-security",
    "Mutual Assured Destruction (MAD)": "institution-security",
    "Offense-Defense Balance": "realism-security",
    "Second-Strike Capability": "institution-security",
    "Securitization": "constructivism-others",
    "Security Community": "liberalism-security",
    "Strategic Culture": "realism-security",

    # Module 023
    "Absolute Gains": "neoliberalism-ir",
    "Balance of Threat": "neorealism-ir",
    "Buck-Passing": "neorealism-ir",
    "Critical Theory": "critical-theory",
    "Defensive Realism": "neorealism-ir",
    "English School (International Society)": "introduction-ir-theories",
    "Feminist International Relations": "feminism-ir",
    "Hegemony (Gramscian / Coxian)": "critical-theory",
    "Neoliberal Institutionalism": "neoliberalism-ir",
    "Offensive Realism": "neorealism-ir",
    "Postcolonialism": "critical-theory",
    "Relative Gains": "neorealism-ir",
    "Social Constructivism": "constructivism-ir",
    "Structural Realism (Neorealism)": "neorealism-ir",

    # Module 031
    "Rational Choice Theory": "rational-choice-theory",

    # Module 032
    "Minilateralism": "modes-diplomacy",
    "Paradiplomacy": "actors-diplomacy",
    "Public Diplomacy": "tools-diplomacy",
    "Soft Power": "tools-diplomacy",
    "Track II Diplomacy": "modes-diplomacy",

    # Module 033
    "Audience Costs": "domestic-politics",
    "Groupthink": "models-fpdm",
    "Two-Level Games": "domestic-politics",

    # Module 034
    "Fragile State": "failed-state",
    "Non-Refoulement": "contemporary-issues-in-global-politics",
    "Nuclear Non-Proliferation Treaty (NPT)": "contemporary-issues-in-global-politics",
    "Strategic Chokepoint": "contemporary-issues-in-global-politics",

    # Module 042
    "Innocent Passage": "law-of-the-sea",
    "Jus ad Bellum": "the-use-of-force-in-international-law",
    "Jus Cogens (Peremptory Norm)": "international-treaties",
    "Responsibility to Protect (R2P)": "the-use-of-force-in-international-law",
    "Rome Statute": "international-criminal-law-and-dispute-settlement",
    "State Immunity": "state-and-international-law",
    "Universal Jurisdiction": "international-criminal-law-and-dispute-settlement",

    # Module 043
    "Export-Oriented Industrialization (EOI)": "asian-model",
    "Import Substitution Industrialization (ISI)": "fifty-years-economic-growth",
    "Washington Consensus": "fifty-years-economic-growth",

    # Module 044
    "ASEAN Centrality": "asean-chapter",
    "Treaty of Amity and Cooperation (TAC)": "southeast-asia-region",
    "ZOPFAN": "southeast-asia-region",

    # Module 045
    "Collective Security": "un-security",
    "Peacebuilding": "un-security",

    # Module 046
    "Sovereign Wealth Fund (SWF)": "global-financial-system",
    "Special Drawing Right (SDR)": "global-financial-system",

    # Module 050
    "Anti-Dumping Duty": "wto-dispute-settlement",
    "Carbon Leakage": "evolution-global-trade",
    "Countervailing Duty (CVD)": "wto-dispute-settlement",
    "National Treatment": "pillars-wto",
    "TRIPS Agreement": "wto-decision-making",
}

def main():
    file_to_slug, slug_to_file = load_real_slugs()
    all_slugs = set(slug_to_file.keys())
    print(f"Authoritative real slugs: {len(all_slugs)}")

    with open("_data/ir_glossary.json", "r", encoding="utf-8") as f:
        glossary = json.load(f)

    print(f"Glossary entries count: {len(glossary)}")

    class_a_count = 0
    class_b_count = 0
    sample_mappings = []

    for entry in glossary:
        term = entry["term"]
        old_slug = entry.get("chapter_slug", "")
        if old_slug in all_slugs:
            continue

        if "/" in old_slug or old_slug.startswith("_chapters"):
            target_slug = file_to_slug.get(old_slug) or file_to_slug.get(old_slug + ".md")
            if not target_slug:
                norm_cand = old_slug.strip("/")
                target_slug = file_to_slug.get(norm_cand) or file_to_slug.get(norm_cand + ".md")
            assert target_slug and target_slug in all_slugs, f"Failed Class A: {term} -> {old_slug}"
            entry["chapter_slug"] = target_slug
            class_a_count += 1
            if len(sample_mappings) < 10:
                sample_mappings.append({"term": term, "old": old_slug, "new": target_slug})
        else:
            assert term in CLASS_B_MAP, f"Unmapped Class B: {term} (old: {old_slug})"
            target_slug = CLASS_B_MAP[term]
            assert target_slug in all_slugs, f"Target slug {target_slug} not in real slugs for {term}"
            entry["chapter_slug"] = target_slug
            class_b_count += 1
            if len(sample_mappings) < 10:
                sample_mappings.append({"term": term, "old": old_slug, "new": target_slug})

    total_fixed = class_a_count + class_b_count
    print(f"Class A fixed: {class_a_count}")
    print(f"Class B fixed: {class_b_count}")
    print(f"Total fixed: {total_fixed}")

    unresolved = 0
    for entry in glossary:
        cs = entry.get("chapter_slug", "")
        if not cs or cs not in all_slugs:
            unresolved += 1
            print(f"UNRESOLVED: {entry['term']} -> '{cs}'")

    print(f"UNRESOLVED={unresolved}")
    assert unresolved == 0, "Verification gate failed!"
    assert len(glossary) == 161, f"Expected 161 entries, got {len(glossary)}"

    json_text = json.dumps(glossary, indent=2, ensure_ascii=False) + "\n"
    with open("_data/ir_glossary.json", "w", encoding="utf-8") as f:
        f.write(json_text)
    with open("assets/data/ir_glossary.json", "w", encoding="utf-8") as f:
        f.write(json_text)

    print("Files written successfully.")

    with open("_data/ir_glossary.json", "rb") as f1, open("assets/data/ir_glossary.json", "rb") as f2:
        assert f1.read() == f2.read(), "Files not byte-identical!"
    print("Byte-identical verified!")

    print("SAMPLE_MAPPINGS:")
    print(json.dumps(sample_mappings, indent=2))

if __name__ == "__main__":
    main()
