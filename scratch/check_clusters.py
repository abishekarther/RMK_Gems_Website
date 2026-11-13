import json
import os
import re

with open('scratch/image_stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

with open('scratch/user_table.json', 'r', encoding='utf-8') as f:
    stones = json.load(f)

# Sort stats by aspect ratio and hue
stats_by_file = {s['file']: s for s in stats}

# Let's check aspect ratio close to 1.0
print("=== Aspect ratio near 1.00 (sphere candidate) ===")
for s in sorted(stats, key=lambda x: abs(x['aspect'] - 1.0)):
    if abs(s['aspect'] - 1.0) < 0.05:
        print(f"{s['file']}: aspect={s['aspect']}, hsv={s['hsv']}, fill={s['fill_ratio']}, rgb={s['rgb']}")

print("\n=== Edge mean high (cushion / faceted candidates) ===")
for s in sorted(stats, key=lambda x: x['edge_mean'], reverse=True)[:25]:
    print(f"{s['file']}: edge={s['edge_mean']}, aspect={s['aspect']}, hsv={s['hsv']}, rgb={s['rgb']}")

