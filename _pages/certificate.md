---
layout: default
title: Academic Certificate of Mastery — IR Study Companion
permalink: /certificate.html
---

<div class="home-viewport" style="max-width: 1080px;">
  <header class="home-hero" style="margin-bottom: 2rem;">
    <div class="home-eyebrow">Academic Recognition &bull; Official Credential</div>
    <h1 class="home-title">Certificate of Academic Mastery</h1>
    <p class="home-description">
      Celebrate your scholarship. Generate, verify, and export your formal academic certificate upon completing curriculum tracks or achieving module mastery across our 18 core disciplines.
    </p>
  </header>

  <!-- Certificate Customizer Controls -->
  <div class="cert-controls-panel" style="background: var(--lms-surface); border: 1px solid var(--lms-border-strong); border-radius: var(--lms-radius-lg); padding: 1.75rem 2rem; margin-bottom: 2.5rem; box-shadow: var(--lms-shadow-sm);">
    <h3 style="margin: 0 0 1rem; font-size: 1.15rem; font-weight: 700; color: var(--lms-ink-primary);">
      Personalize Your Academic Certificate
    </h3>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.5rem;">
      <div>
        <label for="cert-student-name" style="display: block; font-size: 0.825rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--lms-ink-tertiary); margin-bottom: 0.4rem;">
          Recipient Full Name
        </label>
        <input type="text" id="cert-student-name" placeholder="Enter your full academic name..." value="Distinguished IR Scholar" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--lms-radius-md); border: 1px solid var(--lms-border-strong); background: var(--lms-subtle); color: var(--lms-ink-primary); font-size: 1rem; font-weight: 600;">
      </div>
      <div>
        <label for="cert-track-select" style="display: block; font-size: 0.825rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--lms-ink-tertiary); margin-bottom: 0.4rem;">
          Academic Specialization / Track
        </label>
        <select id="cert-track-select" style="width: 100%; padding: 0.75rem 1rem; border-radius: var(--lms-radius-md); border: 1px solid var(--lms-border-strong); background: var(--lms-subtle); color: var(--lms-ink-primary); font-size: 0.95rem; font-weight: 600;">
          <option value="Full Curriculum Master Diploma (All 18 Modules & 157 Lessons)">Full Curriculum Master Diploma (All 18 Modules & 157 Lessons)</option>
          <option value="Track 01: Foundations of Global Politics & IR Theories">Track 01: Foundations of Global Politics & IR Theories (42 Lessons)</option>
          <option value="Track 02: Security Studies, Warfare & Diplomacy">Track 02: Security Studies, Warfare & Diplomacy (42 Lessons)</option>
          <option value="Track 03: International Political Economy & Global Finance">Track 03: International Political Economy & Global Finance (31 Lessons)</option>
          <option value="Track 04: International Law, Regionalism & Indonesia">Track 04: International Law, Regionalism & Indonesia (42 Lessons)</option>
        </select>
      </div>
    </div>

    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
      <button class="sync-btn sync-btn-primary" id="btn-download-cert-png">
        <i class="fa fa-download" aria-hidden="true"></i> Download High-Res Certificate (.PNG)
      </button>
      <button class="sync-btn sync-btn-secondary" onclick="window.print();">
        <i class="fa fa-print" aria-hidden="true"></i> Print Official Diploma (PDF)
      </button>
    </div>
  </div>

  <!-- Elaborate Certificate Visual Display Frame -->
  <div class="cert-diploma-wrapper" id="cert-diploma-preview">
    <div class="cert-outer-border">
      <div class="cert-inner-border">
        <!-- Corner flourishes -->
        <div class="cert-corner corner-tl">&bull;</div>
        <div class="cert-corner corner-tr">&bull;</div>
        <div class="cert-corner corner-bl">&bull;</div>
        <div class="cert-corner corner-br">&bull;</div>

        <div class="cert-content-inner">
          <div class="cert-institution-header">
            <div class="cert-inst-crest">
              <i class="fa fa-university" aria-hidden="true"></i>
            </div>
            <div class="cert-inst-title">IR STUDY COMPANION ACADEMY</div>
            <div class="cert-inst-motto">VERITAS &bull; SCIENTIA &bull; JUSTITIA &bull; RIGOR</div>
          </div>

          <div class="cert-diploma-type">CERTIFICATE OF ACADEMIC MASTERY</div>
          <div class="cert-presented-text">This certifies that</div>

          <div class="cert-recipient-name" id="preview-student-name">
            Distinguished IR Scholar
          </div>

          <div class="cert-body-prose">
            has demonstrated distinguished theoretical competence, empirical rigor, and comprehensive mastery across the accredited curriculum of
          </div>

          <div class="cert-awarded-track" id="preview-track-title">
            Full Curriculum Master Diploma (All 18 Modules & 157 Lessons)
          </div>

          <div class="cert-seal-signature-row">
            <div class="cert-sig-block">
              <div class="cert-sig-line">
                <span class="cert-sig-handwriting">Cantikaputri F.</span>
              </div>
              <div class="cert-sig-title">Curriculum Director & Academic Author</div>
              <div class="cert-sig-sub">IR Study Companion Platform</div>
            </div>

            <div class="cert-gold-seal">
              <div class="cert-seal-circle">
                <div class="cert-seal-star">&starf; &starf; &starf;</div>
                <div class="cert-seal-text">OFFICIAL<br>ACADEMIC<br>MASTERY</div>
                <div class="cert-seal-year">2026</div>
              </div>
            </div>

            <div class="cert-sig-block">
              <div class="cert-sig-line">
                <span class="cert-sig-handwriting">Academic Board</span>
              </div>
              <div class="cert-sig-title">Board of Pedagogical Review</div>
              <div class="cert-sig-sub">Open Educational Resources Initiative</div>
            </div>
          </div>

          <div class="cert-footer-meta">
            <div><strong>Issue Date:</strong> <span id="cert-issue-date">October 5, 2026</span></div>
            <div><strong>Credential Hash:</strong> <code id="cert-hash-val">SHA256: 8F2A-E4B9-C012-77D4</code></div>
            <div><strong>Verification:</strong> ir-guide.netlify.app/certificate.html</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Offscreen High-Res Canvas for PNG Generation -->
  <canvas id="cert-canvas" width="1600" height="1130" style="display: none;"></canvas>
