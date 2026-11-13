import os, sys
sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_stones = prec + semi
stones_dir = 'frontend/public/images/stones'
existing = set(os.listdir(stones_dir))

missing = []
for s in all_stones:
    fname = f"{s['slug']}.webp"
    if fname not in existing:
        missing.append((s['slug'], fname))

if missing:
    print(f"Missing images for {len(missing)} stones:")
    for slug, fname in missing:
        print(f"  {slug} -> {fname}")
else:
    print(f"ALL {len(all_stones)} STONES HAVE EXACT MATCHING <slug>.webp FILES ON DISK!")

