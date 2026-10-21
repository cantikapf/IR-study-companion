import os
import math
from PIL import Image, ImageDraw, ImageFont

ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/paul-bunyan-1976/assets"

def make_dense_tactical_war_room_stage():
    """Generates a rich, highly detailed military tactical map war room table (1080 x 1920)."""
    img = Image.new("RGBA", (1080, 1920), (14, 20, 16, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. Dark mahogany war room desk perimeter
    for y in range(0, 1920, 4):
        v = int(18 + 6 * math.sin(y / 20.0))
        draw.line([(0, y), (1080, y)], fill=(v, v + 2, v + 1, 255))
        
    # 2. Large Tactical Paper Map Surface (980 x 1460)
    mx0, my0, mx1, my1 = 50, 200, 1030, 1660
    draw.rounded_rectangle([mx0, my0, mx1, my1], radius=16, fill=(228, 222, 204, 255))
    # Inner map border
    draw.rounded_rectangle([mx0 + 16, my0 + 16, mx1 - 16, my1 - 16], radius=10, fill=(240, 235, 218, 255))
    
    # 3. Tactical Military Grid (1000m UTM Grid lines in cyan/gray)
    for gx in range(mx0 + 40, mx1 - 20, 70):
        draw.line([(gx, my0 + 20), (gx, my1 - 20)], fill=(185, 195, 205, 180), width=1)
    for gy in range(my0 + 40, my1 - 20, 70):
        draw.line([(mx0 + 20, gy), (mx1 - 20, gy)], fill=(185, 195, 205, 180), width=1)
        
    # 4. Topographic Elevation Contour Rings (Simulated terrain curves)
    for cy in [450, 680, 1050, 1320]:
        for cx in [240, 520, 820]:
            for r in [30, 55, 80, 110, 140]:
                draw.ellipse([(cx - r, cy - r*0.7), (cx + r, cy + r*0.7)], outline=(195, 185, 160, 200), width=1)
                
    # 5. Korean Demilitarized Zone & MDL Line
    # Demarcation line (Red dashed line across map)
    mdl_y = 740
    draw.line([(mx0 + 20, mdl_y), (mx1 - 20, mdl_y)], fill=(193, 18, 31, 240), width=5)
    # DMZ 2km Northern and Southern boundary lines
    draw.line([(mx0 + 20, mdl_y - 120), (mx1 - 20, mdl_y - 120)], fill=(193, 18, 31, 140), width=2)
    draw.line([(mx0 + 20, mdl_y + 120), (mx1 - 20, mdl_y + 120)], fill=(30, 80, 160, 140), width=2)
    
    # DMZ Zone shading
    draw.rectangle([mx0 + 20, mdl_y - 120, mx1 - 20, mdl_y], fill=(245, 220, 220, 80))
    draw.rectangle([mx0 + 20, mdl_y, mx1 - 20, mdl_y + 120], fill=(220, 230, 245, 80))
    
    # 6. Tactical Annotations & Stencils
    try:
        font_stamp_lg = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 26)
        font_map_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 24)
        font_unit = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 20)
    except:
        font_stamp_lg = ImageFont.load_default()
        font_map_bold = ImageFont.load_default()
        font_unit = ImageFont.load_default()
        
    draw.text((mx0 + 40, my0 + 35), "CLASSIFIED // USFK WAR PLAN 5027 // JSA OPERATIONAL SECTOR", font=font_stamp_lg, fill=(180, 25, 30))
    draw.text((mx0 + 40, mdl_y - 35), "MILITARY DEMARCATION LINE (38°40'N)", font=font_map_bold, fill=(193, 18, 31))
    draw.text((mx0 + 40, mdl_y - 150), "NORTHERN LIMIT LINE // KPA SECTOR", font=font_unit, fill=(180, 40, 40))
    draw.text((mx0 + 40, mdl_y + 130), "SOUTHERN LIMIT LINE // UNCMAC SECTOR", font=font_unit, fill=(30, 80, 160))
    
    # 7. Military Unit Icons (Allied Blue vs KPA Red)
    # Bridge of No Return marker
    draw.rectangle([480, mdl_y - 25, 600, mdl_y + 25], fill=(245, 195, 25, 220), outline=(0, 0, 0), width=2)
    draw.text((490, mdl_y - 12), "BRIDGE #3", font=font_unit, fill=(0, 0, 0))
    
    # Allied Force Deployment Arrows (Blue)
    for ax in [260, 540, 820]:
        draw.line([(ax, 1350), (ax, mdl_y + 40)], fill=(30, 80, 160, 240), width=6)
        draw.polygon([(ax - 16, mdl_y + 45), (ax + 16, mdl_y + 45), (ax, mdl_y + 10)], fill=(30, 80, 160, 240))
        # Unit flag box
        draw.rectangle([ax - 70, 1280, ax + 70, 1330], fill=(240, 245, 255), outline=(30, 80, 160), width=3)
        draw.text((ax - 60, 1295), "TASK FORCE", font=font_unit, fill=(20, 60, 140))
        
    # KPA Guard Posts (Red diamonds)
    for kx in [320, 540, 760]:
        draw.polygon([(kx, mdl_y - 65), (kx + 16, mdl_y - 50), (kx, mdl_y - 35), (kx - 16, mdl_y - 50)], fill=(193, 18, 31, 240))
        draw.text((kx - 30, mdl_y - 95), "KPA OP", font=font_unit, fill=(193, 18, 31))

    # 8. Large Red Declassified Rubber Stamp across corner
    draw.rounded_rectangle([mx1 - 340, my1 - 100, mx1 - 40, my1 - 40], radius=8, fill=(193, 18, 31, 220))
    draw.text((mx1 - 325, my1 - 85), "TOP SECRET // DECLASSIFIED", font=font_stamp_lg, fill=(255, 255, 255))
    
    return img

