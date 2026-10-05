---
title: Agent Lessons Learned & Self-Evaluation Log
description: "A continuously updated memory bank of mistakes, best practices, and operational lessons learned from past tasks across the IR Study Companion project."
trigger: always_on
---

# 2-Tier Continuous Learning & Self-Evaluation SOP

**CRITICAL INSTRUCTION FOR ALL AGENTS AND WORKERS:**
You are required to verify your own compliance, extract actionable operational memory, and maintain empirical rigor across all project tasks.

---

## The 2-Tier Self-Evaluation Framework

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              2-TIER SELF-EVALUATION PROTOCOL                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TIER 1: Internal Turn Retrospective (MANDATORY ON EVERY TURN)                          │
│ • Execute in thought process and conclude response with verification footer.           │
│ • Check: Did you run Turn 1 discovery? Read wiki/hot.md? Target master dataset?       │
│ • Acknowledge any rule omissions or tool execution errors immediately.                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TIER 2: Persistent Memory Bank Logging (AGGRESSIVE - CONTINUOUS LEARNING)              │
│ • Append a new bullet point to `## Lessons Learned` below when ANY of these occur:     │
│   (a) New info is discovered (e.g., rate limits, API behaviors, dependencies).         │
│   (b) Trial-and-error results in a solution or informative failure.                    │
│   (c) Architectural decisions or configurations are made/changed by the user.          │
│   (d) A bug, error, or workflow defect is diagnosed and patched.                       │
│   (e) A milestone or specific task is successfully completed.                          │
│ • NEVER wait for the end of the session. Log it immediately after the adjustment!      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Response Footer Format (Tier 1 Mandatory Template)

Every final assistant response in main chat or subagent handoff report should include:

```markdown
---
**Self-Evaluation:** [Explicit verification of SOP compliance, rules followed, and error checks]
**Autonomous Memory & Second Brain Sync:** [Report of what was automatically updated in lessons-learned.md, wiki/hot.md, or Obsidian notes without asking confirmation]
```

---

## Lessons Learned

- **Linguistic Readability Audit & Global Terminology Note Architecture (2026-10-05)**:
  1. *Empirical Readability Gap Diagnosis*: Pengujian matematis Flesch Reading Ease (22.8/100) dan Flesch-Kincaid Grade Level (Grade 14.6) mengungkap kesenjangan tajam: naskah materi ditulis dengan kepadatan kata polisilabel tinggi (27.0%) dan kalimat panjang (rata-rata 18.0 kata, puncak 26.1 kata), setara level jurnal ilmiah pascasarjana. Kondisi ini menciptakan beban kognitif ganda (bahasa Inggris akademik + jargon teoritis pekat) bagi masyarakat umum atau mahasiswa baru.
  2. *Two-Tier Scaffolding Architecture (Zero Core Regression)*: Menulis ulang seluruh 335.000 kata naskah berisiko merusak integritas literatur kanonik dan memicu regresi pengujian. Solusi pedagogis paling elegan adalah *Term Scaffolding*: (a) *Inline Non-Destructive Annotation*: `TreeWalker` memindai kemunculan pertama 161 istilah kunci tanpa merusak tag HTML/math/code, menampilkan floating popover card saat disentuh/di-hover; (b) *In-Lesson Terminology Digest*: Rangkuman kartu istilah ramah pemula di bagian bawah setiap bab pada master template `_layouts/chapter.html` (otomatis aktif di 100% dari 180 halaman materi); dan (c) *Bilingual Search*: Penjelasan bahasa awam Indonesia (`plain_id`) langsung dapat dicari secara instan di `/glossary.html`.
  3. *Domain-Wide Lexical Expansion*: Glosarium awal 122 konsep menyisakan modul non-teori (Metodologi Penelitian, Politik Domestik Indonesia, Sejarah Dunia Modern) tanpa anotasi. Melalui ekspansi kurasi ke 161 konsep (termasuk otonomi daerah, ambang batas parlemen, penelitian kualitatif/kuantitatif, Tirai Besi), seluruh 18 modul kini memiliki cakupan catatan istilah 100% lengkap.

- **Artisanal Bespoke Chapter Summarization & Zero-Script Scaling (2026-10-05)**:
  1. *The Fallacy of Automated Batch Summaries*: Eksperimen otomatisasi konten membuktikan bahwa skrip pembangkit batch berbasis template cenderung menghasilkan abstrak yang dangkal, generik, dan mengulang-ulang frasa seragam ("Examines the...", "Investigates the..."). Pendekatan artisanal—membaca naskah materi bab per bab secara utuh (`view_file`), mengekstraksi paradoks atau ketegangan intinya, lalu merumuskan 2–4 kalimat bergaya Feynman/Kurzgesagt—menghasilkan lonjakan substansial dalam kualitas pedagogis dan retensi belajar mahasiswa.
  2. *Deterministic Uniqueness Verification*: Menjaga keunikan 100% pada repositori skala besar (161 bab materi) membutuhkan verifikasi matematis otomatis (`scripts/audit_simple_words_uniqueness.py`). Skrip berbasis `collections.Counter` memastikan tidak ada satu pun string duplikat (161 ringkasan unik untuk 161 berkas) dan tidak ada berkas materi yang terlewat.
  3. *Zero-Cliché Stylistic Enforcement*: Menjalankan audit leksikal otomatis (`scripts/audit_full_repo.py`) secara berkala setelah modifikasi teks manual berhasil mendeteksi dan mengeliminasi metafora usang (misal: "crucible of", "from the ashes of") sebelum artefak teks masuk ke produksi.


- **Repository-Wide Anti-Hallucination & Academic Elevation Audit (2026-10-05)**:
  1. *Eradication of Formulaic AI Clichés and Childish Analogies*: Pemindaian dan remediasi deterministik di seluruh 18 modul (162 berkas materi, 335.000+ kata) membuktikan bahwa AI generator cenderung meninggalkan 2 kategori artifak buruk: (a) formula klise repetitif ("delves into", "in today's interconnected world", "pave the way for", "rich tapestry of", "cornerstone of"), dan (b) analogi kekanak-kanakan yang di-copy-paste secara massal pada metadata `simple_summary` ("trading snacks", "magic glasses", "pillow forts", "rules of a playground", "important puzzle piece"). Seluruh 162 berkas kini memiliki abstrak akademik tingkat universitas yang presisi.
  2. *Strict Scholarly & Treaty Grounding*: Seluruh konsep teoretis, traktat internasional, dan tokoh akademik telah di-grounding ke literatur kanonik dengan penanggalan dan keanggotaan mutakhir: keanggotaan NATO 32 sekutu (Finlandia 2023, Swedia 2024), keanggotaan WTO 166 negara (Timor-Leste & Komoro pada MC13 Abu Dhabi 2024), Piagam ASEAN 2007 (mengoreksi salah ketik "Chapter"), populasi Indonesia >278 juta jiwa, dan validasi *jus cogens* Pasal 2(4) serta batas maritim UNCLOS 1982.
  3. *Zero-Regression Multi-Tier Verification*: Setiap klaster dieksekusi secara modular bertahap (Cluster 1 s.d. 5) dan diuji secara otomatis melalui `scripts/scan_cluster.py`, `scripts/audit_full_repo.py`, 369/369 test `pytest`, serta verifikasi build SSG produksi Jekyll bersih tanpa eror (`done in ~44-46s`).

