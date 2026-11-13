import json, os

CREDITS_FILE = 'scratch/all_credits.json'
with open(CREDITS_FILE, 'r', encoding='utf-8') as f:
    credits_map = json.load(f)

onyx_credits = {
    'onyx-multicolor': ('Onyx Multicolor', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Calcite,_stalgmitic,_banded,_polished,_Tyuya-Muyun,_Russian_Turkestan_-_Natural_History_Museum,_London_-_DSC05335.jpg', 'Daderot', 'CC0'),
    'onyx-red': ('Onyx Red', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Red_onyx.jpg', 'Pureales', 'CC BY-SA 4.0'),
    'onyx-ivory': ('Onyx Ivory', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Clear_White_Yellow_Onyx_IMG_9477.jpg', 'Aomorikuma', 'CC BY-SA 4.0'),
    'onyx-yellow': ('Onyx Yellow', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Calcite-241250.jpg', 'Robert M. Lavinsky', 'CC BY-SA 3.0'),
    'onyx-rose': ('Onyx Rose', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Cut_and_polished_section_of_stalactite_of_banded_rhodochrosite.jpg', 'Gerd A.T. Müller', 'CC BY-SA 3.0'),
    'onyx-red-pink': ('Onyx Red (Pink)', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Estonian_Museum_of_Natural_History_Specimen_No_178046_photo_(g229_g229-409_jpg).jpg', 'Tiit Hunt', 'CC BY-SA 4.0'),
    'onyx-green': ('Onyx Green', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Chrome_chalcedony_from_Kurdistan,_Iraq._Erbil_Stones_and_Gems_Museum,_Erbil_Citadel,_Hawler,_Iraq.jpg', 'Osama Shukir Muhammed Amin FRCP(Glasg)', 'CC BY-SA 4.0')
}

for s, (name, typ, src, auth, lic) in onyx_credits.items():
    credits_map[s] = {'name': name, 'type': typ, 'source_url': src, 'author': auth, 'license': lic}

with open(CREDITS_FILE, 'w', encoding='utf-8') as f:
    json.dump(credits_map, f, indent=2, ensure_ascii=False)

print(f"Updated credits map. Total cataloged stones: {len(credits_map)}")

