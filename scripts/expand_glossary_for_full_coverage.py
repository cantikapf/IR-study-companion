# scripts/expand_glossary_for_full_coverage.py
"""
Expands the IR glossary with essential concepts across all remaining modules
(Methods, Indonesian Politics, History, Development, Contemporary Issues, International Law, Regionalism)
so that every single chapter across all 18 modules has dedicated plain-language terminology notes.
"""

import json
import os

ADDITIONAL_TERMS = [
    # --- SOCIAL SCIENCE & RESEARCH METHODS ---
    {
        "term": "Qualitative Research",
        "category": "Methods & Epistemology",
        "scholars": "King, Keohane & Verba (1994), George & Bennett (2005)",
        "definition": "A research strategy emphasizing non-numerical data such as texts, interviews, and historical archives to understand meanings, contexts, and causal mechanisms in international politics.",
        "module": "031",
        "chapter_slug": "_chapters/031-international-relations-research-method/040-qualitative",
        "plain_id": "Metode penelitian yang fokus memahami alasan mendalam di balik suatu peristiwa (mengapa dan bagaimana), bukan menghitung angka. Caranya lewat wawancara, dokumen rahasia, atau analisis pidato para pemimpin.",
        "plain_en": "Research focusing on non-numerical evidence—words, historical archives, and interviews—to understand why and how political events unfold."
    },
    {
        "term": "Quantitative Research",
        "category": "Methods & Epistemology",
        "scholars": "Singer (Correlates of War 1963), Fearon (1995)",
        "definition": "An empirical approach using statistical and mathematical models to analyze measurable numerical data across large sets of cases to test causal hypotheses.",
        "module": "031",
        "chapter_slug": "_chapters/031-international-relations-research-method/050-quantitative",
        "plain_id": "Metode penelitian yang mengumpulkan data angka dan statistik dalam jumlah besar (seperti data anggaran militer ratusan negara selama 50 tahun) untuk membuktikan apakah ada pola sebab-akibat yang nyata.",
        "plain_en": "An empirical approach using statistics and datasets across many countries to test hypotheses and discover mathematical patterns in world politics."
    },
    {
        "term": "Case Study",
        "category": "Methods & Epistemology",
        "scholars": "Gerring (2004), Yin (2018)",
        "definition": "An intensive qualitative analysis of a single unit or a small number of units (e.g., the Cuban Missile Crisis) to elucidate features of a larger class of similar phenomena.",
        "module": "031",
        "chapter_slug": "_chapters/031-international-relations-research-method/040-qualitative",
        "plain_id": "Penyelidikan mendalam terhadap satu peristiwa atau negara tertentu (contoh: Krisis Misil Kuba 1962) sebagai 'kaca pembesar' untuk memahami bagaimana krisis nuklir serupa bisa terjadi.",
        "plain_en": "An in-depth investigation of a single historical event or country used to extract broader lessons about international behavior."
    },
    {
        "term": "Process Tracing",
        "category": "Methods & Epistemology",
        "scholars": "Bennett & Checkel (2015), Collier (2011)",
        "definition": "A qualitative method that examines diagnostic pieces of evidence within a single case to unpack the step-by-step causal chain linking cause and effect.",
        "module": "031",
        "chapter_slug": "_chapters/031-international-relations-research-method/040-qualitative",
        "plain_id": "Teknik kerja detektif dalam penelitian HI: melacak mata rantai peristiwa langkah demi langkah secara kronologis untuk membuktikan apakah keputusan A benar-benar yang menyebabkan terjadinya krisis B.",
        "plain_en": "A forensic method tracing the step-by-step causal chain inside a case to prove exactly how an initial decision led to the final outcome."
    },
    {
        "term": "Triangulation",
        "category": "Methods & Epistemology",
        "scholars": "Denzin (1978), Patton (2002)",
        "definition": "The practice of combining multiple independent methods, data sources, or theoretical perspectives to verify research findings and minimize investigative bias.",
        "module": "031",
        "chapter_slug": "_chapters/031-international-relations-research-method/090-survey",
        "plain_id": "Teknik cek-silang kebenaran data dari beberapa sudut berbeda (misalnya mencocokkan dokumen resmi, wawancara diplomat, dan liputan media) agar analisis tidak mudah tertipu oleh satu sumber saja.",
        "plain_en": "Cross-checking facts from multiple independent sources (documents, interviews, statistics) to ensure findings are bulletproof and unbiased."
    },
    {
        "term": "Elite Interview",
        "category": "Methods & Epistemology",
        "scholars": "Aberbach & Rockman (2002), Tansey (2007)",
        "definition": "A qualitative research technique conducting semi-structured interviews with high-ranking decision-makers, diplomats, and policy experts to uncover unwritten negotiation dynamics.",
        "module": "031",
        "chapter_slug": "_chapters/031-international-relations-research-method/090-survey",
        "plain_id": "Wawancara khusus dengan tokoh-tokoh penting pembuat kebijakan (seperti menteri luar negeri, duta besar, atau jenderal) untuk menggali rahasia di balik layar yang tidak tertulis di dokumen publik.",
        "plain_en": "Interviews with high-ranking diplomats, ministers, or military leaders to uncover backstage political dynamics not recorded in public records."
    },
    {
        "term": "Participant Observation",
        "category": "Methods & Epistemology",
        "scholars": "Wacquant (2005), Neumann (2012)",
        "definition": "An ethnographic method where the researcher immerses themselves directly in the daily diplomatic or organizational environment of the subjects being studied.",
        "module": "031",
        "chapter_slug": "_chapters/031-international-relations-research-method/080-observation",
        "plain_id": "Metode di mana peneliti terjun langsung dan ikut beraktivitas di dalam lingkungan yang diteliti (misalnya magang di markas PBB atau kedutaan besar) untuk merasakan langsung budaya kerja diplomasinya.",
        "plain_en": "Immersing oneself directly inside an institution (like interning at the UN or an embassy) to observe diplomatic culture from the inside."
    },
    {
        "term": "Modernization Theory",
        "category": "Theory & Epistemology",
        "scholars": "Rostow (1960), Lipset (1959)",
        "definition": "A developmental paradigm asserting that traditional societies inevitably progress through linear industrial stages toward modern, democratic, Western-style capitalism.",
        "module": "011",
        "chapter_slug": "_chapters/011-introduction-to-social-science/060-social-change",
        "plain_id": "Teori klasik yang meyakini bahwa semua negara berkembang lambat laun akan mengikuti jejak Barat: bergerak dari masyarakat agraris tradisional menuju industrialisasi modern, pasar bebas, dan demokrasi.",
        "plain_en": "The theory that all nations follow a linear evolutionary path from traditional agricultural societies to modern, democratic, industrialized economies."
    },
    {
        "term": "Cultural Relativism",
        "category": "Theory & Epistemology",
        "scholars": "Boas (1887), Donnelly (1984)",
        "definition": "The view that cultural practices, beliefs, and values must be evaluated within their own societal context rather than measured against external universal standards.",
        "module": "011",
        "chapter_slug": "_chapters/011-introduction-to-social-science/030-culture-social-science",
        "plain_id": "Pandangan bahwa norma, etika, dan kebiasaan suatu bangsa harus dinilai berdasarkan konteks budayanya sendiri, bukan dipaksakan diukur memakai standar nilai moral bangsa lain (misalnya nilai Barat).",
        "plain_en": "The principle that cultural values and rights must be understood in their own societal context rather than judged by universal external yardsticks."
    },
    {
        "term": "Path Dependence",
        "category": "Theory & Epistemology",
        "scholars": "Pierson (2000), Arthur (1989)",
        "definition": "The concept that institutional decisions made early in history constrain subsequent choices, making it difficult or costly to alter course once a trajectory is chosen.",
        "module": "012",
        "chapter_slug": "_chapters/012-modern-world-history/010-why-history-matter",
        "plain_id": "Kondisi di mana keputusan sejarah masa lalu 'mengunci' pilihan masa kini. Sekali suatu negara memilih arah sistem tertentu, berpindah haluan di kemudian hari akan sangat sulit dan mahal.",
        "plain_en": "The idea that historical choices lock societies into specific institutional paths, making future changes difficult and costly."
    },

    # --- MODERN WORLD HISTORY & GEOPOLITICS ---
    {
        "term": "Cold War",
        "category": "Modern History & Geopolitics",
        "scholars": "Gaddis (2005), Kennan (1947)",
        "definition": "The geopolitical, ideological, and strategic confrontation between the United States and the Soviet Union (1947–1991), waged through proxy wars, arms races, and covert operations without direct superpower clash.",
        "module": "012",
        "chapter_slug": "_chapters/012-modern-world-history/170-end-cold-war",
        "plain_id": "Persaingan sengit antara blok Barat (AS & sekutu kapitalis) melawan blok Timur (Uni Soviet & sekutu komunis) selama 1947–1991. Disebut 'dingin' karena kedua raksasa nuklir ini tidak pernah saling tembak langsung di medan perang terbuka, melainkan lewat adu pengaruh dan perang perantara (proxy war).",
        "plain_en": "The 1947–1991 global ideological contest between the US and USSR, fought via proxy wars, deterrence, and intelligence rather than direct clash."
    },
    {
        "term": "Iron Curtain",
        "category": "Modern History & Geopolitics",
        "scholars": "Churchill (Fulton Speech 1946)",
        "definition": "The political, military, and ideological barrier erected by the Soviet Union post-WWII to seal itself and its European satellite states off from open contact with the West.",
        "module": "012",
        "chapter_slug": "_chapters/012-modern-world-history/170-end-cold-war",
        "plain_id": "Istilah metafora untuk garis pemisah ideologis dan militer yang membelah benua Eropa menjadi dua selama Perang Dingin: Eropa Barat yang bebas dan Eropa Timur di bawah kendali ketat Uni Soviet.",
        "plain_en": "The ideological and fortified border separating communist Eastern Europe from capitalist Western Europe during the Cold War."
    },
    {
        "term": "Maoism",
        "category": "Modern History & Geopolitics",
        "scholars": "Mao Zedong (1949), Schram (1989)",
        "definition": "The variant of Marxist-Leninist ideology developed by Mao Zedong, viewing the rural peasantry rather than the urban industrial proletariat as the primary engine of anti-imperialist revolution.",
        "module": "012",
        "chapter_slug": "_chapters/012-modern-world-history/160-birth-prc",
        "plain_id": "Paham komunisme khas Tiongkok gagasan Mao Zedong yang menjadikan petani desa—bukan buruh pabrik perkotaan—sebagai motor utama revolusi bersenjata melawan kaum borjuis dan imperialisme.",
        "plain_en": "Mao's adaptation of Marxism-Leninism that positioned rural peasants rather than urban factory workers as the driving force of socialist revolution."
    },
    {
        "term": "Alliance System",
        "category": "Modern History & Geopolitics",
        "scholars": "Snyder (Alliance Politics 1997), Taylor (1954)",
        "definition": "A formal network of bilateral and multilateral mutual defense pacts where signatory states pledge to assist each other militarily if attacked, which in 1914 escalated a local Balkan crisis into World War I.",
        "module": "012",
        "chapter_slug": "_chapters/012-modern-world-history/040-road-to-ww1",
        "plain_id": "Jaringan perjanjian militer antar-negara di mana jika salah satu sekutu diserang, negara lain otomatis ikut berperang membela. Sistem inilah yang mengubah konflik lokal di Balkan tahun 1914 menjadi Perang Dunia I.",
        "plain_en": "Formal defense treaties pledging mutual military aid, which turned a local 1914 Balkan clash into a devastating global world war."
    },

    # --- INDONESIAN POLITICS & GOVERNANCE ---
    {
        "term": "Decentralization (Otonomi Daerah)",
        "category": "Regionalism & Indonesia",
        "scholars": "Aspinall & Fealy (2003), Hadiz (2010)",
        "definition": "The transfer of political, administrative, and fiscal authority from the central government in Jakarta to regional regencies (kabupaten) and cities (kota), enacted under Law No. 22/1999 post-Reformasi.",
        "module": "013",
        "chapter_slug": "_chapters/013-indonesia-political-perspective/060-democracy-indonesia",
        "plain_id": "Pelimpahan wewenang dan pengelolaan anggaran dari pemerintah pusat di Jakarta kepada pemerintah kabupaten dan kota di seluruh daerah Indonesia pasca-Reformasi 1998, agar pembangunan tidak terpusat di Jawa.",
        "plain_en": "The devolution of political and fiscal powers from Jakarta to municipal and regency governments across Indonesia enacted after the 1998 Reformasi."
    },
    {
        "term": "Reformasi (Indonesia 1998)",
        "category": "Regionalism & Indonesia",
        "scholars": "O'Donnell & Schmitter (1986), Mietzner (2009)",
        "definition": "The democratic transition in Indonesia ignited in May 1998 following the collapse of Suharto's authoritarian New Order regime, leading to constitutional amendments, multi-party elections, and press freedom.",
        "module": "013",
        "chapter_slug": "_chapters/013-indonesia-political-perspective/030-evolution-party",
        "plain_id": "Gerakan perubahan besar pada Mei 1998 yang mengakhiri 32 tahun kekuasaan Orde Baru pimpinan Soeharto, membuka pintu kebebasan pers, pemilu multipartai yang demokratis, dan pembatasan masa jabatan presiden.",
        "plain_en": "The 1998 political transition that ended Suharto's 32-year authoritarian New Order, ushering in multi-party democracy, freedom of speech, and institutional reform."
    },
    {
        "term": "Trias Politica",
        "category": "Regionalism & Indonesia",
        "scholars": "Montesquieu (The Spirit of the Laws 1748)",
        "definition": "The constitutional doctrine separating state power into three independent branches—executive, legislative, and judicial—to prevent tyranny through a system of mutual checks and balances.",
        "module": "013",
        "chapter_slug": "_chapters/013-indonesia-political-perspective/020-political-institution",
        "plain_id": "Prinsip pemisahan kekuasaan negara menjadi 3 cabang independen: Eksekutif (Presiden yang menjalankan undang-undang), Legislatif (DPR yang membuat undang-undang), dan Yudikatif (Mahkamah Agung/MK yang mengadili pelanggaran), agar tidak ada penguasa yang bertindak sewenang-wenang.",
        "plain_en": "The separation of government into executive, legislative, and judicial branches to safeguard liberty through checks and balances."
    },
    {
        "term": "Aliran Politics (Politik Aliran)",
        "category": "Regionalism & Indonesia",
        "scholars": "Geertz (The Religion of Java 1960), Feith (1962)",
        "definition": "A sociological framework describing Indonesian political mobilization structured along distinct religious and ideological subcultures: santri (devout Islamic), abangan (traditionalist/nominal), and secular-nationalist.",
        "module": "013",
        "chapter_slug": "_chapters/013-indonesia-political-perspective/030-evolution-party",
        "plain_id": "Pola politik di Indonesia di mana dukungan terhadap partai politik terikat kuat pada identitas keagamaan atau budaya leluhur (seperti santri, abangan, dan nasionalis sekuler) ketimbang isu program kerja semata.",
        "plain_en": "Political loyalty organized around deep-seated religious and socio-cultural identities (Islamic devout vs. traditionalist secular nationalists)."
    },
    {
        "term": "Electoral Threshold (Ambang Batas Parlemen)",
        "category": "Regionalism & Indonesia",
        "scholars": "Reilly (2001), Mietzner (2014)",
        "definition": "A legal minimum percentage of the national popular vote that a political party must secure in legislative elections to obtain seats in the People's Representative Council (DPR).",
        "module": "013",
        "chapter_slug": "_chapters/013-indonesia-political-perspective/050-electoral-indonesia",
        "plain_id": "Syarat minimal persentase suara sah nasional (misalnya 4%) yang wajib diraih oleh sebuah partai politik dalam Pemilu agar berhak mengirimkan wakilnya duduk di kursi DPR RI.",
        "plain_en": "The legal minimum percentage of the national vote a party must win in general elections to secure seats in parliament."
    },
    {
        "term": "Gender Quota (Kuota Gender 30%)",
        "category": "Regionalism & Indonesia",
        "scholars": "Dahlerup (2006), Krook (2009)",
        "definition": "An affirmative action regulation requiring political parties in Indonesia to include at least 30% female candidates on their legislative electoral candidate lists.",
        "module": "013",
        "chapter_slug": "_chapters/013-indonesia-political-perspective/070-women-indonesia",
        "plain_id": "Aturan hukum yang mewajibkan setiap partai politik mencalonkan minimal 30% perempuan dalam daftar calon anggota legislatif (caleg) untuk mendorong keterwakilan perempuan di parlemen.",
        "plain_en": "Affirmative action rule mandating that women make up at least 30% of candidate nomination lists for legislative elections."
    },

    # --- INTERNATIONAL POLITICAL ECONOMY & MONETARY ---
    {
        "term": "International Monetary System",
        "category": "Political Economy",
        "scholars": "Eichengreen (Globalizing Capital 2008), Cohen (1977)",
        "definition": "The institutional arrangements, rules, conventions, and instruments that govern foreign exchange rates, cross-border payments, and capital flows among sovereign nations.",
        "module": "021",
        "chapter_slug": "_chapters/021-international-political-economy/080-monetary-system",
        "plain_id": "Aturan main dan kesepakatan antar-negara tentang bagaimana uang ditukar dan pembayaran antar-negara dilakukan di seluruh dunia (misalnya penentuan nilai dolar AS, emas, atau euro).",
        "plain_en": "The international rules, conventions, and institutions that govern how currencies are valued, traded, and settled across national borders."
    },
    {
        "term": "Floating Exchange Rate",
        "category": "Political Economy",
        "scholars": "Friedman (1953), Obstfeld & Rogoff (1996)",
        "definition": "A monetary regime in which a country's currency price is determined by the open market mechanisms of supply and demand relative to other currencies, without official government pegging.",
        "module": "021",
        "chapter_slug": "_chapters/021-international-political-economy/090-exchange-rates",
        "plain_id": "Sistem kurs mengambang di mana nilai tukar rupiah atau mata uang lain naik-turun secara bebas mengikuti permintaan dan penawaran di pasar uang dunia, bukan dipatok sepihak oleh pemerintah.",
        "plain_en": "A regime where currency values fluctuate freely based on private foreign exchange market forces without fixed government pegs."
    },
    {
        "term": "Structural Adjustment Program (SAP)",
        "category": "Political Economy",
        "scholars": "Stiglitz (Globalization and Its Discontents 2002), Williamson (1990)",
        "definition": "Economic policy conditionalities imposed by the IMF and World Bank on borrowing developing countries, mandating privatization, fiscal austerity, trade liberalization, and currency devaluation.",
        "module": "021",
        "chapter_slug": "_chapters/021-international-political-economy/095-neoliberalism-ipe",
        "plain_id": "Paket syarat pinjaman ketat dari IMF/Bank Dunia yang mewajibkan negara peminjam memotong subsidi rakyat, memangkas anggaran belanja, dan membuka pasar untuk investasi asing agar utang bisa dibayar.",
        "plain_en": "Tough loan conditions imposed by the IMF/World Bank forcing borrowing nations to cut social spending, privatize state assets, and open markets."
    },
    {
        "term": "Neoliberalism",
        "category": "Political Economy",
        "scholars": "Harvey (A Brief History of Neoliberalism 2005), Hayek (1944)",
        "definition": "A political-economic ideology advocating free markets, deregulation, privatization, free trade, and minimal state intervention in the economy.",
        "module": "021",
        "chapter_slug": "_chapters/021-international-political-economy/095-neoliberalism-ipe",
        "plain_id": "Paham ekonomi yang meyakini bahwa pasar bebas adalah jalan terbaik menuju kemakmuran: peran pemerintah harus dibatasi seminimal mungkin, pajak dipangkas, dan sektor publik diserahkan ke pihak swasta.",
        "plain_en": "An economic doctrine advocating deregulation, privatization, free trade, and reducing government intervention in the economy."
    },
    {
        "term": "Single Market (European Integration)",
        "category": "Political Economy",
        "scholars": "Moravcsik (The Choice for Europe 1998), Haas (1958)",
        "definition": "A unified economic area within the European Union characterized by the free movement of goods, services, capital, and labor (the 'Four Freedoms') with zero internal tariffs and common external regulation.",
        "module": "046",
        "chapter_slug": "_chapters/046-global-economic-architecture/050-european-economic",
        "plain_id": "Kawasan pasar terpadu Uni Eropa di mana barang, jasa, uang, dan tenaga kerja bisa berpindah antar negara anggota sebebas di dalam satu negara tanpa bea cukai atau paspor rumit ('Empat Kebebasan').",
        "plain_en": "The EU's unified economic territory allowing goods, services, people, and money to move freely across member borders without tariffs or border checks."
    },

    # --- SECURITY STUDIES & TRANSNATIONAL THREATS ---
    {
        "term": "Transnational Organized Crime (TOC)",
        "category": "Security & Strategy",
        "scholars": "Shelley (Dirty Entanglements 2014), Williams (1994)",
        "definition": "Self-perpetuating criminal associations operating across national borders, using violence, corruption, and illicit commercial supply chains (e.g., narcotics, arms, human trafficking) for economic gain.",
        "module": "022",
        "chapter_slug": "_chapters/022-introduction-to-security-studies/070-crime-terrorism-insurgency",
        "plain_id": "Jaringan sindikat kejahatan yang beroperasi menembus batas-batas negara (seperti perdagangan narkoba internasional, penyelundupan manusia, atau pencucian uang) demi meraup keuntungan finansial raksasa.",
        "plain_en": "Cross-border illicit crime networks (drug cartels, human trafficking, arms smuggling) exploiting globalization for financial profit."
    },
    {
        "term": "Energy Security",
        "category": "Security & Strategy",
        "scholars": "Yergin (The Prize 1991), Hughes (2012)",
        "definition": "The uninterrupted availability of energy sources at an affordable price, encompassing physical protection of critical infrastructure, diversification of fuel supplies, and geopolitical supply chain stability.",
        "module": "022",
        "chapter_slug": "_chapters/022-introduction-to-security-studies/080-energy-security",
        "plain_id": "Kemampuan suatu negara untuk menjamin pasokan energi (minyak, gas, listrik) selalu cukup, tidak terputus, dan dengan harga terjangkau bagi rakyat dan industrinya, tanpa mudah disandera oleh negara pengekspor.",
        "plain_en": "A nation's capacity to secure reliable, uninterrupted, and affordable energy supplies without being vulnerable to geopolitical blackmail."
    },

    # --- CONTEMPORARY ISSUES & GLOBAL GOVERNANCE ---
    {
        "term": "Official Development Assistance (ODA)",
        "category": "Diplomacy & FPA",
        "scholars": "Easterly (The White Man's Burden 2006), Sachs (The End of Poverty 2005)",
        "definition": "Government aid designed to promote the economic development and welfare of developing countries, provided through grants or concessional loans with a grant element of at least 25%.",
        "module": "034",
        "chapter_slug": "_chapters/034-Contemporary Issues In Global Politics/020-poverty-development-aid",
        "plain_id": "Bantuan keuangan resmi (hibah atau pinjaman bunga sangat rendah) dari negara maju kepada negara berkembang untuk membiayai pembangunan rumah sakit, sekolah, jalan, atau pengentasan kemiskinan.",
        "plain_en": "Official financial aid and low-interest loans from rich nations to developing countries dedicated to economic welfare and poverty reduction."
    },
    {
        "term": "Populism",
        "category": "Diplomacy & FPA",
        "scholars": "Mudde & Kaltwasser (Populism: A Very Short Introduction 2017), Müller (2016)",
        "definition": "A political approach that juxtaposes the 'pure, virtuous people' against a 'corrupt, self-serving elite', often challenging internationalist institutions, free trade treaties, and multilateral cooperation.",
        "module": "034",
        "chapter_slug": "_chapters/034-Contemporary Issues In Global Politics/070-populism",
        "plain_id": "Gaya politik yang membelah masyarakat menjadi dua: 'rakyat jelata yang jujur' melawan 'kaum elit penguasa yang korup'. Pemimpin populis sering menyalahkan orang asing, imigran, atau lembaga internasional atas masalah dalam negeri.",
        "plain_en": "A political ideology framing politics as a struggle between the 'pure people' and the 'corrupt globalist elite', often resisting multilateral treaties."
    },
    {
        "term": "Multiculturalism",
        "category": "Theory & Epistemology",
        "scholars": "Kymlicka (Multicultural Citizenship 1995), Taylor (1994)",
        "definition": "A political philosophy advocating the accommodation and equal civic recognition of diverse cultural, ethnic, and religious communities within a single nation-state without forced assimilation.",
        "module": "034",
        "chapter_slug": "_chapters/034-Contemporary Issues In Global Politics/060-multiculturalism",
        "plain_id": "Kebijakan dan pandangan hidup yang menghargai keberagaman suku, agama, dan budaya dalam satu negara, di mana kelompok minoritas tidak dipaksa melebur (asimilasi), melainkan diakui hak-hak budayanya secara setara.",
        "plain_en": "The policy of actively recognizing and protecting diverse ethnic and cultural communities within a society without forcing them to assimilate."
    },
    {
        "term": "CNN Effect",
        "category": "Diplomacy & FPA",
        "scholars": "Livingston (1997), Robinson (The CNN Effect 2002)",
        "definition": "The theory that real-time, 24-hour broadcast news coverage of humanitarian crises pressures government policymakers to intervene militarily or diplomatically abroad.",
        "module": "033",
        "chapter_slug": "_chapters/033-foreign-policy-analysis-in-international-relations/050-public-media-fpdm",
        "plain_id": "Fenomena di mana siaran berita televisi atau media sosial yang menyiarkan penderitaan korban perang selama 24 jam penuh menekan para presiden/perdana menteri untuk segera turun tangan memberi bantuan militer atau kemanusiaan.",
        "plain_en": "The theory that 24/7 rolling news coverage of humanitarian horrors compels political leaders to launch foreign interventions."
    },
    {
        "term": "Disaster Diplomacy",
        "category": "Diplomacy & FPA",
        "scholars": "Kelman (Disaster Diplomacy 2012), Gaillard (2007)",
        "definition": "The investigation of how disaster risk reduction and post-disaster humanitarian aid catalyze, influence, or fail to resolve bilateral political conflicts between hostile nations.",
        "module": "034",
        "chapter_slug": "_chapters/034-Contemporary Issues In Global Politics/080-natural-disaster",
        "plain_id": "Diplomasi yang muncul akibat bencana alam besar: saat dua negara yang bermusuhan saling mengirim tim SAR dan bantuan medis, membuka peluang mencairnya ketegangan politik (contoh: tsunami Aceh 2004 mempercepat perdamaian GAM-RI).",
        "plain_en": "The phenomenon where joint relief efforts after severe natural disasters provide a diplomatic opening to ease hostilities between conflicting states."
    },

    # --- INTERNATIONAL LAW & STATEHOOD ---
    {
        "term": "Subject of International Law",
        "category": "International Law",
        "scholars": "Reparation for Injuries Case (ICJ 1949), Shaw (2021)",
        "definition": "An entity possessing international legal personality, capable of holding rights and duties under international law and having the capacity to bring international legal claims.",
        "module": "042",
        "chapter_slug": "_chapters/042-international-law-issues-and-international-dispute-settlement/030-subject-inter-law",
        "plain_id": "Pihak yang diakui secara sah memiliki hak dan kewajiban di mata hukum internasional (contoh utamanya: negara berdaulat, organisasi internasional seperti PBB, dan Tahta Suci Vatikan).",
        "plain_en": "An entity (such as a sovereign state or international organization) with legal standing to hold rights and make legal claims under international law."
    },
    {
        "term": "Montevideo Convention (1933)",
        "category": "International Law",
        "scholars": "Montevideo Convention on Rights and Duties of States (1933), Crawford (2006)",
        "definition": "The customary treaty codifying the four foundational criteria of statehood: a permanent population, a defined territory, an effective government, and the capacity to enter into relations with other states.",
        "module": "042",
        "chapter_slug": "_chapters/042-international-law-issues-and-international-dispute-settlement/040-state-inter-law",
        "plain_id": "Konvensi internasional yang menetapkan 4 syarat sah bagi suatu wilayah untuk diakui sebagai sebuah 'Negara': punya rakyat tetap, punya wilayah tertentu, punya pemerintah yang berdaulat, dan mampu berhubungan dengan negara lain.",
        "plain_en": "The landmark 1933 treaty establishing the 4 legal criteria of statehood: permanent population, defined territory, functioning government, and diplomatic capacity."
    },
    {
        "term": "Economic Statecraft",
        "category": "Diplomacy & FPA",
        "scholars": "Baldwin (Economic Statecraft 1985), Mastanduno (1998)",
        "definition": "The use of economic instruments (sanctions, tariffs, aid, investment bans, or trade privileges) by a sovereign state to exert power and achieve foreign policy objectives.",
        "module": "041",
        "chapter_slug": "_chapters/041-foreign-policy-of-developed-countries/020-economic-statecraft",
        "plain_id": "Penggunaan kekuatan ekonomi (seperti embargo dagang, sanksi keuangan, pembekuan aset bank, atau bantuan dana) oleh suatu negara sebagai 'senjata' untuk memaksa negara lain menuruti kemauannya tanpa perlu berperang.",
        "plain_en": "Using economic weapons (sanctions, trade embargoes, foreign aid) as diplomatic leverage to compel other nations to change their policies."
    },
    {
        "term": "Bangkok Declaration (1967)",
        "category": "Regionalism & Indonesia",
        "scholars": "ASEAN Declaration (8 August 1967), Leifer (1996)",
        "definition": "The founding five-point document signed by Indonesia, Malaysia, the Philippines, Singapore, and Thailand on August 8, 1967, establishing the Association of Southeast Asian Nations (ASEAN).",
        "module": "044",
        "chapter_slug": "_chapters/044-regionalism-in-southeast-asia-asean-community/030-establishment-asean",
        "plain_id": "Deklarasi bersejarah yang ditandatangani 5 tokoh pendiri (termasuk Adam Malik dari Indonesia) di Bangkok pada 8 Agustus 1967 yang menandai lahirnya organisasi ASEAN demi menjaga perdamaian dan stabilitas Asia Tenggara.",
        "plain_en": "The historic founding document signed on 8 August 1967 by five Southeast Asian foreign ministers establishing the ASEAN regional organization."
    },
    {
        "term": "Gini Coefficient",
        "category": "Political Economy",
        "scholars": "Gini (1912), Milanovic (Worlds Apart 2005)",
        "definition": "A statistical measure of income or wealth distribution inequality across a population, ranging from 0 (perfect equality) to 1 (complete inequality where one person holds all wealth).",
        "module": "043",
        "chapter_slug": "_chapters/043-international-political-economy-of-development/030-inequality-development",
        "plain_id": "Angka statistik (skala 0 sampai 1) yang mengukur tingkat ketimpangan pembagian kekayaan di suatu negara: nilai mendekati 0 berarti pendapatan rakyat terbagi rata, sedangkan mendekati 1 berarti seluruh uang terkumpul di tangan segelintir orang kaya.",
        "plain_en": "A 0-to-1 statistical index measuring income inequality: 0 means everyone earns equally, while 1 means a single elite holds all the wealth."
    },
    {
        "term": "Care Economy (Ekonomi Pengasuhan)",
        "category": "Political Economy",
        "scholars": "Folbre (The Invisible Heart 2001), Benería (2003)",
        "definition": "The sector of economic activities involving childcare, eldercare, nursing, and domestic labor, historically uncompensated and disproportionately performed by women, yet foundational to economic productivity.",
        "module": "043",
        "chapter_slug": "_chapters/043-international-political-economy-of-development/040-women-economic-role",
        "plain_id": "Sektor kerja merawat keluarga (mengurus anak, memasak, merawat lansia) yang sebagian besar dikerjakan perempuan tanpa digaji, padahal menjadi fondasi utama yang memungkinkan para pekerja lain bisa pergi bekerja di kantor atau pabrik setiap hari.",
        "plain_en": "Unpaid household and caregiving work (childcare, nursing, domestic labor) disproportionately done by women, vital for sustaining the formal economy."
    },
    {
        "term": "Developmental State",
        "category": "Political Economy",
        "scholars": "Johnson (MITI and the Japanese Miracle 1982), Wade (1990)",
        "definition": "A political-economic model where the state plays an active, interventionist steering role in directing economic development, subsidizing export industries, and allocating strategic capital (e.g., Japan, South Korea, Taiwan).",
        "module": "043",
        "chapter_slug": "_chapters/043-international-political-economy-of-development/060-dev-china-india-chile-african-arab",
        "plain_id": "Model negara di mana pemerintah pusat turun tangan langsung memimpin strategi ekonomi: memilih industri unggulan, memberi subsidi besar, dan membimbing pengusaha nasional agar mampu bersaing dan mengalahkan produk luar negeri (contoh: Jepang, Korea Selatan pasca-perang).",
        "plain_en": "A model where the government aggressively guides national industrial growth and directs capital to export champions (e.g., post-war Japan and South Korea)."
    }
]

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_data = os.path.join(repo_root, '_data', 'ir_glossary.json')
    target_assets = os.path.join(repo_root, 'assets', 'data', 'ir_glossary.json')

    with open(target_data, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    existing_terms = {item['term'].lower(): item for item in existing_data}

    added = 0
    for term_obj in ADDITIONAL_TERMS:
        key = term_obj['term'].lower()
        if key not in existing_terms:
            existing_data.append(term_obj)
            added += 1

    # Sort alphabetically by term
    existing_data.sort(key=lambda x: x['term'].lower())

    with open(target_data, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=2, ensure_ascii=False)

    with open(target_assets, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=2, ensure_ascii=False)

    print(f"Added {added} new terms. Total glossary terms now: {len(existing_data)}.")

if __name__ == '__main__':
    main()
