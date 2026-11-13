from PIL import Image
import os

def process_and_save_gem(src_path, dst_path, target_size=800, quality=88):
    img = Image.open(src_path).convert('RGB')
    
    # If not square, place on square white canvas or crop
    w, h = img.size
    max_dim = max(w, h)
    
    # Get background color from top-left corner
    bg_color = img.getpixel((0, 0))
    # If corner is close to white/light grey, use it or white
    if sum(bg_color) > 600:
        fill_color = (255, 255, 255)
    else:
        fill_color = bg_color
        
    canvas = Image.new('RGB', (max_dim, max_dim), fill_color)
    paste_x = (max_dim - w) // 2
    paste_y = (max_dim - h) // 2
    canvas.paste(img, (paste_x, paste_y))
    
    # Resize to target_size
    resized = canvas.resize((target_size, target_size), Image.Resampling.LANCZOS)
    resized.save(dst_path, 'WEBP', quality=quality)
    print(f"Saved {dst_path}: size={target_size}x{target_size}, bytes={os.path.getsize(dst_path)}")

process_and_save_gem('scratch/test_dl/hessonite-garnet.jpg', 'frontend/public/images/stones/hessonite-garnet.webp')
process_and_save_gem('scratch/test_dl/obsidian-snowflake.jpg', 'frontend/public/images/stones/obsidian-snowflake.webp')

