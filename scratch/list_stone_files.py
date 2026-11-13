import os

files = sorted(os.listdir('frontend/public/images/stones'))
print(f"Total files: {len(files)}")
for f in files:
    print(f)

