"""
Surgical Remediation Script for Module 034: Contemporary Issues in Global Politics
Cleans duplicate dividers, elevates childish summaries, removes AI artifacts,
and grounds theoretical concepts in canonical peer-reviewed literature.
"""

import os
import re

MOD_DIR = os.path.join("_chapters", "034-Contemporary Issues In Global Politics")

def clean_duplicate_dividers(text):
    cleaned = re.sub(r'--\s*\n\s*---\s*\n', '---\n', text)
    cleaned = re.sub(r'---\s*\n\s*---\s*\n', '---\n', text)
    cleaned = re.sub(r'---\s*\n\s*\n\s*---\s*\n', '---\n', cleaned)
    cleaned = re.sub(r'---\s*\n\s*---\s*', '---\n', cleaned)
    return cleaned

def remediate_010():
    fpath = os.path.join(MOD_DIR, "010-theoritical-perspective.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter summary
    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Critiques the unitary actor assumption and the anthropomorphic concept of the \'national interest,\' proposing Analytical Eclecticism as a pragmatic methodological alternative for unpacking complex global challenges."',
        content
    )

    # Title cleanup
    content = content.replace("title: Theoretical Perspective", "title: Theoretical Perspectives in Global Politics")

    # Ground Sil & Katzenstein (2010), Gourevitch (1978)
    content = content.replace(
        'Known as analytical eclecticism, this strategy uses concrete real world problems as its starting point,',
        'Known as analytic eclecticism—rigorously conceptualized by Rudra Sil and Peter J. Katzenstein in *Beyond Paradigms* (2010)—this strategy uses concrete real-world problems as its starting point,'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 010-theoritical-perspective.md")

def remediate_020():
    fpath = os.path.join(MOD_DIR, "020-poverty-development-aid.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines conceptual paradigms of poverty and underdevelopment—modernization, dependency theory, capability approaches, and structural critique of neoliberal foreign aid conditionality."',
        content
    )

    # Ground Todaro (2020), Amartya Sen (1999)
    content = content.replace(
        'For others, human development factors like health, education, political freedom, and environmental sustainability are central.',
        'For others, as formulated by Amartya Sen in *Development as Freedom* (1999), development is defined as the expansion of real human capabilities and substantial freedoms, rather than merely income growth. Michael Todaro and Stephen Smith (*Economic Development*, 2020) synthesize this as a multidimensional process involving major changes in social structures, popular attitudes, and national institutions, alongside economic acceleration.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 020-poverty-development-aid.md")

def remediate_030():
    fpath = os.path.join(MOD_DIR, "030-failed-state.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines state fragility, collapse, and post-conflict reconstruction, analyzing indicators of failed states (loss of Weberian monopoly of legitimate violence) and the dilemmas of external state-building interventions."',
        content
    )

    # Ground Max Weber (1919), Rotberg (2004), Fukuyama (2004)
    content = content.replace(
        'The key characteristics of **state failure** include the inability of the state to maintain a monopoly on the use of force, provide public services, and sustain a functioning economy and market.',
        'Drawing upon Max Weber\'s classic definition of statehood as the monopoly on the legitimate use of physical force (*Politics as a Vocation*, 1919), state failure occurs when central authorities lose territorial control and institutional efficacy. As Robert Rotberg (*When States Fail*, 2004) and Francis Fukuyama (*State-Building*, 2004) articulate, failed states exhibit an inability to deliver fundamental political goods—foremost among them human security, legal order, and core infrastructural services.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 030-failed-state.md")

def remediate_040():
    fpath = os.path.join(MOD_DIR, "040-media-politics.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Analyzes the impact of digital and alternative media on international politics and mass mobilization, debating techno-utopian \'liberation technology\' narratives against cyber-skepticism and authoritarian digital surveillance."',
        content
    )

    # Ground Morozov (2011), Diamond (2010), Gladwell (2010)
    content = content.replace(
        '## Cyber-enthusiasts vs Skeptics',
        '## Liberation Technology vs Cyber-Skepticism'
    )
    content = content.replace(
        'However, experts debate the actual impact of social media on these protests.',
        'However, scholarly debate divides sharply between proponents of "liberation technology" (Larry Diamond, 2010) who argue networked tools democratize collective action, and cyber-skeptics (Evgeny Morozov in *The Net Delusion*, 2011; Malcolm Gladwell, 2010) who argue digital tools foster slacktivism while empowering authoritarian regimes with advanced surveillance and propaganda capabilities.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 040-media-politics.md")

def remediate_050():
    fpath = os.path.join(MOD_DIR, "050-cyber-warfare.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Analyzes the dynamics of cyber warfare and statecraft—evaluating the attribution problem, critical infrastructure vulnerabilities, offensive-defensive balance, cyber deterrence, and international legal norms under the Tallinn Manual 2.0."',
        content
    )

    # Ground Thomas Rid (2013), Tallinn Manual 2.0 (2017)
    content = content.replace(
        'The lack of ethical norms and rules of engagement in cyberspace makes the damage from cyber wars unpredictable.',
        'To establish normative and legal boundaries in this contested domain, international legal scholars formulated the *Tallinn Manual 2.0 on the International Law Applicable to Cyber Operations* (Schmitt, 2017), analyzing how existing international law (including the UN Charter Article 2(4) and international humanitarian law) governs state-sponsored cyber operations.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 050-cyber-warfare.md")

def remediate_060():
    fpath = os.path.join(MOD_DIR, "060-multiculturalism.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Evaluates the politics of multiculturalism and Samuel Huntington\'s \'Clash of Civilizations\' thesis, contrasting essentialist cultural fault-line arguments with hybridity, cosmopolitanism, and critical post-colonial critiques."',
        content
    )

    # Ground Huntington (1993, 1996), Said (2001), Sen (2006)
    content = content.replace(
        'Critics argued his categories were too simplistic and ignored the dynamic nature of culture and internal differences within civilizations.',
        'Prominent scholars vehemently contested Huntington\'s thesis. Edward Said (2001, "The Clash of Ignorance") criticized Huntington\'s essentialist reduction of complex, diverse cultures into rigid civilizational caricatures. Similarly, Nobel laureate Amartya Sen (*Identity and Violence*, 2006) argued that Huntington falls into a dangerous "solitarist" trap, ignoring the plural identities and cross-cultural hybridity that historically unite humanity.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 060-multiculturalism.md")

def remediate_070():
    fpath = os.path.join(MOD_DIR, "070-populism.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines contemporary political populism as an ideational phenomenon, analyzing Cas Mudde\'s thin-centered ideology framework, left-wing versus right-wing manifestations, and its disruptive impact on multilateral diplomacy and liberal international order."',
        content
    )

    # Clean double dash artifact line 135
    content = re.sub(r'\n--\s*\n\s*---\s*\n', '\n---\n', content)

    # Ground Cas Mudde (2004, 2017), Jan-Werner Müller (2016)
    content = content.replace(
        'So in summary, populism denotes a set of political beliefs, attitudes, and rhetorical techniques that separates "the people" from "the elite" and calls for the will of the masses to be translated directly into policy.',
        'In political science, Cas Mudde (2004, "The Populist Zeitgeist") authoritatively conceptualizes populism as a "thin-centered ideology" that considers society to be ultimately separated into two homogeneous and antagonistic camps: "the pure people" versus "the corrupt elite," arguing that politics should be an expression of the *volonté générale* (general will). As Jan-Werner Müller (*What Is Populism?*, 2016) further highlights, populists inherently make a moralistic, anti-pluralist claim to exclusive representation of the "authentic people."'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 070-populism.md")

def remediate_080():
    fpath = os.path.join(MOD_DIR, "080-natural-disaster.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines the intersection of natural catastrophes and global politics (\'disaster diplomacy\'), analyzing post-disaster political spaces, critical junctures, and the 2004 Indian Ocean Tsunami as a catalyst for the Aceh Peace Agreement (Helsinki MoU 2005)."',
        content
    )

    # Ground Ilan Kelman (2012 Disaster Diplomacy) and Helsinki MoU 2005
    content = content.replace(
        'This materials examines the complex relationship between **natural disasters** and politics,',
        'This field of inquiry, formalized as "disaster diplomacy" by scholars like Ilan Kelman (*Disaster Diplomacy*, 2012), investigates how disaster response catalysts international cooperation or escalates political conflict.'
    )
    content = content.replace(
        'The tsunami disaster became Aceh\'s road to peace and reconstruction.',
        'The tsunami disaster catalyzed the historic Helsinki Memorandum of Understanding (MoU) signed on August 15, 2005, between the Government of Indonesia and the Free Aceh Movement (GAM)—mediated by former Finnish President Martti Ahtisaari and the Crisis Management Initiative (CMI)—demonstrating how catastrophic exogenous shocks can create transformative windows of opportunity for conflict resolution.'
    )

    content = clean_duplicate_dividers(content)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 080-natural-disaster.md")

if __name__ == "__main__":
    remediate_010()
    remediate_020()
    remediate_030()
    remediate_040()
    remediate_050()
    remediate_060()
    remediate_070()
    remediate_080()
    print("Module 034 remediation completed successfully!")
