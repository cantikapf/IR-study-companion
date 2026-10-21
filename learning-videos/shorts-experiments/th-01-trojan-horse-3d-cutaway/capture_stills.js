const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const projectDir = __dirname;
const outDir = path.join(projectDir, "preview_stills");

const timestamps = [
  { t: 2.5, name: "frame_02_5s_hook.png" },
  { t: 10.0, name: "frame_10_0s_two_tier_cutaway.png" },
  { t: 20.0, name: "frame_20_0s_temp_vents.png" },
  { t: 30.0, name: "frame_30_0s_midnight_trapdoor.png" },
  { t: 38.0, name: "frame_38_0s_city_falls_relief.png" },
  { t: 44.0, name: "frame_44_0s_channel_outro.png" }
];

async function captureStills() {
  console.log("Launching headless Chrome for TH-01 preview still capture...");
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

  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  const fileUrl = "file:///" + path.join(projectDir, "composition.html").replace(/\\/g, "/");
  console.log("Loading composition:", fileUrl);
  await page.goto(fileUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await page.waitForTimeout(1000);

  const client = await page.context().newCDPSession(page);

  for (const item of timestamps) {
    await page.evaluate((timeSec) => {
      masterTl.pause();
      masterTl.time(timeSec);
    }, item.t);

    await page.waitForTimeout(200);

    const { data } = await client.send("Page.captureScreenshot", {
      format: "png",
      clip: { x: 0, y: 0, width: 1080, height: 1920, scale: 1 }
    });

    const targetPath = path.join(outDir, item.name);
    fs.writeFileSync(targetPath, Buffer.from(data, "base64"));
    console.log(`Captured still at t=${item.t}s -> ${item.name}`);
  }

  await browser.close();
  console.log("All TH-01 preview stills captured successfully!");
}

captureStills().catch(err => {
  console.error("Error capturing stills:", err);
  process.exit(1);
});
