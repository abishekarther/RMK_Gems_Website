import os, sys
sys.path.insert(0, os.path.abspath('.'))

from backend.app.seed.seed_data import get_seed_data

src_dir = "bgeraser_results (1)"
files = os.listdir(src_dir)
print(f"Total files in {src_dir}: {len(files)}")

cats, slides, shop, hours, prec, semi = get_seed_data()
semi_slugs = [s['slug'] for s in semi]
print(f"Total semi-precious stones expected: {len(semi_slugs)}")

found = []
missing = []

for s in semi_slugs:
    expected_png = f"{s}.png"
    if expected_png in files:
        found.append(s)
    else:
        # Check if there is an alternative name
        candidates = [f for f in files if s in f or f.startswith(s.split('-')[0])]
        missing.append((s, candidates))

print(f"Matched {len(found)} out of {len(semi_slugs)} semi-precious stones.")
if missing:
    print("Missing or mismatch:")
    for m in missing:
        print(" ", m)

