import urllib.request, urllib.parse, json, time, os

CANDIDATES_DIR = "scratch/candidates"
os.makedirs(CANDIDATES_DIR, exist_ok=True)

from fetch_real_stones import QUERIES

def search_wikimedia(query):
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': query,
        'gsrnamespace': '6',
        'gsrlimit': '3',
        'prop': 'imageinfo',
        'iiprop': 'url|mime|size|extmetadata',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (gemstone research)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            for pid, page in data.get('query', {}).get('pages', {}).items():
                info = page.get('imageinfo', [{}])[0]
                meta = info.get('extmetadata', {})
                mime = info.get('mime', '')
                if 'image' in mime and 'svg' not in mime and 'tif' not in mime:
                    desc = meta.get('ImageDescription', {}).get('value', '')
                    artist = meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                    license_name = meta.get('LicenseShortName', {}).get('value', 'CC')
                    url = info.get('url')
                    results.append({
                        'title': page.get('title'),
                        'url': url,
                        'artist': artist,
                        'license': license_name,
                        'description': desc,
                        'size': info.get('size'),
                        'width': info.get('width'),
                        'height': info.get('height')
                    })
            return results
    except Exception as e:
        return []

# Test run for first 10 queries
results_map = {}
for idx, (slug, q_list) in enumerate(list(QUERIES.items())[:10]):
    found = []
    for q in q_list:
        res = search_wikimedia(q)
        if res:
            found.extend(res)
            break
        time.sleep(0.3)
    results_map[slug] = found
    print(f"[{idx+1}/10] {slug}: found {len(found)} candidates")

with open('scratch/candidates_batch1.json', 'w') as f:
    json.dump(results_map, f, indent=2)

