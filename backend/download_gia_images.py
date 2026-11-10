import httpx
import os
import time

out_dir = 'frontend/public/images/gia'
os.makedirs(out_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.gia.edu/gem-encyclopedia'
}

gia_images = {
    'ruby': 'https://www.gia.edu/dam/gemstones/ruby/polished-ruby.png',
    'emerald': 'https://www.gia.edu/dam/gemstones/Image/polished-emerald-gem.png',
    'blue-sapphire': 'https://www.gia.edu/dam/gemstones/sapphire/overview/polished-sapphire.png',
    'yellow-sapphire': 'https://www.gia.edu/dam/gemstones/citrine/overview/polished-citrine-gem.png',
    'diamond': 'https://www.gia.edu/dam/gemstones/diamond/overview/polished-diamond.png',
    'pearl': 'https://www.gia.edu/dam/gemstones/pearl/overview/polished-perl.png',
    'hessonite-garnet': 'https://www.gia.edu/dam/gemstones/garnet/overview/garnet-polished-gem.png',
    'cats-eye-chrysoberyl': 'https://www.gia.edu/dam/gemstones/sunstone/overview/polished-sunstone.png',
    'red-coral': 'https://www.gia.edu/dam/gemstones/spinel/gem-overview/polished-spinel.png',
    'amethyst': 'https://www.gia.edu/dam/gemstones/amethyst/overview/amethyst.png',
    'aquamarine': 'https://www.gia.edu/dam/gemstones/aquamarine/overview/polished-aquamarine-gem.png',
    'citrine': 'https://www.gia.edu/dam/gemstones/citrine/overview/polished-citrine-gem.png',
    'garnet': 'https://www.gia.edu/dam/gemstones/garnet/overview/garnet-polished-gem.png',
    'lapis': 'https://www.gia.edu/dam/gemstones/lapis-lazuli/overview/polished-lapis-lazuli.png',
    'moonstone': 'https://www.gia.edu/dam/gemstones/moonstone/overview/polished-moonstone.png',
    'opal': 'https://www.gia.edu/dam/gemstones/opal/gem-overview/polished-opal.png',
    'rose-quartz': 'https://www.gia.edu/dam/gemstones/rose-quartz/polished-rose-quartz.png',
    'sunstone': 'https://www.gia.edu/dam/gemstones/sunstone/overview/polished-sunstone.png',
    'topaz': 'https://www.gia.edu/dam/migrated-assets/images/polished-topaz.png',
    'tourmaline': 'https://www.gia.edu/dam/gemstones/tourmaline/overview/polished-tourmaline.png',
    'turquoise': 'https://www.gia.edu/dam/gemstones/turquoise/Photos-Videos/polished-turquoise.png',
    'zircon': 'https://www.gia.edu/dam/gemstones/zircon/polished-zircon.png',
    'jade': 'https://www.gia.edu/dam/gemstones/jade/polished-jade-gem.png',
    'alexandrite': 'https://www.gia.edu/dam/gemstones/alexandrite/polished-alexandrite-gem.png',
    'tanzanite': 'https://www.gia.edu/dam/gemstones/tanzanite/polished-tanzanite,0.png',
    'peridot': 'https://www.gia.edu/dam/gemstones/Image/polished-peridot.png',
}

print(f"Downloading {len(gia_images)} polished gemstone images from GIA...")

for name, url in gia_images.items():
    file_path = os.path.join(out_dir, f"{name}.png")
    try:
        res = httpx.get(url, headers=headers, follow_redirects=True, timeout=15)
        if res.status_code == 200 and len(res.content) > 1000:
            with open(file_path, 'wb') as f:
                f.write(res.content)
            print(f"Downloaded: {name}.png ({len(res.content)} bytes)")
        else:
            print(f"Failed {name}: status {res.status_code}")
    except Exception as e:
        print(f"Error {name}: {e}")
    time.sleep(0.3)

print("Finished downloading GIA images!")

