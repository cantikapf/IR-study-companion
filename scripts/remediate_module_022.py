"""
Surgical Remediation Script for Module 022: Introduction to Security Studies
Cleans duplicate dividers, elevates childish pillow-fort summaries, removes AI clichés,
and grounds theoretical concepts in canonical peer-reviewed literature.
"""

import os
import re

MOD_DIR = os.path.join("_chapters", "022-introduction-to-security-studies")

def clean_duplicate_dividers(text):
    # Matches multiple horizontal rules with whitespace/newlines in between
    cleaned = re.sub(r'---\s*\n\s*---\s*\n', '---\n', text)
    cleaned = re.sub(r'---\s*\n\s*\n\s*---\s*\n', '---\n', cleaned)
    cleaned = re.sub(r'---\s*\n\s*---\s*', '---\n', cleaned)
    return cleaned

def remediate_010():
    fpath = os.path.join(MOD_DIR, "010-intro-security.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter summary
    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines the conceptual evolution of International Security Studies (ISS)—from traditional Cold War military statecraft and national defense to post-Cold War human, environmental, and global security frameworks."',
        content
    )

    # Academic grounding in intro
    intro_old = """**Security** has been a heavily debated concept within **International Security Studies** (ISS), evolving significantly from its origins in post-World War II discussions on protecting states and societies from external and internal dangers. At its core, security encompasses the preservation of core values and freedom from threats for individuals, groups, and nations. However, there remains substantial disagreement within ISS on the primary focus and scope of security, whether it should center on safeguarding individual citizens, nation-states, the international system, or an emerging global society."""
    intro_new = """**Security** has been a heavily debated concept within **International Security Studies** (ISS), evolving significantly from its origins in post-World War II strategic studies to contemporary multidimensional frameworks. As Arnold Wolfers classically observed in 1952, security operates as an "ambiguous symbol" that may not have any precise meaning without specifying whose values are being preserved and against which threats. At its core, security encompasses the preservation of core values and freedom from existential threats for referent objects—whether individuals, social groups, sovereign states, or the global ecosystem. However, fundamental debates persist within ISS regarding the primary referent and scope of security, specifically whether analysis should prioritize state survival, regional stability, or global human welfare. Barry Buzan's seminal work *People, States and Fear* (1983) systematically expanded this agenda by demonstrating that security dynamics operate across five distinct yet interconnected sectors: military, political, economic, societal, and environmental."""
    if intro_old in content:
        content = content.replace(intro_old, intro_new)

    # Clean dividers
    content = clean_duplicate_dividers(content)

    # Refine flashcards and quiz
    fc_old = '{% include flashcards.html term1="National Security" def1="Protection of a nation-state from external and internal threats" term2="Global Security" def2="Security threats that affect the entire world, beyond national borders" term3="Human Security" def3="Focus on protecting individuals from threats to their safety and dignity" term4="Realism" def4="Theoretical perspective emphasizing state power and military capabilities" %}'
    fc_new = '{% include flashcards.html term1="National Security" def1="State-centric defense prioritizing survival against external and internal military threats" term2="Global Security" def2="Cooperative frameworks addressing planetary threats to the global commons" term3="Human Security" def3="People-centered approach prioritizing individual freedom from fear and freedom from want" term4="Realism" def4="Theoretical paradigm emphasizing state survival, self-help, and military power" %}'
    if fc_old in content:
        content = content.replace(fc_old, fc_new)

    quiz_old = '{% include quiz.html id="quiz_010_intro_security" question="What is the primary focus of security studies in the context of International Relations?" opt1="Protecting the interests of a particular nation-state" opt2="Addressing global security threats that affect the entire world" opt3="Promoting international cooperation and collective security" opt4="Emancipating individuals from threats to their safety and dignity" correct="2" %}'
    quiz_new = '{% include quiz.html id="quiz_010_intro_security" question="How did the conceptual scope of International Security Studies (ISS) primarily evolve following the Cold War?" opt1="It narrowed strictly to superpower nuclear deterrence postures" opt2="It expanded beyond state-centric military defense to incorporate environmental, economic, and human security dimensions" opt3="It dissolved the concept of state sovereignty in favor of direct world governance" opt4="It eliminated military strategy entirely from the security agenda" correct="2" %}'
    if quiz_old in content:
        content = content.replace(quiz_old, quiz_new)

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 010-intro-security.md")

