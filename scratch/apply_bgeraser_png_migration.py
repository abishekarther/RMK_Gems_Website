import os
import re
from pathlib import Path

BASE = Path("c:/RMK_Gems_Website")
PUBLIC_STONES = BASE / "frontend/public/images/stones"
DIST_STONES = BASE / "frontend/dist/images/stones"
PHOTOS_TS = BASE / "frontend/src/data/gemstonePhotos.ts"
FALLBACK_TS = BASE / "frontend/src/data/gemstoneFallbackData.ts"
CREDITS_MD = PUBLIC_STONES / "CREDITS.md"

PRECIOUS_SLUGS = [
    "ruby", "pearl", "red-coral", "emerald", "yellow-sapphire",
    "diamond", "blue-sapphire", "hessonite-garnet", "cats-eye-chrysoberyl"
]

# 1. Remove leftover precious .webp files from stones folders
for folder in [PUBLIC_STONES, DIST_STONES]:
    for slug in PRECIOUS_SLUGS:
        f = folder / f"{slug}.webp"
        if f.exists():
            f.unlink()
            print(f"Removed leftover precious webp: {f}")

# 2. Update gemstonePhotos.ts
photos_content = PHOTOS_TS.read_text(encoding="utf-8")
# Replace any /images/stones/<name>.webp with /images/stones/<name>.png
updated_photos = re.sub(r"/images/stones/([a-zA-Z0-9\-]+)\.webp", r"/images/stones/\1.png", photos_content)
# Bump version to v=20261113_6
updated_photos = re.sub(r"PHOTO_VERSION = 'v=[^']+'", "PHOTO_VERSION = 'v=20261113_6'", updated_photos)
PHOTOS_TS.write_text(updated_photos, encoding="utf-8")
print("Updated gemstonePhotos.ts to point to .png and bumped PHOTO_VERSION")

# 3. Update gemstoneFallbackData.ts
fallback_content = FALLBACK_TS.read_text(encoding="utf-8")
updated_fallback = re.sub(r"/images/stones/([a-zA-Z0-9\-]+)\.webp", r"/images/stones/\1.png", fallback_content)
FALLBACK_TS.write_text(updated_fallback, encoding="utf-8")
print("Updated gemstoneFallbackData.ts to point to .png")

# 4. Update CREDITS.md if present
if CREDITS_MD.exists():
    credits_content = CREDITS_MD.read_text(encoding="utf-8")
    updated_credits = re.sub(r"/images/stones/([a-zA-Z0-9\-]+)\.webp", r"/images/stones/\1.png", credits_content)
    CREDITS_MD.write_text(updated_credits, encoding="utf-8")
    # Also copy to dist if dist exists
    dist_credits = DIST_STONES / "CREDITS.md"
    dist_credits.write_text(updated_credits, encoding="utf-8")
    print("Updated CREDITS.md")

# 5. Inventory check of stones directory
png_files = sorted([f.name for f in PUBLIC_STONES.glob("*.png")])
webp_files = sorted([f.name for f in PUBLIC_STONES.glob("*.webp")])
print(f"\nPublic stones directory now contains:")
print(f"  {len(png_files)} PNG files")
print(f"  {len(webp_files)} WebP files: {webp_files}")

