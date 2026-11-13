import json, os

CREDITS_FILE = 'scratch/all_credits.json'
with open(CREDITS_FILE, 'r', encoding='utf-8') as f:
    credits_map = json.load(f)

batch2_credits = {
    'chalcedony-white': ('Chalcedony White', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Estonian_Museum_of_Natural_History_Specimen_No_178049_photo_(g229_g229-412_jpg).jpg', 'Tiit Hunt', 'CC BY-SA 4.0'),
    'lemon-citrine': ('Lemon Citrine', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Citrine_taillee.jpg', 'Didier Descouens', 'CC BY-SA 4.0'),
    'pyrite': ('Pyrite', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Pyrite_-_Huanzala_mine,_Huallanca,_Bolognesi,_Ancash,_Peru.jpg', 'Ivar Leidus', 'CC BY-SA 4.0'),
    'white-quartz': ('White Quartz', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Quartz_Br%C3%A9sil.jpg', 'Didier Descouens', 'CC BY-SA 4.0'),
    'white-quartz-crystal': ('White Quartz Crystal', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Quartz-153424.jpg', 'Robert M. Lavinsky', 'CC BY-SA 3.0'),
    'tourmaline-green': ('Tourmaline Green', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Tourmaline_cut.JPG', 'Wikimedia Commons', 'CC BY-SA 3.0'),
    'lapis': ('Lapis', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Lapis2.jpg', 'Richard Seefeld', 'Public domain'),
    'white-topaz': ('White Topaz', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Chalmer%27s_Topaz.jpg', 'Annepetersen', 'CC BY-SA 3.0')
}

for s, (name, typ, src, auth, lic) in batch2_credits.items():
    credits_map[s] = {'name': name, 'type': typ, 'source_url': src, 'author': auth, 'license': lic}

with open(CREDITS_FILE, 'w', encoding='utf-8') as f:
    json.dump(credits_map, f, indent=2, ensure_ascii=False)

print(f"Updated credits map. Total cataloged stones: {len(credits_map)}")

