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
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        results = []
        for pid, p in pages.items():
            info = p.get('imageinfo', [{}])[0]
            thumb = info.get('thumburl')
            title = p.get('title', '')
            if thumb and not any(bad in title.lower() for bad in ['ring', 'necklace', 'earring', 'book', 'pdf', 'map', 'temple', 'building']):
                results.append((title, thumb))
        return results

terms = [
    'sardonyx',
    'sardonyx cabochon',
    '"banded calcite"',
    'travertine polished',
    'rhodochrosite cabochon',
    'pink chalcedony',
    'yellow calcite crystal',
    'green chalcedony cabochon',
    'honey calcite'
]

for t in terms:
    print(f"\n--- {t} ---")
    res = search(t)
    for title, url in res[:3]:
        print(f"  {title} -> {url}")

