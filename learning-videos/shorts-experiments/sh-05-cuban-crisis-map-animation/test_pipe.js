const { chromium } = require("playwright");
const { spawn } = require("child_process");

async function testPipe() {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto("file:///D:/PERSONAL%20PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-05-cuban-crisis-map-animation/index.html");
  
  await page.evaluate(() => {
    const s = document.getElementById("viewport-scaler");
    s.style.transform = "none";
    s.style.top = "0";
    s.style.left = "0";
    s.style.borderRadius = "0";
    s.style.border = "none";
    document.getElementById("hud-controls").style.display = "none";
    masterTl.pause();
  });

  const client = await page.context().newCDPSession(page);

  const ffmpeg = spawn("ffmpeg", [
    "-y",
    "-f", "image2pipe",
    "-vcodec", "mjpeg",
    "-r", "30",
    "-i", "-",
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "C:/Users/xiyeo/AppData/Local/hermes/cache/scratch/pipe_test.mp4"
  ]);

  ffmpeg.stderr.on("data", d => {});

  const t0 = Date.now();
  for (let i = 0; i < 60; i++) {
    await page.evaluate(t => {
      masterTl.time(t);
    }, i / 30.0);
    const { data } = await client.send("Page.captureScreenshot", { format: "jpeg", quality: 90 });
    const buffer = Buffer.from(data, "base64");
    ffmpeg.stdin.write(buffer);
  }
  ffmpeg.stdin.end();

  await new Promise(res => ffmpeg.on("close", res));
  console.log("60 frames piped in:", Date.now() - t0, "ms");
  await browser.close();
}
testPipe();
