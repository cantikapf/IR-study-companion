# SHORTS PLAN v3 — Archival Micro-Documentary

Status: **PLAN ONLY — menunggu ACC pengguna sebelum eksekusi.**
Tanggal: 2026-10-10 · Folder kerja: `learning-videos/shorts-experiments/archival-run/`
Builder yang diusulkan: **model Antigravity via 9router** (bukan Vikey).

---

## 1. Diagnosis: kenapa 3 percobaan sebelumnya gagal

| Percobaan | Masalah inti | Bukti |
|---|---|---|
| Realism Kinetic | Kinetic typography = tidak ada **mekanisme visual**, hanya kata besar bergerak. Tidak ada entitas/artefak nyata yang bisa dilihat. | brief `realism-kinetic/brief.md` (glassmorphic cards, reticles) |
| Madmam Austria (v1 & v2) | Peta memakai **batas negara modern**. Dataset peta historis (aourednik/historical-basemaps) terlalu kasar: pada 1200–1300 Austria hanya satu poligon "Holy Roman Empire". Cerita Habsburg tidak bisa divisualisasikan secara akurat. | diverifikasi hari ini: `world_1200/1279/1300.geojson` → hanya `Holy Roman Empire` |
| Comedic 38-min | Nada komedi + 38 menit, bukan format Shorts. | — |

**Kesimpulan:** kegagalan bukan pada kurang "cinematic", tapi pada **ketiadaan materi visual nyata yang boleh diklaim akurat**.

---

## 2. Riset format (dengan sumber)

Fakta yang dipakai untuk memilih format — semua dari sumber yang bisa dibuka:

