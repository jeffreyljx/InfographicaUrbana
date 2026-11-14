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


def taipei_101():
    H = 508.0
    # The bamboo stalk / pagoda: a tapering base up to floor 26, then eight stacked eight-floor
    # modules that each flare outward (so the edge zigzags in at every joint), a narrower crown
    # of smaller tiers above the 91st-floor deck, and the 60 m pinnacle.
    y_base, mod_h, n_mod = 119.0, 34.0, 8
    w0, w1 = 22.5, 26.5                                  # module half-width at its foot and lip
    right = [(29.0, 0), (w0, y_base)]                    # base frustum, narrowing upward
    for i in range(n_mod):
        y0 = y_base + i * mod_h
        right += [(w0, y0), (w1, y0 + mod_h)]
    top = y_base + n_mod * mod_h                         # 391 m: outdoor deck
    crown = [(13.5, top), (13.5, top + 4), (14.5, top + 4), (17, top + 32),   # flared mini-module
             (11, top + 32), (11, top + 46),                            # floors 100-101
             (7.5, top + 46), (5.5, 449.2),                             # pinnacle base
             (3.0, 449.2), (3.0, 462), (4.0, 462), (4.0, 466),          # spire and its ring
             (2.2, 466), (0.8, H)]
    body = mirror(right + crown)
    # The sunlit right half of each segment, cut apart at the joints so the stack reads.
    shapes = [("body", body), ("lit", [(0, 0), (29.0, 0), (w0, y_base), (0, y_base)])]
    for i in range(n_mod):
        y0 = y_base + i * mod_h
        shapes.append(("lit", [(0, y0 + 3), (w0 + 0.35, y0 + 3), (w1, y0 + mod_h), (0, y0 + mod_h)]))
    shapes.append(("lit", [(0, top + 4), (14.5, top + 4), (17, top + 32), (0, top + 32)]))
    shapes.append(("lit", [(0, top + 34), (11, top + 34), (11, top + 46), (7.5, top + 46), (5.5, 449.2), (0, 449.2)]))
    return H, shapes


def swfc_shanghai():
    H = 492.0
    # Seen through the aperture, across the diagonal of the 58 m square plan: the two vertical
    # corners give straight sides 82 m apart. Two cosmic arcs cut away the near and far corners,
    # narrowing the plan to a single diagonal line at the roof, so the curved front face (mid)
    # opens upward from a point at the base between the two side faces, the right one sunlit.
    # The trapezoidal "bottle opener" aperture under the roof bridge shows the sky.
    W = 41.0                       # half the plan diagonal

    def crease(y):                 # where the arc surface meets the side faces: the arcs
        t = y / H                  # fall in slowly near the base, faster toward the roof
        return 36.0 * (0.25 * t + 0.75 * t * t)

    body = [(W, 0), (W, H), (-W, H), (-W, 0)]
    edge = curve(crease, 0, H, 24)                    # (0, 0) ... (36, 492)
    lit = [(W, 0), (W, H)] + list(reversed(edge))
    front = edge + [(-x, y) for x, y in reversed(edge)]
    aperture = [(-14.5, 440), (14.5, 440), (24.5, 473), (-24.5, 473)]
    return H, [("body", body), ("mid", front), ("lit", lit), ("hi", aperture)]


def icc_hk():
    H = 484.0
    # Face-on elevation of the square tower: its sides taper gently as they rise, and at the foot
    # the facade curves out into the skirts over the entrances. The re-entrant (notched) corners
    # run the full height as dark strips beside the sunlit face; over the hotel floors the walls
    # rake inward, faster near the top, to the blunt, flat-topped crown.
    f = smooth([(0, 38.5), (10, 35), (28, 32.8), (55, 32.2), (250, 30.3), (400, 28.0),
                (430, 26.6), (455, 24.0), (472, 20.8), (H, 17.0)])
    edge = curve(f, 0, H, 40)
    body = mirror(edge)
    # the main face between the notched corners, its sunlit right half; above 425 m the raked
    # crown panels turn partly away from the light
    n = 6.0
    yc = 425.0
    lit = [(0, 0)] + [(x - n, y) for x, y in curve(f, 0, yc, 34)] + [(0, yc)]
    crown = [(0, yc)] + [(x - n, y) for x, y in curve(f, yc, H - 1.0, 8)] + [(0, H - 1.0)]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def wuhan_greenland():
    H = 475.6
    # A tri-lobed plan of three rounded wings, seen with one wing pointing at us: the smooth,
    # gently tapering shaft (cut down from its 636 m design) rounds over into a blunt domed crown.
    # The recessed slots between the front wing and the side wings run up the shaft and converge
    # on the dome; the right side wing catches the light, the front wing's right half is half lit.
    f = smooth([(0, 33), (150, 31.5), (280, 29), (370, 26.5), (412, 24.2), (440, 20.5),
                (458, 15), (469, 9), (474, 4.5), (H, 1.5)])
    right = curve(f, 0, H, 48)
    body = mirror(right)
    k, gap = 0.44, 2.2                                   # slot position (share of half-width), half its width
    ys = [p[1] for p in right]
    slot_r = [(k * f(y) + gap * f(y) / 33, y) for y in ys]   # right edge of the slot
    slot_l = [(k * f(y) - gap * f(y) / 33, y) for y in ys]   # left edge of the slot
    lit = slot_r + list(reversed(right))
    mid = [(0, 0)] + slot_l + [(0, H)]
    return H, [("body", body), ("lit", lit), ("mid", mid)]


def central_park_tower():
    H = 472.4
    # Seen from 57th Street (south), east on the right: a flat-topped glass slab about 50 m wide.
    # From 88 m up, its eastern bay cantilevers 8.5 m out over the Art Students League, leaving
    # a slot under it at the foot of the right side; that bay sits back from the main face (mid).
    # The top floors step in at the west corner for penthouse terraces, louvred mechanical
    # floors band the sunlit face, the crown is a dark slatted screen, and its parapet rises
    # highest at the east end, where the dropped spire was to stand.
    cant, roof, crown = 88.0, 462.0, 436.0
    body = [(16.5, 0), (16.5, cant), (25, cant), (25, H), (11, H), (11, roof),
            (-19, roof), (-19, 418), (-25, 418), (-25, 0)]
    bay = [(16.5, cant), (25, cant), (25, H), (16.5, H)]
    lit = [(-3, 0), (16.5, 0), (16.5, crown), (-3, crown)]
    bands = [(170, 175), (288, 294), (392, 400)]
    shapes = [("body", body), ("mid", bay), ("lit", lit)]
    shapes += [("mid", [(-3, y0), (16.5, y0), (16.5, y1), (-3, y1)]) for y0, y1 in bands]
    return H, shapes


def lakhta_center():
    H = 462.0
    # A five-pointed (pentagonal) plan that twists as it rises and tapers like a flame, the
    # glazed blades running on past the top floors (360 m) into the needle tip. Two petal edges
    # spiral up the face: the petal right of them is sunlit, the one between them faces us (mid).
    f = smooth([(0, 30), (100, 29), (200, 26.3), (280, 22), (330, 17.5), (370, 12.5),
                (400, 8.2), (425, 4.8), (445, 2.4), (462, 0.4)])
    shaft = curve(f, 0, H, 40)
    body = shaft + [(-x, y) for x, y in reversed(shaft)]

    def seam(a0, a1, y1, n=30):
        # a petal edge whose plan angle (degrees from facing us) turns from a0 at the ground to a1 at H
        pts = []
        for i in range(n + 1):
            y = y1 * i / n
            a = math.radians(max(-90.0, min(90.0, a0 + (a1 - a0) * y / H)))
            pts.append((f(y) * math.sin(a), y))
        return pts

    top = 440
    a = seam(-9, 40, top)                                 # right of it: the sunlit petal
    b = seam(-37, 2, top)                                 # left of it: petals in shadow
    lit = a + list(reversed(curve(f, 0, top, 30)))
    mid = b + list(reversed(a))
    return H, [("body", body), ("mid", mid), ("lit", lit)]


def landmark_81():
    H = 461.2
    # The bamboo bundle: a straight square shaft of clustered tubes whose outer sticks stop at
    # staggered heights, so the top steps in, unevenly on each side, toward the tallest central
    # tube; above the top floors the sticks run on as an open-framed crown to 461 m.
    R = [(0, 27.5), (300, 21.5), (332, 16.0), (354, 10.5), (384, 6.5), (H, None)]
    L = [(0, 27.5), (282, 22.0), (318, 15.5), (340, 11.0), (370, 6.5), (434, None)]
    body = steps(R) + [(-1.5, H), (-1.5, 434)] + list(reversed(steps(L, -1)))
    # the sunlit right half of every tube tier; the open crown frame catches less light
    lit = [(0, 0)] + steps(R)[:-1] + [(6.5, 392), (0, 392)]
    crown = [(-1.5, 392), (6.5, 392), (6.5, H), (-1.5, H)]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def exchange_106():
    H = 453.6
    # Seen square-on: a square plan with notched corners whose faces lean in steadily all the way
    # up; above the top floors the glass faces fold together into a tall pointed, crystal-like
    # crown. The notched corners stay dark, so the sunlit face reads as a tapering panel that
    # runs on up into the apex.
    def hw(y):
        return 28.0 - 5.0 * y / 395
    crown = [(21.0, 408), (17.0, 424), (10.5, 438), (4.2, 449), (1.2, H)]
    body = mirror([(hw(0), 0), (hw(395), 395)] + crown)
    n = 6.5                                               # width of the dark notched corner
    lit = [(0, 0), (hw(0) - n, 0), (hw(395) - n, 395), (15.0, 408), (11.6, 424), (6.4, 438), (0, 450)]
    return H, [("body", body), ("lit", lit)]


def changsha_ifs_t1():
    H = 452.1
    # A square glass shaft that tapers gently from its 62 m base; over the hotel floors at the
    # top its faces curve inward in an arched taper to a narrow flat crown. The recessed corner
    # strips stay dark, the main face is lit, and the curving crown face, turned partly up to
    # the sky, is a half tone.
    y_sh = 372.0                                          # the arched taper begins
    f = smooth([(0, 31), (150, 30), (280, 28.8), (y_sh, 27.6)])
    g = smooth([(y_sh, 27.6), (400, 26.4), (425, 23.6), (442, 20.0), (H, 16.5)])
    shaft = curve(f, 0, y_sh, 14)
    crown = curve(g, y_sh, H, 14)[1:]
    body = mirror(shaft + crown)
    inset = 6.0                                           # dark corner strip

    def k(y):                                             # crown strip narrows with the crown
        return inset * g(y) / 27.6
    lit = [(0, 0)] + curve(lambda y: f(y) - inset, 0, y_sh, 14) + [(0, y_sh)]
    crown_face = [(0, y_sh + 3)] + curve(lambda y: g(y) - k(y), y_sh + 3, H - 3, 12) + [(0, H - 3)]
    return H, [("body", body), ("lit", lit), ("mid", crown_face)]


def petronas_tower_1():
    H = 451.9
    # A fluted shaft on the eight-pointed-star plan (about 52 m across) rises to floor 60, then
    # telescopes in five setbacks (floors 60, 73, 82, 85, 88), each eased in with a sloped skirt.
    # On top the pinnacle: the stacked rings of the "ring ball", the mast with its ball, then the
    # needle. A star point faces us: its two facets meet on the axis (half-lit left, lit right),
    # and the outer facets catch the light in a second band beyond a dark notch.
    tiers = [(0, 26.0), (254, 23.5), (313, 20.5), (352, 17.0), (366, 13.5), (379, None)]
    SK = 6.0                                            # height of each sloped setback skirt

    def edge(frac):
        pts = []
        for (y0, hw), (y1, nxt) in zip(tiers, tiers[1:]):
            pts += [(frac * hw, y0), (frac * hw, y1 - SK if nxt else y1)]
        return pts
    rings = [(9.5, 379), (9.0, 383), (7.8, 383), (7.3, 387), (6.2, 387), (5.6, 391),
             (4.5, 391), (3.9, 395), (2.9, 395), (2.6, 399)]
    mast = [(2.2, 399), (2.2, 410)]
    ball = [(3.6 * math.sin(a), 413.4 - 3.6 * math.cos(a)) for a in (math.pi * i / 8 for i in range(1, 8))]
    needle = [(1.8, 417), (1.2, H)]
    body = mirror(edge(1.0) + rings + mast + ball + needle)

    def band(f0, f1):
        return edge(f1) + list(reversed(edge(f0)))
    front_l = band(-0.42, 0.0)                          # the point's left facet, half turned to the light
    front_r = band(0.0, 0.42)                           # its right facet, lit
    outer = band(0.62, 1.0)                             # the outer facets, lit
    ring_lit = [(0, 379)] + rings + [(0, 399)]
    return H, [("body", body), ("mid", front_l), ("lit", front_r), ("lit", outer), ("mid", ring_lit)]


def zifeng_tower():
    H = 450.0
    # Seen toward a corner of the triangular plan: the two faces meet on the axis, the right one
    # sunlit. The faces step back at different heights as the programme changes (offices, hotel,
    # observatory), so the shaft narrows in a spiral of setbacks; above the top floor (316 m) the
    # glass faces fold into a sharp faceted crown and the spire runs on to 450 m.
    R = [(0, 31), (115, 27), (235, 22.5), (318, None)]
    L = [(0, 31), (175, 25.5), (318, None)]
    crown_r = [(22.5, 318), (15, 350), (7.5, 376), (3.0, 392)]
    crown_l = [(-25.5, 318), (-17, 348), (-8.5, 375), (-3.0, 392)]
    spire = [(2.2, 420), (1.2, H)]
    body = (steps(R) + crown_r + spire + [(-x, y) for x, y in reversed(spire)]
            + list(reversed(crown_l)) + list(reversed(steps(L, -1))))
    lit = [(0, 0)] + steps(R) + crown_r + [(0, 392)]
    return H, [("body", body), ("lit", lit)]


