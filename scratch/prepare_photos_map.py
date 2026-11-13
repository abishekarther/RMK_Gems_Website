import sys, os, json
sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_stones = prec + semi

slugs = [g['slug'] for g in all_stones]
print(f"Total slugs: {len(slugs)}")

# Stones that are explicitly placeholders according to spec:
# Aquamarine Yellow: "yellow beryl; if none found, use placeholder"
# Ruby Markara: "only if identity is confirmed; else placeholder"
placeholder_slugs = {'aquamarine-yellow', 'ruby-markara'}

print(f"Placeholder slugs: {placeholder_slugs}")