- **>80% Shorts ditonton tanpa suara** → caption *burned-in* bukan opsional. ([fluxnote](https://fluxnote.io/guides/how-to-make-history-shorts-with-ai))
- **Hook di 2 detik pertama** menahan **+19%** penonton; retensi rata-rata Shorts 73%, viral ~76%. ([zebracat](https://www.zebracat.ai/post/youtube-shorts-statistics))
- **Panjang ideal 45–60 detik** untuk micro-dokumenter sejarah; 30–55 detik tetap sehat. ([fluxnote strategy](https://fluxnote.io/guides/youtube-shorts-history-strategy))
- **Arsip + peta = visual retensi tertinggi** di konten sejarah; "moving maps are the highest-retention visual in history content". ([flowshorts](https://flowshorts.app/faceless-reels/history))
- **Bukti kanal**: Geo History — 1,0 jt sub, 156,1 jt views, 130 video, rata-rata Shorts ~7,6 jt views. ([channelslike](https://www.channelslike.com/@geohistory))

**Format yang dipilih: `Archival Micro-Documentary`**
Artwork/engravir/peta arsip domain-publik asli sebagai bahan utama, gerak kamera halus (Ken Burns), caption editorial tebal, narasi Kokoro. **Bukan** kinetic text, **bukan** peta buatan sendiri.

Alasan saya **mampu** mengerjakan ini dengan bagus (sudah diverifikasi hari ini, bukan asumsi):
- Wikimedia Commons API memberi aset resolusi tinggi berlisensi CC0/public-domain → **0 biaya, 0 risiko klaim**.
- Remotion sudah terpasang di `simulation/ir-motion-library` (Remotion 4.0.473, `d3-geo`, `topojson-client`, `world-atlas`).
- Tidak ada animasi yang perlu "dikarang" — risiko visual gagal jauh lebih kecil.

---

## 3. Topik produksi #1 (fakta terverifikasi, bukan karangan)

**Pulau Run: pulau Indonesia yang ditukar dengan Manhattan.**

Sangat cocok untuk `@IRinANutshell`: cerita HI global, tetapi **berpusat di Maluku, Indonesia**.

Fakta yang akan dipakai di naskah — semua bersumber:

| Fakta | Sumber |
|---|---|
| Run (Pulau Rhun), Banda, Maluku — panjang 3 km, lebar 1 km, luas 13,16 km², penduduk 1.572 (estimasi pertengahan 2022) | [Wikipedia Run (island)](https://en.wikipedia.org/wiki/Run_(island)) |
| Hingga pertengahan abad ke-19, Banda adalah **satu-satunya** sumber pala & mace dunia | [Wikipedia Banda Islands](https://en.wikipedia.org/wiki/Banda_Islands) |
| 1616: Nathaniel Courthope mendarat 25 Desember, bersekutu dengan penduduk, mendirikan benteng | [Wikipedia Courthope](https://en.wikipedia.org/wiki/Nathaniel_Courthope) |
| Courthope dan 39 orang bertahan **1.540 hari**, ia tewas 1620 | [worldhistory.org](https://www.worldhistory.org/article/1872/european-discovery--conquest-of-the-spice-islands/) |
| 1664: Inggris merebut Nieuw Amsterdam; 1667 Perjanjian Breda (31 Juli) mengukuhkan *uti possidetis* — Inggris tetap pegang Nieuw Netherland, Belanda tetap pegang Run & Suriname | [Pepys Diary / Wikipedia Breda](https://www.pepysdiary.com/encyclopedia/14095/) |
| Pohon pala **masih** tumbuh di Run sampai hari ini | [Wikipedia Run](https://en.wikipedia.org/wiki/Run_(island)) |

**Kejujuran naratif (wajib):** Perjanjian Breda **bukan** "tukar-menukar iseng". Secara hukum prinsipnya *uti possidetis* — masing-masing menahan apa yang sudah dikuasai. Narasi akan menyebut ini. Angka "$24" trinket Manhattan **tidak** akan dipakai (disputed).

**Panjang target:** ~45 detik (≈1.350 frame @30fps).

---

## 4. Aset arsip yang SUDAH diverifikasi tersedia

Semua dari Wikimedia Commons, lisensi CC0 / Public domain:

| Kebutuhan shot | Aset | Lisensi | Resolusi |
|---|---|---|---|
| Pala di Banda (1599) | `Nootmuskaat van de Banda-eilanden, 1599, RP-P-OB-75.396.jpg` | CC0 | 5296×4028 |
| Peta Kepulauan Maluku abad ke-17 | `B26056059K - Les Isles Molvcqves; Celebes, Gilolo.jpg` | CC0 | 5400×4191 |
| Peta Nieuw Amsterdam 1660 | `Redraft of the Castello Plan New Amsterdam in 1660` | Public domain | 5776×4197 |
| Perjanjian Breda 1667 | `Vrede van Breda, 1667, RP-P-OB-82.067.jpg` | CC0 | 5666×4606 |
| Buah pala (*Myristica fragrans*) | `Myristica fragrans by kadavoor.jpg` | CC BY-SA 4.0 (atribusi wajib) | 2479×2502 |

> Catatan lisensi: item CC BY-SA 4.0 perlu kredit di deskripsi video. CC0/PD tidak. Ini dicatat di manifest aset.

---

## 5. Struktur naskah 6-beat (draft, ~45 detik)

| # | Waktu | Narasi (EN) | Visual |
|---|---|---|---|
| 1 | 0–4s | Teks hook, diucapkan | Peta Maluku abad-17, dorong cepat ke satu titik kecil di barat |
| 2 | 4–12s | Pulau 3 km, satu-satunya pala di dunia | Close-up buah pala + mace |
| 3 | 12–20s | 1616: orang Inggris mendudukinya, bertahan 1.540 hari | Engravir/peta; pin tahun |
| 4 | 20–28s | Pohon pala ditebang; 1664 Inggris rebut Nieuw Amsterdam | Peta Castello 1660 |
| 5 | 28–36s | 1667 Breda: satu pulau Indonesia ↔ satu pulau Amerika | Dokumen Vrede van Breda 1667 |
| 6 | 36–45s | Hari ini Run penduduk 1.572, pala masih tumbuh. Manhattan jadi New York | Foto/frame penutup + kartu fakta |

Naskah final akan ditulis dalam bahasa Inggris akademik (mandat English-only), ditampilkan untuk ACC bersama storyboard.

---

## 6. Arsitektur produksi

```
learning-videos/shorts-experiments/archival-run/
  brief.md              ← kontrak produksi
  script/script.json    ← 6 beat + narasi + durasi
  assets/               ← aset Commons terunduh + MANIFEST.json (lisensi, sumber, URL)
  audio/voiceover.mp3   ← Kokoro-82M (pipeline yang sudah ada)
  audio/manifest.json
  checkpoints/*.png     ← still per beat untuk QA
  output/*.mp4
```

Komposisi Remotion baru: `src/shorts/ArchivalDocRun.tsx` di `simulation/ir-motion-library`, didaftarkan di `Root.tsx`.
Prinsip deterministik: gerak berbasis frame, tanpa CSS transition, `prefers-reduced-motion` dihormati.

**Peta:** hanya dipakai sebagai **locator** yang diberi label tahun + sumber. Tidak ada pewarnaan wilayah sebagai "kepemilikan" tanpa dasar dataset historis.

---

## 7. Eksekusi memakai model Antigravity via 9router

Hasil audit akses model hari ini (dites langsung, bukan asumsi):

| Model | Status |
|---|---|
| `ag/gemini-3.8-flash-high` | ✅ **jalan** (streaming OK) |
| `ag/gemini-3.8-flash` | tersedia |
| `ag/claude-sonnet-4-6` | ⚠️ **429 quota** (perlu tunggu) |
| `ag/claude-opus-4-6-thinking` | ❌ unavailable ±21 jam |

**Konsekuensi jujur untuk rencana:**
- **Builder** = `ag/gemini-3.8-flash-high` → OK sekarang.
- **Vision QA** (senjata utama supaya tidak "jelek tanpa dicek") = `ag/claude-sonnet-4-6` masih kena kuota; sampai pulih, QA visual dijalankan lewat tool `vision_analyze` milik Hermes (independen dari kuota Antigravity).
- `remotion-opus-skill` (yang Anda minta diinstal) **sudah terpasang**, tetapi CLI-nya butuh API Vikey. Bisa diarahkan ke 9router lewat `VIKEY_BASE_URL=http://127.0.0.1:20128/v1`, namun engine-nya (flythrough/poster/**kinetic**) bukan format Shorts sejarah — jadi **tidak** akan dipakai sebagai engine; opsional hanya sebagai tooling pendamping.

**Gate wajib (sesuai HERMES.md) — QA visual tidak bisa dilewati:**
Setiap beat dirender sebagai still → diperiksa `vision_analyze` → baru lanjut. Tidak ada penyerahan hasil tanpa cek visual.

---

## 8. Yang saya minta dari Anda (gerbang ACC)

1. **Setuju format `Archival Micro-Documentary`** (arsip asli, bukan kinetic, bukan peta modern)?
2. **Setuju topik Pulau Run ↔ Manhattan** sebagai video #1?
3. Kalau setuju keduanya → saya tulis naskah lengkap + storyboard beat-by-beat, lalu **berhenti lagi untuk ACC kedua** sebelum audio/render (sesuai Mandatory Review Gate).