from PIL import Image

src_uploaded = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png"
cur_stone = "frontend/public/images/stones/agate-black-banded.webp"

im_up = Image.open(src_uploaded).convert("RGB")
im_cur = Image.open(cur_stone).convert("RGB")

print("Uploaded size:", im_up.size)
print("Current stone size:", im_cur.size)

# Resize current stone back to 500x500 to check if it's the exact same visual content
im_cur_small = im_cur.crop((100, 100, 700, 700)).resize((500, 500))

# Sample pixel in center of stone (250, 250)
print("Uploaded center pixel (250, 250):", im_up.getpixel((250, 250)))
print("Stone center pixel (400, 400):   ", im_cur.getpixel((400, 400)))
print("Uploaded stripe pixel (250, 220):", im_up.getpixel((250, 220)))
print("Stone stripe pixel (400, 360):   ", im_cur.getpixel((400, 360)))

