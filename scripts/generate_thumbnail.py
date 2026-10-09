#!/usr/bin/env python3
"""
Automated YouTube Thumbnail Generator for @IRinANutshell
Matches the official Photoshop template structure:
- 1920x1080 Canvas (16:9)
- Split screen: Solid black left side + Artistic brush/torn-paper mask transition
- Thematic background image on the right side
- Canonical Typography: Archivo Black (Titles) & Space Mono (Taglines/URLs)
- Red & White academic contrast scheme (#FC1919 & #FFFFFF)
- Integrated YouTube engagement CTA badges (Bell, Subscribe, Like)
"""

import argparse
import os
import sys
from PIL import Image, ImageFont, ImageDraw

# Default paths and configurations
DEFAULT_OVERLAY_PATH = os.path.join(os.path.dirname(__file__), "assets", "thumbnail_overlay_template.png")
ALT_OVERLAY_PATH = r"D:\PERSONAL PROJECT\IR In The Nutshell\Channel Asset\thumbnail_overlay_template.png"

FONT_CANDIDATES_TITLE = [
    r"C:\Users\xiyeo\AppData\Local\Microsoft\Windows\Fonts\ArchivoBlack-Regular.ttf",
    r"C:\Windows\Fonts\ArchivoBlack-Regular.ttf",
    os.path.join(os.path.dirname(__file__), "assets", "ArchivoBlack-Regular.ttf"),
]

FONT_CANDIDATES_MONO = [
    r"C:\Users\xiyeo\AppData\Local\Microsoft\Windows\Fonts\SpaceMono-Regular.ttf",
    r"C:\Windows\Fonts\SpaceMono-Regular.ttf",
    os.path.join(os.path.dirname(__file__), "assets", "SpaceMono-Regular.ttf"),
]

RED_COLOR = (252, 25, 25, 255)      # Canonical vibrant red #FC1919
WHITE_COLOR = (255, 255, 255, 255)  # Crisp white #FFFFFF

def find_font(candidates, fallback="Arial"):
    for path in candidates:
        if os.path.exists(path):
            return path
    return fallback

def parse_lines_and_colors(title_input, default_colors=None):
    """
    Parses title lines and supports markup like:
    [red]GLOBALIZATION[/red]
    [white]AND[/white]
    [red]GLOBAL POLITICS[/red]
    Or defaults to alternating colors (Red, White, Red, White...).
    """
    raw_lines = [l.strip() for l in title_input.replace("\\n", "\n").split("\n") if l.strip()]
    parsed = []
    
    for i, line in enumerate(raw_lines):
        color = None
        text = line
        
        # Check custom tags
        if "[red]" in line.lower() and "[/red]" in line.lower():
            text = line.replace("[red]", "").replace("[RED]", "").replace("[/red]", "").replace("[/RED]", "").strip()
            color = RED_COLOR
        elif "[white]" in line.lower() and "[/white]" in line.lower():
            text = line.replace("[white]", "").replace("[WHITE]", "").replace("[/white]", "").replace("[/WHITE]", "").strip()
            color = WHITE_COLOR
        else:
            # Alternate default scheme: Red, White, Red, Red/White
            if len(raw_lines) == 1:
                color = RED_COLOR
            elif len(raw_lines) == 2:
                color = RED_COLOR if i == 0 else WHITE_COLOR
            elif len(raw_lines) == 3:
                color = RED_COLOR if i in (0, 2) else WHITE_COLOR
            else:
                color = RED_COLOR if i % 2 == 0 else WHITE_COLOR
                
        parsed.append((text.upper(), color))
    return parsed

def process_background(bg_raw: Image.Image, canvas_w: int, canvas_h: int, mode: str = "cover", anchor: str = "center") -> Image.Image:
    """
    Processes right-side background image:
    - 'cover': Scales image to fill entire 1920x1080 canvas (ideal for photos)
    - 'fit-right': Scales image to neatly fit within the right-side reveal window (x=780..1900, y=50..1030)
      on a crisp white background (ideal for full mind map posters)
    """
    if mode == "fit-right":
        base = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 255))
        target_w = 860
        target_h = 960
        target_x = 1020
        target_y = 60
        
        bg_w, bg_h = bg_raw.size
        scale = min(target_w / bg_w, target_h / bg_h)
        new_w, new_h = int(bg_w * scale), int(bg_h * scale)
        bg_resized = bg_raw.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        pos_x = target_x + (target_w - new_w) // 2
        pos_y = target_y + (target_h - new_h) // 2
        base.paste(bg_resized, (pos_x, pos_y), bg_resized if bg_resized.mode == "RGBA" else None)
        return base
    else:
        bg_w, bg_h = bg_raw.size
        scale = max(canvas_w / bg_w, canvas_h / bg_h)
        new_w, new_h = int(bg_w * scale), int(bg_h * scale)
        bg_resized = bg_raw.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        if anchor == "right":
            offset_x = new_w - canvas_w
        elif anchor == "left":
            offset_x = 0
        else:
            offset_x = (new_w - canvas_w) // 2
            
        offset_y = (new_h - canvas_h) // 2
        return bg_resized.crop((offset_x, offset_y, offset_x + canvas_w, offset_y + canvas_h))

