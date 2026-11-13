import json

with open('scratch/all_candidates.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

has_candidates = {}
no_candidates = []

for slug, cands in data.items():
    if cands:
        has_candidates[slug] = cands
    else:
        no_candidates.append(slug)

print(f"Stones with Wikimedia candidates: {len(has_candidates)}")
print(f"Stones needing search or alternative: {len(no_candidates)}")

print("\n--- STONES WITH CANDIDATES ---")
for slug, cands in has_candidates.items():
    print(f"\n[{slug}] ({len(cands)} candidates):")
    for c in cands[:2]:
        print(f"  - Title: {c['title']}")
        print(f"    License: {c['license']}")
        print(f"    URL: {c['url']}")

print("\n--- STONES WITHOUT CANDIDATES ---")
for slug in no_candidates:
    print(f"  - {slug}")

