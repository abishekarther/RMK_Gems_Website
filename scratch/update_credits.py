import json, os

CREDITS_FILE = 'scratch/all_credits.json'
if os.path.exists(CREDITS_FILE):
    with open(CREDITS_FILE, 'r', encoding='utf-8') as f:
        credits_map = json.load(f)
else:
    credits_map = {}

# 1-13: AI generated stones from batch 1 earlier
ai_stones = {
    'ruby': ('Ruby', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'pearl': ('Pearl', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'red-coral': ('Red Coral', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'emerald': ('Emerald', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'yellow-sapphire': ('Yellow Sapphire', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'diamond': ('Diamond', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'garnet-rose-cut-checkerboard': ('Garnet Rose Cut / Checkerboard', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'goldstone-sandstone-blue': ('Goldstone Sandstone Blue', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'goldstone-sandstone-red': ('Goldstone Sandstone Red', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'aventurine-green': ('Aventurine Green', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'bloodstone': ('Bloodstone', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'blue-lace-banded-agate': ('Blue Lace Banded Agate', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
    'carnelian': ('Carnelian', 'AI generated', 'RMK Gems bespoke AI generation (Gemini Flash Imagen)', 'Google DeepMind / RMK Gems', 'Proprietary / RMK Gems'),
}

for s, (name, typ, src, auth, lic) in ai_stones.items():
    credits_map[s] = {'name': name, 'type': typ, 'source_url': src, 'author': auth, 'license': lic}

# Real internet photos already finalized
internet_stones = {
    'cats-eye-chrysoberyl': ('Cat\'s Eye (Chrysoberyl)', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Chrysoberyl_cat%27s_eye.jpg', 'A.M.', 'CC BY-SA 3.0'),
    'chalcedony-blue': ('Chalcedony BLUE', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Blauer_Chalcedon.jpg', 'Gerd A.T. Müller', 'CC BY-SA 3.0'),
    'amethyst-african': ('Amethyst African', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Am%C3%A9thyste_Br%C3%A9sil_3.jpg', 'Didier Descouens', 'CC BY-SA 4.0'),
    'amethyst-brazil': ('Amethyst Brazil', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Amethyst_(faceted)_(Sebago_Pluton).jpg', 'James St. John', 'CC BY 2.0'),
    'garnet-almandine': ('Garnet Almandine', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Almandin_Madagascar.jpg', 'Didier Descouens', 'CC BY-SA 4.0'),
    'labradorite': ('Labradorite', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Labradorite_cabochon.jpg', 'Mauro Cateb', 'CC BY 2.0'),
    'rutile-quartz-golden-needle': ('Rutile Quartz Golden Needle', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Rutilated_quartz.jpg', 'Mauro Cateb', 'CC BY 2.0'),
    'blue-sapphire': ('Blue Sapphire', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Sapphire_oval,_untreated_2.25cts.jpg', 'Wiener Edelstein Zentrum', 'CC BY-SA 3.0'),
    'chrysoprase': ('Chrysoprase', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:A_selection_of_gem_cabochons_and_nacre_1.jpg', 'W.carter', 'CC BY 4.0'),
    'onyx-black': ('Onyx Black', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Black_Hakeeq.jpg', 'Ikigai azma nasreen', 'CC BY-SA 4.0'),
    'moonstone-white': ('Moonstone White', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Moonstone_gem.jpg', 'Wouter Hagens', 'Public domain'),
    'rainbow-moonstone': ('Rainbow Moonstone', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:White_labradorite_cabochon.jpg', 'Gemsphoto', 'CC BY-SA 3.0'),
    'malachite': ('Malachite', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Malachite_cabochon.jpg', 'Mauro Cateb', 'CC BY-SA 3.0'),
    'tiger-eye': ('Tiger Eye', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Tigers_Eye_Cabochon.jpg', 'Reitawood', 'CC BY-SA 4.0'),
    'opal-dendrite': ('Opal Dendrite', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Dendritic_agate.jpg', 'Estonian Museum of Natural History', 'CC BY-SA 4.0'),
    'hessonite-garnet': ('Hessonite Garnet', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Hessonite._Jesenik,_Czech_Republic-8871.jpg', 'Raimond Spekking', 'CC BY-SA 4.0'),
    'obsidian-snowflake': ('Obsidian Snowflake', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Snowflake_obsidian_1.jpg', 'James St. John', 'CC BY 2.0'),
    'sunstone': ('Sunstone', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Sunstone_(Tertiary;_Spectrum_Mine,_Oregon,_USA)_10.jpg', 'James St. John', 'CC BY 2.0'),
    'rose-quartz': ('Rose Quartz', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Two_rose_quartz_cabocons_1.jpg', 'W.carter', 'CC BY-SA 4.0'),
    'smoky-quartz': ('Smoky Quartz', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Smoky_Quartz_-_Faceted_gem_of_Smoky_Quartz_from_Czech_Republic.jpg', 'AdamStejskal', 'CC BY 4.0'),
    'hematite-gunmetal': ('Hematite (Gunmetal)', 'Internet photo', 'https://commons.wikimedia.org/wiki/File:Hematite_pebbles.jpg', 'Mauro Cateb', 'CC BY-SA 3.0'),
    # Explicit placeholders:
    'aquamarine-yellow': ('Aquamarine Yellow', 'Placeholder', 'N/A', 'RMK Gems', 'Internal Placeholder (Unpublished / Unconfirmed identity)'),
    'ruby-markara': ('Ruby Markara', 'Placeholder', 'N/A', 'RMK Gems', 'Internal Placeholder (Unpublished / Unconfirmed identity)')
}

for s, (name, typ, src, auth, lic) in internet_stones.items():
    credits_map[s] = {'name': name, 'type': typ, 'source_url': src, 'author': auth, 'license': lic}

with open(CREDITS_FILE, 'w', encoding='utf-8') as f:
    json.dump(credits_map, f, indent=2, ensure_ascii=False)

print(f"Updated credits map. Total cataloged stones: {len(credits_map)}")

