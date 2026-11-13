import sys
sys.path.insert(0, '.')
from backend.app.seed.seed_data import get_seed_data

cats, slides, shop, hours, precious, semi_precious = get_seed_data()

print("Precious (9):")
for p in precious:
    print(f"  {p['slug']} -> {p['name']} (image_url={p.get('image_url')})")

print(f"\nSemi-Precious ({len(semi_precious)}):")
for sp in semi_precious:
    print(f"  {sp['slug']} -> {sp['name']} (image_url={sp.get('image_url')})")

