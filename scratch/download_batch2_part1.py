import urllib.request, os
from PIL import Image

items = {
    'lemon-citrine': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d0/Citrine_taillee.jpg/960px-Citrine_taillee.jpg',
        'Citrine taillee.jpg',
        'Didier Descouens',
        'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Citrine_taillee.jpg'
    ),
    'pyrite': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/9/91/Pyrite_-_Huanzala_mine%2C_Huallanca%2C_Bolognesi%2C_Ancash%2C_Peru.jpg/960px-Pyrite_-_Huanzala_mine%2C_Huallanca%2C_Bolognesi%2C_Ancash%2C_Peru.jpg',
        'Pyrite - Huanzala mine, Huallanca, Bolognesi, Ancash, Peru.jpg',
        'Ivar Leidus',
        'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Pyrite_-_Huanzala_mine,_Huallanca,_Bolognesi,_Ancash,_Peru.jpg'
    ),
    'white-quartz': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/ce/Quartz_Br%C3%A9sil.jpg/960px-Quartz_Br%C3%A9sil.jpg',
        'Quartz Brésil.jpg',
        'Didier Descouens',
        'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Quartz_Br%C3%A9sil.jpg'
    ),
    'white-quartz-crystal': (
        'https://upload.wikimedia.org/wikipedia/commons/7/74/Quartz-153424.jpg',
        'Quartz-153424.jpg',
        'Robert M. Lavinsky',
        'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:Quartz-153424.jpg'
    )
}

def save_under_150k(img, path, max_dim=800):
    w, h = img.size
    scale = min(max_dim / max(w, h), 1.0)
    if scale < 1.0:
        new_w, new_h = int(w * scale), int(h * scale)
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    q = 85
    while q >= 45:
        img.save(path, 'WEBP', quality=q)
        sz = os.path.getsize(path)
        if sz < 145000:
            print(f"Saved {path}: {sz} bytes (q={q})")
            return
        q -= 5
    print(f"Warning: {path} is {sz} bytes at q={q}")

os.makedirs('scratch/temp_dl', exist_ok=True)
for slug, (url, title, author, lic, page) in items.items():
    raw_path = f"scratch/temp_dl/{slug}.jpg"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research; contact@rmkgems.com)'})
    with urllib.request.urlopen(req, timeout=12) as resp, open(raw_path, 'wb') as f:
        f.write(resp.read())
    
    img = Image.open(raw_path).convert('RGB')
    print(f"{slug} raw size: {img.size}")
    dst_webp = f"frontend/public/images/stones/{slug}.webp"
    save_under_150k(img, dst_webp)

