const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");

const projectDir = __dirname;
const exportsDir = path.join(projectDir, "../../../learning-videos/exports");
if (!fs.existsSync(exportsDir)) {
  fs.mkdirSync(exportsDir, { recursive: true });
}

const finalExportPath = path.join(exportsDir, "SH03_Thucydides_Trap_Map_Animation_Short_1080p.mp4");
const localExportPath = path.join(projectDir, "output_thucydides_trap_short.mp4");
const audioPath = path.join(projectDir, "audio/voiceover.mp3");

const FPS = 30;
const DURATION_SEC = 41.83;
const TOTAL_FRAMES = Math.ceil(DURATION_SEC * FPS); // 1255 frames

async function renderDeterministic() {
  console.log("========================================================");
  console.log("🎬 STARTING DETERMINISTIC FRAME-BY-FRAME RENDER (TRI-HYBRID)");
  console.log(`Resolution: 1080x1920 | FPS: ${FPS} | Frames: ${TOTAL_FRAMES}`);
  console.log("========================================================");

  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: [
      "--disable-gpu-vsync",
      "--disable-background-timer-throttling",
      "--disable-renderer-backgrounding"
    ]
  });

  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  const fileUrl = "file:///" + path.join(projectDir, "index.html").replace(/\\/g, "/");
  console.log("Loading composition:", fileUrl);
  await page.goto(fileUrl);

  // Ensure fonts and scripts are fully evaluated
  await page.waitForTimeout(1000);

  await page.evaluate(() => {
    masterTl.pause();
    masterTl.time(0);
  });

  const client = await page.context().newCDPSession(page);

  console.log("Spawning ffmpeg with image2pipe stdin...");
  const ffmpeg = spawn("ffmpeg", [
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
    "-af", "apad=pad_dur=1.5",
    "-shortest",
    finalExportPath
  ]);

  let ffmpegErr = "";
  ffmpeg.stderr.on("data", d => {
    ffmpegErr += d.toString();
  });

  const tStart = Date.now();
  console.log("Starting frame stepping loop...");

  for (let f = 0; f < TOTAL_FRAMES; f++) {
    const timeSec = f / FPS;
    
    // Exact frame seek in GSAP
    await page.evaluate(t => {
      masterTl.time(t);
    }, timeSec);

    // Capture exact frame as JPEG buffer
    const { data } = await client.send("Page.captureScreenshot", {
      format: "jpeg",
      quality: 92
    });

    const buf = Buffer.from(data, "base64");
    ffmpeg.stdin.write(buf);

    if (f % 90 === 0 || f === TOTAL_FRAMES - 1) {
      const elapsed = (Date.now() - tStart) / 1000;
      const pct = ((f + 1) / TOTAL_FRAMES * 100).toFixed(1);
      const fpsReal = ((f + 1) / elapsed).toFixed(1);
      console.log(`  Frame ${f + 1}/${TOTAL_FRAMES} (${pct}%) | Time: ${timeSec.toFixed(2)}s | Speed: ${fpsReal} fps`);
    }
  }

  console.log("All frames sent! Closing ffmpeg stream...");
  ffmpeg.stdin.end();

  await new Promise((resolve, reject) => {
    ffmpeg.on("close", code => {
      if (code === 0) resolve();
      else reject(new Error(`ffmpeg exited with code ${code}: ${ffmpegErr}`));
    });
  });

  await browser.close();

  fs.copyFileSync(finalExportPath, localExportPath);
  const stats = fs.statSync(finalExportPath);

  const totalTime = ((Date.now() - tStart) / 1000).toFixed(1);
  console.log("\n========================================================");
  console.log("🎉 DETERMINISTIC RENDER COMPLETE (100% BUTTER SMOOTH)!");
  console.log(`Export File: ${finalExportPath}`);
  console.log(`Size: ${(stats.size / (1024 * 1024)).toFixed(2)} MB`);
  console.log(`Render Duration: ${totalTime}s`);
  console.log("========================================================");
}

renderDeterministic().catch(err => {
  console.error("Render failed:", err);
  process.exit(1);
});