def make_dense_dmz_bunker_stage():
    """Generates a dense, weathered observation bunker stage with sandbags & camouflage (1080 x 1920)."""
    img = Image.new("RGBA", (1080, 1920), (22, 24, 28, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. Concrete texture with horizontal seams
    for y in range(0, 1920, 4):
        c = int(24 + 6 * math.sin(y / 14.0) + 3 * math.cos(y / 8.0))
        draw.line([(0, y), (1080, y)], fill=(c, c + 1, c + 2, 255))
        
    # Concrete wall blocks
    for by in range(0, 1920, 240):
        draw.line([(0, by), (1080, by)], fill=(12, 14, 16, 255), width=3)
        
    # 2. Large Observation Aperture Slot (width: 980, height: 1360)
    bx0, by0, bx1, by1 = 50, 180, 1030, 1540
    # Outer bunker frame
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=16, fill=(14, 16, 20, 255), outline=(45, 50, 60), width=4)
    # Inner viewport
    draw.rounded_rectangle([bx0 + 16, by0 + 16, bx1 - 16, by1 - 16], radius=10, fill=(18, 20, 25, 255))
    
    # 3. Tactical Warning Chevron Pattern along top frame
    for ch in range(bx0 + 16, bx1 - 20, 50):
        draw.polygon([(ch, by0 + 16), (ch + 25, by0 + 16), (ch, by0 + 44), (ch - 25, by0 + 44)], fill=(245, 195, 25, 220))
        
    # 4. Dense Sandbag Emplacement across lower aperture
    for sby in range(1200, 1520, 60):
        for sbx in range(bx0 + 16, bx1 - 80, 130):
            draw.rounded_rectangle([sbx, sby, sbx + 120, sby + 52], radius=12, fill=(65, 58, 46, 255), outline=(38, 32, 24), width=3)
            # Sandbag stitch crease
            draw.line([(sbx + 20, sby + 26), (sbx + 100, sby + 26)], fill=(50, 44, 34, 255), width=2)
            
    # 5. Stencil markings on concrete
    try:
        font_st = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 22)
    except:
        font_st = ImageFont.load_default()
    draw.text((bx0 + 35, by0 + 40), "DMZ OBSERVATION POST #3 // SECTOR 1", font=font_st, fill=(245, 195, 25, 220))
    
    return img

print("Rendering dense war room map stage...")
stage2 = make_dense_tactical_war_room_stage()
stage2.save(os.path.join(ASSET_DIR, "stage_2_pentagon.png"))

print("Rendering dense DMZ bunker stage...")
stage1 = make_dense_dmz_bunker_stage()
stage1.save(os.path.join(ASSET_DIR, "stage_1_dmz_bunker.png"))

print("Dense stages generated successfully!")
