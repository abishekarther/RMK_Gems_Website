from PIL import Image
import os

src_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png"
im = Image.open(src_path).convert("RGBA")

# Create 800x800 white canvas
canvas = Image.new("RGBA", (800, 800), (255, 255, 255, 255))

# Scale stone up nicely: 500x500 to ~640x640 with Lanczos
scaled = im.resize((640, 640), Image.Resampling.LANCZOS)
offset = ((800 - 640) // 2, (800 - 640) // 2)

# Paste with alpha mask
canvas.paste(scaled, offset, scaled)

# Convert to RGB
rgb_canvas = canvas.convert("RGB")

target_path = "frontend/public/images/stones/agate-black-banded.webp"
rgb_canvas.save(target_path, "WEBP", quality=88, method=6)
print(f"Saved {target_path}: {os.path.getsize(target_path)} bytes")

