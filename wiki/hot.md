---
type: meta
title: Hot Cache
status: developing
created: 2026-08-31
updated: 2026-08-31
tags:
  - meta
  - hot-cache
---

# Recent Context

## Last Updated

2026-10-05 - Audit Keterbacaan Bahasa Repositori & Peluncuran "Global Plain-Language Terminology Engine" (161 Istilah Terkurasi, Berlaku ke 100% Halaman Materi): Audit kuantitatif Flesch-Kincaid mengungkap tingkat kesulitan bahasa akademik setara pascasarjana (FRE 22.8, FKGL Grade 14.6, 27% polisilabel). Diatasi secara menyeluruh melalui mesin catatan istilah dwibahasa otomatis (Indonesia/Inggris), popover tooltip interaktif ramah pemula, digest box "📖 Catatan Istilah Kunci dalam Bab Ini" di seluruh 180 halaman materi, pembaruan master glosarium 161 konsep dengan pencarian dwibahasa, 369/369 pytest lulus, dan build Jekyll sukses tanpa eror.

## Key Recent Facts

- **Global Plain-Language Terminology Note Engine & Readability Audit (ALL PAGES COMPLETED 100%)**:
  - *Empirical Readability Audit*: Skrip `scripts/audit_readability_and_jargon.py` membedah 161 bab materi: rata-rata Flesch Reading Ease berada di angka 22.8 / 100 (*Very Difficult / Post-Graduate Level*), Flesch-Kincaid Grade Level 14.6 (mahasiswa tingkat akhir/S2), 27% kata bersuku kata 3+, dan rata-rata kalimat 18.0 kata. Menunjukkan adanya hambatan ganda (bahasa Inggris ilmiah + jargon teoritis pekat) bagi pembelajar umum.
  - *Comprehensive 161-Term Plain Vocabulary*: Memperluas kamus istilah dari 122 menjadi 161 konsep inti Hubungan Internasional, mencakup metodologi riset HI (kualitatif, kuantitatif, triangulasi, process tracing), politik domestik Indonesia (otonomi daerah, ambang batas parlemen, trias politica, kuota gender), sejarah modern (Perang Dingin, Tirai Besi, aliansi 1914), isu kontemporer (keamanan energi, kejahatan transnasional, populisme, CNN effect), dan hukum internasional (subjek hukum, Konvensi Montevideo).
  - *Bespoke Floating Inline Term Notes*: Mesin client-side di `assets/js/course-player.js` memindai `#course-article-body` secara non-destruktif menggunakan `TreeWalker`, menandai kemunculan istilah khusus pertama dengan garis bawah bertitik hijau (`.ir-term-mention`), dan menampilkan floating popover card saat di-hover/di-tap yang berisi *💡 Maksud Sederhana* dalam bahasa Indonesia awam, definisi akademik ringkas, dan rujukan tokoh.
  - *In-Lesson Terminology Digest Box*: Terpasang di master layout `_layouts/chapter.html`, merangkum secara otomatis kartu catatan istilah khusus yang muncul di bab tersebut tepat di atas navigation dock. Terverifikasi aktif di 180 dari 180 halaman materi (`_site/*.html`).
  - *Enhanced Master Glossary (`/glossary.html`)*: Menampilkan 161 konsep dengan banner hijau zamrud *💡 Maksud Sederhana (Catatan Bahasa Awam)* dan mendukung pencarian dwibahasa (istilah formal Inggris maupun kata kunci bahasa Indonesia).
  - *Zero Regressions*: 369/369 pytest lolos dalam 0.63 detik dan kompilasi build produksi Jekyll tuntas bersih dalam 47-55 detik.


