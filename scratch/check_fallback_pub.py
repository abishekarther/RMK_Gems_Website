import re

with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Match each object block in FALLBACK_GEMSTONES
blocks = re.findall(r'\{\s*"id":\s*"gem-[^"]+".*?"is_published":\s*(true|false)', text, re.DOTALL)
print(f"Total gemstone blocks with is_published: {len(blocks)}")

# Find all slugs and their is_published
slug_pub = re.findall(r'"slug":\s*"([^"]+)".*?"is_published":\s*(true|false)', text, re.DOTALL)
# Group by slug
unique_slugs = {}
for s, p in slug_pub:
    if s not in unique_slugs:
        unique_slugs[s] = p

print(f"Unique slugs: {len(unique_slugs)}")
unpub = [s for s, p in unique_slugs.items() if p == 'false']
print(f"Unpublished slugs ({len(unpub)}):")
for u in unpub:
    print(f"  {u}")

