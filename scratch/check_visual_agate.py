from PIL import Image

p1 = "scratch/downloaded/agate-black-banded.jpg"
p2 = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png"

im1 = Image.open(p1)
im2 = Image.open(p2)

print("Downloaded:", im1.size, im1.format)
print("Uploaded:  ", im2.size, im2.format)

