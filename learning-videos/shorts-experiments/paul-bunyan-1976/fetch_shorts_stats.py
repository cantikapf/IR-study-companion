import json
import time
from playwright.sync_api import sync_playwright

def safe_eval(page, expr, arg=None):
    for i in range(10):
        try:
            return page.evaluate(expr, arg)
        except Exception as e:
            time.sleep(1.5)
    return None

def fetch_stats():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        
        # Check existing pages or open
        page = None
        for pg in context.pages:
            if "studio.youtube.com" in pg.url:
                page = pg
                break
        if not page:
            page = context.pages[0] if context.pages else context.new_page()
            
        target_url = "https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"
        print("Navigating to YouTube Studio Shorts Content list...")
        page.goto(target_url, wait_until="domcontentloaded")
        time.sleep(6)
        
        # Wait for table rows to appear
        for attempt in range(8):
            count = safe_eval(page, "() => document.querySelectorAll('ytcp-video-row').length")
            print(f"Attempt {attempt+1}: found {count} rows")
            if count and count > 0:
                break
            time.sleep(2)
            
        rows_data = safe_eval(page, r"""() => {
            const rows = Array.from(document.querySelectorAll('ytcp-video-row'));
            return rows.map(r => {
                const titleEl = r.querySelector('#video-title, #title');
                const linkEl = r.querySelector('a#thumbnail-anchor, a[href*="/video/"]');
                const textLines = r.innerText.split('\n').map(s => s.trim()).filter(Boolean);
                
                const href = linkEl ? linkEl.href : '';
                const m = href.match(/video\/([a-zA-Z0-9_-]+)/);
                
                return {
                    title: titleEl ? titleEl.innerText.trim() : (textLines[1] || ''),
                    videoId: m ? m[1] : null,
                    textLines: textLines
                };
            });
        }""")
        
        print("\n=== RAW SHORTS DATA ===")
        print(json.dumps(rows_data, indent=2))

if __name__ == "__main__":
    fetch_stats()
