# 🎓 IR Study Companion — Learning Videos Vault

Selamat datang di direktori penyimpanan dan pemantauan video pembelajaran resmi **IR Study Companion** & channel YouTube [`@IRinANutshell`](https://www.youtube.com/@IRinANutshell).

Direktori ini dirancang sebagai repositori terpusat untuk mengelola, melacak, dan mengotomatisasi seluruh siklus produksi video penjelasan materi berbasis **Mind Map Explanatory**.

---

## 🏛️ 1. Standar Sistem Penamaan (Naming Convention)

Untuk memastikan seluruh video mudah disortir, dipantau statusnya, dan dihubungkan secara otomatis dengan bab kurikulum Jekyll serta metadata YouTube Studio, diterapkan format penamaan deterministik berikut:

### Format Berkas Video:
```text
IR_M{ModuleNumber}_CH{ChapterNumber}_{TitleInSnakeCase}_{Format}_{Resolution}.{ext}
```

### Penjelasan Komponen Token:
| Token | Deskripsi | Contoh |
| :--- | :--- | :--- |
| `IR` | Identitas namespace kurikulum (International Relations) | `IR` |
| `M{Module:02d}` | Nomor modul kurikulum (01 s.d. 18) | `M01` (Modul 1: Intro to IR) |
| `CH{Chapter:03d}` | Nomor indeks bab kurikulum (010, 020, dst.) | `CH010` (Bab 010) |
| `{Title}` | Judul akademik bab (Pascal/Snake Case tanpa spasi/simbol) | `Foundations_of_International_Relations` |
| `{Format}` | Format visual video (`MindMap`, `DeepDive`, `CaseStudy`) | `MindMap` |
| `{Resolution}` | Resolusi dan framerate standar ekspor | `1080p` (1920x1080 @ 30 FPS) |
| `.{ext}` | Ekstensi berkas | `.mp4` (video), `.png` (poster/thumbnail) |

### Contoh Nyata Berkas:
- **Video Export (MP4):**  
  `learning-videos/exports/IR_M01_CH010_Foundations_of_International_Relations_MindMap_1080p.mp4`
- **Poster Mind Map (PNG):**  
  `learning-videos/posters/IR_M01_CH010_Foundations_of_International_Relations_Poster.png`
- **Official YouTube Thumbnail 1080p (PNG):**  
  `learning-videos/posters/IR_M01_CH010_Foundations_of_International_Relations_Thumbnail.png`

---

## 📊 2. Dasbor Inventarisasi & Status Video (Video Inventory Matrix)

| ID Video | Modul & Bab | Judul Materi | Format | Durasi | Resolusi | Status Render | YouTube Thumbnail | YouTube Channel (@IRinANutshell) |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| `IR-M01-CH010` | M01 / CH010 | Foundations of International Relations | Mind Map Explanatory | 05:16 | 1080p | 🟢 RENDERED (41.2 MB) | 🟢 READY | [Sa0PnnZLn0w](https://youtu.be/Sa0PnnZLn0w) |
| `IR-M01-CH020` | M01 / CH020 | Globalization and Global Politics | Mind Map Explanatory | 03:00 | 1080p | 🟢 PUBLISHED | 🟢 READY | [7K4preE-EBY](https://youtu.be/7K4preE-EBY) |
| `IR-M01-CH030` | M01 / CH030 | Basic Explanation of Realism in IR | Mind Map Explanatory | 05:23 | 1080p | 🟢 PUBLISHED (51.8 MB) | 🟢 GENERATED | [3VDcQVYty5M](https://youtu.be/3VDcQVYty5M) |
| `IR-M01-CH040` | M01 / CH040 | Basic Explanation of Liberalism in IR | Mind Map Explanatory | 06:21 | 1080p | 🟢 PUBLISHED (49.3 MB) | 🟢 GENERATED | [FdChrS6Ng3Y](https://youtu.be/FdChrS6Ng3Y) |
| `IR-M01-CH050` | M01 / CH050 | Basic Explanation of Marxism in IR | Mind Map Explanatory | 06:48 | 1080p | 🟢 RENDERED (30.0 MB) | 🟢 GENERATED | *Ready for Upload* |
| `IR-M01-CH060` | M01 / CH060 | Basic Explanation of Constructivism in IR | Mind Map Explanatory | — | 1080p | ⚪ QUEUED | ⚪ PENDING | *Pending* |

> **Catatan Status:**  
> - 🟢 **RENDERED**: Berkas MP4 siap diputar secara lokal dan diunggah ke YouTube.  
> - 🟡 **RENDERING**: Sedang dalam proses rendering komputasi Remotion.  
> - ⚪ **QUEUED**: Naskah/dataset terdaftar dan masuk antrean produksi.

---

## 📁 3. Struktur Direktori

```text
learning-videos/
├── README.md               # Master Documentation & Video Registry Matrix (File ini)
├── catalog.json            # Machine-readable metadata catalog untuk integrasi web/LMS
├── exports/                # Direktori penyimpanan master berkas video MP4 (git-ignored)
│   ├── .gitkeep
│   └── IR_M01_CH010_Foundations_of_International_Relations_MindMap_1080p.mp4
└── posters/                # Thumbnail resmi 1080p untuk kartu web dan YouTube
    ├── .gitkeep
    └── IR_M01_CH010_Foundations_of_International_Relations_Poster.png
```

---

## 🛠️ 4. Panduan Eksekusi Produksi (Production Pipeline)

### Merender Video Baru via Remotion CLI:
Untuk merender komposisi `FlowchartVideo` ke dalam folder ekspor dengan penamaan standar:

```powershell
cd simulation/ir-motion-library
npx remotion render FlowchartVideo "../../learning-videos/exports/IR_M01_CH010_Foundations_of_International_Relations_MindMap_1080p.mp4"
```

### Mengambil Preview Still Frame (Poster Panorama):
Untuk mengambil tangkapan layar frame tertentu (misal Frame 9200 untuk pemandangan panorama):

```powershell
cd simulation/ir-motion-library
npx remotion still FlowchartVideo "../../learning-videos/posters/IR_M01_CH010_Foundations_of_International_Relations_Poster.png" --frame=9200
```

### Membuat Official YouTube Thumbnail (1080p Split Brush Mask):
Untuk menghasilkan YouTube Thumbnail kanonik berformat split-canvas dengan brush torn-paper edge dan typography Archivo Black + Space Mono:

```powershell
uv run --with pillow python scripts/generate_thumbnail.py `
  --title "REALISM`nIN`nGLOBAL POLITICS" `
  --image "learning-videos/posters/realism_visual_chess.jpg" `
  --output "learning-videos/posters/IR_M01_CH030_Basic_Explanation_of_Realism_in_IR_Thumbnail.png"
```

---

## 🔒 5. Kebijakan Isolasi Git (Git Large-Asset Isolation)
Sesuai dengan pedoman proyek di `.agents/rules/lessons-learned.md`, berkas biner video `.mp4` berukuran besar (>50 MB) **secara otomatis diabaikan** oleh Git melalui `.gitignore` (`learning-videos/exports/*.mp4`). 

Hal ini memastikan repositori GitHub tetap ramping, cepat, dan bebas risiko penolakan kuota upload (GitHub 100 MB hard limit), sementara dokumentasi pelacak (`README.md` dan `catalog.json`) tetap tersinkronisasi 100% di version control.
