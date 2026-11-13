import os
import sys

sys.path.insert(0, os.path.abspath('.'))
from backend.app.core.database import SessionLocal
from backend.app.models.gemstone import Gemstone
from backend.app.models.category import GemstoneCategory

db = SessionLocal()
semi_cat = db.query(GemstoneCategory).filter(GemstoneCategory.slug == 'semi-precious').first()
prec_cat = db.query(GemstoneCategory).filter(GemstoneCategory.slug == 'precious').first()

if semi_cat:
    total_semi = db.query(Gemstone).filter(Gemstone.category_id == semi_cat.id).count()
    pub_semi = db.query(Gemstone).filter(Gemstone.category_id == semi_cat.id, Gemstone.is_published == True).count()
    unpub_semi = db.query(Gemstone).filter(Gemstone.category_id == semi_cat.id, Gemstone.is_published == False).all()
    print(f"Database semi-precious total: {total_semi}, published: {pub_semi}")
    print("Unpublished in DB:")
    for g in unpub_semi:
        print(f"  - {g.slug} ({g.name}): is_published={g.is_published}, needs_confirm={g.needs_client_confirmation}")

if prec_cat:
    total_prec = db.query(Gemstone).filter(Gemstone.category_id == prec_cat.id).count()
    pub_prec = db.query(Gemstone).filter(Gemstone.category_id == prec_cat.id, Gemstone.is_published == True).count()
    print(f"Database precious total: {total_prec}, published: {pub_prec}")

db.close()

