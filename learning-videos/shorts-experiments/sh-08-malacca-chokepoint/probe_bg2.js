const { chromium } = require("playwright");
const path = require("path");
const projectDir = __dirname;
(async () => {
  const b = await chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", headless: true });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  const fileUrl = "file:///" + path.join(projectDir, "index_v2.html").replace(/\\/g, "/");
  await p.goto(fileUrl, { waitUntil: "networkidle", timeout: 30000 });
  await p.waitForFunction(() => window.__ready === true, { timeout: 20000 });
  await p.evaluate(() => window.__timeline.seek(2, false));
  const out = await p.evaluate(() => {
    const pts = [[60, 300], [1000, 1700], [540, 960]];
    return pts.map(([x, y]) => ({
      x, y,
      els: document.elementsFromPoint(x, y).slice(0, 6).map(e => {
        const cs = getComputedStyle(e);
        const cls = (e.className && e.className.baseVal !== undefined) ? e.className.baseVal : e.className;
        return e.tagName + "#" + e.id + "|" + String(cls).slice(0, 26) + "|fill=" + cs.fill + "|bg=" + cs.backgroundColor + "|op=" + cs.opacity;
      })
    }));
  });
  require("fs").writeFileSync(path.join(projectDir, "probe_out.json"), JSON.stringify(out, null, 1));
  await b.close();
  process.exit(0);
})().catch(e => { console.log("ERR", e.message); process.exit(1); });
