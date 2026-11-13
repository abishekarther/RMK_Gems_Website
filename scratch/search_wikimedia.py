import urllib.request, urllib.parse, json, time, os

def search_wikimedia(query):
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': query,
        'gsrnamespace': '6',
        'gsrlimit': '5',
        'prop': 'imageinfo',
        'iiprop': 'url|mime|size|extmetadata',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (gemstone research educational)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            for pid, page in data.get('query', {}).get('pages', {}).items():
                info = page.get('imageinfo', [{}])[0]
                meta = info.get('extmetadata', {})
                mime = info.get('mime', '')
                if 'image' in mime and 'svg' not in mime:
                    results.append({
                        'title': page.get('title'),
                        'url': info.get('url'),
                        'license': meta.get('LicenseShortName', {}).get('value', 'CC'),
                        'artist': meta.get('Artist', {}).get('value', 'Wikimedia Commons'),
                        'width': info.get('width'),
                        'height': info.get('height')
                    })
            return results
    except Exception as e:
        return []

test_queries = [
    'malachite cabochon',
    'tiger eye cabochon',
    'lapis lazuli cabochon',
    'moonstone cabochon',
    'chrysoprase cabochon',
    'amethyst faceted oval',
    'emerald cut loose',
    'pyrite crystal macro'
]

for q in test_queries:
    res = search_wikimedia(q)
    print(f"\nQuery: {q} ({len(res)} results)")
    for r in res[:2]:
        print(f"  - {r['title']} | {r['license']} | {r['url']}")
    time.sleep(0.5)

