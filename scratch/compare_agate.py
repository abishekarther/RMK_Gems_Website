from PIL import Image

src_path = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png"
dst_path = "frontend/public/images/stones/agate-black-banded.webp"

im_src = Image.open(src_path)
im_dst = Image.open(dst_path)

print("Source format:", im_src.format, "size:", im_src.size, "mode:", im_src.mode)
print("Dest format:  ", im_dst.format, "size:", im_dst.size, "mode:", im_dst.mode)

# Save a direct PNG copy to frontend/public/images/stones/ if the user looks for .png or .webp

