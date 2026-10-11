const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const projectDir = __dirname;
const tmpDir = path.join(process.env.LOCALAPPDATA || "C:/Users/xiyeo/AppData/Local", "hermes/cache/scratch/sh05_render");
if (fs.existsSync(tmpDir)) {
  fs.rmSync(tmpDir, { recursive: true, force: true });
}
fs.mkdirSync(tmpDir, { recursive: true });

const exportsDir = path.join(projectDir, "../../../learning-videos/exports");
if (!fs.existsSync(exportsDir)) {
  fs.mkdirSync(exportsDir, { recursive: true });
}

const finalExportPath = path.join(exportsDir, "SH05_Cuban_Missile_Crisis_Map_Animation_Short_1080p.mp4");
const localExportPath = path.join(projectDir, "output_cuban_crisis_short.mp4");
const audioPath = path.join(projectDir, "audio/voiceover.mp3");

async function renderVideo() {
  console.log("=== Launching Chrome to render 1080x1920 Shorts ===");
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: [
      "--autoplay-policy=no-user-gesture-required",
      "--disable-gpu-vsync",
      "--disable-background-timer-throttling",
      "--disable-renderer-backgrounding"
    ]
  });

  const context = await browser.newContext({
    viewport: { width: 1080, height: 1920 },
    recordVideo: {
      dir: tmpDir,
      size: { width: 1080, height: 1920 }
    }
  });

  const page = await context.newPage();
  const fileUrl = "file:///" + path.join(projectDir, "index.html").replace(/\\/g, "/");
  console.log("Navigating to:", fileUrl);
  await page.goto(fileUrl);

  // Setup full 1-to-1 canvas without preview scaler borders
  await page.evaluate(() => {
    const s = document.getElementById("viewport-scaler");
    s.style.transform = "none";
    s.style.top = "0";
    s.style.left = "0";
    s.style.borderRadius = "0";
    s.style.border = "none";
    s.style.boxShadow = "none";
    document.getElementById("hud-controls").style.display = "none";
    
    // Play audio & timeline in sync
    const aud = document.getElementById("main-audio");
    aud.currentTime = 0;
    aud.play().catch(() => {});
    masterTl.restart();
    masterTl.play();
  });

  const durationMs = 41200; // 41.2 seconds to allow full tail
  console.log(`Recording animation for ${(durationMs / 1000).toFixed(1)} seconds...`);
  
  // Progress logging
  const interval = 5000;
  for (let elapsed = 0; elapsed < durationMs; elapsed += interval) {
    await page.waitForTimeout(interval);
    console.log(`  Progress: ${((elapsed + interval) / 1000).toFixed(1)}s / ${(durationMs / 1000).toFixed(1)}s`);
  }

  await page.close();
  await context.close();
  await browser.close();

  console.log("Recording complete! Finding recorded file...");
  const files = fs.readdirSync(tmpDir).filter(f => f.endsWith(".webm"));
  if (files.length === 0) {
    throw new Error("No webm recording found in: " + tmpDir);
  }
  const rawWebm = path.join(tmpDir, files[0]);
  console.log("Recorded WebM:", rawWebm);

  console.log("=== Detecting exact start time to eliminate initial loading screen ===");
  // Automatically probe when the dark animation canvas starts
  const pythonProbe = `
import subprocess, os
from PIL import Image

raw_webm = r"${rawWebm}"
start_sec = 0.0
for ms in range(0, 5000, 50):
    sec = ms / 1000.0
    tmp_png = r"${path.join(tmpDir, 'probe.png')}"
    subprocess.run(['ffmpeg', '-y', '-ss', str(sec), '-i', raw_webm, '-vframes', '1', tmp_png], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(tmp_png):
        im = Image.open(tmp_png).convert('L')
        avg = sum(im.getdata()) / (im.width * im.height)
        os.remove(tmp_png)
        if avg < 100:
            start_sec = sec
            break
print(start_sec)
`;

  const probePyPath = path.join(tmpDir, "probe.py");
  fs.writeFileSync(probePyPath, pythonProbe);
  const detectedStart = parseFloat(execSync(`"C:\\Users\\xiyeo\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" "${probePyPath}"`).toString().trim());
  console.log(`Detected exact animation start at: ${detectedStart.toFixed(3)}s`);

  console.log("=== Encoding final 1080x1920 MP4 with ffmpeg ===");
  const ffmpegCmd = [
    "ffmpeg", "-y",
    "-ss", detectedStart.toFixed(3),
    "-i", `"${rawWebm}"`,
    "-i", `"${audioPath}"`,
    "-c:v", "libx264",
    "-preset", "medium",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-r", "30",
    "-c:a", "aac",
    "-b:a", "192k",
    "-shortest",
    `"${finalExportPath}"`
  ].join(" ");

  console.log("Running ffmpeg command...");
  execSync(ffmpegCmd, { stdio: "inherit" });

  fs.copyFileSync(finalExportPath, localExportPath);

  const stats = fs.statSync(finalExportPath);
  console.log("\n========================================================");
  console.log("🎉 SHORT VIDEO RENDER SUCCESS!");
  console.log("Export File 1:", finalExportPath);
  console.log("Export File 2:", localExportPath);
  console.log(`File Size: ${(stats.size / (1024 * 1024)).toFixed(2)} MB`);
  console.log("========================================================");
}

renderVideo().catch(err => {
  console.error("Render failed:", err);
  process.exit(1);
});
