"""Generate a cartoon dirt/soil strip to sit UNDER the grass on the loader pill.
Flat illustrated style to match the existing grass/mower art. Pure PIL."""
import random
from PIL import Image, ImageDraw, ImageFilter

random.seed(7)
W, H = 1200, 150          # wide + short; CSS will keep it thin
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# soil color bands (top lighter topsoil -> deeper brown), matching the pasted dirt
BANDS = [
    (0.00, (181, 130, 74)),   # warm topsoil
    (0.34, (162, 112, 60)),
    (0.62, (138, 92, 47)),
    (1.00, (120, 78, 38)),    # deep soil
]

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def band_color(yt):
    for i in range(len(BANDS) - 1):
        y0, c0 = BANDS[i]; y1, c1 = BANDS[i + 1]
        if y0 <= yt <= y1:
            return lerp(c0, c1, (yt - y0) / (y1 - y0))
    return BANDS[-1][1]

# wavy top edge (where grass meets dirt) so it isn't a hard line
import math
top_edge = [int(10 + 6 * math.sin(x / 55.0) + 4 * math.sin(x / 17.0)) for x in range(W)]

for x in range(W):
    te = top_edge[x]
    for y in range(te, H):
        yt = (y - te) / (H - te)
        d.point((x, y), fill=band_color(yt) + (255,))

# detail drawn on a separate layer, then alpha-composited (so alpha BLENDS,
# instead of ImageDraw punching semi-transparent holes in the base)
detail = Image.new("RGBA", (W, H), (0, 0, 0, 0))
dd = ImageDraw.Draw(detail)

# short broken sediment clumps (darker soil tones only, subtle)
for _ in range(34):
    yy = random.randint(int(H * 0.32), H - 10)
    x0 = random.randint(0, W - 60)
    seg = random.randint(30, 120)
    shade = random.choice([(126, 84, 42), (104, 66, 32), (140, 96, 50)])
    dd.line([(x0, yy), (x0 + seg, yy + random.randint(-3, 3))], fill=shade + (60,), width=random.randint(2, 4))

# little pebbles / dirt specks
for _ in range(120):
    x = random.randint(0, W - 1)
    y = random.randint(int(H * 0.28), H - 6)
    r = random.randint(1, 4)
    dark = random.random() < 0.62
    col = (88, 58, 26) if dark else (196, 150, 92)
    dd.ellipse([x - r, y - r, x + r, y + r], fill=col + (150,))

img.alpha_composite(detail)
img = img.filter(ImageFilter.GaussianBlur(0.5))
img.save("17_dirt_strip.png")
print("saved 17_dirt_strip.png", img.size)
