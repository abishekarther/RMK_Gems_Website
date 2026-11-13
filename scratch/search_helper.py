import urllib.request, urllib.parse, json, sys

def search_wikimedia(query, limit=5):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&gsrlimit={limit}&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=800&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            for pid, p in data.get('query', {}).get('pages', {}).items():
                info = p.get('imageinfo', [{}])[0]
                meta = info.get('extmetadata', {})
                results.append({
                    'title': p.get('title'),
                    'thumburl': info.get('thumburl'),
                    'original': info.get('url'),
                    'license': meta.get('LicenseShortName', {}).get('value', 'CC'),
                    'artist': meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                })
            return results
    except Exception as e:
        print("Search error:", e)
        return []

if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else 'hessonite'
    res = search_wikimedia(q)
    print(f"Results for '{q}': {len(res)}")
    for r in res:
        print(f"  {r['title']}\n    {r['license']} | {r['artist']}\n    {r['thumburl']}\n")

