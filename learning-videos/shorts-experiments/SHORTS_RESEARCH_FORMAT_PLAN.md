# SHORTS RESEARCH — 3 Format Tiruan + Plan Produksi

Status: **RISET + PLAN — menunggu ACC pengguna sebelum eksekusi Fase 2.**
Tanggal riset: 2026-10-10 · Sumber: YouTube Shorts search `history` (live scrape) + verifikasi kanal via oEmbed.
Folder kerja yang diusulkan: `learning-videos/shorts-experiments/`

---

## 1. Data riset (live, bukan asumsi)

Di-scrape langsung dari `youtube.com/results?search_query=history+shorts` (filter Shorts, `sp=EgIYAQ%3D%3D`), kanal diverifikasi via `youtube.com/oembed`:

| Short | Kanal (terverifikasi) | Views | Format |
|---|---|---|---|
| Bizarre punishments from Ancient Rome (Part three) | **Absolute History** | 43M | Micro-doc arsip, satu topik aneh |
| Bizarre punishments from Tudor Britain (Part one) | **Absolute History** | 26M | Micro-doc arsip |
| How did FRANCE keep their MASSIVE secret?? | **Historically** | 17M | Reveal misteri + footage arsip |
| 60s before NUKE... (Japan) | **Historically** | 27M | Countdown ketegangan arsip |
| The Dance of Salomé by Leopold Schmutzler | **History by Mae** | 14M | Analisis 1 lukisan klasik |
| When disease affects fashion... | **History by Mae** | 7.6M | Analisis 1 lukisan klasik |
| Three wildly different historical eras that overlapped | **History by Mae** | 3.1M | Analisis artefak + timeline |
| Historical Facts That Will Distort Your Perception Of Time | **curiousitygeek** | 9.3M | Listicle distorsi waktu |
| Evolution of Turkey | **Histomex** | 4.7M | Evolusi peta/bendera |
| Shortest Wars in History | **Glore** | 2.6M | Ranking perbandingan |
| Eleanor's Aggressive Mothering | **Extra History** | 14M | Micro-doc karakter |
| 1,500-year-old roman senate doors still work | **Farzi_ST** | 17K | Fakta artefak tunggal |

**Pola yang berulang di semua yang viral:** (a) hook di 2 detik pertama, (b) caption burned-in besar (mayoritas ditonton tanpa suara), (c) **materi visual nyata** (lukisan/engravir/dokumen/footage asli) — bukan teks bergerak, (d) durasi 30–60 detik, (e) satu ide tajam per video.

---

## 2. Tiga format yang SAYA PILIH untuk ditiru & dibuat

Kriteria seleksi: harus bisa dikerjakan **dengan stack yang sudah terbukti ada di repo** dan bebas risiko visual/legal. Yang gagal di percobaan lama (kinetic typography; peta dengan batas negara modern) **tidak** dipilih lagi — lihat `SHORTS_PLAN_V3.md` §1.

### Format A — "Hidden Detail" Artifact Reveal (pola **History by Mae**, 14M/7.6M/3.1M)
- **Mekanisme:** satu lukisan/engravir domain-publik → slow Ken Burns zoom ke satu detail tersembunyi → narasi mengungkap makna historisnya.
- **Kenapa bisa saya buat:** 100% aset Wikimedia Commons PD/CC0 (lukisan abad ke-17–19), 0 biaya, 0 risiko klaim. Tidak ada animasi yang perlu "dikarang".
- **Tingkat kesulitan:** RENDAH. Komposisi baru diperlukan (Ken Burns + callout zoom), tapi tidak ada data geo rumit.

### Format B — Archival Micro-Documentary "One Weird Fact" (pola **Absolute History / Historically**, 43M/27M/26M/17M)
- **Mekanisme:** 5–6 beat arsip (peta kuno + engravir + dokumen) + narasi Kokoro + data chips + kapsul subtitle.
- **Kenapa bisa saya buat:** **sudah terbukti** — `ArchivalDocRun.tsx` + `archival-run/` ada di repo, MP4 sudah jadi, dan QA frame beat-1 lolos inspeksi visual (gold frame, docket badge, 2 data chip, subtitle di safe zone, nol overlap).
- **Tingkat kesulitan:** SANGAT RENDAH (engine jadi). Cukup ganti naskah + aset.

