import os

image_dir = "frontend/public/images/stones"
files = os.listdir(image_dir) if os.path.exists(image_dir) else []
print(f"Total files in {image_dir}: {len(files)}")

hidden_slugs = [
    'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
    'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
    'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
    'sapphire-blue-semi-precious', 'zircon-cubic-white'
]

for s in hidden_slugs:
    matched = [f for f in files if s in f or f.startswith(s.split('-')[0])]
    print(f"{s}: {[f for f in files if s in f]}")

