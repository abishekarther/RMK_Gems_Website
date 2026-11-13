import json, urllib.request, time, os
from PIL import Image

os.makedirs('scratch/downloaded', exist_ok=True)

with open('scratch/all_candidates.json', 'r', encoding='utf-8') as f:
    candidates = json.load(f)

# List of already converted stones
done_slugs = {
    'ruby', 'pearl', 'red-coral', 'emerald', 'yellow-sapphire', 'diamond',
    'garnet-rose-cut-checkerboard', 'goldstone-sandstone-blue', 'goldstone-sandstone-red',
    'aventurine-green', 'bloodstone', 'blue-lace-banded-agate', 'carnelian',
    'cats-eye-chrysoberyl', 'chalcedony-blue', 'amethyst-african', 'amethyst-brazil',
    'aquamarine-yellow', 'ruby-markara'
}

downloaded = []

for slug, items in candidates.items():
    if slug in done_slugs:
        continue
    for item in items:
        url = item.get('url', '')
        title = item.get('title', '')
        # Skip books, djvu, rings
        if any(ext in url.lower() for ext in ['.djvu', '.pdf', '.tif']):
            continue
        if any(word in title.lower() for word in ['finger ring', 'medieval', 'vase', 'tights', 'norwood', 'jewellery']):
            continue
            
        dest = f"scratch/downloaded/{slug}.jpg"
        if os.path.exists(dest):
            break
            
        print(f"Downloading for {slug}: {title}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational gemstone research)'})
            with urllib.request.urlopen(req, timeout=15) as resp, open(dest, 'wb') as f:
                f.write(resp.read())
            im = Image.open(dest)
            print(f"  -> Success: {im.size} {im.mode}")
            downloaded.append({
                'slug': slug,
                'path': dest,
                'title': title,
                'license': item.get('license'),
                'artist': item.get('artist'),
                'page_url': item.get('page_url')
            })
            time.sleep(1.2)
            break
        except Exception as e:
            print(f"  -> Error: {e}")
            time.sleep(1.2)

print(f"\nTotal downloaded candidates in this pass: {len(downloaded)}")
with open('scratch/downloaded_meta.json', 'w', encoding='utf-8') as f:
    json.dump(downloaded, f, indent=2, ensure_ascii=False)

