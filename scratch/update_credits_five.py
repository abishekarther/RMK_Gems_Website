import json, os

CREDITS_FILE = 'scratch/all_credits.json'
with open(CREDITS_FILE, 'r', encoding='utf-8') as f:
    credits_map = json.load(f)

five_credits = {
    'rutilated-quartz-black-needle': ('Rutilated Quartz Black Needle', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Tourmalinated_quartz_1.jpg', 'James St. John', 'CC BY 2.0'),
    'pearl-fresh-water': ('Pearl Fresh Water', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Pearl-freshwater_hg.jpg', 'Hannes Grobe', 'CC BY 3.0'),
    'sapphire-blue-semi-precious': ('Sapphire Blue (Semi-Precious)', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Eye_of_God_Star_Sapphire_Front_View.jpg', 'TheMaharlikan', 'CC0'),
    'zircon-cubic-white': ('Zircon Cubic White', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:CZ_brilliant.jpg', 'Gregory Phillips', 'CC BY-SA 3.0'),
    'hessonite-garnet-semi-precious': ('Hessonite Garnet (Semi-Precious)', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Hessonite_(grossular_variety)_Ca3Al2Si3O12_(42302997570).jpg', 'Jan Helebrant', 'CC BY-SA 2.0')
}

for s, (name, typ, src, auth, lic) in five_credits.items():
    credits_map[s] = {'name': name, 'type': typ, 'source_url': src, 'author': auth, 'license': lic}

with open(CREDITS_FILE, 'w', encoding='utf-8') as f:
    json.dump(credits_map, f, indent=2, ensure_ascii=False)

print(f"Updated credits map. Total cataloged stones: {len(credits_map)}")

