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

- **Hermes Desktop Migration & Cross-Agent Linear Workflow Protocol (2026-10-07)**:
  1. *The Trap of Chat-Centric vs Repository-Centric Memory*: Migrasi antar-platform agen (misal dari Google Antigravity ke Hermes Desktop) rentan mengalami *context amnesia*, perombakan fitur yang tidak perlu, dan hilangnya histori progres jika agen hanya bergantung pada jendela konteks percakapan. Solusi deterministiknya adalah memusatkan seluruh state pada repositori (*Repository as Single Source of Truth*): `PROJECT.md` untuk roadmap/milestone, `wiki/hot.md` untuk active working cache, dan `.agents/rules/lessons-learned.md` untuk katalog bug yang sudah terpecahkan.
  2. *Dedicated Bootstrap Gateway (`HERMES.md`, `AGENTS.md`, & `IDEA.md`)*: Menyediakan berkas instruksi khusus di root repositori (`HERMES.md`, universal `AGENTS.md`, dan dialog summary `IDEA.md`) yang merangkum peran persona, 5-Step Linear Execution Loop, batas pengujian (`make test`, Jekyll build), dan guardrails repositori (English-only UI, 10 Diplomatic Labs, standar video Remotion RoughJS). Pendekatan *zero-configuration* berbasis file ini membebaskan pengguna dari keharusan mengatur *custom profile* atau *system prompt* di GUI agen; cukup satu kalimat prompt pembuka ("Baca HERMES.md sebelum mulai"), agen langsung beroperasi linier.
  3. *The 5-Step Linear Loop*: Menjaga kemajuan tetap lurus (linear) dengan siklus deterministik: (1) Bootstrap dari `PROJECT.md` & `wiki/hot.md`, (2) Lock onto 1 Milestone task, (3) Jalankan pre-verification test, (4) Eksekusi & tes empiris, (5) Sinkronisasi balik ke `wiki/hot.md` + Git commit.

- **Curriculum-Wide Mind Map Explanatory Video Coverage Audit (2026-10-07)**:
  1. *Curriculum Scope & Lesson Accounting*: Platform IR Study Companion memiliki total 157 bab pelajaran materi di 18 modul (di luar 18 halaman indeks `000-index.md`, 4 halaman front-matter platform, dan 1 berkas referensi).
  2. *Current Production Baseline (2 Chapters Covered)*: Dua bab awal di Modul 1 telah memiliki video pengantar Mind Map resmi:
     - Bab 010 (*Study of International Relations*, `Sa0PnnZLn0w`): Mind Map Explanatory (5:16, Remotion RoughJS).
     - Bab 020 (*Globalization and Global Politics*, `7K4preE-EBY`): Mind Map Explanatory (3:00, video pengantar konseptual terkonfirmasi oleh pengguna).
  3. *Unfulfilled Production Backlog (155 Chapters)*: Sebanyak 155 bab materi kurikulum saat ini belum memiliki video Mind Map Explanatory, dengan 4 bab di Modul 1 (CH030 s.d. CH060) telah terdaftar dalam antrean rendering (`learning-videos/README.md`) berstatus QUEUED.

- **Dynamic Conceptual Gateway Card & Pre-Reading Video Architecture (2026-10-07)**:
  1. *From Raw Embeds to Conceptual Gateway Standard*: Meletakkan iframe video mentah di dalam tubuh teks markdown menghasilkan tampilan tidak konsisten dan merusak ritme pedagogis. Mengangkat video ringkasan bab ke dalam skema frontmatter deklaratif (`youtube_id`, `explanatory_video: { title, desc, duration, format }`) mengaktifkan kartu *CONCEPTUAL GATEWAY* resmi di atas naskah dengan bingkai elegan dan responsif.
  2. *Dynamic Duration Badge in LMS Layout (`_layouts/chapter.html`)*: Mengganti badge durasi statis ("5 MIN") menjadi token dinamis `🎬 WATCH BEFORE READING ({{ page.explanatory_video.duration | upcase }})` memungkinkan penyajian durasi yang akurat (misal: "3 MIN" untuk video ringkasan Chapter 2 `7K4preE-EBY`, "5 MIN" untuk mind map Chapter 1 `Sa0PnnZLn0w`).
  3. *Polymorphic Video Format Labeling*: Mendukung penanda format fleksibel (`format: "Video Summary"` vs default `"Mind Map Flowchart"`), memberikan kejelasan pedagogis bagi siswa mengenai tipe media pengantar yang disajikan.

