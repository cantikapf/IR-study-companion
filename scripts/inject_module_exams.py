"""
Inject module review exam includes into the final chapter of each of the 18 modules.
"""

from pathlib import Path

module_targets = {
    "010": "_chapters/010-Introduction-to-IR/100-regionalism-affairs.md",
    "011": "_chapters/011-introduction-to-social-science/060-social-change.md",
    "012": "_chapters/012-modern-world-history/190-us-hegemony.md",
    "013": "_chapters/013-indonesia-political-perspective/080-religion-society.md",
    "021": "_chapters/021-international-political-economy/099-neoliberalism-policy.md",
    "022": "_chapters/022-introduction-to-security-studies/090-human-security.md",
    "023": "_chapters/023-theories-of-international-relations/093-critical-theory.md",
    "031": "_chapters/031-international-relations-research-method/090-survey.md",
    "032": "_chapters/032-diplomacy-and-international-politics/060-inter-politics.md",
    "033": "_chapters/033-foreign-policy-analysis-in-international-relations/050-public-media-fpdm.md",
    "034": "_chapters/034-Contemporary Issues In Global Politics/080-natural-disaster.md",
    "041": "_chapters/041-foreign-policy-of-developed-countries/070-japan-foreign-policy.md",
    "042": "_chapters/042-international-law-issues-and-international-dispute-settlement/095-environment-law.md",
    "043": "_chapters/043-international-political-economy-of-development/060-dev-china-india-chile-african-arab.md",
    "044": "_chapters/044-regionalism-in-southeast-asia-asean-community/050-asean-community.md",
    "045": "_chapters/045-international-organization-in-international-relations/060-IMF-world-bank.md",
    "046": "_chapters/046-global-economic-architecture/060-global-financial-system.md",
    "050": "_chapters/050-wto-and-trade-diplomacy/080-wto-decision-making.md"
}

injected_count = 0
for mod_id, file_path_str in module_targets.items():
    p = Path(file_path_str)
    if not p.exists():
        print(f"File not found: {p}")
        continue
    content = p.read_text(encoding="utf-8")
    exam_tag = f'module_exam.html module_id="{mod_id}"'
    if exam_tag in content:
        print(f"Module {mod_id} already has exam include.")
        continue

    injection = f"\n\n---\n\n## Module Review & Summative Examination\n{{% include module_exam.html module_id=\"{mod_id}\" %}}\n"
    content = content.rstrip() + injection
    p.write_text(content, encoding="utf-8")
    injected_count += 1
    print(f"Injected exam for Module {mod_id} into {p.name}")

print(f"Finished. Total injected: {injected_count} files.")
