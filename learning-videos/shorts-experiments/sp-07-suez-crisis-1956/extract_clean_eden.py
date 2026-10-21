import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/assets"

def make_solid_clean_sticker(rgba_np, outline_width=14, shadow_offset=(14, 14)):
    h, w, c = rgba_np.shape
    pad = outline_width * 2 + 40
    new_h = h + pad * 2
    new_w = w + pad * 2
    
    alpha = rgba_np[:, :, 3]
    _, bin_alpha = cv2.threshold(alpha, 128, 255, cv2.THRESH_BINARY)
    
    padded_alpha = np.zeros((new_h, new_w), dtype=np.uint8)
    padded_alpha[pad:pad+h, pad:pad+w] = bin_alpha
    
    # Flood fill hole filling for 100% solid interior
    im_flood = padded_alpha.copy()
    h_f, w_f = im_flood.shape
    mask_f = np.zeros((h_f + 2, w_f + 2), np.uint8)
    cv2.floodFill(im_flood, mask_f, (0, 0), 255)
    im_flood_inv = cv2.bitwise_not(im_flood)
    solid_mask = cv2.bitwise_or(padded_alpha, im_flood_inv)
    
    # Euclidean distance transform
    inv_solid = cv2.bitwise_not(solid_mask)
    dist = cv2.distanceTransform(inv_solid, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
    stroke_mask = np.where(dist <= outline_width, 255, 0).astype(np.uint8)
    stroke_mask = cv2.GaussianBlur(stroke_mask, (5, 5), 0)
    _, stroke_mask = cv2.threshold(stroke_mask, 128, 255, cv2.THRESH_BINARY)
    
    canvas = np.zeros((new_h, new_w, 4), dtype=np.uint8)
    
    # Hard offset shadow
    sx, sy = shadow_offset
    M = np.float32([[1, 0, sx], [0, 1, sy]])
    shadow_mask = cv2.warpAffine(stroke_mask, M, (new_w, new_h))
    canvas[shadow_mask == 255] = [0, 0, 0, 255]
    
    # Solid White Stroke
    canvas[stroke_mask == 255] = [255, 255, 255, 255]
    
    # Composite foreground
    fg_mask = solid_mask[pad:pad+h, pad:pad+w] == 255
    canvas[pad:pad+h, pad:pad+w][fg_mask] = rgba_np[fg_mask]
    
    return Image.fromarray(canvas)

print("Extracting Anthony Eden from high-contrast portrait...")
raw = cv2.imread(os.path.join(RAW_DIR, "eden_alt.jpg"))
h, w = raw.shape[:2]
# Bust crop
crop = raw[int(h*0.02):int(h*0.82), int(w*0.05):int(w*0.95)]
crop = cv2.resize(crop, (680, 800), interpolation=cv2.INTER_LANCZOS4)
ch, cw = crop.shape[:2]

mask = np.zeros((ch, cw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
# Since background is pure dark, rect with 10px padding works brilliantly
cv2.grabCut(crop, mask, (10, 8, cw-20, ch-16), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

# Smooth bottom bust termination
for y in range(int(ch*0.84), ch):
    factor = (y - int(ch*0.84)) / (ch - int(ch*0.84))
    cutoff_x = int(factor * factor * (cw * 0.35))
    clean_mask[y, :cutoff_x] = 0
    clean_mask[y, cw - cutoff_x:] = 0

eden_rgba = cv2.cvtColor(crop, cv2.COLOR_BGR2RGBA)
eden_rgba[:, :, 3] = clean_mask

# Enhance contrast
eden_pil = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
enh = ImageEnhance.Contrast(eden_pil)
eden_pil = enh.enhance(1.25)
eden_rgba[:, :, :3] = np.array(eden_pil)

sticker = make_solid_clean_sticker(eden_rgba, outline_width=14, shadow_offset=(14, 14))
sticker.save(os.path.join(ASSET_DIR, "sticker_anthony_eden.png"))
print("Saved flawless sticker_anthony_eden.png:", sticker.size)
