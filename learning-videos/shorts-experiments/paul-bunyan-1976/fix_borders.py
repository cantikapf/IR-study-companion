import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/paul-bunyan-1976/assets"

def apply_90s_sticker_fx(rgba_img, outline_width=14, shadow_offset=(14, 14), shadow_blur=16, shadow_alpha=170):
    pad = outline_width * 2 + 40
    w, h = rgba_img.size
    new_w = w + pad * 2
    new_h = h + pad * 2
    alpha = rgba_img.split()[3]
    
    stroke_mask = Image.new("L", (new_w, new_h), 0)
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx*dx + dy*dy <= outline_width * outline_width:
                stroke_mask.paste(alpha, (pad + dx, pad + dy), alpha)
                
    shadow_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    shadow_mask = stroke_mask.filter(ImageFilter.GaussianBlur(shadow_blur))
    shadow_fill = Image.new("RGBA", (new_w, new_h), (10, 14, 20, shadow_alpha))
    shadow_img.paste(shadow_fill, shadow_offset, shadow_mask)
    
    stroke_img = Image.new("RGBA", (new_w, new_h), (255, 255, 255, 255))
    comp = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    comp.alpha_composite(shadow_img)
    comp.paste(stroke_img, (0, 0), stroke_mask)
    comp.paste(rgba_img, (pad, pad), rgba_img)
    return comp

# -------------------------------------------------------------------------
# 1. FIX GERALD FORD SIGNING PLATE (ORDER SIGNED: AUG 20 BADGE)
# -------------------------------------------------------------------------
print("Fixing Gerald Ford signing plate badge border...")
ford_raw = Image.open(os.path.join(ASSET_DIR, "raw_gerald_ford.jpg")).convert("RGBA")
fw, fh = 820, 540
ford_plate = Image.new("RGBA", (fw, fh), (0, 0, 0, 0))
draw = ImageDraw.Draw(ford_plate)
draw.rounded_rectangle([0, 0, fw, fh], radius=16, fill=(244, 240, 230, 255))

fpw, fph = 772, 420
ratio = max(fpw / ford_raw.width, fph / ford_raw.height)
ford_res = ford_raw.resize((int(ford_raw.width * ratio), int(ford_raw.height * ratio)), Image.Resampling.LANCZOS)
cx = int((ford_res.width - fpw) * 0.45)
cy = int((ford_res.height - fph) * 0.12)
ford_crop = ford_res.crop((cx, cy, cx + fpw, cy + fph))
ford_plate.paste(ford_crop, (24, 24))
draw.rectangle([24, 24, 24 + fpw, 24 + fph], outline=(35, 40, 50, 180), width=3)

font_stamp = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 24)
font_title = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 32)
font_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)

# Dynamic badge with generous +24px padding around text
badge_text = "ORDER SIGNED: AUG 20"
bbox = draw.textbbox((48, 44), badge_text, font=font_stamp)
bx0, by0, bx1, by1 = 36, 36, bbox[2] + 24, 86
draw.rounded_rectangle([bx0, by0, bx1, by1], radius=8, fill=(193, 18, 31, 240))
draw.text((48, 46), badge_text, font=font_stamp, fill=(255, 255, 255))

draw.text((32, 475), "PRESIDENT GERALD R. FORD", font=font_title, fill=(15, 20, 30, 255))
draw.text((32, 510), "AUTHORIZING MAXIMUM FORCE // OPERATION PAUL BUNYAN", font=font_sub, fill=(193, 18, 31, 255))

ford_sticker = apply_90s_sticker_fx(ford_plate, outline_width=14)
ford_sticker.save(os.path.join(ASSET_DIR, "sticker_ford_signing_large.png"))
print(f"Saved sticker_ford_signing_large.png with badge width {bx1 - bx0}px!")

# -------------------------------------------------------------------------
# 2. FIX PENTAGON WAR ROOM STAGE (TOP SECRET // DECLASSIFIED BADGE)
# -------------------------------------------------------------------------
print("Fixing Pentagon War Room stage badge border...")
img = Image.new("RGBA", (1080, 1920), (14, 20, 16, 255))
draw = ImageDraw.Draw(img)

# 1. Dark mahogany war room desk perimeter
for y in range(0, 1920, 4):
    v = int(18 + 6 * math.sin(y / 20.0))
    draw.line([(0, y), (1080, y)], fill=(v, v + 2, v + 1, 255))
    
# 2. Large Tactical Paper Map Surface
mx0, my0, mx1, my1 = 50, 200, 1030, 1660
draw.rounded_rectangle([mx0, my0, mx1, my1], radius=16, fill=(228, 222, 204, 255))
draw.rounded_rectangle([mx0 + 16, my0 + 16, mx1 - 16, my1 - 16], radius=10, fill=(240, 235, 218, 255))

# 3. Tactical Military Grid
for gx in range(mx0 + 40, mx1 - 20, 70):
    draw.line([(gx, my0 + 20), (gx, my1 - 20)], fill=(185, 195, 205, 180), width=1)
