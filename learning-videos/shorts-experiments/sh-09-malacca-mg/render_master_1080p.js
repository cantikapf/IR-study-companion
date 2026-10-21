const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const { execSync } = require("child_process");

const FPS = 30, DUR = 45;
const W = 1080, H = 1920;
const OUT_FRAMES = path.join(__dirname, "snapshots", "master_frames");
const OUT_VIDEO = path.join(__dirname, "renders", "sh09_malacca_master_1080p.mp4");
const AUDIO_FILE = path.join(__dirname, "audio", "vo_full.wav");

(async () => {
  fs.mkdirSync(path.join(__dirname, "renders"), { recursive: true });
  // fs.rmSync(OUT_FRAMES, { recursive: true, force: true });
  fs.mkdirSync(OUT_FRAMES, { recursive: true });

  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: ["--no-sandbox", "--disable-gpu", "--force-device-scale-factor=1"]
  });
  const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
  const fileUrl = "file:///" + path.join(__dirname, "compositions", "index.html").split(path.sep).join("/");
  await page.goto(fileUrl, { waitUntil: "networkidle", timeout: 30000 });
  await page.waitForFunction(() => window.__ready === true, { timeout: 20000 });

  await page.waitForTimeout(250);

  const total = Math.round(FPS * DUR);
  console.log(`Starting master 1080p extraction: ${total} frames...`);
  for (let f = 0; f < total; f++) {
    const framePath = path.join(OUT_FRAMES, `f${String(f).padStart(5, "0")}.png`);
    if (fs.existsSync(framePath) && fs.statSync(framePath).size > 1000) {
      continue;
    }
    const t = f / FPS;
    await page.evaluate(tt => {
      window.__timeline.seek(tt, false);
      window.__timeline.pause();
      if (window.syncLabels) window.syncLabels(window.cam ? window.cam.t : 1, window.cam ? window.cam.x : 0, window.cam ? window.cam.y : 0);
      if (window.updateCaptions) window.updateCaptions(tt);
    }, t);
    await page.screenshot({ path: framePath });
    if (f % 150 === 0) console.log(`Master frame ${f}/${total} (${t.toFixed(1)}s)`);
  }
  await browser.close();

  console.log("Encoding master 1080p with audio...");
  const cmd = `ffmpeg -y -v error -framerate ${FPS} -i "${path.join(OUT_FRAMES, "f%05d.png")}" -i "${AUDIO_FILE}" -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 256k -movflags +faststart "${OUT_VIDEO}"`;
  execSync(cmd, { stdio: "pipe" });
  console.log("MASTER_1080P_DONE: " + OUT_VIDEO);
  process.exit(0);
})().catch(e => { console.error("FATAL_ERROR", e); process.exit(1); });
