with open('frontend/src/data/gemstoneFallbackData.ts', 'r', encoding='utf-8') as f:
    content = f.read()

prec_slugs = [
    'ruby', 'pearl', 'red-coral', 'emerald', 'yellow-sapphire',
    'diamond', 'blue-sapphire', 'hessonite-garnet', 'cats-eye-chrysoberyl'
]

for slug in prec_slugs:
    old_target = f'"/images/stones/{slug}.webp"'
    new_target = f'"/images/gia/{slug}.png"'
    # Note: avoid replacing hessonite-garnet-semi-precious!
    # Because of the quotes, f'"/images/stones/{slug}.webp"' will only match exact slug, not semi-precious.
    count = content.count(old_target)
    content = content.replace(old_target, new_target)
    print(f"Replaced {slug}: {count} occurrences")

with open('frontend/src/data/gemstoneFallbackData.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated gemstoneFallbackData.ts successfully.")

