import time
from playwright.sync_api import sync_playwright

def safe_eval(page, expr, arg=None):
    for i in range(8):
        try:
            return page.evaluate(expr, arg)
        except Exception:
            time.sleep(1.5)
    return None

def complete():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = [pg for pg in context.pages if "studio.youtube.com" in pg.url][0]
        
        print("Page URL:", page.url)
        time.sleep(2)
        
        # 1. Click 'Edit draft' on row 0
        print("Clicking 'Edit draft' on row 0...")
        clicked = safe_eval(page, """() => {
            const rows = document.querySelectorAll('ytcp-video-row');
            if (!rows.length) return false;
            const r = rows[0];
            const allElements = Array.from(r.querySelectorAll('*'));
            const editBtn = allElements.find(el => (el.innerText || '').trim().toLowerCase() === 'edit draft') ||
                            allElements.find(el => (el.getAttribute('aria-label') || '').toLowerCase().includes('edit draft'));
            if (editBtn) {
                editBtn.click();
                return true;
            }
            return false;
        }""")
        print("Clicked Edit draft:", clicked)
        time.sleep(4)
        
        # 2. Verify dialog is open
        for i in range(10):
            has_dialog = safe_eval(page, """() => {
                const d = document.querySelector('ytcp-uploads-dialog, ytcp-video-metadata-editor');
                return d !== null && d.offsetParent !== null;
            }""")
            if has_dialog:
                print("Editor dialog is now open!")
                break
            time.sleep(1.5)
            
        # 3. Check / Ensure Altered Content (AI) is set to YES
        print("Verifying AI content disclosure...")
        ai_res = safe_eval(page, """() => {
            const toggle = document.querySelector('#toggle-button, ytcp-button#toggle-button');
            if (toggle) toggle.click();
            
            const radios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
            const yesRadio = radios.find(r => {
                const name = (r.getAttribute('name') || '').toUpperCase();
                return name.includes('ALTERED') && name.includes('YES');
            }) || radios.find(r => (r.innerText || '').toLowerCase().trim() === 'yes');
            
            if (yesRadio) {
                yesRadio.click();
                return { success: true, text: yesRadio.innerText.trim(), name: yesRadio.getAttribute('name') };
            }
            return { success: false };
        }""")
        print("AI Disclosure:", ai_res)
        time.sleep(2)
        
        # 4. Advance through Next buttons
        print("Stepping Next to Visibility...")
        for step in range(3):
            next_res = safe_eval(page, """() => {
                const nextBtn = document.querySelector('#next-button');
                if (nextBtn) {
                    nextBtn.click();
                    return true;
                }
                const all = Array.from(document.querySelectorAll('button, ytcp-button'));
                const b = all.find(x => x.id === 'next-button' || (x.innerText || '').trim().toLowerCase() === 'next');
                if (b) {
                    b.click();
                    return true;
                }
                return false;
            }""")
            print(f"Step {step+1} Next clicked:", next_res)
            time.sleep(2.5)
            
        # 5. Set Visibility to PUBLIC
        print("Selecting PUBLIC visibility...")
        pub_res = safe_eval(page, """() => {
            const pubRadio = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (pubRadio) {
                pubRadio.click();
                return true;
            }
            const allRadios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
            const pr = allRadios.find(r => (r.getAttribute('name') || '').toUpperCase() === 'PUBLIC' || 
                                           (r.innerText || '').toLowerCase().trim() === 'public');
            if (pr) {
                pr.click();
                return true;
            }
            return false;
        }""")
        print("Public radio selected:", pub_res)
        time.sleep(2)
        
        # 6. Click Done / Save / Publish
        print("Publishing video...")
        publish_res = safe_eval(page, """() => {
            const doneBtn = document.querySelector('#done-button');
            if (doneBtn && doneBtn.offsetParent !== null) {
                doneBtn.click();
                return { success: true, id: doneBtn.id, text: doneBtn.innerText.trim() };
            }
            const allBtns = Array.from(document.querySelectorAll('button, ytcp-button'));
            const target = allBtns.find(b => {
                const id = (b.id || '').toLowerCase();
                const txt = (b.innerText || '').trim().toLowerCase();
                return id === 'done-button' || id === 'save-button' || txt === 'save' || txt === 'publish';
            });
            if (target) {
                target.click();
                return { success: true, id: target.id, text: target.innerText.trim() };
            }
            return { success: false };
        }""")
        print("Publish button result:", publish_res)
        print("Waiting 15 seconds for upload dialog to finalize and close...")
        time.sleep(15)
        
        # 7. Check video list and get URL
        print("Refreshing content page to extract published video URL...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded")
        time.sleep(5)
        
        for attempt in range(8):
            final_info = safe_eval(page, """() => {
                const row = document.querySelector('ytcp-video-row');
                if (!row) return null;
                const link = row.querySelector('a#thumbnail-anchor, a[href*="/video/"]');
                const title = row.querySelector('#video-title, #title')?.innerText || "";
                const vis = row.querySelector('.cell-body.visibility, #visibility')?.innerText || "";
                const href = link ? link.href : "";
                const m = href.match(/video\\/([a-zA-Z0-9_-]+)/);
                return {
                    title: title.trim(),
                    vis: vis.trim(),
                    videoId: m ? m[1] : null,
                    href: href
                };
            }""")
            if final_info and final_info.get("videoId"):
                vid_id = final_info["videoId"]
                url = f"https://youtube.com/shorts/{vid_id}"
                print("\n" + "="*60)
                print(f"🎉 SUKSES PUBLISH YOUTUBE SHORTS!")
                print(f"Judul: {final_info['title']}")
                print(f"Visibilitas: {final_info['vis']}")
                print(f"URL: {url}")
                print("="*60 + "\n")
                return url
            time.sleep(2)

if __name__ == "__main__":
    complete()
