import json

already_matched = {
    # Cushions & Sphere & Phenomenon
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
    
    # Darks & Cat eyes & Phenomenon
    '9ad29cc7-f25e-457c-b060-35aef9dd308d.webp': 'onyx-black',
    '1227f26f-60c6-413d-a596-c153cec7d004.webp': 'diopside-4-ray-star',
    '1fa3e7df-7d69-4e58-b0b6-b56336dd0783.webp': 'obsidian-snowflake',
    '2f575c2e-8c44-4763-b329-3700bee3d6a7.webp': 'agate-black-banded',
    '994cef7e-37ba-48b0-aafb-ad939f323de5.webp': 'bloodstone',
    '05bff557-0178-46eb-87b8-78e716a60ccf.webp': 'opal-dendrite',
    '53fa994e-b2b3-4e4e-afa3-1c378b36b75a.webp': 'hematite-gunmetal',
    '4f1b05db-9317-408a-9414-f47605c1843b.webp': 'quartz-cats-eye',
    'ec8770a3-c765-4d6a-af28-40e7e69fdea8.webp': 'sillimanite-cats-eye',
    'f45e2239-b82e-47b3-9964-fda636a4923c.webp': 'labradorite',
    
    # Blues & Greens
    'a1e6986d-25a4-40af-8c6c-f4bab42620d9.webp': 'turquoise-tibetan',
    '3d7f054b-3856-4f16-90ea-929e799b598a.webp': 'turquoise-chinese',
    '1d649662-f698-4fcb-86b1-2dcd829f7795.webp': 'lapis',
    '83d1b4f9-0611-4ffa-a4ee-9a2fde43e81f.webp': 'goldstone-sandstone-blue',
    '26109ec9-576c-4453-bd55-8ee761a06fc5.webp': 'blue-lace-banded-agate',
    '4ad964ca-c610-408a-b622-51310a1d0d8d.webp': 'chalcedony-blue',
    '3c287d7d-9370-418e-b9ca-081af27492fc.webp': 'chrysoprase',
    '2f496cbd-e572-40ef-8b5c-ba7857f0423b.webp': 'aventurine-green',
    '490c41c0-c7ed-4ef7-91c9-562903fa2829.webp': 'onyx-green',
    '6b3e9525-884b-4777-a69e-90ac1a46004e.webp': 'malachite',
    'bd537fca-d46d-4de2-b85c-b43011d6352d.webp': 'agate-green-banded',
    'fc0eec37-61d9-48ea-a546-3611f2bd71fd.webp': 'green-serpentine',
    
    # Warm tones & stripes
    '1c12882b-6dd3-4dde-9d67-302667a5046a.webp': 'onyx-multicolor',
    '2c3338ea-5a72-4d8f-89d4-8772e95fc271.webp': 'onyx-yellow',
    '5c2597ef-8cc2-4d0c-830c-ed3589664ce3.webp': 'onyx-red-pink',
    '7d379a1a-d843-40d4-97a6-c3ff68cf13cd.webp': 'sunstone',
    '85c9eae6-60e9-4799-aaaf-3ca1480764d3.webp': 'carnelian',
    '92ffff4a-79d5-4375-bed7-e945659f0db0.webp': 'tiger-eye',
    'aecc2ea9-95cb-41c5-b5d3-a3f6f8bf2c70.webp': 'goldstone-sandstone-red',
    'c5d31f36-ea7c-41a9-8064-225aaa3833ac.webp': 'pyrite',
    'bc98373b-26a6-4bae-baf0-89ef2824c2aa.webp': 'onyx-red',
    'cfbb7fe8-9fa0-4133-b756-325867080010.webp': 'agate-red-jasper',
    'a2088c19-06e7-4308-b01e-dc691764e9ed.webp': 'onyx-rose',
}

with open('scratch/image_stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

with open('scratch/user_table.json', 'r', encoding='utf-8') as f:
    stones = json.load(f)

matched_targets = set(already_matched.values())
remaining_targets = [s for s in stones if s['target'] not in matched_targets]
remaining_files = [s['file'] for s in stats if s['file'] not in already_matched]

print(f"Matched so far: {len(already_matched)}")
print(f"Remaining stones: {len(remaining_targets)}")
print(f"Remaining files: {len(remaining_files)}")

print("\nRemaining stones to match:")
for s in remaining_targets:
    print(f"{s['num']}. {s['target']} ({s['name']}): {s['color']} | {s['features']}")

print("\nRemaining files:")
for f in remaining_files:
    print(f)

