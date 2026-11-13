import json

with open('scratch/user_table.json', 'r', encoding='utf-8') as f:
    stones = json.load(f)

doc = """# RMK Gems — Gemstone Photography Credits & Sourcing Log

This document catalogs the photographic sources, provenance, copyright holders, and licensing for all 68 gemstones displayed in the RMK Gems catalog.

## Photographic Sourcing Hierarchy
1. **Precious Gemstones (GIA Gem Encyclopedia)**: Authentic cut and polished mineralogical photography from the GIA Gem Encyclopedia archives (gia.edu/gem-encyclopedia).
2. **Semi-Precious Gemstones (Client Studio Photography)**: Client original studio photography for all 59 semi-precious loose gemstones on neutral backdrops.

## 1. Precious Gemstones (9 Stones - GIA Gem Encyclopedia)

| # | Stone Name | Slug | Image File | Type | Source / Provenance |
|---|---|---|---|---|---|
| 1 | Ruby | `ruby` | `/images/gia/ruby.png` | Natural Cut Gemstone | GIA Gem Encyclopedia |
| 2 | Pearl | `pearl` | `/images/gia/pearl.png` | Natural Gemstone | GIA Gem Encyclopedia |
| 3 | Red Coral | `red-coral` | `/images/gia/red-coral.png` | Natural Gemstone | GIA Gem Encyclopedia |
| 4 | Emerald | `emerald` | `/images/gia/emerald.png` | Natural Cut Gemstone | GIA Gem Encyclopedia |
| 5 | Yellow Sapphire | `yellow-sapphire` | `/images/gia/yellow-sapphire.png` | Natural Cut Gemstone | GIA Gem Encyclopedia |
| 6 | Diamond | `diamond` | `/images/gia/diamond.png` | Natural Cut Gemstone | GIA Gem Encyclopedia |
| 7 | Blue Sapphire | `blue-sapphire` | `/images/gia/blue-sapphire.png` | Natural Cut Gemstone | GIA Gem Encyclopedia |
| 8 | Hessonite Garnet | `hessonite-garnet` | `/images/gia/hessonite-garnet.png` | Natural Cut Gemstone | GIA Gem Encyclopedia |
| 9 | Cat's Eye (Chrysoberyl) | `cats-eye-chrysoberyl` | `/images/gia/cats-eye-chrysoberyl.png` | Natural Cut Gemstone | GIA Gem Encyclopedia |

## 2. Semi-Precious Gemstones (All 59 Stones - Client Studio Photography)

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
    doc += f"| {num} | {name} | `{target}` | `/images/stones/{target}.webp` | {cut} | {color} — {features} | RMK Gems Client Studio Photography |\n"

with open(r'c:\RMK_Gems_Website\frontend\public\images\stones\CREDITS.md', 'w', encoding='utf-8') as f:
    f.write(doc)

with open(r'c:\RMK_Gems_Website\frontend\dist\images\stones\CREDITS.md', 'w', encoding='utf-8') as f:
    f.write(doc)

print("Updated CREDITS.md successfully.")

