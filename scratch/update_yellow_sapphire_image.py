from PIL import Image
import os

src_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794548785142_509ff345.jpg"
im = Image.open(src_path)
print("Format:", im.format)
print("Size:", im.size)
print("Mode:", im.mode)

# Resize to standard 800x800 with high quality Lanczos resampling
im_resized = im.convert("RGBA").resize((800, 800), Image.Resampling.LANCZOS)

# 1. Target: frontend/public/images/gia/yellow-sapphire.png (Quantized 256 colors for fast loading & under 150 KB)
gia_path = "frontend/public/images/gia/yellow-sapphire.png"
q = im_resized.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
q.save(gia_path, "PNG", optimize=True)
print(f"Saved {gia_path}: {os.path.getsize(gia_path)} bytes")

# 2. Target: frontend/public/images/stones/yellow-sapphire.webp
stones_path = "frontend/public/images/stones/yellow-sapphire.webp"
im_resized.convert("RGB").save(stones_path, "WEBP", quality=88, method=6)
print(f"Saved {stones_path}: {os.path.getsize(stones_path)} bytes")

