import json

with open('scratch/onyx_results.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for slug, items in d.items():
    print(f"\n=== {slug} ({len(items)} items) ===")
    for i, it in enumerate(items[:4]):
        # [title, thumb, artist, lic]
        print(f"[{i}] {it[0]}")
        print(f"    URL: {it[1]}")
        print(f"    Author: {it[2]} | Lic: {it[3]}")