- **Simulation Divider & Redundant Interactive Learning Purge in Non-Simulation Chapters (2026-10-07)**:
  1. *Legacy Feature Injection Artifacts*: Pada fase awal otomatisasi konten kurikulum, skrip ekstraksi menyuntikkan template markdown `\n---\n### Interactive Learning\n{% include flashcards.html ... %}` ke akhir naskah bab materi. Sintaks pemisah `---` merender elemen `<hr>` (garis pembatas horizontal), sedangkan heading `### Interactive Learning` terindeks ke dalam Table of Contents (TOC) sticky drawer dan bertengger tepat di atas kartu konsep flashcards.
  2. *False Simulation Affordance Elimination*: Di 10 bab yang memiliki laboratorium diplomasi interaktif (`{% include sim_*.html %}`), pembatas dan konteks simulasi memang relevan. Namun, pada 145 bab kurikulum lainnya yang tidak memiliki simulasi, keberadaan garis `<hr>` dan judul `Interactive Learning` menimbulkan kebingungan bagi pembelajar (mengindikasikan adanya simulasi yang hilang/rusak). Komponen flashcard sendiri telah memiliki header berdedikasi `Active Recall Cards` dengan microcopy instruktif `Click card to reveal definition`.
  3. *Deterministic Elimination Across 145 Non-Simulation Chapters*: Mengeliminasi seluruh sisa divider `---` dan `### Interactive Learning` sebelum `{% include flashcards.html %}` di 145 bab non-simulasi, menyisakan alur bacaan yang bersih (prose ➔ Active Recall Cards ➔ Knowledge Check), sekaligus melestarikan 10 simulasi diplomasi asli secara utuh. 369/369 pytest lolos dan verifikasi Jekyll build mengonfirmasi 0 residu `interactive-learning` di 151 bab non-simulasi.

- **Universal Concept Tooltip & Wikipedia Popover Rollout Across LMS Prose (2026-10-07)**:
  1. *Legacy Theme Class Selector Trap*: Saat berpindah dari GitBook (`.markdown-section`) ke mesin Bespoke LMS (`.course-prose-body`), selector JavaScript DOM di `_includes/footer.html` tertinggal menargetkan `.markdown-section strong`. Akibatnya, 160 bab kurikulum kehilangan inisialisasi tooltip karena tidak ada elemen yang cocok, dan hanya Bab 1 yang kebetulan memiliki tag manual `mark.nice-mark`. Menyelaraskan selector ke `.course-prose-body strong, .course-prose-body b, .course-prose-body mark.nice-mark` mengaktifkan kembali interaktivitas tooltip di seluruh 161 bab (4.601 keyword).
  2. *Interactive Keyword Semiotics & Defensive Container Filtering*: Bold biasa di dalam teks edukasi harus dibedakan dari UI navigation atau komponen interaktif lainnya. Mengisolasi selector agar mengecualikan kuis (`.quiz-container`), kartu ujian (`.module-exam-card`), flashcard, digest box, tabel, dan heading, serta menambahkan class `.keyword-interactive` (garis bawah titik halus + hover aksen) menjamin estetika bersih dan mencegah tooltip liar pada elemen antarmuka.
  3. *Collision Defense Between Two Tooltip Systems*: Repositori memiliki sistem IR Glossary popover (`.ir-term-mention`) dan sistem Wikipedia/AI Dictionary popover (`.keyword-interactive`). Menambahkan pemeriksaan tabrakan eksplisit (`if (el.classList.contains('ir-term-mention') || el.closest('.ir-term-mention')) return;`) mencegah render ganda atau tooltip bertumpuk.

- **Zero-Exception English-Only Mandate Across All Platform Data & Client Runtime (2026-10-07)**:
  1. *Eradication of Dual-Language UI Leakage*: Sekalipun dataset kamus (`ir_glossary.json`) menyimpan data multibahasa (`plain_id` dan `plain_en`), lapisan runtime antarmuka pengguna (`course-player.js`, popover, `lesson-term-card`, `_pages/glossary.md`) WAJIB secara mutlak mengonsumsi dan menampilkan teks bahasa Inggris (`item.plain_en`). Tidak boleh ada pengecualian tampilan lokal di platform web.
  2. *Full English Microcopy Harmonization*: Seluruh label navigasi dan meta pada komponen istilah wajib seragam: `"In Simple Terms:"`, `"Definition:"`, `"Full Glossary"`, dan `"{N} Key Terms"`.

