import os
import math
from PIL import Image, ImageDraw, ImageFont

ASSET_DIR = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/paul-bunyan-1976/assets"

def make_clean_tactical_war_room_stage():
    """Generates an ultra-clean, authentic military tactical map stage without any collisions (1080 x 1920)."""
    img = Image.new("RGBA", (1080, 1920), (14, 20, 16, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. Dark mahogany desk perimeter with wood grain
    for y in range(0, 1920, 4):
        v = int(18 + 6 * math.sin(y / 20.0))
        draw.line([(0, y), (1080, y)], fill=(v, v + 2, v + 1, 255))
        
    # 2. Large Tactical Paper Map Surface (mx0=50 to mx1=1030, my0=200 to my1=1660)
    mx0, my0, mx1, my1 = 50, 200, 1030, 1660
    draw.rounded_rectangle([mx0, my0, mx1, my1], radius=16, fill=(228, 222, 204, 255))
    draw.rounded_rectangle([mx0 + 16, my0 + 16, mx1 - 16, my1 - 16], radius=10, fill=(240, 235, 218, 255))
    
    # 3. Tactical Military Grid (1000m UTM Grid lines in subtle cyan-gray)
    for gx in range(mx0 + 40, mx1 - 20, 70):
        draw.line([(gx, my0 + 20), (gx, my1 - 20)], fill=(185, 195, 205, 180), width=1)
    for gy in range(my0 + 40, my1 - 20, 70):
        draw.line([(mx0 + 20, gy), (mx1 - 20, gy)], fill=(185, 195, 205, 180), width=1)
        
    # 4. Topographic Elevation Contour Rings (ONLY in upper corners, away from cards and subtitle box)
    for cy in [360]:
        for cx in [220, 860]:
            for r in [35, 65, 95]:
                draw.ellipse([(cx - r, cy - r*0.65), (cx + r, cy + r*0.65)], outline=(195, 185, 160, 160), width=1)
                
    # 5. Fonts setup
    font_stamp_lg = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 22)
    font_map_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
    font_unit = ImageFont.truetype("C:/Windows/Fonts/courbd.ttf", 18)
    
    # Header: Top Map Banner (Y = 225)
    draw.rectangle([mx0 + 32, my0 + 20, mx1 - 32, my0 + 55], fill=(240, 235, 218, 255))
    draw.text((mx0 + 40, my0 + 25), "CLASSIFIED // USFK WAR PLAN 5027 // JSA OPERATIONAL SECTOR", font=font_stamp_lg, fill=(180, 25, 30))
    
    # 6. Demarcation Sector (Mathematically budgeted between Y=1070 and Y=1370)
    # Demarcation label at Y = 1095 (generous 53px gap below counter-box which ends at 1042)
    draw.text((mx0 + 40, 1095), "MILITARY DEMARCATION LINE (38°40'N)", font=font_map_bold, fill=(193, 18, 31))
    
    # Red Demarcation Line at Y = 1125
    mdl_y = 1125
    draw.line([(mx0 + 30, mdl_y), (mx1 - 30, mdl_y)], fill=(193, 18, 31, 240), width=4)
    
    # 7. Allied Force Deployment Arrows & Task Force Units (Cleanly layered, ZERO collisions)
    # Arrowheads: Y = 1146 (pointing north, stopping with 21px gap before the red line at 1125)
    # Arrow shafts: Y = 1162 to Y = 1230
    # Task Force Boxes: Y = 1235 to Y = 1285 (solid white fill, blocks grid lines)
    for ax in [260, 540, 820]:
        # Arrowhead pointing north at Y = 1146
        draw.polygon([(ax - 14, 1165), (ax + 14, 1165), (ax, 1146)], fill=(30, 80, 160, 240))
        # Arrow shaft
        draw.line([(ax, 1232), (ax, 1165)], fill=(30, 80, 160, 240), width=5)
        
        # Unit Box: Y = 1235 to 1285 with solid white background
        draw.rounded_rectangle([ax - 75, 1235, ax + 75, 1285], radius=6, fill=(255, 255, 255, 255), outline=(30, 80, 160), width=3)
        draw.text((ax - 55, 1251), "TASK FORCE", font=font_unit, fill=(20, 60, 140))
        
    # 8. Dynamic TOP SECRET stamp at bottom right (Y = 1560 to 1620)
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
    print("Saved ultra-clean stage_2_pentagon.png with zero collisions!")

if __name__ == "__main__":
    make_clean_tactical_war_room_stage()
