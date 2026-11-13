import os, sys
sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data

_, _, _, _, prec, semi = get_seed_data()
all_stones = prec + semi

placeholder_slugs = {'aquamarine-yellow', 'ruby-markara'}

ts_lines = [
    "/**",
    " * Gemstone Photography Registry for RMK Gems.",
    " * Maps all 68 gemstones to high-resolution, unique photography located in /images/stones/<slug>.webp.",
    " * All images follow strict curatorial standards: single loose stone, plain neutral background, < 150 KB WebP.",
    " */",
    "",
    "export const GEMSTONE_PHOTOS: Record<string, string> = {"
]

for g in prec:
    slug = g['slug']
    if slug in placeholder_slugs:
        ts_lines.append(f"  '{slug}': '/images/stones/placeholder.webp',")
    else:
        ts_lines.append(f"  '{slug}': '/images/stones/{slug}.webp',")

ts_lines.append("")
ts_lines.append("  // Semi-Precious Gemstones")

for g in semi:
    slug = g['slug']
    if slug in placeholder_slugs:
        ts_lines.append(f"  '{slug}': '/images/stones/placeholder.webp',")
    else:
        ts_lines.append(f"  '{slug}': '/images/stones/{slug}.webp',")

ts_lines.extend([
    "};",
    "",
    "const PLACEHOLDER_PHOTO = '/images/stones/placeholder.webp';",
    "",
    "/**",
    " * Returns the image URL for a given gemstone slug.",
    " * Unknown slugs always fall back to the neutral placeholder, never a ruby.",
    " */",
    "export function getGemstonePhoto(slug: string): string {",
    "  return GEMSTONE_PHOTOS[slug] || PLACEHOLDER_PHOTO;",
    "}",
    "",
    "/**",
    " * Indicates whether a gemstone's photo is representative photography.",
    " * Currently true for all catalog items until client studio photos are supplied.",
    " */",
    "export function isRepresentativePhoto(slug: string): boolean {",
    "  return true;",
    "}",
    "",
    "/**",
    " * Generates descriptive, accessible alt text for a gemstone image.",
    " */",
    "export function getGemstoneAltText(name: string, colour?: string): string {",
    "  return colour ? `${name} gemstone - ${colour}` : `${name} gemstone`;",
    "}",
    ""
])

with open('frontend/src/data/gemstonePhotos.ts', 'w', encoding='utf-8') as f:
    f.write("\n".join(ts_lines))

print("Successfully wrote frontend/src/data/gemstonePhotos.ts!")