### Format C — Ranked Comparison / Data-Viz Countdown (pola **Glore / curiousitygeek**, 9.3M/2.6M)
- **Mekanisme:** ranking/deret "terpendek–terpanjang" atau timeline distorsi waktu, dirender sebagai bar/angka yang bergerak dengan narasi cepat.
- **Kenapa bisa saya buat:** murni data-driven; aset visual minimal (tipografi + ikon arsip kecil). Reuse `d3-geo`/`TimelineBar` yang sudah ada. Risiko render kecil.
- **Tingkat kesulitan:** RENDAH–SEDANG.

**Ditolak (dengan alasan):**
- Peta pewarnaan wilayah historis (pola Histomex/Madmam) → dataset historis di repo terlalu kasar (`Holy Roman Empire` satu poligon), sudah terbukti gagal 2×.
- Kinetic typography tanpa artefak nyata (pola Realism Kinetic) → tidak ada mekanisme visual, sudah terbukti gagal.

---

## 3. Plan produksi per format

### 3.1 Alur kerja kanonik (sama untuk ketiganya — mengikuti HERMES.md + `ir-video-director`)

```
FASE 1 · Ekstraksi naskah + shot graph (script.json + storyboard.md)
   │   ← ★ GERBANG ACC #1 (WAJIB BERHENTI). Presentasikan preview ke pengguna.
FASE 2 · Sintesis audio Kokoro-82M + manifest.json (durasi sampel nyata)
   │   ← ★ GERBANG ACC #2 (durasi final dikonfirmasi)
FASE 3 · Komposisi Remotion (per-frame deterministik, tanpa CSS transition)
FASE 4 · Inspection Gate: `npx remotion still` per beat → `vision_analyze`
FASE 5 · Render master MP4 (exports/) + Poster + Thumbnail → sync catalog.json & wiki
```

### 3.2 Kandidat topik (English-only, grounded di kurikulum IR — untuk `@IRinANutshell`)

| # | Format | Judul kerja (EN) | Beat | Aset inti (Wikimedia PD/CC0) |
|---|---|---|---|---|
| **SH-01** | B (micro-doc) | *The Island Traded for Manhattan* (Pulau Run) | 6 | Sudah lengkap di `archival-run/assets/` (Vrede van Breda 1667, Castello Plan 1660, peta Maluku, pala 1599) |
| **SH-02** | A (hidden detail) | *The Painting That Broke the Ottoman Myth* — analisis 1 lukisan VOC/Istana | 4 | 1 lukisan PD resolusi ≥1920 px + callout zoom |
| **SH-03** | C (ranking) | *The 5 Shortest Wars That Reshaped Borders* (Anglo-Zanzibar 38 min, Six-Day War, Football War…) | 6 | Bar-timeline + ikon peta arsip |
| **SH-04** | B (micro-doc) | *The Treaty Signed at a Ballroom* (Congress of Vienna 1815) | 6 | Engravir Kongres Wina, peta Eropa 1815 |
| **SH-05** | A (hidden detail) | *What the Nutmeg Portrait Hid* — detail engravir 1599 | 4 | `nutmeg_vintage_1599.jpg` (sudah ada) |

**Usulan urutan eksekusi:** SH-01 (engine sudah jadi, paling cepat membuktikan pipa) → SH-03 (paling murah) → SH-02/SH-05 (eksperimen Format A).

### 3.3 Struktur direktori per video

```
learning-videos/shorts-experiments/<slug>/
  brief.md            ← kontrak produksi + klaim yang diverifikasi
  storyboard.md       ← shot list beat-by-beat (preview untuk ACC #1)
  script/script.json  ← beat + narasi EN + durasi target
  assets/*.jpg        ← aset Commons + MANIFEST.json (lisensi, sumber, URL)
  audio/voiceover.mp3 + audio/manifest.json
  checkpoints/*.png   ← still per beat untuk QA
  output/*.mp4
```

### 3.4 Aturan tak-boleh-dilanggar (dari skill + lessons-learned)
- Caption burned-in, bold uppercase, keyword kuning; aman di `y:1320–1490`, bottom buffer >360 px.
- Gerak per-frame deterministik; Ken Burns 1.04×–1.15×; hold saat kalimat penting; nol `backdropFilter: blur()` (render headless timeout).
- Pre-scale aset ke ≤1920 px sebelum render.
- **English-only** untuk semua teks on-screen (mandat HERMES.md).
- Setiap tanggal/nama/perjanjian wajib diverifikasi ke sumber identifiabel; sebut doktrin hukum secara akurat (mis. *uti possidetis*); jangan klaim angka yang disengketakan (mis. "$24").

