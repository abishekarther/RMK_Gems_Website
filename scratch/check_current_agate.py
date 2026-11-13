from PIL import Image

p = "frontend/public/images/stones/agate-black-banded.webp"
im = Image.open(p)
print("File:", p)
print("Size:", im.size)
print("Format:", im.format)

# Sample some pixel colors: center, corner
print("Corner pixel (0,0):", im.getpixel((0,0)))
print("Center pixel (400,400):", im.getpixel((400,400)))