def suzhou_ifs():
    H = 450.0
    # Seen from the south, with Jinji Lake to the left (west): the "fish" tower. Its tail flares
    # out at the foot on the lake side, the slender body rises with a slight waist, and the top
    # is cut by a steep scooped roof that falls toward the lake, the dish that "welcomes the
    # water", rising from the lip over the top floor (399 m) to a rounded peak on the east side.
    rf = smooth([(0, 30), (150, 29.5), (300, 28), (400, 25.5), (432, 23)])
    lf = smooth([(0, 46), (30, 38), (90, 31), (200, 29.5), (330, 29.5), (402, 32)])
    right = curve(rf, 0, 432, 24)
    peak = [(21.5, 440), (19, 446), (15.5, 449.2), (12, H)]

    def roof(t):                       # t = 0 at the peak, 1 at the lip: a sagging, dish-like line
        return (12 - 44 * t, H - 48 * (1 - (1 - t) ** 1.8))
    lip = [roof(i / 16) for i in range(17)]
    left = [(-x, y) for x, y in reversed(curve(lf, 0, 402, 24))]
    body = right + peak + lip[1:] + left
    # sunlit east half of the shaft, its edge drifting as the tower gently twists back to the lake
    seam = [(4 - 6 * math.sin(math.pi * y / 430 * 0.9), y) for y in (430 * i / 20 for i in range(21))]
    top = [p for p in lip if p[0] > seam[-1][0]]
    lit = [(seam[0][0], 0)] + right + peak + top + list(reversed(seam[1:]))
    # the scooped face of the crown, turned up to the sky: a crescent under the roof line
    under = [(x + 2 * math.sin(math.pi * i / 16), y - 11 * math.sin(math.pi * i / 16) ** 0.8)
             for i, (x, y) in enumerate(lip)]
    dish = lip + list(reversed(under[1:-1]))
    return H, [("body", body), ("lit", lit), ("mid", dish)]


def wuhan_tower():
    H = 443.1
    # Wuhan Center, "inspired by a sailing vessel": a square-plan glass shaft that tapers gently
    # (its corners chamfer and step in from floor 64 up) to the roof at 394 m, then a tulip-bud
    # crown. Each face is a petal: the slotted corners run up between them and open into notches
    # where the side petals curl in beside the taller front petal that closes to the tip. The face
    # and the front petal's right half are lit; the right side petal is turned partly to the light.
    f = smooth([(0, 30.5), (110, 30.3), (230, 29.3), (320, 27.6), (394, 25.2)])
    shaft = curve(f, 0, 394, 18)
    side = [(25.8, 402), (25.6, 410), (24.6, 418), (22.6, 425.5), (19.4, 432), (15.6, 436.8)]
    notch = (9.6, 421.5)
    front = [(8.2, 428), (6.0, 434), (3.4, 439), (1.4, 442), (0, H)]
    body = mirror(shaft + side + [notch] + front)
    slot = 6.5
    face = curve(lambda y: f(y) - slot, 0, 394, 18)
    petal = [(19.0, 400), (17.0, 409), (13.6, 417), (9.8, 425.5), (7.6, 431), (5.0, 436.5),
             (2.4, 440.2), (0, 441.8)]
    lit = [(0, 0)] + face + petal
    seam = [(x + 2.6, y) for x, y in petal[:4]]               # the corner slot running up the crown
    curl = [(f(394) - slot + 2.6, 394), (f(394), 394)] + side + [(notch[0] + 1.0, notch[1] + 0.5)] + list(reversed(seam[1:]))
    return H, [("body", body), ("lit", lit), ("mid", curl)]


def willis_tower():
    H = 442.1
    # Seen across the diagonal from the south-east (the lakefront view): nine 22.9 m square tubes
    # bundled 3 x 3. The south-east corner tube stops at floor 50, opening a slot down the front
    # corner; the north-east and south-west tubes stop at 66, so both shoulders step in; the cross
    # of five stops at 90 and the west and centre tubes run on to the roof. East faces are lit.
    d = 22.86 / math.sqrt(2)                          # half a tube's diagonal: 16.2 m
    h50, h66, h90 = 203.0, 268.0, 365.0      # roofs of floors 50, 66 and 90
    right = [(3 * d, 0), (3 * d, h66), (2 * d, h66), (2 * d, h90), (d, h90), (d, H)]
    left = [(-2 * d, H), (-2 * d, h66), (-3 * d, h66), (-3 * d, 0)]
    body = right + left
    east = [(0, 0), (3 * d, 0), (3 * d, h66), (2 * d, h66), (2 * d, h90), (d, h90), (d, h50), (0, h50)]
    slot = [(-d, h50), (0, h50), (0, h90), (-d, h90)]  # east face of the south-centre tube
    top = [(0, h90), (d, h90), (d, H), (0, H)]          # east face of the centre tube
    return H, [("body", body), ("lit", east), ("lit", slot), ("lit", top)]


def kk100():
    H = 441.8
    # The broad south face: a slim slab whose gently curved sides swell a little in the lower
    # half and draw in towards the top, then round over into the parabolic arch of the glass
    # crown (the "fountain") that holds the sky garden. The right half of the face is lit; the
    # glazed arch over the sky garden shows as a lighter cap inside the crown's rim.
    y0 = 395.0
    f = smooth([(0, 25), (130, 26.8), (260, 26), (340, 24.3), (y0, 22.0)])
    w = f(y0)

    def arch(inset, top, n=16):
        # rounded parabolic arch from the springing line y0 up to its apex at `top`
        r = w - inset
        return [(r * (1 - s ** 1.6) ** 0.5, y0 + (top - y0) * s) for s in (i / n for i in range(n + 1))]

    def closed(right_half):
        # right half (bottom to apex on the axis) -> whole outline
        return right_half + [(-x, y) for x, y in reversed(right_half[:-1])]

    shaft = curve(f, 0, y0, 20)
    body = closed(shaft + arch(0, H)[1:])
    lit = [(0, 0)] + shaft + [(0, y0)]
    glass = arch(4.0, H - 4.5)
    crown = closed(glass)
    crown_lit = [(0, y0)] + glass
    return H, [("body", body), ("lit", lit), ("mid", crown), ("lit", crown_lit)]


def guangzhou_ifc():
    H = 438.6
    # The smooth glass spindle on its rounded-triangle plan: the faces swell to their widest
    # around level 31 and draw in to the flat roof. The diagrid's diagonals cross in nodes
    # every 12 floors (about 54 m): a chain of diamonds up the face, the sunlit side to the right.
    f = smooth([(0, 31.5), (70, 33.2), (140, 33.8), (230, 32.6), (320, 29.4), (390, 25.8), (H, 22.5)])
    shaft = curve(f, 0, H, 30)
    body = mirror(shaft)
    n = 8
    mod = H / n
    R = []
    for k in range(n):
        y0 = k * mod
        R += [(0.0, y0), (0.42 * f(y0 + mod / 2), y0 + mod / 2)]
    R.append((0.0, H))
    L = [(-x, y) for x, y in R]
    lit = shaft + list(reversed(R))
    diamonds = R + list(reversed(L))
    return H, [("body", body), ("lit", lit), ("mid", diamonds)]


def steinway_111w57():
    H = 435.3
    # Seen from the west, across its long terracotta-and-bronze face (about 44 m, north on the
    # left; only 18 m wide on 57th St, a 1:24 blade). The north edge rises sheer to the top while
    # the south side steps back in a run of ever-deeper setbacks, the "feather" that tapers the
    # upper half to a thin tip. The sunlit south part of every tier is lit.
    xn = -22.0                                          # north face
    ys = [0, 150, 178, 204, 228, 250, 270, 289, 307, 324, 340, 355, 369, 382, 395]
    xs = [22.0, 20.8, 19.2, 17.2, 14.7, 11.8, 8.4, 4.6, 0.4, -4.0, -8.0, -11.4, -13.8, -15.3, -16.2]
    tiers = list(zip(ys, xs)) + [(H, None)]
    body = [(xn, 0)] + steps(tiers) + [(xn, H)]
    split = -6.0                                        # sunlit faces to the right of this line
    n = max(i for i, x in enumerate(xs) if x > split)
    lit = [(split, 0)] + steps(tiers[:n + 1] + [(ys[n + 1], None)]) + [(split, ys[n + 1])]
    return H, [("body", body), ("lit", lit)]


def one_vanderbilt():
    H = 427.0
    # Four interlocking, tapering volumes that spiral up: seen from 42nd Street the front pair
    # (west, then east) end in glazed tops that slope up towards the centre, then the two rear
    # volumes do the same higher up, leaving a narrow crystal-like crown at the 397 m roof and
    # the 30 m spire. The east volume's face is sunlit; the rear volume above it is half-lit.
    right = [(29.5, 0), (23.5, 295), (15.5, 307), (13.5, 362), (7, 384), (6, 397)]
    spire = [(2.0, 397), (0.8, H)]
    left = [(-29.5, 0), (-24, 262), (-15, 276), (-13, 338), (-6, 354), (-5, 397)]
    body = right + spire + [(-x, y) for x, y in reversed(spire)] + list(reversed(left))
    slot = 2.0                                         # the interlock crease up the face
    east = [(slot, 0), (29.5, 0), (23.5, 295), (15.5, 307), (slot, 327.25)]
    rear = [(slot, 327.25), (15.5, 307), (13.5, 362), (7, 384), (6, 397), (slot, 397)]
    return H, [("body", body), ("lit", east), ("mid", rear)]


def park_432():
    H = 425.7
    # A pure square prism, 28.5 m a side and fifteen times as tall, drawn face on with a flat
    # roof. The sunlit half of the grid facade is broken by the five open double-height
    # mechanical floors, spaced about every twelve storeys, and by the open frame round the roof.
    w = 14.25
    body = mirror([(w, 0), (w, H)])
    voids = [(88, 98), (154, 164), (220, 230), (286, 296), (352, 362)]
    top = 413
    edges = [0]
    for a, b in voids:
        edges += [a, b]
    edges.append(top)
    shapes = [("body", body)]
    for y0, y1 in zip(edges[::2], edges[1::2]):
        shapes.append(("lit", [(0, y0), (w, y0), (w, y1), (0, y1)]))
    return H, shapes


def marina_101():
    H = 425.0
    # One of the slenderest supertalls: a straight, square shaft about 36 m wide, ringed by flared
    # Art Deco steel cornices at the mechanical floors (L33, L57, L79) and at the top floor
    # (371 m), crowned by the 50 m sky-blue steel crown whose ribs taper to a four-point pinnacle.
    hw = 18.0
    top = 365.0                                        # shaft top, under the crown's cornice
    bands = [(117, 124), (205, 212), (286, 293)]       # flared cornices at the mechanical floors

    def flare(y0, y1, out):
        return [(hw, y0), (hw + out, y0 + out), (hw + out, y1), (hw, y1)]

    right = [(hw, 0)]
    for y0, y1 in bands:
        right += flare(y0, y1, 1.5)
    right += [(hw, top), (hw + 2.5, top + 2.5), (hw + 2.5, 374), (15.5, 374)]
    f = lambda y: 15.5 * ((H - y) / (H - 374)) ** 1.3
    crown = curve(f, 374, 419, 12)
    body = mirror(right + crown[1:] + [(0.9, H)])
    # The sunlit right face of the shaft, crossed by the cornice bands (mid); on the crown the
    # facet beside the axis catches the light and the corner rib turns away from it.
    shapes = [("body", body), ("lit", [(0, 0), (hw, 0), (hw, top), (0, top)])]
    for y0, y1 in bands:
        shapes.append(("mid", [(0, y0)] + flare(y0, y1, 1.5) + [(0, y1)]))
    shapes.append(("mid", [(0, top), (hw, top), (hw + 2.5, top + 2.5), (hw + 2.5, 374), (0, 374)]))
    shapes.append(("lit", [(0, 374)] + curve(lambda y: 0.62 * f(y), 374, 419, 12) + [(0, 419)]))
    shapes.append(("mid", curve(lambda y: 0.62 * f(y), 374, 419, 12)
                   + list(reversed(curve(f, 374, 419, 12)))))
    return H, shapes


def trump_chicago():
    H = 423.2
    # Seen from the river (south), east to the right: a broad glass slab that steps back in
    # alternate directions to line up with its neighbours: east at 65 m (Wrigley Building cornice),
    # west at 121 m (Marina City / River Plaza), east again at 201 m (330 N Wabash). The top tier
    # steps in once more at 338 m under the flat roof, and the tapering spire rises from its middle.
    L = [(0, 41), (121, 29), (338, 25), (357, None)]     # west edge: one setback
    R = [(0, 41), (65, 30), (201, 18), (338, 14), (357, None)]   # east edge: two setbacks
    sx = -5.5                                            # spire axis: centre of the top tier
    spire = [(sx + 4.2, 357), (sx + 4.2, 361), (sx + 3.0, 361), (sx + 2.0, 392), (sx + 0.7, H)]
    spire_l = [(2 * sx - x, y) for x, y in reversed(spire)]
    body = steps(R) + spire + spire_l + list(reversed(steps(L, -1)))
    # The sunlit right half of each tier, measured from the spire axis, with a dark line at each
    # setback terrace so the stacked slabs read.
    tiers = [(0, 65, 41), (65, 121, 30), (121, 201, 30), (201, 338, 18)]
    shapes = [("body", body)]
    for y0, y1, xr in tiers:
        yb = y0 + 3 if y0 else 0
        shapes.append(("lit", [(sx, yb), (xr, yb), (xr, y1), (sx, y1)]))
    shapes.append(("mid", [(sx, 341), (14, 341), (14, 357), (sx, 357)]))
    return H, shapes


def jpmorganchase_tower():
    H = 423.1
    # 270 Park Avenue seen from the north (48th St), across its long Park-to-Madison face: the body
    # is lifted 24 m on splayed fan columns over a recessed glass lobby, then steps in symmetrically
    # on the east and west, the first setback at the 17th floor; the top two tiers form the crown.
    tiers = [(24, 54), (115, 45), (200, 37), (285, 29), (360, 21), (H, None)]
    right = [(44, 0), (44, 15), (54, 24)] + steps(tiers)
    body = mirror(right)
    lit = [(0, 24)] + steps(tiers) + [(0, H)]          # the sunlit half of every tier
    # the glass lobby seen between two fan columns, which splay up as dark Vs from ground pivots
    glass_mid = [(-24, 0), (24, 0), (5, 23), (-5, 23)]
    glass_r = [(32, 0), (44, 0), (44, 15), (49, 21)]
    glass_l = [(-x, y) for x, y in reversed(glass_r)]
    return H, [("body", body), ("lit", lit), ("mid", glass_mid), ("mid", glass_r), ("mid", glass_l)]


