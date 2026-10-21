import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def apply_90s_sticker_fx(rgba_img, outline_width=14, shadow_offset=(14, 14)):
    pad = outline_width * 2 + 36
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
                
    # 2. Hard 0-blur Drop Shadow (135 deg)
    shadow_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    shadow_fill = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 255))
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
# 1. Master Archival Plate: General George S. Patton (FUSAG)
# -------------------------------------------------------------------
print("Processing General George S. Patton master archival plate...")
patton_raw = cv2.imread(os.path.join(RAW_DIR, "patton_portrait.jpg"))
ph, pw = patton_raw.shape[:2]

# Crop upper torso & helmet
crop_p = patton_raw[int(ph*0.02):int(ph*0.75), int(pw*0.12):int(pw*0.88)]
crop_p = cv2.resize(crop_p, (780, 520), interpolation=cv2.INTER_LANCZOS4)
pil_p = Image.fromarray(cv2.cvtColor(crop_p, cv2.COLOR_BGR2RGB))
enh = ImageEnhance.Contrast(pil_p)
pil_p = enh.enhance(1.2)

card_w, card_h = 840, 660
plate_p = Image.new("RGBA", (card_w, card_h), (244, 240, 228, 255))
draw_p = ImageDraw.Draw(plate_p)

# Paste photo
plate_p.paste(pil_p, (30, 30))
draw_p.rectangle([30, 30, 810, 550], outline=(30, 35, 45, 220), width=3)

# Red stamp on photo
draw_p.rounded_rectangle([45, 45, 420, 95], radius=8, fill=(185, 28, 28, 240))
try:
    font_badge = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 24)
    font_cap = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
except:
    font_badge = font_cap = font_sub = ImageFont.load_default()

draw_p.text((58, 56), "TOP SECRET // DECEPTION OPS", font=font_badge, fill=(255, 255, 255, 255))

# Bottom metadata box
draw_p.rectangle([30, 565, 810, 640], fill=(15, 20, 30, 255))
draw_p.text((50, 575), "GENERAL GEORGE S. PATTON", font=font_cap, fill=(255, 255, 255, 255))
draw_p.text((50, 608), "COMMANDER, FIRST U.S. ARMY GROUP (PHANTOM FORCE)", font=font_sub, fill=(210, 180, 90, 255))

sticker_patton = apply_90s_sticker_fx(plate_p, outline_width=14, shadow_offset=(14, 14))
sticker_patton.save(os.path.join(ASSET_DIR, "plate_patton.png"))
print("Saved plate_patton.png:", sticker_patton.size)

# -------------------------------------------------------------------
# 2. Inflatable Dummy Sherman Tank Sticker (Die-cut with transparent bg)
# -------------------------------------------------------------------
print("Processing Inflatable Dummy Tank sticker...")
tank_raw = cv2.imread(os.path.join(RAW_DIR, "dummy_tank.jpg"))
th, tw = tank_raw.shape[:2]

# Crop around tank
crop_t = cv2.resize(tank_raw, (760, 480), interpolation=cv2.INTER_LANCZOS4)
tch, tcw = crop_t.shape[:2]

mask_t = np.zeros((tch, tcw), np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect_t = (15, 20, tcw - 30, tch - 35)
cv2.grabCut(crop_t, mask_t, rect_t, bgdModel, fgdModel, 6, cv2.GC_INIT_WITH_RECT)
bin_t = np.where((mask_t==2)|(mask_t==0), 0, 255).astype(np.uint8)

num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_t, connectivity=8)
largest = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])
clean_t = np.where(labels == largest, 255, 0).astype(np.uint8)

# Smooth mask
clean_t = cv2.morphologyEx(clean_t, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))

tank_rgba = cv2.cvtColor(crop_t, cv2.COLOR_BGR2RGBA)
tank_rgba[:, :, 3] = clean_t
pil_t = Image.fromarray(tank_rgba)

# Create sticker
pad_t = 14 * 2 + 40
w_t, h_t = pil_t.size
new_wt, new_ht = w_t + pad_t * 2, h_t + pad_t * 2
alpha_t = pil_t.split()[3]

stroke_t = Image.new("L", (new_wt, new_ht), 0)
for dx in range(-14, 15):
    for dy in range(-14, 15):
        if dx*dx + dy*dy <= 196:
            stroke_t.paste(alpha_t, (pad_t + dx, pad_t + dy), alpha_t)

shadow_t = Image.new("RGBA", (new_wt, new_ht), (0, 0, 0, 0))
shadow_t.paste(Image.new("RGBA", (new_wt, new_ht), (0, 0, 0, 255)), (14, 14), stroke_t)

comp_t = Image.new("RGBA", (new_wt, new_ht), (0, 0, 0, 0))
comp_t.alpha_composite(shadow_t)
comp_t.paste(Image.new("RGBA", (new_wt, new_ht), (255, 255, 255, 255)), (0, 0), stroke_t)
comp_t.paste(pil_t, (pad_t, pad_t), pil_t)

