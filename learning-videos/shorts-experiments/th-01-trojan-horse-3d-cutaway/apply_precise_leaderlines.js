const { chromium } = require("playwright");
const fs = require("fs");

async function renderPreciseLeaderLines() {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: ["--no-sandbox", "--disable-gpu", "--allow-file-access-from-files"]
  });

  const baseHtmlPath = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html";
  let html = fs.readFileSync(baseHtmlPath, "utf-8");

  // 1. Hide the old cyan #card-dimension
  // 2. Add precise blueprint leader lines
  const leaderLineCss = `
    #card-dimension { display: none !important; }

    .leader-container {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 35;
    }

    .callout-badge {
      position: absolute;
      background: rgba(10, 15, 26, 0.92);
      border: 2px solid #fbbf24;
      border-radius: 8px;
      padding: 10px 20px;
      color: #ffffff;
      font-family: 'Space Mono', monospace;
      font-size: 22px;
      font-weight: 800;
      letter-spacing: 1.5px;
      display: flex;
      align-items: center;
      gap: 10px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.85);
    }
    .callout-badge .dot {
      width: 10px;
      height: 10px;
      background: #fbbf24;
      border-radius: 50%;
      box-shadow: 0 0 8px #fbbf24;
    }
  `;

  // Tag 1 (Upper Scaffolding):
  // Tag on top right: X = 680 to 980 (width ~300), Y = 740.
  // Leader line starts at left of tag (x=680, y=760) -> elbows to (x=600, y=880) with gold dot at (600, 880) inside upper tier!
  
  // Tag 2 (30 Greek Hoplites):
  // Tag on left: X = 70 to 390 (width ~320), Y = 1040.
  // Leader line starts at right of tag (x=390, y=1060) -> points directly to (x=480, y=1100) with gold dot right on soldiers!
  const leaderLineHtml = `
    <div class="leader-container" id="precise-leaders">
      <!-- Tag 1: Upper Scaffolding Tier -->
      <div class="callout-badge" style="top: 730px; right: 70px;">
        <span class="dot"></span>
        <span>2 NARROW TIERS</span>
      </div>
      <svg style="position: absolute; inset: 0; width: 1080px; height: 1920px; pointer-events: none;">
        <!-- Polyline from tag to upper deck at (580, 880) -->
        <polyline points="730,755 630,755 580,880" fill="none" stroke="#fbbf24" stroke-width="2.5" />
        <circle cx="580" cy="880" r="5" fill="#fbbf24" />
        <circle cx="580" cy="880" r="10" fill="none" stroke="rgba(251, 191, 36, 0.4)" stroke-width="2" />
      </svg>

      <!-- Tag 2: 30 Greek Warriors -->
      <div class="callout-badge" style="top: 1040px; left: 70px;">
        <span class="dot"></span>
        <span>30 GREEK WARRIORS</span>
      </div>
      <svg style="position: absolute; inset: 0; width: 1080px; height: 1920px; pointer-events: none;">
        <!-- Polyline from tag to soldiers at (480, 1100) -->
        <polyline points="380,1065 430,1065 480,1100" fill="none" stroke="#fbbf24" stroke-width="2.5" />
        <circle cx="480" cy="1100" r="5" fill="#fbbf24" />
        <circle cx="480" cy="1100" r="10" fill="none" stroke="rgba(251, 191, 36, 0.4)" stroke-width="2" />
      </svg>
    </div>
  `;

  html = html
    .replace(`</style>`, `${leaderLineCss}</style>`)
    .replace(`<div id="layer-c">`, `<div id="layer-c">${leaderLineHtml}`)
    .replace(`<div id="card-dimension">`, `<div id="card-dimension" style="display: none !important;">`);

  fs.writeFileSync("D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html", html);

  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto("file:///D:/PERSONAL%20PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html", { waitUntil: "networkidle" });
  await page.evaluate(() => {
    window.masterTl.pause();
    window.masterTl.time(10.0);
  });
  await page.waitForTimeout(400);
  await page.screenshot({ path: "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/preview_stills/frame_10_0s_two_tier_cutaway.png" });
  console.log("Captured updated frame_10_0s_two_tier_cutaway.png with precise blueprint leader lines!");

  await browser.close();
}

renderPreciseLeaderLines();
