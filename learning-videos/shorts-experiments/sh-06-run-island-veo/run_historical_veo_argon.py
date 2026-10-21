"""Generate 100% historical Veo video clips via Chrome CDP.
Configuration:
- Account: rickiwardana575@gmail.com (u/2)
- Model: Argon (verified active)
- Aspect Ratio: Potret (9:16) (verified active)
- Prompt: Historical 17th-century European sailing galleon & Banda Sea volcanic island
"""

import asyncio
import json
import os
import urllib.request
import websockets

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS_DIR = os.path.join(HERE, "clips")
TAB_WS_URL = "ws://127.0.0.1:9222/devtools/page/35615497696AEB63C582C93D0ECBC3A0"

PROMPT = (
    "Cinematic vertical 9:16 portrait video, historical 17th-century European wooden sailing ship galleon "
    "navigating across emerald tropical waters toward a lush volcanic island under dramatic sunlight, "
    "photorealistic documentary footage, authentic naval history, slow majestic camera push forward."
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
    print("Populating prompt in Quill editor...")
    insert_js = f"""(() => {{
        const ed = document.querySelector('.ql-editor');
        ed.focus();
        document.execCommand('selectAll', false, null);
        document.execCommand('delete', false, null);
        document.execCommand('insertText', false, {json.dumps(PROMPT)});
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

async def poll_video(ws, out_path, max_wait=400):
    print("Polling for video generation completion (non-destructive)...")
    start_time = asyncio.get_event_loop().time()
    while asyncio.get_event_loop().time() - start_time < max_wait:
        await asyncio.sleep(10)
        check_js = """(() => {
            const vids = Array.from(document.querySelectorAll('video')).map(v => v.src).filter(Boolean);
            const dl = Array.from(document.querySelectorAll('button[aria-label*="Download" i], a[aria-label*="Download" i]')).length;
            const text = document.body.innerText;
            const isReady = text.includes('Video Anda sudah siap') || text.includes('Your video is ready') || dl > 0;
            return {
                isReady: isReady,
                vids: vids,
                dlCount: dl
            };
        })()"""
        res = await send_cdp(ws, 20, "Runtime.evaluate", {"expression": check_js, "returnByValue": True})
        val = res.get("result", {}).get("result", {}).get("value", {})
        elapsed = int(asyncio.get_event_loop().time() - start_time)
        print(f"[{elapsed}s] Generating... isReady={val.get('isReady')}, vids={len(val.get('vids', []))}")
        
        if val.get("isReady") and val.get("vids"):
            video_url = val["vids"][-1]
            print(f"Video is ready! Downloading from: {video_url[:60]}...")
            urllib.request.urlretrieve(video_url, out_path)
            print(f"Downloaded video to {out_path} (size: {os.path.getsize(out_path)} bytes)")
            return True
            
    print("Timed out waiting for video.")
    return False

async def main():
    os.makedirs(CLIPS_DIR, exist_ok=True)
    out_file = os.path.join(CLIPS_DIR, "clip1_historical_galleon_916_argon.mp4")
    
    async with websockets.connect(TAB_WS_URL, max_size=10**7) as ws:
        await submit_prompt(ws)
        success = await poll_video(ws, out_file)
        if success:
            print("Video generated and saved successfully!")
        else:
            print("Video generation failed or timed out.")

if __name__ == "__main__":
    asyncio.run(main())
