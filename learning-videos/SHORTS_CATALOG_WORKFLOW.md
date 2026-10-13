# YouTube Shorts Production Workflow & Catalog Registry

Dokumen ini adalah **Single Source of Truth (SSOT)** resmi untuk lini produksi konten **YouTube Shorts (@IRinANutshell)** dalam proyek IR Study Companion.

Format resmi lini produksi YouTube Shorts (@IRinANutshell): **Animated Geopolitical Vector Map (HyperFrames + D3-Geo)** — peta vektor proyeksi riil (polar azimuthal / Mercator) dengan animasi kamera matriks 2D GPU, rute bomber/armada, arc target, dan **kartu dossier foto tokoh/dokumen autentik sebagai inset kecil** saat narasi menjelaskan figur/peristiwa terkait (bukan slideshow foto/teks layar penuh).

Audio: disuarakan narasi profesional (ElevenLabs / Kokoro) dengan sinkronisasi waktu kata deterministik, di-render via **`hyperframes render`** atau **CDP deterministic stepper** (1080×1920 30 FPS). Output tersimpan di `learning-videos/exports/`.

---

## 🗺️ Pipeline Produksi YouTube Shorts (5 Tahap Deterministik)

```
┌────────────────────────────────────────────────────────────────────────┐
│                   5-STEP SHORTS PRODUCTION PIPELINE                    │
├────────────────────────────────────────────────────────────────────────┤
│ 1. RESEARCH & SCRIPT ➔ 5 Beat Naskah Dramatis (<45s) & Subtitle Vektor │
│ 2. AUDIO SYNTHESIS   ➔ Kokoro-82M ONNX (Voice: af_heart, Speed: 1.08x) │
│ 3. D3-GEO VECTOR RIG ➔ Single-Pass Proyeksi + Hardware 2D Matrix Camera│
│ 4. VISUAL AUDIT QA   ➔ vision_analyze CDP Stills (Bebas Cut & Overlap) │
│ 5. EXPORT & SYNC     ➔ Deterministik MP4 1080x1920 + Git & Web Link    │
└────────────────────────────────────────────────────────────────────────┘
```

### Standar Teknis Wajib:
1. **Resolusi & Aspek Rasio**: 1080 × 1920 (9:16 Vertikal).
2. **Durasi Ideal**: 40.0 – 45.0 detik (Maksimum batas YouTube Shorts: <60 detik).
3. **Engine Visual**: D3-Geo (`countries-110m.json`) + GSAP 60 FPS + SVG hardware transform matrix.
4. **Pencegahan Cacat Visual**:
   - Zero-Flash: Deteksi piksel awal via PIL (`brightness < 100`) dengan trim `-ss` FFmpeg otomatis.
   - Zero-Stutter: Seek deterministik per frame ($f/30.0$) via CDP `Page.captureScreenshot` di-pipe ke stdin FFmpeg.
   - Zero-Collision: Seluruh label taktis wajib di-center (`text-anchor="middle"`) dan diletakkan di `<g id="tactical-labels-layer">` teratas dengan kotak pekat `#060912`.
   - Safe-Zone Vertikal: Subtitle dan telemetri bawah wajib berada di atas `bottom > 380px` agar tidak tertutup antarmuka pemutar YouTube Shorts di HP.

---

## 📋 Catalog Registry YouTube Shorts (10 Episode Top-of-Funnel)

Daftar 10 episode video Shorts taktis terencana yang dipetakan ke 10 Diplomatic Labs dan bab-bab kurikulum kunci:

| # | ID Seri | Topik / Judul Episode | Studi Kasus / Lokasi Geopolitik | Bab Kurikulum Terkait | Status Produksi | Tautan YouTube |
|---|---|---|---|---|---|---|
| **01** | `SH-01` | **The Cuban Missile Crisis: One Vote from Oblivion** | San Cristóbal, Selat Florida, & Sargasso Sea (1962) | `_chapters/012-modern-world-history/130-cuban-missile-crisis.md` | **PUBLISHED** | [Tonton Shorts](https://youtube.com/shorts/WYGiVcO6jNA) |
| **02** | `SH-02` | **The First Nuclear Strike: Operation Dropshot** | Pangkalan SAC AS, Koridor Bomber Lintas Kutub, & Semipalatinsk (1949) | `_chapters/012-modern-world-history/120-domino-cold-war.md` | **PUBLISHED** | [Tonton Shorts](https://youtube.com/shorts/Ws5VoblIcts) |
| **03** | `SH-03` | **The South China Sea Chokepoint: Nine-Dash Line Standoff** | Kepulauan Spratly, Scarborough Shoal, & Selat Malaka | `_chapters/044-regionalism-in-southeast-asia-asean-community/050-asean-community.md` | Planned | - |
| **04** | `SH-04` | **The Berlin Air Corridor: Operation Vittles** | 3 Koridor Udara Sekutu Tempelhof vs Blokade Soviet (1948) | `_chapters/012-modern-world-history/100-post-ww.md` | Planned | - |
| **05** | `SH-05` | **The UN Security Council Veto Trap** | Resolusi Perang Korea 1950 & Boikot Soviet Yakov Malik | `_chapters/045-international-organization-in-international-relations/050-UN-security.md` | Planned | - |
| **06** | `SH-06` | **The 1914 Mobilization Clock: The Schlieffen Plan** | Jaringan Rel Kereta Api Mobilisasi Jerman, Belgia, Prancis | `_chapters/012-modern-world-history/040-road-to-ww1.md` | Planned | - |
| **07** | `SH-07` | **The Suez Crisis: Death of an Empire** | Kanal Suez, Pasukan Terjun Payung Anglo-Prancis, Ancaman Finansial AS (1956) | `_chapters/012-modern-world-history/150-decolonization.md` | Planned | - |
| **08** | `SH-08` | **The Strait of Hormuz: World Economy's Jugular Vein** | Titik Penyempitan Selat Hormuz (21 mil) & Kapal Tanker Minyak Dunia | `_chapters/022-introduction-to-security-studies/020-realism-security.md` | Planned | - |
| **09** | `SH-09` | **UNCLOS Maritime Borders: The Cod Wars** | Ekspansi Zona Perikanan Islandia 4 mil ke 200 mil vs Royal Navy | `_chapters/042-international-law-issues-and-international-dispute-settlement/080-law-of-the-sea.md` | Planned | - |
| **10** | `SH-10` | **The Prisoner's Dilemma of Nuclear Arms: Cold War MAD** | Matriks Teori Permainan: Tembak Duluan vs Kooperasi Damai | `_chapters/023-theories-of-international-relations/092-game-theory-ir.md` | Planned | - |

---

## 📷 Catalog Registry Single Photo Story (SP-xx Series)

Format editorial alternatif anti-AI feel: 1 foto arsip autentik resolusi ultra-tinggi ($\ge 2720\text{px}$) + Ken Burns editorial + narasi Kokoro TTS + aksen shutter kamera mekanis:

| # | ID Seri | Topik / Judul Episode | Foto Arsip / Subjek Sejarah | Bab Kurikulum Terkait | Status Produksi | Tautan YouTube |
|---|---|---|---|---|---|---|
| **01** | `SP-01` | **One of These Men Will Die in 60 Days: The Yalta Photo Story** | NARA 111-SC-260486 (Livadia Palace, 1945) — Churchill, Roosevelt, Stalin | `_chapters/012-modern-world-history/090-end-ww2.md` | **PUBLISHED** | [Tonton Shorts](https://youtube.com/shorts/OP6fEXloh-k) |

---

## 🛠️ CLI Runner Produksi Cepat

### Jalur kanonik (Animated Geopolitical Vector Map / HyperFrames) — SH-02 "Operation Dropshot"

```bash
cd learning-videos/shorts-experiments/sh-02-operation-dropshot-map-hf/

# 1. Bangun index.html dari data proyeksi dan audio manifest
py -3.13 build_html.py

# 2. Gate QA wajib (lint + runtime + layout + motion + kontras WCAG)
npx --yes hyperframes@0.8.145 check

# 3. Render rilis — MP4 >20 MB ke learning-videos/exports/ (gitignored)
npx --yes hyperframes@0.8.145 render -q delivery \
  -o "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/exports/SH02_Operation_Dropshot_Map_Animation_Short_1080p.mp4"
```

### Jalur alternatif (Animated Geopolitical Vector Map / D3-Geo)

```bash
cd learning-videos/shorts-experiments/sh-05-cuban-crisis-map-animation/
node render_shorts_deterministic.js   # frame-by-frame CDP stepper
```