---

## 4. Tools yang dipakai (semua sudah terpasang — terverifikasi hari ini)

| Tool | Versi terverifikasi | Fungsi |
|---|---|---|
| Remotion + @remotion/cli | 4.0.533 | Engine render video |
| React / react-dom | 19.2.3 | Komposisi |
| roughjs | 4.6.6 | Gaya coretan tangan (kanonik M9) |
| d3-geo, topojson-client, world-atlas | 3.1.1 / 3.1.0 / 2.0.2 | Locator peta (bukan klaim wilayah) |
| @remotion/google-fonts | 4.0.533 | Patrick Hand / Plus Jakarta Sans |
| kokoro-onnx + onnxruntime | 0.6.1 / 1.22.1 | Neural TTS (voice am_adam ~1.10–1.15×) |
| soundfile / numpy | 0.14.0 / 2.3.1 | Audio + alignment |
| ffmpeg | n9.0.1 | Mux, kompresi, contact sheet (ingat: tanpa `-vsync`, pakai `-update 1`) |
| Python 3.13 + Pillow | 3.13 / 11.3.0 | `scripts/generate_thumbnail.py` (thumbnail kanonik 1080p) |
| yt-dlp | 2026.06.09 | Riset / unduh referensi |
| Wikimedia Commons API | — | Sumber aset PD/CC0 (`iiurlwidth=1920`) |
| `vision_analyze` (Hermes) | — | **Quality gate visual wajib** Fase 4 |

---

## 4b. Opsi engine kedua: HyperFrames (dipertimbangkan, bukan dipaksakan)

**Status:** terpasang hari ini (21 skill di `~/.hermes/skills/`), v0.8.145, dan **sudah diverifikasi render di mesin ini** — `init` → `check` (0 error, kontras WCAG AA lolos) → `render` menghasilkan MP4 1920×1080/30fps/10s yang valid. Chrome headless dibundel sendiri (`~/.cache/hyperframes/chrome/`), jadi tidak bergantung pada Chrome sistem.

**Di mana ia membantu, dan di mana TIDAK:**

| Kebutuhan | Engine | Alasan |
|---|---|---|
| Format B (Archival Micro-Doc) | **Remotion (tetap)** | `ArchivalDocRun.tsx` sudah jadi & sudah lolos QA frame. Rewrite ke HyperFrames = biaya tanpa manfaat. |
| Format A (Hidden-Detail, Ken Burns + callout teks) | **HyperFrames cocok** | Kekuatannya justru komposisi HTML/CSS + animasi seekable + lint/check otomatis (WCAG, layout, runtime). Lebih cepat diiterasi daripada bikin komponen Remotion baru. |
| Format C (Ranked/Data-Viz) | **HyperFrames cocok** | Cocok untuk overlay HTML angka/bar; lint+`check --snapshots` memberi gate visual per frame. |
| Mind Map kanonik M9 (RoughJS + Patrick Hand) | **Remotion (jangan diubah)** | Sudah standar kanonik `@IRinANutshell`. |

**Keputusan yang saya usulkan:** HyperFrames = engine **eksperimental** untuk Format A/C saja, di direktori terpisah (`learning-videos/shorts-experiments/<slug>-hf/`), **tanpa menyentuh** `simulation/ir-motion-library`. Remotion tetap kanonik.

**Skill HyperFrames yang relevan** (kalau opsi ini diambil): `hyperframes` (router) · `hyperframes-core` (kontrak komposisi HTML) · `hyperframes-cli` (init/lint/check/preview/render) · `hyperframes-keyframes` (wajib dibaca sebelum bikin zoom/Ken Burns) · `hyperframes-audio` (ducking narasi) · `embedded-captions` (subtitle burned-in) · `media-use` (aset/gambar/suara).

**Catatan jujur:** jalur render HyperFrames di Windows sempat gagal karena Chrome sistem tidak terbaca CLI — teratasi dengan `npx hyperframes browser ensure --force` (unduh headless shell). Kalau opsi ini dipakai, langkah itu masuk prasyarat.

---

## 5. Skills yang dipakai

