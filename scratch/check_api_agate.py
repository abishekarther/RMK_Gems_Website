import urllib.request
import json

try:
    with urllib.request.urlopen("http://localhost:8000/api/v1/gemstones/agate-black-banded") as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("API Response for agate-black-banded:")
        print("Name:", data.get("name"))
        print("Slug:", data.get("slug"))
        print("Media:", data.get("media"))
except Exception as e:
    print("API Error:", e)

