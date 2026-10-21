// Proof snapshots + safe-area assertion. node shoot.js
const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

const ROOT = path.join(__dirname);
const OUT = path.join(ROOT, "snapshots");
const TIMES = [0.6, 2.6, 4.2, 9.8, 13.0, 19.0, 24.0, 31.0, 35.5, 40.5, 44.0];
const SAFE_TOP = 200, SAFE_BOTTOM = 1590;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  const errs = [];
  page.on("pageerror", e => errs.push("PAGEERROR " + e.message));
  page.on("console", m => { if (m.type() === "error") errs.push("CONSOLE " + m.text()); });

  await page.goto("file:///" + path.join(ROOT, "compositions", "index.html").replace(/\\/g, "/"),
    { waitUntil: "networkidle", timeout: 30000 });
  await page.waitForFunction(() => window.__ready === true, { timeout: 20000 });

  const results = [];
  for (const t of TIMES) {
    await page.evaluate(tt => {
      window.__timeline.seek(tt, false);
      window.__timeline.pause();
    }, t);
    await page.waitForTimeout(90);
    const name = `t${String(t).replace(".", "_")}.png`;
    await page.screenshot({ path: path.join(OUT, name) });

    // collect every visible text node's rect
    const boxes = await page.evaluate(() => {
      const sel = ".sticker,.card,.tag,#hypo,#endcard h1,#endcard .sub,.geo,#column";
      return [...document.querySelectorAll(sel)].filter(el => {
        const cs = getComputedStyle(el);
        return parseFloat(cs.opacity) > 0.35 && cs.display !== "none";
      }).map(el => {
        const r = el.getBoundingClientRect();
        return { id: el.id || el.className, top: Math.round(r.top), bottom: Math.round(r.bottom),
                 left: Math.round(r.left), right: Math.round(r.right) };
      });
    });
    const bad = boxes.filter(b => b.top < SAFE_TOP || b.bottom > SAFE_BOTTOM || b.left < 24 || b.right > 1056);
    const vb = await page.evaluate(() => document.getElementById("map").getAttribute("viewBox"));
    results.push({ t, name, boxes: boxes.length, bad, viewBox: vb });
    console.log(`t=${t}s  boxes=${boxes.length}  violations=${bad.length}  vb=${vb}` +
      (bad.length ? "  -> " + bad.map(b => `${b.id}(${b.top}-${b.bottom})`).join(" ") : ""));
  }

  fs.writeFileSync(path.join(OUT, "report.json"), JSON.stringify(results, null, 1));
  if (errs.length) { console.log("ERRORS:"); errs.forEach(e => console.log("  " + e)); }
  else console.log("no page errors");
  await browser.close();
})().catch(e => { console.error("FAIL", e.message); process.exit(1); });
