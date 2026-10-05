import os
import re

MOD_DIR = os.path.join("_chapters", "042-international-law-issues-and-international-dispute-settlement")

CHAPTER_UPDATES = {
    "010-basic-inter-law.md": {
        "summary": "Examines the ontology, sources, and normative foundations of public international law, analyzing Article 38(1) of the ICJ Statute (treaties, customary law, general principles) and debates over enforcement and state compliance.",
        "text_replacements": []
    },
    "020-international-treaties.md": {
        "summary": "Analyzes the law of treaties governed by the 1969 Vienna Convention on the Law of Treaties (VCLT), detailing treaty negotiation, consent to be bound, reservations, interpretation (Articles 31–32), invalidity, and termination (pacta sunt servanda).",
        "text_replacements": []
    },
    "030-subject-inter-law.md": {
        "summary": "Investigates international legal personality and subjects of international law, contrasting the sovereign rights and duties of states with the derivative personality of international organizations, individuals, and non-state entities.",
        "text_replacements": [
            ("It remains a cornerstone of international law and diplomacy.",
             "It remains a foundational constitutional principle of international law and diplomacy (Croxton, 1999; Osiander, 2001).")
        ]
    },
    "040-state-inter-law.md": {
        "summary": "Examines statehood and recognition criteria under international law, evaluating the declarative and constitutive theories of recognition, the 1933 Montevideo Convention criteria, and sovereign equality before international law.",
        "text_replacements": []
    },
    "050-io-law.md": {
        "summary": "Analyzes the legal status, implied powers, and immunities of international organizations (IOs), evaluating the landmark 1949 ICJ Reparation for Injuries advisory opinion and institutional autonomy vis-à-vis member states.",
        "text_replacements": []
    },
    "051-customary-law.md": {
        "summary": "Investigates the dual elements of Customary International Law (CIL): state practice (diuturnitas) and legal conviction (opinio juris sive necessitatis), examining persistent objector status and jus cogens peremptory norms.",
        "text_replacements": []
    },
    "052-ngo-law.md": {
        "summary": "Analyzes the legal status, consultative role (UN Charter Article 71), and normative influence of non-governmental organizations (NGOs) in drafting multilateral treaties, monitoring compliance, and filing amicus curiae briefs.",
        "text_replacements": [
            ("abstract: Non-governmental organizations (NGOs) play a crucial role in shaping and influencing international law through advocacy, participation in drafting processes, and promoting compliance with legal standards.",
             "abstract: Non-governmental organizations (NGOs) serve as vital norm entrepreneurs and monitoring mechanisms in the progressive development of international law through advocacy, participation in drafting processes, and compliance tracking.")
        ]
    },
    "060-territory-law.md": {
        "summary": "Examines international legal principles of territorial sovereignty, evaluating modes of territorial acquisition (occupation, accretion, cession, prescription), the doctrine of uti possidetis juris, and border demarcation dispute settlement.",
        "text_replacements": []
    },
    "070-dispute-settlement.md": {
        "summary": "Analyzes the taxonomy of international dispute settlement mechanisms under UN Charter Article 33, contrasting diplomatic procedures (negotiation, good offices, mediation, conciliation, inquiry) with legally binding judicial settlement.",
        "text_replacements": []
    },
    "080-law-of-the-sea.md": {
        "summary": "Examines the 1982 UN Convention on the Law of the Sea (UNCLOS), analyzing maritime zones (Internal Waters, 12 nm Territorial Sea, 24 nm Contiguous Zone, 200 nm EEZ, Continental Shelf, and the High Seas as the Common Heritage of Mankind).",
        "text_replacements": []
    },
    "090-ICL.md": {
        "summary": "Investigates individual criminal responsibility under International Criminal Law (ICL), analyzing core international crimes (genocide, crimes against humanity, war crimes, and aggression) and the jurisdictional reach of universal jurisdiction.",
        "text_replacements": [
            ("In today's globalized world, impunity for international crimes is unacceptable.",
             "In contemporary international jurisprudence, ending impunity for international crimes constitutes a peremptory legal obligation.")
        ]
    },
    "091-IC-tribunal.md": {
        "summary": "Traces the institutional evolution of international courts and tribunals, from the Nuremberg and Tokyo Military Tribunals and UN ad hoc tribunals (ICTY, ICTR) to the permanent International Criminal Court (ICC) and its principle of complementarity.",
        "text_replacements": [
            ("- It was the first war crimes court created by the UN and helped pave the way for other international criminal tribunals.",
             "- It was the first war crimes court created by the UN and established essential jurisprudential foundations for subsequent international criminal tribunals.")
        ]
    },
    "092-force-law.md": {
        "summary": "Analyzes the prohibition on the threat or use of force in international law under UN Charter Article 2(4), examining lawful exceptions including individual and collective self-defense (Article 51) and Chapter VII collective security authorization.",
        "text_replacements": [
            ("This prohibition is a cornerstone of the UN system and modern international law governing relations between states.",
             "This prohibition is a fundamental peremptory norm (jus cogens) of the UN Charter system and modern international law governing interstate relations.")
        ]
    },
    "093-IHRL.md": {
        "summary": "Examines International Human Rights Law (IHRL), analyzing the International Bill of Rights (UDHR, ICCPR, ICESCR), regional human rights regimes, universal periodic review mechanisms, and non-derogable civil and political rights.",
        "text_replacements": [
            ("even as state sovereignty remains a cornerstone principle.",
             "even as state sovereignty remains a foundational principle."),
            ("partly due to the principle of non-intervention in the domestic affairs of states being a cornerstone of the international system.",
             "partly due to the principle of non-intervention in the domestic affairs of states serving as a structural pillar of the international system.")
        ]
    },
    "094-IHL.md": {
        "summary": "Investigates International Humanitarian Law (IHL) / jus in bello, evaluating the four 1949 Geneva Conventions and their Additional Protocols, and fundamental principles: military necessity, distinction, proportionality, and precaution.",
        "text_replacements": []
    },
    "095-environment-law.md": {
        "summary": "Analyzes International Environmental Law (IEL), examining customary principles (no-harm rule, precautionary principle, polluter-pays, common but differentiated responsibilities) and multilateral frameworks from Stockholm 1972 and Rio 1992 to the UNFCCC Paris Agreement.",
        "text_replacements": []
    }
}

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def remediate_module_042():
    print("=== Remediating Module 042 (International Law and Dispute Settlement) ===")
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
    remediate_module_042()
