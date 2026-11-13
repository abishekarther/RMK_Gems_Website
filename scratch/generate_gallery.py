import json
import os

with open('scratch/image_stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

with open('scratch/user_table.json', 'r', encoding='utf-8') as f:
    stones = json.load(f)

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Gemstone Matching Gallery</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #1a1a1a; color: #eee; padding: 20px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
  .card { background: #2a2a2a; border-radius: 8px; padding: 12px; border: 1px solid #444; }
  .card img { width: 100%; height: 220px; object-fit: contain; background: #fff; border-radius: 4px; }
  .filename { font-size: 11px; color: #888; word-break: break-all; margin-top: 8px; }
  .meta { font-size: 12px; color: #aaa; margin-top: 4px; }
  .tag { display: inline-block; padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: bold; }
</style>
</head>
<body>
<h1>59 Candidate Images in semiprecious_stones_images/</h1>
<div class="grid">
"""

for s in stats:
    f = s['file']
    hsv = s['hsv']
    rgb = s['rgb']
    asp = s['aspect']
    edge = s['edge_mean']
    std = s['total_std']
    html += f"""
  <div class="card">
    <img src="../semiprecious_stones_images/{f}" loading="lazy">
    <div class="filename"><b>{f}</b></div>
    <div class="meta">
      Aspect: {asp} | Edge: {edge} | Std: {std}<br>
      HSV: ({hsv[0]}&deg;, {hsv[1]}%, {hsv[2]}%)<br>
      RGB: ({rgb[0]}, {rgb[1]}, {rgb[2]})
    </div>
  </div>
"""

html += """
</div>
</body>
</html>
"""

with open('scratch/gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Created scratch/gallery.html")

