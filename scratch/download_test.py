import urllib.request, json, os

urls = {
    'obsidian-snowflake': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d3/Snowflake_obsidian_1.jpg/960px-Snowflake_obsidian_1.jpg',
        'Snowflake obsidian 1.jpg',
        'James St. John',
        'CC BY 2.0',
        'https://commons.wikimedia.org/wiki/File:Snowflake_obsidian_1.jpg'
    ),
    'hessonite-garnet': (
        'https://thumb.wikimedia.org/wikipedia/commons/thumb/4/4d/Hessonite._Jesenik%2C_Czech_Republic-8871.jpg/960px-Hessonite._Jesenik%2C_Czech_Republic-8871.jpg',
        'Hessonite._Jesenik, Czech Republic-8871.jpg',
        'Raimond Spekking',
        'CC BY-SA 4.0',
        'https://commons.wikimedia.org/wiki/File:Hessonite._Jesenik,_Czech_Republic-8871.jpg'
    )
}

os.makedirs('scratch/test_dl', exist_ok=True)
for slug, (url, title, author, lic, page) in urls.items():
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research; contact@rmkgems.com)'})
    out_path = f"scratch/test_dl/{slug}.jpg"
    try:
        with urllib.request.urlopen(req, timeout=10) as resp, open(out_path, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded {slug} -> {os.path.getsize(out_path)} bytes")
    except Exception as e:
        print(f"Failed {slug}: {e}")

