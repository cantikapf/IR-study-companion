path = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the frame selection logic in updateVideoPlate
old_fn = """    if (timeSec < 24.5) {
      // Beat 1, 2, 3: scene_1_cutaway (240 frames)
      folder = "assets/frames_s1/";
      const tMod = timeSec % 10.0;
      frameNum = Math.min(240, Math.max(1, Math.floor(tMod * 24) + 1));

      // Beat 3 macro zoom on upper mane & nostrils ventilation
      if (timeSec >= 15.5 && timeSec < 24.5) {
        bgImg.style.transformOrigin = "30% 25%";
        bgImg.style.transform = "scale(1.85)";
      } else {
        bgImg.style.transformOrigin = "center center";
        bgImg.style.transform = "scale(1.0)";
      }
    }"""

new_fn = """    if (timeSec < 24.5) {
      // Beat 1, 2, 3: scene_1_cutaway (240 frames)
      folder = "assets/frames_s1/";
      
      if (timeSec < 5.56) {
        // Beat 1 (0 - 5.56s): Opening approach (frames 1 to 80)
        const prog = timeSec / 5.56;
        frameNum = Math.min(80, Math.max(1, Math.floor(prog * 80) + 1));
        bgImg.style.transformOrigin = "center center";
        bgImg.style.transform = "scale(1.0)";
      } else if (timeSec < 15.16) {
        // Beat 2 (5.56s - 15.16s): Cutaway opens and showcases 30 soldiers inside (frames 80 to 180)
        const prog = (timeSec - 5.56) / (15.16 - 5.56);
        frameNum = Math.min(180, Math.max(80, Math.floor(80 + prog * 100)));
        bgImg.style.transformOrigin = "50% 55%";
        bgImg.style.transform = "scale(1.08)";
      } else {
        // Beat 3 (15.16s - 24.5s): Macro zoom on upper mane & nostrils ventilation
        const prog = (timeSec - 15.16) / (24.5 - 15.16);
        frameNum = Math.min(220, Math.max(120, Math.floor(120 + prog * 60)));
        bgImg.style.transformOrigin = "35% 25%";
        bgImg.style.transform = "scale(1.85)";
      }
    }"""

html = html.replace(old_fn, new_fn)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated composition.html frame mapping logic: Beat 2 now smoothly opens and showcases cutaway soldiers (frames 80-180)!")
