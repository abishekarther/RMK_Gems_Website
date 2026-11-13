import urllib.request, urllib.parse, json

params = {
    'action': 'query',
    'generator': 'search',
    'gsrsearch': 'intitle:"cat\'s eye" OR intitle:"catseye" OR intitle:"chatoyant"',
    'gsrnamespace': '6',
    'gsrlimit': '15',
    'prop': 'imageinfo',
    'iiprop': 'url|size|extmetadata|mime',
    'iiurlwidth': '800',
    'format': 'json'
}
url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0'})
with urllib.request.urlopen(req) as r:
    d = json.loads(r.read().decode('utf-8'))
    for k, v in d['query']['pages'].items():
        info = v.get('imageinfo', [{}])[0]
        if 'image' in info.get('mime', ''):
            print(v['title'], '->', info.get('thumburl'))

