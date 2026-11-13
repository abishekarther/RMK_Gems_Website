import sys, os
sys.path.insert(0, os.path.abspath('.'))

from backend.app.core.database import SessionLocal, Base, engine
from backend.app.models.category import GemstoneCategory
from backend.app.models.gemstone import Gemstone
from backend.app.models.media import GemstoneMedia
from backend.app.models.slide import HomepageSlide
from backend.app.models.shop import ShopSettings, OpeningHours
from backend.app.seed.seed_data import get_seed_data

def reseed_database():
    db = SessionLocal()
    try:
        # Delete existing data cleanly
        db.query(GemstoneMedia).delete()
        db.query(Gemstone).delete()
        db.query(HomepageSlide).delete()
        db.query(OpeningHours).delete()
        db.query(ShopSettings).delete()
        db.query(GemstoneCategory).delete()
        db.commit()
        print("Existing database records cleared.")

        categories_data, slides_data, shop_settings_data, opening_hours_data, precious_gems, semi_precious_gems = get_seed_data()

        # Seed categories
        cat_map = {}
        for cdata in categories_data:
            cat = GemstoneCategory(**cdata)
            db.add(cat)
            db.flush()
            cat_map[cat.slug] = cat.id

        # Seed slides
        for sdata in slides_data:
            slide = HomepageSlide(**sdata)
            db.add(slide)

        # Seed shop settings
        shop = ShopSettings(**shop_settings_data)
        db.add(shop)

        # Seed opening hours
        for hdata in opening_hours_data:
            hour = OpeningHours(**hdata)
            db.add(hour)

        # Helper to seed gemstones
        def add_gemstones(gems, cat_slug):
            cat_id = cat_map[cat_slug]
            for g in gems:
                g_copy = dict(g)
                cut_type = g_copy.pop("3d_cut", "brilliant")
                color_hex = g_copy.pop("gem_color_hex", "#C5A880")
                gemstone = Gemstone(category_id=cat_id, **g_copy)
                db.add(gemstone)
                db.flush()

                # Add 3D model media record
                media_3d = GemstoneMedia(
                    gemstone_id=gemstone.id,
                    media_type="model_3d",
                    file_url=f"/models/{cut_type}.glb",
                    thumbnail_url=f"/images/gems/{gemstone.slug}.webp",
                    alt_text=f"Realistic 3D model of {gemstone.name}",
                    display_order=1,
                    is_primary=True,
                )
                db.add(media_3d)

        add_gemstones(precious_gems, "precious")
        add_gemstones(semi_precious_gems, "semi-precious")

        db.commit()
        print("Database successfully reseeded with all 68 gemstones (9 precious + 59 semi-precious)!")

    except Exception as e:
        db.rollback()
        print(f"Error reseeding database: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    reseed_database()
