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
    page.wait_for_timeout(8000)

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
    print("Setting audience (Not made for kids)...")
    not_for_kids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').first
    if not_for_kids.is_visible():
        not_for_kids.click()
        print("Checked NOT MADE FOR KIDS.")
    else:
        page.evaluate('''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el) el.click();
        }''')
    page.wait_for_timeout(1000)

    # 7. ADVANCED CONFIGURATION: AI CONTENT / ALTERED CONTENT DISCLOSURE
    print("Expanding 'Show more' for advanced configuration...")
    # Click Show more toggle
    show_more_clicked = False
    for toggle_sel in ['#toggle-button', 'button:has-text("Show more")', 'button:has-text("SHOW MORE")', 'ytcp-button#toggle-button']:
        try:
            toggle_el = page.locator(toggle_sel).first
            if toggle_el.is_visible():
                toggle_el.click()
                show_more_clicked = True
                print(f"Clicked toggle using {toggle_sel}")
                break
        except Exception:
            pass
            
    if not show_more_clicked:
        page.evaluate('''() => {
            const el = document.querySelector('#toggle-button, ytcp-button#toggle-button');
            if (el) el.click();
        }''')
    page.wait_for_timeout(2000)

    print("Locating Altered or Synthetic Content (AI) disclosure option...")
    # Inspect altered content options
    ai_status = page.evaluate('''() => {
        // Look for altered content section or radio buttons
        const radios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
        const yesRadio = radios.find(r => {
            const name = r.getAttribute('name') || '';
            const txt = (r.innerText || '').toLowerCase();
            return name.includes('ALTERED') && (name.includes('YES') || txt.includes('yes') || txt.includes('ya'));
        }) || radios.find(r => {
            const txt = (r.innerText || '').trim().toLowerCase();
            const parentTxt = (r.closest('ytcp-altered-content-editor, #altered-content, ytcp-form-altered-content') || {}).innerText || '';
            return (txt === 'yes' || txt === 'ya') && (parentTxt.toLowerCase().includes('altered') || parentTxt.toLowerCase().includes('sintetis') || parentTxt.toLowerCase().includes('ai'));
        });

        if (yesRadio) {
            yesRadio.click();
            return { success: true, text: yesRadio.innerText, name: yesRadio.getAttribute('name') };
        }
        
        // Fallback: search by text within altered content container
        const container = document.querySelector('ytcp-altered-content-editor, #altered-content, ytcp-video-metadata-editor-advanced');
        if (container) {
            const yesBtn = container.querySelector('tp-yt-paper-radio-button:first-of-type, tp-yt-paper-radio-button[name*="YES" i]');
            if (yesBtn) {
                yesBtn.click();
                return { success: true, method: 'container_fallback', text: yesBtn.innerText };
            }
        }
        
        return { success: false, available_radios: radios.map(r => ({ name: r.getAttribute('name'), text: r.innerText })) };
    }''')
    print("AI Content Disclosure configuration result:", ai_status)
    page.wait_for_timeout(2000)

    # 8. Step through Next buttons to Visibility
    next_btn = page.locator("#next-button").first
    for step in range(3):
        print(f"Clicking Next (step {step+1})...")
        next_btn.click()
        page.wait_for_timeout(2500)

    # 9. Set Visibility to Public
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

    # 10. Click Publish / Done
    print("Clicking Publish/Done button...")
    done_btn = page.locator('#done-button, button:has-text("Publish")').first
    done_btn.click()
    page.wait_for_timeout(8000)

    # 11. Extract video ID / URL
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
        print(f"\n========================================================")
        print(f"🎉 SUCCESS! Published Shorts URL: https://youtube.com/shorts/{vid_id}")
        print(f"Video Title: {video_info.get('title')}")
        print(f"========================================================\n")
    else:
        print("Upload completed, video ID extraction will be checked via direct list.")
