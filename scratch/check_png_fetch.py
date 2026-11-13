import urllib.request

url = "http://localhost:5173/images/stones/agate-black-banded.png?v=20261113_2"
try:
    with urllib.request.urlopen(url) as resp:
        print("Status:", resp.status)
        print("Length:", len(resp.read()))
except Exception as e:
    print("Error:", e)

