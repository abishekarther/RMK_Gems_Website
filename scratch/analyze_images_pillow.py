import os
import json
import colorsys
from PIL import Image, ImageFilter, ImageStat

def analyze_file(filepath):
    img = Image.open(filepath).convert('RGB')
    w, h = img.size
    
    # Convert to grayscale to find bounding box
    gray = img.convert('L')
    # Background threshold: near white is >= 238
    # We want pixels < 238
    mask = gray.point(lambda p: 255 if p < 238 else 0, mode='1')
    bbox = mask.getbbox()
    if not bbox:
        bbox = (0, 0, w, h)
        
    xmin, ymin, xmax, ymax = bbox
    bw = xmax - xmin
    bh = ymax - ymin
    aspect = round(bh / max(bw, 1), 3)
    
    # Calculate non-background pixel stats
    # Crop to gem
    crop = img.crop(bbox)
    crop_gray = gray.crop(bbox)
    crop_mask = mask.crop(bbox)
    
    # Gem area and fill ratio
    gem_pixels = [p for p, m in zip(crop.getdata(), crop_mask.getdata()) if m]
    if not gem_pixels:
        gem_pixels = list(crop.getdata())
        
    n_pix = len(gem_pixels)
    avg_r = sum(p[0] for p in gem_pixels) / n_pix
    avg_g = sum(p[1] for p in gem_pixels) / n_pix
    avg_b = sum(p[2] for p in gem_pixels) / n_pix
    
    # HSV
    h_norm, s_norm, v_norm = colorsys.rgb_to_hsv(avg_r / 255.0, avg_g / 255.0, avg_b / 255.0)
    hue_deg = round(h_norm * 360, 1)
    sat_pct = round(s_norm * 100, 1)
    val_pct = round(v_norm * 100, 1)
    
    # Fill ratio: gem area / bbox area
    fill_ratio = round(n_pix / max(bw * bh, 1), 3)
    
    # Edges inside the gem to detect facets vs smooth cabochon
    edges = crop_gray.filter(ImageFilter.FIND_EDGES)
    edge_stat = ImageStat.Stat(edges, mask=crop_mask)
    edge_mean = round(edge_stat.mean[0], 2)
    edge_std = round(edge_stat.stddev[0], 2)
    
    # Color variance (to detect stripes, bands, spots, needles)
    r_vals = [p[0] for p in gem_pixels]
    g_vals = [p[1] for p in gem_pixels]
    b_vals = [p[2] for p in gem_pixels]
    stat_crop = ImageStat.Stat(crop, mask=crop_mask)
    std_r, std_g, std_b = [round(s, 1) for s in stat_crop.stddev]
    total_std = round((std_r**2 + std_g**2 + std_b**2)**0.5, 1)
    
    # Center crop stats (center 30% of bbox)
    cx1 = xmin + int(bw * 0.35)
    cy1 = ymin + int(bh * 0.35)
    cx2 = xmin + int(bw * 0.65)
    cy2 = ymin + int(bh * 0.65)
    center_crop = img.crop((cx1, cy1, cx2, cy2))
    center_stat = ImageStat.Stat(center_crop)
    c_r, c_g, c_b = [round(m, 1) for m in center_stat.mean]
    c_h, c_s, c_v = colorsys.rgb_to_hsv(c_r/255.0, c_g/255.0, c_b/255.0)

    return {
        'file': os.path.basename(filepath),
        'size_bytes': os.path.getsize(filepath),
        'aspect': aspect,
        'fill_ratio': fill_ratio,
        'rgb': [round(avg_r, 1), round(avg_g, 1), round(avg_b, 1)],
        'hsv': [hue_deg, sat_pct, val_pct],
        'total_std': total_std,
        'edge_mean': edge_mean,
        'center_rgb': [c_r, c_g, c_b],
        'center_hsv': [round(c_h*360, 1), round(c_s*100, 1), round(c_v*100, 1)]
    }

def main():
    folder = 'semiprecious_stones_images'
    files = sorted([f for f in os.listdir(folder) if f.endswith('.webp')])
    all_stats = []
    for f in files:
        path = os.path.join(folder, f)
        res = analyze_file(path)
        all_stats.append(res)
        
    with open('scratch/image_stats.json', 'w', encoding='utf-8') as f:
        json.dump(all_stats, f, indent=2)
    print(f'Successfully analyzed {len(all_stats)} images.')

if __name__ == '__main__':
    main()