def minying_itc_t2():
    H = 422.6
    # Dongguan's white orchid: a square shaft with a gentle swell that closes at the top like a
    # bud. Seen across the diagonal, the front petal rises to the tip between two lower side
    # petals that hold the club, observation deck and lantern; the front petal is in half-light
    # and the right face is in sun.
    f = smooth([(0, 27), (120, 28), (240, 27.5), (310, 25.5), (350, 22.5), (378, 18.5)])
    shaft = curve(f, 0, 378, 18)
    side_tip = [(16.8, 384), (14.6, 392), (12.0, 398)]          # side petal curling in to its tip
    notch = (7.0, 374)
    front = [(7.6, 384), (7.4, 395), (6.4, 405), (4.6, 413), (2.4, 419.5), (0, H)]
    right = shaft + side_tip + [notch] + front
    body = right + [(-x, y) for x, y in reversed(right[:-1])]
    # the seams of the front petal, swelling slightly and closing in to the notches
    p = smooth([(0, 9.5), (150, 11), (280, 10.5), (335, 9), (374, 7.0)])
    seam = curve(p, 0, 374, 16)
    lit = [(p(0), 0)] + shaft + side_tip + [notch] + list(reversed(seam[1:-1]))
    petal = seam + front + [(-x, y) for x, y in reversed(seam + front[:-1])]
    return H, [("body", body), ("mid", petal), ("lit", lit)]


def jin_mao_tower():
    H = 420.5
    # The pagoda: a 53 m wide shaft whose segments each run about 1/8 shorter than the one below
    # (16 floors at the foot), so the setbacks come ever faster and the outline curves in towards
    # the 88th-floor deck; above it the stepped crown narrows to the roof at ~370 m and the spire.
    r = 7.0 / 8.0
    tiers, y, h = [], 0.0, 64.8
    widths = [26.5, 25.8, 24.9, 23.8, 22.5, 21.0, 19.2, 17.1]      # half-width of each segment
    for hw in widths:
        tiers.append((y, hw)); y += h; h *= r
    deck = y                                                          # ~340 m: 88th-floor deck
    crown_t = [(deck, 14.6), (deck + 11, 11.6), (deck + 20, 8.6), (deck + 26, 5.6), (370.5, None)]
    tiers_all = tiers + crown_t
    spire = [(3.4, 370.5), (2.4, 380), (1.3, 400), (0.5, H)]
    right = steps(tiers_all) + spire
    body = mirror(right)
    # the sunlit right half of every segment, cut apart at the setbacks so the rhythm reads
    shapes = [("body", body)]
    bounds = [t[0] for t in tiers_all]
    for (y0, hw), y1 in zip(tiers_all, bounds[1:]):
        gap = 2.5 if y1 - y0 > 8 else 1.5
        shapes.append(("lit", [(0, y0 + (gap if y0 > 0 else 0)), (hw, y0 + (gap if y0 > 0 else 0)), (hw, y1), (0, y1)]))
    return H, shapes


def zijin_financial():
    H = 416.6
    # gmp's tower of three vertically staggered volumes on a near-square plan (~50 m): the
    # middle volume runs up to the roof, the right one stops lower and the left one lower still,
    # leaving terraces at the top. Two double-height glass bands (the sky lobbies) cut across
    # the lit faces as dark lines; the glass slots between the volumes show as tone changes.
    xl, xm, xr, w = -10.0, 8.0, 25.0, 25.0          # volume edges: left | middle | right
    y_left, y_right = 366.0, 392.0                  # tops of the lower volumes
    body = [(-w, 0), (w, 0), (w, y_right), (xm, y_right), (xm, H), (xl, H),
            (xl, y_left), (-w, y_left)]
    bands = [(128.0, 138.0), (272.0, 282.0)]

    def cut(x0, x1, top):
        out, y = [], 0.0
        for b0, b1 in bands:
            out.append([(x0, y), (x1, y), (x1, b0), (x0, b0)])
            y = b1
        out.append([(x0, y), (x1, y), (x1, top), (x0, top)])
        return out

    gap = 1.2                                        # the vertical glass slot
    shapes = [("body", body)]
    shapes += [("mid", p) for p in cut(xl + gap, xm - gap, H)]
    shapes += [("lit", p) for p in cut(xm + gap, w, y_right)]
    return H, shapes


def princess_tower():
    H = 413.4
    # A slender square residential shaft (about 40 m across) with a column of bowed balconies
    # up the middle of each face (lit) and glazed corners (the sunlit one in mid tone). The
    # glass-clad top floors step back to the top floor at 357 m; above it two crenellated rings
    # step in around the ribbed dome (top 392 m), which carries a short spire.
    right = [
        (20.0, 0), (20.0, 322),            # main shaft
        (17.0, 322), (17.0, 340),          # glass-clad top floors step back
        (14.5, 340), (14.5, 371),          # outer crenellated ring (corner merlon)
        (11.5, 371), (11.5, 367),
        (11.5, 381), (8.5, 381), (8.5, 378),   # inner ring (corner merlon)
    ]
    dome = [(8.5 * math.cos(a), 378 + 14 * math.sin(a)) for a in (math.pi / 2 * i / 12 for i in range(1, 12))]
    spire = [(1.6, 392), (1.0, 402), (0.5, H)]
    body = mirror(right + dome + spire)
    face = [(0, 0), (13, 0), (13, 322), (11, 322), (11, 340), (9, 340), (9, 357), (0, 357)]
    corner = [(13, 0), (20, 0), (20, 322), (17, 322), (17, 340), (14.5, 340), (14.5, 357), (9, 357),
              (9, 340), (11, 340), (11, 322), (13, 322)]
    crown = [(0, 357), (14.5, 357)] + right[5:] + dome + [(0, 392)]     # rings and dome, merlons included
    return H, [("body", body), ("lit", face), ("mid", corner), ("lit", crown)]


def al_hamra_tower():
    H = 412.6
    # Seen from the south. A quarter of each floor plate is carved away, the cut turning from
    # the west side at the base to the east side at the top, so a dark glazed gash sweeps up
    # across the face between the twisting limestone walls: the sunlit stone to its lower right,
    # the stone turned away from the light to its upper left. That stone veil rises past the
    # glass roof into the sloping, pointed crown.
    W = 27.0                                             # half the ~54 m plan
    y_roof = 345.0                                       # the low east end of the sloping top

    def s(t):                                            # smoothstep, for the twist
        t = max(0.0, min(1.0, t))
        return t * t * (3 - 2 * t)

    top = [(W - 2 * W * t, y_roof + (H - y_roof) * t ** 1.5) for t in (i / 20 for i in range(21))]
    body = [(-W, 0), (W, 0)] + top

    def top_y(x):                                        # height of the sloping top above x
        t = (W - x) / (2 * W)
        return y_roof + (H - y_roof) * t ** 1.5

    n = 24
    xa = -3.0                                            # where the gash's left edge meets the crown
    a = [(-W + (W + xa) * s(y / y_roof), y) for y in (y_roof * i / n for i in range(n + 1))]
    b = [(3.0 + (W - 3.0) * s(y / 320.0), y) for y in (320.0 * i / n for i in range(n + 1))]
    lit = [(W, 0)] + list(reversed(b[:-1]))
    mid = a + [(xa, top_y(xa))] + [(x, y) for x, y in top if x < xa]
    return H, [("body", body), ("lit", lit), ("mid", mid)]


def two_ifc():
    H = 412.0
    # Face-on elevation: the 57 m square shaft with its recessed corners runs straight up, then
    # the corners step back four times over the top floors, and the crown of vertical fins rises
    # in steps to its peak, the "shaver" head. The corner recesses stay dark; the face is lit.
    tiers = [(0, 28.5), (288, 26.5), (314, 24.5), (338, 22.5), (360, 20.0), (376, None)]
    # crown fins, outer to centre: blades whose tops slant up toward the axis, each taller
    fins = [(20.0, 390), (16.0, 394), (16.0, 390), (15.0, 390),
            (15.0, 397), (11.0, 401), (11.0, 397), (10.0, 397),
            (10.0, 403), (6.0, 407), (6.0, 403), (5.0, 403),
            (5.0, 408), (0, H)]
    body = mirror(steps(tiers) + [(20.0, 376)] + fins)
    c = 7.0                                               # corner recess left dark
    face = [(x - c, y) for x, y in steps(tiers)]
    lit = [(0, 0)] + face + [(13.0, 376), (13.0, 380), (0, 380)]
    crown = [(0, 380), (13.0, 380), (13.0, 386), (11.0, 386)] + fins[5:]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def lct_landmark():
    H = 411.6
    # Seen from Haeundae Beach: a slim shaft with softly waving sides (the wave-shaped Y plan),
    # whose wings end at staggered heights like the coast's basalt columns: the top steps in on
    # both sides, at different heights, each column's top sloping up towards the axis, to the
    # peaked central prism of the observatory.
    f = smooth([(0, 29), (110, 30), (230, 29.2), (310, 27.8)])
    g = smooth([(0, 29), (110, 30), (230, 29.2), (325, 27.6)])
    rshaft = curve(f, 0, 296, 14)
    lshaft = curve(g, 0, 312, 14)
    R = [(20.5, 308), (20.5, 336), (13.5, 346), (13.5, 368), (7, 378), (7, 398), (0, H)]
    L = [(21, 324), (21, 352), (14, 362), (14, 384), (7, 394), (7, 401)]
    body = rshaft + R + [(-x, y) for x, y in reversed(L)] + [(-x, y) for x, y in reversed(lshaft)]
    # light from the right: the right half of the shaft and of every stepped column, each tier
    # cut apart so the steps read
    lit = [(0, 0)] + rshaft + [(20.5, 308), (0, 316)]
    t1 = [(0, 320), (20.5, 312), (20.5, 336), (13.5, 346), (0, 350)]
    t2 = [(0, 354), (13.5, 350), (13.5, 368), (7, 378), (0, 380)]
    t3 = [(0, 384), (7, 382), (7, 398), (0, H)]
    return H, [("body", body), ("lit", lit), ("lit", t1), ("lit", t2), ("lit", t3)]


def ningbo_center():
    H = 409.0
    # SOM's lotus bud: a square shaft that swells slightly above the base, then draws in over the
    # hotel floors to a crown of four petals. Face-on, the front petal rises to the 409 m tip
    # between the two side petals seen edge-on; the right side catches the light.
    f = smooth([(0, 29), (110, 30), (210, 29.2), (290, 26.6), (345, 23), (368, 20.5)])
    shaft = curve(f, 0, 368, 24)

    def p(y):                                    # half-width of the front petal
        if y >= 368:
            return 12.0 * (1 - ((y - 368) / (H - 368)) ** 1.8)
        return 12.0 * math.sin(0.5 * math.pi * (y - 330) / 38)

    side = [(20.5 - 6.5 * t * t, 368 + 31 * t) for t in (i / 8 for i in range(1, 9))]   # side petal, to its tip
    yn = 384.0                                   # notch between side and front petals
    front_top = [(p(y), y) for y in (yn + (H - yn) * i / 10 for i in range(11))]
    right = shaft + side + front_top[:-1] + [(0, H)]
    body = right[:-1] + [(0, H)] + [(-x, y) for x, y in reversed(right[:-1])]

    lit = [(0, 0)] + shaft + side + [(p(yn), yn), (0, yn)]
    petal_r = [(p(y), y) for y in (330 + (H - 330) * i / 20 for i in range(21))]
    petal = petal_r + [(-x, y) for x, y in reversed(petal_r[:-1])]
    return H, [("body", body), ("lit", lit), ("mid", petal)]


def guangxi_china_resources():
    H = 402.7
    # Seen from the east, north to the left: the office block's south face tapers in on one side
    # only, up to the Level 71 pool terrace (323 m) that caps it; above it the profile shifts as
    # the narrower hotel volume tapers in from the north instead, into the faceted crystal crown
    # with its helipad (396.6 m) and lit beacon.
    def south(y):                                # the single-sided taper of the office block
        return 28.0 - 12.5 * y / 323.0
    right = [(28.0, 0), (south(323), 323), (8.0, 323), (8.0, 372), (4.0, 396.6),
             (0.0, 396.6), (-2.0, H)]
    left = [(-8.0, H), (-10.0, 396.6), (-14.0, 396.6), (-20.0, 372), (-28.0, 323), (-28.0, 0)]
    body = right + left
    # the sunlit face of the office block narrows as the taper bites in
    office = [(2.0, 0), (28.0, 0), (south(323), 323), (2.0, 323)]
    # the hotel volume's sunlit face, and the crown's front facet turned partly to the light
    hotel = [(-6.0, 323), (8.0, 323), (8.0, 372), (4.0, 396.6), (-3.0, 396.6), (-5.0, 372)]
    crown = [(-20.0, 372), (-5.0, 372), (-3.0, 396.6), (-14.0, 396.6)]
    return H, [("body", body), ("lit", office), ("lit", hotel), ("mid", crown)]


def guiyang_ifc_t1():
    H = 401.0
    # A square shaft of curved glass faces runs straight up to the hotel transfer at floor 53
    # (~258 m); above it the faces fold inward twice, each fold steeper than the last, so the
    # top reads as a soft double curve. The crown screen carries the taper on to a flat top.
    # The V-framed corners stay dark; the face between them is lit on its sunny half.
    right = [(27.5, 0), (27.5, 258), (24.8, 320), (19.5, 374), (18.5, 376), (11.5, H)]
    body = mirror(right)
    pier = 6.5
    face = [(27.5 - pier, 0), (27.5 - pier, 258), (24.8 - pier, 320), (19.5 - pier, 374)]
    lit = [(0, 0)] + face + [(0, 374)]
    crown = [(0, 376), (18.5 - pier * 0.8, 376), (11.5 - pier * 0.6, H), (0, H)]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def iconic_tower_cairo():
    H = 393.8
    # A glass obelisk: the slim shaft tapers steadily, then around the top floors (to 360 m)
    # the faces sweep in to a sharp pyramidion tip, the plume crown of Amun. Seen across the
    # diagonal, the arris splits a dark left face from the sunlit right face; the crown's
    # sunlit facet turns a little away from the light.
    f = smooth([(0, 26.5), (160, 24.0), (300, 21.6), (322, 20.6), (342, 17.6), (362, 12.4),
                (378, 7.0), (388, 3.2), (H, 0.6)])
    Y = 318                                                  # where the pyramidion begins
    shaft = curve(f, 0, Y, 10)
    crown = curve(f, Y, H, 20)[1:]
    body = mirror(shaft + crown)
    lit = [(0, 0)] + shaft + [(0, Y)]
    crown_lit = [(0, Y), (f(Y), Y)] + crown[:-2] + [(0, crown[-3][1])]
    return H, [("body", body), ("lit", lit), ("mid", crown_lit)]


