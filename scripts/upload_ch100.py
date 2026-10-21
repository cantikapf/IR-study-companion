import os
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent

VIDEO_PATH = str(REPO_ROOT / "learning-videos" / "exports" / "CH100_Regionalism_in_International_Affairs.mp4")
THUMBNAIL_PATH = str(REPO_ROOT / "learning-videos" / "posters" / "CH100_Regionalism_Thumbnail.png")

TITLE = "Why 27 Nations Gave Up Their Borders | Regionalism Explained"
DESCRIPTION = """Why did 27 sovereign nations willingly dissolve their borders, surrender their currencies, and submit their national parliaments to a higher court?

In this comprehensive explanatory deep dive, we break down the architecture of Regionalism in International Relations:
00:00 The Regionalism Puzzle: Sovereignty vs Scale
00:53 Regional Cooperation: Functionalism (David Mitrany)
01:46 Supranational Integration & Neofunctional Spillover (Ernst Haas)
02:40 Economic Architecture: Trade Creation vs Diversion (Jacob Viner)
03:36 Empirical Case 1: The European Union & Commission Triad
04:33 Empirical Case 2: The ASEAN Way & Consensus Diplomacy
05:25 Empirical Case 3: Post-Colonial Blocs & Identity Limits (AU, Mercosur, SICA)
06:17 Grand Synthesis: The 21st Century Regional Fortress

Interactive learning platform & curriculum companion:
https://ir-guide.netlify.app/chapters/010-introduction-to-ir/100-regionalism-affairs.html

#internationalrelations #geopolitics #europeanunion #asean #politicalscience #regionalism #history #education"""

def safe_eval(page, expr, arg=None):
    for i in range(12):
        try:
            return page.evaluate(expr, arg)
        except Exception:
            time.sleep(1.5)
    return None

def upload():
    video_abs_path = os.path.abspath(VIDEO_PATH)
    thumb_abs_path = os.path.abspath(THUMBNAIL_PATH)
    assert os.path.exists(video_abs_path), f"Video missing: {video_abs_path}"
    assert os.path.exists(thumb_abs_path), f"Thumbnail missing: {thumb_abs_path}"

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
            
        print("Verifying channel...")
        ch_text = ""
        for _ in range(10):
            try:
                ch_text = page.evaluate('() => document.querySelector("#entity-name, ytcp-entity-header h1, #channel-title")?.innerText || ""')
                if ch_text:
                    break
            except Exception:
                time.sleep(1.5)
        print(f"Channel detected: '{ch_text}'")
        assert "nutshell" in ch_text.lower() or "international" in ch_text.lower(), f"Wrong channel: {ch_text}"

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
        print("File provided, waiting 10 seconds for upload processing modal...")
        time.sleep(10)

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
        time.sleep(1.5)
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
        time.sleep(1.5)
        page.keyboard.press("Escape")
        time.sleep(1)

        # 4. Upload Custom Thumbnail
        print("Uploading custom thumbnail...")
        try:
            doc = cdp.send("DOM.getDocument")
            thumb_node = cdp.send("DOM.querySelector", {
                "nodeId": doc["root"]["nodeId"],
                "selector": 'input#file-loader, input[type="file"][accept*="image"]'
            })
            if thumb_node and thumb_node.get("nodeId"):
                cdp.send("DOM.setFileInputFiles", {"files": [thumb_abs_path], "nodeId": thumb_node["nodeId"]})
                print("Thumbnail provided via CDP!")
                time.sleep(3)
            else:
                print("Warning: Thumbnail input node not found directly, checking DOM...")
        except Exception as e:
            print("Thumbnail upload error via CDP:", e)

        # 5. Audience: Not for kids
        print("Setting audience: Not made for kids...")
        safe_eval(page, '''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el && !el.checked) el.click();
        }''')
        time.sleep(1.5)

        # 6. Mandatory AI / Altered Content Disclosure (YES)
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

        # 7. Step through Next buttons (Video Elements, Checks, Visibility)
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

        # 8. Visibility: PUBLIC
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

        # 9. Done / Publish
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

        # 10. Retrieve published video link
        print("Navigating to videos content list to extract URL...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded")
        time.sleep(5)

        for attempt in range(12):
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
                url = f"https://youtu.be/{vid_id}"
                print("\n" + "="*60)
                print("🎉 PUBLIKASI BERHASIL!")
                print(f"Judul: {info['title']}")
                print(f"Visibilitas: {info['vis']}")
                print(f"Video ID: {vid_id}")
                print(f"URL: {url}")
                print("="*60 + "\n")
                
                # Close studio tab to free RAM
                page.close()
                return vid_id, url
            time.sleep(3)

        page.close()
        return None, None

if __name__ == "__main__":
    upload()
