# Creative Brief — SH-08 Malacca Strait (v2 Replan)

Status: **DRAFT — menunggu ACC sebelum Fase 2 (script lock / audio / build)**
Engine: Vox-style tactical geopolitical vector map + 3D explanatory geometry (Kokoro-82M TTS, CDP deterministic frame render)
Format: 1080x1920, 30 FPS, target 48s

---

## 1. Eleven dimensions

| # | Dimension | Answer |
|---|---|---|
| 1 | Business goal | Penonton shorts paham **mengapa** chokepoint itu masalah struktural, bukan sekadar trivia lebar selat. Ukur: average view duration > 55% + komentar yang menyebut konsep (bottleneck/draft/detour), bukan angka acak. |
| 2 | Audience | Mahasiswa IR / penonton geopolitik yang sudah tahu "Malacca penting" tapi tidak tahu mekanismenya. Objeksi mereka: "kenapa tidak lewat selat lain saja?" |
| 3 | Core message (ONE) | **Geografi tidak bisa di-upgrade — satu jalur sempit dan dangkal memaksa seluruh jaringan dagang menaruh risikonya di titik yang sama.** |
| 4 | Tone | Analitis, tenang, presisi kartografi. **But not**: bukan alarmis, bukan clickbait konsumen, bukan dokumenter militermilded. |
| 5 | Mandatories | Header intel HUD, footer koordinat + rujukan bab, caption safe-zone bawah 380px, badge `HYPOTHETICAL SCENARIO` saat beat simulasi, English-only UI. |
| 6 | Deliverables | 1x 48s master 1080x1920 MP4 + burned captions + thumbnail 1080p (foto arsip asli, bukan still mindmap). |
| 7 | Distribution | YouTube Shorts `@IRinANutshell`. Spec: 9:16, <60s, safe-zone bawah. |
| 8 | References | SH-05 Cuban Crisis (map hierarchy + reticle), SH-06 Run Island (caption verbatim). Anti-reference: dashboard-telemetry style SH-08 v1 (angka tanpa sumber). |
| 9 | Timeline | ACC brief -> script lock -> TTS+audio -> still QA -> render -> thumbnail -> upload+sync. |
| 10 | Budget | N/A (in-house pipeline, Kokoro lokal, zero API cost). |
| 11 | Success metric | 30 hari: retention > 55%, dan tidak ada komentar koreksi fakta (indikator akurasi). |

Decision-maker: **Cantikaputri** (ACC per fase).

---

## 2. Claim audit — apa yang dibuang dari v1

| Klaim v1 | Status | Alasan |
|---|---|---|
| "Could you lose your phone if this strait closes?" | **BUANG** | Spekulatif, clickbait konsumen, bukan IR. |
| "60% of world maritime crude oil" | **BUANG** | Angka keliru; porsi transit minyak jauh lebih kecil. |
| "Critical semiconductors transit this exact choke" | **BUANG** | Chip bernilai tinggi mayoritas via **air freight**, bukan bulk container. |
| "Detour adds 3 full days & $5 billion surcharges" | **BUANG** | Estimasi presisi yang tidak punya sumber. |
| "Factory buffer < 72 hrs" | **BUANG** | Klaim blanket lintas sektor, tanpa dasar. |

**Prinsip pengganti**: pakai metrik fisik yang bisa diverifikasi (lebar kanal, draft limit, jarak tambahan), bukan estimasi rupiah/hari.

---

## 3. Fact gate — status verifikasi (diperiksa 2026-10-19)

| Fakta yang akan diucapkan | Nilai | Status | Dasar |
|---|---|---|---|
| Lebar minimum Phillips Channel / Singapore Strait | 1.5 NM / 2.8 km | **VERIFIED** | Konsisten di beberapa paper akademik + ECONSTOR working paper (Uni Bonn) |
| Kedalaman Selat Malaka & draft limit Malaccamax | selat ~25 m; Malaccamax draft 20.5 m (333 m x 60 m, 300k DWT) | **VERIFIED** | Wikipedia/Malaccamax (istilah arsitektur naval baku) |
| Sunda tidak bisa dilalui deep-draft | controlling depth turun sampai ~20 m; arus >5 knot | **VERIFIED** | geopol.uk chokepoint profile + MIMA (Maritime Institute of Malaysia) PDF: kapal >100.000 DWT tidak transit |
| Detour deep-draft lewat Lombok–Makassar | Lombok >150 m dalam; rute Lombok -> Dewakang Sill -> Makassar | **VERIFIED (rute)** | Wikipedia/Malaccamax daftar rute alternatif resmi |
| Angka tambahan jarak (NM) detour | bervariasi ~1.200-1.350 NM tergantung sumber sekunder | **TIDAK DIPAKAI** | Sumber sekunder saling berbeda; VO cukup sebut "rute memutar jauh ke timur", tanpa angka |
| Porsi perdagangan/minyak global lewat Malacca | angka bervariasi antar sumber | **TIDAK DIPAKAI** | Tidak ada sumber primer tunggal yang bisa dipertanggungjawabkan di layar |

