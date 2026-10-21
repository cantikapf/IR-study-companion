import subprocess
import os

project_dir = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway"
assets_dir = f"{project_dir}/assets"

s1_vid = f"{assets_dir}/scene_1_cutaway.mp4"
s4_vid = f"{assets_dir}/scene_4_trapdoor.mp4"
s5_vid = f"{assets_dir}/scene_5_gates_outro.mp4"
bg_out = f"{project_dir}/bg_smooth_master.mp4"

# 1. Part 1 (0 to 10.03s): scene_1_cutaway at 1080x1920 30fps native speed
cmd1 = [
    'ffmpeg', '-y', '-i', s1_vid,
    '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
    '-t', '10.03',
    f'{project_dir}/short_part1.mp4'
]
subprocess.run(cmd1, check=True)
print("Short Part 1 built (10.03s)")

# 2. Part 2 (10.03s to 18.03s = 8.00s): scene_4_trapdoor at 1080x1920 30fps native speed
cmd2 = [
    'ffmpeg', '-y', '-i', s4_vid,
    '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
    '-t', '8.00',
    f'{project_dir}/short_part2.mp4'
]
subprocess.run(cmd2, check=True)
print("Short Part 2 built (8.00s)")

# 3. Part 3 (18.03s to 25.73s = 7.70s): scene_5_gates_outro starting at 7.0s (Greek hoplites on cobblestones with swords & shields!)
cmd3 = [
    'ffmpeg', '-y', '-ss', '00:00:07.00', '-i', s5_vid,
    '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
    '-t', '7.70',
    f'{project_dir}/short_part3.mp4'
]
subprocess.run(cmd3, check=True)
print("Short Part 3 built (7.70s) with hoplites on cobblestones!")

# Concatenate all 3 parts into bg_smooth_master.mp4
concat_txt = f"{project_dir}/short_concat.txt"
with open(concat_txt, "w") as f:
    f.write(f"file '{project_dir}/short_part1.mp4'\n")
    f.write(f"file '{project_dir}/short_part2.mp4'\n")
    f.write(f"file '{project_dir}/short_part3.mp4'\n")

cmd_cat = [
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_txt,
    '-c', 'copy',
    bg_out
]
subprocess.run(cmd_cat, check=True)
print(f"Concatenated 3 parts into {bg_out} (exact 25.73s)!")