| Skill | Peran |
|---|---|
| **`ir-video-director`** | Standar kanonik produksi `@IRinANutshell` (5 fase, kamera, audio hygiene, lokasi berkas) |
| **`viral-history-shorts`** | Standar Format B: 4-layer archival layout, anti-template rules, safe-zone, QA gate |
| **`animated-mapping-shorts`** | Dipakai **hanya** untuk elemen locator/garis peta Format C, bukan klaim wilayah |
| `remotion-best-practices` / `remotion-render` / `remotion-captions` | Router best-practice render, caption, dan ekspor |
| `remotion-video` | Pola Remotion+React+TTS |
| `hermes-agent` | Orkestrasi & konfigurasi |

---

## 6. Model eksekusi (sesuai pipeline M10 & SHORTS_PLAN_V3)

- **Director (audit & gerbang):** GLM 5.3 — mengaudit commit builder, menjalankan ulang semua gate verifikasi, menyajikan verdict + bukti.
- **Builder:** `ag/gemini-3.8-flash-high` via 9router (streaming OK per audit terakhir). Fallback `ag/gemini-3.8-flash`.
- **QA visual:** `vision_analyze` Hermes (independen dari kuota Antigravity).
- **Pengguna memegang ACC** di setiap gerbang; tidak ada Fase 2 sebelum ACC #1.

---

## 6b. Keputusan pengguna (2026-10-10) — mengikat untuk SH-01

Keputusan ini diambil lewat gerbang ACC #1 dan mengikat untuk SH-01. Format A/B/C dan urutan SH-01→SH-03→SH-02 tidak berubah.

| Item | Keputusan |
|---|---|
| Hook Beat 1 | **Hook tipe B (stakes pengepungan)** — *"Thirty-nine men held a three-kilometre island against an empire for 1,540 days — for a spice the world could get nowhere else."* Hook = curiosity gap yang baru dibayar di Beat 6. |
| Restrukturisasi akibat hook B | Hook B membocorkan isi Beat 3. Busur baru: **B1 hook = foreshadow (tanpa menyebut Breda/"traded"/"Manhattan")** → **B2 reveal (pulau + eksklusivitas pala)** → **B3 detail pengepungan (foreshadow diperdalam, bukan diulang)** → **B4 reveal dokumen (Breda + *uti possidetis*)** → **B5 payoff (siapa pegang apa)** → **B6 resolusi hook (kontras hari ini)**. "Manhattan" pertama kali muncul di B4, bukan B1. |
| Beat 2 | Klaim dilunakkan persis mengikuti sumber: *"the world's only source of nutmeg and mace"* (bukan "only place on Earth where nutmeg grew"). |
| Headline Beat 2 | `PULAU RUN: 3 KM OF GOLD` → **dicopot** (kata "gold" hanya metafora). Ganti headline baru. |
| Target durasi | Naik ke **~45–48 dtk** (hook + restrukturisasi menambah kata). Masih dalam rentang sehat Shorts 45–60 dtk dari riset; target lama 40–45 dtk dibatalkan. |
| Voice Fase 2 | **ElevenLabs API** (key sudah ada di `~/.hermes/.env`), bukan Kokoro. |
| Engine Fase 3 | **HyperFrames** di folder terpisah `sh-01-pulau-run-hf/`, bukan reuse Remotion `ArchivalDocRun.tsx`. Remotion tetap kanonik untuk M9. |

**Konsekuensi baru yang wajib diaudit di revisi:**
1. Narasi tidak boleh menyebut "Manhattan", "traded", atau "gave away" sebelum Beat 4.
2. Beat 3 tidak boleh mengulang kalimat hook — ia menambah detail (Courthope 1616, nama, konteks), bukan mengulang "39 men / 1,540 days".
3. Beat 1 butuh headline baru yang tidak sama dengan teks hook.
4. Semua headline/chip/subtitle di storyboard harus diperbarui konsisten dengan narasi baru.

---

## 7. Gerbang ACC — yang saya minta dari Anda

1. Setuju **Format A / B / C** ini sebagai tiga format yang dikejar? (atau mau ganti salah satu?)
2. Setuju **urutan produksi** SH-01 → SH-03 → SH-02?
3. **Goal channel**: konten pendamping kurikulum IR (`@IRinANutshell`), atau eksperimen Shorts mandiri?
4. Kalau setuju → saya tulis **storyboard beat-by-beat + naskah EN lengkap untuk SH-01**, lalu **BERHENTI lagi** untuk ACC #1 (sesuai Mandatory Review Gate HERMES.md).

> Catatan: dokumen ini belum meng-commit apa pun. `learning-videos/shorts-experiments/` masih untracked; commit dilakukan setelah Anda ACC (Step 5 Linear Loop).
