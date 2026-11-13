import os, sys, shutil

src_dir = "bgeraser_results (1)"
public_stones_dir = "frontend/public/images/stones"
dist_stones_dir = "frontend/dist/images/stones"
semi_folder = "semiprecious_stones_images"

# 1. Remove old semi-precious .webp files from public_stones_dir and dist_stones_dir
precious_slugs = {
    'ruby', 'pearl', 'red-coral', 'emerald', 'yellow-sapphire',
    'diamond', 'blue-sapphire', 'hessonite-garnet', 'cats-eye-chrysoberyl'
}

for d in [public_stones_dir, dist_stones_dir, semi_folder]:
    if not os.path.exists(d):
        continue
    for f in os.listdir(d):
        slug = f.replace('.webp', '').replace('.png', '')
        if f.endswith('.webp') and slug not in precious_slugs and f != 'placeholder.webp':
            old_p = os.path.join(d, f)
            os.remove(old_p)
            print(f"Removed old webp: {old_p}")

# 2. Copy all 59 PNG files from bgeraser_results (1) into public_stones_dir, dist_stones_dir, and semi_folder
png_files = [f for f in os.listdir(src_dir) if f.endswith('.png')]
print(f"\nCopying {len(png_files)} PNG files from '{src_dir}'...")

for f in png_files:
    src_path = os.path.join(src_dir, f)
    for d in [public_stones_dir, dist_stones_dir, semi_folder]:
        os.makedirs(d, exist_ok=True)
        dest_path = os.path.join(d, f)
        shutil.copy2(src_path, dest_path)

print(f"Copied all {len(png_files)} PNG files to public, dist, and semiprecious_stones_images!")

