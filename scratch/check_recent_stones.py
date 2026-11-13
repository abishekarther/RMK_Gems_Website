import os, time

d = "frontend/public/images/stones"
now = time.time()
recent = []
for f in os.listdir(d):
    p = os.path.join(d, f)
    mtime = os.path.getmtime(p)
    if now - mtime < 7200: # past 2 hours
        recent.append((f, time.ctime(mtime), os.path.getsize(p)))

print("Recently modified in frontend/public/images/stones:")
for r in recent:
    print(r)

