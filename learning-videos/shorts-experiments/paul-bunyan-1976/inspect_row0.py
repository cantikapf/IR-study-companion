import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://localhost:9222")
    context = browser.contexts[0]
    page = [pg for pg in context.pages if "studio.youtube.com" in pg.url][0]
    
    print("Waiting for page stability...")
    time.sleep(3)
    row_info = None
    for attempt in range(8):
        try:
            row_info = page.evaluate("""() => {
                const row = document.querySelector('ytcp-video-row');
                if (!row) return null;
                const link = row.querySelector('a#thumbnail-anchor, a[href*="/video/"], a#video-title');
                const cells = Array.from(row.querySelectorAll('.cell-body, ytcp-table-cell, .table-cell-content')).map(c => c.innerText.trim()).filter(Boolean);
                return {
                    title: row.querySelector('#video-title, #title')?.innerText || '',
                    link: link ? link.href : '',
                    cells: cells,
                    textLines: row.innerText.split('\\n').map(s => s.trim()).filter(Boolean)
                };
            }""")
            if row_info:
                break
        except Exception as e:
            time.sleep(2)
    print("Row 0:", row_info)
