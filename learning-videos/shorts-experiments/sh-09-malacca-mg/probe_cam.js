const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const b = await chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", headless: true });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  const url = "file:///" + path.join(__dirname, "compositions", "index.html").replace(/\\/g, "/");
  await p.goto(url, { waitUntil: "networkidle" });
  await p.waitForFunction(() => window.__ready === true);
  for (const t of [0, 8, 10.5, 13, 17, 37.5]) {
    await p.evaluate(tt => window.__timeline.seek(tt, false), t);
    const vb = await p.evaluate(() => document.getElementById("map").getAttribute("viewBox"));
    const camState = await p.evaluate(() => JSON.stringify(window.__camDbg || {}));
    console.log("t=" + t, "viewBox=", vb, camState);
  }
  await b.close();
  process.exit(0);
})().catch(e => { console.log("ERR", e.message); process.exit(1); });
