const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const b = await chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", headless: true });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto("file:///" + path.join(__dirname, "compositions", "index.html").replace(/\\/g, "/"), { waitUntil: "networkidle" });
  await p.waitForFunction(() => window.__ready === true);
  for (const t of [18.5, 20.5, 22.0, 23.0, 24.0]) {
    await p.evaluate(tt => window.__timeline.seek(tt, false), t);
    const s = await p.evaluate(() => ({
      wrapOp: getComputedStyle(document.getElementById("tankerWrap")).opacity,
      colOp: getComputedStyle(document.getElementById("column")).opacity,
      imgTop: Math.round(document.getElementById("tankerImg").getBoundingClientRect().top)
    }));
    console.log(t, JSON.stringify(s));
    await p.screenshot({ path: `snapshots/tk_${String(t).replace(".", "_")}.png` });
  }
  await b.close();
  process.exit(0);
})().catch(e => { console.log("ERR", e.message); process.exit(1); });
