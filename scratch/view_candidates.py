import json

with open('scratch/batch1_candidates.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for slug, items in d.items():
    print(f"\n=================== {slug} ({len(items)} items) ===================")
    for i, it in enumerate(items):
        print(f"[{i}] {it['title']}")
        print(f"    URL: {it['thumburl']}")
        print(f"    Author: {it['artist']} | Lic: {it['license']}")

