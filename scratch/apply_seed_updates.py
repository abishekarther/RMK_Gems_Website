import sys, os, re, json

sys.path.insert(0, os.path.abspath('.'))

# The updated data for the 11 stones
UPDATED_11 = {
    "agate-red-jasper": {
        "name": "Agate Red Jasper",
        "slug": "agate-red-jasper",
        "short_description": "A microcrystalline quartz stone displaying rich brick-red jasper body with chalcedonic banding.",
        "full_description": "Agate Red Jasper is a microcrystalline quartz variety combining the translucent layered structure of banded agate with opaque red jasper pigmented by iron oxide inclusions.",
        "material_type": "unconfirmed",
        "colour": "Brick-red and terracotta with subtle banding",
        "hardness_min": 6.5,
        "hardness_max": 7.0,
        "chemical_composition": "SiO2 with iron oxide inclusions",
        "crystal_system": "Trigonal",
        "origin": "Found in volcanic rock cavities across India, South Africa, and Brazil.",
        "formation": "Precipitated from low-temperature silica-bearing hydrothermal fluids in rock cavities.",
        "history_notes": "Used ornamentally since antiquity for seals, beads, and decorative carvings.",
        "treatments": "Cut directly from rough stones; polishing enhances surface luster.",
        "care_instructions": "Clean with warm soapy water and a soft brush.",
        "source_notes": "Mindat Jasper: https://www.mindat.org/min-2082.html; Mindat Agate: https://www.mindat.org/min-51.html",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 3,
        "is_published": True,
        "3d_cut": "cabochon",
        "gem_color_hex": "#933A2B",
    },
    "aquamarine-yellow": {
        "name": "Aquamarine Yellow",
        "slug": "aquamarine-yellow",
        "short_description": "A trade designation applied to yellow beryl.",
        "full_description": "Aquamarine Yellow is a commercial trade term for yellow beryl, historically referred to as heliodor. While aquamarine gemologically designates blue beryl, yellow beryl shares the hexagonal beryl crystal structure.",
        "material_type": "unconfirmed",
        "colour": "Yellow to greenish yellow",
        "hardness_min": 7.5,
        "hardness_max": 8.0,
        "chemical_composition": "Be3Al2Si6O18",
        "crystal_system": "Hexagonal",
        "origin": None,
        "formation": None,
        "history_notes": "Yellow beryl was historically named heliodor from Greek words meaning gift of the sun.",
        "treatments": None,
        "care_instructions": "Clean with warm soapy water and a soft brush.",
        "source_notes": "GIA Gem Encyclopedia - Beryl: https://www.gia.edu/aquamarine",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 7,
        "is_published": True,
        "3d_cut": "emerald",
        "gem_color_hex": "#E0C850",
    },
    "garnet-rose-cut-checkerboard": {
        "name": "Garnet Rose Cut / Checkerboard",
        "slug": "garnet-rose-cut-checkerboard",
        "short_description": "Deep red garnet fashioned with geometric checkerboard crown facets or an antique rose cut.",
        "full_description": "Garnet Rose Cut / Checkerboard features deep red garnet fashioned with geometric checkerboard facets or a flat-backed rose cut, reflecting light across multiple triangular surface facets.",
        "material_type": "unconfirmed",
        "colour": "Deep red to wine red",
        "hardness_min": 7.0,
        "hardness_max": 7.5,
        "chemical_composition": "Fe3Al2(SiO4)3 / Mg3Al2(SiO4)3",
        "crystal_system": "Isometric",
        "origin": "Mined in India, Sri Lanka, Madagascar, and Mozambique.",
        "formation": "Metamorphic schists and gneisses formed under elevated pressure and temperature.",
        "history_notes": "Rose cuts originated in the 16th century, while checkerboard crowns gained prominence in modern faceted jewellery.",
        "treatments": "Garnets are generally not treated; cutting technique determines the facet pattern.",
        "care_instructions": "Clean with warm soapy water and a soft cloth.",
        "source_notes": "GIA Gem Encyclopedia - Garnet: https://www.gia.edu/garnet",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 18,
        "is_published": True,
        "3d_cut": "cushion",
        "gem_color_hex": "#731B2A",
    },
    "goldstone-sandstone-blue": {
        "name": "Goldstone Sandstone Blue",
        "slug": "goldstone-sandstone-blue",
        "short_description": "Manufactured blue glass containing glittering metallic crystalline inclusions.",
        "full_description": "Goldstone Sandstone Blue is a manufactured glass produced in a low-oxygen atmosphere with cobalt and metallic flecks, creating a shimmering optical effect.",
        "material_type": "imitation",
        "colour": "Midnight blue with glittering flecks",
        "hardness_min": 5.5,
        "hardness_max": 6.0,
        "chemical_composition": "Silica glass with cobalt and metallic flecks",
        "crystal_system": "Amorphous (manufactured glass)",
        "origin": "Manufactured material originally developed in Murano, Italy.",
        "formation": "Produced by melting silica glass with metallic oxides in a reducing environment.",
        "history_notes": "Origins trace to 17th-century Venetian glassmaking artisans.",
        "treatments": "Manufactured glass material.",
        "care_instructions": "Clean with a soft damp cloth. Avoid sharp impacts and harsh chemicals.",
        "source_notes": "Mindat Aventurine Glass / Goldstone: https://www.mindat.org/min-26588.html",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 19,
        "is_published": True,
        "3d_cut": "cabochon",
        "gem_color_hex": "#1E2D4A",
    },
    "goldstone-sandstone-red": {
        "name": "Goldstone Sandstone Red",
        "slug": "goldstone-sandstone-red",
        "short_description": "Manufactured reddish-brown glass containing sparkling copper flecks.",
        "full_description": "Goldstone Sandstone Red is a manufactured glass containing suspended octahedral copper crystals that produce a golden sparkle.",
        "material_type": "imitation",
        "colour": "Reddish brown with golden copper sparkles",
        "hardness_min": 5.5,
        "hardness_max": 6.0,
        "chemical_composition": "Silica glass with copper crystal flecks",
        "crystal_system": "Amorphous (manufactured glass)",
        "origin": "Manufactured material originally developed in Murano, Italy.",
        "formation": "Produced by melting silica glass with copper oxides in a reducing environment.",
        "history_notes": "Origins trace to 17th-century Venetian glassmaking artisans.",
        "treatments": "Manufactured glass material.",
        "care_instructions": "Clean with a soft damp cloth. Avoid harsh chemicals.",
        "source_notes": "Mindat Aventurine Glass / Goldstone: https://www.mindat.org/min-26588.html",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 20,
        "is_published": True,
        "3d_cut": "cabochon",
        "gem_color_hex": "#8B3A22",
    },
    "hessonite-garnet-semi-precious": {
        "name": "Hessonite Garnet",
        "slug": "hessonite-garnet-semi-precious",
        "short_description": "The grossular garnet variety known for its warm cinnamon-orange to brownish-red hue.",
        "full_description": "Hessonite is a calcium-aluminium variety of the grossular garnet species. Its characteristic amber to cinnamon colour is caused by traces of iron and manganese. Viewed under magnification, hessonite often shows a granular, roiled internal texture.",
        "material_type": "unconfirmed",
        "colour": "Cinnamon orange to brownish red",
        "hardness_min": 7.0,
        "hardness_max": 7.5,
        "chemical_composition": "Ca3Al2(SiO4)3",
        "crystal_system": "Isometric",
        "origin": "Historically sourced from Sri Lanka, India, Madagascar, and Tanzania.",
        "formation": "Contact and regional metamorphic skarn deposits.",
        "history_notes": "Hessonite takes its name from the Greek word hesson, meaning inferior, in reference to its lower density compared to other garnets.",
        "treatments": "Generally not treated; cut directly from garnet crystals.",
        "care_instructions": "Clean with warm soapy water and a soft cloth.",
        "source_notes": "GIA Gem Encyclopedia - Garnet: https://www.gia.edu/garnet",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 23,
        "is_published": True,
        "3d_cut": "cushion",
        "gem_color_hex": "#A84B1A",
    },
    "pearl-fresh-water": {
        "name": "Pearl Fresh Water",
        "slug": "pearl-fresh-water",
        "short_description": "Cultured freshwater pearls formed within river mussels.",
        "full_description": "Pearl Fresh Water denotes pearls cultivated in freshwater unionid mussels. Composed of alternating layers of calcium carbonate (aragonite) and conchiolin, freshwater pearls display a soft, warm nacreous luster and occur in varied pastel shades.",
        "material_type": "organic",
        "colour": "White, cream, pink, and lavender",
        "hardness_min": 2.5,
        "hardness_max": 4.0,
        "chemical_composition": "CaCO3 with organic conchiolin and water",
        "crystal_system": "Orthorhombic (microcrystalline aragonite)",
        "origin": "Cultivated in freshwater lakes and rivers, predominantly in China.",
        "formation": "Formed organically through nacre secretion inside freshwater mussels.",
        "history_notes": "Freshwater pearls have been harvested from rivers across Asia, Europe, and North America for centuries.",
        "treatments": "Mild bleaching and polishing are standard trade practices for cultured pearls.",
        "care_instructions": "Wipe with a soft damp cloth after wearing. Store separately from harder gemstones and avoid exposure to perfumes or acids.",
        "source_notes": "GIA Gem Encyclopedia - Pearl: https://www.gia.edu/pearl",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 39,
        "is_published": True,
        "3d_cut": "cabochon",
        "gem_color_hex": "#F4F2EC",
    },
    "ruby-markara": {
        "name": "Ruby Markara",
        "slug": "ruby-markara",
        "short_description": "A trade name listed in commercial gemstone inventories.",
        "full_description": "Ruby Markara is a commercial trade designation listed for cut red stones. Mineralogical parameters and geological origin are pending laboratory confirmation.",
        "material_type": "unconfirmed",
        "colour": "Red to purplish red",
        "hardness_min": None,
        "hardness_max": None,
        "chemical_composition": None,
        "crystal_system": None,
        "origin": None,
        "formation": None,
        "history_notes": None,
        "treatments": None,
        "care_instructions": "Clean gently with a soft cloth and mild soapy water.",
        "source_notes": "Trade catalog designation; pending gemological laboratory verification.",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 44,
        "is_published": True,
        "3d_cut": "oval",
        "gem_color_hex": "#991B32",
    },
    "rutilated-quartz-black-needle": {
        "name": "Rutilated Quartz Black Needle",
        "slug": "rutilated-quartz-black-needle",
        "short_description": "Transparent rock crystal quartz containing sharp black needle-like mineral inclusions.",
        "full_description": "Rutilated Quartz Black Needle consists of transparent crystalline quartz hosting slender black acicular inclusions. In gemological analysis, these black needles are typically schorl (black tourmaline) or dark titanium-bearing rutile.",
        "material_type": "unconfirmed",
        "colour": "Transparent colourless quartz with black needles",
        "hardness_min": 7.0,
        "hardness_max": 7.0,
        "chemical_composition": "SiO2 with tourmaline or rutile needle inclusions",
        "crystal_system": "Trigonal",
        "origin": "Found in pegmatite deposits in Brazil, Madagascar, and India.",
        "formation": "Crystallized in hydrothermal veins and pegmatite pockets where quartz grows around existing needle crystals.",
        "history_notes": "Acicular inclusions in quartz create distinct graphic patterns valued in ornamental gem carving.",
        "treatments": "Cut directly from crystal rough without artificial enhancement.",
        "care_instructions": "Clean with warm soapy water and a soft brush.",
        "source_notes": "Mindat Tourmalinated Quartz: https://www.mindat.org/min-27083.html",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 45,
        "is_published": True,
        "3d_cut": "cushion",
        "gem_color_hex": "#D8D8D8",
    },
    "sapphire-blue-semi-precious": {
        "name": "Sapphire Blue",
        "slug": "sapphire-blue-semi-precious",
        "short_description": "The blue variety of the corundum mineral species.",
        "full_description": "Sapphire Blue is the blue variety of the corundum species (aluminium oxide), coloured by trace amounts of iron and titanium. Known for its hardness of 9 on the Mohs scale, corundum is second in hardness only to diamond.",
        "material_type": "unconfirmed",
        "colour": "Deep blue to royal blue",
        "hardness_min": 9.0,
        "hardness_max": 9.0,
        "chemical_composition": "Al2O3:Fe,Ti",
        "crystal_system": "Trigonal",
        "origin": "Mined in Sri Lanka, Madagascar, Thailand, and Australia.",
        "formation": "Forms in metamorphic rocks such as marble or gneiss, and in basaltic deposits.",
        "history_notes": "Sapphires have decorated royal regalia and religious adornments across multiple civilizations.",
        "treatments": "Heat treatment is commonly used in the trade to improve colour and clarity.",
        "care_instructions": "Clean with warm soapy water and a soft brush.",
        "source_notes": "GIA Gem Encyclopedia - Sapphire: https://www.gia.edu/sapphire",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 47,
        "is_published": True,
        "3d_cut": "oval",
        "gem_color_hex": "#1E4D8C",
    },
    "zircon-cubic-white": {
        "name": "Zircon Cubic White",
        "slug": "zircon-cubic-white",
        "short_description": "A trade listing describing a colourless faceted stone.",
        "full_description": "Zircon Cubic White is a trade designation. Mineral classification between natural zircon and synthetic cubic zirconia is pending verification.",
        "material_type": "unconfirmed",
        "colour": "Colourless",
        "hardness_min": None,
        "hardness_max": None,
        "chemical_composition": None,
        "crystal_system": None,
        "origin": None,
        "formation": None,
        "history_notes": None,
        "treatments": None,
        "care_instructions": "Clean with warm soapy water and a soft brush.",
        "source_notes": "GIA Gem Encyclopedia and Diamond Simulants: https://www.gia.edu/zircon",
        "needs_client_confirmation": False,
        "availability": "available",
        "is_featured": False,
        "display_order": 59,
        "is_published": True,
        "3d_cut": "brilliant",
        "gem_color_hex": "#F8FAFB",
    }
}

