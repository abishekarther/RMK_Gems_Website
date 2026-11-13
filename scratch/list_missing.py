import os, sys
sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_stones = prec + semi

existing = {f.replace('.webp', '') for f in os.listdir('frontend/public/images/stones') if f.endswith('.webp') and f != 'placeholder.webp'}

missing = [s for s in all_stones if s['slug'] not in existing]
print(f"Total missing: {len(missing)}")
for s in missing:
    print(f"{s['slug']}|{s['name']}|{s['is_published']}|{s['colour']}")

