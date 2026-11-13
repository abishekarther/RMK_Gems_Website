from PIL import Image

old_img_path = "scratch/downloaded/agate-black-banded.jpg"
semi_img_path = "semiprecious_stones_images/agate-black-banded.png"
user_uploaded_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png"
current_stone_path = "frontend/public/images/stones/agate-black-banded.webp"

for label, p in [("old downloaded", old_img_path), ("semi folder", semi_img_path), ("user uploaded", user_uploaded_path), ("current stone", current_stone_path)]:
    im = Image.open(p)
    print(f"=== {label} ===")
    print(f"Path: {p}")
    print(f"Size: {im.size}, Format: {im.format}, Mode: {im.mode}")

