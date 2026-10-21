import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/assets"

def make_euclidean_sticker(rgba_np, outline_width=16, shadow_offset=(16, 16)):
    """
    Creates an ultra-smooth Euclidean distance transform sticker:
    - Distance transform computes exact Euclidean distance (L2) from boundary
    - Perfectly rounded, continuous stroke
    - Hard 0-blur drop shadow
    """
    h, w, c = rgba_np.shape
    pad = outline_width * 2 + 50
    new_h = h + pad * 2
    new_w = w + pad * 2
    
    alpha = rgba_np[:, :, 3]
    _, bin_alpha = cv2.threshold(alpha, 128, 255, cv2.THRESH_BINARY)
    
    padded_alpha = np.zeros((new_h, new_w), dtype=np.uint8)
    padded_alpha[pad:pad+h, pad:pad+w] = bin_alpha
    
    # Exact Euclidean Distance Transform
    inv_mask = cv2.bitwise_not(padded_alpha)
    dist = cv2.distanceTransform(inv_mask, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
    
    # Smooth Euclidean contour stroke
    stroke_mask = np.where(dist <= outline_width, 255, 0).astype(np.uint8)
    # Morphological smooth
    stroke_mask = cv2.GaussianBlur(stroke_mask, (7, 7), 0)
    _, stroke_mask = cv2.threshold(stroke_mask, 128, 255, cv2.THRESH_BINARY)
    
    # Canvas
    canvas = np.zeros((new_h, new_w, 4), dtype=np.uint8)
    
    # 1. Hard Drop Shadow (135 deg)
    sx, sy = shadow_offset
    M = np.float32([[1, 0, sx], [0, 1, sy]])
    shadow_mask = cv2.warpAffine(stroke_mask, M, (new_w, new_h))
    canvas[shadow_mask == 255] = [0, 0, 0, 255]
    
    # 2. Solid White Stroke
    canvas[stroke_mask == 255] = [255, 255, 255, 255]
    
    # 3. Composite FG
    fg_mask = bin_alpha == 255
    canvas[pad:pad+h, pad:pad+w][fg_mask] = rgba_np[fg_mask]
    
    return Image.fromarray(canvas)

print("Testing Euclidean distance sticker for Anthony Eden...")
eden_raw = cv2.imread(os.path.join(RAW_DIR, "eden_portrait.jpg"))
eh, ew = eden_raw.shape[:2]
eden_crop = eden_raw[int(eh*0.01):int(eh*0.75), int(ew*0.06):int(ew*0.94)]
eden_crop = cv2.resize(eden_crop, (680, 750), interpolation=cv2.INTER_LANCZOS4)
ch, cw = eden_crop.shape[:2]

mask = np.zeros((ch, cw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(eden_crop, mask, (8, 8, cw-16, ch-16), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

# Smooth hairline and bottom
clean_mask = cv2.morphologyEx(clean_mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))

for y in range(int(ch*0.82), ch):
    factor = (y - int(ch*0.82)) / (ch - int(ch*0.82))
    cutoff_x = int(factor * factor * (cw * 0.36))
    clean_mask[y, :cutoff_x] = 0
    clean_mask[y, cw - cutoff_x:] = 0

eden_rgba = cv2.cvtColor(eden_crop, cv2.COLOR_BGR2RGBA)
eden_rgba[:, :, 3] = clean_mask
sticker_eden = make_euclidean_sticker(eden_rgba, outline_width=16)
sticker_eden.save(os.path.join(ASSET_DIR, "sticker_anthony_eden.png"))
print("Saved Euclidean sticker_anthony_eden.png successfully!")
