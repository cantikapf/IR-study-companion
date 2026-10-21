import urllib.request
import os

OUT_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/raw_assets"
os.makedirs(OUT_DIR, exist_ok=True)

headers = {'User-Agent': 'IRStudyArchivalDownloader/1.0 (contact@studyir.org)'}

assets = [
    {
        "filename": "earth_texture.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/83/Equirectangular_projection_SW.jpg"
    },
    {
        "filename": "patton_portrait.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/0/0a/George_S._Patton_06.jpg"
    },
    {
        "filename": "dummy_tank.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f9/DummyShermanTank.jpg"
    },
    {
        "filename": "rommel_atlantikwall.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Bundesarchiv_Bild_101I-295-1596-10%2C_Frankreich%2C_Atlantikk%C3%BCste%2C_Erwin_Rommel_%28cropped%29.jpg"
    },
    {
        "filename": "panzer_france.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Bundesarchiv_Bild_101I-297-1740-19A%2C_Frankreich%2C_SS-Division_%22Hitlerjugend%22%2C_Panzer_IV.jpg"
    },
    {
        "filename": "dummy_equipment.jpg",
        "url": "https://upload.wikimedia.org/wikipedia/commons/5/54/Dummy_Vehicles_and_Equipment_USED_For_Deception_during_the_Second_World_War_H42531.jpg"
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
