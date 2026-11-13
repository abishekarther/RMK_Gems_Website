import os
import json
import shutil
from PIL import Image

MAPPING = {
    # 1-3 Agates
    '2f575c2e-8c44-4763-b329-3700bee3d6a7.webp': 'agate-black-banded',
    'bd537fca-d46d-4de2-b85c-b43011d6352d.webp': 'agate-green-banded',
    'cfbb7fe8-9fa0-4133-b756-325867080010.webp': 'agate-red-jasper',
    
    # 4-6 Amethysts
    'watermarked_img_17757265627695894731.webp': 'amethyst-african',
    'watermarked_img_11311302170131594416.webp': 'amethyst-brazil',
    '42e13544-7511-4597-897d-a501e6eedd0f.webp': 'amethyst-brazil-pink',
    
    # 7 Aquamarine Yellow
    'f14e3f30-4b9c-48b3-9b7c-4c1b371bd971.webp': 'aquamarine-yellow',
    
    # 8 Aventurine Green
    '2f496cbd-e572-40ef-8b5c-ba7857f0423b.webp': 'aventurine-green',
    
    # 9 Bloodstone
    '994cef7e-37ba-48b0-aafb-ad939f323de5.webp': 'bloodstone',
    
    # 10 Blue Lace Banded Agate
    '26109ec9-576c-4453-bd55-8ee761a06fc5.webp': 'blue-lace-banded-agate',
    
    # 11 Carnelian
    '85c9eae6-60e9-4799-aaaf-3ca1480764d3.webp': 'carnelian',
    
    # 12-13 Chalcedony
    '4ad964ca-c610-408a-b622-51310a1d0d8d.webp': 'chalcedony-blue',
    'ec592734-081d-4eb9-935d-eda8625acb6a.webp': 'chalcedony-white',
    
    # 14 Chrysoprase
    '3c287d7d-9370-418e-b9ca-081af27492fc.webp': 'chrysoprase',
    
    # 15 Diopside
    '1227f26f-60c6-413d-a596-c153cec7d004.webp': 'diopside-4-ray-star',
    
    # 16 Fluorite Multicolor Banded
    'e5ace251-7842-4ff4-b96e-78780c56efa4.webp': 'fluorite-multicolor-banded',
    
    # 17-18 Garnet
    '10c566df-d601-43f1-bbb1-99a81398d6f2.webp': 'garnet-almandine',
    '396d963f-728a-4327-91dd-c57715099582.webp': 'garnet-checkerboard',
    
    # 19-20 Goldstone
    '83d1b4f9-0611-4ffa-a4ee-9a2fde43e81f.webp': 'goldstone-sandstone-blue',
    'aecc2ea9-95cb-41c5-b5d3-a3f6f8bf2c70.webp': 'goldstone-sandstone-red',
    
    # 21 Green Serpentine
    'fc0eec37-61d9-48ea-a546-3611f2bd71fd.webp': 'green-serpentine',
    
    # 22 Hematite
    '53fa994e-b2b3-4e4e-afa3-1c378b36b75a.webp': 'hematite-gunmetal',
    
    # 23 Hessonite Garnet
    '32d2c86a-51eb-4543-9d6e-59ea08eec356.webp': 'hessonite-garnet',
    
    # 24 Labradorite
    'f45e2239-b82e-47b3-9964-fda636a4923c.webp': 'labradorite',
    
    # 25 Lapis
    '1d649662-f698-4fcb-86b1-2dcd829f7795.webp': 'lapis',
    
    # 26 Lemon Citrine
    '8f9baeba-f14a-41cb-88f4-16f096d53d75.webp': 'lemon-citrine',
    
    # 27 Malachite
    '6b3e9525-884b-4777-a69e-90ac1a46004e.webp': 'malachite',
    
    # 28 Moonstone White
    '96b379c7-bf67-4ab8-8b7c-4c66571beeea.webp': 'moonstone-white',
    
    # 29 Obsidian Snowflake
    '1fa3e7df-7d69-4e58-b0b6-b56336dd0783.webp': 'obsidian-snowflake',
    
    # 30-37 Onyx series
    '9ad29cc7-f25e-457c-b060-35aef9dd308d.webp': 'onyx-black',
    '490c41c0-c7ed-4ef7-91c9-562903fa2829.webp': 'onyx-green',
    'e809ecb7-184a-4649-89bb-197316de85c1.webp': 'onyx-ivory',
    '1c12882b-6dd3-4dde-9d67-302667a5046a.webp': 'onyx-multicolor',
    'bc98373b-26a6-4bae-baf0-89ef2824c2aa.webp': 'onyx-red',
    '5c2597ef-8cc2-4d0c-830c-ed3589664ce3.webp': 'onyx-red-pink',
    'a2088c19-06e7-4308-b01e-dc691764e9ed.webp': 'onyx-rose',
    '2c3338ea-5a72-4d8f-89d4-8772e95fc271.webp': 'onyx-yellow',
    
    # 38 Opal Dendrite
    '05bff557-0178-46eb-87b8-78e716a60ccf.webp': 'opal-dendrite',
    
    # 39 Pearl Fresh Water
    'ac249b55-b23b-4ca4-996b-6cd63376a21c.webp': 'pearl-fresh-water',
    
    # 40 Pyrite
    'c5d31f36-ea7c-41a9-8064-225aaa3833ac.webp': 'pyrite',
    
    # 41 Quartz Cat's Eye
    '4f1b05db-9317-408a-9414-f47605c1843b.webp': 'quartz-cats-eye',
    
    # 42 Rainbow Moonstone
    '01b1c93a-9a50-4d77-9b2d-e5cb2245f05b.webp': 'rainbow-moonstone',
    
    # 43 Rose Quartz
    'cdc820b8-f7b2-4e0d-ba03-80cf78bb29dd.webp': 'rose-quartz',
    
    # 44 Ruby Markara
    'd67d367c-67a3-41c7-b80f-175cd964705a.webp': 'ruby-markara',
    
    # 45 Rutilated Quartz Black Needle
    '7f35a3eb-3464-4aff-b2f1-f759604016c3.webp': 'rutilated-quartz-black-needle',
    
    # 46 Rutile Quartz Golden Needle
    'be108a0a-87f4-4198-9187-7169337a6d66.webp': 'rutile-quartz-golden-needle',
    
    # 47 Sapphire Blue
    '01fe31cf-93e0-4b7b-8ff8-57289553b691.webp': 'sapphire-blue',
    
    # 48 Sillimanite Cat's Eye
    'ec8770a3-c765-4d6a-af28-40e7e69fdea8.webp': 'sillimanite-cats-eye',
    
    # 49 Smoky Quartz
    '4738ee53-16d3-4d8f-803c-29a9b8482f1d.webp': 'smoky-quartz',
    
    # 50 Spectrolite Cat's Eye
    '13ab1b47-709b-4bd1-a022-b6ff27ead219.webp': 'spectrolite-cats-eye',
    
    # 51 Sunstone
    '7d379a1a-d843-40d4-97a6-c3ff68cf13cd.webp': 'sunstone',
    
    # 52 Tiger Eye
    '92ffff4a-79d5-4375-bed7-e945659f0db0.webp': 'tiger-eye',
    
    # 53 Tourmaline Green
    '66cc2610-4839-47a7-87fe-ea88ee9753d1.webp': 'tourmaline-green',
    
    # 54-55 Turquoise
    '3d7f054b-3856-4f16-90ea-929e799b598a.webp': 'turquoise-chinese',
    'a1e6986d-25a4-40af-8c6c-f4bab42620d9.webp': 'turquoise-tibetan',
    
    # 56-57 Quartz
    'b8147d15-3cfc-44a2-befe-9ced4d815553.webp': 'white-quartz',
    'ec33f068-fb59-4b1f-b074-a01630a3c928.webp': 'white-quartz-crystal',
    
    # 58 White Topaz
    'd5e93ae4-a47a-40f8-87f1-2b0f26b88256.webp': 'white-topaz',
    
    # 59 Zircon Cubic White
    '18b9dd28-aab3-4c4c-b9bc-bd9010043d7e.webp': 'zircon-cubic-white',
}

