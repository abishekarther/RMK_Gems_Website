import sys, re
sys.path.append('.')
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_gems = prec + semi

forbidden = ['untreated', 'unheated', 'natural color', 'natural colour', 'certif', 'premium', 'valuation', 'talisman', 'fortune', 'luck', 'rare', 'flawless', 'finest', 'tamil']

matches = []
for g in all_gems:
    for k, v in g.items():
        if isinstance(v, str):
            for f in forbidden:
                if re.search(r'\b' + f, v, re.I):
                    matches.append((g['slug'], g['name'], k, f, v))

print(f"Found {len(matches)} violations:")
for slug, name, k, f, v in matches:
    print(f"\n[{slug}] {k} (found: '{f}'):\n  Current text: {v}")