Aturan: **kalau gate gagal, kalimat dibuang, bukan diperhalus.** VO tidak boleh berisi angka tanpa sumber.

---

## 4. Struktur 4 beat (explainer-video skill: problem -> stakes -> mechanism -> payoff)

### Beat 1 — The Funnel (0.0 – 10.0s)
- Visual: peta Indo-Pasifik penuh. Sorot Semenanjung Malaya + Sumatra, tarik garis koridor dari Samudra Hindia ke Laut China Selatan.
- Kamera: wide 1.0x -> dolly 1.35x ke koridor. Tanpa reticle dulu.
- VO: *"Two landmasses. Sumatra and the Malay Peninsula. Between them, one sea gate connecting the Indian Ocean to the South China Sea."*
- Job naratif: penonton lihat **tidak ada alternatif** — pilihan itu bukan sukarela.

### Beat 2 — The Pinch & The Draft (10.0 – 22.0s)
- Visual: zoom ke Phillips Channel 2.0x. Garis ukur 1.5 NM muncul di titik tersempit. Lalu **tilt halus** peta ke potongan 3D: permukaan laut, lambung kapal, dasar laut — garis draft 20.5 m.
- Kamera: hold stasioner selama kalimat draft diucapkan (v = 0).
- VO: *"At its narrowest, the Phillips Channel is one point five nautical miles wide. Deep enough for most ships -- but only just. Malaccamax: twenty point five metres of draft. Anything deeper goes around."*
- Catatan teknis: 3D di sini adalah **irisan penjelas (cross-section)**, bukan globe dekoratif dan bukan "parking lot" kapal.

### Beat 3 — Hypothetical Closure & Real Detours (22.0 – 36.0s)
- Visual: badge merah `HYPOTHETICAL SCENARIO` muncul top-center dan **bertahan** sampai beat habis. Dua panah bypass: Sunda (kapal lebih ringan) dan Lombok–Makassar (tanker bermuatan penuh). Masing-masing diberi label kelas kapal.
- Kamera: zoom-out 1.15x ke koridor Nusantara, lalu pan ke timur.
- VO: *"Now imagine the gate closes. Ships divert. Smaller ones through Sunda. Loaded tankers must run further east, through Lombok and Makassar -- thousands of extra nautical miles."*
- Job naratif: penonton paham **tidak ada detour gratis**, dan tidak semua kapal bisa lewat jalur yang sama.

### Beat 4 — Payoff (36.0 – 48.0s)
- Visual: pull-back ke teater Indo-Pasifik, jalur utama menyala, badge hipotetis hilang, endcard kanal.
- VO: *"You cannot widen a strait. That is the whole problem. Chokepoints do not create risk. They concentrate it."*
- Job naratif: satu takeaway yang bisa diulang penonton.

---

## 5. VO budget

| Beat | Kata | Durasi @2.3 w/s |
|---|---|---|
| 1 | ~20 | 8.7s |
| 2 | ~28 | 12.2s |
| 3 | ~27 | 11.7s |
| 4 | ~17 | 7.4s |
| **Total** | **~92** | **~40s + 8s breathing/hold = 48s** |

---

## 6. Yang TIDAK dilakukan

- Tidak ada dashboard telemetry counter (angka besar berputar) — itu yang bikin v1 terasa kosong.
- Tidak ada globe 3D dekoratif yang menutupi peta.
- Tidak render sebelum still QA lolos per beat.
- Tidak ada angka tanpa sumber di layar maupun di VO.

---

## 7. Gate

**ACC dibutuhkan sebelum:** menulis script final, sintesis TTS, build timeline, render.
