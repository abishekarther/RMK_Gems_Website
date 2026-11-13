import json, re

with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract FALLBACK_GEMSTONES array
m = re.search(r'export const FALLBACK_GEMSTONES:\s*GemstoneDetail\[\]\s*=\s*(\[.*?\]);', content, re.DOTALL)
if m:
    data_str = m.group(1)
    gems = json.loads(data_str)
    hidden_slugs = [
        'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
        'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
        'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
        'sapphire-blue-semi-precious', 'zircon-cubic-white'
    ]
    for g in gems:
        if g['slug'] in hidden_slugs:
            print(f"Slug: {g['slug']}")
            print(f"  Name: {g['name']}")
            print(f"  material_type: {g.get('material_type')}")
            print(f"  short_description: {g.get('short_description')}")
            print(f"  media: {g.get('media')}")
            print()
else:
    print("Could not parse json")

