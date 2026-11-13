import urllib.request, urllib.parse, json

params = {
    'action': 'query',
    'generator': 'search',
    'gsrsearch': 'lapis lazuli cabochon',
    'gsrnamespace': '6',
    'gsrlimit': '6',
    'prop': 'imageinfo',
    'iiprop': 'url|size|extmetadata',
    'iiurlwidth': '800',
    'format': 'json'
}
url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research; contact@rmkgems.com)'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        raw = resp.read().decode('utf-8')
        data = json.loads(raw)
        print("Pages key:", list(data.get('query', {}).get('pages', {}).keys()))
        for pid, page in data.get('query', {}).get('pages', {}).items():
            print("Title:", page.get('title'))
            info = page.get('imageinfo', [{}])[0]
            print("Mime:", info.get('mime'))
            print("Thumb:", info.get('thumburl'))
except Exception as e:
    print("Error:", e)

