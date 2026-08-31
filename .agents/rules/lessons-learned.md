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
  2. *Silent Visuals & Multi-Track Separation*: Prompt video generator (Seedance/Kling Free) wajib berstatus *silent visuals* tanpa teks narasi agar model tidak merender tipografi rusak di layar. Narasi ditangani oleh Edge-TTS (Microsoft Neural Voice gratis tanpa kuota/API key), subtitle otomatis oleh Video Subtitle Master / Whisper, dan SFX diunduh secara terprogram via Pixabay/Mixkit.
  3. *Diffusion Studio CLI & Antigravity Agent Orchestration*: Menggabungkan konsep Apil (@apilpirman) dan Snow Brave (@Sn0wbrave), seluruh proses penyusunan storyboard, peracikan naskah, penjadwalan klip, dan penggabungan video (stitching) dapat diorkestrasi langsung oleh Antigravity Assistant menggunakan skill `.agents/skills/ir-video-director/` dengan total biaya API Rp 0,-.
  4. *Live Simulation Validation (Classical Realism 45s)*: Simulasi end-to-end berhasil menghasilkan video Full HD 1080p berdurasi 45 detik (1.080 frame pada 24 fps) menggabungkan audio Edge-TTS `id-ID-ArdiNeural`, sinkronisasi ritme 4 chapter, dan rendering stickman monokrom via FFmpeg. Ukuran file final sangat efisien (~1.1 MB) dan total biaya eksekusi adalah Rp 0,-.
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
  2. *Legacy Dark Mode CSS Override Purge*: File `_includes/dark_mode.html` memuat baris CSS peninggalan GitBook dengan deklarasi `!important` (`background-color: #111827 !important` dan `#60a5fa !important`) yang menimpa palet Skandinavia ketika OS user mengaktifkan dark mode. Menghapus deklarasi usang tersebut dan memusatkan seluruh variabel tema ke `assets/css/course-player.css` mengembalikan tampilan monokrom bersih yang konsisten.

