import sys, os, json, re

sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    ts_content = f.read()

m = re.search(r'export const FALLBACK_GEMSTONES:\s*GemstoneDetail\[\]\s*=\s*(\[.*?\]);', ts_content, re.DOTALL)
if not m:
    print("Could not find FALLBACK_GEMSTONES array")
    sys.exit(1)

current_fallback = json.loads(m.group(1))
fallback_by_slug = {g['slug']: g for g in current_fallback}

cats, slides, shop, hours, prec, semi = get_seed_data()
all_seed = prec + semi

print(f"Total fallback stones: {len(current_fallback)}, Total seed stones: {len(all_seed)}")

diff_count = 0
for s in all_seed:
    slug = s['slug']
    fb = fallback_by_slug.get(slug)
    if fb:
        for field in ['name', 'short_description', 'full_description', 'material_type', 'colour', 
                      'hardness_min', 'hardness_max', 'chemical_composition', 'crystal_system',
                      'origin', 'formation', 'history_notes', 'treatments', 'care_instructions']:
            s_val = s.get(field)
            fb_val = fb.get(field)
            if s_val != fb_val:
                diff_count += 1
                print(f"[{slug}] Diff in '{field}': seed='{s_val}' vs fallback='{fb_val}'")
    else:
        print(f"Missing from fallback: {slug}")

print(f"Total field differences: {diff_count}")
