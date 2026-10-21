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
    
    im_flood = padded_alpha.copy()
    h_f, w_f = im_flood.shape
    mask_f = np.zeros((h_f + 2, w_f + 2), np.uint8)
    cv2.floodFill(im_flood, mask_f, (0, 0), 255)
    im_flood_inv = cv2.bitwise_not(im_flood)
    solid_mask = cv2.bitwise_or(padded_alpha, im_flood_inv)
    
    inv_solid = cv2.bitwise_not(solid_mask)
    dist = cv2.distanceTransform(inv_solid, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
    stroke_mask = np.where(dist <= outline_width, 255, 0).astype(np.uint8)
    stroke_mask = cv2.GaussianBlur(stroke_mask, (5, 5), 0)
    _, stroke_mask = cv2.threshold(stroke_mask, 128, 255, cv2.THRESH_BINARY)
    
    canvas = np.zeros((new_h, new_w, 4), dtype=np.uint8)
    
    sx, sy = shadow_offset
    M = np.float32([[1, 0, sx], [0, 1, sy]])
    shadow_mask = cv2.warpAffine(stroke_mask, M, (new_w, new_h))
    canvas[shadow_mask == 255] = [0, 0, 0, 255]
    canvas[stroke_mask == 255] = [255, 255, 255, 255]
    
    fg_mask = solid_mask[pad:pad+h, pad:pad+w] == 255
    canvas[pad:pad+h, pad:pad+w][fg_mask] = rgba_np[fg_mask]
    
    return Image.fromarray(canvas)

print("Extracting commanding full-shoulders Eisenhower bust from ultra-res portrait...")
raw = cv2.imread(os.path.join(RAW_DIR, "eisenhower_portrait.jpg"))
h, w = raw.shape[:2]

# Keep FULL width to retain both broad shoulders!
# Head starts at y: 0.05, suit extends down to y: 0.92
crop = raw[int(h*0.04):int(h*0.92), int(w*0.02):int(w*0.98)]
# Resize to large canvas: width 860, height 960
crop = cv2.resize(crop, (860, 960), interpolation=cv2.INTER_LANCZOS4)
ch, cw = crop.shape[:2]

mask = np.zeros((ch, cw), np.uint8)
mask[:10, :] = cv2.GC_BGD
mask[-10:, :] = cv2.GC_BGD
mask[:, :10] = cv2.GC_BGD
mask[:, -10:] = cv2.GC_BGD

mask[10:-10, 10:-10] = cv2.GC_PR_FGD

# Sure foreground: Head, face, both broad shoulders, suit, tie
# Head: y: 80 to 450, x: 260 to 600
mask[80:450, 260:600] = cv2.GC_FGD
# Full broad shoulders & suit: y: 450 to 900, x: 60 to 800
mask[450:900, 60:800] = cv2.GC_FGD

# Sure background top corners
mask[:160, :200] = cv2.GC_BGD
mask[:160, 660:] = cv2.GC_BGD

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(crop, mask, None, bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_MASK)
bin_mask = np.where((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD), 255, 0).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

# Smooth clean outline
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
clean_mask = cv2.morphologyEx(clean_mask, cv2.MORPH_CLOSE, kernel)

# Flat clean bottom across chest
clean_mask[int(ch*0.94):, :] = 0

ike_rgba = cv2.cvtColor(crop, cv2.COLOR_BGR2RGBA)
ike_rgba[:, :, 3] = clean_mask

# Enhance contrast
pil_crop = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
enh = ImageEnhance.Contrast(pil_crop)
pil_crop = enh.enhance(1.2)
ike_rgba[:, :, :3] = np.array(pil_crop)

sticker = make_solid_clean_sticker(ike_rgba, outline_width=14, shadow_offset=(14, 14))
sticker.save(os.path.join(ASSET_DIR, "sticker_eisenhower_broad.png"))
sticker.save(os.path.join(ASSET_DIR, "sticker_eisenhower.png"))
print("Saved commanding sticker_eisenhower.png:", sticker.size)
