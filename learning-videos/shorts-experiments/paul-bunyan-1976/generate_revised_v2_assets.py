import os
import cv2
import numpy as np
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/paul-bunyan-1976/assets"

def apply_90s_sticker_fx(rgba_img, outline_width=14, shadow_offset=(14, 14), shadow_blur=14, shadow_alpha=190):
    """Adds mandatory @90secondslab white contour outline and 135 deg soft shadow to an RGBA image."""
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

# -------------------------------------------------------------------------
# 1. Hero Large Archival Plate: Gerald Ford Signing Order (840x560)
# -------------------------------------------------------------------------
print("Generating large Gerald Ford signing plate...")
ford_raw = Image.open(os.path.join(ASSET_DIR, "raw_ford_desk.jpg")).convert("RGBA")
# Target photo crop inside dossier plate (780 x 440)
fw, fh = 840, 560
ford_plate = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
draw = ImageDraw.Draw(ford_plate)

# Aged tactile parchment card
draw.rounded_rectangle([0, 0, fw, fh], radius=16, fill=(244, 240, 230, 255))

# Crop Ford at desk
pw, ph = 792, 440
ratio = max(pw / ford_raw.width, ph / ford_raw.height)
ford_res = ford_raw.resize((int(ford_raw.width * ratio), int(ford_raw.height * ratio)), Image.Resampling.LANCZOS)
# Center-crop focused on Ford and the desk papers
cx = int((ford_res.width - pw) * 0.45)
cy = int((ford_res.height - ph) * 0.4)
ford_crop = ford_res.crop((cx, cy, cx + pw, cy + ph))
ford_plate.paste(ford_crop, (24, 24))

# Inner photo outline
draw.rectangle([24, 24, 24 + pw, 24 + ph], outline=(35, 40, 50, 180), width=3)

# Red Tactical Order Seal on photo corner
draw.rounded_rectangle([36, 36, 310, 84], radius=8, fill=(193, 18, 31, 235))
try:
    font_stamp = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 26)
    font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 32)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
except:
    font_stamp = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

draw.text((48, 44), "ORDER SIGNED: AUG 20", font=font_stamp, fill=(255, 255, 255))
draw.text((32, 480), "PRESIDENT GERALD R. FORD", font=font_title, fill=(15, 20, 30, 255))
draw.text((32, 520), "AUTHORIZING MAXIMUM FORCE // OPERATION PAUL BUNYAN", font=font_sub, fill=(193, 18, 31, 255))

ford_sticker = apply_90s_sticker_fx(ford_plate, outline_width=14)
ford_sticker.save(os.path.join(ASSET_DIR, "sticker_ford_signing_large.png"))

# -------------------------------------------------------------------------
# 2. Hero Large Archival Plate: DMZ Incident Poplar Tree (840x540)
# -------------------------------------------------------------------------
print("Generating large DMZ tree plate for Scene 1...")
tree_raw = Image.open(os.path.join(ASSET_DIR, "raw_dmz_tree.jpg")).convert("RGBA")
tw, th = 840, 540
tree_plate = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
draw = ImageDraw.Draw(tree_plate)
draw.rounded_rectangle([0, 0, tw, th], radius=16, fill=(244, 240, 230, 255))

tpw, tph = 792, 420
ratio = max(tpw / tree_raw.width, tph / tree_raw.height)
tree_res = tree_raw.resize((int(tree_raw.width * ratio), int(tree_raw.height * ratio)), Image.Resampling.LANCZOS)
tcx = int((tree_res.width - tpw) * 0.5)
tcy = int((tree_res.height - tph) * 0.3)
tree_crop = tree_res.crop((tcx, tcy, tcx + tpw, tcy + tph))
tree_plate.paste(tree_crop, (24, 24))
draw.rectangle([24, 24, 24 + tpw, 24 + tph], outline=(35, 40, 50, 180), width=3)

# Red Evidence Badge
draw.rounded_rectangle([36, 36, 260, 84], radius=8, fill=(193, 18, 31, 235))
draw.text((48, 44), "EVIDENCE // DMZ", font=font_stamp, fill=(255, 255, 255))
draw.text((32, 460), "THE DISPUTED POPLAR TREE", font=font_title, fill=(15, 20, 30, 255))
draw.text((32, 498), "JOINT SECURITY AREA, PANMUNJOM (1976)", font=font_sub, fill=(180, 25, 30, 255))

tree_sticker = apply_90s_sticker_fx(tree_plate, outline_width=14)
tree_sticker.save(os.path.join(ASSET_DIR, "sticker_dmz_tree_large.png"))

# -------------------------------------------------------------------------
# 3. Hero Large Outro Plate: The Severed Tree Stump Payoff (860x560)
# -------------------------------------------------------------------------
print("Generating large severed stump payoff plate for Scene 4...")
stump_plate = Image.new("RGBA", (860, 560), (0, 0, 0, 0))
draw = ImageDraw.Draw(stump_plate)
draw.rounded_rectangle([0, 0, 860, 560], radius=16, fill=(242, 238, 226, 255))

