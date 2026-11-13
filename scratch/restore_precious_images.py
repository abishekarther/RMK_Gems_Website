from PIL import Image
import os, shutil

precious_slugs = [
    'ruby', 'pearl', 'red-coral', 'emerald', 'yellow-sapphire',
    'diamond', 'blue-sapphire', 'hessonite-garnet', 'cats-eye-chrysoberyl'
]

gia_dir = "frontend/public/images/gia"
dist_gia_dir = "frontend/dist/images/gia"
stones_dir = "frontend/public/images/stones"
dist_stones_dir = "frontend/dist/images/stones"

os.makedirs(dist_gia_dir, exist_ok=True)

for slug in precious_slugs:
    png_path = os.path.join(gia_dir, f"{slug}.png")
    dist_png_path = os.path.join(dist_gia_dir, f"{slug}.png")
    
    # Copy PNG to dist/images/gia/
    shutil.copy2(png_path, dist_png_path)
    
    # Convert to 800x800 WebP for stones_dir
    im = Image.open(png_path).convert("RGB")
    webp_path = os.path.join(stones_dir, f"{slug}.webp")
    dist_webp_path = os.path.join(dist_stones_dir, f"{slug}.webp")
    
    im.save(webp_path, "WEBP", quality=88, method=6)
    im.save(dist_webp_path, "WEBP", quality=88, method=6)
    print(f"Updated {slug}: PNG {os.path.getsize(png_path)} bytes, WebP {os.path.getsize(webp_path)} bytes")

print("All 9 precious stones synchronized with old images!")
