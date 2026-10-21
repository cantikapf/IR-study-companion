"""Generate Clip 4 in strict Vox Collage style via Chrome CDP on Account 4 (u/3).
Configuration:
- Account: nkuni3911@gmail.com (u/3)
- Model: Argon (verified active)
- Aspect Ratio: Portrait (9:16) (verified active)
- Style: Vox-style editorial paper cut-out collage, yellow circle graphic (#FFE619), archival texture, drop shadows, minimal off-white backdrop.
- Subject: 1667 diplomatic parchment treaty with cracked red wax seal on a rustic wooden table, antique quill pen beside it, paper cut-out maps of Manhattan and Run Island swapping places.
"""

import asyncio
import json
import os
import urllib.request
import websockets

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS_DIR = os.path.join(HERE, "clips")
TAB_ID = "0CEC7E227DC888EBE0EEBB51E2A48C71"

PROMPT_CLIP4 = (
    "Vox-style documentary collage animation in 9:16 vertical portrait format, "
    "vintage historical paper cut-out of 1667 Treaty of Breda parchment with cracked red wax seal, "
    "antique quill pen resting beside it with paper drop shadow, "
    "two stylized paper cut-out island maps labeled Manhattan and Run Island sliding and exchanging positions, "
    "a bold graphic yellow accent circle (#FFE619) popping in the background, "
    "minimal clean off-white background (#fbfaf8), dynamic stop-motion paper craft documentary aesthetic."
)

async def get_ws_url():
    res = urllib.request.urlopen("http://127.0.0.1:9222/json/list")
    tabs = json.loads(res.read().decode())
    target = [t for t in tabs if TAB_ID in t.get("id", "")][0]
    return target["webSocketDebuggerUrl"]

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
    print("Inserting Vox-style prompt for Clip 4 into editor...")
    insert_js = f"""(() => {{
        const ed = document.querySelector('.ql-editor');
        ed.focus();
        document.execCommand('selectAll', false, null);
        document.execCommand('delete', false, null);
        document.execCommand('insertText', false, {json.dumps(PROMPT_CLIP4)});
        return ed.innerText;
    }})()"""
    await send_cdp(ws, 10, "Runtime.evaluate", {"expression": insert_js, "returnByValue": True})
    await asyncio.sleep(1)
    
    print("Clicking 'Send message' button...")
    send_js = """(() => {
        const btn = document.querySelector('button[aria-label*="Send message" i], button[aria-label*="Kirim pesan" i]');
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
    print("Polling for Clip 4 generation completion...")
    start_time = asyncio.get_event_loop().time()
    
    await send_cdp(ws, 15, "Page.setDownloadBehavior", {
        "behavior": "allow",
        "downloadPath": CLIPS_DIR
    })
    
    while asyncio.get_event_loop().time() - start_time < max_wait:
        await asyncio.sleep(10)
        try:
            check_js = """(() => {
                const vids = Array.from(document.querySelectorAll('video')).map(v => v.src).filter(Boolean);
                const dlBtns = Array.from(document.querySelectorAll('button[aria-label*="Download" i], a[aria-label*="Download" i]'));
                const text = document.body.innerText;
                const isReady = text.includes('Your video is ready') || text.includes('Video Anda sudah siap') || dlBtns.length > 0;
                return {
                    isReady: isReady,
                    vidsCount: vids.length,
                    dlCount: dlBtns.length
                };
            })()"""
            res = await send_cdp(ws, 20, "Runtime.evaluate", {"expression": check_js, "returnByValue": True})
            val = res.get("result", {}).get("result", {}).get("value", {})
            elapsed = int(asyncio.get_event_loop().time() - start_time)
            print(f"[{elapsed}s] Generating... dlCount={val.get('dlCount')}, isReady={val.get('isReady')}")
            
            if val.get("dlCount", 0) > 0 or val.get("isReady"):
                print("Clip 4 is ready! Triggering download...")
                before_files = set(os.listdir(CLIPS_DIR))
                click_dl = """(() => {
                    const dlBtns = Array.from(document.querySelectorAll('button[aria-label*="Download" i], a[aria-label*="Download" i]'));
                    if (dlBtns.length > 0) {
                        dlBtns[0].dispatchEvent(new MouseEvent('mousedown', {bubbles: true, cancelable: true}));
                        dlBtns[0].dispatchEvent(new MouseEvent('mouseup', {bubbles: true, cancelable: true}));
                        dlBtns[0].dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true}));
                        return 'clicked download';
                    }
                    return 'no download button';
                })()"""
                await send_cdp(ws, 25, "Runtime.evaluate", {"expression": click_dl, "returnByValue": True})
                
                for _ in range(25):
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
        except Exception as e:
            print("Poll check warning:", e)
            await asyncio.sleep(5)
            
    print("Timed out waiting for Clip 4.")
    return False

async def main():
    os.makedirs(CLIPS_DIR, exist_ok=True)
    out_file = os.path.join(CLIPS_DIR, "clip4_treaty_breda_vox_argon.mp4")
    ws_url = await get_ws_url()
    
    async with websockets.connect(ws_url, max_size=10**7) as ws:
        await submit_prompt(ws)
        success = await poll_and_download(ws, out_file)
        if success:
            print("Clip 4 Vox style generated successfully!")
        else:
            print("Clip 4 generation failed or timed out.")

if __name__ == "__main__":
    asyncio.run(main())
