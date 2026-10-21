import os

font_dir = os.path.abspath("learning-videos/shorts-experiments/sh-04-cuban-missile-b59/fonts")

# Buat file ASS (Advanced SubStation Alpha)
# Target: 720x1280.
# Area aman bawah: y sekitar 1040 - 1100 (MarginV: 180 - 220 dari bawah).
# Gaya: Archivo Black, FontSize 26 (di 720p), bold, border tebal hitam tanpa box kaku, highlight warna kuning/merah.

ass_content = f"""[Script Info]
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
Dialogue: 0,0:00:00.30,0:00:04.20,VoxTitle,,0,0,0,,OCTOBER 1962\N{\c&H002EFFFF}TRAPPED{\c&H00FFFFFF} UNDER DEPTH CHARGES
Dialogue: 0,0:00:04.20,0:00:08.80,VoxTitle,,0,0,0,,SOVIET SUB B-59\N{\c&H00002EFF}LOST ALL CONTACT{\c&H00FFFFFF} WITH MOSCOW
Dialogue: 0,0:00:10.30,0:00:14.20,VoxTitle,,0,0,0,,CONVINCED WORLD WAR 3 BEGAN\N{\c&H00002EFF}TWO OFFICERS VOTED TO FIRE{\c&H00FFFFFF}
Dialogue: 0,0:00:14.20,0:00:18.20,VoxTitle,,0,0,0,,A 10-KILOTON NUCLEAR TORPEDO\N{\c&H002EFFFF}BUT ONE MAN SAID NO{\c&H00FFFFFF}
Dialogue: 0,0:00:20.30,0:00:24.50,VoxTitle,,0,0,0,,VASILY ARKHIPOV\N{\c&H002EFFFF}REFUSED AUTHORIZATION{\c&H00FFFFFF}
Dialogue: 0,0:00:24.50,0:00:29.20,VoxTitle,,0,0,0,,THE SUB SURFACED PEACEFULLY\N{\c&H002EFFFF}SAVING HUMAN CIVILIZATION{\c&H00FFFFFF}
"""

with open("learning-videos/shorts-experiments/sh-04-cuban-missile-b59/vox_captions.ass", "w", encoding="utf-8") as f:
    f.write(ass_content)
print("Saved ASS file successfully!")
