from PIL import Image
import os

src_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png"
im = Image.open(src_path)
print("Format:", im.format)
print("Size:", im.size)
print("Mode:", im.mode)

