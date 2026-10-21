import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def make_silhouette_sticker(rgba_img, outline_width=14, shadow_offset=(14, 14), shadow_blur=0, shadow_alpha=255):
    """Adds crisp white contour outline around silhouette + 135 deg hard 0-blur offset shadow per @90secondslab."""
    pad = outline_width * 2 + 50
    w, h = rgba_img.size
    new_w = w + pad * 2
    new_h = h + pad * 2
    
    alpha = rgba_img.split()[3]
    
    # 1. Dilation stroke mask (White outline)
    stroke_mask = Image.new("L", (new_w, new_h), 0)
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx*dx + dy*dy <= outline_width * outline_width:
                stroke_mask.paste(alpha, (pad + dx, pad + dy), alpha)
                
    # 2. Hard 0-blur drop shadow (135 deg)
    shadow_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    shadow_fill = Image.new("RGBA", (new_w, new_h), color=(0, 0, 0, shadow_alpha))
    shadow_img.paste(shadow_fill, shadow_offset, stroke_mask)
    
    # 3. Solid White Outline
    stroke_img = Image.new("RGBA", (new_w, new_h), (255, 255, 255, 255))
    
    # 4. Composite
    comp = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    comp.alpha_composite(shadow_img)
    comp.paste(stroke_img, (0, 0), stroke_mask)
    comp.paste(rgba_img, (pad, pad), rgba_img)
    return comp

# -------------------------------------------------------------------
# 1. Anthony Eden Clean Bust
# -------------------------------------------------------------------
print("Refining Anthony Eden bust cutout...")
eden_raw = Image.open(os.path.join(RAW_DIR, "eden_portrait.jpg")).convert("RGB")
ew, eh = eden_raw.size
# Crop head, neck, and upper chest
eden_crop = eden_raw.crop((int(ew*0.12), int(eh*0.02), int(ew*0.88), int(eh*0.75)))
eden_crop.thumbnail((560, 660), Image.Resampling.LANCZOS)
cw, ch = eden_crop.size

# High-precision GrabCut with oval bottom mask
eden_cv = cv2.cvtColor(np.array(eden_crop), cv2.COLOR_RGB2BGR)
mask = np.zeros(eden_cv.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (15, 10, cw - 30, ch - 20)
cv2.grabCut(eden_cv, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

# Keep only the largest connected component to kill ghost debris
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask2, connectivity=8)
largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest_label, 255, 0).astype(np.uint8)

# Smooth rounded crop at bottom
bottom_curve = np.ones((ch, cw), dtype=np.uint8) * 255
for y in range(int(ch*0.75), ch):
    factor = (y - int(ch*0.75)) / (ch - int(ch*0.75))
    cutoff_x = int(factor * factor * (cw * 0.42))
    bottom_curve[y, :cutoff_x] = 0
    bottom_curve[y, cw - cutoff_x:] = 0
clean_mask = cv2.bitwise_and(clean_mask, bottom_curve)
clean_mask = cv2.GaussianBlur(clean_mask, (3, 3), 0)

eden_rgba = Image.fromarray(cv2.cvtColor(eden_cv, cv2.COLOR_BGR2RGBA))
eden_rgba.putalpha(Image.fromarray(clean_mask))

eden_sticker = make_silhouette_sticker(eden_rgba, outline_width=14)
eden_sticker.save(os.path.join(ASSET_DIR, "sticker_anthony_eden.png"))
print("Saved clean sticker_anthony_eden.png")

# -------------------------------------------------------------------
# 2. President Dwight D. Eisenhower Clean Bust
# -------------------------------------------------------------------
print("Refining Eisenhower bust cutout...")
ike_raw = Image.open(os.path.join(RAW_DIR, "eisenhower_portrait.jpg")).convert("RGB")
iw, ih = ike_raw.size
ike_crop = ike_raw.crop((int(iw*0.14), int(ih*0.06), int(iw*0.86), int(ih*0.75)))
ike_crop.thumbnail((560, 660), Image.Resampling.LANCZOS)
icw, ich = ike_crop.size

ike_cv = cv2.cvtColor(np.array(ike_crop), cv2.COLOR_RGB2BGR)
mask = np.zeros(ike_cv.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (15, 10, icw - 30, ich - 20)
cv2.grabCut(ike_cv, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask2, connectivity=8)
largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest_label, 255, 0).astype(np.uint8)

# Smooth bottom curve
bottom_curve = np.ones((ich, icw), dtype=np.uint8) * 255
for y in range(int(ich*0.78), ich):
    factor = (y - int(ich*0.78)) / (ich - int(ich*0.78))
    cutoff_x = int(factor * factor * (icw * 0.40))
    bottom_curve[y, :cutoff_x] = 0
    bottom_curve[y, icw - cutoff_x:] = 0
clean_mask = cv2.bitwise_and(clean_mask, bottom_curve)
clean_mask = cv2.GaussianBlur(clean_mask, (3, 3), 0)

ike_rgba = Image.fromarray(cv2.cvtColor(ike_cv, cv2.COLOR_BGR2RGBA))
ike_rgba.putalpha(Image.fromarray(clean_mask))

ike_sticker = make_silhouette_sticker(ike_rgba, outline_width=14)
ike_sticker.save(os.path.join(ASSET_DIR, "sticker_eisenhower.png"))
print("Saved clean sticker_eisenhower.png")

