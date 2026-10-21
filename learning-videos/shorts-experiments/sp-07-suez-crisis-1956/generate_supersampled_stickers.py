import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageOps

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def create_supersampled_sticker(rgba_img, outline_width=14, shadow_offset=(14, 14)):
    """
    2x Supersampled anti-aliased sticker generation:
    - Scales up by 2x
    - Dilates binary mask with circular kernel
    - Anti-aliases stroke edges
    - Downsamples with Lanczos for vector-grade smoothness
    """
    w, h = rgba_img.size
    scale = 2
    sw, sh = w * scale, h * scale
    pad = (outline_width * 2 + 50) * scale
    new_w, new_h = sw + pad * 2, sh + pad * 2
    
    # Resize input by 2x
    rgba_2x = rgba_img.resize((sw, sh), Image.Resampling.LANCZOS)
    np_rgba = np.array(rgba_2x)
    alpha = np_rgba[:, :, 3]
    
    # Binary alpha
    _, bin_alpha = cv2.threshold(alpha, 128, 255, cv2.THRESH_BINARY)
    
    padded_alpha = np.zeros((new_h, new_w), dtype=np.uint8)
    padded_alpha[pad:pad+sh, pad:pad+sw] = bin_alpha
    
    # 2x dilation
    ksize = (outline_width * scale) * 2 + 1
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (ksize, ksize))
    dilated_mask = cv2.dilate(padded_alpha, kernel)
    
    # Smooth dilated stroke slightly for anti-aliasing
    stroke_smooth = cv2.GaussianBlur(dilated_mask, (5, 5), 0)
    
    # Canvas at 2x
    canvas_2x = np.zeros((new_h, new_w, 4), dtype=np.uint8)
    
    # Hard offset shadow (2x offset)
    sx, sy = shadow_offset[0] * scale, shadow_offset[1] * scale
    M = np.float32([[1, 0, sx], [0, 1, sy]])
    shadow_mask = cv2.warpAffine(dilated_mask, M, (new_w, new_h))
    canvas_2x[shadow_mask > 128] = [0, 0, 0, 255]
    
    # Solid White Stroke
    canvas_2x[stroke_smooth > 128] = [255, 255, 255, 255]
    
    # Composite FG
    fg_mask = bin_alpha == 255
    canvas_2x[pad:pad+sh, pad:pad+sw][fg_mask] = np_rgba[fg_mask]
    
    # Downsample back to 1x
    img_2x = Image.fromarray(canvas_2x)
    final_img = img_2x.resize((new_w // scale, new_h // scale), Image.Resampling.LANCZOS)
    return final_img

# -------------------------------------------------------------------
# 1. Anthony Eden
# -------------------------------------------------------------------
print("Generating supersampled Anthony Eden sticker...")
eden_raw = cv2.imread(os.path.join(RAW_DIR, "eden_portrait.jpg"))
eh, ew = eden_raw.shape[:2]
# Widen crop: 0.05 to 0.95
eden_crop = eden_raw[int(eh*0.01):int(eh*0.75), int(ew*0.05):int(ew*0.95)]
eden_crop = cv2.resize(eden_crop, (640, 700), interpolation=cv2.INTER_LANCZOS4)
ch, cw = eden_crop.shape[:2]

mask = np.zeros((ch, cw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(eden_crop, mask, (8, 8, cw-16, ch-16), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

# Smooth hairline notches via morphological closing
k_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
clean_mask = cv2.morphologyEx(clean_mask, cv2.MORPH_CLOSE, k_close)

for y in range(int(ch*0.82), ch):
    factor = (y - int(ch*0.82)) / (ch - int(ch*0.82))
    cutoff_x = int(factor * factor * (cw * 0.36))
    clean_mask[y, :cutoff_x] = 0
    clean_mask[y, cw - cutoff_x:] = 0

eden_rgba = cv2.cvtColor(eden_crop, cv2.COLOR_BGR2RGBA)
eden_rgba[:, :, 3] = clean_mask
eden_pil = Image.fromarray(eden_rgba)
# Enhance contrast
enh = ImageEnhance.Contrast(eden_pil)
eden_pil = enh.enhance(1.2)

sticker_eden = create_supersampled_sticker(eden_pil, outline_width=14)
sticker_eden.save(os.path.join(ASSET_DIR, "sticker_anthony_eden.png"))
print("Saved supersampled sticker_anthony_eden.png")

# -------------------------------------------------------------------
# 2. Tanker Ship High Contrast
# -------------------------------------------------------------------
print("Generating supersampled high-contrast Tanker Ship sticker...")
ship_raw = cv2.imread(os.path.join(RAW_DIR, "tanker_ship.jpg"))
sh, sw = ship_raw.shape[:2]
ship_crop = ship_raw[int(sh*0.22):int(sh*0.78), int(sw*0.04):int(sw*0.96)]
# Enhance grayscale levels & contrast
gray_ship = cv2.cvtColor(ship_crop, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
enhanced_gray = clahe.apply(gray_ship)
ship_bgr = cv2.cvtColor(enhanced_gray, cv2.COLOR_GRAY2BGR)

sch, scw = ship_bgr.shape[:2]
mask = np.zeros((sch, scw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(ship_bgr, mask, (10, 10, scw-20, sch-15), bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_mask = np.where((mask==2)|(mask==0), 0, 255).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_mask, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest, 255, 0).astype(np.uint8)

ship_rgba = cv2.cvtColor(ship_bgr, cv2.COLOR_BGR2RGBA)
ship_rgba[:, :, 3] = clean_mask
ship_pil = Image.fromarray(ship_rgba)
# Resize to bold presence width 700
ship_pil.thumbnail((720, 360), Image.Resampling.LANCZOS)

sticker_ship = create_supersampled_sticker(ship_pil, outline_width=14)
sticker_ship.save(os.path.join(ASSET_DIR, "sticker_tanker.png"))
print("Saved supersampled sticker_tanker.png")

print("All supersampled stickers generated successfully!")
