const { chromium } = require("playwright");
const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");

const projectDir = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway";
const exportsDir = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/exports";

const finalExportPath = path.join(exportsDir, "TH01_Trojan_Horse_3D_Cutaway_Short_1080p.mp4");
const localExportPath = path.join(projectDir, "TH01_Trojan_Horse_3D_Cutaway_Short_1080p.mp4");
const bgVideoPath = path.join(projectDir, "bg_smooth_master.mp4");
const audioPath = path.join(projectDir, "audio/final_soundtrack_master.wav");
const compositionOverlayUrl = "file:///" + path.join(projectDir, "composition_short_overlay.html").replace(/\\/g, "/");

const FPS = 30;
const DURATION_SEC = 25.73;
const TOTAL_FRAMES = Math.ceil(DURATION_SEC * FPS); // 772 frames
const WIDTH = 1080;
const HEIGHT = 1920;

async function renderShort26s() {
  console.log("========================================================");
  console.log("🎬 STARTING PUNCHY 26s SHORT COMPOSITING: TH-01 TROJAN HORSE");
  console.log(`Resolution: ${WIDTH}x${HEIGHT} | FPS: ${FPS} | Frames: ${TOTAL_FRAMES} | Duration: ${DURATION_SEC}s`);
  console.log("Background Video Stream:", bgVideoPath);
  console.log("Audio Soundtrack:", audioPath);
  console.log("Target MP4:", finalExportPath);
  console.log("========================================================");

  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: [
      "--no-sandbox",
      "--disable-gpu",
      "--disable-dev-shm-usage",
      "--allow-file-access-from-files"
    ]
  });

  const page = await browser.newPage({
    viewport: { width: WIDTH, height: HEIGHT },
    deviceScaleFactor: 1
  });

  await page.goto(compositionOverlayUrl, { waitUntil: "networkidle" });
  await page.waitForTimeout(400);

  // Initialize GSAP to pause
  await page.evaluate(() => {
    if (window.masterTl) {
      window.masterTl.pause();
      window.masterTl.time(0);
    }
  });

  const ffmpeg = spawn("ffmpeg", [
    "-y",
    "-i", bgVideoPath,                              // Input 0: 30fps smooth background video (25.73s)
    "-f", "image2pipe",
    "-vcodec", "png",
    "-r", String(FPS),
    "-i", "-",                                     // Input 1: Transparent PNG stream
    "-i", audioPath,                                // Input 2: Master audio (25.73s)
    "-filter_complex", "[0:v][1:v]overlay=0:0[v]", // Hardware/C-level transparent overlay
    "-map", "[v]",
    "-map", "2:a",
    "-c:v", "libx264",
    "-preset", "fast",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-r", String(FPS),
    "-c:a", "aac",
    "-b:a", "192k",
    "-t", String(DURATION_SEC),
    finalExportPath
  ]);

  let ffmpegErr = "";
  ffmpeg.stderr.on("data", d => {
    ffmpegErr += d.toString();
  });
  ffmpeg.stdin.on("error", err => {
    console.error("FFmpeg stdin error:", err.message);
  });
  ffmpeg.on("error", err => {
    console.error("FFmpeg process error:", err);
  });

  const tStart = Date.now();
  console.log("Starting deterministic overlay stepping loop (772 frames)...");

  for (let f = 0; f < TOTAL_FRAMES; f++) {
    const timeSec = f / FPS;
    await page.evaluate((t) => {
      window.masterTl.pause();
      window.masterTl.time(t);
    }, timeSec);

    // Capture transparent PNG
    const buf = await page.screenshot({ type: "png", omitBackground: true });

    if (!ffmpeg.stdin.write(buf)) {
      await new Promise(r => ffmpeg.stdin.once("drain", r));
    }

    if (f % 100 === 0 || f === TOTAL_FRAMES - 1) {
      const pct = ((f / TOTAL_FRAMES) * 100).toFixed(1);
      const elapsed = ((Date.now() - tStart) / 1000).toFixed(1);
      console.log(`Rendered frame ${f}/${TOTAL_FRAMES} (${pct}%) in ${elapsed}s`);
    }
  }

  console.log("All overlay frames written to FFmpeg stdin! Closing pipe and awaiting encode...");
  ffmpeg.stdin.end();

  await new Promise((resolve, reject) => {
    ffmpeg.on("close", code => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`FFmpeg exited with code ${code}\n${ffmpegErr}`));
      }
    });
  });

  await browser.close();

  // Copy to local project directory
  fs.copyFileSync(finalExportPath, localExportPath);
  const stat = fs.statSync(finalExportPath);
  const sizeMb = (stat.size / (1024 * 1024)).toFixed(2);
  const totalTime = ((Date.now() - tStart) / 1000).toFixed(1);

  console.log("========================================================");
  console.log(`✅ COMPOSITING 26s PUNCHY SHORT COMPLETE in ${totalTime}s!`);
  console.log(`File: ${finalExportPath} (${sizeMb} MB) | Duration: ${DURATION_SEC}s`);
  console.log("========================================================");
}

renderShort26s().catch(err => {
  console.error("Render failed:", err);
  process.exit(1);
});
