
const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: true});
  const p = await b.newPage({viewport: {width: 540, height: 960}});
  const u = 'file:///' + path.join(__dirname, 'compositions', 'index.html').split(path.sep).join('/');
  await p.goto(u, {waitUntil: 'networkidle'});
  await p.evaluate(() => window.updateCaptions(2.5));
  const t = await p.evaluate(() => document.getElementById('subSentence').innerText);
  const op = await p.evaluate(() => getComputedStyle(document.getElementById('subtitlesWrap')).opacity);
  console.log('t=2.5s caption:', t, 'op:', op);
  await b.close();
})();
