import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/paul-bunyan-1976/assets"
os.makedirs(ASSET_DIR, exist_ok=True)

def apply_90s_sticker_fx(base_img, outline_width=14, shadow_offset=(16, 16), shadow_blur=16, shadow_alpha=180):
    """Adds mandatory @90secondslab white contour outline and 135 deg soft shadow to an RGBA image."""
    pad = outline_width * 2 + 40
    w, h = base_img.size
    new_w = w + pad * 2
    new_h = h + pad * 2
    
    alpha = base_img.split()[3]
    
    # 1. Stroke mask via dilation
    stroke_mask = Image.new("L", (new_w, new_h), 0)
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx*dx + dy*dy <= outline_width * outline_width:
                stroke_mask.paste(alpha, (pad + dx, pad + dy), alpha)
                
    # 2. Soft Drop Shadow
    shadow_img = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    shadow_mask = stroke_mask.filter(ImageFilter.GaussianBlur(shadow_blur))
    shadow_fill = Image.new("RGBA", (new_w, new_h), (8, 12, 20, shadow_alpha))
    shadow_img.paste(shadow_fill, shadow_offset, shadow_mask)
    
    # 3. Solid White Contour Stroke
    stroke_img = Image.new("RGBA", (new_w, new_h), (255, 255, 255, 255))
    
    # 4. Composite: Shadow -> White Stroke -> Original Object
    comp = Image.new("RGBA", (new_w, new_h), (0, 0, 0, 0))
    comp.alpha_composite(shadow_img)
    comp.paste(stroke_img, (0, 0), stroke_mask)
    comp.paste(base_img, (pad, pad), base_img)
    return comp

def draw_hook_ladder_sticker(text, bg_color, text_color, tilt=0):
    """Hook ladder block with 0-blur hard shadow per @90secondslab standard."""
    w, h = 880, 150
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 0-blur hard shadow offset (12px, 12px)
    draw.rounded_rectangle([18, 18, w - 18, h - 18], radius=16, fill=(10, 14, 22, 245))
    # Main block
    draw.rounded_rectangle([10, 10, w - 26, h - 26], radius=16, fill=bg_color)
    # White outline
    draw.rounded_rectangle([10, 10, w - 26, h - 26], radius=16, outline=(255, 255, 255), width=8)
    
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 64)
    except:
        font = ImageFont.load_default()
        
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (w - 26 - tw) // 2 + 10
    ty = (h - 26 - th) // 2 + 4
    draw.text((tx, ty), text, font=font, fill=text_color)
    
    if tilt != 0:
        img = img.rotate(tilt, resample=Image.Resampling.BICUBIC, expand=True)
    return img

def create_archival_photo_card(raw_photo_path, title_main, title_sub, stamp_text="DECLASSIFIED", accent_color=(200, 35, 40)):
    """Creates a tactile archival dossier card with photo, tape, stamp, and white stroke."""
    w, h = 480, 620
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(card)
    
    # Aged dossier parchment card
    draw.rounded_rectangle([0, 0, w, h], radius=14, fill=(244, 240, 230, 255))
    
    # Load and crop photo
    if os.path.exists(raw_photo_path):
        photo = Image.open(raw_photo_path).convert("RGBA")
        target_pw, target_ph = 432, 450
        pratio = photo.width / photo.height
        tratio = target_pw / target_ph
        if pratio > tratio:
            nh = target_ph
            nw = int(nh * pratio)
        else:
            nw = target_pw
            nh = int(nw / pratio)
        photo_res = photo.resize((nw, nh), Image.Resampling.LANCZOS)
        left = (nw - target_pw) // 2
        top = (nh - target_ph) // 2
        photo_crop = photo_res.crop((left, top, left + target_pw, top + target_ph))
        card.paste(photo_crop, (24, 24))
    else:
        draw.rectangle([24, 24, 456, 474], fill=(50, 55, 65, 255))
        
    # Inner photo border
    draw.rectangle([24, 24, 456, 474], outline=(40, 45, 55, 160), width=2)
    
    # Red Declassified Stamp on photo corner
    draw.rounded_rectangle([32, 32, 220, 72], radius=6, fill=(185, 25, 30, 220))
    try:
        font_stamp = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 22)
        font_name = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 28)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 20)
    except:
        font_stamp = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    draw.text((44, 40), stamp_text, font=font_stamp, fill=(255, 255, 255))
    
    # Metadata labels
    draw.text((28, 492), title_main, font=font_name, fill=(18, 24, 38, 255))
    draw.text((28, 532), title_sub, font=font_sub, fill=accent_color)
    
    return apply_90s_sticker_fx(card, outline_width=12)

