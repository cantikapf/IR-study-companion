path = "D:/PERSONAL PROJECT/IR-study-companion/learning-videos/shorts-experiments/sh-11-dday-ghost-army/composition.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update plate-tank-outro size & position:
# Scale down slightly to 780px width, top: 180px
# Rendered height will be: (780 / 968) * 788 = 635px.
# Bottom edge of photo plate will be: 180 + 635 = 815px.
old_plate_css = """  /* Inflatable Tank Master Plate for Outro (Scene 5) - replaces buggy cutout */
  #plate-tank-outro {
    top: 220px;
    left: 110px;
    width: 860px;
    height: auto;
  }"""

new_plate_css = """  /* Inflatable Tank Master Plate for Outro (Scene 5) */
  #plate-tank-outro {
    top: 180px;
    left: 150px;
    width: 780px;
    height: auto;
  }"""

html = html.replace(old_plate_css, new_plate_css)

# 2. Update outro-payoff-card position:
# Move top down to 870px.
# Clearance will be: 870 - 815 = +55px clean breathing room!
old_card_css = """  /* Outro Hoax Payoff Card (Scene 5) */
  #outro-payoff-card {
    position: absolute;
    top: 890px;
    left: 100px;
    width: 880px;
    background: #0f172a;"""

new_card_css = """  /* Outro Hoax Payoff Card (Scene 5) */
  #outro-payoff-card {
    position: absolute;
    top: 870px;
    left: 110px;
    width: 860px;
    background: #0f172a;"""

html = html.replace(old_card_css, new_card_css)

# 3. Update GSAP timeline positions in Scene 5:
old_tl_plate = "tl.set('#plate-tank-outro', { display: 'block', top: '220px' }, 31.9);"
new_tl_plate = "tl.set('#plate-tank-outro', { display: 'block', top: '180px' }, 31.9);"
html = html.replace(old_tl_plate, new_tl_plate)

old_tl_card = "tl.set('#outro-payoff-card', { display: 'block', top: '890px' }, 33.2);"
new_tl_card = "tl.set('#outro-payoff-card', { display: 'block', top: '870px' }, 33.2);"
html = html.replace(old_tl_card, new_tl_card)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed layout: Plate top=180px (bottom=815px), Payoff card top=870px. Clearance: +55px")
