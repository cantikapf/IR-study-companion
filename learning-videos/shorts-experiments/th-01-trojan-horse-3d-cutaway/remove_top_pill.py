path = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Hide #top-hud and .hud-pill completely as requested by user
old_css = """  /* Top Tactical Clean HUD */
  #top-hud {
    position: absolute;
    top: 95px;
    left: 60px;
    right: 60px;
    height: 64px;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 40;
  }"""

new_css = """  /* Top Tactical Clean HUD - REMOVED PER USER INSTRUCTION */
  #top-hud {
    display: none !important;
  }"""

html = html.replace(old_css, new_css)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully removed top pill badge header (#top-hud / .hud-pill) completely!")
