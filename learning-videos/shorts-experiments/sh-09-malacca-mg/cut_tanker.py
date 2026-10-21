"""Cut the tanker out of the real photo -> transparent PNG with a paper die-cut edge.

Source: assets/tanker_solomon_solent.jpg (Wikimedia Commons, CC BY-SA 4.0, ITookSomePhotos)
Crop coords measured from the full-res frame: ship spans x 408..1642 in the original,
hull meets water at y ~716 (crop 380,380 + 338).

Output: assets/tanker_cutout.png  (transparent, ship only, no water/sky/tug)

Run: py -3.13 cut_tanker.py
"""

import os
import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "tanker_solomon_solent.jpg")
DST = os.path.join(HERE, "assets", "tanker_cutout.png")

X0, Y0, X1, Y1 = 400, 380, 1680, 760
HULL_Y = 716 - Y0      # waterline, crop coords
TUG_X = 480 - X0       # right edge of the tug zone
DECK_Y = 500 - Y0      # above this and left of TUG_X is sky / mast / tug


def main():
    img = cv2.imread(SRC)
    assert img is not None, "source photo missing"
    crop = img[Y0:Y1, X0:X1].copy()
    h, w = crop.shape[:2]
    print("crop:", w, "x", h, "| hull_y:", HULL_Y, "| tug_x:", TUG_X)

    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    S = hsv[:, :, 1].astype(np.float32)
    V = hsv[:, :, 2].astype(np.float32)

    # ship pixels: very dark hull, or bright neutral superstructure
    seed = ((V < 95) | ((V > 165) & (S < 55))).astype(np.uint8) * 255

    mask = np.full((h, w), cv2.GC_PR_BGD, np.uint8)
    mask[seed > 0] = cv2.GC_PR_FGD
    mask[:int(h * 0.08), :] = cv2.GC_BGD
    bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(crop, mask, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
    alpha = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)

    # drop the tug, then the wake
    alpha[0:int(DECK_Y) + 90, 0:TUG_X] = 0
    alpha[int(HULL_Y) + 8:, :] = 0

    n, lab, stats, _ = cv2.connectedComponentsWithStats(alpha, 8)
    if n > 1:
        big = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
        alpha = np.where(lab == big, 255, 0).astype(np.uint8)

    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    alpha = cv2.morphologyEx(alpha, cv2.MORPH_CLOSE, k, iterations=2)
    alpha = cv2.morphologyEx(alpha, cv2.MORPH_OPEN, k, iterations=1)
    alpha = cv2.GaussianBlur(alpha, (3, 3), 0.7)

    b, g, r = cv2.split(crop)
    cv2.imwrite(DST, cv2.merge([b, g, r, alpha]))

    ys, xs = np.where(alpha > 128)
    print(f"bbox: x {xs.min()}..{xs.max()}  y {ys.min()}..{ys.max()}")
    print("kept:", f"{(alpha > 128).mean() * 100:.1f}%")


if __name__ == "__main__":
    main()
