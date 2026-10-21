import os
import sys
import time
from playwright.sync_api import sync_playwright

VIDEO_PATH = r"D:\PERSONAL PROJECT\IR-study-companion\learning-videos\exports\SP06_Operation_Paul_Bunyan_Short_1080p.mp4"
TITLE = "The Deadliest Tree Trimming in History: Operation Paul Bunyan (1976) #Shorts"
DESCRIPTION = """In 1976, the United States deployed an entire war armada... just to cut down a single tree.

After North Korean soldiers killed two American officers attempting to trim a poplar tree blocking the DMZ view, Washington launched Operation Paul Bunyan: 813 combat troops, 27 helicopters, B-52 bombers, fighter jets, and an aircraft carrier battle group.

In 42 minutes, the tree was gone. Zero bullets fired.

Discover more untold geopolitical history on IR in a Nutshell.
Explore structured study guides: https://ir-guide.netlify.app/

#coldwar #historyfacts #koreanwar #dmz #militaryhistory #internationalrelations #shorts"""

def upload():
    video_abs_path = os.path.abspath(VIDEO_PATH)
    assert os.path.exists(video_abs_path), f"Video missing: {video_abs_path}"
    file_size_mb = os.path.getsize(video_abs_path) / (1024 * 1024)
    print(f"Uploading: {video_abs_path} ({file_size_mb:.2f} MB)")

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
            page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ", wait_until="domcontentloaded")
            time.sleep(3)

        print("Studio URL:", page.url)
        time.sleep(4)

        # 1. Verify Channel Name (bounded retry loop per skill)
        ch_text = ""
        for attempt in range(6):
            try:
                ch_text = page.evaluate('() => document.querySelector("#entity-name, ytcp-entity-header h1, #channel-title")?.innerText || ""')
                if ch_text:
                    break
            except Exception:
                time.sleep(2)
        print("Channel detected:", ch_text)
        assert "International Relations in a nutshell" in ch_text, f"Wrong channel: {ch_text}"

        # 2. Trigger Upload Modal (skill standard)
        print("Triggering Create -> Upload videos...")
        create_btn = page.locator('button[aria-label="Create"], button:has-text("Create")').first
        if not create_btn.is_visible():
            page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ", wait_until="domcontentloaded")
            time.sleep(4)
            create_btn = page.locator('button[aria-label="Create"], button:has-text("Create")').first
            
        create_btn.click()
        page.wait_for_timeout(1500)
        
        upload_item = page.locator('tp-yt-paper-item:has-text("Upload videos"), #text-item-0').first
        upload_item.click()
        page.wait_for_timeout(3000)
        print("Upload dialog opened.")

        # 3. Feed Video File via Native CDP
        print("Feeding video file via native CDP...")
        cdp = context.new_cdp_session(page)
        doc = cdp.send("DOM.getDocument")
        node = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": 'input[name="Filedata"]'})
        cdp.send("DOM.setFileInputFiles", {"files": [video_abs_path], "nodeId": node["nodeId"]})
        print("File submitted to input element. Waiting for upload processing...")
        page.wait_for_timeout(8000)

        # 4. Fill Title
        print("Filling title...")
        title_el = page.locator('#title-textarea #textbox, #textbox[aria-label*="title" i]').first
        title_el.wait_for(state="visible", timeout=30000)
        title_el.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        title_el.fill(TITLE)
        page.wait_for_timeout(500)
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)

        # 5. Fill Description
        print("Filling description...")
        desc_el = page.locator('#description-textarea #textbox, #textbox[aria-label*="description" i]').first
        desc_el.wait_for(state="visible", timeout=10000)
        desc_el.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        desc_el.fill(DESCRIPTION)
        page.wait_for_timeout(500)
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)

        # 6. Audience: Not made for kids
        print("Setting audience: Not made for kids...")
        not_for_kids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first
        if not_for_kids.is_visible() and not not_for_kids.is_checked():
            not_for_kids.click()
            print("Checked NOT MADE FOR KIDS.")
        page.wait_for_timeout(1000)

        # 7. ADVANCED CONFIGURATION: AI / ALTERED CONTENT DISCLOSURE
        print("Configuring Advance AI / Altered Content disclosure...")
        toggle_btn = page.locator('#toggle-button, ytcp-button#toggle-button').first
        if toggle_btn.is_visible():
            toggle_btn.click()
            page.wait_for_timeout(1500)
            
        # Select 'Yes' on Altered / Synthetic Content radio
        ai_radio = page.locator('tp-yt-paper-radio-button[name="VIDEO_HAS_ALTERED_CONTENT_YES"]').first
        if ai_radio.is_visible():
            ai_radio.click()
            print("Selected: VIDEO_HAS_ALTERED_CONTENT_YES (AI Altered Content = Yes)")
        else:
            # Fallback search by text
            page.evaluate('''() => {
                const radios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
                const r = radios.find(x => (x.getAttribute('name') || '').includes('ALTERED') && (x.getAttribute('name') || '').includes('YES')) ||
                          radios.find(x => (x.innerText || '').toLowerCase().trim() === 'yes');
                if (r) r.click();
            }''')
            print("Selected Altered Content YES via evaluate.")
        page.wait_for_timeout(1500)

        # 8. Step through Next buttons to Visibility
        next_btn = page.locator("#next-button").first
        for step in range(3):
            print(f"Clicking Next (step {step+1})...")
            next_btn.click()
            page.wait_for_timeout(2000)

        # 9. Set Visibility to Public & Publish
        print("Setting visibility to PUBLIC...")
        public_radio = page.locator('tp-yt-paper-radio-button[name="PUBLIC"]').first
        if public_radio.is_visible() and not public_radio.is_checked():
            public_radio.click()
        page.wait_for_timeout(1500)

        print("Clicking Publish/Done...")
        publish_btn = page.locator('#done-button, button:has-text("Publish")').first
        publish_btn.click()
        print("Publishing... Waiting 10 seconds...")
        page.wait_for_timeout(10000)

        # 10. Retrieve Video URL / ID
        print("Navigating to shorts content list to retrieve video ID...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short", wait_until="domcontentloaded")
        page.wait_for_timeout(5000)

        video_info = page.evaluate('''() => {
            const first = document.querySelector('ytcp-video-row a#thumbnail-anchor, ytcp-video-row a[href*="/video/"]');
            if (!first) return null;
            const m = first.href.match(/video\\/([a-zA-Z0-9_-]+)/);
            return {
                href: first.href,
                videoId: m ? m[1] : null
            };
        }''')
        print("Video Row Result:", video_info)

        if video_info and video_info.get("videoId"):
            vid_id = video_info["videoId"]
            url = f"https://youtube.com/shorts/{vid_id}"
            print("\n" + "="*60)
            print(f"🎉 SUKSES PUBLISH YOUTUBE SHORTS!")
            print(f"URL: {url}")
            print("="*60 + "\n")
            return url
        else:
            print("Upload completed, video row being indexed by YouTube.")
            return None

if __name__ == "__main__":
    upload()
