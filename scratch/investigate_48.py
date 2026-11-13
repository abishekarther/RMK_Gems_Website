import os
import sys
import json

sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data
categories_data, slides_data, shop_settings_data, opening_hours_data, precious_gems, semi_precious_gems = get_seed_data()

print(f"Total precious in seed: {len(precious_gems)}")
print(f"Total semi-precious in seed: {len(semi_precious_gems)}")

pub_semi = [g for g in semi_precious_gems if g.get('is_published') is True]
unpub_semi = [g for g in semi_precious_gems if not g.get('is_published')]

print(f"Published semi-precious in seed: {len(pub_semi)}")
print(f"Unpublished semi-precious in seed: {len(unpub_semi)}")

print("\nUnpublished stones in seed_data:")
for g in unpub_semi:
    print(f"- {g['slug']} ({g['name']}): is_published={g.get('is_published')}, needs_client_confirmation={g.get('needs_client_confirmation')}")

# Also check frontendFallbackData.ts
with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Check API endpoint and page limit
with open('backend/app/api/endpoints/gemstones.py', 'r', encoding='utf-8') as f:
    api_text = f.read()

print("\nChecking backend API limit:")
for line in api_text.split('\n'):
    if 'limit' in line or 'page_size' in line or 'is_published' in line:
        print(" ", line.strip())

# Check frontend page code
print("\nChecking frontend page code:")
page_path = 'frontend/src/pages/SemiPreciousGemstonesPage.tsx'
if os.path.exists(page_path):
    with open(page_path, 'r', encoding='utf-8') as f:
        p_text = f.read()
    for line in p_text.split('\n'):
        if 'limit' in line or 'page' in line or 'filter' in line or 'is_published' in line or 'category' in line:
            print(" ", line.strip())
