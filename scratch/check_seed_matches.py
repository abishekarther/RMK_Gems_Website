with open('backend/app/seed/seed_data.py', 'r', encoding='utf-8') as f:
    seed_content = f.read()

hidden_slugs = [
    'agate-red-jasper', 'aquamarine-yellow', 'garnet-rose-cut-checkerboard',
    'goldstone-sandstone-blue', 'goldstone-sandstone-red', 'hessonite-garnet-semi-precious',
    'pearl-fresh-water', 'ruby-markara', 'rutilated-quartz-black-needle',
    'sapphire-blue-semi-precious', 'zircon-cubic-white'
]

for s in hidden_slugs:
    pattern = f'"slug": \'{s}\''
    print(f"{s}: {pattern in seed_content}")