- **Interactive Diplomatic Labs Architecture & Scoped Simulation Pattern (2026-09-17)**:
  1. *Zero-Dependency Pedagogical Engines*: 10 laboratorium diplomasi interaktif membuktikan bahwa simulasi pembelajaran teori HI yang kompleks (Putnam Two-Level Games, Veto P5 DK-PBB, Arms Race Jervis, UNCLOS Maritime Zones, Balance of Power 1914, ASEAN SCS Dispute, Deterrence MAD) dapat dibangun 100% menggunakan vanilla ES6 + CSS tanpa library pihak ketiga atau bundler tambahan.
  2. *Strict CSS Namespace Scoping*: Menggunakan prefix CSS spesifik per simulasi (`.sim-sd-*`, `.sim-unsc-*`, `.sim-tn-*`, `.sim-uz-*`, `.sim-bop-*`, `.sim-scs-*`, `.sim-nd-*`) mutlak diperlukan agar styling elemen simulasi tidak bocor atau merusak hierarki desain platform course player Jekyll.
  3. *Jekyll Asset Exclusion Criticality*: Penambahan modul berat seperti `simulation/` (yang berisi `node_modules` Remotion puluhan ribu berkas) harus segera didaftarkan ke `exclude:` di `_config.yml`. Jika tidak, Jekyll akan mencoba menelusuri dan menyalin seluruh `node_modules` ke `_site`, menyebabkan build tampak macet dan memakan waktu puluhan menit.
- **Crash Course Visual Density & Pacing Formula (2026-09-04)**:
  1. *The 4–8 Second Visual Beat Law*: Pada video edukasi bertempo lincah (160–180 WPM), pergantian atau respons visual harus terjadi setiap 1–2 kalimat (~4 hingga 8 detik). Membiarkan kartu teks statis bertahan selama 25–40 detik memicu kebosanan penonton (*slideshow fatigue*).
  2. *Sentence-Level Beat Synchronization*: Video 10 menit (109 kalimat) membutuhkan minimal 60–70 micro-scenes/beats visual yang terikat langsung ke stempel waktu kalimat (`sentence_timings.json`), dengan ilustrasi aktif (rotating globe, flashing siren, missile silo, exploded tech diagrams, bar chart race), bukan sekadar kotak teks.
  3. *CameraRig & Micro-Motion*: Setiap frame wajib memiliki gerakan kontinu (slow push-in 1.0 $\rightarrow$ 1.06, subtle drift, atau snappy punch-in pada kata kunci penting) agar tidak ada momen visual yang sepenuhnya mati.
- **Long-Form Video Engine Scaling & Local Kokoro-82M Neural Synthesis (2026-09-04)**:
  1. *Remotion 10+ Minute Stability*: Merender video 10+ menit (19.368 frame @ 30 FPS, 1080p) berhasil diselesaikan dalam 16 menit tanpa memory leak dengan membagi arsitektur ke dalam 6 komponen babak independen (`Act1TheHook` s.d. `Act6TheTakeaway`) yang diikat oleh master sequence dan global word-level caption overlay.
  2. *Zero-Cost High-Quality Voiceover via Kokoro-82M ONNX*: Kokoro-82M membuktikan kemampuan menghasilkan vokal ekspresif berbahasa Inggris (`am_adam`, speed=1.12) yang merespons tanda baca alami manusia (pause, em-dash, tanda tanya retoris) dengan biaya Rp 0,- dan inferensi CPU cepat (1.778 kata selesai dalam <2 menit).
  3. *Exact Subtitle Synchronization*: Menghitung durasi audio per kalimat secara deterministik dan memetakan bounding timestamp per-kata ke format `startMs` / `endMs` menghasilkan subtitle karaoke yang 100% sinkron tanpa latensi drift sepanjang 10 menit 45 detik.
- **Faceless Course Production & Multi-Modal Pedagogy (2026-09-03)**: Analisis video Website Learners (9k2c4KIn210) menegaskan bahwa nilai utama platform online course terletak pada kualitas struktur bahan ajar dan media pendukung (slide, audio, infografis), bukan rekaman wajah instruktur. Adaptasi strategis ke IR Study Companion: (1) Ekspor materi bab ke slide PowerPoint (.pptx) untuk dosen/mahasiswa, (2) Audio briefing 3 menit di header bab berbasis neural TTS, (3) Pembuatan cheat sheet infografis SVG per modul, dan (4) Menghindari avatar wajah generatif sintetis yang menurunkan reputasi akademik.
- **VibeCoding Adoption (2026-08-31)**: Dalam mode adopsi, struktur proyek yang sudah berjalan (Jekyll SSG, layout, include, Ruby gems, Python scripts) tidak boleh dirombak atau dipindahkan jalurnya. Folder `.agents/`, `wiki/`, `.obsidian/`, `inbox/`, `.raw/` ditambahkan sebagai pendamping orkestrasi kecerdasan buatan dan Second Brain. `Copy-Item` di PowerShell tidak mendukung `-NoClobber` pada kombinasi parameter tertentu, sehingga penyalinan aman dilakukan dengan memverifikasi direktori sumber dan target.
- **Autonomous Memory Sync Mandate (2026-08-31)**: Sesuai instruksi eksplisit pengguna, pembaruan log pelajaran (`lessons-learned.md`), pembaruan memori proyek (`wiki/hot.md`), dan sinkronisasi Obsidian Vault dieksekusi secara otomatis dan langsung tanpa meminta konfirmasi interaktif di setiap giliran kerja. Laporan pembaruan langsung dimuat di footer tanggapan.
- **Reference & Citation Integrity (2026-08-31)**: Audit otomatis terhadap seluruh referensi terpusat di `_chapters/999-back/010-references.md` membuktikan seluruh 29 DOI terdaftar lolos validasi CrossRef REST API tanpa adanya DOI fiktif. URL berita/institusi (IMF, World Bank, The Diplomat) valid. Oleh karena itu, fokus audit halusinasi dialihkan ke konsistensi substansi konseptual bab dan validitas kunci jawaban kuis.
- **Pytest Discovery with Jekyll SSG Build (2026-08-31)**: Menjalankan `pytest` tanpa argumen akan menduplikasi file test di dalam folder `_site/tests/` dan memicu `ModuleNotFoundError`. Solusi permanen adalah menyetel `-o pythonpath=scripts --ignore=_site` pada Makefile dan eksekusi pengujian.
- **Repository-Wide AI Keyword Formatting Artifacts (2026-08-31)**: AI generator otomatis kerap meninggalkan pola markdown ganda yang rusak saat mem-bold istilah kunci (misal: `**International** Relations**` atau `**trade **policy**`). Pemindaian regex batch di 18 modul (157 bab) berhasil menormalkan 28 bab terdampak sekaligus mengonfirmasi integritas 156 kuis interaktif (semua parameter `correct` memiliki opsi jawaban yang valid).
- **Substantive Factual Audit - Cluster 1: Theory, Methodology & FPA (2026-08-31)**:
  1. *Game Theory Payoff Distortion*: Pada `092-game-theory-ir.md`, teks asli AI mengalami kerancuan parah pada definisi Prisoner's Dilemma (menyebut DD sebagai "mutually preferable"). Telah diperbaiki ke standar formal teori permainan (CC = *Pareto-optimal*, DD = *Nash Equilibrium*, DC/CD = *temptation/sucker's payoff*).
  2. *Two-Level Games (Putnam 1988)*: Pada `080-domestic-politics.md`, terjadi kesalahan penyebutan konstituen "Level 1" pada determinan win-set yang seharusnya konstituen domestik Level II.