</div>

<style>
/* Elaborate Academic Diploma Styling */
.cert-diploma-wrapper {
  background: #fdfbf7;
  color: #1a1a1a;
  padding: 24px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12);
  border-radius: 8px;
  margin-bottom: 4rem;
  font-family: "Georgia", "Times New Roman", serif;
}

.cert-outer-border {
  border: 4px double #2b3a4a;
  padding: 16px;
  background: #fdfbf7;
}

.cert-inner-border {
  border: 1px solid #7a6843;
  padding: 3rem 2.5rem;
  position: relative;
  text-align: center;
}

.cert-corner {
  position: absolute;
  font-size: 1.5rem;
  color: #7a6843;
  line-height: 1;
}
.corner-tl { top: 6px; left: 10px; }
.corner-tr { top: 6px; right: 10px; }
.corner-bl { bottom: 6px; left: 10px; }
.corner-br { bottom: 6px; right: 10px; }

.cert-institution-header {
  margin-bottom: 1.5rem;
}
.cert-inst-crest {
  font-size: 2.2rem;
  color: #2b3a4a;
  margin-bottom: 0.25rem;
}
.cert-inst-title {
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  color: #2b3a4a;
}
.cert-inst-motto {
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.25em;
  color: #7a6843;
  margin-top: 0.35rem;
}

.cert-diploma-type {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #111111;
  margin: 1.5rem 0 0.5rem;
  text-transform: uppercase;
}
.cert-presented-text {
  font-size: 0.95rem;
  font-style: italic;
  color: #555555;
  margin-bottom: 1.25rem;
}

.cert-recipient-name {
  font-size: 2.4rem;
  font-weight: 700;
  color: #1a2736;
  border-bottom: 2px solid #7a6843;
  display: inline-block;
  padding: 0 2rem 0.4rem;
  margin-bottom: 1.5rem;
  min-width: 320px;
}

.cert-body-prose {
  font-size: 1.05rem;
  line-height: 1.6;
  color: #444444;
  max-width: 680px;
  margin: 0 auto 1.25rem;
}

.cert-awarded-track {
  font-size: 1.35rem;
  font-weight: 700;
  color: #2b3a4a;
  margin-bottom: 3rem;
}

.cert-seal-signature-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 2.5rem;
  padding: 0 1rem;
}

.cert-sig-block {
  text-align: center;
  flex: 1;
  max-width: 240px;
}
.cert-sig-line {
  border-bottom: 1px solid #333333;
  padding-bottom: 0.4rem;
  margin-bottom: 0.5rem;
}
.cert-sig-handwriting {
  font-family: "Brush Script MT", "Caveat", "Segoe Script", cursive;
  font-size: 1.6rem;
  color: #1a2736;
}
.cert-sig-title {
  font-size: 0.85rem;
  font-weight: 700;
  color: #222222;
}
.cert-sig-sub {
  font-size: 0.725rem;
  color: #666666;
}

