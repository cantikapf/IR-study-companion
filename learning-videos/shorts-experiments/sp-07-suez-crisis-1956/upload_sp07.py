import os
import sys
import time
from playwright.sync_api import sync_playwright

VIDEO_PATH = r"D:\PERSONAL PROJECT\IR-study-companion\learning-videos\exports\SP07_Suez_Crisis_1956_Short_1080p.mp4"
TITLE = "The Day Washington Bankrupted the British Empire (1956) #Shorts"
DESCRIPTION = """In 1956, America defeated the British Empire... without firing a single bullet.

When Egypt nationalized the Suez Canal, Britain, France, and Israel launched a secret military invasion: Operation Musketeer.

They expected American backing. Instead, President Dwight D. Eisenhower was furious. When London refused to withdraw, Washington struck their financial jugular: dumping British pound reserves and vetoing emergency IMF loans.

Facing total currency collapse within days, London surrendered. The British Empire died not by gunfire, but by financial checkmate.

Discover more untold geopolitics on IR in a Nutshell.
Interactive learning platform: https://ir-guide.netlify.app/

#history #geopolitics #coldwar #suezcrisis #internationalrelations #britishempire #money #shorts"""

def safe_eval(page, expr, arg=None):
    for i in range(12):
        try:
            return page.evaluate(expr, arg)
        except Exception:
            time.sleep(1.5)
    return None

def upload():
    video_abs_path = os.path.abspath(VIDEO_PATH)
    assert os.path.exists(video_abs_path), f"Video missing: {video_abs_path}"

    with sync_playwright() as p:
        print("Connecting to Chrome on port 9222...")
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = None
        for pg in context.pages:
            if "studio.youtube.com" in pg.url:
                page = pg
                break
        if not page:
            page = context.pages[0] if context.pages else context.new_page()
            page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ", wait_until="domcontentloaded")
            time.sleep(5)
            
        print("Waiting for page stability...")
        page.wait_for_load_state("domcontentloaded")
        time.sleep(3)

        # 1. Trigger Upload Modal
        print("Looking for Create button...")
        create_btn = None
        for attempt in range(10):
            try:
                btn = page.locator('button:has-text("Create"), ytcp-button#create-icon, button#create-icon').first
                if btn.is_visible():
                    btn.click()
                    print("Clicked Create button!")
                    create_btn = True
                    break
            except Exception:
                pass
            time.sleep(2)

        time.sleep(2)
        print("Clicking 'Upload videos' item...")
        for attempt in range(5):
            try:
                item = page.locator('tp-yt-paper-item:has-text("Upload videos"), #text-item-0').first
                if item.is_visible():
                    item.click()
                    print("Clicked Upload videos item!")
                    break
            except Exception:
                pass
            time.sleep(1.5)
        time.sleep(3)

        # 2. Feed Video File via Native CDP
        print("Feeding video via Native CDP...")
        cdp = context.new_cdp_session(page)
        doc = cdp.send("DOM.getDocument")
        node = cdp.send("DOM.querySelector", {"nodeId": doc["root"]["nodeId"], "selector": 'input[name="Filedata"]'})
        cdp.send("DOM.setFileInputFiles", {"files": [video_abs_path], "nodeId": node["nodeId"]})
        print("File provided, waiting 8 seconds for upload processing modal...")
        time.sleep(8)

        # 3. Fill Title & Description
        print("Filling Title & Description...")
        safe_eval(page, '''title => {
            const el = document.querySelector('#title-textarea #textbox');
            if (!el) return;
            el.focus();
            document.execCommand('selectAll', false, null);
            document.execCommand('delete', false, null);
            document.execCommand('insertText', false, title);
        }''', TITLE)
        time.sleep(1)
        page.keyboard.press("Escape")
        time.sleep(1)

        safe_eval(page, '''desc => {
            const el = document.querySelector('#description-textarea #textbox');
            if (!el) return;
            el.focus();
            document.execCommand('selectAll', false, null);
            document.execCommand('delete', false, null);
            document.execCommand('insertText', false, desc);
        }''', DESCRIPTION)
        time.sleep(1)
        page.keyboard.press("Escape")
        time.sleep(1)

        # 4. Audience: Not for kids
        print("Setting audience: Not made for kids...")
        safe_eval(page, '''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el && !el.checked) el.click();
        }''')
        time.sleep(1.5)

        # 5. Mandatory AI / Altered Content Disclosure (YES)
        print("Expanding Show more & configuring Altered Content Disclosure (YES)...")
        safe_eval(page, '''() => {
            const toggle = document.querySelector('#toggle-button, ytcp-button#toggle-button');
            if (toggle) toggle.click();
        }''')
        time.sleep(1.5)

        ai_set = safe_eval(page, '''() => {
            const r = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_HAS_ALTERED_CONTENT_YES"]');
            if (r) {
                r.click();
                return true;
            }
            return false;
        }''')
        print("Altered Content set to YES:", ai_set)
        time.sleep(1.5)

        # 6. Step through Next buttons
        print("Stepping through Next buttons...")
        for step in range(3):
            next_clicked = safe_eval(page, '''() => {
                const btn = document.querySelector('#next-button');
                if (btn) {
                    btn.click();
                    return true;
                }
                return false;
            }''')
            print(f"Step {step+1} next: {next_clicked}")
            time.sleep(2.5)

        # 7. Visibility: PUBLIC
        print("Setting visibility to PUBLIC...")
        pub_clicked = safe_eval(page, '''() => {
            const pub = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (pub) {
                pub.click();
                return true;
            }
            return false;
        }''')
        print("Public radio clicked:", pub_clicked)
        time.sleep(2)

        # 8. Done / Publish
        print("Clicking Publish / Done...")
        publish_res = safe_eval(page, '''() => {
            const done = document.querySelector('#done-button');
            if (done) {
                done.click();
                return 'CLICKED_DONE';
            }
            const save = document.querySelector('#save-button');
            if (save) {
                save.click();
                return 'CLICKED_SAVE';
            }
            return 'NOT_FOUND';
        }''')
        print("Publish button result:", publish_res)
        print("Waiting 15 seconds for YouTube Studio to commit upload...")
        time.sleep(15)

        # 9. Retrieve published video link
        print("Navigating to shorts content list to extract URL...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded")
        time.sleep(5)

        for attempt in range(10):
            info = safe_eval(page, '''() => {
                const row = document.querySelector('ytcp-video-row');
                if (!row) return null;
                const link = row.querySelector('a#thumbnail-anchor, a[href*="/video/"]');
                const title = row.querySelector('#video-title, #title')?.innerText || "";
                const vis = row.querySelector('.cell-body.visibility, #visibility')?.innerText || "";
                const m = link && link.href ? link.href.match(/video\\/([a-zA-Z0-9_-]+)/) : null;
                return {
                    title: title.trim(),
                    vis: vis.trim(),
                    videoId: m ? m[1] : null
                };
            }''')
            if info and info.get("videoId"):
                vid_id = info["videoId"]
                url = f"https://youtube.com/shorts/{vid_id}"
                print("\n" + "="*60)
                print("🎉 PUBLIKASI BERHASIL!")
                print(f"Judul: {info['title']}")
                print(f"Visibilitas: {info['vis']}")
                print(f"URL: {url}")
                print("="*60 + "\n")
                return url
            time.sleep(2)

if __name__ == "__main__":
    upload()