def main():
    src_dir = r'c:\RMK_Gems_Website\semiprecious_stones_images'
    pub_dir = r'c:\RMK_Gems_Website\frontend\public\images\stones'
    dist_dir = r'c:\RMK_Gems_Website\frontend\dist\images\stones'
    
    os.makedirs(pub_dir, exist_ok=True)
    if os.path.exists(os.path.dirname(dist_dir)):
        os.makedirs(dist_dir, exist_ok=True)
        
    print("Step 1: Processing and deploying images...")
    
    # First, let's create a backup or rename in place in semiprecious_stones_images
    # To rename safely without collision, do two-phase rename or copy
    temp_map = {}
    for src_file, target_slug in MAPPING.items():
        src_path = os.path.join(src_dir, src_file)
        target_name = f"{target_slug}.webp"
        
        # Load and optimize to public dir
        if os.path.exists(src_path):
            img = Image.open(src_path)
            # Save optimized to public/images/stones
            pub_path = os.path.join(pub_dir, target_name)
            img.save(pub_path, 'WEBP', quality=88, method=6)
            
            # Also save to dist if exists
            if os.path.exists(dist_dir):
                dist_path = os.path.join(dist_dir, target_name)
                img.save(dist_path, 'WEBP', quality=88, method=6)
                
            # Handle aliases for seed/codebase compatibility:
            if target_slug == 'garnet-checkerboard':
                shutil.copyfile(pub_path, os.path.join(pub_dir, 'garnet-rose-cut-checkerboard.webp'))
                if os.path.exists(dist_dir):
                    shutil.copyfile(pub_path, os.path.join(dist_dir, 'garnet-rose-cut-checkerboard.webp'))
            elif target_slug == 'hessonite-garnet':
                shutil.copyfile(pub_path, os.path.join(pub_dir, 'hessonite-garnet-semi-precious.webp'))
                if os.path.exists(dist_dir):
                    shutil.copyfile(pub_path, os.path.join(dist_dir, 'hessonite-garnet-semi-precious.webp'))
            elif target_slug == 'sapphire-blue':
                shutil.copyfile(pub_path, os.path.join(pub_dir, 'sapphire-blue-semi-precious.webp'))
                if os.path.exists(dist_dir):
                    shutil.copyfile(pub_path, os.path.join(dist_dir, 'sapphire-blue-semi-precious.webp'))
                    
            print(f"  [OK] Processed {target_slug} ({os.path.getsize(pub_path)} bytes)")
        else:
            print(f"  [ERR] Source not found: {src_path}")

    # Now rename in semiprecious_stones_images folder directly
    print("\nStep 2: Renaming files in semiprecious_stones_images folder...")
    # To prevent overwriting, rename all to temp names first, then to target names
    for src_file, target_slug in MAPPING.items():
        old_path = os.path.join(src_dir, src_file)
        tmp_path = os.path.join(src_dir, f"__tmp__{target_slug}.webp")
        if os.path.exists(old_path):
            os.rename(old_path, tmp_path)
            
    for _, target_slug in MAPPING.items():
        tmp_path = os.path.join(src_dir, f"__tmp__{target_slug}.webp")
        final_path = os.path.join(src_dir, f"{target_slug}.webp")
        if os.path.exists(tmp_path):
            os.rename(tmp_path, final_path)
            
    print(f"  Renamed all 59 files in {src_dir} to target filenames.")

if __name__ == '__main__':
    main()