def remediate_020():
    fpath = os.path.join(MOD_DIR, "020-realism-security.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Analyzes realist approaches to security studies, contrasting classical realism\'s human nature focus with structural realism (defensive vs. offensive), rise-and-fall hegemonic transitions, and neoclassical intervening domestic variables."',
        content
    )

    # Clean malformed bold
    content = content.replace("**international** relations", "**international relations**")

    # Clean dividers
    content = clean_duplicate_dividers(content)

    # Ground Waltz 1979 and Mearsheimer 2001
    content = content.replace(
        'Kenneth Waltz in his book "Theory of International Politics"',
        'Kenneth Waltz in his seminal book *Theory of International Politics* (1979)'
    )
    content = content.replace(
        'Hans Morgenthau\'s 1948 book "Politics Among Nations,"',
        'Hans Morgenthau\'s 1948 book *Politics Among Nations: The Struggle for Power and Peace*,'
    )
    content = content.replace(
        'Offensive realism, represented by John Mearsheimer, contends',
        'Offensive realism, advanced by John Mearsheimer in *The Tragedy of Great Power Politics* (2001), contends'
    )
    content = content.replace(
        'Stephen Walt\'s "balance of threat" theory,',
        'Stephen Walt\'s balance of threat theory (*The Origins of Alliances*, 1987),'
    )
    content = content.replace(
        'focusing on an offense-defense balance.',
        'elaborating Robert Jervis\'s (1978) offense-defense balance.'
    )
    content = content.replace(
        'Neoclassical realism asserts that systemic pressures',
        'Neoclassical realism, coined by Gideon Rose (1998), asserts that systemic pressures'
    )

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 020-realism-security.md")

def remediate_030():
    fpath = os.path.join(MOD_DIR, "030-liberalism-security.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines liberal paradigms in security studies, articulating the Kantian tripod of peace: republican constitutionalism (Democratic Peace), commercial interdependence, and international institutions (Neoliberal Institutionalism)."',
        content
    )

    content = clean_duplicate_dividers(content)

    # Ground Kant 1795, Doyle 1983, Russett 1993, Keohane 1984
    content = content.replace(
        'Traditional liberalism emerged in the 17th and 18th centuries during the Age of Enlightenment. Key thinkers such as John Locke, Adam Smith, and Immanuel Kant',
        'Traditional liberalism in security studies traces its philosophical foundation to the Enlightenment, notably Immanuel Kant\'s 1795 philosophical sketch *Perpetual Peace: A Philosophical Sketch* (*Zum ewigen Frieden*), alongside the political and economic writings of John Locke and Adam Smith'
    )
    content = content.replace(
        'The Democratic Peace Theory posits that democratic regimes',
        'The Democratic Peace Theory—systematized empirically by Michael Doyle (1983) and Bruce Russett (1993)—posits that democratic regimes'
    )
    content = content.replace(
        "- Liberal democratic states do not fight war against other liberal democratic states. that's why democratic states spread democratic liberal ideology to other states",
        "- Dyadic Democratic Peace: While democracies are historically just as war-prone as non-democracies in general, they exhibit an exceptionally robust empirical record of mutual non-belligerence toward other established constitutional democracies (Doyle, 1983)."
    )
    content = content.replace(
        'Neoliberal institutionalism argues that international institutions',
        'Neoliberal institutionalism, formulated by Robert Keohane in *After Hegemony* (1984) and extended to security by Celeste Wallander and Robert Keohane (1999),'
    )

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 030-liberalism-security.md")

