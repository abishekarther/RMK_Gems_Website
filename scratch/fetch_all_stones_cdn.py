import urllib.request, urllib.parse, json, time, os
from PIL import Image

OUT_DIR = "scratch/cdn_candidates"
os.makedirs(OUT_DIR, exist_ok=True)

# List of already finalized stones in frontend/public/images/stones:
finalized = {
    'amethyst-african', 'amethyst-brazil', 'aventurine-green', 'bloodstone', 'blue-lace-banded-agate',
    'blue-sapphire', 'carnelian', 'cats-eye-chrysoberyl', 'chalcedony-blue', 'chrysoprase',
    'diamond', 'emerald', 'garnet-almandine', 'garnet-rose-cut-checkerboard', 'goldstone-sandstone-blue',
    'goldstone-sandstone-red', 'labradorite', 'malachite', 'moonstone-white', 'onyx-black',
    'opal-dendrite', 'pearl', 'rainbow-moonstone', 'red-coral', 'ruby',
    'rutile-quartz-golden-needle', 'tiger-eye', 'yellow-sapphire',
    'aquamarine-yellow', 'ruby-markara'
}

SEARCH_TERMS = {
    'blue-sapphire': ['faceted blue sapphire', 'blue sapphire cut', 'blue sapphire oval'],
    'hessonite-garnet': ['hessonite garnet', 'hessonite faceted', 'cinnamon stone'],
    'agate-black-banded': ['banded black agate', 'black agate', 'banded agate'],
    'agate-green-banded': ['green banded agate', 'green agate', 'banded green chalcedony'],
    'agate-red-jasper': ['red jasper polished', 'red jasper cabochon', 'jasper red'],
    'amethyst-brazil-pink': ['pink quartz', 'rose amethyst', 'pink chalcedony'],
    'chalcedony-white': ['white chalcedony', 'milky chalcedony', 'white agate'],
    'chrysoprase': ['chrysoprase cabochon', 'chrysoprase polished', 'chrysoprase'],
    'diopside-4-ray-star': ['star diopside', 'diopside star', 'black star diopside'],
    'fluorite-multicolor-banded': ['fluorite polished', 'banded fluorite', 'rainbow fluorite'],
    'green-serpentine': ['serpentine polished', 'bowenite', 'green serpentine'],
    'hematite-gunmetal': ['hematite polished', 'hematite cabochon', 'hematite'],
    'hessonite-garnet-semi-precious': ['grossular garnet', 'hessonite cabochon', 'hessonite'],
    'labradorite': ['labradorite polished', 'labradorite cabochon', 'labradorescence'],
    'lapis': ['lapis lazuli polished', 'lapis cabochon', 'lapis lazuli'],
    'lemon-citrine': ['citrine faceted', 'yellow citrine', 'citrine cut'],
    'malachite': ['malachite polished', 'malachite cabochon', 'banded malachite'],
    'moonstone-white': ['moonstone cabochon', 'adularia moonstone', 'white moonstone'],
    'obsidian-snowflake': ['snowflake obsidian', 'obsidian snowflake', 'snowflake obsidian polished'],
    'onyx-black': ['black onyx', 'black chalcedony', 'polished onyx'],
    'onyx-green': ['green onyx', 'green banded calcite', 'green marble onyx'],
    'onyx-ivory': ['white onyx', 'ivory onyx', 'banded calcite'],
    'onyx-multicolor': ['banded calcite', 'multicolor onyx', 'travertine onyx'],
    'onyx-red': ['sardonyx', 'red onyx', 'carnelian onyx'],
    'onyx-red-pink': ['pink onyx', 'rhodochrosite', 'pink agate'],
    'onyx-rose': ['rose onyx', 'pink chalcedony', 'rose quartz cabochon'],
    'onyx-yellow': ['yellow onyx', 'honey onyx', 'yellow calcite'],
    'opal-dendrite': ['dendritic agate', 'dendritic opal', 'merlinite'],
    'pearl-fresh-water': ['freshwater pearl', 'baroque pearl', 'cultured pearl'],
    'pyrite': ['pyrite cubic', 'iron pyrite', 'pyrite crystal'],
    'quartz-cats-eye': ['chatoyant quartz', 'cats eye quartz', 'quartz cats eye'],
    'rainbow-moonstone': ['rainbow moonstone', 'white labradorite', 'spectrolite'],
    'rose-quartz': ['rose quartz polished', 'rose quartz cabochon', 'rose quartz'],
    'rutilated-quartz-black-needle': ['tourmalinated quartz', 'tourmaline in quartz', 'black rutilated quartz'],
    'rutile-quartz-golden-needle': ['rutilated quartz', 'golden rutilated quartz', 'rutile quartz'],
    'sapphire-blue-semi-precious': ['blue star sapphire', 'blue corundum cabochon', 'sapphire cabochon'],
    'sillimanite-cats-eye': ['sillimanite', 'fibrolite', 'sillimanite cats eye'],
    'smoky-quartz': ['smoky quartz faceted', 'smoky quartz cut', 'cairngorm'],
    'spectrolite-cats-eye': ['spectrolite', 'spectrolite finland', 'spectrolite cabochon'],
    'sunstone': ['sunstone cabochon', 'oregon sunstone', 'aventurine feldspar'],
    'tiger-eye': ['tiger eye cabochon', 'tigers eye', 'tiger eye polished'],
    'tourmaline-green': ['green tourmaline faceted', 'verdelite cut', 'tourmaline faceted'],
    'turquoise-chinese': ['turquoise cabochon', 'persian turquoise', 'blue turquoise'],
    'turquoise-tibetan': ['matrix turquoise', 'spiderweb turquoise', 'tibetan turquoise'],
    'white-quartz': ['milky quartz', 'snow quartz', 'white quartz'],
    'white-quartz-crystal': ['rock crystal quartz', 'clear quartz crystal', 'quartz point'],
    'white-topaz': ['colorless topaz', 'white topaz faceted', 'clear topaz'],
    'zircon-cubic-white': ['cubic zirconia', 'white zircon', 'colorless zircon']
}

