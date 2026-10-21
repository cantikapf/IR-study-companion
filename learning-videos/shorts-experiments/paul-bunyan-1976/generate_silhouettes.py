import os
import cv2
import numpy as np
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/paul-bunyan-1976/assets"

def make_silhouette_sticker(rgba_img, outline_width=12, shadow_offset=(14, 14), shadow_blur=14, shadow_alpha=180):
    """Adds white contour outline directly around transparent silhouette edges + 135 deg soft shadow."""
    pad = outline_width * 2 + 40
    w, h = rgba_img.size
    new_w = w + pad * 2
    new_h = h + pad * 2
    
    alpha = rgba_img.split()[3]
    
    # 1. Dilation stroke mask
    stroke_mask = Image.new("L", (new_w, new_h), 0)
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx*dx + dy*dy <= outline_width * outline_width:
                stroke_mask.paste(alpha, (pad + dx, pad + dy), alpha)
                
    # 2. Soft Drop Shadow
    shadow_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    shadow_mask = stroke_mask.filter(ImageFilter.GaussianBlur(shadow_blur))
    shadow_fill = Image.new("RGBA", (new_w, new_h), (8, 12, 18, shadow_alpha))
    shadow_img.paste(shadow_fill, shadow_offset, shadow_mask)
    
    # 3. Solid White Outline
    stroke_img = Image.new("RGBA", (new_w, new_h), (255, 255, 255, 255))
    
    # 4. Composite
    comp = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    comp.alpha_composite(shadow_img)
    comp.paste(stroke_img, (0, 0), stroke_mask)
    comp.paste(rgba_img, (pad, pad), rgba_img)
    return comp

# -------------------------------------------------------------
# 1. B-52 Stratofortress Silhouette Cutout
# -------------------------------------------------------------
print("Creating B-52 silhouette...")
b52_raw = cv2.imread(os.path.join(ASSET_DIR, "raw_b52.jpg"))
hsv_b52 = cv2.cvtColor(b52_raw, cv2.COLOR_BGR2HSV)
# Sky mask
mask_sky = cv2.inRange(hsv_b52, (85, 20, 80), (135, 255, 255))
plane_mask = cv2.bitwise_not(mask_sky)
kernel = np.ones((5,5), np.uint8)
plane_mask = cv2.morphologyEx(plane_mask, cv2.MORPH_OPEN, kernel)
plane_mask = cv2.morphologyEx(plane_mask, cv2.MORPH_CLOSE, kernel)

# Crop tight to plane bounding box
contours, _ = cv2.findContours(plane_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest)
b, g, r = cv2.split(b52_raw)
b52_rgba = cv2.merge([b, g, r, plane_mask])[y:y+h, x:x+w]

# Convert to PIL
b52_pil = Image.fromarray(cv2.cvtColor(b52_rgba, cv2.COLOR_BGRA2RGBA))
# Resize to target width 720px
b52_pil.thumbnail((720, 450), Image.Resampling.LANCZOS)
b52_sticker = make_silhouette_sticker(b52_pil, outline_width=12)
b52_sticker.save(os.path.join(ASSET_DIR, "sticker_b52_silhouette.png"))

