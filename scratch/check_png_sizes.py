import os

src_dir = "bgeraser_results (1)"
large = []
small = []
for f in sorted(os.listdir(src_dir)):
    p = os.path.join(src_dir, f)
    sz = os.path.getsize(p)
    if sz > 153600:
        large.append((f, sz))
    else:
        small.append((f, sz))

print(f"Total files: {len(large) + len(small)}")
print(f"Under 150 KB: {len(small)}")
print(f"Over 150 KB:  {len(large)}")
print("\nFirst 10 over 150 KB:")
for f, sz in large[:10]:
    print(f"  {f}: {sz / 1024:.1f} KB")

