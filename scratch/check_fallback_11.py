import re

with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

hidden_slugs = [
    'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
    'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
    'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
    'sapphire-blue-semi-precious', 'zircon-cubic-white'
]

for s in hidden_slugs:
    m = re.search(r"slug:\s*['\"]" + s + r"['\"].*?is_published:\s*(true|false)", content, re.DOTALL)
    if m:
        print(f"{s}: is_published={m.group(1)}")
    else:
        print(f"{s}: NOT FOUND or pattern mismatch")

