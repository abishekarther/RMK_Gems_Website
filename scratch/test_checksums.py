import hashlib, os, sys

stones_dir = 'frontend/public/images/stones'
gia_dir = 'frontend/public/images/gia'

print("=== CHECK 2: CHECKSUM UNIQUENESS ACROSS ALL STONE IMAGES ===")

files_to_check = []
for f in os.listdir(stones_dir):
    if (f.endswith('.webp') or f.endswith('.png')) and not f.startswith('placeholder'):
        files_to_check.append(os.path.join(stones_dir, f))

if os.path.exists(gia_dir):
    for f in os.listdir(gia_dir):
        if f.endswith(('.png', '.webp', '.jpg')):
            files_to_check.append(os.path.join(gia_dir, f))

print(f"Total gemstone image files being checked: {len(files_to_check)}")

sha_map = {}
duplicates = []

for path in sorted(files_to_check):
    with open(path, 'rb') as fp:
        content = fp.read()
    sha = hashlib.sha256(content).hexdigest()
    fname = os.path.basename(path)
    
    if sha in sha_map:
        duplicates.append((fname, sha_map[sha], sha))
    else:
        sha_map[sha] = fname

if duplicates:
    print(f"FAILED: Found {len(duplicates)} duplicate image files with matching checksums:")
    for d in duplicates:
        print(f"  - '{d[0]}' shares checksum with '{d[1]}' (SHA-256: {d[2]})")
    sys.exit(1)
else:
    print(f"SUCCESS: All {len(files_to_check)} gemstone images have 100% unique checksums! No duplicate images exist.")