# -------------------------------------------------------------------
# 3. Gamal Abdel Nasser Clean Bust
# -------------------------------------------------------------------
print("Refining Gamal Abdel Nasser bust...")
nas_raw = Image.open(os.path.join(RAW_DIR, "nasser_portrait.jpg")).convert("RGB")
nw, nh = nas_raw.size
nas_crop = nas_raw.crop((int(nw*0.12), int(nh*0.05), int(nw*0.88), int(nh*0.80)))
nas_crop.thumbnail((460, 580), Image.Resampling.LANCZOS)
ncw, nch = nas_crop.size

nas_cv = cv2.cvtColor(np.array(nas_crop), cv2.COLOR_RGB2BGR)
mask = np.zeros(nas_cv.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (15, 10, ncw - 30, nch - 20)
cv2.grabCut(nas_cv, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask2, connectivity=8)
largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest_label, 255, 0).astype(np.uint8)
clean_mask = cv2.GaussianBlur(clean_mask, (3, 3), 0)

nas_rgba = Image.fromarray(cv2.cvtColor(nas_cv, cv2.COLOR_BGR2RGBA))
nas_rgba.putalpha(Image.fromarray(clean_mask))

nas_sticker = make_silhouette_sticker(nas_rgba, outline_width=14)
nas_sticker.save(os.path.join(ASSET_DIR, "sticker_nasser.png"))
print("Saved clean sticker_nasser.png")

# -------------------------------------------------------------------
# 4. Tanker Ship Clean Cutout
# -------------------------------------------------------------------
print("Refining tanker ship cutout...")
ship_raw = Image.open(os.path.join(RAW_DIR, "tanker_ship.jpg")).convert("RGB")
sw, sh = ship_raw.size
ship_crop = ship_raw.crop((int(sw*0.04), int(sh*0.22), int(sw*0.96), int(sh*0.78)))
ship_crop.thumbnail((640, 320), Image.Resampling.LANCZOS)
scw, sch = ship_crop.size

ship_cv = cv2.cvtColor(np.array(ship_crop), cv2.COLOR_RGB2BGR)
mask = np.zeros(ship_cv.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (10, 10, scw - 20, sch - 15)
cv2.grabCut(ship_cv, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask2, connectivity=8)
largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_mask = np.where(labels == largest_label, 255, 0).astype(np.uint8)
clean_mask = cv2.GaussianBlur(clean_mask, (3, 3), 0)

ship_rgba = Image.fromarray(cv2.cvtColor(ship_cv, cv2.COLOR_BGR2RGBA))
ship_rgba.putalpha(Image.fromarray(clean_mask))

ship_sticker = make_silhouette_sticker(ship_rgba, outline_width=14)
ship_sticker.save(os.path.join(ASSET_DIR, "sticker_tanker.png"))
print("Saved clean sticker_tanker.png")

# -------------------------------------------------------------------
# 5. Operation Musketeer Dossier Card with Bold Contrast
# -------------------------------------------------------------------
print("Refining Operation Musketeer dossier card...")
musk_raw = Image.open(os.path.join(RAW_DIR, "operation_musketeer.jpg")).convert("RGB")
musk_raw.thumbnail((680, 500), Image.Resampling.LANCZOS)
mw, mh = musk_raw.size

card_w = mw + 50
card_h = mh + 120
dossier_card = Image.new("RGBA", (card_w, card_h), (242, 238, 226, 255))
dossier_card.paste(musk_raw, (25, 25))
d_draw = ImageDraw.Draw(dossier_card)
d_draw.rectangle([12, 12, card_w-12, card_h-12], outline=(180, 20, 20, 255), width=4)

d_draw.rectangle([25, mh + 35, card_w - 25, mh + 105], fill=(15, 20, 30, 255))
d_draw.text((40, mh + 44), "OPERATION MUSKETEER // PORT SAID 1956", fill=(255, 255, 255, 255))
d_draw.text((40, mh + 72), "ANGLO-FRENCH INVASION FLEET", fill=(250, 200, 80, 255))

dossier_sticker = make_silhouette_sticker(dossier_card, outline_width=14)
dossier_sticker.save(os.path.join(ASSET_DIR, "sticker_musketeer_card.png"))
print("Saved clean sticker_musketeer_card.png")

# -------------------------------------------------------------------
# 6. Cracked Banknote
# -------------------------------------------------------------------
print("Refining British £5 banknote sticker...")
pound_raw = Image.open(os.path.join(RAW_DIR, "pound_banknote.jpg")).convert("RGBA")
pound_raw.thumbnail((740, 450), Image.Resampling.LANCZOS)
pw, ph = pound_raw.size

crack_mask = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
draw = ImageDraw.Draw(crack_mask)
points = [
    (pw//2, 0),
    (pw//2 + 15, int(ph*0.2)),
    (pw//2 - 25, int(ph*0.45)),
    (pw//2 + 30, int(ph*0.7)),
    (pw//2 - 10, ph)
]
for p in range(len(points)-1):
    draw.line([points[p], points[p+1]], fill=(180, 20, 20, 240), width=8)
    draw.line([points[p], points[p+1]], fill=(255, 255, 255, 200), width=2)

pound_cracked = Image.alpha_composite(pound_raw, crack_mask)
pound_sticker = make_silhouette_sticker(pound_cracked, outline_width=14)
pound_sticker.save(os.path.join(ASSET_DIR, "sticker_pound_cracked.png"))
print("Saved clean sticker_pound_cracked.png")

print("All asset refinements completed successfully!")
