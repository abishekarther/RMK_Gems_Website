import os
import re

pub_dir = r'c:\RMK_Gems_Website\frontend\public'

with open(r'c:\RMK_Gems_Website\frontend\src\data\gemstonePhotos.ts', 'r', encoding='utf-8') as f:
    content = f.read()

entries = re.findall(r"'([a-z0-9\-]+)':\s*'(/images/[^']+)'", content)
print(f"Total registry entries: {len(entries)}")

missing = []
for slug, path in entries:
    rel_path = path.lstrip('/')
    full_path = os.path.join(pub_dir, rel_path)
    if not os.path.exists(full_path):
        missing.append((slug, path, full_path))
    else:
        sz = os.path.getsize(full_path)
        if sz == 0:
            missing.append((slug, path, "empty file"))

if missing:
    print(f"FAILED: Missing files: {missing}")
else:
    print(f"SUCCESS: All {len(entries)} registry entries exist on disk with valid file size!")

# Check precious stones
prec_slugs = [
    'ruby', 'pearl', 'red-coral', 'emerald', 'yellow-sapphire',
    'diamond', 'blue-sapphire', 'hessonite-garnet', 'cats-eye-chrysoberyl'
]
dict_entries = dict(entries)
for slug in prec_slugs:
    print(f"Precious stone {slug} -> {dict_entries.get(slug)}")

