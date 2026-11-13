import json
with open('scratch/batch1_candidates.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
for k, v in d.items():
    print(f"\n=== {k} ({len(v)} results) ===")
    for item in v:
        print(f"  Title: {item['title']}")
        print(f"  Thumb: {item['thumburl']}")
        print(f"  Artist: {item['artist']}")
        print(f"  License: {item['license']}")

