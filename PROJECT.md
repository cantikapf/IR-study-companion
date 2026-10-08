# Project: IR Study Companion

## Status: 🟢 Active Development

## Architecture / Workflow
- **Overview**: 
  Platform pembelajaran daring mandiri untuk studi Hubungan Internasional berbasis static site generator Jekyll. Dilengkapi dengan pipeline otomatisasi Python untuk ekstraksi dan penataan fitur interaktif (kuis, flashcard), serta jaminan kualitas melalui unit testing `pytest` dan E2E testing `Playwright`.
- **Official YouTube Channel**:
  [`https://www.youtube.com/@IRinANutshell`](https://www.youtube.com/@IRinANutshell) — Channel video edukasi resmi pendamping kurikulum web IR Study Companion, dirancang dengan format faceless explainer/mini-dokumenter berdurasi 3–5 menit menuju monetisasi YouTube Partner Program (YPP).

## Feature Inventory
| # | Feature / Scope Item | Description | Milestone | Status |
|---|---|---|---|---|
| 1 | VibeCoding Architecture | Integrasi modul .agents, wiki Obsidian, dan GEMINI.md | M0 | DONE |
| 2 | Structured Curriculum | Bab-bab materi Hubungan Internasional terstruktur (_chapters/) | M1 | DONE |
| 3 | Interactive Learning | Kuis interaktif dan flippable flashcards | M1 | DONE |
| 4 | Visual Progress Tracking | Penyimpanan kemajuan membaca via browser localStorage | M1 | DONE |
| 5 | Diagrams & Maps | Visualisasi skenario krisis dan peta interaktif SVG | M1 | DONE |
| 6 | Dark/Light Mode | Dukungan tema kontras tinggi dan aksesibel | M1 | DONE |
| 7 | Quality Assurance (QA) | Suite pengujian otomatis via pytest dan Playwright | M1 | DONE |
| 8 | Content & Reference Verification | Audit keaslian sitasi akademik via CrossRef & fact-check AI | M2 | IN PROGRESS |
| 9 | Interactive Diplomatic Labs Expansion | 10 simulasi interaktif mandiri (zero external dependencies) | M6 | DONE |
| 10 | Final Stage Online Course Transformation | Backup/Sync, Deep Search, 18-Module Exams (180 soal), Curated Glossary (122 konsep), Elaborate Certificate, Onboarding Tour | M7 | DONE |
| 11 | IR Motion Graphics Library | Kurzgesagt-style Remotion component library (World Map, Timeline, Concept Diagram) + Pilot Chapter 010 dataset | M8 | DONE |
| 12 | Mind Map Explanatory Video Engine | Produksi video kanonik 1080p Mind Map & Flowchart Remotion (@IRinANutshell, Kokoro TTS, Deep Zoom 2.05x, Stationary Hold, RoughJS) | M9 | DONE |
| 13 | Learning Videos Vault & Registry | Direktori khusus learning-videos/ (exports, posters, catalog.json, README registry matrix) dengan standar penamaan deterministik | M9 | DONE |
| 14 | Diplomatic Lab Experience Overhaul | Lab Shell "Mission Console" + lapisan onboarding Briefing/Play/Debrief + panggung CSS-3D + pilot WebGL lab peta + integrasi homepage | M10 | IN PROGRESS |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| M0 | VibeCoding Adoption | Adopsi profil software VibeCoding secara non-destruktif | None | DONE |
| M1 | Core Platform & Content | Penyelarasan konten bab, kuis, dan pipeline QA | M0 | DONE |
| M2 | Second Brain & Content Audit | Verifikasi fakta, mitigasi halusinasi, dan audit referensi | M1 | DONE |
| M3 | Scandinavian Course Prototype | Interactive LMS harness + Utilitarian Home Academy | M2 | DONE |
| M4 | Production Theme Upgrade | Migrasi layout Jekyll ke Utilitarian Course Player & Home | M3 | DONE |
| M5 | Bespoke Native LMS Engine | Eliminasi GitBook & implementasi Full LMS Player + Drawer | M4 | DONE |
| M6 | Interactive Diplomatic Labs | 7 simulasi baru (total 10 labs) + homepage showcase update | M5 | DONE |
| M7 | Online Course Transformation | 180-Soal Exam System, Backup/Restore JSON, 122-Term Glossary, Elaborate Certificate Generator, Onboarding Tour | M6 | DONE |
| M8 | IR Motion Graphics Library | Arsitektur grafis gerak modular Kurzgesagt: AnimatedWorldMap, TimelineBar, ConceptDiagram, data JSON Module 010 | M7 | DONE |
| M9 | Mind Map Explanatory Engine | Standarisasi alur kerja video kanonik Mind Map Explanatory (Decluttering spotlight dimming 0.35, warna semantik akademis, dual-font captioning, pre-reading gateway card, 34 node graf, Deep Zoom 2.05x, Stationary Hold, eliminasi ~3,35 GB berkas usang) | M8 | DONE |
| M10 | Diplomatic Lab Experience Overhaul | Lab Shell Mission Console theme-aware, briefing terkunci + objective tracker + debrief terstruktur di 10 lab, panggung CSS-3D spasial, pilot WebGL (three.js vendored) di lab peta, integrasi homepage + status Completed | M9 | IN PROGRESS |





## Lessons Learned
*(Update this section regularly during the project lifecycle based on Tier 2 self-evaluations)*
- [x] **M2.1: Cluster 1 (IR Theories, FPA & Methodology)**: Diverifikasi faktual di Modul 010, 023, 031, 033. Matriks Teori Permainan & Putnam Two-Level Games diperbaiki.
- [x] **M2.2: Cluster 2 (International Law & International Organizations)**: Diverifikasi faktual di Modul 042, 045, 050. Menghapus komisi konsiliasi fiktif 1984, memverifikasi pasal Piagam PBB, UNCLOS 1982, dan IHL Jenewa 1949.
- [x] **M2.3: Cluster 3 (Modern World History & Diplomacy)**: Diverifikasi faktual di Modul 012, 032. Mengoreksi kronologi diplomasi Timur Dekat Kuno (Amarna) dan penanggalan VCDR 1961.
- [x] **M2.4: Cluster 4 (IPE & Global Economic Architecture)**: Diverifikasi faktual di Modul 021, 043, 046. Memperbarui status traktat mega-regional (CPTPP 2018 dan berlakunya RCEP 2022).
- [x] **M2.5: Cluster 5 (Security, Regionalism ASEAN & Indonesian Foreign Policy)**: Diverifikasi faktual di Modul 011, 013, 022, 034, 044. Menyelaraskan kronologi Deklarasi Bangkok 1967, Piagam ASEAN 2007, Komunitas ASEAN 2015, dan reformasi sektor keamanan Indonesia pasca-1998 (UU TNI 34/2004).
- **Adopsi Struktur**: Mengadopsi struktur VibeCoding ke repositori yang sudah matang harus menjaga pondasi SSG (Jekyll), dependensi Ruby/Node, dan workflow testing tanpa menimpa README.md dan file arsitektur inti.
- **Integritas Referensi**: Daftar pustaka terpusat di `010-references.md` terbukti berbasis karya nyata (29 DOI diverifikasi CrossRef), sehingga mitigasi halusinasi dapat difokuskan pada ketepatan interpretasi substansi bab dan kunci kuis.
- **Normalisasi Markdown AI**: Pemindaian menyeluruh terhadap 157 bab berhasil menormalkan 28 anomali sintaks markdown bolding (`**`) hasil AI generator di 18 modul kurikulum dan memastikan 156 kuis interaktif 100% konsisten.