# -------------------------------------------------------------
# 2. F-4 Phantom II Silhouette Cutout
# -------------------------------------------------------------
print("Creating F-4 Phantom silhouette...")
f4_raw = cv2.imread(os.path.join(ASSET_DIR, "raw_f4_phantom.jpg"))
# F-4 is flying over desert/sky: GrabCut bounding box around jet
h, w = f4_raw.shape[:2]
scale = 800 / w
small_f4 = cv2.resize(f4_raw, (int(w*scale), int(h*scale)))
sh, sw = small_f4.shape[:2]
rect_f4 = (int(sw*0.1), int(sh*0.15), int(sw*0.8), int(sh*0.7))
mask_f4 = np.zeros(small_f4.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(small_f4, mask_f4, rect_f4, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask_f4_clean = np.where((mask_f4==2)|(mask_f4==0), 0, 1).astype('uint8')

# Tight crop
contours, _ = cv2.findContours(mask_f4_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest)

b, g, r = cv2.split(small_f4)
alpha_f4 = (mask_f4_clean * 255).astype('uint8')
f4_rgba = cv2.merge([b, g, r, alpha_f4])[y:y+h, x:x+w]
f4_pil = Image.fromarray(cv2.cvtColor(f4_rgba, cv2.COLOR_BGRA2RGBA))
f4_pil.thumbnail((620, 380), Image.Resampling.LANCZOS)
f4_sticker = make_silhouette_sticker(f4_pil, outline_width=12)
f4_sticker.save(os.path.join(ASSET_DIR, "sticker_f4_silhouette.png"))

# -------------------------------------------------------------
# 3. USS Midway Aircraft Carrier Silhouette Cutout
# -------------------------------------------------------------
print("Creating USS Midway silhouette...")
midway_raw = cv2.imread(os.path.join(ASSET_DIR, "raw_uss_midway.jpg"))
h, w = midway_raw.shape[:2]
scale = 800 / w
small_m = cv2.resize(midway_raw, (int(w*scale), int(h*scale)))
sh, sw = small_m.shape[:2]
# Carrier hull & deck are in lower half
rect_m = (int(sw*0.08), int(sh*0.35), int(sw*0.84), int(sh*0.55))
mask_m = np.zeros(small_m.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(small_m, mask_m, rect_m, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask_m_clean = np.where((mask_m==2)|(mask_m==0), 0, 1).astype('uint8')

contours, _ = cv2.findContours(mask_m_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest)

b, g, r = cv2.split(small_m)
alpha_m = (mask_m_clean * 255).astype('uint8')
midway_rgba = cv2.merge([b, g, r, alpha_m])[y:y+h, x:x+w]
midway_pil = Image.fromarray(cv2.cvtColor(midway_rgba, cv2.COLOR_BGRA2RGBA))
midway_pil.thumbnail((720, 360), Image.Resampling.LANCZOS)
midway_sticker = make_silhouette_sticker(midway_pil, outline_width=12)
midway_sticker.save(os.path.join(ASSET_DIR, "sticker_midway_silhouette.png"))

# -------------------------------------------------------------
# 4. President Gerald Ford Bust Silhouette Cutout
# -------------------------------------------------------------
print("Creating Gerald Ford bust silhouette...")
ford_raw = cv2.imread(os.path.join(ASSET_DIR, "raw_gerald_ford.jpg"))
h, w = ford_raw.shape[:2]
scale = 750 / w
small_ford = cv2.resize(ford_raw, (int(w*scale), int(h*scale)))
sh, sw = small_ford.shape[:2]

rect_ford = (int(sw*0.18), int(sh*0.04), int(sw*0.64), int(sh*0.92))
mask_ford = np.zeros(small_ford.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
cv2.grabCut(small_ford, mask_ford, rect_ford, bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
mask_ford_clean = np.where((mask_ford==2)|(mask_ford==0), 0, 1).astype('uint8')

# Refine mask with morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask_ford_clean = cv2.morphologyEx(mask_ford_clean, cv2.MORPH_CLOSE, kernel)

contours, _ = cv2.findContours(mask_ford_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest)

b, g, r = cv2.split(small_ford)
alpha_ford = (mask_ford_clean * 255).astype('uint8')
ford_rgba = cv2.merge([b, g, r, alpha_ford])[y:y+h, x:x+w]
ford_pil = Image.fromarray(cv2.cvtColor(ford_rgba, cv2.COLOR_BGRA2RGBA))
ford_pil.thumbnail((520, 640), Image.Resampling.LANCZOS)
ford_sticker = make_silhouette_sticker(ford_pil, outline_width=14)
ford_sticker.save(os.path.join(ASSET_DIR, "sticker_ford_silhouette.png"))

# -------------------------------------------------------------
# 5. Realistic Physical Carrier Flight Deck (USS Midway CV-41)
# -------------------------------------------------------------
print("Creating physical carrier flight deck stage...")
deck = Image.new("RGBA", (1080, 1920), (22, 26, 32, 255))
draw = ImageDraw.Draw(deck)

# Heavy textured dark charcoal non-skid deck plate
for y in range(0, 1920, 4):
    var = int(24 + 8 * math.sin(y / 14.0) + 4 * math.cos(y / 7.0))
    draw.line([(0, y), (1080, y)], fill=(var, var + 2, var + 5, 255))

# Steel plate seams (horizontal expansion joints)
for y in range(200, 1920, 280):
    draw.line([(0, y), (1080, y)], fill=(12, 14, 18, 255), width=4)
    draw.line([(0, y+4), (1080, y+4)], fill=(45, 52, 64, 255), width=2)

# Grid of circular deck tie-down pad eyes (star crosses)
for py in range(240, 1800, 140):
    for px in range(100, 1000, 140):
        draw.ellipse([(px - 8, py - 8), (px + 8, py + 8)], fill=(12, 14, 18, 255), outline=(50, 58, 70), width=2)
        draw.line([(px - 6, py), (px + 6, py)], fill=(70, 80, 95), width=2)
        draw.line([(px, py - 6), (px, py + 6)], fill=(70, 80, 95), width=2)

# Angled Catapult Runway Markings
# Thick Catapult track slot in center
draw.line([(540, 0), (540, 1920)], fill=(10, 12, 15, 255), width=18)
draw.line([(540, 0), (540, 1920)], fill=(38, 42, 50, 255), width=6)

# Vibrant yellow and black hazard caution boundaries
draw.line([(450, 0), (450, 1920)], fill=(245, 195, 25, 240), width=12)
draw.line([(630, 0), (630, 1920)], fill=(245, 195, 25, 240), width=12)

# White dashed centerline markings
for y in range(40, 1920, 120):
    draw.line([(495, y), (495, y + 60)], fill=(240, 240, 245, 220), width=8)
    draw.line([(585, y), (585, y + 60)], fill=(240, 240, 245, 220), width=8)

# Warning Stencil Text along deck edge
try:
    font_stencil = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 26)
    font_stencil_sm = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 20)
except:
    font_stencil = ImageFont.load_default()
    font_stencil_sm = ImageFont.load_default()

draw.text((70, 260), "FLIGHT DECK // USS MIDWAY (CV-41)", font=font_stencil, fill=(245, 195, 25, 230))
draw.text((70, 300), "DANGER: JET BLAST & ARRESTING CABLES", font=font_stencil_sm, fill=(200, 205, 215, 200))

deck.save(os.path.join(ASSET_DIR, "stage_3_carrier_deck.png"))
print("All silhouette cutouts & physical deck stage created successfully!")
