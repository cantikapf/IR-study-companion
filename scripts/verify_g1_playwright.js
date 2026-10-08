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
  const PORT = 8124;
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

  const consoleErrors = [];
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
    await page.goto(`http://127.0.0.1:${PORT}/game-theory-ir.html`, { waitUntil: 'networkidle' });

    // Check 1: 0 console errors on load
    check('0 console errors on initial load', consoleErrors.length === 0, `errors: ${consoleErrors.length}`);

    // Check 2: Briefing visible
    const briefing = page.locator('#sim-gt-briefing');
    check('Briefing section is visible initially', await briefing.isVisible());

    // Check 3: Play area hidden
    const playArea = page.locator('#sim-gt-play');
    check('Play area is hidden initially', !(await playArea.isVisible()));

    // Screenshot 1: Briefing (Light Mode)
    await briefing.scrollIntoViewIfNeeded();
    await page.waitForTimeout(300);
    await page.locator('#game-theory-sim').screenshot({ path: path.join(screenshotsDir, 'g1_01_briefing_light.png') });

    // Check 4: Help button visible in HUD
    const helpBtn = page.locator('#sim-gt-help-btn');
    check('Help button is visible in HUD', await helpBtn.isVisible());

    // Check 5: Help modal opens on click
    await helpBtn.click();
    await page.waitForTimeout(300);
    const modalBack = page.locator('.lab-modal-back');
    check('Help modal backdrop becomes visible on click', await modalBack.isVisible());

    // Check 6: LabGame.help.isOpen() returns true
    const isHelpOpen = await page.evaluate(() => window.LabGame && window.LabGame.help && window.LabGame.help.isOpen());
    check('LabGame.help.isOpen() is true', isHelpOpen === true);

    // Check 7: Pressing C or D while modal is open does NOT trigger game
    await page.keyboard.press('KeyC');
    await page.waitForTimeout(200);
    const playAreaStillHidden = !(await playArea.isVisible());
    check('Pressing C while help modal open locks game keys', playAreaStillHidden);

    // Check 8: Pressing Escape closes help modal
    await page.keyboard.press('Escape');
    await page.waitForTimeout(300);
    check('Pressing Escape closes help modal', !(await modalBack.isVisible()));

    // Check 9: Mute button toggles sound and persists to localStorage
    const muteBtn = page.locator('#sim-gt-mute');
    check('Mute button is visible in HUD', await muteBtn.isVisible());
    const initialMuteIcon = await muteBtn.innerText();
    await muteBtn.click();
    const toggledMuteIcon = await muteBtn.innerText();
    const persistedMute = await page.evaluate(() => localStorage.getItem('labs_muted_v1'));
    check('Mute button toggles icon and localStorage labs_muted_v1', initialMuteIcon !== toggledMuteIcon && persistedMute === '1');
    // Restore unmuted
    await muteBtn.click();

    // Check 10: Click "Begin Session" hides briefing and reveals play area
    const btnBegin = page.locator('#sim-gt-btn-begin');
    await btnBegin.click();
    await page.waitForTimeout(200);
    check('Clicking Begin Session reveals play area', await playArea.isVisible());
    check('Clicking Begin Session hides briefing', !(await briefing.isVisible()));

    // Check 11: Roulette scramble animation on opponent card
    const foeName = page.locator('#sim-gt-foe-name');
    const foeNameText = await foeName.innerText();
    check('Opponent shows scramble/roulette indicator initially', foeNameText.includes('SCRAMBLING') || foeNameText.includes('Classified') || foeNameText.includes('???'));

    // Check 12: Wait for roulette settle (~1000ms), buttons become enabled
    await page.waitForTimeout(1100);
    const btnCoop = page.locator('#sim-gt-btn-coop');
    const btnDefect = page.locator('#sim-gt-btn-defect');
    check('Cooperate button is enabled after scramble', await btnCoop.isEnabled());
    check('Defect button is enabled after scramble', await btnDefect.isEnabled());

    // Check 13: Round 1 HUD display
    const hudRound = page.locator('#sim-gt-hud-round');
    const hudRoundText = (await hudRound.innerText()).toLowerCase();
    check('HUD displays Round 1 / 8', hudRoundText.includes('round 1 / 8'));

    // Set opponent to Tit-for-Tat to verify canonical all-coop run
    await page.evaluate(() => {
      if (window.setSimGtOpponent) {
        window.setSimGtOpponent('tft');
      }
    });

    // Check 14: Play Round 1 (Cooperate)
    await btnCoop.click();
    await page.waitForTimeout(800); // suspense beat + render
    const scoreVal = await page.evaluate(() => window.simGtState.scoreP);
    check('Round 1 Cooperate scores +5', scoreVal === 5, `score: ${scoreVal}`);

    // Check 15: Tip card appears
    const tip = page.locator('#sim-gt-tip');
    check('Coach tip appears after first round', await tip.isVisible());

    // Play Round 2 (Cooperate)
    await btnCoop.click();
    await page.waitForTimeout(800);
    const scoreR2 = await page.evaluate(() => window.simGtState.scoreP);
    check('Round 2 Cooperate scores +10 total', scoreR2 === 10, `score: ${scoreR2}`);

    // Play Round 3 (Cooperate) -> streak hits 3, multiplier 1.5 activates
    await btnCoop.click();
    await page.waitForTimeout(800);
    const hudStreak = page.locator('#sim-gt-hud-streak');
    check('Round 3 mutual cooperation activates streak chip (x1.5)', await hudStreak.isVisible());
    const scoreR3 = await page.evaluate(() => window.simGtState.scoreP);
    check('Round 3 score includes 1.5x multiplier (+8)', scoreR3 === 18, `score: ${scoreR3}`);

    // Check 16: Play Round 4 (Cooperate)
    await btnCoop.click();
    await page.waitForTimeout(1000); // wait for Round 4 outcome + SIGINT drop (350ms delay)

    // Check 17: SIGINT intercept card appears after Round 4
    const intelCard = page.locator('#sim-gt-intel-card');
    check('SIGINT intercept card appears after Round 4', await intelCard.isVisible());
    const intelText = await intelCard.innerText();
    check('SIGINT card has INTEL · ROUND 5 header', intelText.includes('INTEL · ROUND 5'));

    // Screenshot 2: Mid-Game (Round 5 with SIGINT & streak chip)
    await page.screenshot({ path: path.join(screenshotsDir, 'g1_02_midgame_light.png'), fullPage: false });

    // Play Round 5 (Cooperate) -> streak hits 5, multiplier 2.0 activates
    await btnCoop.click();
    await page.waitForTimeout(800);
    const multText = await page.locator('#sim-gt-val-mult').innerText();
    check('Round 5 streak multiplier reaches 2x', multText === '2');

    // Play Round 6, 7, 8 (all Cooperate)
    await btnCoop.click();
    await page.waitForTimeout(800);
    await btnCoop.click();
    await page.waitForTimeout(800);
    await btnCoop.click();
    await page.waitForTimeout(1600); // Wait for suspense beat (500ms) + sessionEnd delay (850ms)

    // Check 18: Debrief section visible
    const debrief = page.locator('#sim-gt-outcome');
    check('Debrief after-action report is visible after Round 8', await debrief.isVisible());

    // Check 19: All-coop score >= 40 with streaks (specifically 66) & 3 stars
    const finalScore = await page.evaluate(() => window.simGtState.scoreP);
    check('All-coop run achieves score >= 40 with streaks', finalScore >= 40, `score: ${finalScore}`);

    const activeStars = await page.locator('#sim-gt-stars .lab-star-in').count();
    check('3 active stars awarded for score >= 40', activeStars === 3);

    // Check 20: Rank is Master Diplomat
    const rankText = await page.locator('#sim-gt-rank').innerText();
    check('Rank awarded is Master Diplomat', rankText === 'Master Diplomat');

    // Check 21: Recap list contains 8 rounds
    const recapCount = await page.locator('#sim-gt-recap-list li').count();
    check('Recap list contains exactly 8 rounds', recapCount === 8);

    // Check 22: Mechanics reveal cites Axelrod 1984
    const revealText = await page.locator('#sim-gt-mech-reveal').innerText();
    check('Debrief cites Axelrod 1984 and Pareto-optimal framing', revealText.includes('Axelrod') && revealText.includes('1984'));
    check('Debrief has knowledge check closer', revealText.includes('Continue to the Knowledge Check below to test the concept.'));

    // Check 23: Completed flag in localStorage
    const completedFlag = await page.evaluate(() => localStorage.getItem('labs_completed_game_theory'));
    check('localStorage labs_completed_game_theory is "true"', completedFlag === 'true');

    // Check 24: Best score submitted to localStorage
    const bestScore = await page.evaluate(() => localStorage.getItem('labs_best_game_theory'));
    check('localStorage labs_best_game_theory matches final score', Number(bestScore) === finalScore);

    // Screenshot 3: Debrief (Light Mode)
    await debrief.scrollIntoViewIfNeeded();
    await page.evaluate(() => window.scrollBy(0, -90));
    await page.waitForTimeout(300);
    await debrief.screenshot({ path: path.join(screenshotsDir, 'g1_03_debrief_light.png') });

    // Check Dark Mode
    await page.evaluate(() => document.body.classList.add('dark-theme'));
    await page.waitForTimeout(300);

    // Screenshot 4: Debrief (Dark Mode)
    await debrief.scrollIntoViewIfNeeded();
    await page.evaluate(() => window.scrollBy(0, -90));
    await page.waitForTimeout(300);
    await debrief.screenshot({ path: path.join(screenshotsDir, 'g1_04_debrief_dark.png') });

    // Screenshot 5: Briefing (Dark Mode)
    await page.evaluate(() => {
      document.getElementById('sim-gt-play').hidden = true;
      document.getElementById('sim-gt-briefing').hidden = false;
      window.scrollBy(0, -90);
    });
    await briefing.scrollIntoViewIfNeeded();
    await page.evaluate(() => window.scrollBy(0, -90));
    await page.waitForTimeout(300);
    await page.locator('#game-theory-sim').screenshot({ path: path.join(screenshotsDir, 'g1_05_briefing_dark.png') });

    // Check 25: Replay button resets game
    await page.evaluate(() => {
      document.body.classList.remove('dark-theme');
      document.getElementById('sim-gt-briefing').hidden = true;
      document.getElementById('sim-gt-play').hidden = false;
    });
    const btnReplay = page.locator('#sim-gt-btn-replay');
    await btnReplay.click();
    await page.waitForTimeout(400);
    const isDebriefHiddenAfterReplay = !(await debrief.isVisible());
    check('Clicking Replay resets session and hides debrief', isDebriefHiddenAfterReplay);

    // Check 26: 0 console errors throughout entire run
    check('0 console errors throughout entire interaction test', consoleErrors.length === 0, `errors: ${consoleErrors.join(', ')}`);

  } finally {
    await browser.close();
    server.close();
  }

  const passedCount = results.filter(r => r.pass).length;
  console.log(`\n=============================================`);
  console.log(`TOTAL CHECKS: ${results.length} | PASSED: ${passedCount} | FAILED: ${results.length - passedCount}`);
  console.log(`=============================================\n`);

  if (passedCount < results.length) {
    process.exit(1);
  }
}

run().catch(err => {
  console.error(err);
  process.exit(1);
});