def create_plane_cutout(raw_photo_path, label="B-52 STRATOFORTRESS"):
    """Extracts plane silhouette/cutout from photo and wraps in sticker contour."""
    # Load photo, crop to aircraft, create transparent cutout
    im = Image.open(raw_photo_path).convert("RGBA")
    # Resize to workable width 700px
    ratio = 700 / im.width
    im_res = im.resize((700, int(im.height * ratio)), Image.Resampling.LANCZOS)
    
    # For robust sticker without complex alpha thresholding, place in a sleek tactical cutout capsule
    card_w = 720
    card_h = int(im_res.height + 60)
    cutout = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(cutout)
    
    # Archival military plate backing
    draw.rounded_rectangle([0, 0, card_w, card_h], radius=16, fill=(22, 28, 38, 255))
    cutout.paste(im_res, (10, 10))
    draw.rounded_rectangle([10, 10, card_w - 10, card_h - 10], radius=12, outline=(255, 255, 255), width=3)
    
    # Tactical badge
    try:
        font_badge = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
    except:
        font_badge = ImageFont.load_default()
    draw.text((24, card_h - 44), label, font=font_badge, fill=(245, 190, 40, 255))
    
    return apply_90s_sticker_fx(cutout, outline_width=14)

def create_carrier_cutout(raw_photo_path):
    return create_plane_cutout(raw_photo_path, label="USS MIDWAY (CV-41) BATTLE GROUP")

def create_f4_cutout(raw_photo_path):
    return create_plane_cutout(raw_photo_path, label="F-4E PHANTOM II // TACTICAL AIR COMMAND")

# Stage 1: DMZ Concrete Bunker
def create_stage_dmz_bunker():
    img = Image.new("RGBA", (1080, 1920), (28, 32, 38, 255))
    draw = ImageDraw.Draw(img)
    # Concrete texture scanlines
    for y in range(0, 1920, 6):
        shade = int(32 + 8 * math.sin(y / 24.0))
        draw.line([(0, y), (1080, y)], fill=(shade, shade + 2, shade + 4, 255))
    # Sandbag bunker ledge at bottom
    draw.rectangle([0, 1400, 1080, 1920], fill=(62, 54, 42, 255))
    # Barbed wire line & observation slot
    draw.rectangle([60, 260, 1020, 1380], fill=(16, 20, 26, 255))
    draw.rectangle([80, 280, 1000, 1360], fill=(22, 26, 34, 255))
    # Caution diagonal hazard stripe
    for i in range(0, 1080, 60):
        draw.polygon([(i, 260), (i + 30, 260), (i - 10, 290), (i - 40, 290)], fill=(220, 180, 20, 220))
    return img

# Stage 2: Pentagon War Room Green Table
def create_stage_pentagon():
    img = Image.new("RGBA", (1080, 1920), (14, 28, 22, 255))
    draw = ImageDraw.Draw(img)
    # Tactical grid
    for x in range(0, 1080, 80):
        draw.line([(x, 0), (x, 1920)], fill=(22, 45, 34, 255), width=1)
    for y in range(0, 1920, 80):
        draw.line([(0, y), (1080, y)], fill=(22, 45, 34, 255), width=1)
    # Large center tactical map board
    draw.rounded_rectangle([60, 250, 1020, 1690], radius=20, fill=(240, 235, 220, 255))
    draw.rounded_rectangle([75, 265, 1005, 1675], radius=14, fill=(246, 242, 232, 255))
    draw.rectangle([100, 290, 980, 340], fill=(185, 25, 30, 230))
    try:
        font_h = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 30)
    except:
        font_h = ImageFont.load_default()
    draw.text((120, 298), "WAR ROOM BRIEFING: OPERATION PAUL BUNYAN (1976)", font=font_h, fill=(255, 255, 255))
    return img