- **Learning Videos Vault & Deterministic Media Asset Governance (2026-10-06)**:
  1. *Centralized Media Asset Vault (`learning-videos/`)*: Mengisolasi aset video final ke dalam folder master khusus dengan arsitektur subfolder terpisah (`exports/` untuk MP4 render, `posters/` untuk thumbnail PNG resolusi tinggi) memudahkan pemantauan lintas modul dan mencegah fragmentasi file media di direktori eksperimen.
  2. *Strict Deterministic Naming Convention*: Mengadopsi pola penamaan terstruktur `IR_M{Module:02d}_CH{Chapter:03d}_{Title}_{Format}_{Resolution}.{ext}` (contoh: `IR_M01_CH010_Foundations_of_International_Relations_MindMap_1080p.mp4`) menjamin keterurutan leksikografis di filesystem dan memudahkan sinkronisasi otomatis dengan slug bab kurikulum serta metadata YouTube Studio.
  3. *Decoupled Dual-Layer Registry*: Mengelola inventarisasi melalui format ganda (`README.md` matriks tabel visual untuk manusia dan `catalog.json` untuk konsumsi mesin/CI) memberikan transparansi status produksi (Rendered, Rendering, Queued) tanpa ketergantungan database eksternal.
  4. *Git Hard-Limit & SSG Compilation Defense*: Menjamin file biner video berukuran besar (>50 MB) dieksklusi secara deterministik dari `_config.yml` (mencegah beban build Jekyll berlebih) dan `.gitignore` (`learning-videos/exports/*.mp4`), melindungi repositori dari kegagalan push akibat batas 100 MB GitHub.

- **English-Only Standardization for Educational UI & Explanatory Video Gateways (2026-10-06)**:
  1. *Strict Linguistic Uniformity across Platform Surface*: Seluruh komponen antarmuka, heading, call-to-action, status badge, dan metadata video penjelas (`_layouts/chapter.html` dan frontmatter bab) WAJIB menggunakan bahasa Inggris akademik standar internasional tanpa campuran bahasa Indonesia (kecuali kamus lokal `plain_id` yang terisolasi di glossary).
  2. *Standardized Pre-Reading Badge Microcopy*: Mengubah label tombol dan kartu menjadi format ringkas dan instruktif: `"🎬 WATCH BEFORE READING (5 MIN)"`, `"CONCEPTUAL GATEWAY"`, dan `"Mind Map Explanatory: Foundations of International Relations"`. Memberikan sinyal pedagogis instan kepada pembaca global untuk menonton peta konsep sebelum membaca teks bab.

- **The Cognitive Advance Organizer & Decluttering Architecture in Educational Mind Map Videos (2026-10-06)**:
  1. *Mind Map as Pre-Reading Schema Anchor*: Video mind map bukan suplemen pasif atau slide presentasi biasa, melainkan *Advance Organizer* (David Ausubel) yang ditonton pembelajar *sebelum* membaca artikel materi untuk membentuk kerangka kompas mental yang kokoh.
  2. *Dynamic Spotlight Dimming (0.35 Attentional Isolation)*: Menampilkan seluruh node dengan bobot visual yang sama memicu *Split-Attention Effect* (Richard Mayer). Menerapkan *Spotlight Dimming*—di mana node aktif menyala 100% dengan bayangan fokus sementara node tetangga yang sedang tidak dibahas meredup ke `opacity: 0.35` dan panah tidak aktif memudar ke `0.20`—menghasilkan ketenangan visual mutlak dan membimbing mata audiens mengikuti alur cerita tanpa kebingungan.
  3. *Semantic Academic Color Hierarchy*: Menghindari palet pelangi acak tanpa makna. Menetapkan skema warna semantik teoretis yang konsisten di seluruh 18 modul (Kuning untuk Hub/Pertanyaan Inti, Biru Langit untuk Aktor Negara & Sistem, Coral/Merah untuk Realisme/Anarki/Konflik, Mint Green untuk Liberalisme/Institusi/Kerjasama, Soft Lavender untuk Konstruktivisme/Norma/Wendt, dan Putih Kertas untuk Detail Kasus) mempercepat retensi kognitif dan asosiasi teoretis secara instan.
  4. *Dual-Font System Cognitive Boundary*: Mengisolasi font tulisan tangan papan tulis *Patrick Hand* untuk kanvas diagram dan font modern *Plus Jakarta Sans* untuk kapsul subtitle bawah menegaskan batas kognitif yang jelas antara apa yang digambar di papan tulis vs apa yang diucapkan narator.

- **Phonetic Normalization for Neural TTS in Educational Videos (2026-10-06)**:
  1. *The Cardinal vs Idiomatic Number Trap*: Model neural TTS seperti Kokoro-82M secara default memperlakukan deretan angka `"911"` sebagai bilangan kardinal (*"nine hundred eleven"*), bukan nomor darurat idiomatik (*"nine-one-one"*).
  2. *Pre-Synthesis Normalization Pipeline*: Teks narasi untuk audio wajib melalui pembersihan fonetik regex (misal: `re.sub(r'\b911\b', 'nine-one-one', text)`) sebelum dikirim ke engine sintesis suara, sementara teks tampilan subtitle dan diagram tetap mempertahankan format bersih `"911"` untuk estetika visual dan keterbacaan penonton.

