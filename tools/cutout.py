import sys
from collections import deque
from PIL import Image

def cutout(src, dst, size=512, thr=110):
    im = Image.open(src).convert("RGB").resize((size, size), Image.LANCZOS)
    w, h = im.size
    px = im.load()
    seen = bytearray(w * h)
    q = deque()
    for x in range(w):
        q.append((x, 0)); q.append((x, h - 1))
    for y in range(h):
        q.append((0, y)); q.append((w - 1, y))
    out = Image.new("RGBA", (w, h))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            op[x, y] = (r, g, b, 255)
    while q:
        x, y = q.popleft()
        i = y * w + x
        if seen[i]:
            continue
        seen[i] = 1
        r, g, b = px[x, y]
        if min(r, g, b) < thr:
            continue
        # color-to-alpha against white
        a = max(255 - r, 255 - g, 255 - b) / 255
        if a <= 0.01:
            op[x, y] = (0, 0, 0, 0)
        else:
            c = lambda v: max(0, min(255, round((v - 255 * (1 - a)) / a)))
            op[x, y] = (c(r), c(g), c(b), round(a * 255))
        for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0 <= nx < w and 0 <= ny < h and not seen[ny*w+nx]:
                q.append((nx, ny))
    out.save(dst)

for src, dst in zip(sys.argv[1::2], sys.argv[2::2]):
    cutout(src, dst)
    print("saved", dst)
