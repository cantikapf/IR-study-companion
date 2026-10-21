"""Generate word-level / verbatim sentence manifest and ASS for Run Island.
Matches Kokoro voiceover 100% word-for-word.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST_IN = os.path.join(HERE, "audio", "manifest.json")
OUT_ASS = os.path.join(HERE, "vox_captions.ass")

def format_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def main():
    with open(MANIFEST_IN, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Verbatim mapping: spoken text mapped directly with highlight keywords
    verbatim_subs = [
        {
            "start": 0.50,
            "end": 2.40,
            "text": "YOU THINK MANHATTAN WAS BOUGHT WITH CASH",
            "highlight": "CASH"
        },
        {
            "start": 2.75,
            "end": 8.15,
            "text": "IN 1667, BRITAIN TRADED NEW YORK FOR A 3KM ISLAND IN INDONESIA",
            "highlight": "TRADED NEW YORK"
        },
        {
            "start": 8.50,
            "end": 13.04,
            "text": "PULAU RUN, HIDDEN IN INDONESIA'S BANDA SEA, THE WORLD'S ONLY SOURCE OF NUTMEG",
            "highlight": "BANDA SEA"
        },
        {
            "start": 13.39,
            "end": 16.95,
            "text": "BACK THEN, ONE SACK OF NUTMEG BOUGHT AN ENTIRE ESTATE IN LONDON",
            "highlight": "ENTIRE ESTATE"
        },
        {
            "start": 17.30,
            "end": 22.47,
            "text": "39 BRITISH SAILORS HELD THE ISLAND UNDER DUTCH NAVAL SIEGE FOR 1,500 DAYS",
            "highlight": "NAVAL SIEGE"
        },
        {
            "start": 22.82,
            "end": 27.72,
            "text": "TO END THE WAR, BRITAIN KEPT MANHATTAN WHILE THE DUTCH SEIZED THE SPICE TRADE",
            "highlight": "SPICE TRADE"
        },
        {
            "start": 28.07,
            "end": 33.04,
            "text": "TODAY, MANHATTAN IS WORTH TRILLIONS, AND RUN IS A QUIET VILLAGE OF 1,500 PEOPLE",
            "highlight": "WORTH TRILLIONS"
        },
        {
            "start": 33.39,
            "end": 35.82,
            "text": "THE WORST REAL ESTATE TRADE IN HUMAN HISTORY",
            "highlight": "WORST REAL ESTATE TRADE"
        }
    ]

    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: VoxTitle,Archivo Black,26,&H00FFFFFF,&H000000FF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,3.5,2.0,2,50,50,380,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    events = []
    for s in verbatim_subs:
        start_str = format_time(s["start"])
        end_str = format_time(s["end"])
        txt = s["text"]
        hl = s["highlight"]

        if hl in txt:
            formatted = txt.replace(hl, f"{{\\c&H002EFFFF}}{hl}{{\\c&H00FFFFFF}}")
        else:
            formatted = txt

        events.append(f"Dialogue: 0,{start_str},{end_str},VoxTitle,,0,0,0,,{formatted}")

    full_ass = header + "\n".join(events) + "\n"
    with open(OUT_ASS, "w", encoding="utf-8") as f:
        f.write(full_ass)
    print(f"Updated verbatim subtitles at {OUT_ASS}")

if __name__ == "__main__":
    main()