def remediate_040():
    fpath = os.path.join(MOD_DIR, "040-constructivism-others.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Explores constructivist and critical security paradigms, highlighting social construction and intersubjectivity, the Copenhagen School\'s securitization framework, the Welsh School\'s emancipatory critique, and feminist security studies."',
        content
    )

    content = clean_duplicate_dividers(content)

    # Heading typo
    content = content.replace('# Contructivism', '# Constructivism')

    # Cliché fix
    content = content.replace("De Wilde's research delved into environmental security", "De Wilde's scholarship analyzed environmental security")

    # Ground Alexander Wendt (1992, 1999)
    content = content.replace(
        'Constructivism is an influential theoretical approach in **international relations** that emerged in the 1980s and 1990s.',
        'Constructivism is an influential theoretical approach in **international relations** pioneered by Nicholas Onuf (1989) and Alexander Wendt (1992, 1999).'
    )
    # Ground Cynthia Enloe & J. Ann Tickner
    content = content.replace(
        'Feminist perspectives in security studies have challenged patriarchal assumptions',
        'Feminist security studies, developed by scholars such as J. Ann Tickner (*Gender in International Relations*, 1992) and Cynthia Enloe (*Bananas, Beaches and Bases*, 1989), challenge patriarchal assumptions'
    )
    # Ground Welsh School
    content = content.replace(
        'The **Welsh School** of Critical Security Studies',
        'The **Welsh School** (or Aberystwyth School) of Critical Security Studies, founded by Ken Booth and Richard Wyn Jones,'
    )

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 040-constructivism-others.md")

def remediate_050():
    fpath = os.path.join(MOD_DIR, "050-institution-security.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Analyzes international security institutions across regional and global levels, distinguishing collective defense (alliances) from collective security (UN Charter Chapter VII), arms control regimes (NPT), and the regulation of Private Military and Security Companies (PMSCs)."',
        content
    )

    content = clean_duplicate_dividers(content)

    # Ground Inis Claude (1962), UN Charter Chapter VII
    content = content.replace(
        'Alliances is a formal or informal relationship',
        'An alliance is a formal or informal relationship'
    )
    content = content.replace(
        'The United Nations was founded in 1945 with the aim of maintaining international peace and security.',
        'The United Nations was founded in 1945 as a global collective security organization under its Charter, distinguishing itself from balance-of-power alliances (Inis Claude, *Swords into Plowshares*, 1962).'
    )
    # Ground Montreux Document 2008
    content = content.replace(
        'The private security industry has grown substantially',
        'The private military and security industry has grown substantially since the end of the Cold War, prompting international regulatory initiatives such as the 2008 Montreux Document on pertinent international legal obligations for private military and security companies (PMSCs).'
    )

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 050-institution-security.md")

def remediate_060():
    fpath = os.path.join(MOD_DIR, "060-peace-operations.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines the evolution of UN peace operations from traditional Chapter VI peacekeeping to robust Chapter VII peace enforcement, multidimensional peacebuilding, the Brahimi Report (2000), and the Responsibility to Protect (R2P) doctrine."',
        content
    )

    content = clean_duplicate_dividers(content)

    # Ground UN Charter Chapter VI & VII, Boutros-Ghali 1992 Agenda for Peace, Brahimi 2000 Report
    content = content.replace(
        '**Peace operations** encompass conflict prevention, peacemaking, peacekeeping, peace enforcement, and peacebuilding.',
        '**Peace operations** encompass conflict prevention, peacemaking, peacekeeping, peace enforcement, and peacebuilding—first comprehensively codified in UN Secretary-General Boutros Boutros-Ghali\'s landmark report *An Agenda for Peace* (1992).'
    )
    content = content.replace(
        'Lakhdar Brahimi (2000)\n\t- Impartial defense, flexibility, robustness',
        'Lakhdar Brahimi (2000 Report of the Panel on UN Peace Operations, A/55/305)\n\t- Operational doctrine of robust peacekeeping, realistic mandates, and clear rules of engagement'
    )
    content = content.replace(
        'The Responsibility to Protect (R2P) is a global political commitment to prevent genocide, war crimes, ethnic cleansing, and crimes against humanity. R2P involves three pillars:',
        'The Responsibility to Protect (R2P), formulated by the International Commission on Intervention and State Sovereignty (ICISS, 2001) and unanimously endorsed at the 2005 UN World Summit (Resolution A/RES/60/1, paras 138–139), rests upon three non-sequential pillars:'
    )

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 060-peace-operations.md")

