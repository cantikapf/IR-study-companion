"""Generate 100% historical Veo video clips via Chrome CDP.
Strictly follows creative/gemini-veo-video-automation-v4:
- Direct CDP WebSocket
- Aspect Ratio Portrait (9:16)
- Pure historical prompts (17th-century European sailing galleon & nutmeg)
- ZERO clicks on template cards
- Native events to submit and poll completion
"""

import asyncio
import json
import os
import urllib.request
import websockets

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS_DIR = os.path.join(HERE, "clips")
TAB_WS_URL = "ws://127.0.0.1:9222/devtools/page/ADF299D2E0ABACA26420909ECFB2B1AC"

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

async def set_portrait(ws):
    print("Verifying Aspect Ratio...")
    # Click aspect ratio button
    res = await send_cdp(ws, 1, "Runtime.evaluate", {
        "expression": "(() => { const b = document.querySelector('button[aria-label*=\"Aspect ratio\"]'); if (b) b.click(); return !!b; })()",
        "returnByValue": True
    })
    print("Clicked aspect ratio dropdown:", res["result"]["result"]["value"])
    await asyncio.sleep(1)
    
    # Click second item: Portrait (9:16)
    click_p = """(() => {
        const items = Array.from(document.querySelectorAll('input-companion-item'));
        if (items.length > 1) {
            items[1].click();
            return 'clicked: ' + items[1].innerText;
        }
        return 'no item';
    })()"""
    res2 = await send_cdp(ws, 2, "Runtime.evaluate", {"expression": click_p, "returnByValue": True})
    print("Item click:", res2["result"]["result"]["value"])
    await asyncio.sleep(1)
    
    # Verify
    verify = "document.querySelector('button[aria-label*=\"Aspect ratio\"]')?.getAttribute('aria-label')"
    res3 = await send_cdp(ws, 3, "Runtime.evaluate", {"expression": verify, "returnByValue": True})
    print("Current Aspect Ratio:", res3["result"]["result"]["value"])

async def submit_historical_prompt(ws):
    print("Inserting prompt into editor...")
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
    
    print("Clicking Send message button...")
    send_js = """(() => {
        const btn = document.querySelector('button[aria-label*="Send message" i]');
        if (btn) {
            const ev1 = new MouseEvent('mousedown', {bubbles: true, cancelable: true, view: window});
            const ev2 = new MouseEvent('mouseup', {bubbles: true, cancelable: true, view: window});
            const ev3 = new MouseEvent('click', {bubbles: true, cancelable: true, view: window});
            btn.dispatchEvent(ev1);
            btn.dispatchEvent(ev2);
            btn.dispatchEvent(ev3);
            return 'Dispatched click events to Send button';
        }
        return 'Send button not found';
    })()"""
    res = await send_cdp(ws, 11, "Runtime.evaluate", {"expression": send_js, "returnByValue": True})
    print("Send result:", res["result"]["result"]["value"])

async def poll_video(ws, out_path, max_wait=360):
    print("Polling for video generation completion...")
    start_time = asyncio.get_event_loop().time()
    while asyncio.get_event_loop().time() - start_time < max_wait:
        await asyncio.sleep(8)
        check_js = """(() => {
            const vids = Array.from(document.querySelectorAll('video')).map(v => v.src).filter(Boolean);
            const dl = Array.from(document.querySelectorAll('button[aria-label*="Download video" i], a[aria-label*="Download video" i]')).length;
            const text = document.body.innerText;
            const isReady = text.includes('Your video is ready') || dl > 0;
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
    out_file = os.path.join(CLIPS_DIR, "clip1_historical_galleon_916.mp4")
    
    async with websockets.connect(TAB_WS_URL) as ws:
        await set_portrait(ws)
        await submit_historical_prompt(ws)
        success = await poll_video(ws, out_file)
        if success:
            print("Historical clip successfully generated!")
        else:
            print("Generation failed or timed out.")

if __name__ == "__main__":
    asyncio.run(main())
