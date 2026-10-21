path = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update #precise-leaders CSS so it starts hidden:
old_css = """    .leader-container {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 35;
    }"""

new_css = """    .leader-container {
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 35;
      display: none;
      opacity: 0;
    }"""

html = html.replace(old_css, new_css)

# 2. In GSAP timeline:
# Beat 2: Animate #precise-leaders in at 6.2s, animate out at 14.8s, hide at 15.16s
old_beat2_tl = """  // Dimension Spec Card enters below at top: 210px
  tl.set('#card-dimension', { display: 'block', top: '210px' }, 6.2);
  tl.fromTo('#card-dimension', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.45, ease: 'power3.out' }, 6.2);

  // Clean Beat 2 Card
  tl.to('#card-dimension', { opacity: 0, y: -30, duration: 0.35, ease: 'power2.in' }, 14.8);
  tl.set('#card-dimension', { display: 'none' }, 15.16);"""

new_beat2_tl = """  // Precise Leader Lines enter in Beat 2 at 6.2s
  tl.set('#precise-leaders', { display: 'block' }, 6.2);
  tl.fromTo('#precise-leaders', { opacity: 0, scale: 0.96 }, { opacity: 1, scale: 1.0, duration: 0.45, ease: 'power3.out' }, 6.2);

  // Clean Beat 2 Leader Lines at 14.8s (CRITICAL: MUST DISAPPEAR COMPLETELY!)
  tl.to('#precise-leaders', { opacity: 0, duration: 0.35, ease: 'power2.in' }, 14.8);
  tl.set('#precise-leaders', { display: 'none' }, 15.16);"""

html = html.replace(old_beat2_tl, new_beat2_tl)

# 3. In Beat 3: Sleek unified thermal & vent callout instead of clunky stacked boxes
# Let's adjust #card-temp and #badge-vents spacing and styling
old_b3_css = """  /* Temperature & Suffocation Alert Card (Beat 3, positioned at top: 210px -> ZERO occlusion!) */
  #card-temp {
    position: absolute;
    top: 210px;
    left: 110px;
    width: 860px;
    background: #18090a;
    border: 3.5px solid #ef4444;
    border-radius: 18px;
    padding: 24px 32px;
    box-shadow: 14px 14px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }
  .temp-val {
    font-size: 38px;
    font-weight: 900;
    color: #ef4444;
  }

  /* Disguised Ventilation Badge (Beat 3, top: 410px) */
  #badge-vents {
    position: absolute;
    top: 410px;
    left: 140px;
    width: 800px;
    background: #0369a1;
    border: 3.5px solid #38bdf8;
    border-radius: 18px;
    padding: 20px 28px;
    text-align: center;
    box-shadow: 14px 14px 0px #000000;
    opacity: 0;
    display: none;
    z-index: 25;
  }"""

new_b3_css = """  /* Temperature & Suffocation Alert Card (Beat 3) - Sleek unified styling */
  #card-temp {
    position: absolute;
    top: 180px;
    left: 130px;
    width: 820px;
    background: rgba(24, 9, 10, 0.94);
    border: 3px solid #ef4444;
    border-radius: 16px;
    padding: 20px 28px;
    box-shadow: 0 16px 36px rgba(0,0,0,0.9);
    opacity: 0;
    display: none;
    z-index: 25;
  }
  .temp-val {
    font-size: 34px;
    font-weight: 900;
    color: #ef4444;
  }

  /* Disguised Ventilation Badge (Beat 3) - Sleek, separated cleanly */
  #badge-vents {
    position: absolute;
    top: 360px;
    left: 150px;
    width: 780px;
    background: rgba(3, 105, 161, 0.92);
    border: 2.5px solid #38bdf8;
    border-radius: 16px;
    padding: 16px 24px;
    text-align: center;
    box-shadow: 0 16px 36px rgba(0,0,0,0.9);
    opacity: 0;
    display: none;
    z-index: 25;
  }"""

html = html.replace(old_b3_css, new_b3_css)

# Also ensure in Beat 4 timeline that precise-leaders is 100% hidden
old_b4_tl = """  // In Beat 4: 3D Trapdoor & Ropes are the absolute hero! We keep the center unblocked!
  // Subtle compact tactical badge at top: 200px instead of opaque blocking plate
  tl.set('#plate-motte', { display: 'none' }, 25.84);"""

new_b4_tl = """  // In Beat 4: 3D Trapdoor & Ropes are the absolute hero! Center is 100% clean and unblocked!
  tl.set(['#plate-motte', '#precise-leaders', '#card-temp', '#badge-vents'], { display: 'none', opacity: 0 }, 25.84);"""

html = html.replace(old_b4_tl, new_b4_tl)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated composition.html: leader lines strictly vanish after Beat 2 (t=15.16s), Beat 4 center is 100% clear!")
