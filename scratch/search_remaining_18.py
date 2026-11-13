import urllib.request, urllib.parse, json, time, os

BROADER_QUERIES = {
    'hematite-gunmetal': ['hematite', 'polished hematite'],
    'hessonite-garnet-semi-precious': ['hessonite', 'grossular'],
    'labradorite': ['labradorite', 'polished labradorite'],
    'onyx-multicolor': ['banded calcite', 'banded travertine'],
    'onyx-red': ['sardonyx', 'red sardonyx'],
    'quartz-cats-eye': ['chatoyant quartz', 'cats eye'],
    'rainbow-moonstone': ['rainbow moonstone', 'spectrolite'],
    'rose-quartz': ['rose quartz', 'polished rose quartz'],
    'rutilated-quartz-black-needle': ['tourmaline in quartz', 'tourmalinated quartz'],
    'rutile-quartz-golden-needle': ['rutilated quartz', 'rutile quartz'],
    'sillimanite-cats-eye': ['sillimanite', 'fibrolite'],
    'tourmaline-green': ['green tourmaline', 'verdelite'],
    'turquoise-chinese': ['turquoise', 'sleeping beauty turquoise'],
    'turquoise-tibetan': ['matrix turquoise', 'spiderweb turquoise'],
    'white-quartz': ['milky quartz', 'snow quartz'],
    'white-quartz-crystal': ['rock crystal quartz', 'quartz crystal'],
    'white-topaz': ['colorless topaz', 'white topaz'],
    'zircon-cubic-white': ['cubic zirconia', 'white zircon']
}

def search(q):
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': q,
        'gsrnamespace': '6',
        'gsrlimit': '3',
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
                if 'image' in mime and 'svg' not in mime and 'tif' not in mime:
                    title = page.get('title', '')
                    results.append({
                        'title': title,
                        'url': info.get('url'),
                        'page_url': f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}",
                        'artist': meta.get('Artist', {}).get('value', 'Wikimedia Commons'),
                        'license': meta.get('LicenseShortName', {}).get('value', 'CC'),
                    })
            return results
    except Exception as e:
        return []

results = {}
for slug, q_list in BROADER_QUERIES.items():
    found = []
    for q in q_list:
        res = search(q)
        if res:
            found.extend(res)
            break
        time.sleep(0.3)
    results[slug] = found
    print(f"{slug:32s}: found {len(found)} candidates")

with open('scratch/remaining_18_candidates.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

