---
name: ir-video-director
description: Workflow produksi video edukasi kanonik Mind Map Explanatory berbasis Remotion, RoughJS, font Patrick Hand, dan audio Kokoro-82M untuk IR Study Companion (@IRinANutshell).
---

# Mind Map Explanatory Video Director Skill

Gunakan skill ini sebagai standar resmi tunggal (*canonical standard*) dalam memproduksi video pembelajaran (*explanatory videos*) di seluruh ekosistem **IR Study Companion** dan channel YouTube resmi **`@IRinANutshell`**.

### 🎯 Tujuan Utama Pedagogis (Pre-Reading Cognitive Advance Organizer):
Video Mind Map Explanatory dirancang secara khusus untuk **ditonton oleh pembaca terlebih dahulu sebelum mulai membaca chapter**. Fungsinya adalah membangun peta mental (*mental schema*) yang utuh mengenai aktor, dinamika sistem, dan pertarungan paradigma dalam 5 menit, sehingga saat pembaca menyelami teks akademik bab yang padat, mereka sudah memiliki kompas konseptual yang kokoh.

---

## 🎨 Empat Prinsip Visualisasi Data & Desain Pedagogis

### 1. Decluttering (Fokus Bebas Noise & Reduksi Beban Kognitif)
- **Dynamic Spotlight Dimming**: Node yang sedang dijelaskan kamera aktif berdiri pada `opacity: 1.0` dengan bayangan fokus lembut (`drop-shadow: 0 8px 24px rgba(0,0,0,0.12)`). Seluruh node sekitarnya yang sedang tidak dibahas diredupkan ke `opacity: 0.35` untuk mencegah *split-attention effect*.
- **Progressive Disclosure**: Kartu dan panah muncul bertahap tepat pada saat diperkenalkan narator (`revealFrame`).
- **Selective Arrow Fade**: Panah konektor yang tidak menghubungkan konsep aktif memudar ke `opacity: 0.20` dengan garis tipis, menjaga kanvas tetap lapang.
- **Panorama Reset**: Pada pandangan panorama akhir, seluruh kartu kembali ke kecerahan penuh `100%`.

### 2. Captioning (Keterbacaan & Pemisahan Kognitif Hibrida)
- **Dual-Font System**:
  - *Kanvas Diagram*: **Patrick Hand** (Google Font tulisan tangan) untuk sensasi dosen/mentor mencoret papan tulis secara hangat.
  - *Kapsul Subtitle*: **Plus Jakarta Sans** (sans-serif geometris modern berdaya baca tinggi) di bagian bawah.
  - Pemisahan ini membedakan secara instan antara objek grafis yang dilihat dan narasi lisan yang didengar.
- **Safe-Zone Geometry**: Kapsul melayang di `bottom: 26px`, background dark slate glass `rgba(15, 23, 42, 0.88)` dengan teks putih `#FFFFFF` (rasio kontras >12:1). Jarak vertikal kartu ke subtitle selalu dijaga >280px saat zoom dekat.

### 3. Warna Semantik (Semantic Academic Color Hierarchy)
Dilarang menggunakan warna pastel acak tanpa makna. Skema warna wajib mencerminkan taksonomi teori Hubungan Internasional yang konsisten di semua bab:
- **Warm Yellow (`#FEFCBF`)**: Pertanyaan Inti, Hub Pusat, Ekosistem Platform.
- **Sky Blue (`#BEE3F8`)**: Aktor Negara, Kedaulatan Westphalia, Arsitektur Sistem.
- **Soft Coral/Crimson (`#FED7D7`)**: Realisme, Kekuatan Materi, Anarki (Tanpa 911), Konflik, Chokepoints.
- **Mint Green (`#C6F6D5`)**: Liberalisme, Kerjasama, Institusi Multilateral (PBB, WTO), Perdamaian Demokratis.
- **Soft Lavender (`#E9D8FD`)**: Konstruktivisme, Norma Sosial, Identitas, Pemikiran Wendt.
- **Paper White (`#FFFFFF`)**: Bukti Empiris, Studi Kasus, Kriteria Hukum (Montevideo 1933, Selat Malaka).

### 4. Storytelling Berfokus & 4-Act Narrative Arc
Data diceritakan dengan busur cerita terstruktur:
1. *The Hook & Actors*: Aktor negara vs non-negara.
2. *The Core Dilemma*: Kontras hukum domestik (telepon polisi) vs sistem internasional anarkis (tanpa 911).
3. *The Triad Lenses*: Navigasi berurutan ke lensa Realisme (Merah) ➔ Liberalisme (Hijau) ➔ Konstruktivisme (Ungu).
4. *The Panorama Synthesis*: Pull-back kamera sinematik `zoom: 0.39` merangkum 34 node, diakhiri dengan ajakan: *"Peta ini adalah kerangka kompas Anda. Sekarang, selami Bab ini dengan pemahaman yang utuh."*

---

## 🎥 Hukum Koreografi Kamera (The 3 Golden Camera Laws)

