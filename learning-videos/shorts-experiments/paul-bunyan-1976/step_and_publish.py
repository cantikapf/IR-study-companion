import time
from playwright.sync_api import sync_playwright

def safe_eval(page, expr, arg=None):
    for i in range(8):
        try:
            return page.evaluate(expr, arg)
        except Exception:
            time.sleep(1.5)
    return None

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = [pg for pg in context.pages if "studio.youtube.com" in pg.url][0]
    
    print("Checking current state of studio...")
    state = safe_eval(page, """() => {
        const dialog = document.querySelector('ytcp-uploads-dialog');
        const nextBtn = document.querySelector('#next-button');
        const doneBtn = document.querySelector('#done-button');
        const publicRadio = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
        return {
            hasDialog: dialog !== null,
            nextVisible: nextBtn !== null && nextBtn.offsetParent !== null,
            doneVisible: doneBtn !== null && doneBtn.offsetParent !== null,
            publicVisible: publicRadio !== null && publicRadio.offsetParent !== null
        };
    }""")
    print("Current State:", state)
    
    # If Next button is visible, click it until Done/Public is reached
    for step in range(4):
        res = safe_eval(page, """() => {
            const pubRadio = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (pubRadio && pubRadio.offsetParent !== null && !pubRadio.checked) {
                pubRadio.click();
            }
            
            const done = document.querySelector('#done-button');
            if (done && done.offsetParent !== null) {
                done.click();
                return 'CLICKED_DONE';
            }
            
            const next = document.querySelector('#next-button');
            if (next && next.offsetParent !== null) {
                next.click();
                return 'CLICKED_NEXT';
            }
            return 'NONE';
        }""")
        print(f"Loop {step+1}: {res}")
        time.sleep(3)
        if res == 'CLICKED_DONE':
            print("Successfully clicked Done/Publish!")
            break
            
    print("Waiting 12 seconds for YouTube to process publish...")
    time.sleep(12)
    
    # Check shorts list
    page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded")
    time.sleep(5)
    
    for i in range(8):
        info = safe_eval(page, """() => {
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
        }""")
        if info and info.get("videoId"):
            url = f"https://youtube.com/shorts/{info['videoId']}"
            print("\n" + "="*60)
            print(f"🎉 PUBLIKASI BERHASIL!")
            print(f"Judul: {info['title']}")
            print(f"Visibilitas: {info['vis']}")
            print(f"URL: {url}")
            print("="*60 + "\n")
            break
        time.sleep(2)