def china_merchants_bank_hq():
    H = 393.0
    # The south face towards Shenzhen Bay: a plain, flat-topped prism with the helipad on its
    # roof. The core sits to one side (the north), so the broad south face is all folded glass,
    # its sunlit right half broken at regular intervals by the double-height sky terraces (dark
    # slots). Above the top office floor the tall atrium and landscaped roof terraces form a
    # lighter band under a dark parapet.
    hw = 28.0
    body = mirror([(hw, 0), (hw, H)])
    top_office = 364.6
    slots = [288, 214, 140, 66]                     # sky terraces, top down
    edge = hw - 2.5                                 # a thin lit strip at the corner keeps it whole
    lit = [(0, 0), (hw, 0), (hw, top_office), (0, top_office)]
    for y in slots:
        lit += [(0, y + 7), (edge, y + 7), (edge, y), (0, y)]
    band = [(-hw + 3, top_office + 4), (hw - 3, top_office + 4), (hw - 3, H - 6), (-hw + 3, H - 6)]
    band_lit = [(0, top_office + 4), (hw - 3, top_office + 4), (hw - 3, H - 6), (0, H - 6)]
    return H, [("body", body), ("lit", lit), ("mid", band), ("lit", band_lit)]


def china_resources_tower():
    H = 392.5
    # "Spring Bamboo": a round shaft that swells gently above a slightly tucked-in foot (where
    # the column grid gathers into the lobby diagrid), then closes into a pointed bullet nose
    # where its 56 perimeter columns converge at the apex. The sunlit face is bounded by a
    # column line that follows the taper and meets the others at the tip.
    f = smooth([(0, 28), (40, 30.3), (120, 31), (220, 30), (290, 27), (330, 21.5),
                (358, 14.5), (377, 7.5), (392.5, 0)])
    shaft = curve(f, 0, H, 48)
    body = shaft + [(-x, y) for x, y in reversed(shaft[:-1])]
    rib = [(0.18 * x, y) for x, y in shaft]
    lit = list(reversed(rib)) + shaft[:-1]
    # the round face turning towards the light, between two column lines
    turn = [(-0.3 * x, y) for x, y in shaft]
    mid = list(reversed(turn)) + rib[:-1]
    return H, [("body", body), ("mid", mid), ("lit", lit)]


def marina_23():
    H = 392.4
    # The "pencil" of Dubai Marina, seen square to one face of its octagonal plan (about 42 m
    # across): a straight, slender shaft whose front face and two chamfered corners read as three
    # bands (left in shade, front half lit, right in the sun). At the top the faces fold inward as
    # the sculpted petal canopies over the roof terrace, sharpening to a point round the 67 m mast.
    hw, a = 21.0, 8.7                      # half-width across flats, half the front face
    y0, yp = 310.0, 360.0                  # petals start, petals close on the mast
    f = smooth([(y0, hw), (322, 18.2), (340, 10.9), (yp, 2.6)])
    crown = curve(f, y0, yp, 12)
    right = [(hw, 0)] + crown + [(2.2, yp), (1.0, H)]
    body = mirror(right)
    # front face (partly lit) and right chamfer (sunlit); the face edges converge on the mast
    g = smooth([(y0, a), (322, 7.6), (340, 4.7), (yp, 1.0)])
    edge = curve(g, y0, yp, 12)
    front = [(-a, 0), (a, 0)] + edge + [(-x, y) for x, y in reversed(edge)]
    side = [(a, 0), (hw, 0)] + crown + list(reversed(edge))
    return H, [("body", body), ("mid", front), ("lit", side)]


def citic_plaza():
    H = 390.2
    # A plain square shaft (about 46 m a side) with notched corners, capped by a steep glass
    # pyramid ending at the 322 m roof, from which twin masts rise side by side to the top.
    hw, y_shaft, y_roof = 23.2, 290.0, 321.9
    top_hw = 9.0
    mx, mb, mt = 6.5, 2.2, 1.2                       # mast centre offset, half-width at base / top
    right = [(hw, 0), (hw, y_shaft), (top_hw, y_roof),
             (mx + mb, y_roof), (mx + mt, H), (mx - mt, H), (mx - mb, y_roof)]
    body = mirror(right)
    # the face between the notched corners catches the light (its right half); the pyramid's
    # right half is lit too, a shade softer
    lit = [(0, 0), (17.0, 0), (17.0, y_shaft), (0, y_shaft)]
    crown = [(0, y_shaft), (hw, y_shaft), (top_hw, y_roof), (0, y_roof)]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def citymark_centre():
    H = 388.3
    # KPF's tapering square shaft, seen face-on: straight edges narrow from the ~54 m office base
    # to the slimmer residential top. Recessed corner grooves (the terraces) widen as they rise,
    # so the reflective main face reads as a tapering shard; at the crown its edges flare out and
    # up into wing tips at the corners, with the roof garden parapet dipping between them.
    yc = 352.0                                   # crown starts
    D = lambda y: 27.0 - 9.0 * y / yc            # outer edge of the shaft
    A = lambda y: 25.0 - 15.5 * y / yc           # edge of the main face panel
    tip = (19.6, H)
    dip = 375.0                                  # parapet low point on the axis
    right = [(D(0), 0), (D(yc), yc), (18.6, 372.0), tip, (10.0, 381.0), (0, dip)]
    body = right[:-1] + [(0, dip)] + [(-x, y) for x, y in reversed(right[:-1])]
    # main face: its sunlit right half; the grooves and the shaded half stay dark
    flare = [(A(yc), yc), (11.8, 366.0), (15.6, 378.0), tip, (10.0, 381.0), (0, dip)]
    lit = [(0, 0), (A(0), 0)] + flare
    return H, [("body", body), ("lit", lit)]


def upperhills_t1():
    H = 388.1
    # SOM's ladder-core tower: a plain, slender square prism (megacolumns 28.5 m apart, the corners
    # cantilevered 8.5 m beyond them) tapering gently as it rises. The corners are notched back and
    # stay in shadow; the fin screen of the face runs on 9 m past the top floor as a low parapet crown.
    f = smooth([(0, 23.5), (190, 22.4), (379.1, 20.6)])
    top = 379.1
    shaft = curve(f, 0, top, 12)
    crown = [(f(top) - 5.5, top), (f(top) - 5.5, H)]
    body = mirror(shaft + crown)
    # the main face between the notched corners: its sunlit right half
    face = curve(lambda y: f(y) - 5.5, 0, top, 12)
    lit = [(0, 0)] + face + [(f(top) - 5.5, H), (0, H)]
    return H, [("body", body), ("lit", lit)]


def hudson_yards_30():
    H = 387.1
    # Seen from the south: a broad glass shaft that narrows slightly on its east side, its top
    # sheared off by a crown plane sloping down to the east, and Edge, the triangular sky deck,
    # cantilevered about 24 m out from the 100th floor (335 m) just below the slope.
    xl, x0, x1 = -30.0, 30.0, 26.5          # west edge; east edge at the ground and at the crown
    yc, band = 344.0, 14.0                  # where the crown slope meets the east face; its depth
    deck = [(x1 + 0.3, 325.5), (x1 + 21.5, 333.0), (x1 + 24.0, 339.5), (x1, 339.5)]
    body = [(xl, 0), (x0, 0)] + deck + [(x1, yc), (xl, H)]
    # the east half of the shaft catches the light; the sloping crown plane is a lighter facet
    slope = lambda x: yc + (H - yc) * (x1 - x) / (x1 - xl)
    lit = [(0, 0), (x0, 0), (x1 + 0.3, 325.5), (x1, yc - band), (0, slope(0) - band)]
    crown = [(x1, yc - band), (x1, yc), (xl, H), (xl, H - band)]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def pif_tower():
    H = 385.0
    # A slim prism on a pleated hexagonal plan, its faceted glass faces folding along a crease
    # up the middle, so the right half catches the light. Above the office floors the facets
    # fold inward into the tall crystalline crown, sharpening to a point; the side facet that
    # turns away from us begins lower down and runs up into the tip.
    f = smooth([(0, 26.5), (150, 25.2), (296, 23.5)])
    shaft = curve(f, 0, 296, 12)
    crown = [(18.5, 326), (11.5, 352), (5.5, 372), (2.2, 380.5), (0.6, H)]
    body = mirror(shaft + crown)
    tip = (0, 383)
    # the crease runs up the face to the tip; to its right the sunlit facet
    lit = [(0, 0)] + curve(f, 0, 240, 10) + [(13.5, 300), (8.5, 334), tip]
    # the outer facet folding into the crown, turned partly to the light
    side = curve(f, 240, 296, 4) + crown[:-1] + [tip, (8.5, 334), (13.5, 300)]
    return H, [("body", body), ("lit", lit), ("mid", side)]


def shun_hing_square():
    H = 384.0
    # Seen on its broad face: a slab about 70 m wide (only ~36 m deep, hence its famous
    # slenderness) whose two rounded end towers rise past the central roof (305 m) to 325 m,
    # taper like syringe barrels and run on up as the twin needle spires. The flat glass face
    # between them is half-lit; the right end tower and the spires' right halves catch the light.
    W, E, c = 34.5, 20.5, 27.5           # half-width, inner edge of the end towers, spire axis
    roof, shoulder, cone = 305, 314, 326
    def needle(cx):                      # hub, then the needle, listed right side bottom to top
        return [(cx + 3.0, cone), (cx + 3.0, 346), (cx + 1.7, 346), (cx + 1.0, H)]
    right = ([(W, 0), (W, shoulder)] + needle(c)
             + [(2 * c - x, y) for x, y in reversed(needle(c))]
             + [(E, shoulder), (E, roof)])
    body = mirror(right)
    face = [(-E, 0), (E, 0), (E, roof), (-E, roof)]
    lit_end = ([(E, 0), (W, 0), (W, shoulder)] + needle(c)
               + [(c, H), (c, cone), (c - 3.0, cone), (E, shoulder)])
    lit_spire = needle(-c) + [(-c, H), (-c, cone)]
    return H, [("body", body), ("mid", face), ("lit", lit_end), ("lit", lit_spire)]


def eton_place_dalian():
    H = 383.2
    # A slim, near-square glass prism that tapers slightly; its top is sliced off at a slant,
    # the facade screen running on above the top floor (349.5 m) up to the high corner. The
    # sunlit face is lit; the crown screen above the roof is a paler wedge.
    def hw(y):
        return 23.0 - 2.2 * y / 383.2
    top = 349.5
    yl = 351.0                                   # low corner of the slanted crown
    right = [(hw(0), 0), (hw(H), H)]
    left = [(-hw(yl), yl), (-hw(0), 0)]
    body = right + left
    def slope(x):                                # the slanted top edge, low left to high right
        return yl + (H - yl) * (x + hw(yl)) / (hw(yl) + hw(H))
    x0 = 1.5
    lit = [(x0, 0), (hw(0), 0), (hw(top), top), (x0, top)]
    crown = [(x0, top), (hw(top), top), (hw(H), H), (x0, slope(x0))]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def autograph_tower():
    H = 382.9
    # A straight square shaft of pinwheeling glass planes; the cantilevered observation box at
    # level 56-58 (~250 m) juts out from one face, the roof steps up in staggered blocks and an
    # occupiable spire runs on to the tip.
    W = 26.0
    right = [(W, 0), (W, 246), (37, 246), (37, 261), (W, 261),      # observation box
             (W, 330), (9, 330), (9, 341),                          # stepped roof blocks
             (5.0, 341), (3.6, 360), (1.0, H)]                      # spire
    left = [(-1.0, H), (-3.6, 360), (-5.0, 341), (-9, 341), (-9, 315), (-W, 315), (-W, 0)]
    body = right + left
    face = [(2, 0), (23, 0), (23, 330), (9, 330), (9, 338), (2, 338)]   # sunlit glass plane
    box = [(W, 246), (37, 246), (37, 261), (W, 261)]
    spire = [(0, 341), (5.0, 341), (3.6, 360), (1.0, H), (0, H)]
    return H, [("body", body), ("lit", face), ("lit", box), ("mid", spire)]


def nanning_logan_1():
    H = 381.3
    # Face-on: the rectangular plan is split into four segments by deep grooves, so the face
    # reads as two halves meeting at a central groove. The shaft runs straight through the
    # office floors, then tapers through the hotel zone; above the top floor the segments open
    # out into the lotus crown, petals whose pointed tips lean outwards at the corners around
    # the rooftop helipad, leaving a V between them over the groove.
    f = smooth([(0, 24), (200, 23.5), (270, 22), (325, 19.2), (348, 18.4)])
    shaft = curve(f, 0, 348, 18)
    # outer edge of the right petal flaring out to its tip, then its inner edge down to the groove
    petal = [(19.0, 358), (20.4, 367), (22.2, 375), (23.8, H),
             (19.8, 378.8), (14, 374.6), (8, 370.4), (3.5, 366.2), (1.6, 364.4)]
    right = shaft + petal
    body = right + [(0, 363.4)] + [(-x, y) for x, y in reversed(right)]
    # light from the right: the right-hand segment is lit, the groove and left segment dark
    lit = [(2.2, 0)] + shaft + petal[:-1] + [(2.2, 365.4)]
    return H, [("body", body), ("lit", lit)]


