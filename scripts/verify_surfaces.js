const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

const projectRoot = "D:/PERSONAL PROJECT/IR-study-companion";
const outDir = path.join(projectRoot, "preview_stills_qa");
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

async function verifySurfaces() {
  console.log("Starting OMH served-surface verification...");
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: ["--allow-file-access-from-files", "--disable-web-security"]
  });

  // 1. Verify prototype/home.html at Desktop (1440x900) and Mobile (390x844)
  const homeUrl = "file:///" + path.join(projectRoot, "prototype/home.html").replace(/\\/g, "/");
  
  // Desktop
  console.log("Testing Desktop home surface (1440x900)...");
  const pageDesk = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await pageDesk.goto(homeUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await pageDesk.waitForTimeout(1000);

  // Check Decolonization video badge in CX_DATA
  const decolonizationHasVideo = await pageDesk.evaluate(() => {
    const mod = CX_DATA.modules.find(m => m.num === "012");
    const lesson = mod ? mod.lessons.find(l => l.slug === "decolonization") : null;
    return lesson ? lesson.v : false;
  });
  console.log("prototype/home.html Decolonization video badge in CX_DATA:", decolonizationHasVideo);

  await pageDesk.screenshot({ path: path.join(outDir, "desktop_home_1440.png"), fullPage: false });
  await pageDesk.close();

  // Mobile
  console.log("Testing Mobile home surface (390x844)...");
  const pageMob = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true });
  await pageMob.goto(homeUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await pageMob.waitForTimeout(1000);
  await pageMob.screenshot({ path: path.join(outDir, "mobile_home_390.png"), fullPage: false });
  await pageMob.close();

  // 2. Verify SH-11 composition surface (1080x1920)
  console.log("Testing SH-11 Mobile Vertical Video Surface (1080x1920)...");
  const compUrl = "file:///" + path.join(projectRoot, "learning-videos/shorts-experiments/sh-11-dday-ghost-army/composition.html").replace(/\\/g, "/");
  const pageComp = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await pageComp.goto(compUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await pageComp.waitForTimeout(1000);

  // Verify GSAP timeline integrity and Three.js canvas
  const compHealth = await pageComp.evaluate(() => {
    return {
      masterTlExists: typeof masterTl !== "undefined",
      duration: masterTl ? masterTl.duration() : 0,
      canvasWidth: document.getElementById("webgl-canvas").width,
      canvasHeight: document.getElementById("webgl-canvas").height,
      subtitleTextPresent: !!document.getElementById("subtitle-text").innerText
    };
  });
  console.log("SH-11 composition health check:", compHealth);
  await pageComp.screenshot({ path: path.join(outDir, "sh11_comp_surface_1080x1920.png") });
  await pageComp.close();

  await browser.close();
  console.log("Surface verification completed successfully!");
}

verifySurfaces().catch(err => {
  console.error("Verification error:", err);
  process.exit(1);
});
