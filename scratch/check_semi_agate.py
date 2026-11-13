from PIL import Image

p = "semiprecious_stones_images/agate-black-banded.png"
im = Image.open(p)
print("semiprecious_stones_images agate-black-banded.png size:", im.size, "mode:", im.mode)

