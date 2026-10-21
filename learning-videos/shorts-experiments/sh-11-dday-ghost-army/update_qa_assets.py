import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/assets"

print("Regenerating sticker_dummy_tank.png with +25% brightness & contrast enhancement...")
tank_raw = cv2.imread(os.path.join(RAW_DIR, "dummy_tank.jpg"))

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
clean_t = cv2.morphologyEx(clean_t, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))

tank_rgba = cv2.cvtColor(crop_t, cv2.COLOR_BGR2RGBA)
tank_rgba[:, :, 3] = clean_t
pil_t = Image.fromarray(tank_rgba)

# Boost brightness +25% and contrast +15% per QA audit
enh_b = ImageEnhance.Brightness(pil_t)
pil_t = enh_b.enhance(1.25)
enh_c = ImageEnhance.Contrast(pil_t)
pil_t = enh_c.enhance(1.15)

# 14px white outline + 0-blur hard shadow (135 deg)
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

out_path = os.path.join(ASSET_DIR, "sticker_dummy_tank.png")
comp_t.save(out_path)
print(f"Saved enhanced sticker_dummy_tank.png to {out_path} ({comp_t.size})")

# Also update Rommel plate with aligned military label
print("Updating Rommel plate with aligned military label: 15TH ARMY // PANZER RESERVE...")
card_w, card_h = 840, 660
plate_r = Image.new("RGBA", (card_w, card_h), (244, 240, 228, 255))
draw_r = ImageDraw.Draw(plate_r)

rommel_raw = cv2.imread(os.path.join(RAW_DIR, "rommel_atlantikwall.jpg"))
crop_r = cv2.resize(rommel_raw, (780, 500), interpolation=cv2.INTER_LANCZOS4)
pil_r = Image.fromarray(cv2.cvtColor(crop_r, cv2.COLOR_BGR2RGB))
enh_r = ImageEnhance.Contrast(pil_r)
pil_r = enh_r.enhance(1.22)
plate_r.paste(pil_r, (30, 30))
draw_r.rectangle([30, 30, 810, 530], outline=(30, 35, 45, 220), width=3)

try:
    font_badge = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 18)
    font_cap = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 19)
except:
    font_badge = font_cap = font_sub = ImageFont.load_default()

draw_r.rounded_rectangle([45, 45, 640, 95], radius=8, fill=(185, 28, 28, 240))
draw_r.text((58, 58), "PAS-DE-CALAIS // 15TH ARMY // PANZER RESERVE", font=font_badge, fill=(255, 255, 255, 255))

draw_r.rectangle([30, 545, 810, 640], fill=(15, 20, 30, 255))
draw_r.text((50, 555), "FIELD MARSHAL ERWIN ROMMEL", font=font_cap, fill=(255, 255, 255, 255))
draw_r.text((50, 588), "PAS-DE-CALAIS // 15TH ARMY // PANZER RESERVE", font=font_sub, fill=(210, 180, 90, 255))

pad = 14 * 2 + 36
new_w, new_h = card_w + pad * 2, card_h + pad * 2
alpha = plate_r.split()[3]
stroke_mask = Image.new("L", (new_w, new_h), 0)
for dx in range(-14, 15):
    for dy in range(-14, 15):
        if dx*dx + dy*dy <= 196:
            stroke_mask.paste(alpha, (pad + dx, pad + dy), alpha)

shadow_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
shadow_fill = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 255))
shadow_img.paste(shadow_fill, (14, 14), stroke_mask)

comp_r = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
comp_r.alpha_composite(shadow_img)
comp_r.paste(Image.new("RGBA", (new_w, new_h), (255, 255, 255, 255)), (0, 0), stroke_mask)
comp_r.paste(plate_r, (pad, pad), plate_r)

comp_r.save(os.path.join(ASSET_DIR, "plate_rommel_calais.png"))
print("Saved updated plate_rommel_calais.png")
