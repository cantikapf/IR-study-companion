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

def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = [pg for pg in context.pages if "studio.youtube.com" in pg.url][0]
        
        print("Connected to page:", page.url)
        time.sleep(3)
        
        # Step 1: Wait for table to load
        print("Locating video row...")
        row_found = False
        for i in range(10):
            try:
                res = page.evaluate("""() => {
                    const rows = Array.from(document.querySelectorAll('ytcp-video-row'));
                    if (rows.length === 0) return null;
                    const r = rows[0];
                    const title = r.querySelector('#video-title, #title')?.innerText || '';
                    return { count: rows.length, title: title };
                }""")
                if res:
                    print(f"Found {res['count']} rows. Top video: {res['title']}")
                    row_found = True
                    break
            except Exception as e:
                pass
            time.sleep(2)
            
        assert row_found, "Could not find any video row in Studio"
        
        # Step 2: Click on the draft video or edit button
        print("Opening video editor dialog...")
        opened = page.evaluate("""() => {
            const rows = Array.from(document.querySelectorAll('ytcp-video-row'));
            const r = rows[0];
            if (!r) return false;
            const btns = Array.from(r.querySelectorAll('button, ytcp-button, a'));
            const draftBtn = btns.find(b => (b.innerText || '').toLowerCase().includes('draft') || 
                                           (b.getAttribute('aria-label') || '').toLowerCase().includes('draft')) || 
                             r.querySelector('a#video-title, a[href*="/video/"]') || r;
            if (draftBtn) {
                draftBtn.click();
                return true;
            }
            return false;
        }""")
        print("Clicked draft video:", opened)
        time.sleep(4)
        
        # Step 3: Wait for editor dialog or page
        print("Waiting for editor/dialog...")
        for i in range(10):
            try:
                state = page.evaluate("""() => {
                    const titleEl = document.querySelector('#title-textarea #textbox, input#title, #textbox[aria-label*="title" i]');
                    const descEl = document.querySelector('#description-textarea #textbox, #textbox[aria-label*="description" i]');
                    const dialog = document.querySelector('ytcp-uploads-dialog, ytcp-video-metadata-editor');
                    return {
                        hasEditor: titleEl !== null || dialog !== null,
                        currentTitle: titleEl ? titleEl.innerText : null
                    };
                }""")
                if state and state["hasEditor"]:
                    print("Editor active! Current title:", state["currentTitle"])
                    break
            except Exception:
                pass
            time.sleep(2)
            
        # Step 4: Fill Description cleanly
        print("Setting description...")
        page.evaluate("""desc => {
            const el = document.querySelector('#description-textarea #textbox, #textbox[aria-label*="description" i]');
            if (!el) return false;
            el.focus();
            document.execCommand('selectAll', false, null);
            document.execCommand('delete', false, null);
            document.execCommand('insertText', false, desc);
            return true;
        }""", DESCRIPTION)
        time.sleep(1)
        page.keyboard.press("Escape")
        time.sleep(1)
        
        # Step 5: Audience - Not made for kids
        print("Setting audience: Not made for kids...")
        page.evaluate("""() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el && !el.checked) el.click();
        }""")
        time.sleep(1)
        
        # Step 6: Expand 'Show more' for advanced configuration
        print("Expanding 'Show more'...")
        page.evaluate("""() => {
            const toggle = document.querySelector('#toggle-button, ytcp-button#toggle-button');
            if (toggle) toggle.click();
        }""")
        time.sleep(2)
        
        # Step 7: ADVANCED CONFIGURATION: AI / ALTERED CONTENT DISCLOSURE
        print("Selecting 'Yes' for Altered/Synthetic Content (AI disclosure)...")
        ai_result = page.evaluate("""() => {
            const radios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
            
            // Priority 1: Match by name attribute containing ALTERED and YES
            let yesRadio = radios.find(r => {
                const name = (r.getAttribute('name') || '').toUpperCase();
                return name.includes('ALTERED') && name.includes('YES');
            });
            
            // Priority 2: Match by text 'Yes' / 'Ya' inside altered content section
            if (!yesRadio) {
                yesRadio = radios.find(r => {
                    const txt = (r.innerText || '').toLowerCase().trim();
                    const parent = r.closest('ytcp-altered-content-editor, #altered-content, ytcp-form-altered-content') || {};
                    const ptxt = (parent.innerText || '').toLowerCase();
                    return (txt === 'yes' || txt === 'ya') && (ptxt.includes('altered') || ptxt.includes('sintetis') || ptxt.includes('ai') || ptxt.includes('content'));
                });
            }
            
            // Priority 3: Fallback search on all radios
            if (!yesRadio) {
                yesRadio = radios.find(r => {
                    const txt = (r.innerText || '').toLowerCase().trim();
                    return txt === 'yes' || txt === 'ya';
                });
            }

            if (yesRadio) {
                yesRadio.click();
                return { success: true, name: yesRadio.getAttribute('name'), text: yesRadio.innerText.trim() };
            }
            return { success: false, available_radios: radios.map(r => ({ name: r.getAttribute('name'), text: r.innerText.trim() })) };
        }""")
        print("Altered Content (AI) result:", ai_result)
        time.sleep(2)
        
        # Step 8: Step through Next buttons
        print("Navigating through Next buttons...")
        for step in range(3):
            next_clicked = page.evaluate("""() => {
                const btn = document.querySelector('#next-button');
                if (btn && btn.offsetParent !== null) {
                    btn.click();
                    return true;
                }
                return false;
            }""")
            print(f"Step {step+1} next clicked: {next_clicked}")
            time.sleep(2.5)
            
        # Step 9: Set Visibility to PUBLIC
        print("Setting visibility to PUBLIC...")
        page.evaluate("""() => {
            const pubRadio = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (pubRadio) pubRadio.click();
        }""")
        time.sleep(2)
        
        # Step 10: Click Save / Done / Publish
        print("Publishing video...")
        published = page.evaluate("""() => {
            const btn = document.querySelector('#done-button, #save-button, button:has-text("Publish"), button:has-text("Save")');
            if (btn) {
                btn.click();
                return true;
            }
            return false;
        }""")
        print("Publish button clicked:", published)
        print("Waiting 10 seconds for publish completion...")
        time.sleep(10)
        
        # Step 11: Refresh content list and extract final video URL
        print("Checking final published video list...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D", wait_until="domcontentloaded")
        time.sleep(5)
        
        for attempt in range(8):
            try:
                final_info = page.evaluate("""() => {
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
                if final_info and final_info["videoId"]:
                    vid_id = final_info["videoId"]
                    url = f"https://youtube.com/shorts/{vid_id}"
                    print("\n" + "="*60)
                    print(f"🎉 BERHASIL PUBLIKASI! URL Shorts: {url}")
                    print(f"Judul: {final_info['title']}")
                    print(f"Visibilitas: {final_info['visibility']}")
                    print("="*60 + "\n")
                    return url
            except Exception:
                pass
            time.sleep(2)

if __name__ == "__main__":
    main()