---
title: Agent Lessons Learned & Self-Evaluation Log
description: "A continuously updated memory bank of mistakes, best practices, and operational lessons learned from past tasks across the IR Study Companion project."
trigger: always_on
---

# 2-Tier Continuous Learning & Self-Evaluation SOP

**CRITICAL INSTRUCTION FOR ALL AGENTS AND WORKERS:**
You are required to verify your own compliance, extract actionable operational memory, and maintain empirical rigor across all project tasks.

---

## The 2-Tier Self-Evaluation Framework

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              2-TIER SELF-EVALUATION PROTOCOL                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TIER 1: Internal Turn Retrospective (MANDATORY ON EVERY TURN)                          │
│ • Execute in thought process and conclude response with verification footer.           │
│ • Check: Did you run Turn 1 discovery? Read wiki/hot.md? Target master dataset?       │
│ • Acknowledge any rule omissions or tool execution errors immediately.                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TIER 2: Persistent Memory Bank Logging (AGGRESSIVE - CONTINUOUS LEARNING)              │
│ • Append a new bullet point to `## Lessons Learned` below when ANY of these occur:     │
│   (a) New info is discovered (e.g., rate limits, API behaviors, dependencies).         │
│   (b) Trial-and-error results in a solution or informative failure.                    │
│   (c) Architectural decisions or configurations are made/changed by the user.          │
│   (d) A bug, error, or workflow defect is diagnosed and patched.                       │
│   (e) A milestone or specific task is successfully completed.                          │
│ • NEVER wait for the end of the session. Log it immediately after the adjustment!      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Response Footer Format (Tier 1 Mandatory Template)

Every final assistant response in main chat or subagent handoff report should include:

```markdown
---
**Self-Evaluation:** [Explicit verification of SOP compliance, rules followed, and error checks]
**Autonomous Memory & Second Brain Sync:** [Report of what was automatically updated in lessons-learned.md, wiki/hot.md, or Obsidian notes without asking confirmation]
```

---

## Lessons Learned

- **VibeCoding Adoption (2026-08-31)**: Dalam mode adopsi, struktur proyek yang sudah berjalan (Jekyll SSG, layout, include, Ruby gems, Python scripts) tidak boleh dirombak atau dipindahkan jalurnya. Folder `.agents/`, `wiki/`, `.obsidian/`, `inbox/`, `.raw/` ditambahkan sebagai pendamping orkestrasi kecerdasan buatan dan Second Brain. `Copy-Item` di PowerShell tidak mendukung `-NoClobber` pada kombinasi parameter tertentu, sehingga penyalinan aman dilakukan dengan memverifikasi direktori sumber dan target.
- **Autonomous Memory Sync Mandate (2026-08-31)**: Sesuai instruksi eksplisit pengguna, pembaruan log pelajaran (`lessons-learned.md`), pembaruan memori proyek (`wiki/hot.md`), dan sinkronisasi Obsidian Vault dieksekusi secara otomatis dan langsung tanpa meminta konfirmasi interaktif di setiap giliran kerja. Laporan pembaruan langsung dimuat di footer tanggapan.
- **Reference & Citation Integrity (2026-08-31)**: Audit otomatis terhadap seluruh referensi terpusat di `_chapters/999-back/010-references.md` membuktikan seluruh 29 DOI terdaftar lolos validasi CrossRef REST API tanpa adanya DOI fiktif. URL berita/institusi (IMF, World Bank, The Diplomat) valid. Oleh karena itu, fokus audit halusinasi dialihkan ke konsistensi substansi konseptual bab dan validitas kunci jawaban kuis.
- **Pytest Discovery with Jekyll SSG Build (2026-08-31)**: Menjalankan `pytest` tanpa argumen akan menduplikasi file test di dalam folder `_site/tests/` dan memicu `ModuleNotFoundError`. Solusi permanen adalah menyetel `-o pythonpath=scripts --ignore=_site` pada Makefile dan eksekusi pengujian.
- **Repository-Wide AI Keyword Formatting Artifacts (2026-08-31)**: AI generator otomatis kerap meninggalkan pola markdown ganda yang rusak saat mem-bold istilah kunci (misal: `**International** Relations**` atau `**trade **policy**`). Pemindaian regex batch di 18 modul (157 bab) berhasil menormalkan 28 bab terdampak sekaligus mengonfirmasi integritas 156 kuis interaktif (semua parameter `correct` memiliki opsi jawaban yang valid).
- **Substantive Factual Audit - Cluster 1: Theory, Methodology & FPA (2026-08-31)**:
  1. *Game Theory Payoff Distortion*: Pada `092-game-theory-ir.md`, teks asli AI mengalami kerancuan parah pada definisi Prisoner's Dilemma (menyebut DD sebagai "mutually preferable"). Telah diperbaiki ke standar formal teori permainan (CC = *Pareto-optimal*, DD = *Nash Equilibrium*, DC/CD = *temptation/sucker's payoff*).
  2. *Two-Level Games (Putnam 1988)*: Pada `080-domestic-politics.md`, terjadi kesalahan penyebutan konstituen "Level 1" pada determinan win-set yang seharusnya konstituen domestik Level II.
  3. *Atribusi Bibliografi & Biografi Akademik*: Mengoreksi tipografi nama sarjana FPA Greg Cashman (*What Causes War?* 1993, bukan "Crashman"), tahun publikasi buku babon Keohane & Nye *Power and Interdependence* (1977, bukan 1989), dan kewarganegaraan Robert W. Cox (ilmuwan politik kritis asal Kanada).
  4. *Pembersihan Teks Redundan & Frontmatter*: Menghapus seksi ganda Conventional/Critical Constructivism pada `070-constuctivism-ir.md` dan membetulkan metadata judul pada `091-rational-choice.md`.
- **Substantive Factual Audit - Clusters 3, 4 & 5 (History, IPE, Regionalism & Indonesian Politics) (2026-08-31)**:
  1. *Diplomasi Kuno & Konvensi Wina 1961*: Pada `020-history-diplomacy.md`, mengoreksi distorsi kronologi AI "2-4 BCE" untuk Raja-Raja Timur Dekat kuno menjadi Milenium ke-2 SM (Surat Amarna), memperjelas penanggalan VCDR 1961 (berlaku 1964).
  2. *Evolusi TPP ke CPTPP & Berlakunya RCEP*: Pada `050-TPP-RCEP.md`, mengoreksi narasi kedaluwarsa AI yang menyebut "TPP menunggu ratifikasi setelah AS mundur". Diperbarui secara faktual dengan pembentukan CPTPP (berlaku Desember 2018) dan RCEP (berlaku 1 Januari 2022).
  3. *Kronologi Reformasi Sektor Keamanan Indonesia*: Pada `040-civil-military.md`, memperjelas atribusi pemisahan Polri dari TNI (dimulai 1999 masa Habibie, Ketetapan MPR VI & VII/2000 masa Gus Dur) dan UU No. 34/2004 serta penghapusan kursi fraksi TNI/Polri di DPR menjelang Pemilu 2004 pada masa Megawati.
