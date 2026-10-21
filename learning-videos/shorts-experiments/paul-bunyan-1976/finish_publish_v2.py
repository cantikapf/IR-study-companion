import os
import sys
import time
from playwright.sync_api import sync_playwright

DESCRIPTION = """In 1976, the United States deployed an entire war armada... just to cut down a single tree.

After North Korean soldiers killed two American officers attempting to trim a poplar tree blocking the DMZ view, Washington launched Operation Paul Bunyan: 813 combat troops, 27 helicopters, B-52 bombers, fighter jets, and an aircraft carrier battle group.

In 42 minutes, the tree was gone. Zero bullets fired.

Discover more untold geopolitical history on IR in a Nutshell.
Explore structured study guides: https://ir-guide.netlify.app/

#coldwar #historyfacts #koreanwar #dmz #militaryhistory #internationalrelations #shorts"""

def safe_eval(page, expr, arg=None):
    for i in range(10):
        try:
            return page.evaluate(expr, arg)
        except Exception:
            time.sleep(1.5)
    return None

def run():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = [pg for pg in context.pages if "studio.youtube.com" in pg.url][0]
        
        print("Waiting for page stability on opened dialog...")
        time.sleep(5)
        
        # 1. Fill/Verify Description
        print("Checking description...")
        curr_desc = safe_eval(page, '() => document.querySelector("#description-textarea #textbox")?.innerText || ""') or ""
        print(f"Current description length: {len(curr_desc)}")
        if "Operation Paul Bunyan" not in curr_desc:
            print("Inserting full description...")
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

        # 2. Audience: Not made for kids
        print("Setting audience (Not made for kids)...")
        safe_eval(page, '''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el && !el.checked) el.click();
        }''')
        time.sleep(1)

        # 3. ADVANCED CONFIGURATION: AI CONTENT DISCLOSURE
        print("Expanding 'Show more'...")
        safe_eval(page, '''() => {
            const toggle = document.querySelector('#toggle-button, ytcp-button#toggle-button');
            if (toggle) toggle.click();
        }''')
        time.sleep(1.5)

        print("Setting Altered / Synthetic Content (AI) to YES...")
        ai_res = safe_eval(page, '''() => {
            const r = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_HAS_ALTERED_CONTENT_YES"]');
            if (r) {
                r.click();
                return { success: true, text: r.innerText.trim() };
            }
            return { success: false };
        }''')
        print("AI Disclosure selection:", ai_res)
        time.sleep(1.5)

        # 4. Step through Next buttons
        print("Stepping through Next buttons...")
        for step in range(3):
            clicked_next = safe_eval(page, '''() => {
                const btn = document.querySelector('#next-button');
                if (btn) {
                    btn.click();
                    return true;
                }
                return false;
            }''')
            print(f"Clicking Next (step {step+1}): {clicked_next}")
            time.sleep(2.5)

        # 5. Set Visibility to PUBLIC
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

        # 6. Click Publish / Done / Save
        print("Clicking Publish / Done / Save...")
        done_clicked = safe_eval(page, '''() => {
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
        print("Result of publish click:", done_clicked)
        print("Waiting 15 seconds for YouTube to finish publishing...")
        time.sleep(15)

        # 7. Retrieve video URL
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
                print(f"🎉 PUBLIKASI BERHASIL!")
                print(f"Judul: {info['title']}")
                print(f"Visibilitas: {info['vis']}")
                print(f"URL: {url}")
                print("="*60 + "\n")
                return url
            time.sleep(2)

if __name__ == "__main__":
    run()
