import hashlib

def h(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

print("blue-sapphire.webp:", h('frontend/public/images/stones/blue-sapphire.webp'))
print("sapphire-blue.webp:", h('frontend/public/images/stones/sapphire-blue.webp'))
print("hessonite-garnet.webp:", h('frontend/public/images/stones/hessonite-garnet.webp'))
print("hessonite-garnet-semi-precious.webp:", h('frontend/public/images/stones/hessonite-garnet-semi-precious.webp'))
print("garnet-checkerboard.webp:", h('frontend/public/images/stones/garnet-checkerboard.webp'))