- **Production LMS Theme Upgrade Rollout (Milestone M4) (2026-08-31)**:
  1. *Jekyll Static Engine Non-Destructive Ingestion*: Pembaruan tema produksi ke gaya Utilitarian Skandinavia berhasil diterapkan langsung melalui `custom.css`, `quiz.html`, `flashcards.html`, `chapter.html`, dan `_pages/index.md` tanpa mengubah satu pun dari 157 berkas markdown materi asli.
  2. *Action-Driven Player Flow*: Mengganti tombol navigasi standar menjadi aksi ganda pembelajaran `[ Complete Lesson ]` (yang otomatis mencatat progres ke `localStorage` dan meluncurkan event global `chapter_read`) serta `[ Next Lesson ➔ ]` meningkatkan retensi siswa dan alur belajar linier.
  3. *Zero Build-Breaking Validation*: Eksekusi build Jekyll produksi (`bundle exec jekyll build`) sukses 100% menghasilkan seluruh 157 halaman materi HTML dalam 56 detik tanpa konflik Liquid syntax maupun dependensi eksternal.
- **Scandinavian Design & Interface Engineering Synthesis (2026-08-31)**:
  1. *Evolusi dari GitBook ke Course Player*: Transformasi dari "documentation site" ke "online course platform" menuntut pengalihan paradigma: dari hierarki pasif (*nested links*) ke antarmuka pembelajaran aktif (*learning outcomes*, *action bars*, *monochrome knowledge checkpoints*, *curriculum progress drawers*).
  2. *Scandinavian Neutral Alpha Ladder*: Mengganti gradien warna-warni jenuh (`#4facfe` $\rightarrow$ `#00f2fe`) dengan skala tinta alfa netral atas kanvas putih (`#000` 100%, 64%, 56% terangkat untuk kontras teks instruksional) menciptakan ketenangan visual (*visual restraint*) yang memperkuat fokus membaca materi teori HI yang padat.
  3. *Aturan Presisi jakubkrehel/skills*: Menerapkan *concentric border radius* ($R_{outer} = R_{inner} + padding$), *capped measure* (~68ch), `font-variant-numeric: tabular-nums`, `text-wrap: balance`, dan transisi interupsi instan `cubic-bezier(0.2, 0, 0, 1)` secara signifikan mendongkrak keanggunan dan responsivitas taktil UI tanpa menambah beban runtime/library pihak ketiga.
  4. *Utilitarian Home Academy Architecture*: Beranda kursus modern menolak teks pembuka pasif. Format *Command Center* dengan kartu *Resume Learning* dinamis, *Metrics Strip* terukur (18 modul, 157 bab, 3 lab), katalog 4 *Learning Tracks* tematik, serta *Interactive Simulation Labs Showcase* mengubah mental model pengunjung dari "pembaca pasif dokumentasi" menjadi "pembelajar aktif terpandu".
- **Zero-Budget AI Faceless Video Pipeline Architecture (2026-08-31)**:
  1. *Visual Consistency via Stickman Monochrome DNA (Rollandex v4.3)*: Eksplorasi bookmark X mengungkap bahwa format visual animasi paling tangguh untuk video course edukasi berbiaya nol adalah *white line-art stick figure* pada *pure black background* (`#000000`). Format ini mengeliminasi masalah *character drift* pada AI video generator tanpa membutuhkan compute GPU monster.
---
title: Agent Lessons Learned & Self-Evaluation Log
description: "A continuously updated memory bank of mistakes, best practices, and operational lessons learned from past tasks across the IR Study Companion project."
trigger: always_on
---

# 2-Tier Continuous Learning & Self-Evaluation SOP

**CRITICAL INSTRUCTION FOR ALL AGENTS AND WORKERS:**
You are required to verify your own compliance, extract actionable operational memory, and maintain empirical rigor across all project tasks.

---

## The 2-Tier Self-Evaluation Framework

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              2-TIER SELF-EVALUATION PROTOCOL                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TIER 1: Internal Turn Retrospective (MANDATORY ON EVERY TURN)                          │
│ • Execute in thought process and conclude response with verification footer.           │
│ • Check: Did you run Turn 1 discovery? Read wiki/hot.md? Target master dataset?       │
│ • Acknowledge any rule omissions or tool execution errors immediately.                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ TIER 2: Persistent Memory Bank Logging (AGGRESSIVE - CONTINUOUS LEARNING)              │
│ • Append a new bullet point to `## Lessons Learned` below when ANY of these occur:     │
│   (a) New info is discovered (e.g., rate limits, API behaviors, dependencies).         │
│   (b) Trial-and-error results in a solution or informative failure.                    │
│   (c) Architectural decisions or configurations are made/changed by the user.          │
│   (d) A bug, error, or workflow defect is diagnosed and patched.                       │
│   (e) A milestone or specific task is successfully completed.                          │
│ • NEVER wait for the end of the session. Log it immediately after the adjustment!      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Response Footer Format (Tier 1 Mandatory Template)

Every final assistant response in main chat or subagent handoff report should include:

```markdown
---
**Self-Evaluation:** [Explicit verification of SOP compliance, rules followed, and error checks]
**Autonomous Memory & Second Brain Sync:** [Report of what was automatically updated in lessons-learned.md, wiki/hot.md, or Obsidian notes without asking confirmation]
```

---

## Lessons Learned

- **Vox-Director Architecture & Paper-Collage Mechanics (2026-08-31)**:
  1. *Paper-Collage Look Genesis*: Repositori `Alisa0808/vox-director` membuktikan estetika Vox-explainer bersandar pada pembentukan visual *paper-collage poster* di tahap awal (*torn edges, halftone dots, tape, newspaper strips, bold flat color background*).
  2. *API vs Local-Engine Tradeoff*: Pipeline default-nya mengandalkan Atlas Cloud API (Nano-Banana 2, Gemini Omni Flash, Kling O3 Pro, xAI TTS) dengan biaya ~$1 per 30s video. Namun repositori ini juga menyediakan fallback mesin lokal gratis (`motion.py`, `kenburns.py`, `text_overlay.py`) yang menggerakkan potongan elemen transparan menggunakan Pillow + FFmpeg xfade whip slide tanpa biaya API.
- **Cinematic Clean Layout (2026-08-31)**:
  1. *Elimination of HUD Clutter*: Penonton video dokumenter sejarah YouTube lebih menghargai tampilan visual yang bersih tanpa badge/tag identitas kaku di pojok layar. Menghilangkan elemen HUD pojok kiri atas secara total memberikan kesan sinematik seperti film bioskop/arsip murni (*pure archival reel*), membiarkan rekaman sejarah dan tipografi judul utama menjadi fokus tunggal.
