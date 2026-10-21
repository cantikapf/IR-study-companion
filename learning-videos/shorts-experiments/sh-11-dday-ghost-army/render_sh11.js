const { chromium } = require("playwright");
const { spawn } = require("child_process");
const path = require("path");
const fs = require("fs");

const projectDir = __dirname;
const htmlPath = path.join(projectDir, "composition.html");
const audioPath = path.join(projectDir, "audio/final_soundtrack_master.wav");
const outMp4 = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/exports/SH11_DDay_Ghost_Army_Short_1080p.mp4";

const FFMPEG_BIN = "C:/ProgramData/chocolatey/bin/ffmpeg.exe";

// Video specs
const FPS = 30;
const DURATION = 42.62;
const TOTAL_FRAMES = Math.ceil(DURATION * FPS); // 1279 frames
const WIDTH = 1080;
const HEIGHT = 1920;

console.log(`Starting deterministic Playwright render for SH-11...`);
console.log(`Total duration: ${DURATION}s | FPS: ${FPS} | Total frames: ${TOTAL_FRAMES}`);

async function renderVideo() {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: [
      "--disable-gpu-vsync",
      "--disable-background-timer-throttling",
      "--allow-file-access-from-files",
      "--disable-web-security",
      "--use-gl=angle"
    ]
  });

  const page = await browser.newPage({ viewport: { width: WIDTH, height: HEIGHT } });
  const fileUrl = "file:///" + htmlPath.replace(/\\/g, "/");
  console.log("Loading composition:", fileUrl);
  await page.goto(fileUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await page.waitForTimeout(1000);

  const client = await page.context().newCDPSession(page);

  // Spawn FFmpeg with stdin pipe
  const ffmpegArgs = [
    "-y",
    "-f", "image2pipe",
    "-vcodec", "mjpeg",
    "-r", FPS.toString(),
    "-i", "-",
    "-i", audioPath,
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    outMp4
  ];

  console.log(`Spawning FFmpeg -> ${outMp4}`);
  const ffmpegProc = spawn(FFMPEG_BIN, ffmpegArgs);

  let ffmpegErr = "";
  ffmpegProc.stderr.on("data", d => {
    const s = d.toString();
    ffmpegErr += s;
    console.log("FFMPEG:", s.trim());
  });

  ffmpegProc.stdin.on("error", err => {
    console.error("FFMPEG STDIN ERROR:", err.message);
  });

  ffmpegProc.on("error", (err) => {
    console.error("FFmpeg process error:", err);
  });

  const startTime = Date.now();

  for (let frame = 0; frame < TOTAL_FRAMES; frame++) {
    const timeSec = frame / FPS;

    await page.evaluate((t) => {
      masterTl.pause();
      masterTl.time(t);
    }, timeSec);

    const { data } = await client.send("Page.captureScreenshot", {
      format: "jpeg",
      quality: 95,
      clip: { x: 0, y: 0, width: WIDTH, height: HEIGHT, scale: 1 }
    });

    const buffer = Buffer.from(data, "base64");
    const ok = ffmpegProc.stdin.write(buffer);
    if (!ok) {
      await new Promise(resolve => ffmpegProc.stdin.once("drain", resolve));
    }

    if (frame % 100 === 0 || frame === TOTAL_FRAMES - 1) {
      const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
      const pct = ((frame / TOTAL_FRAMES) * 100).toFixed(1);
      console.log(`Frame ${frame}/${TOTAL_FRAMES} (${pct}%) encoded [${elapsed}s elapsed]`);
    }
  }

  ffmpegProc.stdin.end();

  await new Promise((resolve, reject) => {
    ffmpegProc.on("close", (code) => {
      if (code === 0) resolve();
      else reject(new Error(`FFmpeg exited with code ${code}: ${ffmpegErr}`));
    });
  });

  await browser.close();
  const totalElapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`Render complete in ${totalElapsed}s! Master MP4 output saved at: ${outMp4}`);
}

renderVideo().catch(err => {
  console.error("Render failed:", err);
  process.exit(1);
});
