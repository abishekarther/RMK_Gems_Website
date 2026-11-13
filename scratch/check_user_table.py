import sys, os
sys.path.insert(0, os.path.abspath('.'))
from backend.app.seed.seed_data import get_seed_data
_, _, _, _, prec, semi = get_seed_data()

user_table = [
    ("Agate Black Banded", "agate-black-banded"),
    ("Agate Green Banded", "agate-green-banded"),
    ("Agate Red Jasper", "agate-red-jasper"),
    ("Amethyst African", "amethyst-african"),
    ("Amethyst Brazil", "amethyst-brazil"),
    ("Amethyst Brazil Pink", "amethyst-brazil-pink"),
    ("Aquamarine Yellow", "aquamarine-yellow"),
    ("Aventurine Green", "aventurine-green"),
    ("Bloodstone", "bloodstone"),
    ("Blue Lace Banded Agate", "blue-lace-banded-agate"),
    ("Carnelian", "carnelian"),
    ("Chalcedony Blue", "chalcedony-blue"),
    ("Chalcedony White", "chalcedony-white"),
    ("Chrysoprase", "chrysoprase"),
    ("Diopside 4-ray Star", "diopside-4-ray-star"),
    ("Fluorite Multicolor Banded", "fluorite-multicolor-banded"),
    ("Garnet Almandine", "garnet-almandine"),
    ("Garnet Rose Cut / Checkerboard", "garnet-checkerboard"),
    ("Goldstone Sandstone Blue", "goldstone-sandstone-blue"),
    ("Goldstone Sandstone Red", "goldstone-sandstone-red"),
    ("Green Serpentine", "green-serpentine"),
    ("Hematite (Gunmetal)", "hematite-gunmetal"),
    ("Hessonite Garnet", "hessonite-garnet"),
    ("Labradorite", "labradorite"),
    ("Lapis", "lapis"),
    ("Lemon Citrine", "lemon-citrine"),
    ("Malachite", "malachite"),
    ("Moonstone White", "moonstone-white"),
    ("Obsidian Snowflake", "obsidian-snowflake"),
    ("Onyx Black", "onyx-black"),
    ("Onyx Green", "onyx-green"),
    ("Onyx Ivory", "onyx-ivory"),
    ("Onyx Multicolor", "onyx-multicolor"),
    ("Onyx Red", "onyx-red"),
    ("Onyx Red (Pink)", "onyx-red-pink"),
    ("Onyx Rose", "onyx-rose"),
    ("Onyx Yellow", "onyx-yellow"),
    ("Opal Dendrite", "opal-dendrite"),
    ("Pearl Fresh Water", "pearl-fresh-water"),
    ("Pyrite", "pyrite"),
    ("Quartz Cat's Eye", "quartz-cats-eye"),
    ("Rainbow Moonstone", "rainbow-moonstone"),
    ("Rose Quartz", "rose-quartz"),
    ("Ruby Markara", "ruby-markara"),
    ("Rutilated Quartz Black Needle", "rutilated-quartz-black-needle"),
    ("Rutile Quartz Golden Needle", "rutile-quartz-golden-needle"),
    ("Sapphire Blue", "sapphire-blue"),
    ("Sillimanite Cat's Eye", "sillimanite-cats-eye"),
    ("Smoky Quartz", "smoky-quartz"),
    ("Spectrolite Cat's Eye", "spectrolite-cats-eye"),
    ("Sunstone", "sunstone"),
    ("Tiger Eye", "tiger-eye"),
    ("Tourmaline Green", "tourmaline-green"),
    ("Turquoise Chinese", "turquoise-chinese"),
    ("Turquoise Tibetan", "turquoise-tibetan"),
    ("White Quartz", "white-quartz"),
    ("White Quartz Crystal", "white-quartz-crystal"),
    ("White Topaz", "white-topaz"),
    ("Zircon Cubic White", "zircon-cubic-white"),
]

semi_slugs = {s['slug'] for s in semi}
user_targets = {t[1] for t in user_table}

print("In semi_slugs but not in user_targets:", semi_slugs - user_targets)
print("In user_targets but not in semi_slugs:", user_targets - semi_slugs)

