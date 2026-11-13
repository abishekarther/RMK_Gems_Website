import os, sys
from PIL import Image

sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

src_dir = "bgeraser_results (1)"
public_stones_dir = "frontend/public/images/stones"
dist_stones_dir = "frontend/dist/images/stones"
semi_folder = "semiprecious_stones_images"

cats, slides, shop, hours, prec, semi = get_seed_data()
semi_slugs = [s['slug'] for s in semi]

print(f"Processing all {len(semi_slugs)} semi-precious stones from '{src_dir}'...")

processed_count = 0
oversized = []

for slug in semi_slugs:
    src_file = os.path.join(src_dir, f"{slug}.png")
    if not os.path.exists(src_file):
        print(f"ERROR: Missing source file: {src_file}")
        continue
    
    im = Image.open(src_file).convert("RGBA")
    
    # Bounding box of non-transparent pixels
    alpha = im.split()[-1]
    bbox = alpha.getbbox()
    if bbox:
        stone_crop = im.crop(bbox)
    else:
        stone_crop = im
    
    sw, sh = stone_crop.size
    # Fit into 650x650 box inside 800x800 canvas
    target_dim = 650
    scale = target_dim / max(sw, sh)
    nw, nh = int(sw * scale), int(sh * scale)
    scaled = stone_crop.resize((nw, nh), Image.Resampling.LANCZOS)
    
    # Canvas 800x800 white
    canvas = Image.new("RGBA", (800, 800), (255, 255, 255, 255))
    offset = ((800 - nw) // 2, (800 - nh) // 2)
    canvas.paste(scaled, offset, scaled)
    rgb_canvas = canvas.convert("RGB")
    
    # Save WebP to public and dist
    dest_webp = os.path.join(public_stones_dir, f"{slug}.webp")
    dist_webp = os.path.join(dist_stones_dir, f"{slug}.webp")
    
    rgb_canvas.save(dest_webp, "WEBP", quality=88, method=6)
    rgb_canvas.save(dist_webp, "WEBP", quality=88, method=6)
    
    sz = os.path.getsize(dest_webp)
    if sz > 153600:
        oversized.append((slug, sz))
    
    # Also save to semiprecious_stones_images/
    semi_dest_webp = os.path.join(semi_folder, f"{slug}.webp")
    rgb_canvas.save(semi_dest_webp, "WEBP", quality=88, method=6)
    
    processed_count += 1

# Special handling for agate-black-banded: ensure .png also updated
agate_png_src = os.path.join(src_dir, "agate-black-banded.png")
if os.path.exists(agate_png_src):
    # Process 800x800 PNG
    im_agate = Image.open(agate_png_src).convert("RGBA")
    alpha = im_agate.split()[-1]
    bbox = alpha.getbbox()
    stone_crop = im_agate.crop(bbox) if bbox else im_agate
    sw, sh = stone_crop.size
    scale = 650 / max(sw, sh)
    nw, nh = int(sw * scale), int(sh * scale)
    scaled = stone_crop.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (800, 800), (255, 255, 255, 255))
    canvas.paste(scaled, ((800 - nw) // 2, (800 - nh) // 2), scaled)
    
    for d in [public_stones_dir, dist_stones_dir, semi_folder]:
        p = os.path.join(d, "agate-black-banded.png")
        canvas.convert("RGB").save(p, "PNG", optimize=True)

print(f"Successfully processed {processed_count} semi-precious gemstone images!")
if oversized:
    print(f"WARNING: {len(oversized)} images exceed 150 KB:")
    for s, sz in oversized:
        print(f"  {s}: {sz} bytes")
else:
    print("All processed WebP images are strictly under 150 KB!")

