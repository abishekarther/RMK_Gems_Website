import sys, json, os, re
sys.path.append('.')
from backend.app.seed.seed_data import get_seed_data
from scratch.stone_content_definitions import UPDATES

# 1. Fetch current seed data
cats, slides, shop, hours, precious, semi = get_seed_data()

# 2. Apply updates
changelog = []

def update_gem_list(gem_list, cat_slug, cat_name, cat_id):
    updated = []
    for g in gem_list:
        slug = g['slug']
        g_copy = dict(g)
        if slug in UPDATES:
            for field, new_val in UPDATES[slug].items():
                old_val = g_copy.get(field)
                if old_val != new_val:
                    changelog.append({
                        'slug': slug,
                        'name': g_copy['name'],
                        'field': field,
                        'old': old_val,
                        'new': new_val
                    })
                g_copy[field] = new_val
        updated.append(g_copy)
    return updated

updated_precious = update_gem_list(precious, "precious", "Precious Gemstones", "cat-precious")
updated_semi = update_gem_list(semi, "semi-precious", "Semi-Precious Gemstones", "cat-semi-precious")

print(f"Total fields updated across dataset: {len(changelog)}")

# Save changelog to scratch
with open('scratch/content_changelog.json', 'w', encoding='utf-8') as f:
    json.dump(changelog, f, indent=2, ensure_ascii=False)

# 3. Re-generate seed_data.py
def format_python_gem_dict(g, indent=8):
    lines = [" " * indent + "{"]
    # Key order
    order = [
        'name', 'slug', 'short_description', 'full_description', 'material_type',
        'colour', 'hardness_min', 'hardness_max', 'chemical_composition', 'crystal_system',
        'origin', 'formation', 'history_notes', 'treatments', 'care_instructions',
        'source_notes', 'needs_client_confirmation', 'availability', 'is_featured',
        'display_order', 'is_published', '3d_cut', 'gem_color_hex'
    ]
    for k in order:
        if k in g:
            v = g[k]
            val_repr = repr(v)
            lines.append(" " * (indent + 4) + f'"{k}": {val_repr},')
    lines.append(" " * indent + "},")
    return "\n".join(lines)

def build_seed_data_file():
    with open('backend/app/seed/seed_data.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Split before precious_gemstones = [
    prefix = content.split("    # Precious Gemstones (9 items)\n    precious_gemstones = [")[0]
    
    # Split after semi_precious_data return
    suffix_marker = "    return categories_data, slides_data, shop_settings_data, opening_hours_data, precious_gemstones, semi_precious_data"
    suffix = content.split(suffix_marker)[1]
    
    # Build precious block
    prec_lines = ["    # Precious Gemstones (9 items)", "    precious_gemstones = ["]
    for g in updated_precious:
        prec_lines.append(format_python_gem_dict(g))
    prec_lines.append("    ]")
    prec_block = "\n".join(prec_lines)
    
    # Build semi block
    semi_lines = ["    # Semi-Precious Gemstones (59 items)", "    semi_precious_data = ["]
    for g in updated_semi:
        semi_lines.append(format_python_gem_dict(g))
    semi_lines.append("    ]")
    semi_block = "\n".join(semi_lines)
    
    new_seed_data = prefix + prec_block + "\n\n" + semi_block + "\n\n    return categories_data, slides_data, shop_settings_data, opening_hours_data, precious_gemstones, semi_precious_data" + suffix
    
    with open('backend/app/seed/seed_data.py', 'w', encoding='utf-8') as f:
        f.write(new_seed_data)
    print("Updated backend/app/seed/seed_data.py successfully!")

build_seed_data_file()

# 4. Re-generate frontend/src/data/gemstoneFallbackData.ts
def build_fallback_ts_file():
    with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
        ts_content = f.read()
        
    ts_prefix = ts_content.split("export const FALLBACK_GEMSTONES: GemstoneDetail[] = [")[0]
    
    fallback_gems = []
    
    for g in updated_precious:
        item = {
            "id": f"gem-{g['slug']}",
            "category_id": "cat-precious",
            "category_slug": "precious",
            "category_name": "Precious Gemstones",
            "name": g["name"],
            "slug": g["slug"],
            "short_description": g["short_description"],
            "full_description": g["full_description"],
            "material_type": g["material_type"],
            "colour": g["colour"],
            "hardness_min": g["hardness_min"],
            "hardness_max": g["hardness_max"],
            "chemical_composition": g["chemical_composition"],
            "crystal_system": g["crystal_system"],
            "origin": g["origin"],
            "formation": g["formation"],
            "history_notes": g["history_notes"],
            "treatments": g["treatments"],
            "care_instructions": g["care_instructions"],
            "availability": g["availability"],
            "is_featured": g["is_featured"],
            "display_order": g["display_order"],
            "media": [
                {
                    "id": f"media-{g['slug']}-photo",
                    "media_type": "image",
                    "file_url": f"/images/stones/{g['slug']}.webp",
                    "thumbnail_url": f"/images/stones/{g['slug']}.webp",
                    "alt_text": f"{g['name']} gemstone - {g['colour']}",
                    "display_order": 1,
                    "is_primary": True
                }
            ]
        }
        fallback_gems.append(item)
        
    for g in updated_semi:
        item = {
            "id": f"gem-{g['slug']}",
            "category_id": "cat-semi-precious",
            "category_slug": "semi-precious",
            "category_name": "Semi-Precious Gemstones",
            "name": g["name"],
            "slug": g["slug"],
            "short_description": g["short_description"],
            "full_description": g["full_description"],
            "material_type": g["material_type"],
            "colour": g["colour"],
            "hardness_min": g["hardness_min"],
            "hardness_max": g["hardness_max"],
            "chemical_composition": g["chemical_composition"],
            "crystal_system": g["crystal_system"],
            "origin": g["origin"],
            "formation": g["formation"],
            "history_notes": g["history_notes"],
            "treatments": g["treatments"],
            "care_instructions": g["care_instructions"],
            "availability": g["availability"],
            "is_featured": g["is_featured"],
            "display_order": g["display_order"],
            "media": [
                {
                    "id": f"media-{g['slug']}-photo",
                    "media_type": "image",
                    "file_url": f"/images/stones/{g['slug']}.webp",
                    "thumbnail_url": f"/images/stones/{g['slug']}.webp",
                    "alt_text": f"{g['name']} gemstone - {g['colour']}",
                    "display_order": 1,
                    "is_primary": True
                }
            ]
        }
        fallback_gems.append(item)
        
    ts_json = json.dumps(fallback_gems, indent=2, ensure_ascii=False)
    new_ts_content = ts_prefix + f"export const FALLBACK_GEMSTONES: GemstoneDetail[] = {ts_json};\n"
    
    with open('frontend/src/data/gemstoneFallbackData.ts', 'w', encoding='utf-8') as f:
        f.write(new_ts_content)
    print("Updated frontend/src/data/gemstoneFallbackData.ts successfully!")

build_fallback_ts_file()

