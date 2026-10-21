"""ASS Subtitle generator in Vox style for Run Island explainer."""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "audio", "manifest.json")
OUT_ASS = os.path.join(HERE, "vox_captions.ass")

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def main():
    with open(MANIFEST, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    lines = data["lines"]
    
    # ASS Header (720x1280 base coordinates)
    # MarginV: 220 from bottom to stay well clear of YouTube Shorts player controls
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: VoxTitle,Archivo Black,28,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3.5,2.0,2,60,60,220,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    for item in lines:
        start_str = format_time(item["start"])
        end_str = format_time(item["end"])
        
        display = item["display"]
        highlight = item["highlight"]
        
        # Color codes in ASS: &H00BBGGRR
        # Yellow: &H002EFFFF
        # White: &H00FFFFFF
        if highlight in display:
            formatted_text = display.replace(highlight, f"{{\\c&H002EFFFF}}{highlight}{{\\c&H00FFFFFF}}")
        else:
            formatted_text = display
            
        events.append(f"Dialogue: 0,{start_str},{end_str},VoxTitle,,0,0,0,,{formatted_text}")
        
    full_ass = header + "\n".join(events) + "\n"
    
    with open(OUT_ASS, "w", encoding="utf-8") as f:
        f.write(full_ass)
        
    print(f"Generated Vox ASS subtitles at {OUT_ASS}")

if __name__ == "__main__":
    main()
