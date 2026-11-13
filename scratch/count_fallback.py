import json

# Let's count how many gemstones in FALLBACK_GEMSTONES
with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
slugs = [l.strip().split(':')[1].strip().strip('",') for l in lines if '"slug":' in l]
print(f"Total slugs in fallback data: {len(slugs)}")
print(slugs)

