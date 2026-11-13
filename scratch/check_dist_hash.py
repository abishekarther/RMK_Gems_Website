import hashlib

def h(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

print("public:", h("frontend/public/images/stones/agate-black-banded.webp"))
print("dist:  ", h("frontend/dist/images/stones/agate-black-banded.webp"))

