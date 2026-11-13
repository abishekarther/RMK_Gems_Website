import urllib.request, urllib.parse, json

def test_cat(cat_name):
    params = {
        'action': 'query',
        'generator': 'categorymembers',
        'gcmtitle': f'Category:{cat_name}',
        'gcmnamespace': '6',
        'gcmlimit': '10',
        'prop': 'imageinfo',
        'iiprop': 'url|size|extmetadata|mime',
        'iiurlwidth': '800',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'RMKGemsBot/1.0 (educational research; contact@rmkgems.com)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            print(f"\n=== Category:{cat_name} ({len(pages)} items) ===")
            for pid, page in pages.items():
                info = page.get('imageinfo', [{}])[0]
                print(f"  {page.get('title')} | mime={info.get('mime')}")
                print(f"    thumb: {info.get('thumburl')}")
    except Exception as e:
        print(f"Error for {cat_name}: {e}")

test_cat("Cut lapis lazuli")
test_cat("Cut quartz")
test_cat("Cut garnets")
test_cat("Cut topaz")

