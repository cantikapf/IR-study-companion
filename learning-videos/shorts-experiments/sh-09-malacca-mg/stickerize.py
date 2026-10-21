"""Give the tanker cutout the paper-sticker treatment used across SH-09:
a cream die-cut edge (outside stroke) + soft contact shadow rendered into the PNG.

The composition then only has to place the file; it does not re-draw the effect,
so the photos and the SVG landmasses share one visual grammar.

Run: py -3.13 stickerize.py
"""

import os
import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "tanker_cutout.png")
DST = os.path.join(HERE, "assets", "tanker_sticker.png")

CREAM = (234, 241, 244)     # BGR of #F4F1EA
EDGE = 7                    # die-cut stroke, px
SHADOW_OFF = (10, 14)       # dx, dy
SHADOW_BLUR = 18
SHADOW_OP = 0.30


def main():
    img = cv2.imread(SRC, cv2.IMREAD_UNCHANGED)
    assert img is not None and img.shape[2] == 4, "need RGBA cutout"
    bgra = img
    b, g, r, a = cv2.split(bgra)

    alpha = a.copy()
    # straighten the waterline edge: a hull sits flat on the sea, so the
    # cutout's bottom must be a clean horizontal line, not a wobbly mask edge
    ys, xs = np.where(alpha > 128)
    bottom = ys.max()
    alpha[bottom - 2:, :] = np.where(alpha[bottom - 2:, :] > 128, 255, 0)
    alpha[bottom:, :] = 0
    alpha[bottom - 1, :] = np.where(alpha[bottom - 1, :] > 128, 255, 0)

    # grow the silhouette outward = the die-cut edge
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (EDGE * 2 + 1, EDGE * 2 + 1))
    grown = cv2.dilate(alpha, k, iterations=1)
    grown = cv2.GaussianBlur(grown, (3, 3), 0.6)

    pad = EDGE + max(SHADOW_OFF) + SHADOW_BLUR
    H, W = alpha.shape
    canvas = np.zeros((H + pad * 2, W + pad * 2, 4), np.uint8)

    # --- shadow layer: silhouette offset, blurred, tinted black ---
    sh = np.zeros_like(canvas[:, :, 3])
    sh[pad + SHADOW_OFF[1]:pad + SHADOW_OFF[1] + H,
       pad + SHADOW_OFF[0]:pad + SHADOW_OFF[0] + W] = grown
    sh = cv2.GaussianBlur(sh, (SHADOW_BLUR * 2 + 1, SHADOW_BLUR * 2 + 1), 0)
    canvas[:, :, 0:3] = 0
    canvas[:, :, 3] = (sh.astype(np.float32) * SHADOW_OP).astype(np.uint8)

    # --- cream edge ---
    edge_layer = np.zeros_like(canvas)
    edge_layer[pad:pad + H, pad:pad + W, 0] = CREAM[0]
    edge_layer[pad:pad + H, pad:pad + W, 1] = CREAM[1]
    edge_layer[pad:pad + H, pad:pad + W, 2] = CREAM[2]
    edge_layer[pad:pad + H, pad:pad + W, 3] = grown

    # composite edge over shadow, then the photo over the edge
    def over(dst, src):
        sa = src[:, :, 3:4].astype(np.float32) / 255.0
        da = dst[:, :, 3:4].astype(np.float32) / 255.0
        out_a = sa + da * (1 - sa)
        rgb = (src[:, :, 0:3].astype(np.float32) * sa +
               dst[:, :, 0:3].astype(np.float32) * da * (1 - sa))
        rgb = np.where(out_a > 1e-6, rgb / np.maximum(out_a, 1e-6), 0)
        out = np.dstack([rgb, out_a * 255]).astype(np.uint8)
        return out

    comp = over(canvas, edge_layer)

    photo = np.zeros_like(canvas)
    photo[pad:pad + H, pad:pad + W] = bgra
    comp = over(comp, photo)

    cv2.imwrite(DST, comp)
    print(f"wrote {DST}  {comp.shape[1]}x{comp.shape[0]}")


if __name__ == "__main__":
    main()
