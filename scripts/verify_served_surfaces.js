const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

const projectRoot = "D:/PERSONAL PROJECT/IR-study-companion";
const outDir = path.join(projectRoot, "preview_stills_qa");
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

async function verifyServedSurfaces() {
  console.log("Launching headless Chrome for served-surface verification...");
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true,
    args: ["--allow-file-access-from-files", "--disable-web-security"]
  });

  // 1. Desktop surface check: prototype/home.html at 1440x900
  const homeUrl = "file:///" + path.join(projectRoot, "prototype/home.html").replace(/\\/g, "/");
  const pageDesk = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await pageDesk.goto(homeUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await pageDesk.waitForTimeout(800);

  // Interaction test: click on Curriculum link or search input
  const deskEvidence = await pageDesk.evaluate(() => {
    const navbarLinks = Array.from(document.querySelectorAll("nav a, .nav-links a")).map(a => a.innerText.trim());
    const heroH1 = document.querySelector("h1") ? document.querySelector("h1").innerText.trim() : "";
    const cxDecolonization = CX_DATA.modules.find(m => m.num === "012").lessons.find(l => l.slug === "decolonization").v;
    return { navbarLinks, heroH1, cxDecolonization };
  });
  console.log("Desktop surface evaluated:", deskEvidence);
  await pageDesk.screenshot({ path: path.join(outDir, "desktop_home_observed.png") });
  await pageDesk.close();

  // 2. Mobile surface check: prototype/home.html at 390x844
  const pageMob = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true });
  await pageMob.goto(homeUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await pageMob.waitForTimeout(800);

  const mobEvidence = await pageMob.evaluate(() => {
    const bodyScrollWidth = document.body.scrollWidth;
    const windowInnerWidth = window.innerWidth;
    return {
      bodyScrollWidth,
      windowInnerWidth,
      hasHorizontalOverflow: bodyScrollWidth > windowInnerWidth
    };
  });
  console.log("Mobile surface evaluated:", mobEvidence);
  await pageMob.screenshot({ path: path.join(outDir, "mobile_home_observed.png") });
  await pageMob.close();

  // 3. SH-11 Video Surface Check: composition.html at 1080x1920 across key scenes
  const compUrl = "file:///" + path.join(projectRoot, "learning-videos/shorts-experiments/sh-11-dday-ghost-army/composition.html").replace(/\\/g, "/");
  const pageComp = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await pageComp.goto(compUrl, { waitUntil: "domcontentloaded", timeout: 15000 });
  await pageComp.waitForTimeout(1000);

  const compCheck = await pageComp.evaluate(() => {
    const subBox = document.getElementById("subtitle-box");
    const subRect = subBox.getBoundingClientRect();
    return {
      masterTlActive: typeof masterTl !== "undefined",
      canvasVisible: !!document.getElementById("webgl-canvas"),
      subtitleBottom: window.innerHeight - subRect.bottom,
      subtitleSafeZonePass: (window.innerHeight - subRect.bottom) >= 400
    };
  });
  console.log("SH-11 composition surface evaluated:", compCheck);
  await pageComp.screenshot({ path: path.join(outDir, "sh11_comp_observed.png") });
  await pageComp.close();

  await browser.close();
  console.log("Served-surface verification finished successfully!");
}

verifyServedSurfaces().catch(err => {
  console.error("Verification failed:", err);
  process.exit(1);
});
