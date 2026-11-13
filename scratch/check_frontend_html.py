import urllib.request

try:
    with urllib.request.urlopen("http://localhost:5173/gemstones/agate-black-banded") as resp:
        html = resp.read().decode('utf-8')
        print("Page fetched, length:", len(html))
        # Find any img tags or script tags
        print("HTML preview (first 500 chars):")
        print(html[:500])
except Exception as e:
    print("Error:", e)

