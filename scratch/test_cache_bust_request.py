import urllib.request

url = "http://localhost:5173/images/stones/agate-black-banded.webp?v=20261113_2"
try:
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
        print("HTTP Status:", resp.status)
        print("Fetched bytes with query param:", len(data))
except Exception as e:
    print("Error:", e)

