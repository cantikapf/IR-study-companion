const { chromium } = require("playwright");
const fs = require("fs");

async function generateComparison() {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: ["--no-sandbox", "--disable-gpu", "--allow-file-access-from-files"]
  });

  const baseHtmlPath = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html";
  const rawHtml = fs.readFileSync(baseHtmlPath, "utf-8");

  // === OPTION 3: PURE 3D FULL-BLEED (No card at all) ===
  const htmlOpt3 = rawHtml.replace(
    `<div id="card-dimension">`,
    `<div id="card-dimension" style="display: none !important;">`
  );
  fs.writeFileSync("D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/test_opt3.html", htmlOpt3);

  // === OPTION 1: MINIMALIST LEADER-LINE CALLOUTS (Architectural / Vox Clean) ===
  const leaderLineCss = `
    #card-dimension { display: none !important; }
    .leader-line-container {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 35;
    }
    .leader-tag {
      position: absolute;
      background: rgba(10, 15, 25, 0.85);
      border: 1.5px solid #fbbf24;
      border-radius: 8px;
      padding: 8px 18px;
      color: #ffffff;
      font-family: 'Space Mono', monospace;
      font-size: 22px;
      font-weight: 800;
      letter-spacing: 1.5px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.8);
    }
    .leader-tag::before {
      content: '';
      width: 8px;
      height: 8px;
      background: #fbbf24;
      border-radius: 50%;
    }
  `;
  const leaderLineHtml = `
    <div class="leader-line-container">
      <!-- Tag 1: Upper Tier Scaffolding -->
      <div class="leader-tag" style="top: 360px; right: 80px;">
        <span>2 NARROW TIERS</span>
      </div>
      <svg style="position: absolute; inset: 0; width: 1080px; height: 1920px; pointer-events: none;">
        <line x1="880" y1="380" x2="680" y2="440" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6,4" />
        <circle cx="680" cy="440" r="5" fill="#fbbf24" />
      </svg>

      <!-- Tag 2: Lower Tier Hoplite Capacity -->
      <div class="leader-tag" style="top: 680px; left: 80px;">
        <span>30 GREEK WARRIORS</span>
      </div>
      <svg style="position: absolute; inset: 0; width: 1080px; height: 1920px; pointer-events: none;">
        <line x1="280" y1="700" x2="480" y2="760" stroke="#fbbf24" stroke-width="2.5" stroke-dasharray="6,4" />
        <circle cx="480" cy="760" r="5" fill="#fbbf24" />
      </svg>
    </div>
  `;
  const htmlOpt1 = rawHtml
    .replace(`</style>`, `${leaderLineCss}</style>`)
    .replace(`<div id="layer-c">`, `<div id="layer-c">${leaderLineHtml}`)
    .replace(`<div id="card-dimension">`, `<div id="card-dimension" style="display: none !important;">`);
  fs.writeFileSync("D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/test_opt1.html", htmlOpt1);

  // === OPTION 2: ANCIENT BRONZE TABLET PLAQUE ===
  const bronzeCss = `
    #card-dimension {
      position: absolute;
      top: 140px;
      left: 140px;
      width: 800px;
      background: linear-gradient(145deg, #2b1f14 0%, #17110b 100%);
      border: 3px solid #d97706;
      border-radius: 12px;
      padding: 20px 32px;
      box-shadow: 0 16px 36px rgba(0,0,0,0.9), inset 0 0 20px rgba(217, 119, 6, 0.2);
      display: block !important;
      opacity: 1 !important;
      z-index: 25;
    }
    .bronze-title {
      font-size: 20px;
      font-weight: 800;
      color: #fbbf24;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      border-bottom: 1.5px solid rgba(251, 191, 36, 0.3);
      padding-bottom: 8px;
      margin-bottom: 12px;
      text-align: center;
    }
    .spec-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }
    .spec-label {
      font-size: 20px;
      font-weight: 700;
      color: #d1d5db;
      letter-spacing: 1px;
    }
    .spec-val-cyan {
      font-size: 28px;
      font-weight: 800;
      color: #fde68a;
    }
    .spec-val-yellow {
      font-size: 28px;
      font-weight: 800;
      color: #f59e0b;
    }
  `;
  const bronzeHtml = `
    <div id="card-dimension">
      <div class="bronze-title">⚔️ ANCIENT GREEK NAVAL ENGINEERING ⚔️</div>
      <div class="spec-row">
        <span class="spec-label">HULL TIMBER</span>
        <span class="spec-val-cyan">18 CM PINE</span>
      </div>
      <div class="spec-row">
        <span class="spec-label">INTERIOR COMPARTMENT</span>
        <span class="spec-val-yellow">2 NARROW TIERS</span>
      </div>
      <div class="spec-row" style="margin-bottom:0;">
        <span class="spec-label">CREW CAPACITY</span>
        <span class="spec-val-cyan">30 WARRIORS</span>
      </div>
    </div>
  `;
  const htmlOpt2 = rawHtml
    .replace(`</style>`, `${bronzeCss}</style>`)
    .replace(/<div id="card-dimension">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/, bronzeHtml);
  fs.writeFileSync("D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/test_opt2.html", htmlOpt2);

  // Capture all 3 options at t=10.0s
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });

  // Option 1
  await page.goto("file:///D:/PERSONAL%20PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/test_opt1.html", { waitUntil: "networkidle" });
  await page.evaluate(() => { window.masterTl.pause(); window.masterTl.time(10.0); });
  await page.waitForTimeout(400);
  await page.screenshot({ path: "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/preview_stills/compare_opt1_leaderlines.png" });
  console.log("Captured compare_opt1_leaderlines.png");

  // Option 2
  await page.goto("file:///D:/PERSONAL%20PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/test_opt2.html", { waitUntil: "networkidle" });
  await page.evaluate(() => { window.masterTl.pause(); window.masterTl.time(10.0); });
  await page.waitForTimeout(400);
  await page.screenshot({ path: "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/compare_opt2_bronzetablet.png" });
  console.log("Captured compare_opt2_bronzetablet.png");

  // Option 3
  await page.goto("file:///D:/PERSONAL%20PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/test_opt3.html", { waitUntil: "networkidle" });
  await page.evaluate(() => { window.masterTl.pause(); window.masterTl.time(10.0); });
  await page.waitForTimeout(400);
  await page.screenshot({ path: "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/compare_opt3_pure3d.png" });
  console.log("Captured compare_opt3_pure3d.png");

  await browser.close();
  console.log("All comparison options captured!");
}

generateComparison();
