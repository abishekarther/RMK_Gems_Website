import os
from PIL import Image

pub_dir = r'c:\RMK_Gems_Website\frontend\public\images\stones'
dist_dir = r'c:\RMK_Gems_Website\frontend\dist\images\stones'

# 1. Restore precious hessonite-garnet.webp from scratch/downloaded/hessonite-garnet.jpg
src_prec_hessonite = r'c:\RMK_Gems_Website\scratch\downloaded\hessonite-garnet.jpg'
if os.path.exists(src_prec_hessonite):
    img = Image.open(src_prec_hessonite)
    for d in [pub_dir, dist_dir]:
        if os.path.exists(d):
            img.save(os.path.join(d, 'hessonite-garnet.webp'), 'WEBP', quality=88, method=6)
    print("Restored precious hessonite-garnet.webp")

# 2. Ensure semi-precious hessonite is saved as hessonite-garnet-semi-precious.webp
semi_hessonite_src = r'c:\RMK_Gems_Website\semiprecious_stones_images\hessonite-garnet.webp'
if os.path.exists(semi_hessonite_src):
    img = Image.open(semi_hessonite_src)
    for d in [pub_dir, dist_dir]:
        if os.path.exists(d):
            img.save(os.path.join(d, 'hessonite-garnet-semi-precious.webp'), 'WEBP', quality=88, method=6)
    print("Saved semi-precious hessonite-garnet-semi-precious.webp")

# 3. Remove duplicate garnet-rose-cut-checkerboard.webp (use garnet-checkerboard.webp)
for d in [pub_dir, dist_dir]:
    p = os.path.join(d, 'garnet-rose-cut-checkerboard.webp')
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed {p}")

# 4. Remove duplicate sapphire-blue-semi-precious.webp (use sapphire-blue.webp)
for d in [pub_dir, dist_dir]:
    p = os.path.join(d, 'sapphire-blue-semi-precious.webp')
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed {p}")

print("Completed.")

