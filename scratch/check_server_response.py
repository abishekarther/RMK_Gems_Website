import urllib.request
import hashlib

url = "http://localhost:5173/images/stones/agate-black-banded.webp"
try:
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
        print("Fetched bytes:", len(data))
        print("SHA-256 from localhost:5173:", hashlib.sha256(data).hexdigest())
except Exception as e:
    print("Error fetching:", e)

with open("frontend/public/images/stones/agate-black-banded.webp", "rb") as f:
    disk_data = f.read()
    print("Disk SHA-256:              ", hashlib.sha256(disk_data).hexdigest())

