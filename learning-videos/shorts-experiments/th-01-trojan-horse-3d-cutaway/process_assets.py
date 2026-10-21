import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/assets"
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

card_w, card_h = 840, 660

try:
    font_badge = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 20)
    font_cap = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 19)
except:
    font_badge = font_cap = font_sub = ImageFont.load_default()

# -------------------------------------------------------------------
# 1. Plate: Tiepolo Trojan Horse Procession
# -------------------------------------------------------------------
print("Processing Tiepolo Trojan Horse plate...")
raw_t = cv2.imread(os.path.join(RAW_DIR, "tiepolo_procession.jpg"))
crop_t = cv2.resize(raw_t, (780, 500), interpolation=cv2.INTER_LANCZOS4)
pil_t = Image.fromarray(cv2.cvtColor(crop_t, cv2.COLOR_BGR2RGB))
enh_t = ImageEnhance.Contrast(pil_t)
pil_t = enh_t.enhance(1.18)

plate_t = Image.new("RGBA", (card_w, card_h), (244, 240, 228, 255))
draw_t = ImageDraw.Draw(plate_t)
plate_t.paste(pil_t, (30, 30))
draw_t.rectangle([30, 30, 810, 530], outline=(30, 35, 45, 220), width=3)

draw_t.rounded_rectangle([45, 45, 520, 95], radius=8, fill=(185, 28, 28, 240))
draw_t.text((58, 58), "THE TROJAN HORSE // 1184 BC", font=font_badge, fill=(255, 255, 255, 255))

draw_t.rectangle([30, 545, 810, 640], fill=(15, 20, 30, 255))
draw_t.text((50, 555), "THE PROCESSION INTO TROY", font=font_cap, fill=(255, 255, 255, 255))
draw_t.text((50, 588), "DISMANTLED PHOENICIAN PINE SHIP TIMBER // 30 MEN HIDDEN", font=font_sub, fill=(210, 180, 90, 255))

sticker_t = apply_90s_sticker_fx(plate_t, outline_width=14, shadow_offset=(14, 14))
sticker_t.save(os.path.join(ASSET_DIR, "plate_trojan_horse.png"))
print("Saved plate_trojan_horse.png")

# -------------------------------------------------------------------
# 2. Plate: Henri-Paul Motte Night Drop (1874)
# -------------------------------------------------------------------
print("Processing Motte Night Infiltration plate...")
raw_m = cv2.imread(os.path.join(RAW_DIR, "motte_trojan_horse.jpg"))
crop_m = cv2.resize(raw_m, (780, 500), interpolation=cv2.INTER_LANCZOS4)
pil_m = Image.fromarray(cv2.cvtColor(crop_m, cv2.COLOR_BGR2RGB))
enh_m = ImageEnhance.Contrast(pil_m)
pil_m = enh_m.enhance(1.22)

plate_m = Image.new("RGBA", (card_w, card_h), (244, 240, 228, 255))
draw_m = ImageDraw.Draw(plate_m)
plate_m.paste(pil_m, (30, 30))
draw_m.rectangle([30, 30, 810, 530], outline=(30, 35, 45, 220), width=3)

draw_m.rounded_rectangle([45, 45, 520, 95], radius=8, fill=(185, 28, 28, 240))
draw_m.text((58, 58), "MIDNIGHT DESCENT // HEMP ROPES", font=font_badge, fill=(255, 255, 255, 255))

draw_m.rectangle([30, 545, 810, 640], fill=(15, 20, 30, 255))
draw_m.text((50, 555), "ODYSSEUS UNLOCKS THE BELLY TRAPDOOR", font=font_cap, fill=(255, 255, 255, 255))
draw_m.text((50, 588), "SILENT DESCENT ONTO SLEEPING TROY // GATES UNLOCKED", font=font_sub, fill=(210, 180, 90, 255))

sticker_m = apply_90s_sticker_fx(plate_m, outline_width=14, shadow_offset=(14, 14))
sticker_m.save(os.path.join(ASSET_DIR, "plate_motte_night.png"))
print("Saved plate_motte_night.png")

# -------------------------------------------------------------------
# 3. Plate: Mykonos Pithos (Earliest 670 BC Relief Depiction)
# -------------------------------------------------------------------
print("Processing Mykonos Relief plate...")
raw_p = cv2.imread(os.path.join(RAW_DIR, "mykonos_pithos_relief.jpg"))
ph, pw = raw_p.shape[:2]
# Crop neck of vase showing horse relief
crop_p = raw_p[int(ph*0.1):int(ph*0.55), int(pw*0.15):int(pw*0.85)]
crop_p = cv2.resize(crop_p, (780, 500), interpolation=cv2.INTER_LANCZOS4)
pil_p = Image.fromarray(cv2.cvtColor(crop_p, cv2.COLOR_BGR2RGB))
enh_p = ImageEnhance.Contrast(pil_p)
pil_p = enh_p.enhance(1.25)

plate_p = Image.new("RGBA", (card_w, card_h), (244, 240, 228, 255))
draw_p = ImageDraw.Draw(plate_p)
plate_p.paste(pil_p, (30, 30))
draw_p.rectangle([30, 30, 810, 530], outline=(30, 35, 45, 220), width=3)

draw_p.rounded_rectangle([45, 45, 520, 95], radius=8, fill=(185, 28, 28, 240))
draw_p.text((58, 58), "ARCHAEOLOGICAL RECORD // 670 BC", font=font_badge, fill=(255, 255, 255, 255))

draw_p.rectangle([30, 545, 810, 640], fill=(15, 20, 30, 255))
draw_p.text((50, 555), "THE MYKONOS PITHOS RELIEF", font=font_cap, fill=(255, 255, 255, 255))
draw_p.text((50, 588), "PORT HOLES REVEALING WARRIOR HEADS INSIDE THE BELLY", font=font_sub, fill=(210, 180, 90, 255))

sticker_p = apply_90s_sticker_fx(plate_p, outline_width=14, shadow_offset=(14, 14))
sticker_p.save(os.path.join(ASSET_DIR, "plate_mykonos_pithos.png"))
print("Saved plate_mykonos_pithos.png")

print("All archival plates processed successfully!")
