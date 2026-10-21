path = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/th-01-trojan-horse-3d-cutaway/composition.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Lower subtitle-box to bottom: 220px (frees up 200px of vertical space in the center!)
old_sub = """  #subtitle-box {
    position: absolute;
    bottom: 420px;
    left: 110px;
    right: 110px;"""

new_sub = """  #subtitle-box {
    position: absolute;
    bottom: 220px;
    left: 80px;
    right: 80px;"""

html = html.replace(old_sub, new_sub)

# 2. In Beat 4, remove the large opaque plate-motte so the 3D trapdoor and falling ropes are 100% visible!
# In CSS, hide plate-motte or disable display
old_beat4 = """  // Motte Master Archival Plate enters at top: 200px
  tl.set('#plate-motte', { display: 'block', top: '200px', scale: 0.95 }, 26.2);
  tl.fromTo('#plate-motte', { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.5, ease: 'back.out(1.4)' }, 26.2);

  // Clean Beat 4 Plate
  tl.to('#plate-motte', { opacity: 0, y: -60, duration: 0.35, ease: 'power2.in' }, 34.0);
  tl.set('#plate-motte', { display: 'none' }, 34.32);"""

new_beat4 = """  // In Beat 4: 3D Trapdoor & Ropes are the absolute hero! We keep the center unblocked!
  // Subtle compact tactical badge at top: 200px instead of opaque blocking plate
  tl.set('#plate-motte', { display: 'none' }, 25.84);"""

html = html.replace(old_beat4, new_beat4)

# 3. In Beat 5, adjust outro-payoff-card top position to 940px and channel badge to 1250px so it sits cleanly above the lowered subtitle
old_outro = """  // Outro Payoff Card enters below at top: 890px
  tl.set('#outro-payoff-card', { display: 'block', top: '890px' }, 35.8);
  tl.fromTo('#outro-payoff-card', { opacity: 0, scale: 0.85, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: 'back.out(1.8)' }, 35.8);

  // CTA Beat 6 (42.34s)
  tl.call(() => {
    sub.innerText = "Discover more untold ancient geopolitics on IR in a Nutshell.";
    hudTitle.innerText = "SUBSCRIBE // @IRinANutshell";
  }, null, 42.34);

  // Channel badge pop-in below payoff card at top: 1180px
  tl.set('#channel-badge', { display: 'block', top: '1180px' }, 42.5);"""

new_outro = """  // Outro Payoff Card enters at top: 860px
  tl.set('#outro-payoff-card', { display: 'block', top: '860px' }, 35.8);
  tl.fromTo('#outro-payoff-card', { opacity: 0, scale: 0.85, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: 'back.out(1.8)' }, 35.8);

  // CTA Beat 6 (42.34s)
  tl.call(() => {
    sub.innerText = "Discover more untold ancient geopolitics on IR in a Nutshell.";
    hudTitle.innerText = "SUBSCRIBE // @IRinANutshell";
  }, null, 42.34);

  // Channel badge pop-in below payoff card at top: 1160px
  tl.set('#channel-badge', { display: 'block', top: '1160px' }, 42.5);"""

html = html.replace(old_outro, new_outro)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Applied user feedback: Subtitle lowered to bottom: 220px, opaque card in Beat 4 removed to let 3D trapdoor shine!")
