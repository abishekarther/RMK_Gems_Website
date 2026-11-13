import urllib.request, os
from PIL import Image

five_stones = {
    'rutilated-quartz-black-needle': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/e/e7/Tourmalinated_quartz_1.jpg/960px-Tourmalinated_quartz_1.jpg',
        'Tourmalinated quartz 1.jpg',
        'James St. John',
        'CC BY 2.0',
        'https://commons.wikimedia.org/wiki/File:Tourmalinated_quartz_1.jpg'
    ),
    'pearl-fresh-water': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/da/Pearl-freshwater_hg.jpg/960px-Pearl-freshwater_hg.jpg',
        'Pearl-freshwater hg.jpg',
        'Hannes Grobe',
        'CC BY 3.0',
        'https://commons.wikimedia.org/wiki/File:Pearl-freshwater_hg.jpg'
    ),
    'sapphire-blue-semi-precious': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/c/cc/Eye_of_God_Star_Sapphire_Front_View.jpg/960px-Eye_of_God_Star_Sapphire_Front_View.jpg',
        'Eye of God Star Sapphire Front View.jpg',
        'TheMaharlikan',
        'CC0',
        'https://commons.wikimedia.org/wiki/File:Eye_of_God_Star_Sapphire_Front_View.jpg'
    ),
    'zircon-cubic-white': (
        'https://upload.wikimedia.org/wikipedia/commons/b/bd/CZ_brilliant.jpg',
        'CZ brilliant.jpg',
        'Gregory Phillips',
        'CC BY-SA 3.0',
        'https://commons.wikimedia.org/wiki/File:CZ_brilliant.jpg'
    ),
    'hessonite-garnet-semi-precious': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4f/Hessonite_%28grossular_variety%29_Ca3Al2Si3O12_%2842302997570%29.jpg/960px-Hessonite_%28grossular_variety%29_Ca3Al2Si3O12_%2842302997570%29.jpg',
        'Hessonite (grossular variety) Ca3Al2Si3O12 (42302997570).jpg',
        'Jan Helebrant',
        'CC BY-SA 2.0',
        'https://commons.wikimedia.org/wiki/File:Hessonite_(grossular_variety)_Ca3Al2Si3O12_(42302997570).jpg'
    )
}

def save_under_150k(img, path, max_dim=800):
    w, h = img.size
    max_d = max(w, h)
    bg = img.getpixel((5, 5))
    if sum(bg) > 600:
        bg_fill = (255, 255, 255)
    else:
        bg_fill = bg
    canvas = Image.new('RGB', (max_d, max_d), bg_fill)
    canvas.paste(img, ((max_d - w) // 2, (max_d - h) // 2))
    
    resized = canvas.resize((max_dim, max_dim), Image.Resampling.LANCZOS)
    q = 85
    while q >= 45:
        resized.save(path, 'WEBP', quality=q)
        sz = os.path.getsize(path)
        if sz < 145000:
            print(f"Saved {path}: {sz} bytes (q={q})")
            return
        q -= 5
    print(f"Warning: {path} is {sz} bytes at q={q}")

os.makedirs('scratch/temp_dl4', exist_ok=True)
for slug, (url, title, author, lic, page) in five_stones.items():
    raw_path = f"scratch/temp_dl4/{slug}.jpg"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0'})
    with urllib.request.urlopen(req, timeout=12) as resp, open(raw_path, 'wb') as f:
        f.write(resp.read())
    img = Image.open(raw_path).convert('RGB')
    dst = f"frontend/public/images/stones/{slug}.webp"
    save_under_150k(img, dst)
