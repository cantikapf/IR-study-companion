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

print(f"Target video: {VIDEO_PATH}")
assert os.path.exists(VIDEO_PATH), f"File not found: {VIDEO_PATH}"

def run():
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
            
        print("Initial page URL:", page.url)
        time.sleep(5)
        
        # 1. Settle & verify channel
        ch_text = ""
        for attempt in range(8):
            try:
                ch_text = page.evaluate('() => document.querySelector("#entity-name, ytcp-entity-header h1, #channel-title")?.innerText || ""')
                if ch_text:
                    break
            except Exception as e:
                print(f"Waiting for context stability (attempt {attempt+1})...")
            time.sleep(2)
            
        print("Channel detected:", ch_text)
        assert "International Relations in a nutshell" in ch_text, f"Wrong channel: {ch_text}"
        
        # 2. Check if upload dialog already open
        has_dialog = page.evaluate('() => document.querySelector("ytcp-uploads-dialog") !== null')
        if not has_dialog:
            print("Opening Create -> Upload videos...")
            # Click Create
            page.evaluate('''() => {
                const btn = document.querySelector('button[aria-label="Create"], ytcp-button.ytcpAppHeaderCreateIcon');
                if (btn) btn.click();
            }''')
            time.sleep(2)
            
            # Click Upload videos
            page.evaluate('''() => {
                const items = Array.from(document.querySelectorAll('tp-yt-paper-item, paper-item, [role="menuitem"]'));
                const uploadItem = items.find(it => (it.innerText || "").includes("Upload videos"));
                if (uploadItem) uploadItem.click();
            }''')
            time.sleep(3)
            
        # 3. Feed video file via Native CDP
        print("Feeding video file via Native CDP...")
        cdp = context.new_cdp_session(page)
        doc = cdp.send("DOM.getDocument")
        node = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": 'input[name="Filedata"]'})
        print("Target node ID:", node)
        assert node["nodeId"] > 0, "Could not find input[name='Filedata'] in DOM"
        cdp.send("DOM.setFileInputFiles", {"files": [VIDEO_PATH], "nodeId": node["nodeId"]})
        print("File submitted. Waiting for upload processing...")
        time.sleep(8)
        
        # 4. Fill Title
        print("Filling title...")
        title_el = page.locator('#title-textarea #textbox, #textbox[aria-label*="title" i]').first
        title_el.wait_for(state="visible", timeout=30000)
        title_el.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        title_el.fill(TITLE)
        time.sleep(1)
        
        # 5. Fill Description
        print("Filling description...")
        desc_el = page.locator('#description-textarea #textbox, #textbox[aria-label*="description" i]').first
        desc_el.wait_for(state="visible", timeout=10000)
        desc_el.click()
        page.keyboard.press("Control+A")
        page.keyboard.press("Backspace")
        desc_el.fill(DESCRIPTION)
        time.sleep(1)
        
        # 6. Audience: Not made for kids
        print("Setting audience: Not made for kids...")
        page.evaluate('''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el && !el.checked) el.click();
        }''')
        time.sleep(1)
        
        # 7. ADVANCED CONFIGURATION: AI / ALTERED CONTENT DISCLOSURE
        print("Configuring AI / Altered Content disclosure...")
        # Expand 'Show more'
        page.evaluate('''() => {
            const toggle = document.querySelector('#toggle-button, ytcp-button#toggle-button');
            if (toggle) toggle.click();
        }''')
        time.sleep(2)
        
        # Select 'Yes' for Altered / Synthetic Content (AI)
        ai_set = page.evaluate('''() => {
            const radios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
            // Look for altered content radio buttons
            const yesRadio = radios.find(r => {
                const name = (r.getAttribute('name') || '').toUpperCase();
                const txt = (r.innerText || '').toLowerCase().trim();
                return (name.includes('ALTERED') || name.includes('SYNTHETIC')) && (name.includes('YES') || txt === 'yes' || txt === 'ya');
            }) || radios.find(r => {
                const txt = (r.innerText || '').toLowerCase().trim();
                const container = r.closest('ytcp-altered-content-editor, #altered-content, ytcp-form-altered-content') || {};
                const ctxt = (container.innerText || '').toLowerCase();
                return (txt === 'yes' || txt === 'ya') && (ctxt.includes('altered') || ctxt.includes('sintetis') || ctxt.includes('ai'));
            });

            if (yesRadio) {
                yesRadio.click();
                return { success: true, text: yesRadio.innerText.trim(), name: yesRadio.getAttribute('name') };
            }
            return { success: false, radios_found: radios.map(r => ({ name: r.getAttribute('name'), text: r.innerText.trim() })) };
        }''')
        print("AI Disclosure Status:", ai_set)
        time.sleep(2)
        
        # 8. Step through Next buttons
        print("Stepping through Next buttons...")
        next_btn = page.locator("#next-button").first
        for step in range(3):
            print(f"Clicking Next (step {step+1})...")
            next_btn.click()
            time.sleep(2)
            
        # 9. Set Visibility to Public
        print("Setting visibility to PUBLIC...")
        page.evaluate('''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (el) el.click();
        }''')
        time.sleep(2)
        
        # 10. Click Publish / Done
        print("Clicking Publish / Done...")
        done_btn = page.locator('#done-button, button:has-text("Publish")').first
        done_btn.click()
        print("Waiting 10 seconds for publish confirmation...")
        time.sleep(10)
        
        # 11. Navigate to content list and retrieve video ID
        print("Navigating to shorts content list to retrieve video ID...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short", wait_until="domcontentloaded")
        time.sleep(5)
        
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
            url = f"https://youtube.com/shorts/{vid_id}"
            print("\n" + "="*60)
            print(f"🎉 SUCCESS! Published Shorts URL: {url}")
            print(f"Title: {video_info.get('title')}")
            print("="*60 + "\n")
            return url
        else:
            print("Upload completed, video ID will be checked via direct list.")
            return None

if __name__ == "__main__":
    run()
