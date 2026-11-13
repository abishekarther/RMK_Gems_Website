from PIL import Image
import os

src_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794548172337_d15c8ed9.jpg"
im = Image.open(src_path)

# Resize to standard 800x800 with high quality Lanczos resampling
im_resized = im.resize((800, 800), Image.Resampling.LANCZOS)

# Target 1: frontend/public/images/gia/cats-eye-chrysoberyl.png
gia_path = "frontend/public/images/gia/cats-eye-chrysoberyl.png"
im_resized.save(gia_path, "PNG", optimize=True)
print(f"Saved {gia_path}: {os.path.getsize(gia_path)} bytes")

# Target 2: frontend/public/images/stones/cats-eye-chrysoberyl.webp
stones_path = "frontend/public/images/stones/cats-eye-chrysoberyl.webp"
im_resized.save(stones_path, "WEBP", quality=88, method=6)
print(f"Saved {stones_path}: {os.path.getsize(stones_path)} bytes")