- **Anti-Hallucination & Academic Elevation Audit (ALL 5 CLUSTERS COMPLETED 100%)**:
  - *Cluster 1 (Foundations & Theories — 47 bab)*: Pembersihan klise AI ("delves into", "pave the way", "rich tapestry"), perbaikan formal Game Theory (CC Pareto-optimal, DD Nash Eq), koreksi Putnam Level II, eliminasi analogi formulaik.
  - *Cluster 2 (Security, History & Diplomacy — 46 bab)*: Pemutakhiran NATO 32 anggota, landasan teoretis Wolfers 1952, Buzan 1983, Mearsheimer 2001, Doyle 1983, Zartman 2000, Tallinn Manual 2.0, eliminasi "In a nutshell" & duplicate dividers.
  - *Cluster 3 (IPE & Global Economic Architecture — 35 bab)*: Grounding Susan Strange 1988, Robert Gilpin 1987, Stolper-Samuelson 1941, Rogowski 1989, Mundell-Fleming Trilemma, Kuznets-Piketty-Milanovic, WTO 166 anggota (Timor-Leste & Comoros 2024), eliminasi total analogi "trading snacks".
  - *Cluster 4 (International Law, Regionalism & Indonesia — 47 bab)*: Restorasi judul ASEAN Charter (bukan Chapter), pemutakhiran populasi Indonesia (>278 juta BPS), penegasan *jus cogens* Pasal 2(4) Piagam PBB & UNCLOS 1982, eliminasi analogi "rules of a playground" dan "pillow forts".
  - *Cluster 5 (Comprehensive Assessment & Knowledge Assets)*: Validasi 180 soal ujian di 18 modul (100% valid index, options, dan rasional ilmiah), audit 155 kuis bab, audit 122 entri glosarium, dan konfirmasi zero-hallucination pada seluruh referensi DOI di `010-references.md`.
  - *Automated Verification*: `scripts/audit_full_repo.py` mengonfirmasi 0 AI cliché, 0 childish analogy, 0 duplicate divider di seluruh 162 berkas materi. 369 unit test pytest lolos 100%. Site Jekyll ter-generate sempurna.

- **Milestone M7: Online Course Platform Transformation (COMPLETED)**:
  - Berhasil mentransformasikan IR Study Companion dari platform membaca statis menjadi *Full-Fledged Online Course Academy* setara standar Coursera/edX melalui 3 sprint terintegrasi:
    1. *Progress Backup & Sync Manager*: Modal backup client-side (`_includes/progress_sync_modal.html`) yang mengekspor dan mengimpor riwayat belajar (`.json`) tanpa pelacakan cloud atau akun pihak ketiga.
    2. *Deep Concept Search Engine*: Mengindeks seluruh 162 berkas materi, abstrak, sub-heading, dan kata kunci konseptual (`assets/data/search_index.json`), memungkinkan pencarian teori, traktat, atau tokoh secara instan dari Curriculum Drawer.
    3. *18-Module Summative Assessment System*: 180 soal ujian komprehensif (10 soal per modul) dengan passing grade 70%, feedback rasional ilmiah mendalam, dan status *Module Mastered* (`_includes/module_exam.html`).
    4. *Quiz Explanatory Feedback*: Peningkatan komponen kuis (`_includes/quiz.html`) dengan penjelasan ilmiah (*Scholarly Context & Rationale*) dan link lompat ke bagian teks bab.
    5. *Curated Academic Glossary (`/glossary.html`)*: Kamus referensi akademik berisi 122 istilah fundamental Hubungan Internasional terkurasi mendalam, dilengkapi filter kategori (Teori, Keamanan, IPE, Hukum Internasional, Diplomasi/FPA, Regionalisme/Indonesia), pencarian realtime, dan cross-link materi.
    6. *Elaborate Academic Certificate Generator (`/certificate.html`)*: Generator sertifikat akademik resmi berdesain elaborat (double border klasik, corner flourishes, watermark stempel emas timbul, tanda tangan digital, hash kriptografi SHA-256 verifikasi, dan ekspor instan resolusi tinggi 1600x1130 PNG via HTML5 Canvas).
    7. *Guided Onboarding Tour & Track Recommender*: Orientasi 3 langkah (`_includes/onboarding_modal.html`) menyambut pembelajar baru dan merekomendasikan track belajar yang sesuai.
    8. *Per-Module & Per-Track Progress Bars*: Pill progres persentase realtime di setiap modul pada Curriculum Drawer dan progress bar di 4 kartu track beranda.
    9. *Official YouTube Channel Showcase (@IRinANutshell)*: Seksi pendamping kursus video di beranda yang menghubungkan materi bacaan dengan video penjelasan 10 menit beranimasi.
    10. *Academic Credibility & Editorial Methodology (`/about-me.html`)*: Dokumentasi metodologi peer-review, audit referensi CrossRef DOI, arsitektur pedagogis Taksonomi Bloom, dan komitmen OER.
    11. *Visual Consistency Purge*: Mengeliminasi seluruh sisa gradien biru jenuh (`#4facfe` / `#00f2fe`) di `timeline.html`, `theory_matrix.html`, `geomap.html`, dan `reading_progress.html`, menyelaraskannya ke token desain Skandinavia (*neutral alpha ink ladder*).
    12. *Milestone Celebration Micro-Interaction*: Efek partikel konfeti halus vanilla JS saat siswa lulus ujian modul (skor $\ge 70\%$).
    13. *Professional Print Stylesheet*: Aturan `@media print` untuk mencetak materi bab dan sertifikat ke format A4/PDF yang bersih dan rapi.
