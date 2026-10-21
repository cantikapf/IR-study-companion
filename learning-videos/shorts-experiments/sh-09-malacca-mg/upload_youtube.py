import os, time
from playwright.sync_api import sync_playwright

VIDEO_PATH = r"D:\PERSONAL PROJECT\IR-study-companion\learning-videos\shorts-experiments\sh-09-malacca-mg\renders\sh09_malacca_master_1080p.mp4"
TITLE = "Why 1.5 Miles of Water Controls Global Trade | Malacca Chokepoint #Shorts"
DESCRIPTION = """Two landmasses. One narrow channel. Over twenty-five percent of global commerce and oil passes through the 1.5-mile gap of the Malacca Strait.

If this bottleneck closes, supertankers face massive detours through Sunda or Lombok. You cannot widen a strait.

#geopolitics #malacca #internationalrelations #maritime #history #shipping #supplychain #IRinANutshell #Shorts"""

def main():
    video_abs_path = os.path.abspath(VIDEO_PATH)
    assert os.path.exists(video_abs_path), f"Video missing: {video_abs_path}"

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = None
        for pg in context.pages:
            if "studio.youtube.com" in pg.url:
                page = pg
                break
        if not page:
            page = context.new_page()
            page.goto("https://studio.youtube.com/", wait_until="domcontentloaded")
            time.sleep(4)

        # Guarded channel verification
        ch_text = ""
        for _ in range(5):
            try:
                ch_text = page.evaluate('() => document.querySelector("#entity-name, ytcp-entity-header h1, #channel-title")?.innerText || ""')
                if ch_text: break
            except Exception:
                time.sleep(1.5)
        print("Verified Channel:", ch_text)
        assert "international relations in a nutshell" in ch_text.lower(), f"Unexpected channel: {ch_text}"

        # 1. Trigger Upload Modal
        create_btn = page.locator('button:has-text("Create"), #create-icon').first
        create_btn.click()
        time.sleep(1.5)

        upload_item = page.locator('tp-yt-paper-item:has-text("Upload videos"), #text-item-0').first
        upload_item.click()
        time.sleep(3)

        # 2. Native CDP File Selection (bypasses 50MB limit)
        cdp = context.new_cdp_session(page)
        doc = cdp.send("DOM.getDocument")
        node = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": 'input[name="Filedata"]'})
        cdp.send("DOM.setFileInputFiles", {"files": [video_abs_path], "nodeId": node["nodeId"]})
        print("Fed file via CDP, waiting for upload dialog...")
        time.sleep(6)

        # 3. Fill Title
        print("Filling Title & Description...")
        title_box = page.locator('#title-textarea #textbox, #textbox[aria-label*="title" i]').first
        title_box.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        title_box.fill(TITLE)

        # 4. Fill Description
        desc_box = page.locator('#description-textarea #textbox, #textbox[aria-label*="description" i]').first
        desc_box.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        desc_box.fill(DESCRIPTION)

        # 5. Set Audience: Not for kids
        time.sleep(2)
        not_for_kids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first
        if not_for_kids.is_visible() and not not_for_kids.is_checked():
            not_for_kids.click()
            time.sleep(1)

        # 6. Click Next until Visibility tab
        print("Navigating through wizard...")
        next_btn = page.locator("#next-button").first
        for step in range(3):
            next_btn.click()
            time.sleep(2)

        # 7. Select Public and Publish
        print("Selecting Public visibility...")
        public_radio = page.locator('tp-yt-paper-radio-button[name="PUBLIC"]').first
        if public_radio.is_visible() and not public_radio.is_checked():
            public_radio.click()
            time.sleep(1.5)

        done_btn = page.locator('#done-button, button:has-text("Publish")').first
        print("Clicking Publish...")
        done_btn.click()
        time.sleep(6)

        # 8. Check uploaded videos to grab ID
        print("Navigating to shorts list to verify ID...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short", wait_until="domcontentloaded")
        time.sleep(4)
        video_id = page.evaluate('''() => {
            const first = document.querySelector('ytcp-video-row a#thumbnail-anchor, ytcp-video-row a[href*="/video/"]');
            if (!first) return null;
            const m = first.href.match(/video\\/([a-zA-Z0-9_-]+)/);
            return m ? m[1] : null;
        }''')
        print("UPLOADED_VIDEO_ID:", video_id)

if __name__ == "__main__":
    main()
