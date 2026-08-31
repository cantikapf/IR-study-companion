---
name: ir-video-director
description: Mentransformasikan materi kuliah Hubungan Internasional (_chapters/) menjadi naskah video faceless dan paket prompt animasi stickman v4.3 monokrom (Seedance / Kling) 100% gratis.
---

# IR Video Director Skill

Gunakan skill ini ketika pengguna ingin membuat video pembelajaran animasi faceless (misal: gaya stickman YouTube atau penjelasan konsep) untuk bab materi di IR Study Companion.

## Arsitektur & Aturan Gaya

1. **Format Visual (Stickman DNA)**:
   - Garis putih minimalis tebal ~3px pada latar hitam pekat #000000.
   - Kepala lingkaran sempurna, mata titik kembar, mulut garis datar.
   - Variasi busana line-art: *Diplomat* (dasi), *Statesman* (jas), *Theorist* (lab coat), atau *Plain* (polos).
   - Props digambar dalam gaya line-art yang sama (peta dunia garis, bendera, perisai, neraca kekuatan).

2. **Writing DNA (Naskah Edukasi)**:
   - Durasi default 60s (~140-150 kata) atau 90s (~230 kata).
   - **Cold Open**: Pertanyaan reflektif atau skenario dilematis yang menempatkan audiens di posisi pembuat keputusan.
   - **Reframe**: Mematahkan asumsi umum (misal: 'Kebanyakan orang mengira perang terjadi karena kebencian. Faktanya, sering kali karena rasa takut.').
   - **Core Concept**: 1 model atau konsep kunci Hubungan Internasional (misal: Balance of Power, Anarki, Two-Level Games).
   - **Motivational / Intellectual Landing**: Refleksi tentang bagaimana konsep ini membentuk cara kita memahami dunia hari ini.

3. **Format Prompt Animasi (Silent Visuals v4.3)**:
   - Setiap klip berdurasi ~14 detik (5-7 micro-beats).
   - **JANGAN** masukkan teks naskah ke dalam prompt video generator AI (agar tidak terjadi distorsi teks di layar).
   - Selalu sertakan:
     - CHARACTER LOCK
     - STYLE ANCHOR
     - ENVIRONMENT LOCK
     - Micro-beats dengan durasi jelas (misal: [00:00–00:03] WIDE - ...)
     - NEGATIVE PROMPT
     - HANDOFF (Match-cut)

4. **Integrasi Voiceover & Stitching**:
   - Voiceover dihasilkan gratis via dge-tts (suara id-ID-ArdiNeural atau id-ID-GadisNeural).
   - Video dirangkai secara otomatis via Diffusion Studio CLI atau script Python FFmpeg.
