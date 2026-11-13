import urllib.request, urllib.parse, json

def search(q):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=3&prop=imageinfo&iiprop=url|size&iiurlwidth=800&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return [p.get('title') for pid, p in data.get('query', {}).get('pages', {}).items()]
    except Exception as e:
        return []

queries = [
    'intitle:onyx intitle:cabochon',
    'intitle:malachite intitle:cabochon',
    'intitle:tiger intitle:cabochon',
    'intitle:moonstone intitle:cabochon',
    'intitle:labradorite intitle:cabochon',
    'intitle:hematite intitle:cabochon',
    'intitle:serpentine intitle:cabochon',
    'intitle:jasper intitle:cabochon',
    'intitle:sunstone intitle:cabochon',
    'intitle:topaz intitle:faceted',
    'intitle:tourmaline intitle:faceted',
    'intitle:citrine intitle:faceted',
    'intitle:rutile intitle:quartz'
]

for q in queries:
    res = search(q)
    print(f"{q}: {res}")

