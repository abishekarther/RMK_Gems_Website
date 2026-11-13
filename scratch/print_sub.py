import json
with open('scratch/batch1_candidates.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
for k in ['pyrite', 'rose-quartz', 'smoky-quartz', 'sunstone']:
    print(f"\n=== {k} ===")
    for item in d.get(k, []):
        print(f"  {item['title']}")
        print(f"    {item['thumburl']}")
        print(f"    {item['artist']} | {item['license']}")

