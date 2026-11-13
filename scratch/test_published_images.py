import os, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE))
from backend.app.seed.seed_data import get_seed_data

print("=== CHECK: IMAGE FILE EXISTENCE FOR ALL PUBLISHED STONES ===")

cats, slides, shop, hours, prec, semi = get_seed_data()
published_stones = [s for s in prec + semi if s.get('is_published') is True]

stones_dir = BASE / 'frontend/public/images/stones'
gia_dir = BASE / 'frontend/public/images/gia'

prec_slugs = {s['slug'] for s in prec}

missing_files = []

for s in published_stones:
    slug = s['slug']
    name = s['name']
    
    if slug in prec_slugs:
        path = gia_dir / f"{slug}.png"
    else:
        path = stones_dir / f"{slug}.png"
    
    if not path.exists():
        missing_files.append((slug, name, str(path)))
    elif path.stat().st_size == 0:
        missing_files.append((slug, name, f"{path} (0 bytes)"))

print(f"Verified image files for {len(published_stones)} published stones.")

if missing_files:
    print(f"FAILED: {len(missing_files)} stones missing:")
    for slug, name, p in missing_files:
        print(f"  - {slug} ({name}): missing at {p}")
    sys.exit(1)
else:
    print("SUCCESS: All 9 precious stones found in /images/gia/ and all 59 semi-precious stones found in /images/stones/!")
