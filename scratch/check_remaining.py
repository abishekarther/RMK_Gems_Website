import sys
import os
sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_stones = prec + semi

stone_files = set(os.listdir('frontend/public/images/stones'))
existing_slugs = {f.replace('.webp', '') for f in stone_files if f.endswith('.webp') and f != 'placeholder.webp'}

published = [g for g in all_stones if g['is_published']]
unpublished = [g for g in all_stones if not g['is_published']]

print(f"Total stones: {len(all_stones)}")
print(f"Published stones: {len(published)}")
print(f"Unpublished stones: {len(unpublished)}")
print(f"Existing stone images: {len(existing_slugs)}")

remaining_published = [g for g in published if g['slug'] not in existing_slugs]
print(f"\nRemaining published stones without images ({len(remaining_published)}):")
for g in remaining_published:
    print(f"- {g['slug']}: {g['name']} ({g.get('colour', '')})")

remaining_unpublished = [g for g in unpublished if g['slug'] not in existing_slugs]
print(f"\nRemaining unpublished stones without images ({len(remaining_unpublished)}):")
for g in remaining_unpublished:
    print(f"- {g['slug']}: {g['name']}")
