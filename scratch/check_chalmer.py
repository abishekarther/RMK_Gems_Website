import urllib.request, urllib.parse, json
params = {'action': 'query', 'titles': "File:Chalmer's Topaz.jpg", 'prop': 'imageinfo', 'iiprop': 'extmetadata', 'format': 'json'}
url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0'})
with urllib.request.urlopen(req) as r:
    d = json.loads(r.read().decode('utf-8'))
    for k, v in d['query']['pages'].items():
        meta = v.get('imageinfo', [{}])[0].get('extmetadata', {})
        print('Artist:', meta.get('Artist', {}).get('value'))
        print('License:', meta.get('LicenseShortName', {}).get('value'))

