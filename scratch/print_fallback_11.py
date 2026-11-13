import json, re

with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'export const FALLBACK_GEMSTONES:\s*GemstoneDetail\[\]\s*=\s*(\[.*?\]);', content, re.DOTALL)
if m:
    gems = json.loads(m.group(1))
    hidden_slugs = [
        'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
        'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
        'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
        'sapphire-blue-semi-precious', 'zircon-cubic-white'
    ]
    for g in gems:
        if g['slug'] in hidden_slugs:
            print("========================================")
            print(f"SLUG: {g['slug']}")
            for k, v in g.items():
                print(f"  {k}: {v}")

