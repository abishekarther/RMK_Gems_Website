import re

with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

slugs = re.findall(r'"slug":\s*"([^"]+)"', content)
print(f"Total slugs in FALLBACK_GEMSTONES: {len(slugs)}")
print("Slugs:", slugs)

hidden_slugs = [
    'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
    'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
    'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
    'sapphire-blue-semi-precious', 'zircon-cubic-white'
]
found = [s for s in hidden_slugs if s in slugs]
missing = [s for s in hidden_slugs if s not in slugs]
print("Found hidden slugs:", found)
print("Missing hidden slugs:", missing)