# 1. Update backend/app/seed/seed_data.py
seed_path = 'backend/app/seed/seed_data.py'
with open(seed_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    matched_slug = None
    for s in UPDATED_11:
        if f"'slug': '{s}'" in line or f'"slug": \'{s}\'' in line or f'"slug": "{s}"' in line:
            matched_slug = s
            break
    
    if matched_slug:
        # Find where this dict started (rewind new_lines to `{`)
        while new_lines and '{' not in new_lines[-1]:
            new_lines.pop()
        if new_lines and '{' in new_lines[-1]:
            new_lines.pop() # remove the '{' line
        
        # Advance i until the closing `},`
        while i < len(lines) and not (lines[i].strip() == '},' or lines[i].strip() == '}'):
            i += 1
        # i is now on `},`
        
        # Insert formatted dict
        d = UPDATED_11[matched_slug]
        new_lines.append('        {\n')
        for k, v in d.items():
            if v is None:
                new_lines.append(f'            "{k}": None,\n')
            elif isinstance(v, bool):
                new_lines.append(f'            "{k}": {v},\n')
            elif isinstance(v, (int, float)):
                new_lines.append(f'            "{k}": {v},\n')
            else:
                escaped = v.replace("'", "\\'")
                new_lines.append(f"            \"{k}\": '{escaped}',\n")
        new_lines.append('        },\n')
    else:
        new_lines.append(line)
    i += 1

with open(seed_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Updated backend/app/seed/seed_data.py successfully!")

