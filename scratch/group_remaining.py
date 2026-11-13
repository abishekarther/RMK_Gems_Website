import json

already_matched = {
    'watermarked_img_17757265627695894731.webp': 'amethyst-african',
    'watermarked_img_11311302170131594416.webp': 'amethyst-brazil',
    '42e13544-7511-4597-897d-a501e6eedd0f.webp': 'amethyst-brazil-pink',
    'f14e3f30-4b9c-48b3-9b7c-4c1b371bd971.webp': 'aquamarine-yellow',
    '10c566df-d601-43f1-bbb1-99a81398d6f2.webp': 'garnet-almandine',
    '396d963f-728a-4327-91dd-c57715099582.webp': 'garnet-checkerboard',
    '32d2c86a-51eb-4543-9d6e-59ea08eec356.webp': 'hessonite-garnet',
    '8f9baeba-f14a-41cb-88f4-16f096d53d75.webp': 'lemon-citrine',
    'ac249b55-b23b-4ca4-996b-6cd63376a21c.webp': 'pearl-fresh-water',
    'd67d367c-67a3-41c7-b80f-175cd964705a.webp': 'ruby-markara',
    '01fe31cf-93e0-4b7b-8ff8-57289553b691.webp': 'sapphire-blue',
    '4738ee53-16d3-4d8f-803c-29a9b8482f1d.webp': 'smoky-quartz',
    '13ab1b47-709b-4bd1-a022-b6ff27ead219.webp': 'spectrolite-cats-eye',
    '66cc2610-4839-47a7-87fe-ea88ee9753d1.webp': 'tourmaline-green',
    'ec33f068-fb59-4b1f-b074-a01630a3c928.webp': 'white-quartz-crystal',
    'd5e93ae4-a47a-40f8-87f1-2b0f26b88256.webp': 'white-topaz',
    '18b9dd28-aab3-4c4c-b9bc-bd9010043d7e.webp': 'zircon-cubic-white',
    '01b1c93a-9a50-4d77-9b2d-e5cb2245f05b.webp': 'rainbow-moonstone',
}

with open('scratch/image_stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

remaining = [s for s in stats if s['file'] not in already_matched]
print(f"Remaining unmatched images: {len(remaining)}")

# Group by color:
# 1. Very dark (val < 25)
print("\n--- Very Dark (val < 25) ---")
for s in remaining:
    if s['hsv'][2] < 25:
        print(f"{s['file']}: hsv={s['hsv']}, std={s['total_std']}, rgb={s['rgb']}")

# 2. Blues & Cyan (170 <= hue <= 250 and sat > 10)
print("\n--- Blues & Cyans (170 <= hue <= 250) ---")
for s in remaining:
    if 170 <= s['hsv'][0] <= 250 and s['hsv'][1] > 10 and s['hsv'][2] >= 25:
        print(f"{s['file']}: hsv={s['hsv']}, std={s['total_std']}, rgb={s['rgb']}")

# 3. Greens (70 <= hue < 170 and sat > 10)
print("\n--- Greens (70 <= hue < 170) ---")
for s in remaining:
    if 70 <= s['hsv'][0] < 170 and s['hsv'][1] > 10 and s['hsv'][2] >= 25:
        print(f"{s['file']}: hsv={s['hsv']}, std={s['total_std']}, rgb={s['rgb']}")

# 4. Reds & Oranges (hue < 40 or hue > 330, and sat > 20)
print("\n--- Reds & Oranges (hue < 40 or hue > 330) ---")
for s in remaining:
    if (s['hsv'][0] < 40 or s['hsv'][0] > 330) and s['hsv'][1] > 20 and s['hsv'][2] >= 25:
        print(f"{s['file']}: hsv={s['hsv']}, std={s['total_std']}, rgb={s['rgb']}")

# 5. Yellows & Browns (40 <= hue < 70, or sat > 15 and 20 <= hue < 40)
print("\n--- Yellows & Browns ---")
for s in remaining:
    if 40 <= s['hsv'][0] < 70 and s['hsv'][1] > 15 and s['hsv'][2] >= 25:
        print(f"{s['file']}: hsv={s['hsv']}, std={s['total_std']}, rgb={s['rgb']}")

# 6. Neutrals / Whites / Low saturation (sat <= 15)
print("\n--- Neutrals / Whites / Gray (sat <= 15) ---")
for s in remaining:
    if s['hsv'][1] <= 15 and s['hsv'][2] >= 25:
        print(f"{s['file']}: hsv={s['hsv']}, std={s['total_std']}, rgb={s['rgb']}")

