import sys, os

sys.path.insert(0, os.path.abspath('.'))
from backend.app.core.database import SessionLocal
from backend.app.models.gemstone import Gemstone
from backend.app.models.category import GemstoneCategory
from backend.app.seed.seed_data import get_seed_data

print("=== CHECK 1: EXACTLY 9 PRECIOUS & 59 SEMI-PRECIOUS PUBLISHED STONES ===")

# 1. Check in Seed Data
cats, slides, shop, hours, prec, semi = get_seed_data()
pub_prec_seed = [s for s in prec if s.get('is_published') is True]
pub_semi_seed = [s for s in semi if s.get('is_published') is True]

print(f"Seed Data - Precious published: {len(pub_prec_seed)} / {len(prec)}")
print(f"Seed Data - Semi-precious published: {len(pub_semi_seed)} / {len(semi)}")

# 2. Check in Live Database
db = SessionLocal()
try:
    cat_prec = db.query(GemstoneCategory).filter(GemstoneCategory.slug == 'precious').first()
    cat_semi = db.query(GemstoneCategory).filter(GemstoneCategory.slug == 'semi-precious').first()
    
    db_pub_prec = db.query(Gemstone).filter(Gemstone.category_id == cat_prec.id, Gemstone.is_published == True).all()
    db_pub_semi = db.query(Gemstone).filter(Gemstone.category_id == cat_semi.id, Gemstone.is_published == True).all()
    
    print(f"Database - Precious published: {len(db_pub_prec)}")
    print(f"Database - Semi-precious published: {len(db_pub_semi)}")
    
    errors = []
    if len(pub_prec_seed) != 9:
        errors.append(f"Seed precious published count is {len(pub_prec_seed)}, expected 9")
    if len(pub_semi_seed) != 59:
        errors.append(f"Seed semi-precious published count is {len(pub_semi_seed)}, expected 59")
    if len(db_pub_prec) != 9:
        errors.append(f"Database precious published count is {len(db_pub_prec)}, expected 9")
    if len(db_pub_semi) != 59:
        errors.append(f"Database semi-precious published count is {len(db_pub_semi)}, expected 59")
        
    if errors:
        print("FAILED: Count checks failed:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("SUCCESS: Exactly 9 precious and 59 semi-precious gemstones are published (68 total) in both seed data and database!")
finally:
    db.close()

