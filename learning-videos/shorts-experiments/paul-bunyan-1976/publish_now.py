import os
import sys
import time
from playwright.sync_api import sync_playwright

def safe_eval(page, expr, arg=None):
    for i in range(8):
        try:
            return page.evaluate(expr, arg)
        except Exception as e:
            time.sleep(1.5)
    return None

def publish():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = [pg for pg in context.pages if "studio.youtube.com" in pg.url][0]
        
        print("Connected to YouTube Studio:", page.url)
        time.sleep(2)
        
        # 1. Click 'Edit draft' on row 0
        print("Clicking 'Edit draft' on row 0...")
        clicked_edit = safe_eval(page, """() => {
            const rows = document.querySelectorAll('ytcp-video-row');
            if (!rows.length) return false;
            const r = rows[0];
            const allElements = Array.from(r.querySelectorAll('*'));
            const editBtn = allElements.find(el => (el.innerText || '').trim().toLowerCase() === 'edit draft') ||
                            allElements.find(el => (el.getAttribute('aria-label') || '').toLowerCase().includes('edit draft')) ||
                            r.querySelector('button, ytcp-button');
            if (editBtn) {
                editBtn.click();
                return true;
            }
            return false;
        }""")
        print("Edit draft clicked?", clicked_edit)
        time.sleep(4)
        
        # 2. Check if editor modal is open
        print("Waiting for dialog...")
        for i in range(8):
            has_dialog = safe_eval(page, """() => {
                const d = document.querySelector('ytcp-uploads-dialog, ytcp-video-metadata-editor');
                return d !== null && d.offsetParent !== null;
            }""")
            if has_dialog:
                print("Editor dialog confirmed open!")
                break
            time.sleep(1.5)
            
        # 3. Verify Audience (Not made for kids)
        print("Verifying audience: Not made for kids...")
        safe_eval(page, """() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el && !el.checked) el.click();
        }""")
        time.sleep(1)
        
        # 4. Verify / Set Altered Content (AI) -> YES
        print("Expanding 'Show more' for AI content verification...")
        safe_eval(page, """() => {
            const toggle = document.querySelector('#toggle-button, ytcp-button#toggle-button');
            if (toggle) toggle.click();
        }""")
        time.sleep(2)
        
        print("Selecting 'Yes' for Altered Content (AI)...")
        ai_res = safe_eval(page, """() => {
            const radios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
            let yesRadio = radios.find(r => {
                const name = (r.getAttribute('name') || '').toUpperCase();
                return name.includes('ALTERED') && name.includes('YES');
            }) || radios.find(r => {
                const txt = (r.innerText || '').toLowerCase().trim();
                return txt === 'yes' || txt === 'ya';
            });
            if (yesRadio) {
                yesRadio.click();
                return { success: true, name: yesRadio.getAttribute('name'), text: yesRadio.innerText.trim() };
            }
            return { success: false };
        }""")
        print("AI Disclosure selection:", ai_res)
        time.sleep(1.5)
        
        # 5. Step through Next buttons to Visibility
        print("Clicking Next buttons...")
        for step in range(3):
            next_clicked = safe_eval(page, """() => {
                const btn = document.querySelector('#next-button');
                if (btn && btn.offsetParent !== null) {
                    btn.click();
                    return true;
                }
                // Fallback search by id
                const allBtns = Array.from(document.querySelectorAll('button, ytcp-button'));
                const b = allBtns.find(x => x.id === 'next-button' || (x.innerText || '').trim().toLowerCase() === 'next');
                if (b) {
                    b.click();
                    return true;
                }
                return false;
            }""")
            print(f"Step {step+1} Next clicked: {next_clicked}")
            time.sleep(2.5)
            
        # 6. Set Visibility to PUBLIC
        print("Setting visibility to PUBLIC...")
        pub_set = safe_eval(page, """() => {
            const pubRadio = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (pubRadio) {
                pubRadio.click();
                return true;
            }
            const allRadios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
            const pRadio = allRadios.find(r => (r.getAttribute('name') || '').toUpperCase() === 'PUBLIC' || (r.innerText || '').toLowerCase().includes('public'));
            if (pRadio) {
                pRadio.click();
                return true;
            }
            return false;
        }""")
        print("Visibility set to Public?", pub_set)
        time.sleep(2)
        
        # 7. Click Save / Done / Publish (Safe DOM Search, NO syntax error)
        print("Clicking Save / Done / Publish button...")
        save_clicked = safe_eval(page, """() => {
            // First check #done-button
            const done = document.querySelector('#done-button');
            if (done && done.offsetParent !== null) {
                done.click();
                return { success: true, id: done.id, text: done.innerText.trim() };
            }
            // Check all buttons
            const allBtns = Array.from(document.querySelectorAll('button, ytcp-button, ytcp-button-shape'));
            const target = allBtns.find(b => {
                const id = (b.id || '').toLowerCase();
                const txt = (b.innerText || '').trim().toLowerCase();
                const aria = (b.getAttribute('aria-label') || '').toLowerCase();
                return id === 'done-button' || id === 'save-button' || 
                       txt === 'save' || txt === 'publish' || txt === 'simpan' || txt === 'publikasikan' ||
                       aria.includes('save') || aria.includes('publish');
            });
            if (target) {
                target.click();
                return { success: true, id: target.id, text: target.innerText.trim() };
            }
            return { success: false, buttons: allBtns.map(b => ({ id: b.id, text: b.innerText.trim() })).filter(b => b.text.length > 0) };
        }""")
        print("Publish button result:", save_clicked)
        print("Waiting 12 seconds for YouTube to process publishing...")
        time.sleep(12)
        
        # 8. Refresh and retrieve final Video ID and URL
        print("Retrieving published video info...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded")
        time.sleep(5)
        
        for attempt in range(8):
            final_info = safe_eval(page, """() => {
                const row = document.querySelector('ytcp-video-row');
                if (!row) return null;
                const link = row.querySelector('a#thumbnail-anchor, a[href*="/video/"]');
                const title = row.querySelector('#video-title, #title')?.innerText || "";
                const visibility = row.querySelector('.cell-body.visibility, #visibility')?.innerText || "";
                const href = link ? link.href : "";
                const m = href.match(/video\\/([a-zA-Z0-9_-]+)/);
                return {
                    title: title.trim(),
                    visibility: visibility.trim(),
                    videoId: m ? m[1] : null
                };
            }""")
            if final_info and final_info.get("videoId"):
                vid_id = final_info["videoId"]
                url = f"https://youtube.com/shorts/{vid_id}"
                print("\n" + "="*60)
                print(f"🎉 BERHASIL PUBLIKASI! URL Shorts: {url}")
                print(f"Judul: {final_info['title']}")
                print(f"Visibilitas: {final_info['visibility']}")
                print("="*60 + "\n")
                return url
            time.sleep(2)
            
        print("Finished script execution.")

if __name__ == "__main__":
    publish()