- **VibeCoding Adoption (2026-08-31)**: Dalam mode adopsi, struktur proyek yang sudah berjalan (Jekyll SSG, layout, include, Ruby gems, Python scripts) tidak boleh dirombak atau dipindahkan jalurnya. Folder `.agents/`, `wiki/`, `.obsidian/`, `inbox/`, `.raw/` ditambahkan sebagai pendamping orkestrasi kecerdasan buatan dan Second Brain. `Copy-Item` di PowerShell tidak mendukung `-NoClobber` pada kombinasi parameter tertentu, sehingga penyalinan aman dilakukan dengan memverifikasi direktori sumber dan target.
- **Autonomous Memory Sync Mandate (2026-08-31)**: Sesuai instruksi eksplisit pengguna, pembaruan log pelajaran (`lessons-learned.md`), pembaruan memori proyek (`wiki/hot.md`), dan sinkronisasi Obsidian Vault dieksekusi secara otomatis dan langsung tanpa meminta konfirmasi interaktif di setiap giliran kerja. Laporan pembaruan langsung dimuat di footer tanggapan.
- **Reference & Citation Integrity (2026-08-31)**: Audit otomatis terhadap seluruh referensi terpusat di `_chapters/999-back/010-references.md` membuktikan seluruh 29 DOI terdaftar lolos validasi CrossRef REST API tanpa adanya DOI fiktif. URL berita/institusi (IMF, World Bank, The Diplomat) valid. Oleh karena itu, fokus audit halusinasi dialihkan ke konsistensi substansi konseptual bab dan validitas kunci jawaban kuis.
- **Pytest Discovery with Jekyll SSG Build (2026-08-31)**: Menjalankan `pytest` tanpa argumen akan menduplikasi file test di dalam folder `_site/tests/` dan memicu `ModuleNotFoundError`. Solusi permanen adalah menyetel `-o pythonpath=scripts --ignore=_site` pada Makefile dan eksekusi pengujian.
- **Repository-Wide AI Keyword Formatting Artifacts (2026-08-31)**: AI generator otomatis kerap meninggalkan pola markdown ganda yang rusak saat mem-bold istilah kunci (misal: `**International** Relations**` atau `**trade **policy**`). Pemindaian regex batch di 18 modul (157 bab) berhasil menormalkan 28 bab terdampak sekaligus mengonfirmasi integritas 156 kuis interaktif (semua parameter `correct` memiliki opsi jawaban yang valid).
- **Script & Narration Reconciliation Protocol (2026-08-31)**:
  1. *Substantive Script Divergence Trap*: Jika menggunakan berkas audio narasi gabungan dari tahap pengujian sebelumnya, naskah kalimat narator bisa berbeda dari array kata subtitle (`CaptionOverlay`). Selalu render audio segar yang terikat langsung pada naskah yang sama persis dengan ekstraksi batas kalimat (*SentenceBoundary*) agar kata-kata yang diucapkan narator 100% cocok dengan teks di layar.
  2. *Adaptive Composition Length*: Durasi komposisi Remotion wajib mengikuti durasi audio narator aktual (`durationInFrames = ceil(audio_duration * fps)`), dalam kasus ini 15.5 detik (465 frame @ 30 FPS).
- **Substantive Factual Audit - Cluster 1: Theory, Methodology & FPA (2026-08-31)**:
  1. *Game Theory Payoff Distortion*: Pada `092-game-theory-ir.md`, teks asli AI mengalami kerancuan parah pada definisi Prisoner's Dilemma (menyebut DD sebagai "mutually preferable"). Telah diperbaiki ke standar formal teori permainan (CC = *Pareto-optimal*, DD = *Nash Equilibrium*, DC/CD = *temptation/sucker's payoff*).
  2. *Two-Level Games (Putnam 1988)*: Pada `080-domestic-politics.md`, terjadi kesalahan penyebutan konstituen "Level 1" pada determinan win-set yang seharusnya konstituen domestik Level II.
  3. *Atribusi Bibliografi & Biografi Akademik*: Mengoreksi tipografi nama sarjana FPA Greg Cashman (*What Causes War?* 1993, bukan "Crashman"), tahun publikasi buku babon Keohane & Nye *Power and Interdependence* (1977, bukan 1989), dan kewarganegaraan Robert W. Cox (ilmuwan politik kritis asal Kanada).
  4. *Pembersihan Teks Redundan & Frontmatter*: Menghapus seksi ganda Conventional/Critical Constructivism pada `070-constuctivism-ir.md` dan membetulkan metadata judul pada `091-rational-choice.md`.
- **Substantive Factual Audit - Clusters 3, 4 & 5 (History, IPE, Regionalism & Indonesian Politics) (2026-08-31)**:
  1. *Diplomasi Kuno & Konvensi Wina 1961*: Pada `020-history-diplomacy.md`, mengoreksi distorsi kronologi AI "2-4 BCE" untuk Raja-Raja Timur Dekat kuno menjadi Milenium ke-2 SM (Surat Amarna), memperjelas penanggalan VCDR 1961 (berlaku 1964).
  2. *Evolusi TPP ke CPTPP & Berlakunya RCEP*: Pada `050-TPP-RCEP.md`, mengoreksi narasi kedaluwarsa AI yang menyebut "TPP menunggu ratifikasi setelah AS mundur". Diperbarui secara faktual dengan pembentukan CPTPP (berlaku Desember 2018) dan RCEP (berlaku 1 Januari 2022).
  3. *Kronologi Reformasi Sektor Keamanan Indonesia*: Pada `040-civil-military.md`, memperjelas atribusi pemisahan Polri dari TNI (dimulai 1999 masa Habibie, Ketetapan MPR VI & VII/2000 masa Gus Dur) dan UU No. 34/2004 serta penghapusan kursi fraksi TNI/Polri di DPR menjelang Pemilu 2004 pada masa Megawati.
  1. *Sub-Word Timing & Spacing Integrity*: Pada rendering teks kinetik kata-per-kata (`CaptionOverlay`), pembagian kata berbasis token DOM wajib menyertakan margin horizontal eksplisit (`marginRight: 12px`). Jika hanya mengandalkan inline space, kompresi CSS Remotion dapat menyebabkan kata menempel rapat (`word1word2`). Offset waktu kata dihitung proporsional terhadap boundary kalimat suara neural agar transisi sorotan kuning (`#F59E0B`) pas tepat di bibir narator.
  2. *Diegetic Archival Watermarks*: Tag identitas saluran di pojok kiri atas tidak boleh menggunakan badge modern yang mencolok (seperti bulatan merah neon). Mengubahnya menjadi cap klasifikasi arsip retro beropasitas rendah (`ARCHIVE REF // DOD-1962-OCT`) dengan font monospaced dan border tipis memberikan nuansa rekaman sejarah autentik yang menyatu alami ke latar video.
- **Production LMS Theme Upgrade Rollout (Milestone M4) (2026-08-31)**:
  1. *Jekyll Static Engine Non-Destructive Ingestion*: Pembaruan tema produksi ke gaya Utilitarian Skandinavia berhasil diterapkan langsung melalui `custom.css`, `quiz.html`, `flashcards.html`, `chapter.html`, dan `_pages/index.md` tanpa mengubah satu pun dari 157 berkas markdown materi asli.
  2. *Action-Driven Player Flow*: Mengganti tombol navigasi standar menjadi aksi ganda pembelajaran `[ Complete Lesson ]` (yang otomatis mencatat progres ke `localStorage` dan meluncurkan event global `chapter_read`) serta `[ Next Lesson ➔ ]` meningkatkan retensi siswa dan alur belajar linier.
  3. *Zero Build-Breaking Validation*: Eksekusi build Jekyll produksi (`bundle exec jekyll build`) sukses 100% menghasilkan seluruh 157 halaman materi HTML dalam 56 detik tanpa konflik Liquid syntax maupun dependensi eksternal.