- **Deep Dynamic Zoom Contrast Architecture in Educational Mindmap Videos (2026-10-06)**:
  1. *The Fallacy of Narrow-Band Zooming*: Mengompresi seluruh segmen kamera dalam rentang zoom sempit (`1.25x - 1.34x`) membuat kartu materi tetap terasa kecil dan jauh (hanya mencakup ~25% lebar layar 1080p), sementara 75% layar terbuang menjadi ruang putih kosong.
  2. *True Deep Zoom-In (`1.95x - 2.05x`) for Reading Clarity*: Saat sebuah konsep spesifik sedang diuraikan dalam narasi kalimat, kamera harus melakukan zoom-in mendalam hingga skala `1.95x - 2.05x`. Kartu membesar mencakup ~42% lebar layar 1080p, ukuran font tulisan tangan naik 200%+ (~44px), teks terbaca sangat jelas dan nyaman tanpa squinting, serta menyisakan margin lapang >320px di atas kapsul subtitle.
  3. *Contextual Zoom-Out (`1.15x - 1.20x`) for Macro Structural Contrast*: Saat transisi antar-babak atau perbandingan paradigma (misal Realisme vs Liberalisme), kamera melakukan zoom-out untuk memperlihatkan keterhubungan cabang induk secara makro sebelum menyelam kembali ke detail kartu berikutnya.

- **Discrete Travel & Stationary Hold Architecture in Educational Mindmap Videos (2026-10-06)**:
  1. *The Stationary Hold Law (Cognitive Reading Window)*: Dalam video berbasis peta pikiran/flowchart, kamera tidak boleh terus melayang tanpa henti (*continuous drift*) saat sebuah konsep sedang dijelaskan. Hal ini memicu disorientasi spasial dan kelelahan visual penonton. Kamera harus menerapkan *stationary hold* (kecepatan $v = 0$) selama 3 hingga 10 detik tepat saat narasi kalimat berlangsung, memberi audiens ketenangan penuh untuk membaca teks kartu dan menyimak audio.
  2. *Precision Targeted Centering & Tighter Zoom (`zoom: 1.28 - 1.34`)*: Mengunci koordinat kamera $(x, y)$ tepat pada titik tengah geometris node kartu aktif yang sedang diulas dan memperbesar skala ke `1.28`–`1.34` memastikan kartu menjadi fokus primer di 1080p dengan teks tulisan tangan (*Patrick Hand*) yang tajam, sementara node sekitar tetap terlihat samar di latar perifer tanpa saling bertumpuk.
  3. *Zero-Collision Screen Hygiene (Watermark & Section Decoupling)*: Menghapus watermark tetap di sudut layar mencegah tabrakan visual dengan node kanvas saat zoom jarak dekat. Mengisolasi seksi baru (seperti Seksi 7 Interdependensi) di ruang kanvas terpisah menjamin nol tumpang tindih dengan kapsul subtitle bawah.


