import urllib.request, json, os
from PIL import Image

def dl(url, path):
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (gemstone research educational)'})
    with urllib.request.urlopen(req, timeout=15) as resp, open(path, 'wb') as f:
        f.write(resp.read())

candidates_to_test = [
    # Amethyst
    ('amethyst-african', 'https://upload.wikimedia.org/wikipedia/commons/e/ed/Amethystetaille.jpg', 'CC BY-SA 3.0', 'Didier Descouens'),
    ('amethyst-brazil', 'https://upload.wikimedia.org/wikipedia/commons/a/ab/Amethyst_%28faceted%29_1.jpg', 'CC BY 2.0', 'James St. John'),
    # Chrysoberyl & Star
    ('diopside-4-ray-star', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Star_diopside.JPG/800px-Star_diopside.JPG', 'CC BY-SA 3.0', 'Ra\'ike'),
    # Tiger eye
    ('tiger-eye', 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Tigers-Eye.jpg', 'Public domain', 'Wikimedia Commons'),
    # Malachite
    ('malachite', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Malachite_jewellery_arp.jpg/800px-Malachite_jewellery_arp.jpg', 'Public domain', 'Adrian Pingstone'),
    # Moonstone
    ('moonstone-white', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Moonstone.cabochons.arp.jpg/800px-Moonstone.cabochons.arp.jpg', 'Public domain', 'Adrian Pingstone'),
    # Chrysoprase
    ('chrysoprase', 'https://upload.wikimedia.org/wikipedia/commons/a/a7/Chrysoprase_%28Australia%29_5.jpg', 'CC BY 2.0', 'James St. John'),
    # Garnet almandine
    ('garnet-almandine', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Almandine_oval_faceted.jpg/800px-Almandine_oval_faceted.jpg', 'CC BY-SA 3.0', 'Didier Descouens'),
    # Pyrite
    ('pyrite', 'https://upload.wikimedia.org/wikipedia/commons/1/14/Pyrite_Cube_Corner_-_Flickr_-_places_lost.jpg', 'CC BY 2.0', 'places lost'),
    # Lapis
    ('lapis', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Lapis-lazuli_cabochon.jpg/800px-Lapis-lazuli_cabochon.jpg', 'CC BY-SA 3.0', 'Didier Descouens'),
    # Obsidian snowflake
    ('obsidian-snowflake', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Snowflake_obsidian_pebble.jpg/800px-Snowflake_obsidian_pebble.jpg', 'CC BY-SA 4.0', 'Ji-Elle'),
    # Fluorite
    ('fluorite-multicolor-banded', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Fluorite_-_polished.jpg/800px-Fluorite_-_polished.jpg', 'CC BY-SA 3.0', 'Didier Descouens'),
]

os.makedirs('scratch/test_dl', exist_ok=True)
for slug, url, lic, author in candidates_to_test:
    dest = f'scratch/test_dl/{slug}.jpg'
    try:
        dl(url, dest)
        im = Image.open(dest)
        print(f"Downloaded {slug}: {im.size} {im.mode}")
    except Exception as e:
        print(f"Failed {slug}: {e}")

