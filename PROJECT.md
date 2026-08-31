# Project: IR Study Companion

## Status: 🟢 Active Development

## Architecture / Workflow
- **Overview**: 
  Platform pembelajaran daring mandiri untuk studi Hubungan Internasional berbasis static site generator Jekyll. Dilengkapi dengan pipeline otomatisasi Python untuk ekstraksi dan penataan fitur interaktif (kuis, flashcard), serta jaminan kualitas melalui unit testing `pytest` dan E2E testing `Playwright`.

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

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| M0 | VibeCoding Adoption | Adopsi profil software VibeCoding secara non-destruktif | None | DONE |
| M1 | Core Platform & Content | Penyelarasan konten bab, kuis, dan pipeline QA | M0 | DONE |
| M2 | Second Brain & Content Audit | Verifikasi fakta, mitigasi halusinasi, dan audit referensi | M1 | DONE |
| M3 | Scandinavian Course Prototype | Interactive LMS harness + Utilitarian Home Academy | M2 | DONE |
| M4 | Production Theme Upgrade | Migrasi layout Jekyll ke Utilitarian Course Player & Home | M3 | DONE |
| M5 | Bespoke Native LMS Engine | Eliminasi GitBook & implementasi Full LMS Player + Drawer | M4 | DONE |



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
