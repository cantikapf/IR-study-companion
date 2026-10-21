import urllib.request
import os

OUT_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/raw_assets"
os.makedirs(OUT_DIR, exist_ok=True)

headers = {'User-Agent': 'IRStudyArchivalDownloader/1.0 (contact@studyir.org)'}

assets = [
    {
        "filename": "motte_trojan_horse.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Henri-Paul_Motte_-_Le_Cheval_de_Troie.jpg"
    },
    {
        "filename": "tiepolo_procession.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/33/The_Procession_of_the_Trojan_Horse_in_Troy_by_Giovanni_Domenico_Tiepolo_%28cropped%29.jpg"
    },
    {
        "filename": "mykonos_pithos_relief.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/18/Mykonos_vase%2C_relief_pithos%2C_capture_of_Troy%2C_670_BC%2C_AM_Mykonos%2C_2240%2C_177256.jpg"
    }
]

for item in assets:
    target_path = os.path.join(OUT_DIR, item["filename"])
    if os.path.exists(target_path) and os.path.getsize(target_path) > 1000:
        print(f"Skipping {item['filename']} (already downloaded)")
        continue
    print(f"Downloading {item['filename']}...")
    req = urllib.request.Request(item["url"], headers=headers)
    try:
        with urllib.request.urlopen(req) as resp, open(target_path, "wb") as f:
            f.write(resp.read())
        print(f"Saved {item['filename']} ({os.path.getsize(target_path)} bytes)")
    except Exception as e:
        print(f"Failed to download {item['filename']}: {e}")

print("Asset download process completed.")
