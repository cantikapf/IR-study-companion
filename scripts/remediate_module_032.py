"""
Surgical Remediation Script for Module 032: Diplomacy and International Politics
Cleans duplicate dividers, elevates childish peacemaker summaries, eliminates AI clichés,
and grounds theoretical concepts in canonical peer-reviewed literature.
"""

import os
import re

MOD_DIR = os.path.join("_chapters", "032-diplomacy-and-international-politics")

def clean_duplicate_dividers(text):
    cleaned = re.sub(r'---\s*\n\s*---\s*\n', '---\n', text)
    cleaned = re.sub(r'---\s*\n\s*\n\s*---\s*\n', '---\n', cleaned)
    cleaned = re.sub(r'---\s*\n\s*---\s*', '---\n', cleaned)
    return cleaned

def remediate_010():
    fpath = os.path.join(MOD_DIR, "010-intro-diplo.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter summary
    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines diplomacy as the primary non-coercive instrument of statecraft, distinguishing diplomatic communication from foreign policy formulation, and tracing its historical evolution from ancient Near Eastern records to multilateral diplomacy."',
        content
    )

    # Correct kingdom of Amazi -> Hamazi
    content = content.replace("kingdom of Amazi", "kingdom of Hamazi")

    # Ground Nicolson (1939), Berridge (2022), and Kautilya's Arthashastra categories
    content = content.replace(
        'ancient Indian civilization, as outlined in the Arthashastra, detailed different classes of diplomatic representatives with varying levels of authority.',
        'ancient Indian statecraft, as codified in Kautilya\'s *Arthashastra* (~3rd century BCE), systematically categorized diplomatic envoys into three distinct functional ranks: *nisrstartha* (plenipotentiary ambassadors), *parimitartha* (envoys with bounded negotiating mandates), and *sasanahara* (official messengers and conveyers of royal decrees). In modern diplomatic theory, scholars like Harold Nicolson (*Diplomacy*, 1939) and G.R. Berridge (*Diplomacy: Theory and Practice*, 2022) have reaffirmed this institutional distinction between high foreign policy decision-making and diplomatic execution.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 010-intro-diplo.md")

def remediate_020():
    fpath = os.path.join(MOD_DIR, "020-history-diplomacy.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Traces the institutional history of diplomacy from the 14th-century BCE Amarna system and ancient Greek proxenia to Italian Renaissance resident embassies, the 1815 Congress of Vienna, and the 1961 Vienna Convention on Diplomatic Relations (VCDR)."',
        content
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 020-history-diplomacy.md")

def remediate_030():
    fpath = os.path.join(MOD_DIR, "030-modes-diplomacy.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Categorizes the operational modes of diplomacy—bilateral, multilateral, conference, coercive, mediation, humanitarian, defense, and parliamentary diplomacy—evaluating their institutional mechanisms and strategic trade-offs."',
        content
    )

    # Cliché removal: "pave the way for" and "paving the way for"
    content = content.replace(
        "Mediation can prevent escalation of violence and pave the way for peaceful resolution of conflicts.",
        "Mediation can prevent the escalation of hostilities and establish structural preconditions for the peaceful resolution of conflicts."
    )
    content = content.replace(
        "foster trust and understanding between conflicting parties, paving the way for reconciliation.",
        "foster trust and mutual understanding between conflicting parties, laying institutional foundations for durable reconciliation."
    )

    # Ground I. William Zartman 2000 (Ripeness, Mutually Hurting Stalemate)
    content = content.replace(
        'Some conflicts may be so complex or deeply rooted that finding a solution seems impossible.',
        'Conflict resolution scholars like I. William Zartman (2000) demonstrate that mediation success often hinges on conflict "ripeness"—a perceptual moment where adversaries perceive a "mutually hurting stalemate" and recognize that unilateral victory is unattainable.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 030-modes-diplomacy.md")

def remediate_040():
    fpath = os.path.join(MOD_DIR, "040-actors-diplomacy.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Analyzes the plurality of diplomatic actors beyond traditional foreign ministries, including foreign service corps, intergovernmental bodies, sub-state entities (paradiplomacy), civil society NGOs, and digital public diplomacy."',
        content
    )

    # Cliché removal: "rich tapestry of"
    content = content.replace(
        "Cities, universities, community organizations, companies, and individuals all contribute to the rich tapestry of global cultural connections.",
        "Cities, universities, community organizations, companies, and non-state entities establish dense, decentralized networks of cross-border engagement, a phenomenon Brian Hocking (1999) termed 'catalytic diplomacy'."
    )

    # Ground Joseph Nye (2004 Soft Power / Public Diplomacy)
    content = content.replace(
        'Cultural exchange plays a vital role in international relations by fostering greater mutual understanding between countries.',
        'Cultural exchange constitutes a primary instrument of soft power—defined by Joseph Nye (2004) as the ability to achieve desired outcomes through attraction and persuasion rather than military coercion or economic inducement.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 040-actors-diplomacy.md")

def remediate_050():
    fpath = os.path.join(MOD_DIR, "050-tools-diplomacy.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines the multifaceted instruments of diplomacy—trade and investment promotion, economic sanctions, cultural and digital public diplomacy, and legal codification under the Vienna Conventions."',
        content
    )

    # Ground Vienna Convention on Consular Relations (1963)
    content = content.replace(
        'The convention contains 79 articles with significant provisions including:',
        'The Vienna Convention on Consular Relations (VCCR, adopted 1963, entered into force 1967) codified consular relations into 79 formal articles, with landmark provisions including:'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 050-tools-diplomacy.md")

def remediate_060():
    fpath = os.path.join(MOD_DIR, "060-inter-politics.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Surveys key structural issues in contemporary international politics—strategic security dilemmas, bilateral arms control treaties (SALT/START), post-conflict peacebuilding, universal human rights norms, and global health diplomacy."',
        content
    )

    # Ground Hedley Bull (1977), Schelling & Halperin (1961)
    content = content.replace(
        '**International** politics refers to the relationships between countries and how they interact on the global stage.',
        'International politics operates within what Hedley Bull (1977, *The Anarchical Society*) termed an "anarchical society"—a domain where sovereign states recognize common rules and shared institutions despite the absence of an overarching world government.'
    )
    content = content.replace(
        'Arms control negotiations aim to reduce stockpiles and the risk of war through treaties like SALT and START.',
        'As Thomas Schelling and Morton Halperin classically formulated in *Strategy and Arms Control* (1961), modern arms control aims to stabilize deterrence, minimize the likelihood of war, and reduce the catastrophic destruction should deterrence fail, as institutionalized in the Strategic Arms Limitation Talks (SALT I & II) and Strategic Arms Reduction Treaties (START).'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 060-inter-politics.md")

if __name__ == "__main__":
    remediate_010()
    remediate_020()
    remediate_030()
    remediate_040()
    remediate_050()
    remediate_060()
    print("Module 032 remediation completed successfully!")