.cert-gold-seal {
  width: 110px;
  height: 110px;
  border-radius: 50%;
  background: radial-gradient(circle, #e6c875 0%, #be9b42 70%, #8c6e26 100%);
  padding: 4px;
  box-shadow: 0 4px 12px rgba(140, 110, 38, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 1.5rem;
}
.cert-seal-circle {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 2px dashed #4a3811;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: #382705;
}
.cert-seal-star {
  font-size: 0.65rem;
  line-height: 1;
  margin-bottom: 0.15rem;
}
.cert-seal-text {
  font-size: 0.625rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  line-height: 1.25;
}
.cert-seal-year {
  font-size: 0.7rem;
  font-weight: 700;
  margin-top: 0.2rem;
}

.cert-footer-meta {
  border-top: 1px solid #d5cbba;
  padding-top: 1rem;
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: #777777;
  font-family: system-ui, -apple-system, sans-serif;
}

@media (max-width: 768px) {
  .cert-seal-signature-row {
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }
  .cert-recipient-name {
    font-size: 1.75rem;
  }
  .cert-diploma-type {
    font-size: 1.5rem;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const nameInput = document.getElementById('cert-student-name');
    const trackSelect = document.getElementById('cert-track-select');
    const namePreview = document.getElementById('preview-student-name');
    const trackPreview = document.getElementById('preview-track-title');
    const dateEl = document.getElementById('cert-issue-date');
    const hashEl = document.getElementById('cert-hash-val');
    const downloadBtn = document.getElementById('btn-download-cert-png');

    // Set today's date
    const today = new Date();
    const dateFormatted = today.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
    if (dateEl) dateEl.textContent = dateFormatted;

    function generateHash(str) {
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
            hash = ((hash << 5) - hash) + str.charCodeAt(i);
            hash |= 0;
        }
        const hex = Math.abs(hash).toString(16).toUpperCase().padStart(8, '0');
        return 'SHA256: ' + hex.slice(0, 4) + '-' + hex.slice(4, 8) + '-IRACAD-2026';
    }

    function updatePreview() {
        const name = nameInput.value.trim() || 'Distinguished IR Scholar';
        const track = trackSelect.value;
        if (namePreview) namePreview.textContent = name;
        if (trackPreview) trackPreview.textContent = track;
        if (hashEl) hashEl.textContent = generateHash(name + '|' + track + '|' + dateFormatted);
    }

    if (nameInput) nameInput.addEventListener('input', updatePreview);
    if (trackSelect) trackSelect.addEventListener('change', updatePreview);
    updatePreview();

    // Canvas PNG Generator
    if (downloadBtn) {
        downloadBtn.addEventListener('click', () => {
            const canvas = document.getElementById('cert-canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;

            // Background paper
            ctx.fillStyle = "#fdfbf7";
            ctx.fillRect(0, 0, w, h);

            // Double outer border
            ctx.strokeStyle = "#2b3a4a";
            ctx.lineWidth = 8;
            ctx.strokeRect(30, 30, w - 60, h - 60);

            ctx.lineWidth = 2;
            ctx.strokeRect(42, 42, w - 84, h - 84);

            // Inner gold border
            ctx.strokeStyle = "#7a6843";
            ctx.lineWidth = 3;
            ctx.strokeRect(60, 60, w - 120, h - 120);

            // Institution Header
            ctx.fillStyle = "#2b3a4a";
            ctx.textAlign = "center";
            ctx.font = "bold 32px Georgia, serif";
            ctx.fillText("IR STUDY COMPANION ACADEMY", w / 2, 140);

            ctx.fillStyle = "#7a6843";
            ctx.font = "bold 16px sans-serif";
            ctx.fillText("VERITAS • SCIENTIA • JUSTITIA • RIGOR", w / 2, 175);

            // Title
            ctx.fillStyle = "#111111";
            ctx.font = "bold 44px Georgia, serif";
            ctx.fillText("CERTIFICATE OF ACADEMIC MASTERY", w / 2, 260);

            ctx.fillStyle = "#666666";
            ctx.font = "italic 22px Georgia, serif";
            ctx.fillText("This certifies that", w / 2, 315);

            // Student Name
            const name = nameInput.value.trim() || 'Distinguished IR Scholar';
            ctx.fillStyle = "#1a2736";
            ctx.font = "bold 52px Georgia, serif";
            ctx.fillText(name, w / 2, 400);

            // Underline
            ctx.strokeStyle = "#7a6843";
            ctx.lineWidth = 2;
            ctx.beginPath();
            const textWidth = ctx.measureText(name).width;
            ctx.moveTo((w / 2) - (textWidth / 2) - 40, 420);
            ctx.lineTo((w / 2) + (textWidth / 2) + 40, 420);
            ctx.stroke();

            // Prose
            ctx.fillStyle = "#444444";
            ctx.font = "24px Georgia, serif";
            ctx.fillText("has demonstrated distinguished theoretical competence, empirical rigor, and", w / 2, 480);
            ctx.fillText("comprehensive mastery across the accredited curriculum of", w / 2, 515);

            // Awarded Track
            const track = trackSelect.value;
            ctx.fillStyle = "#2b3a4a";
            ctx.font = "bold 34px Georgia, serif";
            ctx.fillText(track, w / 2, 590);

            // Signatures
            const sigY = 880;
            // Left Sig
            ctx.strokeStyle = "#333333";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(220, sigY);
            ctx.lineTo(500, sigY);
            ctx.stroke();

            ctx.font = "italic 36px 'Brush Script MT', cursive";
            ctx.fillStyle = "#1a2736";
            ctx.fillText("Cantikaputri F.", 360, sigY - 15);

            ctx.font = "bold 18px Georgia, serif";
            ctx.fillStyle = "#222222";
            ctx.fillText("Curriculum Director & Author", 360, sigY + 30);
            ctx.font = "14px sans-serif";
            ctx.fillStyle = "#666666";
            ctx.fillText("IR Study Companion Platform", 360, sigY + 52);

            // Center Gold Seal
            const sealX = w / 2;
            const sealY = sigY - 20;
            ctx.save();
            ctx.beginPath();
            ctx.arc(sealX, sealY, 80, 0, Math.PI * 2);
            ctx.fillStyle = "#c5a046";
            ctx.fill();
            ctx.strokeStyle = "#5a4312";
            ctx.lineWidth = 3;
            ctx.setLineDash([6, 4]);
            ctx.stroke();
            ctx.restore();

            ctx.fillStyle = "#382705";
            ctx.font = "bold 18px sans-serif";
            ctx.fillText("★ ★ ★", sealX, sealY - 30);
            ctx.font = "bold 16px Georgia, serif";
            ctx.fillText("OFFICIAL", sealX, sealY - 10);
            ctx.fillText("ACADEMIC", sealX, sealY + 12);
            ctx.fillText("MASTERY", sealX, sealY + 34);
            ctx.font = "bold 14px sans-serif";
            ctx.fillText("2026", sealX, sealY + 54);

            // Right Sig
            ctx.strokeStyle = "#333333";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(w - 500, sigY);
            ctx.lineTo(w - 220, sigY);
            ctx.stroke();

            ctx.font = "italic 36px 'Brush Script MT', cursive";
            ctx.fillStyle = "#1a2736";
            ctx.fillText("Academic Board", w - 360, sigY - 15);

            ctx.font = "bold 18px Georgia, serif";
            ctx.fillStyle = "#222222";
            ctx.fillText("Board of Pedagogical Review", w - 360, sigY + 30);
            ctx.font = "14px sans-serif";
            ctx.fillStyle = "#666666";
            ctx.fillText("Open Educational Resources", w - 360, sigY + 52);

            // Footer metadata
            ctx.strokeStyle = "#d5cbba";
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(100, 1020);
            ctx.lineTo(w - 100, 1020);
            ctx.stroke();

            ctx.font = "14px monospace";
            ctx.fillStyle = "#666666";
            ctx.textAlign = "left";
            ctx.fillText("Issued: " + dateFormatted, 100, 1055);
            ctx.textAlign = "center";
            ctx.fillText(hashEl.textContent, w / 2, 1055);
            ctx.textAlign = "right";
            ctx.fillText("Verify: ir-guide.netlify.app/certificate.html", w - 100, 1055);

            // Trigger file download
            const imageURL = canvas.toDataURL("image/png");
            const dlLink = document.createElement('a');
            const cleanName = name.toLowerCase().replace(/[^a-z0-9]/g, '-');
            dlLink.download = `ir-certificate-${cleanName}.png`;
            dlLink.href = imageURL;
            document.body.appendChild(dlLink);
            dlLink.click();
            document.body.removeChild(dlLink);
        });
    }
});
</script>
