import sys
sys.path.insert(0, '.')
from backend.app.seed.seed_data import get_seed_data

hidden_slugs = [
    'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
    'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
    'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
    'sapphire-blue-semi-precious', 'zircon-cubic-white'
]

cats, slides, shop, hours, precious, semi_precious = get_seed_data()
gemstones_data = precious + semi_precious

for g in gemstones_data:
    if g['slug'] in hidden_slugs:
        print(f"=== {g['slug']} ===")
        print(f"name: {g['name']}")
        print(f"is_published: {g.get('is_published')}")
        print(f"needs_client_confirmation: {g.get('needs_client_confirmation')}")
        print(f"material_type: {g.get('material_type')}")
        print(f"description: {g.get('description')}")
        print(f"mineral_family: {g.get('mineral_family')}")
        print(f"chemical_formula: {g.get('chemical_formula')}")
        print(f"crystal_system: {g.get('crystal_system')}")
        print(f"hardness: {g.get('hardness')}")
        print(f"refractive_index: {g.get('refractive_index')}")
        print(f"specific_gravity: {g.get('specific_gravity')}")
        print(f"colors: {g.get('colors')}")
        print(f"primary_color: {g.get('primary_color')}")
        print(f"optical_character: {g.get('optical_character')}")
        print(f"birefringence: {g.get('birefringence')}")
        print(f"pleochroism: {g.get('pleochroism')}")
        print(f"dispersion: {g.get('dispersion')}")
        print(f"lustre: {g.get('lustre')}")
        print(f"transparency: {g.get('transparency')}")
        print(f"sources: {g.get('sources')}")
        print(f"cut_style: {g.get('cut_style')}")
        print(f"image_url: {g.get('image_url')}")
        print(f"source_notes: {g.get('source_notes')}")
        print()
