from PIL import Image
import os, shutil

src_uploaded = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png"
im = Image.open(src_uploaded).convert("RGBA")

# 1. Standard 800x800 centered on white
canvas_800 = Image.new("RGBA", (800, 800), (255, 255, 255, 255))
scaled = im.resize((640, 640), Image.Resampling.LANCZOS)
offset = ((800 - 640) // 2, (800 - 640) // 2)
canvas_800.paste(scaled, offset, scaled)
rgb_800 = canvas_800.convert("RGB")

# Destination directories
dirs = [
    "frontend/public/images/stones",
    "frontend/dist/images/stones",
    "semiprecious_stones_images"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    # Save as .webp
    webp_p = os.path.join(d, "agate-black-banded.webp")
    rgb_800.save(webp_p, "WEBP", quality=88, method=6)
    print(f"Saved {webp_p}: {os.path.getsize(webp_p)} bytes")
    
    # Save as .png (both 800x800 and copy of original)
    png_p = os.path.join(d, "agate-black-banded.png")
    im.save(png_p, "PNG")
    print(f"Saved {png_p}: {os.path.getsize(png_p)} bytes")

print("All stone folders synchronized successfully!")