- **Scandinavian Design & Interface Engineering Synthesis (2026-08-31)**:
  1. *Evolusi dari GitBook ke Course Player*: Transformasi dari "documentation site" ke "online course platform" menuntut pengalihan paradigma: dari hierarki pasif (*nested links*) ke antarmuka pembelajaran aktif (*learning outcomes*, *action bars*, *monochrome knowledge checkpoints*, *curriculum progress drawers*).
  2. *Scandinavian Neutral Alpha Ladder*: Mengganti gradien warna-warni jenuh (`#4facfe` $\rightarrow$ `#00f2fe`) dengan skala tinta alfa netral atas kanvas putih (`#000` 100%, 64%, 56% terangkat untuk kontras teks instruksional) menciptakan ketenangan visual (*visual restraint*) yang memperkuat fokus membaca materi teori HI yang padat.
  3. *Aturan Presisi jakubkrehel/skills*: Menerapkan *concentric border radius* ($R_{outer} = R_{inner} + padding$), *capped measure* (~68ch), `font-variant-numeric: tabular-nums`, `text-wrap: balance`, dan transisi interupsi instan `cubic-bezier(0.2, 0, 0, 1)` secara signifikan mendongkrak keanggunan dan responsivitas taktil UI tanpa menambah beban runtime/library pihak ketiga.
  4. *Utilitarian Home Academy Architecture*: Beranda kursus modern menolak teks pembuka pasif. Format *Command Center* dengan kartu *Resume Learning* dinamis, *Metrics Strip* terukur (18 modul, 157 bab, 3 lab), katalog 4 *Learning Tracks* tematik, serta *Interactive Simulation Labs Showcase* mengubah mental model pengunjung dari "pembaca pasif dokumentasi" menjadi "pembelajar aktif terpandu".
- **OpenMontage Agentic Archival Production Pipeline (2026-08-31)**:
  1. *Real Footage Supremacy over Programmer Art*: Eksperimen membuktikan bahwa untuk topik Hubungan Internasional & Geopolitik berat (seperti Krisis Kuba), animasi gambar tangan primitif sering tampak tidak meyakinkan. Arsitektur `documentary-montage` OpenMontage yang memadukan rekaman arsip historis nyata (Archive.org/Prelinger, Wikimedia Commons) dengan tipografi gerak `HeroTitle` (`Space Grotesk`) dan subtitle highlight per-kata (`CaptionOverlay`) memberikan bobot dokumenter sinematik tingkat tinggi dengan biaya API Rp 0,-.
  2. *Archive.org Public Domain Streaming via FFmpeg*: Mengambil cuplikan arsip historis secara langsung dari Archive.org MP4 stream (`ffmpeg -ss <time> -i <url> -t <duration>`) memangkas kebutuhan mengunduh gigabytes file master berukuran besar, menghasilkan potongan klip 1080p yang siap di-grade dalam hitungan detik.
  3. *OpenMontage Remotion Composer Structure*: OpenMontage menggunakan Remotion versi 4.0.484 dengan pustaka internal kaya komponen (`TextCard`, `StatCard`, `CaptionOverlay`, `CinematicRenderer`, `HeroTitle`). Menambahkan komposisi kustom ke `Root.tsx` dan merendernya via `npx remotion render` menghasilkan video edukasi yang sepenuhnya otomatis dan siap unggah ke YouTube.
- **Zero-Budget AI Faceless Video Pipeline Architecture (2026-08-31)**:
  1. *Visual Consistency via Stickman Monochrome DNA (Rollandex v4.3)*: Eksplorasi bookmark X mengungkap bahwa format visual animasi paling tangguh untuk video course edukasi berbiaya nol adalah *white line-art stick figure* pada *pure black background* (`#000000`). Format ini mengeliminasi masalah *character drift* pada AI video generator tanpa membutuhkan compute GPU monster.
  2. *Silent Visuals & Multi-Track Separation*: Prompt video generator (Seedance/Kling Free) wajib berstatus *silent visuals* tanpa teks narasi agar model tidak merender tipografi rusak di layar. Narasi ditangani oleh Edge-TTS (Microsoft Neural Voice gratis tanpa kuota/API key), subtitle otomatis oleh Video Subtitle Master / Whisper, dan SFX diunduh secara terprogram via Pixabay/Mixkit.
  3. *Diffusion Studio CLI & Antigravity Agent Orchestration*: Menggabungkan konsep Apil (@apilpirman) dan Snow Brave (@Sn0wbrave), seluruh proses penyusunan storyboard, peracikan naskah, penjadwalan klip, dan penggabungan video (stitching) dapat diorkestrasi langsung oleh Antigravity Assistant menggunakan skill `.agents/skills/ir-video-director/` dengan total biaya API Rp 0,-.
  4. *Live Simulation Validation (Classical Realism 45s)*: Simulasi end-to-end berhasil menghasilkan video Full HD 1080p berdurasi 45 detik (1.080 frame pada 24 fps) menggabungkan audio Edge-TTS `id-ID-ArdiNeural`, sinkronisasi ritme 4 chapter, dan rendering stickman monokrom via FFmpeg. Ukuran file final sangat efisien (~1.1 MB) dan total biaya eksekusi adalah Rp 0,-.
- **Remotion Video Engine & Headless Chromium Rendering (2026-08-31)**:
  1. *From Primitives to React Spring Physics*: Mengganti skrip Python PIL primitif dengan framework Remotion (`@remotion/cli`, `remotion`, `react`) mengubah grafis menjadi SVG vector tajam, anti-aliasing sempurna via Chromium, dan animasi membal alami menggunakan `spring({ damping: 12, stiffness: 120 })`.
  2. *Remotion Sequence Layout Trap*: Komponen `<Sequence>` Remotion secara default membungkus anak elemen dalam `div` absolut (`position: absolute; inset: 0`). Jika ingin menyelaraskan komponen fleksibel/tengah (seperti banner kinetik), wajib menyertakan properti `layout="none"` agar pembungkus tidak memaksa elemen ke kiri atas.
  3. *Output Directory Pre-Creation*: Perintah `remotion render` akan gagal pada tahap stitching FFmpeg jika folder target output (misal `out/`) belum dibuat di filesystem. Folder wajib dibuat terlebih dahulu (`New-Item -ItemType Directory -Path out -Force`).
