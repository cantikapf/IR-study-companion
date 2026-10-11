const { chromium } = require("playwright");

async function testCDP() {
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

  const t0 = Date.now();
  for (let i = 0; i < 20; i++) {
    await page.evaluate(t => {
      masterTl.time(t);
    }, i / 30.0);
    const { data } = await client.send("Page.captureScreenshot", { format: "jpeg", quality: 85 });
  }
  const dt = Date.now() - t0;
  console.log("20 frames with CDP took:", dt, "ms (", (20 / (dt / 1000)).toFixed(1), "fps render speed )");
  await browser.close();
}
testCDP();
