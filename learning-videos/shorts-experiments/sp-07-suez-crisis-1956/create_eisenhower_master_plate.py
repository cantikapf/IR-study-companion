import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/assets"

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

print("Creating Master Archival Plate: Eisenhower Oval Office Desk (1956)...")
# Load the cropped Eisenhower at desk
ike_crop = cv2.imread(os.path.join(ASSET_DIR, "test_ike_strauss_crop.jpg"))
# Resize photo to fit inside plate: 800 x 480
ike_photo = cv2.resize(ike_crop, (800, 480), interpolation=cv2.INTER_LANCZOS4)
ike_photo_pil = Image.fromarray(cv2.cvtColor(ike_photo, cv2.COLOR_BGR2RGBA))

pw, ph = 850, 610
plate = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
draw = ImageDraw.Draw(plate)

# 1. Aged Parchment Dossier Card
draw.rounded_rectangle([0, 0, pw, ph], radius=16, fill=(244, 240, 228, 255))

# 2. Paste Archival Photo
plate.paste(ike_photo_pil, (25, 25))
draw.rectangle([25, 25, 825, 505], outline=(30, 35, 45, 220), width=3)

# 3. Top-Left Red Classification Badge on photo
draw.rounded_rectangle([38, 38, 380, 84], radius=8, fill=(185, 28, 28, 240))
try:
    font_badge = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 24)
    font_cap = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
except:
    font_badge = font_cap = font_sub = ImageFont.load_default()

draw.text((50, 48), "TOP SECRET // WHITE HOUSE", font=font_badge, fill=(255, 255, 255, 255))

# 4. Lower Dossier Typography
draw.rectangle([25, 520, 825, 595], fill=(15, 20, 30, 255))
draw.text((45, 532), "PRESIDENT DWIGHT D. EISENHOWER", font=font_cap, fill=(255, 255, 255, 255))
draw.text((45, 564), "OVAL OFFICE EXECUTIVE DIRECTIVE // NOV 1956", font=font_sub, fill=(210, 180, 90, 255))

# 5. Apply @90secondslab 14px white outline + 0-blur hard shadow
sticker = apply_90s_sticker_fx(plate, outline_width=14, shadow_offset=(14, 14))
sticker.save(os.path.join(ASSET_DIR, "sticker_eisenhower_plate.png"))
# Overwrite sticker_eisenhower.png
sticker.save(os.path.join(ASSET_DIR, "sticker_eisenhower.png"))
print("Saved Master Archival Eisenhower Plate:", sticker.size)
