// Low-res moving preview: 30fps, 540x960, frames stepped from the paused timeline.
// Not the final render — proof of motion only.
const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

const FPS = 30, DUR = 45;
const OUT = path.join(__dirname, "snapshots", "preview_frames");
const W = 540, H = 960;

(async () => {
  fs.rmSync(OUT, { recursive: true, force: true });
  fs.mkdirSync(OUT, { recursive: true });

  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: ["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"]
  });
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  await page.goto("file:///" + path.join(__dirname, "compositions", "index.html").replace(/\\/g, "/"),
    { waitUntil: "networkidle", timeout: 30000 });
  await page.waitForFunction(() => window.__ready === true, { timeout: 20000 });

  // scale the 1080x1920 stage down to fit the small viewport
  await page.addStyleTag({ content: `
    html,body{width:${W}px!important;height:${H}px!important;overflow:hidden!important;}
    #stage{transform:scale(${W / 1080});transform-origin:top left;}
  ` });
  await page.waitForTimeout(250);

  const total = Math.round(FPS * DUR);
  for (let f = 0; f < total; f++) {
    const t = f / FPS;
    await page.evaluate(tt => { window.__timeline.seek(tt, false); window.__timeline.pause(); }, t);
    await page.screenshot({ path: path.join(OUT, `f${String(f).padStart(5, "0")}.png`) });
    if (f % 300 === 0) console.log(`${f}/${total} (${t.toFixed(1)}s)`);
  }
  console.log("frames:", total);
  await browser.close();
})().catch(e => { console.error("FAIL", e.message); process.exit(1); });