def burj_mohammed_bin_rashid():
    H = 381.2
    # Foster's slender residential tower over the Central Market souk: a gently tapering shaft
    # whose curved face sweeps in at the top to a sliced, sloping crown, peaking on the left.
    rf = smooth([(0, 24), (150, 23.5), (270, 22.5), (310, 20), (345, 12), (368, 0), (H, -13)])
    lf = smooth([(0, 24), (200, 23), (330, 21.5), (365, 18.5), (H, 13)])
    right = curve(rf, 0, H, 40)
    left = [(-x, y) for x, y in reversed(curve(lf, 0, H, 30))]
    body = right + left[1:]
    # the curved face to the right of the ridge catches the light, all the way up the crown
    ridge = lambda y: 3 - 16 * max(0.0, (y - 300) / (H - 300)) ** 1.4
    lit = [(ridge(0), 0)] + right + list(reversed(curve(ridge, 0, H, 20)))[1:]
    # the crown of fins above the top floor, sloping with the roof, on the shaded side
    cap = [(-lf(342), 342), (ridge(302), 302)] + curve(ridge, 302, H, 16)[1:] \
        + [(-x, y) for x, y in reversed(curve(lf, 342, H, 10))][1:]
    return H, [("body", body), ("lit", lit), ("mid", cap)]


def empire_state():
    H = 381.0
    # The broad 34th Street face. The five-storey base fills the 129 m lot; above it the tower is
    # set back 18 m from each end and steps in like a wedding cake at the 21st, 25th and 30th
    # floors to the 56 m shaft, which narrows again at the 72nd, 81st and 85th floors to the
    # 86th-floor observatory. On top, the mooring mast: finned rectangular tiers, a slim
    # cylinder and the truncated cone at 381 m (the later TV antenna above is left out).
    tiers = [(0, 64.6), (25, 46.3), (80, 40.1), (95, 34.0), (113, 27.8), (268, 23.0),
             (302, 17.5), (316, 13.0), (320, 10.0), (326, None)]
    flare = smooth([(326, 8.5), (334, 6.6), (342, 5.0), (348, 4.2)])
    mast = curve(flare, 326, 348, 8) + [(4.2, 371), (4.6, 371), (4.6, 376), (3.4, 376), (1.6, H)]
    right = steps(tiers) + mast
    body = mirror(right)
    # the sunlit right half of every tier, and of the mast's finned base
    lit = [(0, 0)] + steps(tiers) + [(0, 326)]
    mast_lit = [(0, 326)] + curve(flare, 326, 348, 8) + [(4.2, 371), (0, 371)]
    return H, [("body", body), ("lit", lit), ("mid", mast_lit)]


def elite_residence():
    H = 380.5
    # A slender square shaft (~42 m) of beige stone piers that narrows in two setbacks round
    # the top occupied floor (314.5 m); above them the concrete crown steps in like a tiered
    # pyramid to about 355 m, where the steel pinnacle takes it to a point. The sunlit right
    # half of the shaft is lit; the crown's right face, turned partly to the light, is mid.
    tiers = [(0, 21), (286, 18.5), (306, 16), (322, None)]
    crown = [(13, 322), (13, 330), (10.5, 330), (10.5, 338), (8, 338), (8, 346), (5.5, 346),
             (5.5, 353), (3.4, 353), (2.4, 364), (1.0, H)]
    body = mirror(steps(tiers) + crown)
    lit = [(0, 0)] + steps(tiers) + [(0, 322)]
    crown_lit = [(0, 322)] + crown[:-1] + [(0, 364)]
    return H, [("body", body), ("lit", lit), ("mid", crown_lit)]


def corporate_avenue_1():
    H = 376.0
    # Pelli's "sail" tower by the Yangtze: a slim shaft whose curving faces draw in as they rise,
    # glass up to the top floor at 336 m, then the facade runs on as a tapering screen crown.
    f = smooth([(0, 27), (150, 26.5), (250, 25.2), (300, 22.5), (336, 18.5), (360, 14), (376, 10.5)])
    shaft = curve(f, 0, H, 30)
    body = mirror(shaft)
    # the face is curved in plan: its right half turns to the light; the crown screen reads mid
    lit = [(0, 0)] + curve(f, 0, 336, 26) + [(0, 336)]
    crown = [(0, 336)] + curve(f, 336, H, 6) + [(0, H)]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def dabaihui_plaza():
    H = 375.6
    # KPF's columnar, subtly tapering shaft (about 49 m wide) is wrapped in four overlapping,
    # pinwheeling facade screens (the bougainvillea's bracts). Above the top floor (307 m) the
    # screens rise on and are cut away in sweeping curves, each climbing to a tip at a corner,
    # revealing the occupied dome between them: the sunlit front screen sweeps up to the right
    # tip, the shaded back screen to the left one, and the dome shows in the cleft.
    f = smooth([(0, 24.5), (100, 24.9), (220, 23.9), (300, 22.4), (H, 21)])
    t = f(H)
    def front(x): return 316 + (H - 316) * max(0.0, (x + t) / (2 * t)) ** 2.4
    def back(x): return 316 + (H - 316) * max(0.0, (t - x) / (2 * t)) ** 2.4
    def dome(x): return 318 + 29 * math.sqrt(max(0.0, 1 - (x / 18.5) ** 2))
    xs = [t - 2 * t * i / 60 for i in range(61)]
    top = [(x, max(front(x), back(x), dome(x))) for x in xs]
    right = curve(f, 0, H, 24)
    left = [(-x, y) for x, y in reversed(right)]
    body = right[:-1] + top + left[1:]
    # lit: the front screen, right of its overlap with the shaded west screen, up to its cut edge
    seam = [(-0.42 * f(y), y) for y in (318 * (1 - i / 16) for i in range(17))]
    x0 = seam[0][0]
    cut = [(x, front(x)) for x in xs if x > x0] + [(x0, front(x0))]
    lit = right[:-1] + cut + seam
    # the dome, where it shows above the front screen's cut edge
    ds = [x for x in (-18.5 + 37 * i / 74 for i in range(75)) if dome(x) > front(x)]
    dome_up = [(x, dome(x)) for x in ds]
    dome_lo = [(x, front(x)) for x in reversed(ds)]
    return H, [("body", body), ("mid", dome_up + dome_lo), ("lit", lit)]


def guangdong_business_center():
    H = 375.5
    # SOM's all-steel box (57 x 49.5 m plan), seen on its 49.5 m east face: the 22 m glazed
    # "City Room" lifts the tower off the street, belt trusses at floors 4-6 and 34-35, and the
    # mega-braced frame on the three office faces reads as stacked X's (dark left, lit right,
    # mid diamonds where the braces cross). The open, perforated crown screens the roof
    # plant from the 338 m roof up to 375.5 m. The offset core is on the far (west) side.
    w = 24.75                      # half the face width
    a = 21.0                       # inside the corner mega columns
    body = mirror([(w, 0), (w, H)])

    def xbrace(y0, y1):
        m = (y0 + y1) / 2
        return [("lit", [(a, y0), (a, y1), (0, m)]),
                ("mid", [(-a, y0), (a, y0), (0, m)]),
                ("mid", [(-a, y1), (0, m), (a, y1)])]

    shapes = [("body", body)]
    shapes.append(("mid", [(-a, 0), (a, 0), (a, 22), (-a, 22)]))       # glazed city room
    for y0, y1 in ((33, 104.5), (104.5, 176), (186, 262), (262, 338)):  # mega braces
        shapes += xbrace(y0, y1)
    shapes.append(("mid", [(-a, 342), (a, 342), (a, H), (-a, H)]))      # crown screen
    shapes.append(("lit", [(0, 342), (a, 342), (a, H), (0, H)]))
    return H, shapes


def central_plaza_hk():
    H = 373.9
    # Seen corner-on: the triangular plan with its three corners cut off, so the front chamfer is a
    # narrow strip between the two side faces, the right one sunlit. The prism rises straight to
    # 266 m, where the three-sided glass pyramid closes to the roof at 309 m, and the 102 m mast
    # (partly hidden inside the pyramid) runs on up to its tip.
    W = 29.5                     # half the corner-on width (side ~77 m less the ~15 m corner cuts)
    c = 7.75                     # half the front chamfer
    yt, yr = 266.0, 309.0        # top of the prism; apex of the pyramid
    a = 3.0                      # half-width of the pyramid's apex, where the mast leaves it
    right = [(W, 0), (W, yt), (a, yr),
             (2.6, yr), (2.6, 338), (1.9, 338), (1.3, H)]   # mast, slimmer upper stage
    body = mirror(right)
    face = [(c, 0), (W, 0), (W, yt), (a, yr), (1.0, yr)]          # sunlit side face and its pyramid face
    chamfer = [(-c, 0), (c, 0), (c, yt), (1.0, yr), (-1.0, yr), (-c, yt)]  # front corner, half-lit
    return H, [("body", body), ("lit", face), ("mid", chamfer)]


def federation_tower():
    H = 373.7
    # Federation Tower East, a glass "sail": a rounded triangle in plan (sides about 60 m),
    # seen a little off the side so its one vertical face (which faces the West tower) shows
    # as a dark strip on the left. Above level 26 the two outer faces slope inward, so the
    # plan shrinks towards the vertical face and the tower narrows into a short pointed crown
    # above the top floor at 360 m. The sloping face toward us takes the light.
    M = -20.5                                     # the plan shrinks towards this line
    s = smooth([(0, 1.0), (105, 1.0), (180, 0.95), (250, 0.84), (300, 0.70), (335, 0.53),
                (355, 0.38), (364, 0.27)])
    right = curve(lambda y: M + 49 * s(y), 0, 364, 28)
    left = curve(lambda y: M - 8 * s(y), 0, 364, 28)
    seam = curve(lambda y: M + 7.5 * s(y), 0, 364, 28)        # corner between the two faces
    crown_r = [(-12.5, 369), (-17.5, 372.3), (-19.6, H)]
    crown_l = [(-21.4, H), (-22.3, 369)]
    body = right + crown_r + crown_l + list(reversed(left))
    lit = right + [(-12.8, 368.6), (-17.8, 372.0), (-19.9, 373.2)] + list(reversed(seam))
    return H, [("body", body), ("lit", lit)]


def ciel_tower():
    H = 373.5
    # Seen on its broad, sea-facing side: a tapered oval drawn in at the foot and narrowing to a
    # rounded needle tip. A slot up the middle (the 300 m atrium of stacked sky gardens) splits it
    # into two curved halves that rejoin at the crown, where the slot opens into the "eye of the
    # needle", a cut-out you see the sky through.
    yc = 354                                         # where the shaft turns into the rounded tip
    f = smooth([(0, 22.5), (50, 25.8), (130, 27.5), (215, 26.8), (290, 23.8), (330, 19.8), (yc, 15.5)])
    w0 = f(yc)

    def w(y):                                        # half-width of the whole outline, tip included
        if y <= yc:
            return f(y)
        u = min(1.0, (y - yc) / (H - yc))
        return w0 * (1 - u * u) ** 0.625

    right = curve(f, 0, yc, 22) + [(w(y), y) for y in (yc + (H - yc) * i / 10 for i in range(1, 10))] + [(0, H)]
    body = right + [(-x, y) for x, y in reversed(right[:-1])]
    s = 4.3                                          # half-width of the atrium slot
    y_a, y_e0, y_e1 = 24, 318, 356                   # atrium foot, eye bottom and top
    eye = [(4.8 * math.sin(math.pi * i / 20), y_e0 + (y_e1 - y_e0) * (1 - math.cos(math.pi * i / 20)) / 2)
           for i in range(21)]
    eye = eye + [(-x, y) for x, y in reversed(eye[1:-1])]
    # sunlit right half; the left half's inner face is half-lit, its far edge turns away into shadow
    top = y_e0 + 6
    lit = [(0, 0)] + right + [(0, y_e1), (s, top), (s, y_a), (0, y_a)]
    mid = ([(0, 0), (0, y_a), (-s, y_a), (-s, top), (0, y_e1), (0, H - 1)]
           + [(-0.72 * w(y), y) for y in (H - 1 - (H - 1) * i / 30 for i in range(31))])
    return H, [("body", body), ("mid", mid), ("lit", lit), ("hi", eye)]


def dalian_itc():
    H = 370.2
    # A straight prism on a rectangular plan with chamfered corners, seen square to its broad
    # face; it rises without setbacks to a flat roof (helipad). The chamfers read as edge strips
    # (the right one turned to the light), the face right of the axis is lit, and the crown,
    # where the mullions cross in a diamond pattern, shows one big dark diamond.
    hw, c = 25.0, 6.0                   # half the broad face; chamfer strip at each corner
    dw = hw - c                         # half the flat face between the chamfers
    y0 = 338.0                          # foot of the crown
    ym = (y0 + H) / 2                   # height of the diamond's side points
    body = [(-hw, 0), (hw, 0), (hw, H), (-hw, H)]
    face = [(0, 0), (dw, 0), (dw, y0), (0, y0)]
    chamfer = [(dw, 0), (hw, 0), (hw, H), (dw, H)]
    crown_l = [[(-dw, y0), (0, y0), (-dw, ym)], [(-dw, ym), (0, H), (-dw, H)]]
    crown_r = [[(0, y0), (dw, y0), (dw, ym)], [(dw, ym), (dw, H), (0, H)]]
    shapes = [("body", body), ("lit", face), ("mid", chamfer)]
    shapes += [("mid", t) for t in crown_l] + [("lit", t) for t in crown_r]
    return H, shapes


def address_boulevard():
    H = 370.0
    # Seen on its broad face: the elliptical shaft (about 60 m along the long axis) steps in
    # through a run of Art Deco setbacks from about 200 m, while the projecting central spine
    # of fins runs up the face and splits above the top into the two matching spires.
    tiers = [(0, 30), (205, 27), (235, 23.5), (258, 19.5), (278, 15), (295, 11.5), (305, None)]
    spire = [(9.5, 305), (8.6, 330), (7.3, 355), (6.4, H), (5.6, 358), (4.6, 330), (3.6, 305)]
    right = steps(tiers) + spire + [(0, 305)]
    body = right[:-1] + [(-x, y) for x, y in reversed(right)][1:]
    sp = 9.5                                            # half-width of the central spine
    lit = [(sp, 0)] + steps(tiers) + [(sp, 305)]        # the curved face turning to the light
    spine = [(-sp, 0), (sp, 0), (sp, 305), (-sp, 305)]  # the spine faces us
    lit_spire = [(6.5, 305), (9.5, 305), (8.6, 330), (7.3, 355), (6.4, H)]
    return H, [("body", body), ("mid", spine), ("lit", lit), ("lit", lit_spire)]


