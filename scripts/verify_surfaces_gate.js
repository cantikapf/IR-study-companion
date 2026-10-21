const { chromium } = require("playwright");
const path = require("path");

async function verifySurfaces() {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: ["--no-sandbox", "--disable-gpu", "--allow-file-access-from-files"]
  });

  const outDir = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/preview_stills";

  // 1. Mobile Portrait (Shorts 9:16 Screen - 1080x1920 and 390x844 mobile phone)
  const mobilePage = await browser.newPage({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2
  });

  // Test home.html on mobile
  await mobilePage.goto("file:///D:/PERSONAL%20PROJECT/IR-study-companion/prototype/home.html", { waitUntil: "networkidle" });
  await mobilePage.screenshot({ path: `${outDir}/surface_home_mobile.png`, fullPage: false });
  console.log("Captured surface_home_mobile.png");

  // 2. Desktop Viewport (1440x900)
  const desktopPage = await browser.newPage({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1
  });

  await desktopPage.goto("file:///D:/PERSONAL%20PROJECT/IR-study-companion/prototype/home.html", { waitUntil: "networkidle" });
  await desktopPage.screenshot({ path: `${outDir}/surface_home_desktop.png`, fullPage: false });
  console.log("Captured surface_home_desktop.png");

  // 3. Mobile Video Overlay Surface (390x844 scaled view)
  const videoOverlayPage = await browser.newPage({
    viewport: { width: 1080, height: 1920 },
    deviceScaleFactor: 1
  });
  await videoOverlayPage.goto("file:///D:/PERSONAL%20PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition_short_overlay.html", { waitUntil: "networkidle" });

  await videoOverlayPage.evaluate(() => {
    window.masterTl.pause();
    window.masterTl.time(6.0); // Scene 1 leader lines & subtitle
  });
  await videoOverlayPage.waitForTimeout(300);
  await videoOverlayPage.screenshot({ path: `${outDir}/surface_overlay_scene1.png` });
  console.log("Captured surface_overlay_scene1.png");

  await videoOverlayPage.evaluate(() => {
    window.masterTl.pause();
    window.masterTl.time(23.0); // Scene 3 outro & CTA
  });
  await videoOverlayPage.waitForTimeout(300);
  await videoOverlayPage.screenshot({ path: `${outDir}/surface_overlay_outro.png` });
  console.log("Captured surface_overlay_outro.png");

  await browser.close();
  console.log("All served surfaces verified and captured!");
}

verifySurfaces().catch(console.error);