for gy in range(my0 + 40, my1 - 20, 70):
    draw.line([(mx0 + 20, gy), (mx1 - 20, gy)], fill=(185, 195, 205, 180), width=1)
    
# 4. Topographic Elevation Contour Rings
for cy in [450, 680, 1050, 1320]:
    for cx in [240, 520, 820]:
        for r in [30, 55, 80, 110, 140]:
            draw.ellipse([(cx - r, cy - r*0.7), (cx + r, cy + r*0.7)], outline=(195, 185, 160, 200), width=1)
            
# 5. Korean Demilitarized Zone & MDL Line
mdl_y = 1070
draw.line([(mx0 + 20, mdl_y), (mx1 - 20, mdl_y)], fill=(193, 18, 31, 240), width=4)
draw.line([(mx0 + 20, mdl_y + 40), (mx1 - 20, mdl_y + 40)], fill=(30, 80, 160, 140), width=2)

font_stamp_lg = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 22)
font_map_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
font_unit = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 18)

draw.text((mx0 + 40, my0 + 35), "CLASSIFIED // USFK WAR PLAN 5027 // JSA OPERATIONAL SECTOR", font=font_stamp_lg, fill=(180, 25, 30))
draw.text((mx0 + 40, mdl_y - 28), "MILITARY DEMARCATION LINE (38-40N)", font=font_map_bold, fill=(193, 18, 31))
draw.text((mx0 + 40, 1050), "SOUTHERN LIMIT LINE // UNCMAC SECTOR", font=font_unit, fill=(30, 80, 160))

# Allied Force Deployment Arrows - placed cleanly in visible zone (1150 to 1340)
for ax in [260, 540, 820]:
    draw.line([(ax, 1330), (ax, mdl_y + 55)], fill=(30, 80, 160, 240), width=5)
    draw.polygon([(ax - 14, mdl_y + 60), (ax + 14, mdl_y + 60), (ax, mdl_y + 30)], fill=(30, 80, 160, 240))
    draw.rectangle([ax - 70, 1270, ax + 70, 1320], fill=(240, 245, 255), outline=(30, 80, 160), width=2)
    draw.text((ax - 55, 1286), "TASK FORCE", font=font_unit, fill=(20, 60, 140))
    
for kx in [320, 540, 760]:
    draw.polygon([(kx, mdl_y - 65), (kx + 16, mdl_y - 50), (kx, mdl_y - 35), (kx - 16, mdl_y - 50)], fill=(193, 18, 31, 240))
    draw.text((kx - 30, mdl_y - 95), "KPA OP", font=font_unit, fill=(193, 18, 31))

# Dynamic TOP SECRET stamp with generous +28px padding
top_secret_text = "TOP SECRET // DECLASSIFIED"
ts_bbox = draw.textbbox((0, 0), top_secret_text, font=font_stamp_lg)
ts_w = ts_bbox[2] - ts_bbox[0]
ts_h = ts_bbox[3] - ts_bbox[1]

stamp_pad_x = 24
stamp_pad_y = 12
box_w = ts_w + stamp_pad_x * 2
box_h = ts_h + stamp_pad_y * 2
sbx1 = mx1 - 40
sbx0 = sbx1 - box_w
sby1 = my1 - 40
sby0 = sby1 - box_h

draw.rounded_rectangle([sbx0, sby0, sbx1, sby1], radius=8, fill=(193, 18, 31, 235))
draw.text((sbx0 + stamp_pad_x, sby0 + stamp_pad_y), top_secret_text, font=font_stamp_lg, fill=(255, 255, 255))

img.save(os.path.join(ASSET_DIR, "stage_2_pentagon.png"))
print(f"Saved stage_2_pentagon.png with stamp width {box_w}px (text {ts_w}px)!")

# -------------------------------------------------------------------------
# 3. FIX EVIDENCE // DMZ BADGE ON DMZ TREE PLATE
# -------------------------------------------------------------------------
print("Fixing DMZ tree plate badge border...")
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

ev_text = "EVIDENCE // DMZ JSA"
ev_bbox = draw.textbbox((48, 44), ev_text, font=font_stamp)
ev_w = ev_bbox[2] - ev_bbox[0]
draw.rounded_rectangle([36, 36, 48 + ev_w + 24, 86], radius=8, fill=(193, 18, 31, 235))
draw.text((48, 46), ev_text, font=font_stamp, fill=(255, 255, 255))

draw.text((32, 460), "THE DISPUTED POPLAR TREE", font=font_title, fill=(15, 20, 30, 255))
draw.text((32, 498), "JOINT SECURITY AREA, PANMUNJOM (1976)", font=font_sub, fill=(180, 25, 30, 255))

tree_sticker = apply_90s_sticker_fx(tree_plate, outline_width=14)
tree_sticker.save(os.path.join(ASSET_DIR, "sticker_dmz_tree_large.png"))
print("Saved sticker_dmz_tree_large.png with clean padded badge!")

print("All badge borders fixed with 100% dynamic bounding boxes!")
