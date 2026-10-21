import subprocess
import os

assets_dir = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/assets"
out_dir = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway"

s1_vid = f"{assets_dir}/scene_1_cutaway.mp4"
s4_vid = f"{assets_dir}/scene_4_trapdoor.mp4"
s5_vid = f"{assets_dir}/scene_5_gates_outro.mp4"
s1_interior_img = f"{assets_dir}/s1_t9.8.jpg"
s1_head_img = f"{assets_dir}/s1_t2.jpg"

bg_video_path = f"{out_dir}/bg_smooth_master.mp4"

# 1. Part 1 (0 to 10.03s): scene_1_cutaway scaled to 1080x1920 30fps
cmd1 = [
    'ffmpeg', '-y', '-i', s1_vid,
    '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
    '-t', '10.03',
    f'{out_dir}/part1.mp4'
]
subprocess.run(cmd1, check=True)
print("Part 1 built (10.03s)")

# 2. Part 2 (10.03s to 15.16s = 5.13s): s1_t9.8.jpg smooth zoom 1.0 to 1.08
cmd2 = [
    'ffmpeg', '-y', '-loop', '1', '-i', s1_interior_img,
    '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,zoompan=z=\'min(zoom+0.0006,1.1)\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d=154:s=1080x1920:fps=30',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
    '-t', '5.13',
    f'{out_dir}/part2.mp4'
]
subprocess.run(cmd2, check=True)
print("Part 2 built (5.13s)")

# 3. Part 3 (15.16s to 25.84s = 10.68s): s1_t2.jpg macro zoom into horse head & nostrils
# Nostrils/mane are in upper half: x=380, y=360
cmd3 = [
    'ffmpeg', '-y', '-loop', '1', '-i', s1_head_img,
    '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,zoompan=z=\'min(1.45+0.0005*on,1.75)\':x=\'iw*0.35-(iw/zoom/2)\':y=\'ih*0.25-(ih/zoom/2)\':d=321:s=1080x1920:fps=30',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
    '-t', '10.68',
    f'{out_dir}/part3.mp4'
]
subprocess.run(cmd3, check=True)
print("Part 3 built (10.68s)")

# 4. Part 4 (25.84s to 34.32s = 8.48s): scene_4_trapdoor at native 30fps
cmd4 = [
    'ffmpeg', '-y', '-i', s4_vid,
    '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
    '-t', '8.48',
    f'{out_dir}/part4.mp4'
]
subprocess.run(cmd4, check=True)
print("Part 4 built (8.48s)")

# 5. Part 5 (34.32s to 45.80s = 11.48s): scene_5_gates_outro at native 30fps
cmd5 = [
    'ffmpeg', '-y', '-i', s5_vid,
    '-vf', 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
    '-t', '11.48',
    f'{out_dir}/part5.mp4'
]
subprocess.run(cmd5, check=True)
print("Part 5 built (11.48s)")

# Concatenate all 5 parts into bg_smooth_master.mp4
concat_list = f"{out_dir}/concat_parts.txt"
with open(concat_list, "w") as f:
    f.write(f"file '{out_dir}/part1.mp4'\n")
    f.write(f"file '{out_dir}/part2.mp4'\n")
    f.write(f"file '{out_dir}/part3.mp4'\n")
    f.write(f"file '{out_dir}/part4.mp4'\n")
    f.write(f"file '{out_dir}/part5.mp4'\n")

cmd_cat = [
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_list,
    '-c', 'copy',
    bg_video_path
]
subprocess.run(cmd_cat, check=True)
print(f"Concatenated 5 parts into {bg_video_path} successfully!")