- **Interactive Diplomatic Labs Expansion (10 Labs Total - COMPLETED)**:
  - Berhasil merancang, membangun, dan menyematkan 7 simulasi diplomasi baru ke kurikulum (_includes/):
    1. `sim_security_dilemma.html` (Lab 04 - Spiral Model Jervis di `020-realism-security.md`)
    2. `sim_unsc_veto.html` (Lab 05 - Bab VII & Hak Veto P5 di `050-UN-security.md`)
    3. `sim_treaty_negotiation.html` (Lab 06 - Putnam Two-Level Games di `050-tools-diplomacy.md`)
    4. `sim_unclos_zones.html` (Lab 07 - UNCLOS 1982 Maritime Zones di `080-law-of-the-sea.md`)
    5. `sim_balance_of_power.html` (Lab 08 - Aliansi 1914 & Balance of Power di `040-road-to-ww1.md`)
    6. `sim_scs_dispute.html` (Lab 09 - ASEAN Chair & Laut China Selatan di `050-asean-community.md`)
    7. `sim_nuclear_deterrence.html` (Lab 10 - Postur MAD & First/Second Strike di `120-domino-cold-war.md`)
  - Seluruh lab dibangun dengan prinsip *zero external dependencies* (vanilla ES6 + scoped CSS), animasi transisi mulus, feedback analisis teoretis mendalam, dan terhubung ke Homepage Command Center (`_pages/index.md`) dengan metrik 10 Simulation Labs.
- **Structured Learning Tracks 18-Module Full Integration (COMPLETED)**:
  - Mengintegrasikan seluruh 18 modul kurikulum (157 bab) secara komprehensif ke dalam 4 kartu *Structured Learning Tracks* di beranda:
    1. *Track 01 (Foundations & Theories)*: 5 modul (Modul 010, 011, 023, 031, 033 — 42 lessons).
    2. *Track 02 (Security, Warfare & Diplomacy)*: 4 modul (Modul 012, 022, 032, 034 — 42 lessons).
    3. *Track 03 (IPE & Global Architecture)*: 4 modul (Modul 021, 043, 046, 050 — 31 lessons).
    4. *Track 04 (International Law, Regionalism & Indonesia)*: 5 modul (Modul 013, 041, 042, 044, 045 — 42 lessons).
  - Setiap modul kini dilengkapi tautan navigasi langsung ke materi awal dan penghitung jumlah pelajaran presisi (`tabular-nums`). Total: 42 + 42 + 31 + 42 = 157 lessons.
- IR Study Companion merupakan platform studi Hubungan Internasional berbasis Jekyll (Ruby) + otomatisasi Python + Playwright E2E.
- Pondasi proyek asli (chapters, layouts, assets, scripts, test QA) dipertahankan 100% utuh.
- Modul `.agents/`, `wiki/`, `.obsidian/`, `inbox/`, `.raw/`, `GEMINI.md`, `PROJECT.md`, dan `Makefile` telah aktif.
- **Reference Integrity Verified**: Seluruh 29 DOI terdaftar di `010-references.md` terkonfirmasi 100% valid (zero phantom DOI). Laporan lengkap di `wiki/reference_audit_report.md`.
- **Factual & Substance Audit Complete Across All 5 Clusters**:
  1. *Cluster 1 (Theories & FPA)*: Normalisasi formal teori permainan (CC Pareto-optimal, DD Nash Equilibrium di `092-game-theory-ir.md`), koreksi Putnam Level II di `080-domestic-politics.md`, koreksi Greg Cashman, Robert Cox, dan Keohane-Nye (1977).
  2. *Cluster 2 (International Law & IO)*: Menghapus komisi konsiliasi fiktif 1984 di `070-dispute-settlement.md`, validasi batas maritim UNCLOS 1982, pasal 2(4), 51, Bab VII Piagam PBB, dan 4 Konvensi Jenewa 1949 / AP 1977.
  3. *Cluster 3 (World History & Diplomacy)*: Mengoreksi kronologi diplomasi Timur Dekat Kuno (Surat Amarna, Milenium ke-2 SM) dan adopsi Konvensi Wina 1961 (berlaku 1964) di `020-history-diplomacy.md`.
  4. *Cluster 4 (IPE & Architecture)*: Memutakhirkan evolusi dari TPP pasca mundurnya AS ke CPTPP (berlaku 2018) dan berlakunya RCEP (1 Januari 2022) di `050-TPP-RCEP.md`.
  5. *Cluster 5 (Security, ASEAN & Indonesia)*: Menyelaraskan kronologi pemisahan Polri dari ABRI/TNI (1999–2000), UU TNI No. 34/2004, dan penghapusan fraksi militer di DPR sebelum Pemilu 2004 di `040-civil-military.md`.

