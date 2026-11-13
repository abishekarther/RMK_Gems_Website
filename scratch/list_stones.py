import sys
sys.path.append('.')
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_gems = prec + semi

print(f"Total stones: {len(all_gems)}")
for idx, g in enumerate(all_gems, 1):
    pub = "PUBLISHED" if g.get('is_published', True) else "UNPUBLISHED"
    cat = "Precious" if idx <= len(prec) else "Semi-Precious"
    print(f"{idx:2d}. {g['slug']:32s} | {g['name']:32s} | {cat:13s} | {pub}")

