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

updated_fallback = []
for s in all_seed:
    slug = s['slug']
    fb = fallback_by_slug.get(slug, {})
    
    is_precious = any(p['slug'] == slug for p in prec)
    cat_slug = "precious" if is_precious else "semi-precious"
    cat_id = f"cat-{cat_slug}"
    cat_name = "Precious Gemstones" if is_precious else "Semi-Precious Gemstones"
    
    # Media URL
    if is_precious:
        media_url = f"/images/gia/{slug}.png"
    elif slug == 'garnet-rose-cut-checkerboard':
        media_url = "/images/stones/garnet-rose-cut-checkerboard.webp"
    elif slug == 'sapphire-blue-semi-precious':
        media_url = "/images/stones/sapphire-blue-semi-precious.webp"
    else:
        media_url = f"/images/stones/{slug}.webp"

    colour_val = s.get('colour')
    alt_text = f"{s['name']} gemstone - {colour_val}" if colour_val else f"{s['name']} gemstone"

    item = {
        "id": f"gem-{slug}",
        "category_id": cat_id,
        "category_slug": cat_slug,
        "category_name": cat_name,
        "name": s['name'],
        "slug": slug,
        "short_description": s.get('short_description'),
        "full_description": s.get('full_description'),
        "material_type": s.get('material_type'),
        "colour": s.get('colour'),
        "hardness_min": s.get('hardness_min'),
        "hardness_max": s.get('hardness_max'),
        "chemical_composition": s.get('chemical_composition'),
        "crystal_system": s.get('crystal_system'),
        "origin": s.get('origin'),
        "formation": s.get('formation'),
        "history_notes": s.get('history_notes'),
        "treatments": s.get('treatments'),
        "care_instructions": s.get('care_instructions'),
        "availability": s.get('availability', 'available'),
        "is_featured": s.get('is_featured', False),
        "display_order": s.get('display_order', 1),
        "media": [
            {
                "id": f"media-{slug}-photo",
                "media_type": "image",
                "file_url": media_url,
                "thumbnail_url": media_url,
                "alt_text": alt_text,
                "display_order": 1,
                "is_primary": True,
            }
        ]
    }
    updated_fallback.append(item)

# Re-serialize to TS
json_text = json.dumps(updated_fallback, indent=2, ensure_ascii=False)
prefix = ts_content[:m.start(1)]
suffix = ts_content[m.end(1):]

new_ts_content = prefix + json_text + suffix

with open('frontend/src/data/gemstoneFallbackData.ts', 'w', encoding='utf-8') as f:
    f.write(new_ts_content)

print(f"Successfully synced frontend/src/data/gemstoneFallbackData.ts with all {len(updated_fallback)} stones!")