def three_itc_b():
    H = 369.7
    # Xujiahui Centre's tall tower (Pelli Clarke & Partners): a slim, gently tapering glass slab
    # whose crown sweeps down in one curve from its high corner, the facade carried up past the
    # roof as a screen. The sunlit half of the face is lit; the screen above the roof is mid.
    lf = lambda y: 25.5 - 2.0 * y / 330.0           # half-width, tapering slightly
    y_hi, y_lo = H, 322.0                            # crown's high (left) and low (right) corners
    def top(x):                                      # the sweep, flat at the left, falling right
        t = (x + lf(330)) / (2 * lf(330))
        return y_hi - (y_hi - y_lo) * t ** 2.2
    w = lf(330)
    sweep = [(w - 2 * w * i / 24, top(w - 2 * w * i / 24)) for i in range(25)]   # right to left
    right = [(lf(0), 0), (w, y_lo)]
    left = [(-w, H), (-lf(0), 0)]
    body = right + sweep[1:-1] + left
    lit = [(0, 0), (lf(0), 0), (w, y_lo)] + [p for p in sweep[1:] if p[0] > 0] + [(0, top(0))]
    roof = 314.0                                     # top of the occupied floors
    screen = [(-w, roof), (0, roof), (0, top(0))] + [p for p in sweep if p[0] < 0] + [(-w, H)]
    return H, [("body", body), ("lit", lit), ("mid", screen)]


def qingdao_haitian():
    H = 368.9
    # Seen broadside (from the east): a slim, elongated hexagonal prism whose north and south tips
    # push in and out as it rises, so the two edges ripple in a slow wave, out of step. The tips
    # round in at the top into the low glass dome over the club and helipad. The long front face
    # takes the half-light; the angled facet to the south (right) catches the sun.
    fr = smooth([(0, 28), (85, 30.5), (185, 27), (275, 30), (330, 29), (348, 26.5),
                 (359, 22), (365.5, 17), (H, 12)])
    fl = smooth([(0, 29), (105, 26.5), (205, 30), (295, 27.5), (335, 27.5), (351, 25),
                 (361, 20.5), (366.5, 16), (H, 12)])
    c = smooth([(0, 17), (335, 17), (352, 15), (363, 11), (H, 7)])   # the front face's creases
    n = 40
    right = curve(fr, 0, H, n)
    left = [(-x, y) for x, y in reversed(curve(fl, 0, H, n))]
    body = right + left
    crease = curve(c, 0, H, n)
    face = crease + [(-x, y) for x, y in reversed(crease)]
    facet = right + list(reversed(crease))
    return H, [("body", body), ("mid", face), ("lit", facet)]


def golden_eagle_tiandi_a():
    H = 368.1
    # The tallest of the three Golden Eagle towers: a slim, gently tapering glass prism whose
    # crown is cut on a slant, high on the right. Two-thirds of the way up, the six-storey sky
    # platform that ties the three towers together crosses the shaft and reaches out to the left
    # towards its neighbours.
    def hw(y):                      # half-width of the shaft, tapering slightly
        return 25.0 - 2.5 * y / H
    p0, p1, reach = 198.0, 228.0, 14.0    # sky platform floors and how far it reaches out
    soffit = 206.0                        # its underside rises towards the open end
    yl = 340.0                            # low side of the slanted crown
    right = [(hw(0), 0), (hw(H), H)]
    left_up = [(-hw(yl), yl), (-hw(p1), p1), (-hw(p1) - reach, p1),
               (-hw(p0) - reach, soffit), (-hw(p0), p0), (-hw(0), 0)]
    body = right + left_up
    lit = [(0, 0), (hw(0), 0), (hw(H), H), (0, yl + (H - yl) * hw(yl) / (hw(yl) + hw(H)))]
    platform = [(-hw(p0) - reach, soffit), (-hw(p0), p0), (hw(p0), p0), (hw(p1), p1), (-hw(p1) - reach, p1)]
    return H, [("body", body), ("lit", lit), ("mid", platform)]


def bank_of_china_tower():
    H = 367.4
    # Face-on elevation of the 52 m square shaft, which is split along its diagonals into four
    # triangular quarters. They end one after another at 45-degree glass roofs rising to the
    # central column (front quarter, then right, then back), so only the left quarter reaches the
    # 315 m apex with its twin masts. The front face's X-bracing reads as a column of diamonds; the
    # roof of the front quarter closes the top diamond. Above it the exposed diagonal faces facing
    # front-right are lit; the right quarter's face, turned away, stays dark.
    w, s = 26.0, 27.0                       # half width; rise of each roof from edge to centre
    h1, h2, h3, h4 = 108.0, 162.0, 216.0, 288.0   # eaves of the front, right, back and left quarters

    def roof(x):                            # the top quarter's roof line, rising to the apex at x=0
        return h4 + s * (x + w) / w

    body = [(-w, 0), (w, 0), (w, h3), (0, h3 + s), (0, h4 + s),
            (-0.8, H), (-2.0, H), (-3.2, roof(-3.2)),                 # first mast, at the apex
            (-6.0, roof(-6.0)), (-7.0, 361.0), (-8.2, 361.0), (-9.2, roof(-9.2)),     # second mast
            (-w, h4)]
    lit = [(-w, h1), (0, h1 + s), (0, h2 + s), (w, h2), (w, h3), (0, h3 + s), (0, h4 + s), (-w, h4)]
    base = [(-w, 0), (w, 0), (0, 27)]
    d1 = [(0, 27), (w, 54), (0, 81), (-w, 54)]
    d2 = [(0, 81), (w, h1), (0, h1 + s), (-w, h1)]
    return H, [("body", body), ("lit", lit), ("mid", base), ("mid", d1), ("mid", d2)]


def bank_of_america_tower():
    H = 365.8
    # Seen from the east (Bryant Park, across Sixth Avenue): a faceted glass crystal. The broad
    # shaft splits near the top into two shards with slanted tops: a lower shoulder on the right
    # and the taller shard, whose folded planes taper to the 288 m peak; the slender spire
    # rises from that peak, off the axis.
    sx = -5.0                                            # spire axis
    body = [(31, 0), (31, 222), (11, 250),               # shoulder, its top sloping in
            (11, 256), (5, 274), (sx + 3.5, 288),        # the main shard's folded top
            (sx + 2.0, 300), (sx + 1.2, 340), (sx + 0.5, H),   # spire
            (sx - 0.5, H), (sx - 1.2, 340), (sx - 2.0, 300),
            (sx - 3.5, 288), (-19, 279), (-29, 254),     # slanted roof and chamfer
            (-30, 120), (-31, 0)]                        # the far face leans in slightly
    # the sunlit shoulder face, and a fold that widens upward and converges on the peak
    shoulder = [(11, 0), (31, 0), (31, 222), (11, 250)]
    fold = [(6, 0), (11, 0), (11, 256), (5, 274), (sx + 3.5, 288), (-1, 256)]
    return H, [("body", body), ("lit", shoulder), ("mid", fold)]


def st_regis_chicago():
    H = 362.9
    # Studio Gang's three interlocked stems of 71, 101 and 47 storeys, tallest in the middle, seen
    # on the long side from the river. Each stem is a stack of frustums that alternately narrow and
    # widen, so the edges ripple and the stems' frustums interlock; the sunlit right half of each
    # stem follows the ripple, which keeps the three stems distinct at map scale.

    def edge(cx, hw, a, joints):
        # half-width at the joints alternates wide / narrow, starting wide at the ground
        ws = [hw + (a if i % 2 == 0 else -a) for i in range(len(joints))]

        def f(y):
            if y <= joints[0]: return ws[0]
            for (y0, w0), (y1, w1) in zip(zip(joints, ws), zip(joints[1:], ws[1:])):
                if y <= y1:
                    return w0 + (w1 - w0) * (y - y0) / (y1 - y0)
            return ws[-1]
        return f

    jC = [0, 44, 90, 136, 181, 226, 272, 318, H]          # middle stem, 101 storeys
    jL = [0, 26, 70, 116, 162, 210, 258.0]                # west stem, 71 storeys
    jR = [0, 36, 82, 128, 172.0]                          # east stem, 47 storeys
    cL, cR, a = -23.0, 23.0, 1.5
    fC = edge(0, 12.0, a, jC)
    fL = edge(cL, 11.0, a, jL)
    fR = edge(cR, 11.0, a, jR)

    left_outer = [(cL - fL(y), y) for y in jL]            # bottom to top
    right_outer = [(cR + fR(y), y) for y in jR]
    c_left = [(-fC(y), y) for y in [jL[-1]] + [y for y in jC if y > jL[-1]]]
    c_right = [(fC(y), y) for y in [jR[-1]] + [y for y in jC if y > jR[-1]]]
    body = left_outer + c_left + list(reversed(c_right)) + list(reversed(right_outer))

    def comb(L, R, joints):
        # the sunlit right half of a stem, between its rippling edges
        pts = [(R(y), y) for y in joints]
        for k in range(len(joints) - 2, -1, -1):
            y0, y1 = joints[k], joints[k + 1]
            t = 0.5
            pts += [(L(y1) + t * (R(y1) - L(y1)), y1), (L(y0) + t * (R(y0) - L(y0)), y0)]
        return pts

    litC = comb(lambda y: -fC(y), fC, jC)
    litL = comb(lambda y: cL - fL(y), lambda y: -fC(y), jL)
    litR = comb(fC, lambda y: cR + fR(y), jR)
    return H, [("body", body), ("lit", litL), ("lit", litC), ("lit", litR)]


def city_tower_one():
    H = 362.8
    # A slim residential slab on Sheikh Zayed Road (about 38 m across its broad face), rising
    # straight to a short setback at the top, then a crown that steps in to a slim finial. The
    # face's right half is sunlit; the corner piers stay dark, and the crown's sunlit side is
    # cut apart from the shaft so the setback reads.
    right = [(19, 0), (19, 318), (15.5, 318), (15.5, 344), (9.5, 344), (9.5, 352), (2.4, 352), (1.5, H)]
    body = mirror(right)
    lit = [(0, 0), (14.5, 0), (14.5, 314), (0, 314)]
    crown = [(0, 320), (12.5, 320), (12.5, 342), (0, 342)]
    return H, [("body", body), ("lit", lit), ("lit", crown)]


def almas_tower():
    H = 360.0
    # Broad face: two interlocking oval shafts of different heights meet at a crease on the
    # axis. Each is cut off by a sloping roof screen rising to the right, so the top reads as a
    # stagger: the shorter left oval tops out near 310 m and the taller right one climbs to its
    # point at 360 m. The right oval's face is sunlit; the lit-facing half of the left oval is mid.
    W = 29.0          # half the broad width
    e = 7.0           # each oval reaches this far past the axis
    body = [(-W, 0), (W, 0), (W, H), (-e, 334), (-e, 306), (-W, 290)]
    lit = [(0, 0), (W, 0), (W, H), (0, 340)]
    roof = lambda x: 290 + (x + W) * 16 / (W - e)     # the shorter oval's sloping roof
    mid = [(-12, 0), (0, 0), (0, roof(0)), (-12, roof(-12))]
    return H, [("body", body), ("mid", mid), ("lit", lit)]


def ping_an_jinan():
    H = 360.0
    # A square shaft with chamfered corners that tapers gently as it rises; near the top the
    # faces fold inward in two stages into a faceted crown that ends in a short finial.
    # The face between the dark corner chamfers is lit on its right half.
    f = smooth([(0, 27), (120, 26), (240, 24.5), (318, 23)])
    crown = [(23, 318), (18.5, 334), (15.5, 334), (12.5, 346), (8.5, 346), (5.0, 354), (2.6, 354), (1.4, H)]
    body = mirror(curve(f, 0, 318, 12) + crown)
    face = curve(lambda y: 0.62 * f(y), 0, 318, 12)
    lit = [(0, 0)] + face + [(11.0, 334), (9.5, 334), (7.5, 346), (5.0, 346), (2.8, 354), (0, 354)]
    return H, [("body", body), ("lit", lit)]


def huiyun_center():
    H = 359.2
    # The first supertall of the Shenzhen Bay "Cloud City" headquarters district: a slim,
    # near-square glass shaft that swells very slightly, then draws in on soft curved shoulders
    # into the crown, whose fins run on past the top floor to the parapet. Light from the right:
    # the face between the dark chamfered corners is lit, the curved crown face half lit.
    f = smooth([(0, 26.5), (120, 27.2), (250, 26.4), (300, 24.8), (330, 21.5), (350, 16.5), (H, 13.5)])
    shaft = curve(f, 0, H, 30)
    body = mirror(shaft)
    g = lambda y: 0.62 * f(y)
    face = [(0, 0)] + curve(g, 0, 300, 15) + [(0, 300)]
    crown = [(0, 304)] + curve(g, 304, H, 8) + [(0, H)]
    return H, [("body", body), ("lit", face), ("mid", crown)]


def hanking_center():
    H = 358.9
    # Morphosis's offset core: the solid circulation core stands outside the office block as a
    # slim tower of its own (left, dark) and runs up to the top; the column-free glass block
    # beside it ends in a roof that slopes down away from the core. The block's steel
    # mega-braces cross the sunlit face in two tall X's.
    cl, cr = -31.0, -15.0                     # core tower, its edges
    xr = 29.0                                 # office block's right edge
    yl, yr = 349.0, 324.0                     # sloped roof: high at the core, low at the far edge
    body = [(cl, 0), (xr, 0), (xr, yr), (cr, yl), (cr, H), (cl, H)]
    face = [(cr, 0), (xr, 0), (xr, yr), (cr, yl)]

    def clip(poly, quad):                     # Sutherland-Hodgman against a convex quad (ccw)
        out = poly
        for (ax, ay), (bx, by) in zip(quad, quad[1:] + quad[:1]):
            src, out = out, []
            side = lambda p: (bx - ax) * (p[1] - ay) - (by - ay) * (p[0] - ax)
            for p, q in zip(src, src[1:] + src[:1]):
                sp, sq = side(p), side(q)
                if sp >= 0: out.append(p)
                if sp * sq < 0:
                    t = sp / (sp - sq)
                    out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
        return out

    def band(p, q, quad, w=9.0):              # a brace: corner-to-corner strip w metres across
        strip = [(p[0] - w / 2, p[1]), (p[0] + w / 2, p[1]), (q[0] + w / 2, q[1]), (q[0] - w / 2, q[1])]
        return clip(strip, quad)

    ym_l, ym_r = 172.0, 162.0                 # the two braced modules meet mid-height
    lower = [(cr, 0), (xr, 0), (xr, ym_r), (cr, ym_l)]
    upper = [(cr, ym_l), (xr, ym_r), (xr, yr), (cr, yl)]
    braces = []
    for (bl, br, tr, tl) in (lower, upper):   # clipped to the whole face, so the X's join cleanly
        braces += [band(bl, tr, face), band(br, tl, face)]
    return H, [("body", body), ("lit", face)] + [("mid", b) for b in braces]


