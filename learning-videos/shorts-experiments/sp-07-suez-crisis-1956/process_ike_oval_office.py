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
    
    # Flood fill hole filling for solid interior
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
    
    # Hard offset shadow (135 deg)
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

print("Extracting Oval Office Eisenhower half-body desk photo...")
raw = cv2.imread(os.path.join(RAW_DIR, "eisenhower_hoover.jpg"))
h, w = raw.shape[:2]
# Normalized coordinates: [ymin: 0.18, xmin: 0.0, ymax: 0.96, xmax: 0.62]
ymin, ymax = int(h * 0.18), int(h * 0.96)
xmin, xmax = int(w * 0.0), int(w * 0.62)
crop = raw[ymin:ymax, xmin:xmax]

# Resize to high resolution half-body: width 740, height 880
crop = cv2.resize(crop, (740, 880), interpolation=cv2.INTER_LANCZOS4)
ch, cw = crop.shape[:2]

# Segment Eisenhower, his chair, and executive desk
mask = np.zeros((ch, cw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (8, 12, cw - 16, ch - 24)
cv2.grabCut(crop, mask, rect, bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

# Smooth bottom desk termination
for y in range(int(ch*0.88), ch):
    factor = (y - int(ch*0.88)) / (ch - int(ch*0.88))
    cutoff_x = int(factor * factor * (cw * 0.25))
    clean_mask[y, :cutoff_x] = 0
    clean_mask[y, cw - cutoff_x:] = 0

# Morphology close
clean_mask = cv2.morphologyEx(clean_mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))

ike_rgba = cv2.cvtColor(crop, cv2.COLOR_BGR2RGBA)
ike_rgba[:, :, 3] = clean_mask

# Enhance contrast & clarity
pil_crop = Image.fromarray(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
enh = ImageEnhance.Contrast(pil_crop)
pil_crop = enh.enhance(1.22)
ike_rgba[:, :, :3] = np.array(pil_crop)

sticker = make_solid_clean_sticker(ike_rgba, outline_width=14, shadow_offset=(14, 14))
sticker.save(os.path.join(ASSET_DIR, "sticker_eisenhower_desk.png"))
# Also overwrite sticker_eisenhower.png
sticker.save(os.path.join(ASSET_DIR, "sticker_eisenhower.png"))
print("Saved flawless sticker_eisenhower_desk.png:", sticker.size)