- **Authentic Hand-Drawn Flowchart Mindmap Architecture & Excalidraw Engine in Remotion (2026-10-06)**:
  1. *Direct Grounding in Creator's Authentic YouTube Format*: Berdasarkan inspeksi langsung via Chrome DevTools terhadap video referensi kanonik pengguna di channel `@IRinANutshell` (`https://www.youtube.com/watch?v=Sa0PnnZLn0w&t=130s` - *"What is International Relations study?"*), format video edukasi terbaik bukanlah kumpulan kartu slide UI kaku, melainkan **infinite canvas hand-drawn flowchart/mindmap** yang dinavigasi oleh kamera 2D dinamis.
  2. *Deterministic RoughJS Architecture (Zero-Jitter Guarantee)*: Mengintegrasikan `roughjs` dengan generator seed deterministik pada kurva rounded rectangle (`rx=18`, `ry=18`) dan panah konektor menghasilkan garis sketsa tangan organik (*double-sketched rough borders*, tebal 2.6px, arang `#1A202C`) yang stabil 100% antar frame (nol flicker/jitter) dengan isian warna pastel lembut (`#BEE3F8` sky blue, `#FEFCBF` yellow, `#C6F6D5` mint green, `#FED7D7` pink, `#FFFFFF` white).
  3. *Handwriting Typography & Dynamic CameraRig*: Mengadopsi Google Font **Patrick Hand** (`@remotion/google-fonts/PatrickHand`) memberikan estetika papan tulis edukatif yang ramah dan alami. Didukung oleh interpolator kamera berbasis *cosine ease-in-out* yang meluncur mulus mengikuti koordinat 33 node bahasan di kanvas 4800x3200 dan melakukan *pull-back* sinematik di akhir video (`zoom: 0.39`), menyajikan panorama utuh seluruh jaringan konseptual ilmu Hubungan Internasional secara terintegrasi.

  1. *The Fallacy of Text-Transcribing Slides in Video*: Menaruh kartu teks, ringkasan bullet point, atau kutipan panjang di layar video edukasi memicu Split-Attention Effect (Richard Mayer). Audiens dipaksa membaca teks yang menduplikasi narasi audio alih-alih memahami mekanisme kerja konsep. Video edukasi sejati BUKAN slide presentasi yang dibacakan, melainkan instrumen piktoral yang memvisualisasikan dinamika kausalitas ($A \rightarrow B \rightarrow C$).
  2. *Live YouTube Pedagogical Extraction (Zero-Hallucination Grounding)*: Investigasi real-time terhadap video edukasi terpopuler (The Analyst 4.8M views, BBC Learning English 280k views, TED-Ed 757k views, CrashCourse 1M+ views, Heinrich-Böll-Stiftung 2.6M views, One Minute Economics 965k views, Soomo Learning 788k views) membuktikan 4 hukum visual fundamental:
     - *Law 1 (Show the Mechanism, Not the Definition)*: Gambar interaksi fisiknya (hakim & polisi vs meja bundar anarki dengan kursi kosong; timbangan neraca kekuatan; stempel tarif yang membelokkan arus massa; bola biliar keras vs benang interdependensi).
     - *Law 2 (Strict 3-Word Rule)*: Teks di layar hanya boleh berupa label entitas (`STATE A`, `UNSC`), metrik kunci (`1933`, `$3T`), atau status sistem (`ESCALATION`, `EQUILIBRIUM`). Nol paragraf, nol kalimat rangkuman.
     - *Law 3 (Event-Driven Visual Beats)*: State visual bertransformasi setiap 4–6 detik mengikuti titik balik narasi suara.
     - *Law 4 (Full-Canvas Open Stage)*: Hilangkan batas kontainer kotak kartu; seluruh ruang 1920x1080 adalah panggung dinamis.

- **Authentic Pedagogical Representation & Editorial Typography Overhaul (2026-10-06)**:
  1. *Substantive Grounding over Abstract Shapes*: Slide edukasi tidak boleh diisi oleh diagram abstrak yang lepas dari konteks bahasan (seperti menggambar model cincin atom untuk "Hubungan Internasional", atau peta samar untuk "Aktor Negara vs Non-Negara"). Menyelaraskan visual secara presisi dengan naskah narasi—seperti *Two-Tier Reality* (berita permukaan vs struktur sistemik), *Montevideo 1933 4-Criteria*, *Domestic Hierarchy 911 vs International Anarchy*, *Waltz's Billiard Ball Model*, *Kantian Triad of Peace*, *Wendt's Nuclear Paradox (500 UK vs 1 Korut)*, dan *Weaponized Chokepoints (Malacca, SWIFT, TSMC)*—mentransformasikan video dari sekadar animasi grafis menjadi instrumen pembelajaran akademik dengan retensi kognitif tinggi.
  2. *Eradication of Monospace Hacker Aesthetics in Humanities*: Penggunaan `fontFamily: monospace` untuk badge, angka, dan label di materi ilmu sosial/humaniora menciptakan kesan tidak nyaman dan kaku seperti terminal koding pengembang. Menggantinya dengan **Plus Jakarta Sans** (geometris modern berdaya baca tinggi dengan `tabular-nums`) untuk elemen UI dan **Newsreader Serif Italic** untuk kutipan literatur klasik (Waltz, Jervis, Keohane, Wendt) menghasilkan perpaduan estetika jurnal akademik Skandinavia yang elegan, tenang, dan berwibawa.

- **Zero-Collision Studio Subtitle Architecture & SOTA Neural TTS Migration (2026-10-06)**:
  1. *Subtitles in Outer Studio Margin vs Slide Overlay*: Menempatkan kapsul subtitle di dalam kontainer slide berisiko menabrak kotak kutipan akademis atau kartu visual interaktif. Dengan menyusutkan kartu slide ke tinggi deterministik 934px (top padding 32px), terbentuk margin studio bawah 114px yang bersih untuk menampung kapsul subtitle melayang (`bottom: 26px`, dark glass `#0F172A`, cyan/white text, badge `AUDIO CC`). Hasilnya: nol tabrakan visual (zero-collision) dengan keterbacaan sempurna di 1080p.
  2. *SOTA Local Diffusion TTS vs Robotic Concatenative TTS*: Mengatasi komplain suara "robotik" dari Edge-TTS (`GuyNeural`) dengan mengadopsi model open-source SOTA **Kokoro-82M (v1.0)**. Menggunakan arsitektur StyleTTS2 diffusion-based latent phoneme synthesis yang menghasilkan artikulasi alami, dinamika intonasi emosional, vokal fry, dan jeda nafas manusia secara 100% lokal di CPU (Rp 0,- biaya API) dalam durasi sintesis 15-20 detik untuk 700 kata.

