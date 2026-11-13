import urllib.request, os
from PIL import Image

test_urls = {
    'lapis': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/3/33/Lazurite_polie_-_53_mm_-_%28Afghanistan%29.JPG/960px-Lazurite_polie_-_53_mm_-_%28Afghanistan%29.JPG',
    'tourmaline-green': 'https://upload.wikimedia.org/wikipedia/commons/2/2e/Tourmaline_cut.JPG',
    'white-topaz': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/45/Chalmer%27s_Topaz.jpg/960px-Chalmer%27s_Topaz.jpg'
}

os.makedirs('scratch/test_dl3', exist_ok=True)
for slug, url in test_urls.items():
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research; contact@rmkgems.com)'})
    raw_path = f"scratch/test_dl3/{slug}.jpg"
    with urllib.request.urlopen(req, timeout=12) as resp, open(raw_path, 'wb') as f:
        f.write(resp.read())
    img = Image.open(raw_path)
    print(f"{slug}: size={img.size}, mode={img.mode}")
    # Inspect center pixel
    print(f"  Center pixel: {img.getpixel((img.width//2, img.height//2))}")
    print(f"  Corner pixel: {img.getpixel((10, 10))}")

