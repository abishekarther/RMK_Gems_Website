import urllib.request, urllib.parse, json, time, os

CANDIDATES_DIR = "scratch/candidates"
os.makedirs(CANDIDATES_DIR, exist_ok=True)

QUERIES_51 = {
    'blue-sapphire': ['faceted sapphire loose', 'blue sapphire oval faceted', 'sapphire faceted'],
    'hessonite-garnet': ['hessonite garnet faceted', 'hessonite garnet cabochon', 'grossular hessonite'],
    'agate-black-banded': ['black banded agate', 'black agate cabochon', 'banded agate polished'],
    'agate-green-banded': ['green banded agate', 'green agate cabochon', 'moss agate cabochon'],
    'agate-red-jasper': ['red jasper cabochon', 'red jasper polished', 'jasper cabochon'],
    'amethyst-african': ['amethyst faceted oval', 'amethyst gemstone cut', 'amethyst oval'],
    'amethyst-brazil': ['amethyst faceted', 'amethyst cut loose', 'amethyst gemstone'],
    'amethyst-brazil-pink': ['pink amethyst cabochon', 'rose amethyst', 'pink quartz cabochon'],
    'chalcedony-white': ['white chalcedony cabochon', 'milky chalcedony', 'white agate cabochon'],
    'chrysoprase': ['chrysoprase cabochon', 'chrysoprase polished', 'chrysoprase gemstone'],
    'diopside-4-ray-star': ['star diopside', 'black star diopside', 'diopside cabochon'],
    'fluorite-multicolor-banded': ['rainbow fluorite cabochon', 'banded fluorite', 'fluorite polished'],
    'garnet-almandine': ['almandine garnet faceted', 'almandine cut', 'garnet faceted'],
    'green-serpentine': ['serpentine cabochon', 'green serpentine polished', 'bowenite'],
    'hematite-gunmetal': ['hematite cabochon', 'polished hematite', 'hematite gemstone'],
    'hessonite-garnet-semi-precious': ['hessonite cabochon', 'grossular garnet cabochon', 'hessonite stone'],
    'labradorite': ['labradorite cabochon', 'spectrolite cabochon', 'labradorite polished'],
    'lapis': ['lapis lazuli cabochon', 'lapis cabochon', 'lapis polished'],
    'lemon-citrine': ['lemon citrine', 'citrine faceted', 'yellow citrine'],
    'malachite': ['malachite cabochon', 'banded malachite', 'malachite polished'],
    'moonstone-white': ['white moonstone cabochon', 'moonstone cabochon', 'adularia cabochon'],
    'obsidian-snowflake': ['snowflake obsidian cabochon', 'snowflake obsidian', 'obsidian cabochon'],
    'onyx-black': ['black onyx cabochon', 'black chalcedony', 'polished black onyx'],
    'onyx-green': ['green onyx cabochon', 'green banded calcite', 'green onyx'],
    'onyx-ivory': ['white onyx cabochon', 'ivory onyx', 'banded calcite white'],
    'onyx-multicolor': ['banded onyx cabochon', 'multicolor onyx', 'banded calcite'],
    'onyx-red': ['red onyx cabochon', 'sardonyx cabochon', 'red carnelian onyx'],
    'onyx-red-pink': ['pink onyx cabochon', 'rhodochrosite cabochon', 'pink banded agate'],
    'onyx-rose': ['rose onyx cabochon', 'pink chalcedony cabochon', 'pink agate'],
    'onyx-yellow': ['yellow onyx cabochon', 'honey onyx', 'yellow calcite cabochon'],
    'opal-dendrite': ['dendritic opal cabochon', 'dendritic agate cabochon', 'merlinite'],
    'pearl-fresh-water': ['freshwater pearl loose', 'baroque pearl white', 'freshwater pearl'],
    'pyrite': ['pyrite crystal macro', 'pyrite cluster', 'iron pyrite'],
    'quartz-cats-eye': ['quartz cats eye', 'cats eye quartz cabochon', 'chatoyant quartz'],
    'rainbow-moonstone': ['rainbow moonstone cabochon', 'white labradorite cabochon'],
    'rose-quartz': ['rose quartz cabochon', 'rose quartz polished', 'pink quartz'],
    'rutilated-quartz-black-needle': ['tourmalinated quartz cabochon', 'tourmaline in quartz', 'black rutilated quartz'],
    'rutile-quartz-golden-needle': ['golden rutilated quartz cabochon', 'rutilated quartz cabochon', 'rutile in quartz'],
    'sapphire-blue-semi-precious': ['blue sapphire cabochon', 'star sapphire cabochon', 'opaque sapphire'],
    'sillimanite-cats-eye': ['sillimanite cats eye', 'fibrolite cabochon', 'sillimanite cabochon'],
    'smoky-quartz': ['smoky quartz faceted', 'smoky quartz cut', 'cairngorm faceted'],
    'spectrolite-cats-eye': ['spectrolite cabochon', 'spectrolite finland', 'spectrolite flash'],
    'sunstone': ['sunstone cabochon', 'oregon sunstone', 'sunstone feldspar'],
    'tiger-eye': ['tigers eye cabochon', 'tiger eye cabochon', 'tiger eye polished'],
    'tourmaline-green': ['green tourmaline faceted', 'verdelite faceted', 'tourmaline cut'],
    'turquoise-chinese': ['turquoise cabochon blue', 'turquoise polished', 'blue turquoise cabochon'],
    'turquoise-tibetan': ['tibetan turquoise cabochon', 'spiderweb turquoise', 'matrix turquoise cabochon'],
    'white-quartz': ['snow quartz cabochon', 'milky quartz cabochon', 'white quartz polished'],
    'white-quartz-crystal': ['quartz crystal point', 'rock crystal prism', 'clear quartz crystal'],
    'white-topaz': ['white topaz faceted', 'colorless topaz faceted', 'clear topaz'],
    'zircon-cubic-white': ['white zircon faceted', 'colorless zircon', 'cubic zirconia']
}

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
                    title = page.get('title', '')
                    page_url = f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}"
                    results.append({
                        'title': title,
                        'url': info.get('url'),
                        'page_url': page_url,
                        'artist': meta.get('Artist', {}).get('value', 'Wikimedia Commons'),
                        'license': meta.get('LicenseShortName', {}).get('value', 'CC'),
                        'description': meta.get('ImageDescription', {}).get('value', '')[:200]
                    })
            return results
    except Exception as e:
        return []

all_candidates = {}
for idx, (slug, queries) in enumerate(QUERIES_51.items(), 1):
    found = []
    for q in queries:
        res = search_wikimedia(q)
        if res:
            found.extend(res)
            if len(found) >= 2:
                break
        time.sleep(0.2)
    all_candidates[slug] = found
    print(f"[{idx:2d}/{len(QUERIES_51)}] {slug:32s}: found {len(found)} candidates")

with open('scratch/all_candidates.json', 'w', encoding='utf-8') as f:
    json.dump(all_candidates, f, indent=2, ensure_ascii=False)

print("\nDone searching all 51 stones! Saved to scratch/all_candidates.json")

