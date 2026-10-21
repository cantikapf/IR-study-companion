import re

path = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/composition.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update styling for #plate-tank in outro
# Replace #sticker-tank-cutout styling or adjust #plate-tank
old_css = """  /* Dummy Tank Cutout Sticker (Outro / Scene 5) */
  #sticker-tank-cutout {
    top: 250px;
    left: 140px;
    width: 800px;
    height: auto;
  }"""

new_css = """  /* Inflatable Tank Master Plate for Outro (Scene 5) - replaces buggy cutout */
  #plate-tank-outro {
    top: 220px;
    left: 110px;
    width: 860px;
    height: auto;
  }"""

html = html.replace(old_css, new_css)

# 2. Update HTML markup
old_markup = """    <img id="plate-rommel" class="sticker-prop" src="assets/plate_rommel_calais.png" alt="Field Marshal Erwin Rommel">
    <img id="sticker-tank-cutout" class="sticker-prop" src="assets/sticker_dummy_tank.png" alt="M4 Sherman Inflatable Cutout">"""

new_markup = """    <img id="plate-rommel" class="sticker-prop" src="assets/plate_rommel_calais.png" alt="Field Marshal Erwin Rommel">
    <img id="plate-tank-outro" class="sticker-prop" src="assets/plate_inflatable_tank.png" alt="Inflatable Dummy Tank Outro Plate">"""

html = html.replace(old_markup, new_markup)

# 3. Update GSAP timeline in Scene 5
old_timeline = """  // Sherman Inflatable Decoy Cutout Sticker enters center (top: 250px)
  tl.set('#sticker-tank-cutout', { display: 'block', top: '250px' }, 31.9);
  tl.fromTo('#sticker-tank-cutout', { opacity: 0, scale: 1.2, rotation: 8 }, { opacity: 1, scale: 1.0, rotation: 2, duration: 0.5, ease: 'back.out(1.5)' }, 31.9);"""

new_timeline = """  // Authentic Master Archival Plate of Inflatable Tank enters center (top: 220px)
  tl.set('#plate-tank-outro', { display: 'block', top: '220px' }, 31.9);
  tl.fromTo('#plate-tank-outro', { opacity: 0, scale: 0.85, y: 30, rotation: -2 }, { opacity: 1, scale: 1.0, y: 0, rotation: 1, duration: 0.5, ease: 'back.out(1.5)' }, 31.9);"""

html = html.replace(old_timeline, new_timeline)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully replaced buggy cutout with master archival plate in composition.html")
