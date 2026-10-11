# YouTube Shorts Production Workflow & Catalog Registry

Dokumen ini adalah **Single Source of Truth (SSOT)** resmi untuk lini produksi konten **YouTube Shorts (@IRinANutshell)** dalam proyek IR Study Companion.

Format resmi: **Animated Geopolitical Vector Map (Vox-Style)** berbasis **D3-Geo + GSAP 60 FPS**, disuarakan oleh **Kokoro-82M ONNX (`af_heart`)**, dan di-render secara **Deterministik via CDP (1080×1920 30 FPS)**.

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
| **02** | `SH-02` | **The First Nuclear Strike: Operation Dropshot** | Garis Arktik, Koridor ICBM Soviet & Pangkalan SAC AS (1949) | `_chapters/012-modern-world-history/120-domino-cold-war.md` | Ready to Produce | - |
| **03** | `SH-03` | **The South China Sea Chokepoint: Nine-Dash Line Standoff** | Kepulauan Spratly, Scarborough Shoal, & Selat Malaka | `_chapters/044-regionalism-in-southeast-asia-asean-community/050-asean-community.md` | Planned | - |
| **04** | `SH-04` | **The Berlin Air Corridor: Operation Vittles** | 3 Koridor Udara Sekutu Tempelhof vs Blokade Soviet (1948) | `_chapters/012-modern-world-history/100-post-ww.md` | Planned | - |
| **05** | `SH-05` | **The UN Security Council Veto Trap** | Resolusi Perang Korea 1950 & Boikot Soviet Yakov Malik | `_chapters/045-international-organization-in-international-relations/050-UN-security.md` | Planned | - |
| **06** | `SH-06` | **The 1914 Mobilization Clock: The Schlieffen Plan** | Jaringan Rel Kereta Api Mobilisasi Jerman, Belgia, Prancis | `_chapters/012-modern-world-history/040-road-to-ww1.md` | Planned | - |
| **07** | `SH-07` | **The Suez Crisis: Death of an Empire** | Kanal Suez, Pasukan Terjun Payung Anglo-Prancis, Ancaman Finansial AS (1956) | `_chapters/012-modern-world-history/150-decolonization.md` | Planned | - |
| **08** | `SH-08` | **The Strait of Hormuz: World Economy's Jugular Vein** | Titik Penyempitan Selat Hormuz (21 mil) & Kapal Tanker Minyak Dunia | `_chapters/022-introduction-to-security-studies/020-realism-security.md` | Planned | - |
| **09** | `SH-09` | **UNCLOS Maritime Borders: The Cod Wars** | Ekspansi Zona Perikanan Islandia 4 mil ke 200 mil vs Royal Navy | `_chapters/042-international-law-issues-and-international-dispute-settlement/080-law-of-the-sea.md` | Planned | - |
| **10** | `SH-10` | **The Prisoner's Dilemma of Nuclear Arms: Cold War MAD** | Matriks Teori Permainan: Tembak Duluan vs Kooperasi Damai | `_chapters/023-theories-of-international-relations/092-game-theory-ir.md` | Planned | - |

---

## 🛠️ CLI Runner Produksi Cepat

Untuk memproduksi dan merender episode Shorts berikutnya menggunakan template deterministik:
```bash
# 1. Masuk ke direktori eksperimen shorts
cd learning-videos/shorts-experiments/sh-05-cuban-crisis-map-animation/

# 2. Render MP4 1080x1920 (Frame-by-Frame CDP Stepper)
node render_shorts_deterministic.js

# 3. Hasil ekspor tersimpan di:
# learning-videos/exports/
```