- **Scene-First Polymorphic Video Architecture vs Rigid Column Layouts (2026-10-06)**:
  1. *Eliminating Template Fatigue in Educational Videos*: Memaksa setiap slide ke dalam format 2-kolom yang seragam (kiri judul/peluru, kanan kotak widget) memicu kelelahan visual dan membuat video terasa seperti presentasi korporat PowerPoint usang. Menggantinya dengan arsitektur panggung polimorfik (`Scene01` s.d. `Scene08`)—di mana setiap konsep memiliki tata panggung piktoral unik 70–80% layar (seperti *50/50 Split Battle Canvas*, *Full-Width Cartographic Theater*, *Dark-Slate Causal Pipeline*, *Mechanical Balance Scale Arena*, dan *Living Ideational Constellation*)—mentransformasikan video biasa menjadi konten edukasi kelas dunia setara Brilliant.org atau Vox.
  2. *Mayer's Cognitive Signaling over Text Walls*: Mengeliminasi paragraf berbutir panjang (1, 2, 3) dan menggantinya dengan kata kunci berdaya tinggi (*power tags*), kartu kaca mengambang (*floating glassmorphism cards*), serta kutipan otoritas akademis kanonik (Jervis, Waltz, Keohane, Wendt) menyelaraskan video dengan prinsip beban kognitif multimedia: telinga mendengarkan penjelasan naratif utuh, mata mencerna model dan sintesis visual.

- **Dynamic Mathematical Motion Graphics & Anti-Slideshow Fatigue Architecture (2026-10-06)**:
  1. *Continuous Frame-Driven Motion vs Static Cards*: Menempatkan kartu teks statis membuat video slide terkesan seperti presentasi PDF pasif. Mengintegrasikan grafik gerak bertenaga matematika frame (`frame * 0.05`, `Math.sin(frame * 0.06)`, `interpolate()`)—seperti bola kawat 3D berputar, timbangan mekanis realisme yang berayun harmonik, sirkuit logika kausal berdenyut energi, dan konstelasi partikel konstruktivis—membuat setiap detik video terasa hidup dan sinematik.
  2. *Global Audio Wave & CameraRig Integration*: Menambahkan `AudioWaveVisualizer` 16-bar di footer yang bergerak sinusoidal dan `CameraRig` subtle push-in kontinu (skala `1.00` ➔ `1.022`) pada kontainer slide menjamin tidak ada 'dead frames' (bingkai mati) sepanjang 5 menit durasi course.
  3. *Pre-Render Inspection Gate Protocol*: Merender still frame preview (`npx remotion still CourseVideo out/motion_preview_slide_X.png --frame=...`) pada titik tengah setiap slide sebelum mengeksekusi render MP4 final memungkinkan evaluasi visual cepat dan menghindari pemborosan siklus komputasi encoding H.264 jika ada penyesuaian tata letak yang diinginkan pengguna.

- **Visual UI Code over Plain Text Blocks in Educational Motion Graphics (2026-10-06)**:
  1. *Eliminating the Right-Panel Visual Lacuna*: Slide presentasi edukasi berskala 1080p akan terasa membosankan jika kolom kanan diisi oleh blok teks deskriptif standar. Menggantinya dengan artefak kode antarmuka pengguna (UI code)—seperti pohon hierarki kurikulum berstatus aktif/terkunci, diagram alur berbingkai CSS dengan garis konektor vertikal, matriks perbandingan dual-tint (soft crimson vs soft emerald), dan mockup dashboard digital academy lengkap dengan progress meter 100% dan tombol aksi—memberikan kesan aplikasi interaktif kelas dunia dan meningkatkan retensi belajar secara drastis.
  2. *Deterministic Full Render Scaling*: Menyesuaikan script naskah menjadi 700 kata dan menyintesisnya via `edge-tts` menghasilkan 9.218 frame (307,27 detik / 5:07 @ 30 FPS). Sinkronisasi otomatis melalui `public/timestamps.json` memungkinkan setiap kartu UI masuk dengan animasi pegas (`spring`) yang sinkron dengan titik bahasan narasi audio tanpa lonjakan beban CPU atau desinkronisasi.

