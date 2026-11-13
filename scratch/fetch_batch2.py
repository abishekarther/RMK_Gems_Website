import urllib.request, urllib.parse, json, time, os, re

BATCH_2 = {
    'lapis': ['lapis lazuli cabochon', 'lapis lazuli polished', 'lapis lazuli oval'],
    'pyrite': ['pyrite crystal cube', 'pyrite mineral crystal', 'pyrite cluster'],
    'tourmaline-green': ['green tourmaline faceted', 'verdelite cut', 'tourmaline faceted green'],
    'white-topaz': ['colorless topaz', 'white topaz cut', 'faceted topaz colorless'],
    'chalcedony-white': ['white chalcedony', 'milky chalcedony', 'chalcedony white cabochon'],
    'white-quartz': ['milky quartz', 'snow quartz', 'white quartz pebble'],
    'white-quartz-crystal': ['rock crystal quartz point', 'clear quartz crystal', 'quartz crystal prism'],
    'lemon-citrine': ['citrine faceted', 'lemon quartz faceted', 'yellow citrine gem']
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
                    if any(bad in title_l for bad in ['ring', 'necklace', 'earring', 'tights', 'book', 'building', 'djvu', 'map', 'coin', 'stamp', 'portrait', 'pendant']):
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

batch2_results = {}
for slug, queries in BATCH_2.items():
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
    batch2_results[slug] = found

with open('scratch/batch2_candidates.json', 'w', encoding='utf-8') as f:
    json.dump(batch2_results, f, indent=2, ensure_ascii=False)

print("\nDone searching Batch 2!")

