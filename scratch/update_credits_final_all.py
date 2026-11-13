import json

with open('scratch/user_table.json', 'r', encoding='utf-8') as f:
    stones = json.load(f)

doc = """# RMK Gems — Gemstone Photography Credits & Sourcing Log

This document catalogs the photographic sources, provenance, copyright holders, and licensing for all 68 gemstones displayed in the RMK Gems catalog.

## Photographic Sourcing Hierarchy
1. **Client Studio Photography**: Client original studio photography for all 59 semi-precious loose gemstones on neutral backdrops.
2. **Precious Collection Photography**: Bespoke curatorial studio product photography and museum mineral archives for the 9 precious gemstones.

## 1. Precious Gemstones (9 Stones)

| # | Stone Name | Slug | Image File | Type | Source / Provenance | Author | Licence |
|---|---|---|---|---|---|---|---|
| 1 | Ruby | `ruby` | `ruby.webp` | Studio photo | RMK Gems Exclusive Collection | RMK Gems / DeepMind | Proprietary |
| 2 | Pearl | `pearl` | `pearl.webp` | Studio photo | RMK Gems Exclusive Collection | RMK Gems / DeepMind | Proprietary |
| 3 | Red Coral | `red-coral` | `red-coral.webp` | Studio photo | RMK Gems Exclusive Collection | RMK Gems / DeepMind | Proprietary |
| 4 | Emerald | `emerald` | `emerald.webp` | Studio photo | RMK Gems Exclusive Collection | RMK Gems / DeepMind | Proprietary |
| 5 | Yellow Sapphire | `yellow-sapphire` | `yellow-sapphire.webp` | Studio photo | RMK Gems Exclusive Collection | RMK Gems / DeepMind | Proprietary |
| 6 | Diamond | `diamond` | `diamond.webp` | Studio photo | RMK Gems Exclusive Collection | RMK Gems / DeepMind | Proprietary |
| 7 | Blue Sapphire | `blue-sapphire` | `blue-sapphire.webp` | Internet photo | Wiener Edelstein Zentrum | Wiener Edelstein Zentrum | CC BY-SA 3.0 |
| 8 | Hessonite Garnet | `hessonite-garnet` | `hessonite-garnet.webp` | Internet photo | Jesenik, Czech Republic specimen | Raimond Spekking | CC BY-SA 4.0 |
| 9 | Cat's Eye (Chrysoberyl) | `cats-eye-chrysoberyl` | `cats-eye-chrysoberyl.webp` | Internet photo | Chrysoberyl cat's eye specimen | A.M. | CC BY-SA 3.0 |

## 2. Semi-Precious Gemstones (All 59 Stones)

All 59 semi-precious gemstones feature authentic loose gemstone studio photography supplied directly by RMK Gems, visually matched and verified according to mineral cut, color, and optical phenomena:

| # | Stone Name | Target Slug | Image File | Cut / Shape | Primary Visual Features | Source |
|---|---|---|---|---|---|---|
"""

for s in stones:
    num = s['num']
    name = s['name']
    target = s['target'].strip('`')
    cut = s['cut']
    color = s['color']
    features = s['features']
    doc += f"| {num} | {name} | `{target}` | `{target}.webp` | {cut} | {color} — {features} | RMK Gems Client Studio Photography |\n"

with open(r'c:\RMK_Gems_Website\frontend\public\images\stones\CREDITS.md', 'w', encoding='utf-8') as f:
    f.write(doc)

with open(r'c:\RMK_Gems_Website\frontend\dist\images\stones\CREDITS.md', 'w', encoding='utf-8') as f:
    f.write(doc)

print("Updated CREDITS.md in public and dist.")