def gevora_hotel():
    H = 356.2
    # A slim gold slab on Sheikh Zayed Road, seen from the road: a plain straight shaft whose
    # top steps in once and then tapers in a tall pointed crown to a short needle.
    right = [(19, 0), (19, 300), (15.5, 300), (15.5, 314),     # shaft, one setback band
             (12, 326), (7.5, 336), (4, 344), (1.8, 347),      # pointed crown
             (1.0, H)]                                          # needle
    body = mirror(right)
    # the central bay's sunlit half; the corner piers stay dark; the crown's right face is lit
    lit = [(0, 0), (14, 0), (14, 300), (0, 300)]
    crown = [(0, 314), (11, 314), (11, 326), (6.5, 336), (3.2, 343), (0, 345)]
    return H, [("body", body), ("lit", lit), ("mid", crown)]


def il_primo():
    H = 356.0
    # A slender, square-plan residential slab of full-floor homes: a plain shaft about 40 m
    # wide that steps in near the top for the penthouse floors, capped by a narrower
    # screen-walled crown that hides the plant and carries the roofline up to 356 m.
    right = [(20, 0), (20, 314), (16, 314), (16, 334), (12, 334), (12, H)]
    body = mirror(right)
    # light from the right: the right half of the shaft, then the penthouse tier and the crown
    # each cut apart so the steps read
    lit = [(0, 0), (20, 0), (20, 314), (0, 314)]
    tier = [(0, 317), (16, 317), (16, 334), (0, 334)]
    crown = [(0, 337), (12, 337), (12, H), (0, H)]
    return H, [("body", body), ("lit", lit), ("lit", tier), ("mid", crown)]


def galaxy_yabao_1():
    H = 356.0
    # A slim square-plan glass shaft (about 50 m across) that swells very slightly at mid-height,
    # then curves in over the top floors to a narrower crown screen whose fins rise to 356 m.
    # The rounded corners stay dark; the face to the right of the axis catches the light.
    f = smooth([(0, 24.5), (140, 25.5), (245, 25), (295, 23), (322, 19.5), (336, 16)])
    shaft = curve(f, 0, 336, 24)
    crown = [(14, 336), (12, H)]
    body = mirror(shaft + crown)
    face = curve(lambda y: f(y) - 7.0, 0, 336, 24)
    lit = [(0, 0)] + face + [(0, 336)]
    screen = [(0, 336), (14, 336), (12, H), (0, H)]
    return H, [("body", body), ("lit", lit), ("mid", screen)]


def jw_marriott_marquis_1():
    H = 355.4
    # A slender square hotel shaft clad in vertical ribs (the date-palm trunk), its stepped
    # corners reading as a darker band up each edge; at the top the floors step back in tiers
    # into a stepped pyramid crown ending in a short pinnacle.
    hw = 19.0
    tiers = [(0, hw), (300, 15.0), (318, 11.0), (332, 7.0), (343, None)]
    pin = [(3.0, 343), (1.0, H)]
    right = steps(tiers) + pin
    body = mirror(right)
    band = 5.0                                           # the notched corner, turned partly to the light
    lit_face = [(0, 0), (hw - band, 0), (hw - band, 300), (0, 300)]
    corner = [(hw - band, 0), (hw, 0), (hw, 300), (hw - band, 300)]
    lit_crown = [(0, 300)] + steps(tiers[1:]) + [(1.8, 343), (0, 343)]
    return H, [("body", body), ("lit", lit_face), ("mid", corner), ("lit", lit_crown)]


def emirates_tower_one():
    H = 354.6
    # Seen at a corner of the triangular plan: the shaded left face and the sunlit right face meet
    # at the front edge. The top is sliced off by one steep plane rising to the right-hand corner
    # (the roof shows as a mid-tone wedge), and that sharp corner runs on up into the needle spire.
    w, lo, pk = 23.5, 240.0, 312.0

    def slope(x):                       # the sloping roof's back edge, seen as the skyline
        return lo + (x + w) / (2 * w) * (pk - lo)

    xs = w - 3.0                        # spire axis, just inside the high corner
    body = [(-w, 0), (w, 0), (w, pk), (xs + 1.5, 330), (xs + 0.7, H), (xs - 0.7, H),
            (xs - 1.5, 330), (xs - 2.4, slope(xs - 2.4)), (-w, lo)]
    lit = [(0, 0), (w, 0), (w, pk), (0, lo)]
    roof = [(-w, lo), (0, lo), (w, pk)]
    return H, [("body", body), ("lit", lit), ("mid", roof)]


def raffles_chongqing_t4n():
    H = 354.5
    # One of Safdie's two tall "sail" towers at the prow of Chaotianmen, seen on its broad face:
    # the inner (left) edge rises straight while the outer face bows out as it climbs, like a sail
    # filling with wind, so the slab is wider at its flat-cut roof than at its foot. The bowed outer
    # face is sunlit and widens as it rises; a strip where the facade turns sits in half light.
    xl = -21.0
    rf = smooth([(0, 21.0), (90, 22.0), (180, 24.5), (270, 28.0), (330, 30.6), (H, 31.5)])
    right = curve(rf, 0, H, 24)
    body = [(xl, 0)] + right + [(xl, H)]
    lit = [(1.5, 0)] + right + [(1.5, H)]
    mid = [(-5.0, 0), (1.5, 0), (1.5, H), (-5.0, H)]
    return H, [("body", body), ("mid", mid), ("lit", lit)]


def oko_residential():
    H = 354.2
    # OKO's taller (south) tower, face-on: a straight, slender square glass prism whose corners are
    # notched for the full height. At the top the notches deepen, so the crown over the top floors
    # steps in twice to the flat roof. The corner notches stay dark and the face between them is
    # lit on its sunlit (right) half; the stepped crown screens are a half-tone.
    hw, f, c1, c2 = 22.0, 17.0, 17.0, 11.5     # shaft, face between the notches, crown steps
    y1, y2 = 333.0, 344.0
    body = mirror([(hw, 0), (hw, y1), (c1, y1), (c1, y2), (c2, y2), (c2, H)])
    face = [(0, 0), (f, 0), (f, y1), (0, y1)]
    crown = [(0, y1), (c1, y1), (c1, y2), (c2, y2), (c2, H), (0, H)]
    return H, [("body", body), ("lit", face), ("mid", crown)]


def cbrt_istanbul():
    H = 353.9
    # A slim, gently tapering prism of offices; above the top floor the facade fins run on and
    # fold into a tall faceted crown, its sunlit facet rising higher on the right, that ends in
    # a slender spire.
    f = smooth([(0, 26), (150, 25), (272, 23)])
    shaft = curve(f, 0, 272, 10)
    w = f(272)
    right = shaft + [(w, 300), (12, 326), (4.5, 336), (1.6, 338), (1.0, H)]
    left = [(-1.0, H), (-1.6, 338), (-4.5, 334), (-13, 312), (-w, 272)]
    body = right + left + [(-x, y) for x, y in reversed(shaft[:-1])]
    # the right face is lit, the crown's right facet fully, the left crown facet half-turned
    face = [(0.2 * x, y) for x, y in shaft]
    lit = face + list(reversed(shaft))
    crown_lit = [(0.2 * w, 272), (w, 272), (w, 300), (12, 326), (4.5, 336), (0.8, 336)]
    crown_mid = [(-w, 272), (0.2 * w, 272), (0.8, 336), (-4.5, 334), (-13, 312)]
    return H, [("body", body), ("lit", lit), ("lit", crown_lit), ("mid", crown_mid)]


def the_torch():
    H = 352.0
    # A slim slab on the Marina: the straight shaft steps in near the top, and the "torch"
    # crown, a tall pointed lantern of fins like a stylised flame, rises off the roof into a
    # short spire.
    flame = smooth([(316, 9.5), (327, 8.8), (337, 6.0), (346, 1.8)])
    crown = curve(flame, 316, 346, 12)
    right = [(17, 0), (17, 294), (12.5, 294), (12.5, 310), (9.5, 310)] + crown + [(1.0, H)]
    body = mirror(right)
    # light from the right: the right half of the shaft and of the step, cut apart so the
    # setback reads, and the sunlit side of the crown
    lit = [(0, 0), (17, 0), (17, 294), (0, 294)]
    t1 = [(0, 298), (12.5, 296), (12.5, 310), (0, 310)]
    fl = [(0, 316)] + curve(flame, 316, 344, 12) + [(0, 344)]
    return H, [("body", body), ("lit", lit), ("lit", t1), ("mid", fl)]


def forum_66_t1():
    H = 350.6
    # KPF's "lantern": a slim square shaft that tapers gently as it rises, its corners notched
    # back, then swells out again into the glowing lantern crown, which closes in to a flat roof.
    f = smooth([(0, 25.5), (150, 24.0), (290, 21.8), (300, 21.5)])
    g = smooth([(304, 21.5), (318, 24.0), (334, 24.0), (346, 21.5), (350.6, 20.5)])
    shaft = curve(f, 0, 300, 12)
    neck = [(20.0, 300), (20.0, 304)]                  # recessed band under the lantern
    crown = curve(g, 304, H, 12)
    body = mirror(shaft + neck + crown)
    # the notched corners stay dark; the face between them is lit on its sunny half
    face = curve(lambda y: f(y) - 4.5, 0, 300, 12)
    lit = [(0, 0)] + face + [(0, 300)]
    lantern = [(0, 306)] + curve(lambda y: g(y) - 4.5, 306, 348, 12) + [(0, 348)]
    return H, [("body", body), ("lit", lit), ("mid", lantern)]


def the_pinnacle_gz():
    H = 350.3
    # A slim square office shaft (about 46 m a side) clad in vertical white ribs. Its corner piers
    # run straight up to the roof and then lean in, the ribs gathering into the tall pointed
    # crown that names the tower, finished with a short needle.
    hw, roof = 23.0, 290.0
    right = [(hw, 0), (hw, roof), (20.5, 298), (14.0, 316), (8.0, 331), (3.6, 342), (1.4, 344.5), (0.9, H)]
    body = mirror(right)
    # the face between the corner piers catches the light, the piers stay dark; above a dark
    # roof band the crown's ribs converge, their sunlit half a separate facet
    face = [(0, 0), (16.0, 0), (16.0, roof), (0, roof)]
    crown = [(0, roof + 7), (16.0, roof + 7), (10.0, 315), (5.0, 330), (1.4, 340), (0, 341)]
    return H, [("body", body), ("lit", face), ("mid", crown)]


def glory_xian_ifc():
    H = 350.0
    # Xi'an's tallest, on Jinye Road in the Hi-tech Zone, seen on a broad face: a square glass
    # shaft about 54 m across that stands nearly straight, then draws in on a soft curve over its
    # top floors. The facade's vertical fins run on past the roof as a tapering screen crown. The
    # chamfered corners stay dark; the face between them is lit on its right half, and the crown
    # screen is a face turned partly to the light.
    roof = 328.0
    f = smooth([(0, 27), (150, 26.5), (250, 25.2), (300, 23.2), (roof, 21.0)])
    shaft = curve(f, 0, roof, 20)
    crown = [(19.8, 336), (18.2, 344), (16.8, H)]
    body = mirror(shaft + crown)
    face = curve(lambda y: f(y) - 6.5, 0, roof, 20)
    lit = [(0, 0)] + face + [(0, roof)]
    screen = [(0, roof), (f(roof) - 6.5, roof), (13.3, 336), (11.7, 344), (10.3, H), (0, H)]
    return H, [("body", body), ("lit", lit), ("mid", screen)]


def spring_city_66():
    H = 349.0
    # A slim, softly tapering square shaft of vertical fins; above the top office floors the
    # faces curve in together into a tall sculpted crown that closes to a pointed tip. The
    # corner stays dark and the face to its right is sunlit; the crown's facets, folding into
    # the point, are a shade darker so the crown reads apart from the shaft.
    f = smooth([(0, 25.5), (120, 25), (230, 23.6), (290, 21.8)])
    shaft = curve(f, 0, 290, 14)
    crown = [(20.8, 300), (18.8, 311), (15.8, 322), (12.0, 332), (7.6, 340), (3.4, 346), (0.8, H)]
    body = mirror(shaft + crown)
    k = 0.4
    face = curve(lambda y: k * f(y), 0, 290, 14)
    lit = shaft + list(reversed(face))
    # the crown's sunlit facet, its inner edge running from the face line up into the tip
    inner = [(k * f(290), 290), (7.6, 306), (6.2, 320), (4.6, 332), (2.7, 341), (0.9, 346.5)]
    top = [(f(290), 290)] + crown + list(reversed(inner))
    return H, [("body", body), ("lit", lit), ("mid", top)]


def tuntex_85_sky():
    H = 347.5
    # Shaped like the character 高 ("tall"): two legs rise some 35 storeys with terraced
    # shoulders and join under the central tower, leaving a tall open portal above the low
    # block between them (sky shows through it); the central shaft ends in a stepped crown
    # and pinnacle.
    right = [
        (48, 0), (48, 104), (40, 104), (40, 120), (32, 120), (32, 136),   # leg and its terraces
        (24, 136), (24, 282),                                              # central shaft
        (19.5, 282), (19.5, 298), (14.5, 298), (14.5, 311),                # stepped crown
        (9.5, 311), (9.5, 321), (5.0, 321), (1.4, H),                      # pinnacle
    ]
    body = mirror(right)
    lit = [(0, 0)] + right[:-1] + [(0, 321)]
    portal = [(-15, 40), (15, 40), (15, 128), (-15, 128)]
    return H, [("body", body), ("lit", lit), ("hi", portal)]