- **5-Minute Slide Video Course Production & Deterministic TTS-to-Remotion Pipeline (2026-10-06)**:
  1. *Zero-Cost Neural Audio Synchronization*: Mengintegrasikan `edge-tts` (`en-US-GuyNeural`) melalui script Python (`scripts/generate_course_assets.py`) menghasilkan sintesis vokal berkualitas studio secara gratis tanpa ketergantungan API berbayar. Penggabungan via `ffmpeg` concat dengan jeda 0,5 detik antar-slide dan pengukuran durasi via `ffprobe` menghasilkan sinkronisasi deterministik: 8.798 frame @ 30 FPS (~293,26 detik / 4:53) tepat menyatu dengan durasi video tanpa desinkronisasi audio.
  2. *Windows Console Unicode Defense*: Pada lingkungan PowerShell Windows, encoding default konsol adalah `cp1252` yang akan memicu `UnicodeEncodeError` jika skrip Python mencetak karakter Unicode (misal checkmark `\u2713`). Mewajibkan penambahan `sys.stdout.reconfigure(encoding='utf-8')` dan `sys.stderr.reconfigure(encoding='utf-8')` pada header skrip mencegah kegagalan pipeline CLI secara deterministik.
  3. *Clean Documentation Aesthetic at 1080p Scale*: Merancang slide video dengan identitas visual dokumentasi `ir-guide.netlify.app` (kanvas putih murni `#FFFFFF`, teks arang gelap `#111827`, kontainer `w-4/5` 80% dengan padding 64px, judul masif 68px, bullet points 34px, dan kartu UI visual modular di sisi kanan) memberikan keterbacaan optimal pada layar 1920x1080 tanpa clipping teks atau kelelahan visual (slideshow fatigue).
  4. *Remotion Audio Integration in AbsoluteFill*: Komponen `<Audio src={staticFile('voiceover.mp3')} />` dari `@remotion/core` dapat diletakkan langsung di dalam root `<AbsoluteFill>` berdampingan dengan komponen `<SlideView />`, memastikan audio dan video diproses dalam satu bundle tanpa perlu pasca-editing manual.

- **Kurzgesagt Motion Graphics Architecture & Decoupled Educational Asset Pipeline (2026-10-05)**:
  1. *Clean-Slate Remotion Scaffolding*: Memisahkan library komponen grafis gerak baru (`simulation/ir-motion-library/`) dari artefak composer legacy (`openmontage_repo`) menghindari konflik dependensi versi React (React 19) dan isolasi bersih melalui `.gitignore` serta `_config.yml exclude:`.
  2. *Kurzgesagt Visual Tokenization*: Mengimplementasikan skema visual bergaya Kurzgesagt (flat saturated vector shapes, dark cosmic background gradients, dan tipografi sans-serif proporsional) memberikan daya tarik pedagogis tinggi bagi materi HI yang abstrak tanpa memerlukan aset gambar generatif AI (zero AI imagery artifacts).
  3. *Decoupled Declarative Asset Datasets*: Memisahkan naskah data bab ke dalam berkas JSON (`data/chapter-XXX-assets.json`) memungkinkan penambahan materi video untuk 161 bab lainnya tanpa menyentuh kode komponen React, menjamin skalabilitas tinggi dan zero-regression.
  4. *Remotion Composition ID Character Constraint*: Remotion secara ketat menolak karakter garis bawah (`_`) pada atribut `id` komposisi (`validateCompositionId` regex hanya mengizinkan `[a-zA-Z0-9-]` dan CJK). Penamaan komposisi harus selalu menggunakan tanda hubung (misal: `Pilot-WorldMap`, bukan `Pilot_WorldMap`) atau PascalCase murni (`PilotWorldMap`).
  5. *Authentic Geographic Projection in Remotion*: Menghindari kurva SVG acak buatan tangan yang tampak seperti 'gumpalan tanpa bentuk'. Memanfaatkan pre-proyeksi `d3-geo` (Natural Earth 1) dari data `world-atlas` (177 negara + landmass MultiPolygon) ke dalam JSON lokal (`src/data/worldMapData.json`) menghasilkan peta dunia asli yang langsung dikenali secara kartografis (benua, kepulauan Indonesia, kepulauan Inggris, Jepang, grid garis bujur/lintang) dengan kinerja render offline 100% instan dan bebas lag.

- **Learner-Centric Microcopy & Eradication of Developer Artifacts (2026-10-05)**:
  1. *Developer Prompt Jargon Leakage*: Frasa seperti "Clean typography (~70ch measure)" atau "variable Inter typography" adalah artefak spesifikasi CSS/desain internal yang bocor ke microcopy antarmuka pengguna. Bagi pembaca awam, hal ini terdengar sangat robotik, pretensius, dan "sangat AI".
  2. *Empathetic Learner Framing*: Pembaca materi edukasi tidak perlu tahu spesifikasi pengukuran karakter per baris CSS (`~70ch`). Mengganti istilah teknis pengembang menjadi nilai manfaat pembelajaran nyata (misal: *"Focused reading layout with live reading time estimates and an in-lesson outline for effortless navigation"*) menghasilkan narasi yang alami, elegan, dan berorientasi pada kenyamanan pembelajar.

