const { chromium } = require("playwright");
const path = require("path");

(async () => {
  const browser = await chromium.launch({
    executablePath: "C:/Program Files/Google/Chrome/Application/chrome.exe",
    headless: true
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  page.on("console", msg => console.log("PAGE LOG:", msg.text()));
  page.on("pageerror", err => console.log("PAGE ERROR:", err.message));
  
  const fileUrl = "file:///" + path.resolve("index.html").replace(/\\/g, "/");
  console.log("Navigating to:", fileUrl);
  await page.goto(fileUrl);
  
  const exists = await page.evaluate(() => typeof window.masterTl !== "undefined");
  console.log("window.masterTl exists:", exists);
  
  const duration = await page.evaluate(() => window.masterTl.duration());
  console.log("masterTl duration:", duration);
  
  await browser.close();
})();
