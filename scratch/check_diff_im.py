from PIL import Image, ImageChops

im1 = Image.open(r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png")
im2 = Image.open("semiprecious_stones_images/agate-black-banded.png")

diff = ImageChops.difference(im1, im2)
bbox = diff.getbbox()
print("Difference bbox between user upload and semi folder:", bbox)

