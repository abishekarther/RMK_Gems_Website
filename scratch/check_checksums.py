import os
import hashlib
from collections import defaultdict

def get_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

stone_dir = 'frontend/public/images/stones'
hashes = defaultdict(list)
for f in os.listdir(stone_dir):
    fp = os.path.join(stone_dir, f)
    if os.path.isfile(fp):
        h = get_hash(fp)
        hashes[h].append(f)

duplicates = {h: files for h, files in hashes.items() if len(files) > 1}
if duplicates:
    print(f"Duplicate image files found in {stone_dir}:")
    for h, files in duplicates.items():
        print(f"  Hash {h[:8]}: {files}")
else:
    print("No duplicate image files found in frontend/public/images/stones.")

