import urllib.request, urllib.parse, json, time, os

def get_category_files(cat_name, limit=10):
    url = f'https://commons.wikimedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:{urllib.parse.quote(cat_name)}&cmlimit={limit}&cmtype=file&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return [m['title'] for m in data.get('query', {}).get('categorymembers', [])]
    except Exception as e:
        return []

cats = [
    'Malachite', 'Lapis lazuli', "Tiger's eye", 'Moonstone', 'Labradorite',
    'Tourmaline', 'Topaz', 'Citrine', 'Pyrite', 'Hematite', 'Serpentine',
    'Chrysoprase', 'Onyx', 'Chalcedony', 'Sunstone', 'Smoky quartz',
    'Rose quartz', 'Rutilated quartz', 'Fluorite', 'Snowflake obsidian'
]

for cat in cats:
    files = get_category_files(cat, 5)
    print(f"Category:{cat} ({len(files)} files)")
    for f in files[:3]:
        print("  -", f)
    time.sleep(0.3)

