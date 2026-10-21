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

def finish():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        context = browser.contexts[0]
        page = [pg for pg in context.pages if "studio.youtube.com" in pg.url][0]
        
        print("Dismissing any active suggestion dropdowns...")
        page.keyboard.press("Escape")
        time.sleep(1)
        page.keyboard.press("Escape")
        time.sleep(1)
        
        # 1. Fill Description cleanly
        print("Filling description...")
        desc_success = page.evaluate('''desc => {
            const el = document.querySelector('#description-textarea #textbox, #textbox[aria-label*="description" i]');
            if (!el) return false;
            el.focus();
            document.execCommand('selectAll', false, null);
            document.execCommand('delete', false, null);
            document.execCommand('insertText', false, desc);
            return true;
        }''', DESCRIPTION)
        print("Description inserted?", desc_success)
        time.sleep(1)
        page.keyboard.press("Escape")
        time.sleep(1)
        
        # 2. Audience: Not made for kids
        print("Setting audience: Not made for kids...")
        page.evaluate('''() => {
            const el = document.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
            if (el) el.click();
        }''')
        time.sleep(1)
        
        # 3. ADVANCED CONFIGURATION: AI / ALTERED CONTENT DISCLOSURE
        print("Expanding 'Show more' for advanced configuration...")
        page.evaluate('''() => {
            const toggle = document.querySelector('#toggle-button, ytcp-button#toggle-button');
            if (toggle) toggle.click();
        }''')
        time.sleep(2)
        
        # Inspect and select 'Yes' for Altered / Synthetic Content (AI)
        print("Locating and selecting 'Yes' for Altered / Synthetic Content...")
        ai_res = page.evaluate('''() => {
            const radios = Array.from(document.querySelectorAll('tp-yt-paper-radio-button'));
            
            // Priority 1: Match by name attribute containing ALTERED and YES
            let targetRadio = radios.find(r => {
                const name = (r.getAttribute('name') || '').toUpperCase();
                return name.includes('ALTERED') && name.includes('YES');
            });
            
            // Priority 2: Look within ytcp-altered-content-editor or similar container
            if (!targetRadio) {
                const container = document.querySelector('ytcp-altered-content-editor, ytcp-form-altered-content, [section*="altered" i]');
                if (container) {
                    const cRadios = Array.from(container.querySelectorAll('tp-yt-paper-radio-button'));
                    targetRadio = cRadios.find(r => {
                        const txt = (r.innerText || '').toLowerCase().trim();
                        return txt === 'yes' || txt === 'ya';
                    }) || cRadios[0];
                }
            }
            
            // Priority 3: Search all radios by text and nearby context
            if (!targetRadio) {
                targetRadio = radios.find(r => {
                    const txt = (r.innerText || '').toLowerCase().trim();
                    const parent = r.closest('div, ytcp-form-item, ytcp-paper-radio-group') || {};
                    const parentText = (parent.innerText || '').toLowerCase();
                    return (txt === 'yes' || txt === 'ya') && (parentText.includes('altered') || parentText.includes('sintetis') || parentText.includes('sound') || parentText.includes('ai'));
                });
            }
            
            if (targetRadio) {
                targetRadio.click();
                return {
                    success: true,
                    name: targetRadio.getAttribute('name'),
                    text: targetRadio.innerText.trim()
                };
            }
            
            return {
                success: false,
                radios: radios.map(r => ({ name: r.getAttribute('name'), text: r.innerText.trim() }))
            };
        }''')
        print("Altered Content (AI) selection result:", ai_res)
        time.sleep(2)
        
        # 4. Next buttons through Checks
        print("Stepping through Next buttons...")
        for step in range(3):
            clicked_next = page.evaluate('''() => {
                const btn = document.querySelector('#next-button');
                if (btn) {
                    btn.click();
                    return true;
                }
                return false;
            }''')
            print(f"Clicked Next (step {step+1}): {clicked_next}")
            time.sleep(2.5)
            
        # 5. Visibility: Public
        print("Setting visibility to PUBLIC...")
        pub_res = page.evaluate('''() => {
            const pubRadio = document.querySelector('tp-yt-paper-radio-button[name="PUBLIC"]');
            if (pubRadio) {
                pubRadio.click();
                return 'Clicked Public radio';
            }
            return 'Public radio not found';
        }''')
        print(pub_res)
        time.sleep(2)
        
        # 6. Click Done / Publish
        print("Clicking Done/Publish...")
        publish_res = page.evaluate('''() => {
            const doneBtn = document.querySelector('#done-button');
            if (doneBtn) {
                doneBtn.click();
                return 'Clicked Done button';
            }
            return 'Done button not found';
        }''')
        print(publish_res)
        print("Waiting 12 seconds for YouTube upload dialog to process and close...")
        time.sleep(12)
        
        # 7. Extract video URL / ID from content list
        print("Navigating to shorts content list to retrieve published video ID...")
        page.goto("https://studio.youtube.com/channel/UCyBF1ApOeP2Db0TJ6S47IoQ/videos/short", wait_until="domcontentloaded")
        time.sleep(5)
        
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
            url = f"https://youtube.com/shorts/{vid_id}"
            print("\n" + "="*60)
            print(f"🎉 SUCCESS! Published Shorts URL: {url}")
            print(f"Title: {video_info.get('title')}")
            print("="*60 + "\n")
            return url
        else:
            print("Video published, checking latest video row...")
            return None

if __name__ == "__main__":
    finish()
