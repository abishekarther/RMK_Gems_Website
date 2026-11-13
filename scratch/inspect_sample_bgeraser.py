from PIL import Image
import os

src_dir = "bgeraser_results (1)"
for f in sorted(os.listdir(src_dir))[:10]:
    p = os.path.join(src_dir, f)
    im = Image.open(p)
    print(f"{f}: size={im.size}, mode={im.mode}, file_size={os.path.getsize(p)} bytes")

