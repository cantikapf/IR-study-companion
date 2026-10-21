"""Automate Gemini Veo clip generation via Chrome CDP WebSocket.
Handles portrait aspect ratio, prompt submission, non-destructive completion polling,
and direct clip stream fetching.
"""

import asyncio
import json
import os
import urllib.request
import websockets

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST_FILE = os.path.join(HERE, "prompts_manifest.json")
CLIPS_DIR = os.path.join(HERE, "clips")

async def get_gemini_ws():
    res = urllib.request.urlopen("http://127.0.0.1:9222/json/list")
    tabs = json.loads(res.read().decode())
    target = [t for t in tabs if "gemini.google.com/videos" in t.get("url", "")]
    if not target:
        # open new tab
        req = urllib.request.Request("http://127.0.0.1:9222/json/new?https://gemini.google.com/videos", method="PUT")
        tab = json.loads(urllib.request.urlopen(req).read().decode())
        await asyncio.sleep(3)
        return tab["webSocketDebuggerUrl"]
    return target[0]["webSocketDebuggerUrl"]

async def send_cdp(ws, msg_id, method, params=None):
    payload = {"id": msg_id, "method": method}
    if params:
        payload["params"] = params
    await ws.send(json.dumps(payload))
    while True:
        resp = json.loads(await ws.recv())
        if resp.get("id") == msg_id:
            return resp

async def set_aspect_ratio_portrait(ws):
    print("Verifying Aspect Ratio...")
    # Check current label
    check_js = 'document.querySelector(\'button[aria-label*="Aspect ratio"]\')?.getAttribute("aria-label") || ""'
    res = await send_cdp(ws, 10, "Runtime.evaluate", {"expression": check_js, "returnByValue": True})
    label = res.get("result", {}).get("result", {}).get("value", "")
    if "Portrait" in label or "9:16" in label:
        print("Aspect ratio already Portrait (9:16).")
        return True
    
    print("Switching aspect ratio to Portrait (9:16)...")
    # Click aspect button
    get_coords = '''(() => {
        const btn = document.querySelector('button[aria-label*="Aspect ratio"]');
        if (!btn) return null;
        const r = btn.getBoundingClientRect();
        return {x: r.x + r.width/2, y: r.y + r.height/2};
    })()'''
    res = await send_cdp(ws, 11, "Runtime.evaluate", {"expression": get_coords, "returnByValue": True})
    coords = res.get("result", {}).get("result", {}).get("value")
    if not coords:
        print("Could not find aspect ratio button!")
        return False
        
    await send_cdp(ws, 12, "Input.dispatchMouseEvent", {"type": "mousePressed", "x": coords["x"], "y": coords["y"], "button": "left", "clickCount": 1})
    await send_cdp(ws, 13, "Input.dispatchMouseEvent", {"type": "mouseReleased", "x": coords["x"], "y": coords["y"], "button": "left", "clickCount": 1})
    await asyncio.sleep(1)
    
    # Click Portrait option
    get_portrait = '''(() => {
        const item = Array.from(document.querySelectorAll('input-companion-item, [role="menuitem"], .mat-mdc-menu-item'))
                         .find(el => el.textContent && el.textContent.includes('Portrait'));
        if (!item) return null;
        const r = item.getBoundingClientRect();
        return {x: r.x + r.width/2, y: r.y + r.height/2};
    })()'''
    res = await send_cdp(ws, 14, "Runtime.evaluate", {"expression": get_portrait, "returnByValue": True})
    p_coords = res.get("result", {}).get("result", {}).get("value")
    if p_coords:
        await send_cdp(ws, 15, "Input.dispatchMouseEvent", {"type": "mousePressed", "x": p_coords["x"], "y": p_coords["y"], "button": "left", "clickCount": 1})
        await send_cdp(ws, 16, "Input.dispatchMouseEvent", {"type": "mouseReleased", "x": p_coords["x"], "y": p_coords["y"], "button": "left", "clickCount": 1})
        await asyncio.sleep(1)
        print("Selected Portrait (9:16).")
        return True
    return False

async def submit_prompt(ws, prompt_text):
    print(f"Typing prompt: {prompt_text[:60]}...")
    type_js = f'''(() => {{
        const ed = document.querySelector('.ql-editor');
        if (!ed) return 'no editor';
        ed.focus();
        document.execCommand('selectAll', false, null);
        document.execCommand('delete', false, null);
        document.execCommand('insertText', false, {json.dumps(prompt_text)});
        return 'typed';
    }})()'''
    await send_cdp(ws, 20, "Runtime.evaluate", {"expression": type_js, "returnByValue": True})
    await asyncio.sleep(1)
    
    # Click Send
    send_js = '''(() => {
        const sendBtn = document.querySelector('button[aria-label*="Send message" i], button.send-button');
        if (sendBtn) {
            sendBtn.click();
            return 'clicked send button';
        }
        return 'no send button';
    })()'''
    res = await send_cdp(ws, 21, "Runtime.evaluate", {"expression": send_js, "returnByValue": True})
    print("Send status:", res.get("result", {}).get("result", {}).get("value"))

async def poll_video_completion(ws, out_filepath, max_wait=400):
    print("Polling for video generation completion (non-destructive)...")
    start_time = asyncio.get_event_loop().time()
    last_src = None
    
    while asyncio.get_event_loop().time() - start_time < max_wait:
        check_js = '''(() => {
            const vids = Array.from(document.querySelectorAll('video'));
            const downloadBtns = Array.from(document.querySelectorAll('button[aria-label*="Download video" i]'));
            const generating = Array.from(document.querySelectorAll('*')).some(el => el.textContent && el.textContent.includes('generating your video'));
            const src = vids.length > 0 ? vids[vids.length - 1].src : null;
            return {
                videoCount: vids.length,
                downloadCount: downloadBtns.length,
                isGenerating: generating,
                latestSrc: src
            };
        })()'''
        res = await send_cdp(ws, 30, "Runtime.evaluate", {"expression": check_js, "returnByValue": True})
        status = res.get("result", {}).get("result", {}).get("value", {})
        
        src = status.get("latestSrc")
        if src and src.startswith("http") and not status.get("isGenerating"):
            print(f"Video ready! Source URL detected: {src[:60]}...")
            urllib.request.urlretrieve(src, out_filepath)
            print(f"Downloaded video to {out_filepath}")
            return True
            
        elapsed = int(asyncio.get_event_loop().time() - start_time)
        print(f"[{elapsed}s] Generating in progress... (isGenerating: {status.get('isGenerating')})")
        await asyncio.sleep(10)
        
    print("Timeout waiting for video generation.")
    return False

async def main():
    os.makedirs(CLIPS_DIR, exist_ok=True)
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        
    ws_url = await get_gemini_ws()
    print("CDP Connected to:", ws_url)
    
    async with websockets.connect(ws_url, max_size=10**8) as ws:
        await set_aspect_ratio_portrait(ws)
        
        # Test generation with clip 1
        clip = manifest[0]
        out_file = os.path.join(CLIPS_DIR, f"{clip['name']}.mp4")
        if os.path.exists(out_file):
            print(f"Clip {out_file} already exists. Skipping.")
        else:
            await submit_prompt(ws, clip["prompt"])
            success = await poll_video_completion(ws, out_file)
            if not success:
                print("Failed to generate clip 1.")

if __name__ == "__main__":
    asyncio.run(main())
