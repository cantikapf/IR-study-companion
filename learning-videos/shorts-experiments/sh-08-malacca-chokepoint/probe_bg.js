const { chromium } = require("playwright");
const path = require("path");
(async () => {
  const b = await chromium.launch({ executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe", headless: true });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto("file:///" + path.join(__dirname, "index_v2.html").replace(/\\/g, "/"), { waitUntil: "networkidle" });
  await p.waitForFunction(() => window.__ready === true, { timeout: 20000 });
  await p.evaluate(() => window.__timeline.seek(2, false));
  const out = await p.evaluate(() => {
    const pts = [[60,300],[1000,1700],[540,960],[540,120]];
    return pts.map(([x,y]) => {
      const els = document.elementsFromPoint(x,y).slice(0,4).map(e => {
        const cs = getComputedStyle(e);
        return `${e.tagName}#${e.id}.${e.className && e.className.baseVal !== undefined ? e.className.baseVal : e.className} fill=${cs.fill} bg=${cs.backgroundColor} op=${cs.opacity}`;
      });
      return { x, y, els };
    });
  });
  console.log(JSON.stringify(out, null, 1));
  await b.close();
})();