comp_t.save(os.path.join(ASSET_DIR, "sticker_dummy_tank.png"))
print("Saved sticker_dummy_tank.png:", comp_t.size)

# -------------------------------------------------------------------
# 3. Master Archival Plate: Inflatable Decoy NARA (3000px NARA photo)
# -------------------------------------------------------------------
print("Processing NARA Inflatable Decoy master plate...")
nara_raw = cv2.imread(os.path.join(RAW_DIR, "inflatable_dummy_nara.jpg"))
nh, nw = nara_raw.shape[:2]
crop_n = cv2.resize(nara_raw, (780, 520), interpolation=cv2.INTER_LANCZOS4)
pil_n = Image.fromarray(cv2.cvtColor(crop_n, cv2.COLOR_BGR2RGB))
enh_n = ImageEnhance.Contrast(pil_n)
pil_n = enh_n.enhance(1.22)

plate_n = Image.new("RGBA", (card_w, card_h), (244, 240, 228, 255))
draw_n = ImageDraw.Draw(plate_n)
plate_n.paste(pil_n, (30, 30))
draw_n.rectangle([30, 30, 810, 550], outline=(30, 35, 45, 220), width=3)

# Generous width badge to prevent any text clipping
draw_n.rounded_rectangle([45, 45, 480, 95], radius=8, fill=(185, 28, 28, 240))
draw_n.text((58, 56), "OPERATION FORTITUDE // DOVER", font=font_badge, fill=(255, 255, 255, 255))

draw_n.rectangle([30, 565, 810, 640], fill=(15, 20, 30, 255))
draw_n.text((50, 575), "PNEUMATIC DUMMY TANK (M4 SHERMAN)", font=font_cap, fill=(255, 255, 255, 255))
draw_n.text((50, 608), "RUBBERIZED CANVAS DECOY // U.S. ARMY GHOST FLEET", font=font_sub, fill=(210, 180, 90, 255))

sticker_nara = apply_90s_sticker_fx(plate_n, outline_width=14, shadow_offset=(14, 14))
sticker_nara.save(os.path.join(ASSET_DIR, "plate_inflatable_tank.png"))
print("Saved plate_inflatable_tank.png:", sticker_nara.size)

# -------------------------------------------------------------------
# 4. Master Archival Plate: Rommel Atlantikwall (Pas-de-Calais)
# -------------------------------------------------------------------
print("Processing Rommel Atlantikwall master plate...")
rommel_raw = cv2.imread(os.path.join(RAW_DIR, "rommel_atlantikwall.jpg"))
rh, rw = rommel_raw.shape[:2]
crop_r = cv2.resize(rommel_raw, (780, 500), interpolation=cv2.INTER_LANCZOS4)
pil_r = Image.fromarray(cv2.cvtColor(crop_r, cv2.COLOR_BGR2RGB))
enh_r = ImageEnhance.Contrast(pil_r)
pil_r = enh_r.enhance(1.22)

plate_r = Image.new("RGBA", (card_w, card_h), (244, 240, 228, 255))
draw_r = ImageDraw.Draw(plate_r)
plate_r.paste(pil_r, (30, 30))
draw_r.rectangle([30, 30, 810, 530], outline=(30, 35, 45, 220), width=3)

draw_r.rounded_rectangle([45, 45, 420, 95], radius=8, fill=(185, 28, 28, 240))
draw_r.text((58, 56), "PAS-DE-CALAIS // 15TH ARMY", font=font_badge, fill=(255, 255, 255, 255))

draw_r.rectangle([30, 545, 810, 640], fill=(15, 20, 30, 255))
draw_r.text((50, 555), "FIELD MARSHAL ERWIN ROMMEL", font=font_cap, fill=(255, 255, 255, 255))
draw_r.text((50, 588), "INSPECTING HEAVY COASTAL BUNKER FORTIFICATIONS", font=font_sub, fill=(210, 180, 90, 255))

sticker_rommel = apply_90s_sticker_fx(plate_r, outline_width=14, shadow_offset=(14, 14))
sticker_rommel.save(os.path.join(ASSET_DIR, "plate_rommel_calais.png"))
print("Saved plate_rommel_calais.png:", sticker_rommel.size)

# -------------------------------------------------------------------
# 5. Earth Texture Optimization for Three.js Sphere
# -------------------------------------------------------------------
print("Optimizing Earth texture for Three.js globe...")
earth_raw = Image.open(os.path.join(RAW_DIR, "earth_texture.jpg")).convert("RGB")
earth_resized = earth_raw.resize((2048, 1024), Image.Resampling.LANCZOS)
# Boost contrast and saturation slightly so oceans and continents look sharp in 3D
enh_e = ImageEnhance.Contrast(earth_resized)
earth_enhanced = enh_e.enhance(1.3)
earth_enhanced.save(os.path.join(ASSET_DIR, "earth_map_2048.jpg"), quality=92)
print("Saved earth_map_2048.jpg")

print("All asset processing finished successfully!")
