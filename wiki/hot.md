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

2026-10-07 - Milestone M9: Site-Wide Concept Tooltip & Wikipedia Popover Universal Rollout:
Merespons pertanyaan pengguna mengenai popup keyword yang sebelumnya hanya muncul di Chapter 1 dan mengaudit seluruh halaman web:
1. `Root Cause Diagnosis & Elimination`: Mengidentifikasi bahwa inisialisasi Tippy.js di `_includes/footer.html` masih menargetkan selector GitBook usang `.markdown-section strong, .markdown-section b, mark.nice-mark`. Karena layout Bespoke LMS menggunakan `.course-prose-body`, dan tag `mark.nice-mark` hanya ada secara manual di Bab 1 (`010-ir-study.md`), tooltip sebelumnya tidak terpicu di 160 bab lainnya.
2. `Universal Chapter Rollout Across 161 Chapters`: Memperbarui selector ke `.course-prose-body strong, .course-prose-body b, .course-prose-body mark.nice-mark`, menambahkan filter pengecualian UI (kuis, flashcard, ujian modul, simulasi diplomasi, digest box, header/tabel), membatasi panjang teks <= 5 kata, dan menghindari tabrakan dengan `.ir-term-mention`.
3. `Interactive Styling & Tippy Light/Dark Tokens`: Menambahkan kelas `.keyword-interactive` di `assets/css/course-player.css` dengan garis bawah bertitik halus, hover state aksen, elevated shadow card Tippy, spinner animasi `.loader-spinner`, serta token tema gelap (`body.dark-theme`).
4. `Full English Microcopy & Production Verification`: Seluruh teks kartu popover Wikipedia dan AI fallback diselaraskan 100% ke bahasa Inggris akademik ("Searching Wikipedia...", "📚 Academic Concept"). Terverifikasi aktif di 186 dari 187 halaman HTML build Jekyll (`_site/`) dengan total 4.601 keyword bold interaktif. 369/369 pytest lolos 100%.

2026-10-07 - Milestone M9: Comprehensive Platform English-Only Standardization:
Merespons temuan pengguna mengenai bagian catatan istilah kunci dan popover yang masih berbahasa Indonesia:
1. `In-Lesson Terminology Digest English Overhaul`: Mengubah template kartu istilah di `assets/js/course-player.js` dan `_layouts/chapter.html` agar menampilkan penjelasan bahasa Inggris (`item.plain_en`), label `"In Simple Terms:"`, `"Definition:"`, `"Full Glossary"`, dan badge count `"{N} Key Terms"`.
2. `Floating Term Popover English Overhaul`: Memperbarui tooltip popover inline di `course-player.js` agar menggunakan `item.plain_en`, `"In Simple Terms"`, `"Definition:"`, dan tautan `"Glossary"`.
3. `Curated Glossary (/glossary.html) English Standardization`: Menyelaraskan seluruh teks intro, placeholder pencarian, filter, dan kartu glosarium di `_pages/glossary.md` ke dalam bahasa Inggris akademik (`"In Simple Terms (Plain-Language Note)"`, `"Academic Definition"`).
4. `Global Repository Scan & Verification`: Memindai seluruh 161 bab kurikulum, 18 ujian modul (180 soal), 10 simulasi diplomasi, dan seluruh komponen include/layout, memastikan 0 teks antarmuka berbahasa Indonesia yang tersisa di seluruh platform. 369 unit test pytest lolos 100%.

2026-10-06 - Milestone M9: Learning Videos Vault Architecture & Deterministic Naming System:
Merespons arahan pengguna untuk merender video penjelasan ke dalam folder khusus video pembelajaran dan merancang sistem penamaan yang rapi dan mudah dipantau:
1. `Struktur Direktori learning-videos/`: Membentuk repositori video terpusat di root project dengan pemisahan subfolder: `learning-videos/exports/` (master berkas MP4 1080p), `learning-videos/posters/` (poster/thumbnail PNG), `learning-videos/catalog.json` (metadata katalog untuk integrasi LMS/web), dan `learning-videos/README.md` (dasbor inventarisasi dan status publikasi).
2. `Standar Penamaan Deterministik`: Mengadopsi konvensi `IR_M{Module:02d}_CH{Chapter:03d}_{Title}_{Format}_{Resolution}.{ext}`, contoh konkret: `IR_M01_CH010_Foundations_of_International_Relations_MindMap_1080p.mp4`.
3. `Isolasi Git & Jekyll Build Hygiene`: Menambahkan `learning-videos/exports/*.mp4` ke `.gitignore` untuk melindungi kuota komit GitHub (>100 MB hard limit) dan mendaftarkan `learning-videos` ke daftar `exclude:` di `_config.yml` agar tidak membebani kompilasi statis Jekyll.
4. `Eksekusi Render FlowchartVideo`: Meluncurkan rendering 9.501 frame (5m 16s @ 30 FPS, 1920x1080) komposisi `FlowchartVideo` langsung ke target direktori ekspor.

