"""Tanker cutout v5 — remove sky and water by flooding from the frame edges.

Sky and water are both connected regions that touch the border, so a
tolerance-based flood fill from each corner removes them cleanly and leaves
the ship untouched. This is deterministic and inspectable, unlike GrabCut.

Source: assets/tanker_solomon_solent.jpg (Wikimedia, CC BY-SA 4.0)
Run: py -3.13 cut_tanker4.py
"""

import os
import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "tanker_solomon_solent.jpg")
DST = os.path.join(HERE, "assets", "tanker_cutout.png")

# frame: include the mast array at the top, cut exactly at the waterline below
X0, Y0, X1, Y1 = 400, 498, 1680, 745
WATERLINE_Y = 718          # measured on the source photo


def flood_remove(img, seeds, lo_diff, up_diff):
    """Fill from seeds and return the visited region (background)."""
    mask = np.zeros((img.shape[0] + 2, img.shape[1] + 2), np.uint8)
    work = img.copy()
    lo = (lo_diff,) * 3
    up = (up_diff,) * 3
    for s in seeds:
        cv2.floodFill(work, mask, s, (0, 0, 0), lo, up,
                      cv2.FLOODFILL_MASK_ONLY | cv2.FLOODFILL_FIXED_RANGE | (255 << 8))
    return mask[1:-1, 1:-1]


def main():
    img = cv2.imread(SRC)
    assert img is not None, "source photo missing"
    crop = img[Y0:Y1, X0:X1].copy()
    h, w = crop.shape[:2]
    print("crop:", w, "x", h)

    # --- sky: flood from the top edge ---
    sky = flood_remove(crop, [(5, 2), (w - 6, 2), (w // 2, 2)], 30, 30)

    # --- water: flood from the bottom edge ---
    water = flood_remove(crop, [(5, h - 3), (w - 6, h - 3), (w // 2, h - 3)], 34, 34)

    bg = cv2.bitwise_or(sky, water)
    alpha = cv2.bitwise_not(bg)

    # hard cut at the waterline: nothing below the hull survives, so the wake
    # and reflected sea cannot be carried into the composition
    cut = WATERLINE_Y - Y0
    alpha[cut:, :] = 0

    # keep the widest remaining component (the ship)
    n, lab, stats, _ = cv2.connectedComponentsWithStats(alpha, 8)
    if n > 1:
        ship = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_WIDTH]))
        alpha = np.where(lab == ship, 255, 0).astype(np.uint8)

    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    alpha = cv2.morphologyEx(alpha, cv2.MORPH_CLOSE, k, iterations=2)
    alpha = cv2.GaussianBlur(alpha, (3, 3), 0.6)

    ys, xs = np.where(alpha > 128)
    if len(xs) == 0:
        raise SystemExit("empty alpha")
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    b, g, r = cv2.split(crop)
    rgba = cv2.merge([b, g, r, alpha])[y0:y1, x0:x1]
    cv2.imwrite(DST, rgba)

    keep = (alpha > 128).mean() * 100
    print(f"bbox x {x0}..{x1} y {y0}..{y1} -> {rgba.shape[1]}x{rgba.shape[0]}")
    print(f"kept {keep:.1f}%  alpha {alpha.min()}..{alpha.max()}")


if __name__ == "__main__":
    main()
