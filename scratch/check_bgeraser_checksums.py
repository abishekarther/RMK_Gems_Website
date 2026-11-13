import hashlib, os
from collections import defaultdict

src_dir = "bgeraser_results (1)"
hashes = defaultdict(list)

for f in sorted(os.listdir(src_dir)):
    p = os.path.join(src_dir, f)
    with open(p, 'rb') as fp:
        h = hashlib.sha256(fp.read()).hexdigest()
    hashes[h].append(f)

dups = {h: flist for h, flist in hashes.items() if len(flist) > 1}
if dups:
    print("Found duplicate checksums in bgeraser_results (1):", dups)
else:
    print(f"All {len(hashes)} PNG files in bgeraser_results (1) have 100% UNIQUE checksums!")

