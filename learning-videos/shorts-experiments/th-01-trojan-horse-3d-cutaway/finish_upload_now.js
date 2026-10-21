const { chromium } = require("playwright");

async function finishUpload() {
  const browser = await chromium.connectOverCDP("http://localhost:9222");
  const context = browser.contexts()[0];
  const page = context.pages().find(p => p.url().includes("studio.youtube.com"));

  if (!page) {
    console.error("No Studio page found");
    return;
  }

  console.log("Found Studio page:", page.url());

  // Step 1: Check if dialog is open, or click Edit draft
  const hasDialog = await page.evaluate(() => {
    const d = document.querySelector("ytcp-uploads-dialog");
    return !!(d && d.offsetParent !== null);
  });

  if (!hasDialog) {
    console.log("Clicking Edit draft button...");
    await page.evaluate(() => {
      const row = document.querySelector("ytcp-video-row");
      const btn = row ? row.querySelector("button[aria-label=\"Edit draft\"]") : null;
      if (btn) btn.click();
    });
    await new Promise(r => setTimeout(r, 4000));
  } else {
    console.log("Upload dialog is already open!");
  }

  // Step 2: Fill Description
  console.log("Filling description...");
  const descText = "Inside this giant wooden horse outside Troy, thirty Greek soldiers were sealed alive in thirty-five-degree heat. How did they survive?\n\nBuilt from warship timber, the hollow belly held two cramped scaffolding tiers where warriors sat in absolute silence.\n\nAt midnight, Odysseus unlocked a spring-loaded trapdoor beneath the horse, dropping hemp ropes to the cobblestones below.\n\nThey opened the gates, ending a ten-year war in a single night.\n\nDiscover more untold ancient geopolitics on IR in a Nutshell.\nInteractive learning platform: https://ir-guide.netlify.app/\n\n#history #ancienthistory #trojanhorse #greece #militaryhistory #geopolitics #shorts";

  await page.evaluate((text) => {
    const el = document.querySelector("#description-textarea #textbox");
    if (el) {
      el.focus();
      document.execCommand("selectAll", false, null);
      document.execCommand("delete", false, null);
      document.execCommand("insertText", false, text);
    }
  }, descText);

  await page.keyboard.press("Escape");
  await new Promise(r => setTimeout(r, 1200));

  // Step 3: Audience Not For Kids
  console.log("Setting audience: Not for kids...");
  await page.evaluate(() => {
    const r = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
    if (r && !r.checked) r.click();
  });
  await new Promise(r => setTimeout(r, 1200));

  // Step 4: Altered Content: YES
  console.log("Configuring Altered Content: YES...");
  await page.evaluate(() => {
    const toggle = document.querySelector("#toggle-button, ytcp-button#toggle-button");
    if (toggle) toggle.click();
  });
  await new Promise(r => setTimeout(r, 1500));

  await page.evaluate(() => {
    const r = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_HAS_ALTERED_CONTENT_YES"]');
    if (r) r.click();
  });
  await new Promise(r => setTimeout(r, 1500));

  // Step 5: Next buttons
  console.log("Stepping Next...");
  for (let i = 0; i < 3; i++) {
    await page.evaluate(() => {
      const next = document.querySelector("#next-button");
      if (next) next.click();
    });
    console.log(`Clicked Next (${i + 1}/3)`);
    await new Promise(r => setTimeout(r, 2000));
  }

  // Step 6: Visibility Public
  console.log("Setting Visibility: Public...");
  await page.evaluate(() => {
    const pub = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
    if (pub) pub.click();
  });
  await new Promise(r => setTimeout(r, 1500));

  // Step 7: Done / Publish
  console.log("Clicking Publish button...");
  const pubResult = await page.evaluate(() => {
    const done = document.querySelector("#done-button");
    if (done) { done.click(); return "DONE"; }
    const save = document.querySelector("#save-button");
    if (save) { save.click(); return "SAVE"; }
    return "NONE";
  });
  console.log("Publish result:", pubResult);

  await new Promise(r => setTimeout(r, 8000));

  // Step 8: Read Video URL
  const videoUrl = await page.evaluate(() => {
    const a = document.querySelector("a.ytcp-video-info, a[href*='youtu.be/'], a[href*='/shorts/']");
    return a ? a.href : null;
  });

  console.log("Published Video Link:", videoUrl);
  await browser.close();
}

finishUpload().catch(console.error);
