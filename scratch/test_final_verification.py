import os
import hashlib
import json

def get_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def test_verification():
    semi_dir = r'c:\RMK_Gems_Website\semiprecious_stones_images'
    pub_dir = r'c:\RMK_Gems_Website\frontend\public\images\stones'
    
    with open('scratch/user_table.json', 'r', encoding='utf-8') as f:
        user_table = json.load(f)
        
    print(f"=== 1. Checking {len(user_table)} Target Files in semiprecious_stones_images ===")
    missing_in_semi = []
    hashes_semi = {}
    for item in user_table:
        target = item['target'].strip('`')
        fn = f"{target}.webp"
        p = os.path.join(semi_dir, fn)
        if not os.path.exists(p):
            missing_in_semi.append(fn)
        else:
            h = get_hash(p)
            hashes_semi.setdefault(h, []).append(fn)
            
    if missing_in_semi:
        print(f"FAILED: Missing in {semi_dir}: {missing_in_semi}")
    else:
        print(f"SUCCESS: All {len(user_table)} files exist in {semi_dir}.")
        
    duplicates_semi = {h: fns for h, fns in hashes_semi.items() if len(fns) > 1}
    if duplicates_semi:
        print(f"FAILED: Found duplicate images in {semi_dir}: {duplicates_semi}")
    else:
        print(f"SUCCESS: All 59 files in {semi_dir} are completely unique (0 duplicates)!")

    print(f"\n=== 2. Checking Public Stones in {pub_dir} ===")
    missing_in_pub = []
    for item in user_table:
        target = item['target'].strip('`')
        fn = f"{target}.webp"
        p = os.path.join(pub_dir, fn)
        if not os.path.exists(p) or os.path.getsize(p) == 0:
            missing_in_pub.append(fn)
            
    if missing_in_pub:
        print(f"FAILED: Missing in {pub_dir}: {missing_in_pub}")
    else:
        print(f"SUCCESS: All 59 files exist in {pub_dir} with valid sizes.")

    print(f"\n=== 3. Checking Frontend GEMSTONE_PHOTOS Registry ===")
    import re
    with open(r'c:\RMK_Gems_Website\frontend\src\data\gemstonePhotos.ts', 'r', encoding='utf-8') as f:
        content = f.read()
        
    mappings = re.findall(r"'([a-z0-9\-]+)':\s*'/images/stones/([a-z0-9\-\.]+)'", content)
    print(f"Total mappings in gemstonePhotos.ts: {len(mappings)}")
    
    placeholders = [m for m in mappings if 'placeholder' in m[1]]
    if placeholders:
        print(f"WARNING: Still pointing to placeholder: {placeholders}")
    else:
        print("SUCCESS: 0 placeholders in gemstonePhotos.ts!")
        
    missing_targets = []
    for slug, img_name in mappings:
        img_path = os.path.join(pub_dir, img_name)
        if not os.path.exists(img_path):
            missing_targets.append((slug, img_name))
            
    if missing_targets:
        print(f"FAILED: Files referenced in gemstonePhotos.ts that do not exist: {missing_targets}")
    else:
        print(f"SUCCESS: All {len(mappings)} entries in gemstonePhotos.ts resolve to physical images on disk.")

if __name__ == '__main__':
    test_verification()

