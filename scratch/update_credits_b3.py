import json, os

CREDITS_FILE = 'scratch/all_credits.json'
with open(CREDITS_FILE, 'r', encoding='utf-8') as f:
    credits_map = json.load(f)

batch3_credits = {
    'diopside-4-ray-star': ('Diopside 4-ray Star', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Diopside_Star.jpg', 'Mr.Auger', 'CC BY-SA 4.0'),
    'green-serpentine': ('Green Serpentine', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Chatoyant_serpentine_01.jpg', 'Astynax', 'CC0'),
    'turquoise-chinese': ('Turquoise CHINESE', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Turquoise_(Blue_Moon_Mine,_Candelaria_Hills,_west_of_Tonopah,_Nevada,_USA)_1.jpg', 'James St. John', 'CC BY 2.0'),
    'turquoise-tibetan': ('Turquoise Tibetan', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Turquoise_(Ithaca_Peak_Mine,_near_Kingman,_Arizona,_USA)_1.jpg', 'James St. John', 'CC BY 2.0'),
    'amethyst-brazil-pink': ('Amethyst Brazil Pink', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Pink_amethyst.jpg', 'Géry PARENT', 'CC BY-SA 4.0'),
    'fluorite-multicolor-banded': ('Fluorite Multicolor Banded', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Fluorite_(mine_near_Cave-in-Rock,_Illinois,_USA)_3.jpg', 'James St. John', 'CC BY 2.0'),
    'agate-black-banded': ('Agate Black Banded', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:A_selection_of_gem_cabochons_and_nacre_1.jpg', 'W.carter', 'CC BY 4.0'),
    'agate-green-banded': ('Agate Green Banded', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:A_selection_of_gem_cabochons_and_nacre_1.jpg', 'W.carter', 'CC BY 4.0'),
    'agate-red-jasper': ('Agate Red Jasper', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:A_selection_of_gem_cabochons_and_nacre_1.jpg', 'W.carter', 'CC BY 4.0'),
    'spectrolite-cats-eye': ('Spectrolite Cat\'s Eye', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Labradorite_(Wiborg_Batholith,_1633_Ma;_Kymi_Province,_Finland)_2.jpg', 'James St. John', 'CC BY 2.0'),
    'quartz-cats-eye': ('Quartz Cat\'s Eye', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Cymophane.jpg', 'Gemshare', 'CC BY-SA 3.0'),
    'sillimanite-cats-eye': ('Sillimanite Cat\'s Eye', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Catseyechrysoberyl.jpg', 'Stickpen', 'Public domain')
}

for s, (name, typ, src, auth, lic) in batch3_credits.items():
    credits_map[s] = {'name': name, 'type': typ, 'source_url': src, 'author': auth, 'license': lic}

with open(CREDITS_FILE, 'w', encoding='utf-8') as f:
    json.dump(credits_map, f, indent=2, ensure_ascii=False)

print(f"Updated credits map. Total cataloged stones: {len(credits_map)}")

