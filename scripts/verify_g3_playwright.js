// E2E Verification Script for Phase G3 (Homepage Integration & Sandbox)
const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

function createServer(port) {
  return new Promise((resolve) => {
    const mimeTypes = {
      '.html': 'text/html',
      '.js': 'text/javascript',
      '.css': 'text/css',
      '.json': 'application/json',
      '.png': 'image/png',
      '.jpg': 'image/jpeg',
      '.svg': 'image/svg+xml',
      '.woff': 'font/woff',
      '.woff2': 'font/woff2',
      '.ttf': 'font/ttf'
    };

    const server = http.createServer((req, res) => {
      let reqPath = decodeURI(req.url.split('?')[0]);
      if (reqPath === '/') reqPath = '/index.html';
      let filePath = path.join(__dirname, '..', '_site', reqPath);

      if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
        filePath = path.join(filePath, 'index.html');
      }

      if (!fs.existsSync(filePath)) {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
        return;
      }

      const ext = path.extname(filePath);
      const contentType = mimeTypes[ext] || 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': contentType });
      fs.createReadStream(filePath).pipe(res);
    });

    server.listen(port, '127.0.0.1', () => {
      resolve(server);
    });
  });
}

async function run() {
  const PORT = 8135;
  const server = await createServer(PORT);
  console.log(`Test server running at http://127.0.0.1:${PORT}`);

  const browser = await chromium.launch({
    channel: 'msedge',
    headless: true
  });

  const context = await browser.newContext({
    viewport: { width: 1280, height: 900 }
  });

  // Pre-seed localStorage to bypass onboarding tour modal and isolate mini-game tests
  await context.addInitScript(() => {
    localStorage.setItem('ir_onboarded_v1', 'true');
  });

  const page = await context.newPage();

  let jsErrors = [];
  page.on('pageerror', err => {
    jsErrors.push(err.message);
  });
  page.on('console', msg => {
    if (msg.type() === 'error' && !msg.text().includes('Failed to load resource')) {
      jsErrors.push(msg.text());
    }
  });

  const results = [];
  function check(desc, pass, details = '') {
    results.push({ desc, pass, details });
    console.log(`[${pass ? 'PASS' : 'FAIL'}] ${desc} ${details ? '(' + details + ')' : ''}`);
  }

  try {
    console.log('\n--- Testing Homepage G3 Features ---');
    await page.goto(`http://127.0.0.1:${PORT}/index.html`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(800);

    check('0 JavaScript runtime errors on initial load', jsErrors.length === 0, jsErrors.join('; '));

    // 1. Catalog Cards Verification
    const catalogCards = page.locator('.labs-scroll-pane .lab-card-sm');
    const cardCount = await catalogCards.count();
    check('All 10 diplomatic lab catalog cards present', cardCount === 10, `count: ${cardCount}`);

    // Verify lab IDs
    const expectedLabIds = [
      'crisis', 'game_theory', 'wto', 'security_dilemma', 'unsc_veto',
      'treaty_negotiation', 'unclos_zones', 'balance_of_power', 'scs_dispute', 'nuclear_deterrence'
    ];
    let allIdsPresent = true;
    for (const id of expectedLabIds) {
      const hasId = await page.locator(`.labs-scroll-pane .lab-card-sm[data-lab-id="${id}"]`).count();
      if (hasId !== 1) allIdsPresent = false;
    }
    check('All 10 cards have correct data-lab-id attributes', allIdsPresent);

    // Duration chips check
    const durationChips = await page.locator('.labs-scroll-pane .lab-card-chip').count();
    check('All 10 cards contain duration chips', durationChips === 10, `count: ${durationChips}`);

    // Category Filtering Check
    await page.click('button[data-filter="security"]');
    await page.waitForTimeout(200);
    let secCount = await page.locator('.labs-scroll-pane .lab-card-sm:visible').count();
    check('Filter Security displays exactly 4 cards', secCount === 4, `count: ${secCount}`);

    await page.click('button[data-filter="strategy"]');
    await page.waitForTimeout(200);
    let stratCount = await page.locator('.labs-scroll-pane .lab-card-sm:visible').count();
    check('Filter Strategy displays exactly 3 cards', stratCount === 3, `count: ${stratCount}`);

    await page.click('button[data-filter="governance"]');
    await page.waitForTimeout(200);
    let govCount = await page.locator('.labs-scroll-pane .lab-card-sm:visible').count();
    check('Filter Governance displays exactly 3 cards', govCount === 3, `count: ${govCount}`);

    await page.click('button[data-filter="all"]');
    await page.waitForTimeout(200);
    let allCount = await page.locator('.labs-scroll-pane .lab-card-sm:visible').count();
    check('Filter All restores all 10 cards', allCount === 10, `count: ${allCount}`);

    // 2. Playable Sandbox G1 Retrofit Verification
    console.log('\n--- Testing Homepage Live Sandbox ---');
    check('Sandbox HUD Round chip visible', await page.locator('#gt-round-chip').isVisible());
    check('Sandbox HUD Streak chip visible', await page.locator('#gt-streak-chip').isVisible());
    check('Sandbox HUD Best chip visible', await page.locator('#gt-best-chip').isVisible());

    // Play through 8 rounds in the sandbox
    for (let r = 1; r <= 8; r++) {
      await page.click('#btn-gt-coop');
      await page.waitForTimeout(200);
    }
    await page.waitForTimeout(600);

    // Check debrief box is now displayed
    check('Sandbox Debrief box visible after Round 8', await page.locator('#gt-debrief-box').isVisible());
    const debriefRank = await page.locator('#gt-debrief-rank').innerText();
    check('Sandbox awards rank and score', debriefRank.length > 0, debriefRank);

    // Check localStorage persistence
    const gtDone = await page.evaluate(() => localStorage.getItem('labs_completed_game_theory'));
    check('Sandbox sets labs_completed_game_theory in localStorage', gtDone === 'true');

    // Check that Lab 02 card reflects Completed ✓ and stars
    const lab2DoneBadge = await page.locator('.lab-card-sm[data-lab-id="game_theory"] .lab-card-badge-done').isVisible();
    check('Lab 02 catalog card displays Completed ✓ badge', lab2DoneBadge);
    const lab2Stars = await page.locator('.lab-card-sm[data-lab-id="game_theory"] .lab-card-stars i.fa-star:not(.is-empty)').count();
    check('Lab 02 catalog card displays active star rating', lab2Stars >= 1, `stars: ${lab2Stars}`);

    // Test dynamic hydration with mock data for other labs
    console.log('\n--- Testing Multi-Lab Dynamic Hydration ---');
    await page.evaluate(() => {
      localStorage.setItem('labs_completed_crisis', 'true');
      localStorage.setItem('labs_best_crisis', '100'); // 3 stars
      localStorage.setItem('labs_completed_wto', 'true');
      localStorage.setItem('labs_best_wto', '5'); // 3 stars
      localStorage.setItem('labs_completed_unsc_veto', 'true');
      localStorage.setItem('labs_best_unsc_veto', '15'); // 3 stars
      window.renderLabCardsProgress();
    });
    await page.waitForTimeout(200);

    const crisisBadge = await page.locator('.lab-card-sm[data-lab-id="crisis"] .lab-card-badge-done').isVisible();
    const crisisStars = await page.locator('.lab-card-sm[data-lab-id="crisis"] .lab-card-stars i.fa-star:not(.is-empty)').count();
    check('Lab 01 dynamically displays Completed ✓ badge', crisisBadge);
    check('Lab 01 dynamically displays 3 gold stars for score 100', crisisStars === 3, `stars: ${crisisStars}`);

    const unscBadge = await page.locator('.lab-card-sm[data-lab-id="unsc_veto"] .lab-card-badge-done').isVisible();
    const unscStars = await page.locator('.lab-card-sm[data-lab-id="unsc_veto"] .lab-card-stars i.fa-star:not(.is-empty)').count();
    check('Lab 05 dynamically displays Completed ✓ badge', unscBadge);
    check('Lab 05 dynamically displays 3 gold stars for 15 votes', unscStars === 3, `stars: ${unscStars}`);

    // Take screenshot of the complete catalog and sandbox
    const probeDir = path.join(__dirname, '..', 'learning-videos', 'probe');
    await page.locator('#simulations').scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(probeDir, 'g3_homepage_labs_integration.png') });
    console.log('Screenshot saved to learning-videos/probe/g3_homepage_labs_integration.png');

  } catch (err) {
    console.error('Test execution error:', err);
    check('Test run completed without unhandled exceptions', false, err.message);
  } finally {
    await browser.close();
    server.close();
  }

  const passed = results.filter(r => r.pass).length;
  const failed = results.filter(r => !r.pass).length;
  console.log('\n=============================================');
  console.log(`G3 E2E SUITE TOTAL: ${results.length} | PASSED: ${passed} | FAILED: ${failed}`);
  console.log('=============================================');

  if (failed > 0) {
    process.exit(1);
  }
}

run();
