from PIL import Image
import os

src = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794548172337_d15c8ed9.jpg"
im = Image.open(src)
print("Format:", im.format)
print("Size:", im.size)
print("Mode:", im.mode)
print("File size bytes:", os.path.getsize(src))