- **YouTube Monetization (YPP) Faceless Pipeline Standards (2026-08-31)**:
  1. *Anti-Reused Content Strictness (Higgsfield & ViralFeed)*: YouTube secara sistematis menolak monetisasi (*Ineligible for YPP*) pada channel yang mengandalkan animasi template statis atau slide AI massal berulang. Nilai tambah orisinal (*transformative editorial substance*) wajib dihadirkan melalui naskah analitis kritis, variasi visual adegan per 3–5 detik, dan multi-track audio berbobot.
  2. *High RPM Geopolitics Advantage*: Niche Hubungan Internasional, Diplomasi, dan Geopolitik memiliki nilai CPM/RPM premium (\$4 – \$12 per 1k views). Durasi video ideal untuk retensi dan monetisasi adalah mid-form **3 hingga 5 menit** per episode (didukung Shorts vertikal 50s sebagai *top-of-funnel discovery*).
  3. *OpenMontage Hybrid Archival & Motion Graphic Architecture*: Solusi video tingkat studio tanpa biaya API dicapai dengan memadukan cuplikan rekaman arsip nyata (Wikimedia Commons, Archive.org, Pexels) dengan infografis/peta animasi terprogram (Remotion/SVG/PIL) dan tata suara sinematik multi-track via FFmpeg.
  4. *Wikipedia Media API Best Practices*: Pengunduhan berkas media sejarah dari Wikimedia Commons wajib menyertakan custom `User-Agent` akademis (`IRStudyCompanionBot/1.0`) dan mengambil URL thumbnail melalui endpoint API resmi Wikipedia `prop=pageimages` atau `prop=imageinfo` untuk menghindari HTTP 403 / 429 rate limit.
  5. *Pillow Typography & Layout Safeguards*: Dalam rendering 1080p frame-by-frame, ukuran font teks penjelasan tidak boleh melebihi 36–44pt pada kotak matriks agar teks tidak meluap (*overflow*). Penataan hierarki visual (HUD militer, timer T+s, banner kasus) secara konsisten memberikan impresi dokumenter profesional kelas siaran televisi.
- **Curriculum Drawer DOM Nesting & Scrolling Architecture (2026-08-31)**:
  1. *Premature Container Termination Bug*: Pada Liquid rendering loop Jekyll, variabel `i_prev_part_folder` terisi sejak bagian unnumbered (`000-front`), sehingga pengecekan `if i_prev_part_folder` menutup tag `</ul></div>` secara prematur sebelum modul 1 dimulai. Akibatnya, `drawer-content` (yang memiliki `overflow-y: auto`) menutup sebelum materi, dan seluruh 18 modul tumpah langsung ke `<aside>` tanpa scroll context.
  2. *Stateful Tag Tracking*: Mengganti pengecekan `i_prev_part_folder` dengan boolean flag eksplisit `drawer_group_open` menjamin setiap modul `drawer-module-group` dibuka dan ditutup secara berpasangan, dengan 0 tag mismatch.
- **Historically-Style 2D Cutout & Full English Pipeline Revamp (2026-08-31)**:
  1. *From Slide-Lecture to Dramatic Narrative Storytelling*: Gaya video edukasi membosankan / kaku (slide statis, teks panjang, narasi formal) diubah total ke formula HeyHistorically: narasi Bahasa Inggris yang cepat, renyah, dan dramatis (*"humanity was one bad mood away from nuclear extinction"*), didukung suara neural `en-US-ChristopherNeural` (+5% rate).
  2. *2D Cutout Caricatures & Visual Gags*: Menggantikan foto kotak statis dengan karakter kartun 2D ekspresif (JFK panik dengan tetesan keringat beranimasi, Khrushchev seringai licik) dan elemen analogi komikal (dua truk monster melaju ke jurang untuk mengilustrasikan Chicken Game).
  3. *Kinetic Pill Banners & Camera Dynamics*: Menghindari paragraf panjang dengan memakai *pill banners* melompat, speed rays, snap-zooms, dan screen shakes saat momen tegang. Seluruh pipeline berhasil dirender frame-by-frame (1.488 frame, 62 detik, 1080p 24fps) dengan total biaya API Rp 0,-.
- **PWA Service Worker Cache Traps & CSS Consolidation (2026-08-31)**:
  1. *PWA Stale-While-Revalidate Navigation Trap*: `sw.js` dengan cache statis `ir-companion-cache-v2` mengunci browser pengguna pada aset usang (termasuk `gitbook/style.css` yang telah dihapus). Solusi permanen: menaikkan versi cache menjadi `ir-companion-lms-v3`, menambahkan `self.skipWaiting()` saat instalasi, `clients.claim()` saat aktivasi, dan menggunakan strategi **Network-First** khusus untuk permintaan navigasi halaman HTML (`mode === 'navigate'`).
- **Multi-Layer Dynamic Sticker Motion Mechanics (2026-08-31)**:
  1. *Decomposition of Monolithic Posters*: Menggerakkan 1 poster utuh membuat video explainer terasa kaku seperti slide presentasi. Membedah poster menjadi *isolated sticker cutouts* (seperti potongan Keynes, batangan emas, pintu brankas, dan stempel pita darurat) memungkinkan penerapan animasi gerak berkecepatan beda (*differential parallax*).
  2. *Tactile Physics & Physicality in Remotion*: Menambahkan animasi fisik berbasis pegas (*spring physics*), seperti batangan emas yang membanting jatuh (*slamming drop with impact bounce*), pintu brankas yang terlempar berputar ($-35^\circ$ spin breakaway), dan label mata uang yang mengambang staggered memberikan rasa *tangible paper art* berkualitas tinggi tanpa memerlukan After Effects maupun biaya komputasi GPU berbayar.
- **Zero-Text AI Generation Policy & Native Code Typography (2026-09-02)**:
  1. *AI Image Pseudo-Text Hallucination Trap*: Model AI generator gambar (Diffusion/Midjourney/DALL-E) tidak memproses teks secara semantik, melainkan sebagai coretan pola visual piksel. Meminta AI merender koran, headline, atau grafik ekonomi langsung di dalam gambar selalu menghasilkan ejaan salah / kata semu (*"Honase Yound Briitish Cellegates", "Pixied excha", "Posnafe co"*).
  2. *Strict Separation of Concerns*: Gambar AI HANYA digunakan untuk tekstur kertas, latar belakang datar, dan potongan karakter/objek murni dengan instruksi prompt eksplisit `NO text, NO letters, blank paper only`.
  3. *Native Code-Driven Vector Typography*: Semua elemen teks yang dapat dibaca penonton (Headline, Sub-headline, Kliping Koran, Sumbu & Label Grafik SVG, Lencana Data, Subtitle) dirender 100% via kode React/Remotion + Google Fonts resmi. Hal ini menjamin **100% Zero Typo, resolusi vektor ultra-tajam, dan kemudahan editing teks tanpa perlu merender ulang gambar AI**.
- **Long-Form Educational Video Course Architecture (2026-09-03)**:
  1. *Mid-Form (5+ Minutes) Retention Framework*: Memproduksi video edukasi 5 menit (9.758 frame @ 30 FPS) membutuhkan modularisasi sekuens babak (*The 6-Act Explainer Arc*) daripada satu file komposisi monolitik. Membagi adegan menjadi sub-komponen terisolasi (`Act1InvisibleEmpire` s.d. `Act7Verdict`) mencegah kebocoran memori pada headless Chromium rendering loop.
  2. *Sentence-to-Word Synchronization at Scale*: Ekstraksi event `SentenceBoundary` dari Edge-TTS (`offset` & `duration`) memungkinkan pembagian durasi rata-rata per kata secara otomatis untuk 777 kata, menghasilkan sinkronisasi karaoke subtitle yang presisi tanpa jeda drift audio sepanjang 325 detik.
  3. *Seamless BGM Looping via Remotion `<Loop>`*: Menggunakan pembungkus `<Loop durationInFrames={1200}>` menjamin musik latar mengalun secara berkelanjutan dan konsisten di bawah suara narator tanpa perlu menyambung berkas audio secara manual di FFmpeg.