def generate_thumbnail(
    title: str,
    image_path: str,
    output_path: str,
    tagline: str = "International Relations in a nutshell",
    url: str = "https://ir-guide.netlify.app/",
    mode: str = "cover",
    anchor: str = "center",
    overlay_path: str | None = None,
    custom_title_font: str | None = None,
    custom_mono_font: str | None = None
) -> str:
    # 1. Resolve overlay
    resolved_overlay = overlay_path
    if not resolved_overlay or not os.path.exists(resolved_overlay):
        if os.path.exists(DEFAULT_OVERLAY_PATH):
            resolved_overlay = DEFAULT_OVERLAY_PATH
        elif os.path.exists(ALT_OVERLAY_PATH):
            resolved_overlay = ALT_OVERLAY_PATH
        else:
            raise FileNotFoundError(f"Thumbnail overlay template not found at {DEFAULT_OVERLAY_PATH}")

    overlay_img = Image.open(resolved_overlay).convert("RGBA")
    canvas_w, canvas_h = 1920, 1080

    # 2. Process right-side background image
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Background image not found: {image_path}")

    bg_raw = Image.open(image_path).convert("RGBA")
    bg_processed = process_background(bg_raw, canvas_w, canvas_h, mode=mode, anchor=anchor)

    # 3. Composite background + overlay frame
    canvas = Image.alpha_composite(bg_processed, overlay_img)

    # 4. Resolve typography
    title_font_path = custom_title_font or find_font(FONT_CANDIDATES_TITLE)
    mono_font_path = custom_mono_font or find_font(FONT_CANDIDATES_MONO)

    draw = ImageDraw.Draw(canvas)

    # Header tagline
    try:
        font_tag = ImageFont.truetype(mono_font_path, 24)
    except Exception:
        font_tag = ImageFont.load_default()
    draw.text((80, 115), tagline, font=font_tag, fill=WHITE_COLOR)

    # Footer URL
    try:
        font_url = ImageFont.truetype(mono_font_path, 26)
    except Exception:
        font_url = ImageFont.load_default()
    draw.text((462, 970), url, font=font_url, fill=WHITE_COLOR)

    # 5. Process & draw main title lines
    parsed_lines = parse_lines_and_colors(title)
    
    # Available content box on left side
    max_text_width = 860
    left_x = 75
    top_bound = 240
    bottom_bound = 880
    available_height = bottom_bound - top_bound

    # Calculate optimal font size dynamically so text never overflows safe margins
    num_lines = len(parsed_lines)
    base_font_size = 92 if num_lines <= 3 else 74

    # Iterative sizing
    chosen_font_size = base_font_size
    while chosen_font_size >= 36:
        test_font = ImageFont.truetype(title_font_path, chosen_font_size)
        fits = True
        line_heights = []
        for text, _ in parsed_lines:
            bbox = draw.textbbox((0, 0), text, font=test_font)
            line_w = bbox[2] - bbox[0]
            line_h = bbox[3] - bbox[1]
            line_heights.append(line_h)
            if line_w > max_text_width:
                fits = False
                break
        total_h = sum(line_heights) + (num_lines - 1) * (chosen_font_size * 0.45)
        if fits and total_h <= available_height:
            break
        chosen_font_size -= 4

    final_title_font = ImageFont.truetype(title_font_path, chosen_font_size)
    
    # Compute exact line heights and total block height
    line_metrics = []
    for text, color in parsed_lines:
        bbox = draw.textbbox((0, 0), text, font=final_title_font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        line_metrics.append((text, color, w, h))

    line_spacing = int(chosen_font_size * 0.48)
    total_block_h = sum(m[3] for m in line_metrics) + (num_lines - 1) * line_spacing
    
    # Center block vertically in the available area
    current_y = top_bound + (available_height - total_block_h) // 2

    for text, color, w, h in line_metrics:
        draw.text((left_x, current_y), text, font=final_title_font, fill=color)
        current_y += h + line_spacing

    # 6. Save output
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    # Convert to RGB if saving to JPG
    if output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
        final_img = canvas.convert("RGB")
        final_img.save(output_path, "JPEG", quality=95)
    else:
        canvas.save(output_path, "PNG")

    print(f"[SUCCESS] YouTube thumbnail generated: {output_path}")
    return output_path

def main():
    parser = argparse.ArgumentParser(description="YouTube Mind Map Thumbnail Generator")
    parser.add_argument("--title", required=True, help="Title text (use \\n for line breaks, or [red]...[/red] [white]...[/white])")
    parser.add_argument("--image", required=True, help="Path to right-side visual image/photo/poster")
    parser.add_argument("--output", required=True, help="Path to save output thumbnail (.png or .jpg)")
    parser.add_argument("--mode", default="cover", choices=["cover", "fit-right"], help="Background fitting mode ('cover' for photos, 'fit-right' for posters)")
    parser.add_argument("--anchor", default="center", choices=["center", "right", "left"], help="Horizontal crop anchor for cover mode")
    parser.add_argument("--tagline", default="International Relations in a nutshell", help="Header tagline text")
    parser.add_argument("--url", default="https://ir-guide.netlify.app/", help="Footer website URL")
    parser.add_argument("--overlay", default=None, help="Path to custom overlay template PNG")

    args = parser.parse_args()
    generate_thumbnail(
        title=args.title,
        image_path=args.image,
        output_path=args.output,
        mode=args.mode,
        anchor=args.anchor,
        tagline=args.tagline,
        url=args.url,
        overlay_path=args.overlay
    )

if __name__ == "__main__":
    main()
