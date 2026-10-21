const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const projectDir = __dirname;
const qaDir = path.join(projectDir, "qa_v2");
if (!fs.existsSync(qaDir)) fs.mkdirSync(qaDir, { recursive: true });

const TARGET = process.argv[2] || "index_v2.html";

async function captureStills() {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  page.on("console", m => console.log("  [page]", m.text()));
  page.on("pageerror", e => console.log("  [PAGE ERROR]", e.message));

  const fileUrl = "file:///" + path.join(projectDir, TARGET).replace(/\\/g, "/");
  await page.goto(fileUrl, { waitUntil: "networkidle" });
  await page.waitForFunction(() => window.__ready === true, { timeout: 20000 });

  const times = [
    [2.0, "b1_funnel_wide"],
    [5.4, "b1_caliper"],
    [9.0, "b2_section_ship"],
    [15.0, "b3_counter"],
    [23.0, "b4_silicon"],
    [31.0, "b5_detour"],
    [38.5, "b6_endcard"]
  ];

  for (const [t, name] of times) {
    await page.evaluate((time) => {
      window.__timeline.seek(time, false);
      window.updateCaptionsAtTime(time);
    }, t);
    await page.waitForTimeout(120);
    const out = path.join(qaDir, `${name}.png`);
    await page.screenshot({ path: out });
    console.log(`t=${t}s -> ${out}`);
  }
  await browser.close();
}

captureStills().catch(e => { console.error(e); process.exit(1); });
