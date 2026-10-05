"""
Build a deeply curated academic glossary of 120+ fundamental International Relations concepts.
Includes formal definition, key scholars, theoretical school, and relevant module cross-links.
"""

import json
from pathlib import Path

def create_curated_glossary():
    terms = [
        # --- Theories & Epistemology ---
        {
            "term": "Anarchy",
            "category": "Theory & Epistemology",
            "scholars": "Thomas Hobbes, Kenneth Waltz, Hedley Bull",
            "definition": "The ordering principle of the international system characterized by the absence of a central, overarching government or hierarchical authority with legitimate monopoly over the use of force.",
            "module": "010",
            "chapter_slug": "study-of-international-relations"
        },
        {
            "term": "Balance of Power",
            "category": "Theory & Epistemology",
            "scholars": "Hans Morgenthau, Kenneth Waltz",
            "definition": "A systemic mechanism wherein states form alliances or expand internal military armaments to prevent any single state or coalition from achieving preponderant hegemony.",
            "module": "023",
            "chapter_slug": "realism-in-ir"
        },
        {
            "term": "Classical Realism",
            "category": "Theory & Epistemology",
            "scholars": "Thucydides, Niccolò Machiavelli, Hans Morgenthau",
            "definition": "An IR paradigm locating the root causes of conflict, war, and power competition in the inherently flawed, power-seeking nature of human beings (animus dominandi).",
            "module": "023",
            "chapter_slug": "classical-realism"
        },
        {
            "term": "Structural Realism (Neorealism)",
            "category": "Theory & Epistemology",
            "scholars": "Kenneth Waltz, John Mearsheimer",
            "definition": "A systemic theory asserting that the anarchic structure of the international system, rather than human nature, compels states to compete for power and prioritize survival.",
            "module": "023",
            "chapter_slug": "neorealism-structural-realism"
        },
        {
            "term": "Offensive Realism",
            "category": "Theory & Epistemology",
            "scholars": "John Mearsheimer",
            "definition": "A structural realist variant arguing that because states can never be certain of others' intentions, rational great powers seek to maximize relative power and attain regional hegemony.",
            "module": "023",
            "chapter_slug": "offensive-vs-defensive-realism"
        },
        {
            "term": "Defensive Realism",
            "category": "Theory & Epistemology",
            "scholars": "Robert Jervis, Stephen Walt, Charles Glaser",
            "definition": "A structural realist variant arguing that the international system incentivizes states to maintain moderate, status-quo balances of power, as aggressive expansion provokes counter-balancing coalitions.",
            "module": "023",
            "chapter_slug": "offensive-vs-defensive-realism"
        },
        {
            "term": "Neoliberal Institutionalism",
            "category": "Theory & Epistemology",
            "scholars": "Robert Keohane, Joseph Nye",
            "definition": "A rationalist perspective demonstrating that even under structural anarchy, international institutions foster durable cooperation by reducing transaction costs, sharing information, and mitigating cheating.",
            "module": "023",
            "chapter_slug": "neoliberal-institutionalism"
        },
        {
            "term": "Social Constructivism",
            "category": "Theory & Epistemology",
            "scholars": "Alexander Wendt, Nicholas Onuf, Martha Finnemore",
            "definition": "A social theory of world politics emphasizing that fundamental aspects of international relations are socially constructed through shared ideas, intersubjective norms, and collective identities rather than material forces alone.",
            "module": "023",
            "chapter_slug": "constructivism-in-ir"
        },
        {
            "term": "English School (International Society)",
            "category": "Theory & Epistemology",
            "scholars": "Hedley Bull, Martin Wight, Barry Buzan",
            "definition": "A theoretical tradition positing that sovereign states form an 'anarchical society' bound by shared norms, diplomatic institutions, conventions, and international law.",
            "module": "023",
            "chapter_slug": "english-school-ir"
        },
        {
            "term": "Critical Theory",
            "category": "Theory & Epistemology",
            "scholars": "Robert W. Cox, Jürgen Habermas, Max Horkheimer",
            "definition": "A dialectical approach that interrogates the historical origins, ideological biases, and power hierarchies embedded in social institutions, aiming at human emancipation rather than mere status-quo problem-solving.",
            "module": "023",
            "chapter_slug": "critical-theory-ir"
        },
        {
            "term": "Feminist International Relations",
            "category": "Theory & Epistemology",
            "scholars": "J. Ann Tickner, Cynthia Enloe",
            "definition": "A critical framework examining how gendered assumptions and hierarchies shape international politics, security doctrines, diplomacy, and global political economy.",
            "module": "023",
            "chapter_slug": "feminist-ir-theory"
        },
        {
            "term": "Postcolonialism",
            "category": "Theory & Epistemology",
            "scholars": "Edward Said, Gayatri Spivak, Frantz Fanon",
            "definition": "A critical perspective interrogating Eurocentric epistemologies and revealing how colonial power relations, racial hierarchies, and imperial legacies continue to structure the contemporary global order.",
            "module": "023",
            "chapter_slug": "postcolonial-approaches"
        },
        {
            "term": "Positivism",
            "category": "Theory & Epistemology",
            "scholars": "Auguste Comte, Karl Popper",
            "definition": "An epistemology asserting that social science can discover objective causal laws governing human behavior through empirical observation, hypothesis falsification, and quantitative measurement.",
            "module": "011",
            "chapter_slug": "social-science-concept"
        },
        {
            "term": "Interpretivism",
            "category": "Theory & Epistemology",
            "scholars": "Max Weber, Clifford Geertz",
            "definition": "An epistemological approach arguing that social reality cannot be explained through natural-science laws, but requires understanding (Verstehen) of subjective meanings, cultural contexts, and human intentions.",
            "module": "011",
            "chapter_slug": "epistemology-social-science"
        },
        {
            "term": "Levels of Analysis",
            "category": "Theory & Epistemology",
            "scholars": "Kenneth Waltz, J. David Singer",
            "definition": "A methodological framework categorizing explanations of international events into three distinct levels: individual (first image), domestic state/society (second image), and international system (third image).",
            "module": "010",
            "chapter_slug": "levels-of-analysis-ir"
        },
        {
            "term": "Prisoner's Dilemma",
            "category": "Theory & Epistemology",
            "scholars": "Albert Tucker, Robert Axelrod",
            "definition": "A fundamental game-theoretic model where two rational actors, unable to communicate or enforce contracts, find mutual defection to be the dominant Nash Equilibrium despite mutual cooperation yielding a Pareto-superior payoff.",
            "module": "023",
            "chapter_slug": "game-theory-ir"
        },

        # --- International Security & Strategy ---
        {
            "term": "Security Dilemma",
            "category": "Security & Strategy",
            "scholars": "John Herz, Robert Jervis, Herbert Butterfield",
            "definition": "A structural dynamic wherein one state's defensive efforts to enhance its security inadvertently make neighboring states feel less secure, prompting counter-measures that result in a mutual, heightened spiral of insecurity.",
            "module": "022",
            "chapter_slug": "realism-security"
        },
        {
            "term": "Mutual Assured Destruction (MAD)",
            "category": "Security & Strategy",
            "scholars": "Bernard Brodie, Thomas Schelling, Robert McNamara",
            "definition": "A condition of strategic stability where two nuclear-armed adversaries both possess secure, survivable second-strike capabilities, ensuring that any nuclear aggression results in the total destruction of both sides.",
            "module": "022",
            "chapter_slug": "deterrence-theory"
        },
        {
            "term": "Securitization",
            "category": "Security & Strategy",
            "scholars": "Barry Buzan, Ole Wæver, Jaap de Wilde (Copenhagen School)",
            "definition": "A discursive speech act through which an actor frames an issue as an existential threat to a designated referent object, legitimizing emergency measures outside normal political procedures.",
            "module": "022",
            "chapter_slug": "securitization-theory"
        },
        {
            "term": "Human Security",
            "category": "Security & Strategy",
            "scholars": "Mahbub ul Haq, Amartya Sen (UNDP 1994)",
            "definition": "A paradigm broadening the referent object of security from the territorial state to the individual human being, focusing on freedom from fear, freedom from want, and freedom to live in dignity.",
            "module": "022",
            "chapter_slug": "human-security"
        },
        {
            "term": "Democratic Peace Theory",
            "category": "Security & Strategy",
            "scholars": "Immanuel Kant, Michael Doyle, Bruce Russett",
            "definition": "The empirical and theoretical proposition that while democracies frequently fight autocratic states, consolidated liberal democracies rarely, if ever, go to war against one another.",
            "module": "022",
            "chapter_slug": "democratic-peace-theory"
        },
        {
            "term": "Offense-Defense Balance",
            "category": "Security & Strategy",
            "scholars": "Robert Jervis, Stephen Van Evera",
            "definition": "A strategic condition assessing whether military technology, geography, and doctrine make it easier to attack and conquer territory or to defend against invasion.",
            "module": "022",
            "chapter_slug": "offense-defense-theory"
        },
        {
            "term": "Deterrence",
            "category": "Security & Strategy",
            "scholars": "Thomas Schelling, Glenn Snyder",
            "definition": "The persuasion of a potential adversary that the expected costs, risks, and retaliation of an aggressive action will far outweigh any anticipated gains.",
            "module": "022",
            "chapter_slug": "deterrence-theory"
        },
        {
            "term": "Compellence",
            "category": "Security & Strategy",
            "scholars": "Thomas Schelling",
            "definition": "The threat or limited application of military force designed to persuade an adversary to halt or reverse an action already initiated.",
            "module": "032",
            "chapter_slug": "tools-diplomacy"
        },
        {
            "term": "Asymmetric Warfare",
            "category": "Security & Strategy",
            "scholars": "Mao Zedong, Ivan Arreguín-Toft",
            "definition": "Conflict between belligerents whose relative military power, resources, and strategic doctrines differ drastically, typically pitting conventional state armed forces against insurgent or guerrilla networks.",
            "module": "022",
            "chapter_slug": "asymmetric-warfare"
        },
        {
            "term": "Hybrid Warfare",
            "category": "Security & Strategy",
            "scholars": "Frank Hoffman, Valery Gerasimov",
            "definition": "A military strategy blending conventional military capabilities, irregular tactics, cyber operations, disinformation, and economic coercion beneath the threshold of open interstate warfare.",
            "module": "034",
            "chapter_slug": "cyber-warfare"
        },
        {
            "term": "Responsibility to Protect (R2P)",
            "category": "Security & Strategy",
            "scholars": "Gareth Evans, Mohamed Sahnoun, ICISS (2001)",
            "definition": "An international political commitment endorsed at the 2005 UN World Summit recognizing sovereign states' duty to protect populations from genocide, war crimes, ethnic cleansing, and crimes against humanity, with international community responsibility when states fail.",
            "module": "042",
            "chapter_slug": "humanitarian-intervention-r2p"
        },
        {
            "term": "Nuclear Non-Proliferation Treaty (NPT)",
            "category": "Security & Strategy",
            "scholars": "UN General Assembly (1968)",
            "definition": "A landmark international treaty establishing a three-pillar regime: preventing the spread of nuclear weapons, promoting nuclear disarmament, and fostering peaceful civilian nuclear energy cooperation.",
            "module": "034",
            "chapter_slug": "nuclear-proliferation"
        },

        # --- International Political Economy (IPE) ---
        {
            "term": "Mercantilism",
            "category": "Political Economy",
            "scholars": "Alexander Hamilton, Friedrich List",
            "definition": "An economic doctrine holding that state power and national security depend upon the accumulation of wealth, trade surpluses, and state intervention to support strategic industries.",
            "module": "021",
            "chapter_slug": "introduction-ipe"
        },
        {
            "term": "Comparative Advantage",
            "category": "Political Economy",
            "scholars": "David Ricardo",
            "definition": "An economic principle demonstrating that nations mutually gain from international trade when each specializes in producing goods for which it incurs the lowest domestic opportunity cost.",
            "module": "021",
            "chapter_slug": "classical-ipe"
        },
        {
            "term": "Hegemonic Stability Theory",
            "category": "Political Economy",
            "scholars": "Charles Kindleberger, Robert Gilpin, Stephen Krasner",
            "definition": "The proposition that an open, stable liberal international economic order requires the leadership of a single dominant hegemonic state to enforce rules, provide market liquidity, and serve as lender of last resort.",
            "module": "021",
            "chapter_slug": "hegemonic-stability-theory"
        },
        {
            "term": "Embedded Liberalism",
            "category": "Political Economy",
            "scholars": "John Gerard Ruggie",
            "definition": "The post-WWII economic compromise reconciling international multilateral free trade with domestic state welfare, full employment policies, and capital controls.",
            "module": "021",
            "chapter_slug": "bretton-woods-system"
        },
        {
            "term": "Triffin Dilemma",
            "category": "Political Economy",
            "scholars": "Robert Triffin",
            "definition": "The economic contradiction wherein a country whose national currency serves as the primary global reserve asset must run continuous balance-of-payments deficits to supply world liquidity, which over time erodes confidence in the currency.",
            "module": "021",
            "chapter_slug": "monetary-system"
        },
        {
            "term": "Washington Consensus",
            "category": "Political Economy",
            "scholars": "John Williamson (1989)",
            "definition": "A standard set of ten neoliberal policy prescriptions promoted by the IMF, World Bank, and US Treasury for developing nations, emphasizing fiscal discipline, privatization, trade liberalization, and deregulation.",
            "module": "043",
            "chapter_slug": "washington-consensus"
        },
        {
            "term": "Dependency Theory (Dependencia)",
            "category": "Political Economy",
            "scholars": "Raúl Prebisch, Fernando Henrique Cardoso, Andre Gunder Frank",
            "definition": "A structuralist school arguing that peripheral developing economies are systematically underdeveloped by an unequal global capitalist system that extracts surplus value to enrich the industrialized core.",
            "module": "043",
            "chapter_slug": "dependency-theory"
        },
        {
            "term": "Prebisch-Singer Thesis",
            "category": "Political Economy",
            "scholars": "Raúl Prebisch, Hans Singer",
            "definition": "The empirical observation that the terms of trade between primary agricultural/mineral commodities and manufactured capital goods systematically deteriorate over time against developing nations.",
            "module": "043",
            "chapter_slug": "study-of-development"
        },
        {
            "term": "Import Substitution Industrialization (ISI)",
            "category": "Political Economy",
            "scholars": "Raúl Prebisch, Celso Furtado",
            "definition": "A developmental trade policy seeking to replace foreign industrial imports with domestically manufactured goods through high protective tariffs, quotas, and state-subsidized credit.",
            "module": "043",
            "chapter_slug": "import-substitution-industrialization"
        },
        {
            "term": "Export-Oriented Industrialization (EOI)",
            "category": "Political Economy",
            "scholars": "Alice Amsden, Robert Wade",
            "definition": "A developmental strategy focusing on integrating domestic industries into competitive global export markets through strategic state industrial policy, used by East Asian Tiger economies.",
            "module": "043",
            "chapter_slug": "east-asian-miracle"
        },
        {
            "term": "World-Systems Theory",
            "category": "Political Economy",
            "scholars": "Immanuel Wallerstein",
            "definition": "A macro-historical perspective analyzing global capitalism as an integrated world-economy divided into an exploitative Core, a raw-material Periphery, and an intermediate stabilizing Semi-Periphery.",
            "module": "021",
            "chapter_slug": "marxism-world-systems"
        },
        {
            "term": "Most-Favoured-Nation (MFN)",
            "category": "Political Economy",
            "scholars": "GATT 1947 Article I, WTO",
            "definition": "A cornerstone principle of international trade law requiring that any commercial advantage, tariff concession, or privilege granted to one nation must immediately be extended to all other WTO member states.",
            "module": "050",
            "chapter_slug": "international-trade-as-diplomacy"
        },
        {
            "term": "National Treatment",
            "category": "Political Economy",
            "scholars": "GATT Article III, WTO",
            "definition": "A foundational trade norm prohibiting states from discriminating against imported foreign goods in favor of domestic products through internal taxes or domestic regulations once customs borders are crossed.",
            "module": "050",
            "chapter_slug": "wto-principles"
        },
        {
            "term": "Special Drawing Right (SDR)",
            "category": "Political Economy",
            "scholars": "International Monetary Fund (1969)",
            "definition": "An international supplementary reserve asset created by the IMF whose value is defined by a weighted basket of five major currencies: US Dollar, Euro, Chinese Renminbi, Japanese Yen, and British Pound.",
            "module": "046",
            "chapter_slug": "imf-governance"
        },

        # --- International Law & Institutions ---
        {
            "term": "Pacta Sunt Servanda",
            "category": "International Law",
            "scholars": "VCLT 1969 Article 26",
            "definition": "The fundamental maxim of public international law establishing that every treaty in force is legally binding upon the sovereign parties to it and must be performed by them in good faith.",
            "module": "042",
            "chapter_slug": "basic-inter-law"
        },
        {
            "term": "Jus Cogens (Peremptory Norm)",
            "category": "International Law",
            "scholars": "VCLT Article 53",
            "definition": "A fundamental body of overarching international legal norms accepted by the global community from which no derogation or treaty exception is permitted (e.g., prohibitions against genocide, slavery, torture, and wars of aggression).",
            "module": "042",
            "chapter_slug": "sources-international-law"
        },
        {
            "term": "Opinio Juris Sive Necessitatis",
            "category": "International Law",
            "scholars": "ICJ Statute Article 38(1)(b)",
            "definition": "The subjective, psychological conviction of sovereign states that a general behavioral practice is undertaken out of a binding sense of legal obligation, constituting a necessary component of customary international law.",
            "module": "042",
            "chapter_slug": "customary-international-law"
        },
        {
            "term": "Territorial Sea",
            "category": "International Law",
            "scholars": "UNCLOS 1982 Article 3",
            "definition": "A maritime zone extending up to 12 nautical miles from a coastal state's baseline, over which the state exercises full territorial sovereignty subject only to the right of innocent passage for foreign vessels.",
            "module": "042",
            "chapter_slug": "law-of-the-sea"
        },
        {
            "term": "Exclusive Economic Zone (EEZ)",
            "category": "International Law",
            "scholars": "UNCLOS 1982 Part V",
            "definition": "A maritime area extending up to 200 nautical miles from baselines in which the coastal state exercises sovereign rights over living and non-living natural resources while preserving high-seas navigation freedoms for all states.",
            "module": "042",
            "chapter_slug": "law-of-the-sea"
        },
        {
            "term": "Archipelagic State Principle",
            "category": "International Law",
            "scholars": "Djuanda Declaration (1957), UNCLOS Part IV",
            "definition": "The legal regime recognizing that an island-state constitutes an indivisible geographic entity, allowing the drawing of straight archipelagic baselines enclosing internal waters and archipelagic sealanes.",
            "module": "013",
            "chapter_slug": "basic-political"
        },
        {
            "term": "Innocent Passage",
            "category": "International Law",
            "scholars": "UNCLOS 1982 Article 17",
            "definition": "The right of foreign ships to navigate continuously and expeditiously through another state's territorial sea without prior authorization, provided the passage is not prejudicial to the peace, good order, or security of the coastal state.",
            "module": "042",
            "chapter_slug": "maritime-zones-unclos"
        },
        {
            "term": "Jus ad Bellum",
            "category": "International Law",
            "scholars": "UN Charter Article 2(4) & Article 51",
            "definition": "The branch of public international law establishing the criteria, conditions, and legal justifications governing when a sovereign state may legitimately resort to armed force.",
            "module": "042",
            "chapter_slug": "use-of-force-international-law"
        },
        {
            "term": "Jus in Bello (International Humanitarian Law)",
            "category": "International Law",
            "scholars": "Geneva Conventions 1949, Additional Protocols 1977",
            "definition": "The law of armed conflict regulating the conduct of warfare, mandating military necessity, distinction between combatants and non-combatants, proportionality, and humane treatment of prisoners of war.",
            "module": "042",
            "chapter_slug": "international-humanitarian-law"
        },
        {
            "term": "Persona Non Grata",
            "category": "International Law",
            "scholars": "Vienna Convention on Diplomatic Relations 1961 Article 9",
            "definition": "A formal diplomatic mechanism whereby a host state informs a sending state that an accredited diplomat is no longer welcome and must be recalled, without needing to justify its decision.",
            "module": "032",
            "chapter_slug": "intro-diplo"
        },

        # --- Diplomacy, Foreign Policy & Regionalism ---
        {
            "term": "Two-Level Games",
            "category": "Diplomacy & FPA",
            "scholars": "Robert Putnam (1988)",
            "definition": "A conceptual model analyzing international bargaining as simultaneously operating at Level I (international negotiations among diplomats) and Level II (domestic political bargaining required for legislative ratification).",
            "module": "033",
            "chapter_slug": "domestic-politics-fpdm"
        },
        {
            "term": "Bureaucratic Politics Model",
            "category": "Diplomacy & FPA",
            "scholars": "Graham Allison, Morton Halperin",
            "definition": "A foreign policy analysis model asserting that foreign policy decisions emerge not from unitary rational calculation, but from bargaining, turf battles, and compromises among competing government ministries and officials.",
            "module": "033",
            "chapter_slug": "models-fpdm"
        },
        {
            "term": "Groupthink",
            "category": "Diplomacy & FPA",
            "scholars": "Irving Janis (1972)",
            "definition": "A psychological phenomenon in cohesive decision-making groups where the desire for harmony and consensus overrides realistic appraisals of alternative courses of action, leading to catastrophic foreign policy errors.",
            "module": "033",
            "chapter_slug": "psychology-foreign-policy"
        },
        {
            "term": "Soft Power",
            "category": "Diplomacy & FPA",
            "scholars": "Joseph Nye (1990)",
            "definition": "The ability to influence the preferences and behavior of other states through co-optation and attraction—derived from a country's culture, political values, and perceived foreign policy legitimacy—rather than coercion or economic inducements.",
            "module": "032",
            "chapter_slug": "soft-power-diplomacy"
        },
        {
            "term": "Public Diplomacy",
            "category": "Diplomacy & FPA",
            "scholars": "Edward R. Murrow, Nicholas Cull",
            "definition": "Government communications and cultural engagement targeted directly at foreign publics to shape public opinion, foster long-term goodwill, and build international understanding.",
            "module": "032",
            "chapter_slug": "public-diplomacy"
        },
        {
            "term": "Track II Diplomacy",
            "category": "Diplomacy & FPA",
            "scholars": "Joseph Montville (1981)",
            "definition": "Unofficial, non-governmental, and informal dialogue between non-state actors (academics, retired officials, civil society leaders) designed to develop creative ideas, build mutual trust, and resolve conflicts.",
            "module": "032",
            "chapter_slug": "track-two-diplomacy"
        },
        {
            "term": "Politik Bebas-Aktif",
            "category": "Indonesian Diplomacy",
            "scholars": "Mohammad Hatta (1948)",
            "definition": "Indonesia's foundational foreign policy doctrine: 'Bebas' (independent from alignment with major power military blocs) and 'Aktif' (actively contributing to international peace and anti-colonial justice).",
            "module": "013",
            "chapter_slug": "basic-political"
        },
        {
            "term": "ASEAN Way",
            "category": "Regionalism & ASEAN",
            "scholars": "Bangkok Declaration 1967, Amitav Acharya",
            "definition": "A normative diplomatic code practiced in Southeast Asia emphasizing consensus decision-making (Musyawarah-Mufakat), non-interference in internal affairs, quiet diplomacy, and informal consultation.",
            "module": "044",
            "chapter_slug": "basic-regionalism"
        },
        {
            "term": "ASEAN Centrality",
            "category": "Regionalism & ASEAN",
            "scholars": "ASEAN Charter Article 1(15)",
            "definition": "The principle that ASEAN acts as the primary driving force and institutional convenor for wider Asia-Pacific and Indo-Pacific multilateral forums, including the ARF, ADMM-Plus, EAS, and RCEP.",
            "module": "044",
            "chapter_slug": "asean-centrality"
        },
        {
            "term": "ZOPFAN",
            "category": "Regionalism & ASEAN",
            "scholars": "Kuala Lumpur Declaration (1971)",
            "definition": "Zone of Peace, Freedom and Neutrality: an ASEAN initiative committing member states to keep Southeast Asia free from external great power interference, containment, and military rivalry.",
            "module": "044",
            "chapter_slug": "zopfan-treaty-amity"
        },
        {
            "term": "Strategic Chokepoint",
            "category": "Security & Strategy",
            "scholars": "Alfred Thayer Mahan, Julian Corbett",
            "definition": "A congested geographic maritime passage (such as the Strait of Malacca, Strait of Hormuz, or Suez Canal) crucial for international commerce whose disruption paralyzes global supply chains.",
            "module": "034",
            "chapter_slug": "maritime-security"
        },
        {
            "term": "Bandwagoning",
            "category": "Theory & Epistemology",
            "scholars": "Kenneth Waltz, Stephen Walt",
            "definition": "A foreign policy alignment strategy where a weaker state aligns with a stronger or threatening power to share the spoils of victory or avoid being attacked.",
            "module": "023",
            "chapter_slug": "realism-in-ir"
        },
        {
            "term": "Buck-Passing",
            "category": "Theory & Epistemology",
            "scholars": "John Mearsheimer, Barry Posen",
            "definition": "A strategic strategy in multipolar systems where a threatened great power attempts to shift the burden of confronting or checking an aggressor state onto another power.",
            "module": "023",
            "chapter_slug": "offensive-vs-defensive-realism"
        },
        {
            "term": "Chain-Ganging",
            "category": "Theory & Epistemology",
            "scholars": "Thomas Christensen, Jack Snyder",
            "definition": "A pathology of rigid multipolar alliance systems (exemplified in 1914) where unconditional defense commitments drag all allied states into war over the recklessness of a single minor partner.",
            "module": "012",
            "chapter_slug": "road-to-ww1"
        },
        {
            "term": "Bipolarity",
            "category": "Theory & Epistemology",
            "scholars": "Kenneth Waltz",
            "definition": "A structural distribution of power in the international system where two superpowers dominate systemic military, diplomatic, and ideological competition (exemplified by the US-Soviet Cold War).",
            "module": "010",
            "chapter_slug": "the-international-system"
        },
        {
            "term": "Multipolarity",
            "category": "Theory & Epistemology",
            "scholars": "Hans Morgenthau, Kenneth Waltz",
            "definition": "An international system characterized by three or more roughly equal great powers competing and forming fluid balance-of-power coalitions.",
            "module": "010",
            "chapter_slug": "the-international-system"
        },
        {
            "term": "Unipolarity",
            "category": "Theory & Epistemology",
            "scholars": "William Wohlforth, Nuno Monteiro",
            "definition": "A systemic structure wherein a single state possesses an overwhelming preponderance of military, economic, and institutional power with no peer competitor (the post-1991 US 'unipolar moment').",
            "module": "010",
            "chapter_slug": "the-international-system"
        },
        {
            "term": "Grand Strategy",
            "category": "Security & Strategy",
            "scholars": "Paul Kennedy, Barry Posen, John Lewis Gaddis",
            "definition": "The overarching, long-term conceptual theory and coordination of a nation-state's military, diplomatic, economic, and moral instruments of power to achieve vital national security objectives.",
            "module": "041",
            "chapter_slug": "history-fpa"
        },
        {
            "term": "Containment",
            "category": "Security & Strategy",
            "scholars": "George F. Kennan (1947)",
            "definition": "The grand strategy pursued by the United States during the Cold War to prevent the geopolitical and ideological expansion of the Soviet Union through a counter-force posture.",
            "module": "012",
            "chapter_slug": "cold-war-origins"
        },
        {
            "term": "First-Strike Capability",
            "category": "Security & Strategy",
            "scholars": "Herman Kahn, Albert Wohlstetter",
            "definition": "The capacity to launch a preemptive nuclear strike that completely destroys the adversary's nuclear retaliatory arsenal before they can respond.",
            "module": "022",
            "chapter_slug": "nuclear-strategy"
        },
        {
            "term": "Second-Strike Capability",
            "category": "Security & Strategy",
            "scholars": "Bernard Brodie, Thomas Schelling",
            "definition": "A state's guaranteed ability to absorb a full-scale surprise nuclear first strike and still deliver a devastating, unacceptable retaliatory counter-strike (the cornerstone of MAD).",
            "module": "022",
            "chapter_slug": "nuclear-strategy"
        },
        {
            "term": "Extended Deterrence",
            "category": "Security & Strategy",
            "scholars": "Thomas Schelling, Glenn Snyder",
            "definition": "A commitment by a nuclear-armed power to protect foreign allies under its 'nuclear umbrella', warning adversaries that an attack on the ally will be treated as an attack on the guarantor itself.",
            "module": "022",
            "chapter_slug": "alliances-deterrence"
        },
        {
            "term": "Brinkmanship",
            "category": "Security & Strategy",
            "scholars": "Thomas Schelling, John Foster Dulles",
            "definition": "A strategic competition where a state deliberately escalates a crisis to the very brink of disaster (e.g., nuclear war) to force the adversary to back down first (the logic of the game of Chicken).",
            "module": "022",
            "chapter_slug": "crisis-escalation"
        },
        {
            "term": "Audience Costs",
            "category": "Diplomacy & FPA",
            "scholars": "James Fearon (1994)",
            "definition": "The domestic political penalties that political leaders suffer from voters or elites if they escalate a public foreign crisis and subsequently back down or bluff.",
            "module": "033",
            "chapter_slug": "domestic-politics-fpdm"
        },
        {
            "term": "Shadow of the Future",
            "category": "Theory & Epistemology",
            "scholars": "Robert Axelrod, Robert Keohane",
            "definition": "The expectation that players will interact repeatedly over time, which significantly increases the cost of short-term cheating and makes cooperation self-enforcing in iterated games.",
            "module": "023",
            "chapter_slug": "game-theory-ir"
        },
        {
            "term": "Relative Gains",
            "category": "Theory & Epistemology",
            "scholars": "Joseph Grieco, Kenneth Waltz",
            "definition": "A realist perspective emphasizing how much a state gains in power or wealth in comparison to rivals ('Who will gain more?'), which frequently inhibits international cooperation.",
            "module": "023",
            "chapter_slug": "neorealism-structural-realism"
        },
        {
            "term": "Absolute Gains",
            "category": "Theory & Epistemology",
            "scholars": "Robert Keohane, Arthur Stein",
            "definition": "A liberal institutionalist perspective focusing on whether an outcome improves a state's own welfare regardless of how much other participants gain ('Do we both gain?').",
            "module": "023",
            "chapter_slug": "neoliberal-institutionalism"
        },
        {
            "term": "Collective Security",
            "category": "International Law",
            "scholars": "Woodrow Wilson, Inis Claude",
            "definition": "A systemic security architecture (embodied in the League of Nations and UN Charter) wherein all member states agree that an attack on any single member constitutes an attack on all, requiring collective enforcement.",
            "module": "045",
            "chapter_slug": "un-collective-security"
        },
        {
            "term": "Collective Defense",
            "category": "Security & Strategy",
            "scholars": "NATO Article 5",
            "definition": "A mutual defense pact where a specific group of allied states pledges to assist and defend one another against external, third-party aggression.",
            "module": "022",
            "chapter_slug": "nato-collective-defense"
        },
        {
            "term": "Universal Jurisdiction",
            "category": "International Law",
            "scholars": "Rome Statute, Geneva Conventions",
            "definition": "A legal principle allowing national courts of any state to prosecute individuals accused of international crimes of universal concern (genocide, piracy, war crimes) regardless of where the crime occurred or the nationality of the perpetrator.",
            "module": "042",
            "chapter_slug": "international-criminal-law"
        },
        {
            "term": "Rome Statute",
            "category": "International Law",
            "scholars": "United Nations (1998)",
            "definition": "The foundational multilateral treaty establishing the permanent International Criminal Court (ICC) at The Hague with jurisdiction over genocide, crimes against humanity, war crimes, and the crime of aggression.",
            "module": "042",
            "chapter_slug": "icc-dispute-settlement"
        },
        {
            "term": "State Immunity",
            "category": "International Law",
            "scholars": "UN Convention on Jurisdictional Immunities (2004)",
            "definition": "A core customary rule of international law providing that a sovereign state and its government property are shielded from the jurisdiction and lawsuits of foreign municipal courts (par in parem non habet imperium).",
            "module": "042",
            "chapter_slug": "state-immunity-jurisdiction"
        },
        {
            "term": "Transnational Advocacy Network (TAN)",
            "category": "Theory & Epistemology",
            "scholars": "Margaret Keck, Kathryn Sikkink (1998)",
            "definition": "Relevant actors working internationally on an issue who are bound together by shared values, dense information exchanges, and common discourses, leveraging the 'boomerang pattern' to press domestic governments.",
            "module": "010",
            "chapter_slug": "non-state-actors-ir"
        },
        {
            "term": "Epistemic Community",
            "category": "Theory & Epistemology",
            "scholars": "Peter M. Haas (1992)",
            "definition": "A network of recognized knowledge-based experts who share principled beliefs, causal methodologies, and common policy enterprises, helping states define interests under conditions of technical uncertainty.",
            "module": "031",
            "chapter_slug": "social-reserach-method"
        },
        {
            "term": "Norm Life Cycle",
            "category": "Theory & Epistemology",
            "scholars": "Martha Finnemore, Kathryn Sikkink (1998)",
            "definition": "A three-stage model of how international norms evolve and become institutionalized: norm emergence (championed by norm entrepreneurs), norm cascade (tipping point across states), and norm internalization (taken-for-granted status).",
            "module": "023",
            "chapter_slug": "constructivism-in-ir"
        },
        {
            "term": "Strategic Culture",
            "category": "Security & Strategy",
            "scholars": "Jack Snyder, Colin Gray, Alastair Iain Johnston",
            "definition": "An integrated system of symbols, historical narratives, and habitual predispositions that conditions a society's perceptions of threat and strategic choices regarding the use of force.",
            "module": "022",
            "chapter_slug": "strategic-culture"
        },
        {
            "term": "Paradiplomacy",
            "category": "Diplomacy & FPA",
            "scholars": "Ivo Duchacek, Panayotis Soldatos",
            "definition": "Foreign policy actions and international relations conducted by sub-national entities (regions, provinces, federated states, and mega-cities) promoting local trade, culture, and environmental cooperation.",
            "module": "032",
            "chapter_slug": "paradiplomacy-subnational"
        },
        {
            "term": "Minilateralism",
            "category": "Diplomacy & FPA",
            "scholars": "Moisés Naím, Stewart Patrick",
            "definition": "A targeted diplomatic format that convenes the smallest number of states necessary to address a specific issue (e.g., Quad, AUKUS, I2U2), chosen as an efficient alternative to unwieldy universal multilateral bodies.",
            "module": "032",
            "chapter_slug": "multilateral-diplomacy"
        },
        {
            "term": "P5 Veto Power",
            "category": "International Law",
            "scholars": "UN Charter Article 27(3)",
            "definition": "The special voting privilege granted to the five permanent members of the UN Security Council (US, UK, France, Russia, China), where a negative vote by any single permanent member vetoes any non-procedural resolution.",
            "module": "045",
            "chapter_slug": "un-security"
        },
        {
            "term": "Chapter VII Enforcement",
            "category": "International Law",
            "scholars": "UN Charter Articles 39–51",
            "definition": "The legal regime empowering the UN Security Council to determine the existence of any threat to the peace, breach of the peace, or act of aggression and mandate binding economic sanctions or armed military force.",
            "module": "045",
            "chapter_slug": "un-security"
        },
        {
            "term": "Bandung Spirit",
            "category": "Indonesian Diplomacy",
            "scholars": "Asian-African Conference (1955)",
            "definition": "The ethos of political solidarity, peaceful coexistence, anti-colonialism, and non-alignment born among newly independent nations in Bandung, championing the Ten Principles of Bandung.",
            "module": "013",
            "chapter_slug": "indonesia-foreign-policy-history"
        },
        {
            "term": "Wawasan Nusantara",
            "category": "Indonesian Diplomacy",
            "scholars": "Mochtar Kusumaatmadja, Djuanda Kartawidjaja",
            "definition": "Indonesia's geopolitical archipelagic doctrine conceiving the nation's land, inland seas, territorial waters, and airspace as an integrated, indivisible socio-political, economic, and defense entity.",
            "module": "013",
            "chapter_slug": "basic-political"
        },
        {
            "term": "RCEP",
            "category": "Political Economy",
            "scholars": "ASEAN, China, Japan, Korea, Australia, New Zealand (2022)",
            "definition": "Regional Comprehensive Economic Partnership: the world's largest mega-regional free trade agreement covering 30% of global population and GDP, harmonizing regional rules of origin across the Asia-Pacific.",
            "module": "050",
            "chapter_slug": "TPP-RCEP"
        },
        {
            "term": "CPTPP",
            "category": "Political Economy",
            "scholars": "11 Pacific Basin Nations (2018)",
            "definition": "Comprehensive and Progressive Agreement for Trans-Pacific Partnership: a high-standard regional trade treaty governing labor standards, state-owned enterprises, environmental protections, and digital trade.",
            "module": "050",
            "chapter_slug": "TPP-RCEP"
        },
        {
            "term": "Dispute Settlement Body (DSB)",
            "category": "Political Economy",
            "scholars": "WTO Dispute Settlement Understanding (1995)",
            "definition": "The judicial branch of the WTO responsible for establishing panels, adopting appellate reports, and authorizing trade retaliation when member states breach multilateral trade agreements.",
            "module": "050",
            "chapter_slug": "wto-decision-making"
        },
        {
            "term": "Anti-Dumping Duty",
            "category": "Political Economy",
            "scholars": "GATT Article VI, WTO Anti-Dumping Agreement",
            "definition": "A border tariff levied by an importing nation to neutralize the unfair price distortion caused when a foreign firm exports products below their normal domestic market value.",
            "module": "050",
            "chapter_slug": "trade-remedies-wto"
        },
        {
            "term": "Countervailing Duty (CVD)",
            "category": "Political Economy",
            "scholars": "WTO Agreement on Subsidies and Countervailing Measures (SCM)",
            "definition": "A specific duty imposed to offset the unfair cost advantage of foreign imports that have received illegal or actionable government subsidies in their country of origin.",
            "module": "050",
            "chapter_slug": "trade-remedies-wto"
        },
        {
            "term": "TRIPS Agreement",
            "category": "Political Economy",
            "scholars": "WTO (1994)",
            "definition": "Trade-Related Aspects of Intellectual Property Rights: a comprehensive multilateral legal agreement establishing minimum standards for patents, copyrights, trademarks, and trade secrets.",
            "module": "050",
            "chapter_slug": "trips-wto-diplomacy"
        },
        {
            "term": "Carbon Leakage",
            "category": "Political Economy",
            "scholars": "EU CBAM (2023)",
            "definition": "The relocation of carbon-intensive industrial manufacturing from nations with strict environmental regulations and carbon pricing to foreign jurisdictions with lax climate policies.",
            "module": "050",
            "chapter_slug": "green-trade-diplomacy"
        },
        {
            "term": "Nine-Dash Line",
            "category": "Regionalism & ASEAN",
            "scholars": "South China Sea Arbitration (2016)",
            "definition": "A historic maritime claim line utilized by China to assert historic rights and maritime jurisdiction over approximately 80% of the South China Sea, ruled invalid under UNCLOS in 2016.",
            "module": "044",
            "chapter_slug": "asean-community"
        },
        {
            "term": "Security Community",
            "category": "Security & Strategy",
            "scholars": "Karl Deutsch (1957), Emanuel Adler, Michael Barnett",
            "definition": "A group of sovereign states whose people and governments have developed a dependable expectation of peaceful change, ruling out the use of armed force against one another.",
            "module": "022",
            "chapter_slug": "security-community"
        },
        {
            "term": "Sovereign Wealth Fund (SWF)",
            "category": "Political Economy",
            "scholars": "IMF Santiago Principles (2008)",
            "definition": "A state-owned investment fund composed of foreign exchange reserves, commodity revenues, or fiscal surpluses, invested globally in stocks, bonds, and real estate (e.g., Norway GPFG, GIC Singapore, INA Indonesia).",
            "module": "046",
            "chapter_slug": "sovereign-wealth-funds"
        },
        {
            "term": "De-Dollarization",
            "category": "Political Economy",
            "scholars": "BRICS, Barry Eichengreen",
            "definition": "The systemic process whereby sovereign nations diversify bilateral trade invoicing, currency reserves, and international settlements away from exclusive reliance on the United States dollar.",
            "module": "046",
            "chapter_slug": "global-financial-system"
        },
        {
            "term": "Peacebuilding",
            "category": "International Law",
            "scholars": "Boutros Boutros-Ghali ('An Agenda for Peace' 1992)",
            "definition": "Action undertaken to identify and support structures which tend to strengthen and solidify peace in order to avoid a relapse into conflict, addressing the socio-economic and institutional root causes of war.",
            "module": "045",
            "chapter_slug": "un-peacekeeping-generations"
        },
        {
            "term": "Autarky",
            "category": "Political Economy",
            "scholars": "Friedrich List, Classical Mercantilism",
            "definition": "A national economic policy of complete self-sufficiency that seeks to eliminate reliance on international trade, foreign imports, and global financial markets.",
            "module": "021",
            "chapter_slug": "introduction-ipe"
        },
        {
            "term": "Financial Contagion",
            "category": "Political Economy",
            "scholars": "Asian Financial Crisis 1997, 2008 Global Financial Crisis",
            "definition": "The rapid cross-border transmission of financial instability, currency collapse, and banking crises from one economy to neighboring or interconnected economies regardless of fundamentals.",
            "module": "046",
            "chapter_slug": "global-financial-system"
        },
        {
            "term": "Non-Refoulement",
            "category": "International Law",
            "scholars": "1951 Refugee Convention Article 33",
            "definition": "A fundamental principle of customary international refugee law prohibiting states from expelling or returning a refugee to a country where their life or freedom would be threatened.",
            "module": "034",
            "chapter_slug": "migration-refugee-politics"
        },
        {
            "term": "Treaty of Amity and Cooperation (TAC)",
            "category": "Regionalism & ASEAN",
            "scholars": "ASEAN Bali Concord I (1976)",
            "definition": "A foundational regional peace treaty legally binding signatories to mutual respect for sovereignty, non-interference, peaceful dispute settlement, and renunciation of the threat or use of force in Southeast Asia.",
            "module": "044",
            "chapter_slug": "zopfan-treaty-amity"
        },
        {
            "term": "AICHR",
            "category": "Regionalism & ASEAN",
            "scholars": "ASEAN (2009)",
            "definition": "The ASEAN Intergovernmental Commission on Human Rights, a consultative regional body mandated to promote and protect human rights across Southeast Asian member states.",
            "module": "044",
            "chapter_slug": "asean-community"
        },
        {
            "term": "Security Sector Reform (SSR)",
            "category": "Indonesian Diplomacy",
            "scholars": "UU TNI No. 34/2004, Reformasi 1998",
            "definition": "The institutional transformation of national defense and police structures to ensure democratic civilian oversight, depoliticization of the armed forces, and human rights compliance.",
            "module": "013",
            "chapter_slug": "civil-military"
        },
        {
            "term": "Balance of Threat",
            "category": "Theory & Epistemology",
            "scholars": "Stephen Walt (1987)",
            "definition": "A modification of neorealist balance of power asserting that states balance against perceived threats, determined by aggregate power, geographical proximity, offensive capabilities, and aggressive intentions.",
            "module": "023",
            "chapter_slug": "neorealism-structural-realism"
        },
        {
            "term": "Liberal International Order (LIO)",
            "category": "Theory & Epistemology",
            "scholars": "G. John Ikenberry",
            "definition": "A rules-based multilateral order structured around open markets, multilateral security institutions, democratic norms, and American leadership forged after 1945.",
            "module": "041",
            "chapter_slug": "history-fpa"
        },
        {
            "term": "Hegemony (Gramscian / Coxian)",
            "category": "Theory & Epistemology",
            "scholars": "Antonio Gramsci, Robert W. Cox",
            "definition": "A historic structure of dominance that combines coercive material power with ideological and normative consent, institutionalized globally through international organizations and culture.",
            "module": "023",
            "chapter_slug": "critical-theory-ir"
        },
        {
            "term": "Revisionist State",
            "category": "Theory & Epistemology",
            "scholars": "E.H. Carr, Randall Schweller",
            "definition": "A state dissatisfied with its current position, prestige, and territorial boundaries in the international system, actively seeking to alter the systemic status quo.",
            "module": "023",
            "chapter_slug": "realism-in-ir"
        },
        {
            "term": "Status Quo State",
            "category": "Theory & Epistemology",
            "scholars": "Hans Morgenthau, Randall Schweller",
            "definition": "A state satisfied with the existing international distribution of power and territorial arrangements, seeking to defend and preserve established systemic rules.",
            "module": "023",
            "chapter_slug": "realism-in-ir"
        },
        {
            "term": "Fragile State",
            "category": "Security & Strategy",
            "scholars": "Fund for Peace, OECD",
            "definition": "A sovereign state where central government authority, institutional capacity, and public service provision have deteriorated to the point where it cannot maintain domestic order or security.",
            "module": "034",
            "chapter_slug": "humanitarian-intervention-r2p"
        },
        {
            "term": "Non-Aligned Movement (NAM)",
            "category": "Indonesian Diplomacy",
            "scholars": "Belgrade Summit (1961), Sukarno, Tito, Nehru, Nasser",
            "definition": "A multilateral forum of 120 developing nations founded to preserve diplomatic independence, oppose colonialism, and resist alignment with either the Western or Eastern superpower blocs during the Cold War.",
            "module": "013",
            "chapter_slug": "indonesia-foreign-policy-history"
        },
        {
            "term": "Hierarchy in International Relations",
            "category": "Theory & Epistemology",
            "scholars": "David A. Lake",
            "definition": "An analytical approach demonstrating that rather than pure anarchy, international relations frequently features institutionalized hierarchical authority relationships (empires, protectorates, spheres of influence).",
            "module": "010",
            "chapter_slug": "the-international-system"
        },
        {
            "term": "Rational Choice Theory",
            "category": "Theory & Epistemology",
            "scholars": "Bruce Bueno de Mesquita, James Morrow",
            "definition": "A formal modeling paradigm assuming political actors have ordered preferences and select strategies calculated to maximize expected utility under institutional constraints.",
            "module": "031",
            "chapter_slug": "rational-choice"
        },
        {
            "term": "Concert of Democracies",
            "category": "Diplomacy & FPA",
            "scholars": "Ivo Daalder, James Lindsay",
            "definition": "A proposed multilateral alliance or coalition of democratic states operating outside universal bodies like the UN to coordinate security and economic responses to illiberal powers.",
            "module": "041",
            "chapter_slug": "history-fpa"
        }
    ]

    out_file = Path("assets/data/ir_glossary.json")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(terms, f, indent=2, ensure_ascii=False)

    # Also copy to _data for Liquid access if needed
    data_file = Path("_data/ir_glossary.json")
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(terms, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {len(terms)} curated academic concepts at {out_file} and {data_file}")

if __name__ == "__main__":
    create_curated_glossary()
