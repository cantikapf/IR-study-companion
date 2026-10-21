const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const projectDir = __dirname;
const qaDir = path.join(projectDir, "qa_stills");
if (!fs.existsSync(qaDir)) fs.mkdirSync(qaDir, { recursive: true });

async function captureStills() {
  console.log("Launching Chromium for QA still capture...");
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: ["--disable-gpu-vsync"]
  });

  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  const fileUrl = "file:///" + path.join(projectDir, "index.html").replace(/\\/g, "/");
  console.log("Loading:", fileUrl);
  await page.goto(fileUrl, { waitUntil: "networkidle" });

  await page.waitForFunction(() => window.__ready === true, { timeout: 15000 });
  console.log("Stage ready.");

  const checkTimes = [
    { t: 1.5, name: "frame_00_3d_globe_hook.png" },
    { t: 4.5, name: "frame_01_hook_caliper.png" },
    { t: 9.0, name: "frame_02_iso_ship_jam.png" },
    { t: 15.0, name: "frame_03_telemetry_ships.png" },
    { t: 22.0, name: "frame_04_exploded_chipset.png" },
    { t: 30.0, name: "frame_05_detour_bypass.png" },
    { t: 38.0, name: "frame_06_3d_globe_outro.png" }
  ];

  for (const item of checkTimes) {
    await page.evaluate((time) => {
      window.__timeline.seek(time, false);
      if (window.updateCaptionsAtTime) window.updateCaptionsAtTime(time);
    }, item.t);

    const outPath = path.join(qaDir, item.name);
    await page.screenshot({ path: outPath });
    console.log(`Captured still at t=${item.t}s -> ${outPath}`);
  }

  await browser.close();
  console.log("All QA stills captured successfully.");
}

captureStills().catch(err => {
  console.error("Error capturing stills:", err);
  process.exit(1);
});