def search_wikimedia_cdn(query):
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': query,
        'gsrnamespace': '6',
        'gsrlimit': '5',
        'prop': 'imageinfo',
        'iiprop': 'url|size|extmetadata',
        'iiurlwidth': '800',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research; contact@rmkgems.com)'})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = []
            pages = data.get('query', {}).get('pages', {})
            for pid, page in pages.items():
                info = page.get('imageinfo', [{}])[0]
                meta = info.get('extmetadata', {})
                mime = info.get('mime', '')
                thumb = info.get('thumburl')
                title = page.get('title', '')
                if 'image' in mime and 'svg' not in mime and 'tif' not in mime and thumb:
                    # Filter out books, rings, jewellery
                    title_l = title.lower()
                    if any(bad in title_l for bad in ['ring', 'necklace', 'earring', 'tights', 'book', 'museum building', 'djvu', 'map']):
                        continue
                    results.append({
                        'title': title,
                        'thumburl': thumb,
                        'page_url': f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(title.replace(' ', '_'))}",
                        'license': meta.get('LicenseShortName', {}).get('value', 'CC'),
                        'artist': meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                    })
            return results
    except Exception as e:
        return []

results_catalog = {}

for idx, (slug, q_list) in enumerate(SEARCH_TERMS.items(), 1):
    if slug in finalized:
        continue
    found = []
    for q in q_list:
        res = search_wikimedia_cdn(q)
        if res:
            found.extend(res)
            if len(found) >= 2:
                break
        time.sleep(0.4)
    results_catalog[slug] = found
    print(f"[{idx:2d}/{len(SEARCH_TERMS)}] {slug:32s}: found {len(found)} candidates")

with open('scratch/cdn_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(results_catalog, f, indent=2, ensure_ascii=False)

print("\nFinished querying CDN thumbnails for all remaining stones!")
