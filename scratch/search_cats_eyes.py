import urllib.request, urllib.parse, json

def search(q):
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': q,
        'gsrnamespace': '6',
        'gsrlimit': '8',
        'prop': 'imageinfo',
        'iiprop': 'url|size|extmetadata|mime',
        'iiurlwidth': '800',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            results = []
            for pid, p in pages.items():
                info = p.get('imageinfo', [{}])[0]
                thumb = info.get('thumburl')
                title = p.get('title', '')
                if thumb and not any(bad in title.lower() for bad in ['ring', 'necklace', 'earring', 'book', 'pdf']):
                    meta = info.get('extmetadata', {})
                    artist = meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                    license_name = meta.get('LicenseShortName', {}).get('value', 'CC BY-SA')
                    results.append((title, thumb, artist, license_name))
            return results
    except Exception as e:
        print(f"Error {q}: {e}")
        return []

queries = {
    'quartz-cats-eye': ['chatoyant quartz', 'cats eye quartz cabochon', 'quartz cats eye'],
    'sillimanite-cats-eye': ['sillimanite', 'fibrolite', 'sillimanite cats eye'],
    'spectrolite-cats-eye': ['spectrolite cabochon', 'spectrolite finland', 'spectrolite polished'],
    'amethyst-brazil-pink': ['pink amethyst', 'rose quartz cabochon', 'pink chalcedony cabochon'],
    'green-serpentine': ['serpentine cabochon', 'bowenite polished', 'green serpentine stone'],
    'turquoise-chinese': ['turquoise cabochon', 'hubei turquoise', 'blue turquoise cabochon'],
    'turquoise-tibetan': ['tibetan turquoise', 'matrix turquoise cabochon', 'spiderweb turquoise cabochon']
}

out = {}
for slug, q_list in queries.items():
    print(f"\nSearching for {slug}...")
    found = []
    for q in q_list:
        res = search(q)
        if res:
            found.extend(res)
            print(f"  {q}: found {len(res)} items")
            if len(found) >= 3:
                break
    out[slug] = found

with open('scratch/cats_and_others.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print("\nDone searching cats eyes and others!")