Kamera navigasi dikendalikan secara deterministik melalui segmen diskrit di [`CameraRig.ts`](file:///d:/PERSONAL%20PROJECT/IR-study-companion/simulation/ir-motion-library/src/flowchart/CameraRig.ts):

### Hukum 1: True Deep Zoom-In (`1.95x` – `2.05x`) saat Menjelaskan Detail
- Saat narasi suara menguraikan sebuah konsep atau kartu tertentu, kamera **WAJIB melakukan zoom-in mendalam** hingga skala `1.95x` – `2.05x`.
- Kartu membesar hingga mengisi ~42% lebar layar 1080p, dan teks tulisan tangan membesar 200%+ (~44px), sehingga terbaca sangat jelas di berbagai perangkat tanpa memicingkan mata (*anti-squinting*).
- Menghasilkan margin lapang >320px di atas kapsul subtitle bawah.

### Hukum 2: Stationary Hold ($v = 0$) selama Durasi Narasi
- Kamera **TIDAK BOLEH terus melayang tanpa henti** saat sebuah konsep sedang dijelaskan.
- Terapkan jendela *hold* `[holdStartFrame, holdEndFrame]` yang disinkronkan tepat dengan kalimat narasi di `subtitles.json`.
- Selama jeda ini, kecepatan kamera adalah **mutlak nol ($v = 0$)** selama 3 hingga 10 detik penuh, memberi audiens ketenangan membaca dan mencerna teks sebelum kamera bergerak ke titik berikutnya.

### Hukum 3: Contextual Zoom-Out (`1.15x` – `1.25x`) & Pull-Back Panorama (`0.39x`)
- Saat narasi beralih ke paradigma atau cabang besar baru (misal pengenalan Realisme vs Liberalisme), kamera melakukan **zoom-out** untuk memperlihatkan struktur percabangan makro.
- Pada penutup video (Slide 8), kamera melakukan *pull-back* sinematik (`zoom: 0.39`) menampilkan seluruh jaringan 30+ kartu konsep dalam satu lanskap terpadu.
- Transisi antar-posisi menggunakan kurva kosinus *ease-in-out* ($0.5 \cdot (1 - \cos(\pi \cdot t))$) sepanjang 30–45 frame untuk menjamin kehalusan bebas sentakan.

---

## 🎙️ Audio & Subtitle Hygiene

1. **Neural Voiceover**: Sintesis lokal SOTA via **Kokoro-82M (v1.0)** atau Edge-TTS, menghasilkan pelafalan alami dengan jeda artikulasi manusia.
2. **Kapsul Subtitle Melayang**: Terletak di bagian bawah layar (`bottom: 24px`, background gelap semi-transparan `rgba(15, 23, 42, 0.92)`).
3. **Zero-Collision Mandate**:
   - Dilarang menempatkan watermark tetap di sudut layar yang dapat menabrak kartu saat zoom dekat.
   - Ruang vertikal kartu selalu dijaga >300px di atas posisi subtitle.

---

## 🚀 Alur Kerja Produksi 5 Tahap (5-Phase Production Pipeline)

```
[Bab Materi _chapters/*.md]
       │
       ▼
[Fase 1: Ekstraksi Naskah & Graf Mind Map]
       │ (30-35 Nodes, Judul Ringkas, Subtitle, Bullet Points, Koneksi Panah)
       ▼
[GATE REVIEW WAJIB: Presentasikan Mind Map Preview ke User]
       │ ⛔ STOP: Tunggu persetujuan (ACC) dari User sebelum lanjut!
       ▼ (Setelah di-ACC)
[Fase 2: Sintesis Audio & Word/Sentence Alignment]
       │ (voiceover.mp3 + public/subtitles.json)
       ▼
[Fase 3: Pemetaan Koordinat & Kamera Remotion]
       │ (flowchartData.ts: Koordinat X/Y, revealFrame, CAMERA_SEGMENTS)
       ▼
[Fase 4: Inspection Gate (Still Frame Previews)]
       │ (npx remotion still FlowchartVideo out/preview_X.png --frame=...)
       │ Evaluasi visual: Center, Zoom-in depth, Keterbacaan teks, Nol tabrakan panah
       ▼
[Fase 5: Render Master Final MP4 & YouTube Thumbnail]
       │ (1. npx remotion render FlowchartVideo learning-videos/exports/nama_video.mp4)
       │ (2. npx remotion still FlowchartVideo learning-videos/posters/nama_video_Poster.png --frame=...)
       │ (3. python scripts/generate_thumbnail.py --title "..." --image "..." --output learning-videos/posters/nama_video_Thumbnail.png)
       │ (4. Sinkronkan metadata ke catalog.json, README.md, dan frontmatter chapter)
       ▼
[Selesai: Siap Rilis ke YouTube / LMS]
```

### Panduan Lokasi Berkas di Repositori:
- **Engine Produksi Utama**: [`simulation/ir-motion-library/`](file:///d:/PERSONAL%20PROJECT/IR-study-companion/simulation/ir-motion-library/)
- **Data Mind Map & Kamera**: `simulation/ir-motion-library/src/flowchart/flowchartData.ts`
- **Komponen Inti**: `src/flowchart/RoughNode.tsx`, `RoughArrow.tsx`, `CameraRig.ts`, `FlowchartCanvas.tsx`, `FlowchartSubtitle.tsx`
- **Output Video Master**: `learning-videos/exports/*.mp4`
- **Output Poster & Thumbnail**: `learning-videos/posters/*_Poster.png` & `*_Thumbnail.png`
- **Generator Thumbnail Kanonik**: `scripts/generate_thumbnail.py` (didukung template master `scripts/assets/thumbnail_overlay_template.png`)
