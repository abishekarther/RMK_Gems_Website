from PIL import Image, ImageOps
import os

src_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794548913461_ae6e7597.jpg"
im = Image.open(src_path).convert("RGB")

# Get bounding box of non-white content
# Invert grayscale image where 255 (white) becomes 0
gray = im.convert("L")
inverted = ImageOps.invert(gray)
# Threshold so subtle off-white is 0
thresh = inverted.point(lambda p: p if p > 15 else 0)
bbox = thresh.getbbox()
print("BBox:", bbox)

# Expand bbox slightly for soft shadow
x0, y0, x1, y1 = bbox
x0 = max(0, x0 - 15)
y0 = max(0, y0 - 15)
x1 = min(im.width, x1 + 15)
y1 = min(im.height, y1 + 15)

stone_crop = im.crop((x0, y0, x1, y1))
sw, sh = stone_crop.size

# Target stone dimension ~580px inside 800x800 canvas
target_dim = 580
scale = target_dim / max(sw, sh)
new_w, new_h = int(sw * scale), int(sh * scale)
stone_scaled = stone_crop.resize((new_w, new_h), Image.Resampling.LANCZOS)

# Create 800x800 white canvas
canvas = Image.new("RGB", (800, 800), (255, 255, 255))
offset = ((800 - new_w) // 2, (800 - new_h) // 2)
canvas.paste(stone_scaled, offset)

# Target 1: frontend/public/images/gia/ruby.png
gia_path = "frontend/public/images/gia/ruby.png"
q = canvas.convert("RGBA").quantize(colors=256, method=Image.Quantize.FASTOCTREE)
q.save(gia_path, "PNG", optimize=True)
print(f"Saved {gia_path}: {os.path.getsize(gia_path)} bytes")

# Target 2: frontend/public/images/stones/ruby.webp
stones_path = "frontend/public/images/stones/ruby.webp"
canvas.save(stones_path, "WEBP", quality=88, method=6)
print(f"Saved {stones_path}: {os.path.getsize(stones_path)} bytes")