def remediate_070():
    fpath = os.path.join(MOD_DIR, "070-crime-terrorism-insurgency.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines non-state asymmetric security threats—transnational organized crime (TOC), the four historical waves of modern terrorism, and classical versus contemporary counterinsurgency (COIN) doctrines."',
        content
    )

    content = clean_duplicate_dividers(content)

    # Ground UNTOC Palermo 2000
    content = content.replace(
        'Transnational **organized crime** (**TOC**) involves illegal activities coordinated across national borders,',
        'Transnational **organized crime** (**TOC**), formally defined under the 2000 United Nations Convention against Transnational Organized Crime (Palermo Convention), involves structured illicit activities conducted across national jurisdictions,'
    )
    # Ground David Rapoport 2002 Four Waves of Modern Terrorism
    content = content.replace(
        'Some prominent historical examples of terrorism include:',
        'David C. Rapoport (2002, "The Four Waves of Modern Terrorism") conceptualizes modern international terrorism across four successive cyclical waves:'
    )
    # Ground David Galula 1964 and General Charles Krulak 1999
    content = content.replace(
        'The concept of the "strategic corporal" highlights the impact individual soldiers can have,',
        'General Charles Krulak (1999, "The Strategic Corporal: Leadership in the Three Block War") highlighted how tactical actions by individual front-line soldiers can immediately generate strategic political ramifications,'
    )

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 070-crime-terrorism-insurgency.md")

def remediate_080():
    fpath = os.path.join(MOD_DIR, "080-energy-security.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Analyzes the geopolitics of energy security, evaluating chokepoint vulnerabilities (Hormuz, Malacca), supply-chain risks, producer-consumer dependency dynamics, and the strategic transition to renewable energy."',
        content
    )

    content = clean_duplicate_dividers(content)

    # Ground Daniel Yergin 2006, IEA 4As framework, maritime chokepoints
    content = content.replace(
        '**Energy** security involves having access to reliable, affordable, and sustainable energy resources. It ensures that economies and societies have the energy they need to function properly.',
        '**Energy security**, as formulated by the International Energy Agency (IEA) and scholar Daniel Yergin (2006, "Ensuring Energy Security"), is defined as the uninterrupted availability of energy sources at an affordable price, encompassing the "4As" framework: Availability, Accessibility, Affordability, and Acceptability (environmental sustainability).'
    )
    content = content.replace(
        'securing key maritime chokepoints.',
        'securing critical maritime chokepoints such as the Strait of Hormuz (transiting ~20% of global petroleum liquids), the Strait of Malacca, Bab el-Mandeb, and the Suez Canal.'
    )

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 080-energy-security.md")

def remediate_090():
    fpath = os.path.join(MOD_DIR, "090-human-security.md")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'simple_summary:\s*"[^"]+"',
        'simple_summary: "Examines the human security paradigm introduced by the 1994 UNDP Human Development Report, analyzing its 7 essential dimensions, freedom from fear versus freedom from want, and the poverty-health-migration nexus."',
        content
    )

    content = clean_duplicate_dividers(content)

    # Ground Mahbub ul Haq, Amartya Sen, 7 dimensions of human security
    content = content.replace(
        'The concept of human security first gained prominence in the 1994 United Nations Development Programme (UNDP) Human Development Report, which argued that ensuring "freedom from want" and "freedom from fear" should be the foundations of human security.',
        'The concept of human security first gained institutional prominence in the landmark 1994 United Nations Development Programme (UNDP) Human Development Report, conceived under the intellectual leadership of Mahbub ul Haq and Amartya Sen. The report articulated two core pillars—"freedom from fear" and "freedom from want"—and defined human security across seven interconnected dimensions: economic, food, health, environmental, personal, community, and political security.'
    )

    with open(fpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("Remediated 090-human-security.md")

if __name__ == "__main__":
    remediate_010()
    remediate_020()
    remediate_030()
    remediate_040()
    remediate_050()
    remediate_060()
    remediate_070()
    remediate_080()
    remediate_090()
    print("Module 022 remediation completed successfully!")
