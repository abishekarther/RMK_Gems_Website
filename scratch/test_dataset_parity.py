import sys, json
sys.path.append('.')
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
backend_map = {g['slug']: g for g in prec + semi}

with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    text = f.read()
json_part = text.split("export const FALLBACK_GEMSTONES: GemstoneDetail[] = ")[1].rstrip(";\n")
frontend_gems = json.loads(json_part)
frontend_map = {g['slug']: g for g in frontend_gems}

print("=== CHECKING DATASET PARITY (BACKEND VS FRONTEND FALLBACK) ===")
print(f"Backend stones count: {len(backend_map)}")
print(f"Frontend fallback stones count: {len(frontend_map)}")
assert len(backend_map) == len(frontend_map) == 68

fields_to_compare = [
    'name', 'slug', 'short_description', 'full_description', 'material_type',
    'colour', 'hardness_min', 'hardness_max', 'chemical_composition', 'crystal_system',
    'origin', 'formation', 'history_notes', 'treatments', 'care_instructions',
    'availability', 'is_featured', 'display_order'
]

mismatches = []
for slug, bg in backend_map.items():
    if slug not in frontend_map:
        mismatches.append(f"Slug '{slug}' missing in frontend fallback!")
        continue
    fg = frontend_map[slug]
    for field in fields_to_compare:
        bv = bg.get(field)
        fv = fg.get(field)
        if bv != fv:
            mismatches.append(f"[{slug}] Field '{field}' mismatch: backend='{bv}' vs frontend='{fv}'")

if mismatches:
    print(f"Mismatches found: {len(mismatches)}")
    for m in mismatches[:10]:
        print(" ", m)
    sys.exit(1)
else:
    print("SUCCESS: 100% PARITY! All 68 stones match identically across all public gemological fields!")