# Stage 3: USS Midway Carrier Flight Deck
def create_stage_carrier_deck():
    img = Image.new("RGBA", (1080, 1920), (18, 24, 34, 255))
    draw = ImageDraw.Draw(img)
    # Steel flight deck non-skid plate texture
    for y in range(0, 1920, 8):
        shade = int(24 + 6 * math.sin(y / 18.0))
        draw.line([(0, y), (1080, y)], fill=(shade, shade + 3, shade + 6, 255))
    # Runway yellow and white catapult guidance lines
    draw.line([(540, 0), (540, 1920)], fill=(245, 205, 40, 220), width=14)
    draw.line([(480, 0), (480, 1920)], fill=(255, 255, 255, 160), width=6)
    draw.line([(600, 0), (600, 1920)], fill=(255, 255, 255, 160), width=6)
    return img

# Stage 4: DMZ Demarcation Line Gravel
def create_stage_dmz_gravel():
    img = Image.new("RGBA", (1080, 1920), (32, 34, 38, 255))
    draw = ImageDraw.Draw(img)
    # Gravel grain pattern
    for y in range(0, 1920, 10):
        shade = int(36 + 10 * math.cos(y / 28.0))
        draw.line([(0, y), (1080, y)], fill=(shade, shade, shade, 255))
    # Military Demarcation Line (MDL) concrete curb marker
    draw.rectangle([510, 0, 570, 1920], fill=(160, 165, 175, 255))
    draw.rectangle([514, 0, 566, 1920], fill=(210, 215, 225, 255))
    return img

print("Generating Hook Ladder stickers...")
h1 = draw_hook_ladder_sticker("THE DEADLIEST", bg_color=(12, 16, 24), text_color=(255, 230, 0), tilt=2)
h1.save(os.path.join(ASSET_DIR, "hook1_deadliest.png"))

h2 = draw_hook_ladder_sticker("TREE TRIMMING", bg_color=(193, 18, 31), text_color=(255, 255, 255), tilt=-3)
h2.save(os.path.join(ASSET_DIR, "hook2_tree_trimming.png"))

h3 = draw_hook_ladder_sticker("IN HISTORY", bg_color=(245, 245, 245), text_color=(12, 16, 24), tilt=3)
h3.save(os.path.join(ASSET_DIR, "hook3_in_history.png"))

print("Generating Archival Cards & Cutouts...")
tree_card = create_archival_photo_card(
    os.path.join(ASSET_DIR, "raw_dmz_tree.jpg"),
    "DMZ POPLAR TREE (1976)",
    "OBJECT OF CONFLICT // JSA PANMUNJOM",
    stamp_text="EVIDENCE #01",
    accent_color=(180, 30, 30)
)
tree_card.save(os.path.join(ASSET_DIR, "sticker_dmz_tree.png"))

ford_card = create_archival_photo_card(
    os.path.join(ASSET_DIR, "raw_gerald_ford.jpg"),
    "PRESIDENT GERALD FORD",
    "COMMANDER-IN-CHIEF // RETALIATION ORDER",
    stamp_text="ORDER SIGNED",
    accent_color=(20, 60, 140)
)
ford_card.save(os.path.join(ASSET_DIR, "sticker_gerald_ford.png"))

b52_cutout = create_plane_cutout(os.path.join(ASSET_DIR, "raw_b52.jpg"), label="B-52 STRATOFORTRESS // 3 ARMED ON-STATION")
b52_cutout.save(os.path.join(ASSET_DIR, "sticker_b52.png"))

f4_cutout = create_f4_cutout(os.path.join(ASSET_DIR, "raw_f4_phantom.jpg"))
f4_cutout.save(os.path.join(ASSET_DIR, "sticker_f4_phantom.png"))

midway_cutout = create_carrier_cutout(os.path.join(ASSET_DIR, "raw_uss_midway.jpg"))
midway_cutout.save(os.path.join(ASSET_DIR, "sticker_uss_midway.png"))

print("Generating 4 Adaptive Stages...")
stage1 = create_stage_dmz_bunker()
stage1.save(os.path.join(ASSET_DIR, "stage_1_dmz_bunker.png"))

stage2 = create_stage_pentagon()
stage2.save(os.path.join(ASSET_DIR, "stage_2_pentagon.png"))

stage3 = create_stage_carrier_deck()
stage3.save(os.path.join(ASSET_DIR, "stage_3_carrier_deck.png"))

stage4 = create_stage_dmz_gravel()
stage4.save(os.path.join(ASSET_DIR, "stage_4_dmz_gravel.png"))

print("All visual assets created successfully!")
