import json

with open('scratch/image_stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

# Cushion cut stones in user's guide:
# Notice in user's guide, cushion cut stones usually have aspect ratio around 1.05 to 1.15 (almost square cushion!)
# Let's see the aspect ratio distribution
cushion_aspects = [s for s in stats if 1.00 <= s['aspect'] <= 1.20]
print(f"Total images with aspect ratio between 1.00 and 1.20: {len(cushion_aspects)}")
for s in sorted(cushion_aspects, key=lambda x: x['hsv'][0]):
    print(f"{s['file']}: aspect={s['aspect']}, hsv={s['hsv']}, edge={s['edge_mean']}, rgb={s['rgb']}")

