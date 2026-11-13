import sys
sys.path.insert(0, '.')
from backend.app.seed.seed_data import get_seed_data

cats, slides, shop, hours, precious, semi_precious = get_seed_data()
hidden_slugs = [
    'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
    'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
    'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
    'sapphire-blue-semi-precious', 'zircon-cubic-white'
]

for s in semi_precious:
    if s['slug'] in hidden_slugs:
        print(f"Slug: {s['slug']}")
        print(f"  Name: {s['name']}")
        print(f"  is_published: {s.get('is_published')}")
        print(f"  needs_client_confirmation: {s.get('needs_client_confirmation')}")
        print(f"  source_notes: {s.get('source_notes')}")
        print(f"  material_type: {s.get('material_type')}")