2026-10-06 - Milestone M9: Mind Map Explanatory English-Only Standardization & Pre-Reading Gateway:
Merespons koreksi pengguna mengenai konsistensi bahasa di seluruh antarmuka web dan materi video:
1. `Strict English-Only Mandate`: Seluruh teks antarmuka, badge, gateway card, dan microcopy web wajib 100% berbahasa Inggris akademik. Mengoreksi badge video menjadi *"🎬 WATCH BEFORE READING (5 MIN)"*, label status *"CONCEPTUAL GATEWAY"*, dan judul default *"Mind Map Explanatory: Core Conceptual Framework"*.
2. `Decluttering via Dynamic Spotlight Dimming`: Kartu fokus aktif berdiri pada kecerahan 100% dengan bayangan fokus, sementara kartu sekitar yang sedang tidak dibahas diredupkan halus ke `opacity: 0.35` (mengeliminasi split-attention effect). Panah yang tidak aktif memudar ke `opacity: 0.20`. Pada panorama overview, seluruh 34 node kembali ke 100%.
3. `Semantic Academic Color Hierarchy`: Menghapus warna pastel acak dan mengadopsi taksonomi teoretis HI yang ketat: Kuning (#FEFCBF - Hub/Pertanyaan Inti), Biru Langit (#BEE3F8 - Aktor Negara & Sistem), Soft Coral (#FED7D7 - Realisme, Anarki, Chokepoints), Mint Green (#C6F6D5 - Liberalisme, Institusi, Kerjasama), Soft Lavender (#E9D8FD - Konstruktivisme, Norma, Wendt), dan Paper White (#FFFFFF - Detail & Kasus).
4. `Dual-Font Captioning Hygiene`: Pemisahan peran kognitif antara font tulisan tangan papan tulis *Patrick Hand* (diagram) dan sans-serif modern *Plus Jakarta Sans* (kapsul subtitle bawah dengan margin aman >280px).
5. `Pre-Reading Explanatory Gateway Card`: Mengintegrasikan kartu video resmi di template master `_layouts/chapter.html` bertanda *"🎬 WATCH BEFORE READING (5 MIN)"* dengan dukungan responsive embed YouTube `@IRinANutshell` dan poster kanvas panorama.

2026-10-06 - Milestone M9: Neural TTS Phonetic Normalization & "911" Audio Fix:
Merespons koreksi pengguna mengenai pelafalan "911" yang terbaca sebagai "nine hundred eleven":
1. `Phonetic Normalization Pipeline`: Mengintegrasikan normalisasi regex pada teks narasi audio di `generate_natural_audio_and_subtitles.py` (`re.sub(r'\b911\b', 'nine-one-one', text)`). Terverifikasi empiris pada fonem Kokoro: '911' (/naɪn hʌndɹɪd ɪlɛvən/) -> 'nine-one-one' (/naɪn wʌn wʌn/).
2. `Clean Display Subtitles`: Mempertahankan teks string "911" dan "No Global 911 Service" pada kartu diagram visual dan caption subtitle bawah untuk estetika dan kenyamanan baca viewer.
3. `Regenerasi Audio & Sinkronisasi`: Berhasil menyintesis ulang `public/voiceover.mp3` (316,69 detik / 9.501 frame @ 30 FPS) dan `public/subtitles.json`. Still render preview frame 2450 sukses terverifikasi sempurna.

2026-10-06 - Milestone M9: Mind Map Explanatory Workflow Standardization & Simulation Cleanup:
Merespons persetujuan resmi pengguna atas rencana implementasi:
1. `Standarisasi Mind Map Explanatory`: Mengkodifikasi format resmi video edukasi ke `.agents/skills/ir-video-director/SKILL.md`, `GEMINI.md` (Pedoman #7), dan `PROJECT.md` (Feature #12 & Milestone M9). Menetapkan kanvas putih 4800x3200, roughjs, font Patrick Hand, dan Hukum Tiga Pilar Kamera (Deep Zoom 2.05x, Stationary Hold v=0, Contextual Zoom-Out 1.15x).
2. `Pembersihan Direktori simulation/`: Menghapus permanen ~3,35 GB data eksperimen usang (openmontage_repo, frames_hybrid, remotion_app, vox-director, dll.). Melestarikan secara eksklusif engine produksi aktif `simulation/ir-motion-library/` dan menyusun `simulation/README.md`.
3. `Verifikasi Sistem`: TypeScript check lulus 0 error (`tsc --noEmit`), smoke render still Remotion sukses dalam 5 detik.

2026-10-06 - Milestone M9: Deep Zoom-In & Contextual Zoom-Out Architecture in Remotion:
Merespons koreksi pengguna terkait perlunya zoom-in nyata saat menjelaskan detail konsep agar teks tidak terlihat kecil:
1. `Deep Zoom-In (1.95x – 2.05x)`: Kamera melakukan zoom-in mendalam saat menjelaskan kartu konsep individual. Kartu mengisi ~42% lebar layar 1080p, ukuran font membesar 200%+ (~44px), teks tulisan tangan sangat tegas dan terbaca tanpa squinting, dengan margin >320px di atas subtitle.
2. `Contextual Zoom-Out (1.15x – 1.20x)`: Saat pengenalan babak/paradigma makro (misal Realisme vs Liberalisme), kamera melakukan zoom-out untuk memperlihatkan struktur percabangan dan kontras antar-teori sebelum menyelam kembali ke detail kartu.
3. `Discrete Travel & Stationary Hold`: Kamera tetap mempertahankan kecepatan nol ($v = 0$) selama 3–10 detik penuh saat narasi berlangsung, memberi waktu membaca yang tenang.
4. `Verifikasi Visual 8 Still Frames`: Preview still terverifikasi 100% di artefak `flowchart-targeted-zoom-gallery.md` memperlihatkan kontras tajam antara zoom-in detail dan zoom-out makro.

2026-10-06 - Milestone M9: Replicated Hand-Drawn Flowchart Video Engine in Remotion:
Merespons arahan langsung pengguna untuk mereplikasi format video orisinal buatannya di YouTube (https://www.youtube.com/watch?v=Sa0PnnZLn0w&t=130s):
1. `Inspeksi Real-Time Viewport YouTube Ground-Truth`: Menganalisis frame $t=25s$, $35s$, $60s$, $110s$, $130s$, $150s$, $180s$, $240s$ via Chrome DevTools MCP: kanvas putih murni `#FFFFFF`, rounded rectangle sketsa tangan organik (double-stroke rough line), isian warna pastel lembut (biru muda `#BEE3F8`, kuning `#FEFCBF`, hijau mint `#C6F6D5`, merah muda `#FED7D7`, putih `#FFFFFF`), font tulisan tangan komik ramah, dan panah sketsa berarah.
2. `Arsitektur Mesin Flowchart Remotion Baru (simulation/ir-motion-library/src/flowchart/)`:
   - *Deterministic RoughJS*: Membangun generator kurva rounded rectangle dan panah konektor dengan seed tetap untuk mencegah flickering antar-frame.
   - *Typography*: Mengintegrasikan `@remotion/google-fonts/PatrickHand` untuk tipografi tulisan tangan alami.
   - *CameraRig 2D Fluid Glide*: Kamera melayang halus (*cosine ease-in-out*) melintasi kanvas 4800x3200 mengikuti koordinat 33 node materi sesuai timeline suara narasi Kokoro-82M.
   - *Pull-Back Panorama (Frame 9200)*: Pada akhir video, kamera mundur berskala `zoom: 0.39` menampilkan pemandangan utuh seluruh peta konsep HI dengan jarak margin yang terkalibrasi presisi.
   - *Subtitle Overlay Bebas Tabrakan*: Kapsul gelap semi-transparan di bagian bawah (`bottom: 28px`) menyajikan subtitle per-kalimat tanpa menghalangi node flowchart.
3. `Verifikasi & Preview Stills`: Kompilasi TypeScript 0 error (`tsc --noEmit`). 9 still frame preview (Frame 1 s.d. 9) berhasil dirender dan didokumentasikan di artefak untuk ditinjau langsung oleh pengguna sebelum eksekusi render final MP4.
   - *The Analyst* (4,8M views): Menggunakan vektor arah kekuasaan dan kompas spasial polimorfik tanpa membaca definisi teks.
   - *BBC Learning English* (280k & 56k views): Metafora ruang sidang (hakim + polisi) vs meja bundar anarki (kursi kosong tanpa penegak hukum) untuk hukum domestik vs internasional.
   - *TED-Ed* (757k views): Animasi rantai kausalitas ekonomi (stempel tarif -> perubahan label harga -> perpindahan massa konsumen -> penumpukan kargo).
   - *CrashCourse* (1M+ & 6,2M views): Mekanika "Thought Bubble" dengan analogi fisik (rig timbangan wortel & tongkat, radar silo rudal).
   - *Heinrich-Böll-Stiftung* (2,65M views): Infografis peta dinamis Asia Tenggara dan animasi palu/sirkulasi konsensus "The ASEAN Way".
   - *One Minute Economics* (965k views): Animasi Prisoner's Dilemma berbasis dua sel penjara dan tombol timer pengakuan, bukan matriks angka 2x2 pasif.
   - *Soomo Learning & Korczyk's Class* (788k & 187k views): Model tabrakan bola biliar Waltz vs jaring benang interdependensi bersinar Liberalisme.
2. `Sintesis Paradigma Video Course Sejati (Anti-Slide Laws)`:
   - *Law 1 (Show the Mechanism, Not the Definition)*: Visual bertugas memperlihatkan mesin kausalitas dan dinamika interaksi, bukan mencatat rangkuman suara.
   - *Law 2 (3-Word On-Screen Rule)*: Teks layar dibatasi ketat hanya untuk label entitas, angka kunci, atau status sistem (nol paragraf, nol bullet point).
   - *Law 3 (Event-Driven State Changes)*: Pergantian state visual dinamis terjadi setiap 4-7 detik mengikuti artikulasi narasi.
   - *Law 4 (Full-Canvas Stage vs Bounded Cards)*: Menghapus batas kontainer kartu/slide; seluruh kanvas 1080p difungsikan sebagai panggung simulasi bebas hambatan.

## Key Recent Facts

- **Milestone M9: 5-Minute Slide Video Course Option A Radical Overhaul (`simulation/ir-motion-library/`)**:
  - *Polymorphic Scene Architecture (`src/course/scenes/`)*: Menggantikan layout 2-kolom statis dengan 8 modul panggung spesifik (`Scene01RadarDock` s.d. `Scene08AcademyCommandCenter`), mendistribusikan visual panggung sebesar 70-80% layar.
  - *Mayer's Cognitive Signaling Alignment*: Menghilangkan dinding teks berbutir (1, 2, 3), menggantinya dengan kartu kaca melayang (*glassmorphic cards*), tag status bertenaga tinggi, dan kutipan kanonik tokoh pendiri disiplin ilmu HI.
  - *TypeScript & Static Inspection*: Kompilasi bersih 0 error (`tsc --noEmit`). 8 still frame preview Option A berhasil di-render dan diverifikasi tanpa distorsi atau overflow. Sesuai komitmen instruksi pengguna, proses render MP4 master final ditahan sampai pengguna memberikan konfirmasi akhir.



- **Milestone M8: IR Motion Graphics Library (`simulation/ir-motion-library/`)**:
  - *Clean-Slate Remotion Architecture*: Diisolasi di `simulation/ir-motion-library/`, diproteksi oleh `.gitignore` dan `_config.yml exclude:` sehingga tidak membebani proses build SSG Jekyll maupun repositori Git.
  - *Kurzgesagt Visual Token System (`src/themes/kurzgesagt.ts`)*: Menyediakan token warna semantik (`deepSpace`, `electricCyan`, `warmAmber`), palet khusus paradigma HI (Realisme: Merah `#FF5252`, Liberalisme: Hijau `#4CAF50`, Konstruktivisme: Lavender `#B388FF`), tipografi proporsional, serta kurva easing frame-level (`snapIn`, `bounce`, `easeOut`).
  - *Phase 1 MVP Components*:
    1. `<AnimatedWorldMap />`: Peta dunia vektor SVG flat dengan animasi pulsing radar markers, kurva kuadratik bezier koneksi traktat/rivalitas, highlight regional, dan focal zoom kamera dinamis.
    2. `<TimelineBar />`: Garis waktu kronologis horizontal dengan auto-calibration tahun, pin milestone bounce-in, dan kartu deskripsi pop-up berlatar blur.
    3. `<ConceptDiagram />`: Diagram teoretis swarakit dengan glowing node cards, vektor relasi berarah, dan pemaparan poin argumentasi bertahap.
  - *Decoupled JSON Data Pipeline*: Modul 010 (Introduction to IR) dimodelkan secara deklaratif di `data/010-intro-ir-assets.json`, memetakan 8 situs sejarah (Aberystwyth 1919, LSE 1924, Westphalia 1648, PBB 1945), 9 tonggak evolusi disiplin ilmu (Thucydides 430 SM s.d. Finnemore-Sikkink 1998), serta triad komparasi paradigma Realisme, Liberalisme, dan Konstruktivisme.
  - *Zero Hallucination & High Rigor*: Seluruh nama tokoh, buku babon, traktat, dan asumsi teori diverifikasi langsung dari kurikulum naskah bab materi asli. Kompilasi TypeScript lulus 100% (`tsc --noEmit`).

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


