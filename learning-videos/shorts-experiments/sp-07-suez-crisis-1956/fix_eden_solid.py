import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/assets"

print("Generating solid, hole-free Anthony Eden sticker...")
eden_raw = cv2.imread(os.path.join(RAW_DIR, "eden_portrait.jpg"))
eh, ew = eden_raw.shape[:2]
# Generous bust crop: head, hair, ears, collar, tie, suit
eden_crop = eden_raw[int(eh*0.01):int(eh*0.82), int(ew*0.04):int(ew*0.96)]
# Scale to LARGE commanding resolution: 780 x 920
eden_crop = cv2.resize(eden_crop, (780, 920), interpolation=cv2.INTER_LANCZOS4)
ch, cw = eden_crop.shape[:2]

# Run GrabCut
mask = np.zeros((ch, cw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(eden_crop, mask, (10, 10, cw-20, ch-20), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

# Keep largest external component
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
solid_component = np.where(labels == largest, 255, 0).astype(np.uint8)

# Morphological closing on hair and edges
kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (19, 19))
solid_component = cv2.morphologyEx(solid_component, cv2.MORPH_CLOSE, kernel_close)

# Smooth bottom curve (bust termination)
for y in range(int(ch*0.84), ch):
    factor = (y - int(ch*0.84)) / (ch - int(ch*0.84))
    cutoff_x = int(factor * factor * (cw * 0.35))
    solid_component[y, :cutoff_x] = 0
    solid_component[y, cw - cutoff_x:] = 0

# Pad by 60px
pad = 60
new_h = ch + pad * 2
new_w = cw + pad * 2

padded_mask = np.zeros((new_h, new_w), dtype=np.uint8)
padded_mask[pad:pad+ch, pad:pad+cw] = solid_component

# CRUCIAL: FLOOD FILL HOLE FILLING to ensure 100% solid interior!
im_floodfill = padded_mask.copy()
h_f, w_f = im_floodfill.shape
mask_f = np.zeros((h_f + 2, w_f + 2), np.uint8)
cv2.floodFill(im_floodfill, mask_f, (0, 0), 255)
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
solid_mask = cv2.bitwise_or(padded_mask, im_floodfill_inv)

# Exact Euclidean distance for pure smooth contour
outline_width = 16
inv_solid = cv2.bitwise_not(solid_mask)
dist = cv2.distanceTransform(inv_solid, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)
stroke_mask = np.where(dist <= outline_width, 255, 0).astype(np.uint8)

# Smooth outer edge
stroke_mask = cv2.GaussianBlur(stroke_mask, (5, 5), 0)
_, stroke_mask = cv2.threshold(stroke_mask, 128, 255, cv2.THRESH_BINARY)

# Hard offset shadow (16px, 16px)
sx, sy = 16, 16
M = np.float32([[1, 0, sx], [0, 1, sy]])
shadow_mask = cv2.warpAffine(stroke_mask, M, (new_w, new_h))

# Assemble final RGBA
canvas = np.zeros((new_h, new_w, 4), dtype=np.uint8)
canvas[shadow_mask == 255] = [0, 0, 0, 255]
canvas[stroke_mask == 255] = [255, 255, 255, 255]

# Paste original subject
fg_crop = eden_crop.copy()
# Enhance contrast
eden_pil = Image.fromarray(cv2.cvtColor(fg_crop, cv2.COLOR_BGR2RGB))
enh = ImageEnhance.Contrast(eden_pil)
eden_pil = enh.enhance(1.25)
fg_enhanced = cv2.cvtColor(np.array(eden_pil), cv2.COLOR_RGB2RGBA)

fg_mask = solid_mask[pad:pad+ch, pad:pad+cw] == 255
canvas[pad:pad+ch, pad:pad+cw][fg_mask] = fg_enhanced[fg_mask]

# Save
sticker_final = Image.fromarray(canvas)
sticker_final.save(os.path.join(ASSET_DIR, "sticker_anthony_eden.png"))
print("Saved 100% solid Anthony Eden sticker:", sticker_final.size)
