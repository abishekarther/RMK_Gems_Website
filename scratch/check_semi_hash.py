import hashlib

def h(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

src = r"C:/Users/jeffrey/.gemini/antigravity/brain/01a08e85-b148-4129-91ef-046faef8ecbf/.user_uploaded/media_1794575906221_8ea02ee9.png"
semi = "semiprecious_stones_images/agate-black-banded.png"

print("uploaded hash:", h(src))
print("semi hash:    ", h(semi))
print("Are they identical?", h(src) == h(semi))

