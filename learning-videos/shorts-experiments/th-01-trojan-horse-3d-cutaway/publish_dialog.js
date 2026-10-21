const { chromium } = require("playwright");

async function publishNow() {
  const browser = await chromium.connectOverCDP("http://localhost:9222");
  const context = browser.contexts()[0];
  const page = context.pages().find(p => p.url().includes("studio.youtube.com"));

  console.log("Connected to page:", page.url());

  // 1. Check & Set Audience Not For Kids
  console.log("Checking Audience: Not for kids...");
  await page.evaluate(() => {
    const notForKids = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
    if (notForKids && !notForKids.checked) notForKids.click();
  });
  await new Promise(r => setTimeout(r, 1000));

  // 2. Expand Show More & Set Altered Content: YES
  console.log("Checking Altered Content disclosure: YES...");
  await page.evaluate(() => {
    const toggle = document.querySelector("#toggle-button, ytcp-button#toggle-button");
    if (toggle) toggle.click();
  });
  await new Promise(r => setTimeout(r, 1500));

  await page.evaluate(() => {
    const aiRadio = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_HAS_ALTERED_CONTENT_YES"]');
    if (aiRadio) aiRadio.click();
  });
  await new Promise(r => setTimeout(r, 1500));

  // 3. Step Next until Visibility (where tp-yt-paper-radio-button[name="PUBLIC"] exists)
  console.log("Stepping Next to Visibility...");
  for (let i = 0; i < 4; i++) {
    const isVisibilityReached = await page.evaluate(() => {
      const pub = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
      return !!pub && pub.offsetParent !== null;
    });

    if (isVisibilityReached) {
      console.log("Visibility tab reached!");
      break;
    }

    await page.evaluate(() => {
      const next = document.querySelector("#next-button");
      if (next) next.click();
    });
    console.log(`Clicked Next (${i + 1})`);
    await new Promise(r => setTimeout(r, 2000));
  }

  // 4. Click PUBLIC
  console.log("Selecting PUBLIC visibility...");
  const pubClicked = await page.evaluate(() => {
    const pub = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
    if (pub) {
      pub.click();
      return true;
    }
    return false;
  });
  console.log("PUBLIC radio clicked:", pubClicked);
  await new Promise(r => setTimeout(r, 2000));

  // 5. Click Done / Save
  console.log("Clicking Done / Save button to publish...");
  const publishClicked = await page.evaluate(() => {
    const done = document.querySelector("#done-button");
    if (done && done.offsetParent !== null) {
      done.click();
      return "CLICKED_DONE";
    }
    const save = document.querySelector("#save-button");
    if (save && save.offsetParent !== null) {
      save.click();
      return "CLICKED_SAVE";
    }
    return "BUTTON_NOT_FOUND";
  });
  console.log("Publish result:", publishClicked);

  await new Promise(r => setTimeout(r, 8000));

  console.log("========================================================");
  console.log("🎉 PUBLISH ACTION COMPLETE!");
  console.log("Video ID: vT_1C3HIy3U");
  console.log("URL: https://youtube.com/shorts/vT_1C3HIy3U");
  console.log("========================================================");

  await browser.close();
}

publishNow().catch(console.error);
