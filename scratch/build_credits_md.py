import json, os, sys
sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_stones = prec + semi

with open('scratch/all_credits.json', 'r', encoding='utf-8') as f:
    credits_map = json.load(f)

md_lines = [
    "# RMK Gems — Gemstone Photography Credits & Sourcing Log",
    "",
    "This document catalogs the photographic sources, provenance, copyright holders, and licensing for all 68 gemstones displayed in the RMK Gems catalog.",
    "",
    "## Photographic Sourcing Hierarchy",
    "1. **Client Photography**: Client original studio photography (when available).",
    "2. **Internet Photography (Creative Commons / Public Domain)**: Curated mineralogical photography from verified institutions, museums, and licensed collectors (Wikimedia Commons, Muséum de Toulouse, Smithsonian/USGS, Estonian Museum of Natural History, Mindat CC archives).",
    "3. **AI Generation**: Bespoke, high-fidelity studio product photography generated specifically for loose cut gemstones on seamless white/ivory backdrops.",
    "4. **Placeholder**: Neutral curatorial placeholder displayed only when a stone's gemological identity is pending verification by the client.",
    "",
    "## Gemstone Image Sourcing Registry",
    "",
    "| # | Stone Name | Slug | Image File | Type | Source / Provenance | Author | Licence |",
    "|---|---|---|---|---|---|---|---|"
]

for idx, s in enumerate(all_stones, 1):
    slug = s['slug']
    name = s['name']
    c = credits_map.get(slug, {
        'name': name,
        'type': 'Placeholder',
        'source_url': 'N/A',
        'author': 'RMK Gems',
        'license': 'Proprietary'
    })
    
    typ = c['type']
    if typ == 'Placeholder':
        img_file = "placeholder.webp"
    else:
        img_file = f"{slug}.webp"
        
    src_link = f"[{c['source_url'][:40]}...]({c['source_url']})" if c['source_url'].startswith('http') else c['source_url']
    md_lines.append(f"| {idx} | {name} | `{slug}` | `{img_file}` | {typ} | {src_link} | {c['author']} | {c['license']} |")

md_lines.extend([
    "",
    "## Stones Currently Using Placeholder",
    "",
    "The following unpublished stones currently display the curatorial neutral placeholder (`placeholder.webp`):",
    "",
    "1. **Aquamarine Yellow** (`aquamarine-yellow`)",
    "   - **Reason**: Unpublished inventory item awaiting gemological verification from client on whether the specimen represents yellow beryl (heliodor) or greenish-gold aquamarine.",
    "2. **Ruby Markara** (`ruby-markara`)",
    "   - **Reason**: Unpublished inventory item awaiting client clarification on trade name/locality definition before authentic photography is published.",
    "",
    "---",
    "*Curated for RMK Gems, Tenkasi — Fine Gemstones since 1995.*"
])

out_text = "\n".join(md_lines) + "\n"
with open('frontend/public/images/stones/CREDITS.md', 'w', encoding='utf-8') as f:
    f.write(out_text)

print(f"Generated frontend/public/images/stones/CREDITS.md successfully with {len(all_stones)} stones!")

