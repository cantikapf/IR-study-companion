import urllib.request
import os

OUT_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
os.makedirs(OUT_DIR, exist_ok=True)

headers = {'User-Agent': 'IRStudyArchivalDownloader/1.0 (contact@studyir.org)'}

assets = [
    {
        "filename": "eden_portrait.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Anthony_Eden_%28retouched%29.jpg"
    },
    {
        "filename": "eisenhower_portrait.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/63/Dwight_D._Eisenhower%2C_official_photo_portrait%2C_May_29%2C_1959.jpg"
    },
    {
        "filename": "nasser_portrait.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/86/President_Gamal_Abdel_Nasser.jpg"
    },
    {
        "filename": "pound_banknote.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/24/Bank_of_England_%C2%A35_note_1931.jpg"
    },
    {
        "filename": "suez_canal_map.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/50/Suez_Canal%2C_Egypt1.jpg"
    },
    {
        "filename": "operation_musketeer.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b6/The_Suez_Crisis_%28operation_Musketeer%29_1956_MH23500.jpg"
    },
    {
        "filename": "tanker_ship.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/StateLibQld_1_148219_Olympic_Torch_%28ship%29.jpg"
    },
    {
        "filename": "alahram_newspaper.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Al-Ahram_Newspaper_Publish_Suez_Canal_Nationalization.jpg"
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