spw, sph = 812, 440
ratio = max(spw / tree_raw.width, sph / tree_raw.height)
stump_res = tree_raw.resize((int(tree_raw.width * ratio), int(tree_raw.height * ratio)), Image.Resampling.LANCZOS)
scx = int((stump_res.width - spw) * 0.75) # Focus on the cut stump on the right
scy = int((stump_res.height - sph) * 0.3)
stump_crop = stump_res.crop((scx, scy, scx + spw, scy + sph))
stump_plate.paste(stump_crop, (24, 24))
draw.rectangle([24, 24, 24 + spw, 24 + sph], outline=(35, 40, 50, 180), width=3)

# Green Mission Accomplished Stamp
draw.rounded_rectangle([36, 36, 320, 84], radius=8, fill=(43, 147, 72, 240))
draw.text((48, 44), "FELLED IN 42 MINUTES", font=font_stamp, fill=(255, 255, 255))
draw.text((32, 480), "THE POPLAR STUMP (AUG 21, 1976)", font=font_title, fill=(15, 20, 30, 255))
draw.text((32, 520), "813 TROOPS WITHDRAWN // ZERO CASUALTIES", font=font_sub, fill=(43, 147, 72, 255))

stump_sticker = apply_90s_sticker_fx(stump_plate, outline_width=14)
stump_sticker.save(os.path.join(ASSET_DIR, "sticker_dmz_stump_outro.png"))

# -------------------------------------------------------------------------
# 4. Dense War Room Tactical Stage (No Blank Void)
# -------------------------------------------------------------------------
print("Generating dense war room tactical stage...")
stage2 = Image.new("RGBA", (1080, 1920), (16, 24, 20, 255))
draw = ImageDraw.Draw(stage2)

# Deep tactical green grid desk
for x in range(0, 1080, 60):
    draw.line([(x, 0), (x, 1920)], fill=(24, 38, 30, 255), width=1)
for y in range(0, 1920, 60):
    draw.line([(0, y), (1080, y)], fill=(24, 38, 30, 255), width=1)

# Large Center Map Mat (1000 x 1300)
draw.rounded_rectangle([40, 220, 1040, 1600], radius=24, fill=(234, 228, 212, 255))
draw.rounded_rectangle([56, 236, 1024, 1584], radius=18, fill=(244, 239, 226, 255))

# Top map title
draw.rectangle([80, 260, 1000, 320], fill=(193, 18, 31, 235))
try:
    font_map_h = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 30)
    font_map_sub = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 22)
except:
    font_map_h = ImageFont.load_default()
    font_map_sub = ImageFont.load_default()

draw.text((100, 274), "KOREA DEMILITARIZED ZONE // OPERATION PAUL BUNYAN", font=font_map_h, fill=(255, 255, 255))

# Map graticules & tactical demarcation line
draw.line([(80, 720), (1000, 720)], fill=(193, 18, 31, 180), width=4) # MDL 38th parallel representation
draw.text((100, 686), "MILITARY DEMARCATION LINE (MDL)", font=font_map_sub, fill=(193, 18, 31, 220))

# Tactical vector deployment arrows
for ax in [240, 540, 840]:
    draw.line([(ax, 1100), (ax, 780)], fill=(30, 80, 160, 200), width=4)
    draw.polygon([(ax - 12, 780), (ax + 12, 780), (ax, 750)], fill=(30, 80, 160, 220))
draw.text((260, 920), "TASK FORCE VIPER // TF TACOMA CONVERGENCE", font=font_map_sub, fill=(30, 80, 160, 200))

stage2.save(os.path.join(ASSET_DIR, "stage_2_pentagon.png"))

# -------------------------------------------------------------------------
# 5. Rich DMZ Concrete Observation Bunker Stage
# -------------------------------------------------------------------------
print("Generating rich DMZ observation bunker stage...")
stage1 = Image.new("RGBA", (1080, 1920), (26, 28, 32, 255))
draw = ImageDraw.Draw(stage1)

# Raw weathered concrete wall texture
for y in range(0, 1920, 4):
    c = int(28 + 8 * math.sin(y / 16.0) + 4 * math.cos(y / 9.0))
    draw.line([(0, y), (1080, y)], fill=(c, c + 1, c + 3, 255))

# Observation slit opening (center)
draw.rounded_rectangle([40, 240, 1040, 1560], radius=20, fill=(16, 18, 22, 255))
# Sandbag reinforcement parapet across bottom of window
draw.rectangle([40, 1280, 1040, 1560], fill=(54, 48, 38, 255))
for sx in range(60, 1020, 160):
    for sy in range(1300, 1540, 80):
        draw.rounded_rectangle([sx, sy, sx + 140, sy + 65], radius=12, fill=(68, 60, 48, 255), outline=(42, 36, 28, 255), width=3)

# Top observation hazard bar
for hx in range(40, 1040, 60):
    draw.polygon([(hx, 240), (hx + 30, 240), (hx, 280), (hx - 30, 280)], fill=(245, 195, 25, 220))

stage1.save(os.path.join(ASSET_DIR, "stage_1_dmz_bunker.png"))

print("All revised V2 assets generated successfully!")
