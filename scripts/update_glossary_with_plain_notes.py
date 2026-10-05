"""
Update _data/ir_glossary.json and assets/data/ir_glossary.json with plain-language notes
(both Indonesian 'plain_id' and English 'plain_en') for all 122 curated IR concepts.
This enables ordinary readers and beginner students to easily understand complex IR jargon.
"""

import json
from pathlib import Path

# Complete mapping of plain-language notes for all 122 terms
PLAIN_EXPLANATIONS = {
    "Anarchy": {
        "plain_id": "Ketiadaan 'pemerintah dunia' atau otoritas tertinggi di atas negara. Bukan berarti dunia selalu rusuh atau kacau balau, melainkan tidak ada 'polisi global' yang punya wewenang mutlak memaksa negara-negara berdaulat untuk patuh.",
        "plain_en": "The absence of an overarching world government or global police. Sovereign states have no higher authority above them to enforce rules or guarantee their safety."
    },
    "Balance of Power": {
        "plain_id": "Keseimbangan kekuatan di mana negara-negara saling mengimbangi kekuatan militer atau membentuk koalisi aliansi agar tidak ada satu negara adidaya pun yang mendominasi dunia.",
        "plain_en": "A situation where states build up their military or form alliances to prevent any single superpower from becoming strong enough to dominate everyone else."
    },
    "Classical Realism": {
        "plain_id": "Pandangan bahwa perang dan perebutan kekuasaan terjadi karena sifat dasar manusia yang memang serakah, egois, dan selalu haus akan kekuasaan.",
        "plain_en": "The view that international conflict is driven by the inherently flawed, selfish, and power-hungry nature of human beings."
    },
    "Structural Realism (Neorealism)": {
        "plain_id": "Pandangan bahwa negara saling curiga dan bersaing bukan karena manusia jahat, melainkan karena sistem dunia tidak punya pemimpin (anarki), sehingga setiap negara terpaksa mementingkan pertahanan diri demi bertahan hidup.",
        "plain_en": "The theory that states compete and fear each other not because humans are evil, but because the leaderless structure of world politics (anarchy) forces them to focus on self-preservation."
    },
    "Offensive Realism": {
        "plain_id": "Teori bahwa cara terbaik bagi negara besar untuk aman adalah menjadi sekuat mungkin dan mendominasi kawasannya (hegemoni), karena niat negara lain tidak pernah bisa dipercaya 100%.",
        "plain_en": "The belief that great powers must maximize their power and strive to become the dominant hegemon because they can never be sure of other countries' true intentions."
    },
    "Defensive Realism": {
        "plain_id": "Teori bahwa negara hanya butuh kekuatan militer secukupnya untuk mempertahankan diri. Jika terlalu agresif memperluas wilayah, negara-negara tetangga justru akan bersatu mengeroyok dan mengalahkannya.",
        "plain_en": "The belief that states only need enough power to defend themselves, as aggressive expansion backfires by provoking counter-alliances."
    },
    "Neoliberal Institutionalism": {
        "plain_id": "Pandangan bahwa meskipun dunia anarki, negara-negara tetap bisa bekerja sama secara damai jika didukung lembaga internasional (seperti PBB atau WTO) yang membuat aturan main menjadi jelas dan mencegah kecurangan.",
        "plain_en": "The theory that international organizations allow countries to cooperate peacefully by creating clear rules, sharing information, and reducing the fear of cheating."
    },
    "Social Constructivism": {
        "plain_id": "Pandangan bahwa hubungan antarnegara dibentuk oleh ide, identitas, budaya, dan persepsi sosial, bukan hanya kalkulasi kekuatan senjata. Contoh: senjata nuklir Inggris tidak membuat AS takut karena mereka saling memandang sebagai sahabat.",
        "plain_en": "The idea that world politics is shaped by shared ideas, identities, and social relationships rather than just guns and money. (e.g., 500 British nuclear weapons don't terrify the US, but 5 North Korean ones do)."
    },
    "English School (International Society)": {
        "plain_id": "Teori yang memandang bahwa meski dunia tidak punya pemerintah tunggal, negara-negara membentuk 'masyarakat beradab' yang terikat norma diplomasi, hukum internasional, dan etika bersama.",
        "plain_en": "A framework arguing that states form an 'international society' bound by common rules, diplomatic norms, and shared values, rather than existing in constant lawless warfare."
    },
    "Critical Theory": {
        "plain_id": "Pendekatan yang membongkar bahwa teori-teori politik internasional sering kali diciptakan untuk melayani kepentingan pihak yang berkuasa, serta memperjuangkan pembebasan kelompok yang tertindas.",
        "plain_en": "An approach questioning who benefits from established theories of world politics, arguing that knowledge is never neutral and should aim to liberate oppressed peoples."
    },
    "Feminist International Relations": {
        "plain_id": "Kritik bahwa politik global dan urusan perang selama ini terlalu didominasi sudut pandang laki-laki dan mengabaikan bagaimana konflik berdampak pada perempuan serta pentingnya kesetaraan gender.",
        "plain_en": "A perspective examining how international politics is heavily shaped by masculine biases, highlighting the role of women and gender inequality in war and diplomacy."
    },
    "Postcolonialism": {
        "plain_id": "Kajian yang menyoroti bagaimana warisan penjajahan masa lalu masih terus melanggengkan ketidakadilan politik, ekonomi, dan cara pandang Barat terhadap negara-negara berkembang di belahan bumi selatan.",
        "plain_en": "An approach showing how historical colonial exploitation continues to shape modern global inequalities and biases against the Global South."
    },
    "Positivism": {
        "plain_id": "Metode ilmiah yang meyakini bahwa fenomena politik internasional bisa diteliti secara objektif menggunakan angka, data statistik, dan hukum sebab-akibat layaknya ilmu pasti (ilmu alam).",
        "plain_en": "The philosophy that human society can be studied like the natural sciences using objective data, testing, and universal causal laws."
    },
    "Interpretivism": {
        "plain_id": "Pendekatan yang menyatakan bahwa tindakan negara tidak bisa sekadar dihitung dengan rumus angka, melainkan harus dipahami dari makna budaya, bahasa, keyakinan, dan cara berpikir para pelakunya.",
        "plain_en": "The philosophy that social reality cannot be reduced to hard numbers, requiring researchers to interpret the subjective meanings, cultures, and beliefs of human actors."
    },
    "Levels of Analysis": {
        "plain_id": "Tiga 'kacamata' untuk membedah peristiwa dunia: tingkat individu (sifat pemimpin), tingkat negara (sistem politik dalam negeri), atau tingkat sistem internasional (hubungan kekuatan global).",
        "plain_en": "A framework dividing foreign policy explanations into three lenses: the individual level (the leader), the domestic level (the country's regime), and the systemic level (the global balance of power)."
    },
    "Prisoner's Dilemma": {
        "plain_id": "Teka-teki di mana dua pihak sebenarnya sama-sama untung jika bekerja sama, namun karena saling curiga dan takut dikhianati, mereka berdua memilih saling menjatuhkan sehingga hasilnya malah paling merugikan.",
        "plain_en": "A classic game theory paradox where two players would benefit most from cooperating, but because they fear betrayal, both act selfishly and end up with a worse outcome."
    },
    "Security Dilemma": {
        "plain_id": "Situasi serba salah ketika satu negara memperkuat militernya murni untuk membela diri, namun tetangganya merasa terancam dan ikut memborong senjata, sehingga kedua negara justru semakin rawan perang.",
        "plain_en": "A paradox where a nation builds up its military strictly for defense, but makes neighboring nations feel threatened, provoking an arms race that leaves all parties less secure."
    },
    "Mutual Assured Destruction (MAD)": {
        "plain_id": "Kondisi di mana dua negara berkekuatan nuklir sama-sama menyadari bahwa jika salah satu memulai perang nuklir, kedua belah pihak dipastikan akan hancur lebur tanpa pemenang, sehingga perang nuklir justru tercegah.",
        "plain_en": "A Cold War doctrine where both superpowers possess enough survivable nuclear weapons that any attack would result in total mutual annihilation, deterring either side from starting a war."
    },
    "Securitization": {
        "plain_id": "Proses ketika suatu isu biasa (seperti imigrasi atau perubahan iklim) dibingkai oleh elite politik sebagai 'ancaman luar biasa terhadap kelangsungan hidup bangsa', sehingga membenarkan penggunaan langkah-langkah darurat.",
        "plain_en": "The political process where leaders frame an ordinary issue as an existential emergency to justify overriding normal democratic procedures and using emergency powers."
    },
    "Human Security": {
        "plain_id": "Pergeseran fokus keamanan dari melindungi 'wilayah negara' ke arah melindungi 'kehidupan manusia' dari kemiskinan, penyakit kelaparan, bencana alam, dan pelanggaran hak asasi manusia.",
        "plain_en": "A human-centered security concept prioritizing the protection of individual citizens from poverty, disease, and violence, rather than merely guarding state borders."
    },
    "Democratic Peace Theory": {
        "plain_id": "Teori yang menyatakan bahwa negara-negara demokrasi hampir tidak pernah saling berperang satu sama lain, karena pemimpinnya bertanggung jawab kepada rakyat dan terbiasa menyelesaikan sengketa lewat musyawarah.",
        "plain_en": "The empirical finding and theory that mature democratic states rarely, if ever, go to war with one another due to institutional checks and shared democratic norms."
    },
    "Offense-Defense Balance": {
        "plain_id": "Kondisi militer apakah lebih mudah menyerang atau bertahan. Jika teknologi membuat penyerangan lebih mudah, perang lebih gampang pecah; sebaliknya jika pertahanan lebih kuat, dunia cenderung lebih damai.",
        "plain_en": "A concept assessing whether military technology favors the attacker or the defender; when defense has the advantage, peace is much more likely."
    },
    "Deterrence": {
        "plain_id": "Upaya mencegah musuh menyerang dengan cara mengancam bahwa jika mereka berani menyerang, balasan yang akan mereka terima akan jauh lebih menyakitkan daripada keuntungan yang mereka peroleh.",
        "plain_en": "The strategy of preventing an adversary from taking hostile action by threatening retaliation so severe that the costs far outweigh any potential gains."
    },
    "Compellence": {
        "plain_id": "Penggunaan ancaman atau kekuatan militer untuk memaksa pihak lain menghentikan sesuatu yang sedang mereka lakukan atau memaksa mereka melakukan tindakan tertentu yang sebenarnya tidak mereka inginkan.",
        "plain_en": "The coercive use of threats or force to make an adversary stop an ongoing action or do something they do not want to do."
    },
    "Asymmetric Warfare": {
        "plain_id": "Peperangan antara dua pihak yang kekuatan militernya sangat timpang (misal: tentara superpower modern melawan milisi gerilya), di mana pihak yang lebih lemah menggunakan taktik non-konvensional, jebakan, atau perang urat saraf.",
        "plain_en": "Conflict between belligerents whose military power differs vastly, where the weaker party relies on unconventional tactics like guerrilla warfare and ambushes."
    },
    "Hybrid Warfare": {
        "plain_id": "Strategi perang modern yang menggabungkan serangan militer konvensional dengan taktik non-militer seperti peretasan siber, penyebaran hoaks/disinformasi, dan tekanan ekonomi untuk mengacaukan lawan.",
        "plain_en": "A modern military strategy blending conventional military force with cyberattacks, disinformation campaigns, and economic coercion to destabilize an adversary."
    },
    "Responsibility to Protect (R2P)": {
        "plain_id": "Komitmen global bahwa jika suatu negara gagal melindungi rakyatnya sendiri dari genosida, kejahatan perang, atau pembersihan etnis, maka komunitas internasional berhak dan berkewajiban untuk turun tangan.",
        "plain_en": "A global norm stating that if a government is unwilling or unable to protect its citizens from mass atrocities, the international community has a duty to intervene."
    },
    "Nuclear Non-Proliferation Treaty (NPT)": {
        "plain_id": "Traktat internasional 1968 yang melarang negara-negara tanpa senjata nuklir untuk membuatnya, sementara lima negara pemilik nuklir resmi berjanji untuk menuju pelucutan senjata total dan berbagi teknologi nuklir damai.",
        "plain_en": "A landmark 1968 treaty designed to prevent the spread of nuclear weapons, promote disarmament, and encourage peaceful uses of nuclear energy."
    },
    "Mercantilism": {
        "plain_id": "Paham ekonomi klasik yang memandang kekayaan dunia bersifat terbatas. Negara harus memaksimalkan ekspor, membatasi impor, dan menimbun cadangan emas/devisa demi memperkuat kekuatan militer dan politiknya.",
        "plain_en": "An economic philosophy viewing trade as a zero-sum game, where states must maximize exports and restrict imports to amass national wealth and power."
    },
    "Comparative Advantage": {
        "plain_id": "Prinsip ekonomi bahwa setiap negara sebaiknya fokus memproduksi barang yang bisa dibuatnya dengan biaya paling efisien, lalu melakukan perdagangan bebas dengan negara lain sehingga semua pihak menjadi lebih makmur.",
        "plain_en": "The economic principle that countries should specialize in producing goods they can make most efficiently and trade with others, making all trading partners better off."
    },
    "Hegemonic Stability Theory": {
        "plain_id": "Teori bahwa sistem perekonomian dunia hanya bisa stabil dan terbuka jika ada satu negara adidaya (hegemon) yang kuat dan rela membiayai aturan main serta menjamin keamanan perdagangan global.",
        "plain_en": "The theory that the global economy requires a single dominant superpower (hegemon) willing to enforce rules and provide public goods to remain open and stable."
    },
    "Embedded Liberalism": {
        "plain_id": "Sistem ekonomi pasca-PD II yang membuka perdagangan bebas internasional namun tetap memperbolehkan pemerintah dalam negeri membelanjakan uang untuk jaminan sosial dan perlindungan buruh.",
        "plain_en": "The post-WWII economic compromise combining free international trade with domestic government social safety nets to protect citizens from market shocks."
    },
    "Triffin Dilemma": {
        "plain_id": "Dilema di mana negara yang mata uangnya dipakai sebagai cadangan dunia (seperti Dolar AS) terpaksa terus mencetak uang dan mengalami defisit demi mencukupi kebutuhan dunia, namun hal itu lama-lama merusak nilai mata uangnya sendiri.",
        "plain_en": "The paradox where the country supplying the world's primary reserve currency (the US) must run chronic deficits to meet global liquidity needs, which eventually undermines confidence in that currency."
    },
    "Washington Consensus": {
        "plain_id": "Paket resep ekonomi pasar bebas dari IMF dan Bank Dunia untuk negara berkembang yang mengalami krisis, biasanya berupa pemotongan anggaran belanja publik, privatisasi BUMN, dan pembukaan keran investasi asing.",
        "plain_en": "A standard package of free-market policies advocated by the IMF and World Bank for developing economies, emphasizing privatization, deregulation, and fiscal austerity."
    },
    "Dependency Theory (Dependencia)": {
        "plain_id": "Teori dari Amerika Latin yang berargumen bahwa negara-negara miskin di belahan selatan dieksploitasi sumber dayanya untuk memperkaya negara-negara maju di belahan utara melalui sistem perdagangan global yang tidak adil.",
        "plain_en": "A theory arguing that global capitalism keeps developing nations impoverished as mere resource suppliers to enrich industrialized wealthy core nations."
    },
    "Prebisch-Singer Thesis": {
        "plain_id": "Temuan ekonomi bahwa harga bahan mentah (hasil bumi/tambang negara berkembang) cenderung makin murah seiring waktu dibanding harga barang industri manufaktur (dari negara maju), sehingga negara miskin selalu rugi.",
        "plain_en": "The economic observation that the price of primary commodities exported by developing nations declines over time relative to manufactured goods from wealthy nations."
    },
    "Import Substitution Industrialization (ISI)": {
        "plain_id": "Strategi pembangunan ekonomi di mana negara melarang atau mengenakan pajak tinggi pada barang impor agar industri pabrik dalam negeri bisa tumbuh membuat produk pengganti sendiri.",
        "plain_en": "A development strategy where a country restricts foreign imports to foster and protect its own domestic manufacturing industries."
    },
    "Export-Oriented Industrialization (EOI)": {
        "plain_id": "Strategi pembangunan (sukses di Asia Timur seperti Korsel dan Taiwan) yang fokus memproduksi barang berdaya saing tinggi untuk diekspor ke pasar dunia alih-alih hanya mengandalkan pasar lokal.",
        "plain_en": "An economic growth strategy focusing on manufacturing high-quality goods specifically for export to competitive global markets."
    },
    "World-Systems Theory": {
        "plain_id": "Pandangan Immanuel Wallerstein bahwa dunia terbagi menjadi tiga lapis ekonomi: Negara Pusat (kaya dan menguasai teknologi canggih), Negara Semi-Pinggiran (manufaktur menengah), dan Negara Pinggiran (pemasok buruh murah dan bahan baku).",
        "plain_en": "Wallerstein's model dividing the global economy into wealthy core states, exploiting semi-periphery industrial states, and resource-producing periphery nations."
    },
    "Most-Favoured-Nation (MFN)": {
        "plain_id": "Aturan dasar WTO yang mewajibkan negara memperlakukan semua mitra dagangnya secara setara; jika satu negara diberi keringanan tarif bea masuk, keringanan itu otomatis berlaku untuk semua anggota WTO lainnya.",
        "plain_en": "The WTO principle requiring a member state to grant the same favorable trade terms (such as low tariffs) to all other member nations without discrimination."
    },
    "National Treatment": {
        "plain_id": "Prinsip WTO bahwa barang impor yang sudah masuk dan membayar bea cukai tidak boleh didiskriminasi atau dikenai pajak tambahan dibanding barang buatan lokal di pasar dalam negeri.",
        "plain_en": "The WTO rule requiring that once imported goods pass customs, they must be treated no less favorably than locally produced domestic products."
    },
    "Special Drawing Right (SDR)": {
        "plain_id": "Aset cadangan devisa buatan IMF yang nilainya dihitung dari keranjang lima mata uang utama dunia (Dolar AS, Euro, Yuan Tiongkok, Yen Jepang, dan Poundsterling Inggris) untuk membantu negara yang kekurangan likuiditas.",
        "plain_en": "An international reserve asset created by the IMF based on a basket of five major currencies to supplement member countries' official foreign exchange reserves."
    },
    "Pacta Sunt Servanda": {
        "plain_id": "Prinsip hukum paling mendasar bahwa 'janji dan traktat yang telah disepakati wajib ditepati dengan itikad baik' oleh setiap negara yang menandatanganinya.",
        "plain_en": "The foundational legal maxim that treaties and international agreements are legally binding and must be performed in good faith."
    },
    "Jus Cogens (Peremptory Norm)": {
        "plain_id": "Norma tertinggi dalam hukum internasional yang bersifat mutlak dan tidak boleh dilanggar dalam situasi apa pun oleh negara mana pun (contoh: larangan genosida, agresi militer, dan perbudakan).",
        "plain_en": "Fundamental, non-negotiable peremptory norms of international law from which no derogation is permitted (e.g., prohibitions on genocide, torture, and aggressive war)."
    },
    "Opinio Juris Sive Necessitatis": {
        "plain_id": "Keyakinan bahwa suatu kebiasaan dijalankan oleh negara bukan karena sopan santun belaka, melainkan karena mereka yakin tindakan tersebut memang diwajibkan oleh hukum internasional.",
        "plain_en": "The subjective belief by states that a general practice is being carried out because it is required by an underlying international legal obligation."
    },
    "Territorial Sea": {
        "plain_id": "Wilayah perairan laut selebar hingga 12 mil laut dari garis pantai di mana negara pantai memiliki kedaulatan penuh, termasuk atas dasar laut, air, dan ruang udara di atasnya.",
        "plain_en": "A belt of coastal waters extending up to 12 nautical miles from a coastal baseline, over which the state exercises sovereign territorial jurisdiction."
    },
    "Exclusive Economic Zone (EEZ)": {
        "plain_id": "Wilayah laut hingga 200 mil laut dari pantai di mana negara memiliki hak eksklusif untuk mengeksploitasi sumber daya alam (seperti menangkap ikan dan mengebor minyak), namun kapal asing tetap bebas berlayar.",
        "plain_en": "An oceanic zone extending up to 200 nautical miles from shore where a coastal state has exclusive rights to manage natural resources like fisheries and offshore oil."
    },
    "Archipelagic State Principle": {
        "plain_id": "Prinsip Negara Kepulauan (seperti Indonesia) di mana seluruh perairan di antara pulau-pulau ditarik sebagai satu kesatuan wilayah kedaulatan utuh, bukan perairan internasional yang memisahkan daratan.",
        "plain_en": "The UNCLOS legal principle recognizing that waters connecting islands in archipelagic nations (like Indonesia) constitute unified sovereign internal territory."
    },
    "Innocent Passage": {
        "plain_id": "Hak lintas damai bagi kapal asing untuk melintasi laut teritorial negara lain secara cepat dan terus-menerus tanpa mengganggu perdamaian, ketertiban, atau keamanan negara pantai tersebut.",
        "plain_en": "The right of foreign ships to navigate peacefully and continuously through a coastal state's territorial sea without threatening its security or peace."
    },
    "Jus ad Bellum": {
        "plain_id": "Aturan hukum internasional mengenai alasan yang sah untuk memulai perang (dalam Piagam PBB hanya dibolehkan untuk membela diri atau atas mandat resmi Dewan Keamanan PBB).",
        "plain_en": "The criteria under international law that determine whether a state has a legitimate justification for resorting to war or armed conflict."
    },
    "Jus in Bello (International Humanitarian Law)": {
        "plain_id": "Aturan hukum mengenai tata cara berperang di medan tempur (seperti Konvensi Jenewa) yang melarang membunuh warga sipil, mewajibkan merawat tawanan, dan membatasi jenis senjata.",
        "plain_en": "The laws of armed conflict governing conduct during warfare, designed to protect civilians, wounded soldiers, and limit unnecessary human suffering."
    },
    "Persona Non Grata": {
        "plain_id": "Pernyataan resmi bahwa seorang diplomat asing tidak lagi diterima di negara tuan rumah dan harus segera meninggalkan negara tersebut (biasanya akibat skandal mata-mata atau pelanggaran hukum).",
        "plain_en": "A formal diplomatic status meaning an unacceptable individual; used by host governments to expel foreign diplomats."
    },
    "Two-Level Games": {
        "plain_id": "Teori Robert Putnam bahwa dalam diplomasi internasional, seorang pemimpin harus bermain di dua papan catur sekaligus: bernegosiasi dengan negara lain di tingkat internasional dan membujuk parlemen/rakyat di dalam negerinya sendiri.",
        "plain_en": "Robert Putnam's model showing that negotiators must simultaneously bargain with foreign counterparts internationally and persuade their domestic voters and legislatures."
    },
    "Bureaucratic Politics Model": {
        "plain_id": "Teori bahwa kebijakan luar negeri bukan hasil keputusan satu pikiran tunggal yang cerdas, melainkan hasil kompromi dan perebutan pengaruh sengit antarmenteri dan lembaga intelijen di balik pintu tertutup.",
        "plain_en": "The model asserting that foreign policy decisions are messy compromises resulting from bureaucratic competition and bargaining between government agencies."
    },
    "Groupthink": {
        "plain_id": "Kelemahan psikologis kelompok pembuat keputusan yang terlalu ingin rukun sehingga tidak ada yang berani mengkritik ide buruk bos mereka, sering kali berujung pada bencana kebijakan luar negeri.",
        "plain_en": "A psychological phenomenon where a desire for conformity and harmony in a decision-making group suppresses dissenting views, leading to disastrous policy blunders."
    },
    "Soft Power": {
        "plain_id": "Kemampuan suatu negara mempengaruhi negara lain bukan lewat ancaman senjata atau suap uang, melainkan lewat daya tarik budaya, film, musik, nilai demokrasi, dan reputasi moral yang memikat.",
        "plain_en": "The ability to attract and co-opt rather than coerce, shaping preferences through cultural appeal, democratic values, and positive reputation."
    },
    "Public Diplomacy": {
        "plain_id": "Komunikasi langsung yang dilakukan suatu negara kepada masyarakat awam di negara lain (bukan ke pemerintahnya) melalui beasiswa, pertukaran pelajar, dan siaran budaya demi membangun simpati publik.",
        "plain_en": "Government communications and cultural outreach aimed directly at the citizens of foreign countries to build goodwill and mutual understanding."
    },
    "Track II Diplomacy": {
        "plain_id": "Diplomasi informal jalur kedua yang dijalankan oleh para akademisi, LSM, atau mantan pejabat tanpa ikatan resmi pemerintah untuk mencari solusi kreatif atas konflik yang macet di jalur resmi.",
        "plain_en": "Unofficial, informal dialogue conducted by academics, non-governmental figures, and retired diplomats to explore creative solutions to stalled disputes."
    },
    "Politik Bebas-Aktif": {
        "plain_id": "Prinsip diplomasi luar negeri Indonesia sejak Mohammad Hatta 1948: 'Bebas' dari ikatan aliansi blok kekuatan besar dunia, dan 'Aktif' menyumbang peran nyata bagi perdamaian dunia.",
        "plain_en": "Indonesia's foundational foreign policy doctrine: remaining independent from great-power military blocs while actively taking initiatives to promote global peace."
    },
    "ASEAN Way": {
        "plain_id": "Gaya diplomasi khas Asia Tenggara yang mengutamakan musyawarah untuk mufakat, obrolan santai tanpa konfrontasi terbuka, dan pantangan keras mencampuri urusan dalam negeri tetangga.",
        "plain_en": "The distinctive diplomatic norm in Southeast Asia emphasizing informal dialogue, unanimous consensus (musyawarah-mufakat), and strict non-interference in domestic affairs."
    },
    "ASEAN Centrality": {
        "plain_id": "Prinsip bahwa ASEAN harus menjadi pengemudi utama dan tuan rumah netral bagi seluruh arsitektur diplomasi dan dialog keamanan di kawasan Asia-Pasifik dan Indo-Pasifik.",
        "plain_en": "The principle that ASEAN must remain the central driver and neutral convener of regional security dialogues and economic partnerships in the Indo-Pacific."
    },
    "ZOPFAN": {
        "plain_id": "Deklarasi 1971 oleh ASEAN untuk menjadikan Asia Tenggara sebagai 'Zona Perdamaian, Kebebasan, dan Netralitas' yang bebas dari campur tangan pangkalan militer negara-negara adidaya.",
        "plain_en": "The 1971 ASEAN declaration committing member states to keep Southeast Asia a Zone of Peace, Freedom, and Neutrality, free from interference by external superpowers."
    },
    "Strategic Chokepoint": {
        "plain_id": "Jalur laut sempit yang sangat vital bagi perdagangan dunia atau kapal perang (seperti Selat Malaka, Terusan Suez, dan Selat Hormuz); jika tersumbat, ekonomi global bisa lumpuh seketika.",
        "plain_en": "A narrow waterway essential for international maritime trade and military transit (like the Strait of Malacca or Suez Canal) that is vulnerable to blockade."
    },
    "Bandwagoning": {
        "plain_id": "Taktik negara kecil atau lemah yang memilih bergabung dan tunduk ke kubu negara adidaya terkuat yang sedang mengancam mereka demi mendapatkan perlindungan dan sisa keuntungan.",
        "plain_en": "The strategic choice of a weaker state to align with a stronger, threatening superpower in hopes of survival and sharing the spoils of victory."
    },
    "Buck-Passing": {
        "plain_id": "Strategi licik suatu negara yang menghindar dari kewajiban melawan ancaman musuh dengan membiarkan negara tetangganya yang menanggung beban perang dan biaya pertempuran terlebih dahulu.",
        "plain_en": "A diplomatic strategy where a state avoids confronting a rising threat directly, hoping that other nations will absorb the costs and fight the aggressor instead."
    },
    "Chain-Ganging": {
        "plain_id": "Bahaya sistem aliansi yang terlalu kaku di mana negara-negara saling terikat seperti rantai; jika satu sekutu kecil terseret perang, seluruh sekutu besar lainnya otomatis ikut terseret ke dalam perang dunia.",
        "plain_en": "The danger in mutual defense pacts where great powers are unconditionally bound together, allowing a reckless junior ally to drag everyone into a catastrophic major war."
    },
    "Bipolarity": {
        "plain_id": "Sistem politik dunia yang dikuasai oleh dua negara adidaya raksasa yang saling bersaing ketat (seperti era Perang Dingin antara Amerika Serikat melawan Uni Soviet).",
        "plain_en": "An international distribution of power dominated by two rival superpowers (such as the US and USSR during the Cold War)."
    },
    "Multipolarity": {
        "plain_id": "Sistem dunia di mana terdapat tiga atau lebih negara kekuatan besar yang kekuatannya relatif seimbang (seperti Eropa sebelum Perang Dunia I atau dinamika dunia saat ini).",
        "plain_en": "An international system where power is distributed among three or more roughly equal major powers."
    },
    "Unipolarity": {
        "plain_id": "Sistem dunia di mana hanya ada satu negara adidaya tunggal yang tidak tertandingi kekuatan militer dan ekonominya di seluruh bumi (seperti Amerika Serikat pasca runtuhnya Uni Soviet dekade 1990-an).",
        "plain_en": "An international system dominated by a single preeminent superpower whose power vastly exceeds that of any other state."
    },
    "Grand Strategy": {
        "plain_id": "Rencana induk jangka panjang suatu negara yang memadukan seluruh sumber daya militer, ekonomi, diplomasi, dan intelijen untuk mengamankan kepentingan nasionalnya dalam puluhan tahun ke depan.",
        "plain_en": "A state's comprehensive long-term roadmap coordinating military, economic, and diplomatic tools to achieve foundational national security goals."
    },
    "Containment": {
        "plain_id": "Strategi pembendungan yang diterapkan AS selama Perang Dingin untuk mencegah pengaruh komunisme Uni Soviet menyebar ke negara-negara lain di dunia.",
        "plain_en": "The Cold War grand strategy devised by George F. Kennan to prevent the territorial and ideological expansion of Soviet communism."
    },
    "First-Strike Capability": {
        "plain_id": "Kemampuan militer suatu negara untuk meluncurkan serangan nuklir kejutan pertama yang begitu dahsyat sehingga seluruh senjata nuklir musuh hancur sebelum sempat membalas.",
        "plain_en": "The capacity to launch a surprise pre-emptive nuclear attack that completely wipes out an opponent's retaliatory arsenal."
    },
    "Second-Strike Capability": {
        "plain_id": "Kemampuan negara untuk tetap bisa membalas dengan serangan nuklir mematikan meskipun wilayahnya sudah terlebih dahulu dihantam bom nuklir lawan (biasanya berkat kapal selam nuklir tersembunyi).",
        "plain_en": "A country's assured ability to absorb a surprise nuclear attack and still retaliate with devastating nuclear force (typically via submarines), guaranteeing deterrence."
    },
    "Extended Deterrence": {
        "plain_id": "Janji negara adidaya (seperti AS) untuk melindungi sekutunya dengan menggunakan senjata nuklirnya jika sekutu tersebut diserang musuh (sering disebut 'payung nuklir').",
        "plain_en": "A superpower's commitment to protect its non-nuclear allies by extending its nuclear umbrella against foreign aggression."
    },
    "Brinkmanship": {
        "plain_id": "Taktik diplomasi berbahaya di mana satu negara sengaja mendorong krisis militer hingga ke tepi jurang perang untuk memaksa musuh mundur ketakutan.",
        "plain_en": "The practice of pushing a dangerous geopolitical crisis to the very brink of active warfare to force an opponent to back down."
    },
    "Audience Costs": {
        "plain_id": "Hukuman politik di dalam negeri (seperti kalah pemilu atau dicemooh rakyat) yang harus ditanggung oleh seorang pemimpin jika dia sudah mengancam negara lain di depan umum namun kemudian menarik ancamannya.",
        "plain_en": "The domestic political penalty a democratic leader suffers from voters if they issue a public threat or red line against an adversary and then back down."
    },
    "Shadow of the Future": {
        "plain_id": "Konsep teori permainan di mana negara-negara memilih tidak berbuat curang hari ini karena mereka tahu mereka masih harus terus berurusan dan berdagang dengan pihak yang sama di masa depan.",
        "plain_en": "The game-theoretic insight that actors cooperate today because they expect repeated interactions in the future, knowing that cheating will trigger punishment later."
    },
    "Relative Gains": {
        "plain_id": "Kekhawatiran negara bukan hanya pada 'apakah saya untung?', melainkan 'siapa yang untung LEBIH BANYAK daripada saya?'. Jika lawan untung lebih besar, kerja sama sering dibatalkan.",
        "plain_en": "A realist concern where a state cares less about its own absolute gains and more about whether an adversary gains more power from cooperation, creating a future threat."
    },
    "Absolute Gains": {
        "plain_id": "Prinsip kaum liberal di mana negara fokus pada keuntungan bersama secara total; asalkan negara sendiri bertambah kaya atau aman, tidak masalah jika negara rekanan juga ikut bertambah kaya.",
        "plain_en": "A liberal perspective where states focus on whether they achieve a positive net benefit from cooperation, regardless of how much other participants also gain."
    },
    "Collective Security": {
        "plain_id": "Sistem keamanan bersama di mana semua negara sepakat bahwa serangan terhadap satu anggota dianggap sebagai serangan terhadap semua anggota, dan semua negara akan bersatu menghukum sang penyerang.",
        "plain_en": "An institutional system where all member states agree that an attack on any member is considered an attack on everyone, requiring universal collective military response."
    },
    "Collective Defense": {
        "plain_id": "Perjanjian aliansi militer sekelompok negara (seperti Pasal 5 NATO) untuk bersama-sama melawan ancaman militer dari negara musuh di luar aliansi mereka.",
        "plain_en": "A mutual defense alliance (such as NATO Article 5) where member states pledge to fight together against external adversaries outside their coalition."
    },
    "Universal Jurisdiction": {
        "plain_id": "Kewenangan pengadilan di negara mana pun untuk mengadili pelaku kejahatan kemanusiaan terberat (seperti genosida atau penyiksaan), di mana pun kejahatan itu terjadi dan apa pun kewarganegaraan pelakunya.",
        "plain_en": "A legal principle allowing national courts to prosecute perpetrators of heinous international crimes (like genocide) regardless of where the crime occurred or who committed it."
    },
    "Rome Statute": {
        "plain_id": "Perjanjian internasional tahun 1998 yang mendirikan Mahkamah Pidana Internasional (ICC) di Den Haag untuk mengadili individu atas kejahatan genosida, kejahatan terhadap kemanusiaan, kejahatan perang, dan agresi.",
        "plain_en": "The 1998 multilateral treaty establishing the permanent International Criminal Court (ICC) to prosecute individuals for the most serious international crimes."
    },
    "State Immunity": {
        "plain_id": "Kekebalan kedaulatan negara di mana pemerintah suatu negara berdaulat tidak bisa dituntut atau diseret ke pengadilan dalam negeri milik negara lain tanpa izinnya.",
        "plain_en": "The legal principle that a sovereign state cannot be sued or brought before the domestic courts of another state without its consent."
    },
    "Transnational Advocacy Network (TAN)": {
        "plain_id": "Jaringan lintas negara yang terdiri dari aktivis, LSM, media, dan akademisi yang bekerja sama melintasi batas negara untuk mendesak perubahan norma hak asasi manusia atau lingkungan hidup.",
        "plain_en": "Networks of activists, NGOs, and researchers who operate across borders to promote human rights, environmental norms, and policy change."
    },
    "Epistemic Community": {
        "plain_id": "Komunitas para ilmuwan dan pakar yang memiliki keahlian ilmiah khusus di bidang tertentu (misal: perubahan iklim) dan memberikan saran teknis yang mempengaruhi kebijakan para pemimpin dunia.",
        "plain_en": "A network of recognized scientific and policy experts whose authoritative knowledge shapes international agreements on technical issues like climate change."
    },
    "Norm Life Cycle": {
        "plain_id": "Tiga tahap lahirnya aturan etika global: dimulai dari pelopor norma yang mengampanyekannya, lalu menyebar luas diadopsi banyak negara, hingga akhirnya menjadi kewajaran yang diakui otomatis oleh seluruh dunia.",
        "plain_en": "Martha Finnemore and Kathryn Sikkink's model tracking how global ideas evolve: norm emergence, norm cascade (broad acceptance), and norm internalization (taken for granted)."
    },
    "Strategic Culture": {
        "plain_id": "Kebiasaan, memori sejarah, dan nilai-nilai budaya turun-temurun suatu bangsa yang membentuk cara pandang militer dan para pemimpinnya dalam mengambil keputusan perang atau damai.",
        "plain_en": "A nation's shared historical experiences, beliefs, and values that shape how its leaders and military think about the use of force."
    },
    "Paradiplomacy": {
        "plain_id": "Aktivitas diplomasi dan hubungan luar negeri yang dijalankan secara mandiri oleh pemerintah daerah, provinsi, atau kota dengan pihak luar negeri (misal: kerja sama kota kembar *Sister City*).",
        "plain_en": "International relations and diplomatic outreach conducted by subnational governments, such as provinces or cities, rather than the central government."
    },
    "Minilateralism": {
        "plain_id": "Diplomasi kelompok kecil yang melibatkan hanya sedikit negara yang berkepentingan langsung (seperti Quad atau AUKUS) agar bisa mengambil keputusan penting secara cepat tanpa hambatan birokrasi forum besar.",
        "plain_en": "Targeted diplomatic cooperation between small groups of countries (e.g., Quad or AUKUS) designed to act quickly on specific shared security or economic problems."
    },
    "P5 Veto Power": {
        "plain_id": "Hak istimewa lima negara anggota tetap Dewan Keamanan PBB (AS, Rusia, Tiongkok, Inggris, Prancis) untuk membatalkan resolusi apa pun hanya dengan satu suara 'tidak'.",
        "plain_en": "The exclusive power of the five permanent UN Security Council members (US, UK, France, Russia, China) to block any substantive resolution with a single negative vote."
    },
    "Chapter VII Enforcement": {
        "plain_id": "Bab VII Piagam PBB yang memberi wewenang legal terkuat bagi Dewan Keamanan PBB untuk menjatuhkan sanksi ekonomi atau mengerahkan pasukan militer gabungan guna memulihkan perdamaian dunia.",
        "plain_en": "The powerful section of the UN Charter granting the Security Council the legal authority to impose binding sanctions or authorize military force to restore international peace."
    },
    "Bandung Spirit": {
        "plain_id": "Semangat Konferensi Asia-Afrika (KAA) Bandung 1955: persatuan antarbangsa yang baru merdeka untuk melawan kolonialisme, menjunjung kesetaraan ras, dan hidup berdampingan secara damai tanpa memihak blok adidaya.",
        "plain_en": "The principles of anti-colonialism, sovereign equality, and peaceful coexistence established at the historic 1955 Asian-African Conference in Bandung, Indonesia."
    },
    "Wawasan Nusantara": {
        "plain_id": "Doktrin geopolitik Indonesia yang memandang seluruh daratan, kepulauan, dan perairan laut di antara pulau-pulau sebagai satu kesatuan wilayah kedaulatan, politik, ekonomi, dan pertahanan yang tidak terpisahkan.",
        "plain_en": "Indonesia's overarching archipelagic geopolitical vision conceiving its land, islands, and connecting seas as one indivisible sovereign whole."
    },
    "RCEP": {
        "plain_id": "Perjanjian Kemitraan Ekonomi Komprehensif Regional: pakta perdagangan bebas terbesar di dunia yang digagas ASEAN bersama Tiongkok, Jepang, Korsel, Australia, dan Selandia Baru, mencakup sepertiga populasi dan ekonomi bumi.",
        "plain_en": "The Regional Comprehensive Economic Partnership: the world's largest free trade agreement, comprising the 10 ASEAN nations and 5 Indo-Pacific trading partners."
    },
    "CPTPP": {
        "plain_id": "Perjanjian perdagangan bebas berstandar tinggi di lingkar Pasifik (melibatkan 11 negara seperti Jepang, Kanada, Australia, dan Singapura) yang menuntut standar ketat perlindungan hak cipta, buruh, dan lingkungan.",
        "plain_en": "A high-standard mega-regional free trade agreement among 11 Pacific Rim nations promoting deep trade liberalization, intellectual property, and labor protections."
    },
    "Dispute Settlement Body (DSB)": {
        "plain_id": "Badan penyelesaian sengketa di bawah WTO yang bertindak sebagai 'pengadilan dagang' resmi untuk memutuskan apakah suatu negara bersalah menerapkan bea masuk atau pembatasan dagang yang curang.",
        "plain_en": "The WTO's dispute adjudication arm that investigates trade violations and issues binding rulings to resolve international commercial disputes."
    },
    "Anti-Dumping Duty": {
        "plain_id": "Pajak bea masuk khusus yang dipungut oleh suatu negara terhadap barang impor yang sengaja dijual dengan harga super murah di bawah harga pasar wajar demi menghancurkan produsen lokal.",
        "plain_en": "A protective customs tariff imposed on foreign imports that are priced unfairly below their normal market value to harm domestic manufacturers."
    },
    "Countervailing Duty (CVD)": {
        "plain_id": "Bea masuk tambahan yang dikenakan untuk menetralkan subsidi yang diberikan pemerintah asing kepada pabriknya, agar harga barang impor tersebut tidak mendistorsi persaingan yang adil.",
        "plain_en": "An additional tariff imposed on imports to offset unfair subsidies provided by the exporting country's government to its domestic industries."
    },
    "TRIPS Agreement": {
        "plain_id": "Perjanjian WTO yang menetapkan standar perlindungan hukum hak kekayaan intelektual global, termasuk paten obat-obatan, hak cipta software, dan merek dagang.",
        "plain_en": "The WTO agreement setting minimum global standards for the legal protection and enforcement of intellectual property rights, including patents and copyrights."
    },
    "Carbon Leakage": {
        "plain_id": "Kondisi di mana pabrik-pabrik penghasil polusi tinggi memindahkan operasionalnya dari negara yang punya aturan emisi ketat ke negara berkembang yang aturannya lebih longgar, sehingga polusi global sama sekali tidak berkurang.",
        "plain_en": "The situation where businesses relocate pollution-heavy manufacturing to countries with lax climate regulations to evade emissions costs, failing to reduce global emissions."
    },
    "Nine-Dash Line": {
        "plain_id": "Klaim sepihak sembilan garis putus-putus oleh Tiongkok atas hampir seluruh wilayah Laut China Selatan, yang telah diputus tidak memiliki dasar hukum oleh Pengadilan Arbitrase Permanen (PCA) 2016.",
        "plain_en": "Beijing's expansive historical maritime claim covering most of the South China Sea, ruled invalid under UNCLOS by the Permanent Court of Arbitration in 2016."
    },
    "Security Community": {
        "plain_id": "Sekelompok negara (seperti sesama anggota ASEAN atau Uni Eropa) yang hubungan pertemanannya sudah begitu erat dan saling percaya sehingga perang antarsesama anggota menjadi hal yang mustahil dipikirkan.",
        "plain_en": "A group of nations whose mutual trust and integrated institutions have grown so deep that war between them has become virtually unthinkable."
    },
    "Sovereign Wealth Fund (SWF)": {
        "plain_id": "Dana investasi milik negara yang dikumpulkan dari surplus devisa atau penjualan komoditas (seperti minyak) untuk diinvestasikan ke aset-aset bernilai tinggi di seluruh dunia demi kemakmuran generasi mendatang.",
        "plain_en": "A state-owned investment fund that invests public wealth from budget surpluses or resource revenues in global financial assets for future generations."
    },
    "De-Dollarization": {
        "plain_id": "Upaya negara-negara (seperti aliansi BRICS) untuk mengurangi pemakaian mata uang Dolar AS dalam perdagangan internasional dan beralih menggunakan mata uang lokal mereka sendiri.",
        "plain_en": "The strategic effort by nations to reduce reliance on the US Dollar in international trade and currency reserves, switching to alternative currencies or gold."
    },
    "Peacebuilding": {
        "plain_id": "Upaya jangka panjang setelah perang usai untuk membangun kembali sekolah, rumah sakit, perekonomian, dan rekonsiliasi masyarakat agar benih-benih konflik tidak kambuh kembali.",
        "plain_en": "Long-term assistance provided to countries emerging from conflict to restore institutions, heal social trauma, and build conditions for lasting peace."
    },
    "Autarky": {
        "plain_id": "Kebijakan isolasi ekonomi ekstrem di mana suatu negara berupaya mencukupi seluruh kebutuhan pangan dan industrinya sendiri tanpa bergantung sama sekali pada perdagangan luar negeri.",
        "plain_en": "A policy of extreme national self-sufficiency where a country refuses or drastically restricts trade with the outside world."
    },
    "Financial Contagion": {
        "plain_id": "Efek penularan krisis finansial layaknya wabah penyakit; ketika krisis perbankan atau anjloknya mata uang di satu negara merembet cepat meruntuhkan ekonomi negara-negara tetangga.",
        "plain_en": "The rapid spread of financial market turmoil and currency crises from one country to other regional or global economies."
    },
    "Non-Refoulement": {
        "plain_id": "Prinsip hukum internasional mutlak yang melarang suatu negara mendeportasi atau memulangkan pengungsi ke negara asalnya jika di sana mereka terancam siksaan atau pembunuhan.",
        "plain_en": "The fundamental international refugee law principle forbidding countries from expelling asylum seekers to places where their life or freedom would be threatened."
    },
    "Treaty of Amity and Cooperation (TAC)": {
        "plain_id": "Traktat persahabatan 1976 yang menjadi janji suci seluruh negara Asia Tenggara dan mitra luarnya untuk saling menghormati kemerdekaan dan tidak saling menyerang.",
        "plain_en": "The foundational 1976 peace treaty binding ASEAN countries and external partners to peaceful dispute settlement, mutual respect, and non-aggression."
    },
    "AICHR": {
        "plain_id": "Komisi Hak Asasi Manusia Antarpemerintah ASEAN: badan regional resmi yang dibentuk untuk mempromosikan dan melindungi hak-hak dasar warga negara di kawasan Asia Tenggara.",
        "plain_en": "The ASEAN Intergovernmental Commission on Human Rights: ASEAN's official regional body established to promote human rights and fundamental freedoms."
    },
    "Security Sector Reform (SSR)": {
        "plain_id": "Proses penataan kembali militer dan kepolisian di negara pasca-diktator (seperti Reformasi Indonesia 1998) agar militer keluar dari politik praktis dan tunduk di bawah kendali pengawasan pemerintah sipil yang demokratis.",
        "plain_en": "The restructuring of a state's military, police, and intelligence services to ensure they operate under democratic civilian control and uphold human rights."
    },
    "Balance of Threat": {
        "plain_id": "Teori Stephen Walt bahwa negara-negara membentuk persekutuan bukan semata-mata untuk mengimbangi negara yang paling kuat secara militer, melainkan untuk mengimbangi negara yang perilakunya paling mengancam.",
        "plain_en": "Stephen Walt's theory arguing that states align against the countries they perceive as most threatening (based on proximity, aggressive intentions, and power), not simply the strongest state."
    },
    "Liberal International Order (LIO)": {
        "plain_id": "Tatanan dunia berbasis aturan yang dipimpin negara-negara Barat sejak 1945, ditopang oleh perdagangan bebas terbuka, lembaga multilateral (PBB, IMF, WTO), dan penegakan demokrasi serta HAM.",
        "plain_en": "The rules-based international order established after WWII led by the West, underpinned by open markets, multilateral institutions, and democratic norms."
    },
    "Hegemony (Gramscian / Coxian)": {
        "plain_id": "Bentuk dominasi kekuasaan di mana pihak yang berkuasa tidak hanya menggunakan senjata dan polisi, melainkan berhasil membuat pihak yang dikuasai secara sukarela menerima cara pandang penguasa sebagai hal yang wajar dan benar.",
        "plain_en": "A critical theory concept showing that true power dominance relies not just on force, but on shaping ideas and culture so that subordinate classes accept the status quo as natural."
    },
    "Revisionist State": {
        "plain_id": "Negara yang tidak puas dengan tatanan dunia yang ada saat ini dan bertekad mengubah batas wilayah, aturan hukum, atau pembagian kekuasaan global (kebalikan dari negara penjaga status quo).",
        "plain_en": "A state that is deeply dissatisfied with the existing international order and actively seeks to overturn borders, power balances, or international rules."
    },
    "Status Quo State": {
        "plain_id": "Negara yang merasa puas dan diuntungkan oleh tatanan dunia saat ini, sehingga berupaya keras mempertahankan aturan hukum dan pembagian kekuasaan yang sedang berlaku.",
        "plain_en": "A state satisfied with the existing international distribution of power and rules, working to preserve stability and prevent systemic revision."
    },
    "Fragile State": {
        "plain_id": "Negara rapuh yang pemerintahnya sangat lemah atau lumpuh, sehingga tidak mampu menjaga keamanan, menegakkan hukum, atau menyediakan kebutuhan dasar bagi warganya.",
        "plain_en": "A country characterized by severe governance weakness, institutional breakdown, and inability to maintain security or provide basic public services."
    },
    "Non-Aligned Movement (NAM)": {
        "plain_id": "Gerakan Non-Blok (GNB): wadah persatuan lebih dari 120 negara berkembang yang memilih netral dan tidak mau menjadi bidak catur dalam persaingan militer blok-blok negara adidaya.",
        "plain_en": "A forum of 120+ developing nations committed to remaining neutral and independent from the geopolitical rivalries of major power blocs."
    },
    "Hierarchy in International Relations": {
        "plain_id": "Kenyataan bahwa meskipun di atas kertas semua negara berdaulat dan setara, dalam praktik nyata hubungan internasional selalu ada negara kuat yang memimpin dan mendikte negara-negara bawahannya.",
        "plain_en": "The empirical reality that despite formal sovereign equality, world politics features distinct hierarchical relationships where dominant powers exert authority over subordinate states."
    },
    "Rational Choice Theory": {
        "plain_id": "Pendekatan matematika dan logika yang mengasumsikan bahwa para pemimpin politik selalu bertindak rasional dengan menghitung untung-rugi secara cermat demi memaksimalkan hasil terbaik bagi kepentingan mereka.",
        "plain_en": "A theoretical approach assuming political leaders act rationally by weighing costs and benefits to maximize their strategic interests under given constraints."
    },
    "Concert of Democracies": {
        "plain_id": "Gagasan aliansi khusus negara-negara demokratis untuk bekerja sama di luar forum PBB dalam menghadapi ancaman dari negara-negara otoriter.",
        "plain_en": "A proposed international coalition of democratic states operating outside universal bodies like the UN to coordinate security and economic responses to illiberal regimes."
    }
}

def update_glossary():
    # Load existing glossary
    in_file = Path("_data/ir_glossary.json")
    with open(in_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated_count = 0
    for item in data:
        term = item["term"]
        if term in PLAIN_EXPLANATIONS:
            item["plain_id"] = PLAIN_EXPLANATIONS[term]["plain_id"]
            item["plain_en"] = PLAIN_EXPLANATIONS[term]["plain_en"]
            updated_count += 1
        else:
            print(f"Warning: term '{term}' not in mapping!")

    # Write back to _data/ir_glossary.json and assets/data/ir_glossary.json
    with open("_data/ir_glossary.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with open("assets/data/ir_glossary.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully enriched {updated_count} / {len(data)} terms with plain-language notes (Indonesian & English)!")

if __name__ == "__main__":
    update_glossary()
