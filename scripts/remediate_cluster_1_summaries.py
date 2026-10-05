import os
import re

SUMMARIES = {
    # 000-front
    "_chapters/000-front/010-title.md": "Course title, curriculum overview, and institutional metadata for the IR Study Companion online learning platform.",
    "_chapters/000-front/020-contents.md": "Complete syllabus and curriculum directory of all 18 modules spanning theory, security, IPE, diplomacy, international law, and regional studies.",
    "_chapters/000-front/025-progress.md": "Student learning dashboard and curriculum completion tracker monitoring progress across all modules, quizzes, and simulations.",
    "_chapters/000-front/030-introduction.md": "Pedagogical introduction to the IR Study Companion, detailing course learning objectives, study methodology, and interactive learning features.",
    
    # 010-Introduction-to-IR
    "_chapters/010-Introduction-to-IR/010-ir-study.md": "Introduces the academic discipline of International Relations, its historical emergence post-WWI, core levels of analysis, and defining debates on power, order, and governance.",
    "_chapters/010-Introduction-to-IR/020-globalization-politics.md": "Analyzes the multifaceted dimensions of globalization, examining transnational flows of capital, culture, and information alongside state sovereignty challenges.",
    "_chapters/010-Introduction-to-IR/030-basic-realism.md": "Introduces classical and structural realism, focusing on systemic anarchy, national interest defined in terms of power, self-help dynamics, and the security dilemma.",
    "_chapters/010-Introduction-to-IR/070-global-finance-trade.md": "Surveys the institutional architecture of global finance and trade, exploring multilateral economic regimes, exchange systems, and cross-border commercial flows.",
    "_chapters/010-Introduction-to-IR/080-global-environment.md": "Examines global environmental governance, transboundary ecological crises, multilateral climate treaties, and the collective action problem of global commons.",
    "_chapters/010-Introduction-to-IR/090-global-security.md": "Introduces security studies, tracing the conceptual expansion from traditional state-centric military deterrence to non-traditional and human security threats.",
    "_chapters/010-Introduction-to-IR/100-regionalism-affairs.md": "Explores the theory and practice of regional cooperation, comparative regionalism, and the proliferation of regional organizations in global affairs.",

    # 023-theories-of-international-relations
    "_chapters/023-theories-of-international-relations/010-ir-theories.md": "Surveys the philosophical foundations, epistemological taxonomies, and major Great Debates of International Relations theory.",
    "_chapters/023-theories-of-international-relations/030-liberalism-ir.md": "Examines classical liberalism in IR, focusing on the Kantian tripod of democracy, economic interdependence, and international organizations.",
    "_chapters/023-theories-of-international-relations/050-neoliberalism.md": "Analyzes neoliberal institutionalism (Robert Keohane), showing how regimes mitigate transaction costs, solve collective action dilemmas, and enable sustained interstate cooperation under anarchy.",
    "_chapters/023-theories-of-international-relations/060-dependency-theory.md": "Evaluates Marxist-structuralist Dependency Theory and Raúl Prebisch's unequal exchange model, explaining unequal terms of trade between the capitalist Core and dependent Periphery.",
    "_chapters/023-theories-of-international-relations/090-feminism-ir.md": "Investigates feminist international relations theory (J. Ann Tickner, Cynthia Enloe), deconstructing gendered assumptions in statecraft, national security, and global political economy.",
    "_chapters/023-theories-of-international-relations/093-critical-theory.md": "Examines Frankfurt School Critical Theory and Robert W. Cox's historical materialism, distinguishing problem-solving theories from emancipatory critique.",

    # 031-international-relations-research-method
    "_chapters/031-international-relations-research-method/020-research-method-ir-study.md": "Examines research design methodology in IR, contrasting positivist, post-positivist, and interpretivist epistemologies.",
    "_chapters/031-international-relations-research-method/030-research-process.md": "Details the step-by-step academic research process in political science, from initial problem identification to literature framing, hypotheses generation, and empirical testing.",
    "_chapters/031-international-relations-research-method/040-qualitative.md": "Analyzes qualitative research methods in IR, focusing on small-N comparative case studies, process tracing, discourse analysis, and elite interviewing.",
    "_chapters/031-international-relations-research-method/050-quantitative.md": "Introduces quantitative methodology in IR, covering large-N datasets (Correlates of War, Polity), regression analysis, causal inference, and descriptive statistics.",
    "_chapters/031-international-relations-research-method/060-research-question.md": "Guides formulating research questions, evaluating theoretical significance, operational feasibility, and the identification of independent, dependent, and intervening variables.",
    "_chapters/031-international-relations-research-method/070-litrev.md": "Provides structural methodology for conducting a comprehensive scholarly literature review, synthesizing theoretical paradigms, identifying research gaps, and building a conceptual framework.",
    "_chapters/031-international-relations-research-method/080-observation.md": "Examines observational and field research methods in international relations, detailing participant observation, archival fieldwork ethics, and ethnographic data collection."
}

EXTRA_DIVIDER_FILES = [
    "_chapters/033-foreign-policy-analysis-in-international-relations/050-public-media-fpdm.md"
]

def clean_duplicate_dividers(content):
    pattern = r"(\n---\s*)+\n(\s*---\s*\n)+"
    content = re.sub(pattern, "\n\n---\n\n", content)
    content = re.sub(r"\n---\s*\n\s*---\s*\n", "\n---\n", content)
    return content

def run():
    print("=== Remediating Remaining Summaries & Duplicate Dividers ===")
    for fpath, new_summary in SUMMARIES.items():
        if not os.path.exists(fpath):
            print(f"File not found: {fpath}")
            continue
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()
            
        content = re.sub(r'simple_summary:\s*"[^"]+"', f'simple_summary: "{new_summary}"', content)
        content = clean_duplicate_dividers(content)
        
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(content)
        print(f"  Updated: {fpath}")
        
    for fpath in EXTRA_DIVIDER_FILES:
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as fp:
                content = fp.read()
            content = clean_duplicate_dividers(content)
            with open(fpath, "w", encoding="utf-8") as fp:
                fp.write(content)
            print(f"  Cleaned dividers: {fpath}")

if __name__ == "__main__":
    run()
