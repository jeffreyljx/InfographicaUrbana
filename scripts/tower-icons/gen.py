"""Draw the map's tower icons: minimalist elevations of the tallest towers.

    python3 scripts/tower-icons/gen.py        # writes public/tower-icons/<id>.svg + index.json

Each tower is a function returning its height and a list of (tone, polygon) shapes, in metres:
x from the tower's axis (negative = left), y from the ground up. Tones:
  body  the whole silhouette (darkest)
  mid   a face turned partly to the light
  lit   the sunlit faces (light comes from the right)
  hi    small highlights, e.g. the Makkah clock face
Curves are sampled into polylines, so every shape is a plain polygon. All icons share one scale
(PX_PER_M), so their heights compare truthfully on the map. To add towers, write a function per
tower and append it to TOWERS with its CTBUH id (the id used across the site's data).
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "public", "tower-icons")
PX_PER_M = 0.15            # screen px per metre at icon-size 1: 828 m -> 124 px
HALO_PX = 1.5              # cream halo outside the silhouette, in px at icon-size 1
PAD = HALO_PX / PX_PER_M + 2.0   # metres of padding round the silhouette, room for the halo
TONES = dict(body="#2B1D17", mid="#4E3B33", lit="#7A655B", hi="#F4ECE9", halo="#FAF4F1")


def curve(f, y0, y1, n=24):
    """Sample the right edge x = f(y) from y0 to y1 (inclusive)."""
    return [(f(y0 + (y1 - y0) * i / n), y0 + (y1 - y0) * i / n) for i in range(n + 1)]


def smooth(knots):
    """Monotone cubic interpolation through (y, half-width) knots -> f(y)."""
    ys = [k[0] for k in knots]; hs = [k[1] for k in knots]
    n = len(ys)
    d = [(hs[i + 1] - hs[i]) / (ys[i + 1] - ys[i]) for i in range(n - 1)]
    m = [d[0]] + [0.0] * (n - 2) + [d[-1]]
    for i in range(1, n - 1):
        m[i] = 0.0 if d[i - 1] * d[i] <= 0 else 2 / (1 / d[i - 1] + 1 / d[i])

    def f(y):
        if y <= ys[0]: return hs[0]
        if y >= ys[-1]: return hs[-1]
        i = max(k for k in range(n - 1) if ys[k] <= y)
        h = ys[i + 1] - ys[i]; t = (y - ys[i]) / h
        return ((2*t**3 - 3*t**2 + 1) * hs[i] + (t**3 - 2*t**2 + t) * h * m[i]
                + (-2*t**3 + 3*t**2) * hs[i + 1] + (t**3 - t**2) * h * m[i + 1])
    return f


def steps(tiers, side=1):
    """Stepped edge from tiers [(y_from, half_width), ..., (y_top, None)]."""
    pts = []
    for (y0, hw), (y1, _) in zip(tiers, tiers[1:]):
        pts += [(side * hw, y0), (side * hw, y1)]
    return pts


def mirror(right):
    """Close a symmetric outline from its right half, listed bottom to top."""
    return right + [(-x, y) for x, y in reversed(right)]


def circle(cx, cy, r, n=40):
    return [(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n)) for i in range(n)]


# ---------------------------------------------------------------------------------------- towers

def burj_khalifa():
    H = 828.0
    # The Y-plan's wings step back in a spiral, so the two sides of the elevation step at
    # different heights; the core then runs on up into the steel spire.
    L = [(0, 50), (120, 45), (215, 39.5), (300, 34), (380, 28), (450, 22), (510, 16.5), (560, 11.5), (600, None)]
    R = [(0, 50), (75, 47), (165, 42), (255, 36.5), (340, 31), (415, 25), (480, 19), (535, 14), (580, 9.5), (600, None)]
    spire = [(8.0, 600), (6.5, 640), (5.0, 668), (3.6, 740), (2.2, H)]
    body = steps(R) + spire + [(-x, y) for x, y in reversed(spire)] + list(reversed(steps(L, -1)))
    lit = [(0, 0)] + steps(R) + [(0, 600)]            # the sunlit half of every wing tier
    return H, [("body", body), ("lit", lit)]


def merdeka_118():
    H = 678.9
    f = smooth([(0, 32), (150, 30.5), (300, 28.5), (420, 26)])
    crown = [(24.5, 450), (21, 480), (16.5, 510), (11.5, 540), (7, 566), (4.4, 578)]
    body = mirror(curve(f, 0, 420, 12) + crown + [(2.0, H)])
    # Faceted shaft: a crease zigzags right-left-right-left up the face and the facets to its
    # right catch the light; the crown's facets fold together into the spire.
    chevron = curve(f, 0, 280, 10) + [(-f(140), 140)]
    upper = curve(f, 280, 420, 10) + [(-f(420), 420)]
    crown_lit = [(0, 420), (f(420), 420)] + crown + [(0, 578)]
    return H, [("body", body), ("lit", chevron), ("lit", upper), ("mid", crown_lit)]


def shanghai_tower():
    H = 632.0
    # Tapering, twisting plan; the parapet rises to its peak on one side.
    lf = smooth([(0, 41), (200, 37), (420, 32), (632, 26)])
    rf = smooth([(0, 41), (200, 37), (420, 31.5), (560, 27.5), (600, 25.5)])
    right = curve(rf, 0, 600, 20)
    top = [(23.5, 612), (19, 621), (12, 627.5), (2, 631), (-8, 632), (-lf(632), H)]
    left = [(-x, y) for x, y in reversed(curve(lf, 0, 632, 20))]
    body = right + top + left[1:]
    # The notch spirals up the tower: in elevation a curve from lower right to upper left,
    # with the sunlit face to its right.
    notch = [(26 - 40 * t + 6 * math.sin(math.pi * t), 625 * t) for t in (i / 20 for i in range(21))]
    lit = [(26, 0), (41, 0)] + right[1:] + top[:4] + list(reversed(notch[1:-1]))
    return H, [("body", body), ("lit", lit)]


def makkah_clock_tower():
    H = 601.0
    right = [
        (60, 0), (60, 48), (31, 48),                     # podium shoulder
        (31, 262), (27, 262), (27, 380),                 # shaft and its setback
        (29.5, 380), (29.5, 398),                        # cornice under the clock
        (25.5, 398), (25.5, 455),                        # clock block
        (28, 455), (28, 467),                            # balcony
        (19, 467), (17, 495), (12.5, 517), (7, 530),     # crown
        (3.0, 532), (1.8, 584),                          # spire
    ]
    r, cy = 8.5, 592.5                                   # crescent finial, horns up
    crescent = ([(r * math.cos(a), cy + r * math.sin(a)) for a in (math.pi * (1 + i / 24) for i in range(25))]
                + [(0.78 * r * math.cos(a), cy + 3.4 + 0.72 * r * math.sin(a)) for a in (math.pi * (2 - i / 24) for i in range(25))])
    lit_podium = [(31, 0), (60, 0), (60, 48), (31, 48)]
    lit_shaft = [(0, 48), (31, 48), (31, 262), (27, 262), (27, 380), (29.5, 380), (29.5, 398), (0, 398)]
    lit_crown = [(0, 455), (28, 455), (28, 467), (19, 467), (17, 495), (12.5, 517), (7, 530), (0, 530)]
    return H, [("body", mirror(right)), ("body", crescent), ("lit", lit_podium), ("lit", lit_shaft),
               ("lit", lit_crown), ("hi", circle(0, 426.5, 20.5))]


def ping_an():
    H = 599.1
    f = smooth([(0, 35), (35, 31.5), (300, 27.5), (540, 23)])
    crown = [(19, 556), (12, 572), (6.5, 584), (3.0, 592), (1.4, H)]
    body = mirror(curve(f, 0, 540, 16) + crown)
    # The face between the corner ribs is lit (its right half); the chamfered corners stay dark,
    # so the ribs read as lines converging on the pointed crown.
    face = curve(lambda y: 0.58 * f(y), 0, 540, 16)
    lit = [(0, 0)] + face + [(11.5, 556), (6.0, 572), (2.4, 586), (0, 588)]
    return H, [("body", body), ("lit", lit)]


def lotte_world_tower():
    H = 554.5
    f = smooth([(0, 43), (150, 39), (300, 31), (430, 21.5), (500, 14.5), (540, 10.5)])
    shaft = curve(f, 0, 540, 24)
    # a smooth convex taper; the seam up the middle splits open at the lantern on top
    body = shaft + [(9.2, H), (2.2, H), (0, 539), (-2.2, H), (-9.2, H)] + [(-x, y) for x, y in reversed(shaft)]
    lit = [(0, 0)] + shaft + [(9.2, H), (2.2, H), (0, 539)]
    return H, [("body", body), ("lit", lit)]


def one_wtc():
    H = 541.3
    # Seen across the diagonal: the 61 m cube base, the chamfered shaft tapering to the rotated
    # square roof, then the mast.
    right = [(43, 0), (43, 57), (22.6, 413), (22.6, 417), (7.5, 417), (7.5, 428), (2.6, 428),
             (2.6, 470), (4.2, 470), (4.2, 476), (2.2, 476), (1.4, H)]
    front = [(0, 57), (22.6, 413), (-22.6, 413)]      # the corner chamfer facing us
    east = [(0, 57), (43, 57), (22.6, 413)]           # the sunlit face
    cube = [(0, 0), (43, 0), (43, 57), (0, 57)]
    return H, [("body", mirror(right)), ("mid", front), ("lit", east), ("lit", cube)]


def guangzhou_ctf():
    H = 530.0
    tiers = [(0, 33), (150, 31.5), (300, 30), (415, 28), (470, None)]
    crown = [(24.5, 470), (24.5, 490), (20, 494), (14, 506), (8.5, 516), (3.2, 521), (2.0, H)]
    body = mirror(steps(tiers) + crown)
    # vertical corner piers stay dark; the main face is lit
    face = [(x - 7.5, y) for x, y in steps(tiers)]
    lit = [(0, 0)] + face + [(17, 470), (17, 490), (13, 502), (8, 512), (3.0, 518), (0, 518)]
    return H, [("body", body), ("lit", lit)]


def tianjin_ctf():
    H = 530.0
    # soft, undulating curves; the roof rounds off
    f = smooth([(0, 31), (60, 33), (150, 31.5), (260, 28.5), (360, 25.5), (440, 21.5), (500, 16.5), (522, 13)])
    shaft = curve(f, 0, 522, 30)
    dome = [(13 * math.cos(a), 522 + 8 * math.sin(a)) for a in (math.pi * i / 16 for i in range(1, 16))]
    body = shaft + dome + [(-x, y) for x, y in reversed(shaft)]
    # a flowing seam, with the face to its right lit
    seam = [(0.35 * f(y) * math.sin(math.pi * y / 522 * 1.3), y) for y in (522 * i / 30 for i in range(31))]
    lit = [(seam[0][0], 0)] + shaft + [d for d in dome if d[0] > seam[-1][0]] + list(reversed(seam[1:]))
    return H, [("body", body), ("lit", lit)]


def citic_tower():
    H = 527.7
    # the "zun" ritual vessel: wide base, slim waist, flaring top
    f = smooth([(0, 39), (110, 34), (250, 29), (350, 27.5), (440, 30), (505, 34.2), (520, 35), (527.7, 35)])
    shaft = curve(f, 0, H, 30)
    body = shaft + [(-x, y) for x, y in reversed(shaft)]
    lit = [(0, 0)] + curve(lambda y: 0.55 * f(y), 0, 512, 30) + [(0, 512)]
    band = [(-f(512), 512), (f(512), 512), (f(H), H), (-f(H), H)]
    return H, [("body", body), ("lit", lit), ("lit", band)]


# CTBUH id, name, drawing; the world's tallest completed buildings, tallest first
TOWERS = [
    (3, "Burj Khalifa", burj_khalifa),
    (10115, "Menara Merdeka Maybank (Merdeka 118)", merdeka_118),
    (56, "Shanghai Tower", shanghai_tower),
    (84, "Makkah Royal Clock Tower", makkah_clock_tower),
    (54, "Ping An Finance Center", ping_an),
    (88, "Lotte World Tower", lotte_world_tower),
    (98, "One World Trade Center", one_wtc),
    (176, "Guangzhou CTF Finance Centre", guangzhou_ctf),
    (310, "Tianjin CTF Finance Centre", tianjin_ctf),
    (11116, "CITIC Tower", citic_tower),
]


# ---------------------------------------------------------------------------------------- output

def svg_for(height, shapes):
    xs = [x for _, pts in shapes for x, _ in pts]
    hw = max(-min(xs), max(xs))
    W, Hh = 2 * (hw + PAD), height + 2 * PAD

    def d(pts):
        return "M" + "L".join(f"{x + hw + PAD:.0f},{Hh - PAD - y:.0f}" for x, y in pts) + "Z"
    halo = "".join(f'<path d="{d(p)}"/>' for t, p in shapes if t == "body")
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {Hh:.1f}" width="{W * PX_PER_M:.2f}" height="{Hh * PX_PER_M:.2f}">',
           f'<g fill="{TONES["halo"]}" stroke="{TONES["halo"]}" stroke-width="{2 * HALO_PX / PX_PER_M:.1f}" stroke-linejoin="round" opacity="0.92">{halo}</g>']
    out += [f'<path d="{d(p)}" fill="{TONES[t]}"/>' for t, p in shapes]
    out.append("</svg>\n")
    return "\n".join(out), W, Hh


def main():
    os.makedirs(OUT, exist_ok=True)
    icons = []
    for tid, name, draw in TOWERS:
        height, shapes = draw()
        svg, W, Hh = svg_for(height, shapes)
        with open(os.path.join(OUT, f"{tid}.svg"), "w") as fh:
            fh.write(svg)
        icons.append({"id": tid, "name": name, "height": height,
                      "w": round(W * PX_PER_M, 2), "h": round(Hh * PX_PER_M, 2), "base": round(PAD * PX_PER_M, 2)})
    with open(os.path.join(OUT, "index.json"), "w") as fh:
        json.dump({"pxPerMetre": PX_PER_M, "icons": icons}, fh, indent=1)
        fh.write("\n")
    print(f"{len(icons)} icons -> {os.path.relpath(OUT)}")


if __name__ == "__main__":
    main()
