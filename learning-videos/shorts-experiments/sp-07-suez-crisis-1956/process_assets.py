import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

RAW_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/raw_assets"
ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sp-07-suez-crisis-1956/assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def make_silhouette_sticker(rgba_img, outline_width=14, shadow_offset=(16, 16), shadow_blur=16, shadow_alpha=190):
    pad = outline_width * 2 + 50
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
                
    # 2. Soft Drop Shadow (135 deg)
    shadow_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    shadow_mask = stroke_mask.filter(ImageFilter.GaussianBlur(shadow_blur))
    shadow_fill = Image.new("RGBA", (new_w, new_h), (5, 8, 14, shadow_alpha))
    shadow_img.paste(shadow_fill, shadow_offset, shadow_mask)
    
    # 3. Solid White Outline
    stroke_img = Image.new("RGBA", (new_w, new_h), (255, 255, 255, 255))
    
    # 4. Composite
    comp = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    comp.alpha_composite(shadow_img)
    comp.paste(stroke_img, (0, 0), stroke_mask)
    comp.paste(rgba_img, (pad, pad), rgba_img)
    return comp

# -------------------------------------------------------------------
# 1. PM Anthony Eden Bust Cutout
# -------------------------------------------------------------------
print("Processing Anthony Eden bust...")
eden_raw = Image.open(os.path.join(RAW_DIR, "eden_portrait.jpg")).convert("RGB")
# Crop upper torso & head
ew, eh = eden_raw.size
# Tight crop to bust
eden_crop = eden_raw.crop((int(ew*0.08), int(eh*0.02), int(ew*0.92), int(eh*0.82)))
eden_crop.thumbnail((650, 800), Image.Resampling.LANCZOS)
cw, ch = eden_crop.size

