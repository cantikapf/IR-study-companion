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
    browser = p.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    
    # Locate or open Studio page
    page = None
    for pg in context.pages:
        if "studio.youtube.com" in pg.url:
            page = pg
            break
    if not page:
        page = context.new_page()
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ", wait_until="domcontentloaded")
        page.wait_for_timeout(3000)

    print("Current page URL:", page.url)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(4000)
    
    # 1. Verify channel name
    ch_text = ""
    for _ in range(5):
        try:
            ch_text = page.evaluate('() => document.querySelector("#entity-name, ytcp-entity-header h1, #channel-title")?.innerText || ""')
            if ch_text:
                break
        except Exception:
            time.sleep(2)
    print("Channel detected:", ch_text)
    assert "International Relations in a nutshell" in ch_text, f"Wrong channel! {ch_text}"

    # 2. Open Create modal
    print("Clicking Create button...")
    create_btn = page.locator('button:has-text("Create")').first
    create_btn.click()
    page.wait_for_timeout(1000)

    upload_item = page.locator('tp-yt-paper-item:has-text("Upload videos"), ytcp-text-menu:has-text("Upload videos")').first
    upload_item.click()
    page.wait_for_timeout(3000)
    print("Upload dialog opened.")

    # 3. Bypass Playwright 50MB limit using Native CDP
    print("Feeding video file via native CDP...")
    cdp = context.new_cdp_session(page)
    doc = cdp.send("DOM.getDocument")
    node = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": 'input[name="Filedata"]'})
    cdp.send("DOM.setFileInputFiles", {"files": [VIDEO_PATH], "nodeId": node["nodeId"]})
    print("File passed to input element. Waiting for upload processing...")
    page.wait_for_timeout(7000)

    # 4. Fill Title
    print("Filling title...")
    title_el = page.locator('#title-textarea #textbox, #textbox[aria-label*="title" i]').first
    title_el.wait_for(state="visible", timeout=30000)
    title_el.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    title_el.fill(TITLE)
    page.wait_for_timeout(1000)

    # 5. Fill Description
    print("Filling description...")
    desc_el = page.locator('#description-textarea #textbox, #textbox[aria-label*="description" i]').first
    desc_el.wait_for(state="visible", timeout=10000)
    desc_el.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    desc_el.fill(DESCRIPTION)
    page.wait_for_timeout(1000)

    # 6. Audience: Not made for kids
    print("Setting audience...")
    not_for_kids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first
    if not_for_kids.is_visible():
        if not not_for_kids.is_checked():
            not_for_kids.click()
            print("Checked NOT MADE FOR KIDS.")
    else:
        page.evaluate('''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el) el.click();
        }''')
    page.wait_for_timeout(1000)

    # 7. Next buttons through Checks
    next_btn = page.locator("#next-button").first
    for step in range(3):
        print(f"Clicking Next (step {step+1})...")
        next_btn.click()
        page.wait_for_timeout(2000)

    # 8. Visibility: Public
    print("Setting visibility to PUBLIC...")
    public_radio = page.locator('tp-yt-paper-radio-button[name="PUBLIC"]').first
    if public_radio.is_visible():
        public_radio.click()
    else:
        page.evaluate('''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (el) el.click();
        }''')
    page.wait_for_timeout(2000)

    # 9. Click Publish / Done
    print("Clicking Publish/Done...")
    done_btn = page.locator('#done-button, button:has-text("Publish")').first
    done_btn.click()
    page.wait_for_timeout(8000)

    # 10. Extract video ID / URL
    print("Navigating to shorts content list to retrieve video ID...")
    page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short", wait_until="domcontentloaded")
    page.wait_for_timeout(5000)

    video_info = page.evaluate('''() => {
        const row = document.querySelector('ytcp-video-row');
        if (!row) return null;
        const link = row.querySelector('a#thumbnail-anchor, a[href*="/video/"]');
        const title = row.querySelector('#video-title, #title')?.innerText || "";
        const href = link ? link.href : "";
        const m = href.match(/video\\/([a-zA-Z0-9_-]+)/);
        return {
            title: title.trim(),
            href: href,
            videoId: m ? m[1] : null
        };
    }''')
    print("Published Video Info:", video_info)

    if video_info and video_info.get("videoId"):
        vid_id = video_info["videoId"]
        print(f"SUCCESS! Published Shorts URL: https://youtube.com/shorts/{vid_id}")
    else:
        print("Upload initiated, but video ID not immediately parsed from first row.")