- **Git Large-Asset Isolation & Production Synchronization Mandate (2026-10-05)**:
  1. *Binary Model Quota Defense*: Eksperimen rendering multimedia lokal (seperti model Kokoro TTS ONNX 310 MB dan render video MP4 Remotion) berisiko fatal menggagalkan sinkronisasi remote jika tidak diisolasi secara deterministik pada `.gitignore`. GitHub menolak komit dengan berkas tunggal $>100$ MB secara absolut.
  2. *Pre-Commit Tree Hygiene*: Mengaudit ukuran berkas sebelum `git add .` dan mendaftarkan direktori pendukung besar (`simulation/`, `*.onnx`, `*.mp4`, `*.bin`) ke `.gitignore` menjamin branch `master` tetap ramping, cepat, dan hanya memuat kode sumber inti, naskah materi, serta aset JSON/CSS/JS produksi.
  3. *Seamless Deployment Sync*: Keberhasilan push 2.057 berkas (243.482 penambahan baris) mencakup seluruh arsitektur Milestone M7, 10 Interactive Labs, audit anti-halusinasi 5 klaster, 161 ringkasan bab unik, dan Terminology Engine ke `origin/master` tanpa konflik.

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
- **Relative Render Output Path Pitfall (2026-10-08)**:
  - *Shadow Directory Trap*: Menjalankan `npx remotion render ... ../learning-videos/exports/...` dari dalam `simulation/ir-motion-library/` menulis output ke `simulation/learning-videos/` (folder bayangan), BUKAN `learning-videos/` di root proyek. Master CH040 sempat "hilang" karena ini.
  - *Rule*: Selalu gunakan path absolut atau `../../learning-videos/exports/` saat merender dari `ir-motion-library`, dan selalu verifikasi `ls learning-videos/exports/` setelah render selesai sebelum melaporkan sukses.

- **Milestone M9: Mandatory Review Gate After Phase 1 in Mind Map Video Pipeline (2026-10-07)**:
  - *User Directive*: Setelah menyelesaikan Fase 1 (Ekstraksi Naskah Narasi Voiceover & Desain Node Graf Mind Map), agen **WAJIB berhenti dan mempresentasikan rancangan mind map preview kepada pengguna**.
  - *Strict Rule*: Fase 2 (sintesis audio Kokoro), Fase 3 (kamera Remotion), Fase 4 (still render), dan Fase 5 (render master MP4) **HANYA boleh dijalankan setelah pengguna memberikan persetujuan (ACC)**.
  - *Why*: Mencegah waktu render Remotion yang sia-sia dan menghindari desinkronisasi narasi dengan graf sebelum fondasi substansi disepakati.

- **Milestone M7: Online Course Platform Transformation (10-Persona Architecture) (2026-10-05)**:
  1. *Zero-Backend LMS Data Portability*: Mengembangkan sistem sinkronisasi kemajuan (*progress backup & sync*) 100% sisi klien tanpa database backend atau akun pengguna eksternal. Struktur state JSON terkompresi mencakup `chapter_read_*`, `quiz_*`, `exam_*`, dan `bookmark_*` yang dapat diekspor dan diimpor secara instan dengan verifikasi skema, memenuhi kebutuhan persona pembelajar multi-perangkat dan privasi data.
  2. *Build-Time Static Assessment Engines*: Mengkompilasi 180 butir soal ujian akhir modul (10 soal per modul) langsung ke dalam data statis Jekyll (`_data/module_exams.json` & `assets/data/module_exams.json`) menghasilkan latensi 0 ms saat penilaian, passing score threshold 70%, feedback rasional ilmiah komprehensif, serta penanda kelulusan deterministik `exam_module_<id>_passed`.
  3. *Client-Side High-DPI Academic Certificate Generator*: Menggunakan HTML5 `<canvas>` (1600x1130 px @ 2x pixel ratio) untuk merender sertifikat akademik diplomatik berornamen mewah, cap emas timbul bergradien, tanda tangan akademik, dan hash verifikasi SHA-256 yang dihitung secara deterministik dari `nama + spesialisasi + tanggal`. Menghasilkan file PNG beresolusi cetak tinggi tanpa perlu library backend berat seperti Puppeteer atau WeasyPrint.
  4. *Deep Concept Search & Curated Academic Lexicon*: Mengindeks seluruh 162 berkas materi ke dalam payload ringkas JSON (120 KB) untuk pencarian instan di off-canvas drawer, dipadukan dengan kamus 122 konsep dasar Hubungan Internasional (`_pages/glossary.md`) yang dikurasi dengan filter subdisiplin, tokoh kunci, dan tautan silang bab materi.

