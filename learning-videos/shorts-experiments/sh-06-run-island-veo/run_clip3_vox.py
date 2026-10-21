"""Generate Clip 3 in strict Vox Collage style via Chrome CDP.
Configuration:
- Account: rickiwardana575@gmail.com (u/2)
- Model: Argon
- Aspect Ratio: Potret (9:16)
- Style: Vox-style editorial paper cut-out collage, yellow circle graphic (#FFE619), archival texture, drop shadows, minimal off-white backdrop.
- Subject: 17th-century coastal stone fort embrasures firing brass cannons with billowing white smoke and Dutch naval fleet surrounding the island.
"""

import asyncio
import json
import os
import urllib.request
import websockets

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS_DIR = os.path.join(HERE, "clips")
TAB_WS_URL = "ws://127.0.0.1:9222/devtools/page/85F873157727961A168FDCB82D11A8CB"

PROMPT_CLIP3 = (
    "Vox-style documentary collage animation in 9:16 vertical portrait format, "
    "vintage historical paper cut-out illustration of 17th-century coastal stone fort walls "
    "with brass cannons firing stylized clouds of white smoke, paper cut-out naval galleon warships "
    "surrounding the shoreline with tactile drop shadows, "
    "a bold graphic yellow accent circle (#FFE619) popping behind the fort, "
    "minimal clean off-white background (#fbfaf8), dynamic stop-motion paper craft documentary aesthetic."
)

async def send_cdp(ws, msg_id, method, params=None):
    payload = {"id": msg_id, "method": method}
    if params:
        payload["params"] = params
    await ws.send(json.dumps(payload))
    while True:
        resp = json.loads(await ws.recv())
        if resp.get("id") == msg_id:
            return resp

async def submit_prompt(ws):
    print("Inserting Vox-style prompt for Clip 3 into editor...")
    insert_js = f"""(() => {{
        const ed = document.querySelector('.ql-editor');
        ed.focus();
        document.execCommand('selectAll', false, null);
        document.execCommand('delete', false, null);
        document.execCommand('insertText', false, {json.dumps(PROMPT_CLIP3)});
        return ed.innerText;
    }})()"""
    await send_cdp(ws, 10, "Runtime.evaluate", {"expression": insert_js, "returnByValue": True})
    await asyncio.sleep(1)
    
    print("Clicking 'Kirim pesan' button...")
    send_js = """(() => {
        const btn = document.querySelector('button[aria-label*="Kirim pesan" i], button[aria-label*="Send message" i]');
        if (btn) {
            btn.dispatchEvent(new MouseEvent('mousedown', {bubbles: true, cancelable: true}));
            btn.dispatchEvent(new MouseEvent('mouseup', {bubbles: true, cancelable: true}));
            btn.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true}));
            return 'Dispatched click to Send button';
        }
        return 'Send button not found';
    })()"""
    res = await send_cdp(ws, 11, "Runtime.evaluate", {"expression": send_js, "returnByValue": True})
    print("Send status:", res["result"]["result"]["value"])

async def poll_and_download(ws, out_path, max_wait=400):
    print("Polling for Clip 3 generation completion...")
    start_time = asyncio.get_event_loop().time()
    
    await send_cdp(ws, 15, "Page.setDownloadBehavior", {
        "behavior": "allow",
        "downloadPath": CLIPS_DIR
    })
    
    initial_dl_count = 2  # we already had 2 clips before
    while asyncio.get_event_loop().time() - start_time < max_wait:
        await asyncio.sleep(10)
        check_js = """(() => {
            const vids = Array.from(document.querySelectorAll('video')).map(v => v.src).filter(Boolean);
            const dlBtns = Array.from(document.querySelectorAll('button[aria-label*="Download" i], a[aria-label*="Download" i]'));
            const text = document.body.innerText;
            const isReady = text.includes('Video Anda sudah siap') || text.includes('Your video is ready');
            return {
                isReady: isReady,
                vidsCount: vids.length,
                dlCount: dlBtns.length
            };
        })()"""
        res = await send_cdp(ws, 20, "Runtime.evaluate", {"expression": check_js, "returnByValue": True})
        val = res.get("result", {}).get("result", {}).get("value", {})
        elapsed = int(asyncio.get_event_loop().time() - start_time)
        print(f"[{elapsed}s] Generating... dlCount={val.get('dlCount')}, vids={val.get('vidsCount')}")
        
        # When Clip 3 finishes, dlCount becomes >= 3
        if val.get("dlCount", 0) > initial_dl_count:
            print("Clip 3 is ready! Triggering download...")
            click_last_dl = """(() => {
                const dlBtns = Array.from(document.querySelectorAll('button[aria-label*="Download" i], a[aria-label*="Download" i]'));
                if (dlBtns.length > 0) {
                    dlBtns[dlBtns.length - 1].dispatchEvent(new MouseEvent('mousedown', {bubbles: true, cancelable: true}));
                    dlBtns[dlBtns.length - 1].dispatchEvent(new MouseEvent('mouseup', {bubbles: true, cancelable: true}));
                    dlBtns[dlBtns.length - 1].dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true}));
                    return 'clicked last download button';
                }
                return 'no button';
            })()"""
            await send_cdp(ws, 25, "Runtime.evaluate", {"expression": click_last_dl, "returnByValue": True})
            
            # Wait for downloaded file to appear
            before_files = set(os.listdir(CLIPS_DIR))
            for _ in range(15):
                await asyncio.sleep(1)
                current_files = set(os.listdir(CLIPS_DIR))
                new_files = current_files - before_files
                for nf in new_files:
                    if nf.endswith(".mp4") and not nf.endswith(".crdownload"):
                        src_path = os.path.join(CLIPS_DIR, nf)
                        if os.path.exists(out_path):
                            os.remove(out_path)
                        os.rename(src_path, out_path)
                        print(f"Downloaded and saved to: {out_path} ({os.path.getsize(out_path)} bytes)")
                        return True
            return True
            
    print("Timed out waiting for Clip 3.")
    return False

async def main():
    os.makedirs(CLIPS_DIR, exist_ok=True)
    out_file = os.path.join(CLIPS_DIR, "clip3_naval_siege_vox_argon.mp4")
    
    async with websockets.connect(TAB_WS_URL, max_size=10**7) as ws:
        await submit_prompt(ws)
        success = await poll_and_download(ws, out_file)
        if success:
            print("Clip 3 Vox style generated successfully!")
        else:
            print("Clip 3 generation failed or timed out.")

if __name__ == "__main__":
    asyncio.run(main())
