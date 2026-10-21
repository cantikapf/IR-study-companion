"""Tanker cutout v3 — luminance segmentation, no GrabCut.

GrabCut leaked sky into the deck and punched holes through the hull, so this
version segments on luminance and keeps only the widest connected component
(the hull silhouette). Sky, water and the tug are separate components and
drop out by construction.

Source: assets/tanker_solomon_solent.jpg (Wikimedia, CC BY-SA 4.0)
Run: py -3.13 cut_tanker2.py
"""

import os
import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "tanker_solomon_solent.jpg")
DST = os.path.join(HERE, "assets", "tanker_cutout.png")

X0, Y0, X1, Y1 = 400, 380, 1680, 740


def main():
    img = cv2.imread(SRC)
    assert img is not None, "source photo missing"
    crop = img[Y0:Y1, X0:X1].copy()
    h, w = crop.shape[:2]

    hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
    S = hsv[:, :, 1].astype(np.float32)
    V = hsv[:, :, 2].astype(np.float32)

    fg = ((V < 110) | ((V > 150) & (S < 70))).astype(np.uint8)

    fg[:int(h * 0.10), :] = 0
    fg[int(h * 0.92):, :] = 0

    fg = cv2.morphologyEx(fg, cv2.MORPH_CLOSE,
                          cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)), iterations=2)

    n, lab, stats, _ = cv2.connectedComponentsWithStats(fg, 8)
    if n <= 1:
        raise SystemExit("no components found")

    spans = stats[1:, cv2.CC_STAT_WIDTH]
    ship = 1 + int(np.argmax(spans))
    alpha = np.where(lab == ship, 255, 0).astype(np.uint8)
    print(f"components: {n - 1}, ship span {stats[ship, cv2.CC_STAT_WIDTH]}px, "
          f"area {stats[ship, cv2.CC_STAT_AREA]}px")

    flood = alpha.copy()
    ffmask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(flood, ffmask, (0, 0), 255)
    alpha = alpha | cv2.bitwise_not(flood)

    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    alpha = cv2.morphologyEx(alpha, cv2.MORPH_CLOSE, k, iterations=2)
    alpha = cv2.GaussianBlur(alpha, (3, 3), 0.6)

    ys, xs = np.where(alpha > 128)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    b, g, r = cv2.split(crop)
    rgba = cv2.merge([b, g, r, alpha])[y0:y1, x0:x1]
    cv2.imwrite(DST, rgba)

    print(f"bbox: x {x0}..{x1}  y {y0}..{y1} -> {rgba.shape[1]}x{rgba.shape[0]}")
    print("kept:", f"{(alpha > 128).mean() * 100:.1f}%")


if __name__ == "__main__":
    main()
