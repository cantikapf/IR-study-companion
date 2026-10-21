import os
import cv2
import numpy as np
from PIL import Image

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def make_perfect_silhouette_sticker(rgba_np, outline_width=14, shadow_offset=(14, 14)):
    """
    Creates a mathematically flawless sticker using OpenCV dilation:
    - Zero stepped/ghost outlines
    - Solid pure white 14px stroke
    - Pure 0-blur hard offset shadow
    """
    h, w, c = rgba_np.shape
    pad = outline_width * 2 + 40
    new_h = h + pad * 2
    new_w = w + pad * 2
    
    # Extract alpha
    alpha = rgba_np[:, :, 3]
    # Threshold to strict binary (0 or 255) to eliminate any semi-transparent fringe
    _, binary_alpha = cv2.threshold(alpha, 128, 255, cv2.THRESH_BINARY)
    
    # Pad binary alpha
    padded_alpha = np.zeros((new_h, new_w), dtype=np.uint8)
    padded_alpha[pad:pad+h, pad:pad+w] = binary_alpha
    
    # Mathematical morphological dilation with circular kernel
    ksize = outline_width * 2 + 1
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize))
    dilated_mask = cv2.dilate(padded_alpha, kernel)
    
    # Output RGBA canvas
    canvas = np.zeros((new_h, new_w, 4), dtype=np.uint8)
    
    # 1. Hard 0-blur drop shadow (Black 100% alpha)
    sx, sy = shadow_offset
    # Shift dilated mask by (sx, sy)
    M = np.float32([[1, 0, sx], [0, 1, sy]])
    shadow_mask = cv2.warpAffine(dilated_mask, M, (new_w, new_h))
    canvas[shadow_mask == 255] = [0, 0, 0, 255]
    
    # 2. Solid White Stroke
    canvas[dilated_mask == 255] = [255, 255, 255, 255]
    
    # 3. Paste Original RGBA Foreground
    fg_mask = binary_alpha == 255
    canvas[pad:pad+h, pad:pad+w][fg_mask] = rgba_np[fg_mask]
    
    return Image.fromarray(canvas)

# -------------------------------------------------------------------
# 1. Anthony Eden
# -------------------------------------------------------------------
print("Generating mathematically smooth Anthony Eden sticker...")
eden_raw = cv2.imread(os.path.join(RAW_DIR, "eden_portrait.jpg"))
eh, ew = eden_raw.shape[:2]
eden_crop = eden_raw[int(eh*0.02):int(eh*0.75), int(ew*0.12):int(ew*0.88)]
eden_crop = cv2.resize(eden_crop, (540, 640), interpolation=cv2.INTER_LANCZOS4)
ch, cw = eden_crop.shape[:2]

mask = np.zeros((ch, cw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(eden_crop, mask, (15, 10, cw-30, ch-20), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

# Single largest component
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

# Smooth bottom curve
for y in range(int(ch*0.78), ch):
    factor = (y - int(ch*0.78)) / (ch - int(ch*0.78))
    cutoff_x = int(factor * factor * (cw * 0.40))
    clean_mask[y, :cutoff_x] = 0
    clean_mask[y, cw - cutoff_x:] = 0

eden_rgba = cv2.cvtColor(eden_crop, cv2.COLOR_BGR2RGBA)
eden_rgba[:, :, 3] = clean_mask
sticker_eden = make_perfect_silhouette_sticker(eden_rgba, outline_width=14)
sticker_eden.save(os.path.join(ASSET_DIR, "sticker_anthony_eden.png"))
print("Saved perfect sticker_anthony_eden.png")

# -------------------------------------------------------------------
# 2. Eisenhower
# -------------------------------------------------------------------
print("Generating mathematically smooth Eisenhower sticker...")
ike_raw = cv2.imread(os.path.join(RAW_DIR, "eisenhower_portrait.jpg"))
ih, iw = ike_raw.shape[:2]
ike_crop = ike_raw[int(ih*0.06):int(ih*0.75), int(iw*0.14):int(iw*0.86)]
ike_crop = cv2.resize(ike_crop, (540, 640), interpolation=cv2.INTER_LANCZOS4)
ich, icw = ike_crop.shape[:2]

mask = np.zeros((ich, icw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(ike_crop, mask, (15, 10, icw-30, ich-20), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

for y in range(int(ich*0.80), ich):
    factor = (y - int(ich*0.80)) / (ich - int(ich*0.80))
    cutoff_x = int(factor * factor * (icw * 0.38))
    clean_mask[y, :cutoff_x] = 0
    clean_mask[y, icw - cutoff_x:] = 0

ike_rgba = cv2.cvtColor(ike_crop, cv2.COLOR_BGR2RGBA)
ike_rgba[:, :, 3] = clean_mask
sticker_ike = make_perfect_silhouette_sticker(ike_rgba, outline_width=14)
sticker_ike.save(os.path.join(ASSET_DIR, "sticker_eisenhower.png"))
print("Saved perfect sticker_eisenhower.png")

# -------------------------------------------------------------------
# 3. Tanker Ship
# -------------------------------------------------------------------
print("Generating mathematically smooth Tanker Ship sticker...")
ship_raw = cv2.imread(os.path.join(RAW_DIR, "tanker_ship.jpg"))
sh, sw = ship_raw.shape[:2]
ship_crop = ship_raw[int(sh*0.22):int(sh*0.78), int(sw*0.04):int(sw*0.96)]
ship_crop = cv2.resize(ship_crop, (640, 320), interpolation=cv2.INTER_LANCZOS4)
sch, scw = ship_crop.shape[:2]

mask = np.zeros((sch, scw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(ship_crop, mask, (10, 10, scw-20, sch-15), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

ship_rgba = cv2.cvtColor(ship_crop, cv2.COLOR_BGR2RGBA)
ship_rgba[:, :, 3] = clean_mask
sticker_ship = make_perfect_silhouette_sticker(ship_rgba, outline_width=14)
sticker_ship.save(os.path.join(ASSET_DIR, "sticker_tanker.png"))
print("Saved perfect sticker_tanker.png")

print("All perfect stickers created!")