def aon_center_chicago():
    H = 346.3
    # A pure square tube, 59.1 m (194 ft) a side and nearly six times as tall, drawn face on with
    # its flat roof. The sunlit half of the face is ribbed by the white chevron columns that run
    # unbroken from the plaza to the roof; the notched corner stays in shadow, and the louvred
    # mechanical floors under the roof make a slightly darker band.
    w = 29.55                                   # half the plan width
    body = mirror([(w, 0), (w, H)])
    notch = 3.0                                 # the re-entrant corner, in shadow
    band = 334.0                                # louvred top floors
    face = [(0, 0), (w - notch, 0), (w - notch, band), (0, band)]
    top = [(0, band), (w - notch, band), (w - notch, H), (0, H)]
    return H, [("body", body), ("lit", face), ("mid", top)]


def the_center_hk():
    H = 346.0
    # Face-on: the square shaft with its notched (re-entrant) corners reading as dark strips at
    # each edge, then the ziggurat crown that steps in five times (the tiers its neon outlines
    # at night), and the tall mast from the roof at about 292 m.
    hw, notch = 23.0, 6.0
    tiers = [(0, hw), (236, 19.5), (248, 16.0), (259, 12.5), (270, 9.5), (281, 6.5), (292, None)]
    mast = [(3.0, 292), (3.0, 300), (2.0, 300), (1.0, H)]
    body = mirror(steps(tiers) + mast)
    # the right half of each tier's front face is sunlit, short of the recessed corner notch
    face = steps([(y, w - notch if w else None) for y, w in tiers[:4]] + [(270, 9.5 - 3.5), (281, 6.5 - 3.0), (292, None)])
    lit = [(0, 0)] + face + [(0, 292)]
    return H, [("body", body), ("lit", lit)]


def neva_tower_2():
    H = 345.0
    # The taller of the two Neva Towers: a straight, slender glass shaft of roughly 46 m, its
    # pleated "crystal" facade folding inward over the top floors into a faceted, clipped crown
    # that ends in a flat parapet. The sunlit half of the shaft is lit; the crown's inward-folding
    # facet, turned partly to the light, is mid.
    hw, yc = 23.0, 312.0
    right = [(hw, 0), (hw, yc), (17.5, 330), (12.5, 341), (12.5, H)]
    body = mirror(right)
    shaft_lit = [(0, 0), (hw, 0), (hw, yc), (0, yc)]
    crown_mid = [(0, yc), (hw, yc), (17.5, 330), (12.5, 341), (12.5, H), (0, H)]
    return H, [("body", body), ("lit", shaft_lit), ("mid", crown_mid)]


def xiamen_cross_strait():
    H = 343.9
    # Xiamen International Centre on Lujiang Road: a slim square glass shaft with recessed
    # corners and a faint taper, whose faces curve inward at the top into a tall, narrowing
    # glass crown that ends in a small flat tip. The recessed corners stay dark; the face to
    # the right of the axis is lit, and the crown's sunlit facet is a half tone.
    f = smooth([(0, 25), (120, 24.4), (240, 23.2), (300, 22)])
    crown = smooth([(300, 22), (318, 19.5), (332, 14), (340, 8.5), (343.9, 4.5)])
    shaft = curve(f, 0, 300, 12) + curve(crown, 300, H, 12)[1:]
    body = mirror(shaft)
    face = curve(lambda y: f(y) - 6.5, 0, 300, 12)
    lit = [(0, 0)] + face + [(0, 300)]
    crown_mid = [(0, 304)] + curve(lambda y: crown(y) - 3.5, 304, 338, 8) + [(0, 338)]
    return H, [("body", body), ("lit", lit), ("mid", crown_mid)]


def north_michigan_875():
    H = 343.7
    # The former John Hancock Center, broad face: a dark, flat-topped obelisk tapering evenly from
    # 81 m wide at the plaza to 49 m at the roof, braced by five stacked X's (each about 18
    # floors) that run corner to corner. The X's are left dark between the faces they frame; the
    # right half of each face catches the light, the left half is in half shade.
    def w(y):                                         # half-width of the broad face
        return 40.4 - (40.4 - 24.4) * y / H

    def inset(poly, d):                               # shrink a convex CCW polygon by d
        n = len(poly)
        lines = []
        for i in range(n):
            (x0, y0), (x1, y1) = poly[i], poly[(i + 1) % n]
            L = math.hypot(x1 - x0, y1 - y0)
            nx, ny = -(y1 - y0) / L, (x1 - x0) / L    # inward normal for CCW
            lines.append(((x0 + nx * d, y0 + ny * d), (x1 - x0, y1 - y0)))
        out = []
        for i in range(n):
            (p, r), (q, s) = lines[i - 1], lines[i]
            den = r[0] * s[1] - r[1] * s[0]
            t = ((q[0] - p[0]) * s[1] - (q[1] - p[1]) * s[0]) / den
            out.append((p[0] + t * r[0], p[1] + t * r[1]))
        return out

    def clip(poly, side):                             # keep the part with side * x >= 0
        out = []
        for i in range(len(poly)):
            a, b = poly[i - 1], poly[i]
            ina, inb = side * a[0] >= 0, side * b[0] >= 0
            if ina != inb:
                t = a[0] / (a[0] - b[0])
                out.append((0.0, a[1] + t * (b[1] - a[1])))
            if inb:
                out.append(b)
        return out

    body = mirror([(w(0), 0), (w(H), H)])
    shapes = [("body", body)]
    y_lo, y_hi, n = 8.0, 333.0, 5                    # lowest and highest ties; five X's
    m, g = 2.0, 3.0                                   # corner column margin; half-width of a brace
    hb = (y_hi - y_lo) / n
    for k in range(n):
        y0, y1 = y_lo + k * hb, y_lo + (k + 1) * hb
        a, b = w(y0) - m, w(y1) - m
        yc = y0 + (y1 - y0) * a / (a + b)             # where the diagonals cross
        tris = [[(-a, y0), (a, y0), (0, yc)],         # bottom
                [(a, y0), (b, y1), (0, yc)],          # right
                [(b, y1), (-b, y1), (0, yc)],         # top
                [(-b, y1), (-a, y0), (0, yc)]]        # left
        for tri in tris:
            p = inset(tri, g)
            for side, tone in ((1, "lit"), (-1, "mid")):
                q = clip(p, side)
                if len(q) >= 3 and max(abs(x) for x, _ in q) > 0.5:
                    shapes.append((tone, q))
    return H, shapes


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
    (117, "TAIPEI 101", taipei_101),
    (131, "Shanghai World Financial Center", swfc_shanghai),
    (137, "International Commerce Centre", icc_hk),
    (33983, "Wuhan Greenland Center", wuhan_greenland),
    (14269, "Central Park Tower", central_park_tower),
    (12575, "Lakhta Center", lakhta_center),
    (18192, "Vincom Landmark 81", landmark_81),
    (24971, "The Exchange 106", exchange_106),
    (13144, "Changsha IFS Tower T1", changsha_ifs_t1),
    (149, "Petronas Twin Tower 1", petronas_tower_1),
    (150, "Petronas Twin Tower 2", petronas_tower_1),
    (165, "Zifeng Tower", zifeng_tower),
    (196, "Suzhou IFS", suzhou_ifs),
    (8823, "Wuhan Tower", wuhan_tower),
    (169, "Willis Tower", willis_tower),
    (173, "KK100", kk100),
    (174, "Guangzhou International Finance Center", guangzhou_ifc),
    (14320, "111 West 57th Street", steinway_111w57),
    (15833, "One Vanderbilt Avenue", one_vanderbilt),
    (13227, "432 Park Avenue", park_432),
    (207, "Marina 101", marina_101),
    (203, "Trump International Hotel & Tower", trump_chicago),
    (34450, "JPMorganChase Tower", jpmorganchase_tower),
    (14196, "Minying International Trade Center T2", minying_itc_t2),
    (189, "Jin Mao Tower", jin_mao_tower),
    (24137, "Zijin Financial Building", zijin_financial),
    (206, "Princess Tower", princess_tower),
    (208, "Al Hamra Tower", al_hamra_tower),
    (205, "Two International Finance Centre", two_ifc),
    (108, "LCT The Sharp Landmark Tower", lct_landmark),
    (13153, "Ningbo Center Tower 1", ningbo_center),
    (33180, "Guangxi China Resources Tower", guangxi_china_resources),
    (33699, "Guiyang International Financial Center T1", guiyang_ifc_t1),
    (34420, "Iconic Tower", iconic_tower_cairo),
    (42765, "China Merchants Bank Global Headquarters Main Tower", china_merchants_bank_hq),
    (14589, "China Resources Tower", china_resources_tower),
    (247, "23 Marina", marina_23),
    (242, "CITIC Plaza", citic_plaza),
    (22997, "CITYMARK CENTRE", citymark_centre),
    (16001, "Shum Yip Upperhills Tower 1", upperhills_t1),
    (13325, "30 Hudson Yards", hudson_yards_30),
    (8774, "PIF Tower", pif_tower),
    (258, "Shun Hing Square", shun_hing_square),
    (249, "Eton Place Dalian Tower 1", eton_place_dalian),
    (39449, "Autograph Tower", autograph_tower),
    (10698, "Nanning Logan Century 1", nanning_logan_1),
    (259, "Burj Mohammed Bin Rashid", burj_mohammed_bin_rashid),
    (261, "Empire State Building", empire_state),
    (263, "Elite Residence", elite_residence),
    (9591, "1 Corporate Avenue", corporate_avenue_1),
    (14198, "Dabaihui Plaza", dabaihui_plaza),
    (30032, "Guangdong Business Center", guangdong_business_center),
    (277, "Central Plaza", central_plaza_hk),
    (118, "Federation Tower", federation_tower),
    (34561, "Ciel Tower", ciel_tower),
    (8980, "Dalian International Trade Center", dalian_itc),
    (14606, "The Address Boulevard", address_boulevard),
    (354, "Three International Trade Center Tower B", three_itc_b),
    (15639, "Qingdao Hai Tian Center", qingdao_haitian),
    (11463, "Golden Eagle Tiandi Tower A", golden_eagle_tiandi_a),
    (287, "Bank of China Tower", bank_of_china_tower),
    (291, "Bank of America Tower", bank_of_america_tower),
    (17137, "The St. Regis Chicago", st_regis_chicago),
    (35099, "City Tower One", city_tower_one),
    (298, "Almas Tower", almas_tower),
    (32086, "Ping An Finance Center", ping_an_jinan),
    (29371, "Huiyun Center", huiyun_center),
    (15741, "Hanking Center", hanking_center),
    (348, "Gevora Hotel", gevora_hotel),
    (26116, "Il Primo Tower", il_primo),
    (27941, "Galaxy Yabao Twin Tower 1", galaxy_yabao_1),
    (27942, "Galaxy Yabao Twin Tower 2", galaxy_yabao_1),
    (237, "JW Marriott Marquis Hotel Dubai Tower 1", jw_marriott_marquis_1),
    (238, "JW Marriott Marquis Hotel Dubai Tower 2", jw_marriott_marquis_1),
    (311, "Emirates Tower One", emirates_tower_one),
    (13610, "Raffles City Chongqing T3N", raffles_chongqing_t4n),
    (13611, "Raffles City Chongqing T4N", raffles_chongqing_t4n),
    (363, "OKO - Residential Tower", oko_residential),
    (41146, "Central Bank of the Republic of Türkiye", cbrt_istanbul),
    (344, "The Torch", the_torch),
    (414, "Forum 66 Tower 1", forum_66_t1),
    (306, "The Pinnacle", the_pinnacle_gz),
    (18932, "Glory・Xi’an International Financial Center", glory_xian_ifc),
    (14797, "Spring City 66", spring_city_66),
    (338, "85 Sky Tower", tuntex_85_sky),
    (339, "Aon Center", aon_center_chicago),
    (343, "The Center", the_center_hk),
    (233, "NEVA TOWERS 2", neva_tower_2),
    (12778, "Xiamen Cross Strait Financial Centre", xiamen_cross_strait),
    (345, "875 North Michigan Avenue", north_michigan_875),
]


# ---------------------------------------------------------------------------------------- output

def svg_for(tid, height, shapes):
    xs = [x for _, pts in shapes for x, _ in pts]
    hw = max(-min(xs), max(xs))
    W, Hh = 2 * (hw + PAD), height + 2 * PAD

    def d(pts):
        return "M" + "L".join(f"{x + hw + PAD:.0f},{Hh - PAD - y:.0f}" for x, y in pts) + "Z"
    body = "".join(d(p) for t, p in shapes if t == "body")
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.1f} {Hh:.1f}" width="{W * PX_PER_M:.2f}" height="{Hh * PX_PER_M:.2f}">',
           f'<defs><path id="t{tid}" d="{body}"/></defs>',
           f'<use href="#t{tid}" fill="{TONES["halo"]}" stroke="{TONES["halo"]}" stroke-width="{2 * HALO_PX / PX_PER_M:.0f}" stroke-linejoin="round" opacity="0.92"/>',
           f'<use href="#t{tid}" fill="{TONES["body"]}"/>']
    out += [f'<path d="{d(p)}" fill="{TONES[t]}"/>' for t, p in shapes if t != "body"]
    out.append("</svg>\n")
    return "\n".join(out), W, Hh


def main():
    os.makedirs(OUT, exist_ok=True)
    icons = []
    for tid, name, draw in TOWERS:
        height, shapes = draw()
        svg, W, Hh = svg_for(tid, height, shapes)
        with open(os.path.join(OUT, f"{tid}.svg"), "w") as fh:
            fh.write(svg)
        icons.append({"id": tid, "name": name, "height": height,
                      "w": round(W * PX_PER_M, 2), "h": round(Hh * PX_PER_M, 2), "base": round(PAD * PX_PER_M, 2)})
    with open(os.path.join(OUT, "index.json"), "w") as fh:     # one icon per line
        fh.write('{"pxPerMetre": %s, "icons": [\n%s\n]}\n' % (PX_PER_M, ",\n".join(json.dumps(i) for i in icons)))
    print(f"{len(icons)} icons -> {os.path.relpath(OUT)}")


if __name__ == "__main__":
    main()