- **Crash Course Visual Density & Rapid-Fire Pacing Overhaul (COMPLETED)**:
  - Berhasil merombak total master video 10 menit berdurasi **10 Menit 45 Detik (645,65 detik / 19.368 frame @ 1080p 30 FPS Full HD)** menjadi **50+ rapid-fire visual beats** (setiap 4–8 detik / 1–2 kalimat berdasarkan `sentence_timings.json`).
  - Dilengkapi CameraRig kinetik (*continuous push-in* $1.0 \rightarrow 1.05$ & *spring bounce*), ilustrasi vektor aktif (bola dunia berputar, lampu sirine berkedip, silo nuklir, telepon 911, piramida bertingkat vs dataran datar, balapan grafik batang Apple $3T vs negara, ring tinju Realisme vs Liberalism, dan pembedahan komponen smartphone), mengeliminasi penuh kebosanan slide statis.
  - File master `simulation/openmontage_repo/remotion-composer/out/crashcourse_ir_episode1_10min.mp4` (93.9 MB) berhasil dirender dan didokumentasikan di artefak walkthrough.
- **Official YouTube (@IRinANutshell) - Full 10-Minute Master Video Course Produced**:
  - Berhasil memproduksi episode video edukasi berdurasi penuh **10 Menit 45 Detik (645,65 detik / 19.368 frame @ 1080p 30 FPS Full HD)** berjudul *"Crash Course International Relations #1: The Anarchy Problem — Who's in Charge of the Planet?"*, mengadaptasi kurikulum [Bab 010: Pengantar Studi Hubungan Internasional](file:///d:/PERSONAL%20PROJECT/IR-study-companion/_chapters/010-Introduction-to-IR/010-ir-study.md).
  - Vokal narasi 1.778 kata (107 kalimat) disuarakan secara 100% lokal oleh **Kokoro-82M ONNX** (`am_adam`, speed=1.12) dengan biaya komputasi Rp 0,-.
  - Subtitle *word-level highlight* (1.778 kata) diselaraskan secara akurat per-milisidetik mengikuti artikulasi suara neural narator dengan zero desynchronization.
  - Struktur 6 Babak (*The 6-Act Crash Course Arc*): The Hook & 8B Counter, What is Anarchy (No 911), Montevideo 1933 & Westphalia 1648, Non-State Titans (Apple $3T vs National GDP), The Anarchy Paradox (Realism vs Liberalism & Smartphone test), dan Outro/Takeaway @IRinANutshell.
  - File master `simulation/openmontage_repo/remotion-composer/out/crashcourse_ir_episode1_10min.mp4` (62.2 MB) dan 6 still frame kunci berhasil dirender dan didokumentasikan di artefak walkthrough.
- **Kokoro-82M Local Neural Engine Adopted**: Mengintegrasikan model open-source SOTA **Kokoro-82M (ONNX Runtime)** untuk menghasilkan vokal narasi bahasa Inggris yang ekspresif, responsif terhadap tanda baca naskah, dan 100% lokal di CPU (Rp 0,-).
- **Language Mandate (English Only)**: Sesuai arahan eksplisit pengguna, seluruh produksi video course untuk channel YouTube (@IRinANutshell) dan media ajar interaktif **selalu dibuat dalam versi Bahasa Inggris**.
- **Crash Course Pedagogy & Audio Formula Adopted**:
  - Mengadopsi formula narasi dan lanskap audio video edukasi terkemuka **[Crash Course Geology #1](https://www.youtube.com/watch?v=ypH6dR7YGfU)** ke dalam produksi video IR Study Companion (@IRinANutshell).
  - Mengubah paradigma penyampaian materi dari "ceramah kuliah monolog yang kering" menjadi "percakapan lincah dan memikat" dengan analogi konkret, humor cerdas, tempo energetik (+8% s.d. +10% rate), dan ritme BGM akustik yang memompa dopamin belajar.
  - Membuat sampel audio pilot versi Bahasa Indonesia (`crashcourse_ir_id.mp3`) dan Bahasa Inggris (`crashcourse_ir_test.mp3`) untuk materi Bab 010 (Konsep Anarki & Mengapa Negara Bertengkar).
- **Remotion AI Skills & Shotcraft/Talkcraft Integrated**:
  - Menginstal seluruh paket resmi **Remotion AI Skills** (`npx skills add remotion-dev/skills`) ke `.agents/skills/` (`remotion-best-practices`, `remotion-markup`, `remotion-maps`, `remotion-captions`, dll.).
  - Mengintegrasikan **`video-shotcraft`** (157 kartu resep sinematik Remotion) dan **`video-talkcraft`** (mesin video edukasi/penjelasan naratif dengan sistem 7-lapisan anti-slideshow dan tipografi elegan ala Apple/Skandinavia).
- **Official YouTube Revamp (@IRinANutshell) - 5-Minute Full-Length Course Produced**:
  - Berhasil memproduksi episode video edukasi berdurasi penuh **5 Menit 25 Detik (9.758 frame @ 1080p 30 FPS)** berjudul *"The Dollar Empire: How Global Money Was Manufactured — And Why It Might Collapse"*, mengadaptasi materi [Bab 080: Sistem Moneter Internasional](file:///d:/PERSONAL%20PROJECT/IR-study-companion/_chapters/021-international-political-economy/080-monetary-system.md).
  - Naskah 777 kata disuarakan secara neural (`en-US-ChristopherNeural`, +4% pace) dengan sinkronisasi karaoke subtitle per-kata yang presisi (0 desinkronisasi).
  - Membagi alur ke dalam 6 babak kurikulum IPE (*The 6-Act Explainer Arc*) menggunakan motion graphics multi-layer, diagram SVG asli (Triffin curve, Petrodollar loop, Trade routes), kliping koran vintage 1944, dan penerapan penuh **Zero-Hallucination Policy** (0 typo).
  - File master `simulation/openmontage_repo/remotion-composer/out/vox_course_5min.mp4` (160.8 MB) dirender 100% lokal dengan biaya Rp 0,-.
- **Official YouTube Revamp (@IRinANutshell) - OpenMontage V2 Refined**:
  - Mengklon dan mengonfigurasi repositori resmi **OpenMontage** (`calesthio/OpenMontage`) di `simulation/openmontage_repo/`.
  - Berhasil merender video pilot sinematik revisi V2 **1080p 30 FPS** (`simulation/openmontage_repo/remotion-composer/out/openmontage_cuba_v2.mp4`):
    - Subtitle *word-level highlight* telah diselaraskan secara akurat per-milisidetik mengikuti artikulasi suara neural narator, dengan jarak spasi kata yang rapi.
    - Tag di pojok kiri atas diubah dari badge modern mencolok menjadi *Vintage Military Archive Slate* (`ARCHIVE REF // DOD-1962-OCT`) dengan font typewriter monospaced dan opasitas 50% yang menyatu harmonis dengan rekaman arsip tahun 1962.
    - Biaya eksekusi tetap **Rp 0,-** (100% open source & lokal).
- Pembuatan **Interactive Course Platform Prototype** di folder terisolasi `prototype/` (`index.html`, `prototype.css`, `prototype.js`) memadukan skill `scandinavian-design` dan `jakubkrehel/skills`.
- Pembuatan **Utilitarian Home Academy Prototype** di `prototype/home.html` lengkap dengan Command Center, Resume Learning widget, 4 Structured Tracks, dan Interactive Labs Showcase.
- **Eksekusi Sukses Milestone M4 (Production Theme Upgrade)**:
  1. `assets/gitbook/custom.css`: Penerapan token desain Skandinavia (*neutral alpha ink ladder*, *concentric border radius*, *capped measure* ~68ch, dan *tabular nums*).
  2. `_includes/quiz.html`: Transformasi ke gaya kuis monokrom Skandinavia yang tenang, konsisten, dan aksesibel.
  3. `_includes/flashcards.html`: Transformasi ke kartu konsep Active Recall 3D flip minimalis dengan elevasi bayangan halus.
  4. `_layouts/chapter.html`: Penambahan aksi pembelajaran Course Player (`[ ✓ Complete Lesson ]` dan `[ Next Lesson ➔ ]`).
  5. `_pages/index.md`: Beranda produksi kini resmi beralih ke *Utilitarian Course Academy Dashboard* lengkap dengan Resume Learning Card dinamis, Metrics Strip, 4 Structured Tracks, dan Interactive Labs Showcase.
- **Eksekusi Sukses Milestone M5 (Bespoke Native LMS Engine Overhaul)**:
  1. `_config.yml`: Mencopot `remote_theme: jasongrimes/jekyll-chapterbook` secara permanen.
  2. `_layouts/default.html`: Menghapus seluruh struktur DOM GitBook (`.book`, `.book-summary`, `.book-header`). Digantikan dengan modern LMS shell (`.lms-topbar`, `.lms-main-viewport`, dan `.lms-curriculum-drawer`).
  3. `_layouts/chapter.html`: Ditransformasikan menjadi *Course Player Focus View* bebas distraksi dengan metadata bar (durasi baca otomatis), on-page outline navigasi sticky, dan *sticky action dock*.
  4. `_includes/curriculum_drawer.html` & `assets/js/course-player.js`: Drawer silabus off-canvas modern dengan status centang realtime (`localStorage`), pencarian instan 157 materi, dan shortcut keyboard `S`/`Esc`.
  5. `_includes/head.html` & `_includes/footer.html`: Membersihkan script dan stylesheet usang GitBook 2016.
  6. **Permalinks & Navigation Audit**: Mengoreksi seluruh tautan di `_pages/index.md` dari format path direktori lama ke flat slug permalinks (`/:slug.html`), menautkan anchor simulasi (`#crisis-sim`, `#game-theory-sim`, `#wto-sim`), dan mengonfirmasi 0 broken link di seluruh 2.828 file output build.
- Pengujian otomatis `pytest` (6 passed) dan build Jekyll produksi 100% sukses tanpa galat (157 bab terkompilasi dalam 80 detik).
- **PWA Service Worker Cache Busting & Legacy Styling Purge**:
  - Memperbaiki isu halaman live Netlify yang masih menyajikan tampilan lama pada browser pengguna karena caching PWA.
  - Memperbarui `sw.js` ke `CACHE_NAME = 'ir-companion-lms-v3'`, menambahkan `skipWaiting()` dan `clients.claim()`, serta mengaktifkan strategi **Network-First** khusus permintaan navigasi HTML.
  - Menghapus 76 baris CSS GitBook usang di `_includes/dark_mode.html` dan mencopot pemanggilan `assets/gitbook/custom.css` di `_includes/head.html`.
- **Analisis AI Course Workflow & Ekspansi Pedagogis (Video: 9k2c4KIn210)**:
  - Mengkaji arsitektur produksi kursus tanpa kamera (*faceless online course*) dari video *Website Learners* ("How To Create an Online Course For Beginners (Without Filming Yourself)").
  - Mengidentifikasi 4 pilar ekspansi strategis untuk IR Study Companion:
    1. *Programmatic Slide Deck Generator (`.pptx` / PDF)* untuk 157 bab agar dapat langsung diunduh dan digunakan dosen/mahasiswa HI dalam perkuliahan/seminar.
    2. *Multi-Modal Chapter Audio Briefings / Mini-Podcast* (player audio ringkasan eksekutif 3 menit di setiap awal bab berbasis neural TTS / NotebookLM paradigm).
    3. *One-Page Visual Policy Briefs / Cheat Sheets* (infografis terstruktur berbasis SVG per modul studi).
    4. *Industrialisasi YouTube Automation (@IRinANutshell)* mengintegrasikan template Remotion best practices ke dalam CLI lokal untuk merender video materi secara mandiri.
  - Menolak pendekatan avatar wajah sintesis murahan (GravityWrite) demi mempertahankan otoritas ilmiah dan estetika sinematik/arsip dokumenter.


