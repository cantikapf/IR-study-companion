import os, math
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080
FPS = 24
TOTAL_SEC = 45
TOTAL_FRAMES = TOTAL_SEC * FPS
BG = (0, 0, 0)
WHITE = (255, 255, 255)
LW = 5

os.makedirs('simulation/frames', exist_ok=True)

# Try loading font or default
try:
    font_large = ImageFont.truetype('arial.ttf', 72)
    font_mid = ImageFont.truetype('arial.ttf', 48)
    font_sub = ImageFont.truetype('arial.ttf', 38)
except:
    font_large = ImageFont.load_default()
    font_mid = font_large
    font_sub = font_large

def draw_stick(draw, x, y, scale=1.2, arm_l_deg=20, arm_r_deg=20, costume='tie', head_tilt=0):
    r = int(50 * scale)
    hc = (x, y - int(130 * scale))
    draw.ellipse([hc[0]-r, hc[1]-r, hc[0]+r, hc[1]+r], outline=WHITE, width=LW)
    
    # Eyes & Mouth with tilt
    rad_t = math.radians(head_tilt)
    dx = int(18 * scale * math.cos(rad_t))
    dy = int(18 * scale * math.sin(rad_t))
    draw.ellipse([hc[0]-dx-4, hc[1]-dy-4, hc[0]-dx+4, hc[1]-dy+4], fill=WHITE)
    draw.ellipse([hc[0]+dx-4, hc[1]+dy-4, hc[0]+dx+4, hc[1]+dy+4], fill=WHITE)
    draw.line([hc[0]-int(15*scale), hc[1]+int(22*scale), hc[0]+int(15*scale), hc[1]+int(22*scale)], fill=WHITE, width=LW)
    
    neck = (x, hc[1]+r)
    pelvis = (x, y + int(80 * scale))
    draw.line([neck, pelvis], fill=WHITE, width=LW)
    
    if costume == 'tie':
        draw.polygon([(x-int(10*scale), neck[1]), (x+int(10*scale), neck[1]), (x, neck[1]+int(22*scale))], outline=WHITE)
        draw.line([x, neck[1]+int(22*scale), x, neck[1]+int(85*scale)], fill=WHITE, width=LW)
        
    shoulder = (x, neck[1] + int(28 * scale))
    arm_len = int(70 * scale)
    
    # Left arm
    rad_l = math.radians(arm_l_deg + 90)
    el_l = (int(shoulder[0] + arm_len * math.cos(rad_l)), int(shoulder[1] + arm_len * math.sin(rad_l)))
    h_l = (int(el_l[0] + arm_len * math.cos(rad_l)), int(el_l[1] + arm_len * math.sin(rad_l)))
    draw.line([shoulder, el_l, h_l], fill=WHITE, width=LW)
    
    # Right arm
    rad_r = math.radians(-arm_r_deg + 90)
    el_r = (int(shoulder[0] + arm_len * math.cos(rad_r)), int(shoulder[1] + arm_len * math.sin(rad_r)))
    h_r = (int(el_r[0] + arm_len * math.cos(rad_r)), int(el_r[1] + arm_len * math.sin(rad_r)))
    draw.line([shoulder, el_r, h_r], fill=WHITE, width=LW)
    
    # Legs
    leg_len = int(90 * scale)
    draw.line([(x-int(12*scale), pelvis[1]), (x-int(28*scale), pelvis[1]+leg_len), (x-int(32*scale), pelvis[1]+leg_len*2)], fill=WHITE, width=LW)
    draw.line([(x+int(12*scale), pelvis[1]), (x+int(28*scale), pelvis[1]+leg_len), (x+int(32*scale), pelvis[1]+leg_len*2)], fill=WHITE, width=LW)

