import urllib.request, urllib.parse, json, time, os, re

BATCH_4 = {
    'onyx-green': ['green onyx', 'green banded calcite', 'green onyx marble'],
    'onyx-ivory': ['white onyx', 'ivory onyx', 'banded calcite white'],
    'onyx-multicolor': ['banded calcite', 'multicolor onyx', 'rainbow onyx marble'],
    'onyx-red': ['sardonyx', 'red onyx', 'carnelian onyx'],
    'onyx-red-pink': ['pink onyx', 'pink banded calcite', 'pink chalcedony'],
    'onyx-rose': ['rose onyx', 'pink marble polished', 'rose chalcedony'],
    'onyx-yellow': ['yellow onyx', 'honey onyx', 'yellow calcite polished'],
    'hessonite-garnet-semi-precious': ['grossular garnet cabochon', 'hessonite cabochon', 'hessonite garnet'],
    'pearl-fresh-water': ['freshwater pearl', 'baroque pearl', 'cultured pearl loose'],
    'rutilated-quartz-black-needle': ['tourmalinated quartz', 'tourmaline in quartz', 'black rutilated quartz'],
    'sapphire-blue-semi-precious': ['blue star sapphire', 'blue sapphire cabochon', 'blue corundum cabochon'],
    'zircon-cubic-white': ['cubic zirconia', 'white zircon faceted', 'colorless zircon']
}

def search_commons(query):
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': query,
        'gsrnamespace': '6',
        'gsrlimit': '6',
        'prop': 'imageinfo',
        'iiprop': 'url|size|extmetadata|mime',
        'iiurlwidth': '800',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research; contact@rmkgems.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            pages = data.get('query', {}).get('pages', {})
            for pid, page in pages.items():
                info = page.get('imageinfo', [{}])[0]
                meta = info.get('extmetadata', {})
                mime = info.get('mime', '')
                thumb = info.get('thumburl')
                title = page.get('title', '')
                if 'image' in mime and 'svg' not in mime and 'tif' not in mime and thumb:
                    title_l = title.lower()
                    if any(bad in title_l for bad in ['ring', 'necklace', 'earring', 'tights', 'book', 'building', 'djvu', 'map', 'coin', 'stamp', 'portrait', 'pdf']):
                        continue
                    artist = meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                    artist = re.sub(r'<[^>]+>', '', artist).strip()
                    license_name = meta.get('LicenseShortName', {}).get('value', 'CC BY-SA')
                    results.append({
                        'title': title,
                        'thumburl': thumb,
                        'page_url': f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}",
                        'license': license_name,
                        'artist': artist or 'Wikimedia Commons'
                    })
            return results
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

batch4_results = {}
for slug, queries in BATCH_4.items():
    print(f"Searching for {slug}...")
    found = []
    for q in queries:
        res = search_commons(q)
        if res:
            found.extend(res)
            print(f"  Query '{q}': found {len(res)} items")
            if len(found) >= 3:
                break
        time.sleep(0.3)
    batch4_results[slug] = found

with open('scratch/batch4_candidates.json', 'w', encoding='utf-8') as f:
    json.dump(batch4_results, f, indent=2, ensure_ascii=False)

print("\nDone searching Batch 4!")

