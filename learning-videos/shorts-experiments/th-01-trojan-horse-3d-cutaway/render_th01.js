const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");

const projectDir = __dirname;
const exportsDir = path.join(projectDir, "../../exports");
if (!fs.existsSync(exportsDir)) {
  fs.mkdirSync(exportsDir, { recursive: true });
}

const finalExportPath = path.join(exportsDir, "TH01_Trojan_Horse_3D_Cutaway_Short_1080p.mp4");
const localExportPath = path.join(projectDir, "TH01_Trojan_Horse_3D_Cutaway_Short_1080p.mp4");
const audioPath = path.join(projectDir, "audio/final_soundtrack_master.wav");

const FPS = 30;
const DURATION_SEC = 45.79;
const TOTAL_FRAMES = Math.ceil(DURATION_SEC * FPS); // 1374 frames
const WIDTH = 1080;
const HEIGHT = 1920;

async function renderDeterministic() {
  console.log("========================================================");
  console.log("🎬 STARTING DETERMINISTIC MP4 RENDER: TH-01 TROJAN HORSE");
  console.log(`Resolution: ${WIDTH}x${HEIGHT} | FPS: ${FPS} | Frames: ${TOTAL_FRAMES}`);
  console.log("Audio Soundtrack:", audioPath);
  console.log("Target MP4:", finalExportPath);
  console.log("========================================================");

  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: [
      "--disable-gpu-vsync",
      "--disable-background-timer-throttling",
      "--disable-renderer-backgrounding",
      "--allow-file-access-from-files",
      "--disable-web-security"
    ]
  });

  const page = await browser.newPage({ viewport: { width: WIDTH, height: HEIGHT } });
  const fileUrl = "file:///" + path.join(projectDir, "composition.html").replace(/\\/g, "/");
  console.log("Loading composition:", fileUrl);
  await page.goto(fileUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await page.waitForTimeout(1000);

  await page.evaluate(() => {
    masterTl.pause();
    masterTl.time(0);
  });

  const client = await page.context().newCDPSession(page);

  const FFMPEG_BIN = "C:/ProgramData/chocolatey/bin/ffmpeg.exe";
  console.log("Spawning FFmpeg:", FFMPEG_BIN);
  const ffmpeg = spawn(FFMPEG_BIN, [
    "-y",
    "-f", "image2pipe",
    "-vcodec", "mjpeg",
    "-r", String(FPS),
    "-i", "-",
    "-i", audioPath,
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-r", String(FPS),
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
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
  console.log("Starting deterministic frame stepping loop...");

  for (let f = 0; f < TOTAL_FRAMES; f++) {
    const timeSec = f / FPS;
    
    // Seek GSAP and video plate frame
    await page.evaluate(t => {
      masterTl.time(t);
    }, timeSec);

    // Capture screenshot as JPEG buffer
    const { data } = await client.send("Page.captureScreenshot", {
      format: "jpeg",
      quality: 92
    });

    const buf = Buffer.from(data, "base64");
    const ok = ffmpeg.stdin.write(buf);
    if (!ok) {
      await new Promise(resolve => ffmpeg.stdin.once("drain", resolve));
    }

    if (f % 100 === 0 || f === TOTAL_FRAMES - 1) {
      const elapsed = (Date.now() - tStart) / 1000;
      const pct = ((f + 1) / TOTAL_FRAMES * 100).toFixed(1);
      const fpsReal = ((f + 1) / elapsed).toFixed(1);
      console.log(`  Frame ${f + 1}/${TOTAL_FRAMES} (${pct}%) | Time: ${timeSec.toFixed(2)}s | Speed: ${fpsReal} fps`);
    }
  }

  console.log("All frames sent! Closing FFmpeg stream...");
  ffmpeg.stdin.end();

  await new Promise((resolve, reject) => {
    ffmpeg.on("close", code => {
      if (code === 0) resolve();
      else reject(new Error(`FFmpeg exited with code ${code}: ${ffmpegErr}`));
    });
  });

  await browser.close();

  fs.copyFileSync(finalExportPath, localExportPath);
  const stats = fs.statSync(finalExportPath);

  const totalTime = ((Date.now() - tStart) / 1000).toFixed(1);
  console.log("\n========================================================");
  console.log(`✅ TH-01 RENDER FINISHED IN ${totalTime}s!`);
  console.log(`File: ${finalExportPath}`);
  console.log(`Size: ${(stats.size / 1024 / 1024).toFixed(2)} MB`);
  console.log("========================================================");
}

renderDeterministic().catch(err => {
  console.error("Render failed:", err);
  process.exit(1);
});
