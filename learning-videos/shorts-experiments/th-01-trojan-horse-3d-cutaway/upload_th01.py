import os
import sys
import time
from playwright.sync_api import sync_playwright

def upload_th01():
    video_path = os.path.abspath("D:/PERSONAL PROJECT/IR-study-companion/learning-videos/exports/TH01_Trojan_Horse_3D_Cutaway_Short_1080p.mp4")
    assert os.path.exists(video_path), f"Video missing: {video_path}"

    title = "How 30 Men Actually Survived Inside the Trojan Horse #Shorts"
    description = (
        "How did 30 Greek soldiers survive inside the Trojan Horse in 35°C heat without suffocating before Troy burned? 3D tactical cutaway simulation.\n\n"
        "Study the full history & international relations curriculum at: https://ir-guide.netlify.app/\n\n"
        "#TrojanHorse #AncientHistory #MilitaryHistory #Shorts #GreekMythology #Geopolitics #Troy"
    )

    print("========================================================")
    print("🚀 STARTING AUTOMATED UPLOAD TO YOUTUBE STUDIO: TH-01")
    print("Video File:", video_path)
    print("Title:", title)
    print("========================================================")

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = None
        for pg in context.pages:
            if "studio.youtube.com" in pg.url:
                page = pg
                break
        
        if not page:
            print("Opening new tab for studio.youtube.com...")
            page = context.new_page()
            page.goto("https://studio.youtube.com/", wait_until="domcontentloaded")
            time.sleep(4)
        else:
            print("Found existing YouTube Studio tab. Bringing to front...")
            page.bring_to_front()
            time.sleep(2)

        # 1. Verify Channel Name with retry loop
        print("Verifying channel...")
        ch_text = ""
        for _ in range(6):
            try:
                ch_text = page.evaluate('() => document.querySelector("#entity-name, ytcp-entity-header h1, #channel-title")?.innerText || ""')
                if ch_text:
                    break
            except Exception:
                time.sleep(1.5)

        print(f"Detected Channel: '{ch_text}'")
        assert "international relations" in ch_text.lower() or "ir" in ch_text.lower() or "nutshell" in ch_text.lower(), f"Wrong channel detected: '{ch_text}'"

        # 2. Trigger Upload Modal
        print("Triggering upload modal...")
        upload_item = page.locator('tp-yt-paper-item:has-text("Upload videos"), #text-item-0').first
        if not upload_item.is_visible():
            create_btn = page.locator('button:has-text("Create")').first
            create_btn.click()
            time.sleep(1.5)
            upload_item = page.locator('tp-yt-paper-item:has-text("Upload videos"), #text-item-0').first
        
        upload_item.click()
        time.sleep(3)

        # 3. Feed Video File via Native CDP
        print("Feeding video file via native CDP DOM.setFileInputFiles...")
        cdp = context.new_cdp_session(page)
        doc = cdp.send("DOM.getDocument")
        node = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": 'input[name="Filedata"]'})
        cdp.send("DOM.setFileInputFiles", {"files": [video_path], "nodeId": node["nodeId"]})
        print("Video file transferred to upload modal. Waiting for initial processing...")
        time.sleep(8)

        # 4. Fill Title
        print("Filling Title...")
        title_el = page.locator('#title-textarea #textbox, #textbox[aria-label*="title" i]').first
        title_el.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        title_el.fill(title)
        page.keyboard.press("Escape")  # Dismiss hashtag autocomplete
        time.sleep(1.5)

        # 5. Fill Description
        print("Filling Description...")
        desc_el = page.locator('#description-textarea #textbox, #textbox[aria-label*="description" i]').first
        desc_el.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        desc_el.fill(description)
        page.keyboard.press("Escape")  # Dismiss autocomplete
        time.sleep(1.5)

        # 6. Set Audience: Not for kids
        print("Setting audience: Not for kids...")
        not_for_kids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first
        if not_for_kids.is_visible() and not not_for_kids.is_checked():
            not_for_kids.click()
            time.sleep(1)

        # 7. MANDATORY ADVANCE AI / ALTERED CONTENT DISCLOSURE (YES)
        print("Configuring Altered / Synthetic AI Content disclosure: YES...")
        toggle = page.locator('#toggle-button, ytcp-button#toggle-button').first
        if toggle.is_visible():
            toggle.click()
            time.sleep(2)
        
        # Click YES for altered content
        ai_radio = page.locator('tp-yt-paper-radio-button[name="VIDEO_HAS_ALTERED_CONTENT_YES"]').first
        if ai_radio.is_visible():
            ai_radio.click()
        else:
            page.evaluate('''() => {
                const r = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_HAS_ALTERED_CONTENT_YES"]');
                if (r) r.click();
            }''')
        print("Altered Content set to YES successfully!")
        time.sleep(2)

        # 8. Step through Next buttons
        print("Stepping through Next buttons...")
        for step in range(3):
            page.evaluate("() => document.querySelector('#next-button')?.click()")
            print(f"Clicked Next ({step+1}/3)")
            time.sleep(2.5)

        # 9. Set Visibility to PUBLIC and Publish
        print("Setting visibility to PUBLIC...")
        page.evaluate('''() => {
            const pub = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (pub) pub.click();
        }''')
        time.sleep(2)

        print("Publishing video...")
        page.evaluate('''() => {
            const done = document.querySelector('#done-button') || document.querySelector('#save-button');
            if (done) done.click();
        }''')
        print("Clicked Publish button! Waiting for dialog settlement...")
        time.sleep(12)

        # 10. Retrieve Published Video URL
        print("Retrieving published video URL...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short", wait_until="domcontentloaded")
        time.sleep(4)

        video_id = page.evaluate('''() => {
            const first = document.querySelector('ytcp-video-row a#thumbnail-anchor, ytcp-video-row a[href*="/video/"]');
            if (!first) return null;
            const m = first.href.match(/video\/([a-zA-Z0-9_-]+)/);
            return m ? m[1] : null;
        }''')

        if video_id:
            short_url = f"https://youtube.com/shorts/{video_id}"
            print("========================================================")
            print("🎉 UPLOAD SUCCESSFUL!")
            print("Video ID:", video_id)
            print("Shorts URL:", short_url)
            print("========================================================")
            return short_url
        else:
            print("Video published, but could not parse video_id automatically.")
            return None

if __name__ == "__main__":
    url = upload_th01()
    print("Done. URL:", url)
