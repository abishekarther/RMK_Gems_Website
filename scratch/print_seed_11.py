import sys
sys.path.insert(0, '.')
from backend.app.seed.seed_data import get_seed_data

cats, slides, shop, hours, prec, semi = get_seed_data()
hidden_slugs = [
    'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
    'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
    'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
    'sapphire-blue-semi-precious', 'zircon-cubic-white'
]

for s in semi:
    if s['slug'] in hidden_slugs:
        print("========================================")
        print(f"SLUG: {s['slug']}")
        for k, v in s.items():
            print(f"  {k}: {repr(v)}")

