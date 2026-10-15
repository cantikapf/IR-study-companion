const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

(async () => {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  const fileUrl = "file:///" + path.resolve("index.html").replace(/\\/g, "/");
  await page.goto(fileUrl);
  await page.waitForTimeout(500);

  const outDir = path.resolve("qa_stills");
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const checkpoints = [
    { name: "01_beat1_harvard.jpg", time: 2.5 },
    { name: "02_beat2_thucydides.jpg", time: 11.0 },
    { name: "03_beat3_carrier.jpg", time: 21.0 },
    { name: "04_beat4_chokepoint.jpg", time: 29.5 },
    { name: "05_beat5_climax.jpg", time: 37.0 }
  ];

  for (const cp of checkpoints) {
    await page.evaluate(t => {
      masterTl.time(t);
    }, cp.time);
    const dest = path.join(outDir, cp.name);
    await page.screenshot({ path: dest, quality: 90, type: "jpeg" });
    console.log("Captured:", cp.name, "at", cp.time, "s");
  }

  await browser.close();
  console.log("All stills captured successfully!");
})();
