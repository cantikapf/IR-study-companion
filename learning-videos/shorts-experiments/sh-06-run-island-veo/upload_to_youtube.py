import os
import sys
import time
from playwright.sync_api import sync_playwright

VIDEO_PATH = r"D:\PERSONAL PROJECT\IR-study-companion\learning-videos\exports\SH06_The_Island_Traded_for_New_York_Short_1080p.mp4"
TITLE = "The 1 Island Britain Traded for New York #shorts"
DESCRIPTION = """In 1667, the British Empire gave away Manhattan to the Dutch. In exchange, they got a 3-kilometer speck of land in Indonesia called Pulau Run.

Why? Because in the 17th century, Pulau Run was the only place on Earth where nutmeg grew—a spice worth more than its weight in gold. 

Under the Treaty of Breda, the Dutch secured their global spice monopoly, while Britain walked away with New Netherland (renamed New York). Today, Manhattan is the financial capital of the world worth trillions, and Pulau Run is a quiet fishing village of 1,500 people.

Explore our free interactive International Relations & History curriculum:
👉 https://cantikapf.github.io/IR-study-companion/

#History #Geopolitics #NewYork #Manhattan #Indonesia #BandaIslands #TreatyOfBreda #DutchEastIndiaCompany #VOC #Shorts"""

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
        time.sleep(3)

    print("Current page URL:", page.url)
    page.wait_for_load_state("domcontentloaded")
    time.sleep(3)
    
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
    time.sleep(1.5)

    upload_item = page.locator('tp-yt-paper-item:has-text("Upload videos"), #text-item-0').first
    if not upload_item.is_visible():
        create_btn.click()
        time.sleep(1.5)
    upload_item.click()
    time.sleep(3)

    # 3. Feed video via Native CDP
    print("Selecting video file via CDP...")
    cdp = context.new_cdp_session(page)
    doc = cdp.send("DOM.getDocument")
    node = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": 'input[name="Filedata"]'})
    cdp.send("DOM.setFileInputFiles", {"files": [VIDEO_PATH], "nodeId": node["nodeId"]})
    print("File selected. Waiting for upload dialog initialization...")
    time.sleep(8)

    # 4. Fill Title & Description
    print("Filling Title & Description...")
    title_box = page.locator('#title-textarea #textbox, #textbox[aria-label*="title" i]').first
    title_box.wait_for(state="visible", timeout=30000)
    title_box.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    title_box.fill(TITLE)
    time.sleep(1)

    desc_box = page.locator('#description-textarea #textbox, #textbox[aria-label*="description" i]').first
    desc_box.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    desc_box.fill(DESCRIPTION)
    time.sleep(1)

    # 5. Set Audience (Not for kids)
    print("Setting audience...")
    not_for_kids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first
    if not_for_kids.is_visible() and not not_for_kids.is_checked():
        not_for_kids.click()
    time.sleep(1)

    # 6. Step Next through Video elements, Checks, Visibility
    print("Navigating through wizard...")
    next_btn = page.locator("#next-button").first
    for step in range(3):
        next_btn.click()
        time.sleep(2)

    # 7. Visibility -> Public
    print("Setting visibility to Public...")
    public_radio = page.locator('tp-yt-paper-radio-button[name="PUBLIC"]').first
    if public_radio.is_visible() and not public_radio.is_checked():
        public_radio.click()
    time.sleep(2)

    # 8. Publish
    print("Publishing video...")
    publish_btn = page.locator('#done-button, button:has-text("Publish")').first
    publish_btn.click()
    print("Publish button clicked! Waiting 10s for upload to settle...")
    time.sleep(10)

    # 9. Get Video URL / ID
    try:
        dialog_link = page.locator('a.ytcp-video-info, a[href*="youtu.be"]').first
        if dialog_link.is_visible():
            print("Video Link from Dialog:", dialog_link.get_attribute("href"))
    except Exception as e:
        print("Note on dialog link:", e)

    print("Checking Shorts list in channel...")
    page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short", wait_until="domcontentloaded")
    time.sleep(5)
    
    video_id = page.evaluate('''() => {
        const first = document.querySelector('ytcp-video-row a#thumbnail-anchor, ytcp-video-row a[href*="/video/"]');
        if (!first) return null;
        const m = first.href.match(/video\/([a-zA-Z0-9_-]+)/);
        return m ? m[1] : null;
    }''')
    print(f"LATEST SHORTS VIDEO ID: {video_id}")
    if video_id:
        print(f"SHORTS PUBLIC URL: https://youtube.com/shorts/{video_id}")