# Create soft rounded / contoured mask for bust
eden_cv = cv2.cvtColor(np.array(eden_crop), cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(eden_cv, cv2.COLOR_BGR2GRAY)
# Background in retouched portrait is light/studio gray, subject is dark suit
# Let's use GrabCut with rectangular ROI
mask = np.zeros(eden_cv.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (int(cw*0.05), int(ch*0.02), int(cw*0.90), int(ch*0.96))
cv2.grabCut(eden_cv, mask, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
eden_cv_cut = eden_cv * mask2[:, :, np.newaxis]

# Smooth mask
alpha_mask = (mask2 * 255).astype(np.uint8)
alpha_mask = cv2.GaussianBlur(alpha_mask, (5, 5), 0)

eden_rgba = Image.fromarray(cv2.cvtColor(eden_cv, cv2.COLOR_BGR2RGBA))
eden_rgba.putalpha(Image.fromarray(alpha_mask))

eden_sticker = make_silhouette_sticker(eden_rgba, outline_width=14)
eden_sticker.save(os.path.join(ASSET_DIR, "sticker_anthony_eden.png"))
print("Saved sticker_anthony_eden.png")

# -------------------------------------------------------------------
# 2. President Dwight D. Eisenhower Bust Cutout
# -------------------------------------------------------------------
print("Processing Eisenhower bust...")
ike_raw = Image.open(os.path.join(RAW_DIR, "eisenhower_portrait.jpg")).convert("RGB")
# Official portrait: crop head & chest
iw, ih = ike_raw.size
ike_crop = ike_raw.crop((int(iw*0.12), int(ih*0.05), int(iw*0.88), int(ih*0.80)))
ike_crop.thumbnail((650, 800), Image.Resampling.LANCZOS)
icw, ich = ike_crop.size

ike_cv = cv2.cvtColor(np.array(ike_crop), cv2.COLOR_RGB2BGR)
mask = np.zeros(ike_cv.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (int(icw*0.05), int(ich*0.02), int(icw*0.90), int(ich*0.96))
cv2.grabCut(ike_cv, mask, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
alpha_mask = (mask2 * 255).astype(np.uint8)
alpha_mask = cv2.GaussianBlur(alpha_mask, (5, 5), 0)

ike_rgba = Image.fromarray(cv2.cvtColor(ike_cv, cv2.COLOR_BGR2RGBA))
ike_rgba.putalpha(Image.fromarray(alpha_mask))

ike_sticker = make_silhouette_sticker(ike_rgba, outline_width=14)
ike_sticker.save(os.path.join(ASSET_DIR, "sticker_eisenhower.png"))
print("Saved sticker_eisenhower.png")

# -------------------------------------------------------------------
# 3. President Gamal Abdel Nasser Bust Cutout
# -------------------------------------------------------------------
print("Processing Gamal Abdel Nasser bust...")
nas_raw = Image.open(os.path.join(RAW_DIR, "nasser_portrait.jpg")).convert("RGB")
nw, nh = nas_raw.size
nas_crop = nas_raw.crop((int(nw*0.10), int(nh*0.03), int(nw*0.90), int(nh*0.85)))
nas_crop.thumbnail((600, 750), Image.Resampling.LANCZOS)
ncw, nch = nas_crop.size

nas_cv = cv2.cvtColor(np.array(nas_crop), cv2.COLOR_RGB2BGR)
mask = np.zeros(nas_cv.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (int(ncw*0.05), int(nch*0.02), int(ncw*0.90), int(nch*0.96))
cv2.grabCut(nas_cv, mask, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
alpha_mask = (mask2 * 255).astype(np.uint8)
alpha_mask = cv2.GaussianBlur(alpha_mask, (5, 5), 0)

nas_rgba = Image.fromarray(cv2.cvtColor(nas_cv, cv2.COLOR_BGR2RGBA))
nas_rgba.putalpha(Image.fromarray(alpha_mask))

nas_sticker = make_silhouette_sticker(nas_rgba, outline_width=14)
nas_sticker.save(os.path.join(ASSET_DIR, "sticker_nasser.png"))
print("Saved sticker_nasser.png")

# -------------------------------------------------------------------
# 4. British £5 Banknote with Crack / Devaluation Tear
# -------------------------------------------------------------------
print("Processing British £5 banknote sticker...")
pound_raw = Image.open(os.path.join(RAW_DIR, "pound_banknote.jpg")).convert("RGBA")
pound_raw.thumbnail((820, 520), Image.Resampling.LANCZOS)
pw, ph = pound_raw.size

# Draw physical jagged crack down the center
crack_mask = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
draw = ImageDraw.Draw(crack_mask)
# Jagged crack line in dark red / black with shadow
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
print("Saved sticker_pound_cracked.png")

# -------------------------------------------------------------------
# 5. Tanker Ship Cutout (Olympic Torch)
# -------------------------------------------------------------------
print("Processing tanker ship...")
ship_raw = Image.open(os.path.join(RAW_DIR, "tanker_ship.jpg")).convert("RGB")
sw, sh = ship_raw.size
# Crop around ship hull & superstructure
ship_crop = ship_raw.crop((int(sw*0.02), int(sh*0.15), int(sw*0.98), int(sh*0.85)))
ship_crop.thumbnail((780, 480), Image.Resampling.LANCZOS)
scw, sch = ship_crop.size

ship_cv = cv2.cvtColor(np.array(ship_crop), cv2.COLOR_RGB2BGR)
mask = np.zeros(ship_cv.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
rect = (int(scw*0.05), int(sch*0.10), int(scw*0.90), int(sch*0.85))
cv2.grabCut(ship_cv, mask, rect, bgdModel, fgdModel, 4, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
alpha_mask = (mask2 * 255).astype(np.uint8)
alpha_mask = cv2.GaussianBlur(alpha_mask, (5, 5), 0)

ship_rgba = Image.fromarray(cv2.cvtColor(ship_cv, cv2.COLOR_BGR2RGBA))
ship_rgba.putalpha(Image.fromarray(alpha_mask))

ship_sticker = make_silhouette_sticker(ship_rgba, outline_width=14)
ship_sticker.save(os.path.join(ASSET_DIR, "sticker_tanker.png"))
print("Saved sticker_tanker.png")

# -------------------------------------------------------------------
# 6. Operation Musketeer Archival Dossier Card
# -------------------------------------------------------------------
print("Processing Operation Musketeer dossier card...")
musk_raw = Image.open(os.path.join(RAW_DIR, "operation_musketeer.jpg")).convert("RGB")
musk_raw.thumbnail((650, 480), Image.Resampling.LANCZOS)
mw, mh = musk_raw.size

# Frame with aged paper border and classification stamps
card_w = mw + 40
card_h = mh + 90
dossier_card = Image.new("RGBA", (card_w, card_h), (242, 238, 226, 255))
dossier_card.paste(musk_raw, (20, 20))
d_draw = ImageDraw.Draw(dossier_card)
# Red stamp border
d_draw.rectangle([10, 10, card_w-10, card_h-10], outline=(180, 30, 30, 220), width=3)
# Text line
# Default sans font
d_draw.text((25, mh + 30), "OPERATION MUSKETEER // PORT SAID 1956", fill=(30, 35, 45, 255))
d_draw.text((25, mh + 55), "COMBINED ANGLO-FRENCH INVASION FORCE", fill=(160, 20, 20, 255))

dossier_sticker = make_silhouette_sticker(dossier_card, outline_width=14)
dossier_sticker.save(os.path.join(ASSET_DIR, "sticker_musketeer_card.png"))
print("Saved sticker_musketeer_card.png")

# -------------------------------------------------------------------
# 7. Layer B Physical Stages
# -------------------------------------------------------------------
print("Generating Layer B 3D Adaptive Stages...")

# Stage 1 & 2: Suez Canal Tactical Map Table (1080x1920)
suez_map = Image.open(os.path.join(RAW_DIR, "suez_canal_map.jpg")).convert("RGB")
# Scale and crop to 1080x1920 with high visual texture
sm_w, sm_h = suez_map.size
# Center crop on the canal region (middle vertical band)
crop_x1 = int(sm_w * 0.28)
crop_x2 = int(sm_w * 0.72)
suez_crop = suez_map.crop((crop_x1, 0, crop_x2, sm_h))
suez_stage = suez_crop.resize((1080, 1920), Image.Resampling.LANCZOS)

# Dark vignette & grid overlay to make stickers pop
overlay = Image.new("RGBA", (1080, 1920), (10, 15, 24, 160))
o_draw = ImageDraw.Draw(overlay)
# Grid lines
for x in range(0, 1080, 120):
    o_draw.line([(x, 0), (x, 1920)], fill=(255, 255, 255, 20), width=1)
for y in range(0, 1920, 120):
    o_draw.line([(0, y), (1080, y)], fill=(255, 255, 255, 20), width=1)

# Subtle vignette at top and bottom
suez_final = Image.alpha_composite(suez_stage.convert("RGBA"), overlay)
suez_final.save(os.path.join(ASSET_DIR, "stage_suez_map.png"))
print("Saved stage_suez_map.png")

# Stage 3: Pentagon War Room / Cabinet Table (Deep green felt & mahogany)
pentagon_stage = Image.new("RGBA", (1080, 1920), (18, 32, 26, 255))
p_draw = ImageDraw.Draw(pentagon_stage)
# Felt texture noise & grid
for x in range(0, 1080, 100):
    p_draw.line([(x, 0), (x, 1920)], fill=(255, 255, 255, 15), width=1)
for y in range(0, 1920, 100):
    p_draw.line([(0, y), (1080, y)], fill=(255, 255, 255, 15), width=1)
# Circular tactical conference ring
p_draw.ellipse([140, 400, 940, 1200], outline=(210, 170, 80, 60), width=3)
p_draw.ellipse([240, 500, 840, 1100], outline=(210, 170, 80, 30), width=1)
pentagon_stage.save(os.path.join(ASSET_DIR, "stage_pentagon.png"))
print("Saved stage_pentagon.png")

# Stage 4: Bank of England & US Treasury Ledger (Dark slate & gold bullion grid)
treasury_stage = Image.new("RGBA", (1080, 1920), (16, 20, 28, 255))
t_draw = ImageDraw.Draw(treasury_stage)
# Financial ledger horizontal lines
for y in range(0, 1920, 60):
    t_draw.line([(0, y), (1080, y)], fill=(40, 50, 70, 120), width=1)
# Vertical ledger divisions
for x in [120, 480, 840]:
    t_draw.line([(x, 0), (x, 1920)], fill=(60, 75, 100, 180), width=2)
treasury_stage.save(os.path.join(ASSET_DIR, "stage_treasury.png"))
print("Saved stage_treasury.png")

# Stage 5: Downing Street Red Dispatch Box (Rich crimson leather texture)
dispatch_stage = Image.new("RGBA", (1080, 1920), (28, 12, 16, 255))
d_draw = ImageDraw.Draw(dispatch_stage)
# Gold embossed double border around perimeter
d_draw.rectangle([50, 80, 1030, 1840], outline=(200, 160, 60, 140), width=3)
d_draw.rectangle([65, 95, 1015, 1825], outline=(200, 160, 60, 70), width=1)
dispatch_stage.save(os.path.join(ASSET_DIR, "stage_dispatch.png"))
print("Saved stage_dispatch.png")

print("All visual assets processed successfully!")
