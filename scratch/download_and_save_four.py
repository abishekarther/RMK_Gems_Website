import urllib.request, os
from PIL import Image

def save_under_150k(img, path, max_dim=800):
    w, h = img.size
    scale = min(max_dim / max(w, h), 1.0)
    if scale < 1.0:
        new_w, new_h = int(w * scale), int(h * scale)
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    q = 88
    while q >= 45:
        img.save(path, 'WEBP', quality=q)
        sz = os.path.getsize(path)
        if sz < 145000:
            print(f"Saved {path}: {sz} bytes (q={q})")
            return
        q -= 5
    print(f"Warning: {path} is {sz} bytes at q={q}")

items = {
    'sunstone': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/be/Sunstone_%28Tertiary%3B_Spectrum_Mine%2C_Oregon%2C_USA%29_10.jpg/960px-Sunstone_%28Tertiary%3B_Spectrum_Mine%2C_Oregon%2C_USA%29_10.jpg',
        'Sunstone (Tertiary; Spectrum Mine, Oregon, USA) 10.jpg',
        'James St. John',
        'CC BY 2.0',
        'https://commons.wikimedia.org/wiki/File:Sunstone_(Tertiary;_Spectrum_Mine,_Oregon,_USA)_10.jpg'
    ),
    'rose-quartz': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/0/01/Two_rose_quartz_cabocons_1.jpg/960px-Two_rose_quartz_cabocons_1.jpg',
        'Two rose quartz cabocons 1.jpg',
        'W.carter',
        'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Two_rose_quartz_cabocons_1.jpg'
    ),
    'smoky-quartz': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b4/Smoky_Quartz_-_Faceted_gem_of_Smoky_Quartz_from_Czech_Republic.jpg/960px-Smoky_Quartz_-_Faceted_gem_of_Smoky_Quartz_from_Czech_Republic.jpg',
        'Smoky Quartz - Faceted gem of Smoky Quartz from Czech Republic.jpg',
        'AdamStejskal',
        'CC BY 4.0',
        'https://commons.wikimedia.org/wiki/File:Smoky_Quartz_-_Faceted_gem_of_Smoky_Quartz_from_Czech_Republic.jpg'
    ),
    'hematite-gunmetal': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/53/Hematite_pebbles.jpg/960px-Hematite_pebbles.jpg',
        'Hematite pebbles.jpg',
        'Mauro Cateb',
        'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Hematite_pebbles.jpg'
    )
}

os.makedirs('scratch/temp_dl', exist_ok=True)
for slug, (url, title, author, lic, page) in items.items():
    raw_path = f"scratch/temp_dl/{slug}.jpg"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research; contact@rmkgems.com)'})
    with urllib.request.urlopen(req, timeout=12) as resp, open(raw_path, 'wb') as f:
        f.write(resp.read())
    
    img = Image.open(raw_path).convert('RGB')
    # If rose-quartz, crop to isolate one beautiful cabochon
    if slug == 'rose-quartz':
        # Two cabochons side by side, let's crop the left or right one
        w, h = img.size
        # The cabochons are centered. Let's inspect size
        print("rose-quartz raw size:", img.size)
    dst_webp = f"frontend/public/images/stones/{slug}.webp"
    save_under_150k(img, dst_webp)

