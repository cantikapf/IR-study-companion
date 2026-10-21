const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

const MIME_TYPES = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.mjs': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2',
  '.mp3': 'audio/mpeg'
};

const SITE_ROOT = path.join(process.cwd(), '_site');

function startSiteServer(port) {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      let cleanUrl = decodeURI(req.url.split('?')[0].split('#')[0]);
      if (cleanUrl === '/') cleanUrl = '/index.html';
      let filePath = path.join(SITE_ROOT, cleanUrl);

      if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
        filePath = path.join(filePath, 'index.html');
      }

      if (!fs.existsSync(filePath)) {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found: ' + cleanUrl);
        return;
      }

      const ext = path.extname(filePath);
      res.writeHead(200, {
        'Content-Type': MIME_TYPES[ext] || 'application/octet-stream',
        'Cache-Control': 'no-store'
      });
      fs.createReadStream(filePath).pipe(res);
    });

    server.listen(port, '127.0.0.1', () => resolve(server));
  });
}

(async () => {
  const PORT = 8421;
  const server = await startSiteServer(PORT);
  console.log(`_site server running at http://127.0.0.1:${PORT}`);

  const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
  const browser = await chromium.launch({
    headless: true,
    executablePath: edgePath
  });
  const context = await browser.newContext({
    viewport: { width: 1400, height: 900 }
  });

  await context.addInitScript(() => {
    localStorage.setItem('ir_onboarded_v1', 'true');
    localStorage.setItem('onboarding_dismissed_v1', 'true');
  });

  const page = await context.newPage();
  const scratchDir = 'C:/Users/xiyeo/AppData/Local/hermes/cache/scratch';

  try {
    // 1. Test Production Homepage
    console.log('--- Testing Production Homepage ---');
    await page.goto(`http://127.0.0.1:${PORT}/index.html#simulations`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(3000);

    const homeTitle = await page.title();
    console.log('Homepage Title:', homeTitle);

    // Initial Badge & Frame
    let badgeText = await page.$eval('#homeLiveBadge', el => el.textContent.trim());
    let iframeSrc = await page.$eval('#homeLabFrame', el => el.getAttribute('src'));
    console.log('Homepage initial active lab ->', badgeText, '| src:', iframeSrc);

    // Click Lab 04 on production homepage
    console.log('Switching to Lab 04 on production homepage...');
    await page.click('.home-lab-card[data-id="lab-04"]');
    await page.waitForTimeout(2500);

    badgeText = await page.$eval('#homeLiveBadge', el => el.textContent.trim());
    iframeSrc = await page.$eval('#homeLabFrame', el => el.getAttribute('src'));
    console.log('Homepage switched to ->', badgeText, '| src:', iframeSrc);

    const shotProdHome = path.join(scratchDir, 'prod_homepage_simulations.png');
    await page.screenshot({ path: shotProdHome });
    console.log('Production homepage screenshot saved:', shotProdHome);

    // 2. Test Production Chapter with Total Replacement Embed (Chapter 030 FPA)
    console.log('\n--- Testing Production Chapter 030 (Models FPDM) ---');
    await page.goto(`http://127.0.0.1:${PORT}/models-fpdm.html#sim-lab-01-crisis-command-container`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(3000);

    const chapterTitle = await page.title();
    console.log('Chapter 030 Title:', chapterTitle);

    const embedEl = await page.$('#sim-lab-01-crisis-command-container');
    console.log('Has #sim-lab-01-crisis-command-container:', !!embedEl);

    // Scroll embed into view centered
    if (embedEl) {
      await embedEl.scrollIntoViewIfNeeded();
      await page.waitForTimeout(2000);
    }

    const chIframeSrc = await page.$eval('#sim-lab-01-crisis-command-container iframe', el => el.getAttribute('src'));
    console.log('Chapter 030 Iframe src:', chIframeSrc);

    const shotProdChapter = path.join(scratchDir, 'prod_chapter_models_fpdm.png');
    await page.screenshot({ path: shotProdChapter });
    console.log('Production Chapter 030 screenshot saved:', shotProdChapter);

    console.log('\nALL E2E BROWSER TESTS PASSED ON _site OUTPUT!');
  } catch (err) {
    console.error('Test error:', err);
    process.exitCode = 1;
  } finally {
    await browser.close();
    server.close();
  }
})();
