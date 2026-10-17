import os
import sys
import time
from playwright.sync_api import sync_playwright

VIDEO_PATH = r"D:\PERSONAL PROJECT\IR-study-companion\learning-videos\exports\SP05_Bretton_Woods_Soviet_Spy_Short_1080p.mp4"
TITLE = "The Soviet Spy Who Built the Global Economy #shorts"
DESCRIPTION = """In 1944 at Bretton Woods, two men designed the modern capitalist financial system: John Maynard Keynes and Harry Dexter White.

White outmaneuvered the British Empire, crowned the US Dollar world reserve currency, and created the IMF. 

What Washington didn't discover until the Venona decrypts was that White had a Soviet code name: "Jurist". 

Learn the full history of the Bretton Woods conference and postwar monetary order in our free interactive curriculum:
👉 https://cantikapf.github.io/IR-study-companion/chapters/012-modern-world-history/110-bretton-woods/

#History #ColdWar #Geopolitics #Economy #IMF #BrettonWoods #Espionage #SovietUnion #Shorts"""

assert os.path.exists(VIDEO_PATH), f"Video not found: {VIDEO_PATH}"
file_size_mb = os.path.getsize(VIDEO_PATH) / (1024 * 1024)
print(f"Target video: {VIDEO_PATH} ({file_size_mb:.2f} MB)")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    context = browser.contexts[0]
    page = [pg for pg in context.pages if "studio.youtube.com" in pg.url][0]
    print("Page URL:", page.url)

    # 1. Click 'Upload videos' from open dropdown or open create first
    upload_item = page.locator('tp-yt-paper-item:has-text("Upload videos"), #text-item-0').first
    if not upload_item.is_visible():
        print("Clicking Create button...")
        page.locator('button:has-text("Create")').first.click()
        time.sleep(1.5)
    
    print("Clicking Upload videos...")
    upload_item.click()
    time.sleep(3)

    # 2. Feed file via CDP
    print("Feeding file via native CDP...")
    cdp = context.new_cdp_session(page)
    doc = cdp.send("DOM.getDocument")
    node = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": 'input[name="Filedata"]'})
    cdp.send("DOM.setFileInputFiles", {"files": [VIDEO_PATH], "nodeId": node["nodeId"]})
    print("File passed to Filedata input. Waiting for details form...")
    time.sleep(6)

    # 3. Fill Title
    print("Filling title...")
    title_box = page.locator('#title-textarea #textbox, ytcp-social-suggestions-textbox[aria-label*="title" i] #textbox, #textbox[aria-label*="title" i]').first
    title_box.wait_for(state="visible", timeout=20000)
    title_box.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    title_box.fill(TITLE)
    time.sleep(1)

    # 4. Fill Description
    print("Filling description...")
    desc_box = page.locator('#description-textarea #textbox, ytcp-social-suggestions-textbox[aria-label*="description" i] #textbox, #textbox[aria-label*="description" i]').first
    if desc_box.is_visible():
        desc_box.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        desc_box.fill(DESCRIPTION)
        time.sleep(1)

    # 5. Audience
    print("Checking Audience...")
    not_for_kids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first
    if not_for_kids.is_visible():
        not_for_kids.click()
    else:
        page.evaluate('''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el) el.click();
        }''')
    time.sleep(1)

    # 6. Step Next 3 times
    next_btn = page.locator('#next-button').first
    for i in range(3):
        print(f"Clicking Next step {i+1}...")
        next_btn.click()
        time.sleep(2)

    # 7. Visibility Public
    print("Setting visibility to PUBLIC...")
    public_radio = page.locator('tp-yt-paper-radio-button[name="PUBLIC"]').first
    if public_radio.is_visible():
        public_radio.click()
    else:
        page.evaluate('''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (el) el.click();
        }''')
    time.sleep(2)

    # 8. Click Publish / Done
    print("Clicking Publish/Done...")
    done_btn = page.locator('#done-button, button:has-text("Publish")').first
    done_btn.click()
    time.sleep(8)
    page.screenshot(path='C:/Users/xiyeo/AppData/Local/hermes/cache/scratch/after_publish_click.png')
    print("After publish screenshot saved.")

    # 9. Extract video ID / URL
    print("Navigating to shorts content tab to grab video ID...")
    page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short", wait_until="domcontentloaded")
    time.sleep(5)

    video_info = page.evaluate('''() => {
        const rows = Array.from(document.querySelectorAll('ytcp-video-row'));
        for (const row of rows) {
            const link = row.querySelector('a#thumbnail-anchor, a[href*="/video/"]');
            const title = row.querySelector('#video-title, #title')?.innerText || "";
            const href = link ? link.href : "";
            const m = href.match(/video\\/([a-zA-Z0-9_-]+)/);
            if (m) {
                return {
                    title: title.trim(),
                    videoId: m[1]
                };
            }
        }
        return null;
    }''')
    print("Published Video Info:", video_info)

    if video_info and video_info.get("videoId"):
        vid_id = video_info["videoId"]
        print(f"SUCCESS! Published Shorts URL: https://youtube.com/shorts/{vid_id}")
    else:
        print("Upload initiated, but video ID not immediately parsed from first row.")