print('Rendering frames...')
for i in range(TOTAL_FRAMES):
    t = i / FPS
    img = Image.new('RGB', (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)
    
    # Chapter 1: Hook (0s - 12s) - Leader suspicion & Anarchy
    if t < 12:
        # Two leaders facing each other across a table / divide
        # Figure 1 walks from left to 650
        x1 = min(650, int(200 + t * 90))
        x2 = max(1270, int(1720 - t * 90))
        arm_wave = int(15 * math.sin(t * 4))
        draw_stick(draw, x1, 620, scale=1.3, arm_l_deg=-20+arm_wave, arm_r_deg=30, costume='tie')
        draw_stick(draw, x2, 620, scale=1.3, arm_l_deg=30, arm_r_deg=-20-arm_wave, costume='tie')
        
        # Draw question mark or divide
        if t > 3:
            draw.line([(960, 300), (960, 850)], fill=WHITE, width=3)
            draw.text((960, 240), '?', fill=WHITE, font=font_large, anchor='mm')
            
        # Draw subtitle label
        if t < 6:
            draw.text((960, 950), 'Kenapa para pemimpin dunia selalu curiga?', fill=WHITE, font=font_sub, anchor='mm')
        else:
            draw.text((960, 950), 'Apakah perdamaian semudah berniat baik?', fill=WHITE, font=font_sub, anchor='mm')

    # Chapter 2: The Theorist - Hans Morgenthau & Human Nature (12s - 24s)
    elif t < 24:
        rel_t = t - 12
        # Center Scholar Stickman with glasses/book
        draw_stick(draw, 960, 620, scale=1.4, arm_l_deg=-40, arm_r_deg=-40, costume='tie')
        
        # Book / Pedestal in front
        draw.rectangle([860, 620, 1060, 740], outline=WHITE, width=LW)
        draw.text((960, 680), 'POLITICS', fill=WHITE, font=font_mid, anchor='mm')
        
        # Morgenthau Quote banner
        draw.text((960, 180), 'HANS MORGENTHAU (1948)', fill=WHITE, font=font_large, anchor='mm')
        draw.line([(600, 230), (1320, 230)], fill=WHITE, width=4)
        
        if rel_t < 6:
            draw.text((960, 950), 'Bapak Realisme Klasik Hubungan Internasional', fill=WHITE, font=font_sub, anchor='mm')
        else:
            draw.text((960, 950), 'Politik Berakar dari Sifat Dasar Manusia (Animus Dominandi)', fill=WHITE, font=font_sub, anchor='mm')

    # Chapter 3: The Framework - Anarchy & Power as Currency (24s - 36s)
    elif t < 36:
        rel_t = t - 24
        # Left side: Anarchy (No police)
        # Center: Scales of Power
        draw.line([(960, 300), (960, 700)], fill=WHITE, width=6)
        draw.line([(700, 420), (1220, 420)], fill=WHITE, width=6)
        # Pan Left & Right
        tilt = int(40 * math.sin(rel_t * 2))
        draw.line([(700, 420), (620, 560 + tilt)], fill=WHITE, width=4)
        draw.line([(700, 420), (780, 560 + tilt)], fill=WHITE, width=4)
        draw.rectangle([580, 560 + tilt, 820, 580 + tilt], outline=WHITE, width=LW)
        draw.text((700, 530 + tilt), 'STATE A', fill=WHITE, font=font_mid, anchor='mm')
        
        draw.line([(1220, 420), (1140, 560 - tilt)], fill=WHITE, width=4)
        draw.line([(1220, 420), (1300, 560 - tilt)], fill=WHITE, width=4)
        draw.rectangle([1100, 560 - tilt, 1340, 580 - tilt], outline=WHITE, width=LW)
        draw.text((1220, 530 - tilt), 'STATE B', fill=WHITE, font=font_mid, anchor='mm')
        
        draw.text((960, 180), 'ANARKI & IMBANGAN KEKUASAAN', fill=WHITE, font=font_large, anchor='mm')
        
        if rel_t < 6:
            draw.text((960, 950), 'Anarki Global: Tanpa Polisi Dunia = Self-Help System', fill=WHITE, font=font_sub, anchor='mm')
        else:
            draw.text((960, 950), 'Kepentingan Nasional Dihitung dengan KEKUASAAN (Power)', fill=WHITE, font=font_sub, anchor='mm')

    # Chapter 4: The Landing - See the world as it is (36s - 45s)
    else:
        rel_t = t - 36
        # Confident Diplomat Stickman facing viewer
        draw_stick(draw, 960, 580, scale=1.5, arm_l_deg=10, arm_r_deg=10, costume='tie')
        
        # Globe line-art circle
        draw.ellipse([960-350, 580-350, 960+350, 580+350], outline=WHITE, width=2)
        draw.ellipse([960-150, 580-350, 960+150, 580+350], outline=WHITE, width=2)
        draw.line([(960-350, 580), (960+350, 580)], fill=WHITE, width=2)
        
        draw.text((960, 140), 'REALISME KLASIK', fill=WHITE, font=font_large, anchor='mm')
        draw.text((960, 950), 'Melihat dunia apa adanya, bukan yang kita inginkan.', fill=WHITE, font=font_sub, anchor='mm')

    img.save(f'simulation/frames/frame_{i:04d}.png')

print(f'Done rendering {TOTAL_FRAMES} frames!')
