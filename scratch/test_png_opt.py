from PIL import Image
import io

src = "bgeraser_results (1)/agate-green-banded.png"
im = Image.open(src)
print("Original size:", im.size)

# Resize to 800x800 RGBA
im_800 = im.resize((800, 800), Image.Resampling.LANCZOS)
buf = io.BytesIO()
im_800.save(buf, format="PNG", optimize=True)
print("Standard PNG optimize:", len(buf.getvalue()), "bytes")

# Quantize to 256 colors RGBA
q = im_800.quantize(colors=256, method=Image.Quantize.FASTOCTREE)
buf_q = io.BytesIO()
q.save(buf_q, format="PNG", optimize=True)
print("Quantized 256 RGBA PNG:", len(buf_q.getvalue()), "bytes")

# WebP lossless/lossy with alpha
buf_w = io.BytesIO()
im_800.save(buf_w, format="WEBP", quality=88, method=6)
print("WebP with alpha:", len(buf_w.getvalue()), "bytes")

