import os
from PIL import Image

stone_dir = 'frontend/public/images/stones'
files = [f for f in os.listdir(stone_dir) if f.endswith('.webp') and f != 'placeholder.webp']

print(f"Checking {len(files)} stone images in {stone_dir}...")
issues = []
for f in sorted(files):
    p = os.path.join(stone_dir, f)
    sz = os.path.getsize(p)
    im = Image.open(p)
    w, h = im.size
    if sz > 153600:
        issues.append(f"{f}: size {sz} > 150KB")
    # print small summary
    # print(f"{f}: {w}x{h}, {sz/1024:.1f} KB")

if issues:
    print("Issues found:")
    for i in issues:
        print(" ", i)
else:
    print(f"All {len(files)} images are under 150 KB!")

