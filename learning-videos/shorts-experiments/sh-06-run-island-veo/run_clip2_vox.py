"""Generate Clip 2 in strict Vox Collage style via Chrome CDP.
Configuration:
- Account: rickiwardana575@gmail.com (u/2)
- Model: Argon
- Aspect Ratio: Potret (9:16)
- Style: Vox-style editorial paper cut-out collage, yellow circle graphic (#FFE619), archival texture, drop shadows, minimal off-white backdrop.
- Subject: 17th-century sailor hands holding ripe cracked nutmeg and red mace.
"""

import asyncio
import json
import os
import urllib.request
import websockets

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS_DIR = os.path.join(HERE, "clips")
TAB_WS_URL = "ws://127.0.0.1:9222/devtools/page/85F873157727961A168FDCB82D11A8CB"

PROMPT_CLIP2 = (
    "Vox-style documentary collage animation in 9:16 vertical portrait format, "
    "vintage botanical paper cut-out illustration of hands holding a cracked ripe nutmeg fruit "
    "with vibrant crimson red mace, textured paper craft cut-out with tactile edges and realistic drop shadow, "
    "a bold graphic yellow circle (#FFE619) scaling up behind the nutmeg fruit, "
    "minimal clean off-white background (#fbfaf8), fast-paced modern editorial documentary aesthetic."
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
    print("Inserting Vox-style prompt into editor...")
    insert_js = f"""(() => {{
        const ed = document.querySelector('.ql-editor');
        ed.focus();
        document.execCommand('selectAll', false, null);
        document.execCommand('delete', false, null);
        document.execCommand('insertText', false, {json.dumps(PROMPT_CLIP2)});
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
    print("Polling for video generation completion...")
    start_time = asyncio.get_event_loop().time()
    
    # Configure download behavior
    await send_cdp(ws, 15, "Page.setDownloadBehavior", {
        "behavior": "allow",
        "downloadPath": CLIPS_DIR
    })
    
    initial_dl_count = 1  # we already had 1 from clip 1
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
        
        # When new video finishes, dlCount increases or vidsCount increases
        if val.get("dlCount", 0) > initial_dl_count or (val.get("isReady") and val.get("vidsCount", 0) >= 2):
            print("Clip 2 is ready! Triggering download...")
            click_last_dl = """(() => {
                const dlBtns = Array.from(document.querySelectorAll('button[aria-label*="Download" i], a[aria-label*="Download" i]'));
                if (dlBtns.length > 0) {
                    dlBtns[dlBtns.length - 1].click();
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
                        os.rename(src_path, out_path)
                        print(f"Downloaded and renamed to: {out_path} ({os.path.getsize(out_path)} bytes)")
                        return True
            return True
            
    print("Timed out waiting for video.")
    return False

async def main():
    os.makedirs(CLIPS_DIR, exist_ok=True)
    out_file = os.path.join(CLIPS_DIR, "clip2_nutmeg_vox_argon.mp4")
    
    async with websockets.connect(TAB_WS_URL, max_size=10**7) as ws:
        await submit_prompt(ws)
        success = await poll_and_download(ws, out_file)
        if success:
            print("Clip 2 Vox style generated successfully!")
        else:
            print("Clip 2 generation failed or timed out.")

if __name__ == "__main__":
    asyncio.run(main())
