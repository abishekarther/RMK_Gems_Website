from PIL import Image
import os

src_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794548913461_ae6e7597.jpg"
im = Image.open(src_path)
print("Format:", im.format)
print("Size:", im.size)
print("Mode:", im.mode)

