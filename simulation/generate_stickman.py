import math
from PIL import Image, ImageDraw

WIDTH = 1024
HEIGHT = 1024
BG_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
LINE_WIDTH = 4

def draw_stickman(draw, x, y, scale=1.0, costume= suit, arm_angle_l=20, arm_angle_r=20):
    r = int(45 * scale)
    head_center = (x, y - int(120 * scale))
    draw.ellipse([head_center[0] - r, head_center[1] - r, head_center[0] + r, head_center[1] + r], outline=WHITE, width=LINE_WIDTH)
    eye_r = max(2, int(4 * scale))
    draw.ellipse([head_center[0] - int(15 * scale) - eye_r, head_center[1] - eye_r, head_center[0] - int(15 * scale) + eye_r, head_center[1] + eye_r], fill=WHITE)
    draw.ellipse([head_center[0] + int(15 * scale) - eye_r, head_center[1] - eye_r, head_center[0] + int(15 * scale) + eye_r, head_center[1] + eye_r], fill=WHITE)
    draw.line([head_center[0] - int(12 * scale), head_center[1] + int(20 * scale), head_center[0] + int(12 * scale), head_center[1] + int(20 * scale)], fill=WHITE, width=LINE_WIDTH)

    neck = (x, head_center[1] + r)
    pelvis = (x, y + int(70 * scale))
    draw.line([neck, pelvis], fill=WHITE, width=LINE_WIDTH)

    if costume == suit:
        draw.line([neck[0] - int(15 * scale), neck[1] + int(10 * scale), neck[0], neck[1] + int(35 * scale)], fill=WHITE, width=LINE_WIDTH)
        draw.line([neck[0] + int(15 * scale), neck[1] + int(10 * scale), neck[0], neck[1] + int(35 * scale)], fill=WHITE, width=LINE_WIDTH)
        draw.line([neck[0] - int(30 * scale), neck[1] + int(15 * scale), neck[0] - int(25 * scale), pelvis[1]], fill=WHITE, width=LINE_WIDTH)
        draw.line([neck[0] + int(30 * scale), neck[1] + int(15 * scale), neck[0] + int(25 * scale), pelvis[1]], fill=WHITE, width=LINE_WIDTH)

    shoulder = (x, neck[1] + int(25 * scale))
    arm_len = int(60 * scale)
    
    rad_l = math.radians(arm_angle_l + 90)
    elbow_l = (int(shoulder[0] + arm_len * math.cos(rad_l)), int(shoulder[1] + arm_len * math.sin(rad_l)))
    hand_l = (int(elbow_l[0] + arm_len * math.cos(rad_l)), int(elbow_l[1] + arm_len * math.sin(rad_l)))
    draw.line([shoulder, elbow_l, hand_l], fill=WHITE, width=LINE_WIDTH)

    rad_r = math.radians(-arm_angle_r + 90)
    elbow_r = (int(shoulder[0] + arm_len * math.cos(rad_r)), int(shoulder[1] + arm_len * math.sin(rad_r)))
    hand_r = (int(elbow_r[0] + arm_len * math.cos(rad_r)), int(elbow_r[1] + arm_len * math.sin(rad_r)))
    draw.line([shoulder, elbow_r, hand_r], fill=WHITE, width=LINE_WIDTH)

    leg_len = int(75 * scale)
    hip_l = (pelvis[0] - int(10 * scale), pelvis[1])
    hip_r = (pelvis[0] + int(10 * scale), pelvis[1])
    draw.line([hip_l, (hip_l[0] - int(20 * scale), hip_l[1] + leg_len), (hip_l[0] - int(25 * scale), hip_l[1] + leg_len * 2)], fill=WHITE, width=LINE_WIDTH)
    draw.line([hip_r, (hip_r[0] + int(20 * scale), hip_r[1] + leg_len), (hip_r[0] + int(25 * scale), hip_r[1] + leg_len * 2)], fill=WHITE, width=LINE_WIDTH)

img_ref = Image.new(\RGB\, (WIDTH, HEIGHT), BG_COLOR)
draw_ref = ImageDraw.Draw(img_ref)
draw_stickman(draw_ref, 512, 580, scale=1.6, costume=\suit\, arm_angle_l=20, arm_angle_r=20)
img_ref.save(\simulation/assets/STICKMAN_ref.png\)
print(\Reference image generated successfully!\)
