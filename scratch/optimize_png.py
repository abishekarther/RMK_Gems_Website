from PIL import Image
import os

src_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794548172337_d15c8ed9.jpg"
im = Image.open(src_path).convert("RGBA").resize((800, 800), Image.Resampling.LANCZOS)

# Quantize to 256 colors adaptive palette with no dither for ultra clean look
q = im.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
gia_path = "frontend/public/images/gia/cats-eye-chrysoberyl.png"
q.save(gia_path, "PNG", optimize=True)
print(f"Quantized {gia_path}: {os.path.getsize(gia_path)} bytes")

