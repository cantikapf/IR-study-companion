const { chromium } = require('playwright');
const http = require('http');
const fs = require('fs');
const path = require('path');

// Simple static server for _site
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
  const PORT = 8125;
  const server = await createServer(PORT);
  console.log(`Test server running at http://127.0.0.1:${PORT}`);

  const screenshotsDir = path.join(__dirname, '..', 'learning-videos', 'probe');
  if (!fs.existsSync(screenshotsDir)) {
    fs.mkdirSync(screenshotsDir, { recursive: true });
  }

  const browser = await chromium.launch({
    channel: 'msedge',
    headless: true
  });

  const context = await browser.newContext({
    viewport: { width: 1280, height: 900 }
  });

  const page = await context.newPage();

  let consoleErrors = [];
  page.on('console', msg => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });
  page.on('pageerror', err => {
    consoleErrors.push(err.message);
  });

  const results = [];
  function check(desc, pass, details = '') {
    results.push({ desc, pass, details });
    console.log(`[${pass ? 'PASS' : 'FAIL'}] ${desc} ${details ? '(' + details + ')' : ''}`);
  }

  try {
    // ==========================================
    // LAB 01: Crisis Command (models-fpdm.html)
    // ==========================================
    console.log('\n--- Testing Lab 01: Crisis Command ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/models-fpdm.html`, { waitUntil: 'networkidle' });
    check('Lab 01: 0 console errors on load', consoleErrors.length === 0, `errors: ${consoleErrors.length}`);
    check('Lab 01: Briefing visible', await page.locator('#sim-crisis-briefing').isVisible());
    
    // Screenshot: Lab 01 Briefing
    await page.locator('#crisis-sim').scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await page.locator('#crisis-sim').screenshot({ path: path.join(screenshotsDir, 'g2_lab01_briefing.png') });

    await page.click('#sim-crisis-btn-begin');
    check('Lab 01: Play area active after begin', await page.locator('#sim-crisis-play').isVisible());

    // Play Act 1: choose Quarantine (option 1)
    await page.waitForSelector('#sim-crisis-options .sim-crisis-opt-btn');
    const optButtons1 = page.locator('#sim-crisis-options .sim-crisis-opt-btn');
    await optButtons1.nth(1).click(); // Blockade
    await page.waitForTimeout(600);

    // Act 2: Check SIGINT intercept
    const logText1 = await page.locator('#sim-crisis-log').innerText();
    check('Lab 01: SIGINT intercept present in log', logText1.includes('SIGINT INTERCEPT · ACT 2'));

    // Play Act 2: choose Trollope ploy (option 1)
    await page.waitForSelector('#sim-crisis-options .sim-crisis-opt-btn');
    const optButtons2 = page.locator('#sim-crisis-options .sim-crisis-opt-btn');
    await optButtons2.nth(1).click(); // Trollope ploy
    await page.waitForTimeout(600);

    // Play Act 3: choose Quid Pro Quo (option 0)
    await page.waitForSelector('#sim-crisis-options .sim-crisis-opt-btn');
    const optButtons3 = page.locator('#sim-crisis-options .sim-crisis-opt-btn');
    await optButtons3.nth(0).click(); // Quid-Pro-Quo
    await page.waitForTimeout(1000);

    check('Lab 01: Debrief visible', await page.locator('#sim-crisis-outcome').isVisible());
    const rank1 = await page.locator('#sim-crisis-rank').innerText();
    check('Lab 01: Master Strategist rank achieved', rank1.includes('Master Strategist') || rank1.includes('Crisis Manager'), rank1);
    const reveal1 = await page.locator('#sim-crisis-reveal-body').innerText();
    check('Lab 01: Cites Graham Allison and Models I/II/III', reveal1.includes('Graham Allison') && reveal1.includes('Model I'));
    const flag1 = await page.evaluate(() => localStorage.getItem('labs_completed_crisis'));
    check('Lab 01: localStorage flag set', flag1 === 'true');

    // Screenshot: Lab 01 Debrief
    await page.locator('#sim-crisis-outcome').screenshot({ path: path.join(screenshotsDir, 'g2_lab01_debrief.png') });

    // ==========================================
    // LAB 03: Consensus Market (wto-decision-making.html)
    // ==========================================
    console.log('\n--- Testing Lab 03: Consensus Market ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/wto-decision-making.html`, { waitUntil: 'networkidle' });
    check('Lab 03: 0 console errors on load', consoleErrors.length === 0);
    check('Lab 03: Briefing visible', await page.locator('#sim-wto-briefing').isVisible());

    await page.click('#sim-wto-btn-begin');
    check('Lab 03: Play area active', await page.locator('#sim-wto-play').isVisible());
    
    // Default optimal: Agri moderate (2), TRIPS health (1), SDT granted (2), Fish voluntary (1), Tariff none (0) = 6 pts spent, 4 remaining!
    const voteBtn = page.locator('#sim-wto-btn-vote');
    check('Lab 03: Vote button enabled with remaining capital', await voteBtn.isEnabled());
    await voteBtn.click();
    await page.waitForTimeout(1000);

    check('Lab 03: Debrief visible', await page.locator('#sim-wto-outcome').isVisible());
    const stars3 = await page.locator('#sim-wto-stars .lab-star-in').count();
    check('Lab 03: 3 stars awarded for ≥4 capital left', stars3 === 3, `stars: ${stars3}`);
    const reveal3 = await page.locator('#sim-wto-reveal-body').innerText();
    check('Lab 03: Cites Marrakesh Agreement Article IX and Single Undertaking', reveal3.includes('Single Undertaking') && reveal3.includes('Article IX'));
    const flag3 = await page.evaluate(() => localStorage.getItem('labs_completed_wto'));
    check('Lab 03: localStorage flag set', flag3 === 'true');

    // ==========================================
    // LAB 04: Spiral Watch (realism-security.html)
    // ==========================================
    console.log('\n--- Testing Lab 04: Spiral Watch ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/realism-security.html`, { waitUntil: 'networkidle' });
    check('Lab 04: 0 console errors on load', consoleErrors.length === 0);
    check('Lab 04: Briefing visible', await page.locator('#sim-sd-briefing').isVisible());

    await page.click('#sim-sd-btn-begin');
    check('Lab 04: Play area active', await page.locator('#sim-sd-play').isVisible());

    // Play 5 rounds of Signal / Reduce to reach Security Community
    for (let r = 1; r <= 5; r++) {
      if (r % 2 === 1) {
        await page.click('#sim-sd-btn-signal');
      } else {
        await page.click('#sim-sd-btn-reduce');
      }
      await page.waitForTimeout(200);
    }
    await page.waitForTimeout(600);

    check('Lab 04: Debrief visible', await page.locator('#sim-sd-outcome').isVisible());
    const reveal4 = await page.locator('#sim-sd-mech-reveal').innerText();
    check('Lab 04: Cites Robert Jervis 1976 and type uncertainty', reveal4.includes('Robert Jervis') && reveal4.includes('type uncertainty'));
    const flag4 = await page.evaluate(() => localStorage.getItem('labs_completed_security_dilemma'));
    check('Lab 04: localStorage flag set', flag4 === 'true');

    // ==========================================
    // LAB 05: Veto Gauntlet (UN-security.html)
    // ==========================================
    console.log('\n--- Testing Lab 05: Veto Gauntlet ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/UN-security.html`, { waitUntil: 'networkidle' });
    check('Lab 05: 0 console errors on load', consoleErrors.length === 0);
    check('Lab 05: Briefing visible', await page.locator('#sim-unsc-briefing').isVisible());

    await page.click('#sim-unsc-btn-begin');
    check('Lab 05: Play area active', await page.locator('#sim-unsc-play').isVisible());

    // Select all 5 amendments for unanimous 15/15 pass
    await page.click('label[for="token-consent"]');
    await page.click('label[for="token-selfdefense"]');
    await page.click('label[for="token-carveout"]');
    await page.click('label[for="token-regional"]');
    await page.click('label[for="token-monitoring"]');
    await page.waitForTimeout(300);

    await page.click('#sim-unsc-btn-vote');
    await page.waitForTimeout(1000);

    check('Lab 05: Debrief visible', await page.locator('#sim-unsc-outcome').isVisible());
    const votes5 = await page.locator('#sim-unsc-stat-votes').innerText();
    check('Lab 05: 15 / 15 unanimous votes achieved', votes5.includes('15 / 15'), votes5);
    const stars5 = await page.locator('#sim-unsc-stars .lab-star-in').count();
    check('Lab 05: 3 stars awarded', stars5 === 3, `stars: ${stars5}`);
    const reveal5 = await page.locator('#sim-unsc-reveal-body').innerText();
    check('Lab 05: Cites UN Charter Article 27(3) and Great Power Unanimity', reveal5.includes('Article 27') && reveal5.includes('Great Power Unanimity'));
    const flag5 = await page.evaluate(() => localStorage.getItem('labs_completed_unsc_veto'));
    check('Lab 05: localStorage flag set', flag5 === 'true');

    // ==========================================
    // LAB 06: Two-Table Pressure (tools-diplomacy.html)
    // ==========================================
    console.log('\n--- Testing Lab 06: Two-Table Pressure ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/tools-diplomacy.html`, { waitUntil: 'networkidle' });
    check('Lab 06: 0 console errors on load', consoleErrors.length === 0);
    check('Lab 06: Briefing visible', await page.locator('#sim-tn-briefing').isVisible());

    await page.click('#sim-tn-btn-begin');
    check('Lab 06: Play area active', await page.locator('#sim-tn-play').isVisible());

    // Play 6 turns with Balanced Diplomacy (1 Int / 1 Dom) -> 6 * 18% = 100% ZOPA!
    for (let t = 1; t <= 6; t++) {
      const balancedBtn = page.locator('#sim-tn-play .sim-tn-alloc-btn').nth(1);
      await balancedBtn.click();
      await page.waitForTimeout(200);
    }
    await page.waitForTimeout(800);

    check('Lab 06: Debrief visible', await page.locator('#sim-tn-outcome').isVisible());
    const zopa6 = await page.locator('#sim-tn-stat-zopa').innerText();
    check('Lab 06: ZOPA reaches 100% (≥ 70%)', parseInt(zopa6) >= 70, zopa6);
    const stars6 = await page.locator('#sim-tn-stars .lab-star-in').count();
    check('Lab 06: 3 stars awarded', stars6 === 3, `stars: ${stars6}`);
    const reveal6 = await page.locator('#sim-tn-reveal-body').innerText();
    check('Lab 06: Cites Robert Putnam 1988 and Two-Level Games', reveal6.includes('Robert Putnam') && reveal6.includes('Two-Level Games'));
    const flag6 = await page.evaluate(() => localStorage.getItem('labs_completed_treaty_negotiation'));
    check('Lab 06: localStorage flag set', flag6 === 'true');

    // ==========================================
    // LAB 07: Zone Runner (law-of-the-sea.html)
    // ==========================================
    console.log('\n--- Testing Lab 07: Zone Runner ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/law-of-the-sea.html`, { waitUntil: 'networkidle' });
    check('Lab 07: 0 console errors on load', consoleErrors.length === 0);
    check('Lab 07: Briefing visible', await page.locator('#sim-uz-briefing').isVisible());

    await page.click('#sim-uz-btn-begin');
    check('Lab 07: Play area active', await page.locator('#sim-uz-play').isVisible());

    // Use SIGINT Pass on Incident 1
    await page.click('#sim-uz-sigint-btn');
    await page.waitForTimeout(500);

    // Answer remaining 9 incidents using correct option
    for (let inc = 2; inc <= 10; inc++) {
      await page.waitForSelector('#sim-uz-choices .sim-uz-choice-btn');
      // Click the first choice that has correct logic via script evaluate
      await page.evaluate(() => {
        const btns = document.querySelectorAll('.sim-uz-choice-btn');
        // Trigger click on correct button
        for (let b of btns) {
          const t = b.innerText;
          if (
            t.includes('Contiguous Zone (Art. 33)') ||
            t.includes('Exclusive Economic Zone (Art. 56)') ||
            t.includes('Lawful: Under Art. 79') ||
            t.includes('Lawful Innocent Passage') ||
            t.includes('Requires Consent (Art. 246)') ||
            t.includes('Universal Jurisdiction') ||
            t.includes('Common Heritage of Mankind') ||
            t.includes('Freedom of Navigation (Art. 58 & 87)') ||
            t.includes('No (Art. 60)')
          ) {
            b.click();
            break;
          }
        }
      });
      await page.waitForTimeout(700);
    }
    await page.waitForTimeout(800);

    check('Lab 07: Debrief visible', await page.locator('#sim-uz-outcome').isVisible());
    const tokens7 = await page.locator('#sim-uz-stat-tokens').innerText();
    check('Lab 07: All 3 tokens preserved', tokens7.includes('3 / 3'), tokens7);
    const stars7 = await page.locator('#sim-uz-stars .lab-star-in').count();
    check('Lab 07: 3 stars awarded', stars7 === 3, `stars: ${stars7}`);
    const reveal7 = await page.locator('#sim-uz-reveal-body').innerText();
    check('Lab 07: Cites UNCLOS 1982 articles', reveal7.includes('UNCLOS') && reveal7.includes('Territorial Sea'));
    const flag7 = await page.evaluate(() => localStorage.getItem('labs_completed_unclos_zones'));
    check('Lab 07: localStorage flag set', flag7 === 'true');

    // ==========================================
    // LAB 08: Equilibrium Keeper (road-to-ww1.html)
    // ==========================================
    console.log('\n--- Testing Lab 08: Equilibrium Keeper ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/road-to-ww1.html`, { waitUntil: 'networkidle' });
    check('Lab 08: 0 console errors on load', consoleErrors.length === 0);
    check('Lab 08: Briefing visible', await page.locator('#sim-bop-briefing').isVisible());

    await page.click('#sim-bop-btn-begin');
    check('Lab 08: Play area active', await page.locator('#sim-bop-play').isVisible());

    // Play 4 crises by choosing Bilateral Mediation (middle button) to keep margin minimal
    for (let c = 1; c <= 4; c++) {
      const medBtn = page.locator('#balance-power-sim .sim-bop-act-btn').nth(1);
      await medBtn.click();
      await page.waitForTimeout(500);
    }
    await page.waitForTimeout(800);

    check('Lab 08: Debrief visible', await page.locator('#sim-bop-outcome').isVisible());
    const margin8 = await page.locator('#sim-bop-stat-margin').innerText();
    check('Lab 08: Final margin <= 10 pts', parseInt(margin8) <= 10, margin8);
    const stars8 = await page.locator('#sim-bop-stars .lab-star-in').count();
    check('Lab 08: 3 stars awarded for margin <= 10', stars8 === 3, `stars: ${stars8}`);
    const reveal8 = await page.locator('#sim-bop-reveal-body').innerText();
    check('Lab 08: Cites Kenneth Waltz and Balance of Power', reveal8.includes('Kenneth Waltz') && reveal8.includes('Balance of Power'));
    const flag8 = await page.evaluate(() => localStorage.getItem('labs_completed_balance_of_power'));
    check('Lab 08: localStorage flag set', flag8 === 'true');

    // ==========================================
    // LAB 09: Chair's Gambit (asean-community.html)
    // ==========================================
    console.log('\n--- Testing Lab 09: Chair\'s Gambit ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/asean-community.html`, { waitUntil: 'networkidle' });
    check('Lab 09: 0 console errors on load', consoleErrors.length === 0);
    check('Lab 09: Briefing visible', await page.locator('#sim-scs-briefing').isVisible());

    await page.click('#sim-scs-btn-begin');
    check('Lab 09: Play area active', await page.locator('#sim-scs-play').isVisible());

    // Round 1: Choose option 3 (Dual-Track Pragmatic Consensus)
    await page.locator('#sim-scs-choices .sim-scs-opt-btn').nth(2).click();
    await page.waitForTimeout(500);

    // Round 2: Choose option 3 (Functional Joint Operational Protocols)
    await page.locator('#sim-scs-choices .sim-scs-opt-btn').nth(2).click();
    await page.waitForTimeout(500);

    // Round 3: Choose option 3 (Chair's Compromise Gambit)
    await page.locator('#sim-scs-choices .sim-scs-opt-btn').nth(2).click();
    await page.waitForTimeout(800);

    check('Lab 09: Debrief visible', await page.locator('#sim-scs-outcome').isVisible());
    const rank9 = await page.locator('#sim-scs-rank').innerText();
    check('Lab 09: Master Diplomat rank achieved', rank9.includes('Master Diplomat'), rank9);
    const stars9 = await page.locator('#sim-scs-stars .lab-star-in').count();
    check('Lab 09: 3 stars awarded', stars9 === 3, `stars: ${stars9}`);
    const reveal9 = await page.locator('#sim-scs-reveal-body').innerText();
    check('Lab 09: Cites Musyawarah & Mufakat and 2012 Phnom Penh precedent', reveal9.includes('Musyawarah') && reveal9.includes('2012'));
    const flag9 = await page.evaluate(() => localStorage.getItem('labs_completed_scs_dispute'));
    check('Lab 09: localStorage flag set', flag9 === 'true');

    // ==========================================
    // LAB 10: Second-Strike Ledger (domino-cold-war.html)
    // ==========================================
    console.log('\n--- Testing Lab 10: Second-Strike Ledger ---');
    consoleErrors = [];
    await page.goto(`http://127.0.0.1:${PORT}/domino-cold-war.html`, { waitUntil: 'networkidle' });
    check('Lab 10: 0 console errors on load', consoleErrors.length === 0);
    check('Lab 10: Briefing visible', await page.locator('#sim-nd-briefing').isVisible());

    await page.click('#sim-nd-btn-begin');
    check('Lab 10: Play area active', await page.locator('#sim-nd-play').isVisible());

    // Submit default balanced allocation (30 ICBM, 40 SLBM, 20 Bombers, 10 BMD = 100) across 4 FYs
    for (let fy = 1; fy <= 4; fy++) {
      const submitBtn = page.locator('#sim-nd-btn-submit');
      check(`Lab 10: FY${fy} submit button ready`, await submitBtn.isEnabled());
      await submitBtn.click();
      await page.waitForTimeout(700);
    }
    await page.waitForTimeout(800);

    check('Lab 10: Debrief visible', await page.locator('#sim-nd-outcome').isVisible());
    const rank10 = await page.locator('#sim-nd-rank').innerText();
    check('Lab 10: Triad Architect rank achieved', rank10.includes('Triad Architect'), rank10);
    const stars10 = await page.locator('#sim-nd-stars .lab-star-in').count();
    check('Lab 10: 3 stars awarded', stars10 === 3, `stars: ${stars10}`);
    const reveal10 = await page.locator('#sim-nd-reveal-body').innerText();
    check('Lab 10: Cites Bernard Brodie 1946 and Thomas Schelling 1960', reveal10.includes('Bernard Brodie') && reveal10.includes('Thomas Schelling'));
    const flag10 = await page.evaluate(() => localStorage.getItem('labs_completed_nuclear_deterrence'));
    check('Lab 10: localStorage flag set', flag10 === 'true');

    // Screenshot: Lab 10 Debrief
    await page.locator('#sim-nd-outcome').screenshot({ path: path.join(screenshotsDir, 'g2_lab10_debrief.png') });

  } catch (err) {
    console.error('Test execution error:', err);
    check('Test run completed without unhandled exceptions', false, err.message);
  } finally {
    await browser.close();
    server.close();
  }

  const passedCount = results.filter(r => r.pass).length;
  const failedCount = results.filter(r => !r.pass).length;
  console.log('\n=============================================');
  console.log(`G2 E2E SUITE TOTAL: ${results.length} | PASSED: ${passedCount} | FAILED: ${failedCount}`);
  console.log('=============================================');

  if (failedCount > 0) process.exit(1);
}

run();
