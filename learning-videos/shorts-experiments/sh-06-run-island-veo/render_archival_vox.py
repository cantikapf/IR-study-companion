"""Deterministic frame-by-frame CDP renderer for 100% Authentic Archival Vox Short.
Renders index_archival.html at 1080x1920 @ 30 FPS.
Muxes with voiceover.mp3.
"""

import asyncio
import os
import subprocess
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(HERE, "index_pure_archival.html").replace("\\", "/")
AUDIO_PATH = os.path.join(HERE, "audio", "voiceover.mp3")
LOCAL_OUT = os.path.join(HERE, "sh06_pure_archival_vox_1080p.mp4")
EXPORTS_DIR = os.path.abspath(os.path.join(HERE, "../../../learning-videos/exports"))
EXPORTS_OUT = os.path.join(EXPORTS_DIR, "SH06_The_Island_Traded_for_New_York_Short_1080p.mp4")

FPS = 30
DURATION = 36.17
TOTAL_FRAMES = int(DURATION * FPS)

async def main():
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    print("=" * 60)
    print(f"STARTING ARCHIVAL VOX RENDER (Total Frames: {TOTAL_FRAMES} @ {FPS} fps)")
    print("=" * 60)

    # Launch Chrome via Playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
            headless=True,
            args=[
                "--disable-gpu-vsync",
                "--disable-background-timer-throttling",
                "--disable-renderer-backgrounding"
            ]
        )
        page = await browser.new_page(viewport={"width": 1080, "height": 1920})
        await page.goto(f"file:///{HTML_PATH}")
        await page.wait_for_timeout(1000)

        # Pause timeline
        await page.evaluate("() => { masterTl.pause(); masterTl.time(0); }")

        # Spawn ffmpeg image2pipe
        cmd = [
            "ffmpeg", "-y",
            "-f", "image2pipe",
            "-vcodec", "mjpeg",
            "-r", str(FPS),
            "-i", "-",
            "-i", AUDIO_PATH,
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            "-r", str(FPS),
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            LOCAL_OUT
        ]
        ffmpeg_proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

        client = await page.context.new_cdp_session(page)

        for f in range(TOTAL_FRAMES):
            t = f / FPS
            await page.evaluate(f"t => {{ masterTl.time(t); }}", t)
            shot = await client.send("Page.captureScreenshot", {"format": "jpeg", "quality": 95})
            import base64
            frame_bytes = base64.b64decode(shot["data"])
            ffmpeg_proc.stdin.write(frame_bytes)

            if f % 150 == 0 or f == TOTAL_FRAMES - 1:
                pct = int((f / TOTAL_FRAMES) * 100)
                print(f"Rendering frame {f}/{TOTAL_FRAMES} ({pct}%) - t={t:.2f}s")

        ffmpeg_proc.stdin.close()
        ffmpeg_proc.wait()
        await browser.close()

    print(f"Rendered local output: {LOCAL_OUT} ({os.path.getsize(LOCAL_OUT)} bytes)")
    import shutil
    shutil.copy2(LOCAL_OUT, EXPORTS_OUT)
    print(f"Propagated to exports: {EXPORTS_OUT} ({os.path.getsize(EXPORTS_OUT)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())