- **Remotion AI Skills & Shotcraft/Talkcraft Architecture Integration (2026-09-03)**:
  1. *Official Remotion Agent Skills Suite*: Menginstal 12 paket skill resmi `remotion-dev/skills` (`remotion-best-practices`, `remotion-markup`, `remotion-maps`, `remotion-captions`, `remotion-render`, `remotion-studio`, dll.) ke direktori `.agents/skills/`. Memberikan standarisasi aturan animasi interpolasi inline, eliminasi glitch transisi CSS, dan peta interaktif MapLibre tanpa biaya API.
  2. *Video-Shotcraft & Video-Talkcraft Paradigm (Vincentwei1021)*: Mengadopsi dua repositori mutakhir untuk video edukasi:
     - `video-shotcraft`: 157 kartu resep sinematik Remotion, pergerakan kamera 2.5D, pemotongan sinkron ketukan (*beat-synced cuts*), dan tata suara SFX filmis.
     - `video-talkcraft`: Khusus video edukasi / penjelasan naratif (*talking-head / explainer*). Menggantikan kekacauan kolase tabloid Vox dengan **Prinsip Apple / Scandinavian Restraint** (1 aksen warna, hierarki tipografi bersih), **Sistem 7-Lapisan Anti-Slideshow** (*CameraRig*, bidang paralaks dinamis, *idle breathing*, *yield lifecycle* saat elemen baru masuk), serta aturan keras **Evidence-First** (wajib menggunakan rekaman arsip asli `<OffthreadVideo>`, tangkapan layar nyata Playwright, dan diagram vektor, bukan mock UI buatan).
  3. *Pilot Test Validation (Cuban Missile Crisis & Graham Allison Models)*: Pengujian pilot 34,75 detik (1.043 frame @ 1080p 30 FPS) membuktikan keunggulan *video-talkcraft*: footage arsip asli berpadu mulus dengan kartu teori 3-Model Graham Allison, transisi *yield lifecycle* meredupkan Model 1 saat Model 2/3 aktif, dan karaoke subtitle per-kata tersemat stabil tanpa flicker maupun distraksi stiker kartun.
- **Crash Course Pedagogy & Engaging Audio Architecture (2026-09-04)**:
  1. *Deconstructing "Engaging to Listen" (Crash Course ypH6dR7YGfU)*: Daya tarik utama format Crash Course terletak pada perombakan total dari gaya "buku teks monolog" menjadi "percakapan energetik seorang kawan":
     - *Punchy Contrast Hook*: Membuka dengan kontras dramatis & membongkar stereotip membosankan ("Jangan kira HI cuma diplomat tua minum teh...").
     - *Everyday Analogies*: Menjelaskan konsep berat (seperti Anarki internasional) lewat analogi nyata ("Kalau rumah kemalingan panggil polisi, kalau negara diserang tidak ada 911").
     - *Conversational Rhythm & Micro-Humor*: Celetukan spontan dan jeda intonasi yang memecah kebosanan akademis.
  2. *Sonic Landscape Overhaul*: Mengganti BGM drone sinematik berat dengan ritme akustik/indie ceria (115–125 BPM) dengan efek suara punktuatif (*bubble pop, paper whoosh, bell ding*) pada setiap kemunculan istilah kunci.
  3. *Neural TTS Expressiveness Tuning*: Kecepatan narasi disetel di `+8%` s.d. `+10%` dengan aksen intonasi `+2Hz` untuk menghasilkan figur narator yang antusias, cerdas, dan lincah didengar.
- **Language Mandate - English Only for Course Video Production (2026-09-04)**:
  - *User Directive*: Seluruh produksi video edukasi untuk channel YouTube @IRinANutshell dan modul kursus multimedia **wajib selalu dibuat dalam versi Bahasa Inggris**.
  - *Rationale & Voice Profile*: Menyesuaikan standar global *Crash Course* (Complexly), memaksimalkan jangkauan audiens internasional dan monetisasi global, serta memanfaatkan keunggulan variasi suara neural berkualitas tinggi (`en-US-GuyNeural`, `en-US-ChristopherNeural`, `en-US-AvaNeural`) yang memiliki ritme, penekanan intonasi (pitch), dan kejelasan artikulasi CJK/Latin yang superior.
- **Kokoro-82M Local Neural TTS Engine Adoption (2026-09-04)**:
  - *User Selection*: Memilih mesin TTS open-source **Kokoro-82M (ONNX Runtime)** untuk menghasilkan vokal yang responsif terhadap naskah (*script-adaptive prosody*).
  - *Architectural Advantages*:
    1. *Zero Cloud Latency & Zero Cost*: Berjalan 100% lokal pada CPU (82M parameter) tanpa kuota rate limit atau ketergantungan API eksternal.
    2. *Punctuation-Aware Human Cadence*: Peka terhadap tanda baca (`?`, `!`, `--`, `,`) dan ritme bicara santai ala Crash Course host (`am_adam`, `am_michael`).
    3. *Long-Form Scaling*: Mampu menyintesis naskah 1.500+ kata (10+ menit) secara berurutan dengan konsistensi timbre dan zero audio drift.
- **Milestone M7: Online Course Platform Transformation (10-Persona Architecture) (2026-10-05)**:
  1. *Zero-Backend LMS Data Portability*: Mengembangkan sistem sinkronisasi kemajuan (*progress backup & sync*) 100% sisi klien tanpa database backend atau akun pengguna eksternal. Struktur state JSON terkompresi mencakup `chapter_read_*`, `quiz_*`, `exam_*`, dan `bookmark_*` yang dapat diekspor dan diimpor secara instan dengan verifikasi skema, memenuhi kebutuhan persona pembelajar multi-perangkat dan privasi data.
  2. *Build-Time Static Assessment Engines*: Mengkompilasi 180 butir soal ujian akhir modul (10 soal per modul) langsung ke dalam data statis Jekyll (`_data/module_exams.json` & `assets/data/module_exams.json`) menghasilkan latensi 0 ms saat penilaian, passing score threshold 70%, feedback rasional ilmiah komprehensif, serta penanda kelulusan deterministik `exam_module_<id>_passed`.
  3. *Client-Side High-DPI Academic Certificate Generator*: Menggunakan HTML5 `<canvas>` (1600x1130 px @ 2x pixel ratio) untuk merender sertifikat akademik diplomatik berornamen mewah, cap emas timbul bergradien, tanda tangan akademik, dan hash verifikasi SHA-256 yang dihitung secara deterministik dari `nama + spesialisasi + tanggal`. Menghasilkan file PNG beresolusi cetak tinggi tanpa perlu library backend berat seperti Puppeteer atau WeasyPrint.
  4. *Deep Concept Search & Curated Academic Lexicon*: Mengindeks seluruh 162 berkas materi ke dalam payload ringkas JSON (120 KB) untuk pencarian instan di off-canvas drawer, dipadukan dengan kamus 122 konsep dasar Hubungan Internasional (`_pages/glossary.md`) yang dikurasi dengan filter subdisiplin, tokoh kunci, dan tautan silang bab materi.

